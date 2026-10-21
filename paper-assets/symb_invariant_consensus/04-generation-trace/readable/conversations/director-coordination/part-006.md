# Director coordination — Part 6 of 9

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

[← Part 5](part-005.md) · [Transcript overview](../director-coordination.md) · [Part 7 →](part-007.md) · [Structured JSON](../../../sessions/bd/bdd0e6c8e8a0a8a81e76.json)

## Round 119

### Tool call

_source line 1702 · 2026-05-23T08:24:03.933354+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "symb_invariant_consensus",
  "issues_yaml": "# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)\n- id: \"R1-C1\"\n  summary: \"Method Stage 3 sat() implementation undescribed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit.\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Most experiments underpowered (n≤60), no power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Power analysis + Bootstrap CIs added. Larger n conditions (200-600).\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Oracle/upper-bound experiment missing\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp.\"\n  resolution_round: 3\n\n- id: \"R1-C4\"\n  summary: \"Huang et al. (ICLR 2024) not cited\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Huang, Stechly, Kambhampati all cited and discussed.\"\n  resolution_round: 2\n\n- id: \"R1-C5\"\n  summary: \"Critical related work missing\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"~48 citations, 5 Related Work paragraphs.\"\n  resolution_round: 3\n\n- id: \"R1-C9\"\n  summary: \"Capability trap novelty unclear\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Reframed as regime-dependent analysis with CJT framework.\"\n  resolution_round: 3\n\n- id: \"R3-N1\"\n  summary: \"σ(c,a) scoring inconsistent between self-extraction and oracle\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Paper Agent added clarifying sentence in method.tex.\"\n  resolution_round: 4\n\n- id: \"R3-N2\"\n  summary: \"α value never specified\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"α=0.5 explicit in Eq.(3) and §4.1.\"\n  resolution_round: 3\n\n# Round 9+ issues\n\n- id: \"R9-W2\"\n  summary: \"NLI combo weight parameter w 未交叉验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 16\n  mentions:\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 未单独提及 w 参数\"\n    - round: 15\n      reviewers: []\n      note: \"R15(fresh) 未单独提及\"\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n\n- id: \"R9-W3\"\n  summary: \"Capability Gap Hypothesis 基于极小样本 (n=6)\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 16\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 共识: 仅6条件仅Mistral-7B显著, 需软化结论\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识: §6 escape仅SC<40%验证, 'SC≈70%'无数据支撑\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 共识AGREE: 仅1个条件显著(Mistral-7B SC=39.33%), 'principle'措辞过强, 应降级为'preliminary observation/hypothesis'\"\n  action_items:\n    - round: 14\n      action: \"§6结论软化为preliminary evidence + 讨论task gap\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R9-VL1\"\n  summary: \"Pages 1-2 连续纯文本无 display item\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16 视觉审查: Page 1纯文本(Abstract+Intro), Figure 1在page 2顶部, 仍在'前2分钟扫描'窗口内, 影响有限\"\n\n- id: \"R9-VL4\"\n  summary: \"Discussion/Conclusion 展开不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及, R2-M4仅提Limitations长度(R1 rebut citing EMNLP rules)\"\n\n- id: \"R10-N1\"\n  summary: \"Proposition 1 (Self-Extraction Ceiling) 无证明——empirical claim dressed as theorem\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 13\n  resolution: \"当前论文使用 Proposition 1 with formal proof (page 6)\"\n  resolution_round: 13\n\n- id: \"R10-N2\"\n  summary: \"κ→K_eff 映射理论基础不足——r=0.625 验证弱\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R16(fresh) R1-W7: K_eff exchangeable correlation假设可能被违反, minor concern\"\n\n- id: \"R10-N3\"\n  summary: \"Capability gap 'perfectly monotonic' 结论基于 n=6 非独立数据点\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 与R9-W3合并. 共识AGREE: n=6数据点不足以支撑'principle'\"\n\n- id: \"R10-W1\"\n  summary: \"DRC τ 阈值无 held-out 评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n\n- id: \"R10-W2\"\n  summary: \"Cross-architecture NLI escape 适用面极窄\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R1-W8+R2-W3共识: generalizability受限, 仅NLI-friendly数据集测试\"\n\n- id: \"R10-W3\"\n  summary: \"四种子复制方差大 + 统计功效 <21%\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R1-W3: multi-seed仅2/6模型, seed noise ±2.34pp超过多数|Δ|. R2 AGREE\"\n\n- id: \"R10-W4\"\n  summary: \"TOST ±2pp margin 缺少显式理由\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R16(fresh) R1-N2: ±2pp margin缺乏先验依据, 需sensitivity analysis. R2 AGREE\"\n\n- id: \"R10-W5\"\n  summary: \"Bias Ratio 无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"BR CI 已整合: Mistral [3.98,6.37], Qwen [2.44,7.11]\"\n  resolution_round: 10\n\n- id: \"R10-W6\"\n  summary: \"SatLM specification-generation vs SICA trace-extraction 对比不充分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n\n- id: \"R10-W7\"\n  summary: \"'Symbolic Confirmation Bias' 需与近期 CoT confirmation bias 工作区分\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R2-N1: SCB是Huang(2024)+Wan(2025)的自然延伸, R1部分REBUT(negative result value不应事后贬低, 但同意DPI部分近平凡). 部分共识: 贡献在empirical depth非conceptual novelty\"\n\n- id: \"R10-W8\"\n  summary: \"Related Work 过度压缩——引用列表而非文献讨论\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [2]\n      note: \"R16(fresh) R2-M5: §2段间逻辑衔接不够清晰\"\n\n- id: \"R10-I1\"\n  summary: \"'Symbolic Mirage' 概念新颖性——与 Huang/Wan 的 confirmation bias 区别\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 同R10-W7. R2: DPI是教科书推论, novelty在于识别正确的Markov chain而非DPI本身\"\n\n- id: \"R10-I2\"\n  summary: \"Independence-Accuracy Trade-off 作为独立贡献有 bias-variance 重述嫌疑\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n\n- id: \"R10-VL1\"\n  summary: \"主文缺结果可视化\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16 视觉审查: 主文5 display items(Figure 1-4 + Table 1-3), 合理\"\n\n- id: \"R11-N1\"\n  summary: \"Spearman ρ=1.0 (n=6) 被过度使用——有效自由度远低于6\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 与R9-W3合并. 共识: n=6 suggestive非definitive\"\n\n- id: \"R11-N2\"\n  summary: \"中心 claim 'SICA fails' 与统计功效不匹配——Abstract/title 过强\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 共识critical: R1-N2(power<21%, MDE≥1.86pp, ~79%概率检测不到2pp效果) + R2-W1(标题'Fail to Improve'overclaiming). R2 AGREE R1分析. 建议标题改为'Do Not Substantially Improve'或加power caveat\"\n  action_items:\n    - round: 16\n      action: \"标题软化 + Abstract加power caveat + TOST margin sensitivity analysis\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R11-N3\"\n  summary: \"TOST ±2pp margin 缺乏 principled 论证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R1-N2涵盖: ±2pp margin无先验依据, 需补充不同margin(±1/3/5pp)的TOST sensitivity\"\n\n- id: \"R11-W1\"\n  summary: \"DRC 评估不充分——仅PW完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n\n- id: \"R11-W2\"\n  summary: \"BR 指标存在循环论证倾向\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R2-N2 critical: BR>1部分是base-rate效应(60% traces→60%约束支持多数答案), 需permutation null model量化excess bias. R1 AGREE(审稿中未注意到此问题). 共识: BR循环论证不否定SCB整体论证(Table 11/degeneration condition/oracle独立支持), 但BR指标本身需null model或降级为描述性指标\"\n  action_items:\n    - round: 16\n      action: \"补充permutation-based null distribution, 或将BR降级为描述性指标并明确声明base-rate组成\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R11-W3\"\n  summary: \"术语过度品牌化——'Symbolic Mirage' 偏 dramatic\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n\n- id: \"R11-W4\"\n  summary: \"新颖性定位需更早更明确建立与先验工作的 distinction\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R2-N1+R2-W5: SCB是Huang et al.的自然延伸, 'extending'是overselling. R1部分REBUT: 机制定位+27策略否证+诊断框架是非平凡贡献, 但同意DPI部分近平凡\"\n\n- id: \"R11-W5\"\n  summary: \"Independence-Accuracy Trade-off 应定位为量化而非新发现\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n\n- id: \"R11-W6\"\n  summary: \"遗漏引用: Byerly & Khashabi (2026 TACL) 等\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"当前论文已引用 Byerly and Khashabi (2026)\"\n  resolution_round: 13\n\n- id: \"R11-W7\"\n  summary: \"27 策略计数膨胀 + 未尝试 trained constraint extractor\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R2-W4: 27策略局限于self-extraction paradigm内变体, claim scope需限定. R1部分REBUT: 策略确实跨多维度(prompt/method/cross-model/formal proof), 但同意应限定scope为'within constraint-extraction-aggregation paradigm'\"\n\n- id: \"R11-VL1\"\n  summary: \"主文缺结果可视化——需上提 Figure 到主文\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16 视觉审查: Figure 2(散点图p4), Figure 3(DAG p6), Figure 4(柱状图p7)已在主文, 覆盖合理\"\n\n- id: \"R12-N1\"\n  summary: \"标题 overclaiming about frontier scale\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 标题已含'Logical Reasoning'(非'LLM Reasoning'), 但'Fail to Improve'仍overclaiming given power<21%. 共识: 需进一步软化\"\n\n- id: \"R12-N2\"\n  summary: \"SCB 核心新颖性不足——self-correction failure 在 FOL 载体上的实例化\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R2-N1 critical: SCB=Huang+DPI, Wan(2025)/Jhaveri(2026)从不同角度得出类似结论. R1 partial REBUT: negative result不应事后贬低, 诊断框架+27策略否证有独立价值. 部分共识: 定位为'系统性量化'而非'发现', 弱化Prop 1呈现\"\n\n- id: \"R12-N3\"\n  summary: \"DRC 作为 Contribution 4 不够充分\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"DRC demoted to practical observation in §6\"\n  resolution_round: 13\n  first_raised_round: 12\n  last_seen_round: 13\n\n- id: \"R12-W1\"\n  summary: \"BR 可能存在循环论证——56.4%零变量重叠使约束按定义支持source answer\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 与R11-W2合并. R2-N2提升为critical: 需null model\"\n\n- id: \"R12-W2\"\n  summary: \"CIL 名称和 information-theoretic 声称有误导\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Renamed to CCR, removed 'unify' claim\"\n  resolution_round: 13\n  first_raised_round: 12\n  last_seen_round: 13\n\n- id: \"R12-W3\"\n  summary: \"Figure 2 placement——应在正文而非附录\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Figure 2 已在正文 page 4\"\n  resolution_round: 13\n\n- id: \"R12-W4\"\n  summary: \"Appendix vs 主文关键信息分配不合理\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [2]\n      note: \"R16(fresh) R2-M3: Abstract信息过载(6个要素). R2-M2: K_eff缺直觉解释\"\n\n- id: \"R12-EC1\"\n  summary: \"Extractor Confound——所有 frontier cross-model extraction 使用同一 Mistral-7B extractor\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n\n- id: \"R13-N1\"\n  summary: \"摘要 BR 4.97× 选择性报告——最极端条件\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) Abstract报告'at least 1.66×', 为最小值. 比报告4.97×更保守, 但BR循环论证问题(R11-W2)影响所有BR值的可信度\"\n\n- id: \"R13-N2\"\n  summary: \"统计功效呈现不足——10/16 underpowered, power analysis 埋在附录\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 与R11-N2合并. R1-N2 critical: observed power<21%, TOST仅8/16显著. R2 fully AGREE\"\n\n- id: \"R13-N3\"\n  summary: \"α=0.5 无敏感性分析\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R1-W6: α=0.5无理论依据, 需sensitivity analysis α∈{0,0.25,0.5,0.75,1.0}. R2 AGREE. 论文有Table 11(α ablation ≥99% agreement), 但R1/R2共识: ceiling effect不等于鲁棒性\"\n\n- id: \"R13-W1\"\n  summary: \"符号/指标过载——8页内7个定量工具\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n\n- id: \"R13-W2\"\n  summary: \"NLI claim 须限定到命题逻辑任务\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R16(fresh) R1-W9: 'First-order logic'描述轻微overselling, 99%约束是propositional level. R2 AGREE\"\n\n- id: \"R13-W3\"\n  summary: \"语法去重可能膨胀 BR——未报告语义去重后 BR\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n\n- id: \"R13-W4\"\n  summary: \"Symbolic Mirage Hypothesis §3.3 与 §5 验证不连贯\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及(当前论文无显式§3.3 Hypothesis section)\"\n\n- id: \"R13-W5\"\n  summary: \"缺引: Dhuliawala et al. 2023 Chain-of-Verification\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"已引用 dhuliawala2023chainofverification\"\n  resolution_round: 14\n\n- id: \"R14-N1\"\n  summary: \"标题'LLM Reasoning'范围超出实验证据——仅覆盖逻辑推理\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 标题已为'LLM Logical Reasoning', domain scope改善. 但'Fail to Improve'仍overclaiming\"\n\n- id: \"R14-N2\"\n  summary: \"Symbolic Mirage Hypothesis Predictions 1-2 为事后总结非独立预测\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 当前论文无显式Predictions标签, 未单独提及\"\n\n- id: \"R14-W1\"\n  summary: \"Cross-architecture实验仅6条件/单一verifier/仅Mistral-7B显著\"\n  category: experiment\n  severity: major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R1-W8+R2-W3共识: 仅Mistral-7B(SC=39.33%)显著, 'principle'过强, 降级为'preliminary observation'\"\n\n- id: \"R14-W2\"\n  summary: \"8页正文信息过载——§5.5/§6/§7展开不足\"\n  category: writing\n  severity: major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [2]\n      note: \"R16(fresh) R2-M3: Abstract信息过载(6要素). R2-M2: K_eff缺直觉解释. R2-M5: §2段间衔接不够\"\n\n- id: \"R14-W3\"\n  summary: \"'No evidence' claim scope与统计功效不匹配\"\n  category: framing\n  severity: major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 与R11-N2合并. 共识critical\"\n\n- id: \"R14-W4\"\n  summary: \"BR计算子集大小(n_err)未报告\"\n  category: experiment\n  severity: moderate\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R1-W4: Table 2多数条件未报CI. R2 AGREE. 当前论文Table 2已有n_err列但多数条件无CI\"\n\n- id: \"R14-W5\"\n  summary: \"Related Work遗漏: SETS(2025), MAV(2025)\"\n  category: writing\n  severity: minor-to-major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R2-W2新增: S²R(ACL 2025), DuPO(2025), Kamoi et al.(TACL 2024). R1部分REBUT(scope外)但同意应讨论理论边界\"\n\n- id: \"R14-W6\"\n  summary: \"Fleiss' κ→ICC近似仅r=0.625——prevalence paradox\"\n  category: method\n  severity: moderate\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R16(fresh) R1-W7: K_eff exchangeability假设可能被违反, 但minor, 不影响核心结论\"\n\n# R15(fresh) issues\n\n- id: \"R15-M1\"\n  summary: \"遗漏引用: DuPO (ICLR 2026) — training-based self-verification\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"共识AGREE\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R2-W2提出, R1部分REBUT(scope外但应讨论理论边界)\"\n\n- id: \"R15-M2\"\n  summary: \"遗漏引用: S²R (2025) — RL-based self-verification\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"共识AGREE\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R2-W2提出, R1部分REBUT(scope外但应讨论理论边界)\"\n\n- id: \"R15-M3\"\n  summary: \"遗漏引用: LLM as Formalizers on CSP (arXiv 2505.13252, 2025)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n\n- id: \"R15-M4\"\n  summary: \"遗漏引用: Lakshminarayanan et al. (2017) Deep Ensembles\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R16(fresh) R1 REBUT: Kuncheva & Whitaker(2003)和Ladha(1992)已更直接相关. Minor\"\n\n- id: \"R15-W1\"\n  summary: \"α=0.5敏感性分析≥99% agreement是ceiling effect\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R1-W6要求补充α sensitivity analysis. R2 AGREE. 共识: ceiling effect不等于鲁棒性\"\n\n# R16(fresh) 新发现\n\n- id: \"R16-N1\"\n  summary: \"Proposition 1 证明范围与声称范围不匹配——Part(i)仅对source-attribution成立但标题claim 'structural'\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R1-N1 critical, R2 fully AGREE. 共识: Part(i)依赖SICA特定的source attribution scoring(Eq.3), 非数学必然; Part(ii) DPI是平凡推论(I(C;Y)≤I(T;Y)). 建议拆分为两个结果, 明确区分适用范围. R2补充: DPI不排除约束通过重新组织信息打破相关模式\"\n  action_items:\n    - round: 16\n      action: \"将Proposition 1分为source-attribution退化定理(精确但specific) + DPI bound(普遍但弱), 正文明确区分\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R16-N2\"\n  summary: \"Diagnostics 100%准确率是in-sample评估——overfitting风险, holdout验证不充分\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-N3 critical, R1 fully AGREE(审稿中未注意到). 共识: (1) 决策边界从60条件推导并在同一60条件上评估=in-sample fitting; (2) holdout仅LLaMA-3.1-8B×FOLIO 1个条件=不充分; (3) 60条件全为negative cases, 任何trivial classifier('永远预测不帮助')都能100%; (4) 未在positive cases(cross-arch escape, oracle)上验证. Abstract/§1/§7中此claim为三大贡献之一, 过度表述\"\n  action_items:\n    - round: 16\n      action: \"增加held-out model family验证 + 弱化claim为'correctly classify all tested conditions within experimental scope' + 讨论OOD失败条件\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R16-M1\"\n  summary: \"遗漏引用: Kamoi et al. (TACL 2024) self-correction survey\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2提出, R1 AGREE. self-correction方向最全面survey, 应引用定位论文\"\n\n- id: \"R16-M2\"\n  summary: \"遗漏引用: AlphaCode/CodeT — constraint verification in code domain\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R1提出: code domain中约束过滤成功案例, 可对比讨论为何逻辑推理领域失败\"\n\n- id: \"R16-W1\"\n  summary: \"'Extending Huang et al. (2024) to formal verification' 是overselling——两者证明框架不同不构成逻辑extension\"\n  category: framing\n  severity: major\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W5, R1 fully AGREE. 共识: Huang基于value/policy iteration, 本文基于DPI+source attribution, 形式化框架不同. 建议改为'consistent with / complement / provide independent evidence for'\"\n  action_items:\n    - round: 16\n      action: \"§1和Abstract将'extend'改为'provide independent evidence consistent with'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R16-W2\"\n  summary: \"GSM8K(n=30)/AIME(n=22)样本量过小, 不应与大样本条件等权重引用\"\n  category: experiment\n  severity: major\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R1-W5, R2 AGREE. 论文已标注为'exploratory, n<60'(Table 1 caption), 但正文§5.3引用时未区分\"\n\n- id: \"R16-W3\"\n  summary: \"缺少training-based self-verification方法讨论——Proposition 1理论边界不完整\"\n  category: writing\n  severity: major\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W2 major, R1部分REBUT(scope已限定为training-free, §7提及trained extractors)但AGREE应讨论训练如何通过违反A2打破信息上限. 共识: §2增加一段training-based self-verification, 明确Prop 1适用边界\"\n  action_items:\n    - round: 16\n      action: \"§2增加training-based self-verification段落, 引用S²R/DuPO, 明确Prop 1仅适用于inference-time same-model\"\n      assigned_to: \"paper_agent\"\n      status: open\n"
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
    "issues_yaml": "# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)\n- id: \"R1-C1\"\n  summary: \"Method Stage 3 sat() implementation undescribed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit.\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Most experiments underpowered (n≤60), no power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Power analysis + Bootstrap CIs added. Larger n conditions (200-600).\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Oracle/upper-bound experiment missing\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp.\"\n  resolution_round: 3\n\n- id: \"R1-C4\"\n  summary: \"Huang et al. (ICLR 2024) not cited\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Huang, Stechly, Kambhampati all cited and discussed.\"\n  resolution_round: 2\n\n- id: \"R1-C5\"\n  summary: \"Critical related work missing\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"~48 citations, 5 Related Work paragraphs.\"\n  resolution_round: 3\n\n- id: \"R1-C9\"\n  summary: \"Capability trap novelty unclear\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Reframed as regime-dependent analysis with CJT framework.\"\n  resolution_round: 3\n\n- id: \"R3-N1\"\n  summary: \"σ(c,a) scoring inconsistent between self-extraction and oracle\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Paper Agent added clarifying sentence in method.tex.\"\n  resolution_round: 4\n\n- id: \"R3-N2\"\n  summary: \"α value never specified\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"α=0.5 explicit in Eq.(3) and §4.1.\"\n  resolution_round: 3\n\n# Round 9+ issues\n\n- id: \"R9-W2\"\n  summary: \"NLI combo weight parameter w 未交叉验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 16\n  mentions:\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 未单独提及 w 参数\"\n    - round: 15\n      reviewers: []\n      note: \"R15(fresh) 未单独提及\"\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n\n- id: \"R9-W3\"\n  summary: \"Capability Gap Hypothesis 基于极小样本 (n=6)\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 16\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 共识: 仅6条件仅Mistral-7B显著, 需软化结论\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识: §6 escape仅SC<40%验证, 'SC≈70%'无数据支撑\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 共识AGREE: 仅1个条件显著(Mistral-7B SC=39.33%), 'principle'措辞过强, 应降级为'preliminary observation/hypothesis'\"\n  action_items:\n    - round: 14\n      action: \"§6结论软化为preliminary evidence + 讨论task gap\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R9-VL1\"\n  summary: \"Pages 1-2 连续纯文本无 display item\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16 视觉审查: Page 1纯文本(Abstract+Intro), Figure 1在page 2顶部, 仍在'前2分钟扫描'窗口内, 影响有限\"\n\n- id: \"R9-VL4\"\n  summary: \"Discussion/Conclusion 展开不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及, R2-M4仅提Limitations长度(R1 rebut citing EMNLP rules)\"\n\n- id: \"R10-N1\"\n  summary: \"Proposition 1 (Self-Extraction Ceiling) 无证明——empirical claim dressed as theorem\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 13\n  resolution: \"当前论文使用 Proposition 1 with formal proof (page 6)\"\n  resolution_round: 13\n\n- id: \"R10-N2\"\n  summary: \"κ→K_eff 映射理论基础不足——r=0.625 验证弱\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R16(fresh) R1-W7: K_eff exchangeable correlation假设可能被违反, minor concern\"\n\n- id: \"R10-N3\"\n  summary: \"Capability gap 'perfectly monotonic' 结论基于 n=6 非独立数据点\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 与R9-W3合并. 共识AGREE: n=6数据点不足以支撑'principle'\"\n\n- id: \"R10-W1\"\n  summary: \"DRC τ 阈值无 held-out 评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n\n- id: \"R10-W2\"\n  summary: \"Cross-architecture NLI escape 适用面极窄\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R1-W8+R2-W3共识: generalizability受限, 仅NLI-friendly数据集测试\"\n\n- id: \"R10-W3\"\n  summary: \"四种子复制方差大 + 统计功效 <21%\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R1-W3: multi-seed仅2/6模型, seed noise ±2.34pp超过多数|Δ|. R2 AGREE\"\n\n- id: \"R10-W4\"\n  summary: \"TOST ±2pp margin 缺少显式理由\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R16(fresh) R1-N2: ±2pp margin缺乏先验依据, 需sensitivity analysis. R2 AGREE\"\n\n- id: \"R10-W5\"\n  summary: \"Bias Ratio 无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"BR CI 已整合: Mistral [3.98,6.37], Qwen [2.44,7.11]\"\n  resolution_round: 10\n\n- id: \"R10-W6\"\n  summary: \"SatLM specification-generation vs SICA trace-extraction 对比不充分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n\n- id: \"R10-W7\"\n  summary: \"'Symbolic Confirmation Bias' 需与近期 CoT confirmation bias 工作区分\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R2-N1: SCB是Huang(2024)+Wan(2025)的自然延伸, R1部分REBUT(negative result value不应事后贬低, 但同意DPI部分近平凡). 部分共识: 贡献在empirical depth非conceptual novelty\"\n\n- id: \"R10-W8\"\n  summary: \"Related Work 过度压缩——引用列表而非文献讨论\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [2]\n      note: \"R16(fresh) R2-M5: §2段间逻辑衔接不够清晰\"\n\n- id: \"R10-I1\"\n  summary: \"'Symbolic Mirage' 概念新颖性——与 Huang/Wan 的 confirmation bias 区别\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 同R10-W7. R2: DPI是教科书推论, novelty在于识别正确的Markov chain而非DPI本身\"\n\n- id: \"R10-I2\"\n  summary: \"Independence-Accuracy Trade-off 作为独立贡献有 bias-variance 重述嫌疑\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n\n- id: \"R10-VL1\"\n  summary: \"主文缺结果可视化\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16 视觉审查: 主文5 display items(Figure 1-4 + Table 1-3), 合理\"\n\n- id: \"R11-N1\"\n  summary: \"Spearman ρ=1.0 (n=6) 被过度使用——有效自由度远低于6\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 与R9-W3合并. 共识: n=6 suggestive非definitive\"\n\n- id: \"R11-N2\"\n  summary: \"中心 claim 'SICA fails' 与统计功效不匹配——Abstract/title 过强\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 共识critical: R1-N2(power<21%, MDE≥1.86pp, ~79%概率检测不到2pp效果) + R2-W1(标题'Fail to Improve'overclaiming). R2 AGREE R1分析. 建议标题改为'Do Not Substantially Improve'或加power caveat\"\n  action_items:\n    - round: 16\n      action: \"标题软化 + Abstract加power caveat + TOST margin sensitivity analysis\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R11-N3\"\n  summary: \"TOST ±2pp margin 缺乏 principled 论证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R1-N2涵盖: ±2pp margin无先验依据, 需补充不同margin(±1/3/5pp)的TOST sensitivity\"\n\n- id: \"R11-W1\"\n  summary: \"DRC 评估不充分——仅PW完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n\n- id: \"R11-W2\"\n  summary: \"BR 指标存在循环论证倾向\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R2-N2 critical: BR>1部分是base-rate效应(60% traces→60%约束支持多数答案), 需permutation null model量化excess bias. R1 AGREE(审稿中未注意到此问题). 共识: BR循环论证不否定SCB整体论证(Table 11/degeneration condition/oracle独立支持), 但BR指标本身需null model或降级为描述性指标\"\n  action_items:\n    - round: 16\n      action: \"补充permutation-based null distribution, 或将BR降级为描述性指标并明确声明base-rate组成\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R11-W3\"\n  summary: \"术语过度品牌化——'Symbolic Mirage' 偏 dramatic\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n\n- id: \"R11-W4\"\n  summary: \"新颖性定位需更早更明确建立与先验工作的 distinction\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R2-N1+R2-W5: SCB是Huang et al.的自然延伸, 'extending'是overselling. R1部分REBUT: 机制定位+27策略否证+诊断框架是非平凡贡献, 但同意DPI部分近平凡\"\n\n- id: \"R11-W5\"\n  summary: \"Independence-Accuracy Trade-off 应定位为量化而非新发现\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n\n- id: \"R11-W6\"\n  summary: \"遗漏引用: Byerly & Khashabi (2026 TACL) 等\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"当前论文已引用 Byerly and Khashabi (2026)\"\n  resolution_round: 13\n\n- id: \"R11-W7\"\n  summary: \"27 策略计数膨胀 + 未尝试 trained constraint extractor\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R2-W4: 27策略局限于self-extraction paradigm内变体, claim scope需限定. R1部分REBUT: 策略确实跨多维度(prompt/method/cross-model/formal proof), 但同意应限定scope为'within constraint-extraction-aggregation paradigm'\"\n\n- id: \"R11-VL1\"\n  summary: \"主文缺结果可视化——需上提 Figure 到主文\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16 视觉审查: Figure 2(散点图p4), Figure 3(DAG p6), Figure 4(柱状图p7)已在主文, 覆盖合理\"\n\n- id: \"R12-N1\"\n  summary: \"标题 overclaiming about frontier scale\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 标题已含'Logical Reasoning'(非'LLM Reasoning'), 但'Fail to Improve'仍overclaiming given power<21%. 共识: 需进一步软化\"\n\n- id: \"R12-N2\"\n  summary: \"SCB 核心新颖性不足——self-correction failure 在 FOL 载体上的实例化\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R2-N1 critical: SCB=Huang+DPI, Wan(2025)/Jhaveri(2026)从不同角度得出类似结论. R1 partial REBUT: negative result不应事后贬低, 诊断框架+27策略否证有独立价值. 部分共识: 定位为'系统性量化'而非'发现', 弱化Prop 1呈现\"\n\n- id: \"R12-N3\"\n  summary: \"DRC 作为 Contribution 4 不够充分\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"DRC demoted to practical observation in §6\"\n  resolution_round: 13\n  first_raised_round: 12\n  last_seen_round: 13\n\n- id: \"R12-W1\"\n  summary: \"BR 可能存在循环论证——56.4%零变量重叠使约束按定义支持source answer\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 与R11-W2合并. R2-N2提升为critical: 需null model\"\n\n- id: \"R12-W2\"\n  summary: \"CIL 名称和 information-theoretic 声称有误导\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Renamed to CCR, removed 'unify' claim\"\n  resolution_round: 13\n  first_raised_round: 12\n  last_seen_round: 13\n\n- id: \"R12-W3\"\n  summary: \"Figure 2 placement——应在正文而非附录\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Figure 2 已在正文 page 4\"\n  resolution_round: 13\n\n- id: \"R12-W4\"\n  summary: \"Appendix vs 主文关键信息分配不合理\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [2]\n      note: \"R16(fresh) R2-M3: Abstract信息过载(6个要素). R2-M2: K_eff缺直觉解释\"\n\n- id: \"R12-EC1\"\n  summary: \"Extractor Confound——所有 frontier cross-model extraction 使用同一 Mistral-7B extractor\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n\n- id: \"R13-N1\"\n  summary: \"摘要 BR 4.97× 选择性报告——最极端条件\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) Abstract报告'at least 1.66×', 为最小值. 比报告4.97×更保守, 但BR循环论证问题(R11-W2)影响所有BR值的可信度\"\n\n- id: \"R13-N2\"\n  summary: \"统计功效呈现不足——10/16 underpowered, power analysis 埋在附录\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 与R11-N2合并. R1-N2 critical: observed power<21%, TOST仅8/16显著. R2 fully AGREE\"\n\n- id: \"R13-N3\"\n  summary: \"α=0.5 无敏感性分析\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R1-W6: α=0.5无理论依据, 需sensitivity analysis α∈{0,0.25,0.5,0.75,1.0}. R2 AGREE. 论文有Table 11(α ablation ≥99% agreement), 但R1/R2共识: ceiling effect不等于鲁棒性\"\n\n- id: \"R13-W1\"\n  summary: \"符号/指标过载——8页内7个定量工具\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n\n- id: \"R13-W2\"\n  summary: \"NLI claim 须限定到命题逻辑任务\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R16(fresh) R1-W9: 'First-order logic'描述轻微overselling, 99%约束是propositional level. R2 AGREE\"\n\n- id: \"R13-W3\"\n  summary: \"语法去重可能膨胀 BR——未报告语义去重后 BR\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n\n- id: \"R13-W4\"\n  summary: \"Symbolic Mirage Hypothesis §3.3 与 §5 验证不连贯\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及(当前论文无显式§3.3 Hypothesis section)\"\n\n- id: \"R13-W5\"\n  summary: \"缺引: Dhuliawala et al. 2023 Chain-of-Verification\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"已引用 dhuliawala2023chainofverification\"\n  resolution_round: 14\n\n- id: \"R14-N1\"\n  summary: \"标题'LLM Reasoning'范围超出实验证据——仅覆盖逻辑推理\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 标题已为'LLM Logical Reasoning', domain scope改善. 但'Fail to Improve'仍overclaiming\"\n\n- id: \"R14-N2\"\n  summary: \"Symbolic Mirage Hypothesis Predictions 1-2 为事后总结非独立预测\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 当前论文无显式Predictions标签, 未单独提及\"\n\n- id: \"R14-W1\"\n  summary: \"Cross-architecture实验仅6条件/单一verifier/仅Mistral-7B显著\"\n  category: experiment\n  severity: major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R1-W8+R2-W3共识: 仅Mistral-7B(SC=39.33%)显著, 'principle'过强, 降级为'preliminary observation'\"\n\n- id: \"R14-W2\"\n  summary: \"8页正文信息过载——§5.5/§6/§7展开不足\"\n  category: writing\n  severity: major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [2]\n      note: \"R16(fresh) R2-M3: Abstract信息过载(6要素). R2-M2: K_eff缺直觉解释. R2-M5: §2段间衔接不够\"\n\n- id: \"R14-W3\"\n  summary: \"'No evidence' claim scope与统计功效不匹配\"\n  category: framing\n  severity: major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 与R11-N2合并. 共识critical\"\n\n- id: \"R14-W4\"\n  summary: \"BR计算子集大小(n_err)未报告\"\n  category: experiment\n  severity: moderate\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R1-W4: Table 2多数条件未报CI. R2 AGREE. 当前论文Table 2已有n_err列但多数条件无CI\"\n\n- id: \"R14-W5\"\n  summary: \"Related Work遗漏: SETS(2025), MAV(2025)\"\n  category: writing\n  severity: minor-to-major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R2-W2新增: S²R(ACL 2025), DuPO(2025), Kamoi et al.(TACL 2024). R1部分REBUT(scope外)但同意应讨论理论边界\"\n\n- id: \"R14-W6\"\n  summary: \"Fleiss' κ→ICC近似仅r=0.625——prevalence paradox\"\n  category: method\n  severity: moderate\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R16(fresh) R1-W7: K_eff exchangeability假设可能被违反, 但minor, 不影响核心结论\"\n\n# R15(fresh) issues\n\n- id: \"R15-M1\"\n  summary: \"遗漏引用: DuPO (ICLR 2026) — training-based self-verification\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"共识AGREE\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R2-W2提出, R1部分REBUT(scope外但应讨论理论边界)\"\n\n- id: \"R15-M2\"\n  summary: \"遗漏引用: S²R (2025) — RL-based self-verification\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"共识AGREE\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R2-W2提出, R1部分REBUT(scope外但应讨论理论边界)\"\n\n- id: \"R15-M3\"\n  summary: \"遗漏引用: LLM as Formalizers on CSP (arXiv 2505.13252, 2025)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n\n- id: \"R15-M4\"\n  summary: \"遗漏引用: Lakshminarayanan et al. (2017) Deep Ensembles\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R16(fresh) R1 REBUT: Kuncheva & Whitaker(2003)和Ladha(1992)已更直接相关. Minor\"\n\n- id: \"R15-W1\"\n  summary: \"α=0.5敏感性分析≥99% agreement是ceiling effect\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R1-W6要求补充α sensitivity analysis. R2 AGREE. 共识: ceiling effect不等于鲁棒性\"\n\n# R16(fresh) 新发现\n\n- id: \"R16-N1\"\n  summary: \"Proposition 1 证明范围与声称范围不匹配——Part(i)仅对source-attribution成立但标题claim 'structural'\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R1-N1 critical, R2 fully AGREE. 共识: Part(i)依赖SICA特定的source attribution scoring(Eq.3), 非数学必然; Part(ii) DPI是平凡推论(I(C;Y)≤I(T;Y)). 建议拆分为两个结果, 明确区分适用范围. R2补充: DPI不排除约束通过重新组织信息打破相关模式\"\n  action_items:\n    - round: 16\n      action: \"将Proposition 1分为source-attribution退化定理(精确但specific) + DPI bound(普遍但弱), 正文明确区分\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R16-N2\"\n  summary: \"Diagnostics 100%准确率是in-sample评估——overfitting风险, holdout验证不充分\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-N3 critical, R1 fully AGREE(审稿中未注意到). 共识: (1) 决策边界从60条件推导并在同一60条件上评估=in-sample fitting; (2) holdout仅LLaMA-3.1-8B×FOLIO 1个条件=不充分; (3) 60条件全为negative cases, 任何trivial classifier('永远预测不帮助')都能100%; (4) 未在positive cases(cross-arch escape, oracle)上验证. Abstract/§1/§7中此claim为三大贡献之一, 过度表述\"\n  action_items:\n    - round: 16\n      action: \"增加held-out model family验证 + 弱化claim为'correctly classify all tested conditions within experimental scope' + 讨论OOD失败条件\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R16-M1\"\n  summary: \"遗漏引用: Kamoi et al. (TACL 2024) self-correction survey\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2提出, R1 AGREE. self-correction方向最全面survey, 应引用定位论文\"\n\n- id: \"R16-M2\"\n  summary: \"遗漏引用: AlphaCode/CodeT — constraint verification in code domain\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R1提出: code domain中约束过滤成功案例, 可对比讨论为何逻辑推理领域失败\"\n\n- id: \"R16-W1\"\n  summary: \"'Extending Huang et al. (2024) to formal verification' 是overselling——两者证明框架不同不构成逻辑extension\"\n  category: framing\n  severity: major\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W5, R1 fully AGREE. 共识: Huang基于value/policy iteration, 本文基于DPI+source attribution, 形式化框架不同. 建议改为'consistent with / complement / provide independent evidence for'\"\n  action_items:\n    - round: 16\n      action: \"§1和Abstract将'extend'改为'provide independent evidence consistent with'\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R16-W2\"\n  summary: \"GSM8K(n=30)/AIME(n=22)样本量过小, 不应与大样本条件等权重引用\"\n  category: experiment\n  severity: major\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R1-W5, R2 AGREE. 论文已标注为'exploratory, n<60'(Table 1 caption), 但正文§5.3引用时未区分\"\n\n- id: \"R16-W3\"\n  summary: \"缺少training-based self-verification方法讨论——Proposition 1理论边界不完整\"\n  category: writing\n  severity: major\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W2 major, R1部分REBUT(scope已限定为training-free, §7提及trained extractors)但AGREE应讨论训练如何通过违反A2打破信息上限. 共识: §2增加一段training-based self-verification, 明确Prop 1适用边界\"\n  action_items:\n    - round: 16\n      action: \"§2增加training-based self-verification段落, 引用S²R/DuPO, 明确Prop 1仅适用于inference-time same-model\"\n      assigned_to: \"paper_agent\"\n      status: open\n"
  }
}
```

</details>

---


### Tool result

_source line 1703 · 2026-05-23T08:24:03.984289+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml\", \"bytes\": 24393}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1704 · 2026-05-23T08:27:17.171250+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "symb_invariant_consensus",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0",
  "report": "# 审稿报告 — Round 16 (Fresh)\n\n**论文**: Beyond Self-Consistency: Why Self-Extracted Constraints Fail to Improve LLM Logical Reasoning\n**Venue**: EMNLP 2026 ARR\n**审稿模式**: Fresh（重新审稿，无上轮记忆）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+Related Work+写作质量+Claims合理性）\n**交叉轮次**: 1 轮交叉分享 + 逐条 [AGREE]/[REBUT] 回应，关键问题已收敛\n\n---\n\n## Summary\n\n本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM chain-of-thought traces 中提取一阶逻辑约束，经去重后用 weighted partial MAX-SAT（Z3 求解）选择答案。核心发现为 null result：尽管 Z3 验证 99% 的自提取约束有效，SICA 在 6 个模型（7B–32B）、3 个推理数据集上与 majority voting 结果几乎一致（94.4% 问题答案相同），FDR 校正后无显著正效应。论文提出\"Symbolic Confirmation Bias\"概念（自提取约束系统性偏向模型多数答案），通过 Proposition 1（source-attribution 退化 + DPI information ceiling）给出理论论证，测试 27 种 training-free 修复策略均失败，并初步探索 cross-architecture NLI 验证作为突破路径。\n\n---\n\n## Strengths\n\n**S1. 实验规模和系统性达到顶会标准。** 9 个模型 × 3 个数据集 × 60 个非退化条件 × 27 种修复策略的实验矩阵，附录 18 页包含详尽的 ablation（K sensitivity、temperature、multi-seed、oracle、error taxonomy、constraint ablation、entropy decomposition）。这种彻底性对 negative result paper 至关重要。[共识]\n\n**S2. Oracle 控制实验设计精巧。** 用 gold FOL annotations 替换自提取约束后，FOLIO 上获得 +29.90/+13.73pp 的显著提升（Mistral-7B/Qwen2.5-14B），精确分离方法论有效性与提取质量，定位瓶颈在 extraction 而非 verification/aggregation。[共识]\n\n**S3. 统计方法论多层次且诚实。** McNemar exact test + BH FDR 校正、bootstrap 95% CI（Table 7）、power analysis（Appendix D）、TOST equivalence test（Appendix U）、shuffle control（§5.1）。明确报告 observed power < 21%，承认 \"absence of evidence is not evidence of absence\"。这种统计诚实性在 NLP 社区中少见。[共识]\n\n**S4. 诊断框架有潜在实用价值。** 三个 zero-cost diagnostics（C₀, K_eff, BR）从 K=12 pilot run 即可预测 trace-aggregation 方法是否有帮助，为实践者提供部署前筛选工具。Table 5 的 per-condition diagnostics 具体可操作。[共识，但泛化性存疑——见 W3]\n\n**S5. Cross-architecture escape 提供建设性方向。** 不仅报告负面结果，还识别了 capability-gap 条件下 DeBERTa verifier 的显著提升路径（Mistral-7B 上 +6.67pp, p < 0.001），domain-adapted fine-tuning 进一步放大至 +12.67pp。[共识]\n\n**S6. 附录极为详尽，可复现性强。** Prompt 模板（Appendix A）、MAX-SAT 伪代码（Appendix B）、完整 per-condition 结果、子群分析等 25 个 appendix sections。[共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**W1 [Critical] Proposition 1 证明范围与声称范围不匹配 [共识]**\n- **位置**: §5.1, page 6, Proposition 1 及证明\n- **问题**: Proposition 1 标题 \"Symbolic Confirmation Bias is Structural\" 暗示普遍性，但证明由两部分组成：\n  - Part (i) voting degeneration 依赖 SICA 特定的 source attribution scoring (Eq. 3)。如果用逻辑一致性（而非来源归属）对约束打分，Part (i) 不一定成立。论文 Remark 承认但未反映在 Proposition 表述中。\n  - Part (ii) information ceiling 是 data processing inequality 的直接应用（I(C;Y) ≤ I(T;Y)），数学正确但平凡——只证明约束不能比 traces 包含更多信息，不排除约束通过重新组织信息打破相关模式。\n- **Reviewer 共识**: R1 首提（N1 critical），R2 fully AGREE 并补充 DPI 部分是教科书推论。两者互补：R1 指出 validity/scope 问题，R2 指出 significance/novelty 问题。\n- **修改建议**: 拆分为 (a) source-attribution 下的退化定理（精确但 SICA-specific）和 (b) DPI bound（普遍但弱）；正文明确区分两者适用范围。\n\n**W2 [Critical] 统计功效 < 21% 与 negative claim 强度不匹配 [共识]**\n- **位置**: Title, Abstract, §4, Appendix D\n- **问题**: \n  - Observed power < 21%，MDE ≥ 1.86pp（最大样本条件）。即使 SICA 有 2pp 真实效果，~79% 概率无法检测。\n  - TOST equivalence test 仅 8/16 条件达到等价显著，6 条件 underpowered，2 条件 genuinely different (negative)。±2pp equivalence margin 缺乏先验理论依据。\n  - Bootstrap 95% CI（Table 7）全部包含零，宽度约 ±1.5pp。\n  - 标题 \"Fail to Improve\" 是无条件否定声明，但论文无法排除 1-2pp 量级的正效应。\n- **Reviewer 共识**: R1-N2 critical + R2-W1 major，交叉后 R2 fully AGREE R1 的详细分析。\n- **修改建议**: (a) 标题软化（如 \"Do Not Substantially Improve\"）；(b) Abstract 加 power caveat；(c) 补充 TOST margin sensitivity analysis（±1/3/5pp）。\n\n**W3 [Critical] Diagnostics 100% 准确率是 in-sample 评估——overfitting 风险 [共识]**\n- **位置**: §5.3, §1 contributions, §7 conclusion, Abstract\n- **问题**: \n  - 决策边界（C₀ < 5%, K_eff ≤ 1.30, SC < 40%）从 60 个条件推导，并在同一 60 个条件上评估 → in-sample fitting。\n  - 60 个条件全为 negative cases，任何 trivial classifier（\"永远预测不帮助\"）都能 100%。\n  - \"Holdout\" 验证仅 LLaMA-3.1-8B on FOLIO 1 个条件 → 不构成充分 OOD 验证。\n  - 未在 positive cases（cross-architecture escape, oracle）上验证诊断框架能否正确预测\"会帮助\"。\n- **Reviewer 共识**: R2-N3 critical，R1 fully AGREE（承认初审疏漏）。\n- **修改建议**: (a) 增加完整的 held-out model family；(b) 弱化 claim 为 \"correctly classify all tested conditions within our experimental scope\"；(c) 讨论 OOD 失败条件。\n\n**W4 [Critical] BR 指标存在循环论证风险——缺乏 null model [共识]**\n- **位置**: §3.1 (Eq. 5), §5.1, Table 2\n- **问题**: \n  - BR 通过 source attribution 衡量约束是否偏向支持多数答案。但约束从产生答案的 trace 中提取——如果 60% traces 产生答案 A，提取的约束自然更多支持 A（base-rate 效应）。\n  - 论文未建立 null model：如果约束提取完全\"无偏\"（support 比例精确反映 trace 投票分布），BR 期望值是多少？只有观测 BR 显著超过 null expectation 才能声称\"额外的\" confirmation bias。\n  - Shuffle control（§5.1, p.5: BR_shuffle ≈ BR_obs）确认 BR 主要反映 trace-count 分布而非提取特异性——但论文措辞混淆这两个组成部分。\n- **Reviewer 共识**: R2-N2 critical，R1 fully AGREE（初审未注意此问题），但共识补充：BR 循环论证不否定 SCB 整体论证（Table 11、degeneration condition、oracle 独立支持），只影响 BR 指标本身的概念有效性。\n- **修改建议**: (a) 构建 permutation-based null distribution；(b) 或将 BR 降级为描述性指标，明确声明 base-rate 组成。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W5 [Major] 新颖性定位——SCB 是已知结论的实证深化而非概念突破 [部分共识]**\n- **位置**: §1 contributions, §5 \"The Symbolic Mirage\", Abstract\n- **问题**: \n  - Huang et al. (2024) 已建立 \"LLMs cannot self-correct without external feedback\"。SCB 将此延伸到形式化约束自验证——可预见但不平凡。\n  - Wan et al. (2025, ACL Findings) 已从认知心理学角度证明 CoT 推理中存在 confirmation bias。SCB 底层机制（model beliefs dominate downstream processing）高度重叠。\n  - Proposition 1 Part (ii) 是 DPI 的教科书应用。\n- **Reviewer 分歧**: R2 认为 critical（可预见的延伸），R1 partial REBUT（negative result 不应事后贬低；诊断框架 + 27 策略否证 + 机制定位是非平凡贡献）。\n- **最终判定**: 部分共识——两者同意定位应从\"发现\"转为\"系统性量化\"，弱化 Proposition 1 呈现权重。R1 的反驳有一定道理：negative result paper 的价值在于提供系统性证据，不应仅因\"可预见\"而否定。\n\n**W6 [Major] \"Extending Huang et al. (2024) to formal verification\" 是 overselling [共识]**\n- **位置**: Abstract, §1 contribution 1, §5.1\n- **问题**: Huang et al. 基于 value/policy iteration 分析 self-correction，本文基于 DPI + source attribution 分析 self-verification。形式化框架、假设条件和证明技术完全不同，不构成逻辑 extension。\n- **修改建议**: 改为 \"consistent with / complement / provide independent evidence for\"。\n\n**W7 [Major] 缺少 training-based self-verification 方法讨论 [部分共识]**\n- **位置**: §2 Related Work, §7 Discussion\n- **问题**: 论文几乎未讨论 S²R (Zeng et al., ACL 2025)、DuPO (2025) 等 training-based 方法。这些方法通过训练引入外部奖励信号，理论上可通过违反 Proposition 1 的 A2 假设（约束不再 trace-determined）打破信息上限。\n- **Reviewer 分歧**: R2 认为 major missing，R1 partial REBUT（论文 scope 已限定为 training-free，§7 提及 trained extractors），但 R1 同意应讨论理论边界。\n- **修改建议**: §2 增加一段 training-based self-verification，引用 S²R/DuPO，明确 Proposition 1 仅适用于 inference-time same-model extraction。\n\n**W8 [Major] Multi-seed replication 不充分 [共识]**\n- **位置**: Appendix X.1, Table 33\n- **问题**: 仅 Mistral-7B (3 seeds) 和 Qwen2.5-14B (4 seeds) 做了 multi-seed replication。Seed-level noise ≈ ±2.34pp，而 Table 1 大部分条件 |Δ| < 3pp 且为 single-seed。许多观测效应可能完全由 seed variance 解释。\n- **修改建议**: 至少对效应最大的条件补充 multi-seed，或在 Limitations 明确讨论 single-seed 局限。\n\n**W9 [Major] Capability-gap principle 基于 n=6 条件——不足以支撑 \"principle\" 级别 claim [共识]**\n- **位置**: §6 \"Escaping the Bottleneck\", Table 3, Figure 8\n- **问题**: 仅约 6 个 verifier-generator 组合，Table 3 仅 Mistral-7B (SC=39.33%) 1 个条件显著。§6 标题 \"Escaping the Bottleneck\" 语气过强。\n- **修改建议**: 降级为 \"preliminary observation\" 或 \"hypothesis\"。\n\n**W10 [Major] \"27 strategies fail\" scope 不匹配 [部分共识]**\n- **位置**: §5.2, Table 14, Abstract\n- **问题**: 27 个策略局限于 self-extraction paradigm 内的变体（prompt-level + method-level + cross-model），不等于所有 training-free 方法都失败。\n- **Reviewer 分歧**: R2 认为 scope 过宽，R1 partial REBUT（策略确实跨多个独立维度），但 R1 同意应限定 claim scope。\n- **修改建议**: 限定为 \"27 training-free variants within the constraint-extraction-aggregation paradigm\"。\n\n### Minor 问题（不影响接收）\n\n**M1** [Minor] α = 0.5 缺乏理论依据和真正的 sensitivity analysis。Table 11 的 ≥99% agreement 是 ceiling effect（主效应近零时 penalty 项影响自然可忽略），非真正鲁棒性。[共识]\n\n**M2** [Minor] \"First-order logic\" 描述轻微 overselling——99% 约束是 propositional level at Z3，仅 1.06% 使用真正量词。[共识]\n\n**M3** [Minor] Figure 1 信息密度偏高；K_eff 缺乏直觉解释；Abstract 信息过载（6 个要素）。[R2 提出]\n\n**M4** [Minor] §2 Related Work 段间逻辑衔接可改善——建议构建从 majority voting → self-correction → formal verification → this paper 的叙事线。[R2 提出]\n\n**M5** [Minor] GSM8K (n=30) 和 AIME (n=22) 样本量过小，不应与大样本条件等权重引用。论文已标注 \"exploratory\"（Table 1 caption），但正文 §5.3 引用时未区分。[共识]\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** Proposition 1 Part (i) 依赖 source attribution scoring。如果使用 source-agnostic scoring（基于逻辑一致性而非来源归属评估约束-答案关系），是否仍会退化？是否测试过 source-agnostic alternatives？\n\n**Q2.** BR 的 null expectation 是什么？如果约束提取完全\"无偏\"（support 比例精确反映 trace 投票分布），BR 期望值是否恰好为 1？请提供 permutation test 或 null model 分析。\n\n**Q3.** Diagnostics 的决策边界在 positive cases（cross-architecture escape, oracle）上是否能正确预测\"SICA 会帮助\"？\n\n**Q4.** TOST ±2pp equivalence margin 如何选择？如果 margin 放宽至 ±3pp 或 ±5pp，有多少额外条件达到等价显著？\n\n**Q5.** Table 1 中 |Δ| < 3pp 的所有 single-seed 条件，作者是否承认这些差异可能完全由 seed variance 解释（given seed noise ≈ ±2.34pp）？\n\n**Q6.** Cross-architecture NLI 验证仅在 NLI-friendly 数据集（FOLIO, ProofWriter）上测试。对非 NLI 格式推理任务是否适用？\n\n---\n\n## Missing References\n\n1. **Kamoi et al. (TACL 2024)**: \"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\" — self-correction 方向最全面 survey。[R2 提出，R1 AGREE]\n2. **S²R (Zeng et al., ACL 2025)**: RL-based self-verification，通过训练打破 Proposition 1 信息上限。[R2 提出，R1 同意应讨论理论边界]\n3. **DuPO (arXiv 2508.14460, 2025)**: Dual preference optimization self-verification。[R2 提出，R1 同意应讨论理论边界]\n4. **AlphaCode / CodeT**: Constraint verification in code domain 的成功案例，可对比讨论为何逻辑推理领域失败。[R1 提出，Minor]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: ✅ 完成（耗时 ~4 分钟）\n\n**统计**: 0 critical, 1 warning, 24 info\n\n**Warning**:\n- Page 7, Figure 4: 柱状图底部 x 轴策略名称字号偏小，27 个 bar 密度高，灰度打印时 4 种颜色区分度可能下降。建议增加 marker pattern 或 hatching。\n\n**Info 要点**:\n- Figure 1 (p.2) pipeline 图 caption 自包含，Title-Abstract-Figure 1 narrative 一致，第一印象良好\n- 所有 Figure/Table 出现在首次引用附近，无 float 漂移\n- 表格一致使用 booktabs 风格，最优值加粗，显著性标记有脚注说明\n- 公式渲染正确，无 LaTeX 错误残留或未解析引用\n- Limitations section 在 page 8 底部延伸至 page 9，符合 EMNLP 2026 规定\n- 参考文献约 2.5 页，格式统一\n\n**总体**: 排版质量良好，无严重视觉问题。\n\n---\n\n## Reviewer Consensus\n\n### 完全共识（14 项 AGREE）\n1. Proposition 1 scope mismatch（Part (i) SICA-specific，标题 claim \"structural\"）\n2. 统计功效 < 21% 与 negative claim 强度不匹配\n3. 标题 \"Fail to Improve\" overclaiming\n4. BR 循环论证风险（base-rate 效应未排除）\n5. Diagnostics in-sample overfitting（100% 准确率无意义）\n6. Multi-seed replication 不充分（2/6 模型）\n7. BR 小 n_err 条件缺 CI\n8. α = 0.5 sensitivity analysis 不充分\n9. Capability-gap principle n=6 不足以支撑 \"principle\"\n10. \"Extending Huang et al.\" 是 overselling\n11. GSM8K/AIME 样本量过小\n12. K_eff exchangeability 假设局限\n13. Cross-architecture generalizability 受限\n14. \"First-order logic\" 轻微 overselling\n\n### 部分分歧（3 项 partial REBUT，已记录各方理由）\n1. **新颖性**: R2 认为核心洞察可预见（Huang + DPI 延伸），R1 认为不应事后贬低 negative result 且诊断框架/27 策略有独立价值 → 共识：定位为\"系统性量化\"而非\"发现\"\n2. **Training-based refs**: R2 认为 major missing，R1 认为 scope 外但同意讨论理论边界\n3. **\"27 strategies\" scope**: R1 指出策略跨多维度，但同意应限定 claim scope\n\n---\n\n## Overall Assessment\n\n### 评分汇总\n\n| 维度 | R1 | R2 (交叉后修正) | 加权综合 |\n|------|-----|----------------|---------|\n| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |\n| Excitement | 3.0–3.5/5 | 2.5/5 | 3.0/5 |\n| Reproducibility | 4.0/5 | 4.0/5 | 4.0/5 |\n| Overall | 3.5 | 3.0 | **3.0** |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n### Overall: 3.0 — Findings\n\n**一句话总结**: 实验执行出色的 negative result paper，但核心理论贡献（Proposition 1）证明与声称范围不匹配、统计功效不足以支撑标题级 claim、诊断框架泛化性未验证、BR 指标概念有效性存疑，且新颖性有限（SCB 是已知结论的实证深化）。\n\n**详细理由**:\n\n*支持接收的因素*: (1) 实验规模大（9 模型 × 3 数据集 × 60 条件 × 27 策略），远超同类工作；(2) 统计方法论多层次且诚实（McNemar + BH + TOST + bootstrap + power analysis + shuffle control）；(3) Oracle 控制实验精巧，精确分离提取质量与方法论有效性；(4) 诊断框架有潜在实用价值；(5) Cross-architecture escape 提供建设性方向；(6) 附录极为详尽（18 页），可复现性强。作为 Findings 论文，对社区有实际指导价值——帮助避免在 self-extracted constraint verification 方向上的无效探索。\n\n*限制接收为 Conference 的因素*: (1) Proposition 1 的 scope mismatch 使核心理论贡献被削弱——Part (i) 仅对 source-attribution 成立，Part (ii) 是平凡 DPI 推论；(2) 21% 的统计功效使 \"fail to improve\" 的标题级 claim 无法被统计证据充分支撑；(3) Diagnostics 的 100% 准确率是 in-sample 评估，holdout 验证不充分，这是论文三大贡献之一；(4) BR 作为 SCB 的量化基础存在循环论证风险（base-rate 效应未排除），需要 null model 才能确定\"额外 bias\"的存在；(5) 新颖性有限——核心洞察（自提取约束继承模型 bias）是 Huang et al. (2024) + Wan et al. (2025) 已知结论在形式化验证管道中的实证深化。\n\n*如果以下问题得到解决，评分可提升至 3.5（Borderline Conference）*:\n1. 标题软化 + Abstract 加 power caveat + TOST margin sensitivity\n2. Proposition 1 拆分并明确 scope\n3. BR 提供 permutation null model 或降级为描述性指标\n4. Diagnostics 增加 held-out model family 验证并弱化 claim\n5. §2 补充 training-based self-verification 讨论\n6. \"Extending Huang et al.\" 改为 \"consistent with / provide independent evidence for\"\n\n---\n\n## Detailed Comments（逐节）\n\n**Title**: \"Fail to Improve\" 过于绝对，与 power < 21% 不匹配。建议 \"Do Not Substantially Improve\" 或 \"The Limits of Self-Extracted Constraints for\"。\n\n**Abstract**: 信息密度高但覆盖完整。需加 power caveat（如 \"though underpowered for effects below ~2pp\"）。\"extends the self-correction impossibility of Huang et al.\" 改为 \"provides independent evidence consistent with\"。BR 报告 \"at least 1.66×\" 应注明 base-rate 组成未排除。\n\n**§1 Introduction**: Contribution 2（diagnostics 100% 准确率）需加 scope 限定。Contribution 3 \"capability-gap principle\" 降级为 \"preliminary observation\"。\n\n**§2 Related Work**: 缺 training-based self-verification 讨论（S²R, DuPO）。缺 Kamoi et al. (TACL 2024) self-correction survey。段间逻辑衔接可改善。\n\n**§3 Method**: α = 0.5 缺理论依据。K_eff 缺直觉解释。BR 定义（Eq. 5）需声明 base-rate 效应。\n\n**§4 Results**: 统计诚实（报告 power 局限），但 claim 强度与证据强度仍有 gap。Single-seed 条件应标注不确定性。\n\n**§5.1 Symbolic Confirmation Bias**: Proposition 1 需拆分。BR > 1 的解读需 null model。Table 11 的 ≥99% agreement 应加 ceiling effect caveat。\n\n**§5.2 Why Remediation Fails**: 27 策略 claim scope 应限定为 \"within constraint-extraction-aggregation paradigm\"。\n\n**§5.3 Diagnostic Framework**: 100% 准确率 claim 需大幅弱化。增加 OOD 验证。讨论 positive case 预测能力。\n\n**§6 Escaping the Bottleneck**: 标题过强。\"Capability-gap principle\" → \"preliminary observation\"。仅 1 个条件显著。\n\n**§7 Discussion and Conclusion**: \"extending... to formal verification\" 改措辞。Future work 应明确 training-based methods 如何 escape Proposition 1。\n\n**Limitations**: 长度合规（EMNLP 2026 规定\"一小段覆盖 3 个点\"），覆盖了关键局限（open-source only, English only, logical reasoning only）。可考虑增加 power limitation 的一句话提及。\n"
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
    "overall_score": "3.0",
    "report": "# 审稿报告 — Round 16 (Fresh)\n\n**论文**: Beyond Self-Consistency: Why Self-Extracted Constraints Fail to Improve LLM Logical Reasoning\n**Venue**: EMNLP 2026 ARR\n**审稿模式**: Fresh（重新审稿，无上轮记忆）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+Related Work+写作质量+Claims合理性）\n**交叉轮次**: 1 轮交叉分享 + 逐条 [AGREE]/[REBUT] 回应，关键问题已收敛\n\n---\n\n## Summary\n\n本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM chain-of-thought traces 中提取一阶逻辑约束，经去重后用 weighted partial MAX-SAT（Z3 求解）选择答案。核心发现为 null result：尽管 Z3 验证 99% 的自提取约束有效，SICA 在 6 个模型（7B–32B）、3 个推理数据集上与 majority voting 结果几乎一致（94.4% 问题答案相同），FDR 校正后无显著正效应。论文提出\"Symbolic Confirmation Bias\"概念（自提取约束系统性偏向模型多数答案），通过 Proposition 1（source-attribution 退化 + DPI information ceiling）给出理论论证，测试 27 种 training-free 修复策略均失败，并初步探索 cross-architecture NLI 验证作为突破路径。\n\n---\n\n## Strengths\n\n**S1. 实验规模和系统性达到顶会标准。** 9 个模型 × 3 个数据集 × 60 个非退化条件 × 27 种修复策略的实验矩阵，附录 18 页包含详尽的 ablation（K sensitivity、temperature、multi-seed、oracle、error taxonomy、constraint ablation、entropy decomposition）。这种彻底性对 negative result paper 至关重要。[共识]\n\n**S2. Oracle 控制实验设计精巧。** 用 gold FOL annotations 替换自提取约束后，FOLIO 上获得 +29.90/+13.73pp 的显著提升（Mistral-7B/Qwen2.5-14B），精确分离方法论有效性与提取质量，定位瓶颈在 extraction 而非 verification/aggregation。[共识]\n\n**S3. 统计方法论多层次且诚实。** McNemar exact test + BH FDR 校正、bootstrap 95% CI（Table 7）、power analysis（Appendix D）、TOST equivalence test（Appendix U）、shuffle control（§5.1）。明确报告 observed power < 21%，承认 \"absence of evidence is not evidence of absence\"。这种统计诚实性在 NLP 社区中少见。[共识]\n\n**S4. 诊断框架有潜在实用价值。** 三个 zero-cost diagnostics（C₀, K_eff, BR）从 K=12 pilot run 即可预测 trace-aggregation 方法是否有帮助，为实践者提供部署前筛选工具。Table 5 的 per-condition diagnostics 具体可操作。[共识，但泛化性存疑——见 W3]\n\n**S5. Cross-architecture escape 提供建设性方向。** 不仅报告负面结果，还识别了 capability-gap 条件下 DeBERTa verifier 的显著提升路径（Mistral-7B 上 +6.67pp, p < 0.001），domain-adapted fine-tuning 进一步放大至 +12.67pp。[共识]\n\n**S6. 附录极为详尽，可复现性强。** Prompt 模板（Appendix A）、MAX-SAT 伪代码（Appendix B）、完整 per-condition 结果、子群分析等 25 个 appendix sections。[共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**W1 [Critical] Proposition 1 证明范围与声称范围不匹配 [共识]**\n- **位置**: §5.1, page 6, Proposition 1 及证明\n- **问题**: Proposition 1 标题 \"Symbolic Confirmation Bias is Structural\" 暗示普遍性，但证明由两部分组成：\n  - Part (i) voting degeneration 依赖 SICA 特定的 source attribution scoring (Eq. 3)。如果用逻辑一致性（而非来源归属）对约束打分，Part (i) 不一定成立。论文 Remark 承认但未反映在 Proposition 表述中。\n  - Part (ii) information ceiling 是 data processing inequality 的直接应用（I(C;Y) ≤ I(T;Y)），数学正确但平凡——只证明约束不能比 traces 包含更多信息，不排除约束通过重新组织信息打破相关模式。\n- **Reviewer 共识**: R1 首提（N1 critical），R2 fully AGREE 并补充 DPI 部分是教科书推论。两者互补：R1 指出 validity/scope 问题，R2 指出 significance/novelty 问题。\n- **修改建议**: 拆分为 (a) source-attribution 下的退化定理（精确但 SICA-specific）和 (b) DPI bound（普遍但弱）；正文明确区分两者适用范围。\n\n**W2 [Critical] 统计功效 < 21% 与 negative claim 强度不匹配 [共识]**\n- **位置**: Title, Abstract, §4, Appendix D\n- **问题**: \n  - Observed power < 21%，MDE ≥ 1.86pp（最大样本条件）。即使 SICA 有 2pp 真实效果，~79% 概率无法检测。\n  - TOST equivalence test 仅 8/16 条件达到等价显著，6 条件 underpowered，2 条件 genuinely different (negative)。±2pp equivalence margin 缺乏先验理论依据。\n  - Bootstrap 95% CI（Table 7）全部包含零，宽度约 ±1.5pp。\n  - 标题 \"Fail to Improve\" 是无条件否定声明，但论文无法排除 1-2pp 量级的正效应。\n- **Reviewer 共识**: R1-N2 critical + R2-W1 major，交叉后 R2 fully AGREE R1 的详细分析。\n- **修改建议**: (a) 标题软化（如 \"Do Not Substantially Improve\"）；(b) Abstract 加 power caveat；(c) 补充 TOST margin sensitivity analysis（±1/3/5pp）。\n\n**W3 [Critical] Diagnostics 100% 准确率是 in-sample 评估——overfitting 风险 [共识]**\n- **位置**: §5.3, §1 contributions, §7 conclusion, Abstract\n- **问题**: \n  - 决策边界（C₀ < 5%, K_eff ≤ 1.30, SC < 40%）从 60 个条件推导，并在同一 60 个条件上评估 → in-sample fitting。\n  - 60 个条件全为 negative cases，任何 trivial classifier（\"永远预测不帮助\"）都能 100%。\n  - \"Holdout\" 验证仅 LLaMA-3.1-8B on FOLIO 1 个条件 → 不构成充分 OOD 验证。\n  - 未在 positive cases（cross-architecture escape, oracle）上验证诊断框架能否正确预测\"会帮助\"。\n- **Reviewer 共识**: R2-N3 critical，R1 fully AGREE（承认初审疏漏）。\n- **修改建议**: (a) 增加完整的 held-out model family；(b) 弱化 claim 为 \"correctly classify all tested conditions within our experimental scope\"；(c) 讨论 OOD 失败条件。\n\n**W4 [Critical] BR 指标存在循环论证风险——缺乏 null model [共识]**\n- **位置**: §3.1 (Eq. 5), §5.1, Table 2\n- **问题**: \n  - BR 通过 source attribution 衡量约束是否偏向支持多数答案。但约束从产生答案的 trace 中提取——如果 60% traces 产生答案 A，提取的约束自然更多支持 A（base-rate 效应）。\n  - 论文未建立 null model：如果约束提取完全\"无偏\"（support 比例精确反映 trace 投票分布），BR 期望值是多少？只有观测 BR 显著超过 null expectation 才能声称\"额外的\" confirmation bias。\n  - Shuffle control（§5.1, p.5: BR_shuffle ≈ BR_obs）确认 BR 主要反映 trace-count 分布而非提取特异性——但论文措辞混淆这两个组成部分。\n- **Reviewer 共识**: R2-N2 critical，R1 fully AGREE（初审未注意此问题），但共识补充：BR 循环论证不否定 SCB 整体论证（Table 11、degeneration condition、oracle 独立支持），只影响 BR 指标本身的概念有效性。\n- **修改建议**: (a) 构建 permutation-based null distribution；(b) 或将 BR 降级为描述性指标，明确声明 base-rate 组成。\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W5 [Major] 新颖性定位——SCB 是已知结论的实证深化而非概念突破 [部分共识]**\n- **位置**: §1 contributions, §5 \"The Symbolic Mirage\", Abstract\n- **问题**: \n  - Huang et al. (2024) 已建立 \"LLMs cannot self-correct without external feedback\"。SCB 将此延伸到形式化约束自验证——可预见但不平凡。\n  - Wan et al. (2025, ACL Findings) 已从认知心理学角度证明 CoT 推理中存在 confirmation bias。SCB 底层机制（model beliefs dominate downstream processing）高度重叠。\n  - Proposition 1 Part (ii) 是 DPI 的教科书应用。\n- **Reviewer 分歧**: R2 认为 critical（可预见的延伸），R1 partial REBUT（negative result 不应事后贬低；诊断框架 + 27 策略否证 + 机制定位是非平凡贡献）。\n- **最终判定**: 部分共识——两者同意定位应从\"发现\"转为\"系统性量化\"，弱化 Proposition 1 呈现权重。R1 的反驳有一定道理：negative result paper 的价值在于提供系统性证据，不应仅因\"可预见\"而否定。\n\n**W6 [Major] \"Extending Huang et al. (2024) to formal verification\" 是 overselling [共识]**\n- **位置**: Abstract, §1 contribution 1, §5.1\n- **问题**: Huang et al. 基于 value/policy iteration 分析 self-correction，本文基于 DPI + source attribution 分析 self-verification。形式化框架、假设条件和证明技术完全不同，不构成逻辑 extension。\n- **修改建议**: 改为 \"consistent with / complement / provide independent evidence for\"。\n\n**W7 [Major] 缺少 training-based self-verification 方法讨论 [部分共识]**\n- **位置**: §2 Related Work, §7 Discussion\n- **问题**: 论文几乎未讨论 S²R (Zeng et al., ACL 2025)、DuPO (2025) 等 training-based 方法。这些方法通过训练引入外部奖励信号，理论上可通过违反 Proposition 1 的 A2 假设（约束不再 trace-determined）打破信息上限。\n- **Reviewer 分歧**: R2 认为 major missing，R1 partial REBUT（论文 scope 已限定为 training-free，§7 提及 trained extractors），但 R1 同意应讨论理论边界。\n- **修改建议**: §2 增加一段 training-based self-verification，引用 S²R/DuPO，明确 Proposition 1 仅适用于 inference-time same-model extraction。\n\n**W8 [Major] Multi-seed replication 不充分 [共识]**\n- **位置**: Appendix X.1, Table 33\n- **问题**: 仅 Mistral-7B (3 seeds) 和 Qwen2.5-14B (4 seeds) 做了 multi-seed replication。Seed-level noise ≈ ±2.34pp，而 Table 1 大部分条件 |Δ| < 3pp 且为 single-seed。许多观测效应可能完全由 seed variance 解释。\n- **修改建议**: 至少对效应最大的条件补充 multi-seed，或在 Limitations 明确讨论 single-seed 局限。\n\n**W9 [Major] Capability-gap principle 基于 n=6 条件——不足以支撑 \"principle\" 级别 claim [共识]**\n- **位置**: §6 \"Escaping the Bottleneck\", Table 3, Figure 8\n- **问题**: 仅约 6 个 verifier-generator 组合，Table 3 仅 Mistral-7B (SC=39.33%) 1 个条件显著。§6 标题 \"Escaping the Bottleneck\" 语气过强。\n- **修改建议**: 降级为 \"preliminary observation\" 或 \"hypothesis\"。\n\n**W10 [Major] \"27 strategies fail\" scope 不匹配 [部分共识]**\n- **位置**: §5.2, Table 14, Abstract\n- **问题**: 27 个策略局限于 self-extraction paradigm 内的变体（prompt-level + method-level + cross-model），不等于所有 training-free 方法都失败。\n- **Reviewer 分歧**: R2 认为 scope 过宽，R1 partial REBUT（策略确实跨多个独立维度），但 R1 同意应限定 claim scope。\n- **修改建议**: 限定为 \"27 training-free variants within the constraint-extraction-aggregation paradigm\"。\n\n### Minor 问题（不影响接收）\n\n**M1** [Minor] α = 0.5 缺乏理论依据和真正的 sensitivity analysis。Table 11 的 ≥99% agreement 是 ceiling effect（主效应近零时 penalty 项影响自然可忽略），非真正鲁棒性。[共识]\n\n**M2** [Minor] \"First-order logic\" 描述轻微 overselling——99% 约束是 propositional level at Z3，仅 1.06% 使用真正量词。[共识]\n\n**M3** [Minor] Figure 1 信息密度偏高；K_eff 缺乏直觉解释；Abstract 信息过载（6 个要素）。[R2 提出]\n\n**M4** [Minor] §2 Related Work 段间逻辑衔接可改善——建议构建从 majority voting → self-correction → formal verification → this paper 的叙事线。[R2 提出]\n\n**M5** [Minor] GSM8K (n=30) 和 AIME (n=22) 样本量过小，不应与大样本条件等权重引用。论文已标注 \"exploratory\"（Table 1 caption），但正文 §5.3 引用时未区分。[共识]\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1.** Proposition 1 Part (i) 依赖 source attribution scoring。如果使用 source-agnostic scoring（基于逻辑一致性而非来源归属评估约束-答案关系），是否仍会退化？是否测试过 source-agnostic alternatives？\n\n**Q2.** BR 的 null expectation 是什么？如果约束提取完全\"无偏\"（support 比例精确反映 trace 投票分布），BR 期望值是否恰好为 1？请提供 permutation test 或 null model 分析。\n\n**Q3.** Diagnostics 的决策边界在 positive cases（cross-architecture escape, oracle）上是否能正确预测\"SICA 会帮助\"？\n\n**Q4.** TOST ±2pp equivalence margin 如何选择？如果 margin 放宽至 ±3pp 或 ±5pp，有多少额外条件达到等价显著？\n\n**Q5.** Table 1 中 |Δ| < 3pp 的所有 single-seed 条件，作者是否承认这些差异可能完全由 seed variance 解释（given seed noise ≈ ±2.34pp）？\n\n**Q6.** Cross-architecture NLI 验证仅在 NLI-friendly 数据集（FOLIO, ProofWriter）上测试。对非 NLI 格式推理任务是否适用？\n\n---\n\n## Missing References\n\n1. **Kamoi et al. (TACL 2024)**: \"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\" — self-correction 方向最全面 survey。[R2 提出，R1 AGREE]\n2. **S²R (Zeng et al., ACL 2025)**: RL-based self-verification，通过训练打破 Proposition 1 信息上限。[R2 提出，R1 同意应讨论理论边界]\n3. **DuPO (arXiv 2508.14460, 2025)**: Dual preference optimization self-verification。[R2 提出，R1 同意应讨论理论边界]\n4. **AlphaCode / CodeT**: Constraint verification in code domain 的成功案例，可对比讨论为何逻辑推理领域失败。[R1 提出，Minor]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: ✅ 完成（耗时 ~4 分钟）\n\n**统计**: 0 critical, 1 warning, 24 info\n\n**Warning**:\n- Page 7, Figure 4: 柱状图底部 x 轴策略名称字号偏小，27 个 bar 密度高，灰度打印时 4 种颜色区分度可能下降。建议增加 marker pattern 或 hatching。\n\n**Info 要点**:\n- Figure 1 (p.2) pipeline 图 caption 自包含，Title-Abstract-Figure 1 narrative 一致，第一印象良好\n- 所有 Figure/Table 出现在首次引用附近，无 float 漂移\n- 表格一致使用 booktabs 风格，最优值加粗，显著性标记有脚注说明\n- 公式渲染正确，无 LaTeX 错误残留或未解析引用\n- Limitations section 在 page 8 底部延伸至 page 9，符合 EMNLP 2026 规定\n- 参考文献约 2.5 页，格式统一\n\n**总体**: 排版质量良好，无严重视觉问题。\n\n---\n\n## Reviewer Consensus\n\n### 完全共识（14 项 AGREE）\n1. Proposition 1 scope mismatch（Part (i) SICA-specific，标题 claim \"structural\"）\n2. 统计功效 < 21% 与 negative claim 强度不匹配\n3. 标题 \"Fail to Improve\" overclaiming\n4. BR 循环论证风险（base-rate 效应未排除）\n5. Diagnostics in-sample overfitting（100% 准确率无意义）\n6. Multi-seed replication 不充分（2/6 模型）\n7. BR 小 n_err 条件缺 CI\n8. α = 0.5 sensitivity analysis 不充分\n9. Capability-gap principle n=6 不足以支撑 \"principle\"\n10. \"Extending Huang et al.\" 是 overselling\n11. GSM8K/AIME 样本量过小\n12. K_eff exchangeability 假设局限\n13. Cross-architecture generalizability 受限\n14. \"First-order logic\" 轻微 overselling\n\n### 部分分歧（3 项 partial REBUT，已记录各方理由）\n1. **新颖性**: R2 认为核心洞察可预见（Huang + DPI 延伸），R1 认为不应事后贬低 negative result 且诊断框架/27 策略有独立价值 → 共识：定位为\"系统性量化\"而非\"发现\"\n2. **Training-based refs**: R2 认为 major missing，R1 认为 scope 外但同意讨论理论边界\n3. **\"27 strategies\" scope**: R1 指出策略跨多维度，但同意应限定 claim scope\n\n---\n\n## Overall Assessment\n\n### 评分汇总\n\n| 维度 | R1 | R2 (交叉后修正) | 加权综合 |\n|------|-----|----------------|---------|\n| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |\n| Excitement | 3.0–3.5/5 | 2.5/5 | 3.0/5 |\n| Reproducibility | 4.0/5 | 4.0/5 | 4.0/5 |\n| Overall | 3.5 | 3.0 | **3.0** |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n### Overall: 3.0 — Findings\n\n**一句话总结**: 实验执行出色的 negative result paper，但核心理论贡献（Proposition 1）证明与声称范围不匹配、统计功效不足以支撑标题级 claim、诊断框架泛化性未验证、BR 指标概念有效性存疑，且新颖性有限（SCB 是已知结论的实证深化）。\n\n**详细理由**:\n\n*支持接收的因素*: (1) 实验规模大（9 模型 × 3 数据集 × 60 条件 × 27 策略），远超同类工作；(2) 统计方法论多层次且诚实（McNemar + BH + TOST + bootstrap + power analysis + shuffle control）；(3) Oracle 控制实验精巧，精确分离提取质量与方法论有效性；(4) 诊断框架有潜在实用价值；(5) Cross-architecture escape 提供建设性方向；(6) 附录极为详尽（18 页），可复现性强。作为 Findings 论文，对社区有实际指导价值——帮助避免在 self-extracted constraint verification 方向上的无效探索。\n\n*限制接收为 Conference 的因素*: (1) Proposition 1 的 scope mismatch 使核心理论贡献被削弱——Part (i) 仅对 source-attribution 成立，Part (ii) 是平凡 DPI 推论；(2) 21% 的统计功效使 \"fail to improve\" 的标题级 claim 无法被统计证据充分支撑；(3) Diagnostics 的 100% 准确率是 in-sample 评估，holdout 验证不充分，这是论文三大贡献之一；(4) BR 作为 SCB 的量化基础存在循环论证风险（base-rate 效应未排除），需要 null model 才能确定\"额外 bias\"的存在；(5) 新颖性有限——核心洞察（自提取约束继承模型 bias）是 Huang et al. (2024) + Wan et al. (2025) 已知结论在形式化验证管道中的实证深化。\n\n*如果以下问题得到解决，评分可提升至 3.5（Borderline Conference）*:\n1. 标题软化 + Abstract 加 power caveat + TOST margin sensitivity\n2. Proposition 1 拆分并明确 scope\n3. BR 提供 permutation null model 或降级为描述性指标\n4. Diagnostics 增加 held-out model family 验证并弱化 claim\n5. §2 补充 training-based self-verification 讨论\n6. \"Extending Huang et al.\" 改为 \"consistent with / provide independent evidence for\"\n\n---\n\n## Detailed Comments（逐节）\n\n**Title**: \"Fail to Improve\" 过于绝对，与 power < 21% 不匹配。建议 \"Do Not Substantially Improve\" 或 \"The Limits of Self-Extracted Constraints for\"。\n\n**Abstract**: 信息密度高但覆盖完整。需加 power caveat（如 \"though underpowered for effects below ~2pp\"）。\"extends the self-correction impossibility of Huang et al.\" 改为 \"provides independent evidence consistent with\"。BR 报告 \"at least 1.66×\" 应注明 base-rate 组成未排除。\n\n**§1 Introduction**: Contribution 2（diagnostics 100% 准确率）需加 scope 限定。Contribution 3 \"capability-gap principle\" 降级为 \"preliminary observation\"。\n\n**§2 Related Work**: 缺 training-based self-verification 讨论（S²R, DuPO）。缺 Kamoi et al. (TACL 2024) self-correction survey。段间逻辑衔接可改善。\n\n**§3 Method**: α = 0.5 缺理论依据。K_eff 缺直觉解释。BR 定义（Eq. 5）需声明 base-rate 效应。\n\n**§4 Results**: 统计诚实（报告 power 局限），但 claim 强度与证据强度仍有 gap。Single-seed 条件应标注不确定性。\n\n**§5.1 Symbolic Confirmation Bias**: Proposition 1 需拆分。BR > 1 的解读需 null model。Table 11 的 ≥99% agreement 应加 ceiling effect caveat。\n\n**§5.2 Why Remediation Fails**: 27 策略 claim scope 应限定为 \"within constraint-extraction-aggregation paradigm\"。\n\n**§5.3 Diagnostic Framework**: 100% 准确率 claim 需大幅弱化。增加 OOD 验证。讨论 positive case 预测能力。\n\n**§6 Escaping the Bottleneck**: 标题过强。\"Capability-gap principle\" → \"preliminary observation\"。仅 1 个条件显著。\n\n**§7 Discussion and Conclusion**: \"extending... to formal verification\" 改措辞。Future work 应明确 training-based methods 如何 escape Proposition 1。\n\n**Limitations**: 长度合规（EMNLP 2026 规定\"一小段覆盖 3 个点\"），覆盖了关键局限（open-source only, English only, logical reasoning only）。可考虑增加 power limitation 的一句话提及。\n"
  }
}
```

</details>

---


### Tool result

_source line 1705 · 2026-05-23T08:27:21.424956+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_970d5ea3f54df81296b97321fcded892:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4253
}
```

</details>

---


### Assistant

_source line 1706 · 2026-05-23T08:27:33.695716+00:00_

审稿报告已投递。

**Round 16 审稿完成汇报**（Group C）：

| 项目 | 结果 |
|------|------|
| **Overall** | **3.0 (Findings)** |
| Soundness | 3.5/5 |
| Excitement | 3.0/5 |
| Reproducibility | 4.0/5 |
| Confidence | 4/5 |

**4 个 Critical 问题**：
1. Proposition 1 证明范围（source-attribution specific）与声称范围（"structural"）不匹配
2. 统计功效 < 21% 无法支撑标题 "Fail to Improve" 的强否定
3. Diagnostics 100% 准确率是 in-sample 评估，holdout 仅 1 个条件
4. BR 指标存在 base-rate 循环论证，缺 null model

**修复路径至 3.5 (Borderline Conference)**：标题软化 + Prop 1 拆分 + BR null model + diagnostics OOD 验证 + training-based refs + "extending Huang" 改措辞。

Issue tracker 已同步更新（新增 R16-N1/N2/M1/M2/W1/W2/W3，更新 27 条历史 issue 的 R16 mentions）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 120

## Round 120

2 recorded events


### User

_source line 1707 · 2026-05-23T08:27:36.265015+00:00_

[Reviewer 1 审稿结果]:
已完成对 R2 全部意见的逐条回应，汇报给 Review Director。

总结：
- **N1 (新颖性)**: [REBUT] — 高层洞察可预见，但机制定位、诊断框架、27策略否证是非平凡贡献，不应以事后论证否定 negative result 的价值
- **N2 (BR 循环)**: [AGREE] — R2 指出的 base-rate 效应是方法论上的正确批评，需要 null model
- **N3 (Diagnostics overfitting)**: [AGREE] — 100% in-sample accuracy 无统计意义，需 held-out 验证
- **W1 (标题)**: [AGREE]，与我 R1-N2 一致
- **W2 (training-based 讨论)**: [REBUT] — 论文已界定 training-free scope，但应讨论 training 如何 escape A2
- **W3 (capability-gap n=6)**: [AGREE]，与我 R1-W8 一致
- **W4 (27 strategies scope)**: [REBUT] — 覆盖范围实际较广，但 claim 措辞应限定
- **W5 (extending Huang)**: [AGREE]
- **评分差距 (3.5 vs 3.0)**: 主要在 novelty 权重和 fixable issues 严重程度上，两者均在合理范围

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

_source line 1708 · 2026-05-23T08:27:54.666347+00:00_

审稿报告已投递至 Research Director。

**Round 16 审稿完成。**

| 项目 | 结果 |
|------|------|
| Overall | **3.0 — Findings** |
| Soundness | 3.5/5 |
| Excitement | 3.0/5 |
| Reproducibility | 4.0/5 |
| Reviewer 1 | 3.5 (Borderline Conference) |
| Reviewer 2 | 3.0 (Findings) |
| 交叉共识 | 14 项 AGREE, 3 项 partial REBUT |

**4 个 Critical 问题**（Must-Fix）：
1. **Proposition 1 scope mismatch** — Part(i) 仅对 source-attribution 成立，标题 claim "structural" 过宽
2. **统计功效 < 21%** — 标题 "Fail to Improve" 与证据强度不匹配
3. **Diagnostics in-sample overfitting** — 100% 准确率在训练集上评估，holdout 仅 1 个条件
4. **BR 循环论证** — base-rate 效应未排除，需 null model

**提升至 3.5 的路径**：软化标题 + Prop 1 拆分 + BR null model + diagnostics held-out 验证 + §2 补 training-based 讨论 + "extending Huang" 改措辞。

Issue tracker 已同步更新（R16 新增 6 条 issue，历史 issue 追加本轮 mentions）。视觉审查已完成（0 critical, 1 warning）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 121

## Round 121

62 recorded events


### User

_source line 1709 · 2026-05-23T09:15:30.442142+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: symb_invariant_consensus
- 论文路径: projects/symb_invariant_consensus/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
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

_source line 1710 · 2026-05-23T09:15:36.108306+00:00_

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

_source line 1711 · 2026-05-23T09:15:36.209677+00:00_

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

_source line 1712 · 2026-05-23T09:15:42.933450+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,WebSearch,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_local_file",
  "max_results": "15"
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
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,director_post_to_reviewer,WebSearch,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_local_file",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 1713 · 2026-05-23T09:15:42.933894+00:00_



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

_source line 1714 · 2026-05-23T09:15:47.452130+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "15"
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "15"
  }
}
```

</details>

---


### Tool result

_source line 1715 · 2026-05-23T09:15:47.452636+00:00_



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

_source line 1716 · 2026-05-23T09:15:52.325571+00:00_

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

_source line 1717 · 2026-05-23T09:15:53.330265+00:00_

{"result":"# 项目 symb_invariant_consensus 概况\n\n## 实验状态 (173 个)\n\n- **sica_k_sensitivity_14b**: DONE (success) — \n- **exp-011-llama8b**: DONE (failed) — \n- **exp-016-weighted-sc**: DONE (success) — \n- **exp-005**: DONE (negative) — \n- **sica_folio30**: DONE (killed) — \n- **sica_d016_c0_precheck**: DONE (success) — \n- **sica_proofwriter30_v2**: DONE (killed) — \n- **sica_proofwriter30**: DONE (failed) — \n- **sica_aime30_v3**: DONE (killed) — \n- **sica_aime30_v2**: DONE (killed) — \n- **sica_aime30_t07**: DONE (killed) — \n- **mvp_math50_t07**: DONE (killed) — \n- **sica_smoke_5q**: DONE (success) — \n- **smoke-test-5q**: PREPARING (failed) — \n- **crd_folio_main**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp-multi-seed-llama-pw-seed789-v2 | LLaMA-3.1-8B PW seed789 多种子复制（westd-30973 cuda:1 全新运行）。替代 16639 cuda:0 上的慢速运行（12/600）。验证 SCB 在 ProofWriter 上跨 seed 稳定性。 | — | — | — |\n| exp-multi-seed-llama-pw-seed456-v2 | LLaMA-3.1-8B PW seed456 多种子复制（westd-30973 cuda:2 全新运行）。验证 SCB 在 ProofWriter 上跨 seed 稳定性（Δ(SICA-SC)≤0）。配合 seed42/123/789 组成 4-seed 覆盖。 | — | — | — |\n| exp-multi-seed-qwen25-pw-seed789-v3 | Qwen2.5-14B PW seed789 多种子复制（westd-30973 cuda:0 全新运行）。替代 v2 在 16639 cuda:2 上的慢速运行（53/600）。验证 SCB 在 ProofWriter 上跨 seed 稳定性。 | — | — | — |\n\n## 待处理\n- exp-multi-seed-llama-pw-seed456: LLaMA-3.1-8B PW seed456 多种子复制。验证 SCB 在 ProofWriter 上跨 seed 稳定性（Δ(SICA-SC)≤0）。配合 seed42/123/789 组成 4-seed 覆盖。（排队等待 GPU）\n- exp-deberta-ft-combo: Fine-tuned DeBERTa-large on ProofWriter OWA depth-5 achieves near-perfect NLI accuracy (99.67%) and provides massive combo gains over SC baseline when used as external verifier, demonstrating that domain-specific NLI fine-tuning breaks the SCB ceiling by providing truly independent verification signal.（准备中）\n- exp-multi-seed-mistral-folio: Multi-seed replication (seeds 123,456,789) of Mistral-7B × FOLIO-20
…[truncated 1733 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1718 · 2026-05-23T09:15:53.330662+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "memory.md",
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
    "file": "memory.md",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1719 · 2026-05-23T09:15:53.330922+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/memory.md\", \"content\": \"# Memory\\n\\n## D061 统一决策 (2026-05-22, D153)\\n\\n**所有表统一用 r11_canonical (ID_FIX 后) 数据**：SC=39.33% (236/600)。39.17% 是 pre-ID_FIX 旧值，已从论文中彻底清除（0 残留）。\\n\\n## vLLM 启动教训 (2026-05-22)\\n\\n**启动 vLLM 后必须加 readiness check 再执行实验脚本。** exp-multi-seed-qwen25-pw-seed789 因 vLLM 未加载完就执行产出全零结果。正确做法：循环 `curl health endpoint` 直到返回 200。\\n\\n**多种子实验必须统一代码路径**：所有种子用 `run_cross_dataset_replication.py`，不用 `run_full_mvp.py`，否则 tiebreaking/preprocessing 可能不一致。\\n\\n## NLI Combo 实验设置参考 (2026-05-22)\\n\\n- Mistral-7B PW combo: SC weight=w, NLI weight=1, DeBERTa-large-MNLI verifier\\n- FT DeBERTa: microsoft/deberta-large-mnli fine-tuned on ProofWriter OWA depth-5 (69,810 samples, 2 epochs, 99.67% accuracy)\\n- Combo tiebreaking: `sorted(tied_c)[0]` (D061 alphabetical)\\n\\n## 多种子实验状态 (2026-05-22 更新)\\n\\n- Qwen2.5-14B FOLIO 4-seed 完成: mean Δ=-1.24±0.86pp, 4/4 seeds ≤0\\n- Mistral FOLIO 3-seed 完成: mean Δ=+0.16±2.70pp (混合方向)\\n- Mistral PW 4-seed 完成: mean Δ=-2.38±1.12pp, 4/4 seeds ≤0\\n- LLaMA FOLIO 3-seed: seed123 Δ=-3.43, seed456 Δ=-0.49, seed789 Δ=+0.98. seed789 已从 westd-14391 恢复 204/204\\n- Qwen2.5-14B PW: cuda:0 跑 seed456, cuda:3 跑 seed123 rerun. seed789 将由 cuda:0 chain 自然执行\\n\\n## 磁盘状态 (2026-05-22)\\n\\n- westd-16639: 根 35% (20G free), 数据盘 66% (121G free). 模型占 ~170G\\n- westd-14391: 根 41% (18G free), 数据盘 11% (225G free). 充裕\\n\\n## Blackwell GPU 注意事项\\n\\nwestd-16639/14391 使用 RTX PRO 6000 Blackwell (sm_120)。vLLM 启动需要 `VLLM_USE_FLASHINFER_SAMPLER=0` + `--enforce-eager`，否则 FlashInfer 报错。\\n\", \"total_chars\": 1426, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1720 · 2026-05-23T09:15:53.732764+00:00_

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


### Tool call

_source line 1721 · 2026-05-23T09:15:55.590523+00:00_

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

_source line 1722 · 2026-05-23T09:15:55.641255+00:00_

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
40	\title{Beyond Self-Consistency: Self-Extracted Constraints\\Do Not Substantially Improve LLM Logical Reasoning}
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
72	\enlargethispage{2\baselineskip}
73	\vspace{-1.5mm}
74	\input{discussion}
75	
76	\vspace{-4mm}
77	\section*{Limitations}
78	\input{limitations_content}
79	
80	\bi
…[truncated 85 chars]

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

_source line 1723 · 2026-05-23T09:15:59.054971+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"}]

Based on my search results, I found i
…[truncated 1302 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 5322
}
```

</details>

---


### Tool call

_source line 1724 · 2026-05-23T09:16:05.331547+00:00_

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

_source line 1725 · 2026-05-23T09:16:06.212189+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers deadline commitment Budapest"
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
    "query": "EMNLP 2026 call for papers deadline commitment Budapest"
  }
}
```

</details>

---


### Tool call

_source line 1726 · 2026-05-23T09:16:07.065683+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "decisions.yaml",
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
    "file": "decisions.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1727 · 2026-05-23T09:16:11.382606+00:00_

Web search results for query: "EMNLP 2026 call for papers deadline commitment Budapest"

Links: [{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"When is EMNLP 2026? Dates, Deadline & Location | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/conference/emnlp"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 - Conference on Empirical Methods in Natural Language Processing Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/emnlp"}]

Based on the search results, here's the information about EMNLP 2026:

**Conference Details:**
The 2026 Conference on Empirical Methods in Natural Language Processing (EMNLP 2026) will be held in Budapest, Hungary from October 24th to October 29th, 2026.

**Call for Papers Deadline:**
The EMNLP 2026 paper submission deadline is 2026-05-25 23:59:59 (UTC-12).

**Commitment Deadline:**
Papers that have received reviews and a meta-review from
…[truncated 648 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 5170
}
```

</details>

---


### Tool result

_source line 1728 · 2026-05-23T09:16:12.186280+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here are the ACL Rolling Review 2026 submission guidelines regarding page limits and format requirements:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Upon acceptance, final versions of long papers will be given one additional page – up to nine (9) pages of content plus unlimited pages for acknowledgments and references.

R
…[truncated 1138 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 6854
}
```

</details>

---


### Tool result

_source line 1729 · 2026-05-23T09:16:12.187072+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/decisions.yaml\", \"content\": \"_next_id: 156\\ndecisions:\\n- id: D001\\n  date: 2026-05-15 08:47 UTC\\n  summary: MVP 验证方案：50 题 MATH-500 分层子集，SICA vs SC@K=12\\n  rationale: SICA 核心价值取决于两个前提：(1) 能从推理 trace 可靠提取符号约束；(2) 跨路径矛盾率足够高（>5%）使形式化验证有意义。Reviewer\\n    给 impact 3/5，核心担忧是\\\"若矛盾率<5%则动机不成立\\\"。MVP 直接验证这两个前提，50 题按难度分层可同时观察 Extraction-Verification\\n    Paradox（难题提取差但矛盾多）。Pass 则进入全量实验冲 EMNLP/AAAI，Fail 则及时止损。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-15 08:52 UTC\\n  summary: 拒绝 CRD pivot，要求回归 SICA 原始方案\\n  rationale: Reviewer critical 审查发现 Agent 实施的是\\\"跨表征分歧诊断\\\"(CRD)，与 IDEA_BRIEF 定义的 SICA\\n    完全不同：CRD 用双表征（FOL+SymPy）做单解分歧检测，无多路径采样、无 MAX-SAT 共识——这正是 SICA 区别于 VERGE/D&P 的核心创新点。CRD\\n    的 novelty 定位与 VERGE 高度重叠（单输出验证+修复），无法支撑 EMNLP 投稿。同时 MVP 标准被静默替换，ROADMAP 的三条 pass\\n    criteria 从未测试。98GB GPU 完全能跑 QwQ-32B，无理由换 Qwen3-32B-AWQ。必须回归 SICA：K=12 多路径采样 →\\n    符号约束提取 → Z3 加权 partial MAX-SAT → 不变量共识打分。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-15 08:54 UTC\\n  summary: MVP 标准 v2：三档判定 + 矛盾绝对数 ≥5 + accuracy ≥SC+2pp + ProofWriter sanity check\\n  rationale: Reviewer warning 指出：(1) 5% 矛盾率阈值在 50 题上仅 2.5 题，置信区间极宽——改为绝对数 ≥5 题；(2)\\n    ≥SC+0.1pp 也过关无意义——改为 ≥2pp 或 p<0.1；(3) 灰色区间无处理——新增 Inconclusive 档，触发扩展到 100 题重测；(4)\\n    单域 MATH-500 不够——加 10 题 ProofWriter 做逻辑域 sanity check；(5) 模型不能模糊——固定 QwQ-32B，不可替换。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-15 12:02 UTC\\n  summary: MVP T=0.7 继续跑完（需要完整数据），diagnostic 自然结束后 GPU 带宽恢复；AIME 30 题排在 MVP 之后\\n  rationale: Temperature 诊断 4/5 题显示 T=0.7/0.9/1.0 均几乎不产生答案分歧——C2/C3 高风险 FAIL。但仍决定让\\n    MVP 跑完：(1) 50 题完整数据无论正负都有价值（负面结果=SICA 在强模型上无信号，本身是发现）；(2) GPU 已分配且无其他实验排队；(3)\\n    smoke test L5 有 3 条矛盾，50 题中 L4-5 有 20 题可能产生更多信号。MVP 完成后立即跑 AIME 30 题（QwQ-32B ~79.5%，分歧应更明显），作为\\\"高难度\\n    sweet
…[truncated 3562 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5121
}
```

</details>

---


### Tool call

_source line 1730 · 2026-05-23T09:16:22.633024+00:00_

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

_source line 1731 · 2026-05-23T09:16:23.035185+00:00_

1	Can symbolic verification via a provably sound solver improve Large Language Model (LLM) reasoning when constraints are self-extracted from the model's own traces? We show the answer is no. We introduce Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from chain-of-thought traces and selects answers via weighted MAX-SAT. Despite Z3 validating 99\% of self-extracted constraints, SICA produces answers identical to majority voting on 94.4\% of problems across six models (7B--32B) and three reasoning domains. No condition shows a significant positive effect after FDR control; four conditions confirm equivalence within $\pm$2\,pp, though ten remain underpowered for effects below ${\sim}$2\,pp (absence of evidence is not evidence of absence). We systematically diagnose the failure as \emph{symbolic confirmation bias}: self-extracted constraints track the model's majority answer, with bias ratios from $1.66\times$ to $4.97\times$ across nine models (7B to frontier scale), reflecting both the base-rate effect of trace-count distributions and extraction alignment. We prove the voting degeneration is structural under source-attribution scoring (Proposition~1) and confirm it via shuffle control, providing independent evidence consistent with the self-correction limitations identified by \citet{huang2024selfcorrect}. Twenty-seven training-free variants within the constraint-extraction paradigm fail due to a persistent independence-accuracy trade-off. Preliminary evidence suggests that structurally independent cross-architecture verification can escape the bias ($+6.67$\,pp on the weakest generator, $p < 0.001$). Three zero-cost diagnostics correctly classify all 60 tested conditions within the self-extraction paradigm, enabling practitioners to predict a priori whether symbolic aggregation will help.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1732 · 2026-05-23T09:16:23.035574+00:00_

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

_source line 1733 · 2026-05-23T09:16:23.538148+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	\looseness=-1
4	Self-Consistency (SC) \citep{wang2023sc} selects the majority answer across $K$ chain-of-thought traces, a strategy grounded in the Condorcet Jury Theorem: independent voters converge to truth \citep{condorcet1785, ladha1992correlated}. In practice, SC's gains plateau for strong models \citep{loo2025reevaluating}, pointing to correlated traces that reduce the effective ensemble size. A natural remedy is to move beyond simple vote-counting: extract logical constraints from the traces and let a provably sound solver adjudicate. If the solver can filter contradictions and enforce logical consistency, it should recover information that raw majority voting discards.
5	
6	\looseness=-1
7	We test this intuition through Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from reasoning traces (prompted as first-order logic; 99\% are propositional at the Z3 level) and selects answers via weighted partial MAX-SAT (\S\ref{sec:pipeline}; Figure~\ref{fig:pipeline}). The result is unequivocal: despite Z3 validating nearly all self-extracted constraints, SICA produces answers identical to majority voting on the vast majority of problems. Across six models (7B--32B), three reasoning domains, and multi-seed replication, no condition shows a significant positive effect after FDR control (Table~\ref{tab:main_results}). Four conditions confirm equivalence within $\pm$2\,pp; ten remain underpowered for effects below ${\sim}$2\,pp.
8	
9	\looseness=-1
10	The failure is not in the solver but in the constraints it operates on. Self-extracted constraints systematically support the model's majority answer, a phenomenon we term \emph{symbolic confirmation bias} (\S\ref{sec:confirmation-bias}). Because each trace determines both an answer and its constraints, the formal channel reduces to a weighted echo of the majority vote. We prove this degeneration is structural (Proposition~1) and show it 
…[truncated 3952 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1734 · 2026-05-23T09:16:23.538504+00:00_

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

_source line 1735 · 2026-05-23T09:16:24.040745+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\looseness=-1
5	\paragraph{Self-consistency and ensemble theory.}
6	Self-consistency (SC) selects the most frequent answer across chain-of-thought traces \citep{wang2023sc}. Extensions address free-form generation \citep{chen2024usc}, confidence weighting \citep{taubenfeld2025cisc}, diverse prompting with step-aware verification \citep{li2023diverse}, program-based vote filtering \citep{toh2024notallvotes}, and reasoning-aware filtering \citep{wan2024rasc, kim2026reasc}. SC gains plateau early \citep{loo2025reevaluating}, particularly in mathematical reasoning \citep{byerly2026selfconsistency}. The Condorcet Jury Theorem \citep{condorcet1785} guarantees majority-vote convergence under independent voting; \citet{ladha1992correlated} show correlated voters reduce effective ensemble size. Our $K_\text{eff}$ adapts Fleiss' $\kappa$ from ensemble diversity theory \citep{kuncheva2003measures, brown2005diversity} to quantify this compression (\S\ref{sec:pipeline}). \citet{kim2025correlated} demonstrate correlated errors in LLM outputs; \citet{kuai2026independent} propose cross-model independence auditing, complementary to our within-model process-$\kappa$. Symbolic confirmation bias is distinct from CoT unfaithfulness \citep{turpin2024language} and CoT-level confirmation bias \citep{wan2025unveiling, jhaveri2026failing}: the latter concern whether reasoning reflects actual computation, while symbolic confirmation bias concerns whether self-extracted formal constraints mirror the model's answer distribution.
7	
8	\looseness=-1
9	\paragraph{Neuro-symbolic reasoning.}
10	We distinguish three paradigms: \emph{specification-generation} \citep{pan2023logiclm, olausson2023linc, ye2024satlm} translates problems into formal specifications before answering; \emph{program-generation} \citep{gao2023pal, chen2023program, lyu2023faithful} produces executable code; both formalize \emph{before} answer generation. \emph{Trace-extract
…[truncated 3066 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1736 · 2026-05-23T09:16:24.041249+00:00_

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

_source line 1737 · 2026-05-23T09:16:24.141989+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{SICA Pipeline}
5	\label{sec:pipeline}
6	\label{sec:condorcet}
7	\label{sec:effective-k}
8	
9	Self-Consistency (SC) \citep{wang2023sc} samples $K$ reasoning traces and selects the majority answer. Under correlated traces (Fleiss' $\kappa$ \citep{fleiss1971kappa}), effective sample size reduces to
10	\begin{equation}
11	\label{eq:effk}
12	K_{\text{eff}} = K \,/\, [1 + (K{-}1) \cdot \kappa]
13	\end{equation}
14	(following \citet{ladha1992correlated}), motivating constraint-based aggregation.
15	
16	Symbolic Invariant Consensus Aggregation (SICA) extends SC by extracting formal constraints from traces and selecting the answer best supported by the satisfiable subset (Figure~\ref{fig:pipeline}).
17	
18	\paragraph{Trace generation.} Given question $q$, an LLM generates $K$ traces $\{t_1, \ldots, t_K\}$ at temperature $T = 0.7$. Each trace $t_i$ yields answer $a_i$.
19	
20	\looseness=-1
21	\paragraph{Constraint extraction.}\label{sec:constraint-extraction} The same LLM extracts logical constraints from each trace at $T_{\text{ext}} = 0.3$. The extraction prompt requests JSON output with constraint type, expression, and Z3-compatible formula (Appendix~\ref{app:prompts}); in practice, 99.0\% of extracted constraints are propositional at the Z3 level, with only 1.0\% using true quantifiers. The \emph{extraction rate} is the fraction of traces yielding at least one parseable constraint.
22	
23	\paragraph{Deduplication and MAX-SAT.} Constraints are deduplicated by syntactic equivalence (global average deduplication ratio: 46.0\%); each unique constraint $c_m$ receives weight $w_m$ equal to the number of source traces. The objective finds the largest-weight satisfiable subset:
24	\begin{equation}
25	\label{eq:maxsat}
26	\mathcal{C}^* = \arg\max_{\mathcal{S} \subseteq \mathcal{C}} \sum_{c \in \mathcal{S}} w_c \quad \text{s.t.} \quad \mathcal{S} \text{ is satisfiable.}
27	\end{equation}
28	Z3 \citep{demoura2008z3} solves thi
…[truncated 3589 chars]

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

_source line 1738 · 2026-05-23T09:16:28.559385+00:00_

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

_source line 1739 · 2026-05-23T09:16:29.463498+00:00_

1	\section{Results}
2	\label{sec:results}
3	\label{sec:main-results}
4	
5	\looseness=-1 Table~\ref{tab:main_results} reports accuracy across all non-degenerate self-extraction conditions sorted by SC baseline. No condition shows a significant SICA effect after FDR control (BH, $m{=}16$). Two conditions show nominally significant degradation: Mistral-7B on ProofWriter ($-2.83$\,pp, raw $p = 0.014$) and Qwen2.5-14B on ProofWriter ($-2.50$\,pp, raw $p = 0.011$); both reach adjusted $p = 0.112$. An aggregate sign test yields 8 positive and 7 negative $\Delta$ values ($p = 1.00$, two-sided).
6	
7	\begin{table*}[t]
8	\centering
9	\small
10	\caption{SICA vs.\ SC across all non-degenerate self-extraction conditions (sorted by SC). No condition shows a significant gain after BH correction ($m{=}16$). $\Delta$ = SICA $-$ SC (pp). Symbols: $^b$gold ICL; \textbf{bold}: $p < 0.05$; {*}\,uncorrected $p < 0.05$ (BH adj.\ $p = 0.112$); $^{3s}$\,3-seed; $^{4s}$\,4-seed confirmatory (unmarked: single-seed exploratory). Degenerate conditions ($C_0 < 5\%$: QwQ-32B AIME, Qwen2.5-14B GSM8K) yield $\Delta = 0$; oracle upper bounds are reported in Appendix~\ref{app:oracle}.}
11	\label{tab:main_results}
12	\begin{tabular}{@{}llrrrrl@{}}
13	\toprule
14	Model & Domain & $n$ & SC (\%) & SICA (\%) & $\Delta$ (pp) & $p$ \\
15	\midrule
16	\multicolumn{7}{l}{\textit{Type C: error amplification (SC $\leq$ 40\%)}} \\
17	Mistral-7B & PW-D5 & 600 & 39.33 & 36.50 & $\mathbf{-2.83}$ & 0.014{*} \\
18	\midrule
19	\multicolumn{7}{l}{\textit{Intermediate SC (SC $\sim$50--60\%, Mistral-7B only)}} \\
20	Mistral-7B & LogiQA & 200 & 50.00 & 51.50 & $+$1.50 & 0.581 \\
21	Mistral-7B & FOLIO (s123) & 204 & 54.41 & 57.35 & $+$2.94 & 0.070 \\
22	Mistral-7B$^{3s}$ & FOLIO & 204 & 56.53 & 56.70 & $+$0.16 & 1.000 \\
23	Mistral-7B & FOLIO (s456) & 204 & 55.88 & 55.88 & 0.00 & 1.000 \\
24	Mistral-7B & FOLIO (s789) & 204 & 59.31 & 56.86 & $-$2.45 & 0.267 \\
25	\midrule
26	\multicolumn{7}{l}{\textit{Type A: confirmation bi
…[truncated 3213 chars]

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

_source line 1740 · 2026-05-23T09:16:29.614512+00:00_

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

_source line 1741 · 2026-05-23T09:16:29.916433+00:00_

1	\section{The Symbolic Mirage}
2	\label{sec:analysis}
3	
4	\subsection{Symbolic Confirmation Bias}
5	\label{sec:confirmation-bias}
6	
7	\looseness=-1 Self-extracted constraints systematically align with the model's majority answer. On Mistral-7B FOLIO, when SICA errs, 83.3\% of constraints support the incorrect answer---bias ratio $4.97\times$ (Table~\ref{tab:cross-model-bias})---and 94\% of errors overlap with SC. Z3 rejects only 3.4\% of constraints, and MAX-SAT produces answers identical to count-only aggregation on 94.4\% of problems (Table~\ref{tab:ablation}), confirming that the formal verification layer is vacuous (Eq.~\ref{eq:degenerate}): 99\% of constraints pass Z3 validation yet add no information beyond majority voting. This vacuity is $\alpha$-insensitive: agreement $\geq$99\% across $\alpha \in \{0.1, \ldots, 0.9\}$ (Table~\ref{tab:alpha-ablation}).
8	
9	\looseness=-1 Empirically, confirmation bias extends beyond incorrect instances. On problems where SC selects the correct answer, constraints still disproportionately support the majority ($\text{BR}_\text{correct}$ $1.29$--$3.64\times$ across all six tested conditions, with 5/6 showing $\text{BR}_\text{correct} \geq \text{BR}_\text{wrong}$), confirming that self-extracted constraints track distributional frequency rather than logical validity. A shuffle control confirms that BR reflects the trace-count distribution: randomizing constraint--answer associations while preserving per-trace counts yields $\text{BR}_\text{null} \approx \text{BR}_\text{obs}$ ($p > 0.7$). The bias is structural precisely because it is inherent to the majority-vote geometry (Proposition~1), not an artifact of extraction.
10	
11	\looseness=-1 The pattern generalizes: $4.97\times$ (Mistral), $3.85\times$ (Qwen-14B), $2.88\times$ (LLaMA), all $> 1.0$ with 95\% bootstrap CIs (Table~\ref{tab:cross-model-bias}). Cross-model extraction confirms universality across nine models from 7B to frontier (BR $1.66$--$4.97\times$; Table~\ref{
…[truncated 12649 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1742 · 2026-05-23T09:16:29.916926+00:00_

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

_source line 1743 · 2026-05-23T09:16:30.168450+00:00_

1	\section{Escaping the Bottleneck}
2	\label{sec:solutions}
3	\label{sec:cross-arch}
4	
5	\paragraph{Motivation.}
6	\looseness=-1 No training-free self-extraction method achieves independence from the model's distributional prior (\S\ref{sec:remediation}). Corollary~1 implies that any escape must break the self-extraction dependency: the information ceiling $I(C;Y) \leq I(T;Y)$ binds whenever constraints are deterministic functions of the generating model's traces. We test whether a structurally independent verifier, sharing neither architecture nor training data with the generator, provides corrective signal that escapes this bound.
7	
8	\paragraph{Method.}
9	\looseness=-1 We use DeBERTa-large \citep{he2021deberta} (406M, encoder-only), fine-tuned on MultiNLI \citep{williams2018mnli}, to classify (premise, conclusion) pairs as entailment, contradiction, or neutral. In combo mode, each NLI-supporting vote counts $w$ times alongside SC's $K$ votes. We evaluate on Mistral-7B FOLIO ($n = 204$) and ProofWriter depth-5 ($n = 600$).
10	
11	\paragraph{Zero-shot results.}
12	\looseness=-1 DeBERTa NLI alone achieves 49.51\% on FOLIO and 55.00\% on ProofWriter. Combo $w{=}3$ yields $+6.67$\,pp on ProofWriter for Mistral-7B ($p < 0.001$, significant after BH correction) and $+2.94$\,pp on FOLIO (n.s.); all generators with SC $\geq 72\%$ show no significant improvement ($\Delta \leq +0.83$\,pp). Same-model SICA \emph{degrades} ProofWriter ($-2.83$\,pp; Table~\ref{tab:main_results}), illustrating that corrective signal must originate outside the model's distribution.
13	
14	\paragraph{Capability gap.}
15	\looseness=-1 Four generators spanning a 47-point SC range on ProofWriter ($n{=}600$), all paired with DeBERTa-large-mnli (55.00\% standalone; Table~\ref{tab:cross_generator_nli}): only Mistral-7B (SC 39.33\%, below the verifier) gains significantly ($+6.67$\,pp, $p < 0.001$); all three above the verifier show no significant improvement ($\Delta \leq +0.83$\,pp). These results p
…[truncated 1990 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1744 · 2026-05-23T09:16:30.168948+00:00_

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

_source line 1745 · 2026-05-23T09:16:30.219559+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	\label{sec:conclusion}
4	
5	\looseness=-1
6	Our central finding is that the value of formal verification depends on the \emph{independence} of its inputs, not the soundness of its logic. The three diagnostics ($K_\text{eff}$, BR, $C_0$) operationalize this principle, extending beyond SICA to any self-extraction-based aggregation method and correctly classifying all 60 tested conditions within this paradigm. Decision boundaries generalize prospectively to a held-out model family (\S\ref{sec:diagnostic-framework}), enabling practitioners to evaluate viability from a pilot run ($K{=}12$) before full deployment.
7	
8	\looseness=-1
9	This independence principle has direct consequences for test-time compute scaling \citep{snell2025scaling}: with $K_\text{eff} \leq 3.62$ for $K{=}12$, same-model traces scale redundancy, not information, and the capability-gap pattern implies the bar rises as generators improve. The principle applies to any self-verification method that draws on the generating model's own distribution, providing independent evidence consistent with the self-correction limitations of \citet{huang2024selfcorrect}. Escaping the bottleneck requires structural independence, capability ordering, and task-verifier alignment (\S\ref{sec:cross-arch}); whether trained extractors can shift this boundary remains open. More broadly, the bottleneck of self-referential verification lies not in the formal reasoning channel but in the extraction pathway---the diagnostics and framework we provide enable future work to recognize this limitation upfront.
10	

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

_source line 1746 · 2026-05-23T09:16:34.798076+00:00_

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

_source line 1747 · 2026-05-23T09:16:34.848816+00:00_

1	\looseness=-1 Open-source models range from 7B to 32B; frontier models confirm SCB universality via cross-model extraction. All datasets are English-language logical reasoning benchmarks; we do not evaluate trained extractors or multilingual settings. Statistical power is limited for effects below ${\sim}$2\,pp; the capability-gap analysis rests on $n{=}6$ conditions (Appendix~\ref{app:limitations-extended}).
2	

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

_source line 1748 · 2026-05-23T09:16:34.950303+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1749 · 2026-05-23T09:16:35.352414+00:00_

File content (30701 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1750 · 2026-05-23T09:16:37.656304+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1751 · 2026-05-23T09:16:37.707123+00:00_

1	\section{Prompt Templates}
2	\label{app:prompts}
3	
4	SICA uses domain-specific prompt templates for constraint extraction: one for mathematical reasoning (GSM8K, AIME) and one for logical reasoning (ProofWriter, FOLIO). Both share the same system prompt. The LLM is called with temperature $T{=}0.3$, max tokens $1024$, and structured JSON output mode. Up to 6 traces are processed in parallel via thread pooling, with 2 retries on failure (exponential backoff, base 0.5s).
5	
6	\paragraph{System Prompt.}
7	
8	\begin{lstlisting}
9	You are a constraint extraction tool. Output ONLY
10	valid JSON. Do NOT solve problems, reason about
11	correctness, or think step-by-step. Extract
12	constraints from the given trace exactly as stated.
13	\end{lstlisting}
14	
15	\paragraph{Mathematical Constraint Extraction (EXTRACTION\_PROMPT).}
16	
17	Used for GSM8K and AIME datasets. The placeholder \texttt{\{trace\}} is replaced with the reasoning trace at runtime.
18	
19	\begin{lstlisting}
20	Extract mathematical constraints from this reasoning
21	trace as a JSON object.
22	
23	Rules:
24	- type: "equation", "inequality", or "predicate"
25	- expression: human-readable, e.g. "x + y == 14"
26	- z3_formula: a single comparison expression in
27	  Python Z3 syntax
28	- source_step: step number where the constraint
29	  appears
30	- Use variable names from the trace
31	
32	z3_formula MUST follow these rules:
33	- Allowed operators: ==, !=, <, >, <=, >=, +, -, *,
34	  /, **, %
35	- Use individual named variables: a1, a2, a3...
36	  NOT arrays a[1] or sets A
37	- Expand all sums explicitly:
38	  "a1 + a2 + a3 == 55" NOT "sum([a1,a2,a3])"
39	- NO Python builtins: sum(), len(), max(), min(),
40	  list(), set(), range(), int()
41	- Each z3_formula must be exactly ONE comparison
42	  (==, !=, <, >, <=, >=)
43	- For multiple values, write separate constraints
44	  for each
45	
46	Output ONLY the JSON below, nothing else:
47	{"constraints": [{"type": "equation",
48	  "expression": "x + y == 14",
49	 
…[truncated 1631 chars]

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

_source line 1752 · 2026-05-23T09:16:47.194922+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "paper_checklist.yaml",
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
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1753 · 2026-05-23T09:16:49.102741+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'symb_invariant_consensus'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1907
}
```

</details>

---


### Tool call

_source line 1754 · 2026-05-23T09:16:49.254145+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 1755 · 2026-05-23T09:16:50.008376+00:00_

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
…[truncated 23170 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 1756 · 2026-05-23T09:16:50.211287+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/project_config.yaml 2>/dev/null | head -80",
  "description": "Check project config for external review settings"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/project_config.yaml 2>/dev/null | head -80",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 1757 · 2026-05-23T09:16:50.261973+00:00_

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

_source line 1758 · 2026-05-23T09:17:00.803217+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/project_config.yaml 2>/dev/null || echo \"NOT_FOUND\"",
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
    "command": "grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/project_config.yaml 2>/dev/null || echo \"NOT_FOUND\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1759 · 2026-05-23T09:17:01.255522+00:00_

NOT_FOUND

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

_source line 1760 · 2026-05-23T09:17:01.306146+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_14/submitted.pdf 2>/dev/null || echo \"PDF_NOT_FOUND\"",
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_14/submitted.pdf 2>/dev/null || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1761 · 2026-05-23T09:17:01.406984+00:00_

-rw-r--r-- 1 ubuntu ubuntu 651385 May 23 09:08 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_14/submitted.pdf

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

_source line 1762 · 2026-05-23T09:17:05.229931+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A5 \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/project_config.yaml 2>/dev/null; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/ --include=\"*.yaml\" --include=\"*.yml\" -l 2>/dev/null | head -5",
  "description": "Search for external review config across yaml files"
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
    "command": "grep -A5 \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/project_config.yaml 2>/dev/null; grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/ --include=\"*.yaml\" --include=\"*.yml\" -l 2>/dev/null | head -5",
    "description": "Search for external review config across yaml files"
  }
}
```

</details>

---


### Tool result

_source line 1763 · 2026-05-23T09:17:05.330803+00:00_

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

_source line 1764 · 2026-05-23T09:17:26.796010+00:00_

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

_source line 1765 · 2026-05-23T09:17:53.592621+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 26796
}
```

</details>

---


### Tool call

_source line 1766 · 2026-05-23T09:17:53.743953+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026 via ACL Rolling Review (ARR)\n- **Deadline**: 2026-05-25\n- **格式**: ACL 模板, double-blind, 正文 8 页限制, 引用无限制\n- **Limitations**: 必须有，放在正文 conclusion 之后、references 之前，不计入页数\n- **匿名规则**: double-blind\n\n## 论文路径\n- LaTeX: `projects/symb_invariant_consensus/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_14/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. Proposition 1 + Corollary 1 的证明严谨性\n- Source-Attribution Degeneration 的证明是否完整？假设是否充分？\n- Corollary 1 (Information Ceiling via DPI) 是否 trivial？贡献何在？\n- Proposition 1 Part(i) 依赖 SICA 特定的 source-attribution scoring (Eq.3)——这是否足以支撑 \"structural\" 的声称？\n- Remark 中 semantic evaluation 的讨论是否充分？\n\n### 2. 统计方法与功效\n- McNemar exact test + BH correction 是否适当？\n- TOST equivalence test margin ±2pp 是否有先验依据？需要 sensitivity analysis 吗？\n- Bootstrap CI 方法是否合理？\n- 16 个条件中 10 个 underpowered (MDE ≥ 1.86pp)——论文如何处理 power 不足问题？\n- Multi-seed replication 覆盖率（仅 2/6 模型）是否足够？\n\n### 3. 实验设计\n- 6 个模型 × 3 个推理域的覆盖是否充分？\n- K=12, T=0.7 的参数选择是否合理？有无 sensitivity analysis？\n- GSM8K (n=30) 和 AIME (n=22) 的小样本是否应与大样本条件区分处理？\n- Oracle control 的设计是否充分验证了 MAX-SAT 机制本身的有效性？\n\n### 4. 诊断框架有效性\n- \"100% accuracy across 60 conditions\" 是否存在 in-sample overfitting？\n- Holdout 验证仅 1 个条件 (LLaMA-3.1-8B × FOLIO)——是否充分？\n- 60 条件全为 negative cases——trivial classifier 也能 100%？\n\n### 5. Bias Ratio (BR) 指标\n- BR > 1 有多少是 base-rate effect (60% traces → 60% constraints support majority)?\n- 是否需要 permutation null model 来量化 excess bias？\n- Shuffle control 是否充分排除了循环论证？\n\n### 6. α 参数敏感性\n- α=0.5 无理论依据——≥99% agreement 是 ceiling effect 还是真正的鲁棒性？\n\n### 7. Cross-architecture escape (§6)\n- 仅 6 个条件，仅 Mistral-7B (SC=39.33%) 显著——\"capability-gap pattern\" 是否被过度推断？\n- Spearman ρ=1.0 (n=6) 的统计意义如何？\n\n请按 ARR 标准给出完整审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (1-5 scale per EMNLP 2026 ARR) → Confidence。"
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
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026 via ACL Rolling Review (ARR)\n- **Deadline**: 2026-05-25\n- **格式**: ACL 模板, double-blind, 正文 8 页限制, 引用无限制\n- **Limitations**: 必须有，放在正文 conclusion 之后、references 之前，不计入页数\n- **匿名规则**: double-blind\n\n## 论文路径\n- LaTeX: `projects/symb_invariant_consensus/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_14/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. Proposition 1 + Corollary 1 的证明严谨性\n- Source-Attribution Degeneration 的证明是否完整？假设是否充分？\n- Corollary 1 (Information Ceiling via DPI) 是否 trivial？贡献何在？\n- Proposition 1 Part(i) 依赖 SICA 特定的 source-attribution scoring (Eq.3)——这是否足以支撑 \"structural\" 的声称？\n- Remark 中 semantic evaluation 的讨论是否充分？\n\n### 2. 统计方法与功效\n- McNemar exact test + BH correction 是否适当？\n- TOST equivalence test margin ±2pp 是否有先验依据？需要 sensitivity analysis 吗？\n- Bootstrap CI 方法是否合理？\n- 16 个条件中 10 个 underpowered (MDE ≥ 1.86pp)——论文如何处理 power 不足问题？\n- Multi-seed replication 覆盖率（仅 2/6 模型）是否足够？\n\n### 3. 实验设计\n- 6 个模型 × 3 个推理域的覆盖是否充分？\n- K=12, T=0.7 的参数选择是否合理？有无 sensitivity analysis？\n- GSM8K (n=30) 和 AIME (n=22) 的小样本是否应与大样本条件区分处理？\n- Oracle control 的设计是否充分验证了 MAX-SAT 机制本身的有效性？\n\n### 4. 诊断框架有效性\n- \"100% accuracy across 60 conditions\" 是否存在 in-sample overfitting？\n- Holdout 验证仅 1 个条件 (LLaMA-3.1-8B × FOLIO)——是否充分？\n- 60 条件全为 negative cases——trivial classifier 也能 100%？\n\n### 5. Bias Ratio (BR) 指标\n- BR > 1 有多少是 base-rate effect (60% traces → 60% constraints support majority)?\n- 是否需要 permutation null model 来量化 excess bias？\n- Shuffle control 是否充分排除了循环论证？\n\n### 6. α 参数敏感性\n- α=0.5 无理论依据——≥99% agreement 是 ceiling effect 还是真正的鲁棒性？\n\n### 7. Cross-architecture escape (§6)\n- 仅 6 个条件，仅 Mistral-7B (SC=39.33%) 显著——\"capability-gap pattern\" 是否被过度推断？\n- Spearman ρ=1.0 (n=6) 的统计意义如何？\n\n请按 ARR 标准给出完整审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (1-5 scale per EMNLP 2026 ARR) → Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 1767 · 2026-05-23T09:18:16.666948+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22922
}
```

</details>

---


### Tool call

_source line 1768 · 2026-05-23T09:18:16.819102+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性**审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026 via ACL Rolling Review (ARR)\n- **Deadline**: 2026-05-25\n- **格式**: ACL 模板, double-blind, 正文 8 页限制, 引用无限制\n- **Limitations**: 必须有，放在正文 conclusion 之后、references 之前，不计入页数\n- **匿名规则**: double-blind\n\n## 论文路径\n- LaTeX: `projects/symb_invariant_consensus/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_14/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 核心新颖性评估\n- \"Symbolic Confirmation Bias (SCB)\" 与 Huang et al. (ICLR 2024) self-correction failure、Wan et al. (2025) CoT confirmation bias、Jhaveri & Kersting (2026) 的关系如何？\n- SCB 是否是已知 self-correction limitation 在 FOL/symbolic 载体上的直接实例化？\n- Proposition 1 + Corollary 1 的理论贡献是否足够新颖？DPI 推论是否 trivial？\n- 论文声称 \"extending\" Huang et al. ——形式化框架完全不同(Huang: value/policy iteration; 本文: DPI + source attribution)，这个声称是否合理？\n\n### 2. 贡献定位与 Scope\n- 标题 \"Do Not Substantially Improve\" 是否与统计功效 (power < 21%) 匹配？\n- \"27 training-free variants\" 的 scope 是否被准确限定？这些变体是否都在 constraint-extraction-aggregation paradigm 内？\n- 三个诊断工具作为 \"contribution\" 是否过强？（100% accuracy 可能是 in-sample）\n- 论文在 SICA-specific claims 和 general claims 之间是否存在 scope 震荡？\n\n### 3. Related Work 覆盖\n- 是否遗漏重要的 self-verification / neuro-symbolic 工作？\n- Training-based verification (S²R, DuPO, AlphaCode, CodeT) 是否充分讨论了 Proposition 1 的适用边界？\n- Self-correction survey (Kamoi et al., TACL 2024) 是否引用？\n- Cross-model independence auditing (Kuai et al., 2026) 的引用和讨论是否充分？\n\n### 4. 写作质量\n- Abstract 信息密度是否过高？6 个核心发现是否应该精简？\n- K_eff 是否需要更多直觉解释（给非 ensemble-theory 背景读者）？\n- §2 Related Work 段间逻辑衔接是否清晰？\n- \"Symbolic Mirage\" 术语是否过度品牌化/dramatic？\n- 符号/指标过载问题（8 页内 BR, K_eff, C_0, κ, σ, α 等）\n\n### 5. 格式合规\n- 正文是否在 8 页限制内？\n- Limitations section 是否存在且位置正确？\n- 是否有违反 double-blind 的信息？\n- 引用格式是否符合 ACL/natbib 规范？\n\n### 6. Negative Result 论文的价值\n- 作为 negative result，本文是否提供了足够深入的失败机制分析？\n- 对社区的指导意义如何？诊断框架和 independence principle 是否有实际价值？\n- 是否为后续工作指明了清晰方向？\n\n请按 ARR 标准给出完整审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (1-5 scale per EMNLP 2026 ARR) → Confidence。"
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
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性**审查。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026 via ACL Rolling Review (ARR)\n- **Deadline**: 2026-05-25\n- **格式**: ACL 模板, double-blind, 正文 8 页限制, 引用无限制\n- **Limitations**: 必须有，放在正文 conclusion 之后、references 之前，不计入页数\n- **匿名规则**: double-blind\n\n## 论文路径\n- LaTeX: `projects/symb_invariant_consensus/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_14/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 核心新颖性评估\n- \"Symbolic Confirmation Bias (SCB)\" 与 Huang et al. (ICLR 2024) self-correction failure、Wan et al. (2025) CoT confirmation bias、Jhaveri & Kersting (2026) 的关系如何？\n- SCB 是否是已知 self-correction limitation 在 FOL/symbolic 载体上的直接实例化？\n- Proposition 1 + Corollary 1 的理论贡献是否足够新颖？DPI 推论是否 trivial？\n- 论文声称 \"extending\" Huang et al. ——形式化框架完全不同(Huang: value/policy iteration; 本文: DPI + source attribution)，这个声称是否合理？\n\n### 2. 贡献定位与 Scope\n- 标题 \"Do Not Substantially Improve\" 是否与统计功效 (power < 21%) 匹配？\n- \"27 training-free variants\" 的 scope 是否被准确限定？这些变体是否都在 constraint-extraction-aggregation paradigm 内？\n- 三个诊断工具作为 \"contribution\" 是否过强？（100% accuracy 可能是 in-sample）\n- 论文在 SICA-specific claims 和 general claims 之间是否存在 scope 震荡？\n\n### 3. Related Work 覆盖\n- 是否遗漏重要的 self-verification / neuro-symbolic 工作？\n- Training-based verification (S²R, DuPO, AlphaCode, CodeT) 是否充分讨论了 Proposition 1 的适用边界？\n- Self-correction survey (Kamoi et al., TACL 2024) 是否引用？\n- Cross-model independence auditing (Kuai et al., 2026) 的引用和讨论是否充分？\n\n### 4. 写作质量\n- Abstract 信息密度是否过高？6 个核心发现是否应该精简？\n- K_eff 是否需要更多直觉解释（给非 ensemble-theory 背景读者）？\n- §2 Related Work 段间逻辑衔接是否清晰？\n- \"Symbolic Mirage\" 术语是否过度品牌化/dramatic？\n- 符号/指标过载问题（8 页内 BR, K_eff, C_0, κ, σ, α 等）\n\n### 5. 格式合规\n- 正文是否在 8 页限制内？\n- Limitations section 是否存在且位置正确？\n- 是否有违反 double-blind 的信息？\n- 引用格式是否符合 ACL/natbib 规范？\n\n### 6. Negative Result 论文的价值\n- 作为 negative result，本文是否提供了足够深入的失败机制分析？\n- 对社区的指导意义如何？诊断框架和 independence principle 是否有实际价值？\n- 是否为后续工作指明了清晰方向？\n\n请按 ARR 标准给出完整审稿报告：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (1-5 scale per EMNLP 2026 ARR) → Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 1769 · 2026-05-23T09:18:18.230343+00:00_

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

_source line 1770 · 2026-05-23T09:18:22.639172+00:00_

Round 1 已启动：
- 视觉审查 Agent：已派发（fire-and-forget）
- Reviewer 1（方法严谨性 + 实验设计）：已分配
- Reviewer 2（新颖性 + 完整性）：已分配

等待两位 Reviewer 返回初审结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 122

## Round 122

2 recorded events


### User

_source line 1771 · 2026-05-23T09:25:35.175186+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 审稿报告：新颖性 + 完整性审查

**论文**: "Beyond Self-Consistency: Self-Extracted Constraints Do Not Substantially Improve LLM Logical Reasoning"
**Venue**: EMNLP 2026 via ACL Rolling Review

---

## Summary

本文引入 SICA（Symbolic Invariant Consensus Aggregation），从 LLM 的 chain-of-thought traces 中提取 FOL 约束并通过加权 MAX-SAT 聚合。尽管 Z3 验证通过率达 99%，SICA 在 94.4% 的问题上与多数投票结果一致（6 个模型，7B-32B，3 个推理领域）。论文将此现象形式化为 "Symbolic Confirmation Bias"（SCB），基于 Data Processing Inequality（DPI）证明 BR ≥ 1（Proposition 1），表明自提取约束无法超越 trace 本身的信息量。测试 27 个 training-free 变体均产生中性至负面结果。提出三个零成本诊断工具（C₀, BR, K_eff）并展示跨架构验证作为突破瓶颈的方向。

---

## 主要优势

**S1. 实验规模与方法论严谨性出色。** 9 个模型（7B-32B）、3 个推理领域（FOLIO, ProofWriter, StrategyQA/LogiQA/AIME/ARC-Challenge）、27 个 training-free 变体的全面覆盖。统计方法完备：TOST 等价性检验、McNemar 检验、bootstrap CI、FDR 校正、统计功效分析。这是该领域最系统的 negative result 研究之一。

**S2. 诊断框架具有实际价值。** C₀（多候选退化率）、BR（偏差比）、K_eff（有效集成大小）三个指标可在不运行完整实验的情况下预测 self-extraction 方法的成败，对从业者具有直接指导意义（§5.3, Figure 4）。

**S3. 因果分析链条清晰。** 从现象（SICA ≈ SC）到机制（trace-count 分布决定约束分布）到理论（DPI Markov chain）到逃逸条件（跨架构独立性），叙事层层递进。Figure 3 的因果 DAG 和 Figure 1 的 pipeline 图有效辅助理解。

**S4. 跨架构逃逸发现有启示性。** §6 的 cross-generator NLI 实验（Table 3）展示独立验证器可将 SC 提升至 72%+，为后续研究指明了清晰方向——这从 negative result 中提炼出了 constructive 的贡献。

**S5. 诚实的统计报告。** 论文坦承 10/16 条件统计功效不足（power < 21%），并在 Limitations 中明确列出模型范围、语言、数据集等局限。这种透明度在 negative result 论文中值得肯定。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 标题的普遍性声明与统计证据不匹配

- 具体位置：Title, Abstract ("We show the answer is no"), §4 Table 1
- 问题：标题 "Do Not Substantially Improve" 暗示一个普遍性结论，但论文自身的 TOST 分析（Appendix D, Table 6）显示：仅 4/16 主条件通过等价性检验（±2pp），2 个条件显示显著负面效果，**10 个条件因统计功效不足（power < 21%）无法判定**。Abstract 声称 "four conditions confirm equivalence within ±2pp, though ten remain underpowered" 但紧接着用 "We show the answer is no" 做总结，逻辑上不一致——underpowered ≠ equivalent。
- 为什么影响接收：Reviewer 和读者会将标题作为 take-home message。在 10/16 条件 underpowered 的情况下做普遍性声明，有 overclaim 风险。EMNLP/ARR 对 claim 与 evidence 的匹配要求严格。
- 建议修改方向：标题改为限定性表述，如 "Self-Extracted Constraints Show No Significant Improvement..."；或在 Abstract 中明确区分 "confirmed equivalent" vs. "underpowered/inconclusive"，不将两者混为一谈。

**N2** [critical] Proposition 1 的 Markov chain 假设缺乏显式论证

- 具体位置：§5.1 Proposition 1, Figure 3 (p6-7)
- 问题：Proposition 1 的核心依赖 Markov chain M → T → A → C → S，其中 C（约束）条件独立于 M（模型）given T（trace）。但 SICA pipeline 中，约束提取使用**同一模型**的**另一次 LLM 调用**重新处理 trace（Appendix A 的 extraction prompt）。如果同一模型生成 trace 并提取约束，模型的 shared latent representations（权重、attention patterns）可能导致 C 和 M 之间存在 T 无法屏蔽的依赖关系，违反条件独立性。论文 §5.1 讨论了 "trace-determined" 但未直接论证 Markov 性质为何成立。
- 为什么影响接收：Proposition 1 是全文理论框架的基石。如果 Markov 假设不成立，BR ≥ 1 的保证不再有效，整个 "structural" argument 需要重新审视。
- 建议修改方向：(1) 明确论证在什么条件下 Markov 假设成立（例如，extraction prompt 只访问 trace 文本而非模型内部状态）；(2) 讨论假设可能失效的场景（例如，模型在 extraction 时使用与 trace generation 相同的 in-context learning patterns）；(3) 如果假设是近似的，量化偏离程度。

**N3** [critical] SCB 与已有 confirmation bias 工作的新颖性区分不充分

- 具体位置：§2 Related Work (p2-3), §5.1 (p5-6)
- 问题：Wan et al. (2025, ACL Findings) 的 "Unveiling Confirmation Bias in Chain-of-Thought Reasoning" 已经证明 model beliefs 通过 CoT 过程产生 confirmation bias，扭曲推理生成和答案预测。本文的 SCB 本质上是同一现象在 FOL/constraint extraction 载体上的实例化。论文 §2 引用了 Wan et al. 但仅一句带过（"symbolic confirmation bias is distinct from CoT unfaithfulness"），未直接对比 SCB 与 Wan et al. 的 CoT confirmation bias 在概念上的重叠与差异。同样，Jhaveri & Kersting (2026) 在 rule-discovery 任务中发现类似 confirmation bias，进一步削弱了 SCB 作为独立发现的新颖性。
- 为什么影响接收：如果 SCB 是 CoT confirmation bias 的直接推论而非独立发现，论文的核心贡献从 "发现新现象 + 形式化" 降级为 "在新载体上验证已知现象 + 形式化"。这仍有价值但需要诚实定位。
- 建议修改方向：在 §2 或 §5.1 中增加显式对比段落：(1) Wan et al. 的 CoT confirmation bias 是关于推理过程的 behavioral 观察；(2) SCB 的增量贡献在于 DPI 形式化和 source-attribution scoring 机制，以及在 formal verification pipeline 中的具体表现；(3) 明确承认 SCB 是 confirmation bias 在 symbolic verification 中的具体实例化，而非全新概念。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] DPI 推论（Proposition 1 + Corollary 1）的理论贡献度偏弱

- 具体位置：§5.1 Proposition 1, Corollary 1 (p6)
- 问题：给定 Markov chain M → T → A → C → S，BR ≥ 1 和 I(C;Y) ≤ I(T;Y) 是 DPI 的直接应用，推导过程本身不含非显然步骤。Corollary 1 尤其接近 trivial——"从 trace 提取的约束所含信息不超过 trace 本身"几乎是同义反复。论文将其列为第一个贡献（"We systematically diagnose symbolic confirmation bias as the mechanism"），但理论新颖性主要在于*选择了正确的 Markov chain 建模*，而非推导本身。
- 建议：在论文中明确区分贡献的层次——modeling contribution（识别正确的 DAG/Markov chain）vs. derivation contribution（DPI 应用），并适当降低 Corollary 1 的声称强度。

**W2** [warning] 诊断框架的 "100% accuracy" 声称部分为 in-sample

- 具体位置：§5.3 (p7), Abstract ("Three zero-cost diagnostics correctly classify all 60 tested conditions"), Figure 4
- 问题：三个诊断工具的决策边界（C₀ ≤ .52, K_eff ≤ 1.30, BR combined with SC regime）是从实验数据中拟合的，而 "100% accuracy" 的评估也在同一数据集上。虽然 §5.3 提到在两个 held-out 模型系列（LLaMA-3.1-8B, Qwen3-14B）上做了前瞻性验证，但 held-out 的是模型而非条件设计，且仅 2 个模型系列。
- 建议：(1) 明确标注哪些结果是 in-sample fitting、哪些是 out-of-sample validation；(2) 将 "correctly classify all 60 conditions" 改为 "correctly classify all 60 conditions in our experimental setting, including prospective validation on 2 held-out model families"；(3) 讨论边界在分布外场景（如 >32B 模型、非英语、非 FOL 领域）的预期鲁棒性。

**W3** [warning] Scope 震荡：SICA-specific claims vs. 一般性 claims

- 具体位置：§1 contributions (p2), §5.2 (p7), §7 (p8)
- 问题：论文在两个 scope 之间摆动：(a) "SICA fails"（specific）和 (b) "any self-extraction-based aggregation method within the constraint-extraction-aggregation paradigm fails"（general）。Proposition 1 的理论声称是 (b)，但 27 个变体的实验验证主要是 SICA 及其衍生方法（均在同一 extraction-aggregation paradigm 内）。§5.2 声称 "the pattern reveals a fundamental independence-accuracy trade-off" 暗示普遍性，但 §7 的 Discussion 又缩回 "within the constraint-extraction-aggregation paradigm"。
- 建议：在 §1 的 contributions 中明确界定 scope："我们的理论结果适用于任何 trace-to-constraint extraction pipeline（Proposition 1）；我们的实验验证覆盖了该 paradigm 内的 27 个代表性变体"。

**W4** [warning] K_eff 对非 ensemble-theory 背景读者的可读性不足

- 具体位置：§3.1 Eq. (1) (p3)
- 问题：K_eff = K/[1+(K-1)·κ] 通过 Fleiss' κ 和 Ladha (1992) 引入，但对不熟悉 ensemble diversity 理论的读者（NLP 社区中占多数），缺少直觉解释。K_eff 是论文的核心诊断指标之一，理解障碍会影响论文的可读性和影响力。
- 建议：在 Eq. (1) 后加一个具体示例，如 "With K=12 traces and inter-trace agreement κ=0.7, the effective ensemble size reduces to K_eff ≈ 1.3, meaning 12 highly correlated traces carry roughly the same information as 1.3 independent ones."

**W5** [warning] "Symbolic Mirage" 术语过度品牌化

- 具体位置：§5 标题 (p5)
- 问题："The Symbolic Mirage" 作为 section 标题带有不必要的修辞色彩。论文已有 "Symbolic Confirmation Bias" 这一技术性术语来描述同一现象。"Mirage" 暗示一种刻意的欺骗性，与实际的技术机制（trace-count 分布决定约束分布）不匹配。
- 建议：将 §5 标题改为更技术性的表述，如 "Analysis of Symbolic Confirmation Bias" 或 "Why Self-Extraction Degenerates"。

---

## 小问题（不影响接收）

- **符号过载**：正文 8 页内引入了 BR, K_eff, C₀, κ, σ, α, Δ, score(a), CCR, ProcessSim 等大量符号/指标。建议将 CCR 和 ProcessSim 的定义移至 Appendix，正文仅引用结论。
- **Abstract 信息密度过高**：一个段落包含 ~6 个核心发现。建议以中心 negative finding 和机制为主线，将 scope 和 escape 发现精简为 1-2 句。
- **§2 Related Work 段间衔接**：三个子节（Self-consistency/ensemble theory, Neuro-symbolic reasoning, Test-time compute/self-verification）之间缺少显式逻辑连接句。读者需自行推断各节与本文研究问题的关系。
- **Table 1 排版密度**：Table 1（p5）压缩了大量信息（11 个模型-领域条件 × 5 列），字体较小。考虑拆分为两个子表或增加水平间距。
- **Appendix 表格编号跳跃**：例如从 Table 8 跳到 Table 9，再到 Table 12，编号不连续可能造成交叉引用困惑。

---

## Questions to Authors

**Q1.** Proposition 1 依赖 M→T→A→C→S 的 Markov chain。当 extraction 使用同一模型的另一次调用时，模型权重构成 C 和 M 之间的隐式依赖。你们是否有实验证据表明这种依赖在实践中可忽略（例如，用不同模型做 extraction 是否改变 BR 的分布）？

**Q2.** 10/16 条件的统计功效不足（power < 21%）。如果将样本量增加到使 power 达到 80% 的水平（对 ±2pp 效应），你们预期结论是否会改变？是否有 pilot 数据暗示某些 underpowered 条件实际上可能显示正面效果？

**Q3.** 诊断框架在 >32B 模型（如 LLaMA-3-70B, Qwen-72B）上的预期表现如何？K_eff 和 BR 是否会因模型能力提升而表现出不同的分布？论文 Limitations 提到模型范围 7B-32B，但不清楚这是资源限制还是有理论原因预期更大模型表现不同。

**Q4.** Cross-architecture escape（§6）中，DeBERTa-large-mnli 作为验证器在 FOLIO 上将 SC 提升至 ~49.5%（Table 3）。但该验证器本身是在 NLI 数据上 fine-tune 的，这是否引入了 Proposition 1 不覆盖的 external supervision signal？换言之，这个 "escape" 是否本质上是因为违反了 Proposition 1 的前提（无外部反馈），而非突破了 information ceiling？

---

## Missing References

1. **Wan et al. (2025)** — 论文已引用但讨论不足。SCB 与 CoT confirmation bias 的关系需要更深入的对比分析（见 N3）。
2. **Reflexion (Shinn et al., 2023)** — 作为 verbal self-reflection 的代表性工作，在 self-verification landscape 中占重要位置，但论文未提及。
3. **LATS (Zhou et al., 2023)** — Language Agent Tree Search 通过树搜索实现 self-verification，是 training-free verification 的另一范式，可能不在 constraint-extraction paradigm 内，但值得在 Related Work 中定位。
4. **STaR (Zelikman et al., 2022)** — Self-Taught Reasoner 是 training-based self-improvement 的奠基性工作。论文讨论了 training-based verification 但未引用此具体工作。
5. 建议检查 Kuai et al. (2026) 的引用深度——论文引用了但仅在 Related Work 一笔带过，考虑到 cross-model independence 是本文 §6 的核心 escape mechanism，应更充分讨论其方法与发现。

---

## 格式合规

- **页数**：正文 8 页（含 Limitations），合规 ✓
- **Limitations**：存在，位于 §7 Discussion and Conclusion 之后、References 之前，合规 ✓
- **匿名性**：首页标注 "Anonymous ACL submission"，未发现明显违反 double-blind 的信息 ✓
- **引用格式**：使用 natbib 风格，parenthetical 和 textual citations 混合使用，合规 ✓
- **Appendix**：18 页 appendix 提供详尽的实验细节、prompts、额外分析，增强可重复性 ✓

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验方法论严谨（TOST, bootstrap CI, power analysis），但 Proposition 1 的 Markov chain 假设未充分论证（N2），标题与统计证据不完全匹配（N1） |
| Excitement | 3.0/5 | Negative result 有价值，诊断框架和跨架构发现有实际意义，但核心发现（自提取约束受 confirmation bias 影响）与 Wan et al. (2025) 等已有工作重叠较大（N3），降低了新颖性感知 |
| Reproducibility | 4/5 | 提供完整 prompt（Appendix A）、超参数设置（§3.2）、统计方法细节（Appendix D），但未提及代码/数据公开计划 |
| Confidence | 4/5 | Self-verification 和 neuro-symbolic reasoning 是我的研究领域，对统计方法和实验设计有充分把握 |

## 总体评分

**Overall**: 3.5 — Borderline Conference

**一句话总结**: 实验设计出色的 negative result 研究，但理论贡献度（DPI 直接应用）和核心发现新颖性（与 CoT confirmation bias 重叠）不足以支撑 conference-level 论文；跨架构逃逸发现和诊断框架是亮点，建议加强新颖性区分后适合 Findings。

**作为 negative result 论文的价值评估**: 本文在失败机制分析深度（Proposition 1 的 DPI 框架 + BR/K_eff 的实证验证）和实验覆盖广度（27 变体）方面超越了大多数 negative result 工作。诊断框架对社区有实际指导意义——从业者可以用 C₀ 和 K_eff 在 pilot run 中快速判断 self-extraction 方法是否值得全面部署。independence principle 为后续工作提供了明确方向。但如果核心洞察可以总结为 "self-extracted constraints inherit the model's distributional prior"——这在 Huang et al. (2024) 和 Wan et al. (2025) 之后已非 surprising——则论文的主要贡献在于 rigor of confirmation 而非 novelty of insight，更适合 Findings track。


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

_source line 1772 · 2026-05-23T09:25:41.872127+00:00_

Reviewer 2 报告已收到。等待 Reviewer 1 报告后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 123

## Round 123

2 recorded events


### User

_source line 1773 · 2026-05-23T09:25:52.758142+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**总结**：Overall 3.5（Borderline Conference）。主要问题集中在三个 critical 点：(1) 标题 "Do Not Substantially Improve" 与统计证据不匹配（10/16 条件 underpowered）；(2) Proposition 1 的 Markov chain 假设未显式论证（同一模型做 extraction 可能违反条件独立性）；(3) SCB 与 Wan et al. (2025) 的 CoT confirmation bias 新颖性区分不充分。实验规模和方法论严谨性是明确优势，诊断框架和跨架构逃逸发现有实际价值，建议加强新颖性定位后适合 Findings。

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

_source line 1774 · 2026-05-23T09:25:58.753513+00:00_

Reviewer 2 报告已收到（Overall 3.5）。等待 Reviewer 1 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 124

## Round 124

6 recorded events


### User

_source line 1775 · 2026-05-23T09:26:06.994028+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿报告：方法严谨性 + 实验设计

**论文标题**: Beyond Self-Consistency: Self-Extracted Constraints Do Not Substantially Improve LLM Logical Reasoning

---

## 总体评分

**Overall Assessment**: 3.5 — Borderline Conference
**一句话总结**: 一篇实验覆盖面广的系统性否定结果论文，核心发现（自提取约束退化为多数投票）具有实用价值，但 Proposition 1 的证明存在关键缺口、统计功效不足覆盖面太大、诊断框架仅在全阴性样本上验证，削弱了理论贡献的可信度。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 实验方法论基本合理，但 Proposition 1 证明有逻辑跳跃；16个条件中10个统计功效不足；诊断框架无正例验证 |
| Excitement | 3/5 | 系统性否定结果有社区价值，诊断工具实用，但贡献主要是"此路不通"而非开辟新方向；cross-architecture escape 数据太少难以激发后续研究 |
| Reproducibility | 4/5 | 数据集公开，超参数明确，extraction prompt 完整附于 Appendix A；但 multi-seed replication 仅覆盖 2/6 模型 |
| Confidence | 4/5 | 仔细检查了数学证明、统计方法和实验设计 |

---

## Summary

本文研究自提取约束（通过 SICA 管线：LLM 生成推理 trace → 提取 FOL 约束 → Z3 验证 → MAX-SAT 加权聚合）能否超越 Self-Consistency (SC)。在 6 个模型 × 3 个推理域上，无条件显示显著正向效果（BH 校正后）。论文将此归因于"源归属退化"：自提取约束系统性地与模型多数答案对齐（BR 1.66×–4.97×），使 MAX-SAT 聚合退化为多数投票。Proposition 1 形式化了这一退化机制，Corollary 1 通过 DPI 建立信息上界。三个零成本诊断指标（C₀, K_eff, BR）在 60 个条件上实现 100% 分类准确率。§6 探索了 cross-architecture 逃逸，发现仅在生成器能力远低于验证器时有显著增益。

---

## 主要优势

**S1. 系统性实验覆盖**：6 模型 × 3 域 × 多 seed/超参数扫描，加上 27 种修复策略（Figure 4），构成了迄今最全面的约束提取聚合范式评估。22 种 training-free 变体均产生 neutral-to-negative 结果（§5.2, Figure 4），排除了简单修复的可能性。

**S2. 因果分析链条清晰**：从 confirmation bias 现象（BR > 1, Table 2）→ 源归属退化机制（Proposition 1）→ 信息上界（Corollary 1）→ 退化诊断（C₀, K_eff）→ 逃逸条件（§6），构成完整的解释框架。Case studies（§F, Cases 1–3）具体展示了约束如何系统性地映射源 trace 偏见。

**S3. Oracle 对照设计**：用 gold FOL 标注替换自提取约束（§G），MAX-SAT 在 Mistral-7B FOLIO 上产生 +29.91pp 增益（Appendix G），明确定位瓶颈在约束提取而非求解器，避免了对 MAX-SAT 机制本身的混淆。

**S4. 统计方法选择得当**：McNemar exact test 适合成对二分类；BH 校正控制 FDR；TOST 等价检验补充了"无差异"的正向证据；bootstrap CI 提供非参数置信区间。方法论整体合理。

**S5. Honest negative result**：论文坦诚报告否定结果，未试图通过 cherry-picking 条件或选择性报告来夸大发现。Limitations 节直接承认 power 不足和模型覆盖局限。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Proposition 1 证明存在关键逻辑跳跃

- **具体位置**：§5.1 Proposition 1 Part (i)；Appendix 中的 proof（对应 analysis.tex）
- **问题**：证明声称 "By definition, score(a) = Σ 1[aᵢ = a] = nₐ"，但 SICA 的实际评分函数（Eq. 3）是 score(a) = Σ_{c∈C*} wc·σ(c,a) − α·Σ_{c∈C\} wc·σ(c,a)，涉及约束权重 wc（去重后的 trace 计数）和源归属指示函数 σ(c,a)。从 Eq. 3 到 score(a) = nₐ 需要证明：(1) 退化条件下 |C\| ≈ 0 使惩罚项消失；(2) 不同答案组的约束不重叠；(3) 每条 trace 的有效约束贡献使 Σ wc 精确等于 nₐ 而非仅成比例。论文报告 42.9% 去重率（§3.1），这意味着约束权重分布不均匀，不同 trace 产生的约束数量不同。证明跳过了这些中间步骤，直接从定义出发得出 score(a) = nₐ，但 Eq. 3 的定义并非如此。
- **为什么影响接收**：Proposition 1 是全文核心理论贡献，支撑了 §5 整个 symbolic mirage 叙事。证明不完整使得理论贡献从"形式化证明"降级为"经验观察"，削弱了论文的核心价值主张。
- **建议修改方向**：(a) 完善证明，明确列出所有假设（如约束跨答案组不重叠、权重均匀化条件），证明 Eq. 3 在这些假设下精确或近似退化为 nₐ；或 (b) 弱化 claim——不声称 score(a) = nₐ（exact equality），而证明 argmax score(a) = argmax nₐ（ranking preservation），这仅需证明 score 与 n 单调关系，门槛更低且足以支撑主要结论；(c) 补充经验验证——在实际数据上计算 score(a) 与 nₐ 的 Spearman 相关或 rank agreement。

**N2** [critical] 统计功效不足覆盖面过大，削弱否定结论的普遍性

- **具体位置**：Table 6 (Appendix D)；§4 Results 第一段
- **问题**：16 个非退化条件中 10 个 underpowered（MDE ≥ 1.86pp），包括所有 n ≤ 600 的条件。GSM8K (n=30) 和 AIME (n=22) 的样本量极小，在主结果 Table 1 中与 n=204 的条件并列展示，未区分处理。论文用 TOST 等价检验部分缓解了这一问题，但 ±2pp margin 下仅 4/16 条件达到等价，10 条件"underpowered/inconclusive"——这意味着论文无法区分"SICA 无效"和"样本不够大"两种解释。
- **为什么影响接收**：论文标题声称 "Do Not Substantially Improve"，但 10/16 条件的证据强度不足以支撑这一全称判断。否定结论需要比肯定结论更高的证据标准（proving a negative），当前 power 不足使核心 claim 的证据不够 decisive。
- **建议修改方向**：(a) 在 Table 1 和正文中明确区分 powered 条件（n ≥ 800, MDE < 1.5pp）和 underpowered 条件，将 GSM8K/AIME 的小样本结果移至附录或标注为 exploratory；(b) 修改结论措辞，限定为"在 powered conditions 下无显著改善，在 underpowered conditions 下方向一致但证据不充分"；(c) 或增加样本量——至少对 2-3 个关键条件重复实验以达到 80% power at MDE=2pp。

**N3** [critical] 诊断框架 100% 准确率可能是 trivial classifier + in-sample overfitting

- **具体位置**：§5.3 Diagnostic Framework；Table 5 (Appendix C)
- **问题**：60 个条件全部为 null 或 negative，trivial classifier（"总是预测无效果"）也能达到 100% 准确率。诊断框架的价值在于区分"何时有效 vs 何时无效"，但数据中没有任何正例验证框架的阳性预测能力。Holdout 验证仅 2 个条件（LLaMA-3.1-8B 和 Qwen3-14B on FOLIO），且同为 negative cases。决策边界（C₀ < 5%, K_eff ≤ 1.30）从训练数据推导并在同一数据上评估，存在 in-sample overfitting 风险。
- **为什么影响接收**：论文将诊断框架列为三大贡献之一（Contribution 2），但框架的区分能力（discriminative power）未经验证。§7 Discussion 中推荐将此框架用于 a priori 预测（"practitioners with a prior prediction of aggregation viability from a pilot run"），但无正例的框架无法可靠预测何时 self-extraction *会* 有效。
- **建议修改方向**：(a) 明确承认框架仅在 negative cases 上验证，不宜用于 positive prediction；(b) 用 §6 cross-architecture escape 的 Mistral-7B (SC=39.33%) 条件作为 positive validation——该条件在 cross-model 设置下产生显著增益，框架是否能预测这一 escape？如果不能，说明框架的局限性；(c) 或重新定位框架为"排除工具"（ruling out self-extraction benefit）而非"诊断工具"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Corollary 1 (DPI) 贡献定位不清

- **具体位置**：§5.1 Corollary 1；analysis.tex lines 57-65
- **问题**：Corollary 1 声称 I(C_{1:K}; Y) ≤ I(T_{1:K}; Y)，证明依赖 cᵢ = f(tᵢ) 构成 Markov chain 后直接应用 DPI。但 "deterministic function 的输出不超过输入的信息量" 是 DPI 的直接推论，几乎是信息论教科书练习题。论文承认 "The contribution is not the inequality itself but the identification of the M→T→A→C Markov chain structure"，但识别 C = f(T) 意味着 T→C 是 Markov chain 这一步骤本身是 trivial 的——这正是 deterministic function 的定义。
- **建议**：要么降低 Corollary 1 在论文中的地位（作为 remark 而非独立 corollary），要么更清楚地说明 Markov chain 识别的 non-trivial 贡献在哪里（例如，之前的工作是否假设约束提供独立于 trace 的信息？如果是，cite 具体工作并对比）。

**W2** [warning] Bias Ratio (BR) 缺少 null model 分解

- **具体位置**：§3.1 Eq. 5；Table 2
- **问题**：BR 衡量约束支持多数答案的偏倚程度，但未分解为 base-rate component + excess bias。若 60% trace 产生答案 a，则纯随机约束-答案关联也会产生 BR = 60/40 = 1.5。Table 2 的 BR 值（1.66×–4.97×）部分可能由 base rate 解释，而非"symbolic confirmation bias"。论文提到 shuffle control（§5.1, "Two controls rule out answer leakage"）表明 breaking source-attribution 消除 bias，但未提供 permutation null distribution 来量化 excess bias 的统计显著性。
- **建议**：计算每个条件的 base-rate predicted BR = n_â / max(n_{a≠â})，与观测 BR 对比，报告 excess ratio。或运行 permutation test（随机打乱约束-答案归属 1000 次），建立 null BR 分布并报告 p-value。

**W3** [warning] Cross-architecture escape (§6) 结论过度推断

- **具体位置**：§6；Table 3；Figure 8 (p.23)
- **问题**：仅 6 个 generator-verifier 条件，仅 Mistral-7B (SC=39.33%) 在 ProofWriter 上显著。Spearman ρ=1.0 (n=6, p=0.003) 虽统计显著，但 6 个点的完美单调关系极易被单个异常值打破，鲁棒性存疑。"Capability-gap pattern" 基于如此少的数据点缺乏 generalization 保障。§7 Discussion 中却进一步推断 "structurally independent verification can break the bottleneck"、"capability-gap pattern between verifier and generator (§6)"——这些表述的置信度远超数据支持。
- **建议**：(a) 增加 generator-verifier 组合（至少 10+ 条件）以稳固 capability-gap 结论；或 (b) 明确将 §6 定位为 "preliminary / exploratory observation" 而非 established finding，并在 §7 中降低对应 claim 的语气强度。

**W4** [warning] α=0.5 无理论依据，sensitivity 分析实质上确认了退化

- **具体位置**：§3.1；Table 11 (Appendix H)
- **问题**：α=0.5 的选择缺乏理论或经验依据。Table 11 显示 α∈{0.1, 0.3, 0.5, 0.7, 1.0} 时 SICA-SC agreement ≥ 99%，论文将此解释为"α 不敏感"——但这实际上是 ceiling effect：由于退化（Proposition 1），SICA 对所有 α 都退化为 SC，α 不影响结果恰恰因为它在退化体制下不起作用。论文未讨论这一解释。
- **建议**：将 α sensitivity 结果重新解释为退化的 corroborating evidence，而非方法的鲁棒性优势。同时讨论在非退化体制（如 cross-architecture 设置）下 α 的敏感性——§6 的实验是否测试了不同 α？

**W5** [warning] Multi-seed replication 覆盖率不足

- **具体位置**：Table 31 (Appendix X.1)；§4
- **问题**：仅 Mistral-7B 和 Qwen2.5-14B 在 FOLIO 上有 multi-seed replication（4 seeds 和 3 seeds）。Mistral-7B 的 4 seed 结果范围为 Δ ∈ [-4.41, +3.43]，跨越正负方向，表明单 seed 结果不稳定。其余 4 个模型均为单 seed 评估——这些结果的可靠性不确定。
- **建议**：至少对 Qwen2.5-7B 和 LLaMA-3.1-8B 补充 2-3 seed replication，或在正文中明确警告单 seed 结果的 instability（引用 Mistral-7B 的 seed variance 作为参照）。

---

## 小问题（不影响接收）

- **M1**: Figure 1 pipeline 图中 "red-dashed box: the independence bottleneck" 在 150dpi 下难以辨认，建议提高线宽或加标注。
- **M2**: Table 1 的 † 和 ‡ 符号含义在 caption 中才解释，建议添加 table footnote 使表格自包含。
- **M3**: §3.2 提到 "K=12 traces at T=0.7"，但 K 和 T 的选择理由直到 Appendix L 才详细讨论。建议在正文中简要提及 sensitivity analysis 的存在和结论。
- **M4**: "Twenty-seven training-free variants" (§5.2) 是重要的实验工作量，但 Figure 4 试图在一个小图中展示所有 27 种方法的结果，信息密度过高。
- **M5**: §2 Related Work 末尾的 "we show the errors are..." 似乎是断句，需检查排版。

---

## Questions for Authors

**Q1**: Proposition 1 的证明中，score(a) = nₐ 的精确等式如何从 Eq. 3 推导？特别是考虑到不同 trace 产生不同数量的约束、42.9% 的去重率导致权重分布不均匀。如果等式仅在 "up to monotone transformation" 意义下成立（即 argmax 保持），请明确。

**Q2**: 诊断框架在 60 个全阴性条件上实现 100% 准确率。如果一个 trivial "always predict negative" classifier 也能达到 100%，框架的附加值（over trivial baseline）具体体现在哪里？是否有任何条件（如 §6 的 cross-architecture escape）可以作为正例验证？

**Q3**: TOST 的 ±2pp equivalence margin 选择基于什么先验？在高基线条件（SC ≥ 75%）下，2pp 的相对效应量仅 ~2.7%，可能低于实际有意义的阈值。论文是否考虑过按条件基线调整 margin？

**Q4**: §6 cross-architecture 实验中，α 是否也固定为 0.5？在 cross-model 设置下约束不再完全耦合到生成器的答案分布（因为验证器独立），α 的敏感性可能不同。

**Q5**: Table 2 中 Gemini-2.5-Pro 的 BR=12.19，远高于其他模型（1.66–4.97）。这一异常值的原因是什么？Gemini 的 trace count (n_mis=12) 极少——是否因为高准确率导致 incorrect instances 样本过小而产生不稳定的 BR 估计？

---

## Missing References

- Cohen's h or other effect size measures for paired proportions（论文仅报告 pp difference，未报告标准化效应量）
- Burnell et al. (2023) "Rethink reporting of evaluation results in AI" 或类似的 negative result reporting guidelines（论文作为 negative result 论文，可引用此类方法论指南来加强 framing）

---

## Reproducibility Assessment

**4/5 — Mostly Reproducible**

优势：数据集全部公开（FOLIO, ProofWriter, GSM8K, AIME）；Appendix A 提供了完整的 extraction prompt 和 system prompt；超参数明确（K=12, T=0.7, α=0.5, Z3 timeout=10s）；统计方法完整描述。

不足：multi-seed replication 仅覆盖 2/6 模型；MAX-SAT 求解器的具体实现细节（Python Z3 binding 版本、constraint encoding 细节）未完全说明；cross-architecture 实验的 DeBERTa fine-tuning 细节（learning rate, epochs, data splits）需查看代码。


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

_source line 1776 · 2026-05-23T09:26:45.430654+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix/Should-Fix/Minor 点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿原文\n\n### Must-Fix 问题\n\n**N1** [critical] Proposition 1 证明存在关键逻辑跳跃\n- 证明声称 \"By definition, score(a) = Σ 1[aᵢ = a] = nₐ\"，但 SICA 的实际评分函数（Eq. 3）是 score(a) = Σ_{c∈C*} wc·σ(c,a) − α·Σ_{c∈C\\} wc·σ(c,a)，涉及约束权重 wc 和源归属指示函数 σ(c,a)。从 Eq. 3 到 score(a) = nₐ 需要证明：(1) 退化条件下 |C\\| ≈ 0 使惩罚项消失；(2) 不同答案组的约束不重叠；(3) 每条 trace 的有效约束贡献使 Σ wc 精确等于 nₐ 而非仅成比例。论文报告 42.9% 去重率（§3.1），这意味着约束权重分布不均匀。证明跳过了这些中间步骤。\n\n**N2** [critical] 统计功效不足覆盖面过大，削弱否定结论的普遍性\n- 16 个条件中 10 个 underpowered（MDE ≥ 1.86pp）。GSM8K (n=30) 和 AIME (n=22) 样本量极小，在 Table 1 中与 n=204 条件并列。论文无法区分\"SICA 无效\"和\"样本不够大\"。\n\n**N3** [critical] 诊断框架 100% 准确率可能是 trivial classifier + in-sample overfitting\n- 60 个条件全部为 null 或 negative，trivial classifier（\"总是预测无效果\"）也能达到 100%。Holdout 验证仅 2 个条件，且同为 negative cases。\n\n### Should-Fix 问题\n\n**W1** [warning] Corollary 1 (DPI) 贡献定位不清\n- I(C;Y) ≤ I(T;Y) 几乎是信息论教科书练习题。\n\n**W2** [warning] Bias Ratio (BR) 缺少 null model 分解\n- 60% trace 产生答案 a 时，纯随机约束-答案关联也会产生 BR = 1.5。需 permutation null model 量化 excess bias。\n\n**W3** [warning] Cross-architecture escape (§6) 结论过度推断\n- 仅 6 个条件，Spearman ρ=1.0 (n=6) 鲁棒性存疑。\"capability-gap pattern\" 数据不足。\n\n**W4** [warning] α=0.5 无理论依据，sensitivity 分析实质上确认了退化\n- ≥99% agreement 是 ceiling effect 而非鲁棒性。\n\n**W5** [warning] Multi-seed replication 覆盖率不足\n- 仅 2/6 模型有 multi-seed。Mistral-7B 的 Δ ∈ [-4.41, +3.43] 跨越正负方向。\n\n### Questions\n\n**Q1**: score(a) = nₐ 如何从 Eq. 3 精确推导？\n**Q2**: 诊断框架的附加值（over trivial baseline）具体体现在哪里？\n**Q3**: TOST ±2pp margin 的先验依据？\n**Q4**: §6 cross-architecture 实验中 α 是否也固定为 0.5？\n**Q5**: Table 2 Gemini BR=12.19 的异常值原因？\n\n### Missing References\n- Cohen's h 或其他标准化效应量\n- Burnell et al. (2023) \"Rethink reporting of evaluation results in AI\"\n\n---\n\n请逐条回应。"
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
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix/Should-Fix/Minor 点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿原文\n\n### Must-Fix 问题\n\n**N1** [critical] Proposition 1 证明存在关键逻辑跳跃\n- 证明声称 \"By definition, score(a) = Σ 1[aᵢ = a] = nₐ\"，但 SICA 的实际评分函数（Eq. 3）是 score(a) = Σ_{c∈C*} wc·σ(c,a) − α·Σ_{c∈C\\} wc·σ(c,a)，涉及约束权重 wc 和源归属指示函数 σ(c,a)。从 Eq. 3 到 score(a) = nₐ 需要证明：(1) 退化条件下 |C\\| ≈ 0 使惩罚项消失；(2) 不同答案组的约束不重叠；(3) 每条 trace 的有效约束贡献使 Σ wc 精确等于 nₐ 而非仅成比例。论文报告 42.9% 去重率（§3.1），这意味着约束权重分布不均匀。证明跳过了这些中间步骤。\n\n**N2** [critical] 统计功效不足覆盖面过大，削弱否定结论的普遍性\n- 16 个条件中 10 个 underpowered（MDE ≥ 1.86pp）。GSM8K (n=30) 和 AIME (n=22) 样本量极小，在 Table 1 中与 n=204 条件并列。论文无法区分\"SICA 无效\"和\"样本不够大\"。\n\n**N3** [critical] 诊断框架 100% 准确率可能是 trivial classifier + in-sample overfitting\n- 60 个条件全部为 null 或 negative，trivial classifier（\"总是预测无效果\"）也能达到 100%。Holdout 验证仅 2 个条件，且同为 negative cases。\n\n### Should-Fix 问题\n\n**W1** [warning] Corollary 1 (DPI) 贡献定位不清\n- I(C;Y) ≤ I(T;Y) 几乎是信息论教科书练习题。\n\n**W2** [warning] Bias Ratio (BR) 缺少 null model 分解\n- 60% trace 产生答案 a 时，纯随机约束-答案关联也会产生 BR = 1.5。需 permutation null model 量化 excess bias。\n\n**W3** [warning] Cross-architecture escape (§6) 结论过度推断\n- 仅 6 个条件，Spearman ρ=1.0 (n=6) 鲁棒性存疑。\"capability-gap pattern\" 数据不足。\n\n**W4** [warning] α=0.5 无理论依据，sensitivity 分析实质上确认了退化\n- ≥99% agreement 是 ceiling effect 而非鲁棒性。\n\n**W5** [warning] Multi-seed replication 覆盖率不足\n- 仅 2/6 模型有 multi-seed。Mistral-7B 的 Δ ∈ [-4.41, +3.43] 跨越正负方向。\n\n### Questions\n\n**Q1**: score(a) = nₐ 如何从 Eq. 3 精确推导？\n**Q2**: 诊断框架的附加值（over trivial baseline）具体体现在哪里？\n**Q3**: TOST ±2pp margin 的先验依据？\n**Q4**: §6 cross-architecture 实验中 α 是否也固定为 0.5？\n**Q5**: Table 2 Gemini BR=12.19 的异常值原因？\n\n### Missing References\n- Cohen's h 或其他标准化效应量\n- Burnell et al. (2023) \"Rethink reporting of evaluation results in AI\"\n\n---\n\n请逐条回应。"
  }
}
```

</details>

---


### Tool result

_source line 1777 · 2026-05-23T09:27:08.483321+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23052
}
```

</details>

---


### Tool call

_source line 1778 · 2026-05-23T09:27:08.634310+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix/Should-Fix/Minor 点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿原文\n\n### Must-Fix 问题\n\n**N1** [critical] 标题的普遍性声明与统计证据不匹配\n- 标题 \"Do Not Substantially Improve\" 暗示一个普遍性结论，但 TOST 分析显示仅 4/16 主条件通过等价性检验（±2pp），10 个条件 underpowered (power < 21%)。Abstract 声称 \"We show the answer is no\" 但紧接着承认 10 条件 underpowered，逻辑不一致。\n\n**N2** [critical] Proposition 1 的 Markov chain 假设缺乏显式论证\n- Markov chain M→T→A→C 依赖 C 条件独立于 M given T，但 SICA 中同一模型生成 trace 和提取约束，模型权重构成 C 和 M 之间的隐式依赖，可能违反条件独立性。\n\n**N3** [critical] SCB 与已有 confirmation bias 工作的新颖性区分不充分\n- Wan et al. (2025) 已证明 CoT confirmation bias，SCB 可能是同一现象在 FOL 载体上的实例化。论文仅一句带过，未充分对比。Jhaveri & Kersting (2026) 进一步削弱新颖性。\n\n### Should-Fix 问题\n\n**W1** [warning] DPI 推论理论贡献度偏弱\n- Corollary 1 \"从 trace 提取的约束不超过 trace 本身信息量\" 接近同义反复。\n\n**W2** [warning] 诊断框架 100% accuracy 部分为 in-sample\n- 决策边界从数据拟合并在同一数据上评估。Holdout 仅 2 个模型系列。\n\n**W3** [warning] Scope 震荡：SICA-specific vs. 一般性 claims\n- 论文在两个 scope 之间摆动。Proposition 1 理论声称是 general，但 27 个变体均在 SICA paradigm 内。\n\n**W4** [warning] K_eff 可读性不足\n- 对非 ensemble-theory 背景读者缺少直觉解释。\n\n**W5** [warning] \"Symbolic Mirage\" 术语过度品牌化\n- Section 标题带修辞色彩，与技术机制不匹配。\n\n### Questions\n\n**Q1**: 同一模型做 extraction 时，是否有证据表明 C-M 隐式依赖可忽略？\n**Q2**: 如果将样本量增加到 power=80%，结论是否会改变？\n**Q3**: 诊断框架在 >32B 模型上的预期表现？\n**Q4**: Cross-architecture escape 本质上是否因为违反了 Proposition 1 的前提？\n\n### Missing References\n- Reflexion (Shinn et al., 2023)\n- LATS (Zhou et al., 2023)\n- STaR (Zelikman et al., 2022)\n- Kuai et al. (2026) 引用深度不足\n\n---\n\n请逐条回应。"
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
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix/Should-Fix/Minor 点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿原文\n\n### Must-Fix 问题\n\n**N1** [critical] 标题的普遍性声明与统计证据不匹配\n- 标题 \"Do Not Substantially Improve\" 暗示一个普遍性结论，但 TOST 分析显示仅 4/16 主条件通过等价性检验（±2pp），10 个条件 underpowered (power < 21%)。Abstract 声称 \"We show the answer is no\" 但紧接着承认 10 条件 underpowered，逻辑不一致。\n\n**N2** [critical] Proposition 1 的 Markov chain 假设缺乏显式论证\n- Markov chain M→T→A→C 依赖 C 条件独立于 M given T，但 SICA 中同一模型生成 trace 和提取约束，模型权重构成 C 和 M 之间的隐式依赖，可能违反条件独立性。\n\n**N3** [critical] SCB 与已有 confirmation bias 工作的新颖性区分不充分\n- Wan et al. (2025) 已证明 CoT confirmation bias，SCB 可能是同一现象在 FOL 载体上的实例化。论文仅一句带过，未充分对比。Jhaveri & Kersting (2026) 进一步削弱新颖性。\n\n### Should-Fix 问题\n\n**W1** [warning] DPI 推论理论贡献度偏弱\n- Corollary 1 \"从 trace 提取的约束不超过 trace 本身信息量\" 接近同义反复。\n\n**W2** [warning] 诊断框架 100% accuracy 部分为 in-sample\n- 决策边界从数据拟合并在同一数据上评估。Holdout 仅 2 个模型系列。\n\n**W3** [warning] Scope 震荡：SICA-specific vs. 一般性 claims\n- 论文在两个 scope 之间摆动。Proposition 1 理论声称是 general，但 27 个变体均在 SICA paradigm 内。\n\n**W4** [warning] K_eff 可读性不足\n- 对非 ensemble-theory 背景读者缺少直觉解释。\n\n**W5** [warning] \"Symbolic Mirage\" 术语过度品牌化\n- Section 标题带修辞色彩，与技术机制不匹配。\n\n### Questions\n\n**Q1**: 同一模型做 extraction 时，是否有证据表明 C-M 隐式依赖可忽略？\n**Q2**: 如果将样本量增加到 power=80%，结论是否会改变？\n**Q3**: 诊断框架在 >32B 模型上的预期表现？\n**Q4**: Cross-architecture escape 本质上是否因为违反了 Proposition 1 的前提？\n\n### Missing References\n- Reflexion (Shinn et al., 2023)\n- LATS (Zhou et al., 2023)\n- STaR (Zelikman et al., 2022)\n- Kuai et al. (2026) 引用深度不足\n\n---\n\n请逐条回应。"
  }
}
```

</details>

---


### Tool result

_source line 1779 · 2026-05-23T09:27:10.138243+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1503
}
```

</details>

---


### Assistant

_source line 1780 · 2026-05-23T09:27:17.209303+00:00_

交叉分享已发出，等待两位 Reviewer 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 125

## Round 125

2 recorded events


### User

_source line 1781 · 2026-05-23T09:27:19.822764+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

核心判断：**Overall 3.5 (Borderline Conference)**。

三个 Must-Fix 问题：
1. **Proposition 1 证明不完整**——从 Eq.3 到 score(a)=nₐ 缺少关键中间步骤（约束权重不均匀、去重率 42.9% 下精确等式不成立）
2. **16 个条件中 10 个统计功效不足**——无法区分"SICA 无效"和"样本不够大"，标题的全称否定 claim 证据不充分
3. **诊断框架 100% 准确率是 trivial 的**——60 个条件全为阴性，"永远预测无效"的 baseline 也能 100%，框架的区分能力未经正例验证

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

_source line 1782 · 2026-05-23T09:27:23.765450+00:00_

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


## Round 126

## Round 126

2 recorded events


### User

_source line 1783 · 2026-05-23T09:29:29.845627+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: 标题的普遍性声明与统计证据不匹配**

同意，与我的 N2 一致。论文标题 "Do Not Substantially Improve" 和 Abstract 的 "We show the answer is no" 是全称判断，但 TOST 仅在 4/16 条件下确立等价性，10 条件 underpowered。证据的确不足以支撑如此 categorical 的结论。

补充：我在审查中进一步注意到 GSM8K (n=30) 和 AIME (n=22) 在 Table 1 中与 n=200+ 条件无区分地并列展示，加剧了误导性。建议作者 (a) 将标题改为限定性表述（如 "Self-Extracted Constraints Show No Significant Improvement..."），(b) 在 Table 1 中以视觉标记区分 powered 和 underpowered 条件。

---

**[REBUT] R2-N2: Proposition 1 的 Markov chain 假设缺乏显式论证**

R2 的核心论点是：同一模型 M 既生成 trace 又提取约束，模型权重构成 C 和 M 之间的隐式依赖，可能违反 Markov chain Y—T—C 的条件独立性。

这一担忧在技术上不成立。DPI 所需的条件独立性是 **C ⊥ Y | T**（给定 trace，约束不包含关于 ground truth 的额外信息），而非 C ⊥ M | T。具体来说：

1. 约束提取过程 c = f_M(t) 仅以 trace t 和 extraction prompt 为输入，**不接触 ground truth Y**。因此 P(C|T,Y) = P(C|T)，即 C ⊥ Y | T，Markov chain 成立。

2. R2 担心 "模型权重构成 C 和 M 之间的隐式依赖"——这是对 Markov chain 条件的误读。M 的确影响 C（通过 f_M），但 DPI 不要求 C ⊥ M | T，只要求 C ⊥ Y | T。模型 M 是固定的生成机制，不是 Markov chain 中的随机变量。

3. 即使考虑 extraction 温度 T_ext = 0.3 引入的随机性（§3.1），c ~ P_M(·|t, prompt) 仍满足 C ⊥ Y | T，因为随机性来自模型采样而非 Y。

**不过**，R2 的关注方向提示了一个我在 N1 中指出的更实质性问题：Proposition 1 Part (i) 的证明从 Eq. 3 跳到 score(a) = nₐ 的逻辑缺口。Markov chain 本身是成立的，但 source-attribution scoring 退化为 majority voting 的证明步骤不完整。建议 R2 和作者将讨论聚焦于此。

---

**[AGREE with nuance] R2-N3: SCB 与已有 confirmation bias 工作的新颖性区分**

部分同意。论文的确需要更充分地与 Wan et al. (2025) 和其他 CoT self-correction bias 工作对比。

但我认为 R2 低估了论文的区分度。论文在 §2 Related Work（page 3 右栏底部）已指出 "confirmation bias here is distinct from CoT unfaithfulness"。关键区别在于：

- **Wan et al. (2025)** 研究的是 CoT 推理过程中的 unfaithfulness（模型的推理步骤不忠实于其内部计算），这是 **语义层面** 的 bias。
- **本文 SCB** 研究的是 **结构层面** 的退化：自提取约束通过 source-attribution scoring (Eq. 3) 在数学上退化为 majority voting（Proposition 1），这是一个关于 aggregation mechanism 的形式化结论，而非关于 LLM 推理忠实性的结论。
- 经验证据也不同：94.4% 的问题上约束通过 Z3 验证（§3.1），说明约束在形式逻辑层面是"正确"的——问题不是约束不可靠，而是约束虽然正确但不提供超越 trace 本身的信息。

不过，我同意论文应更明确地用 1-2 段对比 Wan et al.，说明 SCB 不是 CoT bias 的 "FOL 载体实例化" 而是 "正交的 aggregation-level 现象"。关于 Jhaveri & Kersting (2026)，如果确实存在该引用，论文应讨论。

---

### Should-Fix 问题

**[AGREE] R2-W1: DPI 推论理论贡献度偏弱**

完全同意，与我的 W1 一致。Corollary 1 本质上是 "deterministic function 不增加信息量" 的直接应用。建议降级为 Remark。

---

**[AGREE] R2-W2: 诊断框架 100% accuracy 部分为 in-sample**

完全同意，与我的 N3 一致。我进一步指出 60 条件全为 negative cases 意味着 trivial "always predict negative" classifier 也达到 100%，框架的区分能力（discriminative power）未经验证。

---

**[AGREE with nuance] R2-W3: Scope 震荡**

部分同意。论文确实在 "SICA-specific finding" 和 "general impossibility" 之间摆动。Proposition 1 + Corollary 1 的理论声称是 general（"applies to any self-extraction pipeline"），但 27 个实验变体全在 SICA 范式内，其他 self-extraction 范式（如 LeanAgent、CriticGPT-style 方法）未被覆盖。

不过，我认为这种 scope 震荡在否定结果论文中是常见且可接受的，只要论文明确标注边界。Proposition 1 的 generality 来自数学结构（任何 c = f(t) 的 pipeline 都满足），实验覆盖的限制是 engineering effort 问题而非逻辑问题。建议论文在 §7 或 Limitations 中增加一句："We verify the theoretical predictions empirically within the SICA paradigm; validation on other self-extraction architectures (e.g., trained verifiers, tool-augmented extraction) remains future work."

---

**[AGREE] R2-W4: K_eff 可读性不足**

同意。K_eff = K / [1 + (K-1)·κ] 引用了 Fleiss (1971)，但对非 ensemble 背景读者缺少直觉。建议添加一句："K_eff can be interpreted as the effective number of independent voters: when all traces agree (κ=1), K_eff=1; when fully independent (κ=0), K_eff=K."

---

**[REBUT] R2-W5: "Symbolic Mirage" 过度品牌化**

不同意这是一个问题。学术论文中使用隐喻性 section title 是常见做法（如 "The Lottery Ticket Hypothesis"、"The Bitter Lesson"、"Attention Is All You Need"）。"Symbolic Mirage" 精确传达了论文核心发现：形式验证的表象（所有约束通过 Z3）掩盖了实质上的退化（回到 majority voting）。这个术语有具体的技术对应物（§5.1 的 confirmation bias + Proposition 1 的退化），并非空洞修辞。

如果 R2 的关注点是 section title 而非术语本身，建议保留术语但将 section title 改为更中性的表述（如 "§5 Analysis: Source-Attribution Degeneration"），在正文中使用 "symbolic mirage" 作为现象描述。

---

### Questions 回应

**Q1**: 如我在 R2-N2 rebut 中所述，C ⊥ Y | T 成立是因为 extraction 不使用 ground truth，与 C-M 依赖无关。C-M 依赖确实存在（f_M 取决于 M），但不影响 DPI 论证的有效性。

**Q2**: 基于当前效应量（多数 |Δ| < 2pp，Table 1），增加样本量大概率会确认 near-zero 效应。但 Mistral-7B 的 seed variance（Δ ∈ [-4.41, +3.43]，Table 31）提示在 intermediate-SC regime 中可能存在 condition-specific 正效应被 averaging 掉的情况。这是一个有价值的实证问题，无法从当前数据确定答案。

**Q3**: 论文未覆盖 >32B 模型。Table 5 (Appendix C) 包含 DeepSeek-R1-7B 和 Gemini-2.5-Pro（frontier model），但 Gemini 的 C₀ = 2% 意味着 SICA 完全退化为 SC，诊断框架在 frontier model 上"预测正确"但这是 trivial prediction（高准确率模型自然满足 C₀ < 5%）。框架对 >32B open-weight 模型（如 LLaMA-3.1-70B）的表现是有意义的未知数。

**Q4**: 同意 R2 的分析方向。Cross-architecture escape 本质上绕过了 Proposition 1 的前提条件（c = f_M(t) 中 M 固定），因为验证器是不同模型，打破了 source-attribution coupling。论文在 §6 中已隐含此逻辑（"structurally independent verification"），但应更显式地说明 cross-architecture 之所以有效，正是因为违反了 Proposition 1 的 "same model generates and evaluates" 前提。这实际上是论文理论框架的**优势**——theory 正确预测了 escape 的条件。

---

### Missing References 回应

- **Reflexion (Shinn et al., 2023)** 和 **LATS (Zhou et al., 2023)**：这两篇是 self-refinement / tree-search 方法，与论文的 constraint-extraction 范式有概念联系但技术路径不同。建议在 §2 Related Work 中简要提及作为 alternative self-improvement 范式。
- **STaR (Zelikman et al., 2022)**：STaR 是 training-based self-improvement，论文聚焦 training-free 方法，STaR 的相关性有限但作为 background 可以引用。
- **Kuai et al. (2026)**：如果 R2 指的是与 cross-model independence 相关的工作，论文应增加讨论深度。需要 R2 澄清具体引用内容。


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

_source line 1784 · 2026-05-23T09:29:34.097486+00:00_

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


## Round 127

## Round 127

2 recorded events


### User

_source line 1785 · 2026-05-23T09:29:39.806353+00:00_

[Reviewer 1 审稿结果]:
已完成对 Reviewer 2 全部审稿意见的逐条回应，已提交给 Review Director。

总结：
- **3 个 Must-Fix**：同意 N1（标题过度声称），反驳 N2（Markov chain 技术上成立，R2 混淆了所需的条件独立性），部分同意 N3（需更充分对比已有 confirmation bias 工作，但 SCB 有结构层面的独立贡献）
- **5 个 Should-Fix**：同意 W1-W4，反驳 W5（"Symbolic Mirage" 有具体技术对应物，非空洞修辞）
- **4 个 Questions**：逐一给出了基于论文证据的分析

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

_source line 1786 · 2026-05-23T09:29:46.132035+00:00_

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


## Round 128

## Round 128

12 recorded events


### User

_source line 1787 · 2026-05-23T09:30:58.215656+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: Proposition 1 证明存在关键逻辑跳跃**

同意这是一个实质性的证明缺陷。论文 p6 的证明直接写 "score(a) = Σ wᵢ = nₐ"，但这一等式在 SICA 的实际评分机制下不成立。具体分析：

1. **权重与计数的混淆**：§3.1 (p3) 定义 wₖ = "the number of source traces"（该去重约束出现在多少条 trace 中），所以 Σ wc ≠ nₐ，而是 Σ wc = 所有来自答案 a 的 (trace, constraint) 对的总数。如果每条 trace 平均生成 m 条约束，则 Σ wc = m · nₐ，是 *比例* 关系而非 *等式*。
2. **42.9% 去重率的影响**：不同答案组的约束去重率可能不同。如果多数答案组的约束高度重复（高去重率，少数唯一约束但高权重）而少数答案组约束更多样，则 score(a)/score(a') 不再精确等于 nₐ/nₐ'。
3. **但结论可能仍然成立**：BR ≥ 1 只需要 score(majority answer) ≥ score(any other answer)，这在 "约束按比例反映 trace 分布" 的合理假设下仍然成立。问题是 **证明的严谨性**，而非结论的正确性。

**补充**：我在自己的审稿中也指出了 Markov chain 假设 M→T→A→C→S 缺乏显式论证（我的 N2）。R1 的 N1 从评分函数层面、我的 N2 从条件独立性层面分别暴露了 Proposition 1 的不同弱点——两者叠加使该定理的可靠性进一步存疑。

---

**[AGREE] R1-N2: 统计功效不足覆盖面过大**

完全同意，且与我的 N1（标题 overclaim）一致。补充几点：

1. **GSM8K (n=30) 和 AIME (n=22) 不应出现在主结果中**：这些样本量下，即使效应为 5pp 也检测不到（Table 6, Appendix D）。将它们与 n=204 的 FOLIO 条件并列展示，给读者造成 "16 个条件都说 no" 的错误印象。建议将极小样本条件移至 Appendix 作为 exploratory evidence。
2. **Table 1 的呈现方式加剧问题**：Table 1 用 "†gold ICL" 和 "◊seed-confirmatory" 等符号区分条件类型，但未在表内标注每个条件的统计功效。读者需要翻到 Appendix D 才能发现 10/16 条件 underpowered。
3. **与我的评估一致**：我给 Soundness 3.5/5，其中一个关键扣分点就是 title-evidence mismatch。R1 的 N2 从功效分析角度提供了更详细的论证。

---

**[AGREE] R1-N3: 诊断框架 100% 准确率可能是 trivial classifier**

这是一个精准的批评。我在自己的 W2 中也指出了 in-sample 问题，但 R1 的 trivial classifier 论证更加尖锐：

1. **基率论证成立**：查看 Figure 4 (p7) 的决策树，所有叶节点的预测结果均为 neutral-to-negative。如果数据中不存在任何正面案例，则 "always predict no improvement" 这个零规则分类器同样达到 100% 准确率。
2. **Held-out 验证不足以反驳**：§5.3 提到在 LLaMA-3.1-8B 和 Qwen3-14B 上做了前瞻性验证，但这两个模型同样产生 negative 结果。真正的验证需要包含 *positive cases*——即存在 SICA 确实改善 SC 的条件。但论文的核心论点恰恰是不存在这样的条件，这构成一个内在矛盾。
3. **诊断框架的实际价值在于 failure mode 分类而非二分类预测**：Figure 4 区分了退化型（C₀ > 5%）、多样性不足型（K_eff > 1.30）和确认偏差型（SC ≥ 60%）。这种分类对从业者理解 *为什么* 方法失败有指导意义，但 "100% accuracy" 的表述暗示的是预测能力，而非解释能力。建议改为 "correctly characterizes the failure mode" 而非 "correctly classifies"。

---

### Should-Fix 问题

**[AGREE] R1-W1: Corollary 1 贡献定位不清**

同意。我在自己的审稿中将此列为 W1 并给出了相似评价：I(C;Y) ≤ I(T;Y) 是 DPI 在 Markov chain T→C 上的直接应用，几乎不含非显然步骤。论文的贡献在于 *选择了正确的 Markov chain 建模*（modeling contribution），而非推导本身（derivation contribution）。建议论文明确区分这两个层次。

---

**[AGREE] R1-W2: BR 缺少 null model 分解**

这是一个我自己遗漏的重要技术点。

1. **基率效应的量化**：论文 §5.1 (p6) 提到 "reflecting both the base-rate effect of trace-count distributions and any additional extraction alignment"，但未提供形式化分解。如果 trace 分布为 60:40（nₐ/nₐ' = 1.5），纯随机约束-答案关联已经产生 BR = 1.5。Table 2 中 Mistral-7B 的 BR = 4.97、Gemini-2.5-Pro 的 BR = 12.19，其中多少是 base-rate 贡献、多少是 excess extraction bias？
2. **permutation null model 的建议合理**：打乱约束与 trace 的对应关系后计算 null BR，再用 (observed BR - null BR) 作为 excess bias 的度量，可以更清晰地展示提取过程本身引入了多少额外偏差。
3. **这不影响核心结论但影响机制解释的精度**：即使 excess bias = 0（即 BR 完全由 base-rate 解释），论文的 negative result 仍然成立——约束提取没有 *超越* trace 分布。但作者声称的 "structural" bias 需要 excess bias > 0 才能成立。

---

**[AGREE] R1-W3: Cross-architecture escape 结论过度推断**

同意。我在自己的审稿中将跨架构发现列为优势（S4），但未充分关注统计鲁棒性。补充：

1. **Spearman ρ=1.0, n=6 的 p 值问题**：6 个点的完美排名相关虽然 p < 0.05，但鲁棒性极低——移除任一点都可能破坏相关性。且论文 p7-8 Table 3 仅覆盖 FOLIO 和 ProofWriter 两个数据集，不足以建立 "capability-gap pattern" 这样的一般性规律。
2. **但方向性发现仍有价值**：即使证据不足以支撑强因果声明，"独立验证器可打破 SCB 瓶颈" 这一方向性发现对后续研究有启示意义。建议将 §6 的措辞从 "confirming" 改为 "suggesting" 或 "providing preliminary evidence for"。

---

**[AGREE] R1-W4: α=0.5 sensitivity 分析实质上确认退化**

同意。查看 Table 11 (Appendix H, p16)，所有 α ∈ {0.1, 0.3, 0.5, 0.7, 1.0} 下 SICA-SC agreement 均 ≥ 99%。这不是 "SICA 对 α 鲁棒"，而是 "退化条件 |C⁻| ≈ 0 使 α 变得无关"——当惩罚项的输入（矛盾约束）趋近于零时，惩罚系数的值无论如何都不影响结果。论文应明确承认这一点，而非将其包装为鲁棒性验证。

---

**[REBUT] R1-W5: Multi-seed replication 覆盖率不足**

部分反驳。

1. **Mistral-7B 的 Δ ∈ [-4.41, +3.43] 确实令人担忧**：Table 31 (Appendix X, p24) 显示跨 seed 的不稳定性。但论文 p24 报告 mean Δ = -0.17 ± 2.31 (SD)，95% CI 覆盖零，这本身就是 null effect 的证据。
2. **关于覆盖率**：论文在 Appendix X.1 (p24) 同时报告了 Qwen2.5-14B 的 multi-seed 结果（mean Δ = +0.75 ± 1.87, CI: [-1.24, +0.36]），同样与 null 一致。两个模型（一个 7B，一个 14B）的 multi-seed 结果一致支持 null 假说。
3. **但 R1 的方向正确**：更多模型的 multi-seed 数据确实会加强结论。建议作为 revision 中的优先补充实验。
4. **反驳理由**：将此从 "should-fix" 降级为 "nice-to-have"——现有两个模型的 multi-seed 数据虽不充分但方向一致，不构成对核心结论的实质性威胁。

---

### Questions 回应

**Q1**: 同意 R1 的关注——score(a) = nₐ 需要从 Eq. 3 严格推导，中间需证明去重后的权重分布不改变答案间的比例关系（见我对 N1 的分析）。

**Q2**: 同意 R1 的质疑。我建议作者回应时展示：(a) 诊断框架相比 trivial classifier 的附加信息（failure mode 分类），以及 (b) 在某些条件下诊断指标接近但未跨越边界时是否存在 false-near-miss 案例。

**Q3**: ±2pp margin 的先验依据确实缺失。建议作者说明选择依据——是基于领域惯例（如 NLP benchmark 的 typical noise floor）还是事后选择？如果是后者，存在 specification searching 风险。

**Q4**: 合理的实验细节问题。§6 的 cross-architecture 实验是否使用了与 §4 相同的 α=0.5 应该在方法描述中明确。

**Q5**: Table 2 (p6) 中 Gemini-2.5-Pro 的 BR=12.19 确实是异常值（其他模型 BR ∈ [1.66, 4.97]）。结合 R1-W2 的 null model 分解，需要检查 Gemini 是否在 FOLIO 上有极端不平衡的 trace-count 分布导致基率 BR 本身很高，还是 extraction 过程引入了异常偏差。论文 p6 脚注提到 Gemini (n_a ≤ 40) 的 CI 更宽，但未解释 BR 异常值的成因。

---

### Missing References 回应

- **Cohen's h**：[AGREE] 作为标准化效应量，Cohen's h 对读者理解 ±2pp 在不同基率下的实际意义有帮助。例如在 SC=50% vs SC=90% 时，2pp 的 Cohen's h 值差异显著。
- **Burnell et al. (2023)**：[AGREE] 关于 AI 评估报告规范的建议，与本文的统计报告实践相关。但这是建议性引用，非必须。

---

### 综合判断

与 R1 的评估高度一致。我们共同识别了以下核心问题：
1. **Proposition 1 的证明需要补充**（R1-N1 评分函数层面 + 我的 N2 Markov chain 层面）
2. **标题/Abstract 的 overclaim 与统计证据不匹配**（R1-N2 + 我的 N1）
3. **诊断框架的声称过强**（R1-N3 + 我的 W2）

主要分歧仅在 W5（multi-seed 覆盖率）——我认为现有两个模型的 multi-seed 数据虽不充分但方向一致，不构成 should-fix。

我维持 **Overall 3.5 (Borderline Conference)** 的评分。如果作者能在 revision 中解决 N1-N3（补充证明、修改标题/声称、重新定位诊断框架），论文有望达到 Findings 水平。


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

_source line 1788 · 2026-05-23T09:31:31.527693+00:00_

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

_source line 1789 · 2026-05-23T09:31:31.628968+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T09:17:30.259849+00:00\", \"completed_at\": \"2026-05-23T09:21:18.675703+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点（纯 Title/Abstract/Introduction 文本），Figure 1 出现在 page 2 顶部，在 3 页窗口内，可接受。Title-Abstract-Figure 1 三者叙事一致（自提取约束 → pipeline → 负面结论）\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1（SICA pipeline）全宽放置，caption 自包含，红色虚线框标注 independence bottleneck 传达核心 message。管线图配色清晰（蓝/绿/红虚线），但红色虚线框与周围实线框的视觉对比度可再增强\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 2 散点图 legend 文字偏小（模型名+条件标注），打印后可能不够清晰。建议 legend 字号至少与 caption 字号的 70% 持平\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 1 主结果表使用 booktabs 风格，bold 标注显著结果，符号（†, *, ◊）在表注解释。格式专业。列数较多但未溢出 margin\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 2 + Proposition 1 数学证明，页面密度高但节奏合理（表格→文本→公式）\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"Figure 4（training-free strategies 分类图）内部文字过小——每个彩色方框内含 3-5 行小字描述策略细节，打印或缩小后可读性差。建议精简框内文字或增大图尺寸\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3（Causal DAG）尺寸小但节点标签清晰，与 Figure 4 同页形成良好视觉节奏\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"正文最后一页：Table 3 + Section 6 + Section 7 Discussion and Conclusion + Limitations，页面利用率 >95%，无浪费空间。Limitations 在正文内（符合 EMNLP 2026 要求），篇幅简短得当\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"正文恰好 8 页，符合 EMNLP 2026 long paper 页数限制\"}, {\"severity\": \"info\", \"dimension\": \"pages 9-10\", \"message\": \"参考文献两页，格式统一（author 缩写一致），未见 [?] 未解析引用或跳号\"}, {\"severity\": \"info\", \"dimension\": \"page 11\", \"message\": \"Appendix A 开始，prompt templates 使用灰底 monospace 代码块，可读性好\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"Algorithm 1 和 Algorithm 2 使用标准 algorithm 环境，行号清晰，伪代码格式规范\"}, {\"sev
…[truncated 1535 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1790 · 2026-05-23T09:31:31.830512+00:00_

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

_source line 1791 · 2026-05-23T09:31:31.882230+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1792 · 2026-05-23T09:31:50.826242+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml",
  "description": "Check issue tracker size"
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
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml",
    "description": "Check issue tracker size"
  }
}
```

</details>

---


### Tool result

_source line 1793 · 2026-05-23T09:31:50.977243+00:00_

922 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml

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

_source line 1794 · 2026-05-23T09:36:34.941527+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "symb_invariant_consensus",
  "issues_yaml": "# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)\n- id: \"R1-C1\"\n  summary: \"Method Stage 3 sat() implementation undescribed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit.\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Most experiments underpowered (n≤60), no power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Power analysis + Bootstrap CIs added. Larger n conditions (200-600).\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Oracle/upper-bound experiment missing\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp.\"\n  resolution_round: 3\n\n- id: \"R1-C4\"\n  summary: \"Huang et al. (ICLR 2024) not cited\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Huang, Stechly, Kambhampati all cited and discussed.\"\n  resolution_round: 2\n\n- id: \"R1-C5\"\n  summary: \"Critical related work missing\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"~48 citations, 5 Related Work paragraphs.\"\n  resolution_round: 3\n\n- id: \"R1-C9\"\n  summary: \"Capability trap novelty unclear\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Reframed as regime-dependent analysis with CJT framework.\"\n  resolution_round: 3\n\n- id: \"R3-N1\"\n  summary: \"σ(c,a) scoring inconsistent between self-extraction and oracle\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Paper Agent added clarifying sentence in method.tex.\"\n  resolution_round: 4\n\n- id: \"R3-N2\"\n  summary: \"α value never specified\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"α=0.5 explicit in Eq.(3) and §4.1.\"\n  resolution_round: 3\n\n# Round 9+ issues\n\n- id: \"R9-W2\"\n  summary: \"NLI combo weight parameter w 未交叉验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 17\n  mentions:\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 未单独提及 w 参数\"\n    - round: 15\n      reviewers: []\n      note: \"R15(fresh) 未单独提及\"\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n\n- id: \"R9-W3\"\n  summary: \"Capability Gap Hypothesis 基于极小样本 (n=6)\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 17\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 共识: 仅6条件仅Mistral-7B显著, 需软化结论\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识: §6 escape仅SC<40%验证, 'SC≈70%'无数据支撑\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 共识AGREE: 仅1个条件显著(Mistral-7B SC=39.33%), 'principle'措辞过强\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 共识AGREE: Spearman ρ=1.0(n=6)鲁棒性存疑, 建议'preliminary evidence'而非'confirming'. R2补充: 方向性发现仍有启示价值\"\n  action_items:\n    - round: 14\n      action: \"§6结论软化为preliminary evidence + 讨论task gap\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R9-VL1\"\n  summary: \"Pages 1-2 连续纯文本无 display item\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16 视觉审查: Page 1纯文本(Abstract+Intro), Figure 1在page 2顶部\"\n    - round: 17\n      reviewers: []\n      note: \"R17 视觉审查: Figure 1在page 2顶部, 在3页窗口内可接受\"\n\n- id: \"R9-VL4\"\n  summary: \"Discussion/Conclusion 展开不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n\n- id: \"R10-N1\"\n  summary: \"Proposition 1 (Self-Extraction Ceiling) 无证明——empirical claim dressed as theorem\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 13\n  resolution: \"当前论文使用 Proposition 1 with formal proof (page 6)\"\n  resolution_round: 13\n\n- id: \"R10-N2\"\n  summary: \"κ→K_eff 映射理论基础不足——r=0.625 验证弱\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R16(fresh) R1-W7: K_eff exchangeable correlation假设可能被违反, minor concern\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及此技术点, 但R2-W4要求K_eff增加直觉解释, R1 AGREE\"\n\n- id: \"R10-N3\"\n  summary: \"Capability gap 'perfectly monotonic' 结论基于 n=6 非独立数据点\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 与R9-W3合并\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 与R9-W3合并. 共识: n=6 suggestive非definitive\"\n\n- id: \"R10-W1\"\n  summary: \"DRC τ 阈值无 held-out 评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n\n- id: \"R10-W2\"\n  summary: \"Cross-architecture NLI escape 适用面极窄\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R1-W8+R2-W3共识: generalizability受限, 仅NLI-friendly数据集测试\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R1-W3+R2 AGREE: 仅6条件, 仅Mistral显著. 但方向性发现有启示价值\"\n\n- id: \"R10-W3\"\n  summary: \"四种子复制方差大 + 统计功效 <21%\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R1-W3: multi-seed仅2/6模型, seed noise ±2.34pp超过多数|Δ|\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R1-W5: 仅2/6模型有multi-seed. R2 REBUT(降级nice-to-have): 现有2模型方向一致. 轻微分歧: R1认为should-fix, R2认为nice-to-have\"\n\n- id: \"R10-W4\"\n  summary: \"TOST ±2pp margin 缺少显式理由\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R16(fresh) R1-N2: ±2pp margin缺乏先验依据\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R1-Q3问TOST先验依据, R2 AGREE: 是否基于领域惯例还是事后选择? 共识: 需说明选择依据\"\n\n- id: \"R10-W5\"\n  summary: \"Bias Ratio 无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"BR CI 已整合: Mistral [3.98,6.37], Qwen [2.44,7.11]\"\n  resolution_round: 10\n\n- id: \"R10-W6\"\n  summary: \"SatLM specification-generation vs SICA trace-extraction 对比不充分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n\n- id: \"R10-W7\"\n  summary: \"'Symbolic Confirmation Bias' 需与近期 CoT confirmation bias 工作区分\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R2-N1: SCB是Huang(2024)+Wan(2025)的自然延伸\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R2-N3 critical: Wan et al.(2025)已证明CoT confirmation bias, SCB可能是FOL载体实例化. R1 AGREE w/nuance: SCB有aggregation-level结构性区分(source-attribution退化), 但需更充分对比. 部分共识: 定位为'complementary formal verification instance'而非独立发现\"\n\n- id: \"R10-W8\"\n  summary: \"Related Work 过度压缩——引用列表而非文献讨论\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [2]\n      note: \"R16(fresh) R2-M5: §2段间逻辑衔接不够清晰\"\n    - round: 17\n      reviewers: [2]\n      note: \"R17(fresh) R2 minor: §2三个子节间缺显式逻辑连接句\"\n\n- id: \"R10-I1\"\n  summary: \"'Symbolic Mirage' 概念新颖性——与 Huang/Wan 的 confirmation bias 区别\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 同R10-W7\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 同R10-W7. 共识: 需更充分对比Wan et al.(2025)\"\n\n- id: \"R10-I2\"\n  summary: \"Independence-Accuracy Trade-off 作为独立贡献有 bias-variance 重述嫌疑\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n\n- id: \"R10-VL1\"\n  summary: \"主文缺结果可视化\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16 视觉审查: 主文5 display items\"\n    - round: 17\n      reviewers: []\n      note: \"R17 视觉审查: 主文7 display items(Figure 1-4 + Table 1-3), 密度0.88/页, 合理\"\n\n- id: \"R11-N1\"\n  summary: \"Spearman ρ=1.0 (n=6) 被过度使用——有效自由度远低于6\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 与R9-W3合并\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R1-W3: 6点完美排名相关鲁棒性极低, 移除任一点可能破坏. R2 AGREE\"\n\n- id: \"R11-N2\"\n  summary: \"中心 claim 'SICA fails' 与统计功效不匹配——Abstract/title 过强\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 共识critical: power<21%, 建议标题改为'Do Not Substantially Improve'或加power caveat\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 共识critical: 当前标题'Do Not Substantially Improve'仍过强——10/16条件underpowered, 'We show the answer is no'(Abstract)逻辑不一致. R1建议'Show No Significant Improvement'; R2建议限定'confirmed equivalent vs underpowered/inconclusive'. GSM8K(n=30)/AIME(n=22)不应与n=200+并列. 完全共识\"\n  action_items:\n    - round: 16\n      action: \"标题软化 + Abstract加power caveat + TOST margin sensitivity analysis\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 17\n      action: \"标题进一步软化(当前'Substantially'仍不够); Abstract区分confirmed-equivalent vs underpowered; Table 1标注每条件power或区分powered/underpowered\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R11-N3\"\n  summary: \"TOST ±2pp margin 缺乏 principled 论证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 需补充不同margin的TOST sensitivity\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R1-Q3+R2 AGREE: 是领域惯例还是事后选择? 需说明依据, 存在specification searching风险\"\n\n- id: \"R11-W1\"\n  summary: \"DRC 评估不充分——仅PW完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n\n- id: \"R11-W2\"\n  summary: \"BR 指标存在循环论证倾向\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R2-N2 critical: 需permutation null model\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R1-W2+R2 fully AGREE: 纯随机约束-答案关联在60:40分布下已产生BR=1.5. 需permutation null distribution量化excess bias. R2补充: excess bias=0时negative result仍成立, 但'structural bias'声称需excess>0. 共识: 需null model分解\"\n  action_items:\n    - round: 16\n      action: \"BR降级为描述性指标并明确声明base-rate组成\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 17\n      action: \"计算base-rate predicted BR(nâ/max n_{a≠â})并与observed BR对比; 或运行permutation test建立null BR分布\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R11-W3\"\n  summary: \"术语过度品牌化——'Symbolic Mirage' 偏 dramatic\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R2-W5 minor: section title修辞色彩过强. R1 REBUT: 有技术对应物(Proposition 1退化), 非空洞修辞, 类似'Lottery Ticket'. 分歧: R2建议改技术性标题, R1建议保留术语但改section title\"\n\n- id: \"R11-W4\"\n  summary: \"新颖性定位需更早更明确建立与先验工作的 distinction\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R2-N1+R2-W5: SCB是Huang的自然延伸\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 与R10-W7合并. R1 AGREE w/nuance: SCB有结构层面区分(aggregation-level而非behavioral), 但需1-2段显式对比Wan et al.\"\n\n- id: \"R11-W5\"\n  summary: \"Independence-Accuracy Trade-off 应定位为量化而非新发现\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n\n- id: \"R11-W6\"\n  summary: \"遗漏引用: Byerly & Khashabi (2026 TACL) 等\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"当前论文已引用 Byerly and Khashabi (2026)\"\n  resolution_round: 13\n\n- id: \"R11-W7\"\n  summary: \"27 策略计数膨胀 + 未尝试 trained constraint extractor\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R2-W4: 27策略局限于self-extraction paradigm内变体\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R2-W3 scope震荡: 27变体全在SICA paradigm内但claim暗示'all training-free methods'. R1 AGREE w/nuance: generality来自数学结构, 但需明确标注实验覆盖边界\"\n\n- id: \"R11-VL1\"\n  summary: \"主文缺结果可视化——需上提 Figure 到主文\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16 视觉审查: Figure 2-4已在主文\"\n    - round: 17\n      reviewers: []\n      note: \"R17 视觉审查: 主文7 display items, 密度合理\"\n\n- id: \"R12-N1\"\n  summary: \"标题 overclaiming about frontier scale\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 标题已含'Logical Reasoning'\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 与R11-N2合并. 标题scope已改善('Logical Reasoning')但'Do Not Substantially Improve'仍overclaiming\"\n\n- id: \"R12-N2\"\n  summary: \"SCB 核心新颖性不足——self-correction failure 在 FOL 载体上的实例化\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R2-N1 critical\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R2-N3 critical + R1 AGREE w/nuance. R1认为SCB有独立的aggregation-level贡献(source-attribution退化 vs Wan的behavioral观察), 但同意需更充分对比. 部分共识\"\n\n- id: \"R12-N3\"\n  summary: \"DRC 作为 Contribution 4 不够充分\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"DRC demoted to practical observation in §6\"\n  resolution_round: 13\n  first_raised_round: 12\n  last_seen_round: 13\n\n- id: \"R12-W1\"\n  summary: \"BR 可能存在循环论证——56.4%零变量重叠使约束按定义支持source answer\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"与R11-W2合并\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"与R11-W2合并. R1-W2需null model分解\"\n\n- id: \"R12-W2\"\n  summary: \"CIL 名称和 information-theoretic 声称有误导\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Renamed to CCR, removed 'unify' claim\"\n  resolution_round: 13\n  first_raised_round: 12\n  last_seen_round: 13\n\n- id: \"R12-W3\"\n  summary: \"Figure 2 placement——应在正文而非附录\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Figure 2 已在正文 page 4\"\n  resolution_round: 13\n\n- id: \"R12-W4\"\n  summary: \"Appendix vs 主文关键信息分配不合理\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [2]\n      note: \"R16(fresh) R2-M3: Abstract信息过载\"\n    - round: 17\n      reviewers: [2]\n      note: \"R17(fresh) R2 minor: Abstract ~6个核心发现信息密度过高; 符号过载(BR/K_eff/C₀/κ/σ/α/Δ等)\"\n\n- id: \"R12-EC1\"\n  summary: \"Extractor Confound——所有 frontier cross-model extraction 使用同一 Mistral-7B extractor\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n\n- id: \"R13-N1\"\n  summary: \"摘要 BR 4.97× 选择性报告——最极端条件\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) Abstract已改为报告range 1.66×-4.97×\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及. Abstract当前报告'from 1.66× to 4.97×', 覆盖全范围\"\n\n- id: \"R13-N2\"\n  summary: \"统计功效呈现不足——10/16 underpowered, power analysis 埋在附录\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"与R11-N2合并\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 与R11-N2合并. 共识: Table 1应标注power或区分powered/underpowered条件. GSM8K/AIME应移至Appendix或标为exploratory\"\n\n- id: \"R13-N3\"\n  summary: \"α=0.5 无敏感性分析\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"论文有Table 11 α ablation ≥99% agreement\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R1-W4+R2 AGREE: ≥99% agreement是ceiling effect而非鲁棒性. 退化条件|C⁻|≈0使α无关. 论文应重新解释为退化corroborating evidence而非方法鲁棒性\"\n\n- id: \"R13-W1\"\n  summary: \"符号/指标过载——8页内7个定量工具\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n    - round: 17\n      reviewers: [2]\n      note: \"R17(fresh) R2 minor: BR/K_eff/C₀/κ/σ/α/Δ/CCR/ProcessSim等大量符号. 建议CCR和ProcessSim定义移至Appendix\"\n\n- id: \"R13-W2\"\n  summary: \"NLI claim 须限定到命题逻辑任务\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R16(fresh) R1-W9: 99%约束是propositional level\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n\n- id: \"R13-W3\"\n  summary: \"语法去重可能膨胀 BR——未报告语义去重后 BR\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及. 但与R11-W2(BR null model)相关\"\n\n- id: \"R13-W4\"\n  summary: \"Symbolic Mirage Hypothesis §3.3 与 §5 验证不连贯\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"当前论文无显式§3.3 Hypothesis section\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n\n- id: \"R13-W5\"\n  summary: \"缺引: Dhuliawala et al. 2023 Chain-of-Verification\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"已引用 dhuliawala2023chainofverification\"\n  resolution_round: 14\n\n- id: \"R14-N1\"\n  summary: \"标题'LLM Reasoning'范围超出实验证据——仅覆盖逻辑推理\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 标题已为'LLM Logical Reasoning'\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 标题scope改善, 但'Do Not Substantially Improve'仍overclaiming. 与R11-N2合并\"\n\n- id: \"R14-N2\"\n  summary: \"Symbolic Mirage Hypothesis Predictions 1-2 为事后总结非独立预测\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"当前论文无显式Predictions标签\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n\n- id: \"R14-W1\"\n  summary: \"Cross-architecture实验仅6条件/单一verifier/仅Mistral-7B显著\"\n  category: experiment\n  severity: major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 共识: 降级为'preliminary observation'\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R1-W3+R2 AGREE: 方向性发现有价值但证据不足支撑强因果声明. 建议'suggesting/preliminary evidence'而非'confirming'\"\n\n- id: \"R14-W2\"\n  summary: \"8页正文信息过载——§5.5/§6/§7展开不足\"\n  category: writing\n  severity: major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [2]\n      note: \"R16(fresh) R2-M3: Abstract信息过载\"\n    - round: 17\n      reviewers: [2]\n      note: \"R17(fresh) R2 minor: Abstract ~6核心发现, 符号过载, K_eff缺直觉解释\"\n\n- id: \"R14-W3\"\n  summary: \"'No evidence' claim scope与统计功效不匹配\"\n  category: framing\n  severity: major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"与R11-N2合并\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"与R11-N2合并. 共识critical\"\n\n- id: \"R14-W4\"\n  summary: \"BR计算子集大小(n_err)未报告\"\n  category: experiment\n  severity: moderate\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"当前论文Table 2已有n_err列\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R1-Q5: Gemini n_err≈12导致BR=12.19不稳定. R2 AGREE: 需检查base-rate分布. 与R11-W2(BR null model)相关\"\n\n- id: \"R14-W5\"\n  summary: \"Related Work遗漏: SETS(2025), MAV(2025)\"\n  category: writing\n  severity: minor-to-major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R2-W2新增: S²R, DuPO, Kamoi et al.\"\n    - round: 17\n      reviewers: [2]\n      note: \"R17(fresh) R2新增遗漏: Reflexion(Shinn 2023), LATS(Zhou 2023), STaR(Zelikman 2022). R1 AGREE Reflexion/LATS可作alternative self-improvement范式在§2简提, STaR相关性有限\"\n\n- id: \"R14-W6\"\n  summary: \"Fleiss' κ→ICC近似仅r=0.625——prevalence paradox\"\n  category: method\n  severity: moderate\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"minor, 不影响核心结论\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n\n# R15 issues\n\n- id: \"R15-M1\"\n  summary: \"遗漏引用: DuPO (ICLR 2026)\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"共识AGREE\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W2提出\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及. 论文§2已引用dupo2025\"\n\n- id: \"R15-M2\"\n  summary: \"遗漏引用: S²R (2025)\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"共识AGREE\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W2提出\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及. 论文§2已引用zeng2025s2r\"\n\n- id: \"R15-M3\"\n  summary: \"遗漏引用: LLM as Formalizers on CSP\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n\n- id: \"R15-M4\"\n  summary: \"遗漏引用: Lakshminarayanan et al. (2017) Deep Ensembles\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R1 REBUT: Kuncheva等已更直接相关\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n\n- id: \"R15-W1\"\n  summary: \"α=0.5敏感性分析≥99% agreement是ceiling effect\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"ceiling effect不等于鲁棒性\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R1-W4+R2 AGREE: 退化条件|C⁻|≈0使α无关, 应解释为退化证据而非鲁棒性. 共识\"\n\n# R16 issues\n\n- id: \"R16-N1\"\n  summary: \"Proposition 1 证明范围与声称范围不匹配 + 证明逻辑跳跃\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16: Part(i)依赖SICA特定scoring, 非数学必然; Part(ii) DPI近平凡\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R1-N1 critical: 证明从Eq.3跳到score(a)=nₐ缺关键步骤——(1)退化条件|C⁻|≈0未证明; (2)约束跨答案组不重叠未证明; (3)42.9%去重率导致权重不均匀, Σwc≠nₐ而是∝nₐ. R2 fully AGREE并补充: 比例关系可能保持argmax但精确等式不成立. 两人从不同角度(R1:评分函数, R2:Markov chain)暴露证明缺陷. 共识: 需(a)完善证明列出所有假设, 或(b)弱化为argmax preservation, 或(c)补充经验验证\"\n  action_items:\n    - round: 16\n      action: \"将Proposition 1分为source-attribution退化定理(精确但specific) + DPI bound(普遍但弱)\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 17\n      action: \"修复score(a)=nₐ证明: 明确假设(约束不重叠+权重均匀化条件), 或改为argmax preservation证明, 或补充经验rank agreement\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R16-N2\"\n  summary: \"Diagnostics 100%准确率是in-sample评估——overfitting风险, holdout验证不充分\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"决策边界在同一60条件上推导和评估; holdout仅1条件; 60条件全negative\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R1-N3+R2 AGREE: trivial 'always predict negative' classifier也100%. 真正的验证需positive cases但论文核心论点是不存在正例(内在矛盾). R2精辟补充: 框架价值在failure mode分类(退化型/多样性不足型/确认偏差型)而非二分类预测, 建议改'correctly characterizes failure mode'而非'correctly classifies'. R1建议用§6 cross-arch escape作positive validation. 共识: 降级claim + 重新定位为排除工具\"\n  action_items:\n    - round: 16\n      action: \"增加held-out验证 + 弱化claim + 报告60条件组成\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 17\n      action: \"重新定位: (a)'correctly characterizes failure mode'替代'correctly classifies'; (b)用§6 cross-arch作positive validation; (c)承认仅negative cases验证; (d)定位为'ruling-out tool'而非通用诊断\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R16-M1\"\n  summary: \"遗漏引用: Kamoi et al. (TACL 2024) self-correction survey\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2提出, R1 AGREE\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 论文§2已引用kamoi2024selfcorrect. 已解决\"\n\n- id: \"R16-M2\"\n  summary: \"遗漏引用: AlphaCode/CodeT\"\n  category: writing\n  severity: minor\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"code domain约束过滤成功案例\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 论文§2已引用li2022alphacode和chen2023codet. 已解决\"\n\n- id: \"R16-W1\"\n  summary: \"'Extending Huang et al.' overclaiming\"\n  category: framing\n  severity: major\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"建议改为'provide independent evidence consistent with'\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 与R10-W7/R12-N2合并. 当前论文§1/§2使用'provide independent evidence consistent with'措辞, 但§5.1和Abstract仍有'extending'暗示\"\n\n- id: \"R16-W2\"\n  summary: \"GSM8K(n=30)/AIME(n=22)与大样本等权重引用\"\n  category: experiment\n  severity: major\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"正文引用时未区分\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R1-N2+R2 AGREE: GSM8K/AIME在Table 1中与n=200+并列未区分. 建议移至Appendix或标为exploratory. 共识\"\n\n- id: \"R16-W3\"\n  summary: \"缺少training-based self-verification讨论\"\n  category: writing\n  severity: major\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"§2增加training-based段落, 引用S²R/DuPO\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 论文§2已有'Training-based verification'段落, 引用了S²R/DuPO/AlphaCode/CodeT. 基本解决\"\n\n- id: \"R16-SYS1\"\n  summary: \"Scope震荡——SICA-specific和general claims反复切换\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"全文scope qualifier修复需要\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R2-W3+R1 AGREE w/nuance: Prop 1 generality来自数学结构但实验覆盖限于SICA paradigm. R1建议§7加一句边界声明. 共识: 需在§1 contributions中明确界定scope\"\n\n# R17(fresh) 新发现\n\n- id: \"R17-N1\"\n  summary: \"Corollary 1 (DPI) 应降级为 Remark——'deterministic function 不增加信息量'是信息论教科书练习\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-W1+R2-W1共识AGREE: I(C;Y)≤I(T;Y)几乎是同义反复. 论文承认'contribution is identifying the Markov chain'而非推导. 建议降级Corollary 1为Remark, 或更清楚地说明Markov chain识别的non-trivial贡献在哪里\"\n\n- id: \"R17-N2\"\n  summary: \"K_eff 缺少直觉解释——非 ensemble-theory 背景读者理解困难\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R2-W4+R1 AGREE: K_eff=K/[1+(K-1)·κ]需具体示例(如'K=12, κ=0.7 → K_eff≈1.3, 12条高度相关trace仅等价于1.3条独立trace'). 共识\"\n\n- id: \"R17-N3\"\n  summary: \"遗漏引用: Reflexion(Shinn 2023), LATS(Zhou 2023)\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R2提出, R1部分AGREE: 可作alternative self-improvement范式在§2简提. STaR(Zelikman 2022)相关性有限\"\n\n- id: \"R17-N4\"\n  summary: \"Table 1 排版: 未标注每条件统计功效, 读者需翻Appendix D发现10/16 underpowered\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-N2+R2 AGREE: Table 1应以视觉标记区分powered/underpowered条件\"\n\n- id: \"R17-VL1\"\n  summary: \"Figure 4 内部文字过小——打印/缩小后可读性差\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"视觉审查发现: page 7 Figure 4每个彩色方框内含3-5行小字, 建议精简或增大图尺寸\"\n\n- id: \"R17-VL2\"\n  summary: \"Appendix pages 16/22 表格堆叠过度拥挤\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"视觉审查: page 16含5个表格+4个小节, page 22含5个表格+多个小节. 建议适当分页或合并\"\n"
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
    "issues_yaml": "# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)\n- id: \"R1-C1\"\n  summary: \"Method Stage 3 sat() implementation undescribed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit.\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Most experiments underpowered (n≤60), no power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Power analysis + Bootstrap CIs added. Larger n conditions (200-600).\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Oracle/upper-bound experiment missing\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp.\"\n  resolution_round: 3\n\n- id: \"R1-C4\"\n  summary: \"Huang et al. (ICLR 2024) not cited\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Huang, Stechly, Kambhampati all cited and discussed.\"\n  resolution_round: 2\n\n- id: \"R1-C5\"\n  summary: \"Critical related work missing\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"~48 citations, 5 Related Work paragraphs.\"\n  resolution_round: 3\n\n- id: \"R1-C9\"\n  summary: \"Capability trap novelty unclear\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Reframed as regime-dependent analysis with CJT framework.\"\n  resolution_round: 3\n\n- id: \"R3-N1\"\n  summary: \"σ(c,a) scoring inconsistent between self-extraction and oracle\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Paper Agent added clarifying sentence in method.tex.\"\n  resolution_round: 4\n\n- id: \"R3-N2\"\n  summary: \"α value never specified\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"α=0.5 explicit in Eq.(3) and §4.1.\"\n  resolution_round: 3\n\n# Round 9+ issues\n\n- id: \"R9-W2\"\n  summary: \"NLI combo weight parameter w 未交叉验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 17\n  mentions:\n    - round: 14\n      reviewers: []\n      note: \"R14(fresh) 未单独提及 w 参数\"\n    - round: 15\n      reviewers: []\n      note: \"R15(fresh) 未单独提及\"\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n\n- id: \"R9-W3\"\n  summary: \"Capability Gap Hypothesis 基于极小样本 (n=6)\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 17\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14(fresh) 共识: 仅6条件仅Mistral-7B显著, 需软化结论\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15(fresh) 共识: §6 escape仅SC<40%验证, 'SC≈70%'无数据支撑\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 共识AGREE: 仅1个条件显著(Mistral-7B SC=39.33%), 'principle'措辞过强\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 共识AGREE: Spearman ρ=1.0(n=6)鲁棒性存疑, 建议'preliminary evidence'而非'confirming'. R2补充: 方向性发现仍有启示价值\"\n  action_items:\n    - round: 14\n      action: \"§6结论软化为preliminary evidence + 讨论task gap\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R9-VL1\"\n  summary: \"Pages 1-2 连续纯文本无 display item\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16 视觉审查: Page 1纯文本(Abstract+Intro), Figure 1在page 2顶部\"\n    - round: 17\n      reviewers: []\n      note: \"R17 视觉审查: Figure 1在page 2顶部, 在3页窗口内可接受\"\n\n- id: \"R9-VL4\"\n  summary: \"Discussion/Conclusion 展开不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n\n- id: \"R10-N1\"\n  summary: \"Proposition 1 (Self-Extraction Ceiling) 无证明——empirical claim dressed as theorem\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 13\n  resolution: \"当前论文使用 Proposition 1 with formal proof (page 6)\"\n  resolution_round: 13\n\n- id: \"R10-N2\"\n  summary: \"κ→K_eff 映射理论基础不足——r=0.625 验证弱\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R16(fresh) R1-W7: K_eff exchangeable correlation假设可能被违反, minor concern\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及此技术点, 但R2-W4要求K_eff增加直觉解释, R1 AGREE\"\n\n- id: \"R10-N3\"\n  summary: \"Capability gap 'perfectly monotonic' 结论基于 n=6 非独立数据点\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 与R9-W3合并\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 与R9-W3合并. 共识: n=6 suggestive非definitive\"\n\n- id: \"R10-W1\"\n  summary: \"DRC τ 阈值无 held-out 评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n\n- id: \"R10-W2\"\n  summary: \"Cross-architecture NLI escape 适用面极窄\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R1-W8+R2-W3共识: generalizability受限, 仅NLI-friendly数据集测试\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R1-W3+R2 AGREE: 仅6条件, 仅Mistral显著. 但方向性发现有启示价值\"\n\n- id: \"R10-W3\"\n  summary: \"四种子复制方差大 + 统计功效 <21%\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R1-W3: multi-seed仅2/6模型, seed noise ±2.34pp超过多数|Δ|\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R1-W5: 仅2/6模型有multi-seed. R2 REBUT(降级nice-to-have): 现有2模型方向一致. 轻微分歧: R1认为should-fix, R2认为nice-to-have\"\n\n- id: \"R10-W4\"\n  summary: \"TOST ±2pp margin 缺少显式理由\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R16(fresh) R1-N2: ±2pp margin缺乏先验依据\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R1-Q3问TOST先验依据, R2 AGREE: 是否基于领域惯例还是事后选择? 共识: 需说明选择依据\"\n\n- id: \"R10-W5\"\n  summary: \"Bias Ratio 无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"BR CI 已整合: Mistral [3.98,6.37], Qwen [2.44,7.11]\"\n  resolution_round: 10\n\n- id: \"R10-W6\"\n  summary: \"SatLM specification-generation vs SICA trace-extraction 对比不充分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n\n- id: \"R10-W7\"\n  summary: \"'Symbolic Confirmation Bias' 需与近期 CoT confirmation bias 工作区分\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R2-N1: SCB是Huang(2024)+Wan(2025)的自然延伸\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R2-N3 critical: Wan et al.(2025)已证明CoT confirmation bias, SCB可能是FOL载体实例化. R1 AGREE w/nuance: SCB有aggregation-level结构性区分(source-attribution退化), 但需更充分对比. 部分共识: 定位为'complementary formal verification instance'而非独立发现\"\n\n- id: \"R10-W8\"\n  summary: \"Related Work 过度压缩——引用列表而非文献讨论\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [2]\n      note: \"R16(fresh) R2-M5: §2段间逻辑衔接不够清晰\"\n    - round: 17\n      reviewers: [2]\n      note: \"R17(fresh) R2 minor: §2三个子节间缺显式逻辑连接句\"\n\n- id: \"R10-I1\"\n  summary: \"'Symbolic Mirage' 概念新颖性——与 Huang/Wan 的 confirmation bias 区别\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 同R10-W7\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 同R10-W7. 共识: 需更充分对比Wan et al.(2025)\"\n\n- id: \"R10-I2\"\n  summary: \"Independence-Accuracy Trade-off 作为独立贡献有 bias-variance 重述嫌疑\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n\n- id: \"R10-VL1\"\n  summary: \"主文缺结果可视化\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16 视觉审查: 主文5 display items\"\n    - round: 17\n      reviewers: []\n      note: \"R17 视觉审查: 主文7 display items(Figure 1-4 + Table 1-3), 密度0.88/页, 合理\"\n\n- id: \"R11-N1\"\n  summary: \"Spearman ρ=1.0 (n=6) 被过度使用——有效自由度远低于6\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 与R9-W3合并\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R1-W3: 6点完美排名相关鲁棒性极低, 移除任一点可能破坏. R2 AGREE\"\n\n- id: \"R11-N2\"\n  summary: \"中心 claim 'SICA fails' 与统计功效不匹配——Abstract/title 过强\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 共识critical: power<21%, 建议标题改为'Do Not Substantially Improve'或加power caveat\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 共识critical: 当前标题'Do Not Substantially Improve'仍过强——10/16条件underpowered, 'We show the answer is no'(Abstract)逻辑不一致. R1建议'Show No Significant Improvement'; R2建议限定'confirmed equivalent vs underpowered/inconclusive'. GSM8K(n=30)/AIME(n=22)不应与n=200+并列. 完全共识\"\n  action_items:\n    - round: 16\n      action: \"标题软化 + Abstract加power caveat + TOST margin sensitivity analysis\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 17\n      action: \"标题进一步软化(当前'Substantially'仍不够); Abstract区分confirmed-equivalent vs underpowered; Table 1标注每条件power或区分powered/underpowered\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R11-N3\"\n  summary: \"TOST ±2pp margin 缺乏 principled 论证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 需补充不同margin的TOST sensitivity\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R1-Q3+R2 AGREE: 是领域惯例还是事后选择? 需说明依据, 存在specification searching风险\"\n\n- id: \"R11-W1\"\n  summary: \"DRC 评估不充分——仅PW完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n\n- id: \"R11-W2\"\n  summary: \"BR 指标存在循环论证倾向\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R2-N2 critical: 需permutation null model\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R1-W2+R2 fully AGREE: 纯随机约束-答案关联在60:40分布下已产生BR=1.5. 需permutation null distribution量化excess bias. R2补充: excess bias=0时negative result仍成立, 但'structural bias'声称需excess>0. 共识: 需null model分解\"\n  action_items:\n    - round: 16\n      action: \"BR降级为描述性指标并明确声明base-rate组成\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 17\n      action: \"计算base-rate predicted BR(nâ/max n_{a≠â})并与observed BR对比; 或运行permutation test建立null BR分布\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R11-W3\"\n  summary: \"术语过度品牌化——'Symbolic Mirage' 偏 dramatic\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R2-W5 minor: section title修辞色彩过强. R1 REBUT: 有技术对应物(Proposition 1退化), 非空洞修辞, 类似'Lottery Ticket'. 分歧: R2建议改技术性标题, R1建议保留术语但改section title\"\n\n- id: \"R11-W4\"\n  summary: \"新颖性定位需更早更明确建立与先验工作的 distinction\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R2-N1+R2-W5: SCB是Huang的自然延伸\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 与R10-W7合并. R1 AGREE w/nuance: SCB有结构层面区分(aggregation-level而非behavioral), 但需1-2段显式对比Wan et al.\"\n\n- id: \"R11-W5\"\n  summary: \"Independence-Accuracy Trade-off 应定位为量化而非新发现\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n\n- id: \"R11-W6\"\n  summary: \"遗漏引用: Byerly & Khashabi (2026 TACL) 等\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"当前论文已引用 Byerly and Khashabi (2026)\"\n  resolution_round: 13\n\n- id: \"R11-W7\"\n  summary: \"27 策略计数膨胀 + 未尝试 trained constraint extractor\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R2-W4: 27策略局限于self-extraction paradigm内变体\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R2-W3 scope震荡: 27变体全在SICA paradigm内但claim暗示'all training-free methods'. R1 AGREE w/nuance: generality来自数学结构, 但需明确标注实验覆盖边界\"\n\n- id: \"R11-VL1\"\n  summary: \"主文缺结果可视化——需上提 Figure 到主文\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16 视觉审查: Figure 2-4已在主文\"\n    - round: 17\n      reviewers: []\n      note: \"R17 视觉审查: 主文7 display items, 密度合理\"\n\n- id: \"R12-N1\"\n  summary: \"标题 overclaiming about frontier scale\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 标题已含'Logical Reasoning'\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 与R11-N2合并. 标题scope已改善('Logical Reasoning')但'Do Not Substantially Improve'仍overclaiming\"\n\n- id: \"R12-N2\"\n  summary: \"SCB 核心新颖性不足——self-correction failure 在 FOL 载体上的实例化\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R2-N1 critical\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R2-N3 critical + R1 AGREE w/nuance. R1认为SCB有独立的aggregation-level贡献(source-attribution退化 vs Wan的behavioral观察), 但同意需更充分对比. 部分共识\"\n\n- id: \"R12-N3\"\n  summary: \"DRC 作为 Contribution 4 不够充分\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"DRC demoted to practical observation in §6\"\n  resolution_round: 13\n  first_raised_round: 12\n  last_seen_round: 13\n\n- id: \"R12-W1\"\n  summary: \"BR 可能存在循环论证——56.4%零变量重叠使约束按定义支持source answer\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"与R11-W2合并\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"与R11-W2合并. R1-W2需null model分解\"\n\n- id: \"R12-W2\"\n  summary: \"CIL 名称和 information-theoretic 声称有误导\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Renamed to CCR, removed 'unify' claim\"\n  resolution_round: 13\n  first_raised_round: 12\n  last_seen_round: 13\n\n- id: \"R12-W3\"\n  summary: \"Figure 2 placement——应在正文而非附录\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Figure 2 已在正文 page 4\"\n  resolution_round: 13\n\n- id: \"R12-W4\"\n  summary: \"Appendix vs 主文关键信息分配不合理\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [2]\n      note: \"R16(fresh) R2-M3: Abstract信息过载\"\n    - round: 17\n      reviewers: [2]\n      note: \"R17(fresh) R2 minor: Abstract ~6个核心发现信息密度过高; 符号过载(BR/K_eff/C₀/κ/σ/α/Δ等)\"\n\n- id: \"R12-EC1\"\n  summary: \"Extractor Confound——所有 frontier cross-model extraction 使用同一 Mistral-7B extractor\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n\n- id: \"R13-N1\"\n  summary: \"摘要 BR 4.97× 选择性报告——最极端条件\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) Abstract已改为报告range 1.66×-4.97×\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及. Abstract当前报告'from 1.66× to 4.97×', 覆盖全范围\"\n\n- id: \"R13-N2\"\n  summary: \"统计功效呈现不足——10/16 underpowered, power analysis 埋在附录\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"与R11-N2合并\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 与R11-N2合并. 共识: Table 1应标注power或区分powered/underpowered条件. GSM8K/AIME应移至Appendix或标为exploratory\"\n\n- id: \"R13-N3\"\n  summary: \"α=0.5 无敏感性分析\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"论文有Table 11 α ablation ≥99% agreement\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R1-W4+R2 AGREE: ≥99% agreement是ceiling effect而非鲁棒性. 退化条件|C⁻|≈0使α无关. 论文应重新解释为退化corroborating evidence而非方法鲁棒性\"\n\n- id: \"R13-W1\"\n  summary: \"符号/指标过载——8页内7个定量工具\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n    - round: 17\n      reviewers: [2]\n      note: \"R17(fresh) R2 minor: BR/K_eff/C₀/κ/σ/α/Δ/CCR/ProcessSim等大量符号. 建议CCR和ProcessSim定义移至Appendix\"\n\n- id: \"R13-W2\"\n  summary: \"NLI claim 须限定到命题逻辑任务\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R16(fresh) R1-W9: 99%约束是propositional level\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n\n- id: \"R13-W3\"\n  summary: \"语法去重可能膨胀 BR——未报告语义去重后 BR\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及. 但与R11-W2(BR null model)相关\"\n\n- id: \"R13-W4\"\n  summary: \"Symbolic Mirage Hypothesis §3.3 与 §5 验证不连贯\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"当前论文无显式§3.3 Hypothesis section\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n\n- id: \"R13-W5\"\n  summary: \"缺引: Dhuliawala et al. 2023 Chain-of-Verification\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"已引用 dhuliawala2023chainofverification\"\n  resolution_round: 14\n\n- id: \"R14-N1\"\n  summary: \"标题'LLM Reasoning'范围超出实验证据——仅覆盖逻辑推理\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 标题已为'LLM Logical Reasoning'\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 标题scope改善, 但'Do Not Substantially Improve'仍overclaiming. 与R11-N2合并\"\n\n- id: \"R14-N2\"\n  summary: \"Symbolic Mirage Hypothesis Predictions 1-2 为事后总结非独立预测\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"当前论文无显式Predictions标签\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n\n- id: \"R14-W1\"\n  summary: \"Cross-architecture实验仅6条件/单一verifier/仅Mistral-7B显著\"\n  category: experiment\n  severity: major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) 共识: 降级为'preliminary observation'\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R1-W3+R2 AGREE: 方向性发现有价值但证据不足支撑强因果声明. 建议'suggesting/preliminary evidence'而非'confirming'\"\n\n- id: \"R14-W2\"\n  summary: \"8页正文信息过载——§5.5/§6/§7展开不足\"\n  category: writing\n  severity: major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [2]\n      note: \"R16(fresh) R2-M3: Abstract信息过载\"\n    - round: 17\n      reviewers: [2]\n      note: \"R17(fresh) R2 minor: Abstract ~6核心发现, 符号过载, K_eff缺直觉解释\"\n\n- id: \"R14-W3\"\n  summary: \"'No evidence' claim scope与统计功效不匹配\"\n  category: framing\n  severity: major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"与R11-N2合并\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"与R11-N2合并. 共识critical\"\n\n- id: \"R14-W4\"\n  summary: \"BR计算子集大小(n_err)未报告\"\n  category: experiment\n  severity: moderate\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"当前论文Table 2已有n_err列\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R1-Q5: Gemini n_err≈12导致BR=12.19不稳定. R2 AGREE: 需检查base-rate分布. 与R11-W2(BR null model)相关\"\n\n- id: \"R14-W5\"\n  summary: \"Related Work遗漏: SETS(2025), MAV(2025)\"\n  category: writing\n  severity: minor-to-major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16(fresh) R2-W2新增: S²R, DuPO, Kamoi et al.\"\n    - round: 17\n      reviewers: [2]\n      note: \"R17(fresh) R2新增遗漏: Reflexion(Shinn 2023), LATS(Zhou 2023), STaR(Zelikman 2022). R1 AGREE Reflexion/LATS可作alternative self-improvement范式在§2简提, STaR相关性有限\"\n\n- id: \"R14-W6\"\n  summary: \"Fleiss' κ→ICC近似仅r=0.625——prevalence paradox\"\n  category: method\n  severity: moderate\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"minor, 不影响核心结论\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n\n# R15 issues\n\n- id: \"R15-M1\"\n  summary: \"遗漏引用: DuPO (ICLR 2026)\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"共识AGREE\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W2提出\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及. 论文§2已引用dupo2025\"\n\n- id: \"R15-M2\"\n  summary: \"遗漏引用: S²R (2025)\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"共识AGREE\"\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2-W2提出\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及. 论文§2已引用zeng2025s2r\"\n\n- id: \"R15-M3\"\n  summary: \"遗漏引用: LLM as Formalizers on CSP\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16(fresh) 未单独提及\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n\n- id: \"R15-M4\"\n  summary: \"遗漏引用: Lakshminarayanan et al. (2017) Deep Ensembles\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"R1 REBUT: Kuncheva等已更直接相关\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n\n- id: \"R15-W1\"\n  summary: \"α=0.5敏感性分析≥99% agreement是ceiling effect\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"ceiling effect不等于鲁棒性\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R1-W4+R2 AGREE: 退化条件|C⁻|≈0使α无关, 应解释为退化证据而非鲁棒性. 共识\"\n\n# R16 issues\n\n- id: \"R16-N1\"\n  summary: \"Proposition 1 证明范围与声称范围不匹配 + 证明逻辑跳跃\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R16: Part(i)依赖SICA特定scoring, 非数学必然; Part(ii) DPI近平凡\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R1-N1 critical: 证明从Eq.3跳到score(a)=nₐ缺关键步骤——(1)退化条件|C⁻|≈0未证明; (2)约束跨答案组不重叠未证明; (3)42.9%去重率导致权重不均匀, Σwc≠nₐ而是∝nₐ. R2 fully AGREE并补充: 比例关系可能保持argmax但精确等式不成立. 两人从不同角度(R1:评分函数, R2:Markov chain)暴露证明缺陷. 共识: 需(a)完善证明列出所有假设, 或(b)弱化为argmax preservation, 或(c)补充经验验证\"\n  action_items:\n    - round: 16\n      action: \"将Proposition 1分为source-attribution退化定理(精确但specific) + DPI bound(普遍但弱)\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 17\n      action: \"修复score(a)=nₐ证明: 明确假设(约束不重叠+权重均匀化条件), 或改为argmax preservation证明, 或补充经验rank agreement\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R16-N2\"\n  summary: \"Diagnostics 100%准确率是in-sample评估——overfitting风险, holdout验证不充分\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"决策边界在同一60条件上推导和评估; holdout仅1条件; 60条件全negative\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R1-N3+R2 AGREE: trivial 'always predict negative' classifier也100%. 真正的验证需positive cases但论文核心论点是不存在正例(内在矛盾). R2精辟补充: 框架价值在failure mode分类(退化型/多样性不足型/确认偏差型)而非二分类预测, 建议改'correctly characterizes failure mode'而非'correctly classifies'. R1建议用§6 cross-arch escape作positive validation. 共识: 降级claim + 重新定位为排除工具\"\n  action_items:\n    - round: 16\n      action: \"增加held-out验证 + 弱化claim + 报告60条件组成\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 17\n      action: \"重新定位: (a)'correctly characterizes failure mode'替代'correctly classifies'; (b)用§6 cross-arch作positive validation; (c)承认仅negative cases验证; (d)定位为'ruling-out tool'而非通用诊断\"\n      assigned_to: \"paper_agent\"\n      status: open\n\n- id: \"R16-M1\"\n  summary: \"遗漏引用: Kamoi et al. (TACL 2024) self-correction survey\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"R2提出, R1 AGREE\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 论文§2已引用kamoi2024selfcorrect. 已解决\"\n\n- id: \"R16-M2\"\n  summary: \"遗漏引用: AlphaCode/CodeT\"\n  category: writing\n  severity: minor\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1]\n      note: \"code domain约束过滤成功案例\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 论文§2已引用li2022alphacode和chen2023codet. 已解决\"\n\n- id: \"R16-W1\"\n  summary: \"'Extending Huang et al.' overclaiming\"\n  category: framing\n  severity: major\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"建议改为'provide independent evidence consistent with'\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 与R10-W7/R12-N2合并. 当前论文§1/§2使用'provide independent evidence consistent with'措辞, 但§5.1和Abstract仍有'extending'暗示\"\n\n- id: \"R16-W2\"\n  summary: \"GSM8K(n=30)/AIME(n=22)与大样本等权重引用\"\n  category: experiment\n  severity: major\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"正文引用时未区分\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R1-N2+R2 AGREE: GSM8K/AIME在Table 1中与n=200+并列未区分. 建议移至Appendix或标为exploratory. 共识\"\n\n- id: \"R16-W3\"\n  summary: \"缺少training-based self-verification讨论\"\n  category: writing\n  severity: major\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: [1, 2]\n      note: \"§2增加training-based段落, 引用S²R/DuPO\"\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 论文§2已有'Training-based verification'段落, 引用了S²R/DuPO/AlphaCode/CodeT. 基本解决\"\n\n- id: \"R16-SYS1\"\n  summary: \"Scope震荡——SICA-specific和general claims反复切换\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"全文scope qualifier修复需要\"\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R2-W3+R1 AGREE w/nuance: Prop 1 generality来自数学结构但实验覆盖限于SICA paradigm. R1建议§7加一句边界声明. 共识: 需在§1 contributions中明确界定scope\"\n\n# R17(fresh) 新发现\n\n- id: \"R17-N1\"\n  summary: \"Corollary 1 (DPI) 应降级为 Remark——'deterministic function 不增加信息量'是信息论教科书练习\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-W1+R2-W1共识AGREE: I(C;Y)≤I(T;Y)几乎是同义反复. 论文承认'contribution is identifying the Markov chain'而非推导. 建议降级Corollary 1为Remark, 或更清楚地说明Markov chain识别的non-trivial贡献在哪里\"\n\n- id: \"R17-N2\"\n  summary: \"K_eff 缺少直觉解释——非 ensemble-theory 背景读者理解困难\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R2-W4+R1 AGREE: K_eff=K/[1+(K-1)·κ]需具体示例(如'K=12, κ=0.7 → K_eff≈1.3, 12条高度相关trace仅等价于1.3条独立trace'). 共识\"\n\n- id: \"R17-N3\"\n  summary: \"遗漏引用: Reflexion(Shinn 2023), LATS(Zhou 2023)\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R2提出, R1部分AGREE: 可作alternative self-improvement范式在§2简提. STaR(Zelikman 2022)相关性有限\"\n\n- id: \"R17-N4\"\n  summary: \"Table 1 排版: 未标注每条件统计功效, 读者需翻Appendix D发现10/16 underpowered\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R1-N2+R2 AGREE: Table 1应以视觉标记区分powered/underpowered条件\"\n\n- id: \"R17-VL1\"\n  summary: \"Figure 4 内部文字过小——打印/缩小后可读性差\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"视觉审查发现: page 7 Figure 4每个彩色方框内含3-5行小字, 建议精简或增大图尺寸\"\n\n- id: \"R17-VL2\"\n  summary: \"Appendix pages 16/22 表格堆叠过度拥挤\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"视觉审查: page 16含5个表格+4个小节, page 22含5个表格+多个小节. 建议适当分页或合并\"\n"
  }
}
```

</details>

---


### Tool result

_source line 1795 · 2026-05-23T09:36:35.093049+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml\", \"bytes\": 31593}, \"error\": \"\"}"}

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

_source line 1796 · 2026-05-23T09:39:17.379995+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 17 (Fresh) 审稿报告\n\n**论文**: \"Beyond Self-Consistency: Self-Extracted Constraints Do Not Substantially Improve LLM Logical Reasoning\"\n**Venue**: EMNLP 2026 via ACL Rolling Review\n**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验设计; R2: 新颖性 + 完整性）\n**交叉分享**: 完成，1 轮收敛\n\n---\n\n## Summary\n\n本文引入 SICA（Symbolic Invariant Consensus Aggregation），从 LLM chain-of-thought traces 中提取逻辑约束并通过加权 MAX-SAT 聚合答案。在 6 个模型（7B–32B）、3 个推理领域上，SICA 与多数投票结果在 94.4% 的问题上一致，无条件显示显著正向效果（BH 校正后）。论文将此归因于 \"Symbolic Confirmation Bias\"（SCB），通过 Proposition 1（Source-Attribution Degeneration）和 Corollary 1（DPI Information Ceiling）形式化。27 个 training-free 变体均产生中性至负面结果。三个零成本诊断指标（C₀, BR, K_eff）在 60 个条件上 100% 分类。跨架构验证（DeBERTa NLI）在弱生成器上展示逃逸可能。\n\n---\n\n## Strengths\n\n**S1. 实验规模与方法论严谨性。** 9 个模型（含 frontier）、3 个推理域、27 个 training-free 变体的系统覆盖。统计方法完备：TOST 等价性检验、McNemar + BH 校正、bootstrap CI、功效分析。这是该领域最系统的 negative result 研究之一。[R1-S1, R2-S1]\n\n**S2. 因果分析链条清晰。** 从现象（SICA ≈ SC）→ 机制（trace-count 分布决定约束分布）→ 理论（DPI Markov chain）→ 逃逸条件（跨架构独立性），层层递进。Figure 3 因果 DAG 和 Figure 1 pipeline 图有效辅助理解。[R1-S2, R2-S3]\n\n**S3. Oracle 对照设计精确定位瓶颈。** Gold FOL 替换自提取约束后 MAX-SAT 产生 +29.91pp 增益（Appendix G），明确瓶颈在约束提取而非求解器，避免了对 MAX-SAT 机制的混淆。[R1-S3]\n\n**S4. 诊断框架具有实际潜力。** C₀、BR、K_eff 三个指标可在 pilot run 中预估 self-extraction 方法的前景，对从业者有指导意义——尽管 100% accuracy 声称需要软化（见 W3）。[R2-S2]\n\n**S5. 诚实的统计报告。** 论文坦承 10/16 条件统计功效不足、模型范围局限、multi-seed 覆盖不完整。这种透明度在 negative result 论文中值得肯定。[R1-S5, R2-S5]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1** [critical, 共识] **Proposition 1 证明存在关键逻辑跳跃。**\n证明直接声称 \"score(a) = Σ 1[aᵢ = a] = nₐ\"，但 SICA 的实际评分函数（Eq. 3）涉及约束权重 wc（去重后 trace 计数）和源归属指示函数 σ(c,a)。从 Eq. 3 到 score(a) = nₐ 需要证明：(1) 退化条件下 |C⁻| ≈ 0；(2) 不同答案组约束不重叠；(3) 42.9% 去重率下权重分布使 Σwc 精确等于 nₐ 而非仅成比例。R2 补充：比例关系可能保持 argmax 但精确等式不成立。Proposition 1 是全文理论框架的基石，证明不完整使理论贡献从 \"形式化证明\" 降级为 \"经验观察\"。\n**修复方向**: (a) 完善证明列出所有假设；或 (b) 弱化为 argmax preservation（ranking 保持）；或 (c) 补充经验 rank agreement 验证。\n[R1-N1 提出, R2 fully AGREE]\n\n**W2** [critical, 共识] **标题/Abstract 的全称否定与统计证据不匹配。**\n标题 \"Do Not Substantially Improve\" 和 Abstract 的 \"We show the answer is no\" 是全称判断，但 TOST 仅 4/16 条件确立等价（±2pp），10 条件 underpowered（power < 21%, MDE ≥ 1.86pp）。论文无法区分 \"SICA 无效\" 和 \"样本不够大\"。GSM8K (n=30) 和 AIME (n=22) 在 Table 1 中与 n=200+ 条件无区分地并列，加剧误导。\n**修复方向**: (a) 标题改为限定性表述（如 \"Show No Significant Improvement\"）；(b) Abstract 区分 confirmed-equivalent vs. underpowered/inconclusive；(c) Table 1 视觉标记 powered/underpowered 条件；(d) GSM8K/AIME 移至 Appendix 或标为 exploratory。\n[R2-N1 提出, R1 fully AGREE]\n\n**W3** [critical, 共识] **诊断框架 100% 准确率是 trivial 的。**\n60 个条件全部为 null 或 negative，trivial \"always predict no improvement\" classifier 也能达到 100%。Holdout 验证仅 2 个模型系列（LLaMA-3.1-8B、Qwen3-14B），且同为 negative cases。框架的区分能力（discriminative power）未经正例验证。论文将此列为三大贡献之一，但无正例的框架无法预测何时 self-extraction *会* 有效。R2 精辟指出：框架的实际价值在于 failure mode 分类（退化型/多样性不足型/确认偏差型），而非二分类预测。\n**修复方向**: (a) 改 \"correctly classifies\" 为 \"correctly characterizes the failure mode\"；(b) 用 §6 cross-arch escape 的 Mistral-7B 条件作 positive validation；(c) 定位为 \"ruling-out tool\" 而非通用诊断。\n[R1-N3 提出, R2 fully AGREE]\n\n**W4** [critical, 部分共识] **SCB 与已有 confirmation bias 工作的新颖性区分不充分。**\nWan et al. (2025) 已证明 CoT confirmation bias，SCB 可能是同一现象在 FOL/symbolic 载体上的实例化。论文 §2 仅一句区分（\"symbolic confirmation bias is distinct from CoT unfaithfulness\"），未充分对比。Jhaveri & Kersting (2026) 进一步削弱新颖性。R1 部分反驳：SCB 有独立的 aggregation-level 结构性区分——source-attribution scoring 退化是关于 aggregation mechanism 的形式化结论，非推理忠实性结论；且 94.4% 约束通过 Z3 验证说明问题不在约束不可靠而在不提供超越 trace 的信息。\n**共识**: 需 1-2 段显式对比 Wan et al.，明确 SCB 的增量贡献在于 DPI 形式化和 source-attribution 机制，定位为 \"complementary instance in formal verification\" 而非全新概念。\n[R2-N3 提出, R1 AGREE with nuance]\n\n### Should-Fix（影响评分但不一票否决）\n\n**W5** [warning, 共识] **Corollary 1 (DPI) 理论贡献度偏弱。**\nI(C;Y) ≤ I(T;Y) 是 DPI 在 Markov chain T→C 上的直接应用，接近信息论教科书练习。贡献在于 Markov chain 建模识别而非推导。建议降级为 Remark。[R1-W1, R2-W1, 共识]\n\n**W6** [warning, 共识] **Bias Ratio (BR) 缺少 null model 分解。**\n60% trace 产生答案 a 时，纯随机约束-答案关联已产生 BR = 1.5。Table 2 的 BR 值（1.66×–4.97×）部分可能由 base rate 解释。需 permutation null model 量化 excess bias。即使 excess = 0，negative result 仍成立，但 \"structural bias\" 声称需 excess > 0。[R1-W2 提出, R2 fully AGREE]\n\n**W7** [warning, 共识] **Cross-architecture escape (§6) 结论过度推断。**\n仅 6 个 generator-verifier 条件，仅 Mistral-7B (SC=39.33%) 显著。Spearman ρ=1.0 (n=6) 鲁棒性低。\"Capability-gap pattern\" 数据不足。R2 补充：方向性发现有启示价值但不足以建立一般规律。建议措辞从 \"confirming\" 改为 \"suggesting\" 或 \"preliminary evidence\"。[R1-W3, R2 AGREE]\n\n**W8** [warning, 共识] **α=0.5 sensitivity 分析实质上确认退化。**\nTable 11 所有 α∈{0.1,...,1.0} 下 SICA-SC agreement ≥ 99%——这是 ceiling effect（|C⁻| ≈ 0 使 α 无关），非方法鲁棒性。论文应重新解释为退化的 corroborating evidence。[R1-W4, R2 AGREE]\n\n**W9** [warning, 共识] **Scope 震荡。**\n论文在 SICA-specific findings 和 general impossibility claims 之间摆动。Proposition 1 声称适用于 \"any self-extraction pipeline\"，但 27 个实验变体全在 SICA 范式内。建议在 §1 contributions 中明确界定实验覆盖的 scope 边界。[R2-W3, R1 AGREE with nuance]\n\n**W10** [warning, 共识] **K_eff 可读性不足。**\nK_eff = K/[1+(K-1)·κ] 对非 ensemble-theory 背景读者缺少直觉解释。建议添加具体示例（如 \"K=12, κ=0.7 → K_eff ≈ 1.3\"）。[R2-W4, R1 AGREE]\n\n### Minor Issues\n\n- **符号过载**: 正文 8 页内引入 BR, K_eff, C₀, κ, σ, α, Δ, score(a), CCR, ProcessSim 等。建议 CCR/ProcessSim 定义移至 Appendix。[R2]\n- **Abstract 信息密度过高**: ~6 个核心发现压缩在一段。建议精简为中心 negative finding + 机制 + scope。[R2]\n- **§2 段间衔接**: 三个子节间缺显式逻辑连接句。[R2]\n- **Table 1 统计功效未标注**: 读者需翻 Appendix D 才发现 10/16 underpowered。[R1]\n- **TOST ±2pp margin 缺先验依据**: 是领域惯例还是事后选择？存在 specification searching 风险。[R1-Q3, R2 AGREE]\n- **Multi-seed 覆盖率**: 仅 2/6 模型有 multi-seed replication。[R1-W5, R2 REBUT：现有两模型方向一致，降级 nice-to-have]\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全达成一致（[AGREE]）：\n\n1. **Proposition 1 证明不完整**——score(a) = nₐ 从 Eq. 3 推导缺关键步骤 [R1-N1, R2 AGREE]\n2. **标题/Abstract overclaim**——10/16 underpowered，\"We show the answer is no\" 逻辑不一致 [R2-N1, R1 AGREE]\n3. **诊断框架 trivial classifier 问题**——60 全阴性条件，框架价值在 failure mode 分类而非预测 [R1-N3, R2 AGREE]\n4. **Corollary 1 近 trivial**——应降级 Remark [R1-W1, R2-W1]\n5. **BR 缺 null model**——需 permutation 分解 base-rate vs. excess bias [R1-W2, R2 AGREE]\n6. **Cross-arch 过度推断**——n=6 不够，\"preliminary evidence\" 而非 \"confirming\" [R1-W3, R2 AGREE]\n7. **α sensitivity = 退化确认**——ceiling effect，非鲁棒性 [R1-W4, R2 AGREE]\n\n## Reviewer Divergence\n\n1. **SCB 新颖性**: R2 认为 SCB 是 CoT confirmation bias 的 FOL 实例化（critical），R1 部分反驳认为 SCB 有独立的 aggregation-level 贡献但同意需更充分对比。→ **部分共识**：需增加对比段落。\n\n2. **Multi-seed 覆盖**: R1 认为 should-fix（Δ ∈ [-4.41, +3.43] 跨正负），R2 REBUT 降级 nice-to-have（现有两模型方向一致）。→ **轻微分歧**。\n\n3. **\"Symbolic Mirage\" 术语**: R2 认为过度品牌化（minor），R1 REBUT 认为有技术对应物。→ **轻微分歧**：R1 建议保留术语但改 section title。\n\n---\n\n## Questions to Authors\n\n**Q1.** Proposition 1 中 score(a) = nₐ 的精确等式如何从 Eq. 3 推导？特别是 42.9% 去重率导致权重不均匀，Σwc 与 nₐ 是等式还是比例关系？如果仅比例关系，argmax 保持是否有证明？\n\n**Q2.** 诊断框架在 trivial \"always predict negative\" baseline 之上的附加值具体体现在哪里？是否可用 §6 cross-arch escape 条件做 positive validation？\n\n**Q3.** TOST ±2pp margin 的先验依据是什么？高基线（SC ≥ 75%）下 2pp 相对效应量仅 ~2.7%，是否考虑按基线调整 margin？\n\n**Q4.** Cross-architecture 实验中 α 是否固定 0.5？跨模型设置下约束不再完全耦合到生成器分布，α 敏感性可能不同。\n\n**Q5.** Table 2 Gemini-2.5-Pro BR=12.19（n_err≈12）远高于其他模型——是 base-rate 效应还是 extraction 异常？\n\n---\n\n## Missing References\n\n**共识引用建议**:\n- Reflexion (Shinn et al., 2023) — self-reflection 范式，§2 简提\n- LATS (Zhou et al., 2023) — tree-search self-verification，§2 简提\n- Cohen's h 或标准化效应量 — 帮助读者理解 ±2pp 在不同基率下的意义\n\n**已确认引用（不再遗漏）**:\n- Kamoi et al. (TACL 2024) — 已引用 kamoi2024selfcorrect\n- AlphaCode/CodeT — 已引用 li2022alphacode, chen2023codet\n- S²R / DuPO — 已引用 zeng2025s2r, dupo2025\n\n---\n\n## External Review\n\n**外部审稿（Stanford Agentic Reviewer）**: 未请求（项目未配置）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: ✅ 完成\n**发现** (0 critical, 4 warning, 19 info):\n\n- ✅ 正文恰好 8 页，符合 EMNLP 2026 页数限制\n- ✅ Limitations 位于正文 conclusion 后、references 前，合规\n- ✅ 主文 7 个 display items（Figure 1-4 + Table 1-3），密度 0.88/页，合理\n- ✅ 所有 figure/table 出现在首次引用附近，无严重漂移\n- ✅ 引用格式统一，无 [?] 未解析\n- ✅ 散点图使用颜色+marker 形状双重编码，色盲友好\n- ⚠️ Figure 4（p7）内部文字过小——打印/缩小后可读性差，建议精简或增大\n- ⚠️ Appendix p16/p22 表格堆叠过密（各含 5 个表格），建议适当分页\n- ⚠️ Appendix pp25-26 连续纯文本无 display item\n\n---\n\n## Overall Assessment\n\n**Overall Score**: 3.0 — Findings\n\n**评分理由**:\n\n论文的实验工作量和方法论严谨性毋庸置疑——6 模型 × 3 域 × 27 变体的系统覆盖、Oracle 对照、multi-seed replication、完备的统计检验，这些在 negative result 研究中极为少见，值得肯定。\n\n但三大贡献均存在实质性问题：\n\n1. **Proposition 1**（理论贡献）——证明有逻辑跳跃，score(a) = nₐ 从 Eq. 3 推导不完整；Corollary 1 近 trivial。\n2. **诊断框架**（实用贡献）——60 条件全阴性使 100% accuracy 等价于 trivial classifier；正例验证缺失。\n3. **SCB 概念**（发现贡献）——与 Wan et al. (2025) CoT confirmation bias 的新颖性区分不充分。\n\n加之标题/Abstract 的全称否定与统计证据（10/16 underpowered）不匹配，论文的 claim 强度系统性地超出了证据支持。\n\n作为 negative result 论文，核心洞察可总结为 \"self-extracted constraints inherit the model's distributional prior\"——这在 Huang et al. (2024) 和 Wan et al. (2025) 之后非 entirely novel。论文的主要价值在于 rigor of systematic confirmation + failure mode taxonomy + practical diagnostics，更适合 Findings track。\n\n**如修复以下关键问题，可提升至 3.5 (Borderline Conference)**:\n- 补全 Proposition 1 证明（或弱化为 argmax preservation）\n- 标题/Abstract 软化，Table 1 区分 powered/underpowered\n- 诊断框架重定位为 failure mode 分类工具 + positive case 验证\n- SCB 与 Wan et al. 增加 1-2 段显式对比\n\n**Confidence**: 4/5（两位 Reviewer 均给出 4/5 confidence，初审评分一致 3.5，交叉分享后关键问题全部达成共识）\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"We show the answer is no\" 过于 categorical——10/16 underpowered 时应为 \"we find no evidence of improvement in powered conditions\"\n- 三个 contributions 列表中，Contribution 2（diagnostics）的 \"correctly classify all 60 tested conditions\" 需加 caveat\n\n### §3 Method\n- Eq. 3 的 scoring function 与 Proposition 1 证明的 score(a) = nₐ 之间需要桥接步骤\n- K_eff（Eq. 1）后应添加直觉解释示例\n- α=0.5 选择依据需补充\n\n### §4 Results\n- Table 1 应在表内标注统计功效或区分 powered/underpowered 条件\n- GSM8K (n=30) / AIME (n=22) 建议移至 Appendix 或标为 exploratory\n\n### §5 Analysis\n- §5.1 Proposition 1：补全 Eq. 3 → score(a) = nₐ 的证明步骤，或改为 argmax preservation\n- §5.1 Corollary 1：降级为 Remark\n- §5.1 BR：补充 base-rate predicted BR 与 observed BR 的分解对比\n- §5.1 关于 Wan et al. (2025) 的区分：增加 1-2 段显式对比\n- §5.3 Diagnostics：\"correctly classify\" → \"correctly characterize the failure mode\"；增加 positive validation\n\n### §6 Cross-Architecture Escape\n- \"Capability-gap pattern\" 基于 n=6，措辞改 \"preliminary evidence\" / \"suggesting\"\n- Spearman ρ=1.0 (n=6) 的鲁棒性问题需讨论\n\n### §7 Discussion\n- Scope 边界声明：实验覆盖限于 SICA paradigm，其他 self-extraction 架构的验证是 future work\n- α sensitivity 重新解释为退化证据\n\n### Appendix\n- Figure 4 内部文字过小\n- pp16/22 表格堆叠过密\n",
  "project": "symb_invariant_consensus",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0",
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
    "report": "# Round 17 (Fresh) 审稿报告\n\n**论文**: \"Beyond Self-Consistency: Self-Extracted Constraints Do Not Substantially Improve LLM Logical Reasoning\"\n**Venue**: EMNLP 2026 via ACL Rolling Review\n**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验设计; R2: 新颖性 + 完整性）\n**交叉分享**: 完成，1 轮收敛\n\n---\n\n## Summary\n\n本文引入 SICA（Symbolic Invariant Consensus Aggregation），从 LLM chain-of-thought traces 中提取逻辑约束并通过加权 MAX-SAT 聚合答案。在 6 个模型（7B–32B）、3 个推理领域上，SICA 与多数投票结果在 94.4% 的问题上一致，无条件显示显著正向效果（BH 校正后）。论文将此归因于 \"Symbolic Confirmation Bias\"（SCB），通过 Proposition 1（Source-Attribution Degeneration）和 Corollary 1（DPI Information Ceiling）形式化。27 个 training-free 变体均产生中性至负面结果。三个零成本诊断指标（C₀, BR, K_eff）在 60 个条件上 100% 分类。跨架构验证（DeBERTa NLI）在弱生成器上展示逃逸可能。\n\n---\n\n## Strengths\n\n**S1. 实验规模与方法论严谨性。** 9 个模型（含 frontier）、3 个推理域、27 个 training-free 变体的系统覆盖。统计方法完备：TOST 等价性检验、McNemar + BH 校正、bootstrap CI、功效分析。这是该领域最系统的 negative result 研究之一。[R1-S1, R2-S1]\n\n**S2. 因果分析链条清晰。** 从现象（SICA ≈ SC）→ 机制（trace-count 分布决定约束分布）→ 理论（DPI Markov chain）→ 逃逸条件（跨架构独立性），层层递进。Figure 3 因果 DAG 和 Figure 1 pipeline 图有效辅助理解。[R1-S2, R2-S3]\n\n**S3. Oracle 对照设计精确定位瓶颈。** Gold FOL 替换自提取约束后 MAX-SAT 产生 +29.91pp 增益（Appendix G），明确瓶颈在约束提取而非求解器，避免了对 MAX-SAT 机制的混淆。[R1-S3]\n\n**S4. 诊断框架具有实际潜力。** C₀、BR、K_eff 三个指标可在 pilot run 中预估 self-extraction 方法的前景，对从业者有指导意义——尽管 100% accuracy 声称需要软化（见 W3）。[R2-S2]\n\n**S5. 诚实的统计报告。** 论文坦承 10/16 条件统计功效不足、模型范围局限、multi-seed 覆盖不完整。这种透明度在 negative result 论文中值得肯定。[R1-S5, R2-S5]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1** [critical, 共识] **Proposition 1 证明存在关键逻辑跳跃。**\n证明直接声称 \"score(a) = Σ 1[aᵢ = a] = nₐ\"，但 SICA 的实际评分函数（Eq. 3）涉及约束权重 wc（去重后 trace 计数）和源归属指示函数 σ(c,a)。从 Eq. 3 到 score(a) = nₐ 需要证明：(1) 退化条件下 |C⁻| ≈ 0；(2) 不同答案组约束不重叠；(3) 42.9% 去重率下权重分布使 Σwc 精确等于 nₐ 而非仅成比例。R2 补充：比例关系可能保持 argmax 但精确等式不成立。Proposition 1 是全文理论框架的基石，证明不完整使理论贡献从 \"形式化证明\" 降级为 \"经验观察\"。\n**修复方向**: (a) 完善证明列出所有假设；或 (b) 弱化为 argmax preservation（ranking 保持）；或 (c) 补充经验 rank agreement 验证。\n[R1-N1 提出, R2 fully AGREE]\n\n**W2** [critical, 共识] **标题/Abstract 的全称否定与统计证据不匹配。**\n标题 \"Do Not Substantially Improve\" 和 Abstract 的 \"We show the answer is no\" 是全称判断，但 TOST 仅 4/16 条件确立等价（±2pp），10 条件 underpowered（power < 21%, MDE ≥ 1.86pp）。论文无法区分 \"SICA 无效\" 和 \"样本不够大\"。GSM8K (n=30) 和 AIME (n=22) 在 Table 1 中与 n=200+ 条件无区分地并列，加剧误导。\n**修复方向**: (a) 标题改为限定性表述（如 \"Show No Significant Improvement\"）；(b) Abstract 区分 confirmed-equivalent vs. underpowered/inconclusive；(c) Table 1 视觉标记 powered/underpowered 条件；(d) GSM8K/AIME 移至 Appendix 或标为 exploratory。\n[R2-N1 提出, R1 fully AGREE]\n\n**W3** [critical, 共识] **诊断框架 100% 准确率是 trivial 的。**\n60 个条件全部为 null 或 negative，trivial \"always predict no improvement\" classifier 也能达到 100%。Holdout 验证仅 2 个模型系列（LLaMA-3.1-8B、Qwen3-14B），且同为 negative cases。框架的区分能力（discriminative power）未经正例验证。论文将此列为三大贡献之一，但无正例的框架无法预测何时 self-extraction *会* 有效。R2 精辟指出：框架的实际价值在于 failure mode 分类（退化型/多样性不足型/确认偏差型），而非二分类预测。\n**修复方向**: (a) 改 \"correctly classifies\" 为 \"correctly characterizes the failure mode\"；(b) 用 §6 cross-arch escape 的 Mistral-7B 条件作 positive validation；(c) 定位为 \"ruling-out tool\" 而非通用诊断。\n[R1-N3 提出, R2 fully AGREE]\n\n**W4** [critical, 部分共识] **SCB 与已有 confirmation bias 工作的新颖性区分不充分。**\nWan et al. (2025) 已证明 CoT confirmation bias，SCB 可能是同一现象在 FOL/symbolic 载体上的实例化。论文 §2 仅一句区分（\"symbolic confirmation bias is distinct from CoT unfaithfulness\"），未充分对比。Jhaveri & Kersting (2026) 进一步削弱新颖性。R1 部分反驳：SCB 有独立的 aggregation-level 结构性区分——source-attribution scoring 退化是关于 aggregation mechanism 的形式化结论，非推理忠实性结论；且 94.4% 约束通过 Z3 验证说明问题不在约束不可靠而在不提供超越 trace 的信息。\n**共识**: 需 1-2 段显式对比 Wan et al.，明确 SCB 的增量贡献在于 DPI 形式化和 source-attribution 机制，定位为 \"complementary instance in formal verification\" 而非全新概念。\n[R2-N3 提出, R1 AGREE with nuance]\n\n### Should-Fix（影响评分但不一票否决）\n\n**W5** [warning, 共识] **Corollary 1 (DPI) 理论贡献度偏弱。**\nI(C;Y) ≤ I(T;Y) 是 DPI 在 Markov chain T→C 上的直接应用，接近信息论教科书练习。贡献在于 Markov chain 建模识别而非推导。建议降级为 Remark。[R1-W1, R2-W1, 共识]\n\n**W6** [warning, 共识] **Bias Ratio (BR) 缺少 null model 分解。**\n60% trace 产生答案 a 时，纯随机约束-答案关联已产生 BR = 1.5。Table 2 的 BR 值（1.66×–4.97×）部分可能由 base rate 解释。需 permutation null model 量化 excess bias。即使 excess = 0，negative result 仍成立，但 \"structural bias\" 声称需 excess > 0。[R1-W2 提出, R2 fully AGREE]\n\n**W7** [warning, 共识] **Cross-architecture escape (§6) 结论过度推断。**\n仅 6 个 generator-verifier 条件，仅 Mistral-7B (SC=39.33%) 显著。Spearman ρ=1.0 (n=6) 鲁棒性低。\"Capability-gap pattern\" 数据不足。R2 补充：方向性发现有启示价值但不足以建立一般规律。建议措辞从 \"confirming\" 改为 \"suggesting\" 或 \"preliminary evidence\"。[R1-W3, R2 AGREE]\n\n**W8** [warning, 共识] **α=0.5 sensitivity 分析实质上确认退化。**\nTable 11 所有 α∈{0.1,...,1.0} 下 SICA-SC agreement ≥ 99%——这是 ceiling effect（|C⁻| ≈ 0 使 α 无关），非方法鲁棒性。论文应重新解释为退化的 corroborating evidence。[R1-W4, R2 AGREE]\n\n**W9** [warning, 共识] **Scope 震荡。**\n论文在 SICA-specific findings 和 general impossibility claims 之间摆动。Proposition 1 声称适用于 \"any self-extraction pipeline\"，但 27 个实验变体全在 SICA 范式内。建议在 §1 contributions 中明确界定实验覆盖的 scope 边界。[R2-W3, R1 AGREE with nuance]\n\n**W10** [warning, 共识] **K_eff 可读性不足。**\nK_eff = K/[1+(K-1)·κ] 对非 ensemble-theory 背景读者缺少直觉解释。建议添加具体示例（如 \"K=12, κ=0.7 → K_eff ≈ 1.3\"）。[R2-W4, R1 AGREE]\n\n### Minor Issues\n\n- **符号过载**: 正文 8 页内引入 BR, K_eff, C₀, κ, σ, α, Δ, score(a), CCR, ProcessSim 等。建议 CCR/ProcessSim 定义移至 Appendix。[R2]\n- **Abstract 信息密度过高**: ~6 个核心发现压缩在一段。建议精简为中心 negative finding + 机制 + scope。[R2]\n- **§2 段间衔接**: 三个子节间缺显式逻辑连接句。[R2]\n- **Table 1 统计功效未标注**: 读者需翻 Appendix D 才发现 10/16 underpowered。[R1]\n- **TOST ±2pp margin 缺先验依据**: 是领域惯例还是事后选择？存在 specification searching 风险。[R1-Q3, R2 AGREE]\n- **Multi-seed 覆盖率**: 仅 2/6 模型有 multi-seed replication。[R1-W5, R2 REBUT：现有两模型方向一致，降级 nice-to-have]\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 完全达成一致（[AGREE]）：\n\n1. **Proposition 1 证明不完整**——score(a) = nₐ 从 Eq. 3 推导缺关键步骤 [R1-N1, R2 AGREE]\n2. **标题/Abstract overclaim**——10/16 underpowered，\"We show the answer is no\" 逻辑不一致 [R2-N1, R1 AGREE]\n3. **诊断框架 trivial classifier 问题**——60 全阴性条件，框架价值在 failure mode 分类而非预测 [R1-N3, R2 AGREE]\n4. **Corollary 1 近 trivial**——应降级 Remark [R1-W1, R2-W1]\n5. **BR 缺 null model**——需 permutation 分解 base-rate vs. excess bias [R1-W2, R2 AGREE]\n6. **Cross-arch 过度推断**——n=6 不够，\"preliminary evidence\" 而非 \"confirming\" [R1-W3, R2 AGREE]\n7. **α sensitivity = 退化确认**——ceiling effect，非鲁棒性 [R1-W4, R2 AGREE]\n\n## Reviewer Divergence\n\n1. **SCB 新颖性**: R2 认为 SCB 是 CoT confirmation bias 的 FOL 实例化（critical），R1 部分反驳认为 SCB 有独立的 aggregation-level 贡献但同意需更充分对比。→ **部分共识**：需增加对比段落。\n\n2. **Multi-seed 覆盖**: R1 认为 should-fix（Δ ∈ [-4.41, +3.43] 跨正负），R2 REBUT 降级 nice-to-have（现有两模型方向一致）。→ **轻微分歧**。\n\n3. **\"Symbolic Mirage\" 术语**: R2 认为过度品牌化（minor），R1 REBUT 认为有技术对应物。→ **轻微分歧**：R1 建议保留术语但改 section title。\n\n---\n\n## Questions to Authors\n\n**Q1.** Proposition 1 中 score(a) = nₐ 的精确等式如何从 Eq. 3 推导？特别是 42.9% 去重率导致权重不均匀，Σwc 与 nₐ 是等式还是比例关系？如果仅比例关系，argmax 保持是否有证明？\n\n**Q2.** 诊断框架在 trivial \"always predict negative\" baseline 之上的附加值具体体现在哪里？是否可用 §6 cross-arch escape 条件做 positive validation？\n\n**Q3.** TOST ±2pp margin 的先验依据是什么？高基线（SC ≥ 75%）下 2pp 相对效应量仅 ~2.7%，是否考虑按基线调整 margin？\n\n**Q4.** Cross-architecture 实验中 α 是否固定 0.5？跨模型设置下约束不再完全耦合到生成器分布，α 敏感性可能不同。\n\n**Q5.** Table 2 Gemini-2.5-Pro BR=12.19（n_err≈12）远高于其他模型——是 base-rate 效应还是 extraction 异常？\n\n---\n\n## Missing References\n\n**共识引用建议**:\n- Reflexion (Shinn et al., 2023) — self-reflection 范式，§2 简提\n- LATS (Zhou et al., 2023) — tree-search self-verification，§2 简提\n- Cohen's h 或标准化效应量 — 帮助读者理解 ±2pp 在不同基率下的意义\n\n**已确认引用（不再遗漏）**:\n- Kamoi et al. (TACL 2024) — 已引用 kamoi2024selfcorrect\n- AlphaCode/CodeT — 已引用 li2022alphacode, chen2023codet\n- S²R / DuPO — 已引用 zeng2025s2r, dupo2025\n\n---\n\n## External Review\n\n**外部审稿（Stanford Agentic Reviewer）**: 未请求（项目未配置）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: ✅ 完成\n**发现** (0 critical, 4 warning, 19 info):\n\n- ✅ 正文恰好 8 页，符合 EMNLP 2026 页数限制\n- ✅ Limitations 位于正文 conclusion 后、references 前，合规\n- ✅ 主文 7 个 display items（Figure 1-4 + Table 1-3），密度 0.88/页，合理\n- ✅ 所有 figure/table 出现在首次引用附近，无严重漂移\n- ✅ 引用格式统一，无 [?] 未解析\n- ✅ 散点图使用颜色+marker 形状双重编码，色盲友好\n- ⚠️ Figure 4（p7）内部文字过小——打印/缩小后可读性差，建议精简或增大\n- ⚠️ Appendix p16/p22 表格堆叠过密（各含 5 个表格），建议适当分页\n- ⚠️ Appendix pp25-26 连续纯文本无 display item\n\n---\n\n## Overall Assessment\n\n**Overall Score**: 3.0 — Findings\n\n**评分理由**:\n\n论文的实验工作量和方法论严谨性毋庸置疑——6 模型 × 3 域 × 27 变体的系统覆盖、Oracle 对照、multi-seed replication、完备的统计检验，这些在 negative result 研究中极为少见，值得肯定。\n\n但三大贡献均存在实质性问题：\n\n1. **Proposition 1**（理论贡献）——证明有逻辑跳跃，score(a) = nₐ 从 Eq. 3 推导不完整；Corollary 1 近 trivial。\n2. **诊断框架**（实用贡献）——60 条件全阴性使 100% accuracy 等价于 trivial classifier；正例验证缺失。\n3. **SCB 概念**（发现贡献）——与 Wan et al. (2025) CoT confirmation bias 的新颖性区分不充分。\n\n加之标题/Abstract 的全称否定与统计证据（10/16 underpowered）不匹配，论文的 claim 强度系统性地超出了证据支持。\n\n作为 negative result 论文，核心洞察可总结为 \"self-extracted constraints inherit the model's distributional prior\"——这在 Huang et al. (2024) 和 Wan et al. (2025) 之后非 entirely novel。论文的主要价值在于 rigor of systematic confirmation + failure mode taxonomy + practical diagnostics，更适合 Findings track。\n\n**如修复以下关键问题，可提升至 3.5 (Borderline Conference)**:\n- 补全 Proposition 1 证明（或弱化为 argmax preservation）\n- 标题/Abstract 软化，Table 1 区分 powered/underpowered\n- 诊断框架重定位为 failure mode 分类工具 + positive case 验证\n- SCB 与 Wan et al. 增加 1-2 段显式对比\n\n**Confidence**: 4/5（两位 Reviewer 均给出 4/5 confidence，初审评分一致 3.5，交叉分享后关键问题全部达成共识）\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"We show the answer is no\" 过于 categorical——10/16 underpowered 时应为 \"we find no evidence of improvement in powered conditions\"\n- 三个 contributions 列表中，Contribution 2（diagnostics）的 \"correctly classify all 60 tested conditions\" 需加 caveat\n\n### §3 Method\n- Eq. 3 的 scoring function 与 Proposition 1 证明的 score(a) = nₐ 之间需要桥接步骤\n- K_eff（Eq. 1）后应添加直觉解释示例\n- α=0.5 选择依据需补充\n\n### §4 Results\n- Table 1 应在表内标注统计功效或区分 powered/underpowered 条件\n- GSM8K (n=30) / AIME (n=22) 建议移至 Appendix 或标为 exploratory\n\n### §5 Analysis\n- §5.1 Proposition 1：补全 Eq. 3 → score(a) = nₐ 的证明步骤，或改为 argmax preservation\n- §5.1 Corollary 1：降级为 Remark\n- §5.1 BR：补充 base-rate predicted BR 与 observed BR 的分解对比\n- §5.1 关于 Wan et al. (2025) 的区分：增加 1-2 段显式对比\n- §5.3 Diagnostics：\"correctly classify\" → \"correctly characterize the failure mode\"；增加 positive validation\n\n### §6 Cross-Architecture Escape\n- \"Capability-gap pattern\" 基于 n=6，措辞改 \"preliminary evidence\" / \"suggesting\"\n- Spearman ρ=1.0 (n=6) 的鲁棒性问题需讨论\n\n### §7 Discussion\n- Scope 边界声明：实验覆盖限于 SICA paradigm，其他 self-extraction 架构的验证是 future work\n- α sensitivity 重新解释为退化证据\n\n### Appendix\n- Figure 4 内部文字过小\n- pp16/22 表格堆叠过密\n",
    "project": "symb_invariant_consensus",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0",
    "review_chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
  }
}
```

</details>

---


### Tool result

_source line 1797 · 2026-05-23T09:39:21.446328+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_970d5ea3f54df81296b97321fcded892:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4066
}
```

</details>

---


### Assistant

_source line 1798 · 2026-05-23T09:39:35.127076+00:00_

审稿报告已投递给 Research Director。

**Round 17 审稿完成。**

核心结论：**Overall 3.0（Findings）**

两位 Reviewer 初审均给 3.5（Borderline Conference），交叉分享后关键问题全部达成共识。Director 综合评估降至 3.0，原因是论文三大贡献均存在实质性问题：

| 贡献 | 问题 | 共识 |
|------|------|------|
| Proposition 1 理论框架 | 证明逻辑跳跃（Eq.3 → score=nₐ 推导不完整）+ Corollary 1 近 trivial | ✅ 双方一致 |
| 诊断框架 100% accuracy | 60 条件全阴性 → trivial classifier 也 100%，无正例验证 | ✅ 双方一致 |
| SCB 概念新颖性 | 与 Wan et al. (2025) CoT confirmation bias 区分不充分 | ⚠️ 部分共识 |
| 标题/Abstract overclaim | 10/16 underpowered，全称否定证据不足 | ✅ 双方一致 |

**修复路径**: 补全 Prop 1 证明 + 软化标题 + 诊断框架重定位 + SCB 新颖性对比 → 可提升至 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 129

## Round 129

2 recorded events


### User

_source line 1799 · 2026-05-23T09:39:37.737241+00:00_

[Reviewer 2 审稿结果]:
两轮审稿均已提交给 Review Director：

1. **Round 1 独立审稿**（新颖性 + 完整性）：Overall 3.5，识别了 3 个 Must-Fix（标题 overclaim、Markov chain 假设未论证、SCB 与已有 confirmation bias 工作区分不足）和 5 个 Should-Fix。
2. **Round 2 交叉回应**：对 R1 的 3 个 Must-Fix 全部 [AGREE]，5 个 Should-Fix 中 4 个 [AGREE]、1 个 [REBUT]（multi-seed 覆盖率降级为 nice-to-have）。两位 reviewer 在核心问题上高度一致——Proposition 1 证明缺陷、统计功效不足下的 overclaim、诊断框架声称过强。

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

_source line 1800 · 2026-05-23T09:39:54.314202+00:00_

审稿流程全部完成。

**Round 17 (Fresh) 审稿报告已投递至 Research Director。**

**核心结论：Overall 3.0 — Findings**

两位 Reviewer 初审均给出 3.5（Borderline Conference），交叉分享后在所有关键问题上达成共识。Director 综合评估降为 3.0，因为三大贡献均存在实质性问题：

| 贡献 | 问题 | 共识状态 |
|------|------|----------|
| Proposition 1（理论） | 证明 score(a)=nₐ 从 Eq.3 推导不完整；Corollary 1 近 trivial | ✅ 完全共识 |
| 诊断框架（实用） | 60 全阴性条件 → trivial classifier 也 100%；无正例验证 | ✅ 完全共识 |
| SCB 概念（发现） | 与 Wan et al. (2025) CoT confirmation bias 新颖性区分不充分 | ✅ 部分共识 |

**叠加问题**：标题/Abstract 全称否定与统计证据不匹配（10/16 underpowered）。

**修复路径**：补全 Proposition 1 证明（或弱化为 argmax preservation）、标题软化、诊断框架重定位为 failure mode 分类工具、SCB 增加与 Wan et al. 的显式对比 → 可提升至 3.5。

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


## Round 130

## Round 130

58 recorded events


### User

_source line 1801 · 2026-05-23T10:09:04.782595+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: symb_invariant_consensus
- 论文路径: projects/symb_invariant_consensus/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
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

_source line 1802 · 2026-05-23T10:09:10.299572+00:00_

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

_source line 1803 · 2026-05-23T10:09:10.401211+00:00_

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

_source line 1804 · 2026-05-23T10:09:21.794711+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_local_file",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1805 · 2026-05-23T10:09:21.845655+00:00_



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

_source line 1806 · 2026-05-23T10:09:28.347681+00:00_

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

_source line 1807 · 2026-05-23T10:09:28.851201+00:00_

{"result":"# 项目 symb_invariant_consensus 概况\n\n## 实验状态 (173 个)\n\n- **sica_k_sensitivity_14b**: DONE (success) — \n- **exp-011-llama8b**: DONE (failed) — \n- **exp-016-weighted-sc**: DONE (success) — \n- **exp-005**: DONE (negative) — \n- **sica_folio30**: DONE (killed) — \n- **sica_d016_c0_precheck**: DONE (success) — \n- **sica_proofwriter30_v2**: DONE (killed) — \n- **sica_proofwriter30**: DONE (failed) — \n- **sica_aime30_v3**: DONE (killed) — \n- **sica_aime30_v2**: DONE (killed) — \n- **sica_aime30_t07**: DONE (killed) — \n- **mvp_math50_t07**: DONE (killed) — \n- **sica_smoke_5q**: DONE (success) — \n- **smoke-test-5q**: PREPARING (failed) — \n- **crd_folio_main**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp-multi-seed-llama-pw-seed789-v2 | LLaMA-3.1-8B PW seed789 多种子复制（westd-30973 cuda:1 全新运行）。替代 16639 cuda:0 上的慢速运行（12/600）。验证 SCB 在 ProofWriter 上跨 seed 稳定性。 | — | — | — |\n| exp-multi-seed-llama-pw-seed456-v2 | LLaMA-3.1-8B PW seed456 多种子复制（westd-30973 cuda:2 全新运行）。验证 SCB 在 ProofWriter 上跨 seed 稳定性（Δ(SICA-SC)≤0）。配合 seed42/123/789 组成 4-seed 覆盖。 | — | — | — |\n| exp-multi-seed-qwen25-pw-seed789-v3 | Qwen2.5-14B PW seed789 多种子复制（westd-30973 cuda:0 全新运行）。替代 v2 在 16639 cuda:2 上的慢速运行（53/600）。验证 SCB 在 ProofWriter 上跨 seed 稳定性。 | — | — | — |\n\n## 待处理\n- exp-multi-seed-llama-pw-seed456: LLaMA-3.1-8B PW seed456 多种子复制。验证 SCB 在 ProofWriter 上跨 seed 稳定性（Δ(SICA-SC)≤0）。配合 seed42/123/789 组成 4-seed 覆盖。（排队等待 GPU）\n- exp-deberta-ft-combo: Fine-tuned DeBERTa-large on ProofWriter OWA depth-5 achieves near-perfect NLI accuracy (99.67%) and provides massive combo gains over SC baseline when used as external verifier, demonstrating that domain-specific NLI fine-tuning breaks the SCB ceiling by providing truly independent verification signal.（准备中）\n- exp-multi-seed-mistral-folio: Multi-seed replication (seeds 123,456,789) of Mistral-7B × FOLIO-20
…[truncated 1733 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 1808 · 2026-05-23T10:09:28.851667+00:00_

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

_source line 1809 · 2026-05-23T10:09:30.257587+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 1810 · 2026-05-23T10:09:30.812368+00:00_

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

_source line 1811 · 2026-05-23T10:09:31.515292+00:00_

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
40	\title{Beyond Self-Consistency: Self-Extracted Constraints\\Do Not Improve LLM Logical Reasoning}
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
72	\enlargethispage{4\baselineskip}
73	\vspace{-1.5mm}
74	\input{discussion}
75	
76	\vspace{-4mm}
77	\section*{Limitations}
78	\input{limitations_content}
79	
80	\bibliography{ref
…[truncated 71 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 702
}
```

</details>

---


### Tool call

_source line 1812 · 2026-05-23T10:09:31.566045+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_local_file",
  "max_results": "2"
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
    "query": "select:WebSearch,mcp__agent-ml-research__read_local_file",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1813 · 2026-05-23T10:09:31.616682+00:00_



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

_source line 1814 · 2026-05-23T10:09:37.792718+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions"
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
    "query": "EMNLP 2026 ARR call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 1815 · 2026-05-23T10:09:38.796846+00:00_

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
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit anonymity requirements"
  }
}
```

</details>

---


### Tool call

_source line 1816 · 2026-05-23T10:09:40.453958+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper"
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
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1817 · 2026-05-23T10:09:40.506299+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "elapsed_ms": 52
}
```

</details>

---


### Tool result

_source line 1818 · 2026-05-23T10:09:45.727495+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit anonymity requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"Update to Anonymity Policy – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/anonymity/"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"}]

Based on the search results, here are the key submission guidelines for ACL Rolling Review 2026 regarding page limits and anonymity requirements:

## Page Limits

For ACL Rolling Review 2026, the page limit is 8 pages for long papers and 4 pages for short papers, excluding the ethical considerations and limitations sections.

## Anonymity Requirements

Papers must not include authors' names and affiliations. Furt
…[truncated 927 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 6930
}
```

</details>

---


### Tool result

_source line 1819 · 2026-05-23T10:09:47.885982+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the search results, here is information about EMNLP 2026 ARR call for papers submission guidelines:

## Overview
EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

## Important Dates
The ARR submission deadline for long and short papers is May 25, 2026, with a reviewer registration deadline for all authors on May 27, 2026. 
…[truncated 1907 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 10093
}
```

</details>

---


### Tool call

_source line 1820 · 2026-05-23T10:09:56.561074+00:00_

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

_source line 1821 · 2026-05-23T10:09:56.712122+00:00_

1	Can symbolic verification via a provably sound solver improve Large Language Model (LLM) reasoning when constraints are self-extracted from the model's own traces? We find no evidence of improvement. We introduce Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from chain-of-thought traces and selects answers via weighted MAX-SAT. Despite Z3 validating 99\% of self-extracted constraints, SICA produces answers identical to majority voting on over 90\% of problems across six models (7B--32B) and three reasoning domains. No condition shows a significant positive effect after FDR control; four of six powered conditions confirm equivalence within $\pm$2\,pp (TOST), though ten conditions remain underpowered for effects below ${\sim}$2\,pp. We systematically diagnose the failure as \emph{symbolic confirmation bias}: self-extracted constraints track the model's majority answer (bias ratios $1.66$--$4.97\times$ across nine models, 7B to frontier). We identify the structural mechanism---under source-attribution scoring and empirical degeneration, SICA reduces to majority vote (Proposition~1)---and the $M{\to}T{\to}A{\to}C$ Markov chain that bounds self-extracted information (Remark~1), providing independent evidence consistent with the self-correction limitations of \citet{huang2024selfcorrect}. Twenty-seven training-free variants within the constraint-extraction paradigm fail due to a persistent independence-accuracy trade-off. Preliminary cross-architecture verification escapes the bias ($+6.67$\,pp on the weakest generator, $p < 0.001$). Three zero-cost diagnostics characterize failure modes across all 60 tested conditions within this paradigm.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1822 · 2026-05-23T10:09:57.063945+00:00_

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

_source line 1823 · 2026-05-23T10:09:58.017901+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	\looseness=-1
4	Self-Consistency (SC) \citep{wang2023sc} selects the majority answer across $K$ chain-of-thought traces, a strategy grounded in the Condorcet Jury Theorem: independent voters converge to truth \citep{condorcet1785, ladha1992correlated}. In practice, SC's gains plateau for strong models \citep{loo2025reevaluating}, pointing to correlated traces that reduce the effective ensemble size. A natural remedy is to move beyond simple vote-counting: extract logical constraints from the traces and let a provably sound solver adjudicate. If the solver can filter contradictions and enforce logical consistency, it should recover information that raw majority voting discards.
5	
6	\looseness=-1
7	We test this intuition through Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from reasoning traces (prompted as first-order logic; 99\% are propositional at the Z3 level) and selects answers via weighted partial MAX-SAT (\S\ref{sec:pipeline}; Figure~\ref{fig:pipeline}). The result is unequivocal: despite Z3 validating nearly all self-extracted constraints, SICA produces answers identical to majority voting on the vast majority of problems. Across six models (7B--32B), three reasoning domains, and multi-seed replication, no condition shows a significant positive effect after FDR control (Table~\ref{tab:main_results}). Four conditions confirm equivalence within $\pm$2\,pp; ten remain underpowered for effects below ${\sim}$2\,pp.
8	
9	\looseness=-1
10	The failure is not in the solver but in the constraints it operates on. Self-extracted constraints systematically support the model's majority answer, a phenomenon we term \emph{symbolic confirmation bias} (\S\ref{sec:confirmation-bias}). Because each trace determines both an answer and its constraints, the formal channel reduces to a weighted echo of the majority vote. We prove this degeneration is structural (Proposition~1) and show it 
…[truncated 3959 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 1824 · 2026-05-23T10:09:58.018249+00:00_

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

_source line 1825 · 2026-05-23T10:09:58.520305+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{SICA Pipeline}
5	\label{sec:pipeline}
6	\label{sec:condorcet}
7	\label{sec:effective-k}
8	
9	Self-Consistency (SC) \citep{wang2023sc} samples $K$ reasoning traces and selects the majority answer. Under correlated traces (Fleiss' $\kappa$ \citep{fleiss1971kappa}), effective sample size reduces to
10	\begin{equation}
11	\label{eq:effk}
12	K_{\text{eff}} = K \,/\, [1 + (K{-}1) \cdot \kappa]
13	\end{equation}
14	(following \citet{ladha1992correlated}); e.g., $K{=}12$ traces with $\kappa{=}0.69$ yield $K_\text{eff} \approx 1.3$, meaning twelve correlated traces carry no more independent information than 1.3 uncorrelated ones. This motivates constraint-based aggregation.
15	
16	Symbolic Invariant Consensus Aggregation (SICA) extends SC by extracting formal constraints from traces and selecting the answer best supported by the satisfiable subset (Figure~\ref{fig:pipeline}).
17	
18	\paragraph{Trace generation.} Given question $q$, an LLM generates $K$ traces $\{t_1, \ldots, t_K\}$ at temperature $T = 0.7$. Each trace $t_i$ yields answer $a_i$.
19	
20	\looseness=-1
21	\paragraph{Constraint extraction.}\label{sec:constraint-extraction} The same LLM extracts logical constraints from each trace at $T_{\text{ext}} = 0.3$. The extraction prompt requests JSON output with constraint type, expression, and Z3-compatible formula (Appendix~\ref{app:prompts}); in practice, 99.0\% of extracted constraints are propositional at the Z3 level, with only 1.0\% using true quantifiers. The \emph{extraction rate} is the fraction of traces yielding at least one parseable constraint.
22	
23	\paragraph{Deduplication and MAX-SAT.} Constraints are deduplicated by syntactic equivalence (global average deduplication ratio: 46.0\%); each unique constraint $c_m$ receives weight $w_m$ equal to the number of source traces. The objective finds the largest-weight satisfiable subset:
24	\begin{equation}
25	\label{eq:maxsat}
26	\mathcal{C}^* = \arg\max_{
…[truncated 3769 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1826 · 2026-05-23T10:09:58.520677+00:00_

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

_source line 1827 · 2026-05-23T10:09:58.671675+00:00_

1	\section{Results}
2	\label{sec:results}
3	\label{sec:main-results}
4	
5	\looseness=-1 Table~\ref{tab:main_results} reports accuracy across all non-degenerate self-extraction conditions sorted by SC baseline. No condition shows a significant SICA effect after FDR control (BH, $m{=}16$). Two conditions show nominally significant degradation: Mistral-7B on ProofWriter ($-2.83$\,pp, raw $p = 0.014$) and Qwen2.5-14B on ProofWriter ($-2.50$\,pp, raw $p = 0.011$); both reach adjusted $p = 0.112$. An aggregate sign test yields 8 positive and 7 negative $\Delta$ values ($p = 1.00$, two-sided). When SICA and SC disagree, SC selects the correct answer $2.6\times$ more often (139 vs.\ 53 across conditions), indicating that constraint-based reweighting introduces noise rather than corrective signal.
6	
7	\begin{table*}[t]
8	\centering
9	\small
10	\caption{SICA vs.\ SC across all non-degenerate self-extraction conditions (sorted by SC). No condition shows a significant gain after BH correction ($m{=}16$). $\Delta$ = SICA $-$ SC (pp). Symbols: $^b$gold ICL; \textbf{bold}: $p < 0.05$; {*}\,uncorrected $p < 0.05$ (BH adj.\ $p = 0.112$); $^{3s}$\,3-seed; $^{4s}$\,4-seed confirmatory (unmarked: single-seed exploratory). All conditions have McNemar power $< 80\%$ for $|\Delta| = 2$\,pp (Appendix~\ref{app:power}). Degenerate conditions ($C_0 < 5\%$: QwQ-32B AIME $n{=}22$, Qwen2.5-14B GSM8K $n{=}30$; exploratory) yield $\Delta = 0$; oracle upper bounds in Appendix~\ref{app:oracle}.}
11	\label{tab:main_results}
12	\begin{tabular}{@{}llrrrrl@{}}
13	\toprule
14	Model & Domain & $n$ & SC (\%) & SICA (\%) & $\Delta$ (pp) & $p$ \\
15	\midrule
16	\multicolumn{7}{l}{\textit{Type C: error amplification (SC $\leq$ 40\%)}} \\
17	Mistral-7B & PW-D5 & 600 & 39.33 & 36.50 & $\mathbf{-2.83}$ & 0.014{*} \\
18	\midrule
19	\multicolumn{7}{l}{\textit{Intermediate SC (SC $\sim$50--60\%, Mistral-7B only)}} \\
20	Mistral-7B & LogiQA & 200 & 50.00 & 51.50 & $+$1.50 & 0.581 \\
21	Mistral-7B & FOLIO (s123) & 2
…[truncated 3671 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1828 · 2026-05-23T10:09:58.973365+00:00_

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

_source line 1829 · 2026-05-23T10:09:59.325162+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\looseness=-1
5	\paragraph{Self-consistency and ensemble theory.}
6	Self-consistency (SC) selects the most frequent answer across chain-of-thought traces \citep{wang2023sc}. Extensions address free-form generation \citep{chen2024usc}, confidence weighting \citep{taubenfeld2025cisc}, diverse prompting \citep{li2023diverse}, and reasoning-aware filtering \citep{wan2024rasc, toh2024notallvotes, kim2026reasc}. SC gains plateau early \citep{loo2025reevaluating, byerly2026selfconsistency}. The Condorcet Jury Theorem \citep{condorcet1785} guarantees majority-vote convergence under independence; \citet{ladha1992correlated} show correlated voters reduce effective ensemble size. Our $K_\text{eff}$ adapts Fleiss' $\kappa$ from ensemble diversity theory \citep{kuncheva2003measures, brown2005diversity} to quantify this compression (\S\ref{sec:pipeline}). \citet{kim2025correlated} demonstrate correlated errors in LLM outputs; \citet{kuai2026independent} propose cross-model independence auditing, complementary to our within-model process-$\kappa$.
7	
8	\looseness=-1
9	\paragraph{Neuro-symbolic reasoning.}
10	We distinguish three paradigms: \emph{specification-generation} \citep{pan2023logiclm, olausson2023linc, ye2024satlm} translates problems into formal specifications before answering; \emph{program-generation} \citep{gao2023pal, chen2023program, lyu2023faithful} produces executable code; both formalize \emph{before} answer generation. \emph{Trace-extraction} (this work) operates post-hoc, inheriting confirmation bias (\S\ref{sec:confirmation-bias}). Recent extensions expand these paradigms with symbolic planning, logic agents, and verified reasoning \citep{ryu2025clover, xu2026dylos, li2025aristotle, wang2025fover, singh2026verge, luo2025logicagent, miya2025eidoku}; \citet{amonkar2025realitycheck} show formalization quality degrades with problem complexity; \citet{chan2026position} argue logical soundness alone is unrelia
…[truncated 3435 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1830 · 2026-05-23T10:09:59.325677+00:00_

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

_source line 1831 · 2026-05-23T10:09:59.377030+00:00_

1	\section{The Symbolic Mirage}
2	\label{sec:analysis}
3	
4	\subsection{Symbolic Confirmation Bias}
5	\label{sec:confirmation-bias}
6	
7	\looseness=-1 Self-extracted constraints systematically align with the model's majority answer. On Mistral-7B FOLIO, when SICA errs, 83.3\% of constraints support the incorrect answer---bias ratio $4.97\times$ (Table~\ref{tab:cross-model-bias})---and 94\% of errors overlap with SC. Z3 rejects only 3.4\% of constraints, and MAX-SAT produces answers identical to count-only aggregation on 94.4\% of problems (Table~\ref{tab:ablation}), confirming that the formal verification layer is vacuous (Eq.~\ref{eq:degenerate}): 99\% of constraints pass Z3 validation yet add no information beyond majority voting. The $\alpha$-insensitivity confirms degeneration: under $|\mathcal{C}^{\setminus}| \approx 0$ the penalty term vanishes and $\alpha$ becomes irrelevant, producing $\geq$99\% agreement across $\alpha \in \{0.1, \ldots, 0.9\}$ as a ceiling effect (Table~\ref{tab:alpha-ablation}).
8	
9	\looseness=-1 Empirically, confirmation bias extends beyond incorrect instances. On problems where SC selects the correct answer, constraints still disproportionately support the majority ($\text{BR}_\text{correct}$ $1.29$--$3.64\times$ across all six tested conditions, with 5/6 showing $\text{BR}_\text{correct} \geq \text{BR}_\text{wrong}$), confirming that self-extracted constraints track distributional frequency rather than logical validity. A permutation null model---randomizing constraint--answer associations while preserving per-trace counts (1{,}000 permutations)---yields $\text{BR}_\text{null} \approx \text{BR}_\text{obs}$ across all tested conditions ($p > 0.7$), confirming that observed BR is fully explained by the trace-count base rate. The bias is structural precisely because it is inherent to the majority-vote geometry (Proposition~1), not an artifact of extraction.
10	
11	\looseness=-1 The pattern generalizes: $4.97\times$ (Mistral), $3.85\times
…[truncated 12286 chars]

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

_source line 1832 · 2026-05-23T10:10:04.298282+00:00_

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

_source line 1833 · 2026-05-23T10:10:04.803607+00:00_

1	\section{Escaping the Bottleneck}
2	\label{sec:solutions}
3	\label{sec:cross-arch}
4	
5	\paragraph{Motivation.}
6	\looseness=-1 No training-free self-extraction method achieves independence from the model's distributional prior (\S\ref{sec:remediation}). Remark~1 implies that any escape must break the self-extraction dependency: the information ceiling $I(C;Y) \leq I(T;Y)$ binds whenever constraints are deterministic functions of the generating model's traces. We test whether a structurally independent verifier, sharing neither architecture nor training data with the generator, provides corrective signal that escapes this bound.
7	
8	\paragraph{Method.}
9	\looseness=-1 We use DeBERTa-large \citep{he2021deberta} (406M, encoder-only), fine-tuned on MultiNLI \citep{williams2018mnli}, to classify (premise, conclusion) pairs as entailment, contradiction, or neutral. In combo mode, each NLI-supporting vote counts $w$ times alongside SC's $K$ votes. We evaluate on Mistral-7B FOLIO ($n = 204$) and ProofWriter depth-5 ($n = 600$).
10	
11	\paragraph{Zero-shot results.}
12	\looseness=-1 DeBERTa NLI alone achieves 49.51\% on FOLIO and 55.00\% on ProofWriter. Combo $w{=}3$ yields $+6.67$\,pp on ProofWriter for Mistral-7B ($p < 0.001$, significant after BH correction) and $+2.94$\,pp on FOLIO (n.s.); all generators with SC $\geq 72\%$ show no significant improvement ($\Delta \leq +0.83$\,pp). Same-model SICA \emph{degrades} ProofWriter ($-2.83$\,pp; Table~\ref{tab:main_results}), illustrating that corrective signal must originate outside the model's distribution.
13	
14	\paragraph{Capability gap.}
15	\looseness=-1 Four generators spanning a 47-point SC range on ProofWriter ($n{=}600$), all paired with DeBERTa-large-mnli (55.00\% standalone; Table~\ref{tab:cross_generator_nli}): only Mistral-7B (SC 39.33\%, below the verifier) gains significantly ($+6.67$\,pp, $p < 0.001$); all three above the verifier show no significant improvement ($\Delta \leq +0.83$\,pp). These results poin
…[truncated 1987 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 505
}
```

</details>

---


### Tool call

_source line 1834 · 2026-05-23T10:10:04.855746+00:00_

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

_source line 1835 · 2026-05-23T10:10:05.309083+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	\label{sec:conclusion}
4	
5	\looseness=-1
6	Our central finding is that the value of formal verification depends on the \emph{independence} of its inputs, not the soundness of its logic. Three diagnostics ($K_\text{eff}$, BR, $C_0$) operationalize this principle and correctly characterize failure modes across all 60 tested conditions within the self-extraction paradigm, with decision boundaries generalizing prospectively to held-out model families (\S\ref{sec:diagnostic-framework}). The theoretical bounds (Proposition~1, Remark~1) apply to any deterministic self-extraction pipeline by construction; empirical validation covers 27 training-free variants within the SICA paradigm.
7	
8	\looseness=-1
9	This independence principle has direct consequences for test-time compute scaling \citep{snell2025scaling}: with $K_\text{eff} \leq 3.62$ for $K{=}12$, same-model traces scale redundancy, not information. The principle applies to any self-verification method that draws on the generating model's own distribution, providing independent evidence consistent with \citet{huang2024selfcorrect}. Escaping the bottleneck requires structural independence, capability ordering, and task-verifier alignment (\S\ref{sec:cross-arch}); whether trained extractors can shift this boundary remains open. The diagnostics we provide enable future work to recognize this limitation upfront.
10	

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

_source line 1836 · 2026-05-23T10:10:05.309561+00:00_

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

_source line 1837 · 2026-05-23T10:10:05.666909+00:00_

1	\looseness=-1 Open-source models range from 7B to 32B; frontier models confirm SCB universality via cross-model extraction. All datasets are English-language logical reasoning benchmarks; we do not evaluate trained extractors or multilingual settings. Statistical power is limited for effects below ${\sim}$2\,pp; the capability-gap analysis rests on $n{=}6$ conditions (Appendix~\ref{app:limitations-extended}).
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 357
}
```

</details>

---


### Tool call

_source line 1838 · 2026-05-23T10:10:05.667350+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1839 · 2026-05-23T10:10:05.918626+00:00_

File content (30701 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1840 · 2026-05-23T10:10:26.269402+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "paper_checklist.yaml",
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
    "file": "paper_checklist.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1841 · 2026-05-23T10:10:26.721795+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'symb_invariant_consensus'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1842 · 2026-05-23T10:10:27.224216+00:00_

called mcp__agent-ml-research__read_local_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_local_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file_path": "projects/symb_invariant_consensus/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_local_file",
  "tool_args": {
    "project": "symb_invariant_consensus",
    "file_path": "projects/symb_invariant_consensus/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1843 · 2026-05-23T10:10:27.224575+00:00_

&lt;tool_use_error>Error: No such tool available: mcp__agent-ml-research__read_local_file&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_local_file",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1844 · 2026-05-23T10:10:28.680259+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1845 · 2026-05-23T10:10:28.730953+00:00_

1	\section{Prompt Templates}
2	\label{app:prompts}
3	
4	SICA uses domain-specific prompt templates for constraint extraction: one for mathematical reasoning (GSM8K, AIME) and one for logical reasoning (ProofWriter, FOLIO). Both share the same system prompt. The LLM is called with temperature $T{=}0.3$, max tokens $1024$, and structured JSON output mode. Up to 6 traces are processed in parallel via thread pooling, with 2 retries on failure (exponential backoff, base 0.5s).
5	
6	\paragraph{System Prompt.}
7	
8	\begin{lstlisting}
9	You are a constraint extraction tool. Output ONLY
10	valid JSON. Do NOT solve problems, reason about
11	correctness, or think step-by-step. Extract
12	constraints from the given trace exactly as stated.
13	\end{lstlisting}
14	
15	\paragraph{Mathematical Constraint Extraction (EXTRACTION\_PROMPT).}
16	
17	Used for GSM8K and AIME datasets. The placeholder \texttt{\{trace\}} is replaced with the reasoning trace at runtime.
18	
19	\begin{lstlisting}
20	Extract mathematical constraints from this reasoning
21	trace as a JSON object.
22	
23	Rules:
24	- type: "equation", "inequality", or "predicate"
25	- expression: human-readable, e.g. "x + y == 14"
26	- z3_formula: a single comparison expression in
27	  Python Z3 syntax
28	- source_step: step number where the constraint
29	  appears
30	- Use variable names from the trace
31	
32	z3_formula MUST follow these rules:
33	- Allowed operators: ==, !=, <, >, <=, >=, +, -, *,
34	  /, **, %
35	- Use individual named variables: a1, a2, a3...
36	  NOT arrays a[1] or sets A
37	- Expand all sums explicitly:
38	  "a1 + a2 + a3 == 55" NOT "sum([a1,a2,a3])"
39	- NO Python builtins: sum(), len(), max(), min(),
40	  list(), set(), range(), int()
41	- Each z3_formula must be exactly ONE comparison
42	  (==, !=, <, >, <=, >=)
43	- For multiple values, write separate constraints
44	  for each
45	
46	Output ONLY the JSON below, nothing else:
47	{"constraints": [{"type": "equation",
48	  "expression": "x + y == 14",
49	 
…[truncated 944 chars]

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

_source line 1846 · 2026-05-23T10:10:50.154756+00:00_

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

_source line 1847 · 2026-05-23T10:10:50.657531+00:00_

1	
2	# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)
3	- id: "R1-C1"
4	  summary: "Method Stage 3 sat() implementation undescribed"
5	  category: method
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 1
9	  last_seen_round: 3
10	  resolution: "Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit."
11	  resolution_round: 3
12	
13	- id: "R1-C2"
14	  summary: "Most experiments underpowered (n≤60), no power analysis"
15	  category: experiment
16	  severity: critical
17	  status: resolved
18	  first_raised_round: 1
19	  last_seen_round: 1
20	  resolution: "Power analysis + Bootstrap CIs added. Larger n conditions (200-600)."
21	  resolution_round: 3
22	
23	- id: "R1-C3"
24	  summary: "Oracle/upper-bound experiment missing"
25	  category: experiment
26	  severity: critical
27	  status: resolved
28	  first_raised_round: 1
29	  last_seen_round: 1
30	  resolution: "Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp."
31	  resolution_round: 3
32	
33	- id: "R1-C4"
34	  summary: "Huang et al. (ICLR 2024) not cited"
35	  category: framing
36	  severity: critical
37	  status: resolved
38	  first_raised_round: 1
39	  last_seen_round: 2
40	  resolution: "Huang, Stechly, Kambhampati all cited and discussed."
41	  resolution_round: 2
42	
43	- id: "R1-C5"
44	  summary: "Critical related work missing"
45	  category: writing
46	  severity: critical
47	  status: resolved
48	  first_raised_round: 1
49	  last_seen_round: 1
50	  resolution: "~48 citations, 5 Related Work paragraphs."
51	  resolution_round: 3
52	
53	- id: "R1-C9"
54	  summary: "Capability trap novelty unclear"
55	  category: framing
56	  severity: critical
57	  status: resolved
58	  first_raised_round: 1
59	  last_seen_round: 3
60	  resolution: "Reframed as regime-dependent analysis with CJT framework."
61	  resolution_round: 3
62	
63	- id: "R3-N1"
64	  summary: "σ(c,a) scoring inconsistent between self-extraction and oracle"
65	  category: method
66	  severity: criti
…[truncated 27371 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1848 · 2026-05-23T10:10:50.908913+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "output_mode": "content",
  "glob": "*.yaml"
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
    "glob": "*.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1849 · 2026-05-23T10:10:50.959506+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1850 · 2026-05-23T10:11:17.545242+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/submitted.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts"
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
    "pattern": "**/submitted.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 1851 · 2026-05-23T10:11:17.595888+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_10/submitted.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_11/submitted.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_12/submitted.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_13/submitted.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_14/submitted.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_15/submitted.pdf

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

_source line 1852 · 2026-05-23T10:11:30.852225+00:00_

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

_source line 1853 · 2026-05-23T10:11:53.401214+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 22548
}
```

</details>

---


### Tool call

_source line 1854 · 2026-05-23T10:11:53.703039+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查**方法严谨性和实验设计**。\n\n## 论文信息\n- **标题**: Beyond Self-Consistency: Self-Extracted Constraints Do Not Improve LLM Logical Reasoning\n- **论文源码**: `projects/symb_invariant_consensus/docs/paper/main.tex`（及同目录下的 abstract.tex, introduction.tex, method.tex, experiments.tex, analysis.tex, solutions.tex, discussion.tex, limitations_content.tex, related_work.tex, appendix.tex）\n- **PDF**: `projects/symb_invariant_consensus/artifacts/review_round_15/submitted.pdf`\n\n## Venue 要求（EMNLP 2026 via ARR）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（严格），参考文献无限，Limitations/Ethics 不计入\n- **模板**: ACL template（`\\usepackage[review]{acl}`）\n- **匿名**: Double-blind，作者列 Anonymous\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**核心关注**:\n1. **Proposition 1 (Argmax Preservation) 的理论严谨性**: 证明是否完整？假设是否合理且充分？从 Eq.(3) 到 score(a) ∝ n_a 的推导是否有逻辑跳跃？\"approximately uniform constraint yield\" 假设的合理性？\n2. **Remark 1 (Information Ceiling) 的贡献度**: DPI bound 是否 trivial？Markov chain 结构的识别是否有实质贡献？\n3. **统计方法论**: McNemar test + BH correction 是否合适？TOST ±2pp margin 的选择依据是否充分？10/16 conditions underpowered 如何影响 claims？Bootstrap CIs 的使用是否正确？\n4. **BR (Bias Ratio) 指标**: 是否存在循环论证？56.4% 零变量重叠下 BR>1 是否 by construction？Permutation null model 是否充分排除了 base-rate confound？\n5. **实验设计**: 6 个模型 × 3 数据集的覆盖度是否足够？Multi-seed replication 的样本量和结论强度是否匹配？Oracle control 的设计是否sound？\n6. **Cross-architecture escape (§6)**: n=6 条件下 Spearman ρ=1.0 的可信度？Capability gap 结论是否 overclaimed？\n7. **α=0.5 敏感性**: ≥99% agreement 是退化证据还是鲁棒性证据？解释是否正确？\n\n**输出格式**: 按 Summary → Strengths → Weaknesses (按严重性排序: Must-Fix / Should-Fix / Nice-to-Have) → Questions → Missing References → Overall Assessment (含评分和置信度) 组织。每个 weakness 标注严重性 [critical/major/minor]。",
  "project": "symb_invariant_consensus",
  "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
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
    "text": "你是 Reviewer 1，负责审查**方法严谨性和实验设计**。\n\n## 论文信息\n- **标题**: Beyond Self-Consistency: Self-Extracted Constraints Do Not Improve LLM Logical Reasoning\n- **论文源码**: `projects/symb_invariant_consensus/docs/paper/main.tex`（及同目录下的 abstract.tex, introduction.tex, method.tex, experiments.tex, analysis.tex, solutions.tex, discussion.tex, limitations_content.tex, related_work.tex, appendix.tex）\n- **PDF**: `projects/symb_invariant_consensus/artifacts/review_round_15/submitted.pdf`\n\n## Venue 要求（EMNLP 2026 via ARR）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（严格），参考文献无限，Limitations/Ethics 不计入\n- **模板**: ACL template（`\\usepackage[review]{acl}`）\n- **匿名**: Double-blind，作者列 Anonymous\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**核心关注**:\n1. **Proposition 1 (Argmax Preservation) 的理论严谨性**: 证明是否完整？假设是否合理且充分？从 Eq.(3) 到 score(a) ∝ n_a 的推导是否有逻辑跳跃？\"approximately uniform constraint yield\" 假设的合理性？\n2. **Remark 1 (Information Ceiling) 的贡献度**: DPI bound 是否 trivial？Markov chain 结构的识别是否有实质贡献？\n3. **统计方法论**: McNemar test + BH correction 是否合适？TOST ±2pp margin 的选择依据是否充分？10/16 conditions underpowered 如何影响 claims？Bootstrap CIs 的使用是否正确？\n4. **BR (Bias Ratio) 指标**: 是否存在循环论证？56.4% 零变量重叠下 BR>1 是否 by construction？Permutation null model 是否充分排除了 base-rate confound？\n5. **实验设计**: 6 个模型 × 3 数据集的覆盖度是否足够？Multi-seed replication 的样本量和结论强度是否匹配？Oracle control 的设计是否sound？\n6. **Cross-architecture escape (§6)**: n=6 条件下 Spearman ρ=1.0 的可信度？Capability gap 结论是否 overclaimed？\n7. **α=0.5 敏感性**: ≥99% agreement 是退化证据还是鲁棒性证据？解释是否正确？\n\n**输出格式**: 按 Summary → Strengths → Weaknesses (按严重性排序: Must-Fix / Should-Fix / Nice-to-Have) → Questions → Missing References → Overall Assessment (含评分和置信度) 组织。每个 weakness 标注严重性 [critical/major/minor]。",
    "project": "symb_invariant_consensus",
    "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
  }
}
```

</details>

---


### Tool result

_source line 1855 · 2026-05-23T10:12:11.378230+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17675
}
```

</details>

---


### Tool call

_source line 1856 · 2026-05-23T10:12:11.529420+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查**新颖性、完整性和写作质量**。\n\n## 论文信息\n- **标题**: Beyond Self-Consistency: Self-Extracted Constraints Do Not Improve LLM Logical Reasoning\n- **论文源码**: `projects/symb_invariant_consensus/docs/paper/main.tex`（及同目录下的 abstract.tex, introduction.tex, method.tex, experiments.tex, analysis.tex, solutions.tex, discussion.tex, limitations_content.tex, related_work.tex, appendix.tex）\n- **PDF**: `projects/symb_invariant_consensus/artifacts/review_round_15/submitted.pdf`\n\n## Venue 要求（EMNLP 2026 via ARR）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（严格），参考文献无限，Limitations/Ethics 不计入\n- **模板**: ACL template（`\\usepackage[review]{acl}`）\n- **匿名**: Double-blind，作者列 Anonymous\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**核心关注**:\n1. **SCB (Symbolic Confirmation Bias) 概念新颖性**: 与 Huang et al. (2024) self-correction limitation、Wan et al. (2025) CoT confirmation bias 的关系？是已知现象在 FOL 载体上的实例化，还是有独立的理论/实证贡献？论文是否清晰建立了 distinction？\n2. **Contributions 定位**: 三个 contribution（symbolic mirage, diagnostic framework, cross-architecture escape）的力度是否足够 EMNLP main conference？是否存在 scope 震荡（SICA-specific claims 与 general claims 反复切换）？\n3. **Related Work 覆盖度**: 是否有重要遗漏？Neuro-symbolic reasoning 分类（specification-generation / program-generation / trace-extraction）是否准确完整？Self-verification 文献是否充分覆盖？是否漏引了 Reflexion (Shinn 2023)、LATS (Zhou 2023) 等重要工作？\n4. **写作质量**: Abstract 信息密度是否过高？符号/指标过载（K_eff, BR, C_0, κ 等）？K_eff 缺少直觉解释？\"Symbolic Mirage\" 作为 Section 标题是否过于 dramatic？\n5. **标题与 claims 的匹配**: \"Do Not Improve\" 在 10/16 conditions underpowered 下是否 overclaiming？\"LLM Reasoning\" vs 仅覆盖逻辑推理域？\n6. **格式合规**: 正文是否严格 ≤8 页？Limitations section 是否在正文且仅一处？匿名规范是否遵守？ACL template 使用是否正确？\n7. **27 training-free variants**: scope boundary 是否清楚？是否明确声明未尝试 trained constraint extractor？\n\n**输出格式**: 按 Summary → Strengths → Weaknesses (按严重性排序: Must-Fix / Should-Fix / Nice-to-Have) → Questions → Missing References → Overall Assessment (含评分和置信度) 组织。每个 weakness 标注严重性 [critical/major/minor]。",
  "project": "symb_invariant_consensus",
  "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
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
    "text": "你是 Reviewer 2，负责审查**新颖性、完整性和写作质量**。\n\n## 论文信息\n- **标题**: Beyond Self-Consistency: Self-Extracted Constraints Do Not Improve LLM Logical Reasoning\n- **论文源码**: `projects/symb_invariant_consensus/docs/paper/main.tex`（及同目录下的 abstract.tex, introduction.tex, method.tex, experiments.tex, analysis.tex, solutions.tex, discussion.tex, limitations_content.tex, related_work.tex, appendix.tex）\n- **PDF**: `projects/symb_invariant_consensus/artifacts/review_round_15/submitted.pdf`\n\n## Venue 要求（EMNLP 2026 via ARR）\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页（严格），参考文献无限，Limitations/Ethics 不计入\n- **模板**: ACL template（`\\usepackage[review]{acl}`）\n- **匿名**: Double-blind，作者列 Anonymous\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**核心关注**:\n1. **SCB (Symbolic Confirmation Bias) 概念新颖性**: 与 Huang et al. (2024) self-correction limitation、Wan et al. (2025) CoT confirmation bias 的关系？是已知现象在 FOL 载体上的实例化，还是有独立的理论/实证贡献？论文是否清晰建立了 distinction？\n2. **Contributions 定位**: 三个 contribution（symbolic mirage, diagnostic framework, cross-architecture escape）的力度是否足够 EMNLP main conference？是否存在 scope 震荡（SICA-specific claims 与 general claims 反复切换）？\n3. **Related Work 覆盖度**: 是否有重要遗漏？Neuro-symbolic reasoning 分类（specification-generation / program-generation / trace-extraction）是否准确完整？Self-verification 文献是否充分覆盖？是否漏引了 Reflexion (Shinn 2023)、LATS (Zhou 2023) 等重要工作？\n4. **写作质量**: Abstract 信息密度是否过高？符号/指标过载（K_eff, BR, C_0, κ 等）？K_eff 缺少直觉解释？\"Symbolic Mirage\" 作为 Section 标题是否过于 dramatic？\n5. **标题与 claims 的匹配**: \"Do Not Improve\" 在 10/16 conditions underpowered 下是否 overclaiming？\"LLM Reasoning\" vs 仅覆盖逻辑推理域？\n6. **格式合规**: 正文是否严格 ≤8 页？Limitations section 是否在正文且仅一处？匿名规范是否遵守？ACL template 使用是否正确？\n7. **27 training-free variants**: scope boundary 是否清楚？是否明确声明未尝试 trained constraint extractor？\n\n**输出格式**: 按 Summary → Strengths → Weaknesses (按严重性排序: Must-Fix / Should-Fix / Nice-to-Have) → Questions → Missing References → Overall Assessment (含评分和置信度) 组织。每个 weakness 标注严重性 [critical/major/minor]。",
    "project": "symb_invariant_consensus",
    "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
  }
}
```

</details>

---


### Tool result

_source line 1857 · 2026-05-23T10:12:12.900058+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1370
}
```

</details>

---


### Assistant

_source line 1858 · 2026-05-23T10:12:15.708220+00:00_

视觉审查已派发，Reviewer 1 和 Reviewer 2 已同时启动。等待两位 Reviewer 返回初审结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 131

## Round 131

2 recorded events


### User

_source line 1859 · 2026-05-23T10:19:02.196965+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告：方法严谨性与实验设计

**论文**: Beyond Self-Consistency: Self-Extracted Constraints Do Not Improve LLM Logical Reasoning
**Venue**: EMNLP 2026 via ARR

---

## 总体评分

**Overall Assessment**: 3.5 / 5 (Borderline Conference)
**Confidence**: 4 / 5 (Fairly confident)
**一句话总结**: 实证工作扎实全面，但理论贡献偏薄且部分核心 claim 相对于统计检验力度存在 overclaiming 风险。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验方法论总体规范（McNemar+BH、TOST、bootstrap CI），但 Proposition 1 形式化不够严谨（大量使用 ≈），Remark 1 的 DPI bound 接近 trivial，BR 指标存在 by-construction 的循环性问题 |
| Excitement | 3.0/5 | negative result 本身有价值，"symbolic confirmation bias" 的诊断框架有实用性，但理论新颖度有限；cross-architecture escape (§6) 是建设性贡献但证据链过短 (n=6) |
| Reproducibility | 4.0/5 | 提供了完整的 prompt templates (Appendix A)、pseudocode (Appendix B)、超参数设定 (§3.2)，数据集均为公开 benchmark |
| Clarity | 3.5/5 | 主文结构清晰，但信息密度极高（26 页），部分关键论证散落在多个 appendix 中不易追踪 |

---

## Summary

本文提出 Symbolic Invariant Consensus Aggregation (SICA)，从 LLM 推理 trace 中提取逻辑约束并通过 MAX-SAT 选择最佳答案。核心发现是负面的：自提取约束因 "symbolic confirmation bias" 系统性地对齐模型多数票答案，使 SICA 退化为多数投票。论文通过 Proposition 1（Argmax Preservation）和 Remark 1（Information Ceiling）给出理论解释，在 6 个模型 × 3 个数据集上验证，测试 27 种 training-free 修复策略均失败，并展示 cross-architecture verification 作为 escape path。工作量巨大，实验覆盖面广。

---

## 主要优势 (Strengths)

**S1. 实验覆盖度和系统性极高。** 6 个开源模型 (7B–32B) + 5 个 frontier 模型的 cross-model extraction，3 个核心数据集 + 3 个辅助数据集，27 种修复策略的系统排除，multi-seed replication (3-seed/4-seed)，oracle control 验证 MAX-SAT 机制本身的 soundness (+29.90pp on FOLIO)。这种覆盖度在 negative-result 论文中极为罕见。

**S2. 统计方法论总体规范。** McNemar exact test 用于 paired binary outcomes 是正确选择；BH correction 处理 m=16 multiple testing；TOST equivalence test 带 ±1/±2/±3pp 三个 margin 的 sensitivity analysis；bootstrap CI (10,000 resamples)。论文坦诚承认 10/16 conditions underpowered for |Δ|=2pp，并明确指出 "Absence of evidence is not evidence of absence for small effects" (§4)。

**S3. 诊断框架有实用价值。** 三个 zero-cost diagnostics (C₀, K_eff, BR) 在全部 60 个测试条件上正确表征了失败模式，并在两个 held-out model families (LLaMA-3.1-8B, Qwen3-14B) 上前瞻性验证。这是可直接被从业者采用的工具。

**S4. Oracle control 设计精良。** 用 gold logical annotations 替代自提取约束 (FOLIO +29.90pp, ProofWriter +17.17pp)，干净地分离了 "MAX-SAT 机制是否 sound" 和 "自提取约束是否有效" 两个问题。

**S5. Permutation null model 验证 BR。** 1000 次 permutation 得到 BR_null ≈ BR_obs (p > 0.7)，证实观察到的 bias ratio 完全可由 trace-count base rate 解释——这实际上 *加强* 了论文的核心论点（bias 是结构性的而非提取质量问题）。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **Proposition 1 的形式化不够严谨，更像是 empirical observation 而非 theorem**
- 具体位置：§5.1, Proposition 1 及其证明
- 问题：三个假设中，(i) 使用 |C^∖| ≈ 0 而非精确条件，(iii) "approximately uniform constraint yield" 从未给出数学定义（什么程度算 "approximately"？方差阈值是多少？），证明中全程使用 ≈ 而非 =。结论 "SICA reduces to majority vote" 也只通过末尾的 >90% 经验一致性来支撑，而非从假设严格推出。假设 (iii) 也未直接验证——论文给出了 extraction rate（每个 trace 是否产生约束）但未展示每个 trace 的约束数量分布。
- 为什么影响接收：Proposition 1 是论文的理论核心支柱之一，支撑 "SICA degenerates to majority voting" 这个中心论点。如果它只是一个经验观察而非严格命题，论文的理论贡献将显著降低。
- 建议修改方向：(a) 给假设 (iii) 一个精确的数学表述（如 "constraint yield per trace 的变异系数 CV < δ"），并用数据直接验证；(b) 给出 degeneration 的精确条件（如 |C^∖|/|C| < ε），推导 score(a) 与 n_a 之间的近似误差上界，使 "approximately" 变为可量化的。或者，诚实地降格为 "Empirical Observation" 而非 "Proposition"。

**N2** [critical] **标题/中心 claim 与统计检验力不匹配**
- 具体位置：标题 "Do Not Improve"；§4 Table 1；Appendix D (power analysis)
- 问题：标题断言 "Self-Extracted Constraints Do Not Improve LLM Logical Reasoning"，但 10/16 conditions 的 McNemar power 对于 |Δ|=2pp 效应不足 80%，MDE 达 1.86–4.84pp。论文自己也承认 "Absence of evidence is not evidence of absence for small effects"（§4），但标题和 abstract 的措辞并未反映这一限定。这构成了 overclaiming：论文实际上证明的是 "没有证据表明自提取约束带来 ≥2pp 的改善"，而非 "自提取约束不改善推理"。
- 为什么影响接收：标题是论文最重要的 claim statement。如果它与实际证据强度不匹配，会误导读者和引用者。
- 建议修改方向：标题改为更精确的表述，如 "Self-Extracted Constraints Provide No Detectable Improvement to LLM Logical Reasoning" 或在 abstract 中加入效应大小限定语（"no improvement exceeding ~2 percentage points"）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] **Remark 1 (Information Ceiling) 的理论贡献接近 trivial**
- 具体位置：§5.1, Remark 1; Figure 3
- 问题：C = f(T) 是确定性函数，Y — T — C 构成 Markov chain 是 DPI 的直接应用，对任何确定性后处理都成立。论文承认 "The contribution is the identification of the M→T→A→C Markov chain structure"，但 C 作为 T 的确定性函数这一观察本身并不深刻。更有趣的 claim 是 Figure 3 中的 C ⊥ Y | A（约束在给定答案后不携带关于真值的额外信息），但这个更强的条件独立性声明并未被形式化证明——它依赖于经验观察（BR 数据、degeneration 数据）而非因果推断论证。
- 建议：如果保留 Remark 1，应明确区分 trivial 的 DPI bound 和 non-trivial 的 C ⊥ Y | A claim。后者需要更严格的论证（例如，在什么条件下 T → A → C 的信息瓶颈使得 C 对 Y 的信息完全经由 A 传递？）。

**W2** [major] **BR 指标的 "by construction" 循环性未充分讨论**
- 具体位置：§3.1 Eq.(5); §5.1
- 问题：BR = P(c supports a_M | a_M ≠ a*) / P(c supports a* | a_M ≠ a*)。在 source-attribution scoring (σ(c,a) = 1 iff c 来自产生 a 的 trace) 下，如果多数 trace 产生 a_M，则多数约束自然 support a_M，BR > 1 几乎是 tautological。论文在 Proposition 1 之后确实承认 "BR ≥ 1 follows from the trace-count geometry"，permutation test 也确认 BR_null ≈ BR_obs。但这恰恰说明 BR 作为一个诊断指标，在 source-attribution 设定下几乎无法区分 "约束真的有偏" 和 "约束只是数量上反映了 trace 分布"。56.4% 零变量重叠进一步说明约束根本无法跨答案提供判别信号——这更像是一个 pipeline 设计问题而非 LLM 的固有偏差。
- 建议：(a) 在定义 BR 时就明确说明其 lower bound 为 1 是 by construction 的，将其解释从 "measuring bias" 转为 "measuring the degree of structural coupling beyond base-rate effects"；(b) 报告 BR_excess = BR_obs - BR_null 作为更纯净的指标；(c) 对 43.6% 有变量重叠的子集单独分析 BR，看是否存在有效判别信号。

**W3** [major] **Cross-architecture escape (§6) 的 Spearman ρ=1.0, n=6 证据过弱**
- 具体位置：§6, "Spearman ρ = 1.0, p = 0.003, n = 6"; Table 3; Figure 8
- 问题：n=6 个数据点的 perfect monotonic relationship 极为脆弱。(a) 4 个 generator × 1 个 verifier 的 Table 3 只有 4 个点，其中 3 个 generator 的 Δ 在 +0.50 到 +0.83pp 之间几乎无差异，monotonicity 由 Mistral-7B 这一个 outlier 驱动；(b) Figure 8 的 n=6 来自异质条件（不同 verifier 架构 × 不同 generator），将它们混入同一相关分析假设了底层关系的同质性。基于如此小的样本，"suggesting a structural property of independent verification rather than an architecture artifact" 这一 claim 过强。
- 建议：(a) 明确标注这是 preliminary/exploratory evidence，不是 confirmed structural property；(b) 在 ProofWriter 之外的数据集上验证 capability-gap pattern（目前只有 PW-D5 的数据）；(c) 至少讨论 n=6 下 Type I error 风险和效应不稳定性。

**W4** [moderate] **TOST ±2pp margin 的选择依据不够充分**
- 具体位置：§4, "adopted as effects below one percentage point per class provide negligible practical benefit on datasets with ≥3 answer categories"
- 问题：±2pp 作为 equivalence margin 的理由是 "每类不到 1pp 的效应在 ≥3 类数据集上可忽略"，但这个推理有问题：(a) FOLIO 是二分类（True/False/Unknown 但主要是 True/False），1pp/class 的阈值不适用；(b) 在 n=204 的 FOLIO 上，2pp ≈ 4 个样本的差异，而在 n=600 的 ProofWriter 上，2pp = 12 个样本——实际影响规模差异很大；(c) sensitivity analysis (±1/±2/±3pp) 虽然做了，但结论 "margin-dependent" 恰恰说明 margin 选择是主观的。
- 建议：在 §4 中更详细地讨论 margin 选择的敏感性，至少报告 TOST 在 ±1pp 下的结论（大概率全部 underpowered），让读者自行判断。

---

## 小问题（不影响接收）

- **M1** [minor] §3.1 提到 "Z3 rejects only 3.4% of constraints"——这个低拒绝率可以反过来解读为 Z3 验证层几乎没有提供筛选功能（vacuous verification），建议在此处就明确指出而非等到 §5.1。
- **M2** [minor] Table 1 中 Mistral-7B FOLIO s123/s456/s789 三个 seed 和 Mistral-7B 3s (3-seed aggregated) 的关系需要更清晰的说明——读者可能困惑 3s 是否是三个 single-seed 的平均。
- **M3** [minor] §5.1 "constraints use trace-specific variables (56.4% zero cross-answer overlap)"——这个百分比是在什么粒度上计算的（per-problem？per-dataset？）应明确说明。
- **M4** [minor] Appendix Y (Extended Discussion) 中关于 "SCB as an evaluation framework" 的讨论非常有价值（BR, K_eff, ProcessSim, CCR 四个指标），但被埋在 25-26 页的附录中，建议在主文 §7 Discussion 中至少用一句话指引读者。

---

## Questions for Authors

**Q1.** Proposition 1 的假设 (iii) "approximately uniform constraint yield per trace"：能否提供每个 trace 的约束数量分布（均值、标准差、CV）？如果 CV 很大，Proposition 1 的结论在多大程度上仍然成立？

**Q2.** 56.4% 零变量重叠 vs. 43.6% 有重叠：在有变量重叠的子集中，Z3 是否更频繁地拒绝约束？SICA 在这个子集上的表现是否不同于总体？这可能揭示 SICA 在什么条件下有潜力 work。

**Q3.** Capability-gap pattern 目前仅在 ProofWriter 上验证。在 FOLIO 上用 DeBERTa-NLI 做 cross-architecture verification 的结果如何？如果 pattern 不能跨数据集泛化，§6 的结论需要进一步限定。

**Q4.** 27 种 training-free 修复策略全部失败，但有没有考虑过让提取 prompt 显式要求 "不要提取与你的答案直接相关的约束，只提取与问题结构相关的约束"？即在 prompt 层面而非 post-hoc 层面打破 source-attribution。

**Q5.** α 的 ≥99% insensitivity 被解释为 degeneration evidence，但这也意味着 α 作为 SICA 的一个设计参数是多余的。为什么不直接用 α=0 （即只用 C* 部分的 positive scoring）作为默认？

---

## Missing References

- Wang et al. (2024) "Chain-of-Verification Reduces Hallucination in Large Language Models" — 已引用。
- Huang et al. (2024) "Large Language Models Cannot Self-Correct Reasoning Yet Without External Feedback" — 已引用。
- 建议增加：Lightman et al. (2024) "Let's Verify Step by Step" 在 process-level verification 方面的讨论——论文已引用但仅在 Related Work 中一笔带过，考虑到 SICA 本质上也是一种 process-level intervention，应更详细地对比方法论差异。

---

## Overall Assessment

**评分：3.5 (Borderline Conference)**

本文对 "自提取约束能否改善 LLM 推理" 这个问题给出了全面、系统的负面回答，实验覆盖度在同类 negative-result 论文中罕见（6 模型 × 3 数据集 × 27 修复策略 × multi-seed × oracle control）。诊断框架 (C₀, K_eff, BR) 有直接的实用价值。

主要顾虑在于：(1) 理论贡献（Proposition 1, Remark 1）偏薄——前者形式化不够严谨，后者接近 trivial DPI 应用；(2) 标题 claim 与统计检验力之间存在 gap（10/16 conditions underpowered）；(3) cross-architecture escape 的关键证据 (n=6 Spearman ρ=1.0) 过于初步。如果作者能加强 Proposition 1 的形式化、调整标题措辞、并对 §6 的 claim 适当降级，本文达到 Conference 水平的可能性较高。

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

_source line 1860 · 2026-05-23T10:19:08.401766+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 提交后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 132

## Round 132

2 recorded events


### User

_source line 1861 · 2026-05-23T10:19:23.819739+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

核心结论：**Overall 3.5 (Borderline Conference)**。实验工作量和覆盖度极为出色（6 模型 × 3 数据集 × 27 修复策略），诊断框架有实用价值。主要问题集中在三个方面：

1. **Proposition 1 形式化不严谨**——假设 (iii) "approximately uniform constraint yield" 未给出数学定义也未直接验证，证明全程使用 ≈，更像 empirical observation 而非 theorem
2. **标题 overclaiming**——"Do Not Improve" 与 10/16 conditions underpowered (MDE 1.86–4.84pp) 之间存在 gap
3. **§6 cross-architecture escape 证据过弱**——Spearman ρ=1.0 基于 n=6 个点，monotonicity 由单个 outlier (Mistral-7B) 驱动

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

_source line 1862 · 2026-05-23T10:19:29.695128+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 133

## Round 133

6 recorded events


### User

_source line 1863 · 2026-05-23T10:20:17.965134+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告：新颖性、完整性与写作质量

**论文**: Beyond Self-Consistency: Self-Extracted Constraints Do Not Improve LLM Logical Reasoning
**Venue**: EMNLP 2026 via ARR
**审查维度**: 新颖性、完整性、写作质量

---

## 总体评分

**Overall Assessment**: 3.5 / 5 (Borderline Conference)
**Confidence**: 4 / 5 (Quite sure)
**一句话总结**: 方法论扎实、实验覆盖充分的负面结果论文，但标题 overclaim、核心发现的新颖性受限于 Huang et al. (2024) 的先验结论，cross-architecture escape 过于初步，整体处于 Conference/Findings 分界线。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4 / 5 | 实验设计严谨（FDR 校正、TOST 等价检验、power analysis、bootstrap CI、多种子复制），理论贡献（Proposition 1、Remark 1）在假设条件下技术正确。主要扣分：10/16 条件 underpowered 与标题强断言之间的张力。 |
| Excitement | 3 / 5 | 对社区有实用价值（阻止无效研究方向 + 提供诊断工具），但核心发现——self-extraction 不能提供独立验证信号——在 Huang et al. (2024) "LLMs cannot self-correct without external feedback" 的框架下具有较高的先验可预测性。 |
| Reproducibility | 4 / 5 | 模型、数据集、超参数（K=12, T=0.7, T_ext=0.3, α=0.5）均有明确说明；Z3 求解器和 MAX-SAT 算法有伪代码（Appendix B）；prompt 模板完整（Appendix A）。缺少：代码/数据未随投稿提供。 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 标题 "Do Not Improve" 与统计证据不匹配

- 具体位置：标题；Section 4 (Table 1)；Appendix D (power analysis)
- 问题：标题断言 "Self-Extracted Constraints Do Not Improve LLM Logical Reasoning"，这是一个全称否定命题。但论文自身承认 16 个非退化条件中有 10 个 underpowered（MDE 1.86–4.84 pp，observed power < 21%），只有 4 个条件通过 TOST 等价检验确认 ±2pp 内无效果（Section 4, para 5: "ten conditions remain underpowered for effects below ~2pp"）。Abstract 中使用了更审慎的 "We find no evidence of improvement"，但标题的 "Do Not Improve" 是一个 absence-of-evidence → evidence-of-absence 的逻辑跳跃。
- 为什么影响接收：这是 soundness 层面的问题。Reviewer 和 AC 对 overclaiming 非常敏感；一个基于 underpowered 数据的全称否定主张会削弱论文的可信度。
- 建议修改方向：(a) 标题改为更审慎的表述，如 "…Show No Evidence of Improving…" 或 "…Fail to Improve…"（暗示当前证据下的失败而非逻辑上的不可能）；(b) 或在 abstract 开头更显著地 qualify 这一结论的统计边界。

**N2** [critical] SCB 相对于 Huang et al. (2024) 的增量新颖性论证不足

- 具体位置：Section 2 ("Distinction from CoT confirmation bias") 及 Introduction para 3
- 问题：论文多次引用 Huang et al. (2024) "LLMs cannot self-correct reasoning without external feedback"，并将自身定位为提供 "independent evidence consistent with this limitation in formal verification"（Introduction para 3）。这个定位有两个风险：(1) 如果 SCB 只是 Huang et al. 的一般性结论在 FOL/Z3 载体上的实例化，则贡献降级为 case study；(2) Section 2 中对 CoT confirmation bias (Wan et al. 2025, Turpin et al. 2024) 的区分——"trace level vs. aggregation level"——虽然在概念上成立，但论文没有提供实证证据证明这两种 bias 是可分离的（例如，控制 trace faithfulness 后 SCB 是否仍然存在）。
- 为什么影响接收：新颖性是 EMNLP main conference 的核心维度。如果 AC 判定 SCB 只是已知现象的重新包装，论文会被降级到 Findings。
- 建议修改方向：(a) 明确陈述 SCB 提供了什么 Huang et al. (2024) 没有的——例如 Proposition 1 的形式化、K_eff/BR/C_0 诊断框架、27 种变体的系统排除——这些不是 "consistent with" 而是 "extends"；(b) 最好增加一个实验，在控制 trace faithfulness 的条件下测试 aggregation-level bias 是否独立存在。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] Scope 震荡：SICA-specific claims 与 general claims 反复切换

- 具体位置：Introduction contributions list vs. Discussion (Section 7) vs. 标题
- 问题：论文在两个 scope 层级之间来回切换。标题说 "Self-Extracted Constraints Do Not Improve LLM Logical Reasoning"（通用主张）；Contribution 1 说 "Provably sound Z3 verification becomes vacuous under self-extraction"（SICA-specific）；Discussion 说 "The principle applies to any self-verification method that draws on the generating model's own distribution"（通用）；但 Proposition 1 的假设条件（degeneration、source-attribution scoring、uniform yield）是 SICA 的具体设计选择，不是所有 self-extraction pipeline 的共性。Remark 1 的 Markov chain 论证更通用，但需要 "trace-determined constraints" 这一假设，对于非 deterministic extraction（如 sampling-based constraint generation）不成立。
- 建议：在 Introduction 和 Discussion 中明确区分哪些结论是 SICA-specific（Proposition 1）、哪些是结构性的（Remark 1 的 information ceiling）、哪些需要额外假设才能推广。

**W2** [major] "LLM Logical Reasoning" 标题措辞与实际覆盖范围不匹配

- 具体位置：标题；Section 3.2 (Datasets)
- 问题：标题说 "LLM Logical Reasoning"，但实际测试涵盖 FOLIO/ProofWriter（一阶逻辑）、LogiQA（阅读理解）、StrategyQA（常识推理）、ARC-Challenge（科学推理）、GSM8K（数学推理）。其中 StrategyQA 和 ARC-Challenge 的 constraint extraction 使用的是不同的 prompt（Appendix A: EXTRACTION_PROMPT vs. LOGIC_EXTRACTION_PROMPT），提取的不是 FOL 而是自然语言约束。这既 (a) 比标题暗示的更广（不止逻辑推理），又 (b) 模糊了核心发现的边界（FOL 约束 vs. 自然语言约束的 SCB 机制可能不同）。
- 建议：标题改为 "LLM Reasoning" 或在 Method 中更明确区分 formal (FOL) 和 informal (NL) constraint extraction 的结果差异。

**W3** [major] Cross-architecture escape (Section 6) 贡献过于初步

- 具体位置：Section 6；Table 3
- 问题：(1) Zero-shot DeBERTa 仅在最弱 generator (Mistral-7B, SC=39.33%) 上显著，其余三个 generator 均不显著——这本质上是 "用更强模型替代弱模型" 而非 "独立验证提供互补信号"；(2) Domain-adapted verifier (fine-tuned DeBERTa) 效果更好，但这引入了 training，与论文 "training-free" 的主线矛盾；(3) 整个 escape 只在 ProofWriter 一个数据集上展示，FOLIO 上不显著。作为三个 contribution 之一，evidence base 太薄。
- 建议：(a) 降低 cross-architecture escape 在 contribution list 中的地位（从 "contribution" 降为 "preliminary finding"）；(b) 或增加更多 verifier-generator 组合和数据集的结果。

**W4** [moderate] Abstract 信息过载

- 具体位置：Abstract（1 段，约 200 词）
- 问题：Abstract 在一段中塞入了 K_eff、BR、C_0、κ、TOST、FDR、Proposition 1、M→T→A→C Markov chain、±2pp、1.66–4.97×、+6.67pp 等大量符号和数字。对于不熟悉该领域的读者，这个信息密度过高。特别是 K_eff 在 abstract 中出现但没有任何直觉解释（读者需要翻到 Section 3 才能理解它是有效集成大小）。
- 建议：Abstract 分两段，第一段讲 what and why（problem + main finding），第二段讲 how（方法亮点 + 实验规模）。移除 abstract 中的 K_eff/BR 等符号，用自然语言描述。

**W5** [moderate] K_eff 缺少直觉解释

- 具体位置：Section 3 (page 3, Eq. 1)；首次出现在 Abstract
- 问题：K_eff = K / [1 + (K-1)·κ] 的公式给出了，但论文没有用一句话解释其直觉意义。读者需要理解 Fleiss' κ、ensemble diversity theory 和 Condorcet Jury Theorem 的背景才能理解为什么 K_eff ≤ 1.30 意味着 "insufficient vote diversity"。实际上 K_eff 的含义非常直觉：它是 "K 个 traces 中有多少个等效的独立投票者"，但论文从未这样说。
- 建议：在 Eq. 1 后加一句直觉解释，例如 "Intuitively, K_eff measures how many effectively independent voters K correlated traces are worth."

**W6** [minor] "Symbolic Mirage" 作为 Section 5 标题稍显 dramatic

- 具体位置：Section 5 标题
- 问题：学术论文通常偏好描述性标题。"The Symbolic Mirage" 虽然准确捕捉了内容（符号验证的表面力量是幻觉），但在 EMNLP 正文中可能被视为过于修辞化。
- 建议：可改为更中性的 "Analysis of Symbolic Confirmation Bias" 或保留现有标题但确保评审人不会因此对论文的严肃性产生疑虑。这是极小的风格问题。

---

## 小问题（不影响接收）

- Section 3.2: GSM8K 仅有 n=200，且被标记为 degenerate (C_0 < 5%)，这意味着 SICA 在数学领域的适用性几乎未被有效测试。可在 Limitations 中提及。
- Table 2 (page 6): 列出了 9 个模型的 SCB 数据，但 Gemini-2.5-Pro 标注为 interim (n=95/204)，且 n_err=12，置信区间很宽。建议加注 caveat 或移至 appendix。
- Appendix 体量（16 页）远超正文（8 页）。虽然信息量丰富，但部分内容（如 Section F 的 discordant case studies、Section G 的 oracle control）对审稿判断有较高价值，建议在正文中增加指引。
- `\enlargethispage{4\baselineskip}` 和多处 `\vspace{-Xmm}` 表明页面预算非常紧张。内容本身没有溢出，但建议检查最终 camera-ready 是否会因模板更新而超页。
- Limitations section 仅 3 行（约 50 词），虽然 EMNLP 2026 规则说 "一小段，覆盖 3 个点左右"，但当前版本几乎是最低限度。可适当展开 statistical power 限制和 English-only 范围。

---

## 主要优势

1. **实验覆盖极其充分**：6 个 open-source 模型 + 3 个 frontier API 模型、7 个数据集、3 个推理域、27 个 training-free 变体、多种子复制——这是我见过的最彻底的 negative-result 论文之一。
2. **统计方法论严谨**：FDR 控制、TOST 等价检验、power analysis、bootstrap CI、permutation null model、McNemar paired test，远超该领域的平均水准。论文坦诚报告 underpowered conditions（Section 4 para 5），这种透明度值得肯定。
3. **理论贡献有独立价值**：Proposition 1（argmax preservation under degeneration）和 Remark 1（information ceiling via data processing inequality）为理解 self-extraction pipeline 的局限性提供了结构性框架，可推广到 SICA 之外。
4. **诊断框架具有实践价值**：C_0、K_eff、BR 三个零成本指标 + 决策边界 + 前瞻验证（held-out model families），使从业者能在 pilot run 阶段判断是否值得部署 self-extraction 方法。
5. **Related Work 覆盖全面**：结构清晰的分类（specification-generation / program-generation / trace-extraction），Reflexion、LATS、CRITIC 等重要工作均已引用。与 Huang et al. (2024) 和 Wan et al. (2025) 的区分在概念上成立。

---

## 缺失引用

主要引用基本完整。以下是可考虑补充的：

- **Self-Evaluation Guided Beam Search** (Xie et al., 2023): 与 self-verification 相关的 beam search 方法
- **Verification-guided reasoning** 方向的更多最新工作（2025-2026），如果有的话
- 建议确认 Zhou et al. (2023/2024) LATS 的引用年份一致性（bib 中标注 2023 但 main.aux 中解析为 2024）

---

## Overall Assessment

**评分: 3.5 / 5 (Borderline Conference)**

这是一篇执行质量很高的负面结果论文，实验设计和统计方法论远超同类工作的平均水准。核心贡献——识别并形式化 Symbolic Confirmation Bias——在概念上有独立价值，诊断框架具有实践意义。

降低评分的主要因素：(1) 标题 overclaiming（全称否定 vs. underpowered evidence）是 soundness 层面的瑕疵；(2) 核心发现与 Huang et al. (2024) 的增量距离不够大，需要更强的 distinction 论证；(3) Cross-architecture escape 作为三个 contribution 之一，evidence base 不足。

如果作者修正标题表述、加强 SCB 的独立新颖性论证、并将 cross-architecture escape 定位为 preliminary finding 而非 main contribution，本文适合 EMNLP main conference。当前状态下，Findings 是更安全的归宿。

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

_source line 1864 · 2026-05-23T10:20:55.802328+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告：方法严谨性与实验设计\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n**Confidence**: 4 / 5\n\n### Must-Fix\n\n**N1** [critical] Proposition 1 的形式化不够严谨，更像是 empirical observation 而非 theorem\n- 三个假设中，(i) 使用 |C^∖| ≈ 0 而非精确条件，(iii) \"approximately uniform constraint yield\" 从未给出数学定义，证明中全程使用 ≈ 而非 =。结论通过 >90% 经验一致性支撑而非严格推出。假设 (iii) 未直接验证。\n- 建议：给假设 (iii) 精确数学表述（如 CV < δ），推导近似误差上界；或降格为 Empirical Observation。\n\n**N2** [critical] 标题/中心 claim 与统计检验力不匹配\n- 标题 \"Do Not Improve\" 但 10/16 conditions underpowered (MDE 1.86–4.84pp)。论文自己承认 \"Absence of evidence is not evidence of absence\"，但标题未反映。\n- 建议：标题改为 \"Provide No Detectable Improvement\" 或加入效应大小限定。\n\n### Should-Fix\n\n**W1** [major] Remark 1 (DPI) 接近 trivial——C = f(T) 的 Markov chain 对任何确定性后处理成立。更有趣的 C ⊥ Y | A 声明未被形式化证明。\n\n**W2** [major] BR 指标的循环性——source-attribution 下 BR > 1 几乎 tautological。56.4% 零变量重叠使约束根本无法跨答案判别。建议报告 BR_excess = BR_obs - BR_null。\n\n**W3** [major] Cross-architecture escape Spearman ρ=1.0 基于 n=6，monotonicity 由 Mistral-7B 单个 outlier 驱动。Table 3 中 3 个 generator 的 Δ 在 0.50–0.83pp 几乎无差异。\n\n**W4** [moderate] TOST ±2pp margin 选择依据不充分——FOLIO 是近二分类，1pp/class 阈值不适用。\n\n### Minor\n- M1: Z3 3.4% rejection rate 应更早指出 vacuous\n- M2: Mistral-7B 3s vs single-seed 关系需澄清\n- M3: 56.4% 零重叠的计算粒度需说明\n- M4: Appendix Y 的 evaluation framework 讨论应在主文指引\n\n### Questions\nQ1: Proposition 1 假设 (iii) 的约束数量分布？\nQ2: 43.6% 有重叠子集的 Z3 拒绝率和 SICA 表现？\nQ3: FOLIO 上的 cross-architecture verification 结果？\nQ4: 是否尝试过 prompt 层面打破 source-attribution？\nQ5: 为什么不默认 α=0？",
  "project": "symb_invariant_consensus",
  "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
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
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告：方法严谨性与实验设计\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n**Confidence**: 4 / 5\n\n### Must-Fix\n\n**N1** [critical] Proposition 1 的形式化不够严谨，更像是 empirical observation 而非 theorem\n- 三个假设中，(i) 使用 |C^∖| ≈ 0 而非精确条件，(iii) \"approximately uniform constraint yield\" 从未给出数学定义，证明中全程使用 ≈ 而非 =。结论通过 >90% 经验一致性支撑而非严格推出。假设 (iii) 未直接验证。\n- 建议：给假设 (iii) 精确数学表述（如 CV < δ），推导近似误差上界；或降格为 Empirical Observation。\n\n**N2** [critical] 标题/中心 claim 与统计检验力不匹配\n- 标题 \"Do Not Improve\" 但 10/16 conditions underpowered (MDE 1.86–4.84pp)。论文自己承认 \"Absence of evidence is not evidence of absence\"，但标题未反映。\n- 建议：标题改为 \"Provide No Detectable Improvement\" 或加入效应大小限定。\n\n### Should-Fix\n\n**W1** [major] Remark 1 (DPI) 接近 trivial——C = f(T) 的 Markov chain 对任何确定性后处理成立。更有趣的 C ⊥ Y | A 声明未被形式化证明。\n\n**W2** [major] BR 指标的循环性——source-attribution 下 BR > 1 几乎 tautological。56.4% 零变量重叠使约束根本无法跨答案判别。建议报告 BR_excess = BR_obs - BR_null。\n\n**W3** [major] Cross-architecture escape Spearman ρ=1.0 基于 n=6，monotonicity 由 Mistral-7B 单个 outlier 驱动。Table 3 中 3 个 generator 的 Δ 在 0.50–0.83pp 几乎无差异。\n\n**W4** [moderate] TOST ±2pp margin 选择依据不充分——FOLIO 是近二分类，1pp/class 阈值不适用。\n\n### Minor\n- M1: Z3 3.4% rejection rate 应更早指出 vacuous\n- M2: Mistral-7B 3s vs single-seed 关系需澄清\n- M3: 56.4% 零重叠的计算粒度需说明\n- M4: Appendix Y 的 evaluation framework 讨论应在主文指引\n\n### Questions\nQ1: Proposition 1 假设 (iii) 的约束数量分布？\nQ2: 43.6% 有重叠子集的 Z3 拒绝率和 SICA 表现？\nQ3: FOLIO 上的 cross-architecture verification 结果？\nQ4: 是否尝试过 prompt 层面打破 source-attribution？\nQ5: 为什么不默认 α=0？",
    "project": "symb_invariant_consensus",
    "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
  }
}
```

</details>

---


### Tool result

_source line 1865 · 2026-05-23T10:21:18.007846+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22205
}
```

</details>

---


### Tool call

_source line 1866 · 2026-05-23T10:21:18.359275+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告：新颖性、完整性与写作质量\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n**Confidence**: 4 / 5\n\n### Must-Fix\n\n**N1** [critical] 标题 \"Do Not Improve\" 与统计证据不匹配\n- 全称否定命题，但 10/16 underpowered，只有 4 条件通过 TOST。Abstract 的 \"find no evidence\" 更审慎，但标题是逻辑跳跃。\n- 建议改为 \"Show No Evidence of Improving\" 或 \"Fail to Improve\"。\n\n**N2** [critical] SCB 相对于 Huang et al. (2024) 增量新颖性论证不足\n- 论文定位为 \"independent evidence consistent with\" Huang et al.——风险是降级为 case study。§2 对 CoT bias 的区分（trace level vs aggregation level）缺少实证证据证明两种 bias 可分离。\n- 建议：明确 SCB 提供了什么 Huang et al. 没有的（形式化、诊断框架、27 变体排除），最好增加控制 trace faithfulness 的实验。\n\n### Should-Fix\n\n**W1** [major] Scope 震荡——标题通用，Contribution 1 SICA-specific，Discussion 又扩展到 \"any self-verification method\"。Proposition 1 假设是 SICA 设计选择，不是所有 self-extraction pipeline 的共性。Remark 1 需要 \"trace-determined constraints\" 假设。\n\n**W2** [major] \"LLM Logical Reasoning\" 标题措辞与实际覆盖范围不匹配——实际测试包括常识推理、数学推理。FOL 约束 vs NL 约束的 SCB 机制可能不同。\n\n**W3** [major] Cross-architecture escape 贡献过于初步——仅最弱 generator 显著，domain-adapted verifier 引入 training 与主线矛盾，仅 ProofWriter 一个数据集。\n\n**W4** [moderate] Abstract 信息过载——一段中塞入 K_eff、BR、C_0、κ、TOST 等大量符号。\n\n**W5** [moderate] K_eff 缺少直觉解释——Eq. 1 后应加一句 \"K_eff measures how many effectively independent voters K correlated traces are worth\"。\n\n**W6** [minor] \"Symbolic Mirage\" 作为 Section 标题稍 dramatic。\n\n### Minor\n- GSM8K degenerate 意味着数学域未有效测试\n- Gemini interim (n=95) 置信区间很宽\n- Appendix 16 页远超正文，关键内容需主文指引\n- 页面预算极紧张（\\enlargethispage{4\\baselineskip}）\n- Limitations 仅 3 行偏短\n\n### 缺失引用\n- Xie et al. (2023) Self-Evaluation Guided Beam Search\n- LATS 引用年份一致性检查",
  "project": "symb_invariant_consensus",
  "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
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
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告：新颖性、完整性与写作质量\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n**Confidence**: 4 / 5\n\n### Must-Fix\n\n**N1** [critical] 标题 \"Do Not Improve\" 与统计证据不匹配\n- 全称否定命题，但 10/16 underpowered，只有 4 条件通过 TOST。Abstract 的 \"find no evidence\" 更审慎，但标题是逻辑跳跃。\n- 建议改为 \"Show No Evidence of Improving\" 或 \"Fail to Improve\"。\n\n**N2** [critical] SCB 相对于 Huang et al. (2024) 增量新颖性论证不足\n- 论文定位为 \"independent evidence consistent with\" Huang et al.——风险是降级为 case study。§2 对 CoT bias 的区分（trace level vs aggregation level）缺少实证证据证明两种 bias 可分离。\n- 建议：明确 SCB 提供了什么 Huang et al. 没有的（形式化、诊断框架、27 变体排除），最好增加控制 trace faithfulness 的实验。\n\n### Should-Fix\n\n**W1** [major] Scope 震荡——标题通用，Contribution 1 SICA-specific，Discussion 又扩展到 \"any self-verification method\"。Proposition 1 假设是 SICA 设计选择，不是所有 self-extraction pipeline 的共性。Remark 1 需要 \"trace-determined constraints\" 假设。\n\n**W2** [major] \"LLM Logical Reasoning\" 标题措辞与实际覆盖范围不匹配——实际测试包括常识推理、数学推理。FOL 约束 vs NL 约束的 SCB 机制可能不同。\n\n**W3** [major] Cross-architecture escape 贡献过于初步——仅最弱 generator 显著，domain-adapted verifier 引入 training 与主线矛盾，仅 ProofWriter 一个数据集。\n\n**W4** [moderate] Abstract 信息过载——一段中塞入 K_eff、BR、C_0、κ、TOST 等大量符号。\n\n**W5** [moderate] K_eff 缺少直觉解释——Eq. 1 后应加一句 \"K_eff measures how many effectively independent voters K correlated traces are worth\"。\n\n**W6** [minor] \"Symbolic Mirage\" 作为 Section 标题稍 dramatic。\n\n### Minor\n- GSM8K degenerate 意味着数学域未有效测试\n- Gemini interim (n=95) 置信区间很宽\n- Appendix 16 页远超正文，关键内容需主文指引\n- 页面预算极紧张（\\enlargethispage{4\\baselineskip}）\n- Limitations 仅 3 行偏短\n\n### 缺失引用\n- Xie et al. (2023) Self-Evaluation Guided Beam Search\n- LATS 引用年份一致性检查",
    "project": "symb_invariant_consensus",
    "chat_id": "oc_c338e034cbffa10b9cc723e731d288d8"
  }
}
```

</details>

---


### Tool result

_source line 1867 · 2026-05-23T10:21:19.767226+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1407
}
```

</details>

---


### Assistant

_source line 1868 · 2026-05-23T10:21:22.218119+00:00_

交叉分享已派发，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 134

## Round 134

2 recorded events


### User

_source line 1869 · 2026-05-23T10:21:24.758151+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

总结：评分 **3.5/5 (Borderline Conference)**。两个 critical 问题：(1) 标题 "Do Not Improve" 在 10/16 条件 underpowered 下属于 overclaiming；(2) SCB 相对于 Huang et al. (2024) 的增量新颖性论证不足。四个 major/moderate 问题涉及 scope 震荡、cross-architecture escape 证据薄弱、abstract 信息过载、K_eff 缺少直觉解释。主要优势在于实验覆盖极其充分（9 模型 / 7 数据集 / 27 变体）和统计方法论严谨。

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

_source line 1870 · 2026-05-23T10:21:28.890627+00:00_

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


## Round 135

## Round 135

2 recorded events


### User

_source line 1871 · 2026-05-23T10:23:02.281215+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 的交叉回应

---

### Must-Fix

**[AGREE] R1-N1: Proposition 1 形式化不够严谨**

同意 R1 的核心判断。Proposition 1 的三个假设中，(i) 使用 |C^\| ≈ 0 是近似而非精确条件，(iii) "approximately uniform constraint yield" 确实没有数学定义（如 coefficient of variation < δ）。证明中 "By (iii), total weight for answer a is proportional to n_a" 是一个 hand-wave 步骤——如果 yield 不均匀，这个 proportionality 会有多大误差？论文没有给出近似误差上界。

补充：论文用 >90% 的 SICA-SC 一致率作为经验支撑（Section 5.1: "SICA produces answers identical to count-only aggregation on 94.4% of problems"），但这只证明结论大致成立，不能替代严格推导。R1 建议降格为 Empirical Observation 或给出误差界，我认为前者更实际——给 (iii) 一个精确的充分条件 + 误差界会是更好的选择，但即使降格为 Empirical Observation，配合 Remark 1 的 DPI 论证，核心论点仍然成立。

**[AGREE] R1-N2: 标题与统计检验力不匹配**

完全同意，这与我的 N1 一致。标题 "Do Not Improve" 是全称否定，但 10/16 条件 underpowered（Appendix D: MDE 1.86–4.84pp, observed power < 21%）。论文自身在 Section 4 para 5 明确承认 "Absence of evidence is not evidence of absence for small effects"，这与标题矛盾。R1 建议的 "Provide No Detectable Improvement" 比我建议的 "Show No Evidence of Improving" 更精确，我支持 R1 的表述。

---

### Should-Fix

**[AGREE] R1-W1: Remark 1 (DPI) 接近 trivial**

同意 R1 的判断。I(C_{1:K}; Y) ≤ I(T_{1:K}; Y) 对任何确定性后处理 C = f(T) 都成立——这不是 self-extraction 的特殊性质，而是数据处理不等式的直接推论。论文真正有价值的 claim 是 C ⊥ Y | A（Figure 3 causal DAG caption 中标注），即约束不含超出答案的额外信息——但这个更强的命题没有被形式化证明。

补充我的观察：论文在 Remark 1 和 Figure 3 之间存在微妙的 claim 升级。Remark 1 只证明了 I(C;Y) ≤ I(T;Y)（trivial），但 Figure 3 的 DAG 隐含了更强的 C ⊥ Y | A（non-trivial）。后者需要证明 T → A 的映射使得 C 中关于 Y 的信息完全被 A 中介——这需要额外的条件（如 Proposition 1 的 degeneration + source-attribution），但论文没有将两者明确连接。建议作者在 Remark 1 中显式声明：在 Proposition 1 的条件下，更强的 I(C;Y) ≤ I(A;Y) 成立。

**[AGREE] R1-W2: BR 指标的循环性**

这是 R1 审稿中最 insightful 的观察之一，我在初审中未充分挖掘。

论文自身提供了关键证据：Section 5.1 para 2 报告 permutation null model 产生 BR_null ≈ BR_obs（p > 0.7），并称这 "confirming that observed BR is fully explained by the trace-count base rate"。但这恰恰证明了 R1 的论点——如果 BR 完全由 trace-count base rate 解释，那么 BR > 1 不是 "symbolic confirmation bias" 的证据，而只是 source-attribution scoring 的数学必然。

56.4% 零变量重叠（Section 5.1 para 3）进一步强化了这个论点：当超过半数的约束在变量层面就无法跨答案比较时，BR > 1 是 by construction 的。

R1 建议报告 BR_excess = BR_obs - BR_null 很有建设性。如果 BR_excess ≈ 0（论文的 permutation test 暗示如此），这实际上意味着 SCB 的 "bias" 完全来自结构性的 source-attribution，而非约束内容本身的偏向——这反而强化了 Proposition 1 的 degeneration 论点，但需要重新框定 BR 的角色（从 "bias 的度量" 变为 "degeneration 的度量"）。

**[AGREE] R1-W3: Cross-architecture Spearman ρ=1.0 基于 n=6**

同意。Table 3 (Section 6) 的数据结构是：Mistral-7B 获得 +6.67pp，其余三个 generator（LLaMA-3.1-8B +0.83pp, Qwen2.5-14B +0.67pp, Qwen3-14B +0.50pp）几乎无差异。所谓的 "monotonic decrease" 实质上是一个 outlier（Mistral-7B，唯一 SC 低于 verifier standalone accuracy 的 generator）驱动的二元模式，而非连续的单调关系。

n=6 的 Spearman ρ=1.0 在统计上确实可以达到 p=0.003（排列检验），但 R1 指出的 outlier 驱动问题使得这个统计显著性的实质意义大打折扣。更诚实的表述是："只有当 generator 弱于 verifier 时才观察到显著增益"，这是一个二元判断而非连续的 capability-gap pattern。

**[REBUT] R1-W4: TOST ±2pp margin 选择**

部分不同意 R1 的判断。

R1 称 "FOLIO 是近二分类，1pp/class 阈值不适用"。但 FOLIO 有三个类别（True/False/Unknown），并非二分类。论文在 Section 4 para 5 给出了 margin 的依据："effects below one percentage point per class provide negligible practical benefit on datasets with ≥3 answer categories"。对于三分类问题，±2pp 总体效应 ≈ ±0.67pp/class，这个阈值确实很小。

不过，R1 的关注有一定道理：(a) ProofWriter 是二分类（True/False），±2pp = ±1pp/class，在 n=600 时这是合理的 margin；(b) 论文在 Appendix 中做了 ±1pp 和 ±3pp 的 sensitivity analysis，结论随 margin 变化（Section 4 para 5 提到 "equivalence conclusions are margin-dependent"），这恰恰说明 margin 选择确实影响结论。

总结：±2pp margin 在三分类数据集上合理，但论文应在 Section 4 正文中更明确地区分二分类 vs. 三分类数据集的 margin 适用性，而非笼统地使用同一 margin。

---

### Minor

**[AGREE] R1-M1**: Z3 3.4% rejection rate 是 SCB 的一个关键前提条件（对应 Proposition 1 假设 (i)），确实应在 Method 或 Results 开头就明确指出，而非等到 Section 5.1。

**[AGREE] R1-M2**: Table 1 中 Mistral-7B 出现多行（s123, s456, s789, 3s），行间关系不直观。建议在 Table caption 或脚注中说明 3s 是三个 seed 的平均。

**[AGREE] R1-M3**: 56.4% 零重叠的计算粒度确实需要说明——是 per-problem、per-trace 还是 per-constraint pair。

**[AGREE] R1-M4**: Appendix Y 的 SCB evaluation framework 讨论在 Discussion 中确实缺少指引。

---

### Questions 评论

R1 的五个问题质量很高，我特别关注：

- **Q1 (假设 iii 的约束数量分布)** 和 **Q2 (43.6% 有重叠子集的表现)** 直接指向 Proposition 1 的薄弱环节——如果作者能提供这些数据，将显著加强或削弱该命题的可信度。
- **Q4 (prompt 层面打破 source-attribution)** 很有启发性——如果可以通过 prompt 设计使约束不再绑定到 source trace，理论上可以打破 Proposition 1 的假设 (ii)，这是 27 种变体中似乎未探索的方向。
- **Q5 (为什么不默认 α=0)** 指向一个实际的设计选择问题——论文在 Section 5.1 提到 α-insensitivity（α ∈ {0.1,...,0.9} 产生 ≥99% 一致），但没有解释为什么 α=0.5 是默认值而非 α=0（完全忽略 penalty）。如果 degeneration 确实成立，α 的值理论上不应该影响结果。

---

### 综合评价

R1 和我（R2）在以下问题上达成一致：
1. **标题 overclaiming**（R1-N2 = R2-N1）：最高优先级修改项
2. **Proposition 1 形式化不足**（R1-N1）：需要降格或加强
3. **Cross-architecture escape 证据不足**（R1-W3 ≈ R2-W3）

R1 提出了我初审未充分覆盖的重要问题：
- **BR 循环性**（R1-W2）：这实际上可能需要重新框定 BR 在论文中的角色
- **Remark 1 的 trivial 性**（R1-W1）：需要将 DPI bound 与 C ⊥ Y | A 的更强命题显式连接

我在一个问题上与 R1 有分歧：
- **TOST margin**（R1-W4）：±2pp 在三分类上合理，但需要区分数据集

两位 reviewer 均给出 3.5/5 (Borderline Conference)，confidence 4/5。核心问题一致：标题修正 + 理论贡献精确化后，论文可达到 Conference 水平；当前状态下 Findings 更稳妥。

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

_source line 1872 · 2026-05-23T10:23:07.425222+00:00_

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


## Round 136

## Round 136

10 recorded events


### User

_source line 1873 · 2026-05-23T10:23:09.932317+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix

**[AGREE] R2-N1: 标题 "Do Not Improve" 与统计证据不匹配**
同意，且我在自己的审稿意见中独立提出了相同问题（我的 N2）。10/16 conditions 的 McNemar power 对 |Δ|=2pp 效应不足 80%，MDE 达 1.86–4.84pp（Appendix D）。论文自己在 §4 承认 "Absence of evidence is not evidence of absence for small effects"，但标题措辞是全称否定。R2 建议的 "Show No Evidence of Improving" 或 "Fail to Improve" 都比现标题更准确。我自己的建议（"Provide No Detectable Improvement"）也是类似思路。这是两位 reviewer 独立达成共识的问题，应当优先修改。

**[AGREE with nuance] R2-N2: SCB 相对于 Huang et al. (2024) 增量新颖性论证不足**
部分同意。R2 指出的风险（论文被降级为 Huang et al. 的 case study）是真实存在的——§7 Discussion 中 "providing independent evidence consistent with Huang et al. (2024)" 这句话确实在自我降级。

但我认为论文实际贡献超出了 R2 所担心的范围：(1) Proposition 1 和 Remark 1 提供了 Huang et al. 没有的形式化框架（尽管我认为其严谨度不足，见我的 N1）；(2) 诊断框架 (C₀, K_eff, BR) 是可操作的实用工具；(3) 27 种修复策略的系统排除为 "limitation is structural, not fixable by prompting" 提供了远比 Huang et al. 更强的证据。

**但** R2 关于 "需要实证证据证明 CoT bias 和 SCB 可分离" 的建议是对的。§2 区分了 trace-level bias 和 aggregation-level bias，但这个区分目前只是概念性的（"CoT bias operates at the trace level; SCB operates at the aggregation level"），没有设计实验来证明两者独立。例如，如果对 trace 做 faithfulness intervention（使 trace 更 faithful）后 SCB 是否消失？论文没有回答这个问题。

建议作者在 §2 或 §7 中更明确地论证 SCB 的独立贡献，避免 "consistent with" 这种自我降级措辞。

---

### Should-Fix

**[AGREE] R2-W1: Scope 震荡**
同意这是一个结构性问题。Proposition 1 的三个假设——(i) degeneration |C^∖| ≈ 0、(ii) source-attribution scoring、(iii) approximately uniform yield——都是 SICA 的具体设计选择，不是所有 self-extraction pipeline 的共性。一个不使用 source-attribution scoring 的 pipeline（例如 semantic evaluation）不满足假设 (ii)；一个 constraint filtering 更激进的 pipeline 不满足假设 (i)。论文在 Remark 2 (§5.1) 讨论了 semantic evaluation 的情况，但主文的 claim scope 仍然在 "SICA-specific" 和 "any self-verification method" 之间摇摆。

Remark 1 的 DPI bound 确实更通用（只需要 C = f(T) 的确定性假设），但如我在自己的 W1 中指出，这个 bound 本身接近 trivial。

建议：在 §5.1 和 §7 中明确区分 "SICA-specific 结论"（Proposition 1）和 "一般性结论"（Remark 1 的 DPI bound），不要在两者之间混用 scope。

**[AGREE] R2-W2: "LLM Logical Reasoning" 标题措辞与实际覆盖范围不匹配**
同意。论文实际测试了 FOLIO (FOL)、ProofWriter (FOL)、LogiQA (NL 逻辑)、StrategyQA (常识)、GSM8K (数学)、AIME (数学)。但 GSM8K 和 AIME 在 degenerate regime (C₀ < 5%)，StrategyQA 只用于 LLaMA-3.1-8B 一个模型（Table 1），且没有 FOL 注释。核心有效测试集中在 FOLIO 和 ProofWriter，两者都是 FOL 推理。标题中 "Logical Reasoning" 对于 StrategyQA/GSM8K 的覆盖名不副实。

不过我认为这个问题的严重性低于 R2 评级（major）。论文的核心机制（约束与 source trace 耦合）不依赖于推理类型，而是依赖于自提取的结构性属性。即使标题措辞不精确，核心论点不受影响。建议标题改为 "LLM Reasoning" 去掉 "Logical" 即可。

**[AGREE] R2-W3: Cross-architecture escape 贡献过于初步**
同意，且与我的 W3 一致。补充 R2 的论点：domain-adapted verifier（在 ProofWriter depth-5 OWA 上 fine-tune DeBERTa）引入了 task-specific training，与论文主线（training-free 方法的局限性）形成逻辑张力。论文在 §6 试图论证 "escape requires structural independence"，但 domain-adapted verifier 的成功可能更多来自 supervised signal 而非 structural independence 本身。这两个因素（independence + supervision）被混淆了。

**[REBUT] R2-W4: Abstract 信息过载**
不完全同意。Abstract 中确实包含 K_eff、BR、C₀、κ 等符号，信息密度高。但这是一篇方法论密集的 negative-result 论文——abstract 需要传达 (1) 提出了什么方法、(2) 方法为什么失败、(3) 诊断工具是什么、(4) escape path。在 ACL/EMNLP venue，审稿人和读者通常具备处理这些符号的背景。

不过 R2 的关注有一定道理：K_eff 在 abstract 中首次出现时确实缺少直觉解释。建议在 abstract 中对 K_eff 加一个括号解释（如 "effective independent sample count"），而非删除这些符号。

**[AGREE] R2-W5: K_eff 缺少直觉解释**
同意。Eq. 1 后应加一句类似 "K_eff measures how many effectively independent votes K correlated traces contribute" 的解释。当前写法直接给出公式和一个数值例子 (K=12, κ=0.69, K_eff ≈ 1.3)，对不熟悉 ensemble theory 的读者不够友好。这个修改成本很低，应该做。

**[REBUT] R2-W6: "Symbolic Mirage" 标题稍 dramatic**
不同意这是需要修改的问题。"Mirage" 准确描述了论文的核心发现——约束提取看起来在做有意义的形式验证（表面上有 Z3 solver、MAX-SAT、99% Z3 validation rate），但实际上退化为多数投票（>90% agreement with SC）。这正是 "海市蜃楼" 的定义：看起来存在但实际不存在。ACL/EMNLP 论文中使用隐喻性 section 标题是常见做法（如 "The Curse of..." / "The Illusion of..."），不影响学术严肃性。

---

### Minor

**[AGREE] GSM8K degenerate → 数学域未有效测试**
同意。C₀ < 5% 意味着 SICA 退化为 SC，GSM8K/AIME 的结果（Δ = 0）是 trivial 的。论文将它们标注为 "exploratory" 是正确的，但这确实意味着论文对数学推理域的覆盖是名义上的。

**[AGREE] Gemini interim (n=95) 置信区间很宽**
同意。Table 2 中 Gemini-2.5-Pro 标注了 *Interim (n=95/204)，n_err ≈ 12。论文在 caption 中也提醒 "should be interpreted with particular caution"（Table 2 caption）。这个透明度是好的，但确实影响结论的可推广性。

**[AGREE] Appendix 16 页远超正文，关键内容需主文指引**
同意，我在自己的 M4 中也提出了类似建议。特别是 Appendix Y (Extended Discussion) 中 SCB evaluation framework 的内容很有价值但完全被埋没。

**[AGREE] 页面预算极紧张**
从 PDF 视觉检查可以确认页面非常紧凑（使用了 \enlargethispage，\looseness=-1 频繁出现）。这是 8 页限制下的客观约束，不是论文缺陷，但确实说明内容量可能超出了 short paper 的承载能力。

**[REBUT] Limitations 仅 3 行偏短**
不同意这是一个问题。Limitations section（主文 §8 后）虽然简短，但覆盖了三个关键点：(1) 模型规模范围 (7B–32B)，(2) 仅英文逻辑推理 benchmark，(3) 统计检验力对 <2pp 效应有限。按 EMNLP 2026 的要求，Limitations 章节只需覆盖 3 个左右的要点，不需要很长。论文在 Appendix Y 中提供了更详细的 scope 讨论，主文 Limitations 作为简要指引是合规的。

---

### 缺失引用

**[AGREE] Xie et al. (2023) Self-Evaluation Guided Beam Search**
同意应在 Related Work 中讨论，特别是在 §2 "Training-based verification" 段落中。该工作与 SICA 的 self-evaluation 机制有关联。

**[AGREE] LATS 引用年份一致性检查**
同意应检查。引用一致性是基本的学术规范。

---

### 与 R2 的评分对比

R2 给出 Overall 3.5 (Borderline Conference)，与我的评分一致。我们在以下核心问题上达成独立共识：
1. 标题 overclaiming（我的 N2 = R2 的 N1）
2. Cross-architecture escape 证据过于初步（我的 W3 ≈ R2 的 W3）
3. Proposition 1 的理论严谨性/scope 问题（我的 N1 部分对应 R2 的 W1）

我对 Remark 1 的 triviality 问题（我的 W1）和 BR 的 by-construction 循环性（我的 W2）有更强的关注，这是 R2 未覆盖的方法论问题。R2 对 Huang et al. 增量新颖性的关注（R2-N2）和 scope 震荡的分析（R2-W1）是我审稿中覆盖不够的角度，我认为这些补充是有价值的。

---

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- 与 R1 在标题 overclaiming、Proposition 1 形式化不足、cross-architecture escape 证据薄弱上达成一致
- R1 的 BR 循环性和 Remark 1 trivial 性指出了我初审未充分挖掘的问题，予以 AGREE
- 唯一分歧在 TOST ±2pp margin：三分类数据集上合理，但需区分二分类 vs. 三分类
- 两位 reviewer 评分一致：3.5/5 Borderline Conference

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

_source line 1874 · 2026-05-23T10:23:32.874065+00:00_

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

_source line 1875 · 2026-05-23T10:23:32.874517+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-23T10:11:34.361234+00:00\", \"completed_at\": \"2026-05-23T10:15:30.551511+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点（纯文本），但 Figure 1 在 page 2 顶部出现，属于前 3 页内，审稿人第一印象建立速度可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 2 散点图：标记点（marker）和 legend 字号偏小，彩色打印下可辨，但灰度打印时不同模型的 marker 区分度依赖形状差异，建议确认 marker shape 多样性足够\"}, {\"severity\": \"warning\", \"dimension\": \"page 5\", \"message\": \"Table 1（主结果表，全宽）：表内数据字号较小（约 7-8pt），密度高；gold ICL / bold / † 等符号系统虽有 caption 解释，但审稿人初看需要理解的符号较多，认知负荷偏高\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 4（23 种策略分类图）：策略名称文字非常小（估计 ≤6pt），打印后可能难以辨认个别策略名。建议适度增大字号或在 caption 中列出关键策略名\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3（Causal DAG）：图较小但内容简洁（5 个节点），可读性尚可\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Limitations 章节简短（约 6 行，覆盖 3 个限制点），符合 EMNLP 要求；位于正文内且只有一个 Limitations section ✓\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"附录 Algorithm 1 和 Algorithm 2 并排全宽排列，算法框格式规范，行号清晰\"}, {\"severity\": \"info\", \"dimension\": \"page 14\", \"message\": \"附录单页含 3 个表格（Table 4, 5, 6）+ 文本，密度极高但作为附录可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 17\", \"message\": \"Figure 5（双面板散点图）和 Figure 6（折线图）：清晰可读，轴标签和 legend 字号适当\"}, {\"severity\": \"info\", \"dimension\": \"page 18\", \"message\": \"Table 14（全宽附录表）：含大量 intervention 结果，脚注详细，排版干净\"}, {\"severity\": \"info\", \"dimension\": \"page 20\", \"message\": \"Figure 7（independence-accuracy 散点图）：清晰，不同方法用不同 marker 区分\"}, {\"severity\": \"info\", \"dimension\": \"page 23\", \"message\": \"Figure 8（combo gain vs capability gap）：清晰可读\"}, {\"severity\": \"info\", \"dimension\": \"page 26\", \"message\": \"末页（附录 Extended Discussion 结尾）：内容约占页面 85%，无大面积空白\"}], \"counts\": {\"critical\": 0, \"warning\": 1, \"info\": 12}}, \"error
…[truncated 29 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1876 · 2026-05-23T10:23:33.276242+00:00_

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

_source line 1877 · 2026-05-23T10:23:33.427298+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1878 · 2026-05-23T10:27:44.065420+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "symb_invariant_consensus",
  "issues_yaml": "# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)\n- id: \"R1-C1\"\n  summary: \"Method Stage 3 sat() implementation undescribed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit.\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Most experiments underpowered (n≤60), no power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Power analysis + Bootstrap CIs added. Larger n conditions (200-600).\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Oracle/upper-bound experiment missing\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp.\"\n  resolution_round: 3\n\n- id: \"R1-C4\"\n  summary: \"Huang et al. (ICLR 2024) not cited\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Huang, Stechly, Kambhampati all cited and discussed.\"\n  resolution_round: 2\n\n- id: \"R1-C5\"\n  summary: \"Critical related work missing\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"~48 citations, 5 Related Work paragraphs.\"\n  resolution_round: 3\n\n- id: \"R1-C9\"\n  summary: \"Capability trap novelty unclear\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Reframed as regime-dependent analysis with CJT framework.\"\n  resolution_round: 3\n\n- id: \"R3-N1\"\n  summary: \"σ(c,a) scoring inconsistent between self-extraction and oracle\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Paper Agent added clarifying sentence in method.tex.\"\n  resolution_round: 4\n\n- id: \"R3-N2\"\n  summary: \"α value never specified\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"α=0.5 explicit in Eq.(3) and §4.1.\"\n  resolution_round: 3\n\n# Round 9+ issues\n\n- id: \"R9-W2\"\n  summary: \"NLI combo weight parameter w 未交叉验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R9-W3\"\n  summary: \"Capability Gap Hypothesis 基于极小样本 (n=6)\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 共识AGREE: Spearman ρ=1.0(n=6)鲁棒性存疑, 建议'preliminary evidence'\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 共识AGREE: n=6 monotonicity由Mistral-7B单个outlier驱动; Table 3中3个generator Δ在0.50-0.83pp几乎无差异; 实质是二元判断非连续pattern\"\n  action_items:\n    - round: 14\n      action: \"§6结论软化为preliminary evidence + 讨论task gap\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 17\n      action: \"Fix 10: 确认§6和Discussion无残余'confirming'措辞\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R9-VL1\"\n  summary: \"Pages 1-2 连续纯文本无 display item\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17 视觉审查: Figure 1在page 2顶部, 在3页窗口内可接受\"\n    - round: 18\n      reviewers: []\n      note: \"R18 视觉审查: 首页无视觉锚点但Figure 1在page 2顶部, 可接受\"\n\n- id: \"R9-VL4\"\n  summary: \"Discussion/Conclusion 展开不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R10-N1\"\n  summary: \"Proposition 1 (Self-Extraction Ceiling) 无证明——empirical claim dressed as theorem\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 13\n  resolution: \"当前论文使用 Proposition 1 with formal proof (page 6)\"\n  resolution_round: 13\n\n- id: \"R10-N2\"\n  summary: \"κ→K_eff 映射理论基础不足——r=0.625 验证弱\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及此技术点, 但R2-W4要求K_eff增加直觉解释\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) K_eff直觉解释问题被再次提出(R2-W5, R1 AGREE)\"\n  action_items:\n    - round: 17\n      action: \"Fix 9: 添加K_eff具体示例(K=12, κ=0.69 → K_eff≈1.3)\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R10-N3\"\n  summary: \"Capability gap 'perfectly monotonic' 结论基于 n=6 非独立数据点\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 与R9-W3合并. 共识: n=6 suggestive非definitive\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 与R9-W3合并\"\n\n- id: \"R10-W1\"\n  summary: \"DRC τ 阈值无 held-out 评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R10-W2\"\n  summary: \"Cross-architecture NLI escape 适用面极窄\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R1-W3+R2 AGREE: 仅6条件, 仅Mistral显著. 方向性发现有价值\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 共识: domain-adapted verifier引入training与主线training-free矛盾; 仅ProofWriter一个数据集\"\n\n- id: \"R10-W3\"\n  summary: \"四种子复制方差大 + 统计功效 <21%\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 轻微分歧: R1认为should-fix, R2降级nice-to-have\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及但包含在标题overclaiming讨论中\"\n\n- id: \"R10-W4\"\n  summary: \"TOST ±2pp margin 缺少显式理由\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 共识: 需说明选择依据, 存在specification searching风险\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 轻微分歧: R1认为FOLIO近二分类不适用; R2 REBUT称三分类合理但需区分二/三分类数据集\"\n  action_items:\n    - round: 17\n      action: \"Fix 12: 添加±2pp先验依据说明\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R10-W5\"\n  summary: \"Bias Ratio 无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"BR CI 已整合: Mistral [3.98,6.37], Qwen [2.44,7.11]\"\n  resolution_round: 10\n\n- id: \"R10-W6\"\n  summary: \"SatLM specification-generation vs SICA trace-extraction 对比不充分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R10-W7\"\n  summary: \"'Symbolic Confirmation Bias' 需与近期 CoT confirmation bias 工作区分\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R2-N3 critical + R1 AGREE w/nuance. 部分共识: 定位为complementary formal verification instance\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) R2-N2 critical + R1 AGREE w/nuance: 'independent evidence consistent with'措辞自我降级; 需明确SCB提供了什么Huang没有的(形式化/诊断框架/27变体排除); 缺少控制trace faithfulness的实证分离实验\"\n  action_items:\n    - round: 16\n      action: \"§2加hedging语言区分\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 17\n      action: \"Fix 4: §2添加1-2段三维度显式对比\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R10-W8\"\n  summary: \"Related Work 过度压缩——引用列表而非文献讨论\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [2]\n      note: \"R17(fresh) R2 minor: §2三个子节间缺显式逻辑连接句\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) R2 S5: Related Work覆盖全面, 结构清晰. 此问题可能已改善\"\n\n- id: \"R10-I1\"\n  summary: \"'Symbolic Mirage' 概念新颖性——与 Huang/Wan 的 confirmation bias 区别\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 同R10-W7\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 同R10-W7\"\n\n- id: \"R10-I2\"\n  summary: \"Independence-Accuracy Trade-off 作为独立贡献有 bias-variance 重述嫌疑\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R10-VL1\"\n  summary: \"主文缺结果可视化\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 17\n  resolution: \"主文7 display items(Figure 1-4 + Table 1-3), 密度0.88/页\"\n  resolution_round: 17\n\n- id: \"R11-N1\"\n  summary: \"Spearman ρ=1.0 (n=6) 被过度使用\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 与R9-W3合并\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 与R9-W3合并\"\n\n- id: \"R11-N2\"\n  summary: \"中心 claim 'SICA fails' 与统计功效不匹配——Abstract/title 过强\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 共识critical: 标题'Do Not Substantially Improve'仍过强\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 共识critical: 标题'Do Not Improve'是全称否定vs 10/16 underpowered; 建议'Provide No Detectable Improvement'(R1)或'Show No Evidence of Improving'(R2)\"\n  action_items:\n    - round: 16\n      action: \"标题软化 + Abstract加power caveat\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 17\n      action: \"Fix 2: 标题去'Substantially' + Abstract改'find no evidence'\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R11-N3\"\n  summary: \"TOST ±2pp margin 缺乏 principled 论证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 共识: 需说明依据\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 轻微分歧: 三分类合理但需区分二/三分类数据集的margin适用性\"\n\n- id: \"R11-W1\"\n  summary: \"DRC 评估不充分——仅PW完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R11-W2\"\n  summary: \"BR 指标存在循环论证倾向\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 共识: 需null model分解\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 共识AGREE: source-attribution下BR>1几乎tautological; permutation null BR_null≈BR_obs(p>0.7)证实BR完全由base rate解释; 56.4%零变量重叠使BR by construction; 建议报告BR_excess=BR_obs-BR_null并将BR重新框定为'degeneration度量'而非'bias度量'\"\n  action_items:\n    - round: 16\n      action: \"BR降级为描述性指标\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 17\n      action: \"Fix 6: 显式框架shuffle control为permutation null model\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R11-W3\"\n  summary: \"术语过度品牌化——'Symbolic Mirage' 偏 dramatic\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 轻微分歧: R2建议改, R1认为有技术对应物可保留\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 轻微分歧: R2建议更中性标题, R1 REBUT认为metaphor准确且ACL/EMNLP常见\"\n\n- id: \"R11-W4\"\n  summary: \"新颖性定位需更早更明确建立与先验工作的 distinction\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"与R10-W7合并\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"与R10-W7合并\"\n\n- id: \"R11-W5\"\n  summary: \"Independence-Accuracy Trade-off 应定位为量化而非新发现\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R11-W6\"\n  summary: \"遗漏引用: Byerly & Khashabi (2026 TACL) 等\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"当前论文已引用 Byerly and Khashabi (2026)\"\n  resolution_round: 13\n\n- id: \"R11-W7\"\n  summary: \"27 策略计数膨胀 + 未尝试 trained constraint extractor\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) scope震荡: 27变体全在SICA paradigm内\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及, 但scope震荡讨论中隐含覆盖\"\n\n- id: \"R11-VL1\"\n  summary: \"主文缺结果可视化——需上提 Figure 到主文\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 17\n  resolution: \"主文7 display items, 密度合理\"\n  resolution_round: 17\n\n- id: \"R12-N1\"\n  summary: \"标题 overclaiming about frontier scale\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"与R11-N2合并\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"与R11-N2合并\"\n\n- id: \"R12-N2\"\n  summary: \"SCB 核心新颖性不足——self-correction failure 在 FOL 载体上的实例化\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"与R10-W7合并\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"与R10-W7合并\"\n\n- id: \"R12-N3\"\n  summary: \"DRC 作为 Contribution 4 不够充分\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"DRC demoted to practical observation in §6\"\n  resolution_round: 13\n  first_raised_round: 12\n  last_seen_round: 13\n\n- id: \"R12-W1\"\n  summary: \"BR 可能存在循环论证——56.4%零变量重叠使约束按定义支持source answer\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"与R11-W2合并\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"与R11-W2合并\"\n\n- id: \"R12-W2\"\n  summary: \"CIL 名称和 information-theoretic 声称有误导\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Renamed to CCR, removed 'unify' claim\"\n  resolution_round: 13\n  first_raised_round: 12\n  last_seen_round: 13\n\n- id: \"R12-W3\"\n  summary: \"Figure 2 placement——应在正文而非附录\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Figure 2 已在正文 page 4\"\n  resolution_round: 13\n\n- id: \"R12-W4\"\n  summary: \"Appendix vs 主文关键信息分配不合理\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [2]\n      note: \"R17(fresh) minor: Abstract信息密度过高; 符号过载\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) R2-W4 moderate: Abstract信息过载; R1 REBUT称密度适合venue但K_eff需括号解释\"\n\n- id: \"R12-EC1\"\n  summary: \"Extractor Confound——所有 frontier cross-model extraction 使用同一 Mistral-7B extractor\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R13-N1\"\n  summary: \"摘要 BR 4.97× 选择性报告——最极端条件\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 17\n  resolution: \"Abstract当前报告full range 1.66×-4.97×\"\n  resolution_round: 16\n\n- id: \"R13-N2\"\n  summary: \"统计功效呈现不足——10/16 underpowered, power analysis 埋在附录\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"与R11-N2合并\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"与R11-N2合并. R18两位Reviewer共识: Table 1需标注power/underpowered\"\n\n- id: \"R13-N3\"\n  summary: \"α=0.5 无敏感性分析\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 共识: ≥99% agreement是ceiling effect非鲁棒性\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) R1-Q5提出为何不默认α=0; 如degeneration成立α理论上不影响结果\"\n  action_items:\n    - round: 17\n      action: \"Fix 7: α sensitivity重新解释为退化证据\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R13-W1\"\n  summary: \"符号/指标过载——8页内7个定量工具\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [2]\n      note: \"R17(fresh) minor: CCR/ProcessSim建议移至Appendix\"\n    - round: 18\n      reviewers: [2]\n      note: \"R18(fresh) R2-W4: Abstract中K_eff/BR/C_0/κ/TOST过载\"\n\n- id: \"R13-W2\"\n  summary: \"NLI claim 须限定到命题逻辑任务\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R13-W3\"\n  summary: \"语法去重可能膨胀 BR——未报告语义去重后 BR\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R13-W4\"\n  summary: \"Symbolic Mirage Hypothesis §3.3 与 §5 验证不连贯\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R13-W5\"\n  summary: \"缺引: Dhuliawala et al. 2023 Chain-of-Verification\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"已引用 dhuliawala2023chainofverification\"\n  resolution_round: 14\n\n- id: \"R14-N1\"\n  summary: \"标题'LLM Reasoning'范围超出实验证据——仅覆盖逻辑推理\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"与R11-N2合并\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) R2-W2 major: 'LLM Logical Reasoning'与实际覆盖不匹配(含常识/数学); R1 AGREE但降级severity\"\n\n- id: \"R14-N2\"\n  summary: \"Symbolic Mirage Hypothesis Predictions 1-2 为事后总结非独立预测\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R14-W1\"\n  summary: \"Cross-architecture实验仅6条件/单一verifier/仅Mistral-7B显著\"\n  category: experiment\n  severity: major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 共识: 方向性发现有价值但证据不足支撑强因果\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 共识: domain-adapted verifier混淆independence和supervision; 仅PW一个数据集; 建议降级为preliminary finding\"\n\n- id: \"R14-W2\"\n  summary: \"8页正文信息过载——§5.5/§6/§7展开不足\"\n  category: writing\n  severity: major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [2]\n      note: \"R17(fresh) minor: Abstract/K_eff缺直觉解释\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) K_eff直觉解释共识; Abstract密度轻微分歧\"\n\n- id: \"R14-W3\"\n  summary: \"'No evidence' claim scope与统计功效不匹配\"\n  category: framing\n  severity: major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"与R11-N2合并\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"与R11-N2合并\"\n\n- id: \"R14-W4\"\n  summary: \"BR计算子集大小(n_err)未报告\"\n  category: experiment\n  severity: moderate\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 17\n  resolution: \"Table 2已有n_err列\"\n  resolution_round: 16\n\n- id: \"R14-W5\"\n  summary: \"Related Work遗漏: SETS(2025), MAV(2025)\"\n  category: writing\n  severity: minor-to-major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [2]\n      note: \"R17(fresh) 新增遗漏: Reflexion(Shinn 2023), LATS(Zhou 2023)\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) R2建议补Xie et al.(2023) Self-Evaluation Guided Beam Search; R1 AGREE\"\n\n- id: \"R14-W6\"\n  summary: \"Fleiss' κ→ICC近似仅r=0.625——prevalence paradox\"\n  category: method\n  severity: moderate\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R15-M1\"\n  summary: \"遗漏引用: DuPO (ICLR 2026)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 17\n  resolution: \"论文§2已引用dupo2025\"\n  resolution_round: 16\n\n- id: \"R15-M2\"\n  summary: \"遗漏引用: S²R (2025)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 17\n  resolution: \"论文§2已引用zeng2025s2r\"\n  resolution_round: 16\n\n- id: \"R15-M3\"\n  summary: \"遗漏引用: LLM as Formalizers on CSP\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R15-M4\"\n  summary: \"遗漏引用: Lakshminarayanan et al. (2017) Deep Ensembles\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R15-W1\"\n  summary: \"α=0.5敏感性分析≥99% agreement是ceiling effect\"\n  category: method\n  severity: minor\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 共识: 退化证据而非鲁棒性\"\n    - round: 18\n      reviewers: [1]\n      note: \"R18(fresh) R1-Q5: 如degeneration成立为何不默认α=0\"\n\n# R16 issues\n\n- id: \"R16-N1\"\n  summary: \"Proposition 1 证明范围与声称范围不匹配 + 证明逻辑跳跃\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 共识critical: score(a)=nₐ从Eq.3推导缺关键步骤\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 共识critical: (i)使用≈非精确条件; (iii)'approximately uniform yield'无数学定义无验证; 证明全程hand-wave; 降格为Empirical Observation或给出误差界\"\n  action_items:\n    - round: 16\n      action: \"拆分为Prop1(SICA-specific)+Corollary(DPI)\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 17\n      action: \"Fix 1: Prop 1改为argmax preservation + 显式假设链\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R16-N2\"\n  summary: \"Diagnostics 100%准确率是in-sample评估——trivial classifier\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 共识: 重定位为failure mode分类工具\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及, 但R2 S4肯定诊断框架实用价值\"\n\n- id: \"R16-M1\"\n  summary: \"遗漏引用: Kamoi et al. (TACL 2024)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 17\n  resolution: \"论文§2已引用kamoi2024selfcorrect\"\n  resolution_round: 16\n\n- id: \"R16-M2\"\n  summary: \"遗漏引用: AlphaCode/CodeT\"\n  category: writing\n  severity: minor\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 17\n  resolution: \"论文§2已引用li2022alphacode和chen2023codet\"\n  resolution_round: 16\n\n- id: \"R16-W1\"\n  summary: \"'Extending Huang et al.' overclaiming\"\n  category: framing\n  severity: major\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"'independent evidence consistent with'措辞已改善但§5.1仍有暗示\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) §7 Discussion中'providing independent evidence consistent with Huang et al.'被R1认为自我降级; 需转为'extends'定位\"\n\n- id: \"R16-W2\"\n  summary: \"GSM8K(n=30)/AIME(n=22)与大样本等权重引用\"\n  category: experiment\n  severity: major\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"共识: 移至Appendix或标exploratory\"\n    - round: 18\n      reviewers: [1]\n      note: \"R18(fresh) R1同意GSM8K degenerate意味着数学域未有效测试\"\n\n- id: \"R16-W3\"\n  summary: \"缺少training-based self-verification讨论\"\n  category: writing\n  severity: major\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 17\n  resolution: \"论文§2已有Training-based verification段落\"\n  resolution_round: 16\n\n- id: \"R16-SYS1\"\n  summary: \"Scope震荡——SICA-specific和general claims反复切换\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 共识: 需§1 contributions明确scope边界\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 共识AGREE: Prop 1假设是SICA设计选择非通用; Remark 1 DPI更通用但trivial; 需明确区分SICA-specific结论(Prop 1)和一般性结论(Remark 1)\"\n\n# R17 issues\n\n- id: \"R17-N1\"\n  summary: \"Corollary 1 (DPI) 应降级为 Remark\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"共识AGREE: I(C;Y)≤I(T;Y)近trivial, 贡献在Markov chain识别\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 共识AGREE: DPI对任何确定性后处理成立; 真正有价值的是C⊥Y|A(Figure 3)但未被形式化证明; Remark 1和Figure 3间存在claim升级\"\n\n- id: \"R17-N2\"\n  summary: \"K_eff 缺少直觉解释\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"共识: 需具体示例\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 共识AGREE: 'K_eff measures how many effectively independent votes K correlated traces contribute'\"\n\n- id: \"R17-N3\"\n  summary: \"遗漏引用: Reflexion(Shinn 2023), LATS(Zhou 2023)\"\n  category: writing\n  severity: minor\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 18\n  resolution: \"论文§2已引用shinn2023reflexion和zhou2023lats\"\n  resolution_round: 18\n\n- id: \"R17-N4\"\n  summary: \"Table 1未标注统计功效\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"共识: 需视觉区分powered/underpowered\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 包含在标题overclaiming讨论中\"\n\n- id: \"R17-N5\"\n  summary: \"C1 Contribution措辞需与Prop 1弱化同步调整\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"Prop 1→argmax + Corollary→Remark后C1需调整\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及但包含在Prop 1和scope讨论中\"\n\n- id: \"R17-VL1\"\n  summary: \"Figure 4 内部文字过小\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"视觉审查: page 7每彩色方框内3-5行小字\"\n    - round: 18\n      reviewers: []\n      note: \"R18 视觉审查: 策略名称≤6pt, 打印后可能难以辨认\"\n\n- id: \"R17-VL2\"\n  summary: \"Appendix pages 16/22 表格堆叠过度拥挤\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"视觉审查: 建议适当分页\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n# R18 new issues\n\n- id: \"R18-N1\"\n  summary: \"Remark 1与Figure 3间存在claim升级——DPI trivial但C⊥Y|A未证明\"\n  category: method\n  severity: major\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2交叉AGREE: Remark 1只证trivial DPI; Figure 3隐含更强的C⊥Y|A; 需在Prop 1条件下显式证明I(C;Y)≤I(A;Y)\"\n\n- id: \"R18-N2\"\n  summary: \"BR应重新框定为degeneration度量而非bias度量\"\n  category: method\n  severity: major\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R1-W2 + R2交叉AGREE: permutation BR_null≈BR_obs意味着BR完全由base rate解释; 建议报告BR_excess并将BR角色从measuring bias转为measuring structural coupling\"\n\n- id: \"R18-M1\"\n  summary: \"遗漏引用: Xie et al. (2023) Self-Evaluation Guided Beam Search\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R2建议, R1 AGREE\"\n\n- id: \"R18-M2\"\n  summary: \"Table 1 Mistral-7B multi-seed行间关系不直观\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [1]\n      note: \"R1-M2: s123/s456/s789与3s(3-seed aggregated)关系需在caption/脚注说明\"\n\n- id: \"R18-M3\"\n  summary: \"56.4%零变量重叠的计算粒度未说明\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [1]\n      note: \"R1-M3: per-problem? per-dataset? per-constraint pair?\"\n\n- id: \"R18-VL1\"\n  summary: \"Table 1(page 5)数据字号偏小(7-8pt), 符号系统认知负荷高\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: []\n      note: \"R18 视觉审查: gold ICL/bold/†等符号系统需理解多个convention\"\n"
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
    "issues_yaml": "# Round 1-8 issues (all resolved/wont_fix) — retained for history (abbreviated)\n- id: \"R1-C1\"\n  summary: \"Method Stage 3 sat() implementation undescribed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Fully formalized: Eq.(1)-(5), Algorithm 1-2, α=0.5 explicit.\"\n  resolution_round: 3\n\n- id: \"R1-C2\"\n  summary: \"Most experiments underpowered (n≤60), no power analysis\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Power analysis + Bootstrap CIs added. Larger n conditions (200-600).\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Oracle/upper-bound experiment missing\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Dual oracle: FOLIO +14.22pp, ProofWriter +11.50pp.\"\n  resolution_round: 3\n\n- id: \"R1-C4\"\n  summary: \"Huang et al. (ICLR 2024) not cited\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Huang, Stechly, Kambhampati all cited and discussed.\"\n  resolution_round: 2\n\n- id: \"R1-C5\"\n  summary: \"Critical related work missing\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"~48 citations, 5 Related Work paragraphs.\"\n  resolution_round: 3\n\n- id: \"R1-C9\"\n  summary: \"Capability trap novelty unclear\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  resolution: \"Reframed as regime-dependent analysis with CJT framework.\"\n  resolution_round: 3\n\n- id: \"R3-N1\"\n  summary: \"σ(c,a) scoring inconsistent between self-extraction and oracle\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Paper Agent added clarifying sentence in method.tex.\"\n  resolution_round: 4\n\n- id: \"R3-N2\"\n  summary: \"α value never specified\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"α=0.5 explicit in Eq.(3) and §4.1.\"\n  resolution_round: 3\n\n# Round 9+ issues\n\n- id: \"R9-W2\"\n  summary: \"NLI combo weight parameter w 未交叉验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R9-W3\"\n  summary: \"Capability Gap Hypothesis 基于极小样本 (n=6)\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 共识AGREE: Spearman ρ=1.0(n=6)鲁棒性存疑, 建议'preliminary evidence'\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 共识AGREE: n=6 monotonicity由Mistral-7B单个outlier驱动; Table 3中3个generator Δ在0.50-0.83pp几乎无差异; 实质是二元判断非连续pattern\"\n  action_items:\n    - round: 14\n      action: \"§6结论软化为preliminary evidence + 讨论task gap\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 17\n      action: \"Fix 10: 确认§6和Discussion无残余'confirming'措辞\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R9-VL1\"\n  summary: \"Pages 1-2 连续纯文本无 display item\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17 视觉审查: Figure 1在page 2顶部, 在3页窗口内可接受\"\n    - round: 18\n      reviewers: []\n      note: \"R18 视觉审查: 首页无视觉锚点但Figure 1在page 2顶部, 可接受\"\n\n- id: \"R9-VL4\"\n  summary: \"Discussion/Conclusion 展开不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R10-N1\"\n  summary: \"Proposition 1 (Self-Extraction Ceiling) 无证明——empirical claim dressed as theorem\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 13\n  resolution: \"当前论文使用 Proposition 1 with formal proof (page 6)\"\n  resolution_round: 13\n\n- id: \"R10-N2\"\n  summary: \"κ→K_eff 映射理论基础不足——r=0.625 验证弱\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及此技术点, 但R2-W4要求K_eff增加直觉解释\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) K_eff直觉解释问题被再次提出(R2-W5, R1 AGREE)\"\n  action_items:\n    - round: 17\n      action: \"Fix 9: 添加K_eff具体示例(K=12, κ=0.69 → K_eff≈1.3)\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R10-N3\"\n  summary: \"Capability gap 'perfectly monotonic' 结论基于 n=6 非独立数据点\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 与R9-W3合并. 共识: n=6 suggestive非definitive\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 与R9-W3合并\"\n\n- id: \"R10-W1\"\n  summary: \"DRC τ 阈值无 held-out 评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R10-W2\"\n  summary: \"Cross-architecture NLI escape 适用面极窄\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R1-W3+R2 AGREE: 仅6条件, 仅Mistral显著. 方向性发现有价值\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 共识: domain-adapted verifier引入training与主线training-free矛盾; 仅ProofWriter一个数据集\"\n\n- id: \"R10-W3\"\n  summary: \"四种子复制方差大 + 统计功效 <21%\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 轻微分歧: R1认为should-fix, R2降级nice-to-have\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及但包含在标题overclaiming讨论中\"\n\n- id: \"R10-W4\"\n  summary: \"TOST ±2pp margin 缺少显式理由\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 共识: 需说明选择依据, 存在specification searching风险\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 轻微分歧: R1认为FOLIO近二分类不适用; R2 REBUT称三分类合理但需区分二/三分类数据集\"\n  action_items:\n    - round: 17\n      action: \"Fix 12: 添加±2pp先验依据说明\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R10-W5\"\n  summary: \"Bias Ratio 无置信区间\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"BR CI 已整合: Mistral [3.98,6.37], Qwen [2.44,7.11]\"\n  resolution_round: 10\n\n- id: \"R10-W6\"\n  summary: \"SatLM specification-generation vs SICA trace-extraction 对比不充分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R10-W7\"\n  summary: \"'Symbolic Confirmation Bias' 需与近期 CoT confirmation bias 工作区分\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) R2-N3 critical + R1 AGREE w/nuance. 部分共识: 定位为complementary formal verification instance\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) R2-N2 critical + R1 AGREE w/nuance: 'independent evidence consistent with'措辞自我降级; 需明确SCB提供了什么Huang没有的(形式化/诊断框架/27变体排除); 缺少控制trace faithfulness的实证分离实验\"\n  action_items:\n    - round: 16\n      action: \"§2加hedging语言区分\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 17\n      action: \"Fix 4: §2添加1-2段三维度显式对比\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R10-W8\"\n  summary: \"Related Work 过度压缩——引用列表而非文献讨论\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [2]\n      note: \"R17(fresh) R2 minor: §2三个子节间缺显式逻辑连接句\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) R2 S5: Related Work覆盖全面, 结构清晰. 此问题可能已改善\"\n\n- id: \"R10-I1\"\n  summary: \"'Symbolic Mirage' 概念新颖性——与 Huang/Wan 的 confirmation bias 区别\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 同R10-W7\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 同R10-W7\"\n\n- id: \"R10-I2\"\n  summary: \"Independence-Accuracy Trade-off 作为独立贡献有 bias-variance 重述嫌疑\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R10-VL1\"\n  summary: \"主文缺结果可视化\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 17\n  resolution: \"主文7 display items(Figure 1-4 + Table 1-3), 密度0.88/页\"\n  resolution_round: 17\n\n- id: \"R11-N1\"\n  summary: \"Spearman ρ=1.0 (n=6) 被过度使用\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 与R9-W3合并\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 与R9-W3合并\"\n\n- id: \"R11-N2\"\n  summary: \"中心 claim 'SICA fails' 与统计功效不匹配——Abstract/title 过强\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 共识critical: 标题'Do Not Substantially Improve'仍过强\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 共识critical: 标题'Do Not Improve'是全称否定vs 10/16 underpowered; 建议'Provide No Detectable Improvement'(R1)或'Show No Evidence of Improving'(R2)\"\n  action_items:\n    - round: 16\n      action: \"标题软化 + Abstract加power caveat\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 17\n      action: \"Fix 2: 标题去'Substantially' + Abstract改'find no evidence'\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R11-N3\"\n  summary: \"TOST ±2pp margin 缺乏 principled 论证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 共识: 需说明依据\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 轻微分歧: 三分类合理但需区分二/三分类数据集的margin适用性\"\n\n- id: \"R11-W1\"\n  summary: \"DRC 评估不充分——仅PW完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R11-W2\"\n  summary: \"BR 指标存在循环论证倾向\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 共识: 需null model分解\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 共识AGREE: source-attribution下BR>1几乎tautological; permutation null BR_null≈BR_obs(p>0.7)证实BR完全由base rate解释; 56.4%零变量重叠使BR by construction; 建议报告BR_excess=BR_obs-BR_null并将BR重新框定为'degeneration度量'而非'bias度量'\"\n  action_items:\n    - round: 16\n      action: \"BR降级为描述性指标\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 17\n      action: \"Fix 6: 显式框架shuffle control为permutation null model\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R11-W3\"\n  summary: \"术语过度品牌化——'Symbolic Mirage' 偏 dramatic\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 轻微分歧: R2建议改, R1认为有技术对应物可保留\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 轻微分歧: R2建议更中性标题, R1 REBUT认为metaphor准确且ACL/EMNLP常见\"\n\n- id: \"R11-W4\"\n  summary: \"新颖性定位需更早更明确建立与先验工作的 distinction\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"与R10-W7合并\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"与R10-W7合并\"\n\n- id: \"R11-W5\"\n  summary: \"Independence-Accuracy Trade-off 应定位为量化而非新发现\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R11-W6\"\n  summary: \"遗漏引用: Byerly & Khashabi (2026 TACL) 等\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"当前论文已引用 Byerly and Khashabi (2026)\"\n  resolution_round: 13\n\n- id: \"R11-W7\"\n  summary: \"27 策略计数膨胀 + 未尝试 trained constraint extractor\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) scope震荡: 27变体全在SICA paradigm内\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及, 但scope震荡讨论中隐含覆盖\"\n\n- id: \"R11-VL1\"\n  summary: \"主文缺结果可视化——需上提 Figure 到主文\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 17\n  resolution: \"主文7 display items, 密度合理\"\n  resolution_round: 17\n\n- id: \"R12-N1\"\n  summary: \"标题 overclaiming about frontier scale\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"与R11-N2合并\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"与R11-N2合并\"\n\n- id: \"R12-N2\"\n  summary: \"SCB 核心新颖性不足——self-correction failure 在 FOL 载体上的实例化\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"与R10-W7合并\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"与R10-W7合并\"\n\n- id: \"R12-N3\"\n  summary: \"DRC 作为 Contribution 4 不够充分\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"DRC demoted to practical observation in §6\"\n  resolution_round: 13\n  first_raised_round: 12\n  last_seen_round: 13\n\n- id: \"R12-W1\"\n  summary: \"BR 可能存在循环论证——56.4%零变量重叠使约束按定义支持source answer\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"与R11-W2合并\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"与R11-W2合并\"\n\n- id: \"R12-W2\"\n  summary: \"CIL 名称和 information-theoretic 声称有误导\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Renamed to CCR, removed 'unify' claim\"\n  resolution_round: 13\n  first_raised_round: 12\n  last_seen_round: 13\n\n- id: \"R12-W3\"\n  summary: \"Figure 2 placement——应在正文而非附录\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"Figure 2 已在正文 page 4\"\n  resolution_round: 13\n\n- id: \"R12-W4\"\n  summary: \"Appendix vs 主文关键信息分配不合理\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [2]\n      note: \"R17(fresh) minor: Abstract信息密度过高; 符号过载\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) R2-W4 moderate: Abstract信息过载; R1 REBUT称密度适合venue但K_eff需括号解释\"\n\n- id: \"R12-EC1\"\n  summary: \"Extractor Confound——所有 frontier cross-model extraction 使用同一 Mistral-7B extractor\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R13-N1\"\n  summary: \"摘要 BR 4.97× 选择性报告——最极端条件\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 17\n  resolution: \"Abstract当前报告full range 1.66×-4.97×\"\n  resolution_round: 16\n\n- id: \"R13-N2\"\n  summary: \"统计功效呈现不足——10/16 underpowered, power analysis 埋在附录\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"与R11-N2合并\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"与R11-N2合并. R18两位Reviewer共识: Table 1需标注power/underpowered\"\n\n- id: \"R13-N3\"\n  summary: \"α=0.5 无敏感性分析\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 共识: ≥99% agreement是ceiling effect非鲁棒性\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) R1-Q5提出为何不默认α=0; 如degeneration成立α理论上不影响结果\"\n  action_items:\n    - round: 17\n      action: \"Fix 7: α sensitivity重新解释为退化证据\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R13-W1\"\n  summary: \"符号/指标过载——8页内7个定量工具\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [2]\n      note: \"R17(fresh) minor: CCR/ProcessSim建议移至Appendix\"\n    - round: 18\n      reviewers: [2]\n      note: \"R18(fresh) R2-W4: Abstract中K_eff/BR/C_0/κ/TOST过载\"\n\n- id: \"R13-W2\"\n  summary: \"NLI claim 须限定到命题逻辑任务\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R13-W3\"\n  summary: \"语法去重可能膨胀 BR——未报告语义去重后 BR\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R13-W4\"\n  summary: \"Symbolic Mirage Hypothesis §3.3 与 §5 验证不连贯\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R13-W5\"\n  summary: \"缺引: Dhuliawala et al. 2023 Chain-of-Verification\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"已引用 dhuliawala2023chainofverification\"\n  resolution_round: 14\n\n- id: \"R14-N1\"\n  summary: \"标题'LLM Reasoning'范围超出实验证据——仅覆盖逻辑推理\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"与R11-N2合并\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) R2-W2 major: 'LLM Logical Reasoning'与实际覆盖不匹配(含常识/数学); R1 AGREE但降级severity\"\n\n- id: \"R14-N2\"\n  summary: \"Symbolic Mirage Hypothesis Predictions 1-2 为事后总结非独立预测\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R14-W1\"\n  summary: \"Cross-architecture实验仅6条件/单一verifier/仅Mistral-7B显著\"\n  category: experiment\n  severity: major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 共识: 方向性发现有价值但证据不足支撑强因果\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 共识: domain-adapted verifier混淆independence和supervision; 仅PW一个数据集; 建议降级为preliminary finding\"\n\n- id: \"R14-W2\"\n  summary: \"8页正文信息过载——§5.5/§6/§7展开不足\"\n  category: writing\n  severity: major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [2]\n      note: \"R17(fresh) minor: Abstract/K_eff缺直觉解释\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) K_eff直觉解释共识; Abstract密度轻微分歧\"\n\n- id: \"R14-W3\"\n  summary: \"'No evidence' claim scope与统计功效不匹配\"\n  category: framing\n  severity: major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"与R11-N2合并\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"与R11-N2合并\"\n\n- id: \"R14-W4\"\n  summary: \"BR计算子集大小(n_err)未报告\"\n  category: experiment\n  severity: moderate\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 17\n  resolution: \"Table 2已有n_err列\"\n  resolution_round: 16\n\n- id: \"R14-W5\"\n  summary: \"Related Work遗漏: SETS(2025), MAV(2025)\"\n  category: writing\n  severity: minor-to-major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [2]\n      note: \"R17(fresh) 新增遗漏: Reflexion(Shinn 2023), LATS(Zhou 2023)\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) R2建议补Xie et al.(2023) Self-Evaluation Guided Beam Search; R1 AGREE\"\n\n- id: \"R14-W6\"\n  summary: \"Fleiss' κ→ICC近似仅r=0.625——prevalence paradox\"\n  category: method\n  severity: moderate\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"R17(fresh) 未单独提及\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R15-M1\"\n  summary: \"遗漏引用: DuPO (ICLR 2026)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 17\n  resolution: \"论文§2已引用dupo2025\"\n  resolution_round: 16\n\n- id: \"R15-M2\"\n  summary: \"遗漏引用: S²R (2025)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 17\n  resolution: \"论文§2已引用zeng2025s2r\"\n  resolution_round: 16\n\n- id: \"R15-M3\"\n  summary: \"遗漏引用: LLM as Formalizers on CSP\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R15-M4\"\n  summary: \"遗漏引用: Lakshminarayanan et al. (2017) Deep Ensembles\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n- id: \"R15-W1\"\n  summary: \"α=0.5敏感性分析≥99% agreement是ceiling effect\"\n  category: method\n  severity: minor\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 共识: 退化证据而非鲁棒性\"\n    - round: 18\n      reviewers: [1]\n      note: \"R18(fresh) R1-Q5: 如degeneration成立为何不默认α=0\"\n\n# R16 issues\n\n- id: \"R16-N1\"\n  summary: \"Proposition 1 证明范围与声称范围不匹配 + 证明逻辑跳跃\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 共识critical: score(a)=nₐ从Eq.3推导缺关键步骤\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 共识critical: (i)使用≈非精确条件; (iii)'approximately uniform yield'无数学定义无验证; 证明全程hand-wave; 降格为Empirical Observation或给出误差界\"\n  action_items:\n    - round: 16\n      action: \"拆分为Prop1(SICA-specific)+Corollary(DPI)\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n    - round: 17\n      action: \"Fix 1: Prop 1改为argmax preservation + 显式假设链\"\n      assigned_to: \"paper_agent\"\n      status: in_progress\n\n- id: \"R16-N2\"\n  summary: \"Diagnostics 100%准确率是in-sample评估——trivial classifier\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 共识: 重定位为failure mode分类工具\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及, 但R2 S4肯定诊断框架实用价值\"\n\n- id: \"R16-M1\"\n  summary: \"遗漏引用: Kamoi et al. (TACL 2024)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 17\n  resolution: \"论文§2已引用kamoi2024selfcorrect\"\n  resolution_round: 16\n\n- id: \"R16-M2\"\n  summary: \"遗漏引用: AlphaCode/CodeT\"\n  category: writing\n  severity: minor\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 17\n  resolution: \"论文§2已引用li2022alphacode和chen2023codet\"\n  resolution_round: 16\n\n- id: \"R16-W1\"\n  summary: \"'Extending Huang et al.' overclaiming\"\n  category: framing\n  severity: major\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"'independent evidence consistent with'措辞已改善但§5.1仍有暗示\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) §7 Discussion中'providing independent evidence consistent with Huang et al.'被R1认为自我降级; 需转为'extends'定位\"\n\n- id: \"R16-W2\"\n  summary: \"GSM8K(n=30)/AIME(n=22)与大样本等权重引用\"\n  category: experiment\n  severity: major\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"共识: 移至Appendix或标exploratory\"\n    - round: 18\n      reviewers: [1]\n      note: \"R18(fresh) R1同意GSM8K degenerate意味着数学域未有效测试\"\n\n- id: \"R16-W3\"\n  summary: \"缺少training-based self-verification讨论\"\n  category: writing\n  severity: major\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 17\n  resolution: \"论文§2已有Training-based verification段落\"\n  resolution_round: 16\n\n- id: \"R16-SYS1\"\n  summary: \"Scope震荡——SICA-specific和general claims反复切换\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"R17(fresh) 共识: 需§1 contributions明确scope边界\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 共识AGREE: Prop 1假设是SICA设计选择非通用; Remark 1 DPI更通用但trivial; 需明确区分SICA-specific结论(Prop 1)和一般性结论(Remark 1)\"\n\n# R17 issues\n\n- id: \"R17-N1\"\n  summary: \"Corollary 1 (DPI) 应降级为 Remark\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"共识AGREE: I(C;Y)≤I(T;Y)近trivial, 贡献在Markov chain识别\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 共识AGREE: DPI对任何确定性后处理成立; 真正有价值的是C⊥Y|A(Figure 3)但未被形式化证明; Remark 1和Figure 3间存在claim升级\"\n\n- id: \"R17-N2\"\n  summary: \"K_eff 缺少直觉解释\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"共识: 需具体示例\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 共识AGREE: 'K_eff measures how many effectively independent votes K correlated traces contribute'\"\n\n- id: \"R17-N3\"\n  summary: \"遗漏引用: Reflexion(Shinn 2023), LATS(Zhou 2023)\"\n  category: writing\n  severity: minor\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 18\n  resolution: \"论文§2已引用shinn2023reflexion和zhou2023lats\"\n  resolution_round: 18\n\n- id: \"R17-N4\"\n  summary: \"Table 1未标注统计功效\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [1, 2]\n      note: \"共识: 需视觉区分powered/underpowered\"\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R18(fresh) 包含在标题overclaiming讨论中\"\n\n- id: \"R17-N5\"\n  summary: \"C1 Contribution措辞需与Prop 1弱化同步调整\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"Prop 1→argmax + Corollary→Remark后C1需调整\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及但包含在Prop 1和scope讨论中\"\n\n- id: \"R17-VL1\"\n  summary: \"Figure 4 内部文字过小\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"视觉审查: page 7每彩色方框内3-5行小字\"\n    - round: 18\n      reviewers: []\n      note: \"R18 视觉审查: 策略名称≤6pt, 打印后可能难以辨认\"\n\n- id: \"R17-VL2\"\n  summary: \"Appendix pages 16/22 表格堆叠过度拥挤\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: []\n      note: \"视觉审查: 建议适当分页\"\n    - round: 18\n      reviewers: []\n      note: \"R18(fresh) 未单独提及\"\n\n# R18 new issues\n\n- id: \"R18-N1\"\n  summary: \"Remark 1与Figure 3间存在claim升级——DPI trivial但C⊥Y|A未证明\"\n  category: method\n  severity: major\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2交叉AGREE: Remark 1只证trivial DPI; Figure 3隐含更强的C⊥Y|A; 需在Prop 1条件下显式证明I(C;Y)≤I(A;Y)\"\n\n- id: \"R18-N2\"\n  summary: \"BR应重新框定为degeneration度量而非bias度量\"\n  category: method\n  severity: major\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R1-W2 + R2交叉AGREE: permutation BR_null≈BR_obs意味着BR完全由base rate解释; 建议报告BR_excess并将BR角色从measuring bias转为measuring structural coupling\"\n\n- id: \"R18-M1\"\n  summary: \"遗漏引用: Xie et al. (2023) Self-Evaluation Guided Beam Search\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [1, 2]\n      note: \"R2建议, R1 AGREE\"\n\n- id: \"R18-M2\"\n  summary: \"Table 1 Mistral-7B multi-seed行间关系不直观\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [1]\n      note: \"R1-M2: s123/s456/s789与3s(3-seed aggregated)关系需在caption/脚注说明\"\n\n- id: \"R18-M3\"\n  summary: \"56.4%零变量重叠的计算粒度未说明\"\n  category: method\n  severity: minor\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [1]\n      note: \"R1-M3: per-problem? per-dataset? per-constraint pair?\"\n\n- id: \"R18-VL1\"\n  summary: \"Table 1(page 5)数据字号偏小(7-8pt), 符号系统认知负荷高\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: []\n      note: \"R18 视觉审查: gold ICL/bold/†等符号系统需理解多个convention\"\n"
  }
}
```

</details>

---


### Tool result

_source line 1879 · 2026-05-23T10:27:44.216984+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml\", \"bytes\": 30533}, \"error\": \"\"}"}

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

_source line 1880 · 2026-05-23T10:30:30.204793+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 18 (Fresh)\n\n**论文**: Beyond Self-Consistency: Self-Extracted Constraints Do Not Improve LLM Logical Reasoning\n**Venue**: EMNLP 2026 via ARR | **Deadline**: 2026-05-25\n**Reviewer 编排**: R1（方法严谨性 + 实验设计）, R2（新颖性 + 完整性 + 写作质量）\n**交叉分享**: 完成，关键问题高度收敛\n\n---\n\n## Summary\n\n论文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM 推理 trace 中提取逻辑约束并通过 MAX-SAT 选择答案。核心发现为负面结果：自提取约束因 \"symbolic confirmation bias\"（SCB）系统性对齐模型多数票答案，使 SICA 退化为多数投票。论文在 6 个开源模型 (7B–32B) + 5 个 frontier 模型、3 个核心数据集、27 种 training-free 修复策略上验证了这一现象，提供了理论分析（Proposition 1, Remark 1）和诊断框架（C₀, K_eff, BR），并展示 cross-architecture verification 作为初步 escape path。\n\n---\n\n## Strengths\n\n**S1. 实验覆盖度和系统性极高 [R1, R2 共识]。** 6 个开源模型 + 5 个 frontier 模型的 cross-model extraction，3 个核心 + 3 个辅助数据集，27 种修复策略的系统排除，multi-seed replication (3-seed/4-seed)，oracle control 验证 MAX-SAT 机制 soundness (+29.90pp FOLIO, +17.17pp PW)。这种覆盖度在 negative-result 论文中极为罕见。\n\n**S2. 统计方法论严谨 [R1, R2 共识]。** McNemar exact test + BH correction (m=16)、TOST equivalence test (±1/±2/±3pp sensitivity analysis)、bootstrap CI (10,000 resamples)、permutation null model (1,000 permutations)。论文坦诚报告 10/16 conditions underpowered，透明度值得肯定。\n\n**S3. 诊断框架有实用价值 [R1, R2 共识]。** 三个 zero-cost diagnostics (C₀, K_eff, BR) 在全部 60 个测试条件上正确表征失败模式，并在两个 held-out model families (LLaMA-3.1-8B, Qwen3-14B) 上前瞻性验证。可直接被从业者采用。\n\n**S4. Oracle control 设计精良 [R1]。** Gold annotations 替代自提取约束，干净分离 \"MAX-SAT 机制是否 sound\" 和 \"自提取约束是否有效\" 两个问题。\n\n**S5. Permutation null model 验证 BR [R1]。** BR_null ≈ BR_obs (p > 0.7) 证实 bias ratio 由 trace-count base rate 解释——反而加强了论文核心论点（bias 是结构性的）。\n\n**S6. Related Work 覆盖全面 [R2]。** 结构清晰的分类（specification-generation / program-generation / trace-extraction），与 Huang et al. (2024) 和 Wan et al. (2025) 的区分在概念上成立。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [critical, R1+R2 共识] 标题 \"Do Not Improve\" 与统计证据不匹配**\n标题是全称否定命题，但 10/16 条件 underpowered（MDE 1.86–4.84pp, observed power < 21%），仅 4 条件通过 TOST 等价检验。论文自身承认 \"Absence of evidence is not evidence of absence for small effects\"（§4），与标题矛盾。Abstract 中 \"find no evidence\" 更审慎但标题未反映。R1 建议 \"Provide No Detectable Improvement\"，R2 建议 \"Show No Evidence of Improving\"——两种表述均优于现标题。\n\n**W2 [critical, R1 提出 + R2 共识] Proposition 1 形式化不严谨**\n假设 (i) 使用 |C^∖| ≈ 0 而非精确条件；假设 (iii) \"approximately uniform constraint yield\" 无数学定义（CV < δ?）且未直接验证（论文给出 extraction rate 但未展示每 trace 约束数量分布）；证明全程使用 ≈ 而非 =。结论通过 >90% 经验一致性支撑而非严格推导。作为论文理论核心支柱，应降格为 Empirical Observation 或给出误差界。R2 补充：配合 Remark 1 的 DPI 论证，即使降格核心论点仍成立。\n\n**W3 [critical, R2 提出 + R1 部分共识] SCB 相对于 Huang et al. (2024) 增量新颖性论证不足**\n论文定位为 \"independent evidence consistent with\" Huang et al.——风险是降级为 case study。§2 对 CoT bias（trace level）和 SCB（aggregation level）的区分是概念性的，缺少实证证据证明两者可分离（如控制 trace faithfulness 后 SCB 是否仍存在）。R1 指出论文实际贡献超出 case study（形式化、诊断框架、27 变体排除），但 \"consistent with\" 措辞自我降级，应改为 \"extends\"。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W4 [major, R1 提出 + R2 共识] Remark 1 (DPI) 与 Figure 3 间存在 claim 升级**\nI(C;Y) ≤ I(T;Y) 对任何确定性后处理 C = f(T) 成立，接近 trivial。真正有价值的 claim 是 Figure 3 DAG 中隐含的 C ⊥ Y | A——约束在给定答案后不携带关于真值的额外信息——但这个更强的条件独立性声明未被形式化证明。R2 补充：需在 Proposition 1 条件下显式证明 I(C;Y) ≤ I(A;Y)，将 trivial DPI 和 non-trivial C ⊥ Y | A 明确区分。\n\n**W5 [major, R1 提出 + R2 共识] BR 指标的 by-construction 循环性**\nSource-attribution scoring 下，多数 trace 产生 a_M → 多数约束 support a_M → BR > 1 几乎 tautological。Permutation test (BR_null ≈ BR_obs, p > 0.7) 证实 BR 完全由 trace-count base rate 解释。56.4% 零变量重叠使约束无法跨答案判别。R2 洞察：BR_excess ≈ 0 意味着 SCB 的 \"bias\" 完全来自结构性 source-attribution——这反而强化 Proposition 1 的 degeneration 论点，但需将 BR 从 \"bias 度量\" 重新框定为 \"degeneration 度量\"。建议报告 BR_excess = BR_obs - BR_null。\n\n**W6 [major, R1+R2 共识] Cross-architecture escape (§6) 证据过弱**\n(a) Spearman ρ=1.0 基于 n=6，Table 3 中 3 个 generator 的 Δ 在 0.50–0.83pp 几乎无差异，monotonicity 由 Mistral-7B 单个 outlier 驱动——实质是二元判断（generator 低于/高于 verifier）而非连续 pattern。\n(b) Zero-shot DeBERTa 仅在最弱 generator (Mistral-7B, SC=39.33%) 上显著；domain-adapted verifier 引入 training 与论文 training-free 主线矛盾，混淆了 independence 和 supervision 两个因素。\n(c) 仅 ProofWriter 一个数据集。\n作为三个 contribution 之一，evidence base 不足。建议降级为 preliminary finding。\n\n**W7 [major, R2 提出 + R1 共识] Scope 震荡**\n标题说通用（\"Self-Extracted Constraints Do Not Improve LLM Logical Reasoning\"）；Contribution 1 说 SICA-specific（\"Z3 verification becomes vacuous under self-extraction\"）；Discussion 扩展到 \"any self-verification method\"。Proposition 1 假设是 SICA 设计选择（degeneration, source-attribution, uniform yield），非所有 self-extraction pipeline 共性。Remark 1 的 DPI bound 更通用但接近 trivial。需在 §1/§5/§7 明确区分 SICA-specific 结论（Proposition 1）和一般性结论（Remark 1）。\n\n**W8 [moderate, R2 提出 + R1 AGREE 降级] \"LLM Logical Reasoning\" 标题范围与实验覆盖不匹配**\n实际测试包含 FOLIO/PW（FOL）、LogiQA（NL 逻辑）、StrategyQA（常识）、GSM8K/AIME（数学），但 GSM8K/AIME 在 degenerate regime (C₀ < 5%)，StrategyQA 仅一个模型。核心有效测试集中在 FOLIO 和 ProofWriter。R1 认为严重性低于 major——核心机制不依赖推理类型。建议标题去掉 \"Logical\"。\n\n**W9 [moderate, R2 提出 + R1 共识] K_eff 缺少直觉解释**\nEq. 1 后应加一句 \"K_eff measures how many effectively independent votes K correlated traces contribute\"。Abstract 中 K_eff 首次出现时也需括号解释（如 \"effective independent sample count\"）。修改成本极低。\n\n**W10 [moderate, R1 提出, R2 部分 REBUT] TOST ±2pp margin 选择依据**\nR1 认为 FOLIO 近二分类，1pp/class 阈值不适用。R2 REBUT：FOLIO 实为三分类 (True/False/Unknown)，±2pp ≈ ±0.67pp/class 在三分类上合理。共识：需在 §4 区分二分类 (ProofWriter) 和三分类 (FOLIO) 数据集的 margin 适用性。\n\n### Nice-to-Have\n\n- **M1 [minor, R2 提出, R1 REBUT]** Abstract 信息密度高但 R1 认为适合 ACL/EMNLP venue。共识：在 Abstract 中给 K_eff 加括号解释即可。\n- **M2 [minor, R1]** Table 1 中 Mistral-7B multi-seed 行间关系需在 caption/脚注说明（s123/s456/s789 vs. 3s aggregated）。\n- **M3 [minor, R1]** 56.4% 零变量重叠的计算粒度需说明（per-problem? per-dataset?）。\n- **M4 [minor, R1+R2]** Appendix Y (Extended Discussion) 中 SCB evaluation framework 内容有价值但缺乏主文指引。\n- **M5 [minor, R2 提出, R1 REBUT]** \"Symbolic Mirage\" 作为 Section 标题——R2 认为稍 dramatic，R1 REBUT 认为准确且 ACL 常见。保留。\n- **M6 [minor, R2 提出, R1 REBUT]** Limitations 仅约 50 词——R2 认为偏短，R1 认为符合 EMNLP 规则（3 点即可）。R1 判断合规。\n- **M7 [minor, R1]** Z3 3.4% rejection rate 应在 Method/Results 开头更早指出 vacuous verification。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 独立达成 [AGREE] 共识：\n\n1. **标题 overclaiming** [W1]：最高优先级修改项。\"Do Not Improve\" → \"Provide No Detectable Improvement\" 或类似表述。\n2. **Proposition 1 形式化不足** [W2]：降格为 Empirical Observation 或补充误差界。\n3. **Cross-architecture escape 证据不足** [W6]：降级为 preliminary finding，n=6 的 Spearman ρ=1.0 是 outlier-driven。\n4. **BR 循环性** [W5]：重新框定为 degeneration 度量，报告 BR_excess。\n5. **Remark 1 trivial + claim 升级** [W4]：区分 DPI bound (trivial) 和 C ⊥ Y | A (non-trivial but unproven)。\n6. **SCB 新颖性论证** [W3]：避免 \"consistent with\" 自我降级，明确独立贡献。\n7. **Scope 震荡** [W7]：区分 SICA-specific 和 general 结论。\n8. **K_eff 直觉解释** [W9]：加一句自然语言解释。\n\n## Reviewer Divergence\n\n仅在以下 minor 问题上存在轻微分歧，不影响评分：\n\n1. **TOST margin** [W10]：R1 认为 FOLIO 不适用 ±2pp；R2 REBUT 称三分类合理。共识：区分数据集类型。\n2. **Abstract 密度** [M1]：R2 认为过载；R1 认为适合 venue。共识：加 K_eff 括号解释。\n3. **\"Symbolic Mirage\" 标题** [M5]：R2 建议更中性；R1 认为 metaphor 准确。保留。\n4. **Limitations 长度** [M6]：R2 认为偏短；R1 认为合规。不修改。\n\n---\n\n## Questions for Authors\n\n**Q1.** [R1] Proposition 1 假设 (iii) \"approximately uniform constraint yield\"：能否提供每 trace 约束数量分布（均值、标准差、CV）？CV 大时 Proposition 1 结论的误差有多大？\n\n**Q2.** [R1] 56.4% 零变量重叠 vs 43.6% 有重叠：有重叠子集的 Z3 拒绝率和 SICA 表现是否不同？\n\n**Q3.** [R1] Capability-gap pattern 仅在 ProofWriter 验证。FOLIO 上用 DeBERTa-NLI 做 cross-architecture verification 的结果如何？\n\n**Q4.** [R1] 27 种修复策略中是否尝试过 prompt 层面打破 source-attribution（如要求提取与答案无关的结构性约束）？\n\n**Q5.** [R1] α 的 ≥99% insensitivity 意味着 α 作为设计参数是多余的。为什么不默认 α=0？\n\n**Q6.** [R2] §2 区分 trace-level bias (CoT) 和 aggregation-level bias (SCB) 是概念性的——是否可设计实验控制 trace faithfulness 后测试 SCB 是否独立存在？\n\n---\n\n## Missing References\n\n论文引用覆盖度已较全面。建议补充：\n- Xie et al. (2023) Self-Evaluation Guided Beam Search [R2 提出, R1 AGREE]\n- 检查 LATS (Zhou et al.) 引用年份一致性 [R2]\n- Lightman et al. (2024) \"Let's Verify Step by Step\" 在 process-level verification 方面的方法论对比可更详细 [R1]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 项目未配置外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成** (耗时约 4 分钟)\n\n| 严重性 | 数量 |\n|--------|------|\n| Critical | 0 |\n| Warning | 1 |\n| Info | 12 |\n\n**Warning findings:**\n- Page 5, Table 1（主结果表）：数据字号偏小（约 7-8pt），gold ICL / bold / † 等符号系统认知负荷高。\n\n**Info findings 摘要:**\n- Page 1：首页无视觉锚点（纯文本），但 Figure 1 在 page 2 顶部，3 页窗口内可接受。\n- Page 4, Figure 2：marker 和 legend 字号偏小，灰度打印时区分度依赖 marker shape。\n- Page 7, Figure 4：策略名称文字 ≤6pt，打印后可能难以辨认。建议增大字号或 caption 中列出关键策略名。\n- Page 7, Figure 3 (Causal DAG)：图小但简洁（5 节点），可读性尚可。\n- Page 8, Limitations：约 6 行，覆盖 3 点，符合 EMNLP 要求，仅一个 Limitations section ✓。\n- Appendix：Algorithm 1-2 格式规范；page 14 含 3 表密度极高但附录可接受；Figure 5-8 清晰可读。\n\n**格式合规检查 ✓:**\n- ACL template (`\\usepackage[review]{acl}`) ✓\n- Double-blind (Author: Anonymous) ✓\n- 正文 ≤ 8 页 ✓\n- Limitations 在正文且仅一处 ✓\n- 参考文献无页数限制 ✓\n\n---\n\n## Overall Assessment\n\n**评分：3.5 / 5 (Borderline Conference)**\n**两位 Reviewer 一致评分：3.5，置信度 4/5**\n\n**EMNLP 2026 ARR 对应：3.5 = Borderline Conference**\n\n这是一篇执行质量很高的负面结果论文。实验覆盖度在同类工作中罕见（9 模型 / 7 数据集 / 27 变体 / multi-seed / oracle control），统计方法论远超领域平均水准。诊断框架 (C₀, K_eff, BR) 有直接实用价值。\n\n降低评分的核心因素：\n1. **标题 overclaiming**（全称否定 vs. 10/16 underpowered）是 soundness 层面瑕疵，两位 Reviewer 独立共识。\n2. **理论贡献偏薄**——Proposition 1 形式化不够严谨（假设未定义、证明用 ≈），Remark 1 的 DPI bound 接近 trivial，两者间存在 claim 升级。\n3. **SCB 新颖性论证不足**——\"consistent with Huang et al.\" 定位有自我降级风险。\n4. **Cross-architecture escape** 作为三个 contribution 之一，evidence base 不足（n=6, outlier-driven, 单数据集）。\n\n**修改路径（可达 4.0 Conference）：**\n- 标题修正为 \"Provide No Detectable Improvement\" 或类似\n- Proposition 1 降格为 Empirical Observation 或补充误差界\n- 明确 SCB 独立于 Huang et al. 的贡献（形式化 + 诊断框架 + 27 变体排除）\n- Cross-architecture escape 降级为 preliminary finding\n- BR 重新框定为 degeneration 度量\n- K_eff 加直觉解释\n- §1/§5/§7 明确 scope boundary\n\n**当前状态：Borderline Conference，Findings 是更稳妥的归宿。修正后可达 Conference 水平。**\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 信息密度高但可接受。K_eff 需括号解释。BR range 1.66–4.97× 报告完整。\"find no evidence\" 措辞比标题更准确。\n\n### §1 Introduction\n- 三个 contribution 定位清晰但 scope 需精确化。C1 的 \"provably sound Z3 verification becomes vacuous\" 是 SICA-specific，不应暗示通用。C3 cross-architecture escape 应标注 \"preliminary\"。\n\n### §2 Related Work\n- 覆盖全面，分类（specification-generation / program-generation / trace-extraction）准确。\"Distinction from CoT confirmation bias\" 段概念上成立但需实证支持。建议补 Xie et al. (2023)。\n\n### §3 Method\n- SICA pipeline 描述完整。Eq. 1 (K_eff) 缺直觉解释。Eq. 5 (BR) 定义处应说明 lower bound 为 1 是 by construction。α=0.5 选择缺少讨论（Q5）。\n\n### §4 Results\n- Table 1 全面但字号偏小。Multi-seed 行间关系需说明。应标注 powered/underpowered conditions。TOST margin 需区分二/三分类数据集。\n\n### §5 The Symbolic Mirage\n- Proposition 1：形式化不足，需降格或加强。Remark 1：trivial DPI，需与 Figure 3 的 C ⊥ Y | A 显式连接。BR 讨论：permutation test 结果实际上加强了 degeneration 论点但 framing 需调整。27 变体排除系统但 scope boundary 需声明。\n\n### §6 Escaping the Bottleneck\n- n=6 证据不足。Capability-gap 描述应从 \"structural property\" 降为 \"preliminary observation\"。Domain-adapted verifier 与 training-free 主线存在张力。\n\n### §7 Discussion and Conclusion\n- 过于简短。\"consistent with Huang et al.\" 措辞自我降级。Scope 从 SICA 扩展到 \"any self-verification method\" 缺乏论证。\n\n### Limitations\n- 简短但合规（3 点：模型规模、英文、统计功效）。\n\n### Appendix\n- 体量大（16 页）但信息丰富。关键内容（power analysis, oracle control, SCB evaluation framework）需主文指引。",
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
    "report": "# 审稿报告 — Round 18 (Fresh)\n\n**论文**: Beyond Self-Consistency: Self-Extracted Constraints Do Not Improve LLM Logical Reasoning\n**Venue**: EMNLP 2026 via ARR | **Deadline**: 2026-05-25\n**Reviewer 编排**: R1（方法严谨性 + 实验设计）, R2（新颖性 + 完整性 + 写作质量）\n**交叉分享**: 完成，关键问题高度收敛\n\n---\n\n## Summary\n\n论文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM 推理 trace 中提取逻辑约束并通过 MAX-SAT 选择答案。核心发现为负面结果：自提取约束因 \"symbolic confirmation bias\"（SCB）系统性对齐模型多数票答案，使 SICA 退化为多数投票。论文在 6 个开源模型 (7B–32B) + 5 个 frontier 模型、3 个核心数据集、27 种 training-free 修复策略上验证了这一现象，提供了理论分析（Proposition 1, Remark 1）和诊断框架（C₀, K_eff, BR），并展示 cross-architecture verification 作为初步 escape path。\n\n---\n\n## Strengths\n\n**S1. 实验覆盖度和系统性极高 [R1, R2 共识]。** 6 个开源模型 + 5 个 frontier 模型的 cross-model extraction，3 个核心 + 3 个辅助数据集，27 种修复策略的系统排除，multi-seed replication (3-seed/4-seed)，oracle control 验证 MAX-SAT 机制 soundness (+29.90pp FOLIO, +17.17pp PW)。这种覆盖度在 negative-result 论文中极为罕见。\n\n**S2. 统计方法论严谨 [R1, R2 共识]。** McNemar exact test + BH correction (m=16)、TOST equivalence test (±1/±2/±3pp sensitivity analysis)、bootstrap CI (10,000 resamples)、permutation null model (1,000 permutations)。论文坦诚报告 10/16 conditions underpowered，透明度值得肯定。\n\n**S3. 诊断框架有实用价值 [R1, R2 共识]。** 三个 zero-cost diagnostics (C₀, K_eff, BR) 在全部 60 个测试条件上正确表征失败模式，并在两个 held-out model families (LLaMA-3.1-8B, Qwen3-14B) 上前瞻性验证。可直接被从业者采用。\n\n**S4. Oracle control 设计精良 [R1]。** Gold annotations 替代自提取约束，干净分离 \"MAX-SAT 机制是否 sound\" 和 \"自提取约束是否有效\" 两个问题。\n\n**S5. Permutation null model 验证 BR [R1]。** BR_null ≈ BR_obs (p > 0.7) 证实 bias ratio 由 trace-count base rate 解释——反而加强了论文核心论点（bias 是结构性的）。\n\n**S6. Related Work 覆盖全面 [R2]。** 结构清晰的分类（specification-generation / program-generation / trace-extraction），与 Huang et al. (2024) 和 Wan et al. (2025) 的区分在概念上成立。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [critical, R1+R2 共识] 标题 \"Do Not Improve\" 与统计证据不匹配**\n标题是全称否定命题，但 10/16 条件 underpowered（MDE 1.86–4.84pp, observed power < 21%），仅 4 条件通过 TOST 等价检验。论文自身承认 \"Absence of evidence is not evidence of absence for small effects\"（§4），与标题矛盾。Abstract 中 \"find no evidence\" 更审慎但标题未反映。R1 建议 \"Provide No Detectable Improvement\"，R2 建议 \"Show No Evidence of Improving\"——两种表述均优于现标题。\n\n**W2 [critical, R1 提出 + R2 共识] Proposition 1 形式化不严谨**\n假设 (i) 使用 |C^∖| ≈ 0 而非精确条件；假设 (iii) \"approximately uniform constraint yield\" 无数学定义（CV < δ?）且未直接验证（论文给出 extraction rate 但未展示每 trace 约束数量分布）；证明全程使用 ≈ 而非 =。结论通过 >90% 经验一致性支撑而非严格推导。作为论文理论核心支柱，应降格为 Empirical Observation 或给出误差界。R2 补充：配合 Remark 1 的 DPI 论证，即使降格核心论点仍成立。\n\n**W3 [critical, R2 提出 + R1 部分共识] SCB 相对于 Huang et al. (2024) 增量新颖性论证不足**\n论文定位为 \"independent evidence consistent with\" Huang et al.——风险是降级为 case study。§2 对 CoT bias（trace level）和 SCB（aggregation level）的区分是概念性的，缺少实证证据证明两者可分离（如控制 trace faithfulness 后 SCB 是否仍存在）。R1 指出论文实际贡献超出 case study（形式化、诊断框架、27 变体排除），但 \"consistent with\" 措辞自我降级，应改为 \"extends\"。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W4 [major, R1 提出 + R2 共识] Remark 1 (DPI) 与 Figure 3 间存在 claim 升级**\nI(C;Y) ≤ I(T;Y) 对任何确定性后处理 C = f(T) 成立，接近 trivial。真正有价值的 claim 是 Figure 3 DAG 中隐含的 C ⊥ Y | A——约束在给定答案后不携带关于真值的额外信息——但这个更强的条件独立性声明未被形式化证明。R2 补充：需在 Proposition 1 条件下显式证明 I(C;Y) ≤ I(A;Y)，将 trivial DPI 和 non-trivial C ⊥ Y | A 明确区分。\n\n**W5 [major, R1 提出 + R2 共识] BR 指标的 by-construction 循环性**\nSource-attribution scoring 下，多数 trace 产生 a_M → 多数约束 support a_M → BR > 1 几乎 tautological。Permutation test (BR_null ≈ BR_obs, p > 0.7) 证实 BR 完全由 trace-count base rate 解释。56.4% 零变量重叠使约束无法跨答案判别。R2 洞察：BR_excess ≈ 0 意味着 SCB 的 \"bias\" 完全来自结构性 source-attribution——这反而强化 Proposition 1 的 degeneration 论点，但需将 BR 从 \"bias 度量\" 重新框定为 \"degeneration 度量\"。建议报告 BR_excess = BR_obs - BR_null。\n\n**W6 [major, R1+R2 共识] Cross-architecture escape (§6) 证据过弱**\n(a) Spearman ρ=1.0 基于 n=6，Table 3 中 3 个 generator 的 Δ 在 0.50–0.83pp 几乎无差异，monotonicity 由 Mistral-7B 单个 outlier 驱动——实质是二元判断（generator 低于/高于 verifier）而非连续 pattern。\n(b) Zero-shot DeBERTa 仅在最弱 generator (Mistral-7B, SC=39.33%) 上显著；domain-adapted verifier 引入 training 与论文 training-free 主线矛盾，混淆了 independence 和 supervision 两个因素。\n(c) 仅 ProofWriter 一个数据集。\n作为三个 contribution 之一，evidence base 不足。建议降级为 preliminary finding。\n\n**W7 [major, R2 提出 + R1 共识] Scope 震荡**\n标题说通用（\"Self-Extracted Constraints Do Not Improve LLM Logical Reasoning\"）；Contribution 1 说 SICA-specific（\"Z3 verification becomes vacuous under self-extraction\"）；Discussion 扩展到 \"any self-verification method\"。Proposition 1 假设是 SICA 设计选择（degeneration, source-attribution, uniform yield），非所有 self-extraction pipeline 共性。Remark 1 的 DPI bound 更通用但接近 trivial。需在 §1/§5/§7 明确区分 SICA-specific 结论（Proposition 1）和一般性结论（Remark 1）。\n\n**W8 [moderate, R2 提出 + R1 AGREE 降级] \"LLM Logical Reasoning\" 标题范围与实验覆盖不匹配**\n实际测试包含 FOLIO/PW（FOL）、LogiQA（NL 逻辑）、StrategyQA（常识）、GSM8K/AIME（数学），但 GSM8K/AIME 在 degenerate regime (C₀ < 5%)，StrategyQA 仅一个模型。核心有效测试集中在 FOLIO 和 ProofWriter。R1 认为严重性低于 major——核心机制不依赖推理类型。建议标题去掉 \"Logical\"。\n\n**W9 [moderate, R2 提出 + R1 共识] K_eff 缺少直觉解释**\nEq. 1 后应加一句 \"K_eff measures how many effectively independent votes K correlated traces contribute\"。Abstract 中 K_eff 首次出现时也需括号解释（如 \"effective independent sample count\"）。修改成本极低。\n\n**W10 [moderate, R1 提出, R2 部分 REBUT] TOST ±2pp margin 选择依据**\nR1 认为 FOLIO 近二分类，1pp/class 阈值不适用。R2 REBUT：FOLIO 实为三分类 (True/False/Unknown)，±2pp ≈ ±0.67pp/class 在三分类上合理。共识：需在 §4 区分二分类 (ProofWriter) 和三分类 (FOLIO) 数据集的 margin 适用性。\n\n### Nice-to-Have\n\n- **M1 [minor, R2 提出, R1 REBUT]** Abstract 信息密度高但 R1 认为适合 ACL/EMNLP venue。共识：在 Abstract 中给 K_eff 加括号解释即可。\n- **M2 [minor, R1]** Table 1 中 Mistral-7B multi-seed 行间关系需在 caption/脚注说明（s123/s456/s789 vs. 3s aggregated）。\n- **M3 [minor, R1]** 56.4% 零变量重叠的计算粒度需说明（per-problem? per-dataset?）。\n- **M4 [minor, R1+R2]** Appendix Y (Extended Discussion) 中 SCB evaluation framework 内容有价值但缺乏主文指引。\n- **M5 [minor, R2 提出, R1 REBUT]** \"Symbolic Mirage\" 作为 Section 标题——R2 认为稍 dramatic，R1 REBUT 认为准确且 ACL 常见。保留。\n- **M6 [minor, R2 提出, R1 REBUT]** Limitations 仅约 50 词——R2 认为偏短，R1 认为符合 EMNLP 规则（3 点即可）。R1 判断合规。\n- **M7 [minor, R1]** Z3 3.4% rejection rate 应在 Method/Results 开头更早指出 vacuous verification。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 独立达成 [AGREE] 共识：\n\n1. **标题 overclaiming** [W1]：最高优先级修改项。\"Do Not Improve\" → \"Provide No Detectable Improvement\" 或类似表述。\n2. **Proposition 1 形式化不足** [W2]：降格为 Empirical Observation 或补充误差界。\n3. **Cross-architecture escape 证据不足** [W6]：降级为 preliminary finding，n=6 的 Spearman ρ=1.0 是 outlier-driven。\n4. **BR 循环性** [W5]：重新框定为 degeneration 度量，报告 BR_excess。\n5. **Remark 1 trivial + claim 升级** [W4]：区分 DPI bound (trivial) 和 C ⊥ Y | A (non-trivial but unproven)。\n6. **SCB 新颖性论证** [W3]：避免 \"consistent with\" 自我降级，明确独立贡献。\n7. **Scope 震荡** [W7]：区分 SICA-specific 和 general 结论。\n8. **K_eff 直觉解释** [W9]：加一句自然语言解释。\n\n## Reviewer Divergence\n\n仅在以下 minor 问题上存在轻微分歧，不影响评分：\n\n1. **TOST margin** [W10]：R1 认为 FOLIO 不适用 ±2pp；R2 REBUT 称三分类合理。共识：区分数据集类型。\n2. **Abstract 密度** [M1]：R2 认为过载；R1 认为适合 venue。共识：加 K_eff 括号解释。\n3. **\"Symbolic Mirage\" 标题** [M5]：R2 建议更中性；R1 认为 metaphor 准确。保留。\n4. **Limitations 长度** [M6]：R2 认为偏短；R1 认为合规。不修改。\n\n---\n\n## Questions for Authors\n\n**Q1.** [R1] Proposition 1 假设 (iii) \"approximately uniform constraint yield\"：能否提供每 trace 约束数量分布（均值、标准差、CV）？CV 大时 Proposition 1 结论的误差有多大？\n\n**Q2.** [R1] 56.4% 零变量重叠 vs 43.6% 有重叠：有重叠子集的 Z3 拒绝率和 SICA 表现是否不同？\n\n**Q3.** [R1] Capability-gap pattern 仅在 ProofWriter 验证。FOLIO 上用 DeBERTa-NLI 做 cross-architecture verification 的结果如何？\n\n**Q4.** [R1] 27 种修复策略中是否尝试过 prompt 层面打破 source-attribution（如要求提取与答案无关的结构性约束）？\n\n**Q5.** [R1] α 的 ≥99% insensitivity 意味着 α 作为设计参数是多余的。为什么不默认 α=0？\n\n**Q6.** [R2] §2 区分 trace-level bias (CoT) 和 aggregation-level bias (SCB) 是概念性的——是否可设计实验控制 trace faithfulness 后测试 SCB 是否独立存在？\n\n---\n\n## Missing References\n\n论文引用覆盖度已较全面。建议补充：\n- Xie et al. (2023) Self-Evaluation Guided Beam Search [R2 提出, R1 AGREE]\n- 检查 LATS (Zhou et al.) 引用年份一致性 [R2]\n- Lightman et al. (2024) \"Let's Verify Step by Step\" 在 process-level verification 方面的方法论对比可更详细 [R1]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求。** 项目未配置外部审稿。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成** (耗时约 4 分钟)\n\n| 严重性 | 数量 |\n|--------|------|\n| Critical | 0 |\n| Warning | 1 |\n| Info | 12 |\n\n**Warning findings:**\n- Page 5, Table 1（主结果表）：数据字号偏小（约 7-8pt），gold ICL / bold / † 等符号系统认知负荷高。\n\n**Info findings 摘要:**\n- Page 1：首页无视觉锚点（纯文本），但 Figure 1 在 page 2 顶部，3 页窗口内可接受。\n- Page 4, Figure 2：marker 和 legend 字号偏小，灰度打印时区分度依赖 marker shape。\n- Page 7, Figure 4：策略名称文字 ≤6pt，打印后可能难以辨认。建议增大字号或 caption 中列出关键策略名。\n- Page 7, Figure 3 (Causal DAG)：图小但简洁（5 节点），可读性尚可。\n- Page 8, Limitations：约 6 行，覆盖 3 点，符合 EMNLP 要求，仅一个 Limitations section ✓。\n- Appendix：Algorithm 1-2 格式规范；page 14 含 3 表密度极高但附录可接受；Figure 5-8 清晰可读。\n\n**格式合规检查 ✓:**\n- ACL template (`\\usepackage[review]{acl}`) ✓\n- Double-blind (Author: Anonymous) ✓\n- 正文 ≤ 8 页 ✓\n- Limitations 在正文且仅一处 ✓\n- 参考文献无页数限制 ✓\n\n---\n\n## Overall Assessment\n\n**评分：3.5 / 5 (Borderline Conference)**\n**两位 Reviewer 一致评分：3.5，置信度 4/5**\n\n**EMNLP 2026 ARR 对应：3.5 = Borderline Conference**\n\n这是一篇执行质量很高的负面结果论文。实验覆盖度在同类工作中罕见（9 模型 / 7 数据集 / 27 变体 / multi-seed / oracle control），统计方法论远超领域平均水准。诊断框架 (C₀, K_eff, BR) 有直接实用价值。\n\n降低评分的核心因素：\n1. **标题 overclaiming**（全称否定 vs. 10/16 underpowered）是 soundness 层面瑕疵，两位 Reviewer 独立共识。\n2. **理论贡献偏薄**——Proposition 1 形式化不够严谨（假设未定义、证明用 ≈），Remark 1 的 DPI bound 接近 trivial，两者间存在 claim 升级。\n3. **SCB 新颖性论证不足**——\"consistent with Huang et al.\" 定位有自我降级风险。\n4. **Cross-architecture escape** 作为三个 contribution 之一，evidence base 不足（n=6, outlier-driven, 单数据集）。\n\n**修改路径（可达 4.0 Conference）：**\n- 标题修正为 \"Provide No Detectable Improvement\" 或类似\n- Proposition 1 降格为 Empirical Observation 或补充误差界\n- 明确 SCB 独立于 Huang et al. 的贡献（形式化 + 诊断框架 + 27 变体排除）\n- Cross-architecture escape 降级为 preliminary finding\n- BR 重新框定为 degeneration 度量\n- K_eff 加直觉解释\n- §1/§5/§7 明确 scope boundary\n\n**当前状态：Borderline Conference，Findings 是更稳妥的归宿。修正后可达 Conference 水平。**\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 信息密度高但可接受。K_eff 需括号解释。BR range 1.66–4.97× 报告完整。\"find no evidence\" 措辞比标题更准确。\n\n### §1 Introduction\n- 三个 contribution 定位清晰但 scope 需精确化。C1 的 \"provably sound Z3 verification becomes vacuous\" 是 SICA-specific，不应暗示通用。C3 cross-architecture escape 应标注 \"preliminary\"。\n\n### §2 Related Work\n- 覆盖全面，分类（specification-generation / program-generation / trace-extraction）准确。\"Distinction from CoT confirmation bias\" 段概念上成立但需实证支持。建议补 Xie et al. (2023)。\n\n### §3 Method\n- SICA pipeline 描述完整。Eq. 1 (K_eff) 缺直觉解释。Eq. 5 (BR) 定义处应说明 lower bound 为 1 是 by construction。α=0.5 选择缺少讨论（Q5）。\n\n### §4 Results\n- Table 1 全面但字号偏小。Multi-seed 行间关系需说明。应标注 powered/underpowered conditions。TOST margin 需区分二/三分类数据集。\n\n### §5 The Symbolic Mirage\n- Proposition 1：形式化不足，需降格或加强。Remark 1：trivial DPI，需与 Figure 3 的 C ⊥ Y | A 显式连接。BR 讨论：permutation test 结果实际上加强了 degeneration 论点但 framing 需调整。27 变体排除系统但 scope boundary 需声明。\n\n### §6 Escaping the Bottleneck\n- n=6 证据不足。Capability-gap 描述应从 \"structural property\" 降为 \"preliminary observation\"。Domain-adapted verifier 与 training-free 主线存在张力。\n\n### §7 Discussion and Conclusion\n- 过于简短。\"consistent with Huang et al.\" 措辞自我降级。Scope 从 SICA 扩展到 \"any self-verification method\" 缺乏论证。\n\n### Limitations\n- 简短但合规（3 点：模型规模、英文、统计功效）。\n\n### Appendix\n- 体量大（16 页）但信息丰富。关键内容（power analysis, oracle control, SCB evaluation framework）需主文指引。",
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

_source line 1881 · 2026-05-23T10:30:34.556822+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_970d5ea3f54df81296b97321fcded892:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4352
}
```

</details>

---


### Assistant

_source line 1882 · 2026-05-23T10:30:45.782963+00:00_

Round 18 审稿完成。

**最终评分：3.5 / 5 (Borderline Conference)**，两位 Reviewer 一致，置信度 4/5。

**核心共识问题**（优先级排序）：
1. 标题 "Do Not Improve" overclaiming → 改为 "Provide No Detectable Improvement"
2. Proposition 1 形式化不严谨 → 降格或补误差界
3. SCB vs Huang et al. 新颖性论证不足 → 停止 "consistent with" 自我降级
4. BR 循环性 → 重新框定为 degeneration 度量
5. Cross-architecture escape 证据不足 → 降级为 preliminary finding
6. Scope 震荡 → 明确 SICA-specific vs general 结论边界

**修改后可达 4.0 (Conference)**。当前状态 Findings 更稳妥。

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


## Round 137

## Round 137

2 recorded events


### User

_source line 1883 · 2026-05-23T10:30:48.326452+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 的逐条回应。总结：

- 在 5 个 Must-Fix/Should-Fix 问题上 **AGREE**（标题 overclaiming、Huang et al. 增量新颖性、scope 震荡、标题措辞范围、cross-arch escape 初步性）
- 在 3 个问题上 **REBUT**（abstract 信息过载、"Symbolic Mirage" 标题、Limitations 长度）
- 与 R2 在 Overall 3.5 评分上达成独立共识，同时指出 R2 未覆盖的两个方法论问题（Remark 1 triviality、BR 循环性）

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

_source line 1884 · 2026-05-23T10:30:58.181314+00:00_

审稿报告已投递给 Research Director。

**Round 18（fresh）圆桌审稿完成。**

- **评分**：3.5 / 5 (Borderline Conference)，两位 Reviewer 独立一致
- **最高优先修改**：标题 overclaiming → "Provide No Detectable Improvement"
- **3 个 critical 问题**：标题措辞、Proposition 1 形式化不足、SCB 新颖性论证
- **4 个 major 问题**：Remark 1 claim 升级、BR 循环性重框定、cross-arch 降级为 preliminary、scope 震荡
- **修改后可达 4.0 (Conference)**，当前状态 Findings 更稳妥

Issue Tracker 已同步更新至 `review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 138

## Round 138

78 recorded events


### User

_source line 1885 · 2026-05-23T13:42:41.398168+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: symb_invariant_consensus
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
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

_source line 1886 · 2026-05-23T13:42:46.537085+00:00_

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

_source line 1887 · 2026-05-23T13:42:46.588541+00:00_

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

_source line 1888 · 2026-05-23T13:42:52.310045+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
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
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,read_project_file,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1889 · 2026-05-23T13:42:52.310397+00:00_



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

_source line 1890 · 2026-05-23T13:42:54.819387+00:00_

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
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
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

_source line 1891 · 2026-05-23T13:42:54.819731+00:00_

No matching deferred tools found

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

_source line 1892 · 2026-05-23T13:42:59.637147+00:00_

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
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
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

_source line 1893 · 2026-05-23T13:42:59.687806+00:00_



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

_source line 1894 · 2026-05-23T13:43:05.158488+00:00_

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

_source line 1895 · 2026-05-23T13:43:06.529332+00:00_

{"result":"# 项目 symb_invariant_consensus 概况\n\n## 实验状态 (173 个)\n\n- **sica_k_sensitivity_14b**: DONE (success) — \n- **exp-011-llama8b**: DONE (failed) — \n- **exp-016-weighted-sc**: DONE (success) — \n- **exp-005**: DONE (negative) — \n- **sica_folio30**: DONE (killed) — \n- **sica_d016_c0_precheck**: DONE (success) — \n- **sica_proofwriter30_v2**: DONE (killed) — \n- **sica_proofwriter30**: DONE (failed) — \n- **sica_aime30_v3**: DONE (killed) — \n- **sica_aime30_v2**: DONE (killed) — \n- **sica_aime30_t07**: DONE (killed) — \n- **mvp_math50_t07**: DONE (killed) — \n- **sica_smoke_5q**: DONE (success) — \n- **smoke-test-5q**: PREPARING (failed) — \n- **crd_folio_main**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp-multi-seed-llama-pw-seed789-v2 | LLaMA-3.1-8B PW seed789 多种子复制（westd-30973 cuda:1 全新运行）。替代 16639 cuda:0 上的慢速运行（12/600）。验证 SCB 在 ProofWriter 上跨 seed 稳定性。 | — | — | — |\n| exp-multi-seed-llama-pw-seed456-v2 | LLaMA-3.1-8B PW seed456 多种子复制（westd-30973 cuda:2 全新运行）。验证 SCB 在 ProofWriter 上跨 seed 稳定性（Δ(SICA-SC)≤0）。配合 seed42/123/789 组成 4-seed 覆盖。 | — | — | — |\n| exp-multi-seed-qwen25-pw-seed789-v3 | Qwen2.5-14B PW seed789 多种子复制（westd-30973 cuda:0 全新运行）。替代 v2 在 16639 cuda:2 上的慢速运行（53/600）。验证 SCB 在 ProofWriter 上跨 seed 稳定性。 | — | — | — |\n\n## 待处理\n- exp-multi-seed-llama-pw-seed456: LLaMA-3.1-8B PW seed456 多种子复制。验证 SCB 在 ProofWriter 上跨 seed 稳定性（Δ(SICA-SC)≤0）。配合 seed42/123/789 组成 4-seed 覆盖。（排队等待 GPU）\n- exp-deberta-ft-combo: Fine-tuned DeBERTa-large on ProofWriter OWA depth-5 achieves near-perfect NLI accuracy (99.67%) and provides massive combo gains over SC baseline when used as external verifier, demonstrating that domain-specific NLI fine-tuning breaks the SCB ceiling by providing truly independent verification signal.（准备中）\n- exp-multi-seed-mistral-folio: Multi-seed replication (seeds 123,456,789) of Mistral-7B × FOLIO-20
…[truncated 1733 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1370
}
```

</details>

---


### Tool call

_source line 1896 · 2026-05-23T13:43:06.680255+00:00_

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

_source line 1897 · 2026-05-23T13:43:07.533765+00:00_

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
40	\title{Beyond Self-Consistency: Self-Extracted Constraints\\Provide No Detectable Improvement in LLM Reasoning}
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
72	\enlargethispage{6\baselineskip}
73	\vspace{-1.5mm}
74	\input{discussion}
75	
76	\vspace{-4mm}
77	\section*{Limitations}
78	\input{limitations_content}
79	
80	\bi
…[truncated 85 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 1898 · 2026-05-23T13:43:07.584407+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR call for papers submission guidelines author guidelines site:aclweb.org"
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
    "query": "EMNLP 2026 ARR call for papers submission guidelines author guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1899 · 2026-05-23T13:43:08.136691+00:00_

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

_source line 1900 · 2026-05-23T13:43:08.187412+00:00_

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


### Tool result

_source line 1901 · 2026-05-23T13:43:13.607056+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author guidelines site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"}]

Based on the search results, I found information about EMNLP 2026, but the results primarily cover tutorial calls and workshops rather than the main conference call for papers through ARR. Here's what I found:

## E
…[truncated 1173 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 6022
}
```

</details>

---


### Tool call

_source line 1902 · 2026-05-23T13:43:23.441867+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements aclrollingreview.org"
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
    "query": "ACL Rolling Review 2026 submission guidelines page limit format requirements aclrollingreview.org"
  }
}
```

</details>

---


### Tool call

_source line 1903 · 2026-05-23T13:43:24.646731+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper"
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
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1904 · 2026-05-23T13:43:24.697429+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/limitations_content.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/diagnosis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/solutions.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/related_work.tex

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


### Tool result

_source line 1905 · 2026-05-23T13:43:29.816074+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit format requirements aclrollingreview.org"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/changelog"}]

Based on the search results from ACL Rolling Review's official website, here are the submission guidelines regardin
…[truncated 974 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 6374
}
```

</details>

---


### Tool call

_source line 1906 · 2026-05-23T13:43:33.729767+00:00_

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

_source line 1907 · 2026-05-23T13:43:34.031377+00:00_

1	Can symbolic verification via a provably sound solver improve Large Language Model (LLM) reasoning when constraints are self-extracted from the model's own traces? We find no evidence of improvement. We introduce Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from chain-of-thought traces and selects answers via weighted MAX-SAT. Despite Z3 validating 99\% of self-extracted constraints, SICA produces answers identical to majority voting on over 90\% of problems across six models (7B--32B) and three reasoning domains. No condition shows a significant positive effect after FDR control; four of six powered conditions confirm equivalence within $\pm$2\,pp (TOST), though ten conditions remain underpowered for effects below ${\sim}$2\,pp. We systematically diagnose the failure as \emph{symbolic confirmation bias}: self-extracted constraints track the model's majority answer (bias ratios $1.66$--$4.97\times$ across nine models, 7B to frontier). We identify the structural mechanism---under source-attribution scoring and empirical degeneration, SICA reduces to majority vote (Observation~1)---and the $M{\to}T{\to}A{\to}C$ Markov chain that bounds self-extracted information (Remark~1), advancing beyond \citet{huang2024selfcorrect}'s findings to formal self-verification. Twenty-seven training-free variants within the constraint-extraction paradigm fail due to a persistent independence-accuracy trade-off. Preliminary cross-architecture verification escapes the bias ($+6.67$\,pp on the weakest generator, $p < 0.001$). Three zero-cost diagnostics characterize failure modes across all 60 tested conditions within this paradigm.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1908 · 2026-05-23T13:43:34.031745+00:00_

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

_source line 1909 · 2026-05-23T13:43:34.479840+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	\looseness=-1
4	Self-Consistency (SC) \citep{wang2023sc} selects the majority answer across $K$ chain-of-thought traces, a strategy grounded in the Condorcet Jury Theorem: independent voters converge to truth \citep{condorcet1785, ladha1992correlated}. In practice, SC's gains plateau for strong models \citep{loo2025reevaluating}, pointing to correlated traces that reduce the effective ensemble size. A natural remedy is to move beyond simple vote-counting: extract logical constraints from the traces and let a provably sound solver adjudicate. If the solver can filter contradictions and enforce logical consistency, it should recover information that raw majority voting discards.
5	
6	\looseness=-1
7	We test this intuition through Symbolic Invariant Consensus Aggregation (SICA), which extracts logical constraints from reasoning traces (prompted as first-order logic; 99\% are propositional at the Z3 level) and selects answers via weighted partial MAX-SAT (\S\ref{sec:pipeline}; Figure~\ref{fig:pipeline}). The result is unequivocal: despite Z3 validating nearly all self-extracted constraints, SICA produces answers identical to majority voting on the vast majority of problems. Across six models (7B--32B), three reasoning domains, and multi-seed replication, no condition shows a significant positive effect after FDR control (Table~\ref{tab:main_results}). Four conditions confirm equivalence within $\pm$2\,pp; ten remain underpowered for effects below ${\sim}$2\,pp.
8	
9	\looseness=-1
10	The failure is not in the solver but in the constraints it operates on. Self-extracted constraints systematically support the model's majority answer, a phenomenon we term \emph{symbolic confirmation bias} (\S\ref{sec:confirmation-bias}). Because each trace determines both an answer and its constraints, the formal channel reduces to a weighted echo of the majority vote. We prove this degeneration is structural (Observation~1) and show it 
…[truncated 4085 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 448
}
```

</details>

---


### Tool call

_source line 1910 · 2026-05-23T13:43:34.490680+00:00_

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

_source line 1911 · 2026-05-23T13:43:35.066445+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\looseness=-1
5	\paragraph{Self-consistency and ensemble theory.}
6	Self-consistency (SC) selects the most frequent answer across chain-of-thought traces \citep{wang2023sc}. Extensions address free-form generation \citep{chen2024usc}, confidence weighting \citep{taubenfeld2025cisc}, diverse prompting \citep{li2023diverse}, and reasoning-aware filtering \citep{wan2024rasc, toh2024notallvotes, kim2026reasc}. SC gains plateau early \citep{loo2025reevaluating, byerly2026selfconsistency}. The Condorcet Jury Theorem \citep{condorcet1785} guarantees majority-vote convergence under independence; \citet{ladha1992correlated} show correlated voters reduce effective ensemble size. Our $K_\text{eff}$ adapts Fleiss' $\kappa$ from ensemble diversity theory \citep{kuncheva2003measures, brown2005diversity} to quantify this compression (\S\ref{sec:pipeline}). \citet{kim2025correlated} demonstrate correlated errors in LLM outputs; \citet{kuai2026independent} propose cross-model independence auditing, complementary to our within-model process-$\kappa$.
7	
8	\looseness=-1
9	\paragraph{Neuro-symbolic reasoning.}
10	We distinguish three paradigms: \emph{specification-generation} \citep{pan2023logiclm, olausson2023linc, ye2024satlm} translates problems into formal specifications before answering; \emph{program-generation} \citep{gao2023pal, chen2023program, lyu2023faithful} produces executable code; both formalize \emph{before} answer generation. \emph{Trace-extraction} (this work) operates post-hoc, inheriting confirmation bias (\S\ref{sec:confirmation-bias}). Recent extensions expand these paradigms with symbolic planning, logic agents, and verified reasoning \citep{ryu2025clover, xu2026dylos, li2025aristotle, wang2025fover, singh2026verge, luo2025logicagent, miya2025eidoku}; \citet{amonkar2025realitycheck} show formalization quality degrades with problem complexity; \citet{chan2026position} argue logical soundness alone is unrelia
…[truncated 3699 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 575
}
```

</details>

---


### Tool call

_source line 1912 · 2026-05-23T13:43:35.066803+00:00_

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

_source line 1913 · 2026-05-23T13:43:35.418666+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{SICA Pipeline}
5	\label{sec:pipeline}
6	\label{sec:condorcet}
7	\label{sec:effective-k}
8	
9	Self-Consistency (SC) \citep{wang2023sc} samples $K$ reasoning traces and selects the majority answer. Under correlated traces (Fleiss' $\kappa$ \citep{fleiss1971kappa}), effective sample size reduces to
10	\begin{equation}
11	\label{eq:effk}
12	K_{\text{eff}} = K \,/\, [1 + (K{-}1) \cdot \kappa]
13	\end{equation}
14	(following \citet{ladha1992correlated}). Intuitively, $K_\text{eff}$ measures how many effectively independent votes $K$ correlated traces contribute; e.g., $K{=}12$ traces with $\kappa{=}0.69$ yield $K_\text{eff} \approx 1.3$, meaning twelve correlated traces carry no more independent information than 1.3 uncorrelated ones. This motivates constraint-based aggregation.
15	
16	Symbolic Invariant Consensus Aggregation (SICA) extends SC by extracting formal constraints from traces and selecting the answer best supported by the satisfiable subset (Figure~\ref{fig:pipeline}).
17	
18	\paragraph{Trace generation.} Given question $q$, an LLM generates $K$ traces $\{t_1, \ldots, t_K\}$ at temperature $T = 0.7$. Each trace $t_i$ yields answer $a_i$.
19	
20	\looseness=-1
21	\paragraph{Constraint extraction.}\label{sec:constraint-extraction} The same LLM extracts logical constraints from each trace at $T_{\text{ext}} = 0.3$. The extraction prompt requests JSON output with constraint type, expression, and Z3-compatible formula (Appendix~\ref{app:prompts}); in practice, 99.0\% of extracted constraints are propositional at the Z3 level, with only 1.0\% using true quantifiers. The \emph{extraction rate} is the fraction of traces yielding at least one parseable constraint.
22	
23	\paragraph{Deduplication and MAX-SAT.} Constraints are deduplicated by syntactic equivalence (global average deduplication ratio: 46.0\%); each unique constraint $c_m$ receives weight $w_m$ equal to the number of source traces. The objective finds
…[truncated 3806 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1914 · 2026-05-23T13:43:35.469473+00:00_

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

_source line 1915 · 2026-05-23T13:43:36.359304+00:00_

1	\section{Results}
2	\label{sec:results}
3	\label{sec:main-results}
4	
5	\looseness=-1 Table~\ref{tab:main_results} reports accuracy across all non-degenerate self-extraction conditions sorted by SC baseline. No condition shows a significant SICA effect after FDR control (BH, $m{=}16$). Two conditions show nominally significant degradation: Mistral-7B on ProofWriter ($-2.83$\,pp, raw $p = 0.014$) and Qwen2.5-14B on ProofWriter ($-2.50$\,pp, raw $p = 0.011$); both reach adjusted $p = 0.112$. An aggregate sign test yields 8 positive and 7 negative $\Delta$ values ($p = 1.00$, two-sided). When SICA and SC disagree, SC selects the correct answer $2.6\times$ more often (139 vs.\ 53 across conditions), indicating that constraint-based reweighting introduces noise rather than corrective signal.
6	
7	\begin{table*}[t]
8	\centering
9	\small
10	\caption{SICA vs.\ SC across all non-degenerate self-extraction conditions (sorted by SC). No condition shows a significant gain after BH correction ($m{=}16$). $\Delta$ = SICA $-$ SC (pp). Symbols: $^b$gold ICL; \textbf{bold}: $p < 0.05$; {*}\,uncorrected $p < 0.05$ (BH adj.\ $p = 0.112$); $^{3s}$\,3-seed aggregate; $^{4s}$\,4-seed confirmatory aggregate (unmarked: single-seed exploratory; s123/s456/s789 are individual seed runs). All conditions have McNemar power $< 80\%$ for $|\Delta| = 2$\,pp (Appendix~\ref{app:power}). Degenerate conditions ($C_0 < 5\%$: QwQ-32B AIME $n{=}22$, Qwen2.5-14B GSM8K $n{=}30$; exploratory) yield $\Delta = 0$; oracle upper bounds in Appendix~\ref{app:oracle}.}
11	\label{tab:main_results}
12	\begin{tabular}{@{}llrrrrl@{}}
13	\toprule
14	Model & Domain & $n$ & SC (\%) & SICA (\%) & $\Delta$ (pp) & $p$ \\
15	\midrule
16	\multicolumn{7}{l}{\textit{Type C: error amplification (SC $\leq$ 40\%)}} \\
17	Mistral-7B & PW-D5 & 600 & 39.33 & 36.50 & $\mathbf{-2.83}$ & 0.014{*} \\
18	\midrule
19	\multicolumn{7}{l}{\textit{Intermediate SC (SC $\sim$50--60\%, Mistral-7B only)}} \\
20	Mistral-7B & LogiQA & 200 & 50.00 
…[truncated 3683 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 889
}
```

</details>

---


### Tool call

_source line 1916 · 2026-05-23T13:43:36.359812+00:00_

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

_source line 1917 · 2026-05-23T13:43:36.861817+00:00_

1	\section{The Symbolic Mirage}
2	\label{sec:analysis}
3	
4	\subsection{Symbolic Confirmation Bias}
5	\label{sec:confirmation-bias}
6	
7	\looseness=-1 Self-extracted constraints systematically align with the model's majority answer. On Mistral-7B FOLIO, when SICA errs, 83.3\% of constraints support the incorrect answer---bias ratio $4.97\times$ (Table~\ref{tab:cross-model-bias})---and 94\% of errors overlap with SC. Z3 rejects only 3.4\% of constraints, and MAX-SAT produces answers identical to count-only aggregation on $\geq$99\% of problems across all weight settings $\alpha$ (Table~\ref{tab:alpha-ablation}), confirming that the formal verification layer is vacuous (Eq.~\ref{eq:degenerate}): 99\% of constraints pass Z3 validation yet add no information beyond majority voting.
8	
9	\looseness=-1 Empirically, confirmation bias extends beyond incorrect instances. On problems where SC selects the correct answer, constraints still disproportionately support the majority ($\text{BR}_\text{correct}$ $1.29$--$3.64\times$ across all six tested conditions, with 5/6 showing $\text{BR}_\text{correct} \geq \text{BR}_\text{wrong}$), confirming that self-extracted constraints track distributional frequency rather than logical validity. A permutation null model---randomizing constraint--answer associations while preserving per-trace counts (1{,}000 permutations)---yields $\text{BR}_\text{null} \approx \text{BR}_\text{obs}$ ($\text{BR}_\text{excess} \approx 0$; $p > 0.7$) across all tested conditions, confirming that BR quantifies the degree of extraction degeneration---how completely constraints collapse to majority-vote equivalents---rather than an independent bias signal. The bias is inherent to the majority-vote geometry (Observation~1): under source-attribution scoring, BR $> 1$ follows from trace-count distributions, not extraction artifacts.
10	
11	\looseness=-1 The pattern generalizes: $4.97\times$ (Mistral), $3.85\times$ (Qwen-14B), $2.88\times$ (LLaMA), all $> 1.0$ with 
…[truncated 12659 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1918 · 2026-05-23T13:43:36.862215+00:00_

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

_source line 1919 · 2026-05-23T13:43:37.314066+00:00_

1	\section{Escaping the Bottleneck}
2	\label{sec:solutions}
3	\label{sec:cross-arch}
4	
5	\paragraph{Motivation.}
6	\looseness=-1 No training-free self-extraction method achieves independence from the model's distributional prior (\S\ref{sec:remediation}). Remark~1 implies that any escape must break the self-extraction dependency: the information ceiling $I(C;Y) \leq I(T;Y)$ binds whenever constraints are deterministic functions of the generating model's traces. We test whether a structurally independent verifier, sharing neither architecture nor training data with the generator, provides corrective signal that escapes this bound.
7	
8	\paragraph{Method.}
9	\looseness=-1 We use DeBERTa-large \citep{he2021deberta} (406M, encoder-only), fine-tuned on MultiNLI \citep{williams2018mnli}, to classify (premise, conclusion) pairs as entailment, contradiction, or neutral. In combo mode, each NLI-supporting vote counts $w$ times alongside SC's $K$ votes. We evaluate on Mistral-7B FOLIO ($n = 204$) and ProofWriter depth-5 ($n = 600$).
10	
11	\paragraph{Zero-shot results.}
12	\looseness=-1 DeBERTa NLI alone achieves 49.51\% on FOLIO and 55.00\% on ProofWriter. Combo $w{=}3$ yields $+6.67$\,pp on ProofWriter for Mistral-7B ($p < 0.001$, significant after BH correction) and $+2.94$\,pp on FOLIO (n.s.); all generators with SC $\geq 72\%$ show no significant improvement ($\Delta \leq +0.83$\,pp). Same-model SICA \emph{degrades} ProofWriter ($-2.83$\,pp; Table~\ref{tab:main_results}), illustrating that corrective signal must originate outside the model's distribution.
13	
14	\paragraph{Capability gap.}
15	\looseness=-1 Four generators spanning a 47-point SC range on ProofWriter ($n{=}600$), all paired with DeBERTa-large-mnli (55.00\% standalone; Table~\ref{tab:cross_generator_nli}): only Mistral-7B (SC 39.33\%, below the verifier) gains significantly ($+6.67$\,pp, $p < 0.001$); all three above the verifier show no significant $w{=}3$ improvement ($\Delta \leq +0.83$\,pp; Table~\ref{
…[truncated 2182 chars]

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

_source line 1920 · 2026-05-23T13:43:37.465050+00:00_

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

_source line 1921 · 2026-05-23T13:43:37.866819+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	\label{sec:conclusion}
4	
5	\looseness=-1
6	Our central finding is that the value of formal verification depends on the \emph{independence} of its inputs, not the soundness of its logic. \emph{SICA-specific}: under source-attribution scoring, SICA reduces to majority vote (Observation~1), and 27 training-free variants fail to escape. \emph{General}: the DPI bound (Remark~1) applies to any deterministic self-extraction, and SCB (BR $> 1$) holds across nine models (7B to frontier), suggesting the bottleneck is intrinsic to self-referential constraint generation. Three diagnostics ($K_\text{eff}$, BR, $C_0$) correctly characterize failure modes across all 60 tested conditions, with boundaries generalizing to held-out families (\S\ref{sec:diagnostic-framework}).
7	
8	\looseness=-1
9	This has direct consequences for test-time compute scaling \citep{snell2025scaling}: with $K_\text{eff} \leq 3.62$ for $K{=}12$, same-model traces scale redundancy, not information, advancing beyond \citet{huang2024selfcorrect}'s empirical findings to formal self-verification. Escaping the bottleneck requires structural independence (\S\ref{sec:cross-arch}); whether trained extractors or scaled cross-architecture verification can shift this boundary remains open.
10	

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

_source line 1922 · 2026-05-23T13:43:37.867256+00:00_

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

_source line 1923 · 2026-05-23T13:43:38.169021+00:00_

1	\looseness=-1 Models range from 7B to 32B (frontier via cross-model extraction); all benchmarks are English logical reasoning. We do not evaluate trained extractors. Statistical power is limited for effects below ${\sim}$2\,pp; the capability-gap analysis rests on $n{=}6$ conditions (Appendix~\ref{app:limitations-extended}).
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1924 · 2026-05-23T13:43:38.169378+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1925 · 2026-05-23T13:43:38.470600+00:00_

File content (30885 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1926 · 2026-05-23T13:43:51.217850+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "limit": "300"
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
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 1927 · 2026-05-23T13:43:51.218460+00:00_

1	\section{Prompt Templates}
2	\label{app:prompts}
3	
4	SICA uses domain-specific prompt templates for constraint extraction: one for mathematical reasoning (GSM8K, AIME) and one for logical reasoning (ProofWriter, FOLIO). Both share the same system prompt. The LLM is called with temperature $T{=}0.3$, max tokens $1024$, and structured JSON output mode. Up to 6 traces are processed in parallel via thread pooling, with 2 retries on failure (exponential backoff, base 0.5s).
5	
6	\paragraph{System Prompt.}
7	
8	\begin{lstlisting}
9	You are a constraint extraction tool. Output ONLY
10	valid JSON. Do NOT solve problems, reason about
11	correctness, or think step-by-step. Extract
12	constraints from the given trace exactly as stated.
13	\end{lstlisting}
14	
15	\paragraph{Mathematical Constraint Extraction (EXTRACTION\_PROMPT).}
16	
17	Used for GSM8K and AIME datasets. The placeholder \texttt{\{trace\}} is replaced with the reasoning trace at runtime.
18	
19	\begin{lstlisting}
20	Extract mathematical constraints from this reasoning
21	trace as a JSON object.
22	
23	Rules:
24	- type: "equation", "inequality", or "predicate"
25	- expression: human-readable, e.g. "x + y == 14"
26	- z3_formula: a single comparison expression in
27	  Python Z3 syntax
28	- source_step: step number where the constraint
29	  appears
30	- Use variable names from the trace
31	
32	z3_formula MUST follow these rules:
33	- Allowed operators: ==, !=, <, >, <=, >=, +, -, *,
34	  /, **, %
35	- Use individual named variables: a1, a2, a3...
36	  NOT arrays a[1] or sets A
37	- Expand all sums explicitly:
38	  "a1 + a2 + a3 == 55" NOT "sum([a1,a2,a3])"
39	- NO Python builtins: sum(), len(), max(), min(),
40	  list(), set(), range(), int()
41	- Each z3_formula must be exactly ONE comparison
42	  (==, !=, <, >, <=, >=)
43	- For multiple values, write separate constraints
44	  for each
45	
46	Output ONLY the JSON below, nothing else:
47	{"constraints": [{"type": "equation",
48	  "expression": "x + y == 14",
49	 
…[truncated 12941 chars]

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


### Tool call

_source line 1928 · 2026-05-23T13:43:52.624087+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "symb_invariant_consensus",
  "file": "paper_checklist.yaml",
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
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1929 · 2026-05-23T13:43:52.624438+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'symb_invariant_consensus'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1930 · 2026-05-23T13:43:53.980053+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_16/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_MISSING\"",
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_16/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_MISSING\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1931 · 2026-05-23T13:43:54.683081+00:00_

-rw-r--r-- 1 ubuntu ubuntu 651917 May 23 13:33 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_16/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 1932 · 2026-05-23T13:43:55.888064+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 1933 · 2026-05-23T13:43:55.988966+00:00_

-rw-r--r-- 1 ubuntu ubuntu 34561 May 23 10:41 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_issues.yaml
EXISTS

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

_source line 1934 · 2026-05-23T13:43:56.190050+00:00_

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

_source line 1935 · 2026-05-23T13:43:56.290855+00:00_

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

_source line 1936 · 2026-05-23T13:44:01.610446+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/project_config.yaml 2>/dev/null || cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/agent/project_config.yaml 2>/dev/null || echo \"NOT_FOUND\"",
  "description": "Find and read project config"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/agent/project_config.yaml 2>/dev/null || cat /home/ubuntu/.agent-ml-research-idea_gen_0513_3/agent/project_config.yaml 2>/dev/null || echo \"NOT_FOUND\"",
    "description": "Find and read project config"
  }
}
```

</details>

---


### Tool result

_source line 1937 · 2026-05-23T13:44:02.413795+00:00_

NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Bash",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1938 · 2026-05-23T13:44:02.866040+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/appendix.tex",
  "offset": "300",
  "limit": "300"
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
    "offset": "300",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 1939 · 2026-05-23T13:44:03.368709+00:00_

300	\bottomrule
301	\end{tabular}}
302	\caption{Bootstrap 95\% confidence intervals for $\Delta(\text{SICA} - \text{SC})$ in percentage points. All intervals include zero, consistent with no reliable accuracy difference.}
303	\label{tab:bootstrap}
304	\end{table}
305	
306	All three intervals contain zero. The narrowest interval (Qwen-14B, [$-$1.12, $+$1.62]) rules out practically meaningful gains ($>$2pp) even in the most favorable case. The widest interval (LLaMA-8B FOLIO, [$-$5.88, $+$0.98]) skews negative, indicating that SICA may slightly hurt accuracy in this condition. These results corroborate the McNemar tests and power analysis: no condition provides evidence that logical constraint aggregation improves over majority voting.
307	
308	
309	\section{Case Studies: Discordant Predictions}
310	\label{app:case-studies}
311	
312	Among 804 problems, SICA and SC agree on 773 (96.1\%). The 31 discordant cases comprise 16 SICA wins (SICA correct, SC wrong), 14 SC wins (SC correct, SICA wrong), and 1 where both select different wrong answers. All 31 occur at exact ties (entropy${=}1.0$, 6:6 vote split) or near-ties (entropy${\geq}0.9183$, 8:4 at most), since SICA can differ from SC only when constraint weights shift the majority away from SC's tiebreak choice. We present three representative cases that illustrate the mechanism behind capability-accuracy constraint failures.
313	
314	\paragraph{Case 1: SICA Wins (folio\_134, FOLIO).}
315	
316	\emph{Premises}: Some mammals have teeth. Platypus have no teeth. Platypus are mammals. Humans have teeth. \emph{Conclusion}: Humans are mammals. \emph{Gold}: Unknown.
317	
318	The premises state that \emph{some} mammals have teeth and that humans have teeth, but ``having teeth'' is not sufficient for ``being a mammal'' under open-world semantics. SC produces a 6:6 split (Unknown:6, True:6) and tiebreaks alphabetically to True (wrong). SICA extracts 7 constraints; MaxSAT excludes 1 constraint inconsistent with the rest, reducing th
…[truncated 23574 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1940 · 2026-05-23T13:44:03.519838+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1941 · 2026-05-23T13:44:03.520275+00:00_

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
47	@article{ladha1992correlated,
48	  title={The {C}ondorcet Jury Theorem, Fr
…[truncated 1852 chars]

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


### Tool call

_source line 1942 · 2026-05-23T13:44:10.418518+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/project_config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3"
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
    "pattern": "**/project_config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3"
  }
}
```

</details>

---


### Tool result

_source line 1943 · 2026-05-23T13:44:10.519343+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1944 · 2026-05-23T13:44:12.377063+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/project_config.*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3"
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
    "pattern": "**/project_config.*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3"
  }
}
```

</details>

---


### Tool result

_source line 1945 · 2026-05-23T13:44:12.477934+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1946 · 2026-05-23T13:44:27.131574+00:00_

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

_source line 1947 · 2026-05-23T13:44:27.483328+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1948 · 2026-05-23T13:44:27.483766+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline ARR commitment deadline"
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
    "query": "EMNLP 2026 call for papers submission deadline ARR commitment deadline"
  }
}
```

</details>

---


### Tool result

_source line 1949 · 2026-05-23T13:44:32.604081+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline ARR commitment deadline"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"}]

Based on the search results, here are the key deadlines for EMNLP 2026:

## ARR Submission Deadline
The ARR submission deadline for l
…[truncated 819 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebSearch",
  "elapsed_ms": 5120
}
```

</details>

---


### Tool call

_source line 1950 · 2026-05-23T13:44:38.461614+00:00_

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
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
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

_source line 1951 · 2026-05-23T13:44:38.562383+00:00_



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

_source line 1952 · 2026-05-23T13:44:42.677448+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract the complete submission guidelines for EMNLP 2026 main conference papers: page limits (long and short), formatting template, anonymity rules, appendix rules, limitations section requirements, ethics statement requirements, supplementary material rules, and any other formatting requirements. Also extract all deadlines."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract the complete submission guidelines for EMNLP 2026 main conference papers: page limits (long and short), formatting template, anonymity rules, appendix rules, limitations section requirements, ethics statement requirements, supplementary material rules, and any other formatting requirements. Also extract all deadlines."
  }
}
```

</details>

---


### Tool result

_source line 1953 · 2026-05-23T13:44:48.649783+00:00_

# EMNLP 2026 Main Conference Submission Guidelines

## Page Limits
- **Long papers:** 8 pages (9 pages for camera-ready final versions)
- **Short papers:** 4 pages (5 pages for camera-ready final versions)

## Key Formatting Requirements
All submissions must "follow all of the ARR submission requirements," which are detailed on the ACL Rolling Review website rather than this page.

## Anonymity Rules
"The reviewing process will continue to be double-blind. Reviewers will not see authors, nor will authors see reviewers." However, "there is no anonymity period requirement" following ACL and ARR policies.

## Author List Changes
During commitment to EMNLP, "modification of the author list (i.e., addition/deletion of authors is not allowed). However, modification of author order is possible."

## Other Requirements Referenced
The guidelines require compliance with:
- Two-way anonymized review instructions
- ACL's Publication Ethics Policy
- ARR's Ethics Policy including responsible NLP research checklist
- ACL's Disclosure Policy (coordinated disclosure)
- Limitations sections
- Writing assistance policies
- Optional supplementary materials guidelines

## Critical Deadlines (All times: 11:59 PM UTC-12:00)

| Deadline | Date |
|----------|------|
| ARR submission | May 25, 2026 |
| Reviewer registration | May 27, 2026 |
| Author response period | July 7-13, 2026 |
| Meta-review release | July 30, 2026 |
| EMNLP commitment deadline | August 2, 2026 |
| Acceptance notification | August 20, 2026 |
| Camera-ready submission | September 20, 2026 |
| Main conference | October 24-29, 2026 |

**Note:** Complete formatting details are maintained on the ARR website, not within this call.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebFetch",
  "elapsed_ms": 5972
}
```

</details>

---


### Tool call

_source line 1954 · 2026-05-23T13:44:53.116334+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract all submission requirements: page limits for long and short papers, template requirements, anonymization rules, limitations section requirements, appendix rules, supplementary materials, formatting (font size, margins, columns), and any other formatting requirements. Also extract the review form / scoring criteria if available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract all submission requirements: page limits for long and short papers, template requirements, anonymization rules, limitations section requirements, appendix rules, supplementary materials, formatting (font size, margins, columns), and any other formatting requirements. Also extract the review form / scoring criteria if available."
  }
}
```

</details>

---


### Tool result

_source line 1955 · 2026-05-23T13:44:59.439440+00:00_

# ACL Rolling Review - Submission Requirements Summary

## Page Limits

**Long Papers:**
- "up to eight (8) pages of content"
- Unlimited space for limitations section (required) and optional ethical considerations
- Unlimited reference pages

**Short Papers:**
- "up to four (4) pages of content"
- Unlimited space for limitations section (required) and optional ethical considerations
- Unlimited reference pages

## Template & Formatting Requirements

- Must use "the official ACL style template" from the designated GitHub repository
- Follow "*ACL" formatting guidelines regarding paper size, margin width, and font size
- No modifications to style files permitted
- Papers must comply with double-column formatting (with limited exceptions for appendices)
- Non-compliant submissions are "rejected without review"

## Anonymization Rules

- No author names or affiliations in submission
- Avoid self-references revealing identity (use "Smith previously showed..." instead of "We previously showed...")
- Do not reference materials unavailable to reviewers
- Supplementary materials and repository links must be anonymized
- Cloud services like Dropbox are prohibited due to download tracking

## Required Limitations Section

- Mandatory dedicated section titled "Limitations"
- Must appear before references, does not count toward page limit
- Should address both long and short papers
- Cannot introduce new methods, analysis, or results
- Missing section results in desk rejection

## Appendices & Supplementary Materials

Appendices:
- Follow double-column format (with approved exceptions)
- Do not count toward page limits
- Must be fully anonymized
- Key technical content essential for assessment should appear in main paper

Supplementary Materials:
- Software as single .tgz or .zip file
- Data as separate .tgz or .zip archive
- Online repositories must use anonymous hosting (e.g., Anonymous GitHub)
- Reviewers are not required to review appendix content

## Review Form / Scoring 
…[truncated 213 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "WebFetch",
  "elapsed_ms": 6323
}
```

</details>

---


### Tool call

_source line 1956 · 2026-05-23T13:45:42.964306+00:00_

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

_source line 1957 · 2026-05-23T13:46:06.596587+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 23632
}
```

</details>

---


### Tool call

_source line 1958 · 2026-05-23T13:46:06.734088+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026（通过 ARR May 2026 cycle 投稿）\n- **截止日期**：2026-05-25 AoE\n- **格式要求**：Long paper，正文 8 页限制，参考文献不限页数，Limitations section 不计入页数（必须有），ACL style template `[review]` 模式，double-blind\n- **评分标准**：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_16/submitted.pdf`\n（main.tex 使用 \\input 引入各章节文件，均在同一目录下）\n\n## 你的审查重点\n\n**1. 统计方法与实验设计**\n- McNemar exact test 用于配对比较是否合适？BH 校正是否正确应用？\n- TOST 等效性检验的 margin (±2pp) 是否合理？pre-registered 了吗？\n- Bootstrap CI 方法是否恰当？\n- 统计检验力分析 — MDE 计算是否正确？underpowered 的结论是否诚实报告？\n- 多重比较：16 个 condition 的 BH 校正数目是否正确？\n- 样本量是否足够支撑论文声明？特别关注 n=22 (AIME)、n=30 (GSM8K)、n=200-600 的条件\n\n**2. 形式化声明的严谨性**\n- Observation 1 (Argmax Preservation)：前提条件 (i)(ii)(iii) 是否充分？证明是否完整？empirical support 是否足够？\n- Remark 1 (Information Ceiling)：DPI bound 的应用是否正确？Markov chain 假设是否合理？\n- Remark 2：semantic evaluation 的额外假设是否被充分讨论？\n- 这些形式化声明是否真的是\"observation/remark\"还是应该称为 theorem/proposition？\n\n**3. 实验控制与可复现性**\n- Oracle control 是否充分排除了 solver 问题？\n- 27 种 remediation 变体的测试是否系统化？是否有遗漏的重要 baseline？\n- 温度、K、seed 的敏感性分析是否充分？\n- Cross-architecture verification 的实验设计是否公平？DeBERTa-NLI 作为 verifier 是否引入了不公平比较？\n- 能力差距模式基于 n=6 个 condition — 是否过度声明？\n\n**4. Bias Ratio 定义与验证**\n- BR 的定义（Eq. 4）是否有循环论证？BR>1 是否可能是 trivial consequence？\n- Permutation null model 是否恰当？\n- BR 跨模型的可比性？\n\n**5. 可复现性**\n- 代码/数据是否可获取？\n- 超参数报告是否完整？\n- 随机种子控制是否充分？\n\n请提供完整审稿报告，包含：Summary、Strengths、Weaknesses（按 Must-Fix / Should-Fix / Minor 分级）、Questions、Missing References、Overall Assessment（评分 + 置信度）。"
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
    "text": "你是 Reviewer 1，负责**方法严谨性**审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026（通过 ARR May 2026 cycle 投稿）\n- **截止日期**：2026-05-25 AoE\n- **格式要求**：Long paper，正文 8 页限制，参考文献不限页数，Limitations section 不计入页数（必须有），ACL style template `[review]` 模式，double-blind\n- **评分标准**：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_16/submitted.pdf`\n（main.tex 使用 \\input 引入各章节文件，均在同一目录下）\n\n## 你的审查重点\n\n**1. 统计方法与实验设计**\n- McNemar exact test 用于配对比较是否合适？BH 校正是否正确应用？\n- TOST 等效性检验的 margin (±2pp) 是否合理？pre-registered 了吗？\n- Bootstrap CI 方法是否恰当？\n- 统计检验力分析 — MDE 计算是否正确？underpowered 的结论是否诚实报告？\n- 多重比较：16 个 condition 的 BH 校正数目是否正确？\n- 样本量是否足够支撑论文声明？特别关注 n=22 (AIME)、n=30 (GSM8K)、n=200-600 的条件\n\n**2. 形式化声明的严谨性**\n- Observation 1 (Argmax Preservation)：前提条件 (i)(ii)(iii) 是否充分？证明是否完整？empirical support 是否足够？\n- Remark 1 (Information Ceiling)：DPI bound 的应用是否正确？Markov chain 假设是否合理？\n- Remark 2：semantic evaluation 的额外假设是否被充分讨论？\n- 这些形式化声明是否真的是\"observation/remark\"还是应该称为 theorem/proposition？\n\n**3. 实验控制与可复现性**\n- Oracle control 是否充分排除了 solver 问题？\n- 27 种 remediation 变体的测试是否系统化？是否有遗漏的重要 baseline？\n- 温度、K、seed 的敏感性分析是否充分？\n- Cross-architecture verification 的实验设计是否公平？DeBERTa-NLI 作为 verifier 是否引入了不公平比较？\n- 能力差距模式基于 n=6 个 condition — 是否过度声明？\n\n**4. Bias Ratio 定义与验证**\n- BR 的定义（Eq. 4）是否有循环论证？BR>1 是否可能是 trivial consequence？\n- Permutation null model 是否恰当？\n- BR 跨模型的可比性？\n\n**5. 可复现性**\n- 代码/数据是否可获取？\n- 超参数报告是否完整？\n- 随机种子控制是否充分？\n\n请提供完整审稿报告，包含：Summary、Strengths、Weaknesses（按 Must-Fix / Should-Fix / Minor 分级）、Questions、Missing References、Overall Assessment（评分 + 置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 1959 · 2026-05-23T13:46:30.597239+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 23863
}
```

</details>

---


### Tool call

_source line 1960 · 2026-05-23T13:46:30.749105+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026（通过 ARR May 2026 cycle 投稿）\n- **截止日期**：2026-05-25 AoE\n- **格式要求**：Long paper，正文 8 页限制，参考文献不限页数，Limitations section 不计入页数（必须有），ACL style template `[review]` 模式，double-blind\n- **评分标准**：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_16/submitted.pdf`\n（main.tex 使用 \\input 引入各章节文件，均在同一目录下）\n\n## 你的审查重点\n\n**1. 贡献新颖度**\n- \"negative result\"（自提取约束无效）的发现是否真正令人惊讶？还是 obvious in hindsight？\n- Symbolic confirmation bias 概念是否是对 Huang et al. (2024) \"LLMs cannot self-correct\" 的 trivial extension？论文声称 advances beyond 但实际增量在哪？\n- 三个诊断指标 (K_eff, BR, C0) 是否有足够的 practical value？\n- Cross-architecture escape 作为贡献是否太 preliminary（仅一个 verifier family，n=6 conditions）？\n- 对 NLP/ML 社区的影响和启示是什么？\n\n**2. Related Work 覆盖**\n- 检查是否遗漏了重要的 neuro-symbolic reasoning 工作\n- 检查 self-correction / self-refinement 文献是否充分\n- 检查 test-time compute scaling 相关工作是否覆盖\n- 检查 ensemble diversity / committee learning 文献\n- 检查引用是否真实存在（特别是 2025-2026 年的引用，如 kim2026reasc, byerly2026selfconsistency, kuai2026independent, xu2026dylos, singh2026verge, jhaveri2026failing, chan2026position, dupo2025 等）\n- 是否有 self-citation 暴露匿名性的问题？\n\n**3. 叙事结构与写作质量**\n- Abstract 是否在 200 words 以内？（EMNLP 2026 硬约束）\n- 论文的叙事弧是否清晰？从 motivation → method → negative result → diagnosis → escape\n- 术语一致性：SICA、SC、SCB、BR 等缩写是否首次使用时定义？\n- Figure/Table 数量和质量是否恰当？\n- 论文节奏是否合理？正文 8 页是否装得下所有必要内容？是否有内容应该移到 appendix？\n- Limitations section 是否满足要求（简短、3 个点左右）？\n\n**4. Claims 支撑充分性**\n- \"no detectable improvement\" — 是否 fairly stated given underpowered tests？\n- \"symbolic confirmation bias\" 是否过度命名（给一个 expected behavior 起了一个 dramatic name）？\n- \"27 training-free variants all fail\" — 是否穷尽了所有合理方向？\n- \"three zero-cost diagnostics\" — prospective validation 是否足够？\n- Frontier model 实验（Table 3）中部分模型 n_err 很小（如 Gemini n=12），是否过度解读？\n\n**5. 格式合规性**\n- 正文是否在 8 页以内？\n- Limitations section 是否在正文中（非 appendix）？\n- 是否有 double-blind 违规？\n- 引用格式是否一致？\n\n请提供完整审稿报告，包含：Summary、Strengths、Weaknesses（按 Must-Fix / Should-Fix / Minor 分级）、Questions、Missing References、Overall Assessment（评分 + 置信度）。"
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
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026（通过 ARR May 2026 cycle 投稿）\n- **截止日期**：2026-05-25 AoE\n- **格式要求**：Long paper，正文 8 页限制，参考文献不限页数，Limitations section 不计入页数（必须有），ACL style template `[review]` 模式，double-blind\n- **评分标准**：5=Consider for Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/review_round_16/submitted.pdf`\n（main.tex 使用 \\input 引入各章节文件，均在同一目录下）\n\n## 你的审查重点\n\n**1. 贡献新颖度**\n- \"negative result\"（自提取约束无效）的发现是否真正令人惊讶？还是 obvious in hindsight？\n- Symbolic confirmation bias 概念是否是对 Huang et al. (2024) \"LLMs cannot self-correct\" 的 trivial extension？论文声称 advances beyond 但实际增量在哪？\n- 三个诊断指标 (K_eff, BR, C0) 是否有足够的 practical value？\n- Cross-architecture escape 作为贡献是否太 preliminary（仅一个 verifier family，n=6 conditions）？\n- 对 NLP/ML 社区的影响和启示是什么？\n\n**2. Related Work 覆盖**\n- 检查是否遗漏了重要的 neuro-symbolic reasoning 工作\n- 检查 self-correction / self-refinement 文献是否充分\n- 检查 test-time compute scaling 相关工作是否覆盖\n- 检查 ensemble diversity / committee learning 文献\n- 检查引用是否真实存在（特别是 2025-2026 年的引用，如 kim2026reasc, byerly2026selfconsistency, kuai2026independent, xu2026dylos, singh2026verge, jhaveri2026failing, chan2026position, dupo2025 等）\n- 是否有 self-citation 暴露匿名性的问题？\n\n**3. 叙事结构与写作质量**\n- Abstract 是否在 200 words 以内？（EMNLP 2026 硬约束）\n- 论文的叙事弧是否清晰？从 motivation → method → negative result → diagnosis → escape\n- 术语一致性：SICA、SC、SCB、BR 等缩写是否首次使用时定义？\n- Figure/Table 数量和质量是否恰当？\n- 论文节奏是否合理？正文 8 页是否装得下所有必要内容？是否有内容应该移到 appendix？\n- Limitations section 是否满足要求（简短、3 个点左右）？\n\n**4. Claims 支撑充分性**\n- \"no detectable improvement\" — 是否 fairly stated given underpowered tests？\n- \"symbolic confirmation bias\" 是否过度命名（给一个 expected behavior 起了一个 dramatic name）？\n- \"27 training-free variants all fail\" — 是否穷尽了所有合理方向？\n- \"three zero-cost diagnostics\" — prospective validation 是否足够？\n- Frontier model 实验（Table 3）中部分模型 n_err 很小（如 Gemini n=12），是否过度解读？\n\n**5. 格式合规性**\n- 正文是否在 8 页以内？\n- Limitations section 是否在正文中（非 appendix）？\n- 是否有 double-blind 违规？\n- 引用格式是否一致？\n\n请提供完整审稿报告，包含：Summary、Strengths、Weaknesses（按 Must-Fix / Should-Fix / Minor 分级）、Questions、Missing References、Overall Assessment（评分 + 置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 1961 · 2026-05-23T13:46:32.261001+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1511
}
```

</details>

---


### Assistant

_source line 1962 · 2026-05-23T13:46:37.866018+00:00_

Round 1 全部派发完成：

- ✅ 视觉审查 Agent 已启动（fire-and-forget）
- ✅ Reviewer 1（方法严谨性）已收到任务
- ✅ Reviewer 2（新颖性与完整性）已收到任务

等待两位 Reviewer 返回独立审稿报告，收齐后进入交叉分享（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 139

## Round 139

2 recorded events


### User

_source line 1963 · 2026-05-23T13:54:37.599545+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告：方法严谨性审查

**论文标题**: Beyond Self-Consistency: Self-Extracted Constraints Provide No Detectable Improvement in LLM Reasoning

---

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 方法论严谨的负面结果论文，统计设计远超同类工作水准，但核心正面贡献（cross-architecture escape）基于 n=6 且存在共享 verifier 问题，诊断框架的独立贡献有限。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4.0/5 | 统计方法全面（McNemar + BH + TOST + Bootstrap + Power analysis），形式化声明的命名谨慎（Observation/Remark 而非 Theorem），但 BR 指标的诊断独立价值存疑，capability gap 基于 n=6 |
| Excitement | 3.0/5 | 负面结果本身有实践价值（告知社区 self-extraction 方向无效），但缺少令人兴奋的解决方案；cross-architecture escape 太初步 |
| Reproducibility | 3/5 | 超参数报告完整（K=12, T=0.7, T_ext=0.3, α=0.5, Z3 timeout 10s），prompt 模板完整给出，但无代码/数据可获取性声明 |
| Confidence | 4/5 | 统计方法与实验设计是本人专长领域，对形式化声明审查有较高把握 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Capability-gap pattern 基于 n=6 数据点且存在共享 verifier 问题，作为 Contribution 3 过度声明

- 具体位置：Section 6 (Table 3), Appendix W (Figure 8, Table 28), Limitations
- 问题：论文将 capability-gap pattern 列为三大贡献之一（Introduction 第 3 条），但该 pattern 仅基于 6 个 verifier-generator 组合（Spearman ρ = 1.0, p = 0.003）。更关键的是，6 个数据点中有 4 个共享同一个 DeBERTa verifier（Appendix W: "four of six conditions share the DeBERTa verifier, which may reduce effective degrees of freedom"）。这意味着实际有效自由度远小于 n=6。虽然论文在 Limitations 和 Appendix 中多次提及此限制（"with n=6 this should be interpreted cautiously"），但在 Abstract、Introduction、Section 6 标题处仍以 contribution 级别呈现。
- 为什么影响接收：一个仅有 6 个数据点且 4 个共享同一 verifier 的观察不足以作为 top-level contribution。如果这个 pattern 不成立，Section 6 的叙事（"escaping the bottleneck"）就失去了方向性证据。
- 建议修改方向：(a) 将 Contribution 3 降级为 "preliminary observation" 而非并列贡献；(b) 增加至少 2-3 个不同架构的 verifier（如 T5-based NLI, Flan-T5 NLI）验证 monotonic trend；(c) 或者在 Abstract/Introduction 中明确标注 "based on limited evidence (n=6, shared verifier)"。

**N2** [critical] 10/16 条件 underpowered，中心论断的表述需更精确

- 具体位置：Abstract 第 1 句 ("We find no evidence of improvement"), Section 4 (Table 1), Appendix D (Table 6)
- 问题：Table 6 显示三个 confirmatory conditions 的 observed power 均低于 21%（Qwen-14B FOLIO+PW: 5.7%, LLaMA-8B StrategyQA: 20.6%, LLaMA-8B FOLIO: 18.6%）。MDE 为 1.86-4.84pp。这意味着论文无法检测到 <2pp 的效果。论文在正文中诚实承认了这一点（Section 4: "Absence of evidence is not evidence of absence for small effects"），但 Abstract 的表述 "We find no evidence of improvement" 可能被误读为 "已证明无效果"。此外，TOST 仅 4/16 条件确认等效，10 条件 underpowered。
- 为什么影响接收：负面结果论文的核心价值取决于其否定结论的强度。如果论文只能排除 >2pp 的效果，这个结论的实际影响力有限——很多读者会认为 <2pp 的效果在实践中也有意义（特别是 K=12 下 4.5× 计算开销的场景下，2pp 确实不值得，但这个论点需要显式给出）。
- 建议修改方向：(a) Abstract 改为 "We find no evidence of improvement exceeding ~2 percentage points" 或类似更精确的表述；(b) 在 Discussion 中显式论证为什么 <2pp 的改进在 4.5× 计算开销下无实际价值，将 power limitation 转化为 practical insignificance 论证。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Bias Ratio (BR) 的诊断独立价值与 Observation 1 存在循环

- 具体位置：Section 3.1 Eq. 4, Section 5.1
- 问题：论文定义 BR = P(c supports a_M | a_M ≠ a*) / P(c supports a* | a_M ≠ a*)。在 source-attribution scoring 下（σ(c,a)=1 iff c 来自产生 a 的 trace），如果 a_M 是多数答案，那么 P(c supports a_M) > P(c supports a*) 是 trace-count 分布的必然结果。论文自己在 §5.1 承认："The bias is inherent to the majority-vote geometry (Observation 1): under source-attribution scoring, BR > 1 follows from trace-count distributions, not extraction artifacts." Permutation test 确认 BR_excess ≈ 0 (p > 0.7)，即 BR 完全由 trace-count 结构解释。
- 这导致一个概念性问题：BR > 1 本身不是"symbolic confirmation bias"的证据，而只是 source-attribution scoring 的数学后果。BR 度量的是 degeneration 程度（SICA 退化为 majority voting 的程度），但论文标题和叙事将其包装为一种"bias"，暗示 extraction 过程有问题。实际上，问题在于评分机制，而非提取本身。
- 建议：(a) 更清晰地区分 "structural degeneration"（Observation 1 的后果）和 "extraction bias"（如果存在的话，应表现为 BR_excess > 0）；(b) 考虑是否有 BR_excess 显著大于 0 的条件，那才是真正的 extraction-level bias 证据。

**W2** [warning] "Pre-registered" margin ±2pp 无注册凭证

- 具体位置：Section 4 ("TOST equivalence tests with pre-registered margin ±2 pp")
- 问题：论文声称 TOST margin ±2pp 是 "pre-registered" 的，但未提供任何预注册链接（如 OSF、AsPredicted）。如果只是"在分析前决定"，不应使用 "pre-registered" 一词——这在统计学界有严格定义。margin 的选择 "based on the smallest meaningful SC gain reported in Wang et al. (2023)" 是合理的，但 "pre-registered" 要求有可验证的时间戳记录。
- 建议：改为 "pre-specified" 或 "predetermined"，除非能提供实际注册链接。

**W3** [warning] BH correction 中 m=16 包含非独立条件

- 具体位置：Section 4, Table 1 caption ("BH, m=16")
- 问题：16 个条件中包含 Mistral-7B × FOLIO 的三个单独 seed (s123, s456, s789) 和一个 3-seed aggregate，以及 Qwen2.5-14B × FOLIO 的 4-seed aggregate 和 FOLIO(ICL)。aggregate 是其 component seeds 的函数，不是独立检验。这使得 m 被人为膨胀。虽然更大的 m 使 BH 更保守（有利于负面结论），但这在方法论上不够干净。具体影响：两个名义显著条件 (raw p = 0.014, 0.011) 经 BH 校正后 p_adj = 0.112。如果用更合理的 m（去掉重叠条件，约 m=10-12），p_adj 可能降至 ~0.07-0.08，仍不显著但更接近边界。
- 建议：明确说明哪些条件是 confirmatory vs. exploratory，对 confirmatory subset（真正独立的条件）单独报告 BH 校正。实际上论文在 Power Analysis 中已做了这个区分（3 个 confirmatory conditions），可以更一致地应用。

**W4** [warning] Observation 1 条件 (iii) "approximately uniform constraint yield" 缺乏系统验证

- 具体位置：Section 5.1, Observation 1
- 问题：Observation 1 的三个前提条件中，(i) |C\| ≈ 0 由 Z3 rejection rate 3.4% 实证支持，(ii) source-attribution scoring 是系统设计。但 (iii) "approximately uniform constraint yield per trace within each answer group" 缺乏直接验证。论文未报告每条 trace 的 constraint yield 分布（均值、标准差、偏度）。如果某些 trace 产生的约束数量远多于其他 trace，即使 |C\| ≈ 0，score(a) 也不一定正比于 n_a。
- 建议：报告 per-trace constraint yield 的分布统计量（mean, std, CV），最好按 answer group 分层，验证条件 (iii) 的近似成立程度。

**W5** [warning] Cross-architecture escape 可能只是 ensemble diversity 效应

- 具体位置：Section 6
- 问题：DeBERTa-NLI 是 encoder-only 架构，fine-tuned on MultiNLI——与 decoder-only LLM generator 在架构、训练数据、推理方式上完全不同。observed gain（+6.67pp on Mistral-7B ProofWriter）可能不是因为 "structural independence breaks the information bottleneck"，而是简单的 ensemble diversity 效应：组合两个足够不同的分类器通常会带来增益。如果用任意 structurally independent model（如 bag-of-words + logistic regression 在 ProofWriter 上训练）也能获得类似增益，那 Section 6 的理论叙事就不成立。
- 建议：(a) 增加至少一个非 NLI 的 structurally independent baseline（如 random forest on extracted features）作为对照；(b) 或者在讨论中明确承认 ensemble diversity 是一个可能的 confound，cross-architecture escape 的理论解释需要进一步验证。

---

## 小问题（不影响接收）

- **M1**: Introduction 第 10 行 "We prove this degeneration is structural (Observation 1)"——Observation 1 依赖经验条件 (iii)，"prove" 过强，应改为 "show" 或 "demonstrate"。
- **M2**: Frontier model 的 BR 分析（Table 2）中，gpt-4o 标为 self-extraction (^a)，但闭源 API 如何做 self-extraction？如果是通过 API 调用，提取 prompt 仍由 gpt-4o 自身执行，这确实是 self-extraction，但应明确说明 API-based self-extraction 的具体实现。
- **M3**: §5.1 提到 "83.3% of constraints support the incorrect answer" on Mistral-7B FOLIO，但 Table 2 (Appendix O) 报告同一模型 "Wrong % = 80.9%"。二者定义不同（前者是 raw constraint fraction，后者是 MaxSAT-weighted），但正文应明确标注以避免混淆。
- **M4**: ProcessSim (Eq. 7) 使用 TF-IDF cosine similarity 度量推理过程相似性，但 TF-IDF 捕获词汇重叠而非语义推理相似性。Appendix R 提到 SBERT 替代 (ProcessSim = 0.91 vs. TF-IDF 0.74)，证明结论 robust，但主文应提及 representation choice 的限制。
- **M5**: 无代码/数据可获取性声明。理解 double-blind 要求下不能提供实际链接，但应有 "Code and data will be released upon acceptance" 或类似声明。
- **M6**: Abstract 用 "self-extracted" 一词出现 4 次，可适当减少重复。

---

## Questions to Authors

1. **BR_excess ≈ 0 意味着什么？** 如果 permutation test 显示经验 BR 完全由 trace-count 结构解释（BR_excess ≈ 0），那么 "symbolic confirmation bias" 这个术语是否准确？这似乎更应该叫 "structural degeneration" 或 "scoring mechanism artifact"——bias 暗示 extraction 过程引入了额外偏差，但你们的数据显示并没有。

2. **Observation 1 条件 (iii) 的验证数据？** 每条 trace 平均产生多少 constraints？标准差是多少？不同 answer group 之间的 yield 差异有多大？

3. **为什么不测试 non-NLI independent verifier？** 例如在 ProofWriter 上训练一个简单的 rule-based verifier 或 logistic regression classifier，看是否也能获得 cross-architecture escape 效果。这将帮助区分 "information independence" 和 "ensemble diversity" 假说。

4. **TOST margin 的 "pre-registered" 指什么？** 是否有 OSF 或类似平台的注册记录？如果没有，请改为 "pre-specified"。

5. **Domain-adapted verifier (Section 6) 引入了训练** ——fine-tuning DeBERTa on ProofWriter OWA。这与论文 "training-free" 叙事线的关系如何？Combo gains (+12.67pp) 是否主要来自 domain-specific 训练而非 structural independence？

---

## Missing References

- **Verifier-guided reasoning**: 论文引用了 Lightman et al. (2024) 等 process reward model 工作，但缺少 Cobbe et al. (2021) 的 GSM8K verifier 工作的更深入对比——那也是用独立 verifier 提升推理性能的早期实例。
- **Ensemble methods in NLP**: 论文的 cross-architecture escape 实质上是 model ensemble。缺少对 ensemble diversity 文献（如 Dietterich, 2000; Krogh & Vedelsby, 1994）的讨论，这些工作为 "diverse ensembles outperform individual models" 提供了理论基础，可能解释 Section 6 的结果而无需 information bottleneck 理论。

---

## 主要优势

1. **统计方法论极为扎实**: McNemar paired test + BH FDR correction + TOST equivalence + Bootstrap CI + Power analysis + multi-seed replication 的完整组合在 NLP 论文中极为罕见。诚实报告 underpowered conditions 和 power limitations 体现了高水准的科学诚信。

2. **Oracle control 设计精巧**: 用 gold FOL/DSL 标注替换 self-extracted constraints 的对照实验（+29.90pp FOLIO, +17.17pp ProofWriter, p < 10^-7）清晰地将问题定位在 extraction 而非 solver，是本文最有说服力的实验设计。

3. **27 种 remediation 变体的系统化测试**: 涵盖 prompt-level、method-level、paradigm、solver、input diversity、filtering 六个维度，彻底排除了 "换个方法就行" 的反驳。特别是 Debate (κ=0.15, Δ=-18.63pp) 和 Contrastive prompting (94 pro vs. 65 con) 的结果提供了 independence-accuracy trade-off 的直觉。

4. **形式化声明的命名克制得当**: Observation 1 和 Remark 1/2 没有膨胀为 Theorem/Proposition，诚实反映了其依赖经验条件的本质。

5. **Diagnostic framework 有实践价值**: C₀ < 5%, K_eff ≤ 1.30, BR + SC regime 三个 zero-cost diagnostics 可在 K=12 pilot run 后直接判断 self-extraction 方法是否值得尝试，在 held-out families (LLaMA, Qwen3) 上得到 prospective validation。

6. **Entropy decomposition analysis (Appendix M)** 精细地展示了 SICA 效果与 trace agreement 的交互关系：low-entropy 问题 Δ ≈ 0（无信息增益），high-entropy 问题的 Δ 方向取决于 SC regime 而非 entropy 本身。这个分析强化了 regime-dependent 叙事。

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

_source line 1964 · 2026-05-23T13:54:44.290332+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 完成独立审稿后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 140

## Round 140

2 recorded events


### User

_source line 1965 · 2026-05-23T13:54:47.889343+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**总结**：评分 Overall 3.5 (Borderline Conference)，Soundness 4.0/5。论文的统计方法论在 NLP 领域属顶级水准（McNemar + BH + TOST + Bootstrap + Power analysis 全套），oracle control 和 27 种 remediation 变体的系统化测试设计精巧。主要问题：(1) Contribution 3 (capability-gap pattern) 仅基于 n=6 且 4/6 共享 verifier，不足以作为 top-level 贡献；(2) 10/16 条件 underpowered，Abstract 的负面结论表述需更精确；(3) Bias Ratio 的诊断独立价值与 Observation 1 存在概念循环；(4) cross-architecture escape 可能只是 ensemble diversity 效应。

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

_source line 1966 · 2026-05-23T13:54:52.770142+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director"
}
```

</details>

---


## Round 141

## Round 141

6 recorded events


### User

_source line 1967 · 2026-05-23T13:56:50.173153+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告：新颖性与完整性

**论文标题**: Beyond Self-Consistency: Self-Extracted Constraints Provide No Detectable Improvement in LLM Reasoning

---

## Summary

本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM chain-of-thought traces 中提取逻辑约束，通过 Z3 验证后用加权 MAX-SAT 选择答案。核心发现是 negative result：SICA 在 6 个模型（7B–32B）、3 个推理数据集上均未显著优于 majority voting（self-consistency）。论文将此诊断为"symbolic confirmation bias"（SCB）——自提取约束系统性地追踪模型自身的答案分布而非提供独立信号。27 种 training-free 修补策略均失败。跨架构验证（DeBERTa NLI）在最弱生成器上显示初步逃逸（+6.67pp）。提出三个零成本诊断指标（K_eff, BR, C₀）。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 实验方法论扎实（TOST 等价检验、BH 校正、60 个条件），但部分核心 claim 的证据支撑不足（详见 N1–N3） |
| **Excitement** | 2.5/5 | Negative result 有价值但核心洞见（自提取信息无独立性）在 Huang et al. (2024) 之后并不令人惊讶；诊断框架实用但增量有限；cross-architecture escape 过于初步 |
| **Reproducibility** | 4/5 | 实验设置详细（Appendix A–B），参数完整，prompts 提供，数据集公开；但代码未提供 |

**Overall Assessment**: **3.0 — Findings**

**Confidence**: 4/5（仔细阅读全文及附录，熟悉 self-consistency、neuro-symbolic reasoning、ensemble diversity 相关文献）

**一句话总结**: 实验执行扎实的 negative result 论文，但核心发现（自提取约束缺乏独立性）在已有文献下可预见性较高，SCB 概念相对 Huang et al. (2024) 的增量有限，且存在两条引用元数据严重错误的问题。

---

## 主要优势

1. **实验规模与严谨性**：60 个实验条件（6 模型 × 3 数据集 × 多策略），TOST 等价检验、BH 多重校正、bootstrap CI、McNemar 检验等统计方法运用得当，远超多数 negative result 论文的证据标准。

2. **结构化诊断**：Observation 1（source-attribution scoring 下 SICA 退化为 majority vote）和 Remark 1（M→T→A→C Markov chain 的 DPI bound）提供了 beyond-empirical 的形式化分析，使 negative result 从"不 work"提升到"为什么不 work"。

3. **全面的修补策略排除**：27 种 training-free 变体（4 大类）系统性地排除了 prompting、extraction、constraint-level 干预、aggregation 变体，增强了 negative result 的 convincingness。

4. **诊断框架的实用性**：K_eff、BR、C₀ 三个指标零成本可计算，在 60 个条件上 correctly characterize failure modes（Section 5.3），对从业者有直接实用价值——可在部署前判断自提取约束是否值得尝试。

5. **Cross-architecture escape 提供了 constructive direction**：虽然初步，但 capability-gap pattern 为后续研究指明了方向（需要结构独立的验证器）。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 两条引用存在严重元数据错误，疑似部分 hallucinated

- 具体位置：References, Section 2 Related Work
- 问题：
  - `byerly2026selfconsistency`：引用为 "Nicholas Byerly and Daniel Khashabi, 2026, Self-Consistency Falls Short! Analyzing the Effectiveness and Limitations of Self-Consistency in Mathematical Reasoning"。经查证，arXiv:2411.01101 的实际作者是 **Adam Byerly**（非 Nicholas），发表于 **2024 年**（非 2026），实际标题是 "Self-Consistency Falls Short! The Adverse Effects of **Positional Bias on Long-Context Problems**"——主题完全不同。作者名、年份、标题/主题三重错误。
  - `dupo2025`：引用为 "Yang, Chenxu and others, 2025, DuPO: Dual Process Optimization for Scalable Self-Correction of LLMs, arXiv:2508.14460"。经查证，arXiv:2508.14460 的实际标题是 "DuPO: Enabling Reliable LLM Self-Verification via Dual **Preference** Optimization"（非 "Process"），第一作者是 **Shuaijie She**（非 Yang Chenxu），且 Yang Chenxu 不在作者列表中。
- 为什么影响接收：引用准确性是学术诚信的基本要求。两条引用的作者名和标题/主题均与实际论文不符，reviewer 有理由怀疑这些引用细节是 LLM 生成而非人工核实。这在 double-blind 审稿中尤其严重——审稿人无法信任未核实的引用来评估 related work 覆盖度。
- 建议修改方向：核实并修正所有 2025–2026 年引用的作者、标题、年份、arXiv ID 是否匹配。建议对全部参考文献进行系统性交叉验证。

**N2** [critical] "Advances beyond Huang et al. (2024)" 的 claim 过度

- 具体位置：Abstract ("advancing beyond Huang et al. (2024)'s findings to formal self-verification")、Section 2 第 3 段（"SCB further advances beyond..."列出三点 (a)(b)(c)）、Section 7 Discussion ("advancing beyond Huang et al. (2024)'s empirical findings to formal self-verification")
- 问题：论文在至少三处声称"advances beyond"Huang et al. (2024)，但实际增量需要更审慎的表述：
  - Huang et al. (2024) 已经在 ICLR 2024 建立了 "LLMs cannot self-correct reasoning without external feedback" 这一核心结论。本文的贡献是将这一洞见扩展到 formal symbolic verification 场景，并提供了 Markov chain 形式化——这是 scope extension 和 formalization，而非 fundamental insight 上的 "advance beyond"。
  - SCB 的三点"advance"（formalization、diagnostics、exclusion scope）中，(a) 形式化是有价值的但 Observation 1 本质上是在说 "same model, same information"——这在 Condorcet Jury Theorem 框架下是 expected；(b) diagnostics 是实用贡献但量级是 incremental；(c) 27 variants 的排除是工程贡献。
  - 核心洞见——自提取信息缺乏独立性——在 Huang et al. (2024) + Condorcet framework 下是 predictable 的，而非 surprising。
- 为什么影响接收：Excitement 评分直接取决于 novelty claim 是否成立。如果 SCB 是 Huang et al. 的 "formal instantiation" 而非 "advance beyond"，论文的贡献定位需要调整。
- 建议修改方向：将 "advances beyond" 改为更准确的表述如 "extends ... to the formal verification setting" 或 "provides structural formalization of"。明确区分 scope extension vs. fundamental advance。

**N3** [critical] Cross-architecture escape 的证据过于薄弱以支撑其作为独立贡献的定位

- 具体位置：Section 6, Table 3, Section 7
- 问题：
  - 主要证据仅来自 1 个 verifier family（DeBERTa NLI 的 3 个变体）、4 个 generator、2 个数据集。
  - "Capability-gap pattern"（Table 3）的单调递减关系基于仅 4 个数据点（Mistral-7B, LLaMA-3.1-8B, Qwen2.5-14B, Qwen3-14B），Spearman ρ=1.0 在 n=4 时不具统计说服力（p=0.003 来自精确排列检验，但 n=4 的排列空间仅 24 种，且单调排列概率本身为 1/24≈4.2%）。
  - Zero-shot DeBERTa NLI standalone accuracy 仅 49.51%（FOLIO）和 55.00%（ProofWriter），只有当 generator SC < verifier standalone accuracy 时才有显著增益——这是一个 trivial 的 capability gap 条件，而非深刻的 insight。
  - Domain-adapted verifier（99.67% standalone）的结果引入了 training，论文自己也承认 "serve as directional evidence ... rather than a proposed method"。
- 为什么影响接收：论文将 cross-architecture escape 列为三大贡献之一（Contribution 3），但证据仅够称为 "preliminary observation"。如果其他 reviewer 也认为 Contribution 1（negative result）的新颖性有限，那么一篇以两个 preliminary contributions 为主体的论文难以达到 Conference 水平。
- 建议修改方向：将 Contribution 3 降级为 "preliminary evidence suggesting..."，或增加更多 verifier families 和 generator-verifier pairs 的实验。至少应在不同的 verification paradigm（非 NLI）上复现 capability-gap pattern。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Abstract 超过 200 词限制

- 具体位置：Abstract（第 1 页）
- 问题：经过去除 LaTeX 命令后的词数统计为约 202 词，超过 EMNLP 2026 的 200-word 硬约束。虽然仅超出 2 词，但这是明确的格式违规。
- 建议：删减 1-2 个修饰词或合并短句。例如 "across nine models, 7B to frontier" 可简化为 "across nine models"。

**W2** [warning] 部分 claim 存在 underpowered test 问题

- 具体位置：Abstract ("No Detectable Improvement"), Table 1, Section 4
- 问题：
  - 标题和 Abstract 中 "No Detectable Improvement" 是一个 strong negative claim，但 TOST 等价检验仅在 4/6 powered conditions 上确认等价（±2pp），另外 10 个条件因样本量不足而 underpowered（Table 6, Appendix D 显示 power < 21%）。
  - 论文在 abstract 中提到 "ten conditions remain underpowered"——这是正确的，但标题仍然以 "No Detectable Improvement" 作为 blanket claim。
  - Table 1 中 Mistral-7B 在 FOL.IO(x1235) 条件下有 marginally significant degradation（Δ = -2.94pp, raw p = 0.112），但 Qwen2.5-14B 在 FOLIO 上也显示类似模式。
- 建议：考虑在标题或 abstract 中加入更多 hedging，如 "No Detectable Improvement in Most Tested Conditions" 或明确标注 underpowered conditions 的比例。

**W3** [warning] Turpin et al. 引用年份错误

- 具体位置：References (`turpin2024language`)
- 问题：Turpin et al. "Language Models Don't Always Say What They Think" 发表于 **NeurIPS 2023**，非 2024。bib 条目中 year 字段错误。
- 建议：修正为 `year={2023}`。

**W4** [warning] "Symbolic Confirmation Bias" 是否过度命名

- 具体位置：Section 5.1, throughout
- 问题：论文给一个在构造上可预期的现象（同一模型提取的约束反映模型自身的分布偏好）赋予了一个 dramatic 的名称 "symbolic confirmation bias"。在心理学中，confirmation bias 指人类主动寻找支持已有信念的证据并忽视反面证据。而 SCB 更准确的描述是 "information bottleneck under self-referential extraction"——模型不是"主动寻找"支持性约束，而是因为约束和答案来自同一信息源（M→T→A→C）而结构性地耦合。
  - 论文在 Section 5.1 提供了 BR > 1 的实证和 Observation 1 的形式化——这些是好的，但 "bias" 这个词暗示了一种 correctable deficiency，而实际上这更像一个 structural limitation。
- 建议：在首次定义时更明确地说明这是 structural limitation 而非 cognitive bias 的类比，或考虑使用更精确的术语如 "symbolic information collapse" 或 "self-referential degeneracy"。

**W5** [warning] 论文密度过高，可读性受损

- 具体位置：main.tex（`\enlargethispage{6\baselineskip}`、多处 `\vspace` 负值）
- 问题：正文通过 aggressive spacing hacks 将大量内容压入 8 页。这导致：
  - 部分 section 过于压缩（Section 7 Discussion and Conclusion 仅约 1/3 页）
  - Figure 4 包含 27 种策略的 barplot，信息密度极高但难以快速 parse
  - 缩略语密集（SICA、SCB、BR、C₀、K_eff、CCR、DRC），增加认知负荷
- 建议：考虑将 Figure 4 的详细数据移入 appendix，在正文保留总结性描述。Section 5.2 和 5.3 可以更简洁，将 remediation 的详细分析放入 appendix。

---

## 小问题（不影响接收）

1. **Table 2 Gemini-2.5-Pro 的 n_err 很小**（n_err = 10, Table 2 page 6）：BR 值 1.79 基于仅 10 个错误实例，置信区间必然很宽，不应与 n_err=196 的 Mistral-7B 同等权重解读。建议在文中注明。

2. **Figure 3 的 Causal DAG**：M→T→A→C→S 链中，箭头方向和 approximate conditional independence（C ⊥⊥ Y | A）的标注有些突兀——没有足够的正文空间解释 DAG 的 causal assumptions 是否合理（例如，是否真的没有 C→Y 的直接路径？约束验证不影响最终答案？）。

3. **Appendix K "Extraction Error Taxonomy"**（page 16）提到 "91.8% of constraints are technically discriminative"但"only 8.2% are non-discriminative"——这与正文 Section 5.1 中 "constraints track distributional frequency rather than logical validity" 的 narrative 之间需要更好的 reconciliation。如果约束是 discriminative 的，为什么不提供额外信号？

4. **Section 3.1 中 α = 0.5 的选择**（page 3-4）："the selected answer is a* = arg max_a score(a), and α = 0.5"——α 的选择对结果的 sensitivity 未在正文中讨论（虽然 Appendix L.2 有 temperature sensitivity 分析）。

5. **Related Work 缺少 OpenAI reasoning models 的显式讨论**：o1/o3 系列是 test-time compute scaling 最著名的实例，论文引用了 DeepSeek-R1 和 Qwen-QwQ 但未提及 OpenAI 的工作，这在 2026 年的论文中是一个明显遗漏。

---

## Missing References

1. **OpenAI o1/o3 reasoning models**：test-time compute scaling 的开创性工作，应在 Section 2 "Test-time compute" 段落中引用。

2. **Ensemble diversity 的经典文献**：除 Kuncheva & Whitaker (2003) 外，Krogh & Vedelsby (1995) "Neural Network Ensembles, Cross Validation, and Active Learning" 是 ensemble diversity 的理论基础之一，可能值得引用。

3. **Process reward models 的更多近期工作**：Lightman et al. (2024) 已引用，但 Wang et al. (2024) Math-Shepherd 等工作在 verification 的 granularity 上有相关讨论。（注：检查后发现 wang2024mathshepherd 已在 Section 2 最后一段引用——此条撤回。）

---

## Questions for Authors

1. 如果将 SICA 的约束用于 re-prompting（而非 MAX-SAT scoring），结果是否不同？论文测试了 27 种 training-free 策略，但似乎都在 extraction-aggregation paradigm 内，是否尝试过将约束 feedback 回模型？

2. Observation 1 的条件 |C'| = 0（所有约束被所有 trace 满足）在实践中多频繁？Table 1 的 Appendix D 提供了一些数据，但正文中应更清楚地量化 degeneration 的频率。

3. 论文声称 K_eff ≤ 1.30 是 "insufficient" 的阈值——这个阈值是如何选定的？是否有理论依据，还是从数据中 calibrated？

4. 对于 frontier models（Table 2 的 Gemini-2.5-Pro），SCB 是否仍然 holds？n_err=10 是否太小以得出结论？

---

## 格式合规性检查

| 项目 | 状态 | 备注 |
|------|------|------|
| 正文 ≤ 8 页 | ⚠️ 边界 | 正文至 Section 7 结束约占 8 页，但使用了 `\enlargethispage{6\baselineskip}` 人为扩展页面 |
| Limitations section 在正文中 | ✅ | 位于 Section 7 之后、References 之前 |
| Abstract ≤ 200 words | ❌ | 约 202 词，超出 2 词 |
| Double-blind | ✅ | 未发现匿名性违规 |
| 引用格式一致性 | ⚠️ | 3 条引用存在错误（详见 N1, W3） |
| ACL style template [review] | ✅ | 使用 `\usepackage[review]{acl}` |

---

## Overall Assessment

**评分：3.0 (Findings)**

**理由**：

这是一篇实验执行质量高、方法论严谨的 negative result 论文。60 个条件、9 个模型、27 种修补策略的系统排除确实超出了多数同类工作的标准。Observation 1 的形式化和三个诊断指标对从业者有实用价值。

但论文在 excitement 维度存在根本性限制：核心洞见（自提取信息因与答案来自同一信息源而缺乏独立性）在 Huang et al. (2024) 和 Condorcet Jury Theorem 的框架下是可预见的。论文的贡献更多是 confirmation（用大规模实验确认了一个 expected result）和 formalization（Markov chain model），而非 discovery。Cross-architecture escape 作为 constructive contribution 过于初步（n=6 conditions, 1 verifier family）。

两条引用的元数据严重错误（错误的作者名、错误的标题/主题）是一个额外的 red flag，需要在 camera-ready 之前彻底修正。

如果 N1（引用问题）得到修正、N2（novelty claim）得到 tempered、W1（abstract 词数）得到修正，本文作为 Findings 论文是合适的——它为社区提供了有价值的 negative evidence 和实用的诊断工具。但以目前的 novelty framing，不足以支撑 Conference（main）接收。

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

_source line 1968 · 2026-05-23T13:57:43.778969+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix (N1-N3)、Should-Fix (W1-W5)、以及 Overall Assessment 中的关键判断，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注以下分歧点：\n1. R2 给出 3.0 (Findings) vs 你的 3.5 (Borderline Conference)——你是否同意 R2 对 novelty 的更低评价？\n2. R2-N1 发现两条引用存在严重元数据错误（byerly2026selfconsistency 和 dupo2025）——你是否能在论文中确认这些错误？\n3. R2-N2 认为 \"advances beyond Huang et al.\" 的 claim 过度——你的 assessment 中未涉及此点，你同意吗？\n4. R2-W4 认为 \"symbolic confirmation bias\" 是过度命名——你在 W1 中讨论了 BR 的概念循环问题，这两个批评是否指向同一个根本问题？\n\n---\n\n## Reviewer 2 完整审稿原文\n\n### Summary\n本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM chain-of-thought traces 中提取逻辑约束，通过 Z3 验证后用加权 MAX-SAT 选择答案。核心发现是 negative result：SICA 在 6 个模型（7B–32B）、3 个推理数据集上均未显著优于 majority voting（self-consistency）。论文将此诊断为\"symbolic confirmation bias\"（SCB）——自提取约束系统性地追踪模型自身的答案分布而非提供独立信号。27 种 training-free 修补策略均失败。跨架构验证（DeBERTa NLI）在最弱生成器上显示初步逃逸（+6.67pp）。提出三个零成本诊断指标（K_eff, BR, C₀）。\n\n### 官方维度打分\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 2.5/5 |\n| Reproducibility | 4/5 |\n| Overall | 3.0 (Findings) |\n| Confidence | 4/5 |\n\n### Must-Fix (N1-N3)\n\n**N1** [critical] 两条引用存在严重元数据错误，疑似部分 hallucinated\n- `byerly2026selfconsistency`：引用为 \"Nicholas Byerly and Daniel Khashabi, 2026\"，但 arXiv:2411.01101 实际作者是 Adam Byerly，发表于 2024，标题和主题完全不同。\n- `dupo2025`：引用为 \"Yang, Chenxu and others, 2025, DuPO: Dual Process Optimization\"，但实际标题是 \"DuPO: Enabling Reliable LLM Self-Verification via Dual Preference Optimization\"，第一作者是 Shuaijie She，非 Yang Chenxu。\n- 作者名、年份、标题/主题三重错误。\n\n**N2** [critical] \"Advances beyond Huang et al. (2024)\" 的 claim 过度\n- 论文在 Abstract、Section 2、Section 7 至少三处声称 \"advances beyond\" Huang et al.\n- 核心洞见（自提取信息缺乏独立性）在 Huang et al. (2024) + Condorcet framework 下是 predictable 的\n- SCB 的三点 \"advance\"（formalization, diagnostics, exclusion scope）更准确的定位是 scope extension + formalization，而非 fundamental insight advance\n- 建议改为 \"extends ... to the formal verification setting\"\n\n**N3** [critical] Cross-architecture escape 的证据过于薄弱以支撑其作为独立贡献的定位\n- 主要证据仅来自 1 个 verifier family（DeBERTa NLI 的 3 个变体）、4 个 generator、2 个数据集\n- Capability-gap pattern 基于 4 个数据点，Spearman ρ=1.0 在 n=4 时统计说服力有限\n- Zero-shot DeBERTa standalone accuracy 仅 49.51%/55.00%，\"generator < verifier 才有增益\" 是 trivial condition\n- Domain-adapted verifier 引入了 training，与 training-free 叙事线矛盾\n\n### Should-Fix (W1-W5)\n\n**W1** Abstract 超过 200 词限制（约 202 词）\n**W2** \"No Detectable Improvement\" 作为 blanket claim，但 TOST 仅 4/6 条件确认等价\n**W3** Turpin et al. 引用年份错误（应为 2023 非 2024）\n**W4** \"Symbolic Confirmation Bias\" 过度命名——更准确应为 structural limitation / information bottleneck\n**W5** 论文密度过高（\\enlargethispage{6\\baselineskip} + 多处负 vspace），可读性受损\n\n### Missing References\n- OpenAI o1/o3 reasoning models\n- Ensemble diversity 经典文献（Krogh & Vedelsby, 1995）\n\n### Overall Assessment: 3.0 (Findings)\n理由：核心洞见在 Huang et al. (2024) 下可预见；贡献更多是 confirmation + formalization 而非 discovery；cross-architecture escape 过于初步；两条引用元数据严重错误。作为 Findings 合适，但不足以支撑 Conference。"
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
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix (N1-N3)、Should-Fix (W1-W5)、以及 Overall Assessment 中的关键判断，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注以下分歧点：\n1. R2 给出 3.0 (Findings) vs 你的 3.5 (Borderline Conference)——你是否同意 R2 对 novelty 的更低评价？\n2. R2-N1 发现两条引用存在严重元数据错误（byerly2026selfconsistency 和 dupo2025）——你是否能在论文中确认这些错误？\n3. R2-N2 认为 \"advances beyond Huang et al.\" 的 claim 过度——你的 assessment 中未涉及此点，你同意吗？\n4. R2-W4 认为 \"symbolic confirmation bias\" 是过度命名——你在 W1 中讨论了 BR 的概念循环问题，这两个批评是否指向同一个根本问题？\n\n---\n\n## Reviewer 2 完整审稿原文\n\n### Summary\n本文提出 SICA（Symbolic Invariant Consensus Aggregation），从 LLM chain-of-thought traces 中提取逻辑约束，通过 Z3 验证后用加权 MAX-SAT 选择答案。核心发现是 negative result：SICA 在 6 个模型（7B–32B）、3 个推理数据集上均未显著优于 majority voting（self-consistency）。论文将此诊断为\"symbolic confirmation bias\"（SCB）——自提取约束系统性地追踪模型自身的答案分布而非提供独立信号。27 种 training-free 修补策略均失败。跨架构验证（DeBERTa NLI）在最弱生成器上显示初步逃逸（+6.67pp）。提出三个零成本诊断指标（K_eff, BR, C₀）。\n\n### 官方维度打分\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 2.5/5 |\n| Reproducibility | 4/5 |\n| Overall | 3.0 (Findings) |\n| Confidence | 4/5 |\n\n### Must-Fix (N1-N3)\n\n**N1** [critical] 两条引用存在严重元数据错误，疑似部分 hallucinated\n- `byerly2026selfconsistency`：引用为 \"Nicholas Byerly and Daniel Khashabi, 2026\"，但 arXiv:2411.01101 实际作者是 Adam Byerly，发表于 2024，标题和主题完全不同。\n- `dupo2025`：引用为 \"Yang, Chenxu and others, 2025, DuPO: Dual Process Optimization\"，但实际标题是 \"DuPO: Enabling Reliable LLM Self-Verification via Dual Preference Optimization\"，第一作者是 Shuaijie She，非 Yang Chenxu。\n- 作者名、年份、标题/主题三重错误。\n\n**N2** [critical] \"Advances beyond Huang et al. (2024)\" 的 claim 过度\n- 论文在 Abstract、Section 2、Section 7 至少三处声称 \"advances beyond\" Huang et al.\n- 核心洞见（自提取信息缺乏独立性）在 Huang et al. (2024) + Condorcet framework 下是 predictable 的\n- SCB 的三点 \"advance\"（formalization, diagnostics, exclusion scope）更准确的定位是 scope extension + formalization，而非 fundamental insight advance\n- 建议改为 \"extends ... to the formal verification setting\"\n\n**N3** [critical] Cross-architecture escape 的证据过于薄弱以支撑其作为独立贡献的定位\n- 主要证据仅来自 1 个 verifier family（DeBERTa NLI 的 3 个变体）、4 个 generator、2 个数据集\n- Capability-gap pattern 基于 4 个数据点，Spearman ρ=1.0 在 n=4 时统计说服力有限\n- Zero-shot DeBERTa standalone accuracy 仅 49.51%/55.00%，\"generator < verifier 才有增益\" 是 trivial condition\n- Domain-adapted verifier 引入了 training，与 training-free 叙事线矛盾\n\n### Should-Fix (W1-W5)\n\n**W1** Abstract 超过 200 词限制（约 202 词）\n**W2** \"No Detectable Improvement\" 作为 blanket claim，但 TOST 仅 4/6 条件确认等价\n**W3** Turpin et al. 引用年份错误（应为 2023 非 2024）\n**W4** \"Symbolic Confirmation Bias\" 过度命名——更准确应为 structural limitation / information bottleneck\n**W5** 论文密度过高（\\enlargethispage{6\\baselineskip} + 多处负 vspace），可读性受损\n\n### Missing References\n- OpenAI o1/o3 reasoning models\n- Ensemble diversity 经典文献（Krogh & Vedelsby, 1995）\n\n### Overall Assessment: 3.0 (Findings)\n理由：核心洞见在 Huang et al. (2024) 下可预见；贡献更多是 confirmation + formalization 而非 discovery；cross-architecture escape 过于初步；两条引用元数据严重错误。作为 Findings 合适，但不足以支撑 Conference。"
  }
}
```

</details>

---


### Tool result

_source line 1969 · 2026-05-23T13:58:18.400745+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 34621
}
```

</details>

---


### Tool call

_source line 1970 · 2026-05-23T13:58:18.551778+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "symb_invariant_consensus",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix (N1-N2)、Should-Fix (W1-W5)、以及 Overall Assessment 中的关键判断，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注以下分歧点：\n1. R1 给出 3.5 (Borderline Conference) vs 你的 3.0 (Findings)——你认为 R1 的评分是否过高？Soundness 4.0/5 是否合理？\n2. R1-W1 指出 BR 与 Observation 1 存在概念循环——这与你的 W4 (SCB 过度命名) 是否指向同一根本问题？\n3. R1-W5 指出 cross-architecture escape 可能只是 ensemble diversity 效应——你是否同意这是一个独立于你 N3 的额外问题？\n4. R1 认为 \"统计方法论极为扎实\"（Strength 1）——你是否同意这足以弥补 novelty 的不足？\n5. R1 未发现引用错误问题——你发现的 N1 是否改变了对 Soundness 的评价？\n\n---\n\n## Reviewer 1 完整审稿原文\n\n### 总体评分\nOverall: 3.5 (Borderline Conference)\nSoundness: 4.0/5, Excitement: 3.0/5, Reproducibility: 3/5, Confidence: 4/5\n\n### Must-Fix (N1-N2)\n\n**N1** [critical] Capability-gap pattern 基于 n=6 数据点且存在共享 verifier 问题，作为 Contribution 3 过度声明\n- 6 个 verifier-generator 组合中 4 个共享同一 DeBERTa verifier，实际有效自由度远小于 n=6\n- 虽然论文多次提及此限制，但 Abstract/Introduction/Section 6 标题仍以 contribution 级别呈现\n- 建议降级为 \"preliminary observation\"，或增加 2-3 个不同架构的 verifier\n\n**N2** [critical] 10/16 条件 underpowered，中心论断的表述需更精确\n- Table 6: observed power 均低于 21%，MDE 为 1.86-4.84pp\n- Abstract \"We find no evidence of improvement\" 可能被误读为 \"已证明无效果\"\n- 建议改为 \"no evidence of improvement exceeding ~2pp\" 或在 Discussion 中论证 <2pp 在 4.5× 开销下无实际价值\n\n### Should-Fix (W1-W5)\n\n**W1** BR 的诊断独立价值与 Observation 1 存在概念循环\n- Source-attribution scoring 下 BR > 1 是 trace-count 分布的必然结果\n- Permutation test 确认 BR_excess ≈ 0 (p > 0.7)——BR 完全由 trace-count 结构解释\n- \"Bias\" 暗示 extraction 过程有问题，但实际问题在评分机制\n- 建议区分 \"structural degeneration\" 和 \"extraction bias\"\n\n**W2** \"Pre-registered\" margin ±2pp 无注册凭证\n- 论文使用 \"pre-registered\" 但未提供 OSF 等预注册链接\n- 建议改为 \"pre-specified\" 或 \"predetermined\"\n\n**W3** BH correction 中 m=16 包含非独立条件\n- 16 个条件中有 seed aggregates 和 component seeds 的重叠\n- m 被人为膨胀，虽然更保守但方法论不够干净\n- 建议区分 confirmatory vs exploratory 条件\n\n**W4** Observation 1 条件 (iii) \"approximately uniform constraint yield\" 缺乏系统验证\n- 未报告 per-trace constraint yield 分布（均值、标准差、偏度）\n- 建议按 answer group 分层报告 yield 统计量\n\n**W5** Cross-architecture escape 可能只是 ensemble diversity 效应\n- DeBERTa-NLI 与 decoder-only LLM 在架构、训练数据上完全不同\n- Observed gain 可能是简单的 ensemble diversity 效应\n- 建议增加 non-NLI independent baseline 或明确承认 ensemble diversity confound\n\n### 主要优势（Reviewer 1 认可）\n1. 统计方法论极为扎实（McNemar + BH + TOST + Bootstrap + Power analysis 全套）\n2. Oracle control 设计精巧（+29.90pp FOLIO, +17.17pp PW, p < 10^-7）\n3. 27 种 remediation 变体的系统化测试\n4. 形式化声明命名克制得当（Observation/Remark 而非 Theorem）\n5. Diagnostic framework 有实践价值（prospective validation on held-out families）\n6. Entropy decomposition 分析精细\n\n### Missing References\n- Ensemble diversity 文献（Dietterich 2000, Krogh & Vedelsby 1994）\n- Cobbe et al. (2021) GSM8K verifier 的更深入对比\n\n### Overall Assessment: 3.5 (Borderline Conference)\n理由：方法论严谨的负面结果论文，统计设计远超同类工作，但核心正面贡献（cross-architecture escape）基于 n=6 且存在共享 verifier 问题，诊断框架的独立贡献有限。"
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
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix (N1-N2)、Should-Fix (W1-W5)、以及 Overall Assessment 中的关键判断，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注以下分歧点：\n1. R1 给出 3.5 (Borderline Conference) vs 你的 3.0 (Findings)——你认为 R1 的评分是否过高？Soundness 4.0/5 是否合理？\n2. R1-W1 指出 BR 与 Observation 1 存在概念循环——这与你的 W4 (SCB 过度命名) 是否指向同一根本问题？\n3. R1-W5 指出 cross-architecture escape 可能只是 ensemble diversity 效应——你是否同意这是一个独立于你 N3 的额外问题？\n4. R1 认为 \"统计方法论极为扎实\"（Strength 1）——你是否同意这足以弥补 novelty 的不足？\n5. R1 未发现引用错误问题——你发现的 N1 是否改变了对 Soundness 的评价？\n\n---\n\n## Reviewer 1 完整审稿原文\n\n### 总体评分\nOverall: 3.5 (Borderline Conference)\nSoundness: 4.0/5, Excitement: 3.0/5, Reproducibility: 3/5, Confidence: 4/5\n\n### Must-Fix (N1-N2)\n\n**N1** [critical] Capability-gap pattern 基于 n=6 数据点且存在共享 verifier 问题，作为 Contribution 3 过度声明\n- 6 个 verifier-generator 组合中 4 个共享同一 DeBERTa verifier，实际有效自由度远小于 n=6\n- 虽然论文多次提及此限制，但 Abstract/Introduction/Section 6 标题仍以 contribution 级别呈现\n- 建议降级为 \"preliminary observation\"，或增加 2-3 个不同架构的 verifier\n\n**N2** [critical] 10/16 条件 underpowered，中心论断的表述需更精确\n- Table 6: observed power 均低于 21%，MDE 为 1.86-4.84pp\n- Abstract \"We find no evidence of improvement\" 可能被误读为 \"已证明无效果\"\n- 建议改为 \"no evidence of improvement exceeding ~2pp\" 或在 Discussion 中论证 <2pp 在 4.5× 开销下无实际价值\n\n### Should-Fix (W1-W5)\n\n**W1** BR 的诊断独立价值与 Observation 1 存在概念循环\n- Source-attribution scoring 下 BR > 1 是 trace-count 分布的必然结果\n- Permutation test 确认 BR_excess ≈ 0 (p > 0.7)——BR 完全由 trace-count 结构解释\n- \"Bias\" 暗示 extraction 过程有问题，但实际问题在评分机制\n- 建议区分 \"structural degeneration\" 和 \"extraction bias\"\n\n**W2** \"Pre-registered\" margin ±2pp 无注册凭证\n- 论文使用 \"pre-registered\" 但未提供 OSF 等预注册链接\n- 建议改为 \"pre-specified\" 或 \"predetermined\"\n\n**W3** BH correction 中 m=16 包含非独立条件\n- 16 个条件中有 seed aggregates 和 component seeds 的重叠\n- m 被人为膨胀，虽然更保守但方法论不够干净\n- 建议区分 confirmatory vs exploratory 条件\n\n**W4** Observation 1 条件 (iii) \"approximately uniform constraint yield\" 缺乏系统验证\n- 未报告 per-trace constraint yield 分布（均值、标准差、偏度）\n- 建议按 answer group 分层报告 yield 统计量\n\n**W5** Cross-architecture escape 可能只是 ensemble diversity 效应\n- DeBERTa-NLI 与 decoder-only LLM 在架构、训练数据上完全不同\n- Observed gain 可能是简单的 ensemble diversity 效应\n- 建议增加 non-NLI independent baseline 或明确承认 ensemble diversity confound\n\n### 主要优势（Reviewer 1 认可）\n1. 统计方法论极为扎实（McNemar + BH + TOST + Bootstrap + Power analysis 全套）\n2. Oracle control 设计精巧（+29.90pp FOLIO, +17.17pp PW, p < 10^-7）\n3. 27 种 remediation 变体的系统化测试\n4. 形式化声明命名克制得当（Observation/Remark 而非 Theorem）\n5. Diagnostic framework 有实践价值（prospective validation on held-out families）\n6. Entropy decomposition 分析精细\n\n### Missing References\n- Ensemble diversity 文献（Dietterich 2000, Krogh & Vedelsby 1994）\n- Cobbe et al. (2021) GSM8K verifier 的更深入对比\n\n### Overall Assessment: 3.5 (Borderline Conference)\n理由：方法论严谨的负面结果论文，统计设计远超同类工作，但核心正面贡献（cross-architecture escape）基于 n=6 且存在共享 verifier 问题，诊断框架的独立贡献有限。"
  }
}
```

</details>

---


### Tool result

_source line 1971 · 2026-05-23T13:58:19.918931+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c338e034cbffa10b9cc723e731d288d8:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1367
}
```

</details>

---


### Assistant

_source line 1972 · 2026-05-23T13:58:25.492164+00:00_

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


## Round 142

## Round 142

2 recorded events


### User

_source line 1973 · 2026-05-23T13:58:28.044559+00:00_

[Reviewer 2 审稿结果]:
审稿完成。核心结论：

- **Overall: 3.0 (Findings)**，Soundness 3.5, Excitement 2.5
- **3 个 Must-Fix**：两条引用元数据严重错误（byerly2026 作者名/年份/主题三重错误，dupo2025 标题/作者错误）；"advances beyond Huang et al." claim 过度；cross-architecture escape 证据不足以支撑独立贡献
- **5 个 Should-Fix**：abstract 超 200 词、标题 negative claim vs underpowered tests、turpin2024 年份错误、SCB 命名过度、论文密度过高
- 实验执行质量高，适合作为 Findings 论文，但 novelty 不足以支撑 Conference main

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

_source line 1974 · 2026-05-23T13:58:32.120347+00:00_

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


## Round 143

## Round 143

2 recorded events


### User

_source line 1975 · 2026-05-23T14:00:30.684781+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: 引用元数据错误**

我在审稿中未覆盖引用验证（我的 focus 是方法严谨性）。现在验证 bib 条目：

1. `byerly2026selfconsistency`：bib 记录为 `author={Byerly, Nicholas and Khashabi, Daniel}, year={2026}`，无 arXiv ID。R2 称 arXiv:2411.01101 实际作者为 Adam Byerly，发表于 2024，主题不同。虽然 bib 中无 arXiv ID 直接对照，但 "Nicholas Byerly" 作为一作与 Daniel Khashabi 合著、标题为 "Self-Consistency Falls Short" 的 2026 年文章——如果 R2 确认该论文不存在或元数据严重错误，这是 fabricated/hallucinated citation 问题，对 double-blind 审稿论文而言是严重质量问题。

2. `dupo2025`：bib 记录为 `title={DuPO: Dual Process Optimization for Scalable Self-Correction of LLMs}, author={Yang, Chenxu and others}, arXiv:2508.14460`。R2 称实际论文标题为 "Enabling Reliable LLM Self-Verification via Dual Preference Optimization"，一作为 Shuaijie She。如果 arXiv:2508.14460 确实对应不同的标题和作者，这是标题、作者、甚至研究主题的三重错误。

这两条引用错误的模式（作者名、标题、年份多维度偏差）高度暗示 LLM-assisted 文献管理的 hallucination 问题。即使论文本身的方法论是扎实的，引用不可靠会严重损害学术信誉。我将此与 R2 同列为 must-fix。

**[AGREE with nuance] R2-N2: "Advances beyond Huang et al." 过度声明**

我在原始审稿中未涉及此点，现在补充评估。

R2 指出论文在 Abstract、Section 2 (Related Work)、Section 7 (Discussion) 三处使用 "advances beyond Huang et al. (2024)" 措辞。经核实：
- Abstract: "advancing beyond Huang et al. (2024)'s findings to formal self-verification"
- Introduction (§1): "advances beyond Huang et al. (2024)'s empirical findings, providing structural formalization and actionable diagnostics"
- Discussion (§7): "advancing beyond Huang et al. (2024)'s empirical findings to formal self-verification"

R2 的论点是：Huang et al. (2024) 已证明 LLMs cannot self-correct without external feedback，而本文的核心发现（self-extracted constraints 缺乏独立性）在 Huang et al. + Condorcet 框架下是可预见的。

我**部分同意**。具体来说：
- **同意 R2 的核心判断**：the high-level insight (self-extraction ≈ no independence ≈ no gain) IS predictable from Huang et al. + Condorcet。论文的贡献更准确地说是 (a) 将此洞见扩展到形式化验证 setting，(b) 提供了 formalization (Observation 1, Remark 1)，(c) exhaustively 排除了 27 种 remediation。
- **不完全同意 R2 的措辞建议**：R2 建议改为 "extends ... to the formal verification setting"。我认为可以保留一定的 "advance" 语义，但应明确限定：例如 "extends and formalizes Huang et al.'s empirical findings in the context of formal self-verification"。

关键区别：Huang et al. 是纯经验性的（show LLMs can't self-correct），本文提供了 structural explanation (Observation 1 的 argmax preservation + Remark 1 的 DPI bound)。这不只是 scope extension，还有 formalization 层面的推进。但 "advances beyond" 确实暗示了 fundamental insight novelty，这过强了。

**[AGREE] R2-N3: Cross-architecture escape 证据薄弱**

与我的 N1 指向同一问题。R2 的表述更为精确：
- 我说 n=6（counting 3 verifiers × Mistral + 3 generators × DeBERTa），R2 聚焦主表 Table 3 的 n=4 generators。两种计算方式都证明数据点不足。
- R2 额外提出的重要点是 "generator < verifier 才有增益" 可能是 **trivial condition**——这是一个我遗漏的好观察。当 DeBERTa standalone = 55.00%，Mistral SC = 39.33% 时，增益几乎是"用一个更好的模型替代一个更差的模型"的必然结果，不需要 "information independence" 理论来解释。
- R2 关于 domain-adapted verifier 引入 training 与 training-free 叙事矛盾的批评也是准确的。论文在 Section 6 最后一段承认了这一点（"Domain-adapted verification... these results serve as directional evidence... rather than a proposed method"），但叙事结构仍将其作为 escape 的证据呈现。

补充我原始审稿中 W5 的观点：cross-architecture escape 可能只是 ensemble diversity 效应。R2 的 "trivial condition" 论点进一步支持了这个解释——不需要 information bottleneck 理论，简单的 "better model helps" 就足够了。

---

### Should-Fix 问题

**[AGREE] R2-W1: Abstract 超过 200 词**

EMNLP 2026/ARR 规定 abstract ≤ 200 words。我未在原始审稿中检查此项（我的 focus 是方法论），但这是硬性格式违规。

**[AGREE] R2-W2: "No Detectable Improvement" blanket claim**

与我的 N2 指向同一问题。R2 说 "TOST 仅 4/6 条件确认等价"——准确来说是 4/16（Table 1 有 16 个条件），10 个 underpowered。R2 的数字可能指 Table 6 的 3 个 confirmatory + TOST equivalent 条件，但具体数字不影响核心判断：论文的 blanket claim 超出了统计证据支撑的范围。

**[AGREE] R2-W3: Turpin et al. 年份错误**

已验证：`references.bib` 记录 `year={2024}, booktitle={NeurIPS}`。Turpin et al. "Language Models Don't Always Say What They Think" 发表于 NeurIPS 2023，非 2024。这是一个 factual error。

**[AGREE] R2-W4: "Symbolic Confirmation Bias" 过度命名**

这与我的 W1 (BR 的诊断独立价值与 Observation 1 的循环) 指向**同一根本问题**。

R2 的论点更直接：应叫 "structural limitation" 而非 "bias"。我的 W1 从数学角度论证了相同观点——permutation test 显示 BR_excess ≈ 0 (p > 0.7, §5.1)，意味着经验 BR 完全由 trace-count 结构解释，没有 extraction-level 的额外偏差。

两个批评的汇合点是：
1. "Bias" 这个词暗示 extraction 过程引入了系统性偏差（an active distortion）
2. 但数据显示这只是 source-attribution scoring 机制的结构性后果（a passive consequence）
3. 更准确的命名应该是 "structural degeneration" 或 "scoring mechanism artifact"
4. 这不是说论文的发现不重要——structural degeneration IS the finding——而是命名造成了误导性暗示

与 R2 同意这至少是 should-fix 级别。论文的 narrative 建立在 "bias" 这个有强烈暗示性的词之上（标题都没用但正文反复使用），一个更准确的术语不会削弱发现本身，但会提高概念精确度。

**[AGREE, minor] R2-W5: 论文密度过高**

LaTeX source 确认存在 `\enlargethispage{6\baselineskip}` (main.tex:72)、`\vspace{-4mm}` (main.tex:76)、`\vspace{-1.5mm}` (main.tex:73) 等排版 hacks。这些操作暗示内容超出了 8 页预算。但考虑到负面结果论文需要 exhaustive 证据来令人信服，内容密度一定程度上是合理的。建议将部分 Table 1 的 seed-level 重复条目移入 Appendix 以节省空间。

---

### Missing References

**[AGREE] Ensemble diversity 文献**

我在原始审稿中也提到了这一点（Missing References 部分）。R2 指定 Krogh & Vedelsby (1995)，我提到了 Dietterich (2000)。两者指向同一缺口：Section 6 的 cross-architecture escape 本质上是 model ensemble，需要与 ensemble diversity 理论对话。

**[PARTIAL AGREE] OpenAI o1/o3 reasoning models**

论文已在 Table 2 (§5.1) 中包含 o3 的 cross-model extraction 结果 (BR = 1.66, Δ = 0.00)。但 R2 可能指的是对 o1/o3 内部 reasoning chain 机制的讨论——这些模型的 chain-of-thought 是 internalized 的，SICA 的 extraction paradigm 可能根本不适用。Related Work 中确实缺少对这类 reasoning model 的讨论。

---

### Overall Assessment 分歧：R2 的 3.0 vs 我的 3.5

**经过交叉审阅，我将我的评分从 3.5 下调至 3.0 (Findings)**。理由：

1. **引用错误** (R2-N1)：如果两条引用确认为 hallucinated/严重错误元数据，这是不可忽视的学术质量问题。我原始审稿未检查引用，低估了这个风险。

2. **Novelty 重新评估**：R2 说服我，核心洞见在 Huang et al. + Condorcet 框架下确实是 predictable 的。论文的价值更多在于 (a) systematic empirical confirmation，(b) formalization，(c) exhaustive remediation testing——这些是 solid Findings 级别的贡献，但不构成 Conference 级别的 novelty。

3. **Cross-architecture escape 的 trivial condition 问题**：R2 的 "generator < verifier 才有增益是 trivial" 论点，加上我的 "可能只是 ensemble diversity" 论点，共同削弱了 Contribution 3 的独立价值。

4. **我仍然坚持的优势**：统计方法论的水准（McNemar + BH + TOST + Bootstrap + Power analysis 的完整组合）在 NLP 论文中极为罕见。27 种 remediation 的穷举测试、oracle control、regime-based diagnostic framework 有独立的实践价值。这些使论文适合 Findings 而非 reject。

**修正后评分**：
| 维度 | 修正前 | 修正后 | 修正理由 |
|------|--------|--------|----------|
| Overall | 3.5 | 3.0 | R2 的 novelty 和引用问题论点有说服力 |
| Soundness | 4.0 | 3.5 | 引用错误降低整体 rigor 评估；BR 命名问题更明确 |
| Excitement | 3.0 | 2.5 | 接受 R2 的 predictability 论点 |
| Reproducibility | 3 | 3 | 不变 |
| Confidence | 4 | 4 | 不变 |

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

_source line 1976 · 2026-05-23T14:00:35.010420+00:00_

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


## Round 144

## Round 144

20 recorded events
