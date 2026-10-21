# Director coordination — Part 5 of 9

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

[← Part 4](part-004.md) · [Transcript overview](../director-coordination.md) · [Part 6 →](part-006.md) · [Structured JSON](../../../sessions/bd/bdd0e6c8e8a0a8a81e76.json)

## Round 93

### Tool call

_source line 1422 · 2026-05-22T07:58:39.202844+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "symb_invariant_consensus",
  "issues_yaml": "# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)\n- id: \"R1-C1\"\n  summary: \"Method Stage 3 sat() implementation undescribed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit.\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Most experiments underpowered (n≤60), no power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Power analysis + Bootstrap CIs added. Larger n conditions (200-600).\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Oracle/upper-bound experiment missing\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp.\"\n  resolution_round: 3\n\n- id: \"R1-C4\"\n  summary: \"Huang et al. (ICLR 2024) not cited\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Huang, Stechly, Kambhampati all cited and discussed.\"\n  resolution_round: 2\n\n- id: \"R1-C5\"\n  summary: \"Critical related work missing\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"~48 citations, 5 Related Work paragraphs.\"\n  resolution_round: 3\n\n- id: \"R1-C9\"\n  summary: \"Capability trap novelty unclear\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Reframed as regime-dependent analysis with CJT framework.\"\n  resolution_round: 3\n\n- id: \"R3-N1\"\n  summary: \"σ(c,a) scoring inconsistent between self-extraction and oracle\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Paper Agent added clarifying sentence in method.tex.\"\n  resolution_round: 4\n\n- id: \"R3-N2\"\n  summary: \"α value never specified\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"α=0.5 explicit in Eq.(3) and §4.1.\"\n  resolution_round: 3\n\n# Round 9-12 in_progress issues — updated with Round 10 (fresh) mentions\n\n- id: \"R9-W2\"\n  summary: \"NLI combo weight parameter w 未交叉验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 13\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"w=3 primary 但未系统分析 w 选择\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 未单独提及 w 参数，但 DRC 评估不充分的批评间接涵盖\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未单独提及，但 DRC 贡献不足的共识间接涵盖\"\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 未单独提及 w 参数\"\n\n- id: \"R9-W3\"\n  summary: \"Capability Gap Hypothesis 基于极小样本 (n=6)\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 13\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"n=6 permutation test\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 升级为 critical: 4/6 共享 DeBERTa verifier, 有效自由度远低于6\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 再次确认 critical 共识: verifier-collapsed p=0.167 不显著\"\n    - round: 13\n      reviewers: [1]\n      note: \"R13(fresh) R1-W1 触及: capability gap claim scope 超出证据. 论文当前标注 p=0.003 (n=6), Limitations 标注 p=0.167\"\n\n- id: \"R9-VL1\"\n  summary: \"Pages 1-2 连续纯文本无 display item\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 13\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"视觉审查发现\"\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 视觉审查确认: pages 3-5 约2.5页无figure/table\"\n\n- id: \"R9-VL4\"\n  summary: \"Page 8 Conclusion 仓促\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 13\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"Conclusion 在 page 8 下半部\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13(fresh) R2-W2/R1共识: Discussion 仅半页, 缺 test-time scaling 含义和可操作建议\"\n\n- id: \"R10-N1\"\n  summary: \"Proposition 1 (Self-Extraction Ceiling) 无证明——empirical claim dressed as theorem\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 13\n  resolution: \"当前论文使用 'Empirical Finding 1/2'(page 5 tcolorbox), 不再使用 Proposition 术语\"\n  resolution_round: 13\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Bound 1 无推导, ≲ 未定义\"\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 未提及——已改为 Empirical Finding, 问题已解决\"\n\n- id: \"R10-N2\"\n  summary: \"κ→K_eff 映射理论基础不足——r=0.625 验证弱\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fleiss' κ 代入 Kish design effect 公式理论上不严格\"\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 未单独提及. 论文当前有 ordinal diagnostic caveat(§3.1 page 4)\"\n\n- id: \"R10-N3\"\n  summary: \"Capability gap 'perfectly monotonic' 结论基于 n=6 非独立数据点\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"n=6 permutation test, shared verifier\"\n    - round: 13\n      reviewers: [1]\n      note: \"R13(fresh) R1-W1: claim 仅在命题逻辑任务验证; Limitations 已标注 p=0.167\"\n\n- id: \"R10-W1\"\n  summary: \"DRC τ 阈值无 held-out 评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 未单独提及 DRC\"\n\n- id: \"R10-W2\"\n  summary: \"Cross-architecture NLI escape 适用面极窄\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"仅 Mistral-7B 显著\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13(fresh) R2-N1: '仅一个验证器'——R1 REBUT 指出实际3个(DeBERTa/RoBERTa/BART). R1-W1: 仅命题逻辑任务. 共识: 证据比 R2 初判更充分, 但 domain-specificity 仍为问题\"\n\n- id: \"R10-W3\"\n  summary: \"四种子复制方差大 + 统计功效 <21%\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13(fresh) R1-N2/R2-N2 核心共识: 10/16 underpowered, sign test inconclusive(8/15 p=0.21), power analysis 埋在附录. R1-W5: seed间variance未充分报告\"\n\n- id: \"R10-W4\"\n  summary: \"TOST ±2pp margin 缺少显式理由\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13(fresh) R1-W4/R2共识: 用SC效应量定义margin有循环性; ±3pp时全部equivalent说明对margin敏感\"\n\n- id: \"R10-W5\"\n  summary: \"Bias Ratio 无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"BR CI 已整合: Mistral [3.98,6.37], Qwen [2.44,7.11]\"\n  resolution_round: 10\n\n- id: \"R10-W6\"\n  summary: \"SatLM specification-generation vs SICA trace-extraction 对比不充分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 未单独提及. Related Work §2 有 SatLM 讨论\"\n\n- id: \"R10-W7\"\n  summary: \"'Symbolic Confirmation Bias' 需与近期 CoT confirmation bias 工作区分\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"R13(fresh) R2-W2: Discussion 缺 SCB vs CoT unfaithfulness 关系讨论. Related Work §2 已引 Turpin/Wan/Jhaveri 但区分可更清晰\"\n\n- id: \"R10-W8\"\n  summary: \"Related Work 过度压缩——引用列表而非文献讨论\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) R2-S4 反而将 Related Work 覆盖面列为优势. 可能已改善\"\n\n- id: \"R10-W9\"\n  summary: \"27 种修复策略在正文中展示不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"R13(fresh) R1小问题#2: Figure 2 信息密度高但可读性一般, 建议 highlight 3-5 种代表性策略\"\n\n- id: \"R10-I1\"\n  summary: \"相对于 Huang/Stechly 的增量新颖性不足\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13(fresh) R2 Excitement 2.5/5, 核心理由: SCB被先验工作预示. R1 Excitement 3/5, 认为量化贡献有价值. 分歧记录\"\n\n- id: \"R10-I2\"\n  summary: \"Independence-Accuracy Trade-off 作为独立贡献有 bias-variance 重述嫌疑\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 未单独提及此角度\"\n\n- id: \"R10-VL1\"\n  summary: \"主文缺结果可视化\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 视觉审查: pages 3-5 约2.5页低视觉密度. 但当前主文已有 Figure 1(p2) + Table 1(p6) + Table 2(p7) + Figure 2(p7) + Table 3(p8)\"\n\n- id: \"R11-N1\"\n  summary: \"Spearman ρ=1.0 (n=6) 被过度使用——有效自由度远低于6\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"R13(fresh) R1-W1: capability gap claim 超出证据范围. 论文已有 Limitations 标注 p=0.167\"\n\n- id: \"R11-N2\"\n  summary: \"中心 claim 'SICA fails' 与统计功效不匹配——Abstract/title 过强\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13(fresh) R1-N2/R2-N2 核心共识. 当前标题 'Show No Evidence' 比 R12 的 'Do Not Improve' 更审慎, 但 R2 仍认为超出证据. R1 认为标题可保留但正文需加 power statement\"\n\n- id: \"R11-N3\"\n  summary: \"TOST ±2pp margin 缺乏 principled 论证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13(fresh) R1-W4/R2共识: margin 选择有循环性\"\n\n- id: \"R11-W1\"\n  summary: \"DRC 评估不充分——仅PW完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 未单独评估 DRC\"\n\n- id: \"R11-W2\"\n  summary: \"BR 指标存在循环论证倾向\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"R13(fresh) R1-N1: BR 4.97× 选择性报告. R1-W2: 语法去重可能膨胀 BR. R2交叉回应同意需报告语义去重后 BR\"\n\n- id: \"R11-W3\"\n  summary: \"术语过度品牌化——'Independence Bottleneck' 和 'Symbolic Mirage' 偏 dramatic\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"R13(fresh) R2-M6: 'Symbolic Mirage' 可能不如 'Symbolic Echo'. R1交叉回应同意但 minor\"\n\n- id: \"R11-W4\"\n  summary: \"新颖性定位需更早更明确建立与先验工作的 distinction\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"R13(fresh) R2 Excitement 2.5/5: SCB 被 Huang(2024)/Stechly(2025) 预示. R1 认为量化贡献非概念预示\"\n\n- id: \"R11-W5\"\n  summary: \"Independence-Accuracy Trade-off 应定位为量化而非新发现\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 未单独提及\"\n\n- id: \"R11-W6\"\n  summary: \"遗漏引用: Byerly & Khashabi (2026 TACL) 等\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"当前论文 Related Work §2 已引用 Byerly and Khashabi (2026)\"\n  resolution_round: 13\n\n- id: \"R11-W7\"\n  summary: \"27 策略计数膨胀 + 未尝试 trained constraint extractor\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 未直接提及计数膨胀. Limitations 已声明不评估 trained extractors\"\n\n- id: \"R11-VL1\"\n  summary: \"主文缺结果可视化——需上提 Figure 到主文\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"R13(fresh) R1小问题#2: Figure 2 已在正文(p7)但可读性一般\"\n\n- id: \"R12-N1\"\n  summary: \"标题 overclaiming about frontier scale\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12: 标题中 'Self-Extracted' 但 frontier 用 cross-model extraction\"\n    - round: 13\n      reviewers: [1]\n      note: \"R13(fresh) R1-N1: 摘要 BR 4.97× 来自最极端条件, frontier BR≈1. 标题改为 'Show No Evidence' 更审慎, 但摘要仍选择性报告\"\n\n- id: \"R12-N2\"\n  summary: \"SCB 核心新颖性不足——self-correction failure 在 FOL 载体上的实例化\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13(fresh) R2 Excitement 2.5: 被 Huang(2024) 预示. R1 Excitement 3: 量化深度有独立价值. 分歧记录但方向一致\"\n\n- id: \"R12-N3\"\n  summary: \"DRC 作为 Contribution 4 不够充分\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 当前论文未将 DRC 列为独立 Contribution(page 2 仅列3个贡献). DRC 在 §6 作为 practical observation 出现. 可能已修复\"\n\n- id: \"R12-W1\"\n  summary: \"BR 可能存在循环论证——56.4%零变量重叠使约束按定义支持source answer\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13(fresh) R1-W2: 语法去重可能膨胀BR. 论文有 shuffle control(§5.2)部分回应了此问题(BR_shuffle≈BR_real), 但未报告语义去重后 BR\"\n\n- id: \"R12-W2\"\n  summary: \"CIL 名称和 information-theoretic 声称有误导\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 当前论文使用 'Conditional Correction Ratio (CCR)'(§5.4 Eq.7) 而非 CIL. 名称更准确. 但 R1-S3 仍列 CCR 为独立贡献\"\n\n- id: \"R12-W3\"\n  summary: \"Figure 2 placement——应在正文而非附录\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"当前论文 Figure 2 已在正文 page 7(§5.5 Remediation Analysis 旁)\"\n  resolution_round: 13\n\n- id: \"R12-W4\"\n  summary: \"Appendix vs 主文关键信息分配不合理\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13(fresh) R2-W1: 符号过载(7指标挤8页). R2-W2: Discussion 过短. R1-N2: power analysis 埋在附录. 核心信息分配仍有改善空间\"\n\n- id: \"R12-EC1\"\n  summary: \"Extractor Confound——所有 frontier cross-model extraction 使用同一 Mistral-7B extractor\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"R13(fresh) R1-N1: frontier BR≈1 可能反映 extractor 能力而非 SCB 减弱. R2交叉回应Q1: BR与模型能力负相关, 但 extractor confound 未解耦\"\n\n# R13(fresh) 新 issues\n\n- id: \"R13-N1\"\n  summary: \"摘要 BR 4.97× 选择性报告——最极端条件, frontier BR≈1\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1首提, R2完全同意. Table 2 BR范围1.05-4.97, 中位数≈2.8. 摘要应报告范围或中位数\"\n  action_items:\n    - round: 13\n      action: \"摘要改为报告 BR 范围或中位数; 正文增加按模型能力分层的 BR 分析\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R13-N2\"\n  summary: \"统计功效呈现不足——10/16 underpowered, power analysis 埋在附录\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N2/R2-N2 完全共识. 10/16 conditions MDE>2pp at 80% power. Sign test 8/15 positive (p=0.21) inconclusive not negative. §4.2 需增加 power statement. Appendix E Table 6 核心数字应提到正文\"\n  action_items:\n    - round: 13\n      action: \"§4.2 增加明确 power statement; 将 MDE 核心数字从 Appendix E 提到正文\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R13-N3\"\n  summary: \"α=0.5 无敏感性分析——94.4% MAX-SAT退化可能依赖于特定α\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1首提(critical), R2 agree with nuance(影响可能有限因SCB方向一致). 共识: 需在2-3代表性条件上跑α∈{0.1,0.3,0.7}消融\"\n  action_items:\n    - round: 13\n      action: \"在 Mistral-7B/FOLIO + Qwen2.5-14B 上跑 α 消融, 报告 MAX-SAT≡count-only 比率变化\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R13-W1\"\n  summary: \"符号/指标过载——8页内7个定量工具, 认知负担过重\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2首提, R1同意并细化优先级. 建议: ProcessSim/CCR 可移至附录, 正文聚焦 K_eff/BR/C₀\"\n\n- id: \"R13-W2\"\n  summary: \"NLI claim 须限定到命题逻辑任务——domain alignment confound\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W1首提, R2-N1部分涉及(但R1 REBUT了R2的事实错误). 共识: 摘要限定为 'on propositional-logic benchmarks'; §6或Limitations讨论 domain limitation\"\n\n- id: \"R13-W3\"\n  summary: \"语法去重可能膨胀 BR——未报告语义去重后 BR\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W2首提, R2交叉同意. Z3内部处理逻辑等价但BR作为诊断指标可能被语法冗余膨胀. 建议报告语义去重后BR\"\n\n- id: \"R13-W4\"\n  summary: \"Symbolic Mirage Hypothesis §3.3 与 §5 验证状态不连贯\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W3首提, R1同意但低严重性. §5开头有 'We test the three predictions' 但后续小节未回溯具体prediction编号\"\n\n- id: \"R13-W5\"\n  summary: \"缺引: Dhuliawala et al. 2023 Chain-of-Verification\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-M1首提, R1交叉同意. 与自验证局限高度相关\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "issues_yaml": "# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)\n- id: \"R1-C1\"\n  summary: \"Method Stage 3 sat() implementation undescribed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit.\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Most experiments underpowered (n≤60), no power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Power analysis + Bootstrap CIs added. Larger n conditions (200-600).\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Oracle/upper-bound experiment missing\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp.\"\n  resolution_round: 3\n\n- id: \"R1-C4\"\n  summary: \"Huang et al. (ICLR 2024) not cited\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Huang, Stechly, Kambhampati all cited and discussed.\"\n  resolution_round: 2\n\n- id: \"R1-C5\"\n  summary: \"Critical related work missing\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"~48 citations, 5 Related Work paragraphs.\"\n  resolution_round: 3\n\n- id: \"R1-C9\"\n  summary: \"Capability trap novelty unclear\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Reframed as regime-dependent analysis with CJT framework.\"\n  resolution_round: 3\n\n- id: \"R3-N1\"\n  summary: \"σ(c,a) scoring inconsistent between self-extraction and oracle\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Paper Agent added clarifying sentence in method.tex.\"\n  resolution_round: 4\n\n- id: \"R3-N2\"\n  summary: \"α value never specified\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"α=0.5 explicit in Eq.(3) and §4.1.\"\n  resolution_round: 3\n\n# Round 9-12 in_progress issues — updated with Round 10 (fresh) mentions\n\n- id: \"R9-W2\"\n  summary: \"NLI combo weight parameter w 未交叉验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 13\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"w=3 primary 但未系统分析 w 选择\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 未单独提及 w 参数，但 DRC 评估不充分的批评间接涵盖\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未单独提及，但 DRC 贡献不足的共识间接涵盖\"\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 未单独提及 w 参数\"\n\n- id: \"R9-W3\"\n  summary: \"Capability Gap Hypothesis 基于极小样本 (n=6)\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 13\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"n=6 permutation test\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 升级为 critical: 4/6 共享 DeBERTa verifier, 有效自由度远低于6\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 再次确认 critical 共识: verifier-collapsed p=0.167 不显著\"\n    - round: 13\n      reviewers: [1]\n      note: \"R13(fresh) R1-W1 触及: capability gap claim scope 超出证据. 论文当前标注 p=0.003 (n=6), Limitations 标注 p=0.167\"\n\n- id: \"R9-VL1\"\n  summary: \"Pages 1-2 连续纯文本无 display item\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 13\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"视觉审查发现\"\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 视觉审查确认: pages 3-5 约2.5页无figure/table\"\n\n- id: \"R9-VL4\"\n  summary: \"Page 8 Conclusion 仓促\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 13\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"Conclusion 在 page 8 下半部\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13(fresh) R2-W2/R1共识: Discussion 仅半页, 缺 test-time scaling 含义和可操作建议\"\n\n- id: \"R10-N1\"\n  summary: \"Proposition 1 (Self-Extraction Ceiling) 无证明——empirical claim dressed as theorem\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 13\n  resolution: \"当前论文使用 'Empirical Finding 1/2'(page 5 tcolorbox), 不再使用 Proposition 术语\"\n  resolution_round: 13\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Bound 1 无推导, ≲ 未定义\"\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 未提及——已改为 Empirical Finding, 问题已解决\"\n\n- id: \"R10-N2\"\n  summary: \"κ→K_eff 映射理论基础不足——r=0.625 验证弱\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fleiss' κ 代入 Kish design effect 公式理论上不严格\"\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 未单独提及. 论文当前有 ordinal diagnostic caveat(§3.1 page 4)\"\n\n- id: \"R10-N3\"\n  summary: \"Capability gap 'perfectly monotonic' 结论基于 n=6 非独立数据点\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"n=6 permutation test, shared verifier\"\n    - round: 13\n      reviewers: [1]\n      note: \"R13(fresh) R1-W1: claim 仅在命题逻辑任务验证; Limitations 已标注 p=0.167\"\n\n- id: \"R10-W1\"\n  summary: \"DRC τ 阈值无 held-out 评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 未单独提及 DRC\"\n\n- id: \"R10-W2\"\n  summary: \"Cross-architecture NLI escape 适用面极窄\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"仅 Mistral-7B 显著\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13(fresh) R2-N1: '仅一个验证器'——R1 REBUT 指出实际3个(DeBERTa/RoBERTa/BART). R1-W1: 仅命题逻辑任务. 共识: 证据比 R2 初判更充分, 但 domain-specificity 仍为问题\"\n\n- id: \"R10-W3\"\n  summary: \"四种子复制方差大 + 统计功效 <21%\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13(fresh) R1-N2/R2-N2 核心共识: 10/16 underpowered, sign test inconclusive(8/15 p=0.21), power analysis 埋在附录. R1-W5: seed间variance未充分报告\"\n\n- id: \"R10-W4\"\n  summary: \"TOST ±2pp margin 缺少显式理由\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13(fresh) R1-W4/R2共识: 用SC效应量定义margin有循环性; ±3pp时全部equivalent说明对margin敏感\"\n\n- id: \"R10-W5\"\n  summary: \"Bias Ratio 无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"BR CI 已整合: Mistral [3.98,6.37], Qwen [2.44,7.11]\"\n  resolution_round: 10\n\n- id: \"R10-W6\"\n  summary: \"SatLM specification-generation vs SICA trace-extraction 对比不充分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 未单独提及. Related Work §2 有 SatLM 讨论\"\n\n- id: \"R10-W7\"\n  summary: \"'Symbolic Confirmation Bias' 需与近期 CoT confirmation bias 工作区分\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"R13(fresh) R2-W2: Discussion 缺 SCB vs CoT unfaithfulness 关系讨论. Related Work §2 已引 Turpin/Wan/Jhaveri 但区分可更清晰\"\n\n- id: \"R10-W8\"\n  summary: \"Related Work 过度压缩——引用列表而非文献讨论\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) R2-S4 反而将 Related Work 覆盖面列为优势. 可能已改善\"\n\n- id: \"R10-W9\"\n  summary: \"27 种修复策略在正文中展示不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"R13(fresh) R1小问题#2: Figure 2 信息密度高但可读性一般, 建议 highlight 3-5 种代表性策略\"\n\n- id: \"R10-I1\"\n  summary: \"相对于 Huang/Stechly 的增量新颖性不足\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13(fresh) R2 Excitement 2.5/5, 核心理由: SCB被先验工作预示. R1 Excitement 3/5, 认为量化贡献有价值. 分歧记录\"\n\n- id: \"R10-I2\"\n  summary: \"Independence-Accuracy Trade-off 作为独立贡献有 bias-variance 重述嫌疑\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 未单独提及此角度\"\n\n- id: \"R10-VL1\"\n  summary: \"主文缺结果可视化\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 视觉审查: pages 3-5 约2.5页低视觉密度. 但当前主文已有 Figure 1(p2) + Table 1(p6) + Table 2(p7) + Figure 2(p7) + Table 3(p8)\"\n\n- id: \"R11-N1\"\n  summary: \"Spearman ρ=1.0 (n=6) 被过度使用——有效自由度远低于6\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"R13(fresh) R1-W1: capability gap claim 超出证据范围. 论文已有 Limitations 标注 p=0.167\"\n\n- id: \"R11-N2\"\n  summary: \"中心 claim 'SICA fails' 与统计功效不匹配——Abstract/title 过强\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13(fresh) R1-N2/R2-N2 核心共识. 当前标题 'Show No Evidence' 比 R12 的 'Do Not Improve' 更审慎, 但 R2 仍认为超出证据. R1 认为标题可保留但正文需加 power statement\"\n\n- id: \"R11-N3\"\n  summary: \"TOST ±2pp margin 缺乏 principled 论证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13(fresh) R1-W4/R2共识: margin 选择有循环性\"\n\n- id: \"R11-W1\"\n  summary: \"DRC 评估不充分——仅PW完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 未单独评估 DRC\"\n\n- id: \"R11-W2\"\n  summary: \"BR 指标存在循环论证倾向\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"R13(fresh) R1-N1: BR 4.97× 选择性报告. R1-W2: 语法去重可能膨胀 BR. R2交叉回应同意需报告语义去重后 BR\"\n\n- id: \"R11-W3\"\n  summary: \"术语过度品牌化——'Independence Bottleneck' 和 'Symbolic Mirage' 偏 dramatic\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"R13(fresh) R2-M6: 'Symbolic Mirage' 可能不如 'Symbolic Echo'. R1交叉回应同意但 minor\"\n\n- id: \"R11-W4\"\n  summary: \"新颖性定位需更早更明确建立与先验工作的 distinction\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"R13(fresh) R2 Excitement 2.5/5: SCB 被 Huang(2024)/Stechly(2025) 预示. R1 认为量化贡献非概念预示\"\n\n- id: \"R11-W5\"\n  summary: \"Independence-Accuracy Trade-off 应定位为量化而非新发现\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 未单独提及\"\n\n- id: \"R11-W6\"\n  summary: \"遗漏引用: Byerly & Khashabi (2026 TACL) 等\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"当前论文 Related Work §2 已引用 Byerly and Khashabi (2026)\"\n  resolution_round: 13\n\n- id: \"R11-W7\"\n  summary: \"27 策略计数膨胀 + 未尝试 trained constraint extractor\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 未直接提及计数膨胀. Limitations 已声明不评估 trained extractors\"\n\n- id: \"R11-VL1\"\n  summary: \"主文缺结果可视化——需上提 Figure 到主文\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"R13(fresh) R1小问题#2: Figure 2 已在正文(p7)但可读性一般\"\n\n- id: \"R12-N1\"\n  summary: \"标题 overclaiming about frontier scale\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12: 标题中 'Self-Extracted' 但 frontier 用 cross-model extraction\"\n    - round: 13\n      reviewers: [1]\n      note: \"R13(fresh) R1-N1: 摘要 BR 4.97× 来自最极端条件, frontier BR≈1. 标题改为 'Show No Evidence' 更审慎, 但摘要仍选择性报告\"\n\n- id: \"R12-N2\"\n  summary: \"SCB 核心新颖性不足——self-correction failure 在 FOL 载体上的实例化\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13(fresh) R2 Excitement 2.5: 被 Huang(2024) 预示. R1 Excitement 3: 量化深度有独立价值. 分歧记录但方向一致\"\n\n- id: \"R12-N3\"\n  summary: \"DRC 作为 Contribution 4 不够充分\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 当前论文未将 DRC 列为独立 Contribution(page 2 仅列3个贡献). DRC 在 §6 作为 practical observation 出现. 可能已修复\"\n\n- id: \"R12-W1\"\n  summary: \"BR 可能存在循环论证——56.4%零变量重叠使约束按定义支持source answer\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13(fresh) R1-W2: 语法去重可能膨胀BR. 论文有 shuffle control(§5.2)部分回应了此问题(BR_shuffle≈BR_real), 但未报告语义去重后 BR\"\n\n- id: \"R12-W2\"\n  summary: \"CIL 名称和 information-theoretic 声称有误导\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 当前论文使用 'Conditional Correction Ratio (CCR)'(§5.4 Eq.7) 而非 CIL. 名称更准确. 但 R1-S3 仍列 CCR 为独立贡献\"\n\n- id: \"R12-W3\"\n  summary: \"Figure 2 placement——应在正文而非附录\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"当前论文 Figure 2 已在正文 page 7(§5.5 Remediation Analysis 旁)\"\n  resolution_round: 13\n\n- id: \"R12-W4\"\n  summary: \"Appendix vs 主文关键信息分配不合理\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13(fresh) R2-W1: 符号过载(7指标挤8页). R2-W2: Discussion 过短. R1-N2: power analysis 埋在附录. 核心信息分配仍有改善空间\"\n\n- id: \"R12-EC1\"\n  summary: \"Extractor Confound——所有 frontier cross-model extraction 使用同一 Mistral-7B extractor\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"R13(fresh) R1-N1: frontier BR≈1 可能反映 extractor 能力而非 SCB 减弱. R2交叉回应Q1: BR与模型能力负相关, 但 extractor confound 未解耦\"\n\n# R13(fresh) 新 issues\n\n- id: \"R13-N1\"\n  summary: \"摘要 BR 4.97× 选择性报告——最极端条件, frontier BR≈1\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1首提, R2完全同意. Table 2 BR范围1.05-4.97, 中位数≈2.8. 摘要应报告范围或中位数\"\n  action_items:\n    - round: 13\n      action: \"摘要改为报告 BR 范围或中位数; 正文增加按模型能力分层的 BR 分析\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R13-N2\"\n  summary: \"统计功效呈现不足——10/16 underpowered, power analysis 埋在附录\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N2/R2-N2 完全共识. 10/16 conditions MDE>2pp at 80% power. Sign test 8/15 positive (p=0.21) inconclusive not negative. §4.2 需增加 power statement. Appendix E Table 6 核心数字应提到正文\"\n  action_items:\n    - round: 13\n      action: \"§4.2 增加明确 power statement; 将 MDE 核心数字从 Appendix E 提到正文\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R13-N3\"\n  summary: \"α=0.5 无敏感性分析——94.4% MAX-SAT退化可能依赖于特定α\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1首提(critical), R2 agree with nuance(影响可能有限因SCB方向一致). 共识: 需在2-3代表性条件上跑α∈{0.1,0.3,0.7}消融\"\n  action_items:\n    - round: 13\n      action: \"在 Mistral-7B/FOLIO + Qwen2.5-14B 上跑 α 消融, 报告 MAX-SAT≡count-only 比率变化\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R13-W1\"\n  summary: \"符号/指标过载——8页内7个定量工具, 认知负担过重\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2首提, R1同意并细化优先级. 建议: ProcessSim/CCR 可移至附录, 正文聚焦 K_eff/BR/C₀\"\n\n- id: \"R13-W2\"\n  summary: \"NLI claim 须限定到命题逻辑任务——domain alignment confound\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W1首提, R2-N1部分涉及(但R1 REBUT了R2的事实错误). 共识: 摘要限定为 'on propositional-logic benchmarks'; §6或Limitations讨论 domain limitation\"\n\n- id: \"R13-W3\"\n  summary: \"语法去重可能膨胀 BR——未报告语义去重后 BR\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W2首提, R2交叉同意. Z3内部处理逻辑等价但BR作为诊断指标可能被语法冗余膨胀. 建议报告语义去重后BR\"\n\n- id: \"R13-W4\"\n  summary: \"Symbolic Mirage Hypothesis §3.3 与 §5 验证状态不连贯\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W3首提, R1同意但低严重性. §5开头有 'We test the three predictions' 但后续小节未回溯具体prediction编号\"\n\n- id: \"R13-W5\"\n  summary: \"缺引: Dhuliawala et al. 2023 Chain-of-Verification\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-M1首提, R1交叉同意. 与自验证局限高度相关\"\n"
  }
}
```

</details>

---


### Tool result

_source line 1423 · 2026-05-22T07:58:39.304049+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml\", \"bytes\": 18252}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1424 · 2026-05-22T08:01:19.257053+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Consolidated Review Report — Round 10 (Fresh)\n\n**论文**: \"Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Show No Evidence of Improving LLM Reasoning\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**Reviewer Panel**: 2 Reviewers (R1: 方法严谨性+实验有效性; R2: 新颖性+完整性+写作质量)\n**审稿模式**: 圆桌多轮（Round 1 独立审稿 → 交叉分享 → 收敛，1轮完成）\n\n---\n\n## Summary\n\n本文提出 Symbolic Invariant Consensus Aggregation (SICA)，从 LLM 推理 trace 中提取逻辑约束并通过加权 partial MAX-SAT (Z3) 聚合答案，试图突破 Self-Consistency (SC) 的多数投票瓶颈。在 6 个开源模型 (7B–32B)、3 个逻辑推理领域 (FOLIO, ProofWriter, LogiQA)、3,000+ 条件评估（~1,250 unique instances）中，未发现统计显著的改善。论文将失败归因于 Symbolic Confirmation Bias (SCB)：自提取约束系统性支持模型多数答案（BR 1.05–4.97×），MAX-SAT 在 94.4% 情况下退化为简单计数。27 种无训练修复策略均失败。跨架构 NLI 验证 (DeBERTa) 在 ProofWriter 上获得 +6.67pp (p<0.001)。\n\n---\n\n## Strengths\n\n**S1. 实验规模和系统性为负面结果论文树立标杆。** [R1-S1, R2-S1 共识] 6 个主模型 + 5 个 frontier 模型，3 个推理领域，~1,250 unique 实例，4-seed 复制，27 种修复策略——远超典型负面结果论文的评估力度。\n\n**S2. 实验控制设计精巧。** [R1-S2 主导，R2 认可] Oracle control (§4.3) 用 gold 约束证明 MAX-SAT 机制本身有效 (+29.90pp Mistral, +14.22pp Qwen-14B FOLIO, +17.17pp ProofWriter)，精准定位瓶颈在约束质量。Shuffle control (§5.2) 证明 SCB 是结构性偏差（BR_shuffle ≈ BR_real, p>0.7）。Cross-model extraction 扩展到 9 个模型确认 SCB 普遍性。\n\n**S3. 诊断框架有独立复用价值。** [R1-S3, R2-S2 共识] BR、CCR (Eq. 7)、K_eff 构成可复用的诊断工具包，可评估任何\"自提取+聚合\"范式。CCR > 0 vs. CCR < 0 清晰分离了跨架构 vs. 同模型条件。\n\n**S4. CJT 理论框架提供原则性解释。** [R1-S4, R2-S3 共识] 将 SC/SICA 放在 Condorcet Jury Theorem 框架下，K_eff 将\"有效独立样本数\"量化（K_eff = 1.2–3.6 for nominal K=12），为理解采样收益递减提供了理论支撑。\n\n**S5. 叙事层次超越多数负面结果论文。** [R2-S5 主导，R1 认可] 不是简单报告\"方法 X 不 work\"，而是：机制性解释 (SCB) → 理论框架 (CJT violation) → 可操作诊断 (K_eff, BR, C₀) → 初步逃逸方案 (cross-architecture NLI)。\n\n**S6. 附录质量极高。** [R2-S4, R1 Reproducibility 4/5] 14+ 页附录含完整 prompt 模板、MAX-SAT 算法伪代码、per-condition 统计分析、case studies、failure mode taxonomy。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [CRITICAL] 摘要 BR 数值选择性报告，有夸大嫌疑。** [R1-N1, R2 AGREE]\n- 摘要报告 \"bias ratio 4.97×\" 和 \"83.3%\"——来自 Mistral-7B/FOLIO 这一最极端条件\n- Table 2 (p7) 实际 BR 范围：Mistral-7B 4.97 → o3 1.66 → Gemini-2.5-Pro 2.79（注：frontier 模型使用 cross-model extraction，非 self-extraction）\n- 摘要应报告中位数或范围（如 \"BR ranges from 1.66 to 4.97\"），而非最极端值\n- Frontier 模型 BR 相对较低，暗示 SCB 严重性可能与模型能力负相关——论文的 \"universal\" framing 需更强限定\n\n**MF2. [CRITICAL] 统计功效呈现不足，\"No Evidence\" 声明与统计结论存在张力。** [R1-N2 + R2-N2，完全共识]\n- 16 个非退化条件中 10 个 underpowered（MDE > 2pp at 80% power）\n- TOST 仅确认 4/16 条件等价于零效应\n- Aggregate sign test 8+/15− (p=0.21) 是\"inconclusive\"而非\"negative\"\n- Power analysis (Appendix E Table 6) 是关键信息但被埋在附录中\n- 标题 \"Show No Evidence\" 在日常学术用语中可被理解为\"效果已被排除\"，但论文只是\"未检测到显著效果\"——且部分条件下检测力不足以区分无效果与小正效果\n- **必须修改**：§4.2 增加明确 power statement（如 \"For the 10 underpowered conditions, we cannot rule out effects smaller than ±X pp\"）；将 MDE 核心数字从附录提到正文\n\n**MF3. [CRITICAL] α=0.5 参数无敏感性分析。** [R1-N3 主导，R2 AGREE with nuance]\n- α=0.5 控制约束权重与投票权重的相对影响\n- 94.4% MAX-SAT≡count-only 的核心发现可能依赖于 α 的特定取值\n- R2 认为影响可能有限（当 BR>1 时约束方向与投票一致，α 调整不影响最终选择），但缺少实验验证\n- **必须修改**：在 2–3 个代表性条件（高 BR + 低 BR）上跑 α∈{0.1, 0.3, 0.7} 消融，报告退化率变化\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. Discussion/Conclusion 过于压缩。** [R2-W2, R1 AGREE]\n- §7 (p8) 不到半页，缺少：(1) SCB 与 CoT unfaithfulness 关系讨论，(2) 对 neuro-symbolic 实践者的可操作建议，(3) test-time scaling 含义展开\n- 视觉审查发现 Discussion 约 3–4 行溢出到 page 9 顶部——需压缩或重排\n\n**SF2. 符号/指标过载。** [R2-W1, R1 AGREE]\n- 8 页正文引入 7 个定量工具（K_eff, κ, BR, C₀, CCR, ProcessSim, ρ_same），认知负担重\n- 建议：ProcessSim (§5.3) 和 CCR (§5.4) 移至附录，正文聚焦 K_eff/BR/C₀ 三个核心指标\n\n**SF3. 跨架构 NLI claim 须限定到命题逻辑任务。** [R1-W1, R2 部分涉及]\n- FOLIO 和 ProofWriter 均为命题/一阶逻辑任务，NLI 模型天然对齐 textual entailment\n- 未在 StrategyQA、LogiQA 等非逻辑域测试 NLI 验证\n- 摘要应限定为 \"on propositional-logic benchmarks\"；§6 或 Limitations 讨论 domain limitation\n- 注：R2 初审误称\"仅一个验证器\"，R1 交叉纠正（实际 3 个 NLI 架构 × 4 generators × 5 weights），证据规模比 R2 初判更充分\n\n**SF4. TOST ±2pp margin 缺乏独立论证。** [R1-W4, R2 AGREE]\n- 用 SC 自身效应量定义\"可忽略\"有循环性\n- ±3pp 时所有条件均 equivalent——结论对 margin 敏感\n- 建议引用领域公认的最小实际意义差异，或提供 margin sensitivity analysis\n\n**SF5. 语法去重可能系统性膨胀 BR。** [R1-W2, R2 AGREE]\n- 语义等价但语法不同的约束被分别计数（去重率仅 46.0%）\n- 论文有 shuffle control 部分回应（BR_shuffle ≈ BR_real），但未报告 Z3 语义去重后 BR\n- 建议补充语义去重后 BR 值\n\n**SF6. Table 1 核心结果表可读性不足。** [R2-W4, R1 小问题#1 一致]\n- Type A/B/C 子区域分隔视觉层次不够，显著性标记系统复杂\n- 建议增加水平线分隔或浅色底纹；简化显著性标记\n\n**SF7. \"Symbolic Mirage Hypothesis\" 定位不一致。** [R2-W3, R1 AGREE 低严重性]\n- §3.3 提出假设，§5 直接以结论性措辞使用，缺显式验证回溯\n- 建议 §5 结尾增加总结段，显式对应三个 testable predictions\n\n**SF8. 4-seed replication 充分性存疑。** [R1-W5, R2 PARTIALLY AGREE]\n- Seed 间变异性未充分量化（inter-seed SD 未报告）\n- Bootstrap CI 是否聚合 4 seeds 不清楚\n\n**SF9. TF-IDF 作为 process independence 代理粒度较粗。** [R1-W3, R2 AGREE with reservation]\n- 只能捕捉词汇层面重叠，非推理结构相似性\n- 但 ProcessSim 不是核心论证承重墙（R2 观察），属补充证据\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 在交叉分享后达成一致：\n\n| 编号 | 问题 | 共识状态 |\n|------|------|----------|\n| MF1 | BR 选择性报告 | [AGREE] 摘要应报告范围/中位数 |\n| MF2 | 统计功效 framing | [AGREE] 正文需加 power statement，提升 Appendix E |\n| MF3 | α 无消融 | [AGREE] 需跑 α 消融（R2 认为影响有限但同意做） |\n| SF1 | Discussion 过短 | [AGREE] 需扩展覆盖 3 个话题 |\n| SF2 | 指标过载 | [AGREE] ProcessSim/CCR 可移附录 |\n| SF3 | NLI claim scope | [AGREE] 须限定到命题逻辑 |\n| SF4 | TOST margin | [AGREE] 需 sensitivity analysis |\n| SF5 | 语法去重膨胀 BR | [AGREE] 需报告语义去重后 BR |\n| SF6 | Table 1 可读性 | [AGREE] 需增加视觉分隔 |\n\n## Reviewer Divergence\n\n| 编号 | 问题 | R1 | R2 | 最终判断 |\n|------|------|----|----|----------|\n| R2-N1 | §6 跨架构贡献不足 | [REBUT] R2 事实错误（3 verifiers 非 1），证据规模已超 PoC 标准 | [AGREE] 仅 1 verifier（被 R1 纠正） | **降级为 SF3**：证据比 R2 初判更充分，但 domain-specificity 问题成立 |\n| R2-W5 | CJT 边界条件 | [REBUT] 论文已涉及 high/low accuracy 两端，CJT 是 framing device 非完整推导 | [AGREE] | **不作为独立问题**，合并到 SF1 Discussion 扩展 |\n| Excitement | 新颖性增量 | 3/5（量化贡献有独立价值） | 2.5/5（被先验工作预示） | **记录分歧**：SCB 概念层面增量有限，但量化深度和实验规模提供了超越先验工作的实证价值 |\n\n---\n\n## Questions to Authors\n\n**Q1** [R1]: Table 2 中 o3 (BR=1.66) 和 Gemini-2.5-Pro (BR=2.79) 的 BR 远低于 Mistral-7B (4.97)。SCB 严重性是否与模型能力负相关？如果仅在 frontier 模型上测试 SICA，\"no evidence\" 结论是否仍成立？（注意 extractor confound：frontier 使用 Mistral-7B 做 cross-model extraction）\n\n**Q2** [R1]: 94.4% MAX-SAT≡count-only 的统计来自哪些条件？是否包括退化条件 (C₀<5%)？非退化条件单独的比率是多少？\n\n**Q3** [R1]: DeBERTa standalone accuracy 在 FOLIO 上低于 SC baseline (49.51% vs. 55.88%)，但 combo 仍有增益 (+2.94pp)。这是否与 Empirical Finding 2 的 capability gap hypothesis 矛盾？\"Exceed\" 是指 standalone accuracy 还是 independence-adjusted effective accuracy？\n\n**Q4** [R1]: 27 种修复策略中是否有任何在个别条件上通过显著性检验（即使总体不显著）？这些 \"pocket of success\" 的特征是什么？\n\n---\n\n## Missing References\n\n1. **Dhuliawala et al., 2023** — \"Chain-of-Verification Reduces Hallucination in Large Language Models\" [R2-M1, R1 交叉 AGREE] — 直接研究 LLM 自验证局限，与 SCB 发现互补\n2. **Lightman et al., 2024** — R2 初审提出缺引，R1 交叉回应确认论文已引用（References p11: \"Let's verify step by step. In ICLR.\"）——**非遗漏**\n3. R1 建议在 Related Work §2 中更明确地区分 trained verifier 与 self-extracted constraint——论文核心洞见 (CCR 正/负) 依赖于这一区分，应更早建立\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置，跳过。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（耗时 ~4.5 分钟），结果：0 critical, 2 warning, 5 info。\n\n**WARNING:**\n1. **Page 9 溢出**: 主文 §7 (Discussion) 约 3–4 行溢出到 page 9 顶部，Limitations 从 page 9 中段开始。EMNLP 2026 主文限 8 页（Limitations 豁免），当前主文约 8.05–8.1 页。ACL/ARR 对页数限制零容忍，**建议压缩 Discussion 或前文确保 §7 在 page 8 内结束**。\n2. **Pages 3–5 低视觉密度**: Related Work → Experiment Setup 连续约 2.5 页无 figure/table，审稿人快速翻阅时可能感到单调。\n\n**INFO:**\n- Figure 1 (p2) 尺寸偏小，内部标签打印时可能偏小\n- Figure 2 (p7) axis label 字号约正文 65–70%，接近可读下限\n- 附录单页表格密度极高（page 14 有 4 个表），审稿人查阅体验较差\n- 附录 14 页含 29 表 + 5 图 + 2 算法，建议在附录开头加 overview 导航\n- Prompt template 和 Algorithm 排版正确\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 4/5 | 4/5 | **4/5** |\n| Excitement | 3/5 | 2.5/5 | **2.75/5** |\n| Reproducibility | 4/5 | 4/5 | **4/5** |\n| Overall | 3.5 | 3.5 | **3.5** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n**判断依据**：\n- **Soundness 4/5**：实验设计严密（oracle/shuffle/cross-model 三重控制），统计方法总体正确。扣 1 分：10/16 条件 underpowered，α 无消融，TOST margin 有循环性。\n- **Excitement 2.75/5**：SCB 的定量刻画对 neuro-symbolic 和 test-time scaling 社区有参考价值，但核心发现（自提取约束不提供独立信号）部分被 Huang et al. (2024) self-correction 和 Stechly et al. (2025) 所预示。诊断工具 (K_eff, BR, C₀) 实用但是已有统计量的直接适配。跨架构逃逸方案初步但 domain-specific。\n- **Reproducibility 4/5**：参数完整报告，prompt 模板和算法伪代码详尽，受匿名限制未提供代码。\n\n**接收建议**：\n- **当前状态**：Findings 级别确定达标。方法论扎实 + 有用的负面结果 + 可复用的诊断工具。\n- **升至 Conference 需要**：解决 MF1–MF3（BR 报告、power framing、α 消融），扩展 Discussion (SF1)，收窄 NLI claim scope (SF3)。如果 α 消融验证了退化率对 α 不敏感，这反而更强力地支持 SCB 结论。\n- **主要风险**：如果 frontier 模型 BR≈1 且 α 消融显示退化率下降，论文的核心 \"universal SCB\" narrative 需要实质性修改。\n\n---\n\n## Detailed Comments\n\n### Title & Abstract (p1)\n- 标题 \"Show No Evidence\" 在统计学中是标准用法，R1 认为可保留，R2 建议改为更限定的表述。建议保留标题但在 Abstract 增加 MDE 限定句。\n- BR 4.97× 应改为范围/中位数。\n- \"six open-source LLMs (7B–32B)\" 准确，但 cross-model extraction 扩展到 frontier 的角色应在摘要中更清晰区分。\n\n### Introduction (pp1–2)\n- Story arc 清晰：SC ceiling → CJT independence → SICA → SCB → escape。\n- 三个 Contributions (p2) 措辞基本准确。R2 曾质疑 §6 作为贡献，但 R1 纠正后降级为 domain-specificity 问题。\n- Figure 1 (p2) 有效传达 pipeline 但尺寸偏小。\n\n### Related Work (pp2–3)\n- 覆盖面广（SC extensions, neuro-symbolic, test-time compute, CJT positioning），结构清晰。\n- 缺 Dhuliawala et al. (2023) Chain-of-Verification。\n- Trained verifier vs. self-extracted constraint 的核心区分应更早建立。\n\n### Background & Setup (pp3–5)\n- CJT 框架和 K_eff 定义清晰，ordinal diagnostic caveat 正确。\n- SICA pipeline (§3.2) 形式化完整。\n- Symbolic Mirage Hypothesis (§3.3) 的三个 testable predictions 好，但后续验证回溯不够显式。\n- Empirical Finding 1–2 的 tcolorbox 框在负面结果论文中略显过度包装。\n- α=0.5 需消融验证。\n\n### Experiments (pp5–6)\n- Table 1 是论文核心，内容完整但可读性需改善。\n- §4.2 的统计讨论技术正确但缺 power statement。\n- Oracle control (§4.3) 设计精巧，是论文最强证据之一。\n\n### Analysis (pp6–7)\n- SCB 分析 (§5.2) + shuffle control 是核心贡献，论证严密。\n- 指标过多（7 个），ProcessSim 和 CCR 可移至附录。\n- Figure 2 (27 strategies) 信息密度高但个别策略难以区分。\n\n### Cross-Architecture Proof-of-Concept (p8)\n- 3 NLI architectures × 4 generators × 5 weights 的评估规模超出 PoC 标准。\n- 但仅在命题逻辑任务上验证，claim 须限定。\n- Capability gap hypothesis (Spearman ρ=1.0, n=6) 的统计基础有限（4/6 共享 DeBERTa verifier）。\n\n### Discussion & Conclusion (p8)\n- 过于压缩（约半页），与论文的贡献规模不匹配。\n- 缺 SCB vs CoT unfaithfulness 讨论、实践者建议、test-time scaling 含义。\n- 视觉审查发现约 3–4 行溢出到 page 9——需压缩。\n\n### Limitations (pp8–9)\n- 覆盖关键局限（模型范围、domain 限制、power、seed、cost）。\n- \"7B to 32B parameters\" 与论文其他部分一致（注：R2-M4 发现 Limitations 中有 \"7B-128B\" 不一致，需统一检查）。\n\n### Format Compliance\n- 正文约 8.05–8.1 页——**需压缩至严格 8 页内**\n- 匿名完整（\"Anonymous ACL submission\"，无身份泄漏）\n- ACL template 正确（`\\usepackage[review]{acl}`）\n- 引用格式合规",
  "project": "symb_invariant_consensus",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Consolidated Review Report — Round 10 (Fresh)\n\n**论文**: \"Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Show No Evidence of Improving LLM Reasoning\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**Reviewer Panel**: 2 Reviewers (R1: 方法严谨性+实验有效性; R2: 新颖性+完整性+写作质量)\n**审稿模式**: 圆桌多轮（Round 1 独立审稿 → 交叉分享 → 收敛，1轮完成）\n\n---\n\n## Summary\n\n本文提出 Symbolic Invariant Consensus Aggregation (SICA)，从 LLM 推理 trace 中提取逻辑约束并通过加权 partial MAX-SAT (Z3) 聚合答案，试图突破 Self-Consistency (SC) 的多数投票瓶颈。在 6 个开源模型 (7B–32B)、3 个逻辑推理领域 (FOLIO, ProofWriter, LogiQA)、3,000+ 条件评估（~1,250 unique instances）中，未发现统计显著的改善。论文将失败归因于 Symbolic Confirmation Bias (SCB)：自提取约束系统性支持模型多数答案（BR 1.05–4.97×），MAX-SAT 在 94.4% 情况下退化为简单计数。27 种无训练修复策略均失败。跨架构 NLI 验证 (DeBERTa) 在 ProofWriter 上获得 +6.67pp (p<0.001)。\n\n---\n\n## Strengths\n\n**S1. 实验规模和系统性为负面结果论文树立标杆。** [R1-S1, R2-S1 共识] 6 个主模型 + 5 个 frontier 模型，3 个推理领域，~1,250 unique 实例，4-seed 复制，27 种修复策略——远超典型负面结果论文的评估力度。\n\n**S2. 实验控制设计精巧。** [R1-S2 主导，R2 认可] Oracle control (§4.3) 用 gold 约束证明 MAX-SAT 机制本身有效 (+29.90pp Mistral, +14.22pp Qwen-14B FOLIO, +17.17pp ProofWriter)，精准定位瓶颈在约束质量。Shuffle control (§5.2) 证明 SCB 是结构性偏差（BR_shuffle ≈ BR_real, p>0.7）。Cross-model extraction 扩展到 9 个模型确认 SCB 普遍性。\n\n**S3. 诊断框架有独立复用价值。** [R1-S3, R2-S2 共识] BR、CCR (Eq. 7)、K_eff 构成可复用的诊断工具包，可评估任何\"自提取+聚合\"范式。CCR > 0 vs. CCR < 0 清晰分离了跨架构 vs. 同模型条件。\n\n**S4. CJT 理论框架提供原则性解释。** [R1-S4, R2-S3 共识] 将 SC/SICA 放在 Condorcet Jury Theorem 框架下，K_eff 将\"有效独立样本数\"量化（K_eff = 1.2–3.6 for nominal K=12），为理解采样收益递减提供了理论支撑。\n\n**S5. 叙事层次超越多数负面结果论文。** [R2-S5 主导，R1 认可] 不是简单报告\"方法 X 不 work\"，而是：机制性解释 (SCB) → 理论框架 (CJT violation) → 可操作诊断 (K_eff, BR, C₀) → 初步逃逸方案 (cross-architecture NLI)。\n\n**S6. 附录质量极高。** [R2-S4, R1 Reproducibility 4/5] 14+ 页附录含完整 prompt 模板、MAX-SAT 算法伪代码、per-condition 统计分析、case studies、failure mode taxonomy。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [CRITICAL] 摘要 BR 数值选择性报告，有夸大嫌疑。** [R1-N1, R2 AGREE]\n- 摘要报告 \"bias ratio 4.97×\" 和 \"83.3%\"——来自 Mistral-7B/FOLIO 这一最极端条件\n- Table 2 (p7) 实际 BR 范围：Mistral-7B 4.97 → o3 1.66 → Gemini-2.5-Pro 2.79（注：frontier 模型使用 cross-model extraction，非 self-extraction）\n- 摘要应报告中位数或范围（如 \"BR ranges from 1.66 to 4.97\"），而非最极端值\n- Frontier 模型 BR 相对较低，暗示 SCB 严重性可能与模型能力负相关——论文的 \"universal\" framing 需更强限定\n\n**MF2. [CRITICAL] 统计功效呈现不足，\"No Evidence\" 声明与统计结论存在张力。** [R1-N2 + R2-N2，完全共识]\n- 16 个非退化条件中 10 个 underpowered（MDE > 2pp at 80% power）\n- TOST 仅确认 4/16 条件等价于零效应\n- Aggregate sign test 8+/15− (p=0.21) 是\"inconclusive\"而非\"negative\"\n- Power analysis (Appendix E Table 6) 是关键信息但被埋在附录中\n- 标题 \"Show No Evidence\" 在日常学术用语中可被理解为\"效果已被排除\"，但论文只是\"未检测到显著效果\"——且部分条件下检测力不足以区分无效果与小正效果\n- **必须修改**：§4.2 增加明确 power statement（如 \"For the 10 underpowered conditions, we cannot rule out effects smaller than ±X pp\"）；将 MDE 核心数字从附录提到正文\n\n**MF3. [CRITICAL] α=0.5 参数无敏感性分析。** [R1-N3 主导，R2 AGREE with nuance]\n- α=0.5 控制约束权重与投票权重的相对影响\n- 94.4% MAX-SAT≡count-only 的核心发现可能依赖于 α 的特定取值\n- R2 认为影响可能有限（当 BR>1 时约束方向与投票一致，α 调整不影响最终选择），但缺少实验验证\n- **必须修改**：在 2–3 个代表性条件（高 BR + 低 BR）上跑 α∈{0.1, 0.3, 0.7} 消融，报告退化率变化\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. Discussion/Conclusion 过于压缩。** [R2-W2, R1 AGREE]\n- §7 (p8) 不到半页，缺少：(1) SCB 与 CoT unfaithfulness 关系讨论，(2) 对 neuro-symbolic 实践者的可操作建议，(3) test-time scaling 含义展开\n- 视觉审查发现 Discussion 约 3–4 行溢出到 page 9 顶部——需压缩或重排\n\n**SF2. 符号/指标过载。** [R2-W1, R1 AGREE]\n- 8 页正文引入 7 个定量工具（K_eff, κ, BR, C₀, CCR, ProcessSim, ρ_same），认知负担重\n- 建议：ProcessSim (§5.3) 和 CCR (§5.4) 移至附录，正文聚焦 K_eff/BR/C₀ 三个核心指标\n\n**SF3. 跨架构 NLI claim 须限定到命题逻辑任务。** [R1-W1, R2 部分涉及]\n- FOLIO 和 ProofWriter 均为命题/一阶逻辑任务，NLI 模型天然对齐 textual entailment\n- 未在 StrategyQA、LogiQA 等非逻辑域测试 NLI 验证\n- 摘要应限定为 \"on propositional-logic benchmarks\"；§6 或 Limitations 讨论 domain limitation\n- 注：R2 初审误称\"仅一个验证器\"，R1 交叉纠正（实际 3 个 NLI 架构 × 4 generators × 5 weights），证据规模比 R2 初判更充分\n\n**SF4. TOST ±2pp margin 缺乏独立论证。** [R1-W4, R2 AGREE]\n- 用 SC 自身效应量定义\"可忽略\"有循环性\n- ±3pp 时所有条件均 equivalent——结论对 margin 敏感\n- 建议引用领域公认的最小实际意义差异，或提供 margin sensitivity analysis\n\n**SF5. 语法去重可能系统性膨胀 BR。** [R1-W2, R2 AGREE]\n- 语义等价但语法不同的约束被分别计数（去重率仅 46.0%）\n- 论文有 shuffle control 部分回应（BR_shuffle ≈ BR_real），但未报告 Z3 语义去重后 BR\n- 建议补充语义去重后 BR 值\n\n**SF6. Table 1 核心结果表可读性不足。** [R2-W4, R1 小问题#1 一致]\n- Type A/B/C 子区域分隔视觉层次不够，显著性标记系统复杂\n- 建议增加水平线分隔或浅色底纹；简化显著性标记\n\n**SF7. \"Symbolic Mirage Hypothesis\" 定位不一致。** [R2-W3, R1 AGREE 低严重性]\n- §3.3 提出假设，§5 直接以结论性措辞使用，缺显式验证回溯\n- 建议 §5 结尾增加总结段，显式对应三个 testable predictions\n\n**SF8. 4-seed replication 充分性存疑。** [R1-W5, R2 PARTIALLY AGREE]\n- Seed 间变异性未充分量化（inter-seed SD 未报告）\n- Bootstrap CI 是否聚合 4 seeds 不清楚\n\n**SF9. TF-IDF 作为 process independence 代理粒度较粗。** [R1-W3, R2 AGREE with reservation]\n- 只能捕捉词汇层面重叠，非推理结构相似性\n- 但 ProcessSim 不是核心论证承重墙（R2 观察），属补充证据\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 在交叉分享后达成一致：\n\n| 编号 | 问题 | 共识状态 |\n|------|------|----------|\n| MF1 | BR 选择性报告 | [AGREE] 摘要应报告范围/中位数 |\n| MF2 | 统计功效 framing | [AGREE] 正文需加 power statement，提升 Appendix E |\n| MF3 | α 无消融 | [AGREE] 需跑 α 消融（R2 认为影响有限但同意做） |\n| SF1 | Discussion 过短 | [AGREE] 需扩展覆盖 3 个话题 |\n| SF2 | 指标过载 | [AGREE] ProcessSim/CCR 可移附录 |\n| SF3 | NLI claim scope | [AGREE] 须限定到命题逻辑 |\n| SF4 | TOST margin | [AGREE] 需 sensitivity analysis |\n| SF5 | 语法去重膨胀 BR | [AGREE] 需报告语义去重后 BR |\n| SF6 | Table 1 可读性 | [AGREE] 需增加视觉分隔 |\n\n## Reviewer Divergence\n\n| 编号 | 问题 | R1 | R2 | 最终判断 |\n|------|------|----|----|----------|\n| R2-N1 | §6 跨架构贡献不足 | [REBUT] R2 事实错误（3 verifiers 非 1），证据规模已超 PoC 标准 | [AGREE] 仅 1 verifier（被 R1 纠正） | **降级为 SF3**：证据比 R2 初判更充分，但 domain-specificity 问题成立 |\n| R2-W5 | CJT 边界条件 | [REBUT] 论文已涉及 high/low accuracy 两端，CJT 是 framing device 非完整推导 | [AGREE] | **不作为独立问题**，合并到 SF1 Discussion 扩展 |\n| Excitement | 新颖性增量 | 3/5（量化贡献有独立价值） | 2.5/5（被先验工作预示） | **记录分歧**：SCB 概念层面增量有限，但量化深度和实验规模提供了超越先验工作的实证价值 |\n\n---\n\n## Questions to Authors\n\n**Q1** [R1]: Table 2 中 o3 (BR=1.66) 和 Gemini-2.5-Pro (BR=2.79) 的 BR 远低于 Mistral-7B (4.97)。SCB 严重性是否与模型能力负相关？如果仅在 frontier 模型上测试 SICA，\"no evidence\" 结论是否仍成立？（注意 extractor confound：frontier 使用 Mistral-7B 做 cross-model extraction）\n\n**Q2** [R1]: 94.4% MAX-SAT≡count-only 的统计来自哪些条件？是否包括退化条件 (C₀<5%)？非退化条件单独的比率是多少？\n\n**Q3** [R1]: DeBERTa standalone accuracy 在 FOLIO 上低于 SC baseline (49.51% vs. 55.88%)，但 combo 仍有增益 (+2.94pp)。这是否与 Empirical Finding 2 的 capability gap hypothesis 矛盾？\"Exceed\" 是指 standalone accuracy 还是 independence-adjusted effective accuracy？\n\n**Q4** [R1]: 27 种修复策略中是否有任何在个别条件上通过显著性检验（即使总体不显著）？这些 \"pocket of success\" 的特征是什么？\n\n---\n\n## Missing References\n\n1. **Dhuliawala et al., 2023** — \"Chain-of-Verification Reduces Hallucination in Large Language Models\" [R2-M1, R1 交叉 AGREE] — 直接研究 LLM 自验证局限，与 SCB 发现互补\n2. **Lightman et al., 2024** — R2 初审提出缺引，R1 交叉回应确认论文已引用（References p11: \"Let's verify step by step. In ICLR.\"）——**非遗漏**\n3. R1 建议在 Related Work §2 中更明确地区分 trained verifier 与 self-extracted constraint——论文核心洞见 (CCR 正/负) 依赖于这一区分，应更早建立\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置，跳过。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（耗时 ~4.5 分钟），结果：0 critical, 2 warning, 5 info。\n\n**WARNING:**\n1. **Page 9 溢出**: 主文 §7 (Discussion) 约 3–4 行溢出到 page 9 顶部，Limitations 从 page 9 中段开始。EMNLP 2026 主文限 8 页（Limitations 豁免），当前主文约 8.05–8.1 页。ACL/ARR 对页数限制零容忍，**建议压缩 Discussion 或前文确保 §7 在 page 8 内结束**。\n2. **Pages 3–5 低视觉密度**: Related Work → Experiment Setup 连续约 2.5 页无 figure/table，审稿人快速翻阅时可能感到单调。\n\n**INFO:**\n- Figure 1 (p2) 尺寸偏小，内部标签打印时可能偏小\n- Figure 2 (p7) axis label 字号约正文 65–70%，接近可读下限\n- 附录单页表格密度极高（page 14 有 4 个表），审稿人查阅体验较差\n- 附录 14 页含 29 表 + 5 图 + 2 算法，建议在附录开头加 overview 导航\n- Prompt template 和 Algorithm 排版正确\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 — Borderline Conference**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 4/5 | 4/5 | **4/5** |\n| Excitement | 3/5 | 2.5/5 | **2.75/5** |\n| Reproducibility | 4/5 | 4/5 | **4/5** |\n| Overall | 3.5 | 3.5 | **3.5** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n**判断依据**：\n- **Soundness 4/5**：实验设计严密（oracle/shuffle/cross-model 三重控制），统计方法总体正确。扣 1 分：10/16 条件 underpowered，α 无消融，TOST margin 有循环性。\n- **Excitement 2.75/5**：SCB 的定量刻画对 neuro-symbolic 和 test-time scaling 社区有参考价值，但核心发现（自提取约束不提供独立信号）部分被 Huang et al. (2024) self-correction 和 Stechly et al. (2025) 所预示。诊断工具 (K_eff, BR, C₀) 实用但是已有统计量的直接适配。跨架构逃逸方案初步但 domain-specific。\n- **Reproducibility 4/5**：参数完整报告，prompt 模板和算法伪代码详尽，受匿名限制未提供代码。\n\n**接收建议**：\n- **当前状态**：Findings 级别确定达标。方法论扎实 + 有用的负面结果 + 可复用的诊断工具。\n- **升至 Conference 需要**：解决 MF1–MF3（BR 报告、power framing、α 消融），扩展 Discussion (SF1)，收窄 NLI claim scope (SF3)。如果 α 消融验证了退化率对 α 不敏感，这反而更强力地支持 SCB 结论。\n- **主要风险**：如果 frontier 模型 BR≈1 且 α 消融显示退化率下降，论文的核心 \"universal SCB\" narrative 需要实质性修改。\n\n---\n\n## Detailed Comments\n\n### Title & Abstract (p1)\n- 标题 \"Show No Evidence\" 在统计学中是标准用法，R1 认为可保留，R2 建议改为更限定的表述。建议保留标题但在 Abstract 增加 MDE 限定句。\n- BR 4.97× 应改为范围/中位数。\n- \"six open-source LLMs (7B–32B)\" 准确，但 cross-model extraction 扩展到 frontier 的角色应在摘要中更清晰区分。\n\n### Introduction (pp1–2)\n- Story arc 清晰：SC ceiling → CJT independence → SICA → SCB → escape。\n- 三个 Contributions (p2) 措辞基本准确。R2 曾质疑 §6 作为贡献，但 R1 纠正后降级为 domain-specificity 问题。\n- Figure 1 (p2) 有效传达 pipeline 但尺寸偏小。\n\n### Related Work (pp2–3)\n- 覆盖面广（SC extensions, neuro-symbolic, test-time compute, CJT positioning），结构清晰。\n- 缺 Dhuliawala et al. (2023) Chain-of-Verification。\n- Trained verifier vs. self-extracted constraint 的核心区分应更早建立。\n\n### Background & Setup (pp3–5)\n- CJT 框架和 K_eff 定义清晰，ordinal diagnostic caveat 正确。\n- SICA pipeline (§3.2) 形式化完整。\n- Symbolic Mirage Hypothesis (§3.3) 的三个 testable predictions 好，但后续验证回溯不够显式。\n- Empirical Finding 1–2 的 tcolorbox 框在负面结果论文中略显过度包装。\n- α=0.5 需消融验证。\n\n### Experiments (pp5–6)\n- Table 1 是论文核心，内容完整但可读性需改善。\n- §4.2 的统计讨论技术正确但缺 power statement。\n- Oracle control (§4.3) 设计精巧，是论文最强证据之一。\n\n### Analysis (pp6–7)\n- SCB 分析 (§5.2) + shuffle control 是核心贡献，论证严密。\n- 指标过多（7 个），ProcessSim 和 CCR 可移至附录。\n- Figure 2 (27 strategies) 信息密度高但个别策略难以区分。\n\n### Cross-Architecture Proof-of-Concept (p8)\n- 3 NLI architectures × 4 generators × 5 weights 的评估规模超出 PoC 标准。\n- 但仅在命题逻辑任务上验证，claim 须限定。\n- Capability gap hypothesis (Spearman ρ=1.0, n=6) 的统计基础有限（4/6 共享 DeBERTa verifier）。\n\n### Discussion & Conclusion (p8)\n- 过于压缩（约半页），与论文的贡献规模不匹配。\n- 缺 SCB vs CoT unfaithfulness 讨论、实践者建议、test-time scaling 含义。\n- 视觉审查发现约 3–4 行溢出到 page 9——需压缩。\n\n### Limitations (pp8–9)\n- 覆盖关键局限（模型范围、domain 限制、power、seed、cost）。\n- \"7B to 32B parameters\" 与论文其他部分一致（注：R2-M4 发现 Limitations 中有 \"7B-128B\" 不一致，需统一检查）。\n\n### Format Compliance\n- 正文约 8.05–8.1 页——**需压缩至严格 8 页内**\n- 匿名完整（\"Anonymous ACL submission\"，无身份泄漏）\n- ACL template 正确（`\\usepackage[review]{acl}`）\n- 引用格式合规",
    "project": "symb_invariant_consensus",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
  }
}
```

</details>

---


### Tool result

_source line 1425 · 2026-05-22T08:01:24.181508+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_970d5ea3f54df81296b97321fcded892:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4924
}
```

</details>

---


### Tool call

_source line 1426 · 2026-05-22T08:01:28.932095+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-3: 初始化 + 审稿 + 交叉 + 收敛', 'status': 'completed', 'activeForm': '完成全部审稿轮次和收敛判断'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'completed', 'activeForm': '完成报告合成和投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0-3: 初始化 + 审稿 + 交叉 + 收敛', 'status': 'completed', 'activeForm': '完成全部审稿轮次和收敛判断'}, {'content': 'Step 4: 汇总报告 + 投递', 'status': 'completed', 'activeForm': '完成报告合成和投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1427 · 2026-05-22T08:01:28.932613+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 1428 · 2026-05-22T08:01:37.991949+00:00_

**审稿圆桌会议完成。**

报告已投递至 Research Director。核心结论：

- **Overall: 3.5 / 5 (Borderline Conference)**，Soundness 4/5，Excitement 2.75/5
- **3 个 Must-Fix**：BR 选择性报告、统计功效 framing 不足、α 无消融
- **9 个 Should-Fix**：Discussion 过短、指标过载、NLI claim scope、TOST margin、语法去重膨胀 BR、Table 1 可读性、Symbolic Mirage 定位、4-seed 充分性、TF-IDF 粒度
- **视觉审查**：主文约 8.05 页，需压缩至严格 8 页内
- **接收建议**：Findings 确定达标；解决 MF1–MF3 + 扩展 Discussion 后有望升至 Conference

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 94

## Round 94

2 recorded events


### User

_source line 1429 · 2026-05-22T08:01:39.499736+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。逐条总结：

- **R2-N1（跨架构证据不足）**：**REBUT** — R2 误称"仅一个验证器"，实际论文测试了 3 个 NLI 架构（DeBERTa/RoBERTa/BART），Table 25-26 有完整证据。仅同意 verifier error propagation 未讨论这一子论点。
- **R2-N2（标题 vs 统计功效）**：**AGREE** — 与我的 R1-N2 一致，但不同意 R2 的具体改标题建议。
- **R2-W1（指标过载）**：**AGREE**，建议将 CCR 和 ProcessSim 移至附录。
- **R2-W2（Discussion 压缩）**：**AGREE**，缺少 SCB vs CoT unfaithfulness、test-time scaling 含义等讨论。
- **R2-W3（假设定位不一致）**：**AGREE**，但严重程度较低。
- **R2-W4（Table 1 可读性）**：**AGREE**，与我的小问题 #1 一致。
- **R2-W5（CJT 边界条件）**：**REBUT** — 论文通过 degenerate regime 和 intermediate-SC 分析已覆盖了实际相关的边界条件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1430 · 2026-05-22T08:01:53.042573+00:00_

审稿已全部完成。

**审稿报告已投递至 Research Director。**

**最终结果**：Overall 3.5 / 5（Borderline Conference），Soundness 4/5，Excitement 2.75/5。

**3 个 Must-Fix**：
1. 摘要 BR 4.97× 选择性报告（应报范围/中位数）
2. 统计功效 framing 不足（10/16 underpowered，power analysis 需提到正文）
3. α=0.5 无消融实验

**9 个 Should-Fix**：Discussion 过短、指标过载、NLI claim 须限定到命题逻辑、TOST margin 循环论证、语法去重可能膨胀 BR、Table 1 可读性、Symbolic Mirage 定位不一致、4-seed 充分性、TF-IDF 粒度粗。

**视觉审查**：主文约 8.05 页（溢出 3-4 行到 page 9），需压缩至严格 8 页内。

**Issue Tracker** 已同步更新（新增 R13-N1/N2/N3 + R13-W1~W5，更新 16 个历史 issue 的本轮 mention）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 95

## Round 95

76 recorded events


### User

_source line 1431 · 2026-05-22T13:16:37.401871+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: symb_invariant_consensus
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1432 · 2026-05-22T13:16:42.940792+00:00_

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
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1433 · 2026-05-22T13:16:42.991986+00:00_

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
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1434 · 2026-05-22T13:16:46.708643+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,WebSearch",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,WebSearch",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 1435 · 2026-05-22T13:16:46.709156+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1436 · 2026-05-22T13:16:52.797519+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 1437 · 2026-05-22T13:16:52.848109+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1438 · 2026-05-22T13:16:56.362448+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1439 · 2026-05-22T13:16:56.362951+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1440 · 2026-05-22T13:16:59.826203+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 1441 · 2026-05-22T13:17:00.765868+00:00_

{"result":"# 项目 symb_invariant_consensus 概况\n\n## 实验状态 (164 个)\n\n- **sica_k_sensitivity_14b**: DONE (success) — \n- **exp-011-llama8b**: DONE (failed) — \n- **exp-016-weighted-sc**: DONE (success) — \n- **exp-005**: DONE (negative) — \n- **sica_folio30**: DONE (killed) — \n- **sica_d016_c0_precheck**: DONE (success) — \n- **sica_proofwriter30_v2**: DONE (killed) — \n- **sica_proofwriter30**: DONE (failed) — \n- **sica_aime30_v3**: DONE (killed) — \n- **sica_aime30_v2**: DONE (killed) — \n- **sica_aime30_t07**: DONE (killed) — \n- **mvp_math50_t07**: DONE (killed) — \n- **sica_smoke_5q**: DONE (success) — \n- **smoke-test-5q**: PREPARING (failed) — \n- **crd_folio_main**: DONE (success) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-22T12:17:50Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 164 个实验 — DONE 148, PREPARING 16\n**DONE 分布**: failed 19, killed 12, negative 76, success 41\n\n### 💾 磁盘余量\n- **westd-25068**: ❌ 连接失败\n- **westd-16639**:\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\n  - `/init`: 150M/150M 可用（已用 1%）\n  - `/usr/bin/nvidia-smi`: 502G/879G 可用（已用 40%）\n\n### 🏃 RUNNING\n_（无）_\n\n### 📌 最近完成 (top 5)\n- `exp-folio-2x2-crossmodel` [success] — 2026-05-22T05:34:00\n- `exp-d126-70b-sica` [failed] — 2026-05-22T02:08:10 — startup recovery: RUNNING with no cron and no server/pid info\n- `exp-d126-crossmodel-sica` [success] — 2026-05-21T22:22:32 — N/A — cron false alarm, experiment completed successfully via workers (not train\n- `exp-text-ablation` [success] — 2026-05-21T18:07:10\n- `exp_text_ablation` [success] — 2026-05-21T06:41:41\n\n### 🔴 最近失败原因 (top 3)\n- `exp-d126-70b-sica`: startup recovery: RUNNING with no cron and no server/pid info\n\n&lt;!-- AUTO-FACTS-END -->\n\n---\n\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp-multi-seed-llama-folio（准备中）\n- exp-multi-seed-qwen25: Multi-seed replication (seeds 123,456,789) of Qwen2.5-14B × FOLIO-204 an
…[truncated 1758 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 939
}
```

</details>

---


### Tool call

_source line 1442 · 2026-05-22T13:17:01.217928+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1443 · 2026-05-22T13:17:02.272786+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % removed: not available in this TeX distribution
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\usepackage{tcolorbox}
14	\tcbuselibrary{skins}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{enumitem}
19	\usepackage{subcaption}
20	\usepackage{tikz}
21	\usetikzlibrary{arrows.meta,positioning,calc,fit}
22	\usepackage{listings}
23	\usepackage{algorithm}
24	\usepackage{algpseudocode}
25	\usepackage{hyperref}
26	\usepackage{cleveref}
27	
28	\lstset{
29	  basicstyle=\small\ttfamily,
30	  breaklines=true,
31	  frame=single,
32	  xleftmargin=1em,
33	  xrightmargin=1em,
34	  aboveskip=0.5em,
35	  belowskip=0.5em,
36	}
37	
38	\graphicspath{{../figures/paper/}{figures/}}
39	
40	\title{Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints\\Show No Evidence of Improving LLM Reasoning}
41	
42	\author{Anonymous}
43	
44	\begin{document}
45	\maketitle
46	
47	% Tighten spacing for 8-page budget
48	\setlength{\textfloatsep}{5pt plus 2pt minus 4pt}
49	\setlength{\dbltextfloatsep}{5pt plus 2pt minus 4pt}
50	\setlength{\floatsep}{3pt plus 2pt minus 2pt}
51	\setlength{\dblfloatsep}{3pt plus 2pt minus 2pt}
52	\setlength{\abovecaptionskip}{2pt}
53	\setlength{\belowcaptionskip}{0pt}
54	\setlength{\abovedisplayskip}{4pt plus 1pt minus 2pt}
55	\setlength{\belowdisplayskip}{4pt plus 1pt minus 2pt}
56	\setlength{\intextsep}{5pt plus 1pt minus 2pt}
57	
58	\input{abstract}
59	
60	\input{introduction}
61	
62	\input{related_work}
63	
64	\input{method}
65	
66	\input{experiments}
67	
68	\input{analysis}
69	
70	\input{solutions}
71	
72	\input{discussion}
73	
74	\vspace{-1mm}
75	\section*{Limitations}
76	\input{limitations_content}
77	
78	\bibliography{references}
79	
80	\appendix
81	\input
…[truncated 36 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 1444 · 2026-05-22T13:17:02.323926+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARR May 2026 call for papers submission guidelines site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ARR May 2026 call for papers submission guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1445 · 2026-05-22T13:17:02.626514+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1446 · 2026-05-22T13:17:07.158588+00:00_

Web search results for query: "ARR May 2026 call for papers submission guidelines site:aclweb.org"

Links: [{"title":"Call for Papers: ACL 2026 Workshop on Structured Understanding, Retrieval, and Generation in the LLM Era | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-acl-2026-workshop-structured-understanding-retrieval-and-generation-llm-era"},{"title":"The 1st Workshop on Retrieval Augmented Generation for Report Generation @ ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/1st-workshop-retrieval-augmented-generation-report-generation-acl-2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"EACL 2026 - Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-call-system-demonstrations"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Call for Papers - Workshop on AI for Scientific Research @ AAAI 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-workshop-ai-scientific-research-aaai-2026"}]

The search results show various ACL-related calls for papers and workshops, but they don't contain information about a specific "ARR May 2026 call for papers" submission guidelines. 

The results include several relevant references to ARR (the ACL Rolling Review system):

- References to the ARR CfP (Call for Papers) at https://aclrollingreview.org/cfp
- Pap
…[truncated 472 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 4834
}
```

</details>

---


### Tool result

_source line 1447 · 2026-05-22T13:17:07.209318+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'symb_invariant_consensus'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 4582
}
```

</details>

---


### Tool call

_source line 1448 · 2026-05-22T13:17:15.041403+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements"
  }
}
```

</details>

---


### Tool call

_source line 1449 · 2026-05-22T13:17:15.694472+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline ARR commitment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline ARR commitment"
  }
}
```

</details>

---


### Tool call

_source line 1450 · 2026-05-22T13:17:16.698493+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1451 · 2026-05-22T13:17:16.799307+00:00_

1	Self-Consistency (SC) majority voting over chain-of-thought traces saturates as sample count grows because same-model traces are correlated voters.
2	We investigate whether symbolic constraint extraction can break this plateau through Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from reasoning traces and selects answers via weighted partial MAX-SAT.
3	Across six open-source LLMs (7B--32B) on three logical reasoning domains with over 3,000 condition-evaluations (${\sim}$1,250 unique instances), we find no evidence of improvement (aggregate sign test: 5+/10$-$, $p = 0.30$; none of sixteen non-degenerate conditions shows a significant positive effect after FDR control), with equivalence established in four conditions, significant degradation in two, and ten remaining underpowered for effects below ${\sim}$5\,pp.
4	We trace the failure to \emph{symbolic confirmation bias} (SCB): on incorrect problems, 83.3\% of self-extracted constraints support the wrong majority answer (bias ratios ranging from $1.66\times$ to $4.97\times$), but a shuffle control shows this bias is structural---it reflects trace-count distributions rather than extraction-specific error ($\text{BR}_\text{obs} \approx \text{BR}_\text{null}$, $p > 0.7$). MAX-SAT produces answers identical to count-only aggregation on 94.4\% of problems, confirming that the formal verification layer adds no information beyond majority voting despite 99\% of constraints passing Z3 validation.
5	Cross-model extraction confirms SCB universality across nine models from 7B to frontier (BR $1.66$--$4.97\times$), though frontier models use cross-model rather than self-extraction.
6	Twenty-seven training-free remediation strategies spanning fifteen families all fail, confirming a persistent independence-accuracy trade-off.
7	Oracle controls confirm the aggregation mechanism is sound ($+29.90$\,pp, $+14.22$\,pp FOLIO, $+17.17$\,pp ProofWriter; $p < 0.001$); same-model self-extraction captur
…[truncated 281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1452 · 2026-05-22T13:17:16.850009+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1453 · 2026-05-22T13:17:16.850581+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time computation scaling through multiple reasoning samples has emerged as a practical alternative to scaling model parameters \citep{snell2025scaling, guo2025deepseekr1}.
4	The dominant aggregation strategy, Self-Consistency (SC) \citep{wang2023sc}, samples $K$ chain-of-thought traces and selects the majority answer.
5	SC is simple, model-agnostic, and effective---but it is hitting a ceiling.
6	\citet{loo2025reevaluating} demonstrate that gains from increasing $K$ plateau and even decline for strong models.
7	The gap between SC's theoretical promise (independent correct voters converge to truth) and its practical behavior (saturating gains) points to a structural mismatch: same-model traces carry correlated errors, and majority voting has no mechanism to correct shared bias.
8	
9	Confidence-weighted \citep{taubenfeld2025cisc} and universal \citep{chen2024usc} extensions alleviate this, but the core limitation persists.
10	Recent neuro-symbolic methods \citep{pan2023logiclm, olausson2023linc, xu2026dylos, li2025aristotle, wang2025fover, luo2025logicagent} report gains on logical reasoning but introduce components beyond the reasoning model.
11	A simpler question precedes these: can the \emph{same} model extract useful formal constraints from its own traces---a zero-cost upgrade requiring no additional model or data?
12	No prior work has systematically evaluated this.
13	
14	We ground our analysis in the Condorcet Jury Theorem (CJT) \citep{condorcet1785}: if $K$ independent voters each answer correctly with probability $p > 0.5$, the majority converges to truth \citep{austensmith1996}.
15	When independence fails \citep{ladha1992correlated}, additional samples carry diminishing information.
16	Measuring inter-trace agreement with Fleiss' $\kappa$ \citep{fleiss1971kappa}, we find $\kappa = 0.21$--$0.82$ across instruction-tuned conditions, yielding $K_{\text{eff}}$ as an ordinal diagnostic of vote diversity ($K
…[truncated 6387 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 1454 · 2026-05-22T13:17:22.033425+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline ARR commitment"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"}]

Based on the search results, here are the key details about EMNLP 2026's call for papers, submission deadline, and ARR commitment:

## Key Deadlines

The ARR submission deadline fo
…[truncated 1124 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 6338
}
```

</details>

---


### Tool result

_source line 1455 · 2026-05-22T13:17:22.385176+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

Based on the search results, here are the key ACL Rolling Review 2026 submission guidelines regarding page limits and format requirements:

## Page Limits

Short papers are limited to 4 content pages maximum, while long papers are limited to 8 content pages maximum. Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review versions of short papers may have up 
…[truncated 1010 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 7343
}
```

</details>

---


### Tool call

_source line 1456 · 2026-05-22T13:17:30.766792+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1457 · 2026-05-22T13:17:31.771084+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Self-Consistency and extensions.}
5	SC selects the most frequent answer across chain-of-thought traces \citep{wang2023sc}. Extensions include universal SC for free-form generation \citep{chen2024usc}, confidence weighting \citep{taubenfeld2025cisc}, diverse prompting with step-aware verification \citep{li2023diverse}, program-based vote filtering \citep{toh2024notallvotes}, and reasoning-aware filtering \citep{wan2024rasc, kim2026reasc}. \citet{loo2025reevaluating} show that SC gains plateau early; \citet{byerly2026selfconsistency} further analyze SC's limitations in mathematical reasoning. Alternative aggregation strategies beyond majority voting \citep{ai2025beyondmajority} have been proposed but do not address the underlying correlation problem. Our Condorcet analysis explains this: $\kappa = 0.21$--$0.82$ compresses $K_{\text{eff}}$ to 1.20--3.62 for $K = 12$ (\S\ref{sec:effective-k}).
6	
7	\paragraph{Neuro-symbolic reasoning.}
8	We distinguish three paradigms. \emph{Specification-generation} (Logic-LM \citep{pan2023logiclm}, LINC \citep{olausson2023linc}, SatLM \citep{ye2024satlm}) translates problem descriptions into formal specifications before any answer is generated; LINC documents ${\sim}$40\% translation errors even at this level. \emph{Program-generation} \citep{gao2023pal,chen2023program,lyu2023faithful} produces executable code from problem statements. Both paradigms access the problem before generating candidate answers. \emph{Trace-extraction} (this work) operates post-hoc on reasoning traces that already contain candidates, inheriting confirmation bias (\S\ref{sec:confirmation-bias}). SatLM provides a natural control: it succeeds because problem-level formalization precedes answer generation, whereas trace-level extraction cannot avoid contamination (\S\ref{sec:mirage}). Recent extensions \citep{ryu2025clover, xu2026dylos, li2025aristotle, wang2025fover, singh2026verge, luo2025logic
…[truncated 3646 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1458 · 2026-05-22T13:17:31.771463+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1459 · 2026-05-22T13:17:32.225271+00:00_

1	\section{Background \& Setup}
2	\label{sec:method}
3	
4	\subsection{Self-Consistency and the Condorcet Independence Assumption}
5	\label{sec:condorcet}
6	
7	Self-Consistency (SC) \citep{wang2023sc} samples $K$ reasoning traces and selects the majority answer. The Condorcet Jury Theorem (CJT) \citep{condorcet1785} guarantees that if $K$ independent voters are each correct with probability $p > 0.5$, the majority converges to truth as $K \to \infty$ \citep{austensmith1996}. LLM traces violate this independence: all $K$ samples come from the same model with only temperature as variation. Following \citet{ladha1992correlated} and the design-effect framework of \citet{kish1965survey}, we define effective sample size using Fleiss' $\kappa$ \citep{fleiss1971kappa} as proxy for intraclass correlation:
8	\begin{equation}
9	\label{eq:effk}
10	K_{\text{eff}} = \frac{K}{1 + (K - 1) \cdot \kappa}.
11	\end{equation}
12	In our experiments (\S\ref{sec:effective-k}), $\kappa$ ranges from 0.21 to 0.82 across instruction-tuned pairs (0.91 for thinking mode), yielding $K_{\text{eff}} \approx 1.2\text{--}3.6$ for $K = 12$. $K_{\text{eff}}$ should be interpreted as an ordinal diagnostic---ranking which conditions have genuine vote diversity---rather than as a literal effective sample size. Fleiss' $\kappa$ is a chance-corrected agreement measure, not identical to the ICC ($\rho$) in \citeauthor{kish1965survey}'s (\citeyear{kish1965survey}) original formula; we validated their monotonic relationship empirically (mean pairwise $r = 0.625$ across model families). This independence limitation motivates our investigation.
13	
14	\subsection{SICA Pipeline}
15	\label{sec:pipeline}
16	
17	Symbolic Invariant Consensus Aggregation (SICA) extends SC by extracting formal constraints from traces and selecting the answer best supported by the satisfiable subset (Figure~\ref{fig:pipeline}).
18	
19	\paragraph{Trace generation.} Given question $q$, an LLM generates $K$ traces $\{t_1, \ldots, t_K\}$ at 
…[truncated 5543 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1460 · 2026-05-22T13:17:32.225803+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1461 · 2026-05-22T13:17:33.179815+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	\label{sec:exp-setup}
6	
7	We evaluate SICA against Self-Consistency (SC) across six models, three reasoning domains, and over 3,000 condition-evaluations (${\sim}$1,250 unique instances), with diagnostic analyses of confirmation bias and process-level independence (\S\ref{sec:analysis}).
8	
9	\paragraph{Models.} Qwen2.5-14B-Instruct, Qwen2.5-7B-Instruct, Qwen3-14B (non-thinking mode)~\citep{yang2024qwen25}, Mistral-7B-Instruct-v0.3~\citep{jiang2023mistral}, LLaMA-3.1-8B-Instruct~\citep{dubey2024llama3}, and QwQ-32B~\citep{qwen2024qwq} (7B--32B). We additionally evaluate SCB universality via cross-model extraction on five frontier models (gpt-4o, gpt-4.1, gpt-5.5, o3, Gemini-2.5-Pro; Table~\ref{tab:frontier-scb}), where Mistral-7B extracts constraints from the target model's traces since closed-source APIs do not expose internals suitable for self-extraction.
10	
11	\paragraph{Datasets.} FOLIO~\citep{han2022folio} ($n{=}204$, with gold logical annotations), ProofWriter depth-5~\citep{tafjord2021proofwriter} ($n{=}600$), LogiQA~\citep{liu2020logiqa} ($n{=}200$). StrategyQA~\citep{geva2021strategyqa} ($n{=}200$) serves as a domain-formalizability diagnostic. GSM8K~\citep{cobbe2021gsm8k} ($n{=}30$) and AIME 2024 ($n{=}22$) probe the degenerate regime ($C_0 < 5\%$).
12	
13	\paragraph{Parameters.} $K{=}12$ traces at $T{=}0.7$, extraction at $T_{\text{ext}}{=}0.3$, $\alpha{=}0.5$, Z3 timeout 10s. McNemar exact test ($\alpha{=}0.05$); 95\% bootstrap CIs ($10{,}000$ resamples) for $n \geq 200$. SICA incurs $4.5{\times}$ SC wall-clock; extraction accounts for 76\% of overhead.
14	
15	
16	\subsection{Main Results}
17	\label{sec:main-results}
18	
19	Table~\ref{tab:main_results} reports accuracy across all conditions sorted by SC baseline, revealing three observation-driven accuracy regimes.
20	
21	\begin{table*}[t]
22	\centering
23	\small
24	\caption{SICA vs.\ SC across all conditions (sorted by SC). N
…[truncated 5163 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1462 · 2026-05-22T13:17:33.180218+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 1463 · 2026-05-22T13:17:33.632304+00:00_

1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\looseness=-1 We test the three predictions of the symbolic mirage hypothesis (\S\ref{sec:mirage}).
5	
6	\subsection{Condorcet Effective-K}
7	\label{sec:effective-k}
8	
9	\looseness=-1 Table~\ref{tab:independence} (Appendix) reports Fleiss' $\kappa$ and Effective-K (Eq.~\ref{eq:effk}) across 15 conditions at $K = 12$. Among instruction-tuned models, $\kappa$ ranges from 0.21 to 0.82, yielding $K_{\text{eff}} = 1.20\text{--}3.62$ as an ordinal diagnostic: higher $K_{\text{eff}}$ indicates greater vote diversity, though it should not be interpreted as a literal effective sample size (\S\ref{sec:condorcet}). Across four Mistral-7B seeds, $\kappa \in [0.41, 0.51]$ yet $\Delta$ ranges from $+3.43$ to $-0.49$\,pp, indicating seed-level constraint quality matters beyond independence. Positive $\Delta$ requires both sufficient $K_{\text{eff}}$ ($\leq 1.30$ never improves) and SC accuracy ($K_{\text{eff}} = 3.62$ with SC $= 39\%$ degrades). All four model families produce $\kappa \geq 0.41$ (Table~\ref{tab:kappa_generalization}).
10	
11	
12	\subsection{Symbolic Confirmation Bias}
13	\label{sec:confirmation-bias}
14	
15	\looseness=-1 Self-extracted constraints systematically align with the model's majority answer. On Mistral-7B FOLIO, when SICA errs, 83.3\% of constraints support the incorrect answer---bias ratio $4.97\times$ (Table~\ref{tab:cross-model-bias})---and 94\% of errors overlap with SC. A shuffle control reveals this bias is \emph{structural}: randomizing constraint--answer associations while preserving per-trace counts yields $\text{BR}_\text{null} \approx \text{BR}_\text{obs}$ ($p > 0.7$), indicating that BR reflects the trace-count distribution rather than extraction-specific error. Z3 rejects only 3.4\% of constraints, and MAX-SAT produces answers identical to count-only aggregation on 94.4\% of problems on Mistral-7B FOLIO (Table~\ref{tab:ablation}), confirming that the formal verification layer is vacuous (Eq.~
…[truncated 6036 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1464 · 2026-05-22T13:17:33.683179+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1465 · 2026-05-22T13:17:33.784137+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/decisions.yaml\", \"content\": \"_next_id: 148\\ndecisions:\\n- id: D001\\n  date: 2026-05-15 08:47 UTC\\n  summary: MVP 验证方案：50 题 MATH-500 分层子集，SICA vs SC@K=12\\n  rationale: SICA 核心价值取决于两个前提：(1) 能从推理 trace 可靠提取符号约束；(2) 跨路径矛盾率足够高（>5%）使形式化验证有意义。Reviewer\\n    给 impact 3/5，核心担忧是\\\"若矛盾率<5%则动机不成立\\\"。MVP 直接验证这两个前提，50 题按难度分层可同时观察 Extraction-Verification\\n    Paradox（难题提取差但矛盾多）。Pass 则进入全量实验冲 EMNLP/AAAI，Fail 则及时止损。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-15 08:52 UTC\\n  summary: 拒绝 CRD pivot，要求回归 SICA 原始方案\\n  rationale: Reviewer critical 审查发现 Agent 实施的是\\\"跨表征分歧诊断\\\"(CRD)，与 IDEA_BRIEF 定义的 SICA\\n    完全不同：CRD 用双表征（FOL+SymPy）做单解分歧检测，无多路径采样、无 MAX-SAT 共识——这正是 SICA 区别于 VERGE/D&P 的核心创新点。CRD\\n    的 novelty 定位与 VERGE 高度重叠（单输出验证+修复），无法支撑 EMNLP 投稿。同时 MVP 标准被静默替换，ROADMAP 的三条 pass\\n    criteria 从未测试。98GB GPU 完全能跑 QwQ-32B，无理由换 Qwen3-32B-AWQ。必须回归 SICA：K=12 多路径采样 →\\n    符号约束提取 → Z3 加权 partial MAX-SAT → 不变量共识打分。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-15 08:54 UTC\\n  summary: MVP 标准 v2：三档判定 + 矛盾绝对数 ≥5 + accuracy ≥SC+2pp + ProofWriter sanity check\\n  rationale: Reviewer warning 指出：(1) 5% 矛盾率阈值在 50 题上仅 2.5 题，置信区间极宽——改为绝对数 ≥5 题；(2)\\n    ≥SC+0.1pp 也过关无意义——改为 ≥2pp 或 p<0.1；(3) 灰色区间无处理——新增 Inconclusive 档，触发扩展到 100 题重测；(4)\\n    单域 MATH-500 不够——加 10 题 ProofWriter 做逻辑域 sanity check；(5) 模型不能模糊——固定 QwQ-32B，不可替换。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-15 12:02 UTC\\n  summary: MVP T=0.7 继续跑完（需要完整数据），diagnostic 自然结束后 GPU 带宽恢复；AIME 30 题排在 MVP 之后\\n  rationale: Temperature 诊断 4/5 题显示 T=0.7/0.9/1.0 均几乎不产生答案分歧——C2/C3 高风险 FAIL。但仍决定让\\n    MVP 跑完：(1) 50 题完整数据无论正负都有价值（负面结果=SICA 在强模型上无信号，本身是发现）；(2) GPU 已分配且无其他实验排队；(3)\\n    smoke test L5 有 3 条矛盾，50 题中 L4-5 有 20 题可能产生更多信号。MVP 完成后立即跑 AIME 30 题（QwQ-32B ~79.5%，分歧应更明显），作为\\\"高难度\\n    sweet
…[truncated 1463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1466 · 2026-05-22T13:17:42.278440+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex"
  }
}
```

</details>

---


### Tool result

_source line 1467 · 2026-05-22T13:17:43.282601+00:00_

1	\section{Cross-Architecture Proof-of-Concept}
2	\label{sec:solutions}
3	\label{sec:cross-arch}
4	
5	\paragraph{Method.}
6	\looseness=-1 We test with DeBERTa-large \citep{he2021deberta} (406M, encoder-only), fine-tuned on MultiNLI \citep{williams2018mnli}, classifying (premise, conclusion) pairs as entailment, contradiction, or neutral. This proof-of-concept is limited to propositional-logic benchmarks whose premise-conclusion structure naturally suits NLI; generalization to non-logical domains remains untested. In combo mode, each NLI-supporting vote counts $w$ times alongside SC's $K$ votes. We evaluate on Mistral-7B FOLIO ($n = 204$) and ProofWriter depth-5 ($n = 600$).
7	
8	\paragraph{Main result.}
9	\looseness=-1 DeBERTa NLI alone achieves 49.51\% on FOLIO (below SC's 55.88\%) and 55.00\% on ProofWriter (above SC's 39.33\%). On FOLIO ($n = 204$), combo $w{=}3$ yields $+2.94$\,pp (n.s.). On ProofWriter ($n = 600$), $w{=}3$ achieves $+6.67$\,pp ($p < 0.001$) and $w{=}5$ reaches $+11.00$\,pp ($p < 0.001$)---while same-model SICA \emph{degrades} ProofWriter ($-2.83$\,pp; Table~\ref{tab:main_results}), illustrating that corrective signal must originate outside the model's distribution (\S\ref{sec:mirage}). After BH correction ($m{=}12$), only Mistral-7B ProofWriter conditions ($w{=}3$, $w{=}5$) remain significant.
10	
11	\paragraph{Why it works.}
12	\looseness=-1 Three conditions jointly enable the escape---structural independence, positive capability gap, and task-verifier alignment---expanded as design principles in \S\ref{sec:discussion}. Per-label analysis confirms NLI and SC excel on complementary labels (Appendix~\ref{app:multi-nli}); all three NLI architectures produce gains at $w \geq 3$.
13	
14	\paragraph{Capability gap hypothesis.}
15	\looseness=-1 Four generators spanning a 46-point SC range on ProofWriter ($n{=}600$), all paired with DeBERTa-large-mnli (55.00\% standalone; Table~\ref{tab:cross_generator_nli}): only Mistral-7B (SC 39.33\%, below the veri
…[truncated 1367 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1468 · 2026-05-22T13:17:43.283069+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1469 · 2026-05-22T13:17:43.734956+00:00_

1	\enlargethispage{6\baselineskip}
2	\section{Discussion and Conclusion}
3	\label{sec:discussion}
4	\label{sec:conclusion}
5	
6	\paragraph{Practitioner decision framework.}
7	\looseness=-1 Three zero-cost diagnostics predict self-verification failure before deployment. $K_\text{eff} \leq 1.3$: in our experiments, no condition improves ($\Delta \in [0.00, -0.98]$\,pp across four conditions; Table~\ref{tab:independence}). When SC falls below ${\sim}40\%$, constraints amplify errors ($-2.83$\,pp on Mistral-7B ProofWriter). $C_0 < 5\%$: near-unanimous traces reduce any aggregation to majority voting by construction. Only the intermediate regime (SC $\sim$50--60\%, $K_\text{eff} > 1.8$) offers marginal gain; practitioners should compute these before investing in symbolic reasoning.
8	
9	\paragraph{SCB beyond SICA.}
10	\looseness=-1 SCB extends to any method extracting structured representations from a model's own outputs---self-verification \citep{huang2024selfcorrect}, self-refinement \citep{madaan2023selfrefine}, and chain-of-verification \citep{dhuliawala2023chainofverification} all face the same distributional prior. Our debate control ($\kappa = 0.15$, $-18.6$\,pp) confirms that independence and quality are at odds under same-model constraints.
11	
12	\paragraph{Design principles for escaping SCB.}
13	\looseness=-1 The cross-architecture escape (\S\ref{sec:cross-arch}) identifies three necessary conditions: (i)~\emph{structural independence}---no shared architecture or training data; (ii)~\emph{positive capability gap}---the verifier's adjusted contribution exceeds the generator's SC; (iii)~\emph{task-verifier alignment}---the verification paradigm matches task structure. These explain why 27 same-model interventions fail ($\kappa \geq 0.40$) while a 406M encoder succeeds ($+11.00$\,pp). Trained extractors capturing $>$12\% of the oracle ceiling ($+29.90$\,pp) are the most promising direction (Appendix~\ref{app:extended-discussion}). Formal self-verification creates
…[truncated 212 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1470 · 2026-05-22T13:17:43.785611+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex"
  }
}
```

</details>

---


### Tool result

_source line 1471 · 2026-05-22T13:17:44.187490+00:00_

1	\looseness=-1 Open-source models range from 7B to 32B parameters with self-extraction; frontier models confirm SCB universality but use cross-model extraction via Mistral-7B, as closed-source APIs do not expose internals---whether self-extraction on frontier models would yield different BR values remains untested. All datasets are English-language logical reasoning benchmarks; we do not evaluate trained symbolic extractors, multilingual settings, or commonsense domains lacking gold annotations. NLI verification was tested only on propositional/first-order logic tasks; generalization to non-logical reasoning domains remains untested. Syntactic deduplication (46.0\% removal rate) may retain semantically equivalent constraints; however, the shuffle control (\S\ref{sec:confirmation-bias}) preserves the same duplication pattern and yields $\text{BR}_\text{shuffle} \approx \text{BR}_\text{obs}$, suggesting deduplication granularity does not drive the observed bias direction. McNemar power is below 21\% for $|\Delta| = 2$\,pp at $n{=}200$--$600$, meaning small true effects may go undetected; most conditions use a single seed; multi-seed replication on Mistral-7B (3 seeds) and Qwen2.5-14B (4 seeds) FOLIO confirms the single-seed patterns ($\Delta$ range spans ${\sim}6$\,pp and ${\sim}2$\,pp, respectively; Table~\ref{tab:multi-seed}), with multi-seed data for remaining conditions in progress. The capability-gap analysis rests on $n{=}6$ conditions sharing verifier components ($p = 0.167$ after collapsing); we characterize it as a consistent pattern rather than a confirmed law. SICA requires $4.5\times$ the wall-clock time of SC with no significant accuracy gain. Extended limitations are discussed in Appendix~\ref{app:limitations-extended}.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1472 · 2026-05-22T13:17:44.689763+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 1473 · 2026-05-22T13:17:45.593865+00:00_

1	\section{Regime Scatter Plot}
2	\label{app:regime-scatter}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{f2_regime_scatter}
7	\caption{SICA $\Delta$ (pp) vs.\ SC baseline. Filled: $n \geq 100$; open: $n < 100$. The intermediate-SC region (50--60\%, shaded) contains the only positive trends (none reaching $p < 0.05$). Type~C: nominally significant degradation (raw $p = 0.014$; BH adj.\ $p = 0.112$).}
8	\label{fig:regime-scatter}
9	\end{figure}
10	
11	\section{Prompt Templates}
12	\label{app:prompts}
13	
14	SICA uses domain-specific prompt templates for constraint extraction: one for mathematical reasoning (GSM8K, AIME) and one for logical reasoning (ProofWriter, FOLIO). Both share the same system prompt. The LLM is called with temperature $T{=}0.3$, max tokens $1024$, and structured JSON output mode. Up to 6 traces are processed in parallel via thread pooling, with 2 retries on failure (exponential backoff, base 0.5s).
15	
16	\paragraph{System Prompt.}
17	
18	\begin{lstlisting}
19	You are a constraint extraction tool. Output ONLY
20	valid JSON. Do NOT solve problems, reason about
21	correctness, or think step-by-step. Extract
22	constraints from the given trace exactly as stated.
23	\end{lstlisting}
24	
25	\paragraph{Mathematical Constraint Extraction (EXTRACTION\_PROMPT).}
26	
27	Used for GSM8K and AIME datasets. The placeholder \texttt{\{trace\}} is replaced with the reasoning trace at runtime.
28	
29	\begin{lstlisting}
30	Extract mathematical constraints from this reasoning
31	trace as a JSON object.
32	
33	Rules:
34	- type: "equation", "inequality", or "predicate"
35	- expression: human-readable, e.g. "x + y == 14"
36	- z3_formula: a single comparison expression in
37	  Python Z3 syntax
38	- source_step: step number where the constraint
39	  appears
40	- Use variable names from the trace
41	
42	z3_formula MUST follow these rules:
43	- Allowed operators: ==, !=, <, >, <=, >=, +, -, *,
44	  /, **, %
45	- Use individual named variables
…[truncated 3308 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 1474 · 2026-05-22T13:17:45.694714+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/project_config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/project_config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 1475 · 2026-05-22T13:17:45.847197+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 1476 · 2026-05-22T13:17:52.000050+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/ -name \"project_config*\" -o -name \"config*\" 2>/dev/null | head -10",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/ -name \"project_config*\" -o -name \"config*\" 2>/dev/null | head -10",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 1477 · 2026-05-22T13:17:52.953744+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 1478 · 2026-05-22T13:17:53.104748+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "offset": "150",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
    "offset": "150",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1479 · 2026-05-22T13:17:53.155561+00:00_

150	\end{lstlisting}
151	
152	\paragraph{Prompt Selection Logic.}
153	
154	Domain assignment is determined by dataset: FOLIO and ProofWriter use \textsc{Logic\_Extraction\_Prompt}; GSM8K, AIME, StrategyQA, and ARC-Challenge use \textsc{Extraction\_Prompt}. StrategyQA and ARC-Challenge are assigned to the mathematical prompt because their reasoning structure does not involve formal logic predicates or implications, despite StrategyQA producing boolean answers.
155	
156	
157	\section{Z3 MaxSAT Evaluation Pseudocode}
158	\label{app:z3-pseudocode}
159	
160	Algorithm~\ref{alg:maxsat} describes the Z3 MaxSAT solving procedure. Algorithm~\ref{alg:scorer} describes the source-trace attribution scoring.
161	
162	Domain constraint variables (e.g., \texttt{x + y == 14}) and answer assertion variables (e.g., \texttt{\_\_sica\_answer\_42 == True}) are logically independent in the Z3 formulation. Discriminative signal arises solely from conflicts among domain constraints: when traces supporting different answers produce mutually contradictory constraints, the solver excludes the lower-weight subset, and the scorer penalizes the corresponding answers.
163	
164	\begin{algorithm}[h]
165	\caption{Z3 Weighted Partial MAX-SAT}
166	\label{alg:maxsat}
167	\begin{algorithmic}[1]
168	\Require Deduplicated constraint set $\mathcal{C} = \{(c_m, w_m, S_m)\}_{m=1}^M$ where $c_m$ is a Z3 formula, $w_m$ is weight, $S_m$ is the set of source trace indices
169	\Ensure Partition $(\mathcal{C}^*, \mathcal{C}^{\setminus})$ where $\mathcal{C}^*$ is the max-weight satisfiable subset
170	\State $\textit{opt} \gets \textsc{Z3.Optimize()}$
171	\For{$m = 1, \ldots, M$}
172	    \State $b_m \gets$ fresh Boolean indicator
173	    \State $\textit{opt}.\textsc{Add}(b_m \Rightarrow c_m)$ \Comment{soft clause guarded by indicator}
174	    \State $\textit{opt}.\textsc{AddSoft}(b_m,\; \text{weight}=w_m)$
175	\EndFor
176	\State $\textit{result} \gets \textit{opt}.\textsc{Check}()$
177	\State $\textit{model} \gets \t
…[truncated 12910 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1480 · 2026-05-22T13:18:07.419218+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/ -name \"*.yaml\" -path \"*/agent/*\" 2>/dev/null | head -10",
  "description": "Find agent config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/ -name \"*.yaml\" -path \"*/agent/*\" 2>/dev/null | head -10",
    "description": "Find agent config files"
  }
}
```

</details>

---


### Tool result

_source line 1481 · 2026-05-22T13:18:07.821502+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1482 · 2026-05-22T13:18:08.075513+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1483 · 2026-05-22T13:18:09.079097+00:00_

1	% References for SICA paper
2	% Generated from literature_map.yaml — 2026-05-17
3	
4	%%% SAT-Based Reasoning %%%
5	
6	@inproceedings{ye2024satlm,
7	  title={SatLM: Satisfiability-Aided Language Models Using Declarative Prompting},
8	  author={Ye, Xi and Chen, Qiaochu and Dillig, Isil and Durrett, Greg},
9	  booktitle={Advances in Neural Information Processing Systems},
10	  volume={36},
11	  year={2024}
12	}
13	
14	%%% Program-Aided Reasoning %%%
15	
16	@inproceedings{gao2023pal,
17	  title={{PAL}: Program-aided Language Models},
18	  author={Gao, Luyu and Madaan, Aman and Zhou, Shuyan and Alon, Uri and Liu, Pengfei and Yang, Yiming and Callan, Jamie and Neubig, Graham},
19	  booktitle={Proceedings of the 40th International Conference on Machine Learning (ICML)},
20	  year={2023}
21	}
22	
23	@article{chen2023program,
24	  title={Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks},
25	  author={Chen, Wenhu and Ma, Xueguang and Wang, Xinyi and Cohen, William W.},
26	  journal={Transactions on Machine Learning Research},
27	  year={2023}
28	}
29	
30	@inproceedings{lyu2023faithful,
31	  title={Faithful Chain-of-Thought Reasoning},
32	  author={Lyu, Qing and Havaldar, Shreya and Stein, Adam and Zhang, Li and Rao, Delip and Wong, Eric and Apidianaki, Marianna and Callison-Burch, Chris},
33	  booktitle={Proceedings of the 13th International Joint Conference on Natural Language Processing and the 3rd Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics},
34	  year={2023}
35	}
36	
37	%%% Theoretical Foundations %%%
38	
39	@book{condorcet1785,
40	  title={Essai sur l'application de l'analyse \`a la probabilit\'e des d\'ecisions rendues \`a la pluralit\'e des voix},
41	  author={de Condorcet, Marie Jean Antoine Nicolas de Caritat},
42	  year={1785},
43	  publisher={Imprimerie Royale},
44	  address={Paris}
45	}
46	
47	@article{austensmith1996,
48	  title={Information Aggregation, Rationality
…[truncated 143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 1003
}
```

</details>

---


### Tool call

_source line 1484 · 2026-05-22T13:18:09.181035+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_11/submitted.pdf 2>/dev/null && echo \"PDF exists\" || echo \"PDF not found\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_11/submitted.pdf 2>/dev/null && echo \"PDF exists\" || echo \"PDF not found\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1485 · 2026-05-22T13:18:09.334289+00:00_

-rw-r--r-- 1 ubuntu ubuntu 648790 May 22 13:09 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_11/submitted.pdf
PDF exists

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 1486 · 2026-05-22T13:18:16.452266+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/ -name \"project_config*\" -o -name \"config.yaml\" 2>/dev/null | head -10",
  "description": "Search for project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/ -name \"project_config*\" -o -name \"config.yaml\" 2>/dev/null | head -10",
    "description": "Search for project config file"
  }
}
```

</details>

---


### Tool result

_source line 1487 · 2026-05-22T13:18:16.954555+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1488 · 2026-05-22T13:18:17.155602+00:00_

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
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
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

_source line 1489 · 2026-05-22T13:18:17.206253+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1490 · 2026-05-22T13:18:20.180078+00:00_

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
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
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

_source line 1491 · 2026-05-22T13:18:20.230720+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1492 · 2026-05-22T13:18:27.962040+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/ -maxdepth 2 -name \"*.yaml\" -path \"*config*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/ -name \"*.yaml\" -not -path \"*/artifacts/*\" -not -path \"*decisions*\" -not -path \"*review_issues*\" 2>/dev/null | head -20",
  "description": "Find config yaml files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/ -maxdepth 2 -name \"*.yaml\" -path \"*config*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/ -name \"*.yaml\" -not -path \"*/artifacts/*\" -not -path \"*decisions*\" -not -path \"*review_issues*\" 2>/dev/null | head -20",
    "description": "Find config yaml files"
  }
}
```

</details>

---


### Tool result

_source line 1493 · 2026-05-22T13:18:28.062799+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/resources.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/qi2025symbolic_provers.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/aristotle2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/rc2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/pan2023logiclm.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/llm_meets_cp2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/multi_path_plan2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/dissecting2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/olausson2023linc.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/khan2024debating.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/chen2024usc.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/li2023diverse.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/huang2024selfcorrect.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/crest2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/distill_tmp/h
…[truncated 690 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1494 · 2026-05-22T13:18:33.733981+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/*.yaml 2>/dev/null | head -10; echo \"---\"; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/ --include=\"*.yaml\" 2>/dev/null | head -10",
  "description": "Search for external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/*.yaml 2>/dev/null | head -10; echo \"---\"; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/ --include=\"*.yaml\" 2>/dev/null | head -10",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 1495 · 2026-05-22T13:18:33.834991+00:00_

---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1496 · 2026-05-22T13:18:40.812170+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/ 2>/dev/null; echo \"---\"; ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null || echo \"No review_issues.yaml\"",
  "description": "Check existing review reports and issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/ 2>/dev/null; echo \"---\"; ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null || echo \"No review_issues.yaml\"",
    "description": "Check existing review reports and issues"
  }
}
```

</details>

---


### Tool result

_source line 1497 · 2026-05-22T13:18:41.214072+00:00_

total 200
drwxr-xr-x  2 ubuntu ubuntu  4096 May 22 08:01 .
drwxr-xr-x 59 ubuntu ubuntu 12288 May 22 13:16 ..
-rw-r--r--  1 ubuntu ubuntu 11085 May 17 17:54 round_0.md
-rw-r--r--  1 ubuntu ubuntu 13704 May 18 01:49 round_1.md
-rw-r--r--  1 ubuntu ubuntu 16183 May 22 08:01 round_10.md
-rw-r--r--  1 ubuntu ubuntu 11519 May 19 05:12 round_2.md
-rw-r--r--  1 ubuntu ubuntu 17577 May 20 13:21 round_3.md
-rw-r--r--  1 ubuntu ubuntu 17871 May 20 15:17 round_4.md
-rw-r--r--  1 ubuntu ubuntu 15543 May 20 20:08 round_5.md
-rw-r--r--  1 ubuntu ubuntu 14354 May 21 01:59 round_6.md
-rw-r--r--  1 ubuntu ubuntu 13998 May 21 06:51 round_7.md
-rw-r--r--  1 ubuntu ubuntu 16747 May 21 08:03 round_8.md
-rw-r--r--  1 ubuntu ubuntu 18698 May 22 01:20 round_9.md
---
-rw-r--r-- 1 ubuntu ubuntu 21454 May 22 08:08 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1498 · 2026-05-22T13:18:41.615983+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/*.tex 2>/dev/null",
  "description": "Count lines per tex file to estimate page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/*.tex 2>/dev/null",
    "description": "Count lines per tex file to estimate page count"
  }
}
```

</details>

---


### Tool result

_source line 1499 · 2026-05-22T13:18:41.667051+00:00_

     8 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex
    72 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex
  1179 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex
     4 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex
   160 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex
    13 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex
    74 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex
    76 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex
     1 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex
    83 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex
    68 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex
    14 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex
    35 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex
  1787 total

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1500 · 2026-05-22T13:19:27.221582+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "text": "你是 Reviewer 1，负责审查**方法严谨性、实验设计、统计分析**。\n\n## 论文信息\n- **标题**: Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Show No Evidence of Improving LLM Reasoning\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex`（入口文件，通过 `\\input{}` 引用各章节）\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_11/submitted.pdf`\n- **目标 Venue**: EMNLP 2026（ARR May 2026 cycle）\n- **Deadline**: 2026-05-25\n\n## Venue 格式要求\n- 长文：8 页正文 + 无限参考文献页\n- Limitations 和 Ethics 不计入页数限制\n- ACL 模板（`\\usepackage[review]{acl}`）\n- Double-blind 匿名审稿\n- Overall Assessment 评分：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n## 你的审查侧重\n\n1. **方法设计**：\n   - SICA pipeline 是否设计合理？MAX-SAT 公式化是否正确？\n   - Symbolic Mirage Hypothesis 的三个 predictions 是否可被本文实验充分检验？\n   - Condorcet 框架的 K_eff 诊断是否严谨（Fleiss κ → ICC 的近似是否有充分讨论）？\n   - 评分公式（Eq.3）和退化条件（Eq.4）的推导是否完备？\n\n2. **实验设计**：\n   - 模型覆盖（7B-32B + frontier）、数据集选择（FOLIO/ProofWriter/LogiQA）是否充分？\n   - 超参数选择（K=12, T=0.7, T_ext=0.3, α=0.5）是否合理并有敏感性分析？\n   - Oracle control 的设计是否有效证明了 mechanism soundness？\n   - 27 种 remediation strategies 的选取是否全面、分类是否合理？\n\n3. **统计分析**：\n   - McNemar exact test + BH FDR correction 是否恰当？\n   - TOST equivalence test 的 margin（±2pp）选择是否有充分依据？\n   - Power analysis 的 MDE 和 observed power 是否正确报告？\n   - Bootstrap CI 与 McNemar 结果是否一致？\n   - Sign test 的使用是否恰当（aggregate 5+/10-）？\n   - Multi-seed replication（3-seed, 4-seed）是否足以论证 reproducibility？\n\n4. **Cross-architecture 实验**：\n   - DeBERTa NLI proof-of-concept 的实验设计是否有说服力？\n   - Capability gap hypothesis 的验证是否充分（仅 n=6 conditions）？\n   - CCR 指标的定义和使用是否合理？\n\n5. **页数合规性**：检查正文是否在 8 页限制内。\n\n请给出完整审稿报告，包括 Summary、Strengths（逐条）、Weaknesses（逐条，标注 severity: critical/major/minor）、Questions、Missing References、Overall Assessment（按 EMNLP 2026 评分标准打分）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "symb_invariant_consensus",
    "text": "你是 Reviewer 1，负责审查**方法严谨性、实验设计、统计分析**。\n\n## 论文信息\n- **标题**: Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Show No Evidence of Improving LLM Reasoning\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex`（入口文件，通过 `\\input{}` 引用各章节）\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_11/submitted.pdf`\n- **目标 Venue**: EMNLP 2026（ARR May 2026 cycle）\n- **Deadline**: 2026-05-25\n\n## Venue 格式要求\n- 长文：8 页正文 + 无限参考文献页\n- Limitations 和 Ethics 不计入页数限制\n- ACL 模板（`\\usepackage[review]{acl}`）\n- Double-blind 匿名审稿\n- Overall Assessment 评分：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n## 你的审查侧重\n\n1. **方法设计**：\n   - SICA pipeline 是否设计合理？MAX-SAT 公式化是否正确？\n   - Symbolic Mirage Hypothesis 的三个 predictions 是否可被本文实验充分检验？\n   - Condorcet 框架的 K_eff 诊断是否严谨（Fleiss κ → ICC 的近似是否有充分讨论）？\n   - 评分公式（Eq.3）和退化条件（Eq.4）的推导是否完备？\n\n2. **实验设计**：\n   - 模型覆盖（7B-32B + frontier）、数据集选择（FOLIO/ProofWriter/LogiQA）是否充分？\n   - 超参数选择（K=12, T=0.7, T_ext=0.3, α=0.5）是否合理并有敏感性分析？\n   - Oracle control 的设计是否有效证明了 mechanism soundness？\n   - 27 种 remediation strategies 的选取是否全面、分类是否合理？\n\n3. **统计分析**：\n   - McNemar exact test + BH FDR correction 是否恰当？\n   - TOST equivalence test 的 margin（±2pp）选择是否有充分依据？\n   - Power analysis 的 MDE 和 observed power 是否正确报告？\n   - Bootstrap CI 与 McNemar 结果是否一致？\n   - Sign test 的使用是否恰当（aggregate 5+/10-）？\n   - Multi-seed replication（3-seed, 4-seed）是否足以论证 reproducibility？\n\n4. **Cross-architecture 实验**：\n   - DeBERTa NLI proof-of-concept 的实验设计是否有说服力？\n   - Capability gap hypothesis 的验证是否充分（仅 n=6 conditions）？\n   - CCR 指标的定义和使用是否合理？\n\n5. **页数合规性**：检查正文是否在 8 页限制内。\n\n请给出完整审稿报告，包括 Summary、Strengths（逐条）、Weaknesses（逐条，标注 severity: critical/major/minor）、Questions、Missing References、Overall Assessment（按 EMNLP 2026 评分标准打分）。"
  }
}
```

</details>

---


### Tool result

_source line 1501 · 2026-05-22T13:19:46.852959+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19631
}
```

</details>

---


### Tool call

_source line 1502 · 2026-05-22T13:19:46.953624+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "text": "你是 Reviewer 2，负责审查**新颖性、完整性、Related Work 覆盖、写作质量**。\n\n## 论文信息\n- **标题**: Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Show No Evidence of Improving LLM Reasoning\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex`（入口文件，通过 `\\input{}` 引用各章节）\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_11/submitted.pdf`\n- **目标 Venue**: EMNLP 2026（ARR May 2026 cycle）\n- **Deadline**: 2026-05-25\n\n## Venue 格式要求\n- 长文：8 页正文 + 无限参考文献页\n- Limitations 和 Ethics 不计入页数限制\n- ACL 模板（`\\usepackage[review]{acl}`）\n- Double-blind 匿名审稿\n- Overall Assessment 评分：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n## 你的审查侧重\n\n1. **新颖性评估**：\n   - 负面结果的贡献度：SCB 的发现是否足够 novel？相对于 Huang et al. (2024) self-correction、Stechly et al. (2025) self-verification 已知的 negative results，本文增量贡献是什么？\n   - K_eff / BR / C_0 三个诊断工具的 novelty：是否只是已有概念（Condorcet、ensemble diversity）的直接应用？\n   - Symbolic Mirage Hypothesis 是否真的是一个 hypothesis 还是一个对已知现象的重新表述？\n   - Cross-architecture escape 是否足够新颖（vs. 已有的 multi-agent / ensemble diversity 工作）？\n\n2. **Related Work 覆盖**：\n   - 是否遗漏了重要的相关工作？特别是：\n     - 2025-2026 年的 neuro-symbolic reasoning 新进展\n     - LLM self-correction / self-verification 的最新研究\n     - Ensemble diversity / correlated voting 的经典文献\n     - Test-time compute scaling 的最新进展\n   - 与 Logic-LM、LINC、SatLM 的区分是否清晰？\n   - 是否有过度引用或引用不足？\n\n3. **论文完整性**：\n   - 叙事结构是否连贯（从 SC plateau → SICA 尝试 → SCB 发现 → remediation 失败 → cross-arch escape）？\n   - Abstract 是否准确反映了论文内容？\n   - Contributions 是否过度 claim 或 under-claim？\n   - Limitations 是否覆盖了关键弱点？\n   - Discussion 是否有足够的 forward-looking insights？\n\n4. **写作质量**：\n   - 英语是否流畅、学术？\n   - 术语是否一致（SCB、symbolic mirage、bias ratio 等概念首次出现时是否定义清晰）？\n   - 图表是否清晰、信息量充足？Figure 1 pipeline 图是否有效？Table 1 是否直观？\n   - 信息密度是否合适（8 页限制下是否过于拥挤或有冗余）？\n\n5. **格式合规**：\n   - 匿名性：检查是否有任何泄露作者身份的信息（self-citation、acknowledgments、代码链接等）\n   - 引用格式是否一致（natbib）\n   - 是否有 orphan references 或 undefined references\n\n请给出完整审稿报告，包括 Summary、Strengths（逐条）、Weaknesses（逐条，标注 severity: critical/major/minor）、Questions、Missing References、Overall Assessment（按 EMNLP 2026 评分标准打分）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "symb_invariant_consensus",
    "text": "你是 Reviewer 2，负责审查**新颖性、完整性、Related Work 覆盖、写作质量**。\n\n## 论文信息\n- **标题**: Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Show No Evidence of Improving LLM Reasoning\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex`（入口文件，通过 `\\input{}` 引用各章节）\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_11/submitted.pdf`\n- **目标 Venue**: EMNLP 2026（ARR May 2026 cycle）\n- **Deadline**: 2026-05-25\n\n## Venue 格式要求\n- 长文：8 页正文 + 无限参考文献页\n- Limitations 和 Ethics 不计入页数限制\n- ACL 模板（`\\usepackage[review]{acl}`）\n- Double-blind 匿名审稿\n- Overall Assessment 评分：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n## 你的审查侧重\n\n1. **新颖性评估**：\n   - 负面结果的贡献度：SCB 的发现是否足够 novel？相对于 Huang et al. (2024) self-correction、Stechly et al. (2025) self-verification 已知的 negative results，本文增量贡献是什么？\n   - K_eff / BR / C_0 三个诊断工具的 novelty：是否只是已有概念（Condorcet、ensemble diversity）的直接应用？\n   - Symbolic Mirage Hypothesis 是否真的是一个 hypothesis 还是一个对已知现象的重新表述？\n   - Cross-architecture escape 是否足够新颖（vs. 已有的 multi-agent / ensemble diversity 工作）？\n\n2. **Related Work 覆盖**：\n   - 是否遗漏了重要的相关工作？特别是：\n     - 2025-2026 年的 neuro-symbolic reasoning 新进展\n     - LLM self-correction / self-verification 的最新研究\n     - Ensemble diversity / correlated voting 的经典文献\n     - Test-time compute scaling 的最新进展\n   - 与 Logic-LM、LINC、SatLM 的区分是否清晰？\n   - 是否有过度引用或引用不足？\n\n3. **论文完整性**：\n   - 叙事结构是否连贯（从 SC plateau → SICA 尝试 → SCB 发现 → remediation 失败 → cross-arch escape）？\n   - Abstract 是否准确反映了论文内容？\n   - Contributions 是否过度 claim 或 under-claim？\n   - Limitations 是否覆盖了关键弱点？\n   - Discussion 是否有足够的 forward-looking insights？\n\n4. **写作质量**：\n   - 英语是否流畅、学术？\n   - 术语是否一致（SCB、symbolic mirage、bias ratio 等概念首次出现时是否定义清晰）？\n   - 图表是否清晰、信息量充足？Figure 1 pipeline 图是否有效？Table 1 是否直观？\n   - 信息密度是否合适（8 页限制下是否过于拥挤或有冗余）？\n\n5. **格式合规**：\n   - 匿名性：检查是否有任何泄露作者身份的信息（self-citation、acknowledgments、代码链接等）\n   - 引用格式是否一致（natbib）\n   - 是否有 orphan references 或 undefined references\n\n请给出完整审稿报告，包括 Summary、Strengths（逐条）、Weaknesses（逐条，标注 severity: critical/major/minor）、Questions、Missing References、Overall Assessment（按 EMNLP 2026 评分标准打分）。"
  }
}
```

</details>

---


### Tool call

_source line 1503 · 2026-05-22T13:19:48.315384+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "symb_invariant_consensus",
  "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
  }
}
```

</details>

---


### Tool result

_source line 1504 · 2026-05-22T13:19:48.574621+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1620
}
```

</details>

---


### Tool result

_source line 1505 · 2026-05-22T13:19:50.503708+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 2188
}
```

</details>

---


### Assistant

_source line 1506 · 2026-05-22T13:19:57.039564+00:00_

Round 1 已启动：

- **Reviewer 1**（方法/实验/统计）：已派发 ✓
- **Reviewer 2**（新颖性/完整性/Related Work/写作）：已派发 ✓
- **视觉审查 Agent**：已启动（并行，不阻塞）✓
- **外部审稿**：未配置，跳过

等待两位 Reviewer 返回独立审稿报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 96

## Round 96

2 recorded events


### User

_source line 1507 · 2026-05-22T13:26:45.861998+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告（Round 1）

**论文**: Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Show No Evidence of Improving LLM Reasoning
**审查侧重**: 新颖性、完整性、Related Work 覆盖、写作质量

---

## 总体评分
**Overall**: 3.5 / 5（Borderline Conference）
**一句话总结**: 实验方法严谨、诊断框架有实用价值，但核心负面发现的新颖性有限——self-extracted constraints 继承模型偏差这一结论在已有 self-correction 文献下是可预见的，且 8 页内容过于拥挤导致关键贡献展开不充分。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 实验设计非常严谨（6模型×3数据集、FDR校正、TOST等价检验、功效分析），但部分结论的 claim scope 超出了统计证据支撑范围 |
| Excitement | 2.5/5 | 核心发现（self-extracted constraints 继承模型偏差）在 Huang et al. (2024)、Stechly et al. (2025) 已知结论下可预见性较高；诊断工具有实用价值但概念新颖性有限 |
| Reproducibility | 4/5 | 提供了完整 prompt templates（Appendix B）、pseudocode（Algorithm 1-2）、超参数细节；缺少代码/数据发布承诺 |
| Confidence | 4/5 | 该领域是我的研究方向之一，仔细阅读了全文及附录 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Symbolic Mirage Hypothesis 的新颖性不足——更像是对已知现象的重新包装
- 具体位置：Section 3.3, Section 7 (p.4, p.8)
- 问题：论文将"self-extracted constraints inherit the generating model's distributional biases"包装为"Symbolic Mirage Hypothesis"并作为核心贡献之一。然而，Huang et al. (2024, TACL survey) 已系统论证 LLM 无法在无外部反馈下自我纠正推理错误；Stechly et al. (2025) 在 self-verification 场景下也得出了类似负面结论。本文的发现本质上是同一原理在 symbolic constraint extraction 这一具体场景下的又一实例。Section 3.3 的 BR（Bias Ratio）本身只是"constraints 对错误答案的支持比例"的简单度量。论文声称 "No prior work has systematically evaluated this"（p.1），但 self-correction 文献已从多个角度覆盖了这一问题。
- 为什么影响接收：作为论文三个核心贡献之一（Contribution #3），如果 Symbolic Mirage 只是已知原理的重新表述，论文的整体新颖性大幅降低。
- 建议：(1) 明确区分本文发现与 Huang et al. 的增量贡献——在 symbolic/formal 这一被认为可能打破 self-correction 局限的特殊场景下的验证；(2) 降低"Hypothesis"措辞，改为"empirical finding"或"diagnostic pattern"；(3) 讨论为什么 symbolic extraction 被预期能不同于一般 self-correction，以及为什么这一预期失败是非平凡的。

**N2** [critical] 8 页正文信息过载，关键贡献展开严重不足
- 具体位置：Section 5.5 (p.7), Section 6 (p.8), Section 7 (p.8)
- 问题：论文在 8 页内试图覆盖 7 个独立贡献点（SICA方法、负面实验、三个诊断指标、27种remediation策略、cross-architecture escape、Symbolic Mirage、decision framework）。
  - Section 5.5（Remediation Analysis）仅用~15行总结27种策略的全部失败
  - Section 6（Cross-Architecture）在约半页内完成方法+结果+分析，仅测试了一个外部验证器
  - Section 7（Discussion）被压缩在 page 8 底部约1/3页
- 为什么影响接收：信息密度过高导致可读性下降；核心贡献（cross-architecture escape、diagnostic toolkit）无法被充分评估。
- 建议：精简正文——将27种remediation的详细描述移至附录，正文只保留3-5种关键策略的深度分析。或重新聚焦为两个核心贡献（负面发现+诊断工具），将cross-architecture部分降为preliminary exploration。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] Claim scope 超出统计证据——"no evidence" vs. 功效不足
- 具体位置：Abstract (p.1), Table 6 / Appendix E (p.15)
- 问题：Abstract 中"no evidence of improvement"的表述暗示 SICA 确实无效。但功效分析显示 16 个非退化条件中 10 个 underpowered（MDE > 2.1pp）。只有 4 个条件通过了 TOST 等价检验。对于 underpowered 条件，正确结论应是"we cannot detect effects smaller than X"。Limitations 中承认了这一点，但 abstract/intro 的 framing 更强。
- 建议：abstract 使用更审慎的措辞，如 "we find no statistically significant improvement under well-powered conditions, and establish equivalence in four conditions"。

**W2** [major] Cross-architecture escape 证据单薄
- 具体位置：Section 6 (p.8), Table 3 (p.8)
- 问题：仅测试一个外部验证器（DeBERTa-large-mnli），仅在 Mistral-7B 组合中显著。缺少关键 baseline：(1) 用另一个 LLM 做 verification 是否也能 escape？(2) DeBERTa standalone accuracy 是多少？增益是否仅因为 DeBERTa 本身更强？
- 建议：测试更多验证器；报告 standalone performance；将结论降级为 preliminary evidence。

**W3** [major] K_eff 概念新颖性有限
- 具体位置：Section 3.1 (p.4), Section 5.1 (p.6)
- 问题：K_eff = K/(1+(K-1)·κ) 直接来自 Fleiss' κ (1971) 和 Kish (1965) 的 design effect framework。将 Fleiss' κ 重解释为 effective independent voters 在 survey sampling 文献中已有先例。
- 建议：明确定位为"对已有统计概念在 LLM symbolic extraction 场景下的首次应用"。

**W4** [major] 数据集/领域覆盖有限
- 具体位置：Section 4.1 (p.5), Limitations (p.9)
- 问题：仅覆盖逻辑推理数据集。标题为"Improving LLM Reasoning"而非"Improving LLM Logical Reasoning"，claim 范围超出证据覆盖。GSM8K pilot（n=30）太小。
- 建议：标题限定为 logical/formal reasoning，或增加数学推理实验。

**W5** [minor-to-major] Related Work 遗漏近期重要工作
- SETS (2025, arXiv:2501.19306)：声称 self-verification 在 test-time scaling 中有正面效果，与本文负面发现直接矛盾，需讨论差异
- Multi-Agent Verification (MAV, 2025, arXiv:2502.20379)：多验证器扩展 test-time compute，与 Section 6 高度相关
- Decomposing LLM Self-Correction (2026, arXiv:2601.00828)：Accuracy-Correction Paradox 与本文发现可能关联
- "Scaling Test-Time Compute Without Verification or RL is Suboptimal" (2025, arXiv:2502.12118)：为 cross-architecture verifier 方向提供理论支撑

---

## 小问题

- 术语负载过重（SC/SICA/SCB/CJT/BR/K_eff/C_0/CCR/NLI/DRC/TOST/MDE/FDR），建议增加术语对照表或减少非核心缩写
- "Symbolic Confirmation Bias"命名可能与心理学 confirmation bias 混淆，建议使用更精确术语或明确区分
- Abstract 过于密集，~200词内引入5个技术概念
- Figure 1 pipeline 图缺少 SCB failure mode 的视觉表现
- Table 1 缺少 positive/negative Δ 的直观视觉区分
- Page 8 的 Design principles 各只有一句话展开，作为核心贡献展开不足

---

## 主要优势

1. **实验严谨性极高**：6模型×3数据集×3000+条件、FDR校正、TOST等价检验、功效分析、bootstrap CI、McNemar检验，远超大多数负面结果论文
2. **结构性归因**：不止报告失败，通过 shuffle control、process-level independence analysis、CCR 系统分析了*为什么*失败
3. **诊断工具组合有实用价值**：K_eff+BR+C_0 作为组合诊断用于预测 symbolic self-verification 是否有效，对实践者有用
4. **提供建设性出路**：cross-architecture escape 让论文不止于否定
5. **附录极为详尽（19页）**：case studies、ablations、prompts、统计分析齐全
6. **匿名性和格式合规**：未发现身份泄露，引用格式一致，页数合规（8页正文+Limitations不计）

---

## Questions for Authors

Q1. SETS (2025) 报告 self-verification 在 test-time scaling 中有正面效果。你们的负面发现仅限于 symbolic constraint extraction 场景吗？能否讨论差异？

Q2. DeBERTa 的 standalone NLI accuracy 在 FOLIO/PW 上是多少？增益是否可完全归因于更强的 task-specific verifier，而非 architectural independence？

Q3. QwQ-32B 的 SC baseline 已很高（~84%+），ceiling effect 是否是导致无增益的主要原因而非 SCB？

Q4. 27种 remediation 全部 neutral-to-negative——是否有策略显示了定性不同的 failure pattern？全部失败是否暗示问题在 extraction 而非 aggregation？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1508 · 2026-05-22T13:27:03.193866+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 97

## Round 97

2 recorded events


### User

_source line 1509 · 2026-05-22T13:27:07.566157+00:00_

[Reviewer 2 审稿结果]:
审稿完成。核心判断：

- **Overall 3.5（Borderline Conference）**：实验方法论在负面结果论文中达到很高水准，但核心发现（self-extracted constraints 继承模型偏差）的新颖性受限于已有 self-correction 文献的覆盖。
- **两个 critical 问题**：(1) Symbolic Mirage Hypothesis 更像是对已知现象的 formalization 而非新发现，需要更清晰地论证增量贡献；(2) 8 页正文信息严重过载，cross-architecture escape 和 discussion 展开不足。
- **四个 major 问题**：claim scope 超出功效分析支撑、cross-architecture 证据单薄、K_eff 概念新颖性有限、数据集领域覆盖有限。
- **Related Work 缺漏**：SETS (2025)、MAV (2025) 等近期工作与本文发现直接相关但未被讨论。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1510 · 2026-05-22T13:27:14.773304+00:00_

Reviewer 2 报告已收到（Overall 3.5，2 critical + 4 major）。等待 Reviewer 1 完成独立初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 98

## Round 98

6 recorded events


### User

_source line 1511 · 2026-05-22T13:27:47.080190+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿报告

**论文**: Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Show No Evidence of Improving LLM Reasoning
**Venue**: EMNLP 2026 (ARR May 2026)
**审查侧重**: 方法严谨性、实验设计、统计分析

---

## 总体评分
**Overall**: 4 (Conference — 可被主会议接收)
**一句话总结**: 方法论严谨的重要负面结果论文，诊断框架（SCB/Symbolic Mirage）有学术贡献，统计分析全面；主要不足在于标题声明范围显著超出实验证据覆盖面（仅逻辑推理），跨架构实验规模不足以支撑强结论。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 (Strong) | 统计方法全面（McNemar+TOST+Bootstrap+Power analysis），实验设计系统性强；Fleiss' κ 近似讨论充分，多数声明有充分实验支撑 |
| Excitement | 3.5/5 | 负面结果及时且重要，SCB 诊断和 Symbolic Mirage 框架有新意；但研究范围限于逻辑推理，对更广泛 NLP/reasoning 社区的影响有限 |
| Reproducibility | 4/5 | 超参数、prompt 模板（Appendix B）、统计检验细节完整披露；Z3 求解过程可复现；多种子复制增强可靠性；但代码/数据未以匿名方式提供 |
| Confidence | 4/5 | 仔细阅读全文 + 15 页附录，对统计方法和实验设计有专业判断 |

---

## 主要优势

**S1. 统计方法论异常扎实。** 论文罕见地同时采用多种互补的统计工具：McNemar exact test 检测差异显著性、TOST equivalence test 论证等价性、Bootstrap CI 提供非参数置信区间、Power analysis 报告 MDE 和 observed power。这四重检验体系形成完整的证据链——不仅说明"没有显著差异"，还积极论证"效果量小到可忽略"。Table 6（Appendix E）透明报告了 10 个 underpowered condition 的 MDE，承认检验力不足而非回避，体现了统计诚实性。

**S2. 实验规模和系统性覆盖令人信服。** 6 个模型（7B–32B + frontier QwQ-32B）× 3 个逻辑推理数据集 × ~3,000 condition-evaluations，覆盖了从小模型到前沿模型的能力谱。Oracle control（+29.90pp，§4.1）有效证明了 MAX-SAT 机制本身的 soundness，将问题精确定位到约束质量而非聚合方法。

**S3. 诊断框架（SCB + Symbolic Mirage）有学术新意。** Bias Ratio（Eq. 5）和 Conditional Correction Ratio（CCR, Appendix D）提供了可操作的量化诊断工具。SCB 的发现——83.3% 的 self-extracted constraints 支持错误多数答案（§5.2）——是对"自提取约束=独立验证"这一隐含假设的有力反驳。

**S4. 补救分析（Remediation）全面彻底。** 27 种 training-free 策略跨 4 大类（prompt-level, method-level, trace filtering, scoring）系统性测试（Figure 2, Tables 12–14），全部产生 neutral-to-negative 结果。这不是简单的"一个方法不行"，而是在方法空间内做了近乎穷举的搜索，显著增强了负面结论的说服力。

**S5. 论文写作清晰，结构合理。** 从 CJT 理论出发 → 提出 SICA → 实证负面结果 → 诊断原因（SCB）→ 形式化假说（Symbolic Mirage）→ 验证假说（包括 cross-architecture escape），逻辑链完整自洽。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 标题声明范围显著超出实验证据覆盖面
- 具体位置：Title, Abstract（"LLM Reasoning"）
- 问题：标题声称"Self-Extracted Symbolic Constraints Show No Evidence of Improving **LLM Reasoning**"，但全部主实验仅覆盖形式逻辑推理（FOLIO/ProofWriter/LogiQA）。数学推理（GSM8K）仅有 n=30 的 pilot（§4.1 脚注），不构成有效证据。StrategyQA/ARC-Challenge 仅出现在附录部分分析中（Table 19），未纳入主结果。当前社区对 symbolic verification 的兴趣主要集中在数学推理领域（如 chain-of-verification, self-refinement with code），本文的结论直接套用到"LLM Reasoning"整体缺乏支撑。
- 为什么影响接收：Reviewer 和读者会基于标题预期论文覆盖了推理的主要子领域。Title overclaim 是 *ACL 审稿中常见的降分理由。
- 建议修改方向：将标题限定为 "Formal/Logical Reasoning" 或 "Propositional Reasoning"，并在 Abstract/Introduction 中明确声明 scope limitation。或者补充 GSM8K/MATH 的中等规模实验（n≥200）以支撑当前标题。

**N2** [major] Symbolic Mirage Hypothesis 的验证存在部分循环论证
- 具体位置：§3.3, §5.5（Predictions 1–3）
- 问题：Symbolic Mirage Hypothesis 的三个 predictions 中，Prediction 1（BR > 1.0 across architectures）和 Prediction 2（no same-model intervention reduces BR below 1.0）本质上是对已观察数据模式的事后总结，而非独立预测。具体而言：
  - Prediction 1 直接来自 §5.2 的 SCB 诊断（Table 2）——即先观察到 BR > 1，再将其"预测"为假说内容
  - Prediction 2 通过同一轮 27 种补救策略的实验验证——这些策略的设计本身受 SCB 观察的指导
  - 只有 Prediction 3（cross-architecture escape）涉及独立于初始观察的新数据（§6 DeBERTa 实验）
- 为什么影响接收：假说验证的科学价值在于其预测力。将已知观察重新打包为"predictions"削弱了框架的说服力。
- 建议修改方向：(1) 明确区分"基于初始数据的归纳"和"独立验证的预测"；(2) 在 §3.3 中将 Predictions 1–2 重新定位为"observations that motivate the hypothesis"，仅将 Prediction 3 + 可能的 out-of-distribution 测试作为 genuine predictions；(3) 考虑在不同于主实验的数据集或模型上做 held-out 验证。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] 跨架构实验（§6）规模不足以支撑 capability gap hypothesis 的结论强度
- 具体位置：§6, Table 3（n=6 conditions: 3 generators × 2 datasets）
- 问题：仅 6 个实验条件中，只有 Mistral-7B 一个 generator 在 combo gain 上达到统计显著（+4.67 pp, p < 0.001），而且 DeBERTa 仅 400M 参数，capability gap 的单调性只在 3 个 NLI 架构×有限 generator 上测试。论文据此得出"combo gain decreases monotonically with generator capability"和"NLI escape"的较强结论（Figure 7），但 6 个数据点上拟合单调趋势说服力有限。此外，DeBERTa NLI 分类器与 LLM 约束提取在任务性质上有本质区别，将 NLI 三分类与 MAX-SAT 约束验证混为一谈需要更充分的讨论。
- 建议：(1) 增加 generator 和 verifier 的组合数量；(2) 讨论 NLI 验证 vs. 约束逻辑验证的 task gap；(3) 将结论措辞软化为"preliminary evidence"而非暗示已验证的 capability gap ordering。

**W2** [moderate] Fleiss' κ 作为 Condorcet K_eff 中 ICC 的近似仅有中等经验验证
- 具体位置：§3.1, Eq. 1
- 问题：论文使用 Fleiss' κ 代替 ICC 插入 Kish (1965) 的有效样本量公式。两者在理论上有本质区别：Fleiss' κ 是 chance-corrected agreement measure，ICC 是方差分量比。论文虽承认"not identical to the ICC"并报告 r = 0.625 的经验验证（页 4），但 r = 0.625 仅为中等相关。在边际分布偏斜时（如高准确率模型），Fleiss' κ 系统性偏低，可能高估 K_eff（低估相关性），使 Condorcet 分析过于乐观。
- 建议：(1) 报告 ICC 的直接计算值与 κ 的对比；(2) 讨论 base rate（模型准确率）对 κ 估计的影响（prevalence paradox）；(3) 使用 ICC 重新计算 K_eff 作为 robustness check。

**W3** [moderate] BR（Bias Ratio）的计算子集大小未报告，高准确率模型上可能噪声过大
- 具体位置：§3.3 Eq. 5, Table 2
- 问题：BR 仅在 a_M ≠ a* 的错误问题子集上计算。对 SC 准确率 >80% 的模型（如 QwQ-32B），FOLIO (n=204) 上的错误子集可能 <40 个问题。在如此小的子集上计算 BR 的统计可靠性存疑。Table 2 报告了跨时间的 BR，但未提供 BR 计算所基于的问题数量（分母 n），也未报告 BR 的 confidence interval。
- 建议：在 Table 2 中增加 BR 计算的 n（错误问题数），并为 BR 提供 bootstrap CI。

**W4** [moderate] 缺少显式的 α（Eq. 3 混合参数）敏感性分析
- 具体位置：§3.2 Eq. 3, Appendix M
- 问题：主结果固定 α = 0.5，Appendix M 详细分析了 K 和 T 的敏感性，但未包含 α 的系统性扫描。Table 10–11（Appendix I）通过对比 count-only、random-weight 等消融间接涉及 α 的效果，但 α ∈ {0, 0.25, 0.5, 0.75, 1.0} 的直接扫描会更清晰地展示约束信号的边际贡献。α = 0 时 SICA 退化为 SC，α = 1 时完全依赖约束——这两个极端的对比对理解 SCB 机制至关重要。
- 建议：补充 α 敏感性分析，至少 5 个水平，在 1–2 个代表性条件上报告。

**W5** [minor] TOST equivalence margin ±2pp 的选择依据可以更充分
- 具体位置：§4.2, Appendix E
- 问题：论文将 ±2pp 定义为"lower bound of SC literature gains (2–5 pp)"。但 ±2pp 的选择使得 equivalence testing 门槛很低——即使真实效果为 +1.5pp，TOST 也会判定为 equivalent。这在负面结果论文中倾向于支持作者的结论。更常见的做法是基于 smallest effect size of interest (SESOI) 或 clinical significance threshold 来选择 margin，并进行 margin sensitivity analysis（如 ±1pp, ±2pp, ±3pp 分别有多少条件通过 TOST）。
- 建议：补充不同 margin 下的 TOST 结果数量，展示结论的 robustness。

---

## 小问题（不影响接收）

- Table 1 的 "Type C" 标注（footnote 8: κ_eff diagnostic）首次出现时缺少正文中的解释，需要跳转到 §3.1 才能理解含义。建议在 Table 1 caption 中简要定义。
- Figure 3（page 12, Appendix A）展示 SICA vs SC 的 scatter plot，但 x 轴 SC baseline accuracy 与 y 轴 SICA accuracy 的区分不够清晰；可以改为直接绘制 Δ (SICA − SC) vs SC baseline 更直观。
- GSM8K pilot (n=30) 在 §9 Limitations 中被提及但未明确标注为 "exploratory/pilot only, not evidence"。建议在首次提及处加注。
- 多种子复制仅在 2 个模型上执行（Mistral-7B 3-seed, Qwen2.5-14B 4-seed），对其他 4 个模型无复制数据。
- Table 5（Appendix D, page 14）中 per-condition constraint diagnostics 的部分行缺失具体数值（用 dashes 标注），应注明原因。

---

## 审稿人提问（Questions）

**Q1**: 对于 BR > 1 的 models，如果在 constraints 中只保留与 ground truth 一致的约束（即用 oracle filter 而非 oracle constraints），accuracy 如何变化？这比 full oracle 更接近"提升约束质量"的可行路径。

**Q2**: Table 17（Appendix S）的 cross-model process similarity 中，"Gap" 列从 0.31（LLaMA）到 0.102（Mistral）。更大的 process gap 是否对应更好的 cross-model extraction 效果？如果是，这将直接支持 capability gap hypothesis。

**Q3**: 27 种 remediation strategies 是否穷尽了合理的方法空间？特别是 "trained constraint extractor"（论文在 §7 Discussion 中提及为 future direction）和 "ensemble of diverse extractors"（不同 prompt/temperature 提取后合并）是否被考虑过？

**Q4**: 在 DeBERTa cross-architecture 实验中（§6），NLI verifier 的 standalone 准确率是多少？如果 verifier 本身准确率有限，combo gain 的 ceiling 是什么？论文提到 55.00% standalone 但未分析 verifier error 与 generator error 的重叠模式。

---

## 页数合规性

正文（Abstract + §1–§7）结束于第 8 页底部。Limitations 从第 9 页顶部开始，不计入页数。References 从第 9 页中部开始，无限制。**符合 EMNLP 2026 长文 8 页正文限制。**

---

## Missing References

论文的引用覆盖面较好，但以下相关工作可考虑补充：

1. **Lightman et al. (2024)** "Let's Verify Step by Step" — process reward models 作为替代的约束验证方式，与 self-extraction 的 capability gap 讨论直接相关（论文已引用但讨论有限）。
2. **Weng et al. (2023)** "Large Language Models are Better Reasoners with Self-Verification" — 另一种 self-verification 方法，与 SCB 的发现形成对比讨论。论文在 Related Work 中已引用但未深入对比实验差异。
3. 建议在 §2 讨论 **Reflexion (Shinn et al., 2023)** 与 constraint-based self-correction 的区别——Reflexion 使用自然语言反馈而非形式化约束，但同样面临 self-correction 的已知局限。

---

## 总结

这是一篇方法论质量优秀的负面结果论文。其核心贡献——对 self-extracted symbolic constraints 的系统性否证和 SCB 的诊断——对从事 neuro-symbolic reasoning 和 LLM self-improvement 的研究者有实际价值。论文最大的结构性问题是标题/声明范围与实验证据的不匹配（仅逻辑推理，未覆盖数学推理），以及跨架构实验的初步性质。如果作者能缩窄标题范围（或补充数学推理实验）并软化 Symbolic Mirage Hypothesis 的验证表述，本文达到 conference acceptance 水准。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1512 · 2026-05-22T13:28:54.053472+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告（Round 1）\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n### Must-Fix 问题\n\n**N1** [critical] Symbolic Mirage Hypothesis 的新颖性不足——更像是对已知现象的重新包装\n- 论文将\"self-extracted constraints inherit the generating model's distributional biases\"包装为\"Symbolic Mirage Hypothesis\"并作为核心贡献之一。然而，Huang et al. (2024, TACL survey) 已系统论证 LLM 无法在无外部反馈下自我纠正推理错误；Stechly et al. (2025) 在 self-verification 场景下也得出了类似负面结论。本文的发现本质上是同一原理在 symbolic constraint extraction 这一具体场景下的又一实例。Section 3.3 的 BR（Bias Ratio）本身只是\"constraints 对错误答案的支持比例\"的简单度量。论文声称 \"No prior work has systematically evaluated this\"（p.1），但 self-correction 文献已从多个角度覆盖了这一问题。\n- 建议：(1) 明确区分本文发现与 Huang et al. 的增量贡献；(2) 降低\"Hypothesis\"措辞；(3) 讨论为什么 symbolic extraction 被预期能不同于一般 self-correction。\n\n**N2** [critical] 8 页正文信息过载，关键贡献展开严重不足\n- Section 5.5（Remediation Analysis）仅用~15行总结27种策略的全部失败\n- Section 6（Cross-Architecture）在约半页内完成方法+结果+分析\n- Section 7（Discussion）被压缩在 page 8 底部约1/3页\n\n### Should-Fix 问题\n\n**W1** [major] Claim scope 超出统计证据——\"no evidence\" vs. 功效不足\n- Abstract 中\"no evidence of improvement\"的表述暗示 SICA 确实无效。但功效分析显示 16 个非退化条件中 10 个 underpowered（MDE > 2.1pp）。只有 4 个条件通过了 TOST 等价检验。\n\n**W2** [major] Cross-architecture escape 证据单薄\n- 仅测试一个外部验证器（DeBERTa-large-mnli），仅在 Mistral-7B 组合中显著。\n\n**W3** [major] K_eff 概念新颖性有限\n- K_eff = K/(1+(K-1)·κ) 直接来自 Fleiss' κ (1971) 和 Kish (1965) 的 design effect framework。\n\n**W4** [major] 数据集/领域覆盖有限\n- 仅覆盖逻辑推理数据集。标题为\"Improving LLM Reasoning\"而非\"Improving LLM Logical Reasoning\"。\n\n**W5** [minor-to-major] Related Work 遗漏近期重要工作\n- SETS (2025), MAV (2025), Decomposing LLM Self-Correction (2026), \"Scaling Test-Time Compute Without Verification or RL is Suboptimal\" (2025)\n\n### 小问题\n- 术语负载过重\n- \"Symbolic Confirmation Bias\"命名可能与心理学 confirmation bias 混淆\n- Abstract 过于密集\n- Figure 1 缺少 SCB failure mode 的视觉表现\n- Table 1 缺少 positive/negative Δ 的直观视觉区分\n- Design principles 各只有一句话展开\n\n### Questions\nQ1. SETS (2025) 报告 self-verification 在 test-time scaling 中有正面效果。你们的负面发现仅限于 symbolic constraint extraction 场景吗？\nQ2. DeBERTa standalone NLI accuracy 在 FOLIO/PW 上是多少？增益是否可完全归因于更强的 task-specific verifier？\nQ3. QwQ-32B 的高 SC baseline 导致的 ceiling effect 是否是主因而非 SCB？\nQ4. 27种 remediation 全部失败是否暗示问题在 extraction 而非 aggregation？\n\n---\n\n请对以上每个 N/W/小问题/Q 逐条给出 [AGREE] 或 [REBUT] 回应，并说明理由。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "symb_invariant_consensus",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告（Round 1）\n\n**Overall**: 3.5 / 5（Borderline Conference）\n\n### Must-Fix 问题\n\n**N1** [critical] Symbolic Mirage Hypothesis 的新颖性不足——更像是对已知现象的重新包装\n- 论文将\"self-extracted constraints inherit the generating model's distributional biases\"包装为\"Symbolic Mirage Hypothesis\"并作为核心贡献之一。然而，Huang et al. (2024, TACL survey) 已系统论证 LLM 无法在无外部反馈下自我纠正推理错误；Stechly et al. (2025) 在 self-verification 场景下也得出了类似负面结论。本文的发现本质上是同一原理在 symbolic constraint extraction 这一具体场景下的又一实例。Section 3.3 的 BR（Bias Ratio）本身只是\"constraints 对错误答案的支持比例\"的简单度量。论文声称 \"No prior work has systematically evaluated this\"（p.1），但 self-correction 文献已从多个角度覆盖了这一问题。\n- 建议：(1) 明确区分本文发现与 Huang et al. 的增量贡献；(2) 降低\"Hypothesis\"措辞；(3) 讨论为什么 symbolic extraction 被预期能不同于一般 self-correction。\n\n**N2** [critical] 8 页正文信息过载，关键贡献展开严重不足\n- Section 5.5（Remediation Analysis）仅用~15行总结27种策略的全部失败\n- Section 6（Cross-Architecture）在约半页内完成方法+结果+分析\n- Section 7（Discussion）被压缩在 page 8 底部约1/3页\n\n### Should-Fix 问题\n\n**W1** [major] Claim scope 超出统计证据——\"no evidence\" vs. 功效不足\n- Abstract 中\"no evidence of improvement\"的表述暗示 SICA 确实无效。但功效分析显示 16 个非退化条件中 10 个 underpowered（MDE > 2.1pp）。只有 4 个条件通过了 TOST 等价检验。\n\n**W2** [major] Cross-architecture escape 证据单薄\n- 仅测试一个外部验证器（DeBERTa-large-mnli），仅在 Mistral-7B 组合中显著。\n\n**W3** [major] K_eff 概念新颖性有限\n- K_eff = K/(1+(K-1)·κ) 直接来自 Fleiss' κ (1971) 和 Kish (1965) 的 design effect framework。\n\n**W4** [major] 数据集/领域覆盖有限\n- 仅覆盖逻辑推理数据集。标题为\"Improving LLM Reasoning\"而非\"Improving LLM Logical Reasoning\"。\n\n**W5** [minor-to-major] Related Work 遗漏近期重要工作\n- SETS (2025), MAV (2025), Decomposing LLM Self-Correction (2026), \"Scaling Test-Time Compute Without Verification or RL is Suboptimal\" (2025)\n\n### 小问题\n- 术语负载过重\n- \"Symbolic Confirmation Bias\"命名可能与心理学 confirmation bias 混淆\n- Abstract 过于密集\n- Figure 1 缺少 SCB failure mode 的视觉表现\n- Table 1 缺少 positive/negative Δ 的直观视觉区分\n- Design principles 各只有一句话展开\n\n### Questions\nQ1. SETS (2025) 报告 self-verification 在 test-time scaling 中有正面效果。你们的负面发现仅限于 symbolic constraint extraction 场景吗？\nQ2. DeBERTa standalone NLI accuracy 在 FOLIO/PW 上是多少？增益是否可完全归因于更强的 task-specific verifier？\nQ3. QwQ-32B 的高 SC baseline 导致的 ceiling effect 是否是主因而非 SCB？\nQ4. 27种 remediation 全部失败是否暗示问题在 extraction 而非 aggregation？\n\n---\n\n请对以上每个 N/W/小问题/Q 逐条给出 [AGREE] 或 [REBUT] 回应，并说明理由。"
  }
}
```

</details>

---


### Tool result

_source line 1513 · 2026-05-22T13:29:09.986408+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15932
}
```

</details>

---


### Tool call

_source line 1514 · 2026-05-22T13:29:10.287966+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告\n\n**Overall**: 4 / 5 (Conference — 可被主会议接收)\n\n### Must-Fix 问题\n\n**N1** [critical] 标题声明范围显著超出实验证据覆盖面\n- 标题声称\"Improving **LLM Reasoning**\"，但全部主实验仅覆盖形式逻辑推理（FOLIO/ProofWriter/LogiQA）。GSM8K 仅有 n=30 pilot。StrategyQA/ARC-Challenge 仅出现在附录部分分析中。当前社区对 symbolic verification 的兴趣主要集中在数学推理领域。\n- 建议：标题限定为 \"Formal/Logical Reasoning\" 或补充 GSM8K/MATH 中等规模实验。\n\n**N2** [major] Symbolic Mirage Hypothesis 的验证存在部分循环论证\n- Prediction 1（BR > 1.0 across architectures）和 Prediction 2（no same-model intervention reduces BR below 1.0）本质上是对已观察数据模式的事后总结，而非独立预测。只有 Prediction 3（cross-architecture escape）涉及独立数据。\n- 建议：明确区分\"基于初始数据的归纳\"和\"独立验证的预测\"。\n\n### Should-Fix 问题\n\n**W1** [major] 跨架构实验（§6）规模不足以支撑 capability gap hypothesis\n- 仅 6 个条件中只有 Mistral-7B 达到统计显著（+4.67pp, p<0.001）。DeBERTa NLI 分类器与 LLM 约束提取在任务性质上有本质区别。\n- 建议：增加组合数量；讨论 NLI vs. 约束逻辑验证的 task gap；软化结论措辞。\n\n**W2** [moderate] Fleiss' κ 作为 ICC 近似仅有中等经验验证\n- r = 0.625 仅为中等相关。在边际分布偏斜时 Fleiss' κ 系统性偏低可能高估 K_eff。\n- 建议：报告 ICC 直接计算值与 κ 对比；讨论 prevalence paradox；使用 ICC 重算 K_eff 作 robustness check。\n\n**W3** [moderate] BR 计算子集大小未报告\n- 高准确率模型上错误问题子集可能 <40 个问题，BR 统计可靠性存疑。\n- 建议：Table 2 增加 BR 计算的 n，并为 BR 提供 bootstrap CI。\n\n**W4** [moderate] 缺少显式的 α 敏感性分析\n- 主结果固定 α=0.5，未做 α ∈ {0, 0.25, 0.5, 0.75, 1.0} 系统扫描。\n- 建议：补充 α 敏感性分析。\n\n**W5** [minor] TOST margin ±2pp 选择依据可更充分\n- ±2pp 使 equivalence testing 门槛低，倾向支持作者结论。\n- 建议：补充不同 margin 下 TOST 结果数量。\n\n### 小问题\n- Table 1 \"Type C\" 标注缺少正文解释\n- Figure 3 可改为 Δ vs SC baseline\n- GSM8K pilot 应明确标注 \"exploratory only\"\n- 多种子复制仅 2 个模型\n- Table 5 部分行缺失值未注明原因\n\n### Questions\nQ1: 对 BR > 1 的 models，如果只保留与 ground truth 一致的约束（oracle filter），accuracy 变化？\nQ2: Table 17 cross-model process similarity 中更大的 process gap 是否对应更好的 cross-model extraction 效果？\nQ3: 27 种 remediation 是否穷尽合理方法空间？trained constraint extractor 和 ensemble of diverse extractors 是否考虑过？\nQ4: DeBERTa NLI verifier 的 standalone 准确率是多少？combo gain 的 ceiling 是什么？\n\n### 页数合规性\n**符合 EMNLP 2026 长文 8 页正文限制。**\n\n### Missing References\n1. Lightman et al. (2024) \"Let's Verify Step by Step\"\n2. Weng et al. (2023) \"Large Language Models are Better Reasoners with Self-Verification\"\n3. Reflexion (Shinn et al., 2023)\n\n---\n\n请对以上每个 N/W/小问题/Q 逐条给出 [AGREE] 或 [REBUT] 回应，并说明理由。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "symb_invariant_consensus",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个问题标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告\n\n**Overall**: 4 / 5 (Conference — 可被主会议接收)\n\n### Must-Fix 问题\n\n**N1** [critical] 标题声明范围显著超出实验证据覆盖面\n- 标题声称\"Improving **LLM Reasoning**\"，但全部主实验仅覆盖形式逻辑推理（FOLIO/ProofWriter/LogiQA）。GSM8K 仅有 n=30 pilot。StrategyQA/ARC-Challenge 仅出现在附录部分分析中。当前社区对 symbolic verification 的兴趣主要集中在数学推理领域。\n- 建议：标题限定为 \"Formal/Logical Reasoning\" 或补充 GSM8K/MATH 中等规模实验。\n\n**N2** [major] Symbolic Mirage Hypothesis 的验证存在部分循环论证\n- Prediction 1（BR > 1.0 across architectures）和 Prediction 2（no same-model intervention reduces BR below 1.0）本质上是对已观察数据模式的事后总结，而非独立预测。只有 Prediction 3（cross-architecture escape）涉及独立数据。\n- 建议：明确区分\"基于初始数据的归纳\"和\"独立验证的预测\"。\n\n### Should-Fix 问题\n\n**W1** [major] 跨架构实验（§6）规模不足以支撑 capability gap hypothesis\n- 仅 6 个条件中只有 Mistral-7B 达到统计显著（+4.67pp, p<0.001）。DeBERTa NLI 分类器与 LLM 约束提取在任务性质上有本质区别。\n- 建议：增加组合数量；讨论 NLI vs. 约束逻辑验证的 task gap；软化结论措辞。\n\n**W2** [moderate] Fleiss' κ 作为 ICC 近似仅有中等经验验证\n- r = 0.625 仅为中等相关。在边际分布偏斜时 Fleiss' κ 系统性偏低可能高估 K_eff。\n- 建议：报告 ICC 直接计算值与 κ 对比；讨论 prevalence paradox；使用 ICC 重算 K_eff 作 robustness check。\n\n**W3** [moderate] BR 计算子集大小未报告\n- 高准确率模型上错误问题子集可能 <40 个问题，BR 统计可靠性存疑。\n- 建议：Table 2 增加 BR 计算的 n，并为 BR 提供 bootstrap CI。\n\n**W4** [moderate] 缺少显式的 α 敏感性分析\n- 主结果固定 α=0.5，未做 α ∈ {0, 0.25, 0.5, 0.75, 1.0} 系统扫描。\n- 建议：补充 α 敏感性分析。\n\n**W5** [minor] TOST margin ±2pp 选择依据可更充分\n- ±2pp 使 equivalence testing 门槛低，倾向支持作者结论。\n- 建议：补充不同 margin 下 TOST 结果数量。\n\n### 小问题\n- Table 1 \"Type C\" 标注缺少正文解释\n- Figure 3 可改为 Δ vs SC baseline\n- GSM8K pilot 应明确标注 \"exploratory only\"\n- 多种子复制仅 2 个模型\n- Table 5 部分行缺失值未注明原因\n\n### Questions\nQ1: 对 BR > 1 的 models，如果只保留与 ground truth 一致的约束（oracle filter），accuracy 变化？\nQ2: Table 17 cross-model process similarity 中更大的 process gap 是否对应更好的 cross-model extraction 效果？\nQ3: 27 种 remediation 是否穷尽合理方法空间？trained constraint extractor 和 ensemble of diverse extractors 是否考虑过？\nQ4: DeBERTa NLI verifier 的 standalone 准确率是多少？combo gain 的 ceiling 是什么？\n\n### 页数合规性\n**符合 EMNLP 2026 长文 8 页正文限制。**\n\n### Missing References\n1. Lightman et al. (2024) \"Let's Verify Step by Step\"\n2. Weng et al. (2023) \"Large Language Models are Better Reasoners with Self-Verification\"\n3. Reflexion (Shinn et al., 2023)\n\n---\n\n请对以上每个 N/W/小问题/Q 逐条给出 [AGREE] 或 [REBUT] 回应，并说明理由。"
  }
}
```

</details>

---


### Tool result

_source line 1515 · 2026-05-22T13:29:11.699655+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1411
}
```

</details>

---


### Assistant

_source line 1516 · 2026-05-22T13:29:14.904506+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 99

## Round 99

2 recorded events


### User

_source line 1517 · 2026-05-22T13:29:17.488128+00:00_

[Reviewer 1 审稿结果]:
审稿完成。报告已提交至 Review Director，主要结论：

- **Overall: 4 (Conference)**，Soundness 4/5，Excitement 3.5/5
- **2 个 Must-Fix**：(1) 标题"LLM Reasoning"范围超出证据（仅逻辑推理，无数学推理）；(2) Symbolic Mirage Hypothesis 的 Predictions 1–2 存在循环论证（事后观察重新包装为预测）
- **5 个 Should-Fix**：跨架构实验仅 6 条件规模不足、Fleiss' κ→ICC 近似验证中等(r=0.625)、BR 计算子集大小未报告、缺少 α 敏感性扫描、TOST margin 选择依据可更充分
- **主要优势**：统计方法论异常扎实（McNemar+TOST+Bootstrap+Power analysis 四重检验）、27 种补救策略近乎穷举、Oracle control 有效定位问题、SCB 诊断框架有学术新意
- **页数合规**：正文 8 页，符合 EMNLP 2026 要求

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1518 · 2026-05-22T13:29:31.110638+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 100

## Round 100

2 recorded events


### User

_source line 1519 · 2026-05-22T13:32:10.849209+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[REBUT] R2-N1: Symbolic Mirage Hypothesis 新颖性不足**

R2 的论点是 Huang et al. (2024) 已论证 LLM 无法在无外部反馈下自我纠正，因此本文发现只是同一原理的又一实例。这一论点低估了 symbolic constraint extraction 场景的特殊性：

1. **SICA 实际引入了外部组件（Z3 solver）。** Huang et al. 的核心论点是"without external feedback"LLM 无法自我纠正。SICA 将约束转化为 Z3 公式，用形式化求解器（而非 LLM 自身）做验证——这恰好是 Huang et al. 所说的"external feedback"的一个合理实现。本文的关键发现不是"self-correction fails"（已知），而是**即使加了 external solver，extraction step 本身就注入了偏差，使得 formal verification layer 变为空操作**（§5.2: 94% of constraints overlap with SC errors, Table 2: BR > 1.0 across all architectures）。这一发现在 Huang et al. 的框架下并非不言自明——一个合理的先验预期是：formal logic extraction + Z3 solving 应该比 NL self-correction 更有效。

2. **BR（Eq. 5）和 SCB 的量化刻画是新贡献。** BR 精确度量了约束对错误答案的偏好强度（而非仅仅"有/无"自我纠正能力）。Table 2 显示 BR 随 cosine similarity 变化的规律性（BR_init vs BR_late），这是 prior work 未提供的粒度。Stechly et al. (2025) 在 planning 场景下得出负面结论，但未提供类似的 bias quantification mechanism。

3. **退化条件（Eq. 4）的理论贡献。** 论文证明了 MAX-SAT aggregation 在约束退化时精确等价于 majority voting——这不是 Huang et al. 讨论的问题，而是对 "symbolic constraints add value over voting" 这一特定命题的形式化反驳。

但我同意 R2 的一个子论点：论文应更明确讨论与 Huang et al. 框架的关系，说清"为什么 symbolic extraction 被预期能不同于一般 self-correction"（§2 Related Work 对此讨论不够深入）。"Hypothesis" 这一措辞确实偏强，"Diagnostic Framework" 可能更准确。

---

**[AGREE] R2-N2: 信息过载，关键贡献展开不足**

同意这一观察，但认为 severity 应为 major 而非 critical。具体证据：

- §5.5 的 27 种策略确实仅 ~15 行正文 + Figure 2 scatter plot。虽然 Tables 12–14（Appendix L–N）提供了完整细节，但读者需要频繁跳转附录才能理解关键结论的支撑。
- §6 Cross-Architecture 在约半页内从方法到结论，对于论文宣称的三大贡献之一（Symbolic Mirage 的第三个 prediction 验证），展开确实不足。
- §7 Discussion 被压缩在 page 8 底部，design principles 各只有一句话展开——对于一篇以诊断和指导未来方向为核心价值的论文，这部分的深度不够。

不过，8 页硬限制下，作者面临真实的空间约束。可行的调整：(1) 将部分 §3（Background）内容移入附录以腾出空间；(2) CJT 理论框架的推导（§3.1 约半页）可以压缩，因为 K_eff 公式并非论文原创（R2-W3 指出的相同问题）。

---

### Should-Fix 问题

**[REBUT] R2-W1: "no evidence" vs. 功效不足**

R2 的论点有合理之处但对论文的统计处理不够公平：

1. **"No evidence of improvement" 是统计学上准确的表述。** 它表达的是"absence of evidence"而非"evidence of absence"。论文并未声称 SICA "definitively has no effect"——这需要 TOST 全部通过才能说。

2. **论文透明报告了 underpowered conditions。** Table 6（Appendix E）明确列出 10 个条件的 MDE > 2.1pp，并注明"observed power remains below 21% in every condition"。这是统计诚实性的体现，不应被反过来作为批评论据。

3. **多层证据的汇聚超越了单条件功效。** (a) Aggregate sign test: 5+/10−, p > 0.21（非参数，不依赖单条件 power）；(b) Bootstrap CI: 全部三个确认条件区间包含零（Table 7, Appendix F）；(c) 27 种 remediation 全部失败（Figure 2）；(d) Oracle 对照组成功（+29.90pp），排除了 mechanism failure。这些独立证据线的汇合构成了"no evidence of improvement"的合理基础。

不过，我同意 R2 的一个子论点：论文可以在 Abstract 中增加 hedge，如 "we find no statistically significant evidence of improvement across X conditions, with Y remaining underpowered for small effects"，以更准确传达证据状态。

---

**[AGREE] R2-W2: Cross-architecture escape 证据单薄**

完全同意，与我自己的 W1 一致。6 个条件、单一 verifier 架构、仅 Mistral-7B 显著——对于论文三大贡献之一（Prediction 3 验证），这一证据量不足。尤其是 DeBERTa NLI 三分类与 MAX-SAT 约束验证在任务性质上有本质区别，论文未充分讨论这一 gap。

---

**[REBUT] R2-W3: K_eff 概念新颖性有限**

R2 的批评不完全公平。论文从未声称 K_eff 公式本身是新贡献——§3.1 明确说 "Following Ladha (1992) and the design-effect framework of Kish (1965)"。K_eff 的贡献在于**应用层面**：将 effective sample size 作为诊断 SC 局限性的工具，揭示了 κ = 0.21–0.82 时 K_eff 大幅缩减（K = 12 → K_eff = 1.2–3.6, §3.1）的实际后果。这一应用虽非原创公式，但对 SC 文献是有价值的 analytical lens。

不过，我同意论文在主文中花了约半页推导 K_eff（§3.1），对于一个应用已有框架的工具而言，这一篇幅可以压缩以腾出空间给 §5.5/§6/§7（呼应 R2-N2 的空间分配问题）。

---

**[AGREE] R2-W4: 数据集/领域覆盖有限**

完全同意，与我自己的 N1 一致。标题说 "LLM Reasoning" 但仅覆盖逻辑推理。数学推理（GSM8K n=30 仅为 pilot）和常识推理（StrategyQA/ARC-Challenge 仅在附录 Table 19 部分出现）未被主实验覆盖。

---

**[AGREE] R2-W5: Related Work 遗漏近期工作**（部分同意）

同意应讨论更多近期工作。但需注意部分可能是 concurrent submissions（如 2025–2026 年工作可能与本文投稿周期重叠）。对于已公开的 preprints，论文确实应在 §2 中讨论其与本文发现的关系——特别是 test-time scaling 相关工作（如 SETS），因为这些方法使用了不同形式的 self-verification，对比讨论有助于明确本文负面结论的适用边界。

---

### 小问题

**[AGREE]** 术语负载过重：SCB、BR、CCR、K_eff、ProcessSim、DRC 等缩写密集，对非该领域的读者构成认知负担。建议在首次出现时提供更直观的解释。

**[REBUT]** "Symbolic Confirmation Bias" 与心理学 confirmation bias 混淆：论文在 §5.2 首句即明确定义了 SCB 的技术含义（"constraints are coupled to their source answer"），上下文清楚。"Confirmation bias" 在 ML 文献中已有广泛使用先例（如 dataset bias literature），不构成实质混淆风险。

**[AGREE]** Abstract 过于密集：Abstract 确实在约 15 行内塞入了 pipeline 描述、实验规模、六项量化结果、三个 predictions 验证和 cross-architecture 结论。建议精简到核心发现 + 主要证据，细节数字移入正文。

**[AGREE]** Figure 1 缺少 SCB failure mode：Figure 1 仅展示了 SICA 的正常流程，未可视化 SCB 导致约束与错误答案对齐的失败模式。增加一个 failure case 的视觉对比会增强直觉理解。

**[REBUT]** Table 1 缺少 positive/negative Δ 的视觉区分：Table 1 实际已用 bold 标注 p < 0.05 的显著结果，且所有 Δ 值带正负号。虽然颜色编码（如 green/red shading）会更直观，但这在 ACL 模板的黑白打印约束下不一定可行。

**[AGREE]** Design principles 展开不足：§7 的 design principles（cross-architecture escape 的三个必要条件）各仅一句话。对于指导未来研究方向的核心贡献，这确实太简略。

---

### Questions 回应

**[REBUT] R2-Q1: SETS (2025) self-verification 正面效果 vs. 本文负面结论**

两者机制不同。本文的负面发现特指"same-model self-extracted symbolic constraints via MAX-SAT aggregation"（§1, §3.2）。SETS 使用的 self-verification 机制（如 confidence-based scoring）不涉及将推理链转化为 formal logic constraints + Z3 solving。论文的 degeneration analysis（Eq. 4）表明失败的根源在 extraction quality，不是 verification idea 本身。Oracle 对照（§4.1, +29.90pp）直接证明了当约束质量好时，mechanism 有效。两篇论文的结论是互补的，不矛盾。

**[AGREE] R2-Q2: DeBERTa standalone accuracy 与增益归因**

好问题。§6 报告 DeBERTa-large-mnli standalone 55.00%（ProofWriter），但未报告 FOLIO 上的 standalone 准确率，也未分析 verifier error 与 generator error 的重叠模式。如果 DeBERTa 的正确集合是 generator 正确集合的子集，则 combo gain 可能主要来自 task-specific accuracy 而非独立验证能力。论文应补充 error overlap analysis（即 Table 3 对应的 confusion matrix）。这与我自己的 Q4 一致。

**[REBUT] R2-Q3: QwQ-32B ceiling effect vs. SCB**

Ceiling effect 不是 SICA 失败的主因。证据：
1. Mistral-7B 在 FOLIO 上 SC baseline 仅 ~54%（Table 1），远未触顶，SICA 仍无显著改善（Δ = −0.5 to +1.47pp across conditions）
2. Table 1 中 intermediate-SC regime（50–66%）的条件同样无正面结果
3. 论文的 regime analysis（Appendix O, Table 15）明确区分了 high-entropy（SC < 60%）和 low-entropy 条件：low-entropy 条件 Δ ≈ 0pp，high-entropy 条件 SICA 方向不稳定——两种 regime 都无系统性改善
4. QwQ-32B 的高 baseline 确实限制了 improvement room，但 SCB（BR > 1）在所有 accuracy levels 都存在（Table 2）

Ceiling effect 是一个 contributing factor（特别对 frontier models），但 SCB 是更根本的机制解释。

**[AGREE] R2-Q4: 27 种 remediation 全部失败 → 问题在 extraction**

同意这一推断，且论文自身的证据支持这一结论：
1. Oracle controls（§4.1）证明 aggregation mechanism 是 sound 的（+29.90pp）
2. Table 10–11（Appendix I）显示 MAX-SAT 与 count-only aggregation 在 94.4% 的问题上产生相同答案——约束未提供超越投票的增量信息
3. 论文在 §7 Discussion 中将 "trained constraint extractors" 列为最有前景的 future direction
4. §5.3 的 process-level 分析确认 constraint 分布反映 trace 分布而非独立验证信号

这实际上是论文的核心诊断：问题不在 aggregation（Z3/MAX-SAT），而在 extraction 本身继承了 model 的 distributional biases。论文可以更显著地突出这一结论。

---

### 总结

与 R2 在以下问题上达成共识：
- 标题/scope 超出证据覆盖（R2-W4 = 我的 N1）
- Cross-architecture 证据不足（R2-W2 = 我的 W1）
- 正文信息过载（R2-N2）
- Abstract 过密、Figure 1 缺失 failure mode 等呈现问题

与 R2 在以下问题上存在分歧：
- Symbolic Mirage 新颖性（R2-N1）：R2 低估了 symbolic extraction + formal solver 场景的特殊性。论文的贡献不是重复 "self-correction fails"，而是证明 **即使加了 external solver（Z3），extraction step 仍注入偏差使形式化验证层失效**
- "No evidence" 表述（R2-W1）：统计学上准确，且有多层独立证据支撑
- K_eff 新颖性（R2-W3）：论文从未声称公式原创，应用层面有价值
- Ceiling effect vs SCB（R2-Q3）：证据表明 SCB 在所有 accuracy levels 存在，ceiling 非主因

**维持 Overall: 4 (Conference) 的评分。** 论文的方法论质量和诊断贡献足以支撑会议接收，标题 scope 和呈现问题可在 camera-ready 阶段修复。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1520 · 2026-05-22T13:32:17.885400+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 101

## Round 101

2 recorded events


### User

_source line 1521 · 2026-05-22T13:32:20.402705+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结关键分歧：

- **R2-N1 (Symbolic Mirage 新颖性)**：我反驳——R2 忽略了 SICA 引入 Z3 external solver 这一关键区别，论文证明的是"即使加了 formal solver，extraction step 仍注入偏差"，这超越了 Huang et al. 的一般性 self-correction 框架
- **R2-W1 ("no evidence" 表述)**：我反驳——sign test + bootstrap CI + oracle control + 27 remediation 失败构成多层证据汇聚，"no evidence" 是统计学标准用语
- **R2-W3 (K_eff 新颖性)**：我反驳——论文从未声称公式原创，仅作为诊断工具应用

在标题 scope（R2-W4）、cross-architecture 证据不足（R2-W2）、信息过载（R2-N2）等问题上与 R2 达成共识。维持 Overall: 4 的评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1522 · 2026-05-22T13:32:28.088282+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 102

## Round 102

18 recorded events


### User

_source line 1523 · 2026-05-22T13:33:12.366704+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应（R2 → R1）

### Must-Fix

**[AGREE] R1-N1: 标题范围超出实验覆盖**
同意，与我的 W4 一致。标题应限定为 Formal/Logical Reasoning 或补充数学推理实验。

**[AGREE with nuance] R1-N2: Symbolic Mirage Hypothesis 部分循环论证**
方法论批评合理——Prediction 1&2 确为事后总结。但有缓和因素：(1) Prediction 1 覆盖了 9 个模型（含 frontier）远超初始 3 个；(2) 27 种 remediation 构成广泛方法空间探索。严格意义上仅 Prediction 3（cross-arch, §6）是独立验证。建议区分归纳与验证。

### Should-Fix

**[AGREE] R1-W1: 跨架构实验规模不足**
同意，与我的 W2 一致。仅 Mistral-7B 组合显著，且 NLI classification vs. symbolic extraction 的 task gap 需讨论。

**[AGREE] R1-W2: Fleiss' κ 作为 ICC 近似验证不足**
有效统计关切。不过 §5.1 已声明 K_eff 为 "ordinal diagnostic" 而非精确度量，部分缓解此问题。

**[AGREE with nuance] R1-W3: BR 子集大小未报告**
合理。论文有 bootstrap CIs（§5.2），FOLIO Mistral-7B 错误子集约 90 个尚可，但 Gemini-2.5-Pro（SC=87.37%, n=95 interim）错误子集约 12 个，BR 可靠性存疑。建议增加 n_err。

**[REBUT] R1-W4: 缺少 α 敏感性分析**
论文 Appendix Table 11 已有系统 α 分析：α ∈ {0.1, 0.3, 0.5, 0.7, 0.9}，所有值 agreement ≥99%。§5.2 正文明确提及此结果。SCB 导致约束 vacuous，α 无实质影响。但 R1 若要求 Δ(α) 而非仅 agreement(α)，则确实未报告。

**[AGREE] R1-W5: TOST ±2pp margin 依据不足**
同意需更充分论证并报告不同 margin 下结果。

### 小问题
- Table 1 "Type C"：[AGREE] 仅在 caption/appendix 定义，正文缺解释
- Figure 3 改 Δ vs SC：[AGREE] 合理
- GSM8K "exploratory only"：[AGREE] Limitations 有提但需更显眼
- 多种子仅 2 模型：[AGREE]
- Table 5 缺失值：[AGREE]

### Questions
- Q1: §5.5 oracle ceiling +29.90pp 间接回答——正确约束确实有效，但无法在实践中 filter
- Q2: §5.3 ProcessSim 与 gain 单调负相关（ρ=-1.0）已部分回答
- Q3: trained extractor 未测试是合理的 future work，但论文定位为研究 training-free 的局限性
- Q4: 与我的 Q2 一致，DeBERTa standalone accuracy 是关键缺失信息

### Missing References
- **[REBUT]** Lightman (2024)：已被引用（bib: lightman2024prm, ref #37）
- **[REBUT]** Weng (2023)：已被引用（bib: weng2023selfverification, ref #61），§2 明确提及
- **[AGREE]** Reflexion (Shinn 2023)：未引用，但与 symbolic extraction 差异较大，属 minor 遗漏

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1524 · 2026-05-22T13:33:52.608023+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 1525 · 2026-05-22T13:33:52.658891+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T13:19:49.781208+00:00\", \"completed_at\": \"2026-05-22T13:24:27.126218+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点（纯文本：标题+摘要+Introduction开头）。第一个 display item（Figure 1 SICA pipeline）出现在 page 2 右上角，在前 2 页内，位置可接受。Figure 1 传达了核心方法流程（trace → constraint extraction → MAX-SAT），信息传达清晰。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 为单栏宽度，管线图内文字偏小（约正文字号 60-65%）。考虑改为 figure*（全宽）以提升可读性，尤其是 pipeline 中的标注文字和箭头标签。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 3-5\", \"message\": \"连续 3 页无正式 display item（figure/table）。Page 3 为 Related Work 纯文本；Page 4 有 5 个公式提供部分视觉节奏；Page 5 有灰色底色的 \\\"Empirical Finding\\\" 框缓解了单调感，但从 Figure 1（p2）到 Table 1（p6）跨度达 4 页无图表，审稿人浏览时可能产生\\\"纯文本墙\\\"印象。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"\\\"Empirical Finding 1\\\" 和 \\\"Empirical Finding 2\\\" 的灰色框设计是正面的视觉元素，有效打破了文本单调感。建议保留。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1（主结果表）使用 figure* 全宽排版，booktabs 风格，最优值加粗，带显著性标记（*, **）。表格行数多（~25行），字号略小但可读。整体专业。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2 格式规范，booktabs 风格，数值精度统一（2位小数）。页面布局均衡。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 2（27 种 remediation 策略的点图）和 Table 3 共存，视觉密度良好。Figure 2 使用不同标记区分 4 个类别，可读性尚可，但 y 轴标签（策略名称）字号偏小。Section 7（Discussion and Conclusion）在此页开始。\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 简短（约 1/3 页），符合 EMNLP 规范。References 从本页下半部分开始。主正文+Limitations 约占 9 页，Limitations 不计入 8 页限制。\"}, {\"severity\": \"info\", \"dimension\": \"pages 10-11\", \"message\": \"References 排版正常，无 [?] 未解析引用，格式基本统一。双栏对齐良好。\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"Appendix 开始。Figure 3（regime scatter plot）出现在左栏。右栏为 Prompt Templates 的代码块（等宽字体），可读。\"}, {\"severity\": \"info\", \"dimension\
…[truncated 1842 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1526 · 2026-05-22T13:33:53.110864+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 1527 · 2026-05-22T13:33:53.161515+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1528 · 2026-05-22T13:33:54.115921+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | head -100",
  "description": "Read existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | head -100",
    "description": "Read existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1529 · 2026-05-22T13:33:54.267131+00:00_

# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)
- id: "R1-C1"
  summary: "Method Stage 3 sat() implementation undescribed"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit."
  resolution_round: 3

- id: "R1-C2"
  summary: "Most experiments underpowered (n≤60), no power analysis"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "Power analysis + Bootstrap CIs added. Larger n conditions (200-600)."
  resolution_round: 3

- id: "R1-C3"
  summary: "Oracle/upper-bound experiment missing"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp."
  resolution_round: 3

- id: "R1-C4"
  summary: "Huang et al. (ICLR 2024) not cited"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: "Huang, Stechly, Kambhampati all cited and discussed."
  resolution_round: 2

- id: "R1-C5"
  summary: "Critical related work missing"
  category: writing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "~48 citations, 5 Related Work paragraphs."
  resolution_round: 3

- id: "R1-C9"
  summary: "Capability trap novelty unclear"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "Reframed as regime-dependent analysis with CJT framework."
  resolution_round: 3

- id: "R3-N1"
  summary: "σ(c,a) scoring inconsistent between self-extraction and oracle"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 3
  last_seen_round: 4
  resolution: "Paper Agent added clarifying sentence in method.tex."
  resolution_round: 4

- id: "R3-N2"
  summary: "α va
…[truncated 697 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1530 · 2026-05-22T13:33:59.438141+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | wc -l",
  "description": "Count total lines in review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | wc -l",
    "description": "Count total lines in review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1531 · 2026-05-22T13:33:59.488806+00:00_

690

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1532 · 2026-05-22T13:34:05.063099+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | grep -E \"^- id:|status:\" | paste - - | grep -v \"resolved\\|wont_fix\" | head -30",
  "description": "Find open/in_progress issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | grep -E \"^- id:|status:\" | paste - - | grep -v \"resolved\\|wont_fix\" | head -30",
    "description": "Find open/in_progress issues"
  }
}
```

</details>

---


### Tool result

_source line 1533 · 2026-05-22T13:34:05.164016+00:00_

- id: "R9-W2"	  status: in_progress
- id: "R9-W3"	  status: in_progress
- id: "R9-VL1"	  status: in_progress
- id: "R9-VL4"	  status: in_progress
- id: "R10-N2"	  status: in_progress
- id: "R10-N3"	  status: in_progress
- id: "R10-W1"	  status: in_progress
- id: "R10-W2"	  status: in_progress
- id: "R10-W3"	  status: in_progress
- id: "R10-W4"	  status: in_progress
- id: "R10-W6"	  status: in_progress
- id: "R10-W7"	  status: in_progress
- id: "R10-W8"	  status: in_progress
- id: "R10-W9"	  status: in_progress
- id: "R10-I1"	  status: in_progress
- id: "R10-I2"	  status: in_progress
- id: "R10-VL1"	  status: in_progress
- id: "R11-N1"	  status: in_progress
- id: "R11-N2"	  status: in_progress
- id: "R11-N3"	  status: in_progress
- id: "R11-W1"	  status: in_progress
- id: "R11-W2"	  status: in_progress
- id: "R11-W3"	  status: in_progress
- id: "R11-W4"	  status: in_progress
- id: "R11-W5"	  status: in_progress
- id: "R11-W7"	  status: in_progress
- id: "R11-VL1"	  status: in_progress
- id: "R12-N1"	  status: in_progress
- id: "R12-N2"	  status: in_progress
- id: "R12-W1"	  status: in_progress

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1534 · 2026-05-22T13:34:11.301085+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml",
  "description": "Read full review issues YAML"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml",
    "description": "Read full review issues YAML"
  }
}
```

</details>

---


### Tool result

_source line 1535 · 2026-05-22T13:34:11.352410+00:00_

# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)
- id: "R1-C1"
  summary: "Method Stage 3 sat() implementation undescribed"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit."
  resolution_round: 3

- id: "R1-C2"
  summary: "Most experiments underpowered (n≤60), no power analysis"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "Power analysis + Bootstrap CIs added. Larger n conditions (200-600)."
  resolution_round: 3

- id: "R1-C3"
  summary: "Oracle/upper-bound experiment missing"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp."
  resolution_round: 3

- id: "R1-C4"
  summary: "Huang et al. (ICLR 2024) not cited"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: "Huang, Stechly, Kambhampati all cited and discussed."
  resolution_round: 2

- id: "R1-C5"
  summary: "Critical related work missing"
  category: writing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "~48 citations, 5 Related Work paragraphs."
  resolution_round: 3

- id: "R1-C9"
  summary: "Capability trap novelty unclear"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "Reframed as regime-dependent analysis with CJT framework."
  resolution_round: 3

- id: "R3-N1"
  summary: "σ(c,a) scoring inconsistent between self-extraction and oracle"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 3
  last_seen_round: 4
  resolution: "Paper Agent added clarifying sentence in method.tex."
  resolution_round: 4

- id: "R3-N2"
  summary: "α va
…[truncated 16557 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1536 · 2026-05-22T13:37:41.922803+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "symb_invariant_consensus",
  "issues_yaml": "# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)\n- id: \"R1-C1\"\n  summary: \"Method Stage 3 sat() implementation undescribed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit.\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Most experiments underpowered (n≤60), no power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Power analysis + Bootstrap CIs added. Larger n conditions (200-600).\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Oracle/upper-bound experiment missing\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp.\"\n  resolution_round: 3\n\n- id: \"R1-C4\"\n  summary: \"Huang et al. (ICLR 2024) not cited\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Huang, Stechly, Kambhampati all cited and discussed.\"\n  resolution_round: 2\n\n- id: \"R1-C5\"\n  summary: \"Critical related work missing\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"~48 citations, 5 Related Work paragraphs.\"\n  resolution_round: 3\n\n- id: \"R1-C9\"\n  summary: \"Capability trap novelty unclear\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Reframed as regime-dependent analysis with CJT framework.\"\n  resolution_round: 3\n\n- id: \"R3-N1\"\n  summary: \"σ(c,a) scoring inconsistent between self-extraction and oracle\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Paper Agent added clarifying sentence in method.tex.\"\n  resolution_round: 4\n\n- id: \"R3-N2\"\n  summary: \"α value never specified\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"α=0.5 explicit in Eq.(3) and §4.1.\"\n  resolution_round: 3\n\n# Round 9+ issues\n\n- id: \"R9-W2\"\n  summary: \"NLI combo weight parameter w 未交叉验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 14\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"w=3 primary 但未系统分析 w 选择\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 未单独提及 w 参数，但 DRC 评估不充分的批评间接涵盖\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未单独提及，但 DRC 贡献不足的共识间接涵盖\"\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 未单独提及 w 参数\"\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 未单独提及 w 参数\"\n\n- id: \"R9-W3\"\n  summary: \"Capability Gap Hypothesis 基于极小样本 (n=6)\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 14\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"n=6 permutation test\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 升级为 critical: 4/6 共享 DeBERTa verifier, 有效自由度远低于6\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 再次确认 critical 共识: verifier-collapsed p=0.167 不显著\"\n    - round: 13\n      reviewers: [1]\n      note: \"R13(fresh) R1-W1 触及: capability gap claim scope 超出证据\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 两位 Reviewer 再次共识: 仅6条件仅Mistral-7B显著, 需增加验证器/生成器组合或软化结论\"\n\n- id: \"R9-VL1\"\n  summary: \"Pages 1-2 连续纯文本无 display item\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 14\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"视觉审查发现\"\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 视觉审查确认: pages 3-5 约2.5页无figure/table\"\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 视觉审查: pages 3-5 连续3页无正式display item, warning\"\n\n- id: \"R9-VL4\"\n  summary: \"Discussion/Conclusion 仓促, 展开不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 14\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"Conclusion 在 page 8 下半部\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13(fresh) R2-W2/R1共识: Discussion 仅半页\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 再次确认: §7 被压缩在page 8底部约1/3页, design principles 各只有一句话\"\n\n- id: \"R10-N1\"\n  summary: \"Proposition 1 (Self-Extraction Ceiling) 无证明——empirical claim dressed as theorem\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 13\n  resolution: \"当前论文使用 'Empirical Finding 1/2'(page 5 tcolorbox), 不再使用 Proposition 术语\"\n  resolution_round: 13\n\n- id: \"R10-N2\"\n  summary: \"κ→K_eff 映射理论基础不足——r=0.625 验证弱\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fleiss' κ 代入 Kish design effect 公式理论上不严格\"\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 论文有 ordinal diagnostic caveat(§3.1)\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) R1-W2: r=0.625仅中等, prevalence paradox可能高估K_eff. R2同意但指出论文已声明ordinal diagnostic\"\n\n- id: \"R10-N3\"\n  summary: \"Capability gap 'perfectly monotonic' 结论基于 n=6 非独立数据点\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"n=6 permutation test, shared verifier\"\n    - round: 13\n      reviewers: [1]\n      note: \"R13(fresh) Limitations 已标注 p=0.167\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 与R9-W3合并: 共识仍为证据不足\"\n\n- id: \"R10-W1\"\n  summary: \"DRC τ 阈值无 held-out 评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 未单独提及 DRC\"\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 未单独提及\"\n\n- id: \"R10-W2\"\n  summary: \"Cross-architecture NLI escape 适用面极窄\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"仅 Mistral-7B 显著\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13(fresh) 共识: 证据比初判更充分(3个NLI架构), 但domain-specificity仍为问题\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 再次确认: 仅NLI on propositional logic, 需讨论task gap\"\n\n- id: \"R10-W3\"\n  summary: \"四种子复制方差大 + 统计功效 <21%\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"10/16 underpowered, power analysis 埋在附录\"\n    - round: 14\n      reviewers: [1]\n      note: \"R14(fresh) R1-W5: 多种子仅2模型. R1同意R2的claim scope concern\"\n\n- id: \"R10-W4\"\n  summary: \"TOST ±2pp margin 缺少显式理由\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"margin 选择有循环性\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 共识: 需补充不同margin下TOST结果. 论文已有margin sensitivity(±1/2/3pp)但呈现不够\"\n\n- id: \"R10-W5\"\n  summary: \"Bias Ratio 无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"BR CI 已整合: Mistral [3.98,6.37], Qwen [2.44,7.11]\"\n  resolution_round: 10\n\n- id: \"R10-W6\"\n  summary: \"SatLM specification-generation vs SICA trace-extraction 对比不充分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"Related Work §2 有 SatLM 讨论\"\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 未单独提及\"\n\n- id: \"R10-W7\"\n  summary: \"'Symbolic Confirmation Bias' 需与近期 CoT confirmation bias 工作区分\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"Related Work §2 已引 Turpin/Wan/Jhaveri 但区分可更清晰\"\n    - round: 14\n      reviewers: [2]\n      note: \"R14(fresh) R2小问题: SCB命名可能与心理学confirmation bias混淆. R1 REBUT: ML文献有先例, 论文定义清晰\"\n\n- id: \"R10-W8\"\n  summary: \"Related Work 过度压缩——引用列表而非文献讨论\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) R2-S4 反而将 Related Work 覆盖面列为优势\"\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 未单独提及, R2肯定引用覆盖面\"\n\n- id: \"R10-W9\"\n  summary: \"27 种修复策略在正文中展示不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"Figure 2 信息密度高但可读性一般\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) R2-N2: §5.5仅~15行总结27种策略. R1同意(major). 建议正文深度分析3-5种代表性策略\"\n\n- id: \"R10-I1\"\n  summary: \"相对于 Huang/Stechly 的增量新颖性不足\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 Excitement 2.5/5, R1 Excitement 3/5. 分歧记录\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 分歧持续: R2认为可预见, R1认为Z3 formal solver场景使其非平凡. R1建议降低'Hypothesis'措辞为'Diagnostic Framework'\"\n\n- id: \"R10-I2\"\n  summary: \"Independence-Accuracy Trade-off 作为独立贡献有 bias-variance 重述嫌疑\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 未单独提及\"\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 未单独提及\"\n\n- id: \"R10-VL1\"\n  summary: \"主文缺结果可视化\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"主文已有 Figure 1(p2) + Table 1(p6) + Table 2(p7) + Figure 2(p7) + Table 3(p8)\"\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 视觉审查: 主文display items 5个/8页=0.63/页, 合理但偏低\"\n\n- id: \"R11-N1\"\n  summary: \"Spearman ρ=1.0 (n=6) 被过度使用——有效自由度远低于6\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"capability gap claim 超出证据范围. Limitations 标注 p=0.167\"\n    - round: 14\n      reviewers: [1]\n      note: \"R14(fresh) R1-W1再次提及: 6数据点拟合单调趋势说服力有限\"\n\n- id: \"R11-N2\"\n  summary: \"中心 claim 'SICA fails' 与统计功效不匹配——Abstract/title 过强\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"当前标题 'Show No Evidence' 比之前更审慎\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) R1-N1: 标题scope超出(LLM Reasoning vs logical reasoning). R2-W1: 'no evidence'暗示无效但10/16 underpowered. R1 REBUT说统计学准确但同意加hedge. 部分分歧记录\"\n\n- id: \"R11-N3\"\n  summary: \"TOST ±2pp margin 缺乏 principled 论证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"margin 选择有循环性\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 共识持续. 论文已有margin sensitivity但正文呈现不够显著\"\n\n- id: \"R11-W1\"\n  summary: \"DRC 评估不充分——仅PW完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 未单独评估 DRC\"\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 未单独提及\"\n\n- id: \"R11-W2\"\n  summary: \"BR 指标存在循环论证倾向\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"语法去重可能膨胀BR. shuffle control部分回应\"\n    - round: 14\n      reviewers: [1]\n      note: \"R14(fresh) R1-W3: BR计算子集大小未报告, 高准确率模型上噪声大. R2同意需增加n_err\"\n\n- id: \"R11-W3\"\n  summary: \"术语过度品牌化——'Independence Bottleneck' 和 'Symbolic Mirage' 偏 dramatic\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"'Symbolic Mirage' 可能不如 'Symbolic Echo'\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) R1建议降低'Hypothesis'为'Diagnostic Framework'. R2同意. 共识方向一致\"\n\n- id: \"R11-W4\"\n  summary: \"新颖性定位需更早更明确建立与先验工作的 distinction\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"R2 Excitement 2.5/5\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) R2-N1 critical: 新颖性不足. R1 REBUT: Z3 formal solver使其非平凡. R1建议§2讨论为什么symbolic extraction被预期能不同于一般self-correction. 部分分歧但方向一致\"\n\n- id: \"R11-W5\"\n  summary: \"Independence-Accuracy Trade-off 应定位为量化而非新发现\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"未单独提及\"\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 未单独提及\"\n\n- id: \"R11-W6\"\n  summary: \"遗漏引用: Byerly & Khashabi (2026 TACL) 等\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"当前论文 Related Work §2 已引用 Byerly and Khashabi (2026)\"\n  resolution_round: 13\n\n- id: \"R11-W7\"\n  summary: \"27 策略计数膨胀 + 未尝试 trained constraint extractor\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"Limitations 已声明不评估 trained extractors\"\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) R1-Q3: trained extractor为合理future work但论文定位training-free\"\n\n- id: \"R11-VL1\"\n  summary: \"主文缺结果可视化——需上提 Figure 到主文\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"Figure 2 已在正文(p7)\"\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) Figure 2在p8, y轴标签字号偏小(视觉审查)\"\n\n- id: \"R12-N1\"\n  summary: \"标题 overclaiming about frontier scale\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"标题中 'Self-Extracted' 但 frontier 用 cross-model extraction\"\n    - round: 13\n      reviewers: [1]\n      note: \"标题改为 'Show No Evidence' 更审慎\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 标题scope问题转为domain限定: 'LLM Reasoning'应改为'Logical Reasoning'或补实验\"\n\n- id: \"R12-N2\"\n  summary: \"SCB 核心新颖性不足——self-correction failure 在 FOL 载体上的实例化\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 Excitement 2.5, R1 Excitement 3. 分歧记录\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 分歧持续但缩窄: R1认可Z3 formal solver使发现非平凡但建议降低'Hypothesis'措辞; R2维持新颖性有限但承认量化贡献有价值\"\n\n- id: \"R12-N3\"\n  summary: \"DRC 作为 Contribution 4 不够充分\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"DRC demoted to practical observation in §6, no longer listed as independent Contribution\"\n  resolution_round: 13\n  first_raised_round: 12\n  last_seen_round: 13\n\n- id: \"R12-W1\"\n  summary: \"BR 可能存在循环论证——56.4%零变量重叠使约束按定义支持source answer\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"shuffle control部分回应, 但未报告语义去重后BR\"\n    - round: 14\n      reviewers: [1]\n      note: \"R14(fresh) R1-W3再次提及BR子集大小. shuffle control(§5.2)确认BR是structural, 但语义去重后BR仍缺\"\n\n- id: \"R12-W2\"\n  summary: \"CIL 名称和 information-theoretic 声称有误导\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Renamed to Conditional Correction Ratio (CCR), removed 'unify' claim, added bootstrap CI\"\n  resolution_round: 13\n  first_raised_round: 12\n  last_seen_round: 13\n\n- id: \"R12-W3\"\n  summary: \"Figure 2 placement——应在正文而非附录\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"当前论文 Figure 2 已在正文 page 7(§5.5 Remediation Analysis 旁)\"\n  resolution_round: 13\n\n- id: \"R12-W4\"\n  summary: \"Appendix vs 主文关键信息分配不合理\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"符号过载, Discussion过短, power analysis埋在附录\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) R2-N2: 8页信息过载(critical→major共识). R1同意§3.1 K_eff推导可压缩. 建议将CJT推导/ProcessSim/CCR移入附录以腾出空间\"\n\n- id: \"R12-EC1\"\n  summary: \"Extractor Confound——所有 frontier cross-model extraction 使用同一 Mistral-7B extractor\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"frontier BR≈1 可能反映 extractor 能力而非 SCB 减弱\"\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 未单独提及但Table 2 caption已标注cross-model vs self-extraction区别\"\n\n- id: \"R13-N1\"\n  summary: \"摘要 BR 4.97× 选择性报告——最极端条件, frontier BR≈1\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"摘要应报告 BR 范围或中位数\"\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 未单独提及但Abstract报告BR范围1.66-4.97——可能已部分修复\"\n  action_items:\n    - round: 13\n      action: \"摘要改为报告 BR 范围或中位数\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R13-N2\"\n  summary: \"统计功效呈现不足——10/16 underpowered, power analysis 埋在附录\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"§4.2 需增加 power statement\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) §4.2已有TOST结果和power mention, 但R1仍要求更显著呈现MDE. R2-W1: claim scope超出功效\"\n  action_items:\n    - round: 13\n      action: \"§4.2 增加明确 power statement\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R13-N3\"\n  summary: \"α=0.5 无敏感性分析\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"需在代表性条件上跑α消融\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) R2 REBUT R1-W4: Appendix Table 11已有α∈{0.1-0.9}分析, agreement≥99%. 但Δ(α)未报告. 争议缩窄——现有分析方向正确但可补充Δ维度\"\n\n- id: \"R13-W1\"\n  summary: \"符号/指标过载——8页内7个定量工具\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"建议ProcessSim/CCR移至附录\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) R2再次提及术语负载过重. R1同意\"\n\n- id: \"R13-W2\"\n  summary: \"NLI claim 须限定到命题逻辑任务\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"摘要限定为 'on propositional-logic benchmarks'\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 共识持续: §6标题和结论需限定domain scope\"\n\n- id: \"R13-W3\"\n  summary: \"语法去重可能膨胀 BR——未报告语义去重后 BR\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"建议报告语义去重后BR\"\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 未单独提及但shuffle control(§5.2)部分回应\"\n\n- id: \"R13-W4\"\n  summary: \"Symbolic Mirage Hypothesis §3.3 与 §5 验证状态不连贯\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"§5后续小节未回溯具体prediction编号\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) R1-N2: Predictions 1-2为事后总结非独立预测. R2同意(with nuance). 建议区分归纳vs验证\"\n\n- id: \"R13-W5\"\n  summary: \"缺引: Dhuliawala et al. 2023 Chain-of-Verification\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"当前论文 Related Work §2 已引用 dhuliawala2023chainofverification\"\n  resolution_round: 14\n\n# R14(fresh) 新发现的 issues\n\n- id: \"R14-N1\"\n  summary: \"标题'LLM Reasoning'范围超出实验证据——仅覆盖逻辑推理, 无数学推理\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-N1 critical, R2-W4 major. 交叉后完全共识. GSM8K n=30仅为pilot. 建议标题改为'Formal/Logical Reasoning'或补充数学推理实验(n≥200)\"\n  action_items:\n    - round: 14\n      action: \"标题限定为Formal/Logical Reasoning, 或补充GSM8K/MATH中等规模实验\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R14-N2\"\n  summary: \"Symbolic Mirage Hypothesis Predictions 1-2 为事后总结非独立预测——部分循环论证\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-N2首提(major), R2交叉同意(with nuance: Pred1覆盖9模型超出初始3个为缓和因素). 共识: 仅Prediction 3为独立验证. 建议将Pred 1-2重定位为'observations that motivate the hypothesis'\"\n  action_items:\n    - round: 14\n      action: \"§3.3 区分归纳性观察与独立验证的预测; 降低'Hypothesis'措辞为'Diagnostic Framework'或'Empirical Pattern'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R14-W1\"\n  summary: \"Cross-architecture实验仅6条件/单一verifier类型/仅Mistral-7B显著\"\n  category: experiment\n  severity: major\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W1 major, R2-W2 major. 完全共识. R2指出实际3个NLI架构, 但仅在ProofWriter Mistral-7B组合显著. NLI vs symbolic extraction的task gap需讨论\"\n  action_items:\n    - round: 14\n      action: \"增加generator/verifier组合; 讨论NLI vs 约束逻辑验证的task gap; 结论软化为'preliminary evidence'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R14-W2\"\n  summary: \"8页正文信息过载——§5.5/§6/§7展开不足\"\n  category: writing\n  severity: major\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-N2 critical, R1同意降为major. §5.5仅~15行总结27策略; §6半页; §7约1/3页. R1建议压缩§3.1 K_eff推导以腾出空间\"\n  action_items:\n    - round: 14\n      action: \"压缩§3.1 CJT推导; §5.5增加3-5种代表性策略深度分析; §7 Discussion扩展design principles\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R14-W3\"\n  summary: \"'No evidence of improvement' claim scope与统计功效不完全匹配\"\n  category: framing\n  severity: major\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-W1 major. R1 REBUT: 统计学准确, 多层证据汇聚. 但R1同意Abstract可加hedge. 部分分歧: R1认为现有表述可接受, R2认为应更审慎\"\n  action_items:\n    - round: 14\n      action: \"Abstract增加power caveat, 如'with Y conditions remaining underpowered for small effects'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R14-W4\"\n  summary: \"BR计算子集大小(n_err)未报告, 高准确率模型可能噪声过大\"\n  category: experiment\n  severity: moderate\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W3首提, R2同意(Gemini n_err≈12). Table 2增加n_err列并为BR提供bootstrap CI\"\n  action_items:\n    - round: 14\n      action: \"Table 2增加BR计算的n_err列\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R14-W5\"\n  summary: \"Related Work遗漏: SETS(2025), MAV(2025), Decomposing Self-Correction(2026)\"\n  category: writing\n  severity: minor-to-major\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [2]\n      note: \"R2-W5首提. R1同意部分(需讨论与test-time scaling工作的关系). 注意部分可能为concurrent submissions. Lightman/Weng已引用(R2交叉回应确认)\"\n  action_items:\n    - round: 14\n      action: \"§2增加SETS(2025)等近期工作讨论, 特别是self-verification正面结果与本文负面结论的边界差异\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R14-W6\"\n  summary: \"Fleiss' κ→ICC近似仅r=0.625中等验证——prevalence paradox可能高估K_eff\"\n  category: method\n  severity: moderate\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W2首提, R2同意但指出论文已声明ordinal diagnostic. 建议报告ICC直接计算值做robustness check\"\n  action_items:\n    - round: 14\n      action: \"报告ICC直接计算值与κ对比; 讨论base rate对κ的影响\"\n      assigned_to: \"paper_agent\"\n      status: open"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "issues_yaml": "# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)\n- id: \"R1-C1\"\n  summary: \"Method Stage 3 sat() implementation undescribed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit.\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Most experiments underpowered (n≤60), no power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Power analysis + Bootstrap CIs added. Larger n conditions (200-600).\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Oracle/upper-bound experiment missing\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp.\"\n  resolution_round: 3\n\n- id: \"R1-C4\"\n  summary: \"Huang et al. (ICLR 2024) not cited\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Huang, Stechly, Kambhampati all cited and discussed.\"\n  resolution_round: 2\n\n- id: \"R1-C5\"\n  summary: \"Critical related work missing\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"~48 citations, 5 Related Work paragraphs.\"\n  resolution_round: 3\n\n- id: \"R1-C9\"\n  summary: \"Capability trap novelty unclear\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Reframed as regime-dependent analysis with CJT framework.\"\n  resolution_round: 3\n\n- id: \"R3-N1\"\n  summary: \"σ(c,a) scoring inconsistent between self-extraction and oracle\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Paper Agent added clarifying sentence in method.tex.\"\n  resolution_round: 4\n\n- id: \"R3-N2\"\n  summary: \"α value never specified\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"α=0.5 explicit in Eq.(3) and §4.1.\"\n  resolution_round: 3\n\n# Round 9+ issues\n\n- id: \"R9-W2\"\n  summary: \"NLI combo weight parameter w 未交叉验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 14\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"w=3 primary 但未系统分析 w 选择\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 未单独提及 w 参数，但 DRC 评估不充分的批评间接涵盖\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未单独提及，但 DRC 贡献不足的共识间接涵盖\"\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 未单独提及 w 参数\"\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 未单独提及 w 参数\"\n\n- id: \"R9-W3\"\n  summary: \"Capability Gap Hypothesis 基于极小样本 (n=6)\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 14\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"n=6 permutation test\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 升级为 critical: 4/6 共享 DeBERTa verifier, 有效自由度远低于6\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 再次确认 critical 共识: verifier-collapsed p=0.167 不显著\"\n    - round: 13\n      reviewers: [1]\n      note: \"R13(fresh) R1-W1 触及: capability gap claim scope 超出证据\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 两位 Reviewer 再次共识: 仅6条件仅Mistral-7B显著, 需增加验证器/生成器组合或软化结论\"\n\n- id: \"R9-VL1\"\n  summary: \"Pages 1-2 连续纯文本无 display item\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 14\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"视觉审查发现\"\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 视觉审查确认: pages 3-5 约2.5页无figure/table\"\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 视觉审查: pages 3-5 连续3页无正式display item, warning\"\n\n- id: \"R9-VL4\"\n  summary: \"Discussion/Conclusion 仓促, 展开不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 14\n  mentions:\n    - round: 9\n      reviewers: [1]\n      note: \"Conclusion 在 page 8 下半部\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13(fresh) R2-W2/R1共识: Discussion 仅半页\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 再次确认: §7 被压缩在page 8底部约1/3页, design principles 各只有一句话\"\n\n- id: \"R10-N1\"\n  summary: \"Proposition 1 (Self-Extraction Ceiling) 无证明——empirical claim dressed as theorem\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 13\n  resolution: \"当前论文使用 'Empirical Finding 1/2'(page 5 tcolorbox), 不再使用 Proposition 术语\"\n  resolution_round: 13\n\n- id: \"R10-N2\"\n  summary: \"κ→K_eff 映射理论基础不足——r=0.625 验证弱\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Fleiss' κ 代入 Kish design effect 公式理论上不严格\"\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 论文有 ordinal diagnostic caveat(§3.1)\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) R1-W2: r=0.625仅中等, prevalence paradox可能高估K_eff. R2同意但指出论文已声明ordinal diagnostic\"\n\n- id: \"R10-N3\"\n  summary: \"Capability gap 'perfectly monotonic' 结论基于 n=6 非独立数据点\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"n=6 permutation test, shared verifier\"\n    - round: 13\n      reviewers: [1]\n      note: \"R13(fresh) Limitations 已标注 p=0.167\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 与R9-W3合并: 共识仍为证据不足\"\n\n- id: \"R10-W1\"\n  summary: \"DRC τ 阈值无 held-out 评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 未单独提及 DRC\"\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 未单独提及\"\n\n- id: \"R10-W2\"\n  summary: \"Cross-architecture NLI escape 适用面极窄\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"仅 Mistral-7B 显著\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13(fresh) 共识: 证据比初判更充分(3个NLI架构), 但domain-specificity仍为问题\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 再次确认: 仅NLI on propositional logic, 需讨论task gap\"\n\n- id: \"R10-W3\"\n  summary: \"四种子复制方差大 + 统计功效 <21%\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"10/16 underpowered, power analysis 埋在附录\"\n    - round: 14\n      reviewers: [1]\n      note: \"R14(fresh) R1-W5: 多种子仅2模型. R1同意R2的claim scope concern\"\n\n- id: \"R10-W4\"\n  summary: \"TOST ±2pp margin 缺少显式理由\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"margin 选择有循环性\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 共识: 需补充不同margin下TOST结果. 论文已有margin sensitivity(±1/2/3pp)但呈现不够\"\n\n- id: \"R10-W5\"\n  summary: \"Bias Ratio 无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"BR CI 已整合: Mistral [3.98,6.37], Qwen [2.44,7.11]\"\n  resolution_round: 10\n\n- id: \"R10-W6\"\n  summary: \"SatLM specification-generation vs SICA trace-extraction 对比不充分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"Related Work §2 有 SatLM 讨论\"\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 未单独提及\"\n\n- id: \"R10-W7\"\n  summary: \"'Symbolic Confirmation Bias' 需与近期 CoT confirmation bias 工作区分\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"Related Work §2 已引 Turpin/Wan/Jhaveri 但区分可更清晰\"\n    - round: 14\n      reviewers: [2]\n      note: \"R14(fresh) R2小问题: SCB命名可能与心理学confirmation bias混淆. R1 REBUT: ML文献有先例, 论文定义清晰\"\n\n- id: \"R10-W8\"\n  summary: \"Related Work 过度压缩——引用列表而非文献讨论\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) R2-S4 反而将 Related Work 覆盖面列为优势\"\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 未单独提及, R2肯定引用覆盖面\"\n\n- id: \"R10-W9\"\n  summary: \"27 种修复策略在正文中展示不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"Figure 2 信息密度高但可读性一般\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) R2-N2: §5.5仅~15行总结27种策略. R1同意(major). 建议正文深度分析3-5种代表性策略\"\n\n- id: \"R10-I1\"\n  summary: \"相对于 Huang/Stechly 的增量新颖性不足\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 Excitement 2.5/5, R1 Excitement 3/5. 分歧记录\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 分歧持续: R2认为可预见, R1认为Z3 formal solver场景使其非平凡. R1建议降低'Hypothesis'措辞为'Diagnostic Framework'\"\n\n- id: \"R10-I2\"\n  summary: \"Independence-Accuracy Trade-off 作为独立贡献有 bias-variance 重述嫌疑\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 未单独提及\"\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 未单独提及\"\n\n- id: \"R10-VL1\"\n  summary: \"主文缺结果可视化\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"主文已有 Figure 1(p2) + Table 1(p6) + Table 2(p7) + Figure 2(p7) + Table 3(p8)\"\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 视觉审查: 主文display items 5个/8页=0.63/页, 合理但偏低\"\n\n- id: \"R11-N1\"\n  summary: \"Spearman ρ=1.0 (n=6) 被过度使用——有效自由度远低于6\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"capability gap claim 超出证据范围. Limitations 标注 p=0.167\"\n    - round: 14\n      reviewers: [1]\n      note: \"R14(fresh) R1-W1再次提及: 6数据点拟合单调趋势说服力有限\"\n\n- id: \"R11-N2\"\n  summary: \"中心 claim 'SICA fails' 与统计功效不匹配——Abstract/title 过强\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"当前标题 'Show No Evidence' 比之前更审慎\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) R1-N1: 标题scope超出(LLM Reasoning vs logical reasoning). R2-W1: 'no evidence'暗示无效但10/16 underpowered. R1 REBUT说统计学准确但同意加hedge. 部分分歧记录\"\n\n- id: \"R11-N3\"\n  summary: \"TOST ±2pp margin 缺乏 principled 论证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"margin 选择有循环性\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 共识持续. 论文已有margin sensitivity但正文呈现不够显著\"\n\n- id: \"R11-W1\"\n  summary: \"DRC 评估不充分——仅PW完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"R13(fresh) 未单独评估 DRC\"\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 未单独提及\"\n\n- id: \"R11-W2\"\n  summary: \"BR 指标存在循环论证倾向\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"语法去重可能膨胀BR. shuffle control部分回应\"\n    - round: 14\n      reviewers: [1]\n      note: \"R14(fresh) R1-W3: BR计算子集大小未报告, 高准确率模型上噪声大. R2同意需增加n_err\"\n\n- id: \"R11-W3\"\n  summary: \"术语过度品牌化——'Independence Bottleneck' 和 'Symbolic Mirage' 偏 dramatic\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"'Symbolic Mirage' 可能不如 'Symbolic Echo'\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) R1建议降低'Hypothesis'为'Diagnostic Framework'. R2同意. 共识方向一致\"\n\n- id: \"R11-W4\"\n  summary: \"新颖性定位需更早更明确建立与先验工作的 distinction\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [2]\n      note: \"R2 Excitement 2.5/5\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) R2-N1 critical: 新颖性不足. R1 REBUT: Z3 formal solver使其非平凡. R1建议§2讨论为什么symbolic extraction被预期能不同于一般self-correction. 部分分歧但方向一致\"\n\n- id: \"R11-W5\"\n  summary: \"Independence-Accuracy Trade-off 应定位为量化而非新发现\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"未单独提及\"\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 未单独提及\"\n\n- id: \"R11-W6\"\n  summary: \"遗漏引用: Byerly & Khashabi (2026 TACL) 等\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"当前论文 Related Work §2 已引用 Byerly and Khashabi (2026)\"\n  resolution_round: 13\n\n- id: \"R11-W7\"\n  summary: \"27 策略计数膨胀 + 未尝试 trained constraint extractor\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: []\n      note: \"Limitations 已声明不评估 trained extractors\"\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) R1-Q3: trained extractor为合理future work但论文定位training-free\"\n\n- id: \"R11-VL1\"\n  summary: \"主文缺结果可视化——需上提 Figure 到主文\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"Figure 2 已在正文(p7)\"\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) Figure 2在p8, y轴标签字号偏小(视觉审查)\"\n\n- id: \"R12-N1\"\n  summary: \"标题 overclaiming about frontier scale\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"标题中 'Self-Extracted' 但 frontier 用 cross-model extraction\"\n    - round: 13\n      reviewers: [1]\n      note: \"标题改为 'Show No Evidence' 更审慎\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 标题scope问题转为domain限定: 'LLM Reasoning'应改为'Logical Reasoning'或补实验\"\n\n- id: \"R12-N2\"\n  summary: \"SCB 核心新颖性不足——self-correction failure 在 FOL 载体上的实例化\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 Excitement 2.5, R1 Excitement 3. 分歧记录\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 分歧持续但缩窄: R1认可Z3 formal solver使发现非平凡但建议降低'Hypothesis'措辞; R2维持新颖性有限但承认量化贡献有价值\"\n\n- id: \"R12-N3\"\n  summary: \"DRC 作为 Contribution 4 不够充分\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"DRC demoted to practical observation in §6, no longer listed as independent Contribution\"\n  resolution_round: 13\n  first_raised_round: 12\n  last_seen_round: 13\n\n- id: \"R12-W1\"\n  summary: \"BR 可能存在循环论证——56.4%零变量重叠使约束按定义支持source answer\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"shuffle control部分回应, 但未报告语义去重后BR\"\n    - round: 14\n      reviewers: [1]\n      note: \"R14(fresh) R1-W3再次提及BR子集大小. shuffle control(§5.2)确认BR是structural, 但语义去重后BR仍缺\"\n\n- id: \"R12-W2\"\n  summary: \"CIL 名称和 information-theoretic 声称有误导\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Renamed to Conditional Correction Ratio (CCR), removed 'unify' claim, added bootstrap CI\"\n  resolution_round: 13\n  first_raised_round: 12\n  last_seen_round: 13\n\n- id: \"R12-W3\"\n  summary: \"Figure 2 placement——应在正文而非附录\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"当前论文 Figure 2 已在正文 page 7(§5.5 Remediation Analysis 旁)\"\n  resolution_round: 13\n\n- id: \"R12-W4\"\n  summary: \"Appendix vs 主文关键信息分配不合理\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"符号过载, Discussion过短, power analysis埋在附录\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) R2-N2: 8页信息过载(critical→major共识). R1同意§3.1 K_eff推导可压缩. 建议将CJT推导/ProcessSim/CCR移入附录以腾出空间\"\n\n- id: \"R12-EC1\"\n  summary: \"Extractor Confound——所有 frontier cross-model extraction 使用同一 Mistral-7B extractor\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1]\n      note: \"frontier BR≈1 可能反映 extractor 能力而非 SCB 减弱\"\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 未单独提及但Table 2 caption已标注cross-model vs self-extraction区别\"\n\n- id: \"R13-N1\"\n  summary: \"摘要 BR 4.97× 选择性报告——最极端条件, frontier BR≈1\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"摘要应报告 BR 范围或中位数\"\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 未单独提及但Abstract报告BR范围1.66-4.97——可能已部分修复\"\n  action_items:\n    - round: 13\n      action: \"摘要改为报告 BR 范围或中位数\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R13-N2\"\n  summary: \"统计功效呈现不足——10/16 underpowered, power analysis 埋在附录\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"§4.2 需增加 power statement\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) §4.2已有TOST结果和power mention, 但R1仍要求更显著呈现MDE. R2-W1: claim scope超出功效\"\n  action_items:\n    - round: 13\n      action: \"§4.2 增加明确 power statement\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R13-N3\"\n  summary: \"α=0.5 无敏感性分析\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"需在代表性条件上跑α消融\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) R2 REBUT R1-W4: Appendix Table 11已有α∈{0.1-0.9}分析, agreement≥99%. 但Δ(α)未报告. 争议缩窄——现有分析方向正确但可补充Δ维度\"\n\n- id: \"R13-W1\"\n  summary: \"符号/指标过载——8页内7个定量工具\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"建议ProcessSim/CCR移至附录\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) R2再次提及术语负载过重. R1同意\"\n\n- id: \"R13-W2\"\n  summary: \"NLI claim 须限定到命题逻辑任务\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"摘要限定为 'on propositional-logic benchmarks'\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 共识持续: §6标题和结论需限定domain scope\"\n\n- id: \"R13-W3\"\n  summary: \"语法去重可能膨胀 BR——未报告语义去重后 BR\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"建议报告语义去重后BR\"\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 未单独提及但shuffle control(§5.2)部分回应\"\n\n- id: \"R13-W4\"\n  summary: \"Symbolic Mirage Hypothesis §3.3 与 §5 验证状态不连贯\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"§5后续小节未回溯具体prediction编号\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) R1-N2: Predictions 1-2为事后总结非独立预测. R2同意(with nuance). 建议区分归纳vs验证\"\n\n- id: \"R13-W5\"\n  summary: \"缺引: Dhuliawala et al. 2023 Chain-of-Verification\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"当前论文 Related Work §2 已引用 dhuliawala2023chainofverification\"\n  resolution_round: 14\n\n# R14(fresh) 新发现的 issues\n\n- id: \"R14-N1\"\n  summary: \"标题'LLM Reasoning'范围超出实验证据——仅覆盖逻辑推理, 无数学推理\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-N1 critical, R2-W4 major. 交叉后完全共识. GSM8K n=30仅为pilot. 建议标题改为'Formal/Logical Reasoning'或补充数学推理实验(n≥200)\"\n  action_items:\n    - round: 14\n      action: \"标题限定为Formal/Logical Reasoning, 或补充GSM8K/MATH中等规模实验\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R14-N2\"\n  summary: \"Symbolic Mirage Hypothesis Predictions 1-2 为事后总结非独立预测——部分循环论证\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-N2首提(major), R2交叉同意(with nuance: Pred1覆盖9模型超出初始3个为缓和因素). 共识: 仅Prediction 3为独立验证. 建议将Pred 1-2重定位为'observations that motivate the hypothesis'\"\n  action_items:\n    - round: 14\n      action: \"§3.3 区分归纳性观察与独立验证的预测; 降低'Hypothesis'措辞为'Diagnostic Framework'或'Empirical Pattern'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R14-W1\"\n  summary: \"Cross-architecture实验仅6条件/单一verifier类型/仅Mistral-7B显著\"\n  category: experiment\n  severity: major\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W1 major, R2-W2 major. 完全共识. R2指出实际3个NLI架构, 但仅在ProofWriter Mistral-7B组合显著. NLI vs symbolic extraction的task gap需讨论\"\n  action_items:\n    - round: 14\n      action: \"增加generator/verifier组合; 讨论NLI vs 约束逻辑验证的task gap; 结论软化为'preliminary evidence'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R14-W2\"\n  summary: \"8页正文信息过载——§5.5/§6/§7展开不足\"\n  category: writing\n  severity: major\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-N2 critical, R1同意降为major. §5.5仅~15行总结27策略; §6半页; §7约1/3页. R1建议压缩§3.1 K_eff推导以腾出空间\"\n  action_items:\n    - round: 14\n      action: \"压缩§3.1 CJT推导; §5.5增加3-5种代表性策略深度分析; §7 Discussion扩展design principles\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R14-W3\"\n  summary: \"'No evidence of improvement' claim scope与统计功效不完全匹配\"\n  category: framing\n  severity: major\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2-W1 major. R1 REBUT: 统计学准确, 多层证据汇聚. 但R1同意Abstract可加hedge. 部分分歧: R1认为现有表述可接受, R2认为应更审慎\"\n  action_items:\n    - round: 14\n      action: \"Abstract增加power caveat, 如'with Y conditions remaining underpowered for small effects'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R14-W4\"\n  summary: \"BR计算子集大小(n_err)未报告, 高准确率模型可能噪声过大\"\n  category: experiment\n  severity: moderate\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W3首提, R2同意(Gemini n_err≈12). Table 2增加n_err列并为BR提供bootstrap CI\"\n  action_items:\n    - round: 14\n      action: \"Table 2增加BR计算的n_err列\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R14-W5\"\n  summary: \"Related Work遗漏: SETS(2025), MAV(2025), Decomposing Self-Correction(2026)\"\n  category: writing\n  severity: minor-to-major\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [2]\n      note: \"R2-W5首提. R1同意部分(需讨论与test-time scaling工作的关系). 注意部分可能为concurrent submissions. Lightman/Weng已引用(R2交叉回应确认)\"\n  action_items:\n    - round: 14\n      action: \"§2增加SETS(2025)等近期工作讨论, 特别是self-verification正面结果与本文负面结论的边界差异\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R14-W6\"\n  summary: \"Fleiss' κ→ICC近似仅r=0.625中等验证——prevalence paradox可能高估K_eff\"\n  category: method\n  severity: moderate\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1-W2首提, R2同意但指出论文已声明ordinal diagnostic. 建议报告ICC直接计算值做robustness check\"\n  action_items:\n    - round: 14\n      action: \"报告ICC直接计算值与κ对比; 讨论base rate对κ的影响\"\n      assigned_to: \"paper_agent\"\n      status: open"
  }
}
```

</details>

---


### Tool result

_source line 1537 · 2026-05-22T13:37:42.074352+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml\", \"bytes\": 24456}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1538 · 2026-05-22T13:40:33.157221+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "symb_invariant_consensus",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5",
  "report": "# 审稿报告 — Round 14 (Fresh)\n\n**论文**: Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Show No Evidence of Improving LLM Reasoning\n**Venue**: EMNLP 2026 (ARR May 2026)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析；R2: 新颖性+完整性+Related Work+写作质量）\n**审稿模式**: Fresh（重新审稿，无历史轮次记忆）\n\n---\n\n## Summary\n\n本文研究 Self-Consistency (SC) 的一个零成本扩展——Symbolic Invariant Consensus Aggregation (SICA)，从推理链中提取逻辑约束并用 MAX-SAT (Z3) 选择最佳答案。在 6 个开源 LLM（7B–32B）+ 9 个模型（含 frontier）、3 个逻辑推理数据集、3000+ 条件评估上，论文发现 SICA 无显著改善（aggregate sign test: 5+/10−, p=0.30），并将失败归因于 Symbolic Confirmation Bias (SCB)：83.3% 的自提取约束支持错误多数答案（BR 1.66×–4.97×），MAX-SAT 在 94.4% 的问题上退化为 majority voting。论文提出三个诊断工具（K_eff, BR, C₀），测试了 27 种 training-free 补救策略（全部失败），并通过 cross-architecture NLI 验证证明外部验证可打破瓶颈（+6.67pp ProofWriter, p<0.001）。\n\n---\n\n## Strengths\n\n**S1. 统计方法论异常扎实。** McNemar exact test + BH FDR correction + TOST equivalence test + Bootstrap CI + Power analysis 构成四重互补检验体系。10 个 underpowered 条件的 MDE 被透明报告（Appendix E），体现统计诚实性。在负面结果论文中达到极高水准。[R1 S1, R2 S1, 共识]\n\n**S2. 实验规模和系统性覆盖令人信服。** 6 模型 × 3 数据集 × ~3000 condition-evaluations，覆盖 7B–32B 能力谱。Oracle control (+29.90pp Mistral, +14.22pp Qwen-14B FOLIO, +17.17pp ProofWriter) 有效分离 mechanism soundness 与 extraction quality，将问题精确定位到约束提取环节。[R1 S2, R2 S1, 共识]\n\n**S3. 结构性归因超越简单否定。** Shuffle control（BR_null ≈ BR_obs, p>0.7）、process-level independence analysis（ProcessSim 0.69 vs κ 0.46）、CCR 分析（cross-arch CCR>0 vs same-model CCR<0）系统解释了*为什么*失败。这不是\"一个方法不行\"而是对失败机制的量化诊断。[R1 S3, R2 S2, 共识]\n\n**S4. 补救分析近乎穷举。** 27 种 training-free 策略跨 4 类（prompt/method/trace-filtering/scoring）系统测试，全部 neutral-to-negative，显著增强了负面结论的说服力。[R1 S4, R2 S3, 共识]\n\n**S5. 叙事结构清晰自洽。** CJT 理论 → SICA 方法 → 负面实验 → SCB 诊断 → Symbolic Mirage 形式化 → remediation 失败 → cross-arch escape，逻辑链完整。[R1 S5, R2 S5, 共识]\n\n**S6. 附录详尽（~19 页）。** Case studies、prompts、algorithms、ablations、统计分析齐全。[R1 implied, R2 S5, 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1. [critical, 共识] 标题声明范围显著超出实验证据覆盖面。**\n标题说\"LLM Reasoning\"但全部主实验仅覆盖逻辑推理（FOLIO/ProofWriter/LogiQA）。数学推理（GSM8K）仅 n=30 pilot，StrategyQA/ARC-Challenge 仅出现在附录诊断中。当前社区对 symbolic verification 的主要兴趣在数学推理领域——标题 overclaim 是 *ACL 审稿常见降分理由。\n- **R1**: critical（首提）\n- **R2**: major（W4），交叉后同意 R1\n- **建议**: 标题改为\"Formal/Logical Reasoning\"，或补充 GSM8K/MATH 中等规模实验（n≥200）\n\n**N2. [critical→major, 共识] Symbolic Mirage Hypothesis 的验证存在部分循环论证。**\n三个 predictions 中，Prediction 1（BR>1 across architectures）和 Prediction 2（no same-model intervention reduces BR below 1）本质上是对已观察数据的事后总结。只有 Prediction 3（cross-architecture escape）涉及独立数据。\n- **R1**: major（N2, 首提循环论证角度）\n- **R2**: critical（N1, 从新颖性角度；交叉后同意循环论证观点，但指出 Pred1 覆盖 9 模型超出初始 3 个为缓和因素）\n- **建议**: 将 Pred 1-2 重定位为\"observations that motivate the hypothesis\"，仅 Pred 3 为 genuine prediction。降低\"Hypothesis\"措辞为\"Diagnostic Framework\"或\"Empirical Pattern\"\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. [major, 共识] Cross-architecture escape 证据不足以支撑结论强度。**\n仅 6 个条件（4 generators × 1 dataset significant），单一 verifier 类型（NLI），仅 Mistral-7B 组合达到统计显著（+6.67pp, p<0.001）。NLI 三分类与 MAX-SAT 约束验证在任务性质上有本质区别，论文未充分讨论此 task gap。Capability gap 的单调性基于 n=6 数据点（共享 verifier 后有效 n 更小），Limitations 已标注 p=0.167。\n- **R1**: major（W1）\n- **R2**: major（W2），交叉后完全同意\n- **建议**: 增加 generator/verifier 组合；讨论 NLI vs 约束逻辑验证的 task gap；结论措辞软化为\"preliminary evidence\"\n\n**W2. [major, 共识] 8 页正文信息过载，关键贡献展开不足。**\n§5.5（Remediation）仅 ~15 行总结 27 种策略；§6（Cross-Architecture）约半页完成方法+结果+分析；§7（Discussion）被压缩在 page 8 底部约 1/3 页，design principles 各仅一句话。\n- **R2**: critical（N2, 首提）\n- **R1**: 同意但降级为 major（8 页硬限制下空间约束真实存在）\n- **建议**: 压缩 §3.1 CJT/K_eff 推导（非原创公式），将 ProcessSim/CCR 细节移入附录，腾出空间给 §5.5 深度分析 3-5 种代表性策略和 §7 Discussion\n\n**W3. [major, 部分分歧] Claim scope 与统计功效不完全匹配。**\nAbstract \"no evidence of improvement\" 暗示 SICA 确实无效，但 16 个非退化条件中 10 个 underpowered（MDE>2pp at 80% power），仅 4 个通过 TOST 等价检验。\n- **R2**: major（W1）\n- **R1**: REBUT——\"no evidence\"是统计学标准用语（absence of evidence），sign test + bootstrap CI + oracle control + 27 remediation 构成多层证据汇聚。但同意 Abstract 可增加 hedge。\n- **建议**: Abstract 增加 power caveat，如\"with Y conditions remaining underpowered for effects below ~2pp\"\n\n**W4. [moderate, 共识] BR 计算子集大小（n_err）未报告。**\n高准确率模型（SC>80%）上错误子集可能<40题（Gemini-2.5-Pro interim n_err≈12），BR 统计可靠性存疑。\n- **R1**: moderate（W3）\n- **R2**: 同意\n- **建议**: Table 2 增加 n_err 列\n\n**W5. [moderate, 共识] Fleiss' κ 作为 ICC 近似仅有中等经验验证（r=0.625）。**\n高准确率时 Fleiss' κ 系统性偏低（prevalence paradox），可能高估 K_eff。\n- **R1**: moderate（W2）\n- **R2**: 同意，但指出论文已声明 ordinal diagnostic\n- **建议**: 报告 ICC 直接计算值作 robustness check\n\n**W6. [minor-to-major, R2 首提] Related Work 遗漏近期重要工作。**\nSETS (2025, self-verification 正面效果) 与本文负面发现形成直接对比但未被讨论。MAV (2025, multi-agent verification) 与 §6 高度相关。\n- **R1**: 部分同意（需注意 concurrent submissions）\n- **R2**: minor-to-major（W5）\n- **建议**: §2 增加 SETS 等工作讨论，明确本文负面结论的适用边界\n\n**W7. [minor, 共识] TOST equivalence margin ±2pp 选择依据不够充分。**\n论文已有 margin sensitivity（±1/2/3pp），但正文呈现不够显著。\n- **建议**: 在 §4.2 增加 margin sensitivity 结果摘要\n\n### 小问题（不影响接收）\n\n- 术语负载过重（SC/SICA/SCB/CJT/BR/K_eff/C₀/CCR/ProcessSim/DRC/TOST/MDE/FDR），建议增加术语表或减少非核心缩写 [R2, R1 同意]\n- Table 1 \"Type C\" 标注缺少正文解释 [R1]\n- GSM8K pilot (n=30) 应在首次出现处明确标注 \"exploratory only\" [R1]\n- 多种子复制仅覆盖 2/6 模型 [R1, R2]\n- Figure 1 仅展示正常流程，缺少 SCB failure mode 的视觉表现 [R2, R1 同意]\n- Abstract 约 200 词内塞入 5 个技术概念，过于密集 [R2, R1 同意]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **标题必须限定范围**：当前\"LLM Reasoning\"与实验仅覆盖逻辑推理不匹配 [R1-N1, R2-W4]\n2. **Symbolic Mirage Predictions 1-2 非独立验证**：应重定位为归纳性观察 [R1-N2, R2 同意]\n3. **Cross-architecture 证据为 preliminary**：仅 Mistral-7B 组合显著，需软化结论 [R1-W1, R2-W2]\n4. **正文空间分配需优化**：§3.1 CJT 推导可压缩，腾出空间给 §5.5/§6/§7 [R2-N2, R1 同意]\n5. **统计呈现可改善**：BR n_err 报告、TOST margin sensitivity 正文呈现、power statement 前移 [R1-W3/W5, R2-W1]\n6. **Oracle control 是论文核心优势**：有效证明 mechanism soundness 并精确定位失败环节 [R1, R2]\n7. **27 种 remediation 的穷举搜索是重要贡献**：全部失败显著增强负面结论说服力 [R1, R2]\n\n## Reviewer Divergence [REBUT]\n\n1. **Symbolic Mirage 新颖性**\n   - R1（Excitement 3.5/5）: Z3 formal solver 使场景非平凡——论文证明的是\"即使加了 external solver，extraction 仍注入偏差使验证层失效\"，超越 Huang et al. 的一般性 self-correction 框架。BR 量化和退化条件（Eq.4）是新贡献。\n   - R2（Excitement 2.5/5）: 核心发现在 Huang/Stechly 已知结论下可预见性较高。BR 只是简单比例度量。\"Hypothesis\"措辞偏强。\n   - **Director 判断**: R1 的 Z3 区分论点有道理——formal solver 场景确实是 self-correction 文献未覆盖的具体化验证，但 R2 关于概念新颖性有限的评价也合理。建议降低\"Hypothesis\"措辞，但保留 SCB 量化作为独立贡献。\n\n2. **\"No evidence\" 表述**\n   - R1: 统计学标准用语，多层证据汇聚支撑\n   - R2: 10/16 underpowered 时需更审慎\n   - **Director 判断**: 表述技术上准确，但 Abstract 应增加 power caveat 避免过度解读\n\n---\n\n## Questions\n\nQ1. 对 BR > 1 的模型，如果只保留与 ground truth 一致的约束（oracle filter 而非 full oracle），accuracy 如何变化？这比 full oracle 更接近\"提升约束质量\"的实际路径。[R1]\n\nQ2. SETS (2025) 报告 self-verification 在 test-time scaling 中有正面效果。本文负面发现仅限于 symbolic constraint extraction 场景吗？两者机制差异的边界是什么？[R2]\n\nQ3. 27 种 remediation 是否穷尽了合理方法空间？trained constraint extractor 和 ensemble of diverse extractors 是否被考虑过？[R1]\n\nQ4. DeBERTa NLI verifier 的 standalone accuracy 在 FOLIO 上是多少（PW 上已报告 55.00%）？verifier error 与 generator error 的重叠模式如何？[R1, R2]\n\nQ5. QwQ-32B 的高 SC baseline 导致的 ceiling effect 与 SCB 的相对贡献如何区分？[R2；R1 REBUT: 中等 SC regime 同样无改善，SCB 是更根本机制]\n\n---\n\n## Missing References\n\n- SETS (2025, arXiv:2501.19306): self-verification 在 test-time scaling 中的正面结果，与本文负面发现直接对比 [R2, R1 部分同意]\n- MAV (2025, arXiv:2502.20379): 多验证器扩展 test-time compute，与 §6 高度相关 [R2]\n- Reflexion (Shinn et al., 2023): 自然语言反馈 self-correction，与 symbolic extraction 的差异可供讨论 [R1; R2 认为 minor]\n- 注：Lightman et al. (2024) 和 Weng et al. (2023) 已被引用（R2 交叉回应确认）\n\n---\n\n## External Review\n\n**状态**: 未请求（项目未配置外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（0 critical, 2 warning, 20 info）\n\n**Warnings:**\n1. Pages 3–5 连续 3 页无正式 display item（Figure 1 在 p2，Table 1 在 p6，跨度 4 页），审稿人可能产生\"纯文本墙\"印象。p5 的 Empirical Finding 灰色框部分缓解。\n2. 末页（p27 appendix）仅顶部约 10 行文字，~90% 空白。\n\n**正面:**\n- 全文无 margin overflow、公式渲染错误、undefined references\n- 表格全部使用 booktabs 风格，精度统一\n- 颜色使用打印友好\n- 主文 display items 5 个/8 页 = 0.63/页，对分析型论文合理\n- 页数合规：正文 8 页 + Limitations 不计入限制\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 (Borderline Conference)**\n\n**置信度: 4/5**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 4/5 | 4/5 | 4/5 |\n| Excitement | 3.5/5 | 2.5/5 | 3/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Overall | 4 (Conference) | 3.5 (Borderline) | 3.5 (Borderline Conference) |\n\n**综合评分理由:**\n\n本文在方法论严谨性和实验系统性上达到了负面结果论文的高水准（Soundness 4/5），统计分析全面、Oracle control 有效、27 种 remediation 近乎穷举。然而，核心发现的新颖性存在争议（Excitement 2.5–3.5/5）：R1 认为 formal solver 场景的具体化验证有独立价值，R2 认为在 Huang et al. self-correction 框架下可预见。\n\n两个共识问题压低了评分：(1) 标题\"LLM Reasoning\"显著超出实验覆盖面（仅逻辑推理），需限定或补实验；(2) Symbolic Mirage Hypothesis 的三个 predictions 中两个为事后总结，削弱了框架的预测力。Cross-architecture escape 作为建设性出路有价值但证据初步（仅 Mistral-7B 显著）。8 页正文的空间分配需优化。\n\n**如果标题限定范围 + Symbolic Mirage 措辞调整 + Abstract 增加 power caveat，本文可达到 Conference 水准（4.0）。** 核心负面发现（SCB + formal verification layer vacuity）和诊断工具（K_eff, BR, C₀）对 neuro-symbolic reasoning 社区有实际价值。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction (p.1–2)\n- \"No prior work has systematically evaluated this\"（p.1）表述准确但需在 §2 中更充分讨论为什么 symbolic extraction 被预期能不同于一般 self-correction（即 Z3 formal solver 作为 external component 的预期优势）\n- Contributions 列表清晰（3 项），但 Contribution #1 措辞偏强（\"first quantitative characterization\"需确认 Stechly 等人未提供类似量化）\n- Figure 1 pipeline 图清晰，但缺少 SCB failure mode 的可视化\n\n### §2 Related Work (p.3)\n- 覆盖面广（5 段落，~48 引用），specification-generation vs trace-extraction 的三范式分类有效\n- 缺少 SETS (2025) 等 test-time scaling 正面结果的讨论\n- 与 Huang et al. 的增量贡献可以更明确\n\n### §3 Background & Setup (p.4–5)\n- K_eff 公式（Eq.1）来自 Kish/Fleiss，非原创——§3.1 花费约半页推导可压缩\n- SICA pipeline（§3.2）描述完备，Eq.2–4 推导清晰\n- Symbolic Mirage Hypothesis（§3.3）：BR 定义合理，但三个 predictions 中 1-2 为事后归纳\n- Empirical Finding 1-2 的灰色框格式是正面的视觉元素\n\n### §4 Experiments (p.5–6)\n- 模型选择合理（7B–32B + frontier cross-model），数据集覆盖逻辑推理三个子域\n- 超参数（K=12, T=0.7, T_ext=0.3, α=0.5）各有依据\n- Table 1 专业（booktabs, 显著性标记清晰），但 Type C 标注需正文解释\n- Oracle control 是论文最强证据之一\n- §4.2 应在正文增加 power statement 而非仅在 Appendix E\n\n### §5 Analysis (p.6–8)\n- §5.2 SCB 分析是论文核心贡献，shuffle control 优秀\n- §5.3 ProcessSim 和 §5.4 CCR 可考虑移入附录以腾出空间\n- §5.5 Remediation 正文仅~15行，建议深度分析3-5种代表性策略\n\n### §6 Cross-Architecture (p.8)\n- DeBERTa NLI proof-of-concept 有价值但证据初步\n- Table 3 仅 Mistral-7B 显著；capability gap hypothesis 基于 n=6\n- 需讨论 NLI classification vs symbolic extraction 的 task gap\n\n### §7 Discussion (p.8)\n- 被压缩至约 1/3 页，design principles 各仅一句话\n- 对 neuro-symbolic reasoning 社区的实际指导不足\n\n### Limitations (p.9)\n- 覆盖了主要弱点（模型范围、英语仅、untrained extractors、power limitations、capability gap n=6）\n- 简短（约 1/3 页），符合 EMNLP 规范\n\n### 页数合规\n- 正文 8 页 + Limitations 不计入限制 ✓\n- ACL review template ✓\n- Double-blind（Author: Anonymous）✓\n- 无身份泄露检测到 ✓"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5",
    "report": "# 审稿报告 — Round 14 (Fresh)\n\n**论文**: Beyond Self-Consistency: Why Self-Extracted Symbolic Constraints Show No Evidence of Improving LLM Reasoning\n**Venue**: EMNLP 2026 (ARR May 2026)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析；R2: 新颖性+完整性+Related Work+写作质量）\n**审稿模式**: Fresh（重新审稿，无历史轮次记忆）\n\n---\n\n## Summary\n\n本文研究 Self-Consistency (SC) 的一个零成本扩展——Symbolic Invariant Consensus Aggregation (SICA)，从推理链中提取逻辑约束并用 MAX-SAT (Z3) 选择最佳答案。在 6 个开源 LLM（7B–32B）+ 9 个模型（含 frontier）、3 个逻辑推理数据集、3000+ 条件评估上，论文发现 SICA 无显著改善（aggregate sign test: 5+/10−, p=0.30），并将失败归因于 Symbolic Confirmation Bias (SCB)：83.3% 的自提取约束支持错误多数答案（BR 1.66×–4.97×），MAX-SAT 在 94.4% 的问题上退化为 majority voting。论文提出三个诊断工具（K_eff, BR, C₀），测试了 27 种 training-free 补救策略（全部失败），并通过 cross-architecture NLI 验证证明外部验证可打破瓶颈（+6.67pp ProofWriter, p<0.001）。\n\n---\n\n## Strengths\n\n**S1. 统计方法论异常扎实。** McNemar exact test + BH FDR correction + TOST equivalence test + Bootstrap CI + Power analysis 构成四重互补检验体系。10 个 underpowered 条件的 MDE 被透明报告（Appendix E），体现统计诚实性。在负面结果论文中达到极高水准。[R1 S1, R2 S1, 共识]\n\n**S2. 实验规模和系统性覆盖令人信服。** 6 模型 × 3 数据集 × ~3000 condition-evaluations，覆盖 7B–32B 能力谱。Oracle control (+29.90pp Mistral, +14.22pp Qwen-14B FOLIO, +17.17pp ProofWriter) 有效分离 mechanism soundness 与 extraction quality，将问题精确定位到约束提取环节。[R1 S2, R2 S1, 共识]\n\n**S3. 结构性归因超越简单否定。** Shuffle control（BR_null ≈ BR_obs, p>0.7）、process-level independence analysis（ProcessSim 0.69 vs κ 0.46）、CCR 分析（cross-arch CCR>0 vs same-model CCR<0）系统解释了*为什么*失败。这不是\"一个方法不行\"而是对失败机制的量化诊断。[R1 S3, R2 S2, 共识]\n\n**S4. 补救分析近乎穷举。** 27 种 training-free 策略跨 4 类（prompt/method/trace-filtering/scoring）系统测试，全部 neutral-to-negative，显著增强了负面结论的说服力。[R1 S4, R2 S3, 共识]\n\n**S5. 叙事结构清晰自洽。** CJT 理论 → SICA 方法 → 负面实验 → SCB 诊断 → Symbolic Mirage 形式化 → remediation 失败 → cross-arch escape，逻辑链完整。[R1 S5, R2 S5, 共识]\n\n**S6. 附录详尽（~19 页）。** Case studies、prompts、algorithms、ablations、统计分析齐全。[R1 implied, R2 S5, 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1. [critical, 共识] 标题声明范围显著超出实验证据覆盖面。**\n标题说\"LLM Reasoning\"但全部主实验仅覆盖逻辑推理（FOLIO/ProofWriter/LogiQA）。数学推理（GSM8K）仅 n=30 pilot，StrategyQA/ARC-Challenge 仅出现在附录诊断中。当前社区对 symbolic verification 的主要兴趣在数学推理领域——标题 overclaim 是 *ACL 审稿常见降分理由。\n- **R1**: critical（首提）\n- **R2**: major（W4），交叉后同意 R1\n- **建议**: 标题改为\"Formal/Logical Reasoning\"，或补充 GSM8K/MATH 中等规模实验（n≥200）\n\n**N2. [critical→major, 共识] Symbolic Mirage Hypothesis 的验证存在部分循环论证。**\n三个 predictions 中，Prediction 1（BR>1 across architectures）和 Prediction 2（no same-model intervention reduces BR below 1）本质上是对已观察数据的事后总结。只有 Prediction 3（cross-architecture escape）涉及独立数据。\n- **R1**: major（N2, 首提循环论证角度）\n- **R2**: critical（N1, 从新颖性角度；交叉后同意循环论证观点，但指出 Pred1 覆盖 9 模型超出初始 3 个为缓和因素）\n- **建议**: 将 Pred 1-2 重定位为\"observations that motivate the hypothesis\"，仅 Pred 3 为 genuine prediction。降低\"Hypothesis\"措辞为\"Diagnostic Framework\"或\"Empirical Pattern\"\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. [major, 共识] Cross-architecture escape 证据不足以支撑结论强度。**\n仅 6 个条件（4 generators × 1 dataset significant），单一 verifier 类型（NLI），仅 Mistral-7B 组合达到统计显著（+6.67pp, p<0.001）。NLI 三分类与 MAX-SAT 约束验证在任务性质上有本质区别，论文未充分讨论此 task gap。Capability gap 的单调性基于 n=6 数据点（共享 verifier 后有效 n 更小），Limitations 已标注 p=0.167。\n- **R1**: major（W1）\n- **R2**: major（W2），交叉后完全同意\n- **建议**: 增加 generator/verifier 组合；讨论 NLI vs 约束逻辑验证的 task gap；结论措辞软化为\"preliminary evidence\"\n\n**W2. [major, 共识] 8 页正文信息过载，关键贡献展开不足。**\n§5.5（Remediation）仅 ~15 行总结 27 种策略；§6（Cross-Architecture）约半页完成方法+结果+分析；§7（Discussion）被压缩在 page 8 底部约 1/3 页，design principles 各仅一句话。\n- **R2**: critical（N2, 首提）\n- **R1**: 同意但降级为 major（8 页硬限制下空间约束真实存在）\n- **建议**: 压缩 §3.1 CJT/K_eff 推导（非原创公式），将 ProcessSim/CCR 细节移入附录，腾出空间给 §5.5 深度分析 3-5 种代表性策略和 §7 Discussion\n\n**W3. [major, 部分分歧] Claim scope 与统计功效不完全匹配。**\nAbstract \"no evidence of improvement\" 暗示 SICA 确实无效，但 16 个非退化条件中 10 个 underpowered（MDE>2pp at 80% power），仅 4 个通过 TOST 等价检验。\n- **R2**: major（W1）\n- **R1**: REBUT——\"no evidence\"是统计学标准用语（absence of evidence），sign test + bootstrap CI + oracle control + 27 remediation 构成多层证据汇聚。但同意 Abstract 可增加 hedge。\n- **建议**: Abstract 增加 power caveat，如\"with Y conditions remaining underpowered for effects below ~2pp\"\n\n**W4. [moderate, 共识] BR 计算子集大小（n_err）未报告。**\n高准确率模型（SC>80%）上错误子集可能<40题（Gemini-2.5-Pro interim n_err≈12），BR 统计可靠性存疑。\n- **R1**: moderate（W3）\n- **R2**: 同意\n- **建议**: Table 2 增加 n_err 列\n\n**W5. [moderate, 共识] Fleiss' κ 作为 ICC 近似仅有中等经验验证（r=0.625）。**\n高准确率时 Fleiss' κ 系统性偏低（prevalence paradox），可能高估 K_eff。\n- **R1**: moderate（W2）\n- **R2**: 同意，但指出论文已声明 ordinal diagnostic\n- **建议**: 报告 ICC 直接计算值作 robustness check\n\n**W6. [minor-to-major, R2 首提] Related Work 遗漏近期重要工作。**\nSETS (2025, self-verification 正面效果) 与本文负面发现形成直接对比但未被讨论。MAV (2025, multi-agent verification) 与 §6 高度相关。\n- **R1**: 部分同意（需注意 concurrent submissions）\n- **R2**: minor-to-major（W5）\n- **建议**: §2 增加 SETS 等工作讨论，明确本文负面结论的适用边界\n\n**W7. [minor, 共识] TOST equivalence margin ±2pp 选择依据不够充分。**\n论文已有 margin sensitivity（±1/2/3pp），但正文呈现不够显著。\n- **建议**: 在 §4.2 增加 margin sensitivity 结果摘要\n\n### 小问题（不影响接收）\n\n- 术语负载过重（SC/SICA/SCB/CJT/BR/K_eff/C₀/CCR/ProcessSim/DRC/TOST/MDE/FDR），建议增加术语表或减少非核心缩写 [R2, R1 同意]\n- Table 1 \"Type C\" 标注缺少正文解释 [R1]\n- GSM8K pilot (n=30) 应在首次出现处明确标注 \"exploratory only\" [R1]\n- 多种子复制仅覆盖 2/6 模型 [R1, R2]\n- Figure 1 仅展示正常流程，缺少 SCB failure mode 的视觉表现 [R2, R1 同意]\n- Abstract 约 200 词内塞入 5 个技术概念，过于密集 [R2, R1 同意]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **标题必须限定范围**：当前\"LLM Reasoning\"与实验仅覆盖逻辑推理不匹配 [R1-N1, R2-W4]\n2. **Symbolic Mirage Predictions 1-2 非独立验证**：应重定位为归纳性观察 [R1-N2, R2 同意]\n3. **Cross-architecture 证据为 preliminary**：仅 Mistral-7B 组合显著，需软化结论 [R1-W1, R2-W2]\n4. **正文空间分配需优化**：§3.1 CJT 推导可压缩，腾出空间给 §5.5/§6/§7 [R2-N2, R1 同意]\n5. **统计呈现可改善**：BR n_err 报告、TOST margin sensitivity 正文呈现、power statement 前移 [R1-W3/W5, R2-W1]\n6. **Oracle control 是论文核心优势**：有效证明 mechanism soundness 并精确定位失败环节 [R1, R2]\n7. **27 种 remediation 的穷举搜索是重要贡献**：全部失败显著增强负面结论说服力 [R1, R2]\n\n## Reviewer Divergence [REBUT]\n\n1. **Symbolic Mirage 新颖性**\n   - R1（Excitement 3.5/5）: Z3 formal solver 使场景非平凡——论文证明的是\"即使加了 external solver，extraction 仍注入偏差使验证层失效\"，超越 Huang et al. 的一般性 self-correction 框架。BR 量化和退化条件（Eq.4）是新贡献。\n   - R2（Excitement 2.5/5）: 核心发现在 Huang/Stechly 已知结论下可预见性较高。BR 只是简单比例度量。\"Hypothesis\"措辞偏强。\n   - **Director 判断**: R1 的 Z3 区分论点有道理——formal solver 场景确实是 self-correction 文献未覆盖的具体化验证，但 R2 关于概念新颖性有限的评价也合理。建议降低\"Hypothesis\"措辞，但保留 SCB 量化作为独立贡献。\n\n2. **\"No evidence\" 表述**\n   - R1: 统计学标准用语，多层证据汇聚支撑\n   - R2: 10/16 underpowered 时需更审慎\n   - **Director 判断**: 表述技术上准确，但 Abstract 应增加 power caveat 避免过度解读\n\n---\n\n## Questions\n\nQ1. 对 BR > 1 的模型，如果只保留与 ground truth 一致的约束（oracle filter 而非 full oracle），accuracy 如何变化？这比 full oracle 更接近\"提升约束质量\"的实际路径。[R1]\n\nQ2. SETS (2025) 报告 self-verification 在 test-time scaling 中有正面效果。本文负面发现仅限于 symbolic constraint extraction 场景吗？两者机制差异的边界是什么？[R2]\n\nQ3. 27 种 remediation 是否穷尽了合理方法空间？trained constraint extractor 和 ensemble of diverse extractors 是否被考虑过？[R1]\n\nQ4. DeBERTa NLI verifier 的 standalone accuracy 在 FOLIO 上是多少（PW 上已报告 55.00%）？verifier error 与 generator error 的重叠模式如何？[R1, R2]\n\nQ5. QwQ-32B 的高 SC baseline 导致的 ceiling effect 与 SCB 的相对贡献如何区分？[R2；R1 REBUT: 中等 SC regime 同样无改善，SCB 是更根本机制]\n\n---\n\n## Missing References\n\n- SETS (2025, arXiv:2501.19306): self-verification 在 test-time scaling 中的正面结果，与本文负面发现直接对比 [R2, R1 部分同意]\n- MAV (2025, arXiv:2502.20379): 多验证器扩展 test-time compute，与 §6 高度相关 [R2]\n- Reflexion (Shinn et al., 2023): 自然语言反馈 self-correction，与 symbolic extraction 的差异可供讨论 [R1; R2 认为 minor]\n- 注：Lightman et al. (2024) 和 Weng et al. (2023) 已被引用（R2 交叉回应确认）\n\n---\n\n## External Review\n\n**状态**: 未请求（项目未配置外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（0 critical, 2 warning, 20 info）\n\n**Warnings:**\n1. Pages 3–5 连续 3 页无正式 display item（Figure 1 在 p2，Table 1 在 p6，跨度 4 页），审稿人可能产生\"纯文本墙\"印象。p5 的 Empirical Finding 灰色框部分缓解。\n2. 末页（p27 appendix）仅顶部约 10 行文字，~90% 空白。\n\n**正面:**\n- 全文无 margin overflow、公式渲染错误、undefined references\n- 表格全部使用 booktabs 风格，精度统一\n- 颜色使用打印友好\n- 主文 display items 5 个/8 页 = 0.63/页，对分析型论文合理\n- 页数合规：正文 8 页 + Limitations 不计入限制\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 / 5 (Borderline Conference)**\n\n**置信度: 4/5**\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 4/5 | 4/5 | 4/5 |\n| Excitement | 3.5/5 | 2.5/5 | 3/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Overall | 4 (Conference) | 3.5 (Borderline) | 3.5 (Borderline Conference) |\n\n**综合评分理由:**\n\n本文在方法论严谨性和实验系统性上达到了负面结果论文的高水准（Soundness 4/5），统计分析全面、Oracle control 有效、27 种 remediation 近乎穷举。然而，核心发现的新颖性存在争议（Excitement 2.5–3.5/5）：R1 认为 formal solver 场景的具体化验证有独立价值，R2 认为在 Huang et al. self-correction 框架下可预见。\n\n两个共识问题压低了评分：(1) 标题\"LLM Reasoning\"显著超出实验覆盖面（仅逻辑推理），需限定或补实验；(2) Symbolic Mirage Hypothesis 的三个 predictions 中两个为事后总结，削弱了框架的预测力。Cross-architecture escape 作为建设性出路有价值但证据初步（仅 Mistral-7B 显著）。8 页正文的空间分配需优化。\n\n**如果标题限定范围 + Symbolic Mirage 措辞调整 + Abstract 增加 power caveat，本文可达到 Conference 水准（4.0）。** 核心负面发现（SCB + formal verification layer vacuity）和诊断工具（K_eff, BR, C₀）对 neuro-symbolic reasoning 社区有实际价值。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction (p.1–2)\n- \"No prior work has systematically evaluated this\"（p.1）表述准确但需在 §2 中更充分讨论为什么 symbolic extraction 被预期能不同于一般 self-correction（即 Z3 formal solver 作为 external component 的预期优势）\n- Contributions 列表清晰（3 项），但 Contribution #1 措辞偏强（\"first quantitative characterization\"需确认 Stechly 等人未提供类似量化）\n- Figure 1 pipeline 图清晰，但缺少 SCB failure mode 的可视化\n\n### §2 Related Work (p.3)\n- 覆盖面广（5 段落，~48 引用），specification-generation vs trace-extraction 的三范式分类有效\n- 缺少 SETS (2025) 等 test-time scaling 正面结果的讨论\n- 与 Huang et al. 的增量贡献可以更明确\n\n### §3 Background & Setup (p.4–5)\n- K_eff 公式（Eq.1）来自 Kish/Fleiss，非原创——§3.1 花费约半页推导可压缩\n- SICA pipeline（§3.2）描述完备，Eq.2–4 推导清晰\n- Symbolic Mirage Hypothesis（§3.3）：BR 定义合理，但三个 predictions 中 1-2 为事后归纳\n- Empirical Finding 1-2 的灰色框格式是正面的视觉元素\n\n### §4 Experiments (p.5–6)\n- 模型选择合理（7B–32B + frontier cross-model），数据集覆盖逻辑推理三个子域\n- 超参数（K=12, T=0.7, T_ext=0.3, α=0.5）各有依据\n- Table 1 专业（booktabs, 显著性标记清晰），但 Type C 标注需正文解释\n- Oracle control 是论文最强证据之一\n- §4.2 应在正文增加 power statement 而非仅在 Appendix E\n\n### §5 Analysis (p.6–8)\n- §5.2 SCB 分析是论文核心贡献，shuffle control 优秀\n- §5.3 ProcessSim 和 §5.4 CCR 可考虑移入附录以腾出空间\n- §5.5 Remediation 正文仅~15行，建议深度分析3-5种代表性策略\n\n### §6 Cross-Architecture (p.8)\n- DeBERTa NLI proof-of-concept 有价值但证据初步\n- Table 3 仅 Mistral-7B 显著；capability gap hypothesis 基于 n=6\n- 需讨论 NLI classification vs symbolic extraction 的 task gap\n\n### §7 Discussion (p.8)\n- 被压缩至约 1/3 页，design principles 各仅一句话\n- 对 neuro-symbolic reasoning 社区的实际指导不足\n\n### Limitations (p.9)\n- 覆盖了主要弱点（模型范围、英语仅、untrained extractors、power limitations、capability gap n=6）\n- 简短（约 1/3 页），符合 EMNLP 规范\n\n### 页数合规\n- 正文 8 页 + Limitations 不计入限制 ✓\n- ACL review template ✓\n- Double-blind（Author: Anonymous）✓\n- 无身份泄露检测到 ✓"
  }
}
```

</details>

---


### Tool result

_source line 1539 · 2026-05-22T13:40:37.275584+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_970d5ea3f54df81296b97321fcded892:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4118
}
```

</details>

---


### Assistant

_source line 1540 · 2026-05-22T13:40:50.079224+00:00_

审稿报告已投递至 Research Director。

**审稿完成摘要：**

- **Overall: 3.5 (Borderline Conference)**，R1 给 4.0，R2 给 3.5，综合取 3.5
- **2 个 Must-Fix 共识**：(1) 标题"LLM Reasoning"超出实验覆盖（仅逻辑推理）；(2) Symbolic Mirage Hypothesis Predictions 1-2 为事后总结非独立验证
- **7 个 Should-Fix**：cross-architecture 证据初步、信息过载、claim scope 与功效不匹配、BR n_err 未报告、κ→ICC 近似验证中等、近期 Related Work 遗漏、TOST margin 呈现不足
- **核心优势**：统计方法论极高水准、27 种 remediation 穷举搜索、Oracle control 有效定位失败环节、结构性归因超越简单否定
- **升分路径**：标题限定范围 + Mirage 措辞调整 + Abstract 加 power caveat → 可达 4.0 (Conference)

Issue tracker 已同步更新至 `review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 103

## Round 103

2 recorded events


### User

_source line 1541 · 2026-05-22T13:40:52.620964+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

总结：对 R1 的 16 个具体问题/建议，我的回应分布为：
- **[AGREE]**: 10 条（N1, W1, W2, W5, 5 个小问题, Reflexion 引用）
- **[AGREE with nuance]**: 3 条（N2 循环论证, W3 BR 子集）
- **[REBUT]**: 3 条（W4 α 敏感性已有分析, Lightman 和 Weng 已被引用）

核心共识：标题范围、cross-architecture 证据单薄、K_eff 概念新颖性有限。核心分歧：α 敏感性分析已存在但 R1 可能未注意到附录 Table 11；两篇"缺失引用"实际已被引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1542 · 2026-05-22T13:41:08.603322+00:00_

审稿圆桌会议已完成。

**收敛状态**: 关键问题全部达成共识，无需第二轮。

**最终结果**:
- **Overall: 3.5 (Borderline Conference)**
- R1: 4.0 (Conference) / R2: 3.5 (Borderline Conference)
- 2 个 Must-Fix：标题范围超出证据（共识）、Symbolic Mirage Predictions 1-2 循环论证（共识）
- 5 个 Should-Fix：cross-architecture 证据初步、8 页信息过载、claim scope 与功效不完全匹配、BR 子集大小未报告、κ→ICC 近似验证不足
- **核心判断**: 方法论在负面结果论文中达到极高水准（Soundness 4/5），但新颖性存在争议（Excitement 2.5–3.5/5）。标题限定 + Mirage 措辞调整 + power caveat 后可达 Conference 水准。

审稿报告已投递至 Research Director，Issue Tracker 已同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 104

## Round 104

48 recorded events


### User

_source line 1543 · 2026-05-23T00:30:48.937971+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: symb_invariant_consensus
- 论文路径: projects/symb_invariant_consensus/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1544 · 2026-05-23T00:30:54.823725+00:00_

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
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1545 · 2026-05-23T00:30:54.924802+00:00_

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
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1546 · 2026-05-23T00:31:03.756941+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,read_project_file,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch,read_local_file",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,read_project_file,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch,read_local_file",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 1547 · 2026-05-23T00:31:03.807536+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1548 · 2026-05-23T00:31:06.267149+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,read_project_file,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,read_project_file,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1549 · 2026-05-23T00:31:06.367844+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1550 · 2026-05-23T00:31:12.256427+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1551 · 2026-05-23T00:31:12.358197+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1552 · 2026-05-23T00:31:17.129832+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 1553 · 2026-05-23T00:31:19.053087+00:00_

{"result":"# 项目 symb_invariant_consensus 概况\n\n## 实验状态 (167 个)\n\n- **sica_k_sensitivity_14b**: DONE (success) — \n- **exp-011-llama8b**: DONE (failed) — \n- **exp-016-weighted-sc**: DONE (success) — \n- **exp-005**: DONE (negative) — \n- **sica_folio30**: DONE (killed) — \n- **sica_d016_c0_precheck**: DONE (success) — \n- **sica_proofwriter30_v2**: DONE (killed) — \n- **sica_proofwriter30**: DONE (failed) — \n- **sica_aime30_v3**: DONE (killed) — \n- **sica_aime30_v2**: DONE (killed) — \n- **sica_aime30_t07**: DONE (killed) — \n- **mvp_math50_t07**: DONE (killed) — \n- **sica_smoke_5q**: DONE (success) — \n- **smoke-test-5q**: PREPARING (failed) — \n- **crd_folio_main**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp-deberta-ft-combo: Fine-tuned DeBERTa-large on ProofWriter OWA depth-5 achieves near-perfect NLI accuracy (99.67%) and provides massive combo gains over SC baseline when used as external verifier, demonstrating that domain-specific NLI fine-tuning breaks the SCB ceiling by providing truly independent verification signal.（准备中）\n- exp-multi-seed-mistral-folio: Multi-seed replication (seeds 123,456,789) of Mistral-7B × FOLIO-204 shows consistent Δ(SICA-SC) direction across seeds. Baseline seed=42 already available. Combined with Mistral×PW and Qwen2.5×FOLIO/PW multi-seed, provides comprehensive reproducibility evidence for W4 reviewer response.（准备中）\n- exp-multi-seed-qwen25-7b-folio: Multi-seed replication (seeds 123,456,789) of Qwen2.5-7B × FOLIO-204 adds a fourth model family (beyond Qwen2.5-14B, Mistral-7B, LLaMA-8B) for cross-family consistency of SCB. If Δ(SICA-SC)≤0 holds across 7B-scale Qwen as well, it strengthens the scale+architecture invariance claim.（准备中）\n- exp-multi-seed-qwen25: Multi-seed replication (seeds 123,456,789) of Qwen2.5-14B × FOLIO-204 and ProofWriter-600 shows consistent Δ(SICA-SC) direction across seeds. Baseline seed=42: FOLIO Δ=-1.96pp, PW Δ=-2.00pp. 
…[truncated 1730 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1923
}
```

</details>

---


### Tool call

_source line 1554 · 2026-05-23T00:31:19.204186+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_12/submitted.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_12/submitted.pdf"
  }
}
```

</details>

---


### Tool result

_source line 1555 · 2026-05-23T00:31:20.007213+00:00_

This PDF has 27 pages, which is too many to read at once. Use the pages parameter to read specific page ranges (e.g., pages: "1-5"). Maximum 20 pages per request.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1556 · 2026-05-23T00:31:20.007530+00:00_

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
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1557 · 2026-05-23T00:31:20.659927+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1558 · 2026-05-23T00:31:20.710509+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % removed: not available in this TeX distribution
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\usepackage{tcolorbox}
14	\tcbuselibrary{skins}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{enumitem}
19	\usepackage{subcaption}
20	\usepackage{tikz}
21	\usetikzlibrary{arrows.meta,positioning,calc,fit}
22	\usepackage{listings}
23	\usepackage{algorithm}
24	\usepackage{algpseudocode}
25	\usepackage{hyperref}
26	\usepackage{cleveref}
27	
28	\lstset{
29	  basicstyle=\small\ttfamily,
30	  breaklines=true,
31	  frame=single,
32	  xleftmargin=1em,
33	  xrightmargin=1em,
34	  aboveskip=0.5em,
35	  belowskip=0.5em,
36	}
37	
38	\graphicspath{{../figures/paper/}{figures/}}
39	
40	\title{Beyond Self-Consistency: Why Self-Extracted Constraints\\Fail to Improve LLM Logical Reasoning}
41	
42	\author{Anonymous}
43	
44	\begin{document}
45	\maketitle
46	
47	% Tighten spacing for 8-page budget
48	\setlength{\textfloatsep}{5pt plus 2pt minus 4pt}
49	\setlength{\dbltextfloatsep}{5pt plus 2pt minus 4pt}
50	\setlength{\floatsep}{3pt plus 2pt minus 2pt}
51	\setlength{\dblfloatsep}{3pt plus 2pt minus 2pt}
52	\setlength{\abovecaptionskip}{2pt}
53	\setlength{\belowcaptionskip}{0pt}
54	\setlength{\abovedisplayskip}{4pt plus 1pt minus 2pt}
55	\setlength{\belowdisplayskip}{4pt plus 1pt minus 2pt}
56	\setlength{\intextsep}{5pt plus 1pt minus 2pt}
57	
58	\input{abstract}
59	
60	\input{introduction}
61	
62	\input{related_work}
63	
64	\input{method}
65	
66	\input{experiments}
67	
68	\input{analysis}
69	
70	\input{solutions}
71	
72	\input{discussion}
73	
74	\vspace{-1mm}
75	\section*{Limitations}
76	\input{limitations_content}
77	
78	\bibliography{references}
79	
80	\appendix

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1559 · 2026-05-23T00:31:25.778385+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

I found search results related to EMNLP 2026, but the main call for papers for the conference itself was not directly returned.
…[truncated 1184 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 5770
}
```

</details>

---


### Tool call

_source line 1560 · 2026-05-23T00:31:31.809325+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference submission deadline ARR commitment page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference submission deadline ARR commitment page limit"
  }
}
```

</details>

---


### Tool call

_source line 1561 · 2026-05-23T00:31:33.265313+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ACL Rolling Review\" 2026 submission guidelines author instructions page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ACL Rolling Review\" 2026 submission guidelines author instructions page limit"
  }
}
```

</details>

---


### Tool call

_source line 1562 · 2026-05-23T00:31:34.520045+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_12/submitted.pdf",
  "pages": "1-8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_12/submitted.pdf",
    "pages": "1-8"
  }
}
```

</details>

---


### Tool result

_source line 1563 · 2026-05-23T00:31:35.224061+00:00_

PDF pages extracted: 8 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_12/submitted.pdf (637.2KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 704
}
```

</details>

---


### Tool call

_source line 1564 · 2026-05-23T00:31:35.256025+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_12/submitted.pdf",
  "pages": "9-20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_12/submitted.pdf",
    "pages": "9-20"
  }
}
```

</details>

---


### Tool result

_source line 1565 · 2026-05-23T00:31:36.010329+00:00_

PDF pages extracted: 12 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_12/submitted.pdf (637.2KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---


### Tool result

_source line 1566 · 2026-05-23T00:31:36.185519+00:00_

Web search results for query: "EMNLP 2026 main conference submission deadline ARR commitment page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, here's the information about EMNLP 2026 main conference submission:

## ARR Submission Deadline
ARR Submission Deadline: May 25, 2026

## ARR Commitment Policy
Given that the ARR 2026 May 
…[truncated 599 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 4376
}
```

</details>

---


### Tool result

_source line 1567 · 2026-05-23T00:31:39.699505+00:00_

Web search results for query: ""ACL Rolling Review" 2026 submission guidelines author instructions page limit"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"}]

I found information about ACL Rolling Review 2026 submission guidelines. Here's what I found regarding author instructions and page limits:

## Key Submission Guidelines

The submission must adhere to the formatting in the submission templates, which is available as an Overleaf template.

## Page Limits

For ACL 2026 specifically: Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Final versions of accepted papers
…[truncated 1115 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 6434
}
```

</details>

---


### Tool call

_source line 1568 · 2026-05-23T00:31:48.180459+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_12/submitted.pdf",
  "pages": "21-27"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_12/submitted.pdf",
    "pages": "21-27"
  }
}
```

</details>

---


### Tool result

_source line 1569 · 2026-05-23T00:31:48.987720+00:00_

PDF pages extracted: 7 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_12/submitted.pdf (637.2KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 807
}
```

</details>

---


### Tool call

_source line 1570 · 2026-05-23T00:31:49.075454+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers author guidelines anonymity appendix ethics site:2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers author guidelines anonymity appendix ethics site:2026.emnlp.org"
  }
}
```

</details>

---


### Tool result

_source line 1571 · 2026-05-23T00:31:56.450427+00:00_

Web search results for query: "EMNLP 2026 call for papers author guidelines anonymity appendix ethics site:2026.emnlp.org"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"Responsibility is not required for authorship","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12015057/"}]

I found relevant information from the EMNLP 2026 website. Here are the key guidelines related to your search query:

**Anonymity:**
Industry Track submissions must neither include the authors' names nor their affiliations, and the reviewing process will continue to be double-blind, with reviewers not seeing authors, nor will authors see reviewers. Additionally, there is no anonymity period requirement following ACL and ARR policies.

**Appendix:**
Authors are asked not to abuse the option of an unlimited appendix and only to include material that supports the primary messages and content of the paper; for the final papers, especially those with an appendix of excessive length, the EMNLP 2026 Industry Track chairs reserve the right to include a statement that it is not mandatory for reviewers to review the material presented in the appendix.

**Ethics:**
Both long and short paper submissions should follow all of the ARR submission requirements, including ACL's Publication Ethics Policy, and ARR's Ethics Policy including the responsible NLP research checklist
…[truncated 593 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 7374
}
```

</details>

---


### Tool call

_source line 1572 · 2026-05-23T00:32:16.173428+00:00_

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
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
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

_source line 1573 · 2026-05-23T00:32:16.274248+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1574 · 2026-05-23T00:32:22.356619+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "review_issues.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "file": "review_issues.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1575 · 2026-05-23T00:32:23.360752+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1576 · 2026-05-23T00:32:23.361265+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 1577 · 2026-05-23T00:32:23.411753+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1578 · 2026-05-23T00:32:32.849649+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1579 · 2026-05-23T00:32:32.950869+00:00_

1	# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)
2	- id: "R1-C1"
3	  summary: "Method Stage 3 sat() implementation undescribed"
4	  category: method
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 1
8	  last_seen_round: 3
9	  resolution: "Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit."
10	  resolution_round: 3
11	
12	- id: "R1-C2"
13	  summary: "Most experiments underpowered (n≤60), no power analysis"
14	  category: experiment
15	  severity: critical
16	  status: resolved
17	  first_raised_round: 1
18	  last_seen_round: 1
19	  resolution: "Power analysis + Bootstrap CIs added. Larger n conditions (200-600)."
20	  resolution_round: 3
21	
22	- id: "R1-C3"
23	  summary: "Oracle/upper-bound experiment missing"
24	  category: experiment
25	  severity: critical
26	  status: resolved
27	  first_raised_round: 1
28	  last_seen_round: 1
29	  resolution: "Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp."
30	  resolution_round: 3
31	
32	- id: "R1-C4"
33	  summary: "Huang et al. (ICLR 2024) not cited"
34	  category: framing
35	  severity: critical
36	  status: resolved
37	  first_raised_round: 1
38	  last_seen_round: 2
39	  resolution: "Huang, Stechly, Kambhampati all cited and discussed."
40	  resolution_round: 2
41	
42	- id: "R1-C5"
43	  summary: "Critical related work missing"
44	  category: writing
45	  severity: critical
46	  status: resolved
47	  first_raised_round: 1
48	  last_seen_round: 1
49	  resolution: "~48 citations, 5 Related Work paragraphs."
50	  resolution_round: 3
51	
52	- id: "R1-C9"
53	  summary: "Capability trap novelty unclear"
54	  category: framing
55	  severity: critical
56	  status: resolved
57	  first_raised_round: 1
58	  last_seen_round: 3
59	  resolution: "Reframed as regime-dependent analysis with CJT framework."
60	  resolution_round: 3
61	
62	- id: "R3-N1"
63	  summary: "σ(c,a) scoring inconsistent between self-extraction and oracle"
64	  category: method
65	  severity: critical

…[truncated 18535 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1580 · 2026-05-23T00:32:34.808687+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "output_mode": "content",
  "glob": "*.yaml",
  "context": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
    "output_mode": "content",
    "glob": "*.yaml",
    "context": "3"
  }
}
```

</details>

---


### Tool result

_source line 1581 · 2026-05-23T00:32:35.060117+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Grep",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1582 · 2026-05-23T00:32:54.014032+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "output_mode": "content",
  "context": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
    "output_mode": "content",
    "context": "3"
  }
}
```

</details>

---


### Tool result

_source line 1583 · 2026-05-23T00:32:54.918104+00:00_

&lt;persisted-output>
Output too large (60.5KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-review-director-9c155b71/fcf2ed2c-8e75-4747-9f36-2889c2ffd474/tool-results/toolu_012irk5fY4FbPUuP6EoM3WKV.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_8.md-141-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_8.md-142-## External Review (Stanford Agentic Reviewer)
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_8.md-143-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_8.md:144:外部审稿：未配置（项目 config 中 external_review 未启用）。
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_8.md-145-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_8.md-146----
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_8.md-147-
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_3.md-172-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_3.md-173-## External Review
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_3.md-174-
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/round_3.md:175:**外部审稿（Stanford Agentic Reviewer）**: 未请求（项目未配置 `external_review.paperreview_ai.enabled`）。
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_reports/
…[truncated 291 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Grep",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 1584 · 2026-05-23T00:33:31.228650+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "symb_invariant_consensus",
  "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
  }
}
```

</details>

---


### Tool result

_source line 1585 · 2026-05-23T00:33:58.067971+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 26839
}
```

</details>

---


### Tool call

_source line 1586 · 2026-05-23T00:33:59.024052+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计 + 统计推断**。\n\n## 论文信息\n- **标题**: Beyond Self-Consistency: Why Self-Extracted Constraints Fail to Improve LLM Logical Reasoning\n- **论文路径**: projects/symb_invariant_consensus/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_12/submitted.pdf\n\n## Venue 要求 (EMNLP 2026 via ARR)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 + 无限参考文献，Limitations 不计入页数\n- **模板**: ACL template (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind（无作者信息，无自引暴露）\n- **附录**: 允许但审稿人无义务审阅\n\n## 你的审查侧重\n\n### 1. 方法论 (Method)\n- SICA pipeline 完整性：trace generation → constraint extraction → deduplication → MAX-SAT → scoring (Eq. 1-5, Algorithm 1-2)\n- Bias Ratio (BR) 指标定义是否存在循环论证——约束按定义关联 source answer，BR>1 是否部分来自指标设计而非实质性偏差\n- K_eff = K/[1+(K-1)·κ] 作为 diagnostic 的理论基础——Fleiss' κ→ICC 近似在高 prevalence 下的偏差\n- α=0.5 penalty weight 的敏感性（Table 11 显示 ≥99% agreement）\n- \"Symbolic Mirage Hypothesis\" 的 Predictions 1-2 是否为事后总结而非独立预测\n- Empirical Finding 1/2 (tcolorbox) 的严谨性\n\n### 2. 实验设计 (Experiments)\n- 3,000+ condition-evaluations 覆盖度：6 open-source models (7B-32B) + 5 frontier (cross-model extraction)\n- 数据集选择：FOLIO (204), ProofWriter depth-5 (600), LogiQA (200) + exploratory (StrategyQA, GSM8K, AIME)\n- 统计检验：McNemar exact test → BH correction (m=16)，TOST equivalence (±2pp margin) 的合理性\n- **统计功效**：10/16 non-degenerate conditions 为 underpowered（observed power <21%），MDE 远大于观测效应\n- 多种子复制：仅 Mistral-7B (3 seeds) 和 Qwen2.5-14B (4 seeds)，方差大（±2.70pp）\n- Cross-architecture NLI escape (§6)：仅 6 conditions，4/6 共享 DeBERTa verifier，仅 Mistral-7B (SC 39.33%) 显著\n- 27 training-free remediation strategies 的分类和覆盖度\n- Oracle control 实验设计\n\n### 3. 统计推断\n- \"No evidence of improvement\" 的 claim 强度 vs 实际统计功效\n- Aggregate sign test (8+/7−, p=1.00) 的解释力\n- Bootstrap 95% CIs 均包含零——是否支持 \"fail\" 还是 \"underpowered\"\n- Spearman ρ=1.0 (n=6) 用于 capability gap analysis 的有效性\n- BR 95% bootstrap CIs 报告情况\n\n请按以下格式提交审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 severity: critical/major/minor)\n4. **Questions** (需要作者澄清的)\n5. **Missing References** (如有)\n6. **Overall Assessment** (评分 + 置信度)",
  "reviewer_id": "1",
  "project": "symb_invariant_consensus",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计 + 统计推断**。\n\n## 论文信息\n- **标题**: Beyond Self-Consistency: Why Self-Extracted Constraints Fail to Improve LLM Logical Reasoning\n- **论文路径**: projects/symb_invariant_consensus/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_12/submitted.pdf\n\n## Venue 要求 (EMNLP 2026 via ARR)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 + 无限参考文献，Limitations 不计入页数\n- **模板**: ACL template (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind（无作者信息，无自引暴露）\n- **附录**: 允许但审稿人无义务审阅\n\n## 你的审查侧重\n\n### 1. 方法论 (Method)\n- SICA pipeline 完整性：trace generation → constraint extraction → deduplication → MAX-SAT → scoring (Eq. 1-5, Algorithm 1-2)\n- Bias Ratio (BR) 指标定义是否存在循环论证——约束按定义关联 source answer，BR>1 是否部分来自指标设计而非实质性偏差\n- K_eff = K/[1+(K-1)·κ] 作为 diagnostic 的理论基础——Fleiss' κ→ICC 近似在高 prevalence 下的偏差\n- α=0.5 penalty weight 的敏感性（Table 11 显示 ≥99% agreement）\n- \"Symbolic Mirage Hypothesis\" 的 Predictions 1-2 是否为事后总结而非独立预测\n- Empirical Finding 1/2 (tcolorbox) 的严谨性\n\n### 2. 实验设计 (Experiments)\n- 3,000+ condition-evaluations 覆盖度：6 open-source models (7B-32B) + 5 frontier (cross-model extraction)\n- 数据集选择：FOLIO (204), ProofWriter depth-5 (600), LogiQA (200) + exploratory (StrategyQA, GSM8K, AIME)\n- 统计检验：McNemar exact test → BH correction (m=16)，TOST equivalence (±2pp margin) 的合理性\n- **统计功效**：10/16 non-degenerate conditions 为 underpowered（observed power <21%），MDE 远大于观测效应\n- 多种子复制：仅 Mistral-7B (3 seeds) 和 Qwen2.5-14B (4 seeds)，方差大（±2.70pp）\n- Cross-architecture NLI escape (§6)：仅 6 conditions，4/6 共享 DeBERTa verifier，仅 Mistral-7B (SC 39.33%) 显著\n- 27 training-free remediation strategies 的分类和覆盖度\n- Oracle control 实验设计\n\n### 3. 统计推断\n- \"No evidence of improvement\" 的 claim 强度 vs 实际统计功效\n- Aggregate sign test (8+/7−, p=1.00) 的解释力\n- Bootstrap 95% CIs 均包含零——是否支持 \"fail\" 还是 \"underpowered\"\n- Spearman ρ=1.0 (n=6) 用于 capability gap analysis 的有效性\n- BR 95% bootstrap CIs 报告情况\n\n请按以下格式提交审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 severity: critical/major/minor)\n4. **Questions** (需要作者澄清的)\n5. **Missing References** (如有)\n6. **Overall Assessment** (评分 + 置信度)",
    "reviewer_id": "1",
    "project": "symb_invariant_consensus",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1587 · 2026-05-23T00:34:22.031357+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23007
}
```

</details>

---


### Tool call

_source line 1588 · 2026-05-23T00:34:22.333039+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 2，负责**新颖性 + 写作完整性 + 格式合规**。\n\n## 论文信息\n- **标题**: Beyond Self-Consistency: Why Self-Extracted Constraints Fail to Improve LLM Logical Reasoning\n- **论文路径**: projects/symb_invariant_consensus/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_12/submitted.pdf\n\n## Venue 要求 (EMNLP 2026 via ARR)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 + 无限参考文献，Limitations 不计入页数\n- **模板**: ACL template (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind（无作者信息，无自引暴露）\n- **附录**: 允许但审稿人无义务审阅\n- **ARR Overall Assessment评分**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit (含0.5级)\n\n## 你的审查侧重\n\n### 1. 新颖性 (Novelty)\n- 核心 claim \"self-extracted constraints fail\" 相对于以下先验工作的增量贡献：\n  - Huang et al. (ICLR 2024): LLMs cannot self-correct reasoning\n  - Stechly et al. (ICLR 2025): self-verification limitations of LLMs\n  - Wan et al. (ACL Findings 2025): confirmation bias in CoT reasoning\n  - Amonkar et al. (2025): formalization degrades with complexity\n  - Chan et al. (2026): logical soundness unreliable for neurosymbolic fact-checking\n- \"Symbolic Confirmation Bias\" (SCB) 作为新概念的独立性——vs CoT-level confirmation bias\n- K_eff diagnostic framework 作为贡献的价值\n- Independence-accuracy trade-off 是否为 bias-variance 重述\n- 3 contributions 的层级和力度是否足以支撑 EMNLP 长文\n\n### 2. 写作完整性 (Writing)\n- 8 页正文的信息密度和可读性——7 个定量指标 (κ, K_eff, BR, C₀, ProcessSim, CCR, α) 是否过载\n- 主文 vs 附录的关键信息分配：§5.4 remediation analysis 仅约 15 行，§7 Discussion 约 1/3 页\n- Abstract 中 \"BR 1.66-4.97×\" 是否选择性报告\n- \"Symbolic Mirage\" 命名是否过度品牌化\n- Related Work (§2) 引用覆盖度和讨论深度——是否为引用列表而非文献讨论\n- Limitations 章节完整性（是否覆盖关键局限）\n- 叙事连贯性：§3.3 Hypothesis → §5 验证 → §6 Escape → §7 Discussion 的逻辑流\n\n### 3. 格式合规 (Format)\n- 正文是否严格 8 页（检查 §7 Discussion 是否溢出到 page 9）\n- Limitations 位置是否在 references 之前\n- 匿名合规：作者信息、自引、acknowledgments\n- ACL template 使用正确性\n- Figure/Table 编号、引用格式\n- References 格式（natbib/ACL style）\n\n### 4. 遗漏引用 (Missing References)\n请特别关注以下领域是否有遗漏：\n- 2025-2026 年 self-verification / self-correction 新工作\n- Test-time compute scaling 方向\n- Formal verification for LLMs\n- Ensemble diversity / independence 理论\n\n请按以下格式提交审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 severity: critical/major/minor)\n4. **Questions** (需要作者澄清的)\n5. **Missing References** (如有)\n6. **Overall Assessment** (评分 + 置信度)",
  "reviewer_id": "2",
  "project": "symb_invariant_consensus",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 2，负责**新颖性 + 写作完整性 + 格式合规**。\n\n## 论文信息\n- **标题**: Beyond Self-Consistency: Why Self-Extracted Constraints Fail to Improve LLM Logical Reasoning\n- **论文路径**: projects/symb_invariant_consensus/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_12/submitted.pdf\n\n## Venue 要求 (EMNLP 2026 via ARR)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 + 无限参考文献，Limitations 不计入页数\n- **模板**: ACL template (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind（无作者信息，无自引暴露）\n- **附录**: 允许但审稿人无义务审阅\n- **ARR Overall Assessment评分**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit (含0.5级)\n\n## 你的审查侧重\n\n### 1. 新颖性 (Novelty)\n- 核心 claim \"self-extracted constraints fail\" 相对于以下先验工作的增量贡献：\n  - Huang et al. (ICLR 2024): LLMs cannot self-correct reasoning\n  - Stechly et al. (ICLR 2025): self-verification limitations of LLMs\n  - Wan et al. (ACL Findings 2025): confirmation bias in CoT reasoning\n  - Amonkar et al. (2025): formalization degrades with complexity\n  - Chan et al. (2026): logical soundness unreliable for neurosymbolic fact-checking\n- \"Symbolic Confirmation Bias\" (SCB) 作为新概念的独立性——vs CoT-level confirmation bias\n- K_eff diagnostic framework 作为贡献的价值\n- Independence-accuracy trade-off 是否为 bias-variance 重述\n- 3 contributions 的层级和力度是否足以支撑 EMNLP 长文\n\n### 2. 写作完整性 (Writing)\n- 8 页正文的信息密度和可读性——7 个定量指标 (κ, K_eff, BR, C₀, ProcessSim, CCR, α) 是否过载\n- 主文 vs 附录的关键信息分配：§5.4 remediation analysis 仅约 15 行，§7 Discussion 约 1/3 页\n- Abstract 中 \"BR 1.66-4.97×\" 是否选择性报告\n- \"Symbolic Mirage\" 命名是否过度品牌化\n- Related Work (§2) 引用覆盖度和讨论深度——是否为引用列表而非文献讨论\n- Limitations 章节完整性（是否覆盖关键局限）\n- 叙事连贯性：§3.3 Hypothesis → §5 验证 → §6 Escape → §7 Discussion 的逻辑流\n\n### 3. 格式合规 (Format)\n- 正文是否严格 8 页（检查 §7 Discussion 是否溢出到 page 9）\n- Limitations 位置是否在 references 之前\n- 匿名合规：作者信息、自引、acknowledgments\n- ACL template 使用正确性\n- Figure/Table 编号、引用格式\n- References 格式（natbib/ACL style）\n\n### 4. 遗漏引用 (Missing References)\n请特别关注以下领域是否有遗漏：\n- 2025-2026 年 self-verification / self-correction 新工作\n- Test-time compute scaling 方向\n- Formal verification for LLMs\n- Ensemble diversity / independence 理论\n\n请按以下格式提交审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 severity: critical/major/minor)\n4. **Questions** (需要作者澄清的)\n5. **Missing References** (如有)\n6. **Overall Assessment** (评分 + 置信度)",
    "reviewer_id": "2",
    "project": "symb_invariant_consensus",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1589 · 2026-05-23T00:34:23.860229+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1527
}
```

</details>

---


### Assistant

_source line 1590 · 2026-05-23T00:34:33.361457+00:00_

已并行派发：
- **视觉审查 Agent**: fire-and-forget，不阻塞
- **Reviewer 1**: 方法严谨性 + 实验设计 + 统计推断
- **Reviewer 2**: 新颖性 + 写作完整性 + 格式合规

等待两位 Reviewer 返回独立初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 105

## Round 105

2 recorded events


### User

_source line 1591 · 2026-05-23T00:41:15.660118+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见 — Round 1

**论文**: Beyond Self-Consistency: Why Self-Extracted Constraints Fail to Improve LLM Logical Reasoning
**审查侧重**: 新颖性 + 写作完整性 + 格式合规
**Venue**: EMNLP 2026 via ARR

---

## 1. Summary

本文研究 LLM 自提取符号约束能否突破 Self-Consistency (SC) 的投票天花板。通过 SICA pipeline（提取 FOL 约束 → MAX-SAT 求解）在 6 个开源模型、3 个推理域上进行 3000+ 条件评估，发现 SICA 相对 SC 无显著提升。作者将此归因于 "Symbolic Confirmation Bias" (SCB)：83.3% 的自提取约束支持错误的多数答案（BR 1.66–4.97×），且 shuffle control 证实该偏差具有结构性。§6 展示跨架构 NLI 验证可部分逃逸该瓶颈。

---

## 2. Strengths

**S1. 实验设计严谨，统计控制到位**
6 个模型 × 3 个域 × 多种条件，配合 FDR 校正（BH 法）、Bootstrap 95% CI（Appendix F）、TOST 等价性检验（Appendix V）、McNemar 配对检验、统计功效分析（Appendix E, Table 6）。这在 LLM 实证研究中属于上乘水准。

**S2. Shuffle control 设计精巧**
§5.2 的 shuffle control 打乱 constraint-answer 配对后 BR_shuf ≈ BR_orig (p > 0.17)，令人信服地证明偏差来自 trace-count 分布而非提取质量本身。这是本文方法论上最亮眼的一笔。

**S3. 负面结果的社区价值**
在 neuro-symbolic reasoning 方法持续升温的背景下，严格证明"形式化 ≠ 独立验证"对社区有实际指导意义。§6 的 cross-architecture escape 进一步提供了建设性方向。

**S4. 诊断框架有实用价值**
K_eff、BR、C₀ 三个指标组合可快速判断一个 trace-aggregation 方法是否有效。虽然单独看每个指标都非全新（见 W1），但组合使用形成了可操作的评估协议。

**S5. 附录极其详尽**
27 页中 18 页附录，覆盖 prompt 模板（B）、Z3 伪代码（C）、case study（G）、oracle control（H）、failure mode 分类（O）、温度敏感性（M.2）、多种子复现（Y.1）等。可复现性极高。

---

## 3. Weaknesses

**W1 [major] SCB 的概念独立性不足，相对 CoT-level confirmation bias 增量有限**

SCB 的核心机制是：模型的分布先验感染其自生成的输出，无论输出格式是自然语言推理链还是 FOL 约束。Wan et al. (ACL Findings 2025) 已在 CoT 层面建立了 confirmation bias 框架。本文虽然指出 SCB 发生在"形式验证层"（solver 本身可证明正确），但偏差入口是 constraint extraction 而非 solver——因此 SCB 在机制上与 CoT confirmation bias 同构：distributional prior → biased output → downstream process confirms bias。

论文 §3.3 和 §7 未充分论证 SCB 作为独立概念的必要性。如果将 SCB 定位为"confirmation bias 在 formal verification setting 下的实例化"，贡献同样成立但叙事需调整。当前表述暗示 SCB 是一个新类别的偏差，这 overclaim 了概念层面的创新。

**W2 [major] K_eff 作为贡献的新颖性不足**

K_eff = K'/[1+(K'-1)·κ] 是 Kish (1965) 的 effective sample size 直接应用于 voting traces（§3.1 已承认引用 Kish）。将其称为"general diagnostic framework"（Contribution 2, §1）overstates novelty。K_eff 在 survey sampling 和 ensemble learning 中是标准工具。本文的贡献在于将其应用于 LLM trace aggregation 场景并与 CJT 连接，但这属于 application 而非 methodological contribution。

**W3 [major] Independence-accuracy trade-off 与 bias-variance tradeoff 的关系未讨论**

§6 和 Figure 6（Appendix Q）展示跨架构提取获得更高独立性但更低单 trace 准确率的持续权衡。这本质上是 ensemble learning 中的经典 bias-variance tradeoff：多样性更高的 ensemble（更低 correlation/variance）但单个 learner 更弱（更高 bias）。论文 abstract 和 §1 将此作为发现之一报告，但未与 ensemble learning 文献建立任何联系（如 Krogh & Vedelsby 1994, Brown et al. 2005 虽被引但未讨论这一对应关系）。这降低了该发现的 perceived novelty。

**W4 [major] §5.4 Remediation Analysis 主文过薄，无法支撑核心论断**

27 种 training-free 策略的测试是论文论证"self-extraction inherently fails"的关键证据——如果有策略显著有效则主结论被削弱。但主文仅用 ~15 行概述结果（"No strategy achieves significant positive effect after BH correction"），读者无法了解这 27 种策略的分类逻辑、代表性覆盖、或为何全部失败。Figure 2 展示了策略结果但缺乏系统分析。这部分应扩展至至少半页，包括策略分类（prompt-level / filtering / diversity / reranking）及各类别失败的共性原因。

**W5 [minor-major] Abstract 中 "BR 1.66–4.97×" 选择性报告**

Abstract 报告 BR 范围 1.66–4.97× 但未说明这是在模型支持错误多数答案时的测量。Table 2（p7）显示不同模型 BR 差异较大（Mistral-7B 的 BR 高达 4.97，但 LLaMA-3.1-8B 的 BR 为 2.88）。Abstract 选择最极端的范围而非报告中位数或加权均值，有 cherry-picking 之嫌。

**W6 [minor] Related Work (§2) 讨论深度不足**

§2 约 1 页覆盖 4 个子领域，但多处为引用罗列而非深入比较。具体而言：
- Wan et al. (2024) 与本文 SCB 的区别仅用一句话带过（§2 第四段最后一句），但这是最关键的区分点
- 未讨论 MAX-SAT/Z3 之外的形式验证方法（SMT solvers、constraint programming）及 SCB 是否在这些 solver 上同样成立
- 未讨论 trained verifier（如 process reward models, Lightman et al. 2024）与 self-extracted constraints 的根本区别，这对定位本文贡献至关重要

**W7 [minor] §7 Discussion 过短（~1/3 页）**

对于一篇报告大量实证结果的论文，讨论部分应更充分地阐述：
- 对 neuro-symbolic reasoning 议程的启示（当前仅一句提及 self-refinement 和 chain-of-verification）
- 模型规模增大后 SCB 是否会减弱的推测（当前仅限 7B–32B）
- K_eff/BR/C₀ 框架的适用边界
- 与 test-time compute scaling 文献的交叉讨论（自提取约束本质上也是 test-time compute 的一种形式）

**W8 [minor] 指标过载影响可读性**

主文引入 7 个定量指标（κ, K_eff, BR, C₀, ProcessSim, CCR, α）。ProcessSim 和 CCR 主要在附录中使用（§5.3 引入但详细分析在 Appendix P、S），可考虑仅在附录中定义，主文用定性语言描述过程级独立性发现即可。

**W9 [minor] "Symbolic Mirage" 与 "Symbolic Confirmation Bias" 术语关系模糊**

§3.3 标题为 "The Symbolic Mirage Hypothesis"，正文和 §7 混用 "symbolic mirage" 和 "symbolic confirmation bias"。两者是同一现象的不同名称还是假说-机制的关系？需明确界定。Abstract 用 "symbolic confirmation bias"，§3.3 用 "symbolic mirage"，读者在首次阅读时会困惑。

---

## 4. Questions for Authors

**Q1**: SCB 与 Wan et al. (2025) 的 CoT confirmation bias 在机制层面的本质区别是什么？如果一个方法能减轻 CoT confirmation bias，是否预期也能减轻 SCB？如果是，SCB 作为独立概念的价值在哪里？

**Q2**: K_eff 的诊断价值相对于直接计算 inter-trace Fleiss' κ 的附加信息量有多大？实践中何时应该看 K_eff 而非 κ？

**Q3**: §6 的 cross-architecture escape 在 ProofWriter (SC > 72%) 上无显著增益。这是否意味着 escape 策略仅在中等难度/中等基线条件下有效？是否存在一个 SC 阈值，超过该阈值任何外部验证都不再有帮助？

**Q4**: 27 种 training-free remediation 策略中，是否有任何策略在 BH 校正前显示显著正效果？如果有，这些策略的共同特征是什么？

**Q5**: 论文是否考虑过使用 code-specialized LLMs（如 CodeLLaMA、DeepSeek-Coder）进行约束提取？这些模型在形式化方面的能力可能不同于通用指令模型。

---

## 5. Missing References

**M1**: **DuPO: Enabling Reliable LLM Self-Verification via Dual Preference Optimization** (ICLR 2026) — 直接解决 self-verification 可靠性问题的 ICLR 2026 论文，通过训练（而非 prompting）改善自验证。与本文 §6 的"escape requires structural independence"结论直接相关——DuPO 提供了另一条 escape 路径（training-based）。

**M2**: **S²R: Teaching LLMs to Self-verify and Self-correct via Reinforcement Learning** (2025) — 通过 RL 教 LLM 自验证自纠正。本文 Limitations 提到只测试了 training-free 方法，但未在 Related Work 中讨论 training-based self-verification 的进展及其对 SCB 论断的边界条件影响。

**M3**: **"A Reality Check of Language Models as Formalizers on Constraint Satisfaction Problems"** (arXiv 2505.13252, 2025) — 对 LLM 作为形式化器的系统评估，与本文关于 formalization quality 的讨论直接互补。

**M4**: 论文引用了 Krogh & Vedelsby (1994), Brown et al. (2005) 等 ensemble diversity 文献，但未引用 **Lakshminarayanan et al. (2017) "Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles"** — 这篇工作直接量化了 ensemble diversity 与 predictive quality 的关系，与本文 independence-accuracy trade-off 高度相关。

---

## 6. Format Compliance

| 检查项 | 状态 | 备注 |
|--------|------|------|
| 正文页数 | ✅ 8页 | §1-§7 在 pp.1-8 |
| Limitations 位置 | ✅ References 前 | p.9 顶部 |
| 匿名 | ✅ | "Anonymous ACL submission"，未发现自引暴露 |
| ACL 模板 | ✅ | 视觉排版符合 ACL 2-column format |
| Figure/Table 编号 | ✅ | 主文 Figure 1-2, Table 1-3，附录有单独编号 |
| References 格式 | ✅ | natbib/ACL style |
| Limitations 内容量 | ✅ | 约 1/3 页，覆盖 5 个局限点 |

**格式无违规。**

---

## 7. Overall Assessment

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验方法严谨、统计控制充分，但 SCB 概念定义与 CoT confirmation bias 重叠度高，K_eff 贡献被 overstated |
| Excitement | 3/5 | 负面结果有实际价值，但概念创新有限——核心发现可归纳为"已知 confirmation bias 在 formal verification 设置下的又一实例化" |
| Reproducibility | 4/5 | 附录提供 prompt 模板、Z3 伪代码、超参数、seed、统计检验细节，可复现性优秀 |
| Overall Assessment | **3.5** (Borderline Conference) | 实验质量达到会议水准，但概念新颖性在 Conference 与 Findings 之间——SCB 独立性论证不充分、K_eff 新颖性有限、independence-accuracy trade-off 与已知 bias-variance 框架的关系未阐明 |
| Confidence | 4/5 | 熟悉 LLM reasoning、self-consistency、neuro-symbolic 方向，仔细阅读了全文和附录 |

### 一句话总结

一篇实验严谨的实证研究，有效证明了 LLM 自提取符号约束无法超越 SC，但三项声称的概念贡献（SCB、K_eff 框架、independence-accuracy trade-off）相对先验工作的增量有限，需更清晰地定位新颖性边界才能支撑 EMNLP 主会议长文。

### 主要优势
- 实验设计和统计控制在同类工作中属上乘
- Shuffle control 是精巧的方法论创新
- 负面结果对社区有明确的实际指导价值
- 附录完整度极高，可复现性优秀

### 接收建议
当前状态适合 **Findings** 接收。若升至 Conference，需要：(1) 显著加强 SCB 相对 CoT-level confirmation bias 的概念区分论证；(2) 将 K_eff 重新定位为 application 而非 methodological contribution；(3) 正面讨论与 bias-variance tradeoff 的关系。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1592 · 2026-05-23T00:41:30.884189+00:00_

Reviewer 2 初审意见已收到（3.5 Borderline Conference）。等待 Reviewer 1 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 106

## Round 106

2 recorded events


### User

_source line 1593 · 2026-05-23T00:41:42.441305+00:00_

[Reviewer 2 审稿结果]:
审稿完成。总结：

**Overall: 3.5 (Borderline Conference)**，建议 Findings 接收。

核心判断：实验质量优秀（6模型×3域、FDR校正、Bootstrap CI、TOST等价检验、shuffle control），但三项概念贡献的新颖性有限——SCB 与 CoT-level confirmation bias 机制同构（W1）、K_eff 是 Kish effective sample size 的直接应用（W2）、independence-accuracy trade-off 本质是 bias-variance tradeoff（W3）。§5.4 remediation analysis 主文过薄无法支撑"所有 training-free 策略均失败"的强结论（W4）。格式完全合规，无违规项。提出 4 条 missing references（DuPO ICLR 2026、S²R、CSP reality check、Lakshminarayanan 2017）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1594 · 2026-05-23T00:42:00.078436+00:00_

Reviewer 2 已返回。等待 Reviewer 1 完成初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 107

## Round 107

6 recorded events


### User

_source line 1595 · 2026-05-23T00:42:01.585600+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见：方法严谨性 + 实验设计 + 统计推断

## 1. Summary

本文系统评估了符号约束自提取（SICA）能否突破 Self-Consistency（SC）的准确率天花板。通过 6 个开源模型（7B-32B）在 3 个逻辑推理数据集上的 3,000+ condition-evaluations，作者发现 SICA 未能显著超越 SC，并提出"Symbolic Mirage Hypothesis"解释这一负面结果——自提取约束是模型分布先验的投射，而非独立验证信号。论文贡献了三个零成本诊断指标（K_eff, BR, C_0）和跨架构 NLI 验证的概念验证。

这是一篇结构完整、实验规模可观的负面结果论文，诊断框架有实用价值，但统计功效不足削弱了核心 claim 的说服力。

## 2. Strengths

**S1. 评估规模与覆盖度出色。** 3,000+ condition-evaluations 覆盖 6 个开源模型 + 5 个 frontier 模型的跨模型提取、3 个核心逻辑推理数据集 + 3 个探索性数据集，这在负面结果论文中非常罕见。27 种 training-free remediation 策略的穷举式排查（§5.4, Figure 2, Table 14）也增强了结论的稳健性。

**S2. 多重收敛证据策略。** 论文不依赖单一检验，而是通过多条独立证据线汇聚：符号检验（8+/7−, p=1.00）、McNemar + BH 校正（m=16）、Bootstrap 95% CIs、TOST 等价检验、BR 机制分析、ProcessSim 过程独立性分析。这种三角验证方法论值得肯定。

**S3. Oracle 控制实验设计精巧。** Oracle SICA 在 Mistral-7B FOLIO 上 +29.90pp、ProofWriter 上 +17.17pp（Appendix H, §4.2），证明了约束聚合方法在获得高质量约束时确实有效，从而将问题精确定位到自提取环节。这是区分"方法本身无效"和"自提取约束无效"的关键证据。

**S4. 诊断框架具有泛化价值。** K_eff、BR、C_0 三个指标定义清晰（Eq. 1-5），可直接应用于任何 trace-aggregation 方法的事前评估。C_0 作为退化条件零成本检测器（正确分类全部 60 个条件）尤其实用（§5.1）。

**S5. Shuffle 控制分离了偏差来源。** §5.2 的 shuffle 控制保留 per-trace 约束数量但打乱约束-答案关联，结果 BR_real ≈ BR_shuf（p > 0.17），证明偏差来自 trace 计数分布而非提取过程本身。这精确区分了结构性偏差与提取质量问题。

**S6. 跨架构 NLI 概念验证（§6）方向正确。** DeBERTa-large-mnli 在 Mistral-7B 上的显著改善（combo +5.17pp on FOLIO; Table 27: 10/15 条件在 BH 校正后仍显著）为"独立验证信号可以打破 SCB"提供了正面证据，验证了 Prediction 1。

**S7. 论文写作结构清晰。** 正文 8 页高密度，Related Work（§2）分三范式（specification-generation, trace-extraction, trained verifiers）条理分明，Figure 1 pipeline 示意图简洁。附录 18 页提供了充分的复现细节。

## 3. Weaknesses

**W1 [critical] 统计功效严重不足，"fail" 的 claim 强度超出证据支撑。**

论文标题用 "Fail to Improve"（evidence of absence），但 Appendix E Table 6 自报：全部 10 个非退化条件的 observed power < 21%，MDE 远大于观测效应量。最大样本量（n=801, Qwen2.5-14B 聚合）的 MDE 仍为 1.86pp。Bootstrap 95% CIs（Table 7）虽然都包含零，但区间宽度达 ±1.5–2pp，无法排除 ±1pp 量级的真实效应。

这不是"方法无效"的证据，而是"研究无力检测小效应"。根据 ARR reviewer guidelines（H13: "sufficient evidence for the claim"），标题和 Abstract 的 "Fail to Improve" 表述构成 overclaiming（R4）。建议修改为 "No Evidence That Self-Extracted Constraints Improve..." 或明确限定 MDE 范围。

具体数据：
- Table 6: Qwen-14B FOLIO+PW (n=801): MDE = +0.75pp, observed Δ = +0.27pp
- Table 6: LLaMA-3-8B StrategyQA (n=200): MDE = +2.09pp
- Table 7: 全部三个 confirmatory 条件的 95% CI 跨零且宽度 >2pp
- §4.2: "adjusted p = 0.112 for both" nominally significant conditions → BH 校正后无一显著

**W2 [major] "Symbolic Mirage Hypothesis" 的 Predictions 1-2 是事后总结而非独立预测。**

§3.3 将假说表述为两个"testable predictions"，但从论文结构看（§3.3 定义假说 → §4-6 验证），没有任何证据表明这些预测在实验之前被注册或预先制定。Prediction 1（"structurally independent verification should break SCB"）和 Prediction 2（"training-free remediation strategies will fail"）与观察结果完全一致，高度提示事后构造。

这并不意味假说无价值——作为事后解释框架仍有贡献——但以"predictions"框架呈现违反了 ARR guidelines R3（"Hypotheses/speculations presented as conclusions"）的精神。建议明确标注为 exploratory/post-hoc analysis。

**W3 [major] 多种子复制极其有限，方差估计不可靠。**

仅 Mistral-7B（3 seeds）和 Qwen2.5-14B（4 seeds）进行了多种子复制（§4.2, Appendix Y）。Mistral-7B 三种子方差 ±2.70pp——这个方差量级已超过大多数观测效应量。其余 4 个开源模型仅单种子运行。

关键矛盾：如果种子间方差为 ±2.70pp 而观测效应量多在 ±1–2pp 范围，那么单种子结果的可信度严重不足。论文应在更多模型上进行至少 3 种子复制，或至少诚实讨论单种子结果的局限性。

**W4 [major] Bias Ratio (BR) 指标存在部分循环论证风险。**

BR(M,T) 的分子是约束支持错误多数答案的概率，但约束按定义从产生该答案的 trace 中提取。当多数答案错误时，更多 trace 产生错误答案 → 更多约束来自这些 trace → 这些约束自然支持错误答案。BR > 1 部分是 trace 计数不平衡的数学必然，而非仅仅反映"偏差"。

Shuffle 控制（§5.2）实际上确认了这一点（BR_real ≈ BR_shuf），但论文将此解读为"structural bias"的证据。我同意这支持论文的核心论点（自提取约束无法提供独立信号），但论文应更明确区分：(a) BR 测量的是方法的结构性局限，而非 (b) 提取过程的"质量问题"。当前措辞时而混淆两者（e.g., §5.2 "confirmation bias" 暗示提取质量问题，但 shuffle 控制表明是计数分布问题）。

**W5 [major] 跨架构 NLI 验证（§6）证据偏薄，结论外推过度。**

- 仅在 Mistral-7B（SC 39.33%，最弱模型）上显著
- 4/6 main conditions 共享 DeBERTa 系列 verifier（虽然架构不同）
- FOLIO 仅 n=204，ProofWriter n=600
- §6 结论"cross-architecture NLI escapes the mirage for generators up to SC ≈ 70%（§6）"——但实际只在 SC < 40% 验证，SC 40-70% 区间无数据支撑
- Table 3 显示随生成器能力上升 combo gain 单调递减，最强生成器（Qwen2.5-14B, SC > 70%）无显著改善

建议限制 claim 为 "works on weak generators (SC < 40%)"，或补充中等能力模型的证据。

**W6 [minor] Spearman ρ = −1.0 (n=6) 用于 capability gap analysis 过于脆弱。**

§6 Figure 7 报告 ρ = −1.0, p = 0.003（6 个 verifier-generator pairs），用以支持 combo gain 与 capability gap 的单调关系。虽然 p 值在统计上显著，但 n=6 意味着任何一对排名互换都会使 ρ 大幅下降（约至 0.89–0.94），且完美负相关在如此小的 n 下不排除是偶然。这一发现是 suggestive 但远非 definitive，建议降低 claim 强度或增加数据点。

**W7 [minor] K_eff = K/[1+(K-1)·κ] 中 Fleiss' κ → ICC 近似的理论基础薄弱。**

§3.1 使用 Fleiss' κ 作为 ICC 的 proxy 计算 K_eff，但 κ 是分类变量的一致性度量，而 ICC 假定连续变量。在高 prevalence（一个答案主导）下，κ 受 prevalence paradox 影响会偏低，导致 K_eff 偏高。论文承认 K_eff 仅作为"ordinal diagnostic"，这在一定程度上缓解了问题。但既然 prevalence paradox 使 K_eff 偏高（即实际有效样本量更低），这实际上强化了论文的论点——不过应在正文中明确讨论这一方向性偏差。

**W8 [minor] α=0.5 penalty weight 的敏感性分析结论过强。**

Table 11（附录）显示 α 在 [0, 1] 范围内 ≥99% agreement，论文以此论证 α 选择不影响结果。但当主效应本身接近零时，penalty 项的影响自然可忽略——这是 ceiling effect 而非真正的鲁棒性。若 SICA 在某些条件下显示 non-trivial 改善，α 敏感性可能更明显。这一分析的结论应加限定。

## 4. Questions

**Q1.** 论文是否考虑过在 claim 强度上区分 "absence of evidence" vs "evidence of absence"？鉴于 power < 21%，是否愿意将标题和 Abstract 中的 "Fail" 修改为更审慎的表述？

**Q2.** Symbolic Mirage Hypothesis 是在实验结果观察到之后形成的，还是有预注册或先验设计？如果是事后的，能否在论文中明确标注？

**Q3.** 种子间方差 ±2.70pp（Mistral-7B, Appendix Y）超过了多数条件的观测效应量。作者对其余 4 个模型的单种子结果有多少信心？是否有计划补充更多种子？

**Q4.** §6 claim "generators up to SC ≈ 70%" 的依据是什么？实际验证只覆盖 SC < 40%（Mistral-7B），中间区域无数据。

**Q5.** BR > 1 在 SC 正确时是否也成立？论文主要分析了 SC 错误时的 BR，但如果 SC 正确时 BR 也 > 1，这会改变 BR 的解释——说明约束普遍偏向多数答案而非特异性地偏向错误答案。

**Q6.** Empirical Finding 1 和 2（§3.3 tcolorbox）的数学形式化看似严格，但 Δ_emp 和 Δ_total 的 bound 是经验观测还是理论推导？如果是经验的，应标注为 empirical observations 而非 findings。

## 5. Missing References

- **Wang et al. (2024), "Self-Evaluation Improves Selective Generation in LLMs"**: 直接相关的自评估工作，讨论了 self-generated feedback 的局限性。
- **Stechly et al. (2024), "Self-Verification in LLMs is Fundamentally Limited"**: 与本文 Symbolic Mirage Hypothesis 高度相关的独立工作，应在 Related Work 中讨论并对比。
- 建议在 §2 明确对比 Stechly et al. (2024) 与本文的异同——两者结论方向一致但方法路径不同（前者关注 self-verification 的理论界限，本文关注符号约束提取的实证失败）。

## 6. Overall Assessment

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 (Acceptable) | 方法论总体合理，pipeline 定义清晰（Eq. 1-5, Alg. 1-2），多重收敛证据策略得当。但 power < 21% 严重削弱核心 claim，标题构成 overclaiming，BR 循环论证风险未充分讨论。 |
| Excitement | 3/5 (Interesting) | 负面结果对社区有价值（ARR H6），诊断框架（K_eff, BR, C_0）可迁移到其他方法。但研究主要是"验证某方法不 work"而非提出新方法，影响力受限于研究范围。 |
| Confidence | 4/5 (Quite Sure) | 熟悉 LLM 推理、符号推理、统计检验方法论。仔细阅读了正文和全部附录。 |

### Overall Assessment: **3.5 — Borderline Conference**

**一句话总结**: 一篇实验规模可观、诊断框架有价值的负面结果论文，但 power < 21% 下以 "Fail" 定性的 claim 强度超出了统计证据的支撑范围，核心结论需从 "evidence of absence" 降级为 "absence of evidence"。

**接收理由**: 3,000+ 条件的系统评估、可迁移的诊断工具集（K_eff, BR, C_0）、27 种 remediation 策略的穷举排查、跨架构 NLI 的概念验证——这些构成了对社区有意义的贡献。

**拒绝风险**: 核心 claim 超出证据支撑（W1）、假说框架的 post-hoc 性质未披露（W2）、多种子复制不足（W3）。如果作者能在 camera-ready 中 (1) 调整 claim 措辞、(2) 补充 2-3 个模型的多种子、(3) 明确标注假说的 exploratory 性质，则可达到 Conference 水平。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1596 · 2026-05-23T00:42:43.670433+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Weakness：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供具体证据（cite 论文中的 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n**Overall: 3.5 (Borderline Conference)**\n\n### Strengths\n- S1: 实验设计严谨，统计控制到位（6模型×3域，FDR校正，Bootstrap CI，TOST，McNemar）\n- S2: Shuffle control 设计精巧（§5.2，BR_shuf ≈ BR_orig, p>0.17）\n- S3: 负面结果的社区价值\n- S4: 诊断框架有实用价值（K_eff + BR + C₀）\n- S5: 附录极其详尽，可复现性高\n\n### Weaknesses\n**W1 [major] SCB 的概念独立性不足，相对 CoT-level confirmation bias 增量有限。** SCB 核心机制是模型分布先验感染自生成输出，与 Wan et al. (2025) 的 CoT confirmation bias 在机制层面同构：distributional prior → biased output → downstream process confirms bias。论文未充分论证 SCB 作为独立概念的必要性。\n\n**W2 [major] K_eff 作为贡献的新颖性不足。** K_eff = K/[1+(K-1)·κ] 是 Kish (1965) effective sample size 的直接应用。将其称为\"general diagnostic framework\"(Contribution 2) overstates novelty。\n\n**W3 [major] Independence-accuracy trade-off 与 bias-variance tradeoff 的关系未讨论。** §6 展示的权衡本质上是 ensemble learning 经典 bias-variance tradeoff，但论文未与 ensemble learning 文献建立联系。\n\n**W4 [major] §5.4 Remediation Analysis 主文过薄（~15行），无法支撑核心论断。** 27种策略的分类逻辑、代表性覆盖、各类失败的共性原因均未在主文展开。\n\n**W5 [minor-major] Abstract 中 \"BR 1.66–4.97×\" 选择性报告。** 未报告中位数或加权均值，有 cherry-picking 之嫌。\n\n**W6 [minor] Related Work (§2) 讨论深度不足。** Wan et al. 与 SCB 的区别仅一句话；未讨论 trained verifier (PRM) 与 self-extracted constraints 的根本区别。\n\n**W7 [minor] §7 Discussion 过短（~1/3页）。** 未充分讨论：neuro-symbolic 启示、规模扩展后 SCB 趋势、test-time compute scaling 交叉讨论。\n\n**W8 [minor] 指标过载（7个定量指标），ProcessSim 和 CCR 可移至附录。**\n\n**W9 [minor] \"Symbolic Mirage\" 与 \"Symbolic Confirmation Bias\" 术语关系模糊。**\n\n### Missing References\n- M1: DuPO (ICLR 2026) — training-based self-verification\n- M2: S²R (2025) — RL-based self-verification\n- M3: LLM as Formalizers on CSP (arXiv 2505.13252)\n- M4: Lakshminarayanan et al. (2017) Deep Ensembles\n\n---\n\n请对每个 W1-W9 和 Missing References 逐条给出 [AGREE] 或 [REBUT] 回应。",
  "reviewer_id": "1",
  "project": "symb_invariant_consensus",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Weakness：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供具体证据（cite 论文中的 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n**Overall: 3.5 (Borderline Conference)**\n\n### Strengths\n- S1: 实验设计严谨，统计控制到位（6模型×3域，FDR校正，Bootstrap CI，TOST，McNemar）\n- S2: Shuffle control 设计精巧（§5.2，BR_shuf ≈ BR_orig, p>0.17）\n- S3: 负面结果的社区价值\n- S4: 诊断框架有实用价值（K_eff + BR + C₀）\n- S5: 附录极其详尽，可复现性高\n\n### Weaknesses\n**W1 [major] SCB 的概念独立性不足，相对 CoT-level confirmation bias 增量有限。** SCB 核心机制是模型分布先验感染自生成输出，与 Wan et al. (2025) 的 CoT confirmation bias 在机制层面同构：distributional prior → biased output → downstream process confirms bias。论文未充分论证 SCB 作为独立概念的必要性。\n\n**W2 [major] K_eff 作为贡献的新颖性不足。** K_eff = K/[1+(K-1)·κ] 是 Kish (1965) effective sample size 的直接应用。将其称为\"general diagnostic framework\"(Contribution 2) overstates novelty。\n\n**W3 [major] Independence-accuracy trade-off 与 bias-variance tradeoff 的关系未讨论。** §6 展示的权衡本质上是 ensemble learning 经典 bias-variance tradeoff，但论文未与 ensemble learning 文献建立联系。\n\n**W4 [major] §5.4 Remediation Analysis 主文过薄（~15行），无法支撑核心论断。** 27种策略的分类逻辑、代表性覆盖、各类失败的共性原因均未在主文展开。\n\n**W5 [minor-major] Abstract 中 \"BR 1.66–4.97×\" 选择性报告。** 未报告中位数或加权均值，有 cherry-picking 之嫌。\n\n**W6 [minor] Related Work (§2) 讨论深度不足。** Wan et al. 与 SCB 的区别仅一句话；未讨论 trained verifier (PRM) 与 self-extracted constraints 的根本区别。\n\n**W7 [minor] §7 Discussion 过短（~1/3页）。** 未充分讨论：neuro-symbolic 启示、规模扩展后 SCB 趋势、test-time compute scaling 交叉讨论。\n\n**W8 [minor] 指标过载（7个定量指标），ProcessSim 和 CCR 可移至附录。**\n\n**W9 [minor] \"Symbolic Mirage\" 与 \"Symbolic Confirmation Bias\" 术语关系模糊。**\n\n### Missing References\n- M1: DuPO (ICLR 2026) — training-based self-verification\n- M2: S²R (2025) — RL-based self-verification\n- M3: LLM as Formalizers on CSP (arXiv 2505.13252)\n- M4: Lakshminarayanan et al. (2017) Deep Ensembles\n\n---\n\n请对每个 W1-W9 和 Missing References 逐条给出 [AGREE] 或 [REBUT] 回应。",
    "reviewer_id": "1",
    "project": "symb_invariant_consensus",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1597 · 2026-05-23T00:43:12.158961+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 28488
}
```

</details>

---


### Tool call

_source line 1598 · 2026-05-23T00:43:12.662111+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Weakness：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供具体证据（cite 论文中的 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n**Overall: 3.5 (Borderline Conference)**\n\n### Strengths\n- S1: 评估规模与覆盖度出色（3,000+ condition-evaluations，27种remediation策略穷举）\n- S2: 多重收敛证据策略（符号检验+McNemar+BH+Bootstrap+TOST+BR+ProcessSim三角验证）\n- S3: Oracle 控制实验设计精巧（Mistral-7B FOLIO +29.90pp，定位问题到自提取环节）\n- S4: 诊断框架泛化价值（K_eff, BR, C₀ 可应用于任何 trace-aggregation 方法）\n- S5: Shuffle 控制分离偏差来源（BR_real ≈ BR_shuf, p>0.17）\n- S6: 跨架构 NLI 概念验证方向正确\n- S7: 写作结构清晰\n\n### Weaknesses\n**W1 [critical] 统计功效严重不足，\"Fail\" claim 超出证据支撑。** 全部10个非退化条件 observed power < 21%，MDE远大于观测效应量。Bootstrap 95% CIs 区间宽度达 ±1.5-2pp，无法排除 ±1pp 量级的真实效应。这不是\"方法无效\"的证据，而是\"研究无力检测小效应\"。标题 \"Fail to Improve\" 构成 overclaiming（ARR R4）。\n\n**W2 [major] \"Symbolic Mirage Hypothesis\" 的 Predictions 1-2 是事后总结而非独立预测。** 从论文结构看无预注册证据，Prediction 1-2 与观察完全一致，高度提示事后构造。以 \"predictions\" 框架呈现违反 ARR R3 精神。\n\n**W3 [major] 多种子复制极其有限，方差估计不可靠。** 仅 Mistral-7B（3 seeds, ±2.70pp）和 Qwen2.5-14B（4 seeds）。种子间方差超过多数观测效应量，其余4个模型单种子运行。\n\n**W4 [major] BR 指标存在部分循环论证风险。** 当多数答案错误时，更多trace产生错误答案→更多约束来自这些trace→约束自然支持错误答案。BR>1部分是trace计数不平衡的数学必然。论文措辞时而混淆\"结构性局限\"与\"提取质量问题\"。\n\n**W5 [major] 跨架构NLI验证（§6）证据偏薄，结论外推过度。** 仅在SC<40%的Mistral-7B上显著，4/6条件共享DeBERTa系列verifier，\"SC≈70%\"的claim无数据支撑。\n\n**W6 [minor] Spearman ρ=-1.0 (n=6) capability gap analysis 过于脆弱。** n=6下完美负相关不排除偶然，任一排名互换ρ大幅下降。\n\n**W7 [minor] K_eff 中 Fleiss' κ→ICC 近似的理论基础薄弱。** 高prevalence下κ受prevalence paradox影响偏低→K_eff偏高。\n\n**W8 [minor] α=0.5 敏感性分析结论过强。** ≥99% agreement 是主效应接近零时的 ceiling effect，非真正鲁棒性。\n\n### Missing References\n- Wang et al. (2024) Self-Evaluation Improves Selective Generation\n- Stechly et al. (2024) Self-Verification Fundamentally Limited\n\n---\n\n请对每个 W1-W8 和 Missing References 逐条给出 [AGREE] 或 [REBUT] 回应。",
  "reviewer_id": "2",
  "project": "symb_invariant_consensus",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Weakness：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供具体证据（cite 论文中的 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n**Overall: 3.5 (Borderline Conference)**\n\n### Strengths\n- S1: 评估规模与覆盖度出色（3,000+ condition-evaluations，27种remediation策略穷举）\n- S2: 多重收敛证据策略（符号检验+McNemar+BH+Bootstrap+TOST+BR+ProcessSim三角验证）\n- S3: Oracle 控制实验设计精巧（Mistral-7B FOLIO +29.90pp，定位问题到自提取环节）\n- S4: 诊断框架泛化价值（K_eff, BR, C₀ 可应用于任何 trace-aggregation 方法）\n- S5: Shuffle 控制分离偏差来源（BR_real ≈ BR_shuf, p>0.17）\n- S6: 跨架构 NLI 概念验证方向正确\n- S7: 写作结构清晰\n\n### Weaknesses\n**W1 [critical] 统计功效严重不足，\"Fail\" claim 超出证据支撑。** 全部10个非退化条件 observed power < 21%，MDE远大于观测效应量。Bootstrap 95% CIs 区间宽度达 ±1.5-2pp，无法排除 ±1pp 量级的真实效应。这不是\"方法无效\"的证据，而是\"研究无力检测小效应\"。标题 \"Fail to Improve\" 构成 overclaiming（ARR R4）。\n\n**W2 [major] \"Symbolic Mirage Hypothesis\" 的 Predictions 1-2 是事后总结而非独立预测。** 从论文结构看无预注册证据，Prediction 1-2 与观察完全一致，高度提示事后构造。以 \"predictions\" 框架呈现违反 ARR R3 精神。\n\n**W3 [major] 多种子复制极其有限，方差估计不可靠。** 仅 Mistral-7B（3 seeds, ±2.70pp）和 Qwen2.5-14B（4 seeds）。种子间方差超过多数观测效应量，其余4个模型单种子运行。\n\n**W4 [major] BR 指标存在部分循环论证风险。** 当多数答案错误时，更多trace产生错误答案→更多约束来自这些trace→约束自然支持错误答案。BR>1部分是trace计数不平衡的数学必然。论文措辞时而混淆\"结构性局限\"与\"提取质量问题\"。\n\n**W5 [major] 跨架构NLI验证（§6）证据偏薄，结论外推过度。** 仅在SC<40%的Mistral-7B上显著，4/6条件共享DeBERTa系列verifier，\"SC≈70%\"的claim无数据支撑。\n\n**W6 [minor] Spearman ρ=-1.0 (n=6) capability gap analysis 过于脆弱。** n=6下完美负相关不排除偶然，任一排名互换ρ大幅下降。\n\n**W7 [minor] K_eff 中 Fleiss' κ→ICC 近似的理论基础薄弱。** 高prevalence下κ受prevalence paradox影响偏低→K_eff偏高。\n\n**W8 [minor] α=0.5 敏感性分析结论过强。** ≥99% agreement 是主效应接近零时的 ceiling effect，非真正鲁棒性。\n\n### Missing References\n- Wang et al. (2024) Self-Evaluation Improves Selective Generation\n- Stechly et al. (2024) Self-Verification Fundamentally Limited\n\n---\n\n请对每个 W1-W8 和 Missing References 逐条给出 [AGREE] 或 [REBUT] 回应。",
    "reviewer_id": "2",
    "project": "symb_invariant_consensus",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1599 · 2026-05-23T00:43:14.226625+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1564
}
```

</details>

---


### Assistant

_source line 1600 · 2026-05-23T00:43:19.218199+00:00_

交叉分享已发送。等待两位 Reviewer 返回 [AGREE]/[REBUT] 逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 108

## Round 108

2 recorded events


### User

_source line 1601 · 2026-05-23T00:43:21.763274+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**3.5 (Borderline Conference)**。论文实验覆盖广（3,000+ conditions）、诊断框架（K_eff, BR, C_0）有泛化价值、Oracle 控制设计精巧，但三个关键问题制约了评分：

1. **[Critical] 功效不足 vs claim 强度**：全部条件 power < 21%，标题 "Fail to Improve" 属于 overclaiming——实际证据仅支持 "absence of evidence" 而非 "evidence of absence"
2. **[Major] 假说框架事后构造**：Symbolic Mirage Hypothesis 的两个 "predictions" 高度 suggestive 为 post-hoc，但以预测框架呈现
3. **[Major] 多种子复制不足**：仅 2/6 模型有多种子（3-4 seeds），种子方差 ±2.70pp 已超过多数观测效应量

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1602 · 2026-05-23T00:43:41.796087+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 109

## Round 109

2 recorded events


### User

_source line 1603 · 2026-05-23T00:44:53.615589+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 交叉回应 Reviewer 2 审稿意见

---

## Weaknesses 逐条回应

**[AGREE] R2-W1: SCB 概念独立性不足。**
同意 R2 的核心判断。SCB 的机制链（distributional prior → biased self-generated output → downstream confirmation）与 Wan et al. (2025) 的 CoT confirmation bias 在因果结构上确实同构。论文 §2 仅用一句话区分（"SCB is specific to formal verification: the solver is provably sound, yet its outputs are informationally vacuous because self-extracted inputs carry the model's distributional prior"），但这个区分不够有力——"formal verification layer adds no information beyond majority voting"（§4.2）本身说明符号层只是 SC 的重新包装，并未引入新的失败模式。

不过我认为 R2 可能略微 overstate 了问题：SCB 的贡献不在于发现新偏差类型，而在于**量化**这种偏差在形式化验证管道中的具体表现（BR 1.66–4.97×, §5.2），以及证明 Z3 solver 的 provable soundness 无法弥补 input 偏差。这是对已知现象在新场景的实证深化，虽非概念创新，但有 empirical value。建议作者在 §2 或 §3.3 更坦诚地承认与 CoT confirmation bias 的机制同构性，并将 SCB 定位为该现象在符号约束管道中的特例而非独立概念。

---

**[AGREE] R2-W2: K_eff 新颖性有限。**
完全同意。K_eff = K/[1+(K−1)·κ] 直接来自 Kish (1965) effective sample size 公式，论文自己在 §3.1 引用了 Kish (1965) 和 Fleiss (1971)。将一个 60 年前的标准公式应用于 LLM trace 分析并称之为 "general diagnostic framework"（Contribution 2）确实 overstates novelty。

我在 R1 审稿中已指出 κ→ICC 近似的理论薄弱性（R1-W7）——prevalence paradox 使 K_eff 偏高。不过公平地说，K_eff 作为 ordinal diagnostic 仍有实用价值（§3.1 "ordinal diagnostic of vote diversity rather than a literal effective sample size"），问题仅在于贡献声称的措辞。建议将 Contribution 2 从 "general diagnostic framework" 降级为 "application of established diagnostics to trace-aggregation evaluation"。

---

**[AGREE] R2-W3: 未与 ensemble learning bias-variance tradeoff 建立联系。**
同意。§6 的 independence-accuracy trade-off 本质上是：使用独立但较弱的 verifier（DeBERTa NLI）引入更多 variance 但降低了 correlated bias，这是 ensemble learning 的经典权衡。Lakshminarayanan et al. (2017) Deep Ensembles 通过独立初始化降低预测相关性的策略与 §6 的跨架构验证在原理上相通。

论文应在 §6 或 §7 补充与 ensemble diversity 文献的联系，特别是 (a) 为什么独立性带来的 variance 在弱生成器上被 bias 减少所补偿（Table 3: Mistral-7B combo +5.17pp），(b) 为什么在强生成器上 variance 代价超过 bias 收益（Table 3: Qwen2.5-14B 无显著改善）。这也会自然回应我自己在 R1-W5 中关于 §6 证据偏薄的顾虑——将其框架为 ensemble diversity 问题可以增加理论深度。

---

**[REBUT] R2-W4: §5.4 Remediation Analysis 主文过薄。**
部分反驳。R2 认为 ~15 行无法支撑核心论断，但我认为需要区分两种情况：

1. **27 种策略的穷举 listing 本身不适合主文展开**——这是一个覆盖度论证（"我们尝试了所有合理方向，均无效"），详尽的分类和结果表理应放在附录。Figure 2 已在主文提供了可视化概览（4 大类策略，全部 produce neutral-to-negative Δ vs SC），Table 14（Appendix J/K, p18）给出了全部 27 种的具体数值。

2. **但 R2 关于"各类失败的共性原因"缺失的批评是有道理的**——主文仅说 "All 27 training-free strategies fail" 而未分析**为什么**不同类型的 intervention（prompt-level vs. constraint-set vs. solver-objective vs. filtering）都失败。共性失败原因应至少用 2-3 句话在主文概括（例如："所有 training-free 策略无法改变约束的分布来源，因此无法打破 trace-count 主导的结构性偏差"）。

综上，主文篇幅大致合理（8 页限制下的取舍），但应补充 1-2 句共性失败机制的解释。

---

**[AGREE] R2-W5: BR 范围选择性报告。**
同意。Abstract 报告 "bias ratios 1.66–4.97× across nine models" 仅给出 min-max 范围，未提供中位数或均值。查看 Table 2（p7），9 个模型的 BR 值分布并非均匀——大部分集中在 1.5–2.5× 范围，4.97× 可能是单一异常值（我注意到 Mistral-7B 在某些条件下 BR 特别高）。报告中位数（或 IQR）比 min-max 更能反映 central tendency。

不过这是 minor 问题——BR 全部 > 1 的定性结论不受影响，只是 4.97× 的上界可能给读者不恰当的印象。

---

**[AGREE] R2-W6: Related Work 深度不足。**
同意，且与 R2-W1 相关。§2 的三范式分类（specification-generation, trace-extraction, trained verifiers）在结构上清晰，但每个范式的讨论停留在 listing 层面。两个关键缺失：
1. Wan et al. (2025) 与 SCB 的区分仅一句话（如 R2 所述）
2. Trained verifiers（PRM, ORM）与 self-extracted constraints 的根本区别——前者引入 external training signal 打破了自引用循环，这恰好为 §6 的跨架构验证提供了理论对照。§2 应专门讨论为什么 trained verifiers 能 work 而 self-extraction 不能，这正是论文核心论点的镜像。

---

**[REBUT] R2-W7: §7 Discussion 过短。**
部分反驳。R2 指出 §7 仅 ~1/3 页且缺少 neuro-symbolic 启示、规模趋势、test-time compute 讨论。但：

1. 论文有 Appendix Z "Extended Discussion and Limitations"（p25-27, ~2.5 页），覆盖了 R2 要求的大部分内容：SCB vs CoT unfaithfulness（Z p25）、test-time scaling implications（Z p25-26）、neuro-symbolic implications（Z p26）、future directions including trained extractors 和 multi-model ensembles（Z p26）。
2. 在 8 页正文限制下，§7 的篇幅取舍是合理的——将详细讨论放入附录是常见做法。

不过 R2 的批评提醒了一个真实问题：如果 reader 只读正文，会错过重要讨论。建议在 §7 末尾添加一句明确指引："Extended discussion of neuro-symbolic implications, scaling trends, and future directions appears in Appendix Z"。

---

**[REBUT] R2-W8: 指标过载。**
不同意。R2 建议将 ProcessSim 和 CCR 移至附录，但我认为两者在主文中发挥了不可替代的角色：

- **ProcessSim**（§5.3）是唯一量化 process-level independence 的指标——K_eff 和 BR 都在 answer level 工作，ProcessSim 直接测量推理过程的多样性。§5.3 的发现（ProcessSim = 0.10 on Mistral-7B FOLIO, process-convergent but answer-divergent pairs = 9.5%）是论文核心论点的重要支柱。
- **CCR** 定义在 Appendix D（p14），主文仅在 §5.3 简要引用。它已经是附录级的存在。

7 个指标听起来多，但实际上主文核心指标只有 4 个（K_eff, BR, C_0, ProcessSim），Effective-K 是 K_eff 的 variant，CCR 在附录，SICA score 是方法本身的输出而非诊断指标。密度高但各有角色，不建议进一步削减。

---

**[AGREE] R2-W9: "Symbolic Mirage" 与 "SCB" 术语关系模糊。**
同意。论文使用两个术语但未明确界定关系：
- "Symbolic Mirage Hypothesis"（§3.3）：overarching hypothesis，预测自提取约束是分布先验的投射
- "Symbolic Confirmation Bias (SCB)"：在正文中用于描述观测到的偏差现象

合理的关系应为：Symbolic Mirage Hypothesis 是理论假说，SCB 是该假说预测的可观测现象。但论文时而将两者互换使用（e.g., §5 标题 "Analysis" 下用 SCB 描述发现，§3.3 用 Symbolic Mirage 命名假说）。建议在 §3.3 首次引入时用一句话明确："`The Symbolic Mirage Hypothesis predicts a specific observable pattern we term Symbolic Confirmation Bias (SCB): ...`"。

---

## Missing References 回应

**[AGREE] M1 (DuPO) + M2 (S²R)**: 两者都是 training-based self-verification 方法，与本文的 training-free 框架形成对比。特别是 DuPO（ICLR 2026）如果在 formal verification 场景下有效，会直接支持本文 §6 的结论——引入 external training signal 可以打破自引用循环。应在 §2 trained verifiers 部分讨论。

**[AGREE] M3 (LLM as Formalizers on CSP, arXiv 2505.13252)**: 高度相关——该工作研究 LLM 作为形式化工具的能力和局限，直接关联本文 §3.2 的约束提取管道。如果该工作报告了形式化质量问题，会进一步支撑 SCB 假说。

**[AGREE] M4 (Lakshminarayanan et al. 2017 Deep Ensembles)**: 如我在 R2-W3 回应中所述，这是 §6 independence-accuracy tradeoff 的理论基础文献。不引用是一个明显遗漏。

---

## 综合评价

与 R2 的整体评分（3.5 Borderline Conference）一致。R2 的审查在概念层面（SCB 独立性、K_eff 新颖性、ensemble 联系）比我的 R1 审查更深入，我的审查则在统计层面（power < 21%、多种子不足、Spearman n=6）更细致。两份审查的主要 concerns 互补且不冲突。

核心共识：论文的实验规模和诊断框架有价值，但 claim 措辞需要收紧——无论是统计层面（R1-W1 power 问题）还是概念层面（R2-W1 SCB 独立性、R2-W2 K_eff 新颖性）。修改后可达 Conference 水平。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1604 · 2026-05-23T00:45:02.456350+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 110

## Round 110

2 recorded events


### User

_source line 1605 · 2026-05-23T00:45:07.889267+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

**回应总结**：对 R2 的 9 个 Weaknesses，我给出 6 个 [AGREE]、3 个 [REBUT]：
- **AGREE**: W1（SCB 概念独立性）、W2（K_eff 新颖性）、W3（缺 ensemble 文献联系）、W5（BR 选择性报告）、W6（Related Work 深度）、W9（术语关系模糊）
- **REBUT**: W4（Remediation 主文篇幅大致合理，但需补充共性失败机制解释）、W7（Discussion 短但有 Appendix Z 补充，需加指引）、W8（ProcessSim 在主文不可替代，CCR 已在附录）

4 个 Missing References 全部 AGREE。两份审查的 concerns 互补——R2 偏概念层面，R1 偏统计层面，核心共识一致：3.5 Borderline Conference，修改 claim 措辞后可提升。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1606 · 2026-05-23T00:45:15.973221+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 111

## Round 111

12 recorded events


### User

_source line 1607 · 2026-05-23T00:45:52.479817+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 逐条回应 Reviewer 1

---

### [AGREE] R1-W1: 统计功效不足，"Fail" claim 超出证据支撑

同意这是本文最大的方法论问题之一。Table 6 (Appendix E) 显示 n=200 时全部非退化条件 observed power < 21%，MDE 远大于观测效应量。Bootstrap 95% CI 宽度 ±1.5–2pp (Table 7, Appendix F) 确实无法排除 ±1pp 级别的真实正效应。

但我对 "critical" 严重度有保留意见。论文的论证并非仅依赖 null p-values——它构建了多重收敛证据：(1) Oracle control (Appendix H) 显示 Mistral-7B FOLIO 上 +29.90pp 的改进是可实现的，定位问题到自提取环节而非 pipeline 本身；(2) Shuffle control (§5.2) 证明偏差具有结构性；(3) SCB 机制提供了"为什么无效"的因果解释。这些证据链在逻辑上支持"fail"的结论，尽管统计上更准确的表述应为"no detectable improvement consistent with the SCB mechanism"。

**建议**：标题应弱化为 "no evidence of improvement" 或 "limitations of"，主文应增加对功效局限性的显式讨论（目前仅在 Appendix E 中出现），但不应将此升至 critical——因为论文的核心论证不完全依赖于 frequentist null results。

---

### [REBUT] R1-W2: Predictions 1-2 是事后构造

部分反驳。R1 的关切对 **Prediction 2**（MAX-SAT 产生与 count-only 聚合相同答案，94.4%）有道理——P2 本质上是 SCB 假说的同义反复：如果约束偏向多数答案，那么加权求解器当然会复现多数投票结果。这确实更像是观察总结而非独立预测。

但 **Prediction 1**（结构性独立的验证应打破 SCB）是一个真正的 out-of-sample prediction，且在 §6 中用全新的实验设计（cross-architecture NLI, DeBERTa-large-mnli）进行了测试。§6 的实验使用了主实验中未出现的验证器和评估协议，不可能是从 §4-§5 的结果中 "事后总结" 出来的。

**建议**：将 P2 重新定位为 "diagnostic observation" 而非 "prediction"；P1 作为 prediction 的表述可保留。但 R1 提出的预注册缺失这一点，在 ML empirical research 语境下属于普遍现象，对此论文不应受到特别惩罚。

---

### [AGREE] R1-W3: 多种子复制极其有限

完全同意。Appendix Y.1 仅对 Mistral-7B (3 seeds, σ = ±2.70pp) 和 Qwen2.5-14B (4 seeds) 进行了多种子验证。种子间方差 (±2.70pp) 超过了大多数观测效应量 (|Δ| < 2pp)，这意味着对于其余 4 个单种子模型，我们无法区分信号与种子噪声。

这与我自己的审查中未充分强调但隐含在 W1 (abstract 选择性报告) 中的关切一致：当种子方差未被充分量化时，报告精确的 Δ 值（如 abstract 中的 "BR 1.66–4.97×"）可能具有虚假精度。

---

### [AGREE with nuance] R1-W4: BR 指标存在部分循环论证

R1 的核心论点有道理：当多数答案错误时，更多 trace 支持错误答案 → 更多约束来自这些 trace → BR > 1 部分是 trace-count 不平衡的数学必然。

然而，论文的 shuffle control (§5.2) 实际上 **直接验证了 R1 的这个论点**——BR_shuf ≈ BR_real 意味着偏差确实来自 trace-count 分布而非约束内容。但这恰恰是论文的核心论断：自提取约束不提供超越 trace 分布的独立信息，形式验证层是空洞的 (vacuous)。

问题在于 **论文的措辞**：某些段落暗示 BR > 1 揭示了"提取质量"问题（如 §5.2 "indicating that BR reflects the trace-count distribution rather than extraction-specific error"），但另一些段落又将其作为 SCB 的证据。论文需要更清晰地分离 BR 的两个组成部分：(a) 由 trace-count 不平衡导致的 trivial 分量（R1 所指的数学必然），和 (b) 约束未能提供超越 trace 分布的独立信号这一 non-trivial 发现。

**我的补充**：这与我在 W9 中指出的 "Symbolic Mirage" vs "Symbolic Confirmation Bias" 术语混淆有关——论文需要更精确地定义 SCB 到底是指约束质量问题还是信息冗余问题。

---

### [AGREE] R1-W5: 跨架构 NLI 验证证据偏薄

同意。Table 3 (p8) 显示显著增益仅出现在 Mistral-7B（SC < 40% on FOLIO），且 "SC ≈ 70% 阈值" 的 claim 来自极少数据点的外推。4/6 条件使用 DeBERTa 系列 verifier，缺乏验证器多样性。

这与我自己的 review 中对 §6 的关切 (W5 in my review) 一致。我进一步指出：§6 的 "escape" 结果实际上展示了一个 independence-accuracy trade-off（我的 W3），跨架构获得更高独立性但更低单 trace 准确率。论文将其呈现为积极的逃逸路径，但证据基础太窄，无法支撑 §7 中 "practitioners should employ external verifiers from a different architecture family" 的实践建议。

---

### [AGREE] R1-W6: Spearman ρ=-1.0 (n=6) 过于脆弱

同意。n=6 下完美负相关的统计意义极其有限。作者报告 p=0.003，但 Spearman 检验在小样本下 p-value 对排名扰动极为敏感——任一对交换即可大幅改变 ρ。这是一个说明性观察而非稳健发现，论文不应将其作为 "monotonic relationship" 的强证据。

---

### [AGREE] R1-W7: K_eff 中 Fleiss' κ 的 prevalence paradox

同意这是一个有效的技术关切。当某一答案类别的 prevalence 极高（如某题大多数 trace 都选同一答案）时，Fleiss' κ 受 prevalence paradox 影响可能偏低，导致 K_eff 偏高（高估有效多样性）。这与我的 W2 (K_eff novelty) 相关——K_eff 不仅在概念上是 Kish (1965) 的直接应用，在技术实现上还继承了 κ 的已知缺陷。

论文应至少在 Appendix 中讨论 prevalence paradox 对 K_eff 估计的影响，或使用 Gwet's AC1 等对 prevalence 更鲁棒的一致性指标作为敏感性检验。

---

### [AGREE] R1-W8: α=0.5 敏感性分析结论过强

同意。当 SICA ≈ SC（主效应接近零）时，α 权重参数改变不会改变一个本来就没有效果的方法的结果——这是 ceiling effect（或更准确地说，floor effect），不是对 α 的真正鲁棒性。§5.2 中 "≥99% agreement" 的表述暗示了对参数选择的鲁棒性，但实际上只是反映了 SICA 退化为 SC 的程度。

---

### Missing References 回应

**R1 提出的遗漏引用**：

- **Stechly et al. (2024) Self-Verification Fundamentally Limited**：论文已引用 "Stechly et al. (ICLR 2025)"（p1, p3），这应是同一工作的会议发表版本。如果 R1 指的是不同的 2024 preprint 版本，则差异可忽略——论文引用了最终发表版。**不构成遗漏。**

- **Wang et al. (2024) Self-Evaluation Improves Selective Generation**：需要区分论文引用列表中的多个 "Wang et al." 引用。论文引用了 Wang et al. (2023) Self-Consistency、Wang et al. (2024) multi-agent debate、Wang et al. (2025) reasoning-aware self-consistency 等。如果 R1 指的是 self-evaluation 用于 selective generation（即选择性输出而非改进推理），这与本文的 trace aggregation 场景不同，但仍值得在 Related Work §2 中简要提及以区分 self-evaluation 的不同用途。**轻微遗漏，不影响评分。**

---

### 综合评估

R1 和我（R2）的审稿意见在以下核心问题上高度一致：
1. **统计功效不足** → 标题和部分 claim 需弱化 (R1-W1, 我的隐含关切)
2. **§6 escape 证据偏薄** → 无法支撑实践建议 (R1-W5, 我的原 W5 对应关切)
3. **多种子不足** → 效应量精度存疑 (R1-W3, 我的隐含关切)

我们的主要分歧在于：
- **严重度判定**：R1 将 W1 (功效) 定为 critical，我认为 major 更合适——因为论文的论证策略不完全依赖 frequentist testing，还有 oracle/shuffle/SCB 机制的收敛证据。
- **新颖性评估**：R1 未重点讨论 SCB 概念新颖性问题，而我认为这是本文最根本的弱点 (我的 W1: SCB vs CoT confirmation bias 概念同构)。

**维持 Overall Assessment: 3.5 (Borderline Conference)**。论文实验质量优秀但概念贡献增量有限。若 R1 的 W1 被视为 critical 且标题不修改，可能降至 3.0 (Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1608 · 2026-05-23T00:46:17.407820+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 1609 · 2026-05-23T00:46:17.860415+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T00:33:34.690417+00:00\", \"completed_at\": \"2026-05-23T00:37:41.158626+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"前 2 页为纯文本（Abstract + Introduction），无任何视觉锚点。第一个 display item（Figure 1 SICA pipeline 图）直到第 3 页顶部才出现。审稿人需要阅读 2 整页密集文字才能看到第一个图表，可能影响第一印象锚定效果。建议考虑将 Figure 1 提前至第 2 页或在 Introduction 中加入一个 motivating example 小图。\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1（SICA pipeline 全宽图）质量良好：流程清晰，红色虚线框标注 oracle variant，caption 自包含。作为第一个 display item 能有效传达核心方法。Title-Abstract-Figure 1 三者叙事一致。\"}, {\"severity\": \"info\", \"dimension\": \"page 4-5\", \"message\": \"连续 2 页无 figure/table，但有多个数学定义和公式（κ_eff、Bias Ratio 等）穿插，视觉单调感被公式打破。属于方法论/形式化章节的正常节奏，不构成严重问题。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1（主结果表）排版优秀：全宽 booktabs 风格，显著结果加粗，附 p 值和符号标注体系（†/‡/*/**），caption 详细说明符号含义。字号偏小但可读。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 2（Symbolic confirmation bias）同样高质量 booktabs 排版，数据密集但组织清晰。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Figure 2（27 种 training-free 策略柱状图）x 轴标签非常小且密集——在打印或缩放时可能难以辨认。建议增大字号或将策略分组展示。同页 Table 3 单栏表格排列合理，页面整体偏满但不溢出。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"主文 display items 统计：2 figures + 3 tables = 5 个，分布在 8 页正文中（~0.63/页）。对于实证为主的论文，数量处于合理范围低端，但核心结果覆盖充分。\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 章节简短（约 1/3 页，3 个要点），符合 EMNLP 规范。References 从同页开始。主文内容在第 8 页末尾结束，页数合规。\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"Figure 3（散点图）单栏，字号偏小但可读。右栏 prompt template 使用代码框排版，清晰。\"}, {\"severity\": \"info\", \"dimension\": \"page 13-14\", \"message\": \"Algorithm 1 和 Algorithm 2 伪代码格式规范。Table 4-5 数据密集但 booktabs 风格清晰。\"}, {\"severity\": \"info\", \"dimension\": \"page 18\", \"message\": \"Figure 5（K sensitivity 线图）
…[truncated 915 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1610 · 2026-05-23T00:46:17.860782+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 1611 · 2026-05-23T00:46:18.914327+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1053
}
```

</details>

---


### Tool call

_source line 1612 · 2026-05-23T00:46:18.914715+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1613 · 2026-05-23T00:46:19.015670+00:00_

1	# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)
2	- id: "R1-C1"
3	  summary: "Method Stage 3 sat() implementation undescribed"
4	  category: method
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 1
8	  last_seen_round: 3
9	  resolution: "Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit."
10	  resolution_round: 3
11	
12	- id: "R1-C2"
13	  summary: "Most experiments underpowered (n≤60), no power analysis"
14	  category: experiment
15	  severity: critical
16	  status: resolved
17	  first_raised_round: 1
18	  last_seen_round: 1
19	  resolution: "Power analysis + Bootstrap CIs added. Larger n conditions (200-600)."
20	  resolution_round: 3
21	
22	- id: "R1-C3"
23	  summary: "Oracle/upper-bound experiment missing"
24	  category: experiment
25	  severity: critical
26	  status: resolved
27	  first_raised_round: 1
28	  last_seen_round: 1
29	  resolution: "Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp."
30	  resolution_round: 3
31	
32	- id: "R1-C4"
33	  summary: "Huang et al. (ICLR 2024) not cited"
34	  category: framing
35	  severity: critical
36	  status: resolved
37	  first_raised_round: 1
38	  last_seen_round: 2
39	  resolution: "Huang, Stechly, Kambhampati all cited and discussed."
40	  resolution_round: 2
41	
42	- id: "R1-C5"
43	  summary: "Critical related work missing"
44	  category: writing
45	  severity: critical
46	  status: resolved
47	  first_raised_round: 1
48	  last_seen_round: 1
49	  resolution: "~48 citations, 5 Related Work paragraphs."
50	  resolution_round: 3
51	
52	- id: "R1-C9"
53	  summary: "Capability trap novelty unclear"
54	  category: framing
55	  severity: critical
56	  status: resolved
57	  first_raised_round: 1
58	  last_seen_round: 3
59	  resolution: "Reframed as regime-dependent analysis with CJT framework."
60	  resolution_round: 3
61	
62	- id: "R3-N1"
63	  summary: "σ(c,a) scoring inconsistent between self-extraction and oracle"
64	  category: method
65	  severity: critical

…[truncated 18535 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1614 · 2026-05-23T00:50:07.615555+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "symb_invariant_consensus",
  "issues_yaml": "# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)\n- id: \"R1-C1\"\n  summary: \"Method Stage 3 sat() implementation undescribed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit.\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Most experiments underpowered (n≤60), no power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Power analysis + Bootstrap CIs added. Larger n conditions (200-600).\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Oracle/upper-bound experiment missing\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp.\"\n  resolution_round: 3\n\n- id: \"R1-C4\"\n  summary: \"Huang et al. (ICLR 2024) not cited\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Huang, Stechly, Kambhampati all cited and discussed.\"\n  resolution_round: 2\n\n- id: \"R1-C5\"\n  summary: \"Critical related work missing\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"~48 citations, 5 Related Work paragraphs.\"\n  resolution_round: 3\n\n- id: \"R1-C9\"\n  summary: \"Capability trap novelty unclear\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Reframed as regime-dependent analysis with CJT framework.\"\n  resolution_round: 3\n\n- id: \"R3-N1\"\n  summary: \"σ(c,a) scoring inconsistent between self-extraction and oracle\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Paper Agent added clarifying sentence in method.tex.\"\n  resolution_round: 4\n\n- id: \"R3-N2\"\n  summary: \"α value never specified\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"α=0.5 explicit in Eq.(3) and §4.1.\"\n  resolution_round: 3\n\n# Round 9+ issues\n\n- id: \"R9-W2\"\n  summary: \"NLI combo weight parameter w 未交叉验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 未单独提及 w 参数\"\n    - round: 15\n      reviewers: []\n      note: \"R15(fresh) 未单独提及\"\n\n- id: \"R9-W3\"\n  summary: \"Capability Gap Hypothesis 基于极小样本 (n=6)\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 共识: 仅6条件仅Mistral-7B显著, 需软化结论\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识: §6 escape仅SC<40%验证, 'SC≈70%'无数据支撑, Spearman n=6脆弱\"\n  action_items:\n    - round: 14\n      action: \"§6结论软化为preliminary evidence + 讨论task gap\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R9-VL1\"\n  summary: \"Pages 1-2 连续纯文本无 display item\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) pages 3-5 连续3页无正式display item, warning\"\n    - round: 15\n      reviewers: []\n      note: \"R15 视觉审查确认: 前2页纯文本, Figure 1在p3顶部\"\n\n- id: \"R9-VL4\"\n  summary: \"Discussion/Conclusion 展开不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) §7压缩在page 8底部约1/3页, design principles各只有一句话\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) R2维持§7过短, R1反驳称有Appendix Z补充. 分歧: 低优先级\"\n  action_items:\n    - round: 14\n      action: \"§7 Discussion扩展design principles, 每条2-3句+数据支撑\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R10-N1\"\n  summary: \"Proposition 1 (Self-Extraction Ceiling) 无证明——empirical claim dressed as theorem\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 13\n  resolution: \"当前论文使用 'Empirical Finding 1/2'(page 5 tcolorbox), 不再使用 Proposition 术语\"\n  resolution_round: 13\n\n- id: \"R10-N2\"\n  summary: \"κ→K_eff 映射理论基础不足——r=0.625 验证弱\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) prevalence paradox可能高估K_eff. 论文已声明ordinal diagnostic\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识: prevalence paradox使K_eff偏高(强化论点方向), 但应显式讨论. 建议附录用Gwet AC1做敏感性检验\"\n  action_items:\n    - round: 14\n      action: \"附录增加ICC robustness check（低优先级）\"\n      assigned_to: \"agent\"\n      status: in_progress\n\n- id: \"R10-N3\"\n  summary: \"Capability gap 'perfectly monotonic' 结论基于 n=6 非独立数据点\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 与R9-W3合并: 共识仍为证据不足\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识: Spearman ρ=-1.0 (n=6)是suggestive非definitive, 任一排名互换ρ大幅下降\"\n\n- id: \"R10-W1\"\n  summary: \"DRC τ 阈值无 held-out 评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15(fresh) 未单独提及\"\n\n- id: \"R10-W2\"\n  summary: \"Cross-architecture NLI escape 适用面极窄\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 需讨论NLI vs symbolic extraction的task gap\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识: 仅SC<40%验证, 4/6共享DeBERTa verifier, 实践建议外推过度\"\n  action_items:\n    - round: 14\n      action: \"§6增加NLI vs symbolic extraction task gap讨论\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R10-W3\"\n  summary: \"四种子复制方差大 + 统计功效 <21%\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1]\n      note: \"R14(fresh) 多种子仅2模型, 更多模型正在运行\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识critical: Mistral-7B σ=±2.70pp超过多数效应量, 4/6模型单种子. 种子方差未量化下报告精确Δ有虚假精度\"\n\n- id: \"R10-W4\"\n  summary: \"TOST ±2pp margin 缺少显式理由\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"论文已有margin sensitivity但呈现不够显著\"\n    - round: 15\n      reviewers: []\n      note: \"R15(fresh) 未单独提及, 但功效问题(R11-N2)隐含此关切\"\n\n- id: \"R10-W5\"\n  summary: \"Bias Ratio 无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"BR CI 已整合: Mistral [3.98,6.37], Qwen [2.44,7.11]\"\n  resolution_round: 10\n\n- id: \"R10-W6\"\n  summary: \"SatLM specification-generation vs SICA trace-extraction 对比不充分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15(fresh) 未单独提及\"\n\n- id: \"R10-W7\"\n  summary: \"'Symbolic Confirmation Bias' 需与近期 CoT confirmation bias 工作区分\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识major: SCB与Wan et al.(2025) CoT confirmation bias机制同构(distributional prior→biased output→confirmation). 论文应承认同构性, 定位SCB为已知现象在formal verification管道中的实证深化\"\n\n- id: \"R10-W8\"\n  summary: \"Related Work 过度压缩——引用列表而非文献讨论\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) R2肯定引用覆盖面\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识: §2结构清晰但Wan et al.区分仅一句话, trained verifier(PRM)对比缺失\"\n\n- id: \"R10-W9\"\n  summary: \"27 种修复策略在正文中展示不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) §5.5仅~15行. 建议深度分析3-5种代表性策略\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) R2维持major, R1部分REBUT(Figure 2+Table 14在附录已够). 共识: 需补充1-2句共性失败机制解释\"\n  action_items:\n    - round: 14\n      action: \"§5.5展开到~15-20行, 分析debate/cross-model/contrastive/oracle失败机制\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R10-I1\"\n  summary: \"相对于 Huang/Stechly 的增量新颖性不足\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1认可Z3 formal solver场景非平凡. R2维持新颖性有限. 建议降低Hypothesis措辞\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 与R10-W7/R12-N2合并. K_eff是Kish(1965)直接应用, SCB是confirmation bias特例. 贡献在于empirical depth非conceptual novelty\"\n\n- id: \"R10-I2\"\n  summary: \"Independence-Accuracy Trade-off 作为独立贡献有 bias-variance 重述嫌疑\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识major: §6 trade-off与ensemble learning bias-variance tradeoff(Krogh&Vedelsby 1994)同构, 应在§6或§7显式讨论. 缺引Lakshminarayanan et al.(2017)\"\n\n- id: \"R10-VL1\"\n  summary: \"主文缺结果可视化\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15 视觉审查: 主文5个display items(2 figures+3 tables), ~0.63/页, 合理范围低端\"\n\n- id: \"R11-N1\"\n  summary: \"Spearman ρ=1.0 (n=6) 被过度使用——有效自由度远低于6\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识: suggestive非definitive, 应降低claim强度\"\n\n- id: \"R11-N2\"\n  summary: \"中心 claim 'SICA fails' 与统计功效不匹配——Abstract/title 过强\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) R1-N1: 标题scope超出. R2-W1: 'no evidence'需hedge. R1同意加hedge\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识(R1 critical, R2 major): power<21%, MDE远大于观测效应, 'Fail to Improve'=overclaiming. 应改为'No Evidence'或'Limitations of'. R2补充: 多重证据(oracle/shuffle/SCB)部分缓解但不消除功效问题\"\n  action_items:\n    - round: 14\n      action: \"标题限定为Logical Reasoning + Abstract加power caveat\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R11-N3\"\n  summary: \"TOST ±2pp margin 缺乏 principled 论证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15(fresh) 未单独提及\"\n\n- id: \"R11-W1\"\n  summary: \"DRC 评估不充分——仅PW完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15(fresh) 未单独提及\"\n\n- id: \"R11-W2\"\n  summary: \"BR 指标存在循环论证倾向\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1]\n      note: \"R14(fresh) BR子集大小未报告, 需增加n_err列\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识: BR>1部分是trace-count不平衡的数学必然. Shuffle control确认了这一点但论文措辞混淆'结构性局限'与'提取质量问题'. 需更精确区分两个组成部分\"\n  action_items:\n    - round: 14\n      action: \"Table 2增加n_err列 + caption讨论小n_err影响\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R11-W3\"\n  summary: \"术语过度品牌化——'Symbolic Mirage' 偏 dramatic\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"降低'Hypothesis'措辞. 保留名称但重构predictions为observations\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识: 'Symbolic Mirage'与'SCB'关系模糊. 建议明确: Hypothesis是理论假说, SCB是可观测现象\"\n\n- id: \"R11-W4\"\n  summary: \"新颖性定位需更早更明确建立与先验工作的 distinction\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 与R10-W7/R10-I1/R12-N2合并. 三项概念贡献(SCB/K_eff/trade-off)均有先验对应, 需重新定位为empirical contributions\"\n\n- id: \"R11-W5\"\n  summary: \"Independence-Accuracy Trade-off 应定位为量化而非新发现\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识: 见R10-I2, 需与bias-variance tradeoff文献建立联系\"\n\n- id: \"R11-W6\"\n  summary: \"遗漏引用: Byerly & Khashabi (2026 TACL) 等\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"当前论文已引用 Byerly and Khashabi (2026)\"\n  resolution_round: 13\n\n- id: \"R11-W7\"\n  summary: \"27 策略计数膨胀 + 未尝试 trained constraint extractor\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15(fresh) 未单独提及计数膨胀, 但R2提出DuPO/S²R等training-based方法作为missing ref\"\n\n- id: \"R11-VL1\"\n  summary: \"主文缺结果可视化——需上提 Figure 到主文\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15 视觉审查: 主文2 figures+3 tables, 低端但覆盖核心结果\"\n\n- id: \"R12-N1\"\n  summary: \"标题 overclaiming about frontier scale\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 标题scope: 'LLM Reasoning'→'Logical Reasoning'\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 标题仍含'LLM Logical Reasoning', 比'LLM Reasoning'更限定但'Fail to Improve'仍overclaiming given power<21%\"\n  action_items:\n    - round: 14\n      action: \"标题改为 Beyond Self-Consistency: Why Self-Extracted Constraints Fail to Improve LLM Logical Reasoning\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R12-N2\"\n  summary: \"SCB 核心新颖性不足——self-correction failure 在 FOL 载体上的实例化\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识major: SCB = CoT confirmation bias在formal verification管道的实例化. 贡献在于empirical quantification而非新概念\"\n\n- id: \"R12-N3\"\n  summary: \"DRC 作为 Contribution 4 不够充分\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"DRC demoted to practical observation in §6\"\n  resolution_round: 13\n  first_raised_round: 12\n  last_seen_round: 13\n\n- id: \"R12-W1\"\n  summary: \"BR 可能存在循环论证——56.4%零变量重叠使约束按定义支持source answer\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 见R11-W2. 共识: shuffle control确认了trace-count来源, 但论文措辞需更精确\"\n\n- id: \"R12-W2\"\n  summary: \"CIL 名称和 information-theoretic 声称有误导\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Renamed to CCR, removed 'unify' claim\"\n  resolution_round: 13\n  first_raised_round: 12\n  last_seen_round: 13\n\n- id: \"R12-W3\"\n  summary: \"Figure 2 placement——应在正文而非附录\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Figure 2 已在正文 page 7\"\n  resolution_round: 13\n\n- id: \"R12-W4\"\n  summary: \"Appendix vs 主文关键信息分配不合理\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"§3.1压缩+CCR移附录+§5.5/§7展开\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) R2维持§5.4主文过薄, R1部分同意(需补共性失败机制). §7 R1认为Appendix Z已补充\"\n\n- id: \"R12-EC1\"\n  summary: \"Extractor Confound——所有 frontier cross-model extraction 使用同一 Mistral-7B extractor\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15(fresh) 未单独提及, 但§6 escape薄弱问题(R9-W3)隐含此关切\"\n\n- id: \"R13-N1\"\n  summary: \"摘要 BR 4.97× 选择性报告——最极端条件\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识: Abstract报告min-max而非中位数, 4.97×可能是异常值. 定性结论(BR全>1)不受影响但数值呈现有cherry-picking之嫌\"\n  action_items:\n    - round: 13\n      action: \"摘要改为报告 BR 范围或中位数\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R13-N2\"\n  summary: \"统计功效呈现不足——10/16 underpowered, power analysis 埋在附录\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 核心共识: power<21%是最大方法论问题. R1视为critical, R2视为major(多重证据部分缓解). 需在主文§4.2显式讨论功效局限\"\n  action_items:\n    - round: 14\n      action: \"Abstract增加power caveat\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R13-N3\"\n  summary: \"α=0.5 无敏感性分析\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Appendix Table 11已有α ablation(agreement≥99%), 争议缩窄\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识: ≥99% agreement是主效应近零时的ceiling effect, 非真正鲁棒性. 应加限定语\"\n\n- id: \"R13-W1\"\n  summary: \"符号/指标过载——8页内7个定量工具\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) R2维持minor, R1反驳(ProcessSim不可替代, CCR已在附录). 分歧: 低优先级\"\n  action_items:\n    - round: 14\n      action: \"CCR移入附录减少正文指标密度\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R13-W2\"\n  summary: \"NLI claim 须限定到命题逻辑任务\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15(fresh) 未单独提及, 但功效+scope问题(R11-N2)隐含此关切\"\n\n- id: \"R13-W3\"\n  summary: \"语法去重可能膨胀 BR——未报告语义去重后 BR\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15(fresh) 未单独提及\"\n\n- id: \"R13-W4\"\n  summary: \"Symbolic Mirage Hypothesis §3.3 与 §5 验证不连贯\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 与R14-N2合并: Predictions 1-2 post-hoc, 仅P1(跨架构escape)为真预测\"\n  action_items:\n    - round: 14\n      action: \"§3.3重构predictions + §5验证段落同步修改\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R13-W5\"\n  summary: \"缺引: Dhuliawala et al. 2023 Chain-of-Verification\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"已引用 dhuliawala2023chainofverification\"\n  resolution_round: 14\n\n# R14(fresh) issues\n\n- id: \"R14-N1\"\n  summary: \"标题'LLM Reasoning'范围超出实验证据——仅覆盖逻辑推理\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"共识critical. 改为Logical Reasoning\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 标题已含'Logical Reasoning', 但'Fail'仍overclaiming\"\n\n- id: \"R14-N2\"\n  summary: \"Symbolic Mirage Hypothesis Predictions 1-2 为事后总结非独立预测\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"共识: 仅Prediction 3为独立验证. 保留Hypothesis名称但重构presentations\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) R1维持post-hoc, R2部分REBUT: P1(跨架构escape)是真out-of-sample prediction(§6用新实验验证). P2确实是同义反复. 部分共识: P2重定位为observation, P1可保留prediction框架\"\n  action_items:\n    - round: 14\n      action: \"§3.3区分Motivating Observations vs Testable Prediction\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R14-W1\"\n  summary: \"Cross-architecture实验仅6条件/单一verifier/仅Mistral-7B显著\"\n  category: experiment\n  severity: major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识: 'SC≈70%阈值'的claim无数据支撑, 应限定为'works on weak generators (SC<40%)'\"\n  action_items:\n    - round: 14\n      action: \"结论软化为preliminary evidence + NLI task gap讨论\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R14-W2\"\n  summary: \"8页正文信息过载——§5.5/§6/§7展开不足\"\n  category: writing\n  severity: major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) §5.4需补共性失败机制(1-2句), §7 Appendix Z部分补偿但需加指引\"\n  action_items:\n    - round: 14\n      action: \"§3.1压缩+CCR移附录+§5.5展开remediation分析+§7展开\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R14-W3\"\n  summary: \"'No evidence' claim scope与统计功效不匹配\"\n  category: framing\n  severity: major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 见R11-N2. 核心共识问题\"\n  action_items:\n    - round: 14\n      action: \"Abstract增加power caveat\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R14-W4\"\n  summary: \"BR计算子集大小(n_err)未报告\"\n  category: experiment\n  severity: moderate\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1]\n      note: \"R15(fresh) 与BR循环论证(R11-W2)相关, n_err小时BR可靠性降低\"\n  action_items:\n    - round: 14\n      action: \"Table 2增加n_err列 + caption讨论小n_err可靠性\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R14-W5\"\n  summary: \"Related Work遗漏: SETS(2025), MAV(2025)\"\n  category: writing\n  severity: minor-to-major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [2]\n      note: \"R15(fresh) R2补充遗漏: DuPO(ICLR 2026), S²R(2025), CSP reality check(2025), Lakshminarayanan(2017)\"\n  action_items:\n    - round: 14\n      action: \"Agent验证引用 → §2增加SETS/MAV讨论\"\n      assigned_to: \"agent+paper_agent\"\n      status: in_progress\n\n- id: \"R14-W6\"\n  summary: \"Fleiss' κ→ICC近似仅r=0.625——prevalence paradox\"\n  category: method\n  severity: moderate\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 见R10-N2. 共识: 偏差方向强化论点但应显式讨论\"\n  action_items:\n    - round: 14\n      action: \"附录增加ICC robustness check（低优先级）\"\n      assigned_to: \"agent\"\n      status: in_progress\n\n# R15(fresh) 新发现\n\n- id: \"R15-M1\"\n  summary: \"遗漏引用: DuPO (ICLR 2026) — training-based self-verification\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"共识AGREE. 直接相关§6 escape + §2 trained verifiers讨论\"\n\n- id: \"R15-M2\"\n  summary: \"遗漏引用: S²R (2025) — RL-based self-verification\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"共识AGREE. Training-based escape路径\"\n\n- id: \"R15-M3\"\n  summary: \"遗漏引用: LLM as Formalizers on CSP (arXiv 2505.13252, 2025)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"共识AGREE. 直接互补约束提取质量讨论\"\n\n- id: \"R15-M4\"\n  summary: \"遗漏引用: Lakshminarayanan et al. (2017) Deep Ensembles\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"共识AGREE. §6 independence-accuracy trade-off的理论基础文献\"\n\n- id: \"R15-W1\"\n  summary: \"α=0.5敏感性分析≥99% agreement是ceiling effect——主效应近零时penalty项影响自然可忽略\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"共识: Table 11结论应加限定语(ceiling effect caveat)\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "issues_yaml": "# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)\n- id: \"R1-C1\"\n  summary: \"Method Stage 3 sat() implementation undescribed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit.\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Most experiments underpowered (n≤60), no power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Power analysis + Bootstrap CIs added. Larger n conditions (200-600).\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Oracle/upper-bound experiment missing\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp.\"\n  resolution_round: 3\n\n- id: \"R1-C4\"\n  summary: \"Huang et al. (ICLR 2024) not cited\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Huang, Stechly, Kambhampati all cited and discussed.\"\n  resolution_round: 2\n\n- id: \"R1-C5\"\n  summary: \"Critical related work missing\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"~48 citations, 5 Related Work paragraphs.\"\n  resolution_round: 3\n\n- id: \"R1-C9\"\n  summary: \"Capability trap novelty unclear\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Reframed as regime-dependent analysis with CJT framework.\"\n  resolution_round: 3\n\n- id: \"R3-N1\"\n  summary: \"σ(c,a) scoring inconsistent between self-extraction and oracle\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Paper Agent added clarifying sentence in method.tex.\"\n  resolution_round: 4\n\n- id: \"R3-N2\"\n  summary: \"α value never specified\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"α=0.5 explicit in Eq.(3) and §4.1.\"\n  resolution_round: 3\n\n# Round 9+ issues\n\n- id: \"R9-W2\"\n  summary: \"NLI combo weight parameter w 未交叉验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 未单独提及 w 参数\"\n    - round: 15\n      reviewers: []\n      note: \"R15(fresh) 未单独提及\"\n\n- id: \"R9-W3\"\n  summary: \"Capability Gap Hypothesis 基于极小样本 (n=6)\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 共识: 仅6条件仅Mistral-7B显著, 需软化结论\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识: §6 escape仅SC<40%验证, 'SC≈70%'无数据支撑, Spearman n=6脆弱\"\n  action_items:\n    - round: 14\n      action: \"§6结论软化为preliminary evidence + 讨论task gap\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R9-VL1\"\n  summary: \"Pages 1-2 连续纯文本无 display item\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) pages 3-5 连续3页无正式display item, warning\"\n    - round: 15\n      reviewers: []\n      note: \"R15 视觉审查确认: 前2页纯文本, Figure 1在p3顶部\"\n\n- id: \"R9-VL4\"\n  summary: \"Discussion/Conclusion 展开不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) §7压缩在page 8底部约1/3页, design principles各只有一句话\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) R2维持§7过短, R1反驳称有Appendix Z补充. 分歧: 低优先级\"\n  action_items:\n    - round: 14\n      action: \"§7 Discussion扩展design principles, 每条2-3句+数据支撑\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R10-N1\"\n  summary: \"Proposition 1 (Self-Extraction Ceiling) 无证明——empirical claim dressed as theorem\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 13\n  resolution: \"当前论文使用 'Empirical Finding 1/2'(page 5 tcolorbox), 不再使用 Proposition 术语\"\n  resolution_round: 13\n\n- id: \"R10-N2\"\n  summary: \"κ→K_eff 映射理论基础不足——r=0.625 验证弱\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) prevalence paradox可能高估K_eff. 论文已声明ordinal diagnostic\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识: prevalence paradox使K_eff偏高(强化论点方向), 但应显式讨论. 建议附录用Gwet AC1做敏感性检验\"\n  action_items:\n    - round: 14\n      action: \"附录增加ICC robustness check（低优先级）\"\n      assigned_to: \"agent\"\n      status: in_progress\n\n- id: \"R10-N3\"\n  summary: \"Capability gap 'perfectly monotonic' 结论基于 n=6 非独立数据点\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 与R9-W3合并: 共识仍为证据不足\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识: Spearman ρ=-1.0 (n=6)是suggestive非definitive, 任一排名互换ρ大幅下降\"\n\n- id: \"R10-W1\"\n  summary: \"DRC τ 阈值无 held-out 评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15(fresh) 未单独提及\"\n\n- id: \"R10-W2\"\n  summary: \"Cross-architecture NLI escape 适用面极窄\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 需讨论NLI vs symbolic extraction的task gap\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识: 仅SC<40%验证, 4/6共享DeBERTa verifier, 实践建议外推过度\"\n  action_items:\n    - round: 14\n      action: \"§6增加NLI vs symbolic extraction task gap讨论\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R10-W3\"\n  summary: \"四种子复制方差大 + 统计功效 <21%\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1]\n      note: \"R14(fresh) 多种子仅2模型, 更多模型正在运行\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识critical: Mistral-7B σ=±2.70pp超过多数效应量, 4/6模型单种子. 种子方差未量化下报告精确Δ有虚假精度\"\n\n- id: \"R10-W4\"\n  summary: \"TOST ±2pp margin 缺少显式理由\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"论文已有margin sensitivity但呈现不够显著\"\n    - round: 15\n      reviewers: []\n      note: \"R15(fresh) 未单独提及, 但功效问题(R11-N2)隐含此关切\"\n\n- id: \"R10-W5\"\n  summary: \"Bias Ratio 无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"BR CI 已整合: Mistral [3.98,6.37], Qwen [2.44,7.11]\"\n  resolution_round: 10\n\n- id: \"R10-W6\"\n  summary: \"SatLM specification-generation vs SICA trace-extraction 对比不充分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15(fresh) 未单独提及\"\n\n- id: \"R10-W7\"\n  summary: \"'Symbolic Confirmation Bias' 需与近期 CoT confirmation bias 工作区分\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识major: SCB与Wan et al.(2025) CoT confirmation bias机制同构(distributional prior→biased output→confirmation). 论文应承认同构性, 定位SCB为已知现象在formal verification管道中的实证深化\"\n\n- id: \"R10-W8\"\n  summary: \"Related Work 过度压缩——引用列表而非文献讨论\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) R2肯定引用覆盖面\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识: §2结构清晰但Wan et al.区分仅一句话, trained verifier(PRM)对比缺失\"\n\n- id: \"R10-W9\"\n  summary: \"27 种修复策略在正文中展示不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) §5.5仅~15行. 建议深度分析3-5种代表性策略\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) R2维持major, R1部分REBUT(Figure 2+Table 14在附录已够). 共识: 需补充1-2句共性失败机制解释\"\n  action_items:\n    - round: 14\n      action: \"§5.5展开到~15-20行, 分析debate/cross-model/contrastive/oracle失败机制\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R10-I1\"\n  summary: \"相对于 Huang/Stechly 的增量新颖性不足\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1认可Z3 formal solver场景非平凡. R2维持新颖性有限. 建议降低Hypothesis措辞\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 与R10-W7/R12-N2合并. K_eff是Kish(1965)直接应用, SCB是confirmation bias特例. 贡献在于empirical depth非conceptual novelty\"\n\n- id: \"R10-I2\"\n  summary: \"Independence-Accuracy Trade-off 作为独立贡献有 bias-variance 重述嫌疑\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识major: §6 trade-off与ensemble learning bias-variance tradeoff(Krogh&Vedelsby 1994)同构, 应在§6或§7显式讨论. 缺引Lakshminarayanan et al.(2017)\"\n\n- id: \"R10-VL1\"\n  summary: \"主文缺结果可视化\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15 视觉审查: 主文5个display items(2 figures+3 tables), ~0.63/页, 合理范围低端\"\n\n- id: \"R11-N1\"\n  summary: \"Spearman ρ=1.0 (n=6) 被过度使用——有效自由度远低于6\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识: suggestive非definitive, 应降低claim强度\"\n\n- id: \"R11-N2\"\n  summary: \"中心 claim 'SICA fails' 与统计功效不匹配——Abstract/title 过强\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) R1-N1: 标题scope超出. R2-W1: 'no evidence'需hedge. R1同意加hedge\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识(R1 critical, R2 major): power<21%, MDE远大于观测效应, 'Fail to Improve'=overclaiming. 应改为'No Evidence'或'Limitations of'. R2补充: 多重证据(oracle/shuffle/SCB)部分缓解但不消除功效问题\"\n  action_items:\n    - round: 14\n      action: \"标题限定为Logical Reasoning + Abstract加power caveat\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R11-N3\"\n  summary: \"TOST ±2pp margin 缺乏 principled 论证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15(fresh) 未单独提及\"\n\n- id: \"R11-W1\"\n  summary: \"DRC 评估不充分——仅PW完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15(fresh) 未单独提及\"\n\n- id: \"R11-W2\"\n  summary: \"BR 指标存在循环论证倾向\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1]\n      note: \"R14(fresh) BR子集大小未报告, 需增加n_err列\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识: BR>1部分是trace-count不平衡的数学必然. Shuffle control确认了这一点但论文措辞混淆'结构性局限'与'提取质量问题'. 需更精确区分两个组成部分\"\n  action_items:\n    - round: 14\n      action: \"Table 2增加n_err列 + caption讨论小n_err影响\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R11-W3\"\n  summary: \"术语过度品牌化——'Symbolic Mirage' 偏 dramatic\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"降低'Hypothesis'措辞. 保留名称但重构predictions为observations\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识: 'Symbolic Mirage'与'SCB'关系模糊. 建议明确: Hypothesis是理论假说, SCB是可观测现象\"\n\n- id: \"R11-W4\"\n  summary: \"新颖性定位需更早更明确建立与先验工作的 distinction\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 与R10-W7/R10-I1/R12-N2合并. 三项概念贡献(SCB/K_eff/trade-off)均有先验对应, 需重新定位为empirical contributions\"\n\n- id: \"R11-W5\"\n  summary: \"Independence-Accuracy Trade-off 应定位为量化而非新发现\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识: 见R10-I2, 需与bias-variance tradeoff文献建立联系\"\n\n- id: \"R11-W6\"\n  summary: \"遗漏引用: Byerly & Khashabi (2026 TACL) 等\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"当前论文已引用 Byerly and Khashabi (2026)\"\n  resolution_round: 13\n\n- id: \"R11-W7\"\n  summary: \"27 策略计数膨胀 + 未尝试 trained constraint extractor\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15(fresh) 未单独提及计数膨胀, 但R2提出DuPO/S²R等training-based方法作为missing ref\"\n\n- id: \"R11-VL1\"\n  summary: \"主文缺结果可视化——需上提 Figure 到主文\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15 视觉审查: 主文2 figures+3 tables, 低端但覆盖核心结果\"\n\n- id: \"R12-N1\"\n  summary: \"标题 overclaiming about frontier scale\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 标题scope: 'LLM Reasoning'→'Logical Reasoning'\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 标题仍含'LLM Logical Reasoning', 比'LLM Reasoning'更限定但'Fail to Improve'仍overclaiming given power<21%\"\n  action_items:\n    - round: 14\n      action: \"标题改为 Beyond Self-Consistency: Why Self-Extracted Constraints Fail to Improve LLM Logical Reasoning\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R12-N2\"\n  summary: \"SCB 核心新颖性不足——self-correction failure 在 FOL 载体上的实例化\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识major: SCB = CoT confirmation bias在formal verification管道的实例化. 贡献在于empirical quantification而非新概念\"\n\n- id: \"R12-N3\"\n  summary: \"DRC 作为 Contribution 4 不够充分\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"DRC demoted to practical observation in §6\"\n  resolution_round: 13\n  first_raised_round: 12\n  last_seen_round: 13\n\n- id: \"R12-W1\"\n  summary: \"BR 可能存在循环论证——56.4%零变量重叠使约束按定义支持source answer\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 见R11-W2. 共识: shuffle control确认了trace-count来源, 但论文措辞需更精确\"\n\n- id: \"R12-W2\"\n  summary: \"CIL 名称和 information-theoretic 声称有误导\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Renamed to CCR, removed 'unify' claim\"\n  resolution_round: 13\n  first_raised_round: 12\n  last_seen_round: 13\n\n- id: \"R12-W3\"\n  summary: \"Figure 2 placement——应在正文而非附录\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Figure 2 已在正文 page 7\"\n  resolution_round: 13\n\n- id: \"R12-W4\"\n  summary: \"Appendix vs 主文关键信息分配不合理\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"§3.1压缩+CCR移附录+§5.5/§7展开\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) R2维持§5.4主文过薄, R1部分同意(需补共性失败机制). §7 R1认为Appendix Z已补充\"\n\n- id: \"R12-EC1\"\n  summary: \"Extractor Confound——所有 frontier cross-model extraction 使用同一 Mistral-7B extractor\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15(fresh) 未单独提及, 但§6 escape薄弱问题(R9-W3)隐含此关切\"\n\n- id: \"R13-N1\"\n  summary: \"摘要 BR 4.97× 选择性报告——最极端条件\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识: Abstract报告min-max而非中位数, 4.97×可能是异常值. 定性结论(BR全>1)不受影响但数值呈现有cherry-picking之嫌\"\n  action_items:\n    - round: 13\n      action: \"摘要改为报告 BR 范围或中位数\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R13-N2\"\n  summary: \"统计功效呈现不足——10/16 underpowered, power analysis 埋在附录\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 核心共识: power<21%是最大方法论问题. R1视为critical, R2视为major(多重证据部分缓解). 需在主文§4.2显式讨论功效局限\"\n  action_items:\n    - round: 14\n      action: \"Abstract增加power caveat\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R13-N3\"\n  summary: \"α=0.5 无敏感性分析\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"Appendix Table 11已有α ablation(agreement≥99%), 争议缩窄\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识: ≥99% agreement是主效应近零时的ceiling effect, 非真正鲁棒性. 应加限定语\"\n\n- id: \"R13-W1\"\n  summary: \"符号/指标过载——8页内7个定量工具\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) R2维持minor, R1反驳(ProcessSim不可替代, CCR已在附录). 分歧: 低优先级\"\n  action_items:\n    - round: 14\n      action: \"CCR移入附录减少正文指标密度\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R13-W2\"\n  summary: \"NLI claim 须限定到命题逻辑任务\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15(fresh) 未单独提及, 但功效+scope问题(R11-N2)隐含此关切\"\n\n- id: \"R13-W3\"\n  summary: \"语法去重可能膨胀 BR——未报告语义去重后 BR\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15(fresh) 未单独提及\"\n\n- id: \"R13-W4\"\n  summary: \"Symbolic Mirage Hypothesis §3.3 与 §5 验证不连贯\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 与R14-N2合并: Predictions 1-2 post-hoc, 仅P1(跨架构escape)为真预测\"\n  action_items:\n    - round: 14\n      action: \"§3.3重构predictions + §5验证段落同步修改\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R13-W5\"\n  summary: \"缺引: Dhuliawala et al. 2023 Chain-of-Verification\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"已引用 dhuliawala2023chainofverification\"\n  resolution_round: 14\n\n# R14(fresh) issues\n\n- id: \"R14-N1\"\n  summary: \"标题'LLM Reasoning'范围超出实验证据——仅覆盖逻辑推理\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"共识critical. 改为Logical Reasoning\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 标题已含'Logical Reasoning', 但'Fail'仍overclaiming\"\n\n- id: \"R14-N2\"\n  summary: \"Symbolic Mirage Hypothesis Predictions 1-2 为事后总结非独立预测\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"共识: 仅Prediction 3为独立验证. 保留Hypothesis名称但重构presentations\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) R1维持post-hoc, R2部分REBUT: P1(跨架构escape)是真out-of-sample prediction(§6用新实验验证). P2确实是同义反复. 部分共识: P2重定位为observation, P1可保留prediction框架\"\n  action_items:\n    - round: 14\n      action: \"§3.3区分Motivating Observations vs Testable Prediction\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R14-W1\"\n  summary: \"Cross-architecture实验仅6条件/单一verifier/仅Mistral-7B显著\"\n  category: experiment\n  severity: major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识: 'SC≈70%阈值'的claim无数据支撑, 应限定为'works on weak generators (SC<40%)'\"\n  action_items:\n    - round: 14\n      action: \"结论软化为preliminary evidence + NLI task gap讨论\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R14-W2\"\n  summary: \"8页正文信息过载——§5.5/§6/§7展开不足\"\n  category: writing\n  severity: major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) §5.4需补共性失败机制(1-2句), §7 Appendix Z部分补偿但需加指引\"\n  action_items:\n    - round: 14\n      action: \"§3.1压缩+CCR移附录+§5.5展开remediation分析+§7展开\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R14-W3\"\n  summary: \"'No evidence' claim scope与统计功效不匹配\"\n  category: framing\n  severity: major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 见R11-N2. 核心共识问题\"\n  action_items:\n    - round: 14\n      action: \"Abstract增加power caveat\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R14-W4\"\n  summary: \"BR计算子集大小(n_err)未报告\"\n  category: experiment\n  severity: moderate\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1]\n      note: \"R15(fresh) 与BR循环论证(R11-W2)相关, n_err小时BR可靠性降低\"\n  action_items:\n    - round: 14\n      action: \"Table 2增加n_err列 + caption讨论小n_err可靠性\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R14-W5\"\n  summary: \"Related Work遗漏: SETS(2025), MAV(2025)\"\n  category: writing\n  severity: minor-to-major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [2]\n      note: \"R15(fresh) R2补充遗漏: DuPO(ICLR 2026), S²R(2025), CSP reality check(2025), Lakshminarayanan(2017)\"\n  action_items:\n    - round: 14\n      action: \"Agent验证引用 → §2增加SETS/MAV讨论\"\n      assigned_to: \"agent+paper_agent\"\n      status: in_progress\n\n- id: \"R14-W6\"\n  summary: \"Fleiss' κ→ICC近似仅r=0.625——prevalence paradox\"\n  category: method\n  severity: moderate\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 见R10-N2. 共识: 偏差方向强化论点但应显式讨论\"\n  action_items:\n    - round: 14\n      action: \"附录增加ICC robustness check（低优先级）\"\n      assigned_to: \"agent\"\n      status: in_progress\n\n# R15(fresh) 新发现\n\n- id: \"R15-M1\"\n  summary: \"遗漏引用: DuPO (ICLR 2026) — training-based self-verification\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"共识AGREE. 直接相关§6 escape + §2 trained verifiers讨论\"\n\n- id: \"R15-M2\"\n  summary: \"遗漏引用: S²R (2025) — RL-based self-verification\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"共识AGREE. Training-based escape路径\"\n\n- id: \"R15-M3\"\n  summary: \"遗漏引用: LLM as Formalizers on CSP (arXiv 2505.13252, 2025)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"共识AGREE. 直接互补约束提取质量讨论\"\n\n- id: \"R15-M4\"\n  summary: \"遗漏引用: Lakshminarayanan et al. (2017) Deep Ensembles\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"共识AGREE. §6 independence-accuracy trade-off的理论基础文献\"\n\n- id: \"R15-W1\"\n  summary: \"α=0.5敏感性分析≥99% agreement是ceiling effect——主效应近零时penalty项影响自然可忽略\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"共识: Table 11结论应加限定语(ceiling effect caveat)\"\n"
  }
}
```

</details>

---


### Tool result

_source line 1615 · 2026-05-23T00:50:08.520035+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml\", \"bytes\": 24620}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 1616 · 2026-05-23T00:52:46.358274+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 15 (Fresh)\n\n**论文**: Beyond Self-Consistency: Why Self-Extracted Constraints Fail to Improve LLM Logical Reasoning\n**Venue**: EMNLP 2026 via ARR (May cycle)\n**截止日期**: 2026-05-25\n**审稿模式**: Fresh (2 Reviewers × 1 Round + 交叉分享)\n\n---\n\n## Summary\n\n本文系统评估了 LLM 自提取符号约束（SICA pipeline: trace → FOL constraint extraction → Z3 MAX-SAT → scoring）能否突破 Self-Consistency (SC) 投票天花板。在 6 个开源模型（7B–32B）× 3 个逻辑推理数据集上的 3,000+ condition-evaluations 显示 SICA 未能显著超越 SC（aggregate sign test: 8+/7−, p=1.00; McNemar + BH 校正后无一显著）。作者将此归因于\"Symbolic Confirmation Bias\" (SCB)：自提取约束是模型分布先验的投射（BR 1.66–4.97×），shuffle 控制证实偏差具有结构性。论文贡献了三个诊断指标（K_eff, BR, C₀）和跨架构 NLI 验证的概念验证。\n\n---\n\n## Strengths\n\n**S1. 评估规模出色**\n3,000+ condition-evaluations 覆盖 6 个开源模型 + 5 个 frontier 跨模型提取、3 个核心逻辑推理数据集 + 3 个探索性数据集。27 种 training-free remediation 策略的穷举排查。在负面结果论文中属于罕见的覆盖度。[共识]\n\n**S2. 多重收敛证据策略**\n不依赖单一统计检验：符号检验 + McNemar + BH 校正 + Bootstrap 95% CIs + TOST 等价检验 + BR 机制分析 + ProcessSim 过程独立性 + Oracle 控制。这种三角验证方法论值得肯定。[共识]\n\n**S3. Shuffle 控制设计精巧**\n§5.2 打乱 constraint-answer 配对后 BR_shuf ≈ BR_orig (p > 0.17)，令人信服地证明偏差来自 trace-count 分布（结构性）而非提取质量本身。这是本文方法论上最亮眼的设计。[共识]\n\n**S4. Oracle 控制精确定位问题**\nOracle SICA 在 Mistral-7B FOLIO 上 +29.90pp，证明约束聚合方法在获得高质量约束时有效，将问题精确定位到自提取环节而非 pipeline 本身。[R1 提出, R2 认可]\n\n**S5. 诊断框架有泛化价值**\nK_eff、BR、C₀ 三个指标定义清晰（Eq. 1-5），可直接应用于任何 trace-aggregation 方法的事前评估。C₀ 作为退化条件零成本检测器正确分类全部 60 个条件。[共识]\n\n**S6. 附录极其详尽，可复现性优秀**\n27 页中 18 页附录，覆盖 prompt 模板、Z3 伪代码、case study、oracle control、failure mode 分类、温度敏感性、多种子复现等。[共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix (影响接收决定)\n\n**W1 [critical/major, 共识] 统计功效不足 vs \"Fail to Improve\" claim 强度**\n全部 10 个非退化条件 observed power < 21%（Table 6, Appendix E），MDE 远大于观测效应量。Bootstrap 95% CIs 区间宽度达 ±1.5–2pp（Table 7），无法排除 ±1pp 级别的真实正效应。标题 \"Fail to Improve\" 表述为 evidence of absence，但实际证据仅支持 absence of evidence。R1 视为 critical，R2 视为 major（论文有 oracle/shuffle/SCB 机制等多重收敛证据部分缓解），两位均同意标题和 Abstract 需弱化措辞。\n\n→ **建议**: 标题改为 \"No Evidence That...\" 或 \"Limitations of...\"；Abstract 增加 power caveat（\"observed power < 21% for individual conditions; our conclusion rests on converging evidence across...\"); 主文 §4.2 增加对功效局限性的显式讨论。\n\n**W2 [major, 共识] SCB 概念独立性不足——与 CoT confirmation bias 机制同构**\nSCB 的因果链（distributional prior → biased self-generated output → downstream confirmation）与 Wan et al. (ACL Findings 2025) 的 CoT confirmation bias 在机制层面同构。论文 §2 仅用一句话区分，未充分论证 SCB 作为独立概念的必要性。R1 交叉回应中同意此判断，但补充 SCB 的贡献在于量化该偏差在形式化验证管道中的具体表现（BR 1.66–4.97×）以及证明 Z3 solver 的 provable soundness 无法弥补 input 偏差。\n\n→ **建议**: §2 或 §3.3 坦诚承认与 CoT confirmation bias 的机制同构性，将 SCB 定位为该现象在符号约束管道中的特例和实证深化，而非独立概念。\n\n**W3 [major, 共识] 多种子复制极其有限**\n仅 Mistral-7B（3 seeds, σ=±2.70pp）和 Qwen2.5-14B（4 seeds）进行了多种子复制。种子间方差已超过大多数观测效应量（|Δ| < 2pp），其余 4 个模型单种子运行。在种子方差未充分量化下报告精确 Δ 值有虚假精度之嫌。\n\n→ **建议**: 至少再对 2 个模型补充 3-seed 复制；或在主文诚实讨论单种子结果的局限性，将 Δ 值呈现附带种子不确定性范围。\n\n**W4 [major, 共识] §6 跨架构 NLI escape 证据偏薄，结论外推过度**\n显著增益仅出现在 Mistral-7B（SC < 40%，最弱模型），4/6 main conditions 共享 DeBERTa 系列 verifier。§6 claim \"generators up to SC ≈ 70%\" 无数据支撑——实际验证仅覆盖 SC < 40%。Table 3 显示强生成器（Qwen2.5-14B, SC > 70%）无显著改善。\n\n→ **建议**: claim 限定为 \"works on weak generators (SC < 40%)\"；\"SC ≈ 70% 阈值\" 改为 suggestive observation；§7 的实践建议相应弱化。\n\n### Should-Fix (提升论文质量)\n\n**W5 [major, 共识] K_eff 作为贡献的新颖性 overstated**\nK_eff = K/[1+(K−1)·κ] 是 Kish (1965) effective sample size 的直接应用（论文自引 Kish 1965）。将其称为 \"general diagnostic framework\"（Contribution 2）夸大了方法论创新。R1 补充指出 Fleiss' κ→ICC 近似在高 prevalence 下受 paradox 影响（K_eff 偏高）。\n\n→ **建议**: Contribution 2 重新定位为 \"application of established diagnostics to LLM trace-aggregation evaluation\"。\n\n**W6 [major, 共识] Independence-accuracy trade-off 未与 ensemble learning bias-variance 文献建立联系**\n§6 的权衡（独立但较弱的 verifier 引入更多 variance 但降低 correlated bias）是 ensemble learning 经典 bias-variance tradeoff。论文引用了 Krogh & Vedelsby (1994) 但未讨论对应关系。缺引 Lakshminarayanan et al. (2017) Deep Ensembles。\n\n→ **建议**: §6 或 §7 显式建立与 ensemble diversity 文献的联系。\n\n**W7 [major→部分共识] Symbolic Mirage Hypothesis 的 Predictions post-hoc 性质**\nR1 认为 Predictions 1-2 均为事后构造；R2 部分反驳——P1（结构性独立验证打破 SCB）是 out-of-sample prediction（§6 用全新实验设计验证），P2（MAX-SAT ≈ count-only, 94.4%）确实是 SCB 假说的同义反复。\n\n→ **建议**: P2 重定位为 \"diagnostic observation\"；P1 的 prediction 框架可保留；在 §3.3 明确标注 exploratory/post-hoc 性质。\n\n**W8 [major, 共识] BR 指标存在部分循环论证——措辞混淆结构性局限与提取质量问题**\n当多数答案错误时，更多 trace 产生错误答案 → 更多约束来自这些 trace → BR > 1 部分是 trace-count 不平衡的数学必然。Shuffle 控制实际确认了这一点（BR_real ≈ BR_shuf），但论文措辞时而暗示\"提取质量\"问题，时而作为\"结构性局限\"证据。两位 Reviewer 共识：核心论点成立（自提取约束不提供超越 trace 分布的独立信号），但需更精确区分 BR 的两个组成部分。\n\n→ **建议**: 明确区分 (a) BR 中由 trace-count 不平衡导致的 trivial 分量 与 (b) 约束未能提供超越 trace 分布的独立信号（non-trivial 发现）。\n\n**W9 [minor-major, 共识] Abstract 中 BR 1.66–4.97× 选择性报告**\n仅给出 min-max 范围，未提供中位数或均值。4.97× 可能是单一异常值。定性结论（BR 全 > 1）不受影响，但数值呈现有 cherry-picking 之嫌。\n\n→ **建议**: Abstract 报告中位数或 IQR 而非 min-max。\n\n### Nice-to-Fix (次要改进)\n\n**W10 [minor, 共识] §5.4 Remediation Analysis 缺共性失败机制解释**\nR2 认为 ~15 行过薄；R1 部分反驳（Figure 2 + Table 14 在附录已够，8 页限制下取舍合理）。共识：需补充 1-2 句共性失败机制解释（如\"所有 training-free 策略无法改变约束的分布来源\"）。\n\n**W11 [minor, 共识] \"Symbolic Mirage\" 与 \"SCB\" 术语关系模糊**\nAbstract 用 SCB，§3.3 用 Symbolic Mirage Hypothesis，正文混用。建议明确：Symbolic Mirage Hypothesis 是理论假说，SCB 是该假说预测的可观测现象。\n\n**W12 [minor, 共识] Related Work §2 讨论深度不足**\nWan et al. (2025) 与 SCB 的区分仅一句话；trained verifiers (PRM) 与 self-extracted constraints 的根本区别未讨论——前者引入 external training signal 打破自引用循环。\n\n**W13 [minor, 共识] Spearman ρ=-1.0 (n=6) 用于 capability gap analysis 脆弱**\nn=6 下完美负相关统计意义有限，任一排名互换 ρ 大幅下降。建议定位为 suggestive observation。\n\n**W14 [minor, 分歧] §7 Discussion 过短 vs Appendix Z 补充**\nR2 认为 §7 仅 ~1/3 页不足；R1 反驳称 Appendix Z（~2.5 页）覆盖了 neuro-symbolic 启示、test-time scaling、future directions。共识：在 §7 末尾加明确指引句。\n\n**W15 [minor, 共识] α=0.5 敏感性分析结论过强**\nTable 11 的 ≥99% agreement 是主效应接近零时的 ceiling effect，非真正鲁棒性。应加限定语。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **标题和 Abstract 需弱化** — \"Fail to Improve\" overclaims given power < 21%; 应改为 \"No Evidence\" 或限定 MDE 范围 [R1-W1, R2 交叉 AGREE]\n2. **SCB 应定位为 CoT confirmation bias 在 formal verification 的实例化** — 而非独立概念 [R2-W1, R1 交叉 AGREE]\n3. **多种子复制不足** — 种子方差 ±2.70pp 超过多数效应量 [R1-W3, R2 交叉 AGREE]\n4. **§6 escape 证据偏薄** — claim 应限定到 SC < 40% [R1-W5, R2 交叉 AGREE]\n5. **K_eff 新颖性 overstated** — Kish (1965) 的直接应用 [R2-W2, R1 交叉 AGREE]\n6. **Independence-accuracy trade-off = bias-variance** — 缺 ensemble 文献联系 [R2-W3, R1 交叉 AGREE]\n7. **BR 措辞需精确化** — 区分 trivial (trace-count) 与 non-trivial (independence failure) 分量 [R1-W4, R2 交叉 AGREE with nuance]\n\n## Reviewer Divergence [REBUT]\n\n1. **W1 严重度**: R1 视为 critical，R2 视为 major（多重证据部分缓解频率主义功效不足）。Director 判定：**major-to-critical**——功效问题真实存在但论文的多重收敛策略部分缓解了对单一统计检验的依赖。\n2. **§5.4 主文篇幅**: R2 认为过薄(major)，R1 认为大致合理但需补共性机制(minor)。Director 判定：**should-fix minor**——补 1-2 句解释即可。\n3. **§7 Discussion 长度**: R2 认为过短(minor)，R1 反驳有 Appendix Z。Director 判定：**nice-to-fix**——加指引句。\n4. **指标过载**: R2 认为 ProcessSim/CCR 可移附录(minor)，R1 反驳 ProcessSim 不可替代。Director 判定：**不作为缺陷**——当前安排合理。\n5. **Predictions post-hoc**: R1 认为 P1-P2 均 post-hoc (major)，R2 认为 P1 是真 out-of-sample prediction。Director 判定：P2 需重定位为 observation；P1 可保留 prediction 框架。\n\n---\n\n## Questions for Authors\n\n1. SCB 与 Wan et al. (2025) CoT confirmation bias 在机制层面的本质区别是什么？如果一个方法能减轻 CoT bias，是否预期也能减轻 SCB？\n2. 鉴于 power < 21%，是否愿意将标题中的 \"Fail\" 修改为更审慎的表述（如 \"No Evidence\"）？\n3. 种子间方差 ±2.70pp 超过多数效应量——其余 4 个模型的单种子结果有多少信心？\n4. §6 claim \"generators up to SC ≈ 70%\" 的依据是什么？实际验证仅覆盖 SC < 40%。\n5. BR > 1 在 SC 正确时是否也成立？如果是，这会改变 BR 的解释——说明约束普遍偏向多数答案而非特异性偏向错误答案。\n6. 27 种 training-free remediation 策略中，是否有任何策略在 BH 校正前显示显著正效果？共同特征？\n\n---\n\n## Missing References\n\n以下遗漏引用两位 Reviewer 均同意 [AGREE]：\n\n1. **DuPO: Enabling Reliable LLM Self-Verification via Dual Preference Optimization** (ICLR 2026) — training-based self-verification，直接相关 §6 escape 和 §2 trained verifiers\n2. **S²R: Teaching LLMs to Self-verify and Self-correct via Reinforcement Learning** (2025) — RL-based self-verification，training-based escape 路径\n3. **\"A Reality Check of Language Models as Formalizers on Constraint Satisfaction Problems\"** (arXiv 2505.13252, 2025) — LLM 形式化能力系统评估，直接互补约束提取质量讨论\n4. **Lakshminarayanan et al. (2017) \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\"** — §6 independence-accuracy trade-off 的理论基础文献\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目配置中 external_review 未启用）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（耗时 ~4 分钟）。3 warnings, 13 info, 0 critical。\n\n**Warnings:**\n1. **Pages 1-2**: 前 2 页纯文本（Abstract + Introduction），无视觉锚点。第一个 display item（Figure 1）在 p3 顶部。建议考虑将 Figure 1 提前或加入 motivating example 小图。\n2. **Page 8**: Figure 2（27 策略柱状图）x 轴标签非常小且密集，打印/缩放时可能难以辨认。建议增大字号或分组展示。\n3. **Page 23**: Figure 7（capability gap 散点图）使用蓝-红连续色梯度，对红绿色盲不友好。建议改用 viridis/cividis 色图。\n\n**Positive:**\n- 无 margin 溢出、无 LaTeX 渲染错误、无未解析引用\n- 所有表格使用 booktabs 风格，最优值加粗标注\n- 主文 5 个 display items (2 figures + 3 tables)，分布合理\n- 正文严格 8 页，Limitations 在 p9 顶部，格式完全合规\n\n---\n\n## Overall Assessment\n\n### 维度打分（ACL ARR Review Form）\n\n| 维度 | R1 | R2 | Director |\n|------|----|----|----------|\n| Soundness | 3/5 | 3.5/5 | **3/5** — pipeline 定义清晰、多重收敛策略得当，但 power < 21% 严重削弱核心 claim，BR 循环论证风险未充分讨论 |\n| Excitement | 3/5 | 3/5 | **3/5** — 负面结果有社区价值，诊断框架可迁移，但概念创新有限（SCB ≈ CoT bias 实例化, K_eff = Kish 应用） |\n| Reproducibility | — | 4/5 | **4/5** — 附录提供完整复现细节 |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n### Overall Assessment: **3.5 — Borderline Conference**\n\n两位 Reviewer 独立给出 3.5，交叉分享后均维持。\n\n**核心判断**: 这是一篇实验规模可观、统计控制严谨的实证研究，诊断框架（K_eff, BR, C₀）有实用泛化价值。但三项声称的概念贡献均有先验对应（SCB ↔ CoT confirmation bias, K_eff ↔ Kish 1965, independence-accuracy ↔ bias-variance），加之核心 claim \"fail\" 的强度超出了 power < 21% 的统计支撑，论文当前定位在 Conference 与 Findings 之间。\n\n**接收路径**:\n- 当前状态建议 **Findings** 接收\n- 升至 Conference 需：(1) 弱化标题和 claim 措辞；(2) 坦诚 SCB 与 CoT bias 的同构性并重新定位贡献为 empirical；(3) 补充 2+ 模型多种子；(4) 限定 §6 escape claim 到 SC < 40%；(5) 建立与 ensemble diversity 文献的联系\n\n---\n\n*Report generated by Review Director (Round 15, Fresh mode). Reviewers: R1 (方法/实验/统计), R2 (新颖性/写作/格式). 1 round + cross-sharing. Convergence achieved on all key issues.*",
  "project": "symb_invariant_consensus",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 15 (Fresh)\n\n**论文**: Beyond Self-Consistency: Why Self-Extracted Constraints Fail to Improve LLM Logical Reasoning\n**Venue**: EMNLP 2026 via ARR (May cycle)\n**截止日期**: 2026-05-25\n**审稿模式**: Fresh (2 Reviewers × 1 Round + 交叉分享)\n\n---\n\n## Summary\n\n本文系统评估了 LLM 自提取符号约束（SICA pipeline: trace → FOL constraint extraction → Z3 MAX-SAT → scoring）能否突破 Self-Consistency (SC) 投票天花板。在 6 个开源模型（7B–32B）× 3 个逻辑推理数据集上的 3,000+ condition-evaluations 显示 SICA 未能显著超越 SC（aggregate sign test: 8+/7−, p=1.00; McNemar + BH 校正后无一显著）。作者将此归因于\"Symbolic Confirmation Bias\" (SCB)：自提取约束是模型分布先验的投射（BR 1.66–4.97×），shuffle 控制证实偏差具有结构性。论文贡献了三个诊断指标（K_eff, BR, C₀）和跨架构 NLI 验证的概念验证。\n\n---\n\n## Strengths\n\n**S1. 评估规模出色**\n3,000+ condition-evaluations 覆盖 6 个开源模型 + 5 个 frontier 跨模型提取、3 个核心逻辑推理数据集 + 3 个探索性数据集。27 种 training-free remediation 策略的穷举排查。在负面结果论文中属于罕见的覆盖度。[共识]\n\n**S2. 多重收敛证据策略**\n不依赖单一统计检验：符号检验 + McNemar + BH 校正 + Bootstrap 95% CIs + TOST 等价检验 + BR 机制分析 + ProcessSim 过程独立性 + Oracle 控制。这种三角验证方法论值得肯定。[共识]\n\n**S3. Shuffle 控制设计精巧**\n§5.2 打乱 constraint-answer 配对后 BR_shuf ≈ BR_orig (p > 0.17)，令人信服地证明偏差来自 trace-count 分布（结构性）而非提取质量本身。这是本文方法论上最亮眼的设计。[共识]\n\n**S4. Oracle 控制精确定位问题**\nOracle SICA 在 Mistral-7B FOLIO 上 +29.90pp，证明约束聚合方法在获得高质量约束时有效，将问题精确定位到自提取环节而非 pipeline 本身。[R1 提出, R2 认可]\n\n**S5. 诊断框架有泛化价值**\nK_eff、BR、C₀ 三个指标定义清晰（Eq. 1-5），可直接应用于任何 trace-aggregation 方法的事前评估。C₀ 作为退化条件零成本检测器正确分类全部 60 个条件。[共识]\n\n**S6. 附录极其详尽，可复现性优秀**\n27 页中 18 页附录，覆盖 prompt 模板、Z3 伪代码、case study、oracle control、failure mode 分类、温度敏感性、多种子复现等。[共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix (影响接收决定)\n\n**W1 [critical/major, 共识] 统计功效不足 vs \"Fail to Improve\" claim 强度**\n全部 10 个非退化条件 observed power < 21%（Table 6, Appendix E），MDE 远大于观测效应量。Bootstrap 95% CIs 区间宽度达 ±1.5–2pp（Table 7），无法排除 ±1pp 级别的真实正效应。标题 \"Fail to Improve\" 表述为 evidence of absence，但实际证据仅支持 absence of evidence。R1 视为 critical，R2 视为 major（论文有 oracle/shuffle/SCB 机制等多重收敛证据部分缓解），两位均同意标题和 Abstract 需弱化措辞。\n\n→ **建议**: 标题改为 \"No Evidence That...\" 或 \"Limitations of...\"；Abstract 增加 power caveat（\"observed power < 21% for individual conditions; our conclusion rests on converging evidence across...\"); 主文 §4.2 增加对功效局限性的显式讨论。\n\n**W2 [major, 共识] SCB 概念独立性不足——与 CoT confirmation bias 机制同构**\nSCB 的因果链（distributional prior → biased self-generated output → downstream confirmation）与 Wan et al. (ACL Findings 2025) 的 CoT confirmation bias 在机制层面同构。论文 §2 仅用一句话区分，未充分论证 SCB 作为独立概念的必要性。R1 交叉回应中同意此判断，但补充 SCB 的贡献在于量化该偏差在形式化验证管道中的具体表现（BR 1.66–4.97×）以及证明 Z3 solver 的 provable soundness 无法弥补 input 偏差。\n\n→ **建议**: §2 或 §3.3 坦诚承认与 CoT confirmation bias 的机制同构性，将 SCB 定位为该现象在符号约束管道中的特例和实证深化，而非独立概念。\n\n**W3 [major, 共识] 多种子复制极其有限**\n仅 Mistral-7B（3 seeds, σ=±2.70pp）和 Qwen2.5-14B（4 seeds）进行了多种子复制。种子间方差已超过大多数观测效应量（|Δ| < 2pp），其余 4 个模型单种子运行。在种子方差未充分量化下报告精确 Δ 值有虚假精度之嫌。\n\n→ **建议**: 至少再对 2 个模型补充 3-seed 复制；或在主文诚实讨论单种子结果的局限性，将 Δ 值呈现附带种子不确定性范围。\n\n**W4 [major, 共识] §6 跨架构 NLI escape 证据偏薄，结论外推过度**\n显著增益仅出现在 Mistral-7B（SC < 40%，最弱模型），4/6 main conditions 共享 DeBERTa 系列 verifier。§6 claim \"generators up to SC ≈ 70%\" 无数据支撑——实际验证仅覆盖 SC < 40%。Table 3 显示强生成器（Qwen2.5-14B, SC > 70%）无显著改善。\n\n→ **建议**: claim 限定为 \"works on weak generators (SC < 40%)\"；\"SC ≈ 70% 阈值\" 改为 suggestive observation；§7 的实践建议相应弱化。\n\n### Should-Fix (提升论文质量)\n\n**W5 [major, 共识] K_eff 作为贡献的新颖性 overstated**\nK_eff = K/[1+(K−1)·κ] 是 Kish (1965) effective sample size 的直接应用（论文自引 Kish 1965）。将其称为 \"general diagnostic framework\"（Contribution 2）夸大了方法论创新。R1 补充指出 Fleiss' κ→ICC 近似在高 prevalence 下受 paradox 影响（K_eff 偏高）。\n\n→ **建议**: Contribution 2 重新定位为 \"application of established diagnostics to LLM trace-aggregation evaluation\"。\n\n**W6 [major, 共识] Independence-accuracy trade-off 未与 ensemble learning bias-variance 文献建立联系**\n§6 的权衡（独立但较弱的 verifier 引入更多 variance 但降低 correlated bias）是 ensemble learning 经典 bias-variance tradeoff。论文引用了 Krogh & Vedelsby (1994) 但未讨论对应关系。缺引 Lakshminarayanan et al. (2017) Deep Ensembles。\n\n→ **建议**: §6 或 §7 显式建立与 ensemble diversity 文献的联系。\n\n**W7 [major→部分共识] Symbolic Mirage Hypothesis 的 Predictions post-hoc 性质**\nR1 认为 Predictions 1-2 均为事后构造；R2 部分反驳——P1（结构性独立验证打破 SCB）是 out-of-sample prediction（§6 用全新实验设计验证），P2（MAX-SAT ≈ count-only, 94.4%）确实是 SCB 假说的同义反复。\n\n→ **建议**: P2 重定位为 \"diagnostic observation\"；P1 的 prediction 框架可保留；在 §3.3 明确标注 exploratory/post-hoc 性质。\n\n**W8 [major, 共识] BR 指标存在部分循环论证——措辞混淆结构性局限与提取质量问题**\n当多数答案错误时，更多 trace 产生错误答案 → 更多约束来自这些 trace → BR > 1 部分是 trace-count 不平衡的数学必然。Shuffle 控制实际确认了这一点（BR_real ≈ BR_shuf），但论文措辞时而暗示\"提取质量\"问题，时而作为\"结构性局限\"证据。两位 Reviewer 共识：核心论点成立（自提取约束不提供超越 trace 分布的独立信号），但需更精确区分 BR 的两个组成部分。\n\n→ **建议**: 明确区分 (a) BR 中由 trace-count 不平衡导致的 trivial 分量 与 (b) 约束未能提供超越 trace 分布的独立信号（non-trivial 发现）。\n\n**W9 [minor-major, 共识] Abstract 中 BR 1.66–4.97× 选择性报告**\n仅给出 min-max 范围，未提供中位数或均值。4.97× 可能是单一异常值。定性结论（BR 全 > 1）不受影响，但数值呈现有 cherry-picking 之嫌。\n\n→ **建议**: Abstract 报告中位数或 IQR 而非 min-max。\n\n### Nice-to-Fix (次要改进)\n\n**W10 [minor, 共识] §5.4 Remediation Analysis 缺共性失败机制解释**\nR2 认为 ~15 行过薄；R1 部分反驳（Figure 2 + Table 14 在附录已够，8 页限制下取舍合理）。共识：需补充 1-2 句共性失败机制解释（如\"所有 training-free 策略无法改变约束的分布来源\"）。\n\n**W11 [minor, 共识] \"Symbolic Mirage\" 与 \"SCB\" 术语关系模糊**\nAbstract 用 SCB，§3.3 用 Symbolic Mirage Hypothesis，正文混用。建议明确：Symbolic Mirage Hypothesis 是理论假说，SCB 是该假说预测的可观测现象。\n\n**W12 [minor, 共识] Related Work §2 讨论深度不足**\nWan et al. (2025) 与 SCB 的区分仅一句话；trained verifiers (PRM) 与 self-extracted constraints 的根本区别未讨论——前者引入 external training signal 打破自引用循环。\n\n**W13 [minor, 共识] Spearman ρ=-1.0 (n=6) 用于 capability gap analysis 脆弱**\nn=6 下完美负相关统计意义有限，任一排名互换 ρ 大幅下降。建议定位为 suggestive observation。\n\n**W14 [minor, 分歧] §7 Discussion 过短 vs Appendix Z 补充**\nR2 认为 §7 仅 ~1/3 页不足；R1 反驳称 Appendix Z（~2.5 页）覆盖了 neuro-symbolic 启示、test-time scaling、future directions。共识：在 §7 末尾加明确指引句。\n\n**W15 [minor, 共识] α=0.5 敏感性分析结论过强**\nTable 11 的 ≥99% agreement 是主效应接近零时的 ceiling effect，非真正鲁棒性。应加限定语。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **标题和 Abstract 需弱化** — \"Fail to Improve\" overclaims given power < 21%; 应改为 \"No Evidence\" 或限定 MDE 范围 [R1-W1, R2 交叉 AGREE]\n2. **SCB 应定位为 CoT confirmation bias 在 formal verification 的实例化** — 而非独立概念 [R2-W1, R1 交叉 AGREE]\n3. **多种子复制不足** — 种子方差 ±2.70pp 超过多数效应量 [R1-W3, R2 交叉 AGREE]\n4. **§6 escape 证据偏薄** — claim 应限定到 SC < 40% [R1-W5, R2 交叉 AGREE]\n5. **K_eff 新颖性 overstated** — Kish (1965) 的直接应用 [R2-W2, R1 交叉 AGREE]\n6. **Independence-accuracy trade-off = bias-variance** — 缺 ensemble 文献联系 [R2-W3, R1 交叉 AGREE]\n7. **BR 措辞需精确化** — 区分 trivial (trace-count) 与 non-trivial (independence failure) 分量 [R1-W4, R2 交叉 AGREE with nuance]\n\n## Reviewer Divergence [REBUT]\n\n1. **W1 严重度**: R1 视为 critical，R2 视为 major（多重证据部分缓解频率主义功效不足）。Director 判定：**major-to-critical**——功效问题真实存在但论文的多重收敛策略部分缓解了对单一统计检验的依赖。\n2. **§5.4 主文篇幅**: R2 认为过薄(major)，R1 认为大致合理但需补共性机制(minor)。Director 判定：**should-fix minor**——补 1-2 句解释即可。\n3. **§7 Discussion 长度**: R2 认为过短(minor)，R1 反驳有 Appendix Z。Director 判定：**nice-to-fix**——加指引句。\n4. **指标过载**: R2 认为 ProcessSim/CCR 可移附录(minor)，R1 反驳 ProcessSim 不可替代。Director 判定：**不作为缺陷**——当前安排合理。\n5. **Predictions post-hoc**: R1 认为 P1-P2 均 post-hoc (major)，R2 认为 P1 是真 out-of-sample prediction。Director 判定：P2 需重定位为 observation；P1 可保留 prediction 框架。\n\n---\n\n## Questions for Authors\n\n1. SCB 与 Wan et al. (2025) CoT confirmation bias 在机制层面的本质区别是什么？如果一个方法能减轻 CoT bias，是否预期也能减轻 SCB？\n2. 鉴于 power < 21%，是否愿意将标题中的 \"Fail\" 修改为更审慎的表述（如 \"No Evidence\"）？\n3. 种子间方差 ±2.70pp 超过多数效应量——其余 4 个模型的单种子结果有多少信心？\n4. §6 claim \"generators up to SC ≈ 70%\" 的依据是什么？实际验证仅覆盖 SC < 40%。\n5. BR > 1 在 SC 正确时是否也成立？如果是，这会改变 BR 的解释——说明约束普遍偏向多数答案而非特异性偏向错误答案。\n6. 27 种 training-free remediation 策略中，是否有任何策略在 BH 校正前显示显著正效果？共同特征？\n\n---\n\n## Missing References\n\n以下遗漏引用两位 Reviewer 均同意 [AGREE]：\n\n1. **DuPO: Enabling Reliable LLM Self-Verification via Dual Preference Optimization** (ICLR 2026) — training-based self-verification，直接相关 §6 escape 和 §2 trained verifiers\n2. **S²R: Teaching LLMs to Self-verify and Self-correct via Reinforcement Learning** (2025) — RL-based self-verification，training-based escape 路径\n3. **\"A Reality Check of Language Models as Formalizers on Constraint Satisfaction Problems\"** (arXiv 2505.13252, 2025) — LLM 形式化能力系统评估，直接互补约束提取质量讨论\n4. **Lakshminarayanan et al. (2017) \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\"** — §6 independence-accuracy trade-off 的理论基础文献\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目配置中 external_review 未启用）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（耗时 ~4 分钟）。3 warnings, 13 info, 0 critical。\n\n**Warnings:**\n1. **Pages 1-2**: 前 2 页纯文本（Abstract + Introduction），无视觉锚点。第一个 display item（Figure 1）在 p3 顶部。建议考虑将 Figure 1 提前或加入 motivating example 小图。\n2. **Page 8**: Figure 2（27 策略柱状图）x 轴标签非常小且密集，打印/缩放时可能难以辨认。建议增大字号或分组展示。\n3. **Page 23**: Figure 7（capability gap 散点图）使用蓝-红连续色梯度，对红绿色盲不友好。建议改用 viridis/cividis 色图。\n\n**Positive:**\n- 无 margin 溢出、无 LaTeX 渲染错误、无未解析引用\n- 所有表格使用 booktabs 风格，最优值加粗标注\n- 主文 5 个 display items (2 figures + 3 tables)，分布合理\n- 正文严格 8 页，Limitations 在 p9 顶部，格式完全合规\n\n---\n\n## Overall Assessment\n\n### 维度打分（ACL ARR Review Form）\n\n| 维度 | R1 | R2 | Director |\n|------|----|----|----------|\n| Soundness | 3/5 | 3.5/5 | **3/5** — pipeline 定义清晰、多重收敛策略得当，但 power < 21% 严重削弱核心 claim，BR 循环论证风险未充分讨论 |\n| Excitement | 3/5 | 3/5 | **3/5** — 负面结果有社区价值，诊断框架可迁移，但概念创新有限（SCB ≈ CoT bias 实例化, K_eff = Kish 应用） |\n| Reproducibility | — | 4/5 | **4/5** — 附录提供完整复现细节 |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n### Overall Assessment: **3.5 — Borderline Conference**\n\n两位 Reviewer 独立给出 3.5，交叉分享后均维持。\n\n**核心判断**: 这是一篇实验规模可观、统计控制严谨的实证研究，诊断框架（K_eff, BR, C₀）有实用泛化价值。但三项声称的概念贡献均有先验对应（SCB ↔ CoT confirmation bias, K_eff ↔ Kish 1965, independence-accuracy ↔ bias-variance），加之核心 claim \"fail\" 的强度超出了 power < 21% 的统计支撑，论文当前定位在 Conference 与 Findings 之间。\n\n**接收路径**:\n- 当前状态建议 **Findings** 接收\n- 升至 Conference 需：(1) 弱化标题和 claim 措辞；(2) 坦诚 SCB 与 CoT bias 的同构性并重新定位贡献为 empirical；(3) 补充 2+ 模型多种子；(4) 限定 §6 escape claim 到 SC < 40%；(5) 建立与 ensemble diversity 文献的联系\n\n---\n\n*Report generated by Review Director (Round 15, Fresh mode). Reviewers: R1 (方法/实验/统计), R2 (新颖性/写作/格式). 1 round + cross-sharing. Convergence achieved on all key issues.*",
    "project": "symb_invariant_consensus",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
  }
}
```

</details>

---


### Tool result

_source line 1617 · 2026-05-23T00:52:50.375071+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_970d5ea3f54df81296b97321fcded892:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4016
}
```

</details>

---


### Assistant

_source line 1618 · 2026-05-23T00:52:59.302068+00:00_

审稿报告已投递至 Research Director。

**Round 15 (Fresh) 审稿完成**

- **Overall: 3.5 (Borderline Conference)**，建议 Findings 接收
- 2 Reviewers × 1 轮 + 交叉分享，关键问题全部达成共识
- Issue Tracker 已同步更新（新增 5 条 R15 issue，更新 30+ 条现有 issue）
- 视觉审查已完成（3 warnings / 0 critical），结果已拼入报告

**核心问题优先级**:
1. 标题/claim overclaiming (power < 21%) — must-fix
2. SCB 概念独立性 — must-fix (重新定位)
3. 多种子不足 — must-fix
4. §6 escape 外推过度 — must-fix
5. K_eff / bias-variance 贡献定位 — should-fix

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 112

## Round 112

2 recorded events


### User

_source line 1619 · 2026-05-23T00:53:01.854451+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。对 R1 的 8 个 Weakness 逐条回应：

- **W1 (功效不足)**: [AGREE] 但将严重度从 critical 降为 major，因论文有 oracle/shuffle/SCB 多重收敛证据，不完全依赖 frequentist null results
- **W2 (事后预测)**: [REBUT] P1 (cross-architecture escape) 是真正的 out-of-sample prediction (§6 新实验)；仅 P2 属事后总结
- **W3 (多种子不足)**: [AGREE] 4/6 模型单种子，种子方差 > 观测效应量
- **W4 (BR 循环论证)**: [AGREE with nuance] Shuffle control 实际上确认了 R1 的关切——但这恰恰是论文的论点（约束不提供独立信息），问题在措辞不清
- **W5 (§6 证据薄)**: [AGREE] 与我自己的审查一致
- **W6 (ρ=-1.0 脆弱)**: [AGREE]
- **W7 (κ prevalence paradox)**: [AGREE]
- **W8 (α 敏感性)**: [AGREE] 是 floor effect 而非真正鲁棒性

两位 Reviewer 在功效不足、§6 证据薄、多种子不足三个核心问题上高度一致。维持 Overall 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1620 · 2026-05-23T00:53:14.054277+00:00_

审稿报告已投递至 Research Director。

**Round 15 (Fresh) 审稿完成。**

核心结论：**3.5 — Borderline Conference**，建议 Findings 接收。

关键共识问题：
1. 标题 "Fail to Improve" overclaiming（power < 21%）
2. SCB 与 CoT confirmation bias 机制同构，概念贡献需重新定位
3. 多种子复制不足（4/6 模型单种子，σ=±2.70pp > 效应量）
4. §6 escape 证据仅覆盖 SC < 40%，结论外推过度
5. K_eff/independence-accuracy trade-off 相对先验工作增量有限

Issue Tracker 已同步更新（R15 新增 5 条，更新 30+ 条现有 issue）。视觉审查完成（3 warnings，格式合规）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 113

## Round 113

54 recorded events


### User

_source line 1621 · 2026-05-23T08:01:47.779716+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: symb_invariant_consensus
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex
- 目标 venue: EMNLP 2026 ARR
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1622 · 2026-05-23T08:01:53.467050+00:00_

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
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1623 · 2026-05-23T08:01:53.518149+00:00_

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
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1624 · 2026-05-23T08:02:01.702071+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,WebSearch",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,WebSearch",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 1625 · 2026-05-23T08:02:01.702507+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1626 · 2026-05-23T08:02:04.313774+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,get_visual_check_status,submit_review_report_to_research_director,update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,get_visual_check_status,submit_review_report_to_research_director,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1627 · 2026-05-23T08:02:04.364468+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1628 · 2026-05-23T08:02:18.783234+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1629 · 2026-05-23T08:02:18.884078+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1630 · 2026-05-23T08:02:23.052054+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 1631 · 2026-05-23T08:02:25.362398+00:00_

{"result":"# 项目 symb_invariant_consensus 概况\n\n## 实验状态 (173 个)\n\n- **sica_k_sensitivity_14b**: DONE (success) — \n- **exp-011-llama8b**: DONE (failed) — \n- **exp-016-weighted-sc**: DONE (success) — \n- **exp-005**: DONE (negative) — \n- **sica_folio30**: DONE (killed) — \n- **sica_d016_c0_precheck**: DONE (success) — \n- **sica_proofwriter30_v2**: DONE (killed) — \n- **sica_proofwriter30**: DONE (failed) — \n- **sica_aime30_v3**: DONE (killed) — \n- **sica_aime30_v2**: DONE (killed) — \n- **sica_aime30_t07**: DONE (killed) — \n- **mvp_math50_t07**: DONE (killed) — \n- **sica_smoke_5q**: DONE (success) — \n- **smoke-test-5q**: PREPARING (failed) — \n- **crd_folio_main**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp-multi-seed-llama-pw-seed789-v2 | LLaMA-3.1-8B PW seed789 多种子复制（westd-30973 cuda:1 全新运行）。替代 16639 cuda:0 上的慢速运行（12/600）。验证 SCB 在 ProofWriter 上跨 seed 稳定性。 | — | — | — |\n| exp-multi-seed-llama-pw-seed456-v2 | LLaMA-3.1-8B PW seed456 多种子复制（westd-30973 cuda:2 全新运行）。验证 SCB 在 ProofWriter 上跨 seed 稳定性（Δ(SICA-SC)≤0）。配合 seed42/123/789 组成 4-seed 覆盖。 | — | — | — |\n| exp-multi-seed-qwen25-pw-seed789-v3 | Qwen2.5-14B PW seed789 多种子复制（westd-30973 cuda:0 全新运行）。替代 v2 在 16639 cuda:2 上的慢速运行（53/600）。验证 SCB 在 ProofWriter 上跨 seed 稳定性。 | — | — | — |\n\n## 待处理\n- exp-multi-seed-llama-pw-seed456: LLaMA-3.1-8B PW seed456 多种子复制。验证 SCB 在 ProofWriter 上跨 seed 稳定性（Δ(SICA-SC)≤0）。配合 seed42/123/789 组成 4-seed 覆盖。（排队等待 GPU）\n- exp-deberta-ft-combo: Fine-tuned DeBERTa-large on ProofWriter OWA depth-5 achieves near-perfect NLI accuracy (99.67%) and provides massive combo gains over SC baseline when used as external verifier, demonstrating that domain-specific NLI fine-tuning breaks the SCB ceiling by providing truly independent verification signal.（准备中）\n- exp-multi-seed-mistral-folio: Multi-seed replication (seeds 123,456,789) of Mistral-7B × FOLIO-20
…[truncated 1733 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 2310
}
```

</details>

---


### Tool call

_source line 1632 · 2026-05-23T08:02:25.915282+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_13/submitted.pdf 2>&1",
  "description": "Check paper files existence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_13/submitted.pdf 2>&1",
    "description": "Check paper files existence"
  }
}
```

</details>

---


### Tool result

_source line 1633 · 2026-05-23T08:02:26.367845+00:00_

-rw-r--r-- 1 ubuntu ubuntu 652787 May 23 07:50 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_13/submitted.pdf
-rw-r--r-- 1 ubuntu ubuntu   1778 May 22 13:51 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1634 · 2026-05-23T08:02:26.368246+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 1635 · 2026-05-23T08:02:32.596276+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

I found results related to EMNLP 2026
…[truncated 1430 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 6228
}
```

</details>

---


### Tool call

_source line 1636 · 2026-05-23T08:02:35.658636+00:00_

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
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline page limit"
  }
}
```

</details>

---


### Tool call

_source line 1637 · 2026-05-23T08:02:36.212025+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines author instructions format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines author instructions format requirements"
  }
}
```

</details>

---


### Tool call

_source line 1638 · 2026-05-23T08:02:38.370907+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1639 · 2026-05-23T08:02:38.421577+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % removed: not available in this TeX distribution
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{amsthm}
13	\usepackage{tcolorbox}
14	\tcbuselibrary{skins}
15	\usepackage{booktabs}
16	\usepackage{multirow}
17	\usepackage{xcolor}
18	\usepackage{enumitem}
19	\usepackage{subcaption}
20	\usepackage{tikz}
21	\usetikzlibrary{arrows.meta,positioning,calc,fit}
22	\usepackage{listings}
23	\usepackage{algorithm}
24	\usepackage{algpseudocode}
25	\usepackage{hyperref}
26	\usepackage{cleveref}
27	
28	\lstset{
29	  basicstyle=\small\ttfamily,
30	  breaklines=true,
31	  frame=single,
32	  xleftmargin=1em,
33	  xrightmargin=1em,
34	  aboveskip=0.5em,
35	  belowskip=0.5em,
36	}
37	
38	\graphicspath{{../figures/paper/}{figures/}}
39	
40	\title{Beyond Self-Consistency: Why Self-Extracted Constraints\\Fail to Improve LLM Logical Reasoning}
41	
42	\author{Anonymous}
43	
44	\begin{document}
45	\maketitle
46	
47	% Tighten spacing for 8-page budget
48	\setlength{\textfloatsep}{5pt plus 2pt minus 4pt}
49	\setlength{\dbltextfloatsep}{5pt plus 2pt minus 4pt}
50	\setlength{\floatsep}{3pt plus 2pt minus 2pt}
51	\setlength{\dblfloatsep}{3pt plus 2pt minus 2pt}
52	\setlength{\abovecaptionskip}{2pt}
53	\setlength{\belowcaptionskip}{0pt}
54	\setlength{\abovedisplayskip}{4pt plus 1pt minus 2pt}
55	\setlength{\belowdisplayskip}{4pt plus 1pt minus 2pt}
56	\setlength{\intextsep}{5pt plus 1pt minus 2pt}
57	
58	\input{abstract}
59	
60	\input{introduction}
61	
62	\input{related_work}
63	
64	\input{method}
65	
66	\input{experiments}
67	
68	\input{analysis}
69	
70	\input{solutions}
71	
72	\input{discussion}
73	
74	\vspace{-1mm}
75	\section*{Limitations}
76	\input{limitations_content}
77	
78	\bibliography{references}
79	
80	\appendix
81	\input{appendix}
82	

…[truncated 21 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1640 · 2026-05-23T08:02:40.279522+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"}]

Based on the search results for EMNLP 2026 Call for Papers:

**Submission Deadline:**
The EMNLP 2026 paper submission deadline is 2026-05-25 23:59:59 (UTC-12).

**Page Limits:**
The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

**Additional Information:**
All deadlines are 11:59PM UTC-12:00
…[truncated 272 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 4620
}
```

</details>

---


### Tool result

_source line 1641 · 2026-05-23T08:02:45.053054+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines author instructions format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"}]

Based on the search results, here's information about ACL Rolling Review 2026 submission guidelines:

## Submission Format Requirements

All long, short, and theme papers must follow the ACL Author Guidelines. Paper submissions must use the official ACL style template. Submissions that do not conform to the required styles, including paper size, margin width, and font size restrictions, will be rejected without 
…[truncated 1183 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 8841
}
```

</details>

---


### Tool call

_source line 1642 · 2026-05-23T08:03:10.554179+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_13/submitted.pdf",
  "pages": "1-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_13/submitted.pdf",
    "pages": "1-10"
  }
}
```

</details>

---


### Tool call

_source line 1643 · 2026-05-23T08:03:10.554632+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool call

_source line 1644 · 2026-05-23T08:03:10.707218+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>&1; cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | head -100",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>&1; cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | head -100",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1645 · 2026-05-23T08:03:11.261415+00:00_

PDF pages extracted: 10 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_13/submitted.pdf (637.5KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 707
}
```

</details>

---


### Tool result

_source line 1646 · 2026-05-23T08:03:11.281697+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'symb_invariant_consensus'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 727
}
```

</details>

---


### Tool result

_source line 1647 · 2026-05-23T08:03:11.382686+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml
# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)
- id: "R1-C1"
  summary: "Method Stage 3 sat() implementation undescribed"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit."
  resolution_round: 3

- id: "R1-C2"
  summary: "Most experiments underpowered (n≤60), no power analysis"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "Power analysis + Bootstrap CIs added. Larger n conditions (200-600)."
  resolution_round: 3

- id: "R1-C3"
  summary: "Oracle/upper-bound experiment missing"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp."
  resolution_round: 3

- id: "R1-C4"
  summary: "Huang et al. (ICLR 2024) not cited"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: "Huang, Stechly, Kambhampati all cited and discussed."
  resolution_round: 2

- id: "R1-C5"
  summary: "Critical related work missing"
  category: writing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "~48 citations, 5 Related Work paragraphs."
  resolution_round: 3

- id: "R1-C9"
  summary: "Capability trap novelty unclear"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "Reframed as regime-dependent analysis with CJT framework."
  resolution_round: 3

- id: "R3-N1"
  summary: "σ(c,a) scoring inconsistent between self-extraction and oracle"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 3
  last_seen_round: 4
  resolutio
…[truncated 719 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 675
}
```

</details>

---


### Tool call

_source line 1648 · 2026-05-23T08:03:18.153810+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_13/submitted.pdf",
  "pages": "11-20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_13/submitted.pdf",
    "pages": "11-20"
  }
}
```

</details>

---


### Tool result

_source line 1649 · 2026-05-23T08:03:19.560621+00:00_

PDF pages extracted: 10 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_13/submitted.pdf (637.5KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool call

_source line 1650 · 2026-05-23T08:03:19.723080+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | wc -l; echo \"---\"; cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | tail -200",
  "description": "Read full review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | wc -l; echo \"---\"; cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | tail -200",
    "description": "Read full review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1651 · 2026-05-23T08:03:19.824250+00:00_

935
---
# R14(fresh) issues

- id: "R14-N1"
  summary: "标题'LLM Reasoning'范围超出实验证据——仅覆盖逻辑推理"
  category: framing
  severity: critical
  status: in_progress
  first_raised_round: 14
  last_seen_round: 15
  mentions:
    - round: 14
      reviewers: [1, 2]
      note: "共识critical. 改为Logical Reasoning"
    - round: 15
      reviewers: [1, 2]
      note: "R15(fresh) 标题已含'Logical Reasoning', 但'Fail'仍overclaiming"

- id: "R14-N2"
  summary: "Symbolic Mirage Hypothesis Predictions 1-2 为事后总结非独立预测"
  category: method
  severity: critical
  status: in_progress
  first_raised_round: 14
  last_seen_round: 15
  mentions:
    - round: 14
      reviewers: [1, 2]
      note: "共识: 仅Prediction 3为独立验证. 保留Hypothesis名称但重构presentations"
    - round: 15
      reviewers: [1, 2]
      note: "R15(fresh) R1维持post-hoc, R2部分REBUT: P1(跨架构escape)是真out-of-sample prediction(§6用新实验验证). P2确实是同义反复. 部分共识: P2重定位为observation, P1可保留prediction框架"
  action_items:
    - round: 14
      action: "§3.3区分Motivating Observations vs Testable Prediction"
      assigned_to: "paper_agent"
      status: in_progress

- id: "R14-W1"
  summary: "Cross-architecture实验仅6条件/单一verifier/仅Mistral-7B显著"
  category: experiment
  severity: major
  status: in_progress
  first_raised_round: 14
  last_seen_round: 15
  mentions:
    - round: 15
      reviewers: [1, 2]
      note: "R15(fresh) 共识: 'SC≈70%阈值'的claim无数据支撑, 应限定为'works on weak generators (SC<40%)'"
  action_items:
    - round: 14
      action: "结论软化为preliminary evidence + NLI task gap讨论"
      assigned_to: "paper_agent"
      status: in_progress

- id: "R14-W2"
  summary: "8页正文信息过载——§5.5/§6/§7展开不足"
  category: writing
  severity: major
  status: in_progress
  first_raised_round: 14
  last_seen_round: 15
  mentions:
    - round: 15
      reviewers: [1, 2]
      note: "R15(fresh) §5.4需补共性失败机制(1-2句), §7 Appendix Z部分补偿但需加指引"
  action_items:
    - round: 14
      action: "§3.1压缩+CCR移附录+§5.5展开remediation分析+§7展开"
      assigned_to: "paper_agent"
      status: in_progress

- id: "R14
…[truncated 3167 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1652 · 2026-05-23T08:03:28.864130+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_13/submitted.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_13/submitted.pdf 2>/dev/null || echo \"pdfinfo not available\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_13/submitted.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_13/submitted.pdf 2>/dev/null || echo \"pdfinfo not available\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 1653 · 2026-05-23T08:03:29.617501+00:00_

Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Sat May 23 07:50:44 2026 UTC
ModDate:         Sat May 23 07:50:44 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           26
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       652787 bytes
Optimized:       no
PDF version:     1.7

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 1654 · 2026-05-23T08:03:29.818839+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/project_config.yaml 2>/dev/null | grep -A 10 \"external_review\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/project_config.yaml 2>/dev/null | grep -A 10 \"external_review\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1655 · 2026-05-23T08:03:29.869570+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1656 · 2026-05-23T08:03:35.056016+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/project_config.yaml 2>/dev/null | head -80",
  "description": "Read project config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/project_config.yaml 2>/dev/null | head -80",
    "description": "Read project config"
  }
}
```

</details>

---


### Tool result

_source line 1657 · 2026-05-23T08:03:35.106670+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1658 · 2026-05-23T08:03:41.083461+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus -name \"*.yaml\" -path \"*/agent/*\" 2>/dev/null | head -10; find /home/ubuntu/.agent-ml-research-idea_gen_0513_3 -name \"project_config*\" -maxdepth 3 2>/dev/null | head -10",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus -name \"*.yaml\" -path \"*/agent/*\" 2>/dev/null | head -10; find /home/ubuntu/.agent-ml-research-idea_gen_0513_3 -name \"project_config*\" -maxdepth 3 2>/dev/null | head -10",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 1659 · 2026-05-23T08:03:41.184354+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1660 · 2026-05-23T08:03:44.748203+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3 -name \"*.yaml\" -maxdepth 2 2>/dev/null | head -20",
  "description": "Find yaml config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_3 -name \"*.yaml\" -maxdepth 2 2>/dev/null | head -20",
    "description": "Find yaml config files"
  }
}
```

</details>

---


### Tool result

_source line 1661 · 2026-05-23T08:03:44.849208+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_3/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/global/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/global/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/resources.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1662 · 2026-05-23T08:03:51.927586+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A 5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/*.yaml 2>/dev/null; grep -rn \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/ 2>/dev/null",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A 5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/*.yaml 2>/dev/null; grep -rn \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/config/ 2>/dev/null",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1663 · 2026-05-23T08:03:51.978311+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1664 · 2026-05-23T08:03:55.743864+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "file": "decisions.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1665 · 2026-05-23T08:03:55.895535+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/decisions.yaml\", \"content\": \"_next_id: 156\\ndecisions:\\n- id: D001\\n  date: 2026-05-15 08:47 UTC\\n  summary: MVP 验证方案：50 题 MATH-500 分层子集，SICA vs SC@K=12\\n  rationale: SICA 核心价值取决于两个前提：(1) 能从推理 trace 可靠提取符号约束；(2) 跨路径矛盾率足够高（>5%）使形式化验证有意义。Reviewer\\n    给 impact 3/5，核心担忧是\\\"若矛盾率<5%则动机不成立\\\"。MVP 直接验证这两个前提，50 题按难度分层可同时观察 Extraction-Verification\\n    Paradox（难题提取差但矛盾多）。Pass 则进入全量实验冲 EMNLP/AAAI，Fail 则及时止损。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-15 08:52 UTC\\n  summary: 拒绝 CRD pivot，要求回归 SICA 原始方案\\n  rationale: Reviewer critical 审查发现 Agent 实施的是\\\"跨表征分歧诊断\\\"(CRD)，与 IDEA_BRIEF 定义的 SICA\\n    完全不同：CRD 用双表征（FOL+SymPy）做单解分歧检测，无多路径采样、无 MAX-SAT 共识——这正是 SICA 区别于 VERGE/D&P 的核心创新点。CRD\\n    的 novelty 定位与 VERGE 高度重叠（单输出验证+修复），无法支撑 EMNLP 投稿。同时 MVP 标准被静默替换，ROADMAP 的三条 pass\\n    criteria 从未测试。98GB GPU 完全能跑 QwQ-32B，无理由换 Qwen3-32B-AWQ。必须回归 SICA：K=12 多路径采样 →\\n    符号约束提取 → Z3 加权 partial MAX-SAT → 不变量共识打分。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-15 08:54 UTC\\n  summary: MVP 标准 v2：三档判定 + 矛盾绝对数 ≥5 + accuracy ≥SC+2pp + ProofWriter sanity check\\n  rationale: Reviewer warning 指出：(1) 5% 矛盾率阈值在 50 题上仅 2.5 题，置信区间极宽——改为绝对数 ≥5 题；(2)\\n    ≥SC+0.1pp 也过关无意义——改为 ≥2pp 或 p<0.1；(3) 灰色区间无处理——新增 Inconclusive 档，触发扩展到 100 题重测；(4)\\n    单域 MATH-500 不够——加 10 题 ProofWriter 做逻辑域 sanity check；(5) 模型不能模糊——固定 QwQ-32B，不可替换。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-15 12:02 UTC\\n  summary: MVP T=0.7 继续跑完（需要完整数据），diagnostic 自然结束后 GPU 带宽恢复；AIME 30 题排在 MVP 之后\\n  rationale: Temperature 诊断 4/5 题显示 T=0.7/0.9/1.0 均几乎不产生答案分歧——C2/C3 高风险 FAIL。但仍决定让\\n    MVP 跑完：(1) 50 题完整数据无论正负都有价值（负面结果=SICA 在强模型上无信号，本身是发现）；(2) GPU 已分配且无其他实验排队；(3)\\n    smoke test L5 有 3 条矛盾，50 题中 L4-5 有 20 题可能产生更多信号。MVP 完成后立即跑 AIME 30 题（QwQ-32B ~79.5%，分歧应更明显），作为\\\"高难度\\n    sweet
…[truncated 11002 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1666 · 2026-05-23T08:04:36.754166+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "symb_invariant_consensus",
  "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
  }
}
```

</details>

---


### Tool call

_source line 1667 · 2026-05-23T08:04:37.206080+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 1668 · 2026-05-23T08:05:09.445927+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 32691
}
```

</details>

---


### Tool result

_source line 1669 · 2026-05-23T08:05:09.446635+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 32240
}
```

</details>

---


### Tool call

_source line 1670 · 2026-05-23T08:05:13.365758+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计 + 统计分析**。\n\n## 论文信息\n- **标题**: Beyond Self-Consistency: Why Self-Extracted Constraints Fail to Improve LLM Logical Reasoning\n- **文件**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_13/submitted.pdf`\n- **目标 Venue**: EMNLP 2026 ARR (deadline: 2026-05-25)\n\n## Venue 要求\n- **页数限制**: Long paper 正文 8 页，引用不限，Limitations 和 Ethics 不计入页数（但不能包含过多额外内容）\n- **模板**: ACL style template (double-column)\n- **匿名规则**: Double-blind。论文不得包含作者信息，自引须匿名化，补充材料和代码链接须匿名\n- **Limitations**: 必须包含，放在正文中 conclusion 之后，仅讨论局限性，不得包含新实验/图表/分析\n- **评分标准**: Overall Assessment 5分制 (5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit)\n\n## 你的审查侧重\n\n### 1. 方法严谨性\n- **Proposition 1** (Symbolic Confirmation Bias is Structural) 的证明是否严格？假设 A1/A2 是否合理？是否存在逻辑漏洞？\n- **Degeneration condition** (Eq. 4) 的推导是否正确？\n- **Bias Ratio** (Eq. 5) 的定义和使用是否合理？BR > 1 是否真的意味着 confirmation bias？\n- **K_eff** (Eq. 1) 从 ensemble theory 的借用是否恰当？Fleiss' κ → effective sample size 的近似是否有理论支撑？\n- **Scoring function** (Eq. 3) 中 α=0.5 的选择是否有理论或实验依据？敏感性分析是否充分？\n- MAX-SAT 形式化（Algorithm 1-2）是否正确？source-trace attribution scoring 是否有 bias？\n\n### 2. 实验设计\n- 6 个模型 × 3 个 domain 的覆盖是否足够支撑 claims？\n- **样本量**: n=204 (FOLIO), n=600 (ProofWriter), n=200 (LogiQA/StrategyQA), n=30/22 (GSM8K/AIME) 是否充足？\n- **统计检验**: McNemar exact test + BH correction 是否恰当？Bootstrap CI 方法是否正确？\n- **Power analysis** (Appendix D): MDE 和 observed power 是否支持结论？作者承认 observed power < 21%——这对 \"no evidence\" 的 claim 意味着什么？\n- **Multi-seed replication**: 仅 Mistral-7B (3 seeds) 和 Qwen2.5-14B (4 seeds)，是否足够？\n- **Oracle 实验** (Appendix G): gold annotation 替换是否控制了混淆变量？\n- **27 remediation strategies** 的选择是否覆盖了合理的设计空间？是否遗漏了明显的策略？\n- **Cross-architecture escape** (§6): DeBERTa-large 作为 verifier 的实验设计是否合理？仅在 Mistral-7B (SC=39.33%) 上显著——这是否限制了 claim 的 generalizability？\n\n### 3. 统计分析\n- Table 1 中 BH correction 后无条件显著——这是一个 null result paper，统计解读是否恰当？\n- \"absence of evidence is not evidence of absence\" 的讨论是否充分？\n- BR 估计在小 n_err 条件下是否可靠？Table 2 中 n_err 范围 12-90，CI 是否报告？\n- TOST equivalence test (Lakens, 2017) 用 ±2pp margin——这个 margin 的选择是否有依据？\n- Appendix D 中 power analysis 方法是否正确？\n\n请给出完整审稿意见，格式如下：\n\n```\n## Summary\n(2-3句论文概述)\n\n## Strengths\n(逐条列出)\n\n## Weaknesses\n(逐条列出，按严重程度排序，标注 [Critical] / [Major] / [Minor])\n\n## Questions\n(需要作者澄清的问题)\n\n## Missing References\n(遗漏的重要相关工作)\n\n## Overall Assessment\n(评分 + 置信度 + 理由)\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "symb_invariant_consensus",
    "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计 + 统计分析**。\n\n## 论文信息\n- **标题**: Beyond Self-Consistency: Why Self-Extracted Constraints Fail to Improve LLM Logical Reasoning\n- **文件**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_13/submitted.pdf`\n- **目标 Venue**: EMNLP 2026 ARR (deadline: 2026-05-25)\n\n## Venue 要求\n- **页数限制**: Long paper 正文 8 页，引用不限，Limitations 和 Ethics 不计入页数（但不能包含过多额外内容）\n- **模板**: ACL style template (double-column)\n- **匿名规则**: Double-blind。论文不得包含作者信息，自引须匿名化，补充材料和代码链接须匿名\n- **Limitations**: 必须包含，放在正文中 conclusion 之后，仅讨论局限性，不得包含新实验/图表/分析\n- **评分标准**: Overall Assessment 5分制 (5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit)\n\n## 你的审查侧重\n\n### 1. 方法严谨性\n- **Proposition 1** (Symbolic Confirmation Bias is Structural) 的证明是否严格？假设 A1/A2 是否合理？是否存在逻辑漏洞？\n- **Degeneration condition** (Eq. 4) 的推导是否正确？\n- **Bias Ratio** (Eq. 5) 的定义和使用是否合理？BR > 1 是否真的意味着 confirmation bias？\n- **K_eff** (Eq. 1) 从 ensemble theory 的借用是否恰当？Fleiss' κ → effective sample size 的近似是否有理论支撑？\n- **Scoring function** (Eq. 3) 中 α=0.5 的选择是否有理论或实验依据？敏感性分析是否充分？\n- MAX-SAT 形式化（Algorithm 1-2）是否正确？source-trace attribution scoring 是否有 bias？\n\n### 2. 实验设计\n- 6 个模型 × 3 个 domain 的覆盖是否足够支撑 claims？\n- **样本量**: n=204 (FOLIO), n=600 (ProofWriter), n=200 (LogiQA/StrategyQA), n=30/22 (GSM8K/AIME) 是否充足？\n- **统计检验**: McNemar exact test + BH correction 是否恰当？Bootstrap CI 方法是否正确？\n- **Power analysis** (Appendix D): MDE 和 observed power 是否支持结论？作者承认 observed power < 21%——这对 \"no evidence\" 的 claim 意味着什么？\n- **Multi-seed replication**: 仅 Mistral-7B (3 seeds) 和 Qwen2.5-14B (4 seeds)，是否足够？\n- **Oracle 实验** (Appendix G): gold annotation 替换是否控制了混淆变量？\n- **27 remediation strategies** 的选择是否覆盖了合理的设计空间？是否遗漏了明显的策略？\n- **Cross-architecture escape** (§6): DeBERTa-large 作为 verifier 的实验设计是否合理？仅在 Mistral-7B (SC=39.33%) 上显著——这是否限制了 claim 的 generalizability？\n\n### 3. 统计分析\n- Table 1 中 BH correction 后无条件显著——这是一个 null result paper，统计解读是否恰当？\n- \"absence of evidence is not evidence of absence\" 的讨论是否充分？\n- BR 估计在小 n_err 条件下是否可靠？Table 2 中 n_err 范围 12-90，CI 是否报告？\n- TOST equivalence test (Lakens, 2017) 用 ±2pp margin——这个 margin 的选择是否有依据？\n- Appendix D 中 power analysis 方法是否正确？\n\n请给出完整审稿意见，格式如下：\n\n```\n## Summary\n(2-3句论文概述)\n\n## Strengths\n(逐条列出)\n\n## Weaknesses\n(逐条列出，按严重程度排序，标注 [Critical] / [Major] / [Minor])\n\n## Questions\n(需要作者澄清的问题)\n\n## Missing References\n(遗漏的重要相关工作)\n\n## Overall Assessment\n(评分 + 置信度 + 理由)\n```"
  }
}
````

</details>

---


### Tool result

_source line 1671 · 2026-05-23T08:05:35.669348+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22303
}
```

</details>

---


### Tool call

_source line 1672 · 2026-05-23T08:05:36.431126+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "text": "你是 Reviewer 2，负责审查 **新颖性 + Related Work 完整性 + 写作质量 + Claims 合理性**。\n\n## 论文信息\n- **标题**: Beyond Self-Consistency: Why Self-Extracted Constraints Fail to Improve LLM Logical Reasoning\n- **文件**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_13/submitted.pdf`\n- **目标 Venue**: EMNLP 2026 ARR (deadline: 2026-05-25)\n\n## Venue 要求\n- **页数限制**: Long paper 正文 8 页，引用不限，Limitations 和 Ethics 不计入页数（但不能包含过多额外内容）\n- **模板**: ACL style template (double-column)\n- **匿名规则**: Double-blind。论文不得包含作者信息，自引须匿名化，补充材料和代码链接须匿名\n- **Limitations**: 必须包含，放在正文中 conclusion 之后，仅讨论局限性，不得包含新实验/图表/分析\n- **评分标准**: Overall Assessment 5分制 (5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit)\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- \"Symbolic Confirmation Bias\" 概念是否真正新颖？与 Huang et al. (2024) 的 self-correction impossibility、Wan et al. (2025) 的 CoT-level confirmation bias、Jhaveri et al. (2026) 的 confirmation bias 有何本质区别？\n- Proposition 1 的 information ceiling argument 是否是已知结果的直接推论（data processing inequality 的标准应用）？\n- 三个 diagnostics (C₀, K_eff, BR) 的实用价值如何？是否足以构成独立贡献？\n- Cross-architecture escape (§6) 是否足够新颖——外部 verifier 改善 LLM 推理是已知路径？\n\n### 2. Related Work 完整性\n- 是否遗漏了重要的相关工作？特别关注：\n  - Training-based self-verification / self-correction 方向（如 DuPO, S²R 等 RL-based 方法）\n  - Constraint satisfaction / formalization 方向（如 Amonkar et al. 2025 \"A Reality Check\"）\n  - Deep Ensembles (Lakshminarayanan et al., 2017) 作为 independence-accuracy trade-off 的理论基础\n  - 其他 2025-2026 的最新相关工作\n- §2 Related Work 的组织和覆盖是否平衡？\n- 引用格式是否符合 ACL/natbib 标准？\n\n### 3. 写作质量\n- Abstract 是否准确反映论文贡献？是否有 overclaiming？\n- 标题 \"Fail to Improve\" 是否 overclaiming（考虑到 statistical power 不足以检测小效应）？\n- §5 \"The Symbolic Mirage\" 的叙事是否清晰？Proposition 1 的呈现方式是否让读者能理解？\n- 8 页正文的信息密度是否过高？哪些部分展开不足？哪些可以压缩？\n- Figure/Table 的质量和编排是否合理？Figure 1 是否清晰传达 pipeline？\n- Limitations section 是否充分覆盖了关键局限？\n\n### 4. Claims 合理性\n- \"No condition shows a significant positive effect after FDR control\" — 这是一个 null result，claim 的措辞是否恰当？\n- \"symbolic confirmation bias ... all bias ratios at least 1.66×\" — 是否有循环论证风险（BR 的定义本身是否 tautological）？\n- \"Twenty-seven training-free remediation strategies fail\" — 是否穷举了所有合理策略？claim 的 scope 是否匹配？\n- §6 \"Escaping the Bottleneck\" 中 capability-gap principle 基于 n=6 条件——是否支撑 \"principle\" 级别的 claim？\n- \"Three zero-cost diagnostics correctly classify all 60 tested conditions\" — 在训练集上 100% 准确是否 overfitting？holdout 验证（LLaMA-3.1-8B）是否充分？\n- \"extending the self-correction impossibility of Huang et al. (2024) to formal verification\" — 这个 claim 是否 overselling？\n\n请给出完整审稿意见，格式如下：\n\n```\n## Summary\n(2-3句论文概述)\n\n## Strengths\n(逐条列出)\n\n## Weaknesses\n(逐条列出，按严重程度排序，标注 [Critical] / [Major] / [Minor])\n\n## Questions\n(需要作者澄清的问题)\n\n## Missing References\n(遗漏的重要相关工作)\n\n## Overall Assessment\n(评分 + 置信度 + 理由)\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "symb_invariant_consensus",
    "text": "你是 Reviewer 2，负责审查 **新颖性 + Related Work 完整性 + 写作质量 + Claims 合理性**。\n\n## 论文信息\n- **标题**: Beyond Self-Consistency: Why Self-Extracted Constraints Fail to Improve LLM Logical Reasoning\n- **文件**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_13/submitted.pdf`\n- **目标 Venue**: EMNLP 2026 ARR (deadline: 2026-05-25)\n\n## Venue 要求\n- **页数限制**: Long paper 正文 8 页，引用不限，Limitations 和 Ethics 不计入页数（但不能包含过多额外内容）\n- **模板**: ACL style template (double-column)\n- **匿名规则**: Double-blind。论文不得包含作者信息，自引须匿名化，补充材料和代码链接须匿名\n- **Limitations**: 必须包含，放在正文中 conclusion 之后，仅讨论局限性，不得包含新实验/图表/分析\n- **评分标准**: Overall Assessment 5分制 (5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit)\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- \"Symbolic Confirmation Bias\" 概念是否真正新颖？与 Huang et al. (2024) 的 self-correction impossibility、Wan et al. (2025) 的 CoT-level confirmation bias、Jhaveri et al. (2026) 的 confirmation bias 有何本质区别？\n- Proposition 1 的 information ceiling argument 是否是已知结果的直接推论（data processing inequality 的标准应用）？\n- 三个 diagnostics (C₀, K_eff, BR) 的实用价值如何？是否足以构成独立贡献？\n- Cross-architecture escape (§6) 是否足够新颖——外部 verifier 改善 LLM 推理是已知路径？\n\n### 2. Related Work 完整性\n- 是否遗漏了重要的相关工作？特别关注：\n  - Training-based self-verification / self-correction 方向（如 DuPO, S²R 等 RL-based 方法）\n  - Constraint satisfaction / formalization 方向（如 Amonkar et al. 2025 \"A Reality Check\"）\n  - Deep Ensembles (Lakshminarayanan et al., 2017) 作为 independence-accuracy trade-off 的理论基础\n  - 其他 2025-2026 的最新相关工作\n- §2 Related Work 的组织和覆盖是否平衡？\n- 引用格式是否符合 ACL/natbib 标准？\n\n### 3. 写作质量\n- Abstract 是否准确反映论文贡献？是否有 overclaiming？\n- 标题 \"Fail to Improve\" 是否 overclaiming（考虑到 statistical power 不足以检测小效应）？\n- §5 \"The Symbolic Mirage\" 的叙事是否清晰？Proposition 1 的呈现方式是否让读者能理解？\n- 8 页正文的信息密度是否过高？哪些部分展开不足？哪些可以压缩？\n- Figure/Table 的质量和编排是否合理？Figure 1 是否清晰传达 pipeline？\n- Limitations section 是否充分覆盖了关键局限？\n\n### 4. Claims 合理性\n- \"No condition shows a significant positive effect after FDR control\" — 这是一个 null result，claim 的措辞是否恰当？\n- \"symbolic confirmation bias ... all bias ratios at least 1.66×\" — 是否有循环论证风险（BR 的定义本身是否 tautological）？\n- \"Twenty-seven training-free remediation strategies fail\" — 是否穷举了所有合理策略？claim 的 scope 是否匹配？\n- §6 \"Escaping the Bottleneck\" 中 capability-gap principle 基于 n=6 条件——是否支撑 \"principle\" 级别的 claim？\n- \"Three zero-cost diagnostics correctly classify all 60 tested conditions\" — 在训练集上 100% 准确是否 overfitting？holdout 验证（LLaMA-3.1-8B）是否充分？\n- \"extending the self-correction impossibility of Huang et al. (2024) to formal verification\" — 这个 claim 是否 overselling？\n\n请给出完整审稿意见，格式如下：\n\n```\n## Summary\n(2-3句论文概述)\n\n## Strengths\n(逐条列出)\n\n## Weaknesses\n(逐条列出，按严重程度排序，标注 [Critical] / [Major] / [Minor])\n\n## Questions\n(需要作者澄清的问题)\n\n## Missing References\n(遗漏的重要相关工作)\n\n## Overall Assessment\n(评分 + 置信度 + 理由)\n```"
  }
}
````

</details>

---


### Tool result

_source line 1673 · 2026-05-23T08:05:38.061080+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1629
}
```

</details>

---


### Assistant

_source line 1674 · 2026-05-23T08:05:51.835843+00:00_

**Round 13 审稿启动状态汇报**（Group C）：

| 项目 | 状态 |
|------|------|
| 论文确认 | ✅ 26 页 PDF（8 页正文 + 引用 + 15 页附录），ACL double-blind 格式 |
| Venue 验证 | ✅ EMNLP 2026 ARR，deadline 2026-05-25，未过期 |
| 格式检查 | ✅ `\usepackage[review]{acl}`，匿名 "Anonymous ACL submission" |
| Limitations | ✅ 正文末尾有 Limitations section |
| 视觉审查 | 🔄 已派发，与 Reviewer 并行执行 |
| 外部审稿 | ❌ 未配置 |
| Reviewer 1 | 🔄 方法严谨性 + 实验设计 + 统计分析 |
| Reviewer 2 | 🔄 新颖性 + Related Work + 写作质量 + Claims 合理性 |

等待两位 Reviewer 提交初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 114

## Round 114

4 recorded events


### User

_source line 1675 · 2026-05-23T08:12:48.589030+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见 — Round 1（方法严谨性 + 实验设计 + 统计分析）

**论文**: Beyond Self-Consistency: Why Self-Extracted Constraints Fail to Improve LLM Logical Reasoning
**Venue**: EMNLP 2026 ARR

---

## Summary

本文提出 Symbolic Invariant Consensus Aggregation (SICA)，从 LLM 的 chain-of-thought traces 中提取一阶逻辑约束，通过 weighted partial MAX-SAT 聚合选择答案。尽管 Z3 验证了 99% 的约束有效，SICA 在 6 个模型、3 个推理领域上与 majority voting (SC) 的表现几乎完全一致（94.4% 问题答案相同）。论文将此归因于"symbolic confirmation bias"——自提取约束在结构上与模型的多数答案对齐——并通过 Proposition 1 提供理论证明，27 种补救策略的实验验证，以及 cross-architecture verification 的初步逃逸路径。

---

## Strengths

**S1. 系统性和实验覆盖面出色。** 6 个模型×3+ 个领域×27 种补救策略的实验矩阵，附录中还有大量 ablation (K sensitivity, temperature, multi-seed, oracle, error taxonomy)，远超同类工作的实验深度。这种彻底性对于 negative result paper 至关重要。

**S2. Oracle 实验 (Appendix G) 是关键控制实验。** 用 gold FOL annotations 替换自提取约束后，FOLIO 上 SICA 获得 +20.13 / +13.72pp 的显著提升（Mistral-7B/Qwen2.5-14B），精确定位了瓶颈在提取质量而非聚合机制。这个实验设计巧妙，将方法论有效性与提取质量分离。

**S3. 诊断框架 (BR, K_eff, C_q, ProcessSim) 实用性强。** 三个 zero-cost diagnostics 能在 K=12 pilot run 后预测 SICA 是否有帮助，为实践者提供了部署前筛选工具。Table 5 的 per-condition diagnostics 和决策边界 (C_q < 5%, K_eff ≤ 1.30, BR > 1 with SC regime) 具体可操作。

**S4. 统计方法论透明诚实。** 明确报告 observed power < 21%，承认 "absence of evidence is not evidence of absence"，使用 TOST equivalence test 和 bootstrap CI 多角度论证。这种统计诚实性在 NLP 社区中少见且值得肯定。

**S5. Cross-architecture escape (§6) 提供建设性方向。** 不仅报告负面结果，还识别了 capability-gap 条件下 DeBERTa verifier 的显著提升路径 (Mistral-7B 上 +6.67pp, p < 0.001)，使论文不仅是"这不行"而是"什么条件下可能行"。

**S6. Causal DAG (Figure 3) 和信息论框架。** 用 data processing inequality 将 confirmation bias 放入信息论框架中讨论，比纯实验性工作更有深度。

---

## Weaknesses

**W1 [Critical] Proposition 1 的证明范围与声称范围不匹配。**

Proposition 1 声称 "Symbolic Confirmation Bias is Structural"，暗示这是所有自提取方法的固有缺陷。但证明实际由两部分组成：

- Part (i)（voting degeneration）：依赖 source attribution scoring (Eq. 3)，即 e(c, a) = 1 当且仅当 c 来自产生答案 a 的 trace。这是 SICA 的特定设计选择，不是数学必然。如果用逻辑一致性（而非来源归属）对约束打分，Part (i) 不成立。论文在 Remark 中承认了这一点 ("Part (i) relies on source attribution (Eq. 3), the mechanism used by SICA")，但这个限制没有反映在 Proposition 1 的表述中。

- Part (ii)（information ceiling）：I(C; Y) ≤ I(T; Y) 来自 data processing inequality。这在数学上正确，但它只证明约束不能比 traces 包含更多信息——这是一个平凡的结论（因为约束本身就是从 traces 中提取的）。它不能证明约束不能通过重新组织 traces 中的信息来打破相关模式。例如，一个约束提取器可能识别出少数 trace 中的关键逻辑步骤，使其权重超过多数错误 trace——DPI 不排除这种可能性。

**影响**: 论文的核心理论贡献被过度表述。"Structural" 在 Proposition 1 的标题中暗示普遍性，但证明只对 source-attribution scoring 成立。建议将 Proposition 1 重新表述为关于 source-attribution 机制的特定结果，将普遍性 claim 留给实验证据（27 strategies 全部失败）。

**W2 [Critical] 统计功效严重不足，削弱了 negative claim 的可信度。**

Appendix D 报告所有条件的 observed power < 21%，MDE ≥ 1.86pp。这意味着：
- 即使 SICA 真的有 2pp 的效果，该研究有 ~79% 的概率检测不到。
- 论文的核心 claim "no condition shows a significant positive effect" 在很大程度上是因为检验不够灵敏，而不一定是因为效果不存在。

TOST equivalence test 部分弥补了这一问题（Appendix U），但：
- 只有 8/16 条件达到等价性显著，6 条件被归为 underpowered，2 条件为 genuinely different (negative)。
- ±2pp 的等价边界缺乏明确的理论或实践依据（Section U 未解释为何 2pp 是 practical equivalence 的阈值）。在基准准确率 35%~85% 的范围内，2pp 的实际意义差异很大。

**影响**: 论文无法在统计上排除 SICA 存在小但有意义的效果（如 1-2pp）。建议：(a) 明确讨论 ±2pp margin 的选择依据；(b) 补充 sensitivity analysis 展示不同 margin (±1pp, ±3pp, ±5pp) 下 TOST 结论的变化；(c) 在 claim 表述中更加审慎（如 "no evidence of practically significant improvement" 而非 "fail to improve"）。

**W3 [Major] Multi-seed replication 不充分。**

仅在 Mistral-7B (3 seeds) 和 Qwen2.5-14B (4 seeds) 上做了 multi-seed replication（Table 33, Appendix X.1）。结果显示 seed-level noise 很大：Mistral-7B 上 Δ 从 +2.94 到 -2.45pp, Qwen2.5-14B 上 Δ 从 -0.16 到 +2.70pp。

问题：
- 3-4 seeds 不足以可靠估计 seed variance。以 Mistral-7B 为例，3 个 seed 的 SD 约 2.7pp，但 3 个样本的 SD 估计本身有很大不确定性。
- Table 1 的主结果仅基于 single seed（除上述两个模型），其结论可能被 seed noise 淹没。
- 特别是 Table 1 中 Δ ≈ ±1-2pp 的条件（如 LLaMA-3.1-8B LogiQA Δ = +2.00, p = 0.424），其 Δ 完全在 seed noise 范围内。

**建议**: 至少在 3 个代表性条件（high/mid/low SC）上各补充 5 seeds replication，或在 Limitations 中明确讨论 single-seed 结论的局限性。

**W4 [Major] 小样本条件下 BR 估计不可靠。**

Table 2 报告了 9 个模型-数据集条件的 BR 值，但 n_err（模型错误数量）范围为 12-90。在 n_err = 12 的条件下（如 Qwen2.5-14B on FOLIO），BR 的 point estimate 波动可能很大。

- Table 7 仅报告了 3 个条件的 bootstrap CI（FOLIO n=804, ProofWriter n=200），且 CI 包含 0 的条件并未单独讨论。
- Table 2 的 9 个条件中，多数没有报告 CI 或标准误。
- BR 的定义（Eq. 5）是一个比率，小分母条件下极其不稳定。

**建议**: 为 Table 2 所有条件补充 95% bootstrap CI，并讨论 n_err < 20 条件下结论的可靠性。

**W5 [Major] GSM8K (n=30) 和 AIME (n=22) 样本量过小。**

这两个数据集的样本量远小于 FOLIO (n=204) 和 ProofWriter (n=600)。n=30 和 n=22 几乎无法检测任何合理大小的效果，也无法可靠估计 BR。论文在 Table 14 中使用这些小样本条件的结果（如 AIME Δ = -1.47pp）作为 "27 strategies all fail" claim 的一部分证据。

**影响**: 这些条件的结果不应与大样本条件等权重引用。建议在正文中明确区分"有统计功效的条件"和"样本量不足的探索性条件"。

**W6 [Major] α = 0.5 缺乏理论依据和 sensitivity analysis。**

Scoring function (Eq. 3) 中 α = 0.5 控制 conflicting constraints 的惩罚权重。论文未解释选择 α = 0.5 的理由。虽然在完全退化条件下（99% constraints 支持源答案）α 的选择影响不大，但在非退化边界条件下（如 cross-architecture escape experiments），α 可能影响 SICA 的 aggregation 行为。Appendix L 分析了 K 和 temperature 的敏感性，但没有 α 的 sensitivity analysis。

**建议**: 补充 α ∈ {0, 0.25, 0.5, 0.75, 1.0} 的 sensitivity analysis，至少在 FOLIO + Mistral-7B 上。

**W7 [Minor] K_eff (Eq. 1) 的 exchangeable correlation 假设可能被违反。**

K_eff = K / [1 + (K-1)·κ] 假设所有 trace pairs 之间的相关性相同（exchangeability）。LLM 的 temperature sampling 可能产生更复杂的相关结构——某些 trace 可能共享特定推理路径而其他 trace 完全不同。Table 19-20 中 Fleiss' κ 值在 0.21-0.82 之间变化较大，暗示相关结构可能不均匀。

**影响**: K_eff 主要用于 motivational context（§3.1），不直接影响核心结论，因此这是 minor issue。但如果作者希望将 K_eff 作为诊断工具推广（§5.3），应讨论这一假设的局限性。

**W8 [Minor] Cross-architecture escape (§6) 的 generalizability 受限。**

Table 3 显示 DeBERTa-large 作为 verifier 仅在 Mistral-7B (SC = 39.33%) 上产生显著 SICA 提升，Qwen2.5-14B 和 Qwen2.5-7B 上不显著。§6 的 claim "cross-architecture verification can break the bottleneck" 基于一个显著条件，generalizability 有限。

论文将此框定为 "preliminary evidence"（合理），但 Section 6 标题 "Escaping the Bottleneck" 的语气比实际证据更强。

**W9 [Minor] "First-order logic" 的描述有轻微 overselling。**

论文称提取 "first-order logic constraints"，但 Section 3.1 承认 99% 的约束是 propositional level at Z3（only 1.06% use true quantifiers）。实际操作中 SICA 主要处理命题逻辑，称 "first-order" 可能误导读者对系统能力的期望。

---

## Questions

**Q1.** Proposition 1 Part (i) 依赖 source attribution scoring。如果使用 source-agnostic scoring（如基于 Z3 satisfiability checking 来评估约束与候选答案的逻辑一致性，而非基于约束来源），是否仍会退化？作者是否测试过 source-agnostic alternatives？

**Q2.** TOST 的 ±2pp equivalence margin 如何选择？是否有基于 practical significance 的先验理由，还是 post-hoc 选择？如果 margin 放宽至 ±3pp 或 ±5pp，有多少额外条件达到等价显著？

**Q3.** Table 2 中 BR 值在 n_err = 12 条件下的 95% CI 是多少？论文是否考虑过 BR 的有限样本校正？

**Q4.** Oracle 实验 (Appendix G) 仅在 FOLIO 上测试（因为只有 FOLIO 有 gold FOL annotations）。作者是否考虑过在 ProofWriter 上用其 DSL gold labels 做类似控制实验？这会提供 cross-dataset 的 oracle baseline。

**Q5.** 27 种 remediation strategies (Table 14) 全部在 Mistral-7B (FOLIO n=204) 上测试。是否在其他模型上验证过至少 top-performing strategies？单模型结果可能受模型特性影响。

**Q6.** Appendix X.1 的 multi-seed 结果显示 seed noise ~2-3pp。对于 Table 1 中 |Δ| < 3pp 的所有条件，作者是否承认这些差异可能完全由 seed variance 解释？

---

## Missing References

1. **Self-verification 的 training-based approaches**: 论文主要讨论 training-free 方法。但 Lightman et al. (2024) "Let's Verify Step by Step" 的 process reward models 和 Uesato et al. (2022) 的 outcome/process reward models 是 verification scaling 的关键基线，应更充分讨论与本文 cross-architecture escape 的关系。（注：Lightman et al. 已在引用列表中出现但在正文中引用不够充分。）

2. **Formal verification for code generation**: AlphaCode (Li et al., 2022) 和 CodeT (Chen et al., 2023) 使用测试用例作为约束过滤 code candidates，是 self-extracted constraint verification 在 code domain 的成功案例。讨论为什么约束在 code 领域有效但在 logical reasoning 领域失败，会加强论文的分析。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计全面且透明，但 Proposition 1 证明范围过窄而声称范围过宽，统计功效不足 (<21% power) 削弱 negative claim |
| Excitement | 3.5/5 | 重要的 negative result，诊断框架有实用价值，但对社区的直接影响有限（主要是"不要这样做"的信号） |
| Reproducibility | 4/5 | Appendix A-B 提供了完整的 prompt templates 和 MAX-SAT pseudocode，K/T 参数明确，但代码和数据未提供（double-blind 可理解） |
| Reviewer Confidence | 4/5 | 熟悉 LLM reasoning、self-consistency、formal verification 和统计方法论，仔细阅读了全部 26 页 |

---

## Overall Assessment

**Overall: 3.5 — Borderline Conference**

**一句话总结**: 实验工作全面诚实，诊断框架实用，但核心理论贡献 (Proposition 1) 证明与声称的范围不匹配，且 21% 的统计功效使 negative result 的结论力度不足。

**详细理由**:

这是一篇在实验执行层面非常扎实的 negative result paper。27 种 remediation strategies 的系统测试、oracle 控制实验、多维度诊断框架、以及对统计局限性的诚实讨论，都是高水平的实验工作。Cross-architecture escape 的发现为社区提供了建设性方向。

但两个核心问题限制了论文的影响力：(1) Proposition 1 作为论文的理论支柱，其证明 Part (i) 仅对 source-attribution scoring 成立，而非 section title 所暗示的对所有自提取方法的普遍结论，这使理论贡献被过度表述；(2) 21% 的统计功效意味着研究对 2pp 量级的效果几乎没有检测能力，而 TOST 的 ±2pp margin 缺乏先验依据，8/16 条件 underpowered——这使 "fail to improve" 的表述强于实际证据支持的结论。

如果作者能 (a) 将 Proposition 1 重新限定为关于 source-attribution 机制的结果而非普遍性 claim，(b) 补充 ±2pp margin 的选择依据和 sensitivity analysis，(c) 增加 multi-seed replication 或在正文中更明确讨论其局限，论文将更适合 Conference 接收。在当前状态下，实验贡献达到 Findings 水平，但理论 overclaim 需要修正。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Proposition 1 scope mismatch
- 具体位置：Section 5.1, page 6, Proposition 1 及其证明
- 问题：证明 Part (i) 仅对 SICA 的 source-attribution scoring (Eq. 3) 成立，但 Proposition title "Symbolic Confirmation Bias is Structural" 暗示普遍性
- 为什么影响接收：这是论文的核心理论贡献；如果仅对一种特定评分机制成立，则 "structural" claim 需要 qualification
- 建议修改方向：将 Proposition 1 分为两个结果：(a) source-attribution 下的退化定理（精确结果），(b) information ceiling 的 DPI bound（普遍但弱结果）；在正文中明确区分两者的适用范围

**N2** [critical] 统计功效不足与 claim 强度不匹配
- 具体位置：Abstract ("No condition shows a significant positive effect"), Section 4 title ("Results"), Appendix D (power analysis)
- 问题：observed power < 21% + TOST 仅 8/16 条件显著 + ±2pp margin 无先验依据
- 为什么影响接收：Negative result paper 的 claim credibility 取决于排除 false negative 的能力；当前证据无法排除 1-2pp 量级的真实效果
- 建议修改方向：(a) 正文中软化 claim 表述，(b) 补充 TOST margin sensitivity，(c) 在 Limitations 中更显著地讨论 power limitation

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Multi-seed replication 仅覆盖 2/6 模型
- 具体位置：Appendix X.1, Table 33
- 问题：3-4 seeds 的 SD 估计不可靠，Table 1 大部分条件为 single-seed
- 建议：至少在 Limitations 中明确声明，或补充 1-2 个模型的 multi-seed 数据

**W2** [warning] BR 在小 n_err 条件下缺乏 CI 报告
- 具体位置：Table 2, Section 5.1
- 问题：n_err = 12-90，多数条件未报告 CI
- 建议：补充 Table 2 所有条件的 bootstrap CI

**W3** [warning] α = 0.5 缺乏 sensitivity analysis
- 具体位置：Eq. 3, Section 3.1
- 建议：至少在 appendix 中补充 α ∈ {0, 0.25, 0.5, 0.75, 1.0} 的对比

## 小问题（不影响接收）
- "First-order logic" 描述略有 overselling（99% constraints are propositional）
- K_eff exchangeability 假设应在讨论诊断工具时注明
- Section 6 标题 "Escaping the Bottleneck" 语气过强（仅 1 个模型条件显著）

## 主要优势
- 实验覆盖面和系统性达到顶会标准
- Oracle 控制实验设计巧妙，精确分离方法论 vs 提取质量
- 统计方法论多层次（McNemar + BH + TOST + bootstrap + power analysis），且诚实报告局限
- 诊断框架 (BR, K_eff, C_q) 对实践者有直接价值
- Cross-architecture escape 提供建设性 positive finding

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1676 · 2026-05-23T08:13:03.907786+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "symb_invariant_consensus",
  "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
  }
}
```

</details>

---


### Tool result

_source line 1677 · 2026-05-23T08:13:08.128509+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 4220
}
```

</details>

---


### Assistant

_source line 1678 · 2026-05-23T08:13:16.022755+00:00_

视觉审查已派发。当前状态：

| 角色 | 状态 |
|------|------|
| Reviewer 1 | ✅ 初审完成（3.5 Borderline Conference） |
| Reviewer 2 | 🔄 等待中 |
| 视觉审查 | 🔄 已启动，并行执行 |

Reviewer 1 的主要发现：
- **N1 [Critical]**: Proposition 1 证明范围（仅 source-attribution）与声称范围（structural）不匹配
- **N2 [Critical]**: 统计功效 <21%，negative claim 的可信度不足
- **W1-W3 [Warning]**: Multi-seed 不充分、BR 缺 CI、α=0.5 缺 sensitivity analysis

等待 Reviewer 2 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 115

## Round 115

6 recorded events


### User

_source line 1679 · 2026-05-23T08:13:17.098256+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心评估：**Overall 3.5 (Borderline Conference)**。

两个 critical 问题：
1. **Proposition 1 证明范围与声称范围不匹配** — Part (i) 仅对 source-attribution scoring 成立，但标题 claim "structural" 暗示普遍性
2. **统计功效 < 21% 与 negative claim 强度不匹配** — 无法排除 1-2pp 量级的真实效果，TOST 仅 8/16 条件显著且 ±2pp margin 缺乏依据

实验工作本身扎实（27 strategies、oracle 控制、诊断框架），修正理论 overclaim 和补充统计 sensitivity 后可达 Conference 水平。

---

[Reviewer 2 审稿意见]:

# Reviewer 2 — Round 1 审稿意见

**论文**: Beyond Self-Consistency: Why Self-Extracted Constraints Fail to Improve LLM Logical Reasoning
**审查侧重**: 新颖性 + Related Work 完整性 + 写作质量 + Claims 合理性

---

## Summary

本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM 推理 trace 中提取一阶逻辑约束，经去重后用 weighted partial MAX-SAT 选择答案。核心发现是 null result：尽管 Z3 验证 99% 的自提取约束有效，SICA 在 6 个模型（7B–32B）、3 个推理数据集上的结果与多数投票几乎一致（94.4% 相同），FDR 校正后无显著正效应。论文提出"Symbolic Confirmation Bias"概念（自提取约束系统性偏向模型多数答案，BR ≥ 1.66×），通过 Proposition 1（基于 data processing inequality）给出信息上限论证，测试 27 种 training-free 修复策略均失败，并探索 cross-architecture NLI 验证作为突破路径。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0/5 | 实验方法论总体扎实，但 BR 指标存在循环论证风险（见 N2），diagnostics 的 100% 准确率在训练集上评估有 overfitting 嫌疑（见 N3），capability-gap principle 仅基于 n=6 条件 |
| Excitement | 2.5/5 | 有用的 negative result，但核心洞察是 Huang et al. (2024) 的自然延伸；"even formal methods can't help" 的叙事有价值但新颖性有限 |
| Reproducibility | 4.0/5 | 详尽的附录（18 页），pipeline 描述清晰，prompt 模板完整（Appendix A），统计分析严谨（power analysis, bootstrap CI） |
| Overall Assessment | 3.0/5 | Findings 水平。实验执行出色，但新颖性和 claims 合理性的问题将其限制在 Findings 档位 |

**Confidence**: 4/5 — 我对 LLM 推理、形式化方法和 self-correction 文献较为熟悉

---

## Strengths

**S1. 系统性的实验设计和统计严谨性。** 论文覆盖 9 个模型 × 3 个数据集 × 多种配置，共 60 个条件。统计方法包括 McNemar 检验 + BH FDR 校正、bootstrap 95% CI（Table 7）、power analysis（Appendix D，Table 6），远超同类工作的统计严谨度。特别值得肯定的是 power analysis 明确报告了各条件的 minimum detectable effect（MDE），使 null result 的解读有据可依。

**S2. 有价值的 negative result 和清晰的机制解释。** 对"形式化自然能改善推理"这一直觉的系统否定具有实际意义，可以帮助社区避免无效探索。Proposition 1 虽然技术上简单，但将直觉论证形式化为 Markov chain + DPI 论证，有助于理解*为什么*自提取约束必然失败。

**S3. 丰富的附录和可复现性。** 18 页附录包含 prompt 模板（Appendix A）、MAX-SAT 伪代码（Appendix B）、详细的 per-condition 结果（Tables 5, 10, 12, 14）、超参数敏感性分析（Appendix L）、子群分析（Appendix X）等。这种透明度值得赞赏。

**S4. Practical diagnostics 框架有潜在应用价值。** 三个零成本诊断指标（C₀, K_eff, BR）如果泛化性得到验证，可为实践者提供 deployment-stage 的决策工具，避免昂贵的全量评估。

**S5. Cross-architecture escape 方向的初步探索。** §6 提供了 capability-gap principle 的初步证据（Figure 8），将 negative result 论文转化为有建设性的研究方向指引。

---

## Weaknesses

### Must-Fix 问题（影响接收决定）

**N1 [Critical] 新颖性有限——核心洞察是已知结果的自然延伸**

- **具体位置**: §1 贡献声明, §5 "The Symbolic Mirage", Proposition 1
- **问题**: 
  - Huang et al. (2024) 已经建立了 "LLMs cannot self-correct reasoning without external feedback" 的核心结论。本文的 Symbolic Confirmation Bias 本质上是将这一结论从"自然语言自我纠正"延伸到"形式化约束自我验证"——这是一个有意义但可预见的延伸，而非范式级别的新发现。
  - Wan et al. (2025, ACL Findings) 已经从认知心理学角度证明 CoT 推理中存在 confirmation bias，且模型内部信念（prior beliefs）既影响推理生成也影响答案预测。本文的 SCB 虽然在*形式化*维度上是新的，但底层机制（model beliefs dominate downstream processing）与 Wan et al. 高度重叠。
  - Proposition 1 的信息上限论证是 data processing inequality (DPI) 的直接应用：model → traces → constraints 构成 Markov chain，因此 I(constraints; ground truth) ≤ I(traces; ground truth)。这是信息论教科书级别的推论，将其包装为论文的核心理论贡献有 overclaiming 之嫌。论文自身在 proof 中也承认 "forms a Markov chain and the data processing inequality and DPI apply within each stratum"。
  - Jhaveri et al. (2026) 从 hypothesis testing 角度展示 LLMs 倾向于 confirm 而非 falsify——尽管任务不同，但都指向 "LLM 的验证行为被 prior belief 主导" 这一共同结论。
- **为什么影响接收**: EMNLP/ARR 对 novelty 有明确要求（Excitement 维度）。当多个并行工作已经从不同角度建立了类似结论时，增量贡献需要更强的差异化论证。
- **建议修改方向**: (1) 更诚实地定位贡献——不是"发现"了 symbolic confirmation bias，而是"系统性量化"了形式化路径下的 confirmation bias 现象；(2) 加强与 Wan et al. (2025) 和 Jhaveri et al. (2026) 的细粒度区分，明确说明"形式化维度"带来的具体新洞察是什么；(3) 弱化 Proposition 1 的呈现，承认其是 DPI 的标准应用，核心贡献在于*识别了正确的 Markov chain 结构*而非 DPI 本身。

**N2 [Critical] Bias Ratio (BR) 的循环论证风险未充分排除**

- **具体位置**: §3.1 BR 定义（Eq. 5 附近）, §5.1, Table 2
- **问题**: 
  - BR = P(c supports a_M | a_M ≠ a*) / P(c supports a' | a_M ≠ a*) 衡量在模型答错的问题上，约束是否偏向支持错误的多数答案。
  - 但约束是从*产生这些答案的推理 trace* 中提取的。如果 60% 的 trace 产生答案 A，那么从这些 trace 提取的约束自然更多地支持 A——这是一种 *base-rate* 效应，而非独立的"confirmation bias"证据。
  - 论文需要建立一个 **null model**：如果约束提取是"无偏"的（即约束的 support 比例精确反映 trace 投票分布），BR 的期望值是多少？只有当观测到的 BR 显著*超过*这个 null expectation 时，才能声称存在"额外的" confirmation bias。
  - 论文在 §5.1 提到 "the degeneration condition (Eq. 4), which holds on 94.4% of problems (Table 10), these conclusions extend to..." 但这恰恰是问题所在：如果约束几乎总是退化为多数投票，那么 BR > 1 可能只是退化的*结果*而非独立的 bias 证据。
  - Appendix O 的 cross-model confirmation bias analysis（Table 16）提供了一些相关数据，但没有与 null model 对比。
- **为什么影响接收**: BR 是论文三个核心诊断指标之一，也是"symbolic confirmation bias"概念的量化基础。如果 BR > 1 部分由 base-rate 效应解释，则 SCB 的概念本身需要重新界定。
- **建议修改方向**: (1) 构建 permutation-based null distribution：对每个问题，随机打乱约束-trace 归属关系，计算 null BR 分布，与观测 BR 做统计检验；(2) 或者将 BR 重新定义为 *excess* bias ratio（观测 BR / 期望 BR），使其度量的是超出 base-rate 的额外偏差。

**N3 [Critical] Diagnostics 的 100% 分类准确率是在训练集上评估——overfitting 风险**

- **具体位置**: §5.3, §7 "Three zero-cost diagnostics correctly classify all 60 tested conditions"
- **问题**: 
  - 三个诊断指标的决策边界（C₀ < 5%, K_eff ≤ 1.30, BR > 1）是从同样的 60 个条件上推导的（§5.3: "Decision boundaries were derived from Mistral-7B and Qwen2.5-14B conditions"）。在这些条件上报告 100% 准确率是 in-sample 评估。
  - 所谓的 "holdout" 验证（LLaMA-3.1-8B on FOLIO）只覆盖了**单一模型家族 × 单一数据集**的 1 个条件。这不构成充分的 out-of-distribution 验证。
  - 论文声称 "enabling practitioners to predict a priori whether any trace-aggregation method will help"（§5.3），但这个预测工具的泛化性完全未验证——对不同推理类型（数学推理、常识推理）、不同规模模型（70B+）、不同约束提取方式，诊断是否依然有效？
- **为什么影响接收**: 这个 claim 出现在 abstract、§1 contributions 和 §7 conclusion 中，是论文的三大贡献之一。如果诊断框架的泛化性存疑，这个贡献大幅缩水。
- **建议修改方向**: (1) 至少增加一个完整的 held-out model family（不仅是同一家族的不同大小）；(2) 弱化 claim 为 "correctly classify all tested conditions within our experimental scope"；(3) 讨论诊断在 OOD 场景下可能失败的条件。

---

### Should-Fix 问题（影响评分但不一票否决）

**W1 [Major] 标题 "Fail to Improve" overclaiming——与 statistical power 不匹配**

- **具体位置**: Title, Abstract 第二句 "We show the answer is no"
- **问题**: 
  - Power analysis（Appendix D, Table 6）显示最大条件（Qwen-14B, n≈804）的 MDE 约为 1.86pp，较小条件的 MDE 高达 4.5pp。论文无法排除小于 MDE 的正效应存在。
  - 标题 "Fail to Improve" 是一个无条件的否定声明，但实际论文只能声称 "no detectable improvement above [MDE] after FDR correction"。
  - Bootstrap 95% CI（Table 7）显示所有三个条件的 CI 包含零——这是 "evidence of absence" 还是 "absence of evidence" 的问题。CI 的宽度（约 ±1.5pp）表明论文对小效应的检测力有限。
- **建议**: 标题改为 "Why Self-Extracted Constraints Do Not Substantially Improve..." 或在 abstract 中加入明确的 power caveat。

**W2 [Major] 缺少对 training-based self-verification 方法的讨论**

- **具体位置**: §2 Related Work, §7 Discussion
- **问题**: 
  - 论文的理论论证（Proposition 1）明确针对 **inference-time, same-model** 的自提取约束。但 Related Work 和 Discussion 几乎未讨论 training-based 的自验证方法，如：
    - **S²R** (Zeng et al., ACL 2025): 通过 RL 训练 LLM 学习自验证和自纠正，Qwen2.5-math-7B 从 51.0% 提升到 81.6%
    - **DuPO** (arXiv 2508.14460, 2025): 通过 dual preference optimization 实现 self-verification，数学推理平均提升 6.4 分
  - 这些方法通过训练引入外部奖励信号，*理论上*可以打破 Proposition 1 的信息上限（因为训练过程引入了 ground truth 信号，改变了模型分布）。
  - 论文在 §7 提到 "trained constraint extractors" 作为 future work，但未引用这些已有的成功案例，使得论文看起来像是忽视了一个重要的 existing solution。
  - 此外，Pan et al. (2024, TACL) "When Can LLMs Actually Correct Their Own Mistakes?" 作为 self-correction 方向最全面的 survey，也应被引用和讨论。
- **建议**: 在 §2 增加一小段讨论 training-based self-verification，明确 Proposition 1 的适用边界（inference-time, same-model），并引用 S²R 和 DuPO 作为打破信息上限的已知路径。

**W3 [Major] §6 Capability-gap principle 基于 n=6 条件——不足以支撑 "principle" 级别的 claim**

- **具体位置**: §6 "Escaping the Bottleneck", Table 3, Figure 8
- **问题**: 
  - "Capability-gap principle" 基于 3 个 NLI 架构 × 6 个 generator-verifier 组合。在如此小的 n 上建立 "principle" 级别的 claim 过于激进。
  - Figure 8 的 combo gain vs. capability gap 关系虽然看起来有单调趋势，但数据点太少（仅约 6 个有效点），线性关系不可靠。
  - Table 3 中只有 Mistral-7B（SC below verifier）一个条件显示 significant gain。其余条件要么不显著，要么是负效应。
  - 将这些初步观察称为 "principle" 并在 §7 中作为主要建设性结论，不符合证据强度。
- **建议**: 将 "capability-gap principle" 降级为 "preliminary observation" 或 "hypothesis"，并明确指出需要更大规模验证。

**W4 [Major] "27 strategies fail" 的 scope 与 claim 不匹配**

- **具体位置**: §5.2, Table 14, Abstract "Twenty-seven training-free remediation strategies fail"
- **问题**: 
  - 27 个策略涵盖 9 个 prompt-level 和 3 个 method-level 变体（Table 12, 13），但都局限于同一 pipeline 框架（self-extraction + MAX-SAT aggregation）的变体。这不等于"所有 training-free 方法都失败"。
  - 存在论文未测试的 training-free 方法路径：如 multi-agent debate（Du et al., 2024 已引用但未作为修复策略测试）、iterative prompting with structured feedback、constraint-aware decoding 等。
  - Abstract 中 "Twenty-seven training-free remediation strategies fail" 可能让读者误以为穷举了所有合理的 training-free 方法。
- **建议**: 限定 claim scope 为 "27 training-free variants *within the self-extraction paradigm* fail" 或类似措辞。

**W5 [Minor → Major] "Extending the self-correction impossibility of Huang et al. (2024) to formal verification" 是 overselling**

- **具体位置**: Abstract 末段, §1 contribution 1, §5.1 末段
- **问题**: 
  - Huang et al. (2024) 的核心结论是关于 **self-correction**（模型修改自己的答案），且其理论框架基于 value/policy iteration 的收敛性分析。
  - 本文研究的是 **self-verification**（模型通过形式化约束验证答案），使用的理论工具（DPI）完全不同。
  - 说 "extend" Huang et al. 的不可能性结论，暗示本文的定理是 Huang et al. 定理的推广——但两者的形式化框架、假设条件和证明技术完全不同，不构成逻辑上的 extension。
  - 更准确的表述是 "our findings are consistent with / complement / provide independent evidence for the impossibility results of Huang et al."
- **建议**: 修改措辞，避免 "extend" 这个暗示逻辑推广的动词。

---

### 小问题（不影响接收）

**M1 [Minor]** Figure 1 信息密度过高。Pipeline 图试图在一张图中展示 trace 生成、约束提取、去重、MAX-SAT 求解和 Z3 验证等所有步骤，红色虚线框的 "gold constraint variant" 不易理解。建议拆分为两个子图或简化。

**M2 [Minor]** §3.1 中 "effective sample size" K_eff 的定义（Fleiss' κ reduction）在正文中只有一行公式，没有直觉解释。对不熟悉 ensemble theory 的读者不友好。

**M3 [Minor]** Abstract 信息过载——在有限篇幅内塞入了 pipeline 描述、null result、理论命题、27 策略失败、diagnostics 和 cross-architecture escape 六个要素。建议聚焦 2-3 个核心信息。

**M4 [Minor]** Limitations section（p.8 底部）覆盖了关键局限（propositional/FOL only, open-source models only, English only），但略显仓促（约 5 行）。考虑到论文的 negative result 性质，Limitations 部分应该更充分地讨论这些局限如何影响结论的泛化性。

**M5 [Minor]** §2 Related Work 的组织可以改善——目前按话题分段（self-consistency, self-verification, neuro-symbolic, test-time compute），但各段之间的逻辑衔接不够清晰。建议在段首添加过渡句，构建从 "majority voting → self-correction → formal verification → *this paper fills the gap*" 的叙事线。

---

## Questions（需要作者澄清）

**Q1.** Bias Ratio (BR) 的 null expectation 是什么？如果约束提取是完全"无偏"的（即约束的 support 比例精确反映 trace 投票分布），BR 的期望值是否恰好为 1？还是由于 base-rate 效应，即使无偏提取也会产生 BR > 1？请提供 permutation test 或 null model 分析。

**Q2.** Proposition 1 的 assumption A2（"constraints are trace-determined"）在多大程度上是一个真正的约束？如果约束提取函数 f 是确定性的（给定 trace，约束是固定的），A2 自动成立。在这种情况下，Proposition 1 是否退化为 "确定性后处理不能增加信息" 这个平凡结论？

**Q3.** Table 7 中 LLaMA-3-1-4B 的 bootstrap CI 为 [-1.12, +1.62]，SICA Δ = +0.25pp。作者是否进行了 Bayesian analysis 来评估 positive effect 的后验概率？对于 null result 论文，补充 Bayesian 分析可以提供更 nuanced 的结论。

**Q4.** 论文将 C₀ < 5% 作为 degenerate-regime 指标（SICA reduces to SC when C₀ < 5%）。这个 5% 阈值的 sensitivity 如何？如果用 10% 或 3%，分类结果是否变化？

**Q5.** Cross-architecture NLI 验证（§6）只在 FOLIO 和 ProofWriter 上测试。这两个数据集都是 NLI-friendly 的（premises + conclusion 格式天然适合 NLI）。对于非 NLI 格式的推理任务，cross-architecture verification 是否仍然适用？

---

## Missing References

1. **S²R** (Zeng et al., ACL 2025): "Teaching LLMs to Self-verify and Self-correct via Reinforcement Learning" — 通过 RL 训练 LLM 学习自验证能力，是打破 Proposition 1 信息上限的已有成功案例。
2. **DuPO** (arXiv 2508.14460, 2025): "Enabling Reliable LLM Self-Verification via Dual Preference Optimization" — 另一个 training-based self-verification 方法，在数学推理上有显著提升。
3. **Kamoi et al. (TACL 2024)**: "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs" — self-correction 方向最全面的 survey，本文应引用以定位自身在该方向的位置。
4. **Lakshminarayanan et al. (NeurIPS 2017)**: "Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles" — 虽然论文已引用 Kuncheva & Whitaker (2003) 讨论 ensemble diversity，但 Deep Ensembles 作为 independence-accuracy trade-off 的经典理论基础值得引用。（*Minor*，可选）

---

## Overall Assessment

**Overall: 3.0 — Findings**

**一句话总结**: 一个执行出色但新颖性有限的 negative result 论文——核心发现（自提取形式约束继承模型 bias）是 Huang et al. (2024) 和 Wan et al. (2025) 已知结论的自然延伸，且标题和多处 claims 存在 overclaiming。

**详细理由**:

*支持接收的因素*：实验规模大（9 模型 × 3 数据集 × 60 条件）、统计分析严谨（FDR, power analysis, bootstrap CI）、附录极为详尽（18 页）、negative result 对社区有实际指导价值。如果 claims 适当弱化，这是一篇有价值的 Findings 论文。

*限制接收的因素*：(1) 新颖性：核心洞察可从 Huang et al. (2024) + DPI 直接推导，Proposition 1 是教科书级 DPI 应用；(2) Claims 合理性：标题 overclaiming、BR 循环论证风险、diagnostics overfitting、capability-gap principle 数据不足；(3) Related Work：遗漏 training-based self-verification 的重要相关工作。

*如果以下问题得到解决*，评分可提升至 3.5（Borderline Conference）：弱化标题和 overclaiming、为 BR 提供 null model 分析、增加 diagnostics 的 OOD 验证、补充 training-based 相关工作讨论。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1680 · 2026-05-23T08:14:34.866529+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness/Must-Fix/Should-Fix 点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注以下分歧点：\n1. R2 认为新颖性有限（N1），核心洞察是 Huang et al. (2024) 的自然延伸——你是否同意？\n2. R2 认为 BR 存在循环论证风险（N2），需要 null model——你作为方法评审者如何看待？\n3. R2 认为 diagnostics 100% 准确率是 overfitting（N3）——你是否同意？\n4. R2 给出 3.0 (Findings)，你给出 3.5 (Borderline Conference)——你认为差距主要在哪里？\n\n---\n\n# Reviewer 2 完整审稿意见\n\n## Summary\n\n本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM 推理 trace 中提取一阶逻辑约束，经去重后用 weighted partial MAX-SAT 选择答案。核心发现是 null result：尽管 Z3 验证 99% 的自提取约束有效，SICA 在 6 个模型（7B–32B）、3 个推理数据集上的结果与多数投票几乎一致（94.4% 相同），FDR 校正后无显著正效应。论文提出\"Symbolic Confirmation Bias\"概念（自提取约束系统性偏向模型多数答案，BR ≥ 1.66×），通过 Proposition 1（基于 data processing inequality）给出信息上限论证，测试 27 种 training-free 修复策略均失败，并探索 cross-architecture NLI 验证作为突破路径。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0/5 | 实验方法论总体扎实，但 BR 指标存在循环论证风险（见 N2），diagnostics 的 100% 准确率在训练集上评估有 overfitting 嫌疑（见 N3），capability-gap principle 仅基于 n=6 条件 |\n| Excitement | 2.5/5 | 有用的 negative result，但核心洞察是 Huang et al. (2024) 的自然延伸；\"even formal methods can't help\" 的叙事有价值但新颖性有限 |\n| Reproducibility | 4.0/5 | 详尽的附录（18 页），pipeline 描述清晰，prompt 模板完整（Appendix A），统计分析严谨（power analysis, bootstrap CI） |\n| Overall Assessment | 3.0/5 | Findings 水平。实验执行出色，但新颖性和 claims 合理性的问题将其限制在 Findings 档位 |\n\n## Strengths\n\nS1. 系统性的实验设计和统计严谨性。\nS2. 有价值的 negative result 和清晰的机制解释。\nS3. 丰富的附录和可复现性。\nS4. Practical diagnostics 框架有潜在应用价值。\nS5. Cross-architecture escape 方向的初步探索。\n\n## Weaknesses\n\n### Must-Fix 问题\n\n**N1 [Critical] 新颖性有限——核心洞察是已知结果的自然延伸**\n- Huang et al. (2024) 已建立 \"LLMs cannot self-correct reasoning without external feedback\"。本文的 SCB 本质上是将这一结论从自然语言自我纠正延伸到形式化约束自我验证——可预见的延伸，非范式级新发现。\n- Wan et al. (2025, ACL Findings) 已从认知心理学角度证明 CoT 推理中存在 confirmation bias。本文 SCB 底层机制（model beliefs dominate downstream processing）与 Wan et al. 高度重叠。\n- Proposition 1 的 DPI 论证是信息论教科书级推论，包装为核心理论贡献有 overclaiming 之嫌。\n- Jhaveri et al. (2026) 从 hypothesis testing 角度展示 LLMs 倾向于 confirm 而非 falsify。\n- 建议：定位为\"系统性量化\"而非\"发现\"，弱化 Proposition 1 呈现。\n\n**N2 [Critical] Bias Ratio (BR) 的循环论证风险未充分排除**\n- BR 衡量模型答错时约束是否偏向支持错误多数答案。但约束从产生答案的 trace 中提取，60% trace 产生答案 A → 提取的约束自然更多支持 A，这是 base-rate 效应而非独立 bias 证据。\n- 需要 null model：如果约束提取无偏（support 比例精确反映 trace 投票分布），BR 期望值是多少？只有观测 BR 显著超过 null expectation 才能声称额外 confirmation bias。\n- 建议：构建 permutation-based null distribution 或重定义为 excess bias ratio。\n\n**N3 [Critical] Diagnostics 的 100% 分类准确率是在训练集上评估——overfitting 风险**\n- 三个诊断指标决策边界从同一 60 个条件推导，100% 准确率是 in-sample。\n- \"Holdout\" 验证仅 LLaMA-3.1-8B on FOLIO 1 个条件，不构成充分 OOD 验证。\n- 对不同推理类型、不同规模模型、不同约束提取方式的泛化性完全未验证。\n- 建议：增加完整 held-out model family，弱化 claim scope。\n\n### Should-Fix 问题\n\n**W1 [Major] 标题 \"Fail to Improve\" overclaiming——与 statistical power 不匹配**\n- Power < 21%, MDE ≥ 1.86pp。标题是无条件否定，但论文无法排除小于 MDE 的正效应。\n- 建议改为 \"Why Self-Extracted Constraints Do Not Substantially Improve...\"。\n\n**W2 [Major] 缺少对 training-based self-verification 方法的讨论**\n- 论文几乎未讨论 S²R (Zeng et al., ACL 2025)、DuPO (arXiv 2508.14460, 2025) 等 training-based 方法。\n- 这些方法通过训练引入外部奖励信号，理论上可打破 Proposition 1 的信息上限。\n- 建议：§2 增加 training-based self-verification 段落。\n\n**W3 [Major] §6 Capability-gap principle 基于 n=6 条件——不足以支撑 \"principle\" 级别的 claim**\n- 仅约 6 个有效数据点，线性关系不可靠。Table 3 仅 Mistral-7B 1 个条件 significant。\n- 建议降级为 \"preliminary observation\" 或 \"hypothesis\"。\n\n**W4 [Major] \"27 strategies fail\" 的 scope 与 claim 不匹配**\n- 27 个策略局限于同一 pipeline 框架变体，不等于所有 training-free 方法都失败。\n- 建议限定 scope。\n\n**W5 [Minor → Major] \"Extending the self-correction impossibility of Huang et al. (2024) to formal verification\" 是 overselling**\n- 两者形式化框架、假设条件和证明技术完全不同，不构成逻辑 extension。\n- 建议改为 \"consistent with / complement / provide independent evidence for\"。\n\n### 小问题\n- M1: Figure 1 信息密度过高\n- M2: K_eff 缺乏直觉解释\n- M3: Abstract 信息过载\n- M4: Limitations section 仓促（约 5 行）\n- M5: §2 Related Work 段间逻辑衔接不够清晰\n\n## Questions\nQ1. BR 的 null expectation 是什么？permutation test？\nQ2. Proposition 1 A2 是否退化为平凡结论？\nQ3. 是否进行 Bayesian analysis？\nQ4. C₀ < 5% 阈值 sensitivity？\nQ5. Cross-architecture 对非 NLI 格式任务是否适用？\n\n## Missing References\n1. S²R (Zeng et al., ACL 2025)\n2. DuPO (arXiv 2508.14460, 2025)\n3. Kamoi et al. (TACL 2024) self-correction survey\n4. Lakshminarayanan et al. (NeurIPS 2017) Deep Ensembles"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "symb_invariant_consensus",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Weakness/Must-Fix/Should-Fix 点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注以下分歧点：\n1. R2 认为新颖性有限（N1），核心洞察是 Huang et al. (2024) 的自然延伸——你是否同意？\n2. R2 认为 BR 存在循环论证风险（N2），需要 null model——你作为方法评审者如何看待？\n3. R2 认为 diagnostics 100% 准确率是 overfitting（N3）——你是否同意？\n4. R2 给出 3.0 (Findings)，你给出 3.5 (Borderline Conference)——你认为差距主要在哪里？\n\n---\n\n# Reviewer 2 完整审稿意见\n\n## Summary\n\n本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM 推理 trace 中提取一阶逻辑约束，经去重后用 weighted partial MAX-SAT 选择答案。核心发现是 null result：尽管 Z3 验证 99% 的自提取约束有效，SICA 在 6 个模型（7B–32B）、3 个推理数据集上的结果与多数投票几乎一致（94.4% 相同），FDR 校正后无显著正效应。论文提出\"Symbolic Confirmation Bias\"概念（自提取约束系统性偏向模型多数答案，BR ≥ 1.66×），通过 Proposition 1（基于 data processing inequality）给出信息上限论证，测试 27 种 training-free 修复策略均失败，并探索 cross-architecture NLI 验证作为突破路径。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0/5 | 实验方法论总体扎实，但 BR 指标存在循环论证风险（见 N2），diagnostics 的 100% 准确率在训练集上评估有 overfitting 嫌疑（见 N3），capability-gap principle 仅基于 n=6 条件 |\n| Excitement | 2.5/5 | 有用的 negative result，但核心洞察是 Huang et al. (2024) 的自然延伸；\"even formal methods can't help\" 的叙事有价值但新颖性有限 |\n| Reproducibility | 4.0/5 | 详尽的附录（18 页），pipeline 描述清晰，prompt 模板完整（Appendix A），统计分析严谨（power analysis, bootstrap CI） |\n| Overall Assessment | 3.0/5 | Findings 水平。实验执行出色，但新颖性和 claims 合理性的问题将其限制在 Findings 档位 |\n\n## Strengths\n\nS1. 系统性的实验设计和统计严谨性。\nS2. 有价值的 negative result 和清晰的机制解释。\nS3. 丰富的附录和可复现性。\nS4. Practical diagnostics 框架有潜在应用价值。\nS5. Cross-architecture escape 方向的初步探索。\n\n## Weaknesses\n\n### Must-Fix 问题\n\n**N1 [Critical] 新颖性有限——核心洞察是已知结果的自然延伸**\n- Huang et al. (2024) 已建立 \"LLMs cannot self-correct reasoning without external feedback\"。本文的 SCB 本质上是将这一结论从自然语言自我纠正延伸到形式化约束自我验证——可预见的延伸，非范式级新发现。\n- Wan et al. (2025, ACL Findings) 已从认知心理学角度证明 CoT 推理中存在 confirmation bias。本文 SCB 底层机制（model beliefs dominate downstream processing）与 Wan et al. 高度重叠。\n- Proposition 1 的 DPI 论证是信息论教科书级推论，包装为核心理论贡献有 overclaiming 之嫌。\n- Jhaveri et al. (2026) 从 hypothesis testing 角度展示 LLMs 倾向于 confirm 而非 falsify。\n- 建议：定位为\"系统性量化\"而非\"发现\"，弱化 Proposition 1 呈现。\n\n**N2 [Critical] Bias Ratio (BR) 的循环论证风险未充分排除**\n- BR 衡量模型答错时约束是否偏向支持错误多数答案。但约束从产生答案的 trace 中提取，60% trace 产生答案 A → 提取的约束自然更多支持 A，这是 base-rate 效应而非独立 bias 证据。\n- 需要 null model：如果约束提取无偏（support 比例精确反映 trace 投票分布），BR 期望值是多少？只有观测 BR 显著超过 null expectation 才能声称额外 confirmation bias。\n- 建议：构建 permutation-based null distribution 或重定义为 excess bias ratio。\n\n**N3 [Critical] Diagnostics 的 100% 分类准确率是在训练集上评估——overfitting 风险**\n- 三个诊断指标决策边界从同一 60 个条件推导，100% 准确率是 in-sample。\n- \"Holdout\" 验证仅 LLaMA-3.1-8B on FOLIO 1 个条件，不构成充分 OOD 验证。\n- 对不同推理类型、不同规模模型、不同约束提取方式的泛化性完全未验证。\n- 建议：增加完整 held-out model family，弱化 claim scope。\n\n### Should-Fix 问题\n\n**W1 [Major] 标题 \"Fail to Improve\" overclaiming——与 statistical power 不匹配**\n- Power < 21%, MDE ≥ 1.86pp。标题是无条件否定，但论文无法排除小于 MDE 的正效应。\n- 建议改为 \"Why Self-Extracted Constraints Do Not Substantially Improve...\"。\n\n**W2 [Major] 缺少对 training-based self-verification 方法的讨论**\n- 论文几乎未讨论 S²R (Zeng et al., ACL 2025)、DuPO (arXiv 2508.14460, 2025) 等 training-based 方法。\n- 这些方法通过训练引入外部奖励信号，理论上可打破 Proposition 1 的信息上限。\n- 建议：§2 增加 training-based self-verification 段落。\n\n**W3 [Major] §6 Capability-gap principle 基于 n=6 条件——不足以支撑 \"principle\" 级别的 claim**\n- 仅约 6 个有效数据点，线性关系不可靠。Table 3 仅 Mistral-7B 1 个条件 significant。\n- 建议降级为 \"preliminary observation\" 或 \"hypothesis\"。\n\n**W4 [Major] \"27 strategies fail\" 的 scope 与 claim 不匹配**\n- 27 个策略局限于同一 pipeline 框架变体，不等于所有 training-free 方法都失败。\n- 建议限定 scope。\n\n**W5 [Minor → Major] \"Extending the self-correction impossibility of Huang et al. (2024) to formal verification\" 是 overselling**\n- 两者形式化框架、假设条件和证明技术完全不同，不构成逻辑 extension。\n- 建议改为 \"consistent with / complement / provide independent evidence for\"。\n\n### 小问题\n- M1: Figure 1 信息密度过高\n- M2: K_eff 缺乏直觉解释\n- M3: Abstract 信息过载\n- M4: Limitations section 仓促（约 5 行）\n- M5: §2 Related Work 段间逻辑衔接不够清晰\n\n## Questions\nQ1. BR 的 null expectation 是什么？permutation test？\nQ2. Proposition 1 A2 是否退化为平凡结论？\nQ3. 是否进行 Bayesian analysis？\nQ4. C₀ < 5% 阈值 sensitivity？\nQ5. Cross-architecture 对非 NLI 格式任务是否适用？\n\n## Missing References\n1. S²R (Zeng et al., ACL 2025)\n2. DuPO (arXiv 2508.14460, 2025)\n3. Kamoi et al. (TACL 2024) self-correction survey\n4. Lakshminarayanan et al. (NeurIPS 2017) Deep Ensembles"
  }
}
```

</details>

---


### Tool result

_source line 1681 · 2026-05-23T08:15:13.118867+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 38252
}
```

</details>

---


### Tool call

_source line 1682 · 2026-05-23T08:15:13.671249+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness/Must-Fix/Should-Fix 点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注以下分歧点：\n1. R1 给 Soundness 3.5/5，你给 3.0/5——你是否同意 R1 对实验方法论的更高评价？\n2. R1 认为 Proposition 1 的核心问题是 \"scope mismatch\"（证明范围 vs 声称范围），你认为核心问题是 \"novelty limited\"（DPI 是教科书应用）——哪个更准确？\n3. R1 未提出 BR 循环论证问题——你是否坚持你的 N2？\n4. R1 给出 3.5 (Borderline Conference)，你给出 3.0 (Findings)——差距来源是什么？\n\n---\n\n# Reviewer 1 完整审稿意见\n\n## Summary\n\n本文提出 Symbolic Invariant Consensus Aggregation (SICA)，从 LLM 的 chain-of-thought traces 中提取一阶逻辑约束，通过 weighted partial MAX-SAT 聚合选择答案。尽管 Z3 验证了 99% 的约束有效，SICA 在 6 个模型、3 个推理领域上与 majority voting (SC) 的表现几乎完全一致（94.4% 问题答案相同）。论文将此归因于\"symbolic confirmation bias\"——自提取约束在结构上与模型的多数答案对齐——并通过 Proposition 1 提供理论证明，27 种补救策略的实验验证，以及 cross-architecture verification 的初步逃逸路径。\n\n## Strengths\n\nS1. 系统性和实验覆盖面出色。6 个模型×3+ 个领域×27 种补救策略的实验矩阵，附录中还有大量 ablation。\nS2. Oracle 实验 (Appendix G) 是关键控制实验。用 gold FOL annotations 替换自提取约束后获得显著提升，精确定位瓶颈。\nS3. 诊断框架 (BR, K_eff, C_q, ProcessSim) 实用性强。\nS4. 统计方法论透明诚实。明确报告 observed power < 21%。\nS5. Cross-architecture escape (§6) 提供建设性方向。\nS6. Causal DAG (Figure 3) 和信息论框架。\n\n## Weaknesses\n\n### Must-Fix 问题\n\n**N1 [Critical] Proposition 1 的证明范围与声称范围不匹配**\n- Part (i)（voting degeneration）依赖 source attribution scoring (Eq. 3)，是 SICA 特定设计选择。如果用逻辑一致性而非来源归属打分，Part (i) 不成立。论文在 Remark 中承认但未反映在 Proposition 1 表述中。\n- Part (ii)（information ceiling）来自 DPI。数学正确但只证明约束不能比 traces 包含更多信息——平凡结论。不能证明约束不能通过重新组织信息打破相关模式。\n- 建议：将 Proposition 1 分为两个结果，明确区分 source-attribution 特定结果和 DPI 普遍但弱的结果。\n\n**N2 [Critical] 统计功效严重不足，削弱 negative claim 可信度**\n- Observed power < 21%，MDE ≥ 1.86pp。即使 SICA 真有 2pp 效果，~79% 概率检测不到。\n- TOST 仅 8/16 条件显著，±2pp margin 缺乏理论依据。\n- 建议：(a) 讨论 ±2pp 选择依据；(b) 补充不同 margin sensitivity analysis；(c) 审慎表述 claims。\n\n### Should-Fix 问题\n\n**W1 [warning] Multi-seed replication 仅覆盖 2/6 模型**\n- Mistral-7B (3 seeds), Qwen2.5-14B (4 seeds)。Seed-level noise 约 2-3pp，Table 1 大部分 single-seed。\n\n**W2 [warning] BR 在小 n_err 条件下缺乏 CI 报告**\n- n_err = 12-90，多数条件未报告 CI。\n\n**W3 [warning] α = 0.5 缺乏 sensitivity analysis**\n- 论文未解释选择理由，附录无 α sensitivity。\n\n**W4 [Major] GSM8K (n=30) 和 AIME (n=22) 样本量过小**\n- 不应与大样本条件等权重引用。\n\n**W5 [Major] 小样本条件下 BR 估计不可靠**\n- n_err = 12 时 BR point estimate 波动大，Table 2 多数条件没报 CI。\n\n### 小问题\n- W7: K_eff exchangeable correlation 假设可能被违反\n- W8: Cross-architecture escape generalizability 受限\n- W9: \"First-order logic\" 描述轻微 overselling\n\n## Questions\nQ1. Source-agnostic scoring 是否仍会退化？\nQ2. TOST ±2pp margin 如何选择？\nQ3. Table 2 中 n_err=12 条件的 95% CI？\nQ4. ProofWriter 上用 DSL gold labels 做 oracle 实验？\nQ5. 27 strategies 是否在其他模型上验证？\nQ6. |Δ| < 3pp 条件是否可能完全由 seed variance 解释？\n\n## Missing References\n1. Lightman et al. (2024) process reward models\n2. AlphaCode, CodeT — constraint verification in code domain\n\n## Overall Assessment\n**Overall: 3.5 — Borderline Conference**\n实验扎实，统计诚实，但 Proposition 1 scope mismatch 和 power < 21% 限制了 negative claim 力度。修正后可达 Conference。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "symb_invariant_consensus",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness/Must-Fix/Should-Fix 点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注以下分歧点：\n1. R1 给 Soundness 3.5/5，你给 3.0/5——你是否同意 R1 对实验方法论的更高评价？\n2. R1 认为 Proposition 1 的核心问题是 \"scope mismatch\"（证明范围 vs 声称范围），你认为核心问题是 \"novelty limited\"（DPI 是教科书应用）——哪个更准确？\n3. R1 未提出 BR 循环论证问题——你是否坚持你的 N2？\n4. R1 给出 3.5 (Borderline Conference)，你给出 3.0 (Findings)——差距来源是什么？\n\n---\n\n# Reviewer 1 完整审稿意见\n\n## Summary\n\n本文提出 Symbolic Invariant Consensus Aggregation (SICA)，从 LLM 的 chain-of-thought traces 中提取一阶逻辑约束，通过 weighted partial MAX-SAT 聚合选择答案。尽管 Z3 验证了 99% 的约束有效，SICA 在 6 个模型、3 个推理领域上与 majority voting (SC) 的表现几乎完全一致（94.4% 问题答案相同）。论文将此归因于\"symbolic confirmation bias\"——自提取约束在结构上与模型的多数答案对齐——并通过 Proposition 1 提供理论证明，27 种补救策略的实验验证，以及 cross-architecture verification 的初步逃逸路径。\n\n## Strengths\n\nS1. 系统性和实验覆盖面出色。6 个模型×3+ 个领域×27 种补救策略的实验矩阵，附录中还有大量 ablation。\nS2. Oracle 实验 (Appendix G) 是关键控制实验。用 gold FOL annotations 替换自提取约束后获得显著提升，精确定位瓶颈。\nS3. 诊断框架 (BR, K_eff, C_q, ProcessSim) 实用性强。\nS4. 统计方法论透明诚实。明确报告 observed power < 21%。\nS5. Cross-architecture escape (§6) 提供建设性方向。\nS6. Causal DAG (Figure 3) 和信息论框架。\n\n## Weaknesses\n\n### Must-Fix 问题\n\n**N1 [Critical] Proposition 1 的证明范围与声称范围不匹配**\n- Part (i)（voting degeneration）依赖 source attribution scoring (Eq. 3)，是 SICA 特定设计选择。如果用逻辑一致性而非来源归属打分，Part (i) 不成立。论文在 Remark 中承认但未反映在 Proposition 1 表述中。\n- Part (ii)（information ceiling）来自 DPI。数学正确但只证明约束不能比 traces 包含更多信息——平凡结论。不能证明约束不能通过重新组织信息打破相关模式。\n- 建议：将 Proposition 1 分为两个结果，明确区分 source-attribution 特定结果和 DPI 普遍但弱的结果。\n\n**N2 [Critical] 统计功效严重不足，削弱 negative claim 可信度**\n- Observed power < 21%，MDE ≥ 1.86pp。即使 SICA 真有 2pp 效果，~79% 概率检测不到。\n- TOST 仅 8/16 条件显著，±2pp margin 缺乏理论依据。\n- 建议：(a) 讨论 ±2pp 选择依据；(b) 补充不同 margin sensitivity analysis；(c) 审慎表述 claims。\n\n### Should-Fix 问题\n\n**W1 [warning] Multi-seed replication 仅覆盖 2/6 模型**\n- Mistral-7B (3 seeds), Qwen2.5-14B (4 seeds)。Seed-level noise 约 2-3pp，Table 1 大部分 single-seed。\n\n**W2 [warning] BR 在小 n_err 条件下缺乏 CI 报告**\n- n_err = 12-90，多数条件未报告 CI。\n\n**W3 [warning] α = 0.5 缺乏 sensitivity analysis**\n- 论文未解释选择理由，附录无 α sensitivity。\n\n**W4 [Major] GSM8K (n=30) 和 AIME (n=22) 样本量过小**\n- 不应与大样本条件等权重引用。\n\n**W5 [Major] 小样本条件下 BR 估计不可靠**\n- n_err = 12 时 BR point estimate 波动大，Table 2 多数条件没报 CI。\n\n### 小问题\n- W7: K_eff exchangeable correlation 假设可能被违反\n- W8: Cross-architecture escape generalizability 受限\n- W9: \"First-order logic\" 描述轻微 overselling\n\n## Questions\nQ1. Source-agnostic scoring 是否仍会退化？\nQ2. TOST ±2pp margin 如何选择？\nQ3. Table 2 中 n_err=12 条件的 95% CI？\nQ4. ProofWriter 上用 DSL gold labels 做 oracle 实验？\nQ5. 27 strategies 是否在其他模型上验证？\nQ6. |Δ| < 3pp 条件是否可能完全由 seed variance 解释？\n\n## Missing References\n1. Lightman et al. (2024) process reward models\n2. AlphaCode, CodeT — constraint verification in code domain\n\n## Overall Assessment\n**Overall: 3.5 — Borderline Conference**\n实验扎实，统计诚实，但 Proposition 1 scope mismatch 和 power < 21% 限制了 negative claim 力度。修正后可达 Conference。"
  }
}
```

</details>

---


### Tool result

_source line 1683 · 2026-05-23T08:15:15.086119+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1414
}
```

</details>

---


### Assistant

_source line 1684 · 2026-05-23T08:15:19.397278+00:00_

交叉分享已发送，等待两位 Reviewer 的逐条 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 116

## Round 116

2 recorded events


### User

_source line 1685 · 2026-05-23T08:15:20.906342+00:00_

[Reviewer 2 审稿结果]:
Round 1 审稿意见已完成并提交。

核心判断：**Overall 3.0（Findings 水平）**。论文实验执行出色（60 条件、严谨统计），但三个关键问题限制评分：(1) 新颖性有限——SCB 概念是 Huang et al. (2024) + DPI 的自然延伸；(2) BR 指标存在循环论证风险，缺少 null model 对照；(3) diagnostics 的 100% 准确率在训练集上评估，holdout 验证不充分。标题和多处 claims 存在 overclaiming。如果弱化 claims、补充 null model 分析和 OOD 验证，可提升至 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1686 · 2026-05-23T08:15:26.648126+00:00_

等待两位 Reviewer 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 117

## Round 117

2 recorded events


### User

_source line 1687 · 2026-05-23T08:17:54.794581+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — 交叉回应 Reviewer 1 审稿意见

---

## R1 Must-Fix 逐条回应

**[AGREE] R1-N1: Proposition 1 的证明范围与声称范围不匹配**

同意，且 R1 的 critique 比我自己对 Proposition 1 的批评更精确。R1 正确指出了 Part (i) 的 source attribution scoring (Eq. 3) 是 SICA 的设计选择而非必然——如果用逻辑一致性打分，voting degeneration 不一定成立。这是一个具体、可验证的 scope 问题。

我的 N1 侧重"DPI 是教科书应用，novelty 有限"，R1 侧重"证明了 SICA-specific 的结论却声称了 general 的不可能性"。两者互补：R1 指出 *validity* 问题（scope mismatch），我指出 *significance* 问题（即使 scope 正确，general part 也是 trivial）。论文需要同时回应两个维度。

R1 的修改建议（拆分为两个结果）我也支持。进一步建议：拆分后的 Part (ii) 应明确承认 DPI 的局限——它只证明 I(constraints; truth) ≤ I(traces; truth)，但不排除约束通过*重新组织*信息（而非增加信息）来打破 trace-level 的相关结构。这个 gap 论文未讨论。

**[AGREE] R1-N2: 统计功效严重不足，削弱 negative claim 可信度**

完全同意。这与我的 W1（标题 "Fail to Improve" overclaiming）直接相关。R1 提供了更详细的技术分析：

- Observed power < 21% 意味着即使 SICA 有 2pp 真实效果，~79% 概率无法检测。这直接削弱了 "fail to improve" 的 claim 力度。
- TOST 仅 8/16 条件显著，且 ±2pp margin 缺乏理论依据——这一点我在初审中未充分展开，R1 的补充有价值。
- R1 建议的 sensitivity analysis（不同 margin 下的 TOST 结果）非常合理，可以显著增强论文的说服力。

补充一点：Table 7 的 bootstrap 95% CI 全部包含零，宽度约 ±1.5pp。对于一个以 negative result 为核心卖点的论文，这个 CI 宽度不够窄，无法支撑强否定声明。论文应在 abstract 和 conclusion 中加入 power caveat。

---

## R1 Should-Fix 逐条回应

**[AGREE] R1-W1: Multi-seed replication 仅覆盖 2/6 模型**

同意。Seed-level noise 约 ±2.34pp（Table 33，Appendix X.1），而 Table 1 大部分条件的 |Δ| < 3pp。这意味着许多 single-seed 条件的观测效应可能完全由 seed variance 解释。论文应 (a) 至少对 Table 1 中效应最大的条件补充 multi-seed replication，或 (b) 明确标注 single-seed 结果的不确定性。

**[AGREE] R1-W2: BR 在小 n_err 条件下缺乏 CI 报告**

同意，且这一点*强化*了我的 N2（BR 循环论证）。在 n_err 小至 12 时，BR 的 point estimate 本身就不稳定。如果同时存在 base-rate 效应（我的 N2 关注的问题）+ 高方差（R1 关注的问题），那么 "所有条件 BR ≥ 1.66×" 这个 claim 的可信度受到双重削弱。建议 Table 2 补充 bootstrap CI，并对 n_err < 30 的条件标注 "exploratory"。

**[AGREE] R1-W3: α = 0.5 缺乏 sensitivity analysis**

同意。α = 0.5 控制 Fleiss' κ → K_eff 的映射（§3.1），是诊断框架的关键参数，但论文未给出选择理由。建议增加 α ∈ {0.3, 0.5, 0.7} 的 sensitivity analysis。

**[AGREE] R1-W4: GSM8K (n=30) 和 AIME (n=22) 样本量过小**

同意。这些条件在 Table 5 中以 per-condition diagnostics 的形式出现，但样本量不足以支撑任何统计推断。论文在正文中引用这些条件时（§5.3）应加 caveat 或将其明确归类为 exploratory observations。

**[AGREE] R1-W5: 小样本条件下 BR 估计不可靠**

同意，理由同 W2 回应。

**[AGREE] R1-W7: K_eff exchangeable correlation 假设可能被违反**

同意这是一个有效但 minor 的 concern。K_eff 基于 Fleiss' κ 的 exchangeable correlation 假设（所有 trace 对之间的相关性相同），但实际上 trace 之间的相关结构可能不均匀（如 prompt 相似的 trace 相关性更高）。不过这对论文结论的影响有限。

**[AGREE] R1-W8: Cross-architecture escape generalizability 受限**

同意，且与我的 W3（capability-gap principle 基于 n=6 条件不足以支撑 "principle" claim）一致。R1 补充了 "只在 NLI-friendly 数据集上测试" 的角度，我在 Q5 中也提出了类似问题。

**[AGREE] R1-W9: "First-order logic" 描述轻微 overselling**

同意。论文实际提取的是 propositional/quantifier-free FOL 的子集（Appendix A），完整的一阶逻辑包括量词、函数符号等，远比论文实际处理的复杂。

---

## R1 Questions 回应

**R1-Q1 (Source-agnostic scoring 是否仍会退化？)**: 好问题。这直接触及 Proposition 1 的 scope。如果 source-agnostic scoring（如逻辑一致性评分）也退化，则 Proposition 1 的 scope 比 R1-N1 所指出的更宽；如果不退化，则 R1-N1 的 scope mismatch 批评完全成立。我认为*很可能*仍会退化——因为约束本身继承了 trace 的偏差（我的 N2 的核心论点），但这需要实验验证。

**R1-Q6 (|Δ| < 3pp 条件是否可能完全由 seed variance 解释？)**: 是的，极有可能。Seed-level noise ≈ ±2.34pp（Table 33），Table 1 中绝大多数 |Δ| < 3pp，因此 single-seed 条件的效应可能纯属噪声。这进一步支持 R1-N2 和我的 W1。

---

## R1 Missing References 回应

**[AGREE] Lightman et al. (2024) process reward models**: 确实应该引用。PRM 是 training-based verification 的重要方向，与我在 W2 中提出的 S²R 和 DuPO 一起构成 "training-based 自验证" 的完整图景。论文的 Proposition 1 仅适用于 inference-time 自提取，PRM/S²R/DuPO 通过训练引入外部信号可能打破信息上限——论文应明确讨论这个理论边界。

**[AGREE] AlphaCode, CodeT**: 作为 constraint verification in code domain 的相关工作值得引用，但重要性略低于 PRM/S²R。

---

## 四个分歧点的详细回应

### 分歧 1: Soundness 3.5 (R1) vs 3.0 (R2)

重新审视后，我部分同意 R1 的更高评价。R1 正确地认识到*实验方法论*本身（McNemar + BH FDR, bootstrap CI, power analysis, Oracle control）是出色的。我的 3.0 主要被 BR 循环论证（N2）和 diagnostics overfitting（N3）拉低。

仔细考虑后，我认为：
- **实验设计的 soundness: 4.0/5** — 实验矩阵覆盖面大，统计方法严谨，Oracle 实验是优秀的控制
- **Claims 的 soundness: 2.5/5** — BR 循环论证未排除、diagnostics 在训练集上评估、Proposition 1 scope mismatch、power 不足以支撑标题级 claim
- **综合: 3.0-3.5/5** — 我愿意将 Soundness 修正为 **3.5/5**，承认实验执行本身的高质量，但保留对 claims soundness 的保留意见

### 分歧 2: Proposition 1 — "scope mismatch" (R1) vs "novelty limited" (R2)

**两者都准确，互补而非矛盾。**

- R1 的 "scope mismatch" 是*内部一致性*问题：论文声称了比证明范围更宽的结论。这是一个 validity 问题，指出论文的逻辑跳跃，可以通过重写修复。
- 我的 "novelty limited" 是*外部贡献*问题：即使 scope 修正后，Proposition 1 的 general part (DPI) 在信息论领域是 well-known 的，不构成独立的理论贡献。

如果只能保留一个，**R1 的更适合作为 review feedback**（具体、可操作），但从评估论文整体价值的角度，我的 novelty concern 更根本——修复 scope mismatch 后论文仍面临 "这个结果是否足够 non-trivial" 的问题。

### 分歧 3: BR 循环论证——我坚持 N2

**我坚持 N2，R1 未发现这个问题不意味着它不存在。**

R1 的 W2 和 W5 关注 BR 的*统计可靠性*（小 n_err, 无 CI），我的 N2 关注 BR 的*概念有效性*（是否部分由 base-rate 效应解释）。这是两个独立的问题。

具体论证：假设一个问题有 12 条 trace，8 条产生答案 A（多数答案，但错误），4 条产生答案 B。如果约束提取是"无偏"的（每条 trace 提取的约束仅反映该 trace 的推理内容），那么来自 8 条 A-trace 的约束自然更多支持 A，来自 4 条 B-trace 的约束自然更多支持 B。此时 BR > 1 是 base-rate 的直接结果，而非"额外的 confirmation bias"。

论文需要回答：**观测到的 BR 中有多少是 base-rate 效应，多少是超出 base-rate 的真正 bias？** 这需要 permutation test 或 null model。在此之前，SCB 概念的强度无法确定。

不过，公平地说，即使 BR > 1 完全由 base-rate 解释，这也*支持*论文的核心论点（约束不能提供独立信息）——只是 SCB 概念需要重新界定为 "约束继承 trace 分布" 而非 "约束存在额外偏差"。因此 N2 影响的是 SCB 概念的*措辞和定义*，而非论文的*核心结论*。

### 分歧 4: Overall 3.5 (R1) vs 3.0 (R2)

差距来源：

| 因素 | R1 权重 | R2 权重 | 解释 |
|------|--------|--------|------|
| 实验质量 | 高 | 高 | 两人一致认可实验扎实 |
| Oracle 实验 (App. G) | 重要 | 中等 | R1 将其列为 S2 核心优势；我认可但未特别突出 |
| 新颖性 | 中等关注 | **核心关注** | R1 主要从 scope mismatch 角度看 Prop.1，未深入讨论 vs. Huang/Wan 的增量贡献度；我认为整篇论文的核心洞察是已知结论的自然延伸 |
| BR 循环论证 | 未提及 | **Critical** | 如果 BR > 1 部分由 base-rate 解释，SCB 概念需重新界定 |
| Diagnostics overfitting | 未提及 | **Critical** | 100% 准确率在 in-sample 评估的可信度低 |
| Missing related work | 轻微（2条） | **Major**（4条） | 我认为遗漏 training-based self-verification (S²R, DuPO) 是重要缺失 |

**结论**：在 R1 的审查框架（主要关注方法论 soundness + Prop.1 scope）下，3.5 是合理的。在我的审查框架（更关注 novelty + claims 合理性 + related work 完整性）下，3.0 也是合理的。

**我维持 Overall 3.0 (Findings)**，但承认如果以下条件满足，可提至 3.5：
1. BR 提供 null model 分析（回应我的 N2）
2. Diagnostics 增加 OOD 验证（回应我的 N3）
3. 补充 training-based self-verification 讨论（回应我的 W2）

---

## 修正后的评分

经交叉审议，我调整 Soundness 评分：

| 维度 | 原评分 | 修正后 | 理由 |
|------|--------|--------|------|
| Soundness | 3.0/5 | **3.5/5** | 接受 R1 对实验方法论质量的更高评价，但保留 claims soundness 的保留意见 |
| Excitement | 2.5/5 | 2.5/5 | 不变——新颖性关注 R1 未充分讨论 |
| Reproducibility | 4.0/5 | 4.0/5 | 不变 |
| Overall | 3.0/5 | **3.0/5** | 维持——novelty 和 claims 问题是我的核心关注，R1 的意见未改变这些判断 |
| Confidence | 4/5 | 4/5 | 不变 |


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1688 · 2026-05-23T08:18:02.593146+00:00_

Reviewer 2 交叉回应已收到。等待 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 118

## Round 118

2 recorded events


### User

_source line 1689 · 2026-05-23T08:18:09.319086+00:00_

[Reviewer 2 审稿结果]:
交叉回应要点：

- **R1 所有 Weaknesses 均 [AGREE]**，多数补充了与我自身意见的交叉印证
- **Soundness 上调至 3.5/5**，认可 R1 对实验方法论质量的更高评价
- **坚持 N2（BR 循环论证）**：R1 关注 BR 的统计可靠性，我关注其概念有效性——两个独立问题
- **Proposition 1 的两个 critique 互补**：R1 的 "scope mismatch" 更可操作，我的 "novelty limited" 更根本
- **Overall 维持 3.0 (Findings)**：核心分歧在于我对 novelty 和 claims 合理性给予更高权重

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1690 · 2026-05-23T08:18:18.489999+00:00_

Reviewer 2 交叉回应已收到。等待 Reviewer 1 对 Reviewer 2 意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 119

## Round 119

16 recorded events


### User

_source line 1691 · 2026-05-23T08:18:57.549135+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[REBUT] R2-N1: 新颖性有限——核心洞察是 Huang et al. (2024) 的自然延伸**

R2 的论点有一定道理但低估了本文的非平凡贡献。

Huang et al. (2024) 的结论是 LLMs 在自然语言层面无法 self-correct without external feedback。要从中推导出"即使用 Z3 可验证的形式化约束也无法帮助"，需要一个额外且非显而易见的跳跃：许多研究者（包括 symbolic planning、neuro-symbolic verification 方向的工作，如 §2 引用的 Ryu et al. 2025, Xu et al. 2025, Miya 2025 等）的前提假设恰恰是"形式化能打破自我纠正的障碍"——因为 Z3 提供的是机械式逻辑验证，理论上应能捕获自然语言反馈无法发现的矛盾。

本文的非平凡贡献在于：
1. **机制定位**：不仅发现"不行"，而且精确定位瓶颈在 extraction（而非 verification/aggregation），这通过 oracle 实验 (Appendix G, +20.13pp) 证实。Huang et al. 未涉及这一分离。
2. **诊断框架 (§5.3)**：BR、K_eff、C_q 三个 zero-cost diagnostics 是新工具，Huang et al. 无类似贡献。
3. **27 策略系统否证 (§5.2, Table 14)**：覆盖 9 prompt-level + 3 method-level + additional strategies 系统封闭设计空间，这种穷举式否证在 Huang et al. 中不存在。

但我同意以下限定：
- Proposition 1 的 DPI 部分 (Part ii) 确实接近信息论教科书推论，不应作为核心理论"发现"呈现。这与我 R1-N1 的意见一致。
- 论文 Abstract 中 "extending the self-correction impossibility of Huang et al. (2024) to formal verification" 的措辞确实 overselling（§1, page 1），两者的证明技术和假设条件不同，不构成严格的逻辑 extension。这与 R2-W5 一致。

**结论**：建议作者降低 Proposition 1 的呈现权重，将叙事重心放在系统性实证贡献（诊断框架 + 27 策略否证 + 机制定位）上。但"新颖性有限"的判定过重——如果只需要"可预见的延伸"，那么任何 negative result paper 都可以被事后论证为"可预见的"。本文的价值恰恰在于提供了社区缺乏的系统性证据。

---

**[AGREE] R2-N2: Bias Ratio (BR) 的循环论证风险**

R2 的批评在方法论上是正确的，这是我 R1 审稿中未充分注意到的一个重要问题。

关键推理链：BR 通过 source attribution (Eq. 3, §3.1) 衡量约束是否"支持"某个答案——即 e(c, a) = 1 当且仅当 c 来自产生答案 a 的 trace。在模型答错的 error cases 上，多数 trace 产生错误的多数答案 a_M，因此 BR > 1 在一定程度上是 base-rate 效应的数学必然，而非独立的 bias 证据。

具体来说：如果某 error case 上 60% traces 产生 a_M（错误）、40% 产生 a*（正确），那么在 source attribution 下，约 60% 的约束"支持" a_M，40% 支持 a*，给出 BR ≈ 1.5，即使约束提取完全无偏。Table 2 报告的 BR 值 (1.66–4.97) 确实高于这种简单比例，但没有 null model 就无法量化多少是 base-rate 效应、多少是"额外 bias"。

R2 建议的 permutation-based null distribution 是合理的解决方案：在保持 trace 投票分布不变的情况下随机置换约束-答案的对应关系，得到 BR 的 null expectation，然后测试观测 BR 是否显著超过。

但我要指出：BR 的循环问题不否定论文的整体 confirmation bias 论证。以下证据链独立于 BR：
- Table 11 (§5.1): 约束-答案一致率 ≥ 99% across all α levels，直接证明约束几乎不产生独立信号
- Degeneration condition (Eq. 4, Table 10): SICA 在 94.4% 问题上产生与 SC 相同答案
- Table 1: FDR 校正后无条件显著正效应
- Oracle (Appendix G): gold constraints 显著提升，证明问题在提取质量

所以 confirmation bias 的结论是 robust 的，即使 BR 指标本身有方法论问题。建议作者：(a) 补充 permutation null model，(b) 如果无法补充，将 BR 降级为"描述性指标"而非 causal evidence。

---

**[AGREE] R2-N3: Diagnostics 100% 准确率是 in-sample 评估**

R2 的批评完全正确。

§5.3 (page 7) 的三个 zero-cost diagnostics 从 60 个条件推导决策边界，并在同一 60 个条件上评估得到 100% 准确率。这在统计上没有意义——等价于 in-sample fitting。更关键的是，这 60 个条件全部是 negative cases（SICA 不优于 SC），所以任何 trivial classifier（如"永远预测不会帮助"）都能得到 100%。

论文声称在 LLaMA-3.1-8B on FOLIO 上做了 held-out 验证（§5.3, page 7："evaluated prospectively on held-out LLaMA-3.1-8B"），但这仅 1 个条件且仍为 negative case，不构成有意义的 OOD 验证。

诊断框架的真正价值应体现在预测 positive cases（SICA 何时会帮助）。论文中存在 positive cases（cross-architecture escape, Table 3; oracle, Appendix G），但未用这些条件验证诊断框架是否能正确预测"会帮助"。

我在 R1 审稿中未将此列为独立问题，是一个疏漏。同意 R2 的建议：增加完整的 held-out model family 验证，并弱化 100% accuracy claim 的呈现。

---

### Should-Fix 问题

**[AGREE] R2-W1: 标题 "Fail to Improve" overclaiming**

与我 R1-N2 一致。Power < 21% + TOST 仅 8/16 条件显著 → 标题中无条件否定不被统计证据支持。R2 建议的 "Do Not Substantially Improve" 是合理的修改方向。

---

**[REBUT] R2-W2: 缺少 training-based self-verification 讨论**

部分不同意。论文在 §2 (page 2-3) 已明确界定范围为 training-free methods："we find the bottleneck lies in constraint extraction, not verification: self-extracted constraints inherit the model's bias regardless of solver soundness (§5.1)"。并在 §7 Conclusion (page 8) 明确指出 "trained constraint extractors... could produce genuinely discriminative constraints that break the distributional prior" 作为 future direction。

但我同意 R2 的一个具体论点：既然论文声称 extend Huang et al. (2024) 的 impossibility result，就应讨论 training-based 方法如何理论上 escape Proposition 1 的信息上限（通过引入外部训练信号打破 A2 假设）。这会加强理论框架的完整性。

建议：在 §2 增加一段讨论 training-based methods 如何通过违反 A2（引入外部奖励信号使约束不再 trace-determined）来 escape SCB。不需要大量讨论具体方法，但应明确理论边界。

---

**[AGREE] R2-W3: Capability-gap principle 基于 n=6 条件**

与我 R1-W8 完全一致。Table 3 仅 Mistral-7B 1 个条件 significant（SC = 39.33%, Δ = +6.67pp, p < 0.001）。"Principle" 的措辞过强。同意降级为 "preliminary observation" 或 "hypothesis"。§6 标题 "Escaping the Bottleneck" 也应弱化。

---

**[REBUT] R2-W4: "27 strategies fail" scope 不匹配**

部分不同意。R2 说 27 个策略"局限于同一 pipeline 框架变体"，但 Table 14 (Appendix I) 和 §5.2 (page 7) 的覆盖范围实际上跨越了多个独立维度：

- **Prompt-level** (9 strategies): constrastive, cross-model, debate, problem-perturbation, 27 trace filter, Z3 filter, bootstrapped gold, selective abstention, SKCI perturbation
- **Method-level** (3 strategies, Table 13): ICG (independently generated constraints), contrastive scoring, trace coupling
- **Cross-model** (Table 14 #5): cross-model extraction
- **Formal proof** (Table 14 #13): PROVER + code verification
- **UNSAT filtering** (Table 14 #25): UNSAT-based constraint filtering

这些策略覆盖了约束提取、约束评分、约束过滤、独立生成等多个设计轴。虽然全部在"从 LLM 提取约束→用约束聚合"的大框架内，但这正是论文的研究范围——training-free self-extraction methods。

但我同意论文不应 claim "all training-free methods fail"，应限定为 "all training-free methods within the constraint-extraction-aggregation paradigm"。

---

**[AGREE] R2-W5: "Extending Huang et al." 是 overselling**

与我在 R2-N1 回应中的立场一致。Huang et al. (2024) 的证明框架基于 natural language self-correction 的不可能性，本文基于 data processing inequality 和 source attribution 的退化——形式化框架、假设条件和证明技术完全不同，不构成逻辑 extension。

§1 (page 1) 的 "This extends the self-correction impossibility of Huang et al. (2024) to formal verification" 应改为 "This provides independent evidence consistent with Huang et al. (2024), demonstrating that the self-correction limitation persists even under formal symbolic verification."

---

### Minor Issues

**[AGREE] R2-M1**: Figure 1 信息密度确实偏高，但作为 pipeline overview 在 conference paper 中常见。Minor concern。

**[AGREE] R2-M3**: Abstract 信息量大，但考虑到 negative result paper 需要在 abstract 中说服读者问题不是实验不足而是 structural issue，信息密度有一定合理性。可以适当精简。

**[REBUT] R2-M4**: Limitations section 长度。EMNLP 2026 rules 明确要求 limitations "只需写一小段，覆盖 3 个点左右"（见 CLAUDE.md 中用户自定义规则），所以 ~5 行覆盖 3 个点是合规的。R2 可能不熟悉这一具体要求。

**[AGREE] R2-M2, M5**: K_eff 直觉解释和 §2 段间逻辑衔接可以改进，属于写作层面修改。

---

### Missing References 回应

**[AGREE] Kamoi et al. (TACL 2024) self-correction survey**: 作为 self-correction 领域的 survey，应该在 §2 引用。

**[REBUT] S²R 和 DuPO**: 这些是 training-based 方法，在论文的 training-free scope 之外。但如上 R2-W2 回应所述，应在理论边界讨论中提及。

**[REBUT] Lakshminarayanan et al. (NeurIPS 2017) Deep Ensembles**: 与本文讨论的 ensemble diversity 相关性有限。论文已引用 Kuncheva and Whitaker (2003) 和 Ladha (1992) 作为 ensemble/voter theory 基础，这些更直接相关。

---

### 评分差距分析 (R1: 3.5 vs R2: 3.0)

R2 给出 3.0 (Findings)，我给出 3.5 (Borderline Conference)。差距主要在两个维度：

**1. Excitement 评分差异 (R1: 3.5 vs R2: 2.5)**：

R2 认为核心洞察可从 Huang et al. (2024) 预见。我认为这种事后论证对 negative result paper 不公平——如果发现"形式化约束确实帮助了"，没有人会说这是 Huang et al. 的"自然延伸"。Negative result 的价值恰恰在于否证了社区中活跃研究方向（neuro-symbolic verification）的一个隐含假设。论文的诊断框架和 27 策略系统否证提供了超越 "one-liner negative finding" 的实质性贡献。

但我承认 Excitement 3.5 可能略高——诊断框架的实际影响力取决于是否有更多 positive cases 来验证其价值（R2-N3 的 overfitting 问题）。合理的 compromise 可能是 Excitement 3.0。

**2. Soundness 评分差异 (R1: 3.5 vs R2: 3.0)**：

R2 的 BR 循环论证 (N2) 和 diagnostics overfitting (N3) 是我 R1 审稿中未充分关注的问题，两者均有技术实质。但我认为这些是 fixable issues：BR 可通过 permutation null model 修复，diagnostics 可通过 held-out 验证修复，均不需要重新做实验。论文的核心证据链（Table 1 null result + 99% agreement + oracle experiment + degeneration condition）不受这两个问题影响。

**我的评分调整建议**：
- 如果作者修复 N2 (BR null model) 和 N3 (diagnostics held-out)，我维持 3.5 → Conference 推荐
- 如果不修复，我认为 3.0-3.5 区间均合理，偏向 3.0 (Findings)
- R2 的 Excitement 2.5 我认为偏低，3.0 更合理

**总体**: 两位 reviewer 在技术问题上高度一致（Proposition 1 scope、power limitations、标题 overclaiming），分歧主要在 novelty 权重和 fixable issues 的严重程度评估上。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1692 · 2026-05-23T08:19:32.689493+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_13/submitted.pdf",
  "pages": "1-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_13/submitted.pdf",
    "pages": "1-10"
  }
}
```

</details>

---


### Tool call

_source line 1693 · 2026-05-23T08:19:33.141797+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool call

_source line 1694 · 2026-05-23T08:19:33.293099+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "symb_invariant_consensus"
  }
}
```

</details>

---


### Tool result

_source line 1695 · 2026-05-23T08:19:33.394270+00:00_

PDF pages extracted: 10 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_13/submitted.pdf (637.5KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 704
}
```

</details>

---


### Tool result

_source line 1696 · 2026-05-23T08:19:33.462184+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T08:13:07.833834+00:00\", \"completed_at\": \"2026-05-23T08:17:19.279797+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页全为文字（Abstract + Introduction 开头），无视觉锚点。Figure 1 出现在 page 2 顶部，仍在审稿人\\\"前 2 分钟扫描\\\"窗口内，影响有限。ACL 论文此布局常见\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 为全宽 pipeline 图，含红色虚线框标注 Independence Bottleneck，caption 自包含（不看正文可理解），Title-Abstract-Figure 1 三者 narrative 一致。第一印象良好\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"纯文本+公式页（Method §3.1），无 figure/table。但上下文有 page 2 的 Figure 1 和 page 4 的 Figure 2 夹持，不构成连续纯文本\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"两个全宽表格（Table 1 + Table 2）堆叠，页面非常 data-dense。两表各自传达不同 message（主结果 vs confirmation bias 指标），合并不合适，当前布局可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"正文最后一页：Table 3 + §7 Discussion and Conclusion + Limitations 开头。内容填充充分，无大面积空白。Limitations 从 page 8 底部延伸至 page 9 顶部，符合 EMNLP 2026 规定（不计入 8 页限制）\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 2（散点图，SICA Δ vs SC baseline）：三个 regime（Type A/B/C）用背景色带区分，marker 按模型分类。图例可读，颜色区分清晰。点的标注和趋势线可辨\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 3（Causal DAG）：单栏内小图，节点标签为单字母（M, T, A, C, S），在 150 dpi 下可读。Caption 完整解释因果结构。尺寸偏小但 DAG 本身简单，不构成阅读障碍\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 4（27 种 training-free 策略柱状图，全宽）：bars 按 4 个 category 分组着色。caption 说明省略了 4 个策略以保持清晰度。整体 message（绝大多数策略产生 neutral-to-negative 结果）传达明确。个别 bar 标签在打印时可能偏小\"}, {\"severity\": \"info\", \"dimension\": \"page 17\", \"message\": \"Figure 6（SICA Δ vs K 折线图）：单栏图，折线+误差带，轴标签清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 20\", \"message\": \"Figure 7（Independence-accuracy trade-off 散点图）：单栏，marker+虚线标注 baseline，可读\"}, {\"severity\": \"info\", \"dimension\": \"page 23\", 
…[truncated 1915 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 320
}
```

</details>

---


### Tool result

_source line 1697 · 2026-05-23T08:19:33.462744+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 169
}
```

</details>

---


### Tool call

_source line 1698 · 2026-05-23T08:20:16.046410+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | head -300",
  "description": "Read current review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | head -300",
    "description": "Read current review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1699 · 2026-05-23T08:20:16.197620+00:00_

# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)
- id: "R1-C1"
  summary: "Method Stage 3 sat() implementation undescribed"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit."
  resolution_round: 3

- id: "R1-C2"
  summary: "Most experiments underpowered (n≤60), no power analysis"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "Power analysis + Bootstrap CIs added. Larger n conditions (200-600)."
  resolution_round: 3

- id: "R1-C3"
  summary: "Oracle/upper-bound experiment missing"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp."
  resolution_round: 3

- id: "R1-C4"
  summary: "Huang et al. (ICLR 2024) not cited"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: "Huang, Stechly, Kambhampati all cited and discussed."
  resolution_round: 2

- id: "R1-C5"
  summary: "Critical related work missing"
  category: writing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "~48 citations, 5 Related Work paragraphs."
  resolution_round: 3

- id: "R1-C9"
  summary: "Capability trap novelty unclear"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 3
  resolution: "Reframed as regime-dependent analysis with CJT framework."
  resolution_round: 3

- id: "R3-N1"
  summary: "σ(c,a) scoring inconsistent between self-extraction and oracle"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 3
  last_seen_round: 4
  resolution: "Paper Agent added clarifying sentence in method.tex."
  resolution_round: 4

- id: "R3-N2"
  summary: "α va
…[truncated 5934 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1700 · 2026-05-23T08:20:23.015087+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | wc -l; echo \"---TAIL---\"; cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | tail -600",
  "description": "Read remaining review issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | wc -l; echo \"---TAIL---\"; cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null | tail -600",
    "description": "Read remaining review issues"
  }
}
```

</details>

---


### Tool result

_source line 1701 · 2026-05-23T08:20:23.116415+00:00_

935
---TAIL---
  last_seen_round: 15
  mentions:
    - round: 14
      reviewers: [1, 2]
      note: "R1认可Z3 formal solver场景非平凡. R2维持新颖性有限. 建议降低Hypothesis措辞"
    - round: 15
      reviewers: [1, 2]
      note: "R15(fresh) 与R10-W7/R12-N2合并. K_eff是Kish(1965)直接应用, SCB是confirmation bias特例. 贡献在于empirical depth非conceptual novelty"

- id: "R10-I2"
  summary: "Independence-Accuracy Trade-off 作为独立贡献有 bias-variance 重述嫌疑"
  category: framing
  severity: warning
  status: in_progress
  first_raised_round: 10
  last_seen_round: 15
  mentions:
    - round: 15
      reviewers: [1, 2]
      note: "R15(fresh) 共识major: §6 trade-off与ensemble learning bias-variance tradeoff(Krogh&Vedelsby 1994)同构, 应在§6或§7显式讨论. 缺引Lakshminarayanan et al.(2017)"

- id: "R10-VL1"
  summary: "主文缺结果可视化"
  category: format
  severity: warning
  status: in_progress
  first_raised_round: 10
  last_seen_round: 15
  mentions:
    - round: 15
      reviewers: []
      note: "R15 视觉审查: 主文5个display items(2 figures+3 tables), ~0.63/页, 合理范围低端"

- id: "R11-N1"
  summary: "Spearman ρ=1.0 (n=6) 被过度使用——有效自由度远低于6"
  category: experiment
  severity: critical
  status: in_progress
  first_raised_round: 11
  last_seen_round: 15
  mentions:
    - round: 15
      reviewers: [1, 2]
      note: "R15(fresh) 共识: suggestive非definitive, 应降低claim强度"

- id: "R11-N2"
  summary: "中心 claim 'SICA fails' 与统计功效不匹配——Abstract/title 过强"
  category: framing
  severity: critical
  status: in_progress
  first_raised_round: 11
  last_seen_round: 15
  mentions:
    - round: 14
      reviewers: [1, 2]
      note: "R14(fresh) R1-N1: 标题scope超出. R2-W1: 'no evidence'需hedge. R1同意加hedge"
    - round: 15
      reviewers: [1, 2]
      note: "R15(fresh) 共识(R1 critical, R2 major): power<21%, MDE远大于观测效应, 'Fail to Improve'=overclaiming. 应改为'No Evidence'或'Limitations of'. R2补充: 多重证据(oracle/shuffle/SCB)部分缓解但不消除功效问题"
  action_items:
    - round: 14
      action: "标题限定为Logical Reasoning + Abstract加power caveat"
      assigned_to: "paper_agent"
      status: in_progr
…[truncated 13774 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---
