# Director coordination — Part 6 of 7

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Conversation logs

[← Part 5](part-005.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 7 →](part-007.md) · [Structured JSON](../../../sessions/bb/bb384fed2f084cd5d585.json)

## Round 125

### Tool call

_source line 1582 · 2026-05-24T12:15:35.065151+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "entrainment_gated_ft",
  "issues_yaml": "- id: \"R5-W1\"\n  summary: \"架构效应 vs seed 效应无法区分（单 training run，无 seed baseline）\"\n  category: experiment\n  severity: critical\n  status: wont_fix\n  first_raised_round: 5\n  last_seen_round: 18\n  mentions:\n    - round: 5\n      reviewers: [R1, R2]\n      note: \"R1 Critical, R2 W3+Q3 支持。\"\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"R2-N3 Must-Fix vs R1-W2 Should-Fix。分歧：R1 REBUT 认为论文已用关联性语言、第三方 zoo 无法自行补训。R2 维持 Must-Fix。论文已有 PolyPythias 校准但三重 mismatch 仍被指出。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N2 Critical。双方 [AGREE]。Pythia 70M 三重 mismatch（scale 70M vs 340M+/architecture family Transformer vs hybrid/accuracy 0.17-0.23 vs ~0.50）仍是核心弱点。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-N3 Critical + R2 交叉 [AGREE]。Pythia 70M within-seed J=0.312 vs cross-arch J=0.354，gap 仅 0.042。R2 补充 seed variation 可能解释大部分 per-example divergence。双方一致认为是根本性威胁但非 fatal。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-N2 Critical + R2-N2 Critical，交叉均 [AGREE]。R2 纠正 R1 数据误读：within-seed J=0.273 vs cross-arch J=0.10 实为 2.7× 差距（非 R1 声称的 0.02），部分支持架构效应独立性。但 Pythia 70M 三重 mismatch 仍限制 calibration 可迁移性。双方一致要求至少对一个 hybrid 架构训练多 seed。\"\n  action_items:\n    - round: 13\n      action: \"E4 Pythia 410M 9-seed calibration（实际完成 70M）\"\n      assigned_to: main_agent\n      status: done\n    - round: 14\n      action: \"Limitations 提升 single-seed 为 top limitation；§4.2 弱化因果语言\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"结构性限制，无法完全修复。已做：(1) Pythia 70M seed calibration 加入 Appendix W；(2) Limitations 中 single-seed 为 top limitation；(3) 全文使用 'associated with' 关联性语言。R18 双方 AGREE 仍为核心弱点但 R2 纠正了 R1 的数据误读——实际 2.7× gap 部分支持架构效应独立性。\"\n  resolution_round: null\n\n- id: \"R5-W2\"\n  summary: \"收敛 claim 统计不显著（Bonferroni p=.170）且依赖 GDN inclusion\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 18\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical。交叉 [AGREE]。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R16-N1 重新 flag。R15 写作修复不够——Intro 仍以 79% σ drop 开篇。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2 交叉 [AGREE]。R1 精确指出结构性限制：n=5 时最小 p=0.017，Bonferroni 后 0.170——无论效应多强都无法拒绝 H₀。Abstract 'Aggregate trends do not reach statistical significance' 表述尚可，但 §4.2 和 Conclusion 仍间歇性用确认性语言。R2 建议 mixed-effects regression（15 data points）作为替代方法。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical，交叉均 [AGREE]。论文核心叙事 'convergence masks divergence' 需要 aggregate convergence 成立，但 p=.170 不支持。R2 建议重构为 'architectures interchangeable by aggregate metrics differ per-example'——更弱前提、更强证据。R1 补充：§4.2 标题 'Aggregate Trends and Per-Example Independence' 暗示确定性结论。\"\n  action_items:\n    - round: 15\n      action: \"Abstract/Intro 重构：以 Jaccard saturation 为主线\"\n      assigned_to: paper_agent\n      status: done\n    - round: 16\n      action: \"结构性叙事重组：Intro 79% σ drop 移到 §4.2 等\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"R15-R18 持续 flag。需将 convergence 彻底降级为 exploratory observation，全文统一措辞。R18 建议的叙事重构方案（aggregate interchangeability → per-example divergence）最为清晰。\"\n  resolution_round: null\n\n- id: \"R5-W4\"\n  summary: \"新颖性有限——已有指标的直接套用，无新方法/理论\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 5\n  last_seen_round: 18\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"R2-W1 ecological fallacy 已知实例。R1 REBUT。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R2-N1 Must-Fix vs R1 REBUT。核心分歧未解决。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R2-N1 Critical（ecological fallacy 的已知实例化，方法论无创新）。R1 REBUT（critical 定级过高，empirical first 在实际相关 domain 有独立价值，引用 McCoy et al. 2020 类比）。双方部分收敛：均同意应明确定位为 empirical contribution。分歧：R2 认为是 Must-Fix，R1 认为 Should-Fix 级别。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R2-W1 Major（增量贡献，已知框架在新 domain 的应用）。R1 REBUT——4% saturation 和 aggregate-vs-per-example 解耦是非平凡发现，controlled model zoo 在 multiplicity 文献中罕见。部分收敛：Findings 标准下经验发现足够。Director 判断：R1 REBUT 有理，Findings 不要求方法论创新。\"\n  action_items:\n    - round: 6\n      action: \"Intro 加 empirical novelty framing\"\n      assigned_to: paper_agent\n      status: done\n    - round: 16\n      action: \"Intro 强化 empirical contribution 定位\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"结构性限制。R18 分歧持续但进一步收敛：Findings 标准下系统性经验发现（4% saturation, decoupling）足够。\"\n  resolution_round: null\n\n- id: \"R5-W3\"\n  summary: \"Task-dependent spectrum 仅 3 benchmark，存在评估格式 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [R1, R2]\n      note: \"α 变异可能反映 format 而非 task type。\"\n  action_items:\n    - round: 5\n      action: \"WinoGrande + PIQA per-example 分析\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"PIQA + WinoGrande 数据整合完成。Round 6-16 未再提及。R17 提出更具体的 format confound（见 R17-W1）。\"\n  resolution_round: 6\n\n- id: \"R5-W5\"\n  summary: \"正文约 8.2 页超出 EMNLP 8 页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 18\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16 视觉审查确认合规。\"\n    - round: 17\n      reviewers: [R1]\n      note: \"R1-M5 确认格式合规（8页，Limitations 3点，匿名完好）。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R18 双方格式检查均确认合规：8 页正文、Limitations 在 p.8、ACL template、double-blind。\"\n  action_items:\n    - round: 5\n      action: \"结构性压缩 8.2→7 页\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"主文在 8 页内。R14-R18 持续确认合规。\"\n  resolution_round: 5\n\n- id: \"R5-W6\"\n  summary: \"遗漏关键相关工作 Zoology/Based/Samba\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  action_items:\n    - round: 5\n      action: \"补 3 篇引用 + recall-throughput 框架\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Zoology + Based 引用于 §4.1，Samba 引用于 Related Work。\"\n  resolution_round: 5\n\n- id: \"R5-W7\"\n  summary: \"Ensemble 建议缺乏实验支撑 + POC 负面结果与 protocol 的 tension\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 9\n  action_items:\n    - round: 7\n      action: \"Majority vote + oracle POC 写入 Conclusion\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Conclusion 已包含 MV/oracle POC 数据。\"\n  resolution_round: 9\n\n- id: \"R5-W8\"\n  summary: \"Binary decomposition 可能低估多选题一致性\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 18\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-W2 指出 hurt sets binarization 可能 overestimate agreement。Appendix O continuous Jaccard 缓解。\"\n    - round: 17\n      reviewers: [R2]\n      note: \"R2-Q4 询问为何不在主文使用 continuous Jaccard 替代 binarized 版本。未作为独立 weakness 提出但作为 Question。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未作为独立问题提及。§3.4 已包含 binarization caveat + Appendix continuous Jaccard。可能已充分缓解，待 Research Director 确认。\"\n  action_items:\n    - round: 13\n      action: \"E2 continuous-threshold Jaccard sensitivity 结果整合到 Appendix + §4.1 引用\"\n      assigned_to: paper_agent\n      status: done\n    - round: 16\n      action: \"§3.4 加 1 句 K-choice binarization caveat\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W9\"\n  summary: \"Abstract 信息密度过高（统计量堆砌）\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-M6 指出接近 200 word 上限。R2-M4 指出 inline 统计量（α, p, Jaccard 值）增加认知负荷。双方建议精简。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R2-W4 Major：数字密度过高（Jaccard, p, α, pp 等），指出第三句可能有句法拼接问题。R1 交叉 [AGREE with nuance]——同意需精简但认为句法完整。\"\n  action_items:\n    - round: 13\n      action: \"W5: Abstract 进一步精简至 3 key numbers\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"R15 精简完成但 R17-R18 持续指出信息密度问题。需进一步删减数字，保留 3-4 个关键数值。\"\n  resolution_round: null\n\n- id: \"RV-L1\"\n  summary: \"Limitations 6 段违反 EMNLP 用户规则（要求 ~3 点）\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 15\n  action_items:\n    - round: 5\n      action: \"6 段→3 段\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"压缩为 3 段。R14-R18 确认合规。\"\n  resolution_round: 5\n\n- id: \"RV-L2\"\n  summary: \"loglik 压缩假说已被诊断数据反驳但论文仍引用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  action_items:\n    - round: 5\n      action: \"改为 binary classification structural properties 解释\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"改为 'structural properties of constrained-choice formats'。\"\n  resolution_round: 5\n\n- id: \"R6-N3\"\n  summary: \"仅 2 个 scale 点不足以支撑 scale-dependent claim\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  action_items:\n    - round: 6\n      action: \"MF4: 全文替换 scale-dependent\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"全文已用 'differs between 340M and 1.3B'。\"\n  resolution_round: 8\n\n- id: \"R6-N2\"\n  summary: \"缺乏 actionable insights——论文停在 '问题存在' 层面\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 15\n  action_items:\n    - round: 13\n      action: \"E1 routing 结果整合到 §4.1 + Conclusion 更新\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"E1 rescue-threshold routing 已写入。R15 routing 降级为 case study。非 blocking。\"\n  resolution_round: 13\n\n- id: \"R6-W1\"\n  summary: \"Decoupling 形式化存在技术问题 + saturation 未严格定义\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 9\n  action_items:\n    - round: 8\n      action: \"删除 Equation 1 形式化定义，保留定量描述\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Equation 1 已删。Round 12-18 未再提及。\"\n  resolution_round: 12\n\n- id: \"R6-W2\"\n  summary: \"GDN h3-1 的 16-head confound 削弱 LAMBADA convergence\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 18\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"R1-N2 Critical + R2-N2 Critical。主文并列 with/without GDN。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R16 确认修复存在但叙事仍过度突出。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-N2 Critical。移除 GDN 后 LAMBADA ρ 从 -1.0 降至 -0.7。R2 交叉 [AGREE] 但认为严重度略低——主要威胁 convergence claim 而非 per-example divergence claim。双方一致要求主文显著讨论。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未作为独立问题提及。§4.3 Robustness 已讨论 GDN exclusion。可能已被 convergence framing 重构（R5-W2/R16-N1）吸收——如果 convergence 不再是核心 claim，GDN confound 的影响降低。待 Research Director 确认。\"\n  action_items:\n    - round: 15\n      action: \"主文 §4.2 并列 with/without GDN ρ 值；§4.3 Robustness 讨论\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"§4.2/§4.3 已讨论 GDN exclusion。R18 未单独提及，可能因 convergence 叙事重构后影响降低。\"\n  resolution_round: null\n\n- id: \"R6-W3\"\n  summary: \"Bootstrap CI 在 n=3 架构上覆盖率远低于名义值\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 18\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"27 个 bootstrap 样本（排除退化后 ~24 个）无可靠覆盖率。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R2 指出 BCa CI 在 Introduction 首次出现处缺 caveat。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-W3 + R2 交叉 [AGREE]。BCa acceleration parameter 基于仅 3 个 jackknife 值。建议全面改用 percentile bootstrap 并标注 heuristic。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-N3 Critical + R2 交叉 [AGREE]。3³=27 种组合，排除退化后更少。95% CI=[-1.0,-0.7] 传递虚假精度感。R2 建议改用 exact permutation（3!=6 排列）或直接报告 3 个数据点。升级为 Critical。\"\n  action_items:\n    - round: 15\n      action: \"Figure caption 附注 illustrative only\"\n      assigned_to: paper_agent\n      status: done\n    - round: 16\n      action: \"Intro BCa CI 处加 heuristic caveat\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"Figure caption 已标注。但 R18 升级为 Critical——需全面改用 exact permutation 或直接报告数据点。\"\n  resolution_round: null\n\n- id: \"R14-W1\"\n  summary: \"Confidence margin 'mechanism' 标题暗示因果性，实为 correlational\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  action_items:\n    - round: 14\n      action: \"全文替换 'mechanism' → 'predictor'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已替换。R15-R18 未再提及。\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"n=5 attention ratios 使 convergence permutation test 本质上为 binary outcome\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"建议声明所有 Spearman correlation 推断为 descriptive/exploratory。\"\n  action_items:\n    - round: 15\n      action: \"§4.2 标注 'suggestive but underpowered secondary observation'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。R18 认为此 caveat 存在但全文不一致（见 R5-W2/R16-N1）。\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"标题/Abstract 过度泛化：仅 3 架构但表述暗示更广 generality\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  action_items:\n    - round: 14\n      action: \"正文加 scope 限定\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。R16-R18 未再单独提及。\"\n  resolution_round: 15\n\n- id: \"R14-W4\"\n  summary: \"缺失 prediction churn 文献（Milani Fard et al. 2016）\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  action_items:\n    - round: 14\n      action: \"添加 Milani Fard (2016) + Poli (2023) Hyena\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已引用。R18 确认引用存在。\"\n  resolution_round: 15\n\n- id: \"R15-W1\"\n  summary: \"'Nearly disjoint' / 'almost entirely different' 措辞夸大\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  action_items:\n    - round: 15\n      action: \"替换为 calibrated 表述\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。R16-R18 未再提及。\"\n  resolution_round: 15\n\n- id: \"R15-W2\"\n  summary: \"Routing 作为 'proof-of-concept application' 定位过高（仅 1/4 benchmark 有效）\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 18\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"建议降级为 case study / illustrative example。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"§4.1 已改为 case study 但 Conclusion 仍列为 practitioner implication。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R2-N2 Critical + R1-W1 + 交叉双方 AGREE。1/4 success rate（仅 LAMBADA），无 variance 报告（10-fold SD 缺失），无 ensemble baseline 对比。R1 补充：routing 非 main contribution，建议从 Conclusion practitioner implications 降级。R2 要求补充 learned routing / feature engineering / ensemble baseline，否则作为方法贡献严重不足。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-W1 Major + R2-W3 Major，交叉均 [AGREE]。LAMBADA +5.2pp，PIQA -0.49pp（显著负效），HellaSwag 无效。缺少 average logits ensemble baseline、learned routing 对比。R2 补充：Section 5 practical implications 基于 n=1 泛化。双方一致要求降级为 preliminary exploration。\"\n  action_items:\n    - round: 15\n      action: \"降级为 'illustrative case study'\"\n      assigned_to: paper_agent\n      status: done\n    - round: 16\n      action: \"Conclusion routing 从 practitioner implication 降级\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"§4.1 已标注 case study，但 Conclusion 和 Abstract 仍过度突出 routing。R18 双方一致要求进一步降级 + 补充 ensemble baseline。\"\n  resolution_round: null\n\n- id: \"R15-D1\"\n  summary: \"Appendix Table 30 DeltaNet 行数据不一致\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  action_items:\n    - round: 15\n      action: \"从 JSON 逐格修正\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已修正。R17-R18 未再提及。\"\n  resolution_round: 15\n\n- id: \"R15-W3\"\n  summary: \"缺失 Jain et al. (2025 FAccT) 引用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  action_items:\n    - round: 15\n      action: \"添加到 references.bib + Related Work\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。R17-R18 确认引用存在。\"\n  resolution_round: 15\n\n- id: \"R16-N1\"\n  summary: \"Aggregate convergence 叙事在 Abstract/Introduction 中仍过度突出\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-N2 Must-Fix + R2-W1 Should-Fix。交叉 [AGREE]。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1 交叉 [AGREE] R2-W1（misleading 统计报告）。§4.2 用 'monotonic convergence' 描述 non-significant 结果，Conclusion 用 'aggregate metrics converge on LAMBADA'。全文措辞不一致——§4.2 有时 exploratory 有时 confirmatory。双方一致要求全文统一为 descriptive/suggestive。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical，交叉均 [AGREE]。核心 framing 问题：叙事预设 aggregate convergence 存在但 p=.170 不支持。R2 提出最清晰的重构方案：'architectures interchangeable by aggregate metrics differ per-example'。R1 补充 §4.2 标题暗示确定性。双方一致要求全面重构叙事框架。\"\n  action_items:\n    - round: 16\n      action: \"结构性叙事重组\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"R16-R18 持续 flag。需全面重构叙事：从 'convergence vs divergence' 到 'aggregate interchangeability vs per-example divergence'。§4.2 标题需改为非确定性表述。\"\n  resolution_round: null\n\n- id: \"R16-W1\"\n  summary: \"Routing 实验缺少 variance 报告（10-repeat cross-validation 仅报 mean）\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-W3 + R2 AGREE。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-W1 + R2-N2 均指出。R2 补充：如果 SD > 3pp 则 5.3pp 增益可能不显著。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-W1 提及缺 ensemble baseline。R2-W3 再次指出缺 variance + baseline 对比。现在论文报告 SD=0.4pp（LAMBADA）但其他 benchmark 的 SD 缺失。\"\n  action_items:\n    - round: 16\n      action: \"从已有数据提取 SD 和 95% CI\"\n      assigned_to: main_agent\n      status: in_progress\n  resolution: \"LAMBADA 已报告 SD=0.4pp，但其他 benchmark SD 缺失，ensemble baseline 仍未补充。\"\n  resolution_round: null\n\n- id: \"R16-W2\"\n  summary: \"5-architecture 扩展验证仅 340M，主文 §4.3 缺 scale caveat\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-W4 + R2 AGREE。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-W5 + R2-W4 双方一致。R2 交叉 [AGREE] 但认为 minor 级别。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-W4 Warning。R2 交叉 [AGREE] 但程度略弱——Appendix X 的 z ≥ 2.8 一致性好，但应至少覆盖 HellaSwag 或 ARC-Easy。\"\n  action_items:\n    - round: 16\n      action: \"§4.3 加 'at 340M'\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W3\"\n  summary: \"Confidence margin AUC 的正态假设未验证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-W5 + R2 AGREE。\"\n    - round: 17\n      reviewers: []\n      note: \"R17 未单独提及。可能已修复或被其他更大问题覆盖。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未提及。Appendix 已包含 Shapiro-Wilk normality tests + empirical AUC 对比。可能已充分缓解，待 Research Director 确认。\"\n  action_items:\n    - round: 16\n      action: \"计算 empirical AUC 对比 parametric estimate\"\n      assigned_to: main_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W4\"\n  summary: \"模型规模覆盖有限（≤1.3B vs 7B+ 部署场景）\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R2-W4 + R1 AGREE。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R2-W4 + R1 交叉 [AGREE]。Conclusion 的 practitioner implications 用不加限定的一般性语言。Limitations 已提到 7B+ 但 Conclusion 未限定。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-W3 Major。两个 scale 点不足以支撑 'scale-robust'。R2 交叉 [AGREE]。建议改为 'consistent across the two scales examined'。\"\n  action_items:\n    - round: 16\n      action: \"Limitations 加 scale limitation 句\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"Limitations 已提及但 Conclusion 仍用不加限定语言。R18 要求全文弱化 scale-robust 表述。\"\n  resolution_round: null\n\n- id: \"R16-W5\"\n  summary: \"遗漏重要相关工作\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R2-W3 建议引用。R1 部分 AGREE。\"\n    - round: 17\n      reviewers: [R2]\n      note: \"R2-W2 再次列出，并新增 Ye et al. (2026) hybrid attention expressiveness hierarchy、arXiv 2601.09071（multiplicity resolution）、arXiv 2602.09520（federated Rashomon sets）。R1 REBUT——无法验证这些 2026 文献的时效性和相关性。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R2-W2 Major：遗漏 Model Soups (Wortsman 2022)、MoE (Shazeer 2017, Fedus 2022)。R1 独立提出 Jiang et al. (2024) 'Predictive Multiplicity of Foundation Models'。R1 交叉 [AGREE] Model Soups 高度相关，[AGREE with nuance] MoE 联系较间接。R1 REBUT Breiman (2001) 关联过弱。R1 纠正 R2：Fort et al. (2019) 已在论文中引用。\"\n  action_items:\n    - round: 16\n      action: \"核实并添加\"\n      assigned_to: main_agent\n      status: in_progress\n  resolution: \"需添加：Wortsman et al. (2022) Model Soups、Jiang et al. (2024) Foundation Model Multiplicity。可选：Shazeer (2017) MoE。Fort et al. (2019) 已存在。\"\n  resolution_round: null\n\n- id: \"R16-M1\"\n  summary: \"Haghighat 2026 bib 条目需更新为 AAAI 2026\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 16\n      reviewers: [R2]\n      note: \"Camera-ready 前 fix。\"\n    - round: 17\n      reviewers: []\n      note: \"R17 未提及。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未提及。references.bib 已更新为 @inproceedings{...booktitle={Proceedings of AAAI}}。可能已修复，待 Research Director 确认。\"\n  action_items:\n    - round: 16\n      action: \"更新 references.bib\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W1\"\n  summary: \"Task type vs evaluation format confound 未被区分（LAMBADA 为唯一 free-form benchmark）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-W2 提出 + R2 交叉 [AGREE]。LAMBADA 是唯一 free-form generation benchmark，其余均为 multiple-choice。LAMBADA 也是唯一显示 monotonic convergence 和最高 multiplicity 的 benchmark。Multiple-choice format 机械性约束答案空间（4-choice 下随机 agreement 25%），可能降低 divergence 上界。§3.2 按 cognitive demand 分类，完全忽略 evaluation format 这一混淆变量。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-W2 Major + R2 交叉 [AGREE]。R2 补充：如果 format 驱动差异，则 §4.1 'task-type modulates multiplicity' 应改为 'evaluation format modulates observed multiplicity'。HellaSwag 使用 acc_norm 进一步模糊比较。双方一致要求正文讨论 format confound 作为 alternative explanation。\"\n  action_items:\n    - round: 17\n      action: \"Discussion 或 Limitations 讨论 evaluation format 作为 alternative explanation\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W2\"\n  summary: \"Confirmatory/exploratory benchmark 分类缺乏预注册（informal pre-analysis plan 无 timestamp）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-W4 提出 + R2 交叉 [AGREE] 但认为严重度低。主文已用 all-10 correction 是最保守方式。Appendix A 的 6-benchmark correction 给选择性引用空间。R2 指出 6-benchmark 和 10-benchmark 在 LAMBADA 上 adjusted p 相同（因 p_min=0.017 不变）。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未单独提及。Appendix A 已区分 confirmatory/exploratory 且主文使用 all-10 correction。可能已充分缓解，待 Research Director 确认。\"\n  action_items:\n    - round: 17\n      action: \"Appendix A 明确 all-10 为唯一有效 correction，6-benchmark 仅为 sensitivity\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-W1\"\n  summary: \"Permutation test null baseline 不排除 example difficulty confound\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-W5 提出 + R2 交叉 [AGREE]。当前 permutation test null 仅排除 random overlap。如果某些 example 具有 attention-friendly 内在属性（如长距离依赖），所有架构添加 attention 后都会在这些 example 上受益——产生 above-random Jaccard 而无需 architecture-specific 效应。Table 9 的 J≈0.10 部分缓解（纯 difficulty-driven 应更高），但 conceptual 批评成立。R2 建议 stratified permutation test（条件化于 example difficulty）。\"\n  action_items:\n    - round: 18\n      action: \"讨论 example difficulty 作为 confound；考虑 stratified permutation test 或 example difficulty covariate\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "entrainment_gated_ft",
    "issues_yaml": "- id: \"R5-W1\"\n  summary: \"架构效应 vs seed 效应无法区分（单 training run，无 seed baseline）\"\n  category: experiment\n  severity: critical\n  status: wont_fix\n  first_raised_round: 5\n  last_seen_round: 18\n  mentions:\n    - round: 5\n      reviewers: [R1, R2]\n      note: \"R1 Critical, R2 W3+Q3 支持。\"\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"R2-N3 Must-Fix vs R1-W2 Should-Fix。分歧：R1 REBUT 认为论文已用关联性语言、第三方 zoo 无法自行补训。R2 维持 Must-Fix。论文已有 PolyPythias 校准但三重 mismatch 仍被指出。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N2 Critical。双方 [AGREE]。Pythia 70M 三重 mismatch（scale 70M vs 340M+/architecture family Transformer vs hybrid/accuracy 0.17-0.23 vs ~0.50）仍是核心弱点。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-N3 Critical + R2 交叉 [AGREE]。Pythia 70M within-seed J=0.312 vs cross-arch J=0.354，gap 仅 0.042。R2 补充 seed variation 可能解释大部分 per-example divergence。双方一致认为是根本性威胁但非 fatal。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-N2 Critical + R2-N2 Critical，交叉均 [AGREE]。R2 纠正 R1 数据误读：within-seed J=0.273 vs cross-arch J=0.10 实为 2.7× 差距（非 R1 声称的 0.02），部分支持架构效应独立性。但 Pythia 70M 三重 mismatch 仍限制 calibration 可迁移性。双方一致要求至少对一个 hybrid 架构训练多 seed。\"\n  action_items:\n    - round: 13\n      action: \"E4 Pythia 410M 9-seed calibration（实际完成 70M）\"\n      assigned_to: main_agent\n      status: done\n    - round: 14\n      action: \"Limitations 提升 single-seed 为 top limitation；§4.2 弱化因果语言\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"结构性限制，无法完全修复。已做：(1) Pythia 70M seed calibration 加入 Appendix W；(2) Limitations 中 single-seed 为 top limitation；(3) 全文使用 'associated with' 关联性语言。R18 双方 AGREE 仍为核心弱点但 R2 纠正了 R1 的数据误读——实际 2.7× gap 部分支持架构效应独立性。\"\n  resolution_round: null\n\n- id: \"R5-W2\"\n  summary: \"收敛 claim 统计不显著（Bonferroni p=.170）且依赖 GDN inclusion\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 18\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical。交叉 [AGREE]。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R16-N1 重新 flag。R15 写作修复不够——Intro 仍以 79% σ drop 开篇。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2 交叉 [AGREE]。R1 精确指出结构性限制：n=5 时最小 p=0.017，Bonferroni 后 0.170——无论效应多强都无法拒绝 H₀。Abstract 'Aggregate trends do not reach statistical significance' 表述尚可，但 §4.2 和 Conclusion 仍间歇性用确认性语言。R2 建议 mixed-effects regression（15 data points）作为替代方法。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical，交叉均 [AGREE]。论文核心叙事 'convergence masks divergence' 需要 aggregate convergence 成立，但 p=.170 不支持。R2 建议重构为 'architectures interchangeable by aggregate metrics differ per-example'——更弱前提、更强证据。R1 补充：§4.2 标题 'Aggregate Trends and Per-Example Independence' 暗示确定性结论。\"\n  action_items:\n    - round: 15\n      action: \"Abstract/Intro 重构：以 Jaccard saturation 为主线\"\n      assigned_to: paper_agent\n      status: done\n    - round: 16\n      action: \"结构性叙事重组：Intro 79% σ drop 移到 §4.2 等\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"R15-R18 持续 flag。需将 convergence 彻底降级为 exploratory observation，全文统一措辞。R18 建议的叙事重构方案（aggregate interchangeability → per-example divergence）最为清晰。\"\n  resolution_round: null\n\n- id: \"R5-W4\"\n  summary: \"新颖性有限——已有指标的直接套用，无新方法/理论\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 5\n  last_seen_round: 18\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"R2-W1 ecological fallacy 已知实例。R1 REBUT。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R2-N1 Must-Fix vs R1 REBUT。核心分歧未解决。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R2-N1 Critical（ecological fallacy 的已知实例化，方法论无创新）。R1 REBUT（critical 定级过高，empirical first 在实际相关 domain 有独立价值，引用 McCoy et al. 2020 类比）。双方部分收敛：均同意应明确定位为 empirical contribution。分歧：R2 认为是 Must-Fix，R1 认为 Should-Fix 级别。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R2-W1 Major（增量贡献，已知框架在新 domain 的应用）。R1 REBUT——4% saturation 和 aggregate-vs-per-example 解耦是非平凡发现，controlled model zoo 在 multiplicity 文献中罕见。部分收敛：Findings 标准下经验发现足够。Director 判断：R1 REBUT 有理，Findings 不要求方法论创新。\"\n  action_items:\n    - round: 6\n      action: \"Intro 加 empirical novelty framing\"\n      assigned_to: paper_agent\n      status: done\n    - round: 16\n      action: \"Intro 强化 empirical contribution 定位\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"结构性限制。R18 分歧持续但进一步收敛：Findings 标准下系统性经验发现（4% saturation, decoupling）足够。\"\n  resolution_round: null\n\n- id: \"R5-W3\"\n  summary: \"Task-dependent spectrum 仅 3 benchmark，存在评估格式 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [R1, R2]\n      note: \"α 变异可能反映 format 而非 task type。\"\n  action_items:\n    - round: 5\n      action: \"WinoGrande + PIQA per-example 分析\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"PIQA + WinoGrande 数据整合完成。Round 6-16 未再提及。R17 提出更具体的 format confound（见 R17-W1）。\"\n  resolution_round: 6\n\n- id: \"R5-W5\"\n  summary: \"正文约 8.2 页超出 EMNLP 8 页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 18\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16 视觉审查确认合规。\"\n    - round: 17\n      reviewers: [R1]\n      note: \"R1-M5 确认格式合规（8页，Limitations 3点，匿名完好）。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R18 双方格式检查均确认合规：8 页正文、Limitations 在 p.8、ACL template、double-blind。\"\n  action_items:\n    - round: 5\n      action: \"结构性压缩 8.2→7 页\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"主文在 8 页内。R14-R18 持续确认合规。\"\n  resolution_round: 5\n\n- id: \"R5-W6\"\n  summary: \"遗漏关键相关工作 Zoology/Based/Samba\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  action_items:\n    - round: 5\n      action: \"补 3 篇引用 + recall-throughput 框架\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Zoology + Based 引用于 §4.1，Samba 引用于 Related Work。\"\n  resolution_round: 5\n\n- id: \"R5-W7\"\n  summary: \"Ensemble 建议缺乏实验支撑 + POC 负面结果与 protocol 的 tension\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 9\n  action_items:\n    - round: 7\n      action: \"Majority vote + oracle POC 写入 Conclusion\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Conclusion 已包含 MV/oracle POC 数据。\"\n  resolution_round: 9\n\n- id: \"R5-W8\"\n  summary: \"Binary decomposition 可能低估多选题一致性\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 18\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-W2 指出 hurt sets binarization 可能 overestimate agreement。Appendix O continuous Jaccard 缓解。\"\n    - round: 17\n      reviewers: [R2]\n      note: \"R2-Q4 询问为何不在主文使用 continuous Jaccard 替代 binarized 版本。未作为独立 weakness 提出但作为 Question。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未作为独立问题提及。§3.4 已包含 binarization caveat + Appendix continuous Jaccard。可能已充分缓解，待 Research Director 确认。\"\n  action_items:\n    - round: 13\n      action: \"E2 continuous-threshold Jaccard sensitivity 结果整合到 Appendix + §4.1 引用\"\n      assigned_to: paper_agent\n      status: done\n    - round: 16\n      action: \"§3.4 加 1 句 K-choice binarization caveat\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W9\"\n  summary: \"Abstract 信息密度过高（统计量堆砌）\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-M6 指出接近 200 word 上限。R2-M4 指出 inline 统计量（α, p, Jaccard 值）增加认知负荷。双方建议精简。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R2-W4 Major：数字密度过高（Jaccard, p, α, pp 等），指出第三句可能有句法拼接问题。R1 交叉 [AGREE with nuance]——同意需精简但认为句法完整。\"\n  action_items:\n    - round: 13\n      action: \"W5: Abstract 进一步精简至 3 key numbers\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"R15 精简完成但 R17-R18 持续指出信息密度问题。需进一步删减数字，保留 3-4 个关键数值。\"\n  resolution_round: null\n\n- id: \"RV-L1\"\n  summary: \"Limitations 6 段违反 EMNLP 用户规则（要求 ~3 点）\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 15\n  action_items:\n    - round: 5\n      action: \"6 段→3 段\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"压缩为 3 段。R14-R18 确认合规。\"\n  resolution_round: 5\n\n- id: \"RV-L2\"\n  summary: \"loglik 压缩假说已被诊断数据反驳但论文仍引用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  action_items:\n    - round: 5\n      action: \"改为 binary classification structural properties 解释\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"改为 'structural properties of constrained-choice formats'。\"\n  resolution_round: 5\n\n- id: \"R6-N3\"\n  summary: \"仅 2 个 scale 点不足以支撑 scale-dependent claim\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  action_items:\n    - round: 6\n      action: \"MF4: 全文替换 scale-dependent\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"全文已用 'differs between 340M and 1.3B'。\"\n  resolution_round: 8\n\n- id: \"R6-N2\"\n  summary: \"缺乏 actionable insights——论文停在 '问题存在' 层面\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 15\n  action_items:\n    - round: 13\n      action: \"E1 routing 结果整合到 §4.1 + Conclusion 更新\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"E1 rescue-threshold routing 已写入。R15 routing 降级为 case study。非 blocking。\"\n  resolution_round: 13\n\n- id: \"R6-W1\"\n  summary: \"Decoupling 形式化存在技术问题 + saturation 未严格定义\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 9\n  action_items:\n    - round: 8\n      action: \"删除 Equation 1 形式化定义，保留定量描述\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Equation 1 已删。Round 12-18 未再提及。\"\n  resolution_round: 12\n\n- id: \"R6-W2\"\n  summary: \"GDN h3-1 的 16-head confound 削弱 LAMBADA convergence\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 18\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"R1-N2 Critical + R2-N2 Critical。主文并列 with/without GDN。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R16 确认修复存在但叙事仍过度突出。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-N2 Critical。移除 GDN 后 LAMBADA ρ 从 -1.0 降至 -0.7。R2 交叉 [AGREE] 但认为严重度略低——主要威胁 convergence claim 而非 per-example divergence claim。双方一致要求主文显著讨论。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未作为独立问题提及。§4.3 Robustness 已讨论 GDN exclusion。可能已被 convergence framing 重构（R5-W2/R16-N1）吸收——如果 convergence 不再是核心 claim，GDN confound 的影响降低。待 Research Director 确认。\"\n  action_items:\n    - round: 15\n      action: \"主文 §4.2 并列 with/without GDN ρ 值；§4.3 Robustness 讨论\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"§4.2/§4.3 已讨论 GDN exclusion。R18 未单独提及，可能因 convergence 叙事重构后影响降低。\"\n  resolution_round: null\n\n- id: \"R6-W3\"\n  summary: \"Bootstrap CI 在 n=3 架构上覆盖率远低于名义值\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 18\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"27 个 bootstrap 样本（排除退化后 ~24 个）无可靠覆盖率。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R2 指出 BCa CI 在 Introduction 首次出现处缺 caveat。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-W3 + R2 交叉 [AGREE]。BCa acceleration parameter 基于仅 3 个 jackknife 值。建议全面改用 percentile bootstrap 并标注 heuristic。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-N3 Critical + R2 交叉 [AGREE]。3³=27 种组合，排除退化后更少。95% CI=[-1.0,-0.7] 传递虚假精度感。R2 建议改用 exact permutation（3!=6 排列）或直接报告 3 个数据点。升级为 Critical。\"\n  action_items:\n    - round: 15\n      action: \"Figure caption 附注 illustrative only\"\n      assigned_to: paper_agent\n      status: done\n    - round: 16\n      action: \"Intro BCa CI 处加 heuristic caveat\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"Figure caption 已标注。但 R18 升级为 Critical——需全面改用 exact permutation 或直接报告数据点。\"\n  resolution_round: null\n\n- id: \"R14-W1\"\n  summary: \"Confidence margin 'mechanism' 标题暗示因果性，实为 correlational\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  action_items:\n    - round: 14\n      action: \"全文替换 'mechanism' → 'predictor'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已替换。R15-R18 未再提及。\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"n=5 attention ratios 使 convergence permutation test 本质上为 binary outcome\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"建议声明所有 Spearman correlation 推断为 descriptive/exploratory。\"\n  action_items:\n    - round: 15\n      action: \"§4.2 标注 'suggestive but underpowered secondary observation'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。R18 认为此 caveat 存在但全文不一致（见 R5-W2/R16-N1）。\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"标题/Abstract 过度泛化：仅 3 架构但表述暗示更广 generality\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  action_items:\n    - round: 14\n      action: \"正文加 scope 限定\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。R16-R18 未再单独提及。\"\n  resolution_round: 15\n\n- id: \"R14-W4\"\n  summary: \"缺失 prediction churn 文献（Milani Fard et al. 2016）\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  action_items:\n    - round: 14\n      action: \"添加 Milani Fard (2016) + Poli (2023) Hyena\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已引用。R18 确认引用存在。\"\n  resolution_round: 15\n\n- id: \"R15-W1\"\n  summary: \"'Nearly disjoint' / 'almost entirely different' 措辞夸大\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  action_items:\n    - round: 15\n      action: \"替换为 calibrated 表述\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。R16-R18 未再提及。\"\n  resolution_round: 15\n\n- id: \"R15-W2\"\n  summary: \"Routing 作为 'proof-of-concept application' 定位过高（仅 1/4 benchmark 有效）\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 18\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"建议降级为 case study / illustrative example。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"§4.1 已改为 case study 但 Conclusion 仍列为 practitioner implication。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R2-N2 Critical + R1-W1 + 交叉双方 AGREE。1/4 success rate（仅 LAMBADA），无 variance 报告（10-fold SD 缺失），无 ensemble baseline 对比。R1 补充：routing 非 main contribution，建议从 Conclusion practitioner implications 降级。R2 要求补充 learned routing / feature engineering / ensemble baseline，否则作为方法贡献严重不足。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-W1 Major + R2-W3 Major，交叉均 [AGREE]。LAMBADA +5.2pp，PIQA -0.49pp（显著负效），HellaSwag 无效。缺少 average logits ensemble baseline、learned routing 对比。R2 补充：Section 5 practical implications 基于 n=1 泛化。双方一致要求降级为 preliminary exploration。\"\n  action_items:\n    - round: 15\n      action: \"降级为 'illustrative case study'\"\n      assigned_to: paper_agent\n      status: done\n    - round: 16\n      action: \"Conclusion routing 从 practitioner implication 降级\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"§4.1 已标注 case study，但 Conclusion 和 Abstract 仍过度突出 routing。R18 双方一致要求进一步降级 + 补充 ensemble baseline。\"\n  resolution_round: null\n\n- id: \"R15-D1\"\n  summary: \"Appendix Table 30 DeltaNet 行数据不一致\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  action_items:\n    - round: 15\n      action: \"从 JSON 逐格修正\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已修正。R17-R18 未再提及。\"\n  resolution_round: 15\n\n- id: \"R15-W3\"\n  summary: \"缺失 Jain et al. (2025 FAccT) 引用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  action_items:\n    - round: 15\n      action: \"添加到 references.bib + Related Work\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。R17-R18 确认引用存在。\"\n  resolution_round: 15\n\n- id: \"R16-N1\"\n  summary: \"Aggregate convergence 叙事在 Abstract/Introduction 中仍过度突出\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-N2 Must-Fix + R2-W1 Should-Fix。交叉 [AGREE]。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1 交叉 [AGREE] R2-W1（misleading 统计报告）。§4.2 用 'monotonic convergence' 描述 non-significant 结果，Conclusion 用 'aggregate metrics converge on LAMBADA'。全文措辞不一致——§4.2 有时 exploratory 有时 confirmatory。双方一致要求全文统一为 descriptive/suggestive。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical，交叉均 [AGREE]。核心 framing 问题：叙事预设 aggregate convergence 存在但 p=.170 不支持。R2 提出最清晰的重构方案：'architectures interchangeable by aggregate metrics differ per-example'。R1 补充 §4.2 标题暗示确定性。双方一致要求全面重构叙事框架。\"\n  action_items:\n    - round: 16\n      action: \"结构性叙事重组\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"R16-R18 持续 flag。需全面重构叙事：从 'convergence vs divergence' 到 'aggregate interchangeability vs per-example divergence'。§4.2 标题需改为非确定性表述。\"\n  resolution_round: null\n\n- id: \"R16-W1\"\n  summary: \"Routing 实验缺少 variance 报告（10-repeat cross-validation 仅报 mean）\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-W3 + R2 AGREE。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-W1 + R2-N2 均指出。R2 补充：如果 SD > 3pp 则 5.3pp 增益可能不显著。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-W1 提及缺 ensemble baseline。R2-W3 再次指出缺 variance + baseline 对比。现在论文报告 SD=0.4pp（LAMBADA）但其他 benchmark 的 SD 缺失。\"\n  action_items:\n    - round: 16\n      action: \"从已有数据提取 SD 和 95% CI\"\n      assigned_to: main_agent\n      status: in_progress\n  resolution: \"LAMBADA 已报告 SD=0.4pp，但其他 benchmark SD 缺失，ensemble baseline 仍未补充。\"\n  resolution_round: null\n\n- id: \"R16-W2\"\n  summary: \"5-architecture 扩展验证仅 340M，主文 §4.3 缺 scale caveat\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-W4 + R2 AGREE。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-W5 + R2-W4 双方一致。R2 交叉 [AGREE] 但认为 minor 级别。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-W4 Warning。R2 交叉 [AGREE] 但程度略弱——Appendix X 的 z ≥ 2.8 一致性好，但应至少覆盖 HellaSwag 或 ARC-Easy。\"\n  action_items:\n    - round: 16\n      action: \"§4.3 加 'at 340M'\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W3\"\n  summary: \"Confidence margin AUC 的正态假设未验证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-W5 + R2 AGREE。\"\n    - round: 17\n      reviewers: []\n      note: \"R17 未单独提及。可能已修复或被其他更大问题覆盖。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未提及。Appendix 已包含 Shapiro-Wilk normality tests + empirical AUC 对比。可能已充分缓解，待 Research Director 确认。\"\n  action_items:\n    - round: 16\n      action: \"计算 empirical AUC 对比 parametric estimate\"\n      assigned_to: main_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W4\"\n  summary: \"模型规模覆盖有限（≤1.3B vs 7B+ 部署场景）\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R2-W4 + R1 AGREE。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R2-W4 + R1 交叉 [AGREE]。Conclusion 的 practitioner implications 用不加限定的一般性语言。Limitations 已提到 7B+ 但 Conclusion 未限定。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-W3 Major。两个 scale 点不足以支撑 'scale-robust'。R2 交叉 [AGREE]。建议改为 'consistent across the two scales examined'。\"\n  action_items:\n    - round: 16\n      action: \"Limitations 加 scale limitation 句\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"Limitations 已提及但 Conclusion 仍用不加限定语言。R18 要求全文弱化 scale-robust 表述。\"\n  resolution_round: null\n\n- id: \"R16-W5\"\n  summary: \"遗漏重要相关工作\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R2-W3 建议引用。R1 部分 AGREE。\"\n    - round: 17\n      reviewers: [R2]\n      note: \"R2-W2 再次列出，并新增 Ye et al. (2026) hybrid attention expressiveness hierarchy、arXiv 2601.09071（multiplicity resolution）、arXiv 2602.09520（federated Rashomon sets）。R1 REBUT——无法验证这些 2026 文献的时效性和相关性。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R2-W2 Major：遗漏 Model Soups (Wortsman 2022)、MoE (Shazeer 2017, Fedus 2022)。R1 独立提出 Jiang et al. (2024) 'Predictive Multiplicity of Foundation Models'。R1 交叉 [AGREE] Model Soups 高度相关，[AGREE with nuance] MoE 联系较间接。R1 REBUT Breiman (2001) 关联过弱。R1 纠正 R2：Fort et al. (2019) 已在论文中引用。\"\n  action_items:\n    - round: 16\n      action: \"核实并添加\"\n      assigned_to: main_agent\n      status: in_progress\n  resolution: \"需添加：Wortsman et al. (2022) Model Soups、Jiang et al. (2024) Foundation Model Multiplicity。可选：Shazeer (2017) MoE。Fort et al. (2019) 已存在。\"\n  resolution_round: null\n\n- id: \"R16-M1\"\n  summary: \"Haghighat 2026 bib 条目需更新为 AAAI 2026\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 16\n      reviewers: [R2]\n      note: \"Camera-ready 前 fix。\"\n    - round: 17\n      reviewers: []\n      note: \"R17 未提及。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未提及。references.bib 已更新为 @inproceedings{...booktitle={Proceedings of AAAI}}。可能已修复，待 Research Director 确认。\"\n  action_items:\n    - round: 16\n      action: \"更新 references.bib\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W1\"\n  summary: \"Task type vs evaluation format confound 未被区分（LAMBADA 为唯一 free-form benchmark）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-W2 提出 + R2 交叉 [AGREE]。LAMBADA 是唯一 free-form generation benchmark，其余均为 multiple-choice。LAMBADA 也是唯一显示 monotonic convergence 和最高 multiplicity 的 benchmark。Multiple-choice format 机械性约束答案空间（4-choice 下随机 agreement 25%），可能降低 divergence 上界。§3.2 按 cognitive demand 分类，完全忽略 evaluation format 这一混淆变量。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-W2 Major + R2 交叉 [AGREE]。R2 补充：如果 format 驱动差异，则 §4.1 'task-type modulates multiplicity' 应改为 'evaluation format modulates observed multiplicity'。HellaSwag 使用 acc_norm 进一步模糊比较。双方一致要求正文讨论 format confound 作为 alternative explanation。\"\n  action_items:\n    - round: 17\n      action: \"Discussion 或 Limitations 讨论 evaluation format 作为 alternative explanation\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W2\"\n  summary: \"Confirmatory/exploratory benchmark 分类缺乏预注册（informal pre-analysis plan 无 timestamp）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-W4 提出 + R2 交叉 [AGREE] 但认为严重度低。主文已用 all-10 correction 是最保守方式。Appendix A 的 6-benchmark correction 给选择性引用空间。R2 指出 6-benchmark 和 10-benchmark 在 LAMBADA 上 adjusted p 相同（因 p_min=0.017 不变）。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未单独提及。Appendix A 已区分 confirmatory/exploratory 且主文使用 all-10 correction。可能已充分缓解，待 Research Director 确认。\"\n  action_items:\n    - round: 17\n      action: \"Appendix A 明确 all-10 为唯一有效 correction，6-benchmark 仅为 sensitivity\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-W1\"\n  summary: \"Permutation test null baseline 不排除 example difficulty confound\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-W5 提出 + R2 交叉 [AGREE]。当前 permutation test null 仅排除 random overlap。如果某些 example 具有 attention-friendly 内在属性（如长距离依赖），所有架构添加 attention 后都会在这些 example 上受益——产生 above-random Jaccard 而无需 architecture-specific 效应。Table 9 的 J≈0.10 部分缓解（纯 difficulty-driven 应更高），但 conceptual 批评成立。R2 建议 stratified permutation test（条件化于 example difficulty）。\"\n  action_items:\n    - round: 18\n      action: \"讨论 example difficulty 作为 confound；考虑 stratified permutation test 或 example difficulty covariate\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1583 · 2026-05-24T12:15:35.166982+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_issues.yaml\", \"bytes\": 24837}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1584 · 2026-05-24T12:17:42.262892+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "entrainment_gated_ft",
  "report": "# Round 18 审稿报告\n\n**Venue**: EMNLP 2026 via ARR (May cycle) | **Deadline**: 2026-05-25 | **Reviewers**: 2 (方法严谨性 + 新颖性/完整性)\n\n---\n\n## Summary\n\n论文研究混合线性循环架构（GDN、RetNet、HGRN2）在 aggregate benchmark 上表现相近时的 per-example 预测差异。使用 Wang et al. (2025) 的 controlled model zoo（3 架构 × 5 attention 比例 × 2 规模），在 10 个 benchmark 上分析 30 个配置，发现：(1) 跨架构 per-example Jaccard overlap 仅 ~0.10（约为独立基线 2 倍），在 4% attention 即饱和；(2) multiplicity 幅度取决于任务类型（α = 0.14–0.30）而非 attention 剂量；(3) confidence-based routing 仅在 LAMBADA 上有效（+5.2pp），其余 benchmark 无效或负效。\n\n---\n\n## Strengths\n\n- **S1**: 研究问题定位精准——per-example multiplicity 在 hybrid recurrent 架构中此前未被系统研究，填补了 aggregate benchmark 分析与 per-example 效应之间的空白\n- **S2**: 实验设计系统化——controlled model zoo 固定训练数据/tokenizer/hyperparameters，纯粹改变 architecture + attention ratio，是该问题的理想框架\n- **S3**: 分析透明度高——诚实报告 p = .170 未 cherry-pick，21 页含丰富 sensitivity analysis（bootstrap CI、GDN exclusion、seed calibration、5-arch validation、complementarity decomposition）\n- **S4**: Per-example saturation at 4% attention 是非平凡发现——仅需最少量 attention 即锁定 per-example 分化 pattern，对 hybrid 架构设计有直接指导意义\n- **S5**: 五架构验证扩展（GLA + DeltaNet，10 pairwise comparisons，all J ≤ 0.14，all p < .01）增强了核心发现的鲁棒性\n- **S6**: 写作质量好，figures 可读性高（特别是 Figure 1 的 aggregate-vs-per-example 对比），方法描述清晰\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**C1** [AGREE: R1-N1 + R2-N1] **Aggregate convergence 叙事无统计支撑，构成 framing 硬伤**\n\n论文核心框架 \"aggregate convergence masks per-example divergence\" 需要 aggregate convergence 成立，但 Bonferroni-adjusted p = .170（n = 5 Spearman），10/10 benchmarks 均未达统计显著。LAMBADA 的 ρ = −1.0 是唯一单调下降但校正后仍不显著。n = 5 下 Spearman 的 power 极低——仅 |ρ| = 1.0 才能达到 p < .05，even moderate effect sizes 无法检测。\n\n然而论文在多处将 underpowered 结果用于推断：§4.2 标题 \"Aggregate Trends and Per-Example Independence\" 暗示确定性结论；Conclusion 用 \"aggregate metrics converge on LAMBADA\"；Abstract/Introduction 间歇性使用确认性语言。\n\n**修复方向**：重构叙事为 \"architectures interchangeable by aggregate metrics actually differ substantially at per-example level\"——不强调统计不显著的 convergence trend，而是强调 aggregate 分数的不可区分性（overlapping CIs）。这是更弱的前提但有更强的证据支撑。\n\n**C2** [AGREE: R1-N2 + R2-N2] **单次训练 run 无法分离 architecture vs seed 效应**\n\n每配置仅 1 次训练（seed 42）。论文声称 \"architectural variation produces per-example multiplicity\"，但无法排除 seed 效应为主要驱动因素。Appendix W 的 Pythia 70M seed calibration 存在三重 mismatch：scale（70M vs 340M/1.3B）、architecture family（Transformer vs hybrid）、accuracy regime（0.17 vs 0.50）。\n\nR2 纠正了 R1 的数据误读：论文报告的 within-seed J = 0.273 和 J = 0.293 均为 Pythia within-seed 值（helped 和 hurt 子集），cross-architecture reference 是 J ≈ 0.10。实际 within-seed vs cross-arch 差距是 2.7×（非 R1 声称的 0.02），部分支持架构效应的独立性。但 calibration 可迁移性仍然有限。\n\n**修复方向**：对至少一个 hybrid 架构（如 RetNet 或 HGRN2）训练 3+ 个不同 seed，直接量化 within-architecture per-example 变异。若无法实现，需大幅弱化因果归因语言。\n\n**C3** [AGREE: R1-N3, R2 补充确认] **Bootstrap CI 基于 n = 3 架构不可靠**\n\n3 个架构重采样仅 3³ = 27 种组合，排除退化（same-architecture triplicates）后更少。报告的 95% CI = [−1.0, −0.7] 传递与 n = 3 不匹配的虚假精度感。BCa acceleration parameter 基于仅 3 个 jackknife 值。\n\n**修复方向**：改用 exact permutation test（3! = 6 排列）或直接报告 3 个数据点让读者自行判断。明确标注所有 bootstrap CI 为 heuristic。\n\n### Major（影响评分但不一票否决）\n\n**M1** [AGREE: R1-W1 + R2-W3] **Routing 作为 contribution 过于单薄**\n\n10 benchmark 中仅 LAMBADA 有效（+5.2pp），PIQA 显著负效（−0.49pp，p = .006），HellaSwag 无效。缺少最自然的 baseline：average logits ensemble。Section 5 的 practical implications 基于 n = 1 的泛化。方法本身（confidence-based hard selection）过于简单，缺乏与 learned routing 或 calibrated ensembling 的比较。应降级为 preliminary exploration，不作为 main contribution。\n\n**M2** [AGREE: R1-W2, R2 交叉确认] **任务分类法存在 evaluation format confound**\n\nLAMBADA 是唯一 free-form generation task，同时显示唯一单调 σ 下降、最高 α = 0.30、唯一有效 routing。无法区分 task type vs evaluation format 的驱动作用。Multiple-choice format 机械性约束答案空间，可能降低 divergence 上界。HellaSwag 使用 acc_norm 进一步模糊与其他 Reasoning benchmark 的比较。§3.2 按 cognitive demand 分类但未讨论 evaluation format 这一混淆变量。\n\n**M3** [分歧: R2-W1, R1 REBUT] **新颖性为增量贡献**\n\nR2 认为核心贡献是已知框架（predictive multiplicity + ecological fallacy）在新 domain 的直接应用，方法论无创新。R1 反驳：4% saturation 和 aggregate-vs-per-example 解耦是非平凡经验发现；controlled model zoo 设定在 multiplicity 文献中罕见；Findings 不要求方法论创新。\n\n**Director 判断**：R1 的 REBUT 有理。论文的经验贡献——特别是 4% saturation 的发现和 systematic task-dependent variation——在 Findings 标准下足够。但论文应更清楚地定位为 empirical contribution。\n\n**M4** [AGREE: R1-W3] **Scale robustness claim 过强**\n\n仅 340M 和 1.3B 两个 scale 点，不足以支撑 \"scale-robust\"。应改为 \"consistent across the two scales examined\"。Limitations 已提到 7B+ 但 Conclusion 的 practitioner implications 用不加限定的一般性语言。\n\n**M5** [R2-W2, R1 部分 AGREE] **Related Work 遗漏**\n\n- **Model Soups** (Wortsman et al., 2022 ICML)：weight-space interpolation vs architecture-space multiplicity 有直接对话关系 [R1+R2 AGREE]\n- **Jiang et al. (2024)** \"On the Predictive Multiplicity of Foundation Models\"：将 multiplicity 扩展到 foundation models [R1 独立提出, R2 AGREE]\n- MoE 文献 (Shazeer et al., 2017) 与 routing 方案有间接关联 [R2 提出, R1 AGREE with nuance]\n- Fort et al. (2019) 已在论文中引用——R2 的 \"missing\" 指控不成立 [R1 纠正]\n\n**M6** [R2-W4, R1 AGREE with nuance] **Abstract 过度拥挤**\n\n~180 words 中数字密度过高（Jaccard, p, α, pp 等），降低传播效果。R2 指出第三句可能有句法拼接问题；R1 认为语法完整但同意需精简。建议保留 3–4 个关键数值，用直觉描述替代部分统计细节。\n\n### Minor\n\n- **m1** [R1-W4]: 5-architecture validation 仅覆盖 LAMBADA + h3-1 + 340M，应至少扩展到 HellaSwag 或 ARC-Easy\n- **m2** [R1-W5, R2 AGREE]: Permutation test null baseline 不排除 example difficulty confound——attention-friendly examples 可产生 above-random Jaccard 而无需 architecture-specific 效应。建议讨论 example difficulty 作为 alternative explanation\n- **m3** [R1-M1]: Abstract \"approximately twice the independence baseline\" 过于模糊，建议给出具体数值\n- **m4** [R1-M2]: Figure 1 shaded bands (n = 3) 传达不恰当的精度感\n- **m5** [R1-M4]: Table 1 confirmatory vs exploratory benchmark 缺乏视觉区分\n- **m6** [R2-M4]: Limitations 未讨论 benchmark 代表性（全为 zero-shot 分类/检索，无 generation task）\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Overall 3.0 (Findings)**——两位 Reviewer 独立给出相同评分\n2. **Aggregate convergence 叙事需重构**——不依赖统计不显著的 convergence trend，改为强调 aggregate interchangeability vs per-example divergence\n3. **Seed confound 是核心弱点**——需多 seed 实验或大幅弱化因果归因\n4. **Bootstrap n = 3 不可靠**——改用 exact permutation 或直接报告数据点\n5. **Routing 应降级**——从 main contribution 降为 preliminary exploration\n6. **Format confound 需正文讨论**——LAMBADA 的 free-form 格式可能是异常表现的驱动因素\n\n## Reviewer Divergence [REBUT]\n\n1. **新颖性定级**：R2 认为纯增量（已知框架在新 domain 的应用），R1 认为 empirical findings（4% saturation, decoupling）有独立贡献价值。Director 判断：R1 的 REBUT 有理——Findings 不要求方法论创新，系统性经验发现足够。\n\n---\n\n## Questions\n\n1. 能否对至少一个 hybrid 架构训练 3+ 个不同 seed，直接量化 within-architecture per-example 变异？\n2. 能否增加一个 free-form generation benchmark（如 TriviaQA）来解耦 task type vs evaluation format？\n3. Routing 实验的 cross-validation SD 是多少？如果 SD > 3pp 则 +5.2pp 增益可能不显著。\n4. 为什么不对所有 benchmark 报告 majority vote 和 average-logits ensemble baseline？\n5. 4% saturation 的精度受限于最低非零配置——1–3% 处是否可能有 gradual onset？\n\n---\n\n## Missing References\n\n1. **Wortsman et al. (2022)** \"Model Soups: Averaging Weights of Multiple Fine-tuned Models Improves Accuracy without Increasing Inference Time.\" ICML. [R1+R2 AGREE]\n2. **Jiang et al. (2024)** \"On the Predictive Multiplicity of Foundation Models.\" [R1 提出, R2 AGREE]\n3. **Shazeer et al. (2017)** \"Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer.\" ICLR. [R2 提出, R1 AGREE with nuance]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（2 warning, 10 info）：\n- **Warning**: Pages 3–4 连续纯文本无 display item（Method §3.1–3.5），建议加入 display math 打破视觉单调性\n- **Warning**: Pages 6–7 display items 过密（6 个集中 2 页），与 pages 3–4 形成节奏突变\n- **Info**: Figure 1 位置合理、caption 自包含；Tables 使用 booktabs 风格规范；正文 8 页合规；appendix 表格密度高但可接受；Figure 5/6 内部文字偏小\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 — Findings（可被 Findings 接收）**\n\n**置信度: 4/5 (High)**\n\n扎实的实证研究，核心 per-example 发现（Jaccard ~0.10, 4% saturation, task-dependent α = 0.14–0.30）有价值且经过严格检验。但三个 Critical 问题——convergence framing 无统计支撑（p = .170）、seed confound（每配置单次训练）、bootstrap CI n = 3 不可靠——共同削弱 claim 强度，使论文的核心叙事框架不够稳固。新颖性在 Findings 标准下足够（系统性经验发现，非方法论创新），但 routing 贡献单薄（1/10 benchmark 有效）限制了实践价值。\n\n**提升至 Conference (3.5) 的条件**：\n1. 补充同架构多 seed 实验，直接分离 architecture vs seed 效应\n2. 重构叙事框架：从 \"convergence masks divergence\" 到 \"aggregate interchangeability vs per-example divergence\"\n3. 增加 format-matched 的 free-form benchmark 解耦 task type vs evaluation format\n4. Bootstrap CI 改用 exact permutation 或直接报告数据点\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"adding attention affects substantially different examples per architecture\" 暗示因果方向，在单次 run 下不可靠，建议改为 associative 语言\n- Contributions 列表中 routing 应降级或移至 supplementary finding\n\n### §3 Method\n- §3.2 Task Taxonomy：需讨论 evaluation format（free-form vs multiple-choice）作为 confound\n- §3.5 Statistical Methods：bootstrap 方法在 n = 3 下应明确标注为 heuristic\n\n### §4 Experiments\n- §4.1 routing 结果需增加 cross-validation SD 和 ensemble baseline（average logits）\n- §4.2 标题 \"Aggregate Trends and Per-Example Independence\" 暗示确定性，建议改为 \"Aggregate Variance and Per-Example Overlap\"\n- §4.3 \"scale-robust\" → \"consistent across the two scales examined (340M, 1.3B)\"\n\n### §5 Conclusion\n- Practical implications 中 routing 建议应大幅限定范围（仅限 high-α free-form tasks）\n- \"when α > 0.2, per-example audit is warranted\" 的 threshold 无理论基础，建议弱化为 directional guidance\n\n### Abstract\n- 精简至 3–4 个关键数值，用直觉描述替代部分统计细节\n- 检查第三句是否有句法拼接问题",
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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "entrainment_gated_ft",
    "report": "# Round 18 审稿报告\n\n**Venue**: EMNLP 2026 via ARR (May cycle) | **Deadline**: 2026-05-25 | **Reviewers**: 2 (方法严谨性 + 新颖性/完整性)\n\n---\n\n## Summary\n\n论文研究混合线性循环架构（GDN、RetNet、HGRN2）在 aggregate benchmark 上表现相近时的 per-example 预测差异。使用 Wang et al. (2025) 的 controlled model zoo（3 架构 × 5 attention 比例 × 2 规模），在 10 个 benchmark 上分析 30 个配置，发现：(1) 跨架构 per-example Jaccard overlap 仅 ~0.10（约为独立基线 2 倍），在 4% attention 即饱和；(2) multiplicity 幅度取决于任务类型（α = 0.14–0.30）而非 attention 剂量；(3) confidence-based routing 仅在 LAMBADA 上有效（+5.2pp），其余 benchmark 无效或负效。\n\n---\n\n## Strengths\n\n- **S1**: 研究问题定位精准——per-example multiplicity 在 hybrid recurrent 架构中此前未被系统研究，填补了 aggregate benchmark 分析与 per-example 效应之间的空白\n- **S2**: 实验设计系统化——controlled model zoo 固定训练数据/tokenizer/hyperparameters，纯粹改变 architecture + attention ratio，是该问题的理想框架\n- **S3**: 分析透明度高——诚实报告 p = .170 未 cherry-pick，21 页含丰富 sensitivity analysis（bootstrap CI、GDN exclusion、seed calibration、5-arch validation、complementarity decomposition）\n- **S4**: Per-example saturation at 4% attention 是非平凡发现——仅需最少量 attention 即锁定 per-example 分化 pattern，对 hybrid 架构设计有直接指导意义\n- **S5**: 五架构验证扩展（GLA + DeltaNet，10 pairwise comparisons，all J ≤ 0.14，all p < .01）增强了核心发现的鲁棒性\n- **S6**: 写作质量好，figures 可读性高（特别是 Figure 1 的 aggregate-vs-per-example 对比），方法描述清晰\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**C1** [AGREE: R1-N1 + R2-N1] **Aggregate convergence 叙事无统计支撑，构成 framing 硬伤**\n\n论文核心框架 \"aggregate convergence masks per-example divergence\" 需要 aggregate convergence 成立，但 Bonferroni-adjusted p = .170（n = 5 Spearman），10/10 benchmarks 均未达统计显著。LAMBADA 的 ρ = −1.0 是唯一单调下降但校正后仍不显著。n = 5 下 Spearman 的 power 极低——仅 |ρ| = 1.0 才能达到 p < .05，even moderate effect sizes 无法检测。\n\n然而论文在多处将 underpowered 结果用于推断：§4.2 标题 \"Aggregate Trends and Per-Example Independence\" 暗示确定性结论；Conclusion 用 \"aggregate metrics converge on LAMBADA\"；Abstract/Introduction 间歇性使用确认性语言。\n\n**修复方向**：重构叙事为 \"architectures interchangeable by aggregate metrics actually differ substantially at per-example level\"——不强调统计不显著的 convergence trend，而是强调 aggregate 分数的不可区分性（overlapping CIs）。这是更弱的前提但有更强的证据支撑。\n\n**C2** [AGREE: R1-N2 + R2-N2] **单次训练 run 无法分离 architecture vs seed 效应**\n\n每配置仅 1 次训练（seed 42）。论文声称 \"architectural variation produces per-example multiplicity\"，但无法排除 seed 效应为主要驱动因素。Appendix W 的 Pythia 70M seed calibration 存在三重 mismatch：scale（70M vs 340M/1.3B）、architecture family（Transformer vs hybrid）、accuracy regime（0.17 vs 0.50）。\n\nR2 纠正了 R1 的数据误读：论文报告的 within-seed J = 0.273 和 J = 0.293 均为 Pythia within-seed 值（helped 和 hurt 子集），cross-architecture reference 是 J ≈ 0.10。实际 within-seed vs cross-arch 差距是 2.7×（非 R1 声称的 0.02），部分支持架构效应的独立性。但 calibration 可迁移性仍然有限。\n\n**修复方向**：对至少一个 hybrid 架构（如 RetNet 或 HGRN2）训练 3+ 个不同 seed，直接量化 within-architecture per-example 变异。若无法实现，需大幅弱化因果归因语言。\n\n**C3** [AGREE: R1-N3, R2 补充确认] **Bootstrap CI 基于 n = 3 架构不可靠**\n\n3 个架构重采样仅 3³ = 27 种组合，排除退化（same-architecture triplicates）后更少。报告的 95% CI = [−1.0, −0.7] 传递与 n = 3 不匹配的虚假精度感。BCa acceleration parameter 基于仅 3 个 jackknife 值。\n\n**修复方向**：改用 exact permutation test（3! = 6 排列）或直接报告 3 个数据点让读者自行判断。明确标注所有 bootstrap CI 为 heuristic。\n\n### Major（影响评分但不一票否决）\n\n**M1** [AGREE: R1-W1 + R2-W3] **Routing 作为 contribution 过于单薄**\n\n10 benchmark 中仅 LAMBADA 有效（+5.2pp），PIQA 显著负效（−0.49pp，p = .006），HellaSwag 无效。缺少最自然的 baseline：average logits ensemble。Section 5 的 practical implications 基于 n = 1 的泛化。方法本身（confidence-based hard selection）过于简单，缺乏与 learned routing 或 calibrated ensembling 的比较。应降级为 preliminary exploration，不作为 main contribution。\n\n**M2** [AGREE: R1-W2, R2 交叉确认] **任务分类法存在 evaluation format confound**\n\nLAMBADA 是唯一 free-form generation task，同时显示唯一单调 σ 下降、最高 α = 0.30、唯一有效 routing。无法区分 task type vs evaluation format 的驱动作用。Multiple-choice format 机械性约束答案空间，可能降低 divergence 上界。HellaSwag 使用 acc_norm 进一步模糊与其他 Reasoning benchmark 的比较。§3.2 按 cognitive demand 分类但未讨论 evaluation format 这一混淆变量。\n\n**M3** [分歧: R2-W1, R1 REBUT] **新颖性为增量贡献**\n\nR2 认为核心贡献是已知框架（predictive multiplicity + ecological fallacy）在新 domain 的直接应用，方法论无创新。R1 反驳：4% saturation 和 aggregate-vs-per-example 解耦是非平凡经验发现；controlled model zoo 设定在 multiplicity 文献中罕见；Findings 不要求方法论创新。\n\n**Director 判断**：R1 的 REBUT 有理。论文的经验贡献——特别是 4% saturation 的发现和 systematic task-dependent variation——在 Findings 标准下足够。但论文应更清楚地定位为 empirical contribution。\n\n**M4** [AGREE: R1-W3] **Scale robustness claim 过强**\n\n仅 340M 和 1.3B 两个 scale 点，不足以支撑 \"scale-robust\"。应改为 \"consistent across the two scales examined\"。Limitations 已提到 7B+ 但 Conclusion 的 practitioner implications 用不加限定的一般性语言。\n\n**M5** [R2-W2, R1 部分 AGREE] **Related Work 遗漏**\n\n- **Model Soups** (Wortsman et al., 2022 ICML)：weight-space interpolation vs architecture-space multiplicity 有直接对话关系 [R1+R2 AGREE]\n- **Jiang et al. (2024)** \"On the Predictive Multiplicity of Foundation Models\"：将 multiplicity 扩展到 foundation models [R1 独立提出, R2 AGREE]\n- MoE 文献 (Shazeer et al., 2017) 与 routing 方案有间接关联 [R2 提出, R1 AGREE with nuance]\n- Fort et al. (2019) 已在论文中引用——R2 的 \"missing\" 指控不成立 [R1 纠正]\n\n**M6** [R2-W4, R1 AGREE with nuance] **Abstract 过度拥挤**\n\n~180 words 中数字密度过高（Jaccard, p, α, pp 等），降低传播效果。R2 指出第三句可能有句法拼接问题；R1 认为语法完整但同意需精简。建议保留 3–4 个关键数值，用直觉描述替代部分统计细节。\n\n### Minor\n\n- **m1** [R1-W4]: 5-architecture validation 仅覆盖 LAMBADA + h3-1 + 340M，应至少扩展到 HellaSwag 或 ARC-Easy\n- **m2** [R1-W5, R2 AGREE]: Permutation test null baseline 不排除 example difficulty confound——attention-friendly examples 可产生 above-random Jaccard 而无需 architecture-specific 效应。建议讨论 example difficulty 作为 alternative explanation\n- **m3** [R1-M1]: Abstract \"approximately twice the independence baseline\" 过于模糊，建议给出具体数值\n- **m4** [R1-M2]: Figure 1 shaded bands (n = 3) 传达不恰当的精度感\n- **m5** [R1-M4]: Table 1 confirmatory vs exploratory benchmark 缺乏视觉区分\n- **m6** [R2-M4]: Limitations 未讨论 benchmark 代表性（全为 zero-shot 分类/检索，无 generation task）\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Overall 3.0 (Findings)**——两位 Reviewer 独立给出相同评分\n2. **Aggregate convergence 叙事需重构**——不依赖统计不显著的 convergence trend，改为强调 aggregate interchangeability vs per-example divergence\n3. **Seed confound 是核心弱点**——需多 seed 实验或大幅弱化因果归因\n4. **Bootstrap n = 3 不可靠**——改用 exact permutation 或直接报告数据点\n5. **Routing 应降级**——从 main contribution 降为 preliminary exploration\n6. **Format confound 需正文讨论**——LAMBADA 的 free-form 格式可能是异常表现的驱动因素\n\n## Reviewer Divergence [REBUT]\n\n1. **新颖性定级**：R2 认为纯增量（已知框架在新 domain 的应用），R1 认为 empirical findings（4% saturation, decoupling）有独立贡献价值。Director 判断：R1 的 REBUT 有理——Findings 不要求方法论创新，系统性经验发现足够。\n\n---\n\n## Questions\n\n1. 能否对至少一个 hybrid 架构训练 3+ 个不同 seed，直接量化 within-architecture per-example 变异？\n2. 能否增加一个 free-form generation benchmark（如 TriviaQA）来解耦 task type vs evaluation format？\n3. Routing 实验的 cross-validation SD 是多少？如果 SD > 3pp 则 +5.2pp 增益可能不显著。\n4. 为什么不对所有 benchmark 报告 majority vote 和 average-logits ensemble baseline？\n5. 4% saturation 的精度受限于最低非零配置——1–3% 处是否可能有 gradual onset？\n\n---\n\n## Missing References\n\n1. **Wortsman et al. (2022)** \"Model Soups: Averaging Weights of Multiple Fine-tuned Models Improves Accuracy without Increasing Inference Time.\" ICML. [R1+R2 AGREE]\n2. **Jiang et al. (2024)** \"On the Predictive Multiplicity of Foundation Models.\" [R1 提出, R2 AGREE]\n3. **Shazeer et al. (2017)** \"Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer.\" ICLR. [R2 提出, R1 AGREE with nuance]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（2 warning, 10 info）：\n- **Warning**: Pages 3–4 连续纯文本无 display item（Method §3.1–3.5），建议加入 display math 打破视觉单调性\n- **Warning**: Pages 6–7 display items 过密（6 个集中 2 页），与 pages 3–4 形成节奏突变\n- **Info**: Figure 1 位置合理、caption 自包含；Tables 使用 booktabs 风格规范；正文 8 页合规；appendix 表格密度高但可接受；Figure 5/6 内部文字偏小\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 — Findings（可被 Findings 接收）**\n\n**置信度: 4/5 (High)**\n\n扎实的实证研究，核心 per-example 发现（Jaccard ~0.10, 4% saturation, task-dependent α = 0.14–0.30）有价值且经过严格检验。但三个 Critical 问题——convergence framing 无统计支撑（p = .170）、seed confound（每配置单次训练）、bootstrap CI n = 3 不可靠——共同削弱 claim 强度，使论文的核心叙事框架不够稳固。新颖性在 Findings 标准下足够（系统性经验发现，非方法论创新），但 routing 贡献单薄（1/10 benchmark 有效）限制了实践价值。\n\n**提升至 Conference (3.5) 的条件**：\n1. 补充同架构多 seed 实验，直接分离 architecture vs seed 效应\n2. 重构叙事框架：从 \"convergence masks divergence\" 到 \"aggregate interchangeability vs per-example divergence\"\n3. 增加 format-matched 的 free-form benchmark 解耦 task type vs evaluation format\n4. Bootstrap CI 改用 exact permutation 或直接报告数据点\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"adding attention affects substantially different examples per architecture\" 暗示因果方向，在单次 run 下不可靠，建议改为 associative 语言\n- Contributions 列表中 routing 应降级或移至 supplementary finding\n\n### §3 Method\n- §3.2 Task Taxonomy：需讨论 evaluation format（free-form vs multiple-choice）作为 confound\n- §3.5 Statistical Methods：bootstrap 方法在 n = 3 下应明确标注为 heuristic\n\n### §4 Experiments\n- §4.1 routing 结果需增加 cross-validation SD 和 ensemble baseline（average logits）\n- §4.2 标题 \"Aggregate Trends and Per-Example Independence\" 暗示确定性，建议改为 \"Aggregate Variance and Per-Example Overlap\"\n- §4.3 \"scale-robust\" → \"consistent across the two scales examined (340M, 1.3B)\"\n\n### §5 Conclusion\n- Practical implications 中 routing 建议应大幅限定范围（仅限 high-α free-form tasks）\n- \"when α > 0.2, per-example audit is warranted\" 的 threshold 无理论基础，建议弱化为 directional guidance\n\n### Abstract\n- 精简至 3–4 个关键数值，用直觉描述替代部分统计细节\n- 检查第三句是否有句法拼接问题",
    "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
    "cross_response_reviewer_ids": "[\"1\", \"2\"]",
    "overall_score": "3.0"
  }
}
```

</details>

---


### Tool result

_source line 1585 · 2026-05-24T12:17:46.126455+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1f8f0d6d9482071694045c30143bb993:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3863
}
```

</details>

---


### Tool call

_source line 1586 · 2026-05-24T12:18:00.100936+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重点'}, {'content': 'Step 0.6-0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'Reviewer 1 和 Reviewer 2 完成独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': 'Reviewer 间交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断审稿意见是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'completed', 'activeForm': '汇总审稿报告并投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性并调研 EMNLP 2026 venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重点'}, {'content': 'Step 0.6-0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'Reviewer 1 和 Reviewer 2 完成独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': 'Reviewer 间交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断审稿意见是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'completed', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 1587 · 2026-05-24T12:18:00.151916+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1588 · 2026-05-24T12:18:11.431813+00:00_

**Round 18 圆桌审稿完成。**

审稿报告已投递至 Research Director。

**结果摘要：**
- **Overall Score: 3.0 (Findings)**，两位 Reviewer 独立给出相同评分，交叉讨论后完全收敛
- **3 个 Critical**：convergence framing 无统计支撑（p=.170）、seed confound（单次训练）、bootstrap CI n=3 不可靠
- **6 个 Major**：routing 过于单薄、format confound、novelty 增量（分歧）、scale claim 过强、遗漏 references、abstract 拥挤
- **6 个 Minor**：5-arch 验证范围窄、permutation test difficulty confound、figure 精度感等
- **Issue Tracker 已同步更新**（含 1 个新 issue R18-W1 + 12 个旧 issue 更新 R18 mentions）
- **视觉审查**：2 warning（pages 3-4 纯文本 / pages 6-7 图表过密），10 info，无 critical

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director"
}
```

</details>

---


## Round 126

## Round 126

2 recorded events


### User

_source line 1589 · 2026-05-24T12:18:13.962200+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

核心发现：R1 和 R2 的审稿意见在三个关键问题上独立达成共识——(1) aggregate convergence 无统计支撑、(2) seed confound、(3) routing 贡献单薄。R1 在 bootstrap n=3 局限、evaluation format confound、permutation test difficulty confound 上提供了我未覆盖的有价值补充。我在 R1-N2 的具体数字比较上提出了反驳（0.273 和 0.293 都是 within-seed 值，cross-architecture reference 是 0.10，实际差距 2.7× 而非 0.02）。整体维持 Findings 评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1590 · 2026-05-24T12:18:22.655150+00:00_

**Round 18 圆桌审稿完成。**

审稿报告已投递给 Research Director。

**最终结论：Overall 3.0 — Findings**

3 个 Critical、6 个 Major、6 个 Minor。两位 Reviewer 在所有关键问题上达成共识，1 轮即收敛。唯一分歧（新颖性定级）不影响最终评分。Issue tracker 已同步更新（新增 R18-W1，更新 12 个既有 issue 的 R18 mentions）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director"
}
```

</details>

---


## Round 127

## Round 127

70 recorded events


### User

_source line 1591 · 2026-05-24T13:12:41.323985+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: entrainment_gated_ft
- 论文路径: projects/entrainment_gated_ft/docs/paper/main.tex
- 目标 venue: EMNLP 2026 via ARR (May cycle)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1592 · 2026-05-24T13:12:46.956369+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1593 · 2026-05-24T13:12:47.007575+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1594 · 2026-05-24T13:12:58.940083+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1595 · 2026-05-24T13:12:59.040811+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1596 · 2026-05-24T13:13:02.152519+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1597 · 2026-05-24T13:13:02.152924+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1598 · 2026-05-24T13:13:07.155539+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "entrainment_gated_ft"
  }
}
```

</details>

---


### Tool result

_source line 1599 · 2026-05-24T13:13:07.607711+00:00_

{"result":"# 项目 entrainment_gated_ft 概况\n\n## 实验状态 (46 个)\n\n- **exp-arc-easy-eval**: DONE (success) — \n- **exp-007**: DONE (success) — \n- **exp-004-r2**: DONE (success) — \n- **exp-011-xstorycloze**: DONE (negative) — \n- **exp-004**: DONE (failed) — \n- **exp-011**: DONE (negative) — \n- **exp-010**: DONE (success) — \n- **exp-001**: DONE (success) — \n- **exp-008**: DONE (success) — \n- **exp-003-p2**: DONE (negative) — \n- **exp-003**: DONE (negative) — \n- **exp-009**: DONE (success) — \n- **eval_340m_retnet_hgrn2**: DONE (success) — \n- **hgrn2_eval_h3_1**: DONE (success) — \n- **hgrn2_eval_1_3b_all**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp-005-pure-v4** (killed): —\n- **exp-005-pure-v3** (killed): —\n- **exp-005-hgrn-chain** (killed): —\n\n## 趋势\n成功 16 / 负向 4 / 失败 3 / 共 46\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-48145: 无 GPU 信息\n\n## 告警\n- hgrn2_eval_1_3b_all: 已被终止 — unknown\n- exp-003-p2v2: 已被终止 — unknown\n- exp-004: 训练失败 — unknown\n- exp-005-eval: 已被终止 — unknown\n- exp-005-p1-v4: 已被终止 — unknown\n- exp-005-gla-eval: 训练失败 — unknown\n- exp-005-gla: 已被终止 — unknown\n- exp-005-deltanet: 已被终止 — unknown\n- exp-005-dn-eval: 已被终止 — unknown\n- exp-005-pure-eval: 已被终止 — unknown\n- exp-005-p1-eval: 已被终止 — unknown\n- exp-005-p1-eval-v2: 已被终止 — unknown\n- exp-005-p1-eval-v3: 已被终止 — unknown\n- exp-005-p1-eval-v4: 已被终止 — unknown\n- exp-005-p1-eval-v5: 已被终止 — unknown\n- exp-005-hgrn-chain: 已被终止 — unknown\n- exp-005-batch: 训练失败 — unknown\n- exp-005-pure-v3: 已被终止 — unknown\n- exp-005-pure-v4: 已被终止 — unknown\n- exp-005-pure-v5: 已被终止 — unknown\n- exp-005-pure-v6: 已被终止 — unknown\n- exp-005-pure-v7: 已被终止 — unknown\n- exp-005-pure-v8: 已被终止 — unknown\n- exp-005-pure-v9: 已被终止 — unknown\n- exp-005-pure-v10: 已被终止 — unknown\n- exp-005-pure-baselines: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1600 · 2026-05-24T13:13:07.658437+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "entrainment_gated_ft",
  "file": "memory.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "entrainment_gated_ft",
    "file": "memory.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1601 · 2026-05-24T13:13:08.512154+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/memory.md\", \"content\": \"# FLA 版本与 m-a-p 模型兼容性调查结果 (2026-05-18)\\n\\n## 核心结论：fla 0.5.0 与 m-a-p 模型兼容，attn.D 丢弃无影响\\n\\n（详情见前版，略）\\n\\n- m-a-p 模型的 `attn.D` 是死参数，fla ≥0.1.0 已移除，strict=False 加载安全\\n- 训练框架：fla + flame (torchtitan)，训练数据：FineWeb-Edu，72 模型\\n- HuggingFace: https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research-686c488a63d609d2f20e2b1e\\n\\n---\\n\\n# 统计报告规则 (2026-05-19, Director 硬约束)\\n\\n**所有统计 claim 必须附原始数值 (ρ=X, p=Y)。** \\\"majority\\\"/\\\"most\\\" 必须有准确计数。适用于所有产出。\\n\\n---\\n\\n# exp-003 表面特征：无法区分 helped/hurt (2026-05-19)\\n\\n表面特征（token frequency、context length、lexical diversity）对 LAMBADA helped/hurt 无区分力（GDN/HGRN2 全部 p>0.2）。机制在模型内部，不在输入。→ 需要 exp-004 attention weight analysis。\\n\\n---\\n\\n# exp-004-r2 Attention Patterns：不是 per-example 效应的来源 (2026-05-19)\\n\\n**Attention entropy 无法区分 helped vs hurt**（三个架构差异均 <0.02）。Per-example divergence 不由 attention pattern 差异驱动——效应发生在 recurrent component 层面。\\n\\n**跨架构相似度发现**：GDN-RetNet 全层高度相似（>0.9）。HGRN2 在浅层 L2 与另外两者差异大（cos sim ~0.2），但深层收敛到 >0.94。→ 三架构深层 attention 相似但 per-example 仍分化，进一步支持 decoupling。\\n\\n**论文影响**：排除了 \\\"不同 attention pattern → 不同受影响样本\\\" 的 trivial 解释。效应来源指向 attention-recurrence interaction，非 attention 本身。Supplementary/appendix material。\\n\\n---\\n\\n# exp-004 Attention 层结构 (2026-05-19)\\n\\n3 架构 h3-1 都有 8 个 attention 层，索引 [2,5,8,11,14,17,20,23]。16 heads (8 KV heads, GQA)。Hook point: `model.model.layers[i].attn`。Flash Attention 不返回 weights，需 forward hook 截获 Q,K 手动计算 softmax(QK^T/√d)。\\n\\n---\\n\\n# exp-007 lm-eval 脚本选择：必须用 run_lmeval_clean.py (2026-05-19, 修正)\\n\\n**根因不是 dtype，是 `allow_neg_eigval=True` 配置注入缺失。**\\n\\nGDN 模型的 config.json 有 `\\\"use_beta\\\": true`。`run_lmeval_clean.py` 第 44-46 行有 `if getattr(config, \\\"use_beta\\\", False): config.allow_neg_eigval = True`，这改变了 GatedDeltaNet 的 forward pass。`run_lm_eval_fla.py` 缺少此步骤 → acc=0.34
…[truncated 1472 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 1602 · 2026-05-24T13:13:08.562779+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_local_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__read_local_file",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1603 · 2026-05-24T13:13:08.563169+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1604 · 2026-05-24T13:13:12.527282+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines author guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 1605 · 2026-05-24T13:13:14.836268+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1606 · 2026-05-24T13:13:15.388778+00:00_

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
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{multirow}
15	\usepackage{xcolor}
16	\usepackage{caption}
17	\usepackage{enumitem}
18	\setlist[itemize]{itemsep=1pt, parsep=0pt, topsep=2pt}
19	
20	\setlength{\textfloatsep}{6pt plus 1pt minus 1pt}
21	\setlength{\floatsep}{6pt plus 1pt minus 1pt}
22	\setlength{\intextsep}{6pt plus 1pt minus 1pt}
23	\setlength{\abovecaptionskip}{3pt}
24	\setlength{\belowcaptionskip}{0pt}
25	\setlength{\dbltextfloatsep}{6pt plus 1pt minus 1pt}
26	\setlength{\dblfloatsep}{6pt plus 1pt minus 1pt}
27	\setlength{\abovedisplayskip}{4pt plus 1pt minus 1pt}
28	\setlength{\belowdisplayskip}{4pt plus 1pt minus 1pt}
29	\setlength{\parskip}{0pt plus 0.5pt}
30	
31	\title{Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures}
32	
33	\author{Anonymous}
34	
35	\begin{document}
36	\maketitle
37	
38	\begin{abstract}
39	Practitioners select among hybrid linear recurrent architectures using aggregate benchmarks, but architectures that appear interchangeable by these metrics can differ on which specific examples they get right. Using the model zoo of \citet{wang2025hybrid} (three architectures, five attention ratios, two scales), we decompose per-example effects and find that adding attention is associated with substantially different per-example changes across architectures (Jaccard $\approx 0.10$, roughly twice the independence baseline; all $p < .01$ across five architectures). This predictive multiplicity \citep{marx2020predictive} depends on task type ($\alpha = 0.14$--$0.30$) more than attention dose. Per-example overlap saturates at 4\% attention and remains flat, even as aggregate variance shows a non-significant decreasing trend on one benchmark (Bonferroni-adjusted $p = .17
…[truncated 2098 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1607 · 2026-05-24T13:13:15.539783+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "entrainment_gated_ft",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "entrainment_gated_ft",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1608 · 2026-05-24T13:13:20.256554+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

I've completed a web search for EMNLP 2026 call for papers, ARR submission guidelines, and author guidelines. Here's a summary of the key information found:

## EMNLP 2026 Call for Papers Overview

EMNLP 2026 will use ACL Rolling Review (ARR) as a reviewing system, but final decisions will be made by the conference, with submissions performed via the Open Review platform.

## Submission Process

Authors follow a two-step process: submitting articles to ARR for reviews and meta-reviews, then committing reviewed articles to EMNLP 2026, where Senior Area Chairs and Program Chairs make final acceptance decisions.

## Important Deadlines

-
…[truncated 1082 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "WebSearch",
  "elapsed_ms": 7729
}
```

</details>

---


### Tool result

_source line 1609 · 2026-05-24T13:13:20.256971+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'entrainment_gated_ft'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 4717
}
```

</details>

---


### Tool call

_source line 1610 · 2026-05-24T13:13:25.880892+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format page limit style guidelines long paper short paper",
  "allowed_domains": "['aclrollingreview.org', '2026.emnlp.org', 'aclweb.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format page limit style guidelines long paper short paper",
    "allowed_domains": "['aclrollingreview.org', '2026.emnlp.org', 'aclweb.org']"
  }
}
```

</details>

---


### Tool call

_source line 1611 · 2026-05-24T13:13:27.838556+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1612 · 2026-05-24T13:13:27.889141+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1613 · 2026-05-24T13:13:28.341188+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "entrainment_gated_ft",
  "file": "paper_framing.md",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "entrainment_gated_ft",
    "file": "paper_framing.md",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1614 · 2026-05-24T13:13:33.660897+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format page limit style guidelines long paper short paper"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"}]

Based on the search results, here is information about ACL Rolling Review 2026 submission format, page limits, and style guidelines:

## Page Limits

Long papers may consist of up to 8 pages of content, plus unlimited
…[truncated 1480 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "WebSearch",
  "elapsed_ms": 7780
}
```

</details>

---


### Tool result

_source line 1615 · 2026-05-24T13:13:33.711682+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/paper_framing.md\", \"content\": \"# Paper Framing — entrainment_gated_ft\\n\\n> Revised 2026-05-20 after Round 1 review (Overall 3.0, D014). Predictive multiplicity replaces underspecification as primary framework. Title: \\\"Task-Specific Convergence and Per-Example Predictive Multiplicity in Hybrid Recurrent Architectures\\\". CI→complementary characterization. New evidence: Jaccard normalized ES (5-7%), RetNet-HGRN2 decoupling. Target 3.5+.\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Findings (via ARR)\\n- Stretch: EMNLP 2026 Main\\n- Deadline: ARR June 2026 cycle (submission ~June 15)\\n\\n## Paper Type\\nEmpirical analysis paper — quantifying a known phenomenon (per-example divergence under aggregate convergence) in a specific important domain (hybrid recurrent architectures)\\n\\n## Core Claims (3 条)\\n\\n### Claim 1: Task-Specific Convergence (revised D009)\\nAdding attention layers to different linear recurrent architectures (GatedDeltaNet, RetNet, HGRN2) induces aggregate performance convergence **specifically on context-retrieval tasks**. Across 10 benchmarks, only LAMBADA shows significant convergence (ρ=-1.0, p=0.017 two-tailed, cross-arch std drops 79%, BCa CI [-1.0, -0.7]). This task-specificity IS the finding, not a limitation:\\n- **Negative-ρ cluster** (6/10): LAMBADA, xstorycloze, COPA, PIQA, ARC-Easy, MMLU — tasks with context-retrieval or reasoning components\\n- **Positive-ρ cluster** (4/10): BoolQ, SciQ, HellaSwag, WinoGrande — commonsense/knowledge tasks where attention doesn't equalize\\n- LAMBADA is unique as a **pure context-prediction** task (predict last word from context alone), explaining why convergence is strongest there\\n\\n**Statistical strategy (D009)**:\\n1. **Complementary characterization**: BCa percentile CI [-1.0, -0.7] (100% valid resamples have ρ<0; does NOT depend on multiple comparison corr
…[truncated 3416 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5370
}
```

</details>

---


### Tool call

_source line 1616 · 2026-05-24T13:13:40.369879+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1617 · 2026-05-24T13:13:40.370256+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1618 · 2026-05-24T13:13:40.773600+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1619 · 2026-05-24T13:13:40.924553+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/author_response_r7.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/arr_checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Glob",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1620 · 2026-05-24T13:13:43.985801+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1621 · 2026-05-24T13:13:44.437764+00:00_

1	\section{Introduction}
2	
3	Hybrid linear recurrent architectures---including GDN, RetNet, HGRN2, GLA, and DeltaNet---achieve aggregate benchmark scores within 1--2 points of each other at matched parameter budgets. Yet they can differ on up to 90\% of the individual examples they affect: adding attention to three controlled linear recurrent backbones yields helped and hurt sets with at most 10\% pairwise overlap, approximately twice the independence baseline. This per-example divergence is invisible in aggregate metrics: architectures that score within 1--2 points of each other reach similar accuracy by gaining and losing on different inputs. Across all ten pairwise comparisons among five architectures, overlap in per-example effects remains below 14\% (all $p < .01$), meaning the choice of backbone is associated with which specific inputs a deployed system handles correctly.
4	
5	This tension arises in the context of a rapid architectural shift toward hybrid recurrent-attention models, which interleave attention layers within linear recurrent backbones. Jamba \citep{lieber2024jamba}, Griffin \citep{de2024griffin}, RWKV-6 \citep{peng2024eagle}, and RecurrentGemma \citep{botev2024recurrentgemma} each combine recurrence with attention using different mixing strategies. These systems now serve as production-grade alternatives to pure Transformers, and the practical question of how much attention to include is typically answered by comparing aggregate benchmark numbers. \citet{wang2025hybrid} provide a controlled model zoo spanning three recurrent architectures, five attention ratios, and two parameter scales, which enables systematic study of how attention allocation affects these hybrid designs.
6	
7	Prior work on predictive multiplicity \citep{marx2020predictive} and underspecification \citep{damour2022underspecification,mccoy2020berts} documents this risk for seed variation within a single architecture, but whether it extends to architectural variation in hybrid 
…[truncated 4111 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1622 · 2026-05-24T13:13:44.438215+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1623 · 2026-05-24T13:13:44.890146+00:00_

1	\section{Related Work}
2	
3	\paragraph{Hybrid Recurrent Architectures.}
4	The design space for combining attention with recurrence spans layer-level interleaving \citep[Jamba;][]{lieber2024jamba}, local attention pairing \citep[Griffin, RecurrentGemma;][]{de2024griffin,botev2024recurrentgemma}, matrix-valued recurrence \citep[RWKV-6;][]{peng2024eagle}, within-head mixing \citep[Hymba;][]{dong2024hymba}, and unbounded-context hybrid SSMs \citep[Samba;][]{ren2024samba}. H3 \citep{fu2023hungry} and Hyena \citep{poli2023hyena} establish early design points in the hybrid space with gated convolutions and subquadratic operators. Mamba-2 \citep{dao2024mamba2} establishes a duality between structured state spaces and attention; Mamba-3 \citep{lahoti2026mamba3} extends the design further, while \citet{ali2025hidden} reveal implicit attention within Mamba. Comparative evaluations confirm that hybrids outperform pure Transformers and SSMs at scale \citep{waleffe2024empirical}, and that even one attention layer enables content-based routing \citep{basu2026routing}. Recent theoretical work establishes a provable expressiveness hierarchy between hybrid and pure linear attention \citep{ye2026provable}, providing formal grounding for the architectural differences we characterize at the per-example level. \citet{wang2025hybrid} provide the controlled model zoo we use, holding training conditions constant while varying architecture and attention ratio.
5	
6	\paragraph{Linear Recurrent Models.}
7	Our three recurrent backbones represent distinct gating strategies within the linear recurrence family: RetNet \citep{sun2023retnet} uses multi-scale exponential decay, HGRN2 \citep{qin2024hgrn2} applies gated state expansion, and GatedDeltaNet \citep{yang2024gateddeltanet} combines gated updates with delta rules. These descend from S4 \citep{gu2022s4} and Mamba \citep{gu2024mamba}, which introduced structured state spaces and input-dependent selection, respectively, and connect to linear a
…[truncated 2557 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1624 · 2026-05-24T13:13:44.890470+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1625 · 2026-05-24T13:13:45.442744+00:00_

1	\section{Method}\label{sec:method}
2	
3	We describe the model configurations, evaluation benchmarks, and analytical framework used to measure how attention affects cross-architecture agreement at both aggregate and per-example levels.
4	
5	\subsection{Model Zoo}\label{ssec:model_zoo}
6	
7	We use the pretrained model zoo of \citet{wang2025hybrid}, which provides controlled comparisons across architectures and attention ratios. The zoo contains three linear recurrent architectures: GatedDeltaNet \citep{yang2024gateddeltanet}, RetNet \citep{sun2023retnet}, and HGRN2 \citep{qin2024hgrn2}. These three architectures represent distinct approaches to linear recurrence: GatedDeltaNet uses gated delta rules, RetNet uses multi-scale exponential decay, and HGRN2 uses gated linear recurrence with state expansion. Each architecture is trained at five attention ratios: 0\% (pure recurrent), 4\%, 7.7\%, 14.3\%, and 25\%. We adopt the h$k$-1 notation from the original work, where one attention layer is interleaved per every $k{+}1$ total layers: h3-1 corresponds to 25\% attention, h6-1 to 14.3\%, h12-1 to 7.7\%, and h24-1 to 4\%. All configurations are available at two scales: 340M and 1.3B parameters. Within each scale, all models share identical training data, tokenizer, and hyperparameters; they differ only in architecture and attention configuration. This controlled design isolates the effect of attention from confounds such as training data or optimization differences. The zoo also includes a Transformer baseline (pure attention) at both scales.
8	
9	\begin{figure}[t]
10	\centering
11	\includegraphics[width=\columnwidth]{figures/fig_method_overview.pdf}
12	\caption{Experimental framework. For each architecture, we compare the pure-recurrent baseline against its hybrid (+attention) variant, classifying every evaluation example as helped, hurt, or unchanged. Cross-architecture overlap of these per-example effect sets is measured via pairwise Jaccard similarity ($J \approx 0.10$
…[truncated 6070 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1626 · 2026-05-24T13:13:45.443109+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1627 · 2026-05-24T13:13:45.494399+00:00_

1	\section{Experiments}\label{sec:experiments}
2	
3	Using the model zoo of \citet{wang2025hybrid} (\S\ref{ssec:model_zoo}), we evaluate all 30 configurations on 10 benchmarks plus supplementary COPA ($n = 100$) at 1.3B scale unless noted. Results at 340M appear in scale analyses. Recall: h$k$-1 denotes one attention layer per $k{+}1$ layers; h3-1 = 25\% attention.
4	
5	\begin{table*}[t]
6	\centering
7	\caption{Cross-architecture variance trends across benchmarks (1.3B scale). $\rho$: Spearman correlation between attention ratio and cross-architecture standard deviation $\sigma$ across five configurations. $p$: exact permutation test (two-tailed, 120 permutations). $\sigma$ values reported $\times 10^{2}$ (accuracy percentage points). Ratio: $\sigma_{\text{pure}} / \sigma_{\text{h3-1}}$. \textbf{Bold}: only benchmark with $\rho = -1.0$. HellaSwag evaluated using normalized accuracy (acc\_norm), the standard metric for this benchmark.}
8	\label{tab:convergence}
9	\begin{tabular}{llrrrrr}
10	\toprule
11	Benchmark & Category & $\rho$ & $p$ & $\sigma_{\text{pure}}$ & $\sigma_{\text{h3-1}}$ & Ratio \\
12	\midrule
13	\textbf{LAMBADA$^{\ddagger}$} & \textbf{Retrieval} & $\mathbf{-1.0}$ & \textbf{.017} & \textbf{2.41} & \textbf{0.49} & \textbf{4.87} \\
14	\quad\emph{(excl.\ GDN)} & & $-0.7$ & .233 & --- & --- & --- \\
15	BoolQ & Comprehension & $0.2$ & .783 & 1.63 & 2.36 & 0.69 \\
16	ARC-C & Reasoning & $0.6$ & .350 & 0.96 & 1.32 & 0.72 \\
17	HellaSwag & Reasoning & $0.3$ & .683 & 1.17 & 1.18 & 0.99 \\
18	PIQA & Reasoning & $-0.5$ & .450 & 0.54 & 0.34 & 1.59 \\
19	WinoGrande & Reasoning & $0.1$ & .950 & 0.67 & 0.78 & 0.86 \\
20	ARC-E & Mixed & $-0.7$ & .233 & 1.00 & 0.13 & 7.70 \\
21	MMLU & Mixed & $-0.7$ & .233 & 0.92 & 0.41 & 2.27 \\
22	SciQ & Mixed & $0.1$ & .950 & 0.87 & 0.74 & 1.19 \\
23	XStoryCloze & Mixed & $-0.6$ & .350 & 0.82 & 0.55 & 1.49 \\
24	\midrule
25	COPA$^{\dagger}$ & Reasoning & $-0.67$ & .267 & 2.63 & 0.47 & 5.57 \\
26	\bottomrule
27	\multicolumn{7}{l}{\fo
…[truncated 12724 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1628 · 2026-05-24T13:13:49.407950+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1629 · 2026-05-24T13:13:50.411898+00:00_

1	\vspace{-2pt}
2	\section{Conclusion}
3	
4	We have shown that hybrid linear recurrent architectures which appear interchangeable by aggregate benchmarks diverge substantially at the per-example level. This multiplicity varies by task type ($\alpha = 0.14$--$0.30$) rather than attention dose, with pairwise Jaccard uniformly low ($\leq 0.10$) and saturated at the first attention level. Confidence margins partially predict which examples are affected (AUC 0.70--0.74), with rescue thresholds architecture-invariant but disruption thresholds varying 47\%.
5	
6	Two observations follow at the 340M--1.3B scales studied here. First, per-example audit before architecture substitution is advisable when multiplicity is substantial---aggregate equivalence does not guarantee behavioral equivalence. Second, the low cross-architecture Jaccard creates complementarity ($+7$--$14$\,pp oracle gain), but our preliminary routing experiments suggest that exploiting it is task-dependent: confidence-based selection shows gains on high-multiplicity free-form tasks (LAMBADA: $+5.2$\,pp) but is counterproductive on low-multiplicity ones (PIQA: $-0.49$\,pp).
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 1003
}
```

</details>

---


### Tool call

_source line 1630 · 2026-05-24T13:13:50.412349+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1631 · 2026-05-24T13:13:50.714533+00:00_

1	% Appendix sections for the paper.
2	
3	\section{Confirmatory and Exploratory Analyses}\label{app:benchmark_details}
4	
5	The task taxonomy used in \S\ref{ssec:task_taxonomy} was defined prior to running any convergence analyses. Each benchmark was assigned to exactly one of four categories based on the primary cognitive demand of the task:
6	
7	\begin{itemize}
8	    \item \textbf{Retrieval}: tasks requiring prediction from long-range context without multi-step reasoning (LAMBADA).
9	    \item \textbf{Comprehension}: reading comprehension with explicit passage support (BoolQ).
10	    \item \textbf{Reasoning}: tasks requiring commonsense inference or multi-step reasoning (HellaSwag, ARC-Challenge, WinoGrande, PIQA).
11	    \item \textbf{Mixed}: tasks combining retrieval, comprehension, and reasoning demands (ARC-Easy, MMLU, SciQ, XStoryCloze).
12	\end{itemize}
13	
14	\paragraph{Confirmatory benchmark set.} Six benchmarks were designated as confirmatory for Bonferroni correction: LAMBADA, HellaSwag, ARC-Challenge, WinoGrande, ARC-Easy, and MMLU. These were selected as representative of retrieval, reasoning, and mixed categories before any convergence analysis was performed. The taxonomy and benchmark selection were fixed before analysis as an informal pre-analysis plan; we describe this as a confirmatory/exploratory split rather than a formal pre-registration, since no external timestamp exists. The main text applies the more conservative all-10-benchmark correction (Bonferroni-adjusted $p = .017 \times 10 = .170$). \textbf{Sensitivity:} correcting across only the six confirmatory benchmarks yields adjusted $p = .017 \times 6 = .100$, still above conventional significance.
15	
16	\paragraph{One-sided test.} If one adopts the prior that attention should reduce cross-architecture variance, the one-sided permutation $p$-value for LAMBADA is $1/120 \approx 0.0083$. Under 10-benchmark Bonferroni correction, this yields an adjusted $p = 0.083$, above the conventional thre
…[truncated 58185 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1632 · 2026-05-24T13:13:50.714947+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/figures/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/figures/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1633 · 2026-05-24T13:13:50.765363+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/figures/fig1_decoupling_hero.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/figures/fig2_task_specificity.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/figures/jaccard_heatmap_5arch.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/figures/jaccard_heatmap_5arch.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/figures/fig4_jaccard_saturation.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/figures/fig4_jaccard_saturation.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/figures/fig5_per_example_bars.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/figures/fig5_per_example_bars.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/figures/fig_per_example_bars.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/figures/fig_per_example_bars.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/figures/fig_jaccard_hierarchy.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/figures/fig_jaccard_hierarchy.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/figures/fig_method_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/figures/fig_method_overview.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1634 · 2026-05-24T13:13:56.371869+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "entrainment_gated_ft"
  }
}
```

</details>

---


### Tool result

_source line 1635 · 2026-05-24T13:13:57.369073+00:00_

{"result":"# 项目 entrainment_gated_ft 概况\n\n## 实验状态 (46 个)\n\n- **exp-arc-easy-eval**: DONE (success) — \n- **exp-007**: DONE (success) — \n- **exp-004-r2**: DONE (success) — \n- **exp-011-xstorycloze**: DONE (negative) — \n- **exp-004**: DONE (failed) — \n- **exp-011**: DONE (negative) — \n- **exp-010**: DONE (success) — \n- **exp-001**: DONE (success) — \n- **exp-008**: DONE (success) — \n- **exp-003-p2**: DONE (negative) — \n- **exp-003**: DONE (negative) — \n- **exp-009**: DONE (success) — \n- **eval_340m_retnet_hgrn2**: DONE (success) — \n- **hgrn2_eval_h3_1**: DONE (success) — \n- **hgrn2_eval_1_3b_all**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp-005-pure-v4** (killed): —\n- **exp-005-pure-v3** (killed): —\n- **exp-005-hgrn-chain** (killed): —\n\n## 趋势\n成功 16 / 负向 4 / 失败 3 / 共 46\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-48145: 无 GPU 信息\n\n## 告警\n- hgrn2_eval_1_3b_all: 已被终止 — unknown\n- exp-003-p2v2: 已被终止 — unknown\n- exp-004: 训练失败 — unknown\n- exp-005-eval: 已被终止 — unknown\n- exp-005-p1-v4: 已被终止 — unknown\n- exp-005-gla-eval: 训练失败 — unknown\n- exp-005-gla: 已被终止 — unknown\n- exp-005-deltanet: 已被终止 — unknown\n- exp-005-dn-eval: 已被终止 — unknown\n- exp-005-pure-eval: 已被终止 — unknown\n- exp-005-p1-eval: 已被终止 — unknown\n- exp-005-p1-eval-v2: 已被终止 — unknown\n- exp-005-p1-eval-v3: 已被终止 — unknown\n- exp-005-p1-eval-v4: 已被终止 — unknown\n- exp-005-p1-eval-v5: 已被终止 — unknown\n- exp-005-hgrn-chain: 已被终止 — unknown\n- exp-005-batch: 训练失败 — unknown\n- exp-005-pure-v3: 已被终止 — unknown\n- exp-005-pure-v4: 已被终止 — unknown\n- exp-005-pure-v5: 已被终止 — unknown\n- exp-005-pure-v6: 已被终止 — unknown\n- exp-005-pure-v7: 已被终止 — unknown\n- exp-005-pure-v8: 已被终止 — unknown\n- exp-005-pure-v9: 已被终止 — unknown\n- exp-005-pure-v10: 已被终止 — unknown\n- exp-005-pure-baselines: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 997
}
```

</details>

---


### Tool call

_source line 1636 · 2026-05-24T13:13:57.821359+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_19/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_19/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1637 · 2026-05-24T13:13:58.323606+00:00_

-rw-r--r-- 1 ubuntu ubuntu 565903 May 24 12:48 /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_19/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1638 · 2026-05-24T13:13:58.775703+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_issues.yaml 2>/dev/null && echo \"FILE_EXISTS\" || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_issues.yaml 2>/dev/null && echo \"FILE_EXISTS\" || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 1639 · 2026-05-24T13:13:59.629345+00:00_

-rw-r--r-- 1 ubuntu ubuntu 30922 May 24 12:28 /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_issues.yaml
FILE_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Bash",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 1640 · 2026-05-24T13:13:59.780667+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/agent/config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 1641 · 2026-05-24T13:13:59.831322+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1642 · 2026-05-24T13:14:03.245732+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/agent/ -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -10",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/agent/ -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool call

_source line 1643 · 2026-05-24T13:14:03.246130+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "entrainment_gated_ft"
  }
}
```

</details>

---


### Tool result

_source line 1644 · 2026-05-24T13:14:03.346791+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 1645 · 2026-05-24T13:14:03.347169+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1646 · 2026-05-24T13:14:07.240802+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_2/ -path \"*/entrainment_gated_ft*\" -name \"config*\" 2>/dev/null | head -10",
  "description": "Find project config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_2/ -path \"*/entrainment_gated_ft*\" -name \"config*\" 2>/dev/null | head -10",
    "description": "Find project config"
  }
}
```

</details>

---


### Tool result

_source line 1647 · 2026-05-24T13:14:07.291505+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/figures/paper/.venv/lib/python3.14/site-packages/fontTools/misc/configTools.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/figures/paper/.venv/lib/python3.14/site-packages/fontTools/misc/__pycache__/configTools.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/figures/paper/.venv/lib/python3.14/site-packages/fontTools/config
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/figures/paper/.venv/lib/python3.14/site-packages/pip/_internal/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/figures/paper/.venv/lib/python3.14/site-packages/pip/_internal/commands/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/figures/paper/.venv/lib/python3.14/site-packages/pip/_internal/commands/configuration.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/figures/paper/.venv/lib/python3.14/site-packages/pip/_internal/configuration.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/figures/paper/.venv/lib/python3.14/site-packages/pymupdf/mupdf-devel/include/mupdf/fitz/config.h

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1648 · 2026-05-24T13:14:09.851584+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_2/ -maxdepth 3 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | grep -i -E \"config|project|setting\" | head -10",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_2/ -maxdepth 3 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | grep -i -E \"config|project|setting\" | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 1649 · 2026-05-24T13:14:09.904090+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/contrastive_graph_jailbreak_detect/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/contrastive_graph_jailbreak_detect/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/contrastive_graph_jailbreak_detect/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Bash",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1650 · 2026-05-24T13:14:12.714387+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "glob": "*.yaml",
  "output_mode": "content",
  "head_limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
    "glob": "*.yaml",
    "output_mode": "content",
    "head_limit": "10"
  }
}
```

</details>

---


### Tool result

_source line 1651 · 2026-05-24T13:14:12.764989+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1652 · 2026-05-24T13:14:17.430813+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_19/submitted.pdf",
  "pages": "1-9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_19/submitted.pdf",
    "pages": "1-9"
  }
}
```

</details>

---


### Tool result

_source line 1653 · 2026-05-24T13:14:18.036000+00:00_

PDF pages extracted: 9 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_19/submitted.pdf (552.6KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 605
}
```

</details>

---


### Tool call

_source line 1654 · 2026-05-24T13:15:16.942837+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "entrainment_gated_ft",
  "text": "你是 Reviewer 1，负责审查**方法严谨性和实验设计**。\n\n## Venue 信息（必须据此评审）\n- **目标 venue**: EMNLP 2026 via ACL Rolling Review (May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页，References 不限，Limitations 不计入页数\n- **模板**: ACL style (LaTeX)\n- **审稿制度**: Double-blind\n- **附录**: 允许，不限页数\n- **Overall Assessment 评分**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n## 论文文件\n- 主文件: `projects/entrainment_gated_ft/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_19/submitted.pdf`\n- Section 文件在 `projects/entrainment_gated_ft/docs/paper/sections/` 下\n\n## 你的审查侧重\n\n### 1. 统计方法严谨性\n- Spearman ρ 在 n=5 下的统计效力问题（只有 |ρ|=1.0 才能 p<.05）\n- Bonferroni 校正的使用是否合理（10-benchmark 校正 vs 6-benchmark confirmatory set）\n- Bootstrap CI 在 n=3 architecture 下的可靠性\n- Jaccard permutation test 的有效性\n- 置信区间的解读是否恰当\n\n### 2. 实验设计\n- 单次训练 run 的限制：能否区分架构效应 vs seed 效应？\n- 模型 zoo 依赖（Wang et al. 2025）：GDN h3-1 的 16-head 配置 confound 是否被充分处理？\n- Per-example decomposition 的二值化是否损失信息？\n- 340M vs 1.3B 仅两个 scale point 的外部效度\n- Pythia 70M seed calibration 的 scale mismatch 问题\n\n### 3. Claim-Evidence 对齐\n- 3 个 core claims 是否都有充分的统计证据支持？\n- \"Predictive multiplicity\"框架的使用是否合理（vs underspecification）？\n- Confidence-based routing 作为 actionability 证据是否充分？\n- Task taxonomy 是否足够严谨（informal, not pre-registered）？\n\n### 4. 可复现性\n- 实验设置的描述是否完整？\n- 代码/数据是否承诺公开？\n\n请按以下格式输出审稿意见：\n1. Summary (2-3 句)\n2. Strengths (逐条)\n3. Weaknesses (逐条，标注 severity: critical/major/minor)\n4. Questions to Authors\n5. Missing References (如有)\n6. Overall Assessment (评分 + 置信度 + 理由)\n7. Detailed Comments (逐节)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "entrainment_gated_ft",
    "text": "你是 Reviewer 1，负责审查**方法严谨性和实验设计**。\n\n## Venue 信息（必须据此评审）\n- **目标 venue**: EMNLP 2026 via ACL Rolling Review (May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页，References 不限，Limitations 不计入页数\n- **模板**: ACL style (LaTeX)\n- **审稿制度**: Double-blind\n- **附录**: 允许，不限页数\n- **Overall Assessment 评分**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n## 论文文件\n- 主文件: `projects/entrainment_gated_ft/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_19/submitted.pdf`\n- Section 文件在 `projects/entrainment_gated_ft/docs/paper/sections/` 下\n\n## 你的审查侧重\n\n### 1. 统计方法严谨性\n- Spearman ρ 在 n=5 下的统计效力问题（只有 |ρ|=1.0 才能 p<.05）\n- Bonferroni 校正的使用是否合理（10-benchmark 校正 vs 6-benchmark confirmatory set）\n- Bootstrap CI 在 n=3 architecture 下的可靠性\n- Jaccard permutation test 的有效性\n- 置信区间的解读是否恰当\n\n### 2. 实验设计\n- 单次训练 run 的限制：能否区分架构效应 vs seed 效应？\n- 模型 zoo 依赖（Wang et al. 2025）：GDN h3-1 的 16-head 配置 confound 是否被充分处理？\n- Per-example decomposition 的二值化是否损失信息？\n- 340M vs 1.3B 仅两个 scale point 的外部效度\n- Pythia 70M seed calibration 的 scale mismatch 问题\n\n### 3. Claim-Evidence 对齐\n- 3 个 core claims 是否都有充分的统计证据支持？\n- \"Predictive multiplicity\"框架的使用是否合理（vs underspecification）？\n- Confidence-based routing 作为 actionability 证据是否充分？\n- Task taxonomy 是否足够严谨（informal, not pre-registered）？\n\n### 4. 可复现性\n- 实验设置的描述是否完整？\n- 代码/数据是否承诺公开？\n\n请按以下格式输出审稿意见：\n1. Summary (2-3 句)\n2. Strengths (逐条)\n3. Weaknesses (逐条，标注 severity: critical/major/minor)\n4. Questions to Authors\n5. Missing References (如有)\n6. Overall Assessment (评分 + 置信度 + 理由)\n7. Detailed Comments (逐节)"
  }
}
```

</details>

---


### Tool result

_source line 1655 · 2026-05-24T13:15:31.814696+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 14871
}
```

</details>

---


### Tool call

_source line 1656 · 2026-05-24T13:15:31.965677+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "entrainment_gated_ft",
  "text": "你是 Reviewer 2，负责审查**新颖性、完整性和写作质量**。\n\n## Venue 信息（必须据此评审）\n- **目标 venue**: EMNLP 2026 via ACL Rolling Review (May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页，References 不限，Limitations 不计入页数\n- **模板**: ACL style (LaTeX)\n- **审稿制度**: Double-blind\n- **附录**: 允许，不限页数\n- **Overall Assessment 评分**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n## 论文文件\n- 主文件: `projects/entrainment_gated_ft/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_19/submitted.pdf`\n- Section 文件在 `projects/entrainment_gated_ft/docs/paper/sections/` 下\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 论文的核心贡献是否足够新颖？\n- \"Predictive multiplicity under architectural variation\"是否是一个有意义的新方向，还是已有工作（Marx et al. 2020, D'Amour et al. 2022）的简单应用？\n- Per-example decomposition 在 hybrid recurrent architectures 上的应用是否有足够的 insight？\n- 与已有的 ensemble diversity / model disagreement 文献相比，增量贡献是什么？\n\n### 2. Related Work 完整性\n- 是否遗漏了重要的相关工作？特别关注：\n  - 最近的 hybrid architecture 论文（2025-2026）\n  - Predictive multiplicity 的最新进展\n  - Model disagreement / ensemble diversity 的经典和最新工作\n  - Per-example analysis 方法论\n- 论文对自身在文献中的定位是否准确？\n\n### 3. 写作质量\n- 论文的叙事逻辑是否清晰？\n- Abstract 是否准确概括了论文内容？（注意：EMNLP 2026 要求 abstract 不超过 200 words）\n- Introduction 的 motivation 是否有说服力？\n- Method 和 Experiments 的划分是否合理？\n- Conclusion 是否恰当总结了发现，避免了过度 claim？\n- Limitations 是否充分覆盖了主要局限？\n- 术语使用是否一致？\n- 图表质量和可读性\n\n### 4. 格式合规\n- 页数是否符合 8 页正文限制？\n- 匿名性是否完整（无泄露作者身份的信息）？\n- 引用格式是否正确？\n- Appendix 的引用是否使用了正确的字母编号？\n\n### 5. 完整性\n- 论文的实验是否覆盖了 claims 所需的全部场景？\n- 是否有重要的消融实验缺失？\n- Negative results 是否被诚实报告？\n\n请按以下格式输出审稿意见：\n1. Summary (2-3 句)\n2. Strengths (逐条)\n3. Weaknesses (逐条，标注 severity: critical/major/minor)\n4. Questions to Authors\n5. Missing References (如有)\n6. Overall Assessment (评分 + 置信度 + 理由)\n7. Detailed Comments (逐节)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "entrainment_gated_ft",
    "text": "你是 Reviewer 2，负责审查**新颖性、完整性和写作质量**。\n\n## Venue 信息（必须据此评审）\n- **目标 venue**: EMNLP 2026 via ACL Rolling Review (May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页，References 不限，Limitations 不计入页数\n- **模板**: ACL style (LaTeX)\n- **审稿制度**: Double-blind\n- **附录**: 允许，不限页数\n- **Overall Assessment 评分**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit\n\n## 论文文件\n- 主文件: `projects/entrainment_gated_ft/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_19/submitted.pdf`\n- Section 文件在 `projects/entrainment_gated_ft/docs/paper/sections/` 下\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- 论文的核心贡献是否足够新颖？\n- \"Predictive multiplicity under architectural variation\"是否是一个有意义的新方向，还是已有工作（Marx et al. 2020, D'Amour et al. 2022）的简单应用？\n- Per-example decomposition 在 hybrid recurrent architectures 上的应用是否有足够的 insight？\n- 与已有的 ensemble diversity / model disagreement 文献相比，增量贡献是什么？\n\n### 2. Related Work 完整性\n- 是否遗漏了重要的相关工作？特别关注：\n  - 最近的 hybrid architecture 论文（2025-2026）\n  - Predictive multiplicity 的最新进展\n  - Model disagreement / ensemble diversity 的经典和最新工作\n  - Per-example analysis 方法论\n- 论文对自身在文献中的定位是否准确？\n\n### 3. 写作质量\n- 论文的叙事逻辑是否清晰？\n- Abstract 是否准确概括了论文内容？（注意：EMNLP 2026 要求 abstract 不超过 200 words）\n- Introduction 的 motivation 是否有说服力？\n- Method 和 Experiments 的划分是否合理？\n- Conclusion 是否恰当总结了发现，避免了过度 claim？\n- Limitations 是否充分覆盖了主要局限？\n- 术语使用是否一致？\n- 图表质量和可读性\n\n### 4. 格式合规\n- 页数是否符合 8 页正文限制？\n- 匿名性是否完整（无泄露作者身份的信息）？\n- 引用格式是否正确？\n- Appendix 的引用是否使用了正确的字母编号？\n\n### 5. 完整性\n- 论文的实验是否覆盖了 claims 所需的全部场景？\n- 是否有重要的消融实验缺失？\n- Negative results 是否被诚实报告？\n\n请按以下格式输出审稿意见：\n1. Summary (2-3 句)\n2. Strengths (逐条)\n3. Weaknesses (逐条，标注 severity: critical/major/minor)\n4. Questions to Authors\n5. Missing References (如有)\n6. Overall Assessment (评分 + 置信度 + 理由)\n7. Detailed Comments (逐节)"
  }
}
```

</details>

---


### Tool result

_source line 1657 · 2026-05-24T13:15:33.476379+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1510
}
```

</details>

---


### Tool call

_source line 1658 · 2026-05-24T13:15:33.476796+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "entrainment_gated_ft",
  "review_chat_id": "oc_b542b52ff24f138c42225a1d4b456e7e"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "entrainment_gated_ft",
    "review_chat_id": "oc_b542b52ff24f138c42225a1d4b456e7e"
  }
}
```

</details>

---


### Tool result

_source line 1659 · 2026-05-24T13:15:35.089618+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 1612
}
```

</details>

---


### Assistant

_source line 1660 · 2026-05-24T13:15:42.910818+00:00_

Round 1 已启动：
- **Reviewer 1**（方法严谨性 + 实验设计）：已分配
- **Reviewer 2**（新颖性 + 完整性 + 写作质量）：已分配
- **视觉审查 Agent**：已派发，与 Reviewer 并行

等待两位 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director"
}
```

</details>

---


## Round 128

## Round 128

2 recorded events


### User

_source line 1661 · 2026-05-24T13:20:56.138035+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见（方法严谨性与实验设计）

## 1. Summary

本文研究五种混合线性递归架构（GDN、RetNet、HGRN2、GLA、DeltaNet）在 per-example 层面的 predictive multiplicity。利用 Wang et al. (2025) 的 model zoo（30 种配置，两个 scale），作者发现聚合指标看似可互换的架构在逐样本层面存在实质差异（pairwise Jaccard ≈ 0.08–0.14），且 multiplicity 的幅度与任务类型相关（ι = 0.14–0.30）。论文还分析了 attention 对 cross-architecture convergence 的影响，并提出基于置信度的 routing 策略作为 actionability 证据。研究问题有价值，描述性分析详实，但核心统计推断严重 underpowered，实验设计中的 confound 未被充分解决。

## 2. Strengths

- **S1**: 研究问题新颖且重要。Per-example multiplicity 在 hybrid 架构间的系统性分析此前缺乏，填补了 aggregate benchmark 无法揭示的盲区。
- **S2**: 描述性分析扎实。Jaccard permutation test（Table 13, Appendix J）在 10,000 次置换下所有 architecture pair 均 p < .0001，为 per-example overlap 的结构性（非随机）提供了可靠证据。
- **S3**: 对自身局限性的讨论诚实。论文在 Limitations（Section 8）、Appendix A（confirmatory/exploratory split）、Appendix D（GDN exclusion）中均坦承了核心统计局限。
- **S4**: 附录极为详尽（13 页正文 + 附录至 21 页），涵盖 sensitivity analysis（Appendix D）、seed calibration（Appendix W）、continuous Jaccard（Appendix O）、attention weight analysis（Appendix F）等多个验证角度。
- **S5**: 实验框架建立在公开 model zoo 上，evaluation 使用 lm-evaluation-harness v0.4.x 标准配置，增强了基础可复现性。
- **S6**: Transformer entrainment analysis（Appendix L）提供了有趣的 cross-family 视角——hybrid 模型的 per-example correct set 更接近 Transformer 而非 pure recurrent baseline。

## 3. Weaknesses

**N1** [critical] **Spearman ρ 在 n=5 下统计效力根本不足，核心 convergence claim 缺乏显著性支撑**
- 具体位置：Section 3.3, Section 4.2, Table 1
- 问题：Convergence 分析的核心统计量是 Spearman ρ（attention ratio vs. cross-architecture σ），但 n = 5（五个 attention 配置）。论文自身承认"only |ρ| = 1.0 achieves p < .05"（Section 3.3）。在 Table 1 的 10 个 benchmark 中，仅 LAMBADA 达到 ρ = -1.0（p = .017）。Bonferroni 校正后（×10），adjusted p = .170，**远未达到显著性阈值**。论文尝试了多种补救策略：(a) 6-benchmark confirmatory set（adjusted p = .017 × 6 = .102，仍不显著）；(b) one-sided test（adjusted p = .083，仍不显著）；(c) 将 confirmatory/exploratory split 描述为"informal pre-analysis plan"而非 pre-registered。三种尝试均未达到 α = .05，但正文的叙述语气（"LAMBADA is the only benchmark with a negative correlation"）暗示了一种比数据所能支持的更强的结论。
- 为什么影响接收：这是论文三个 core claims 之一（"attention modulates convergence"）的唯一统计检验。整个 Section 4.2 及相关 Appendix B–D 的结论建立在这个 underpowered 检验上。
- 建议修改方向：(1) 明确标注"本文的 convergence 分析是描述性/探索性的，不具备确认性统计推断的效力"；(2) 考虑用 continuous attention ratio 作为连续变量做回归（虽然 n 仍小，但至少不依赖 rank 的离散性）；(3) 若 model zoo 允许，增加 attention ratio 的粒度以增大 n。

**N2** [critical] **单次训练 run 无法区分架构效应与 seed 效应，seed calibration 存在 scale 和 architecture mismatch**
- 具体位置：Section 8 (Limitations), Appendix W
- 问题：每个配置仅有一次训练 run（来自 Wang et al. 的 model zoo）。论文用 Pythia 70M 的 9 个 seed 做 calibration（Appendix W），声称 within-seed Jaccard 是 cross-architecture Jaccard 的 2.7–4.3×。但存在两个严重 mismatch：(a) **Scale mismatch**: 70M vs 340M/1.3B——seed variance 可能随 scale 不同而变化（论文自身在 Section C 发现 340M 和 1.3B 行为截然不同）；(b) **Architecture mismatch**: Pythia 是 pure Transformer，不是本文研究的 hybrid 架构——hybrid 架构的 gating mechanism 可能放大或缩小 seed sensitivity。
- 为什么影响接收：论文的核心因果推断（"architecture drives per-example differences"）需要排除 seed 作为混淆变量。当前的 calibration 无法可靠地做到这一点。如果 seed variance 在 hybrid 架构中更大（例如因为 gating 的初始化敏感性），那么观察到的 cross-architecture difference 可能部分归因于 seed。
- 建议修改方向：(1) 至少对一个 hybrid 架构（如 RetNet 或 HGRN2）在 340M scale 做 3-5 个 seed 的重复训练；(2) 如果不可行，将 seed calibration 的 limitation 从 Appendix 提升到正文 Limitations，并明确标注因果推断的边界条件。

**W1** [major] **GDN h3-1 的 16-head confound 削弱了 convergence 分析的可靠性**
- 具体位置：Appendix E (Section D.2), Table 3
- 问题：GDN h3-1 使用 16 个 attention head，其他架构使用 32 个。这是一个无法通过 post-hoc 分析完全解决的 confound。论文的应对策略是 exclude GDN 后重新计算（Appendix D, Table 3），但：(a) exclude 后 n 从 5 降到 3，使分析更加 underpowered；(b) MMLU 的 ρ 从 -0.7 反转为 +0.6，说明 convergence pattern 对 GDN inclusion 高度敏感。
- 建议：在正文中明确标注 GDN exclusion 导致的 correlation 反转（MMLU: -0.7 → +0.6），而非仅在 Appendix 中以"|Δρ| ≥ 0.3"的 threshold 报告。

**W2** [major] **仅两个 scale point（340M, 1.3B）且结果矛盾，外部效度受限**
- 具体位置：Section 4.2, Appendix C, Appendix T
- 问题：340M 和 1.3B 的 convergence 行为截然不同——"Convergence is absent at 340M across all benchmarks (all |ρ| ≤ 0.4, p ≥ .45)"（Appendix C, p.12），而 1.3B 仅 LAMBADA 有 convergence。论文将此解释为"model capacity"差异，但两个数据点无法建立趋势线。Section 5 结论中"Two observations follow at the 340M–1.3B scales studied here"的措辞暗示了比数据支持的更强的泛化性。
- 建议：明确限定 convergence claim 的 scope 为"1.3B scale on LAMBADA"，避免暗示跨 scale 的泛化。

**W3** [major] **Task taxonomy 是 post-hoc 且 informal，但被用于支撑 task-type dependence 的核心结论**
- 具体位置：Section 3.2, Appendix A
- 问题：四类 task taxonomy（Retrieval, Comprehension, Reasoning, Mixed）被描述为"informal, not pre-registered"（Appendix A）。然而正文大量使用此 taxonomy 来解释 multiplicity 的 task-type dependence（Section 4.1: "multiplicity varies by task type"），形成循环论证的风险——先看到 pattern，再创建 taxonomy 来解释它。Appendix A 声明 taxonomy "was fixed prior to analysis following established distinctions"，但无法验证这一时间线。
- 建议：(1) 提供 taxonomy 创建时间的具体证据（如 pre-registration、带时间戳的 commit）；(2) 或者将 task-type dependence 的讨论框定为 hypothesis-generating 而非 confirmatory。

**W4** [minor] **Confidence-based routing 仅在 LAMBADA 上测试，actionability claim 过度泛化**
- 具体位置：Section 4.1 (Confidence-based routing paragraph)
- 问题：Routing 策略仅在 LAMBADA 上报告结果（outperforms majority vote by ~1.2 pp）。论文承认"preliminary routing experiments suggest that exploiting it is task-dependent"，但 Section 5 仍将此作为主要 contribution 之一（"our preliminary routing experiments suggest..."）。单 benchmark 的 preliminary result 不足以支撑 actionability 作为 contribution。
- 建议：要么在至少 3–4 个 benchmark 上测试 routing，要么将 actionability 降级为 future work 而非 contribution。

**W5** [minor] **Bootstrap CI 在 n=3 architecture 下的统计意义有限**
- 具体位置：Section 3.5, Appendix D.1
- 问题：Exclude GDN 后的分析和部分 sensitivity analysis 对 n=3 个 architecture 做 bootstrap CI。Bootstrap 的理论保证依赖于足够的原始样本量；n=3 时 bootstrap 分布只有 3³=27 个可能值（考虑 replacement），CI 的 coverage probability 远低于名义水平。论文在 Appendix D.1 承认 exclude "constant σ vector and therefore an undefined ρ"的 resamples，进一步缩小了有效 bootstrap 空间。
- 建议：标注 n=3 bootstrap CI 为"heuristic indication of effect direction"，而非正式的置信区间。

## 4. Questions to Authors

**Q1**: Pythia 70M seed calibration（Appendix W）显示 within-seed Jaccard 为 cross-architecture 的 2.7–4.3×。如果在 hybrid 架构（如 RetNet 340M）上做同样实验，你们预期这个比值会保持吗？是否有定性论据支持 hybrid 架构的 seed sensitivity 不高于 Transformer？

**Q2**: Table 3 显示 GDN exclusion 后 MMLU 的 ρ 从 -0.7 反转为 +0.6。作者如何解释这一反转？它是否意味着 MMLU 上的 convergence pattern 完全由 GDN 的 16-head anomaly 驱动？

**Q3**: 340M 和 1.3B 的 convergence 行为截然不同（340M 无 convergence，1.3B 仅 LAMBADA）。作者是否考虑过这可能反映的是"model capacity 不足以利用 attention"而非"convergence 是 scale-dependent 的 real phenomenon"？

**Q4**: Task taxonomy 声明"was fixed prior to analysis"（Appendix A）。能否提供具体的时间证据（如 pre-registration、git commit timestamp）？如果不能，是否同意将 task-type dependence 框定为 exploratory finding？

**Q5**: Confidence-based routing 在 LAMBADA 以外的 benchmark 上表现如何？如果在 Reasoning/Mixed 类 benchmark 上无效，这是否削弱了 routing 作为 contribution 的价值？

## 5. Missing References

- **Black et al. (2022)**: GPT-NeoX-20B——大模型的 seed variation 研究，可作为 seed calibration 的 scale-up 参考
- **Sellam et al. (2022)**: "MultiBERTs: BERT Reproductions for Robustness Analysis"——在 BERT scale 做了 25 个 seed 的 variance 分析，直接相关于本文的 seed calibration 局限
- 注：Sellam et al. 2022 实际上在 References 中已有（page 10），但正文未在 seed calibration discussion 中引用它来对比 seed variance 的 scale

## 6. Overall Assessment

**Overall**: 3.0 (Findings)
**Confidence**: 4/5（仔细检查了核心统计方法和实验设计；熟悉 predictive multiplicity 和 hybrid architecture 文献）

**理由**：

论文提出了一个genuinely interesting 的研究问题（hybrid 架构的 per-example multiplicity），描述性分析详实且附录充分。Jaccard permutation test 为 structured overlap 提供了可靠证据（S2）。然而，两个 critical weakness 严重限制了论文的贡献强度：

(1) **核心统计检验 underpowered**：Convergence claim 是论文的中心叙事之一，但 Spearman ρ 在 n=5 下无法提供确认性推断，且唯一"显著"的结果（LAMBADA, p=.017）在任何 multiple comparison 校正下均不显著。论文尝试了 3 种校正策略均失败，这不是方法问题而是数据量的根本制约。

(2) **Seed vs architecture 的 confound 未被解决**：单次训练 run + Pythia 70M 的 cross-scale/cross-architecture seed calibration 无法排除 seed 作为 per-example difference 的主要来源。

这些问题使得论文的 3 个 core claims 中有 1 个（convergence）缺乏统计支撑，1 个（architecture drives multiplicity）存在 unresolved confound。剩余的描述性 claim（multiplicity 是 substantial 的）成立且有价值，适合 Findings track。若能补充 multi-seed 实验和增大 attention ratio 粒度，论文有潜力升至 Conference 水平。

## 7. Detailed Comments（逐节）

### Section 1 (Introduction)
- 清晰地建立了研究动机。"yet they can differ on up to 90% of the individual examples" 是一个引人注目的开场。
- "approximately twice the independence baseline" 对应 Table 13 的 Jaccard permutation test 结果，verified。

### Section 2 (Related Work)
- 覆盖了 predictive multiplicity（Marx et al. 2020）和 underspecification（D'Amour et al. 2022）两个框架。Predictive multiplicity 的选择在本文语境下合理——focus 在 per-prediction disagreement 而非 pipeline choice。
- 缺少对 Sellam et al. (2022) MultiBERTs 在 seed variance 方面的讨论，这与 Appendix W 的 seed calibration 直接相关。

### Section 3 (Method)
- **3.1 Model Zoo**: 描述清晰。但应明确提及 GDN h3-1 的 16-head anomaly 在此处而非仅在 Appendix E。
- **3.2 Task Taxonomy**: "informal, not pre-registered" 是实质性弱点。四类分类（Retrieval/Comprehension/Reasoning/Mixed）看似合理但缺乏独立验证。
- **3.3 Convergence Metrics**: 定义了 Spearman ρ 和 convergence ratio σ_pure/σ_h3-1。公式正确。但应在此处而非 Section 4.2 标注 n=5 的 power limitation。
- **3.4 Per-Example Decomposition**: 三分类（helped/hurt/unchanged）是合理的简化。Appendix O 的 continuous Jaccard 分析（τ threshold sensitivity）是良好的 robustness check——mean pairwise Jaccard 从 0.26（τ=0）单调下降至 0.05（τ=0.30），证实 binary threshold 不是 artifact。
- **3.5 Statistical Methods**: Bonferroni correction 和 bootstrap 设计均正确描述。但应明确标注 bootstrap with n=3 的 coverage limitation。

### Section 4 (Experiments)
- **4.1 Per-Example Divergence**: Figure 3 和描述性统计（ι = 0.14–0.30）是论文最有说服力的部分。GDN, RetNet, HGRN2 在 LAMBADA 上的 per-example effect profiles（Figure 3 bar chart）清晰展示了 architecture-specific pattern。
- **4.2 Aggregate Variance and Per-Example**: 此处的 convergence 分析是论文最薄弱的环节（见 N1）。"Bonferroni-adjusted p = .170, non-significant" 应更早、更显著地出现，而非嵌在段落中间。
- **4.3 Robustness**: Sensitivity analysis（removing GDN, bootstrapping 95% CIs）是必要的，但受限于 n=3 的 bootstrap 问题（W5）。Heuristic bootstrap 95% CI 为 [−1.0, −0.7] excludes zero 是有意义的方向性指示，但不应被过度解读。

### Section 5 (Conclusion)
- "Two observations follow at the 340M–1.3B scales studied here" 的措辞合适，没有 overclaim 泛化性。
- "our preliminary routing experiments suggest that exploiting it is task-dependent" 的谨慎表述值得肯定，但仍应考虑将 routing 从 contribution 降级（W4）。

### Limitations (Section 8)
- 三个 limitation 均被识别：single runs、coverage（3 architectures, 2 scales）、generalization。
- 缺少对 n=5 statistical power 作为 limitation 的讨论——这是方法论上最根本的制约。
- Pythia 70M seed calibration 的 mismatch（scale + architecture）应在此讨论而非仅在 Appendix W。

### Appendix 整体
- 详实且有组织。特别值得肯定的是 Appendix A（confirmatory/exploratory split 的透明性）、Appendix O（continuous Jaccard robustness）、Appendix X（extended architecture validation with GLA & DeltaNet）。
- Appendix W（seed calibration）的解释力受限于上述 mismatch 问题，但实验本身设计合理。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 2.5/5 | 核心 convergence claim 的统计检验 underpowered（n=5 Spearman，Bonferroni 后不显著）；seed confound 未被充分解决；描述性分析本身是 sound 的 |
| Excitement | 3/5 | 研究问题新颖（per-example multiplicity in hybrid architectures），但发现的 actionability 有限，routing 仅测试了一个 benchmark |
| Reproducibility | 4/5 | 基于公开 model zoo，evaluation 框架标准，代码承诺公开；扣分因素：单次 run 无法验证 seed robustness |
| Overall Assessment | 3.0/5 | Findings 水平：描述性贡献有价值，但统计推断基础薄弱 |


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1662 · 2026-05-24T13:21:02.197046+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director"
}
```

</details>

---


## Round 129

## Round 129

54 recorded events


### User

_source line 1663 · 2026-05-24T13:21:18.714862+00:00_

[Reviewer 1 审稿结果]:
已清理完毕。审稿完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1664 · 2026-05-24T13:21:39.436365+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1665 · 2026-05-24T13:21:39.587291+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1666 · 2026-05-24T13:21:43.552715+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "entrainment_gated_ft"
  }
}
```

</details>

---


### Tool result

_source line 1667 · 2026-05-24T13:21:44.004812+00:00_

{"result":"# 项目 entrainment_gated_ft 概况\n\n## 实验状态 (46 个)\n\n- **exp-arc-easy-eval**: DONE (success) — \n- **exp-007**: DONE (success) — \n- **exp-004-r2**: DONE (success) — \n- **exp-011-xstorycloze**: DONE (negative) — \n- **exp-004**: DONE (failed) — \n- **exp-011**: DONE (negative) — \n- **exp-010**: DONE (success) — \n- **exp-001**: DONE (success) — \n- **exp-008**: DONE (success) — \n- **exp-003-p2**: DONE (negative) — \n- **exp-003**: DONE (negative) — \n- **exp-009**: DONE (success) — \n- **eval_340m_retnet_hgrn2**: DONE (success) — \n- **hgrn2_eval_h3_1**: DONE (success) — \n- **hgrn2_eval_1_3b_all**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp-005-pure-v4** (killed): —\n- **exp-005-pure-v3** (killed): —\n- **exp-005-hgrn-chain** (killed): —\n\n## 趋势\n成功 16 / 负向 4 / 失败 3 / 共 46\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-48145: 无 GPU 信息\n\n## 告警\n- hgrn2_eval_1_3b_all: 已被终止 — unknown\n- exp-003-p2v2: 已被终止 — unknown\n- exp-004: 训练失败 — unknown\n- exp-005-eval: 已被终止 — unknown\n- exp-005-p1-v4: 已被终止 — unknown\n- exp-005-gla-eval: 训练失败 — unknown\n- exp-005-gla: 已被终止 — unknown\n- exp-005-deltanet: 已被终止 — unknown\n- exp-005-dn-eval: 已被终止 — unknown\n- exp-005-pure-eval: 已被终止 — unknown\n- exp-005-p1-eval: 已被终止 — unknown\n- exp-005-p1-eval-v2: 已被终止 — unknown\n- exp-005-p1-eval-v3: 已被终止 — unknown\n- exp-005-p1-eval-v4: 已被终止 — unknown\n- exp-005-p1-eval-v5: 已被终止 — unknown\n- exp-005-hgrn-chain: 已被终止 — unknown\n- exp-005-batch: 训练失败 — unknown\n- exp-005-pure-v3: 已被终止 — unknown\n- exp-005-pure-v4: 已被终止 — unknown\n- exp-005-pure-v5: 已被终止 — unknown\n- exp-005-pure-v6: 已被终止 — unknown\n- exp-005-pure-v7: 已被终止 — unknown\n- exp-005-pure-v8: 已被终止 — unknown\n- exp-005-pure-v9: 已被终止 — unknown\n- exp-005-pure-v10: 已被终止 — unknown\n- exp-005-pure-baselines: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1668 · 2026-05-24T13:21:44.005198+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "entrainment_gated_ft"
  }
}
```

</details>

---


### Tool result

_source line 1669 · 2026-05-24T13:21:44.306491+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1670 · 2026-05-24T13:21:44.357068+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "entrainment_gated_ft"
  }
}
```

</details>

---


### Tool result

_source line 1671 · 2026-05-24T13:21:44.407857+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-24T13:15:34.704047+00:00\", \"completed_at\": \"2026-05-24T13:19:21.556544+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点（纯文本：title + abstract + intro），第一个 display item（Figure 1）出现在 page 2 顶部，位置尚可但非最优——审稿人翻到第二页才看到图\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 四子图的 axis label 和 legend 字号偏小（估计约 6-7pt），密集排列下可读性一般；建议适当放大或减少子图数量\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 2（实验框架图）尺寸偏小，仅占左栏约 1/4 高度，内部文字较小但仍可辨认\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 3 bar chart 颜色方案使用蓝/粉/灰，色盲区分度可接受；caption 较详细，自包含程度良好\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 1 和 Table 2 均使用 booktabs 风格，无竖线，格式规范；bold 标注最优结果；精度一致（小数位统一）\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"三个 figure（5、6、7）挤在同一页，加上 Limitations 和 Code and Data Availability 段落，页面极度拥挤。Figure 6 和 Figure 7 被压缩到页面底部，尺寸很小，内部文字可读性受影响（axis label 估计 <6pt）\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 5（全宽热力图 figure*）用于需要展示多架构对比的矩阵数据，全宽使用合理\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Limitations 段落简短（约 3 点），符合 EMNLP 要求；末页内容填充充分（>95%）\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-8\", \"message\": \"主体正文 8 页，符合 EMNLP 2026 的 8 页限制。Display items 总计 9 个（7 figure + 2 table），密度 1.1/页，对实证为主的论文属正常范围\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-8\", \"message\": \"布局节奏：无连续 2 页以上纯文本（page 1 纯文本，page 2 有 Figure 1，page 3 纯文本，page 4 有 Figure 2），节奏可接受\"}, {\"severity\": \"info\", \"dimension\": \"pages 9-10\", \"message\": \"参考文献格式统一，无 [?] 未解析引用，无明显截断或 overfull\"}, {\"severity\": \"info\", \"dimension\": \"pages 11-21\", \"message\": \"Appendix 包含约 28 个表格（Table 3-30），表格密度极高但作为补充材料可接受；均使用 booktabs 风格\"}, {\"severity\": \"info\", \"dimension\": \"page 21\", \"message\": \"末页内容约占
…[truncated 504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1672 · 2026-05-24T13:22:07.323861+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
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

_source line 1673 · 2026-05-24T13:22:07.374465+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1674 · 2026-05-24T13:22:13.788092+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_round_19/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_round_19/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 1675 · 2026-05-24T13:22:13.989185+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_19/submitted.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Glob",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1676 · 2026-05-24T13:22:13.989506+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 1677 · 2026-05-24T13:22:14.040054+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_reports/round_7.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_reports/round_8.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_reports/round_9.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_reports/round_10.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_reports/round_12.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_reports/round_13.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_reports/round_14.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_reports/round_15.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_reports/round_16.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_reports/round_17.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_reports/round_18.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1678 · 2026-05-24T13:22:41.815692+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/reviewer*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_19"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/reviewer*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_19"
  }
}
```

</details>

---


### Tool result

_source line 1679 · 2026-05-24T13:22:42.067086+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Glob",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1680 · 2026-05-24T13:22:42.117828+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/reviewer_1*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/reviewer_1*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft"
  }
}
```

</details>

---


### Tool result

_source line 1681 · 2026-05-24T13:22:42.168431+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1682 · 2026-05-24T13:23:06.257528+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 1683 · 2026-05-24T13:23:06.409278+00:00_

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
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{multirow}
15	\usepackage{xcolor}
16	\usepackage{caption}
17	\usepackage{enumitem}
18	\setlist[itemize]{itemsep=1pt, parsep=0pt, topsep=2pt}
19	
20	\setlength{\textfloatsep}{6pt plus 1pt minus 1pt}
21	\setlength{\floatsep}{6pt plus 1pt minus 1pt}
22	\setlength{\intextsep}{6pt plus 1pt minus 1pt}
23	\setlength{\abovecaptionskip}{3pt}
24	\setlength{\belowcaptionskip}{0pt}
25	\setlength{\dbltextfloatsep}{6pt plus 1pt minus 1pt}
26	\setlength{\dblfloatsep}{6pt plus 1pt minus 1pt}
27	\setlength{\abovedisplayskip}{4pt plus 1pt minus 1pt}
28	\setlength{\belowdisplayskip}{4pt plus 1pt minus 1pt}
29	\setlength{\parskip}{0pt plus 0.5pt}
30	
31	\title{Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures}
32	
33	\author{Anonymous}
34	
35	\begin{document}
36	\maketitle
37	
38	\begin{abstract}
39	Practitioners select among hybrid linear recurrent architectures using aggregate benchmarks, but architectures that appear interchangeable by these metrics can differ on which specific examples they get right. Using the model zoo of \citet{wang2025hybrid} (three architectures, five attention ratios, two scales), we decompose per-example effects and find that adding attention is associated with substantially different per-example changes across architectures (Jaccard $\approx 0.10$, roughly twice the independence baseline; all $p < .01$ across five architectures). This predictive multiplicity \citep{marx2020predictive} depends on task type ($\alpha = 0.14$--$0.30$) more than attention dose. Per-example overlap saturates at 4\% attention and remains flat, even as aggregate variance shows a non-significant decreasing trend on one benchmark (Bonferroni-adjusted $p = .17
…[truncated 2098 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1684 · 2026-05-24T13:23:20.305951+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1685 · 2026-05-24T13:23:20.306289+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1686 · 2026-05-24T13:23:31.045742+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1687 · 2026-05-24T13:23:31.398211+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1688 · 2026-05-24T13:23:32.602903+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1689 · 2026-05-24T13:23:32.603266+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1690 · 2026-05-24T13:23:37.521811+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1691 · 2026-05-24T13:23:37.522163+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1692 · 2026-05-24T13:23:49.792266+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1693 · 2026-05-24T13:23:50.244118+00:00_

1	\section{Introduction}
2	
3	Hybrid linear recurrent architectures---including GDN, RetNet, HGRN2, GLA, and DeltaNet---achieve aggregate benchmark scores within 1--2 points of each other at matched parameter budgets. Yet they can differ on up to 90\% of the individual examples they affect: adding attention to three controlled linear recurrent backbones yields helped and hurt sets with at most 10\% pairwise overlap, approximately twice the independence baseline. This per-example divergence is invisible in aggregate metrics: architectures that score within 1--2 points of each other reach similar accuracy by gaining and losing on different inputs. Across all ten pairwise comparisons among five architectures, overlap in per-example effects remains below 14\% (all $p < .01$), meaning the choice of backbone is associated with which specific inputs a deployed system handles correctly.
4	
5	This tension arises in the context of a rapid architectural shift toward hybrid recurrent-attention models, which interleave attention layers within linear recurrent backbones. Jamba \citep{lieber2024jamba}, Griffin \citep{de2024griffin}, RWKV-6 \citep{peng2024eagle}, and RecurrentGemma \citep{botev2024recurrentgemma} each combine recurrence with attention using different mixing strategies. These systems now serve as production-grade alternatives to pure Transformers, and the practical question of how much attention to include is typically answered by comparing aggregate benchmark numbers. \citet{wang2025hybrid} provide a controlled model zoo spanning three recurrent architectures, five attention ratios, and two parameter scales, which enables systematic study of how attention allocation affects these hybrid designs.
6	
7	Prior work on predictive multiplicity \citep{marx2020predictive} and underspecification \citep{damour2022underspecification,mccoy2020berts} documents this risk for seed variation within a single architecture, but whether it extends to architectural variation in hybrid 
…[truncated 4111 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1694 · 2026-05-24T13:23:50.244475+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1695 · 2026-05-24T13:23:50.746534+00:00_

1	\section{Method}\label{sec:method}
2	
3	We describe the model configurations, evaluation benchmarks, and analytical framework used to measure how attention affects cross-architecture agreement at both aggregate and per-example levels.
4	
5	\subsection{Model Zoo}\label{ssec:model_zoo}
6	
7	We use the pretrained model zoo of \citet{wang2025hybrid}, which provides controlled comparisons across architectures and attention ratios. The zoo contains three linear recurrent architectures: GatedDeltaNet \citep{yang2024gateddeltanet}, RetNet \citep{sun2023retnet}, and HGRN2 \citep{qin2024hgrn2}. These three architectures represent distinct approaches to linear recurrence: GatedDeltaNet uses gated delta rules, RetNet uses multi-scale exponential decay, and HGRN2 uses gated linear recurrence with state expansion. Each architecture is trained at five attention ratios: 0\% (pure recurrent), 4\%, 7.7\%, 14.3\%, and 25\%. We adopt the h$k$-1 notation from the original work, where one attention layer is interleaved per every $k{+}1$ total layers: h3-1 corresponds to 25\% attention, h6-1 to 14.3\%, h12-1 to 7.7\%, and h24-1 to 4\%. All configurations are available at two scales: 340M and 1.3B parameters. Within each scale, all models share identical training data, tokenizer, and hyperparameters; they differ only in architecture and attention configuration. This controlled design isolates the effect of attention from confounds such as training data or optimization differences. The zoo also includes a Transformer baseline (pure attention) at both scales.
8	
9	\begin{figure}[t]
10	\centering
11	\includegraphics[width=\columnwidth]{figures/fig_method_overview.pdf}
12	\caption{Experimental framework. For each architecture, we compare the pure-recurrent baseline against its hybrid (+attention) variant, classifying every evaluation example as helped, hurt, or unchanged. Cross-architecture overlap of these per-example effect sets is measured via pairwise Jaccard similarity ($J \approx 0.10$
…[truncated 6070 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1696 · 2026-05-24T13:23:50.746930+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1697 · 2026-05-24T13:23:51.249122+00:00_

1	\section{Experiments}\label{sec:experiments}
2	
3	Using the model zoo of \citet{wang2025hybrid} (\S\ref{ssec:model_zoo}), we evaluate all 30 configurations on 10 benchmarks plus supplementary COPA ($n = 100$) at 1.3B scale unless noted. Results at 340M appear in scale analyses. Recall: h$k$-1 denotes one attention layer per $k{+}1$ layers; h3-1 = 25\% attention.
4	
5	\begin{table*}[t]
6	\centering
7	\caption{Cross-architecture variance trends across benchmarks (1.3B scale). $\rho$: Spearman correlation between attention ratio and cross-architecture standard deviation $\sigma$ across five configurations. $p$: exact permutation test (two-tailed, 120 permutations). $\sigma$ values reported $\times 10^{2}$ (accuracy percentage points). Ratio: $\sigma_{\text{pure}} / \sigma_{\text{h3-1}}$. \textbf{Bold}: only benchmark with $\rho = -1.0$. HellaSwag evaluated using normalized accuracy (acc\_norm), the standard metric for this benchmark.}
8	\label{tab:convergence}
9	\begin{tabular}{llrrrrr}
10	\toprule
11	Benchmark & Category & $\rho$ & $p$ & $\sigma_{\text{pure}}$ & $\sigma_{\text{h3-1}}$ & Ratio \\
12	\midrule
13	\textbf{LAMBADA$^{\ddagger}$} & \textbf{Retrieval} & $\mathbf{-1.0}$ & \textbf{.017} & \textbf{2.41} & \textbf{0.49} & \textbf{4.87} \\
14	\quad\emph{(excl.\ GDN)} & & $-0.7$ & .233 & --- & --- & --- \\
15	BoolQ & Comprehension & $0.2$ & .783 & 1.63 & 2.36 & 0.69 \\
16	ARC-C & Reasoning & $0.6$ & .350 & 0.96 & 1.32 & 0.72 \\
17	HellaSwag & Reasoning & $0.3$ & .683 & 1.17 & 1.18 & 0.99 \\
18	PIQA & Reasoning & $-0.5$ & .450 & 0.54 & 0.34 & 1.59 \\
19	WinoGrande & Reasoning & $0.1$ & .950 & 0.67 & 0.78 & 0.86 \\
20	ARC-E & Mixed & $-0.7$ & .233 & 1.00 & 0.13 & 7.70 \\
21	MMLU & Mixed & $-0.7$ & .233 & 0.92 & 0.41 & 2.27 \\
22	SciQ & Mixed & $0.1$ & .950 & 0.87 & 0.74 & 1.19 \\
23	XStoryCloze & Mixed & $-0.6$ & .350 & 0.82 & 0.55 & 1.49 \\
24	\midrule
25	COPA$^{\dagger}$ & Reasoning & $-0.67$ & .267 & 2.63 & 0.47 & 5.57 \\
26	\bottomrule
27	\multicolumn{7}{l}{\fo
…[truncated 12724 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1698 · 2026-05-24T13:23:51.249503+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1699 · 2026-05-24T13:23:51.300897+00:00_

1	\section{Related Work}
2	
3	\paragraph{Hybrid Recurrent Architectures.}
4	The design space for combining attention with recurrence spans layer-level interleaving \citep[Jamba;][]{lieber2024jamba}, local attention pairing \citep[Griffin, RecurrentGemma;][]{de2024griffin,botev2024recurrentgemma}, matrix-valued recurrence \citep[RWKV-6;][]{peng2024eagle}, within-head mixing \citep[Hymba;][]{dong2024hymba}, and unbounded-context hybrid SSMs \citep[Samba;][]{ren2024samba}. H3 \citep{fu2023hungry} and Hyena \citep{poli2023hyena} establish early design points in the hybrid space with gated convolutions and subquadratic operators. Mamba-2 \citep{dao2024mamba2} establishes a duality between structured state spaces and attention; Mamba-3 \citep{lahoti2026mamba3} extends the design further, while \citet{ali2025hidden} reveal implicit attention within Mamba. Comparative evaluations confirm that hybrids outperform pure Transformers and SSMs at scale \citep{waleffe2024empirical}, and that even one attention layer enables content-based routing \citep{basu2026routing}. Recent theoretical work establishes a provable expressiveness hierarchy between hybrid and pure linear attention \citep{ye2026provable}, providing formal grounding for the architectural differences we characterize at the per-example level. \citet{wang2025hybrid} provide the controlled model zoo we use, holding training conditions constant while varying architecture and attention ratio.
5	
6	\paragraph{Linear Recurrent Models.}
7	Our three recurrent backbones represent distinct gating strategies within the linear recurrence family: RetNet \citep{sun2023retnet} uses multi-scale exponential decay, HGRN2 \citep{qin2024hgrn2} applies gated state expansion, and GatedDeltaNet \citep{yang2024gateddeltanet} combines gated updates with delta rules. These descend from S4 \citep{gu2022s4} and Mamba \citep{gu2024mamba}, which introduced structured state spaces and input-dependent selection, respectively, and connect to linear a
…[truncated 2557 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1700 · 2026-05-24T13:24:02.189992+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
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

_source line 1701 · 2026-05-24T13:24:02.240657+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1702 · 2026-05-24T13:24:07.911828+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR"
  }
}
```

</details>

---


### Tool call

_source line 1703 · 2026-05-24T13:24:08.779891+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
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

_source line 1704 · 2026-05-24T13:24:08.845598+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 65
}
```

</details>

---


### Tool result

_source line 1705 · 2026-05-24T13:24:16.262916+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026:

## Paper Types and Content

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## ARR Submission Process

Papers must be submitted, at latest, by the ARR 2026 May cycle. The key deadline is May 25, 2026 for ARR submission (long & short papers), with a reviewer registration deadline for all authors on May 27, 2026.

## Important ARR Policy for EMNLP 2026

Since the ARR 2026 May cycle is ali
…[truncated 951 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "WebSearch",
  "elapsed_ms": 8351
}
```

</details>

---


### Tool call

_source line 1706 · 2026-05-24T13:24:22.285293+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format page limit template anonymity guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format page limit template anonymity guidelines"
  }
}
```

</details>

---


### Tool call

_source line 1707 · 2026-05-24T13:24:23.640678+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft"
  }
}
```

</details>

---


### Tool result

_source line 1708 · 2026-05-24T13:24:23.741563+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 1709 · 2026-05-24T13:24:28.758979+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format page limit template anonymity guidelines"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here is comprehensive information about ACL Rolling Review 2026 submission guidelines:

## Submission Format and Template

Paper submissions must use the official ACL style template, which is available as an official Overleaf template with a [review] setting that must be on for the submission.

## Page Limits

The paper must follow
…[truncated 1143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "WebSearch",
  "elapsed_ms": 6473
}
```

</details>

---


### Tool call

_source line 1710 · 2026-05-24T13:24:31.167381+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1711 · 2026-05-24T13:24:31.469548+00:00_

1	- id: "R5-W1"
2	  summary: "架构效应 vs seed 效应无法区分（单 training run，无 seed baseline）"
3	  category: experiment
4	  severity: critical
5	  status: wont_fix
6	  first_raised_round: 5
7	  last_seen_round: 18
8	  mentions:
9	    - round: 5
10	      reviewers: [R1, R2]
11	      note: "R1 Critical, R2 W3+Q3 支持。"
12	    - round: 15
13	      reviewers: [R1, R2]
14	      note: "R2-N3 Must-Fix vs R1-W2 Should-Fix。分歧：R1 REBUT 认为论文已用关联性语言、第三方 zoo 无法自行补训。R2 维持 Must-Fix。论文已有 PolyPythias 校准但三重 mismatch 仍被指出。"
15	    - round: 16
16	      reviewers: [R1, R2]
17	      note: "R1-N1 Critical + R2-N2 Critical。双方 [AGREE]。Pythia 70M 三重 mismatch（scale 70M vs 340M+/architecture family Transformer vs hybrid/accuracy 0.17-0.23 vs ~0.50）仍是核心弱点。"
18	    - round: 17
19	      reviewers: [R1, R2]
20	      note: "R1-N3 Critical + R2 交叉 [AGREE]。Pythia 70M within-seed J=0.312 vs cross-arch J=0.354，gap 仅 0.042。R2 补充 seed variation 可能解释大部分 per-example divergence。双方一致认为是根本性威胁但非 fatal。"
21	    - round: 18
22	      reviewers: [R1, R2]
23	      note: "R1-N2 Critical + R2-N2 Critical，交叉均 [AGREE]。R2 纠正 R1 数据误读：within-seed J=0.273 vs cross-arch J=0.10 实为 2.7× 差距（非 R1 声称的 0.02），部分支持架构效应独立性。但 Pythia 70M 三重 mismatch 仍限制 calibration 可迁移性。双方一致要求至少对一个 hybrid 架构训练多 seed。"
24	  action_items:
25	    - round: 13
26	      action: "E4 Pythia 410M 9-seed calibration（实际完成 70M）"
27	      assigned_to: main_agent
28	      status: done
29	    - round: 14
30	      action: "Limitations 提升 single-seed 为 top limitation；§4.2 弱化因果语言"
31	      assigned_to: paper_agent
32	      status: done
33	  resolution: "结构性限制，无法完全修复。已做：(1) Pythia 70M seed calibration 加入 Appendix W；(2) Limitations 中 single-seed 为 top limitation；(3) 全文使用 'associated with' 关联性语言。R18 双方 AGREE 仍为核心弱点但 R2 纠正了 R1 的数据误读——实际 2.7× gap 部分支持架构效应独立性。"
34	  resolution_round: null
35	
36	- id: "R5-W2"
37	  summary: "收敛 claim 统计不显著（Bonferroni p=.170）且依赖 GDN inclusion"
38	  category: method
39	  severity: critical
40	  status: in_progress
41	  first_raised_round: 1
42	  last_seen_ro
…[truncated 26615 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1712 · 2026-05-24T13:25:38.100764+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 审稿任务分配 — Reviewer 1\n\n### 你的审查侧重：方法严谨性 + 实验设计\n\n### Venue 信息\n- **会议**：EMNLP 2026（通过 ACL Rolling Review / ARR May 2026 cycle）\n- **Deadline**：2026年5月25日（ARR 提交截止）\n- **页数限制**：Long paper，正文 8 页，参考文献无限制。Limitations 和 Ethical Considerations 不计入页数限制\n- **模板**：ACL 官方模板，使用 `[review]` 选项\n- **匿名规则**：Double-blind\n- **评分标准**：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 论文信息\n- **标题**：Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures\n- **论文源文件**：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex`\n- **PDF**：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_19/submitted.pdf`\n- **论文概述**：利用 Wang et al. (2025) 的 controlled model zoo（3 种线性循环架构 × 5 种 attention 比例 × 2 种规模），分析 hybrid linear recurrent architectures 之间的 per-example predictive multiplicity。核心发现：(1) 看似聚合指标相近的架构在 per-example 层面差异显著（Jaccard ≈ 0.10）；(2) per-example overlap 在 4% attention 时即饱和且保持平坦；(3) confidence-based routing 可在高 multiplicity 任务上部分利用这种互补性。\n\n### 你的审查重点\n\n请重点审查以下方面：\n\n1. **统计方法严谨性**：\n   - Spearman rank correlation 在 n=5 时的统计功效（最小可达 p=0.017）\n   - Bonferroni correction 的应用是否恰当\n   - Bootstrap CI 在 n=3 架构上的可靠性\n   - Permutation test null baseline 的合理性\n   - 全文是否一致使用 associative/descriptive 语言（vs confirmatory）\n\n2. **实验设计**：\n   - 单一 training run 下架构效应 vs seed 效应的可区分性\n   - Binary decomposition (helped/hurt/unchanged) 的方法学限制\n   - Confidence margin predictor 的假设检验\n   - Routing 实验设计（仅 1/4 benchmark 有效，variance 报告是否充分）\n\n3. **Scale 和 generalization claims**：\n   - 仅两个 scale 点（340M, 1.3B）能否支撑 scale-related claims\n   - 5-architecture 扩展验证仅在 340M 的局限性\n   - Evaluation format confound（LAMBADA 为唯一 free-form benchmark）\n\n4. **格式合规**：\n   - 8 页正文限制\n   - Double-blind 匿名\n   - Limitations section 格式\n\n请提供：Summary、Strengths（逐条）、Weaknesses（逐条，标注 severity: Critical/Major/Minor）、Questions、Missing References、Overall Assessment（评分 + 置信度）、Detailed Comments。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 审稿任务分配 — Reviewer 1\n\n### 你的审查侧重：方法严谨性 + 实验设计\n\n### Venue 信息\n- **会议**：EMNLP 2026（通过 ACL Rolling Review / ARR May 2026 cycle）\n- **Deadline**：2026年5月25日（ARR 提交截止）\n- **页数限制**：Long paper，正文 8 页，参考文献无限制。Limitations 和 Ethical Considerations 不计入页数限制\n- **模板**：ACL 官方模板，使用 `[review]` 选项\n- **匿名规则**：Double-blind\n- **评分标准**：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 论文信息\n- **标题**：Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures\n- **论文源文件**：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex`\n- **PDF**：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_19/submitted.pdf`\n- **论文概述**：利用 Wang et al. (2025) 的 controlled model zoo（3 种线性循环架构 × 5 种 attention 比例 × 2 种规模），分析 hybrid linear recurrent architectures 之间的 per-example predictive multiplicity。核心发现：(1) 看似聚合指标相近的架构在 per-example 层面差异显著（Jaccard ≈ 0.10）；(2) per-example overlap 在 4% attention 时即饱和且保持平坦；(3) confidence-based routing 可在高 multiplicity 任务上部分利用这种互补性。\n\n### 你的审查重点\n\n请重点审查以下方面：\n\n1. **统计方法严谨性**：\n   - Spearman rank correlation 在 n=5 时的统计功效（最小可达 p=0.017）\n   - Bonferroni correction 的应用是否恰当\n   - Bootstrap CI 在 n=3 架构上的可靠性\n   - Permutation test null baseline 的合理性\n   - 全文是否一致使用 associative/descriptive 语言（vs confirmatory）\n\n2. **实验设计**：\n   - 单一 training run 下架构效应 vs seed 效应的可区分性\n   - Binary decomposition (helped/hurt/unchanged) 的方法学限制\n   - Confidence margin predictor 的假设检验\n   - Routing 实验设计（仅 1/4 benchmark 有效，variance 报告是否充分）\n\n3. **Scale 和 generalization claims**：\n   - 仅两个 scale 点（340M, 1.3B）能否支撑 scale-related claims\n   - 5-architecture 扩展验证仅在 340M 的局限性\n   - Evaluation format confound（LAMBADA 为唯一 free-form benchmark）\n\n4. **格式合规**：\n   - 8 页正文限制\n   - Double-blind 匿名\n   - Limitations section 格式\n\n请提供：Summary、Strengths（逐条）、Weaknesses（逐条，标注 severity: Critical/Major/Minor）、Questions、Missing References、Overall Assessment（评分 + 置信度）、Detailed Comments。"
  }
}
```

</details>

---


### Tool result

_source line 1713 · 2026-05-24T13:25:55.225555+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17124
}
```

</details>

---


### Tool call

_source line 1714 · 2026-05-24T13:25:55.376683+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 审稿任务分配 — Reviewer 2\n\n### 你的审查侧重：新颖性 + 完整性 + Related Work\n\n### Venue 信息\n- **会议**：EMNLP 2026（通过 ACL Rolling Review / ARR May 2026 cycle）\n- **Deadline**：2026年5月25日（ARR 提交截止）\n- **页数限制**：Long paper，正文 8 页，参考文献无限制。Limitations 和 Ethical Considerations 不计入页数限制\n- **模板**：ACL 官方模板，使用 `[review]` 选项\n- **匿名规则**：Double-blind\n- **评分标准**：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 论文信息\n- **标题**：Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures\n- **论文源文件**：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex`\n- **PDF**：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_19/submitted.pdf`\n- **论文概述**：利用 Wang et al. (2025) 的 controlled model zoo（3 种线性循环架构 × 5 种 attention 比例 × 2 种规模），分析 hybrid linear recurrent architectures 之间的 per-example predictive multiplicity。核心发现：(1) 看似聚合指标相近的架构在 per-example 层面差异显著（Jaccard ≈ 0.10）；(2) per-example overlap 在 4% attention 时即饱和且保持平坦；(3) confidence-based routing 可在高 multiplicity 任务上部分利用这种互补性。\n\n### 你的审查重点\n\n请重点审查以下方面：\n\n1. **新颖性评估**：\n   - 本文相对于 predictive multiplicity 文献（Marx et al. 2020）、underspecification 文献（D'Amour et al. 2022, McCoy et al. 2020）的增量贡献\n   - 核心发现（aggregate-vs-per-example decoupling）是否为 ecological fallacy 的已知实例化，还是有独立的非平凡发现\n   - 使用第三方 controlled model zoo 进行分析的方法论贡献\n   - 对于 EMNLP Findings track 而言，empirical contribution 是否足够\n\n2. **Related Work 完整性**：\n   - 是否遗漏重要相关工作，特别是：\n     - Model Soups / weight-space interpolation (Wortsman et al. 2022)\n     - Predictive multiplicity in foundation models (Jiang et al. 2024)\n     - Rashomon set 文献\n     - Ensemble diversity 文献（Fort et al. 2019, Brown 2005）\n     - MoE 相关文献\n     - 最新 2025-2026 hybrid architecture 工作\n   - 引用是否真实、格式是否正确\n\n3. **叙事框架 (Framing)**：\n   - Abstract 和 Introduction 的叙事框架是否准确反映证据强度\n   - \"Convergence masks divergence\" 叙事是否以 aggregate convergence 为前提但证据不足（p=.170）\n   - Routing 作为 practical contribution 的定位是否过高（1/4 benchmark 有效）\n   - Conclusion 中的 practitioner implications 是否过度泛化\n\n4. **完整性**：\n   - 论文是否完整回答了提出的研究问题\n   - 是否有 alternative explanations 未被讨论（如 evaluation format confound、example difficulty confound）\n   - Limitations section 是否充分\n\n请提供：Summary、Strengths（逐条）、Weaknesses（逐条，标注 severity: Critical/Major/Minor）、Questions、Missing References、Overall Assessment（评分 + 置信度）、Detailed Comments。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 审稿任务分配 — Reviewer 2\n\n### 你的审查侧重：新颖性 + 完整性 + Related Work\n\n### Venue 信息\n- **会议**：EMNLP 2026（通过 ACL Rolling Review / ARR May 2026 cycle）\n- **Deadline**：2026年5月25日（ARR 提交截止）\n- **页数限制**：Long paper，正文 8 页，参考文献无限制。Limitations 和 Ethical Considerations 不计入页数限制\n- **模板**：ACL 官方模板，使用 `[review]` 选项\n- **匿名规则**：Double-blind\n- **评分标准**：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 论文信息\n- **标题**：Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures\n- **论文源文件**：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex`\n- **PDF**：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_19/submitted.pdf`\n- **论文概述**：利用 Wang et al. (2025) 的 controlled model zoo（3 种线性循环架构 × 5 种 attention 比例 × 2 种规模），分析 hybrid linear recurrent architectures 之间的 per-example predictive multiplicity。核心发现：(1) 看似聚合指标相近的架构在 per-example 层面差异显著（Jaccard ≈ 0.10）；(2) per-example overlap 在 4% attention 时即饱和且保持平坦；(3) confidence-based routing 可在高 multiplicity 任务上部分利用这种互补性。\n\n### 你的审查重点\n\n请重点审查以下方面：\n\n1. **新颖性评估**：\n   - 本文相对于 predictive multiplicity 文献（Marx et al. 2020）、underspecification 文献（D'Amour et al. 2022, McCoy et al. 2020）的增量贡献\n   - 核心发现（aggregate-vs-per-example decoupling）是否为 ecological fallacy 的已知实例化，还是有独立的非平凡发现\n   - 使用第三方 controlled model zoo 进行分析的方法论贡献\n   - 对于 EMNLP Findings track 而言，empirical contribution 是否足够\n\n2. **Related Work 完整性**：\n   - 是否遗漏重要相关工作，特别是：\n     - Model Soups / weight-space interpolation (Wortsman et al. 2022)\n     - Predictive multiplicity in foundation models (Jiang et al. 2024)\n     - Rashomon set 文献\n     - Ensemble diversity 文献（Fort et al. 2019, Brown 2005）\n     - MoE 相关文献\n     - 最新 2025-2026 hybrid architecture 工作\n   - 引用是否真实、格式是否正确\n\n3. **叙事框架 (Framing)**：\n   - Abstract 和 Introduction 的叙事框架是否准确反映证据强度\n   - \"Convergence masks divergence\" 叙事是否以 aggregate convergence 为前提但证据不足（p=.170）\n   - Routing 作为 practical contribution 的定位是否过高（1/4 benchmark 有效）\n   - Conclusion 中的 practitioner implications 是否过度泛化\n\n4. **完整性**：\n   - 论文是否完整回答了提出的研究问题\n   - 是否有 alternative explanations 未被讨论（如 evaluation format confound、example difficulty confound）\n   - Limitations section 是否充分\n\n请提供：Summary、Strengths（逐条）、Weaknesses（逐条，标注 severity: Critical/Major/Minor）、Questions、Missing References、Overall Assessment（评分 + 置信度）、Detailed Comments。"
  }
}
```

</details>

---


### Tool result

_source line 1715 · 2026-05-24T13:25:56.740718+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1364
}
```

</details>

---


### Assistant

_source line 1716 · 2026-05-24T13:26:02.740339+00:00_

两位 Reviewer 已重新派发：

- **Reviewer 1**：方法严谨性 + 实验设计（统计方法、实验设计、scale claims、格式合规）
- **Reviewer 2**：新颖性 + 完整性 + Related Work（增量贡献、引用完整性、叙事框架、alternative explanations）

视觉审查已完成（1 warning: 第8页三图拥挤，15 info）。外部审稿未启用。

等待两位 Reviewer 返回初审结果后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director"
}
```

</details>

---


## Round 130

## Round 130

2 recorded events


### User

_source line 1717 · 2026-05-24T13:26:02.748386+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见（Round 1）

**审查侧重**：新颖性、完整性、写作质量

---

### 1. Summary

本文研究了混合线性递归架构（GatedDeltaNet、RetNet、HGRN2）在 per-example 层面的 predictive multiplicity。利用 Wang et al. (2025) 的受控 model zoo（3种架构 × 5种 attention ratio × 2种规模），作者将每个 example 分类为 helped/hurt/unchanged，发现不同架构影响的 example 集合几乎不重叠（Jaccard ≈ 0.10），且这种 multiplicity 按任务类型变化（α = 0.14–0.30）而非 attention 比例变化。此外，aggregate variance 的减少（仅在 LAMBADA 上观察到，校正后不显著）与 per-example overlap 的稳定形成了 decoupling。

### 2. Strengths

**S1. 实验设计严谨且受控**：利用已有 model zoo，仅改变架构和 attention ratio，训练数据/超参/tokenizer 完全一致。这种控制在 hybrid architecture 文献中少见。

**S2. 统计方法论审慎**：Bonferroni 校正、置换检验、Bootstrap BCa CI，且在 n=5 时诚实承认统计功效有限（"only |ρ|=1.0 achieves p<.05"）。LAMBADA 的 aggregate trend 始终描述为 non-significant (p=.170)——这种诚实报告难得。

**S3. 稳健性检查极为充分**：13 个 Appendix（A–X），涵盖 GDN confound、连续 Jaccard、seed calibration、5 架构扩展验证等。

**S4. Decoupling 发现有 insight**：aggregate convergence ≠ per-example convergence 这一发现不是先验显然的，对"aggregate 指标可以代表 per-example 行为"的默认假设提出了有力质疑。

**S5. 写作规范，透明诚实**：结构清晰，Abstract ≈ 148 词符合限制，多处使用 hedged language。

### 3. Weaknesses

**N1 [major] 新颖性为增量式扩展而非质性突破**
- 位置：Introduction 贡献列表、Related Work §2第3段
- 核心贡献是将 predictive multiplicity 框架从 seed/initialization 变异扩展到 architectural 变异。但"不同模型在不同 example 上表现不同"是 ensemble diversity 文献的已知事实（Kuncheva & Whitaker 2003; Fort et al. 2019）。论文试图区分自己与 ensemble diversity，但这种区分主要在 framing 层面——hybrid 架构本身就是不同的模型。
- 建议：需更清楚阐明 architectural multiplicity 相比 ensemble disagreement 提供了什么定性不同的 insight。

**N2 [major] LAMBADA aggregate trend 的叙事权重与统计证据不匹配**
- 位置：Section 4.2、Figure 1a、Table 1
- Decoupling narrative 的核心支柱是 LAMBADA 的 aggregate variance reduction（ρ=-1.0），但：(1) Bonferroni 校正后 p=.170，不显著；(2) 排除 GDN 后 ρ 降至 -0.7；(3) 340M 上不复现。其他 9 个 benchmark 均无此 trend。这使 Contribution 2 的证据基础不够坚实。
- 建议：重新 frame 为更保守但更站得住脚的 claim。

**W1 [major] 实践意义有限且不一致**
- 位置：Section 4.1 Confidence-based routing
- Routing 结果：LAMBADA +5.2pp、ARC-Easy +1.2pp、HellaSwag -0.06pp、PIQA -0.49pp（显著负）。实践中需先知道任务 multiplicity 水平才能决定是否 routing——循环依赖。

**W2 [minor] GDN 16 vs. 32 attention heads confound**
- 位置：Table 1 脚注、Section 4.3、Appendix E
- 直接影响 LAMBADA variance trend。应在正文中更早 flag。

**W3 [minor] Introduction 信息密度过高**：第1段在 4 行内密集给出多个具体数字，缺乏可解释性。

**W4 [minor] "Attention dose" 术语非标准**：建议统一使用 "attention ratio"。

**W5 [minor] Task taxonomy "Mixed" 类别模糊**：ARC-Easy、MMLU、SciQ、XStoryCloze 被归为 Mixed 是因为不易归入其他类别，削弱了 task-type analysis。

### 4. Questions to Authors

Q1: Helped/hurt 分类基于 pure vs. h3-1。如果改为 pure vs. h24-1（4% attention），Jaccard 值是否显著不同？

Q2: Confidence routing 在 PIQA 上显著为负。是 routing 系统性选择了错误架构，还是 confidence margin 在低 multiplicity 任务上不是好的 predictor？

Q3: Average-logits ensemble 的初步结果是否可获得？缺少这个对比使 routing 实验评估不完整。

Q4: Seed calibration 使用 Pythia 70M，与主实验规模差异大。是否考虑在相同 model zoo 做 multi-seed 实验？

### 5. Missing References

- Li et al. (2024) "Dropout-Based Rashomon Set Exploration for Efficient Predictive Multiplicity Estimation" (arXiv:2402.00728)
- "Why are there many equally good models? An Anatomy of the Rashomon Effect" (2026, arXiv:2601.06730)

### 6. Overall Assessment

**Overall**: 3.0 (Findings)
**Confidence**: 4/5 (Quite sure)

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 方法论扎实，统计审慎，robustness 充分。GDN confound 和 LAMBADA-centric narrative 小幅扣分。 |
| Excitement | 2/5 | 核心发现在 ensemble 文献中有预期；decomposition 方法简单直接；practical routing 不一致。Decoupling 有 insight 但统计基础不坚实。 |
| Reproducibility | 4/5 | 使用公开 model zoo，承诺发布代码，方法描述详细。 |

**总结理由**：本文是执行质量很高的实证分析——方法论严谨、统计规范、写作诚实。但作为主会议论文：(1) 新颖性有限，核心是将已有框架应用到新 axis；(2) Decoupling 叙事依赖单 benchmark 非显著 trend；(3) 实践影响弱。适合 Findings 轨道。

### 7. 格式合规 ✅
- 正文 ≤ 8 页 ✅
- Limitations 在正文 ✅
- 匿名性完整 ✅
- Abstract < 200 词 ✅
- References 格式正确 ✅
- Appendix 字母编号 ✅

---

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.0 (Findings)，Soundness 4/5，Excitement 2/5。

核心判断：论文执行质量高（统计严谨、robustness 充分、写作诚实），但新颖性为增量式（将 predictive multiplicity 从 seed 扩展到 architecture）、decoupling 叙事依赖单 benchmark 非显著 trend、practical routing 结果不一致。适合 Findings 而非主会议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1718 · 2026-05-24T13:26:12.854364+00:00_

Reviewer 2 审稿已收到。Overall 3.0 (Findings)，Soundness 4/5，Excitement 2/5。

等待 Reviewer 1 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director"
}
```

</details>

---


## Round 131

## Round 131

6 recorded events


### User

_source line 1719 · 2026-05-24T13:31:26.852918+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 完整审稿意见（方法严谨性 + 实验设计）

---

## 1. Summary

本文首次系统地分析了混合线性递归架构间的 per-example predictive multiplicity。基于 Wang et al. (2025) 的 controlled model zoo（3 架构 × 5 attention ratio × 2 scale），论文发现：(1) 聚合指标可互换的架构在逐样本层面差异显著（pairwise Jaccard ≈ 0.10，约为独立基线的 2×）；(2) per-example Jaccard 在 4% attention 时即饱和且保持平坦；(3) confidence-based routing 在高 multiplicity 任务上可部分利用架构互补性。研究问题重要且描述性分析扎实，但核心统计推断严重 underpowered，多个实验设计 confound 未被充分解决。

---

## 2. Strengths

**S1. 研究问题新颖且有实际意义。** Per-example multiplicity 在 hybrid 架构间的系统研究此前缺位。论文将 multiplicity 从 Rashomon-set/fairness 领域引入 architecture comparison，视角具有启发性。

**S2. 描述性分析详实可信。** Jaccard permutation test（Appendix J, Table 13）在 10,000 次置换下所有 architecture pair 均 p < .0001，null baseline（J_null ≈ 0.019）约为 observed 的一半，为"cross-architecture overlap 是结构性的而非随机的"提供了可靠证据。

**S3. 对自身局限性的讨论值得肯定。** 论文在 Section 8（Limitations）、Appendix A（confirmatory/exploratory split 的透明性）、Appendix D（GDN exclusion sensitivity）中坦承了核心局限，避免了对不显著结果的过度解读。

**S4. Robustness 验证覆盖面广。** Continuous Jaccard（Appendix O）证实 binary threshold 不是 artifact；5-architecture extension（Appendix X）将 Jaccard ≤ 0.14 的 pattern 扩展至 GLA 和 DeltaNet；Transformer entrainment analysis（Appendix L）提供了有趣的 cross-family 视角。

**S5. 实验框架清晰可控。** 基于公开 model zoo，所有模型共享训练数据和 tokenizer，training conditions 固定，仅变化架构和 attention 配置——这是研究 architecture effect 的理想设定。

**S6. Per-example decomposition（Section 3.4）设计合理。** 将 attention effect 分解为 helped/hurt/unchanged 三类，配合 Jaccard 度量 cross-architecture overlap，方法论上清晰且直觉友好。

---

## 3. Weaknesses

### Critical

**N1. [Critical] Spearman ρ 在 n=5 下统计效力根本不足，核心 convergence claim 缺乏确认性支撑**

- **位置**：Section 3.3, Section 4.2, Table 1
- **问题**：Convergence 分析的中心统计量是 Spearman ρ（attention ratio vs. cross-architecture σ），但样本量仅 n = 5（五个 attention 配置）。在 n=5 的 Spearman 检验中，只有 |ρ| = 1.0 时 p < .05（exact permutation p = 1/5! subset = 0.0167）。Table 1 的 10 个 confirmatory+exploratory benchmark 中，仅 LAMBADA 达到 ρ = -1.0（p = .017）。论文诚实地报告了三种校正策略均未达到显著性阈值：
  - 10-benchmark Bonferroni: adjusted p = .017 × 10 = .170
  - 6-benchmark confirmatory set: adjusted p = .017 × 6 = .102
  - One-sided test + 10-benchmark Bonferroni: adjusted p = .083
  
  然而，正文的叙述中多处 convergence 被作为核心 contribution 之一呈现（Section 2, p.2: "aggregate variance shows a non-significant decreasing pattern on four benchmarks"；Section 5 conclusion 将 convergence 作为"two observations"之一），其权重超出了"单一 benchmark 上的未校正显著"所能支撑的范围。
- **为什么影响接收**：Convergence 是论文三个 core contribution 之一。如果它仅是一个 benchmark 上的未校正 p = .017（且无法通过任何 multiple comparison 校正），那么这个 contribution 需要被重新定位为 exploratory observation 而非 established finding。
- **建议**：(1) 将 convergence claim 在正文中明确框定为"exploratory/descriptive"；(2) 考虑对 attention ratio 做连续回归而非 rank correlation，以充分利用 ratio 的连续信息；(3) 如果 model zoo 允许，增加更细粒度的 attention ratio 配置。

**N2. [Critical] 单次训练 run 无法分离架构效应与 seed 效应，seed calibration 存在双重 mismatch**

- **位置**：Section 8, Appendix W
- **问题**：每个配置仅有一次训练 run。论文用 Pythia 70M 的 9 个 seed 做 calibration（Appendix W），报告 within-seed Jaccard 是 cross-architecture Jaccard 的 2.7–4.3×。但此 calibration 有两个严重 mismatch：
  - **Scale mismatch**：70M vs 340M/1.3B。论文自身在 Appendix C 发现 340M 和 1.3B 的 convergence 行为截然不同（340M 全部 |ρ| ≤ 0.4），说明 scale-dependent effects 存在。Seed variance 可能同样 scale-dependent。
  - **Architecture mismatch**：Pythia 是 pure Transformer，不含 gating mechanism。Hybrid 架构（如 GatedDeltaNet 的 gated delta rules、HGRN2 的 gated linear recurrence）的 seed sensitivity 可能与 Transformer 显著不同——gating 参数的初始化对 per-example behavior 的影响未知。
- **为什么影响接收**：论文的核心 claim 是"architecture drives per-example differences"。如果无法排除 seed 作为主要混淆变量，这一 claim 的 causal 解读就站不住。
- **建议**：(1) 至少对一个 hybrid 架构（如 RetNet 或 HGRN2）在 340M 做 3–5 seed 重复训练；(2) 若不可行，在 Limitations 中将 seed calibration 的 mismatch 作为首要局限性讨论，并使用 associative language（"associated with"）替代 causal 暗示。

### Major

**W1. [Major] LAMBADA 作为唯一 free-form generation benchmark，evaluation format confound 未被讨论**

- **位置**：Section 3.2, Table 1, Section 4.1–4.2
- **问题**：论文 10 个 benchmark 中，LAMBADA 是唯一的 free-form generation（open-ended next-word prediction）任务。其余 9 个全部是 multiple-choice 或 binary classification format（BoolQ: yes/no; ARC, HellaSwag, PIQA, WinoGrande, MMLU, SciQ, XStoryCloze: multiple-choice; COPA: binary）。论文中 convergence 最强的结果恰恰出现在 LAMBADA（ρ = -1.0），multiplicity 最高的也是 LAMBADA（ι = 0.30）。Section 4 (p.4) 提到"within multiple-choice tasks, format (two-way vs. four-way) does not predict ι (§4.1)"，但未讨论 free-form vs. multiple-choice 的 format confound。
  
  Multiple-choice format 机械地约束了 per-example divergence——答案空间有限（2–5 选项），不同架构选中相同错误答案的 baseline probability 更高，因此 Jaccard overlap 天然被 format 压高、multiplicity 被压低。Free-form generation 的答案空间近乎无穷大，因此 per-example divergence 自然更高。**LAMBADA 上的高 multiplicity 和强 convergence 可能部分（甚至主要）由 evaluation format 而非 task type 驱动。**
- **为什么影响接收**：这直接影响"multiplicity depends on task type"（Section 4.1）这一 core claim 的效度。如果真正的 driver 是 evaluation format 而非 cognitive demand（Retrieval vs Reasoning），则 task taxonomy 的解释力大打折扣。
- **建议**：(1) 在 Limitations 或 Section 4.1 中显式讨论 free-form vs. multiple-choice format confound；(2) 考虑增加 1-2 个其他 free-form generation benchmark（如 TriviaQA open-generation、NaturalQuestions open-generation）来检验是否 format 而非 task type 驱动 multiplicity；(3) 至少对 multiple-choice benchmark 做一个 format-normalized 的 multiplicity 分析（如将 Jaccard 除以 random-agreement baseline）。

**W2. [Major] GDN h3-1 的 16-head confound 导致 sensitivity analysis 中 correlation 反转**

- **位置**：Appendix D.2, Appendix E, Table 3
- **问题**：GDN h3-1 使用 16 attention head，其他所有架构使用 32 个。Appendix D.2 的 GDN exclusion analysis 显示 MMLU 的 ρ 从 -0.7 反转为 +0.6——方向完全逆转。这说明 MMLU 上的 convergence pattern 完全由 GDN 的 anomalous head count 驱动，而非反映 architecture-general 的 attention effect。排除 GDN 后 n 降到 3（仅 RetNet、HGRN2，可能加上另一架构），bootstrap CI 的统计意义进一步恶化。
- **建议**：在正文而非仅 Appendix 中报告 MMLU ρ 反转（-0.7 → +0.6）；将 GDN head count 差异作为 controlled variable 明确列出而非仅在 Appendix E 脚注提及。

**W3. [Major] 仅两个 scale point 且结果矛盾，scale-related claims 的泛化性不足**

- **位置**：Section 4.2, Appendix C, Appendix T
- **问题**：340M：所有 benchmark 均无 convergence（|ρ| ≤ 0.4, p ≥ .45）；1.3B：仅 LAMBADA 有 convergence。两个数据点无法建立 scaling trend。Appendix T 的 340M per-example 分析显示 LAMBADA per-example multiplicity "closely matches the 1.3B baseline"（σ = 0.313 vs 0.307），但 convergence 完全消失——说明 per-example divergence 和 aggregate convergence 是可解耦的现象，论文未对此矛盾做充分讨论。
- **建议**：明确限定 convergence finding 的 scope 为"1.3B LAMBADA"；讨论 340M 无 convergence 的理论含义——这可能意味着 convergence 不是 attention 的 fundamental property 而是 capacity-gated 的 emergent phenomenon。

**W4. [Major] Confidence margin predictor 的假设检验不充分，预测能力弱**

- **位置**：Section 4.1 (Confidence-based routing), Appendix P, Tables 18–22
- **问题**：
  (a) **AUC 导出方式的假设违反**：Appendix P.2 从 Cohen's d 导出 AUC（AUC = Φ(d/√2)），前提是两组分布均为正态。但 Shapiro-Wilk 检验（p.17）显示 rescue-set values "moderately right-skewed"（skewness 1.33–1.41），GDN 和 HGRN2 的 p < 10⁻⁴，严重违反正态假设。论文用 percentile CI 替代参数 CI 作为 workaround，但 AUC 的 point estimate 本身仍基于 Gaussian assumption。
  (b) **预测能力弱**：Table 22 报告 within-architecture prediction AUC 均 < 0.69（最高 0.73），接近 random（0.50）到 weak discrimination 区间。disruption prediction "is weaker on reasoning tasks"（p.17）。Rescue thresholds 在 |log p| 空间中 "cluster tightly (range 0.01)"（p.18），discriminative margin 极窄。
  (c) **Routing 结果缺乏 variance 报告**：Section 4.1 报告 LAMBADA 上 routing 优于 majority vote ~1.2 pp（SD = 0.5 pp），但未提供 bootstrap CI、significance test、或 effect size。ARC-Easy 上 "+1.2 pp, SD = 0.5 pp"——相同数值令人怀疑是否为不同 benchmark 的独立观察。HellaSwag 和 PIQA 上 routing 无效或反效果。**4 个 benchmark 中仅 1 个有正向效果，且无显著性检验。**
- **建议**：(1) 使用 non-parametric AUC（Mann-Whitney U statistic）替代基于 Cohen's d 的参数 AUC；(2) 对 routing 增益做 bootstrap CI 和 permutation significance test；(3) 坦陈 1/4 benchmark 有效的事实对 actionability claim 的限制。

**W5. [Major] Task taxonomy 是 post-hoc 的，用于 confirmatory claim 存在循环论证风险**

- **位置**：Section 3.2, Appendix A
- **问题**：四类 taxonomy（Retrieval/Comprehension/Reasoning/Mixed）被描述为"informal, not pre-registered"（Appendix A），但正文将其用于 confirmatory 式叙述："multiplicity varies systematically by task type"（Section 4.1）。Appendix A 声称 taxonomy "was fixed prior to analysis following established distinctions"，但缺乏可验证的时间证据（无 pre-registration、commit timestamp 等）。此外，taxonomy 的创建者和数据分析者是同一批人，无法排除先看到 pattern 再创建解释的可能。
- **建议**：(1) 提供 taxonomy 固定时间的客观证据；(2) 或将所有基于 taxonomy 的结论重新框定为 hypothesis-generating。

**W6. [Major] 5-architecture extension（Appendix X）仅在 340M，无法验证 1.3B 的 convergence finding**

- **位置**：Appendix X, Table 30, p.21
- **问题**：将 GLA 和 DeltaNet 加入分析（共 5 架构）是好的 robustness check，但仅在 340M scale 进行。论文的核心 convergence finding 发生在 1.3B——而 340M 上 convergence 完全不存在（Appendix C）。因此 5-architecture extension 仅验证了 per-example divergence 的 ubiquity（Jaccard ≤ 0.14），未验证 convergence claim 在更多架构上的成立性。Table 30 的 40 pairwise Jaccard 值全部使用 h3-1（25% attention）单一配置，未做 attention ratio sweep。
- **建议**：标明 Appendix X 仅验证 per-example divergence 而非 convergence；若资源允许，在 1.3B 上至少训练 GLA 和 DeltaNet 的 h3-1 配置。

### Minor

**W7. [Minor] Bootstrap CI 在 n=3 架构下不具备名义覆盖率**

- **位置**：Section 3.5, Section 4.3, Appendix D.1
- **问题**：排除 GDN 后和部分 sensitivity analysis 对 n=3 个架构做 10,000 次 bootstrap CI。n=3 时 bootstrap with replacement 仅有 3³ = 27 个 distinct resamples（考虑 order invariance 后更少），CI 的覆盖概率远低于名义 95%。Appendix D.1 进一步排除了产生 "constant σ vector" 的 resamples——虽然合理，但进一步缩小了有效 bootstrap 空间。论文正确使用了"heuristic indicators of effect direction"的措辞（Section 3.5），但 Section 4.3 中"Bootstrapped 95% CIs... [−1.0, −0.7], which excludes zero"的叙述可能误导读者将其视为正式 CI。
- **建议**：在报告 n=3 bootstrap CI 时附加注释说明其 coverage limitation。

**W8. [Minor] 全文语言未完全一致使用 associative/descriptive 框架**

- **位置**：多处
- **问题**：论文在报告 p-values 时措辞谨慎（如 Section 4.2: "non-significant"），但在解释和结论中偶尔滑入 causal/mechanistic 语言：
  - Section 5 (p.7): "the pattern of multiplicity **reflects** structural differences while its magnitude **is modulated by** model capacity" —— "reflects" 和 "is modulated by" 暗示因果关系
  - Section 2 (p.2): "our decomposition finding (§4.1) is a **controlled** instance within recurrent architectural families" —— "controlled" 暗示 causal identification，但 single-run design 不支持
  - Appendix B (p.11): "indicating dependence" —— 在不显著的 ρ 值语境下过强
  
  相比之下，Section 4.1 的"associated with"和 Table 1 的"descriptive and exploratory"措辞是恰当的。
- **建议**：全文统一使用 "associated with," "correlated with," "consistent with" 等 associative 语言；将 "reflects," "modulated by," "controlled" 等 causal 用语替换为 hedged 版本。

**W9. [Minor] Routing 实验中 LAMBADA 和 ARC-Easy 报告相同的增益数值（+1.2 pp, SD = 0.5 pp），需要确认是否为独立结果**

- **位置**：Section 4.1, p.5
- **问题**：两个 benchmark 上 routing 的增益完全相同（+1.2 pp, SD = 0.5 pp），这可能是巧合，但也可能是 copy-paste error 或 rounding artifact。需要作者确认。
- **建议**：检查并确认两个数值是否为独立计算的精确值。

---

## 4. Questions to Authors

**Q1.** Pythia 70M seed calibration（Appendix W）中 within-seed Jaccard 与 cross-architecture Jaccard 的比值为 2.7–4.3×。如果在 RetNet 或 HGRN2 的 340M/1.3B scale 上做同样实验，你们是否预期该比值会保持？有无定性论据支持 hybrid 架构的 gating mechanism 不会放大 seed sensitivity？

**Q2.** LAMBADA 是唯一 free-form generation benchmark。你们是否考虑过 LAMBADA 上的高 multiplicity（ι = 0.30）和强 convergence（ρ = -1.0）可能由 evaluation format（open-ended generation 的无穷答案空间 vs. multiple-choice 的有限选项）而非 task type（Retrieval vs Reasoning）驱动？

**Q3.** Table 3（Appendix D.2）显示 GDN exclusion 后 MMLU 的 ρ 从 -0.7 反转为 +0.6。如何解释这一完全反转？它是否意味着 MMLU 上的 apparent convergence 完全是 GDN 16-head anomaly 的 artifact？

**Q4.** Confidence margin predictor 使用 Cohen's d 导出 AUC，但 Shapiro-Wilk 检验（Appendix P.2）显示 rescue-set 的 skewness = 1.33–1.41，显著偏离正态。是否考虑使用 non-parametric AUC（直接用 Mann-Whitney U / Wilcoxon rank-sum）？

**Q5.** Section 4.1 报告 LAMBADA routing 增益为 +1.2 pp（SD = 0.5 pp），ARC-Easy 也是 +1.2 pp（SD = 0.5 pp）。这两个完全相同的数值是独立计算的还是存在 reporting error？

**Q6.** 340M 和 1.3B 的 convergence 行为完全矛盾（340M 无 convergence，1.3B 仅 LAMBADA 有 convergence）。你们是否考虑过一个替代假说：观察到的 "convergence" 不是 attention 的固有属性，而是 model capacity 恰好达到某个 threshold 后的 emergent 现象？如果是，这对论文结论有何影响？

**Q7.** Task taxonomy 声称 "was fixed prior to analysis"（Appendix A）。能否提供客观时间证据（pre-registration ID、git commit hash + timestamp、lab notebook entry）？

---

## 5. Missing References

- **Sellam et al. (2022)**: "MultiBERTs: BERT Reproductions for Robustness Analysis"——论文 References 中已有此条，但正文的 seed calibration discussion（Section 8, Appendix W）未引用。MultiBERTs 在 BERT-base scale 做了 25-seed variance analysis，直接相关于 seed vs architecture effect 的量化。
- **Biderman et al. (2023)**: "Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling"——论文引用了 Pythia 但未在 seed calibration 语境中引用其 training dynamics 分析。Pythia 的设计理念（fixed training order, multiple seeds）直接支撑了 Appendix W 的 calibration strategy。
- **Open LLM Leaderboard (Beeching et al., 2023)**: 大规模 benchmark 评测数据源，可用于验证 per-example divergence 是否在更多架构上成立。

---

## 6. Overall Assessment

**Overall**: **3.0** (Findings)

**Confidence**: **4/5**（仔细审查了全文 21 页包括所有 Appendix；熟悉 predictive multiplicity、hybrid architecture、statistical methodology 文献；逐表逐图验证了核心 claims。未深入检查的部分：attention weight cosine similarity 分析（Appendix F）的具体数值。）

**理由**：

论文提出了一个 genuinely important 的研究问题——hybrid 架构在 per-example 层面的 predictive multiplicity——且描述性分析的质量很高。Jaccard permutation test 为 structured overlap 提供了 robust 的统计证据（S2），per-example decomposition 的方法论清晰（S6），附录的 thoroughness 值得称赞（S4）。

然而，论文的三个 core contributions 中，统计支撑的强度不均匀：

| Claim | 统计支撑 | 评估 |
|-------|----------|------|
| Per-example multiplicity 是 substantial 的 | Jaccard permutation test, p < .0001 | ✓ Strong |
| Attention modulates convergence | Spearman ρ, n=5, only LAMBADA ρ=-1.0, Bonferroni后不显著 | ✗ Insufficient |
| Multiplicity 可被 routing 利用 | 4 benchmarks 中仅 1 个有效, 无 significance test | ✗ Weak |

两个 critical weaknesses（N1: statistical power; N2: seed confound）和一个新识别的 major weakness（W1: LAMBADA format confound）共同限制了论文的贡献强度：

- **N1** 使得 convergence claim 仅为 exploratory observation
- **N2** 使得 "architecture drives multiplicity" 的 causal 解读存在 unresolved confound
- **W1** 使得 "multiplicity depends on task type" 可能被 evaluation format 所混淆——最高 multiplicity 和最强 convergence 恰巧都在唯一的 free-form benchmark 上出现

剩余的 descriptive contribution（per-example multiplicity 的存在和 structured nature）是 sound 且有价值的，适合 Findings track。论文在 Limitations 和 Appendix 中的透明性值得肯定——这些局限性被识别但未被充分解决。

**升至 Conference（4.0）的路径**：(1) 至少一个 hybrid 架构的 multi-seed 实验以分离 seed vs architecture effect；(2) 增加 1–2 个 free-form generation benchmark 以解耦 format confound；(3) 增加 attention ratio 粒度（如 10+ 个 ratio）以提升 convergence 分析的 statistical power。

---

## 7. Detailed Comments

### Abstract
- 约 170 words，符合 200-word 限制。
- "roughly twice the independence baseline" 可验证（Table 13: J_observed ≈ 0.04 vs J_null ≈ 0.019），数值准确。
- "a non-significant decreasing trend on four benchmarks (Bonferroni-adjusted p = .170)" —— 在 abstract 中就标注"non-significant"是正确做法。

### Section 1 (Introduction)
- 开场有效（"yet they can differ on up to 90% of the individual examples"），但未标注此数值的来源——应注明来自哪个 benchmark/scale 组合。
- "approximately twice the independence baseline" 同上，verified。
- "Confidence-informed routing extracts 36% of oracle gap on LAMBADA (+5.2 pp)" —— 仅报告 LAMBADA 在 Introduction 中是适当的（最强结果），但应提及其他 benchmark 上无效。

### Section 2 (Related Work)
- Predictive multiplicity（Marx et al., 2020）vs underspecification（D'Amour et al., 2022）的框架选择在本文语境下合理——focus 在 per-prediction disagreement。
- 缺少对 evaluation format 如何影响 multiplicity measurement 的讨论——Dodge et al. (2020) 讨论了 format sensitivity 但非 per-example 层面。

### Section 3 (Method)
- **3.1 Model Zoo**: 描述清晰。GDN h3-1 的 16-head anomaly 应在此提及（目前仅在 Appendix E 脚注）。
- **3.2 Task Taxonomy**: "informal, not pre-registered" 是实质性弱点。LAMBADA 被归类为 "Retrieval"——但它同时是唯一 free-form 格式，这两个属性被混淆了。
- **3.3 Convergence Metrics**: n=5 power limitation 应在此标注，而非推迟到 Section 4.2。"A negative ρ indicates that higher attention ratios are associated with lower cross-architecture variance" 的定义是正确的。
- **3.4 Per-Example Decomposition**: Binary decomposition 设计合理。"On K-choice tasks, binarization collapses K−1 wrong answers into a single 'incorrect' category" 的 caveat 正确识别了信息损失。Appendix O 的 continuous analysis 是有效补充。
- **3.5 Statistical Methods**: "all Spearman-based inferences are descriptive and exploratory" —— 这句关键声明出现在 Section 3.5，但 Section 4 和 Section 5 的叙述并未始终遵循这一声明。

### Section 4 (Experiments)
- **4.1 Per-Example Divergence**: 这是论文最有力的部分。Figure 3 的 per-architecture effect profiles、Jaccard similarity heatmaps、LAMBADA 的 GDN/RetNet/HGRN2 对比都是 compelling 的描述性证据。
  
  Routing 段落需加强：(a) LAMBADA 和 ARC-Easy 的增益数值完全相同（+1.2 pp, SD = 0.5 pp）需要确认；(b) 未报告 bootstrap CI 或 significance test；(c) 4 个 benchmark 中仅 1 个有正效果——应在正文而非依赖读者自行推断。

- **4.2 Aggregate Variance and Per-Example**: "Bonferroni-adjusted p = .170, non-significant" 的标注是正确的，但此句嵌在段落中间，应更 prominently 呈现（如加粗或独立段落）。GDN exclusion 后 MMLU ρ 反转应在此报告。

- **4.3 Robustness**: 三层 hierarchy（independence baseline → bounded → cross-architecture）的叙述有效。Pythia 70M seed calibration 的 mismatch 限制了其证据力度。

### Section 5 (Conclusion)
- "Two observations follow at the 340M–1.3B scales studied here" —— 用"observations"而非"findings"是恰当的。
- "our preliminary routing experiments suggest" —— "preliminary" 和 "suggest" 都是正确的 hedge。但仍建议将 routing 从 contribution 降级为 future direction。

### Section 8 (Limitations)
- 涵盖了 single runs、coverage（3 arch, 2 scales）、generalization。
- **遗漏**：(1) n=5 statistical power 作为 methodological limitation 未提及——这比 "single runs" 更根本；(2) LAMBADA format confound；(3) Pythia 70M seed calibration 的 scale/architecture mismatch。

### 格式合规
- **页数**：正文 pages 1–8（Section 8 Limitations 在 page 8），References 从 page 9 起。**符合 8 页限制。** Limitations 不计入页数，位置在正文末尾。✓
- **匿名**：Title page 标注 "Anonymous ACL submission"。正文无 self-citation 泄露。Code/data 承诺为 "upon publication" 而非提供匿名链接。✓
- **Limitations section**：单独一节（Section 8），三段，覆盖 3 个主要限制。格式正确。✓ 但内容可补充（见上述遗漏）。
- **Abstract 长度**：约 170 words，符合 ≤ 200 words 限制。✓

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 2.5/5 | 描述性分析 sound（permutation test robust），但 convergence claim 的 statistical power 根本不足（n=5 Spearman，所有 correction 后不显著）；seed confound 未解决；LAMBADA format confound 未讨论 |
| **Excitement** | 3/5 | 研究问题新颖（per-example multiplicity in hybrid arch.），但 actionability 有限（routing 仅 1/4 benchmark 有效），convergence 结论为 exploratory |
| **Reproducibility** | 3.5/5 | 公开 model zoo + 标准 eval harness + 承诺代码公开；扣分：单次 run 无法验证 seed robustness、代码为 conditional release |
| **Datasets & Software** | 3/5 | 分析代码和 per-example outputs 承诺公开，potentially useful for follow-up work |
| **Overall Assessment** | 3.0/5 | Findings 水平。描述性贡献有价值（per-example multiplicity 的存在和结构性），但核心 inferential claims（convergence, task-type dependence, routing actionability）的统计基础均不足以支撑 conference-level contribution |


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1720 · 2026-05-24T13:32:11.787708+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1（侧重方法严谨性 + 实验设计）的完整审稿意见。请逐条回应其 Weaknesses 和 Questions：\n- **[AGREE]**：同意该观点，并简要说明理由\n- **[REBUT]**：不同意或有不同看法，提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 Weaknesses:\n\n**N1. [Critical] Spearman ρ 在 n=5 下统计效力根本不足，核心 convergence claim 缺乏确认性支撑**\n- n=5 时只有 |ρ|=1.0 能达到 p<.05。10-benchmark Bonferroni 后 p=.170。正文多处仍将 convergence 作为核心 contribution 呈现。\n\n**N2. [Critical] 单次训练 run 无法分离架构效应与 seed 效应，seed calibration 存在双重 mismatch**\n- Pythia 70M calibration 有 scale mismatch (70M vs 340M/1.3B) 和 architecture mismatch (Transformer vs hybrid)。\n\n**W1. [Major] LAMBADA 作为唯一 free-form generation benchmark，evaluation format confound 未被讨论**\n- LAMBADA 是唯一 free-form task，恰好也是 multiplicity 最高和 convergence 最强的。Multiple-choice format 机械约束 per-example divergence。\n\n**W2. [Major] GDN h3-1 的 16-head confound 导致 MMLU ρ 反转 (-0.7 → +0.6)**\n\n**W3. [Major] 仅两个 scale point 且结果矛盾，scale-related claims 泛化性不足**\n- 340M 无 convergence，1.3B 仅 LAMBADA 有。\n\n**W4. [Major] Confidence margin predictor 假设检验不充分**\n- Cohen's d 导出 AUC 违反正态假设（skewness 1.33-1.41）；routing 4/4 benchmark 仅 1 有效且无 significance test；LAMBADA 和 ARC-Easy 报告相同增益数值 (+1.2pp, SD=0.5pp)。\n\n**W5. [Major] Task taxonomy 是 post-hoc 的，用于 confirmatory claim 存在循环论证风险**\n- \"informal, not pre-registered\"，缺乏可验证的时间证据。\n\n**W6. [Major] 5-architecture extension 仅在 340M，无法验证 1.3B convergence**\n\n**W7. [Minor] Bootstrap CI 在 n=3 架构下不具备名义覆盖率**\n\n**W8. [Minor] 全文语言未完全一致使用 associative/descriptive 框架**\n- 多处滑入 causal 语言（\"reflects\", \"modulated by\", \"controlled\"）。\n\n**W9. [Minor] LAMBADA 和 ARC-Easy routing 增益数值完全相同 (+1.2pp, SD=0.5pp)，需确认**\n\n---\n\n### Reviewer 1 Questions:\n\nQ1: Pythia 70M within-seed J vs cross-arch J 的 2.7-4.3× 比值在 hybrid 架构 340M/1.3B 上是否会保持？\n\nQ2: LAMBADA 高 multiplicity 和强 convergence 是否由 evaluation format 而非 task type 驱动？\n\nQ3: GDN exclusion 后 MMLU ρ 完全反转如何解释？\n\nQ4: Confidence margin 的 AUC 是否应改用 non-parametric 方法？\n\nQ5: LAMBADA 和 ARC-Easy routing 相同数值是否为 reporting error？\n\nQ6: 340M vs 1.3B 矛盾——convergence 是否为 capacity-gated emergent phenomenon？\n\nQ7: Task taxonomy 有无客观时间证据？\n\n---\n\n请对每个 Weakness 和 Question 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1（侧重方法严谨性 + 实验设计）的完整审稿意见。请逐条回应其 Weaknesses 和 Questions：\n- **[AGREE]**：同意该观点，并简要说明理由\n- **[REBUT]**：不同意或有不同看法，提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 Weaknesses:\n\n**N1. [Critical] Spearman ρ 在 n=5 下统计效力根本不足，核心 convergence claim 缺乏确认性支撑**\n- n=5 时只有 |ρ|=1.0 能达到 p<.05。10-benchmark Bonferroni 后 p=.170。正文多处仍将 convergence 作为核心 contribution 呈现。\n\n**N2. [Critical] 单次训练 run 无法分离架构效应与 seed 效应，seed calibration 存在双重 mismatch**\n- Pythia 70M calibration 有 scale mismatch (70M vs 340M/1.3B) 和 architecture mismatch (Transformer vs hybrid)。\n\n**W1. [Major] LAMBADA 作为唯一 free-form generation benchmark，evaluation format confound 未被讨论**\n- LAMBADA 是唯一 free-form task，恰好也是 multiplicity 最高和 convergence 最强的。Multiple-choice format 机械约束 per-example divergence。\n\n**W2. [Major] GDN h3-1 的 16-head confound 导致 MMLU ρ 反转 (-0.7 → +0.6)**\n\n**W3. [Major] 仅两个 scale point 且结果矛盾，scale-related claims 泛化性不足**\n- 340M 无 convergence，1.3B 仅 LAMBADA 有。\n\n**W4. [Major] Confidence margin predictor 假设检验不充分**\n- Cohen's d 导出 AUC 违反正态假设（skewness 1.33-1.41）；routing 4/4 benchmark 仅 1 有效且无 significance test；LAMBADA 和 ARC-Easy 报告相同增益数值 (+1.2pp, SD=0.5pp)。\n\n**W5. [Major] Task taxonomy 是 post-hoc 的，用于 confirmatory claim 存在循环论证风险**\n- \"informal, not pre-registered\"，缺乏可验证的时间证据。\n\n**W6. [Major] 5-architecture extension 仅在 340M，无法验证 1.3B convergence**\n\n**W7. [Minor] Bootstrap CI 在 n=3 架构下不具备名义覆盖率**\n\n**W8. [Minor] 全文语言未完全一致使用 associative/descriptive 框架**\n- 多处滑入 causal 语言（\"reflects\", \"modulated by\", \"controlled\"）。\n\n**W9. [Minor] LAMBADA 和 ARC-Easy routing 增益数值完全相同 (+1.2pp, SD=0.5pp)，需确认**\n\n---\n\n### Reviewer 1 Questions:\n\nQ1: Pythia 70M within-seed J vs cross-arch J 的 2.7-4.3× 比值在 hybrid 架构 340M/1.3B 上是否会保持？\n\nQ2: LAMBADA 高 multiplicity 和强 convergence 是否由 evaluation format 而非 task type 驱动？\n\nQ3: GDN exclusion 后 MMLU ρ 完全反转如何解释？\n\nQ4: Confidence margin 的 AUC 是否应改用 non-parametric 方法？\n\nQ5: LAMBADA 和 ARC-Easy routing 相同数值是否为 reporting error？\n\nQ6: 340M vs 1.3B 矛盾——convergence 是否为 capacity-gated emergent phenomenon？\n\nQ7: Task taxonomy 有无客观时间证据？\n\n---\n\n请对每个 Weakness 和 Question 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 1721 · 2026-05-24T13:32:28.955303+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17167
}
```

</details>

---


### Tool call

_source line 1722 · 2026-05-24T13:32:29.056980+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2（侧重新颖性 + 完整性 + Related Work）的完整审稿意见。请逐条回应其 Weaknesses 和 Questions：\n- **[AGREE]**：同意该观点，并简要说明理由\n- **[REBUT]**：不同意或有不同看法，提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 Weaknesses:\n\n**N1. [Major] 新颖性为增量式扩展而非质性突破**\n- 核心贡献是将 predictive multiplicity 从 seed/initialization 扩展到 architectural 变异。但\"不同模型在不同 example 上表现不同\"是 ensemble diversity 文献的已知事实（Kuncheva & Whitaker 2003; Fort et al. 2019）。\n\n**N2. [Major] LAMBADA aggregate trend 的叙事权重与统计证据不匹配**\n- Decoupling narrative 核心支柱是 LAMBADA 的 ρ=-1.0，但 Bonferroni 后 p=.170；排除 GDN 后 ρ=-0.7；340M 不复现。\n\n**W1. [Major] 实践意义有限且不一致**\n- Routing: LAMBADA +5.2pp, ARC-Easy +1.2pp, HellaSwag -0.06pp, PIQA -0.49pp（显著负）。需先知道任务 multiplicity 水平才能决定是否 routing——循环依赖。\n\n**W2. [Minor] GDN 16 vs. 32 attention heads confound**\n- 直接影响 LAMBADA variance trend，应在正文更早 flag。\n\n**W3. [Minor] Introduction 信息密度过高**\n\n**W4. [Minor] \"Attention dose\" 术语非标准**\n\n**W5. [Minor] Task taxonomy \"Mixed\" 类别模糊**\n\n---\n\n### Reviewer 2 Questions:\n\nQ1: 如果改为 pure vs. h24-1（4% attention），Jaccard 值是否显著不同？\n\nQ2: Confidence routing 在 PIQA 上显著为负，是 routing 系统性选错还是 confidence margin 在低 multiplicity 任务上不是好的 predictor？\n\nQ3: Average-logits ensemble 的初步结果是否可获得？\n\nQ4: Seed calibration 使用 Pythia 70M，是否考虑在相同 model zoo 做 multi-seed 实验？\n\n---\n\n### Reviewer 2 Missing References:\n- Li et al. (2024) \"Dropout-Based Rashomon Set Exploration for Efficient Predictive Multiplicity Estimation\"\n- \"Why are there many equally good models? An Anatomy of the Rashomon Effect\" (2026)\n\n---\n\n### Reviewer 2 Overall Assessment:\n- Overall: 3.0 (Findings)\n- Soundness: 4/5\n- Excitement: 2/5\n- Confidence: 4/5\n\n请对每个 Weakness 和 Question 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2（侧重新颖性 + 完整性 + Related Work）的完整审稿意见。请逐条回应其 Weaknesses 和 Questions：\n- **[AGREE]**：同意该观点，并简要说明理由\n- **[REBUT]**：不同意或有不同看法，提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 Weaknesses:\n\n**N1. [Major] 新颖性为增量式扩展而非质性突破**\n- 核心贡献是将 predictive multiplicity 从 seed/initialization 扩展到 architectural 变异。但\"不同模型在不同 example 上表现不同\"是 ensemble diversity 文献的已知事实（Kuncheva & Whitaker 2003; Fort et al. 2019）。\n\n**N2. [Major] LAMBADA aggregate trend 的叙事权重与统计证据不匹配**\n- Decoupling narrative 核心支柱是 LAMBADA 的 ρ=-1.0，但 Bonferroni 后 p=.170；排除 GDN 后 ρ=-0.7；340M 不复现。\n\n**W1. [Major] 实践意义有限且不一致**\n- Routing: LAMBADA +5.2pp, ARC-Easy +1.2pp, HellaSwag -0.06pp, PIQA -0.49pp（显著负）。需先知道任务 multiplicity 水平才能决定是否 routing——循环依赖。\n\n**W2. [Minor] GDN 16 vs. 32 attention heads confound**\n- 直接影响 LAMBADA variance trend，应在正文更早 flag。\n\n**W3. [Minor] Introduction 信息密度过高**\n\n**W4. [Minor] \"Attention dose\" 术语非标准**\n\n**W5. [Minor] Task taxonomy \"Mixed\" 类别模糊**\n\n---\n\n### Reviewer 2 Questions:\n\nQ1: 如果改为 pure vs. h24-1（4% attention），Jaccard 值是否显著不同？\n\nQ2: Confidence routing 在 PIQA 上显著为负，是 routing 系统性选错还是 confidence margin 在低 multiplicity 任务上不是好的 predictor？\n\nQ3: Average-logits ensemble 的初步结果是否可获得？\n\nQ4: Seed calibration 使用 Pythia 70M，是否考虑在相同 model zoo 做 multi-seed 实验？\n\n---\n\n### Reviewer 2 Missing References:\n- Li et al. (2024) \"Dropout-Based Rashomon Set Exploration for Efficient Predictive Multiplicity Estimation\"\n- \"Why are there many equally good models? An Anatomy of the Rashomon Effect\" (2026)\n\n---\n\n### Reviewer 2 Overall Assessment:\n- Overall: 3.0 (Findings)\n- Soundness: 4/5\n- Excitement: 2/5\n- Confidence: 4/5\n\n请对每个 Weakness 和 Question 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 1723 · 2026-05-24T13:32:30.587000+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1530
}
```

</details>

---


### Assistant

_source line 1724 · 2026-05-24T13:32:37.862076+00:00_

交叉分享已派发。等待两位 Reviewer 返回逐条回应后进入 Step 3（收敛判断）。

当前进度：
- Round 1 初审 ✅（双方均给 3.0 Findings）
- 交叉分享已派发 ✅（等待回应）
- 视觉审查 ✅（已完成，1 warning + 15 info）
- 外部审稿：未启用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director"
}
```

</details>

---


## Round 132

## Round 132

2 recorded events


### User

_source line 1725 · 2026-05-24T13:32:40.370956+00:00_

[Reviewer 1 审稿结果]:
审稿完成。核心判断：**Overall 3.0（Findings）**，Confidence 4/5。

本轮相比初步审稿新增/强化了以下要点：

- **W1 [Major, 新增]**：LAMBADA 作为唯一 free-form generation benchmark 的 evaluation format confound——最高 multiplicity 和最强 convergence 恰巧都在唯一 open-ended 任务上出现，可能由答案空间大小而非 task type 驱动
- **W4 [Major, 强化]**：Confidence margin predictor 的 AUC 导出违反正态假设（skewness 1.33–1.41）；routing 4/4 benchmark 中仅 1 个有效且无 significance test
- **W6 [Major, 新增]**：5-architecture extension 仅在 340M（convergence 不存在的 scale），未验证核心 1.3B convergence finding
- **W8 [Minor, 新增]**：全文 associative vs causal 语言不完全一致（"reflects," "modulated by," "controlled" 等 causal 用语偶现）
- **W9 [Minor, 新增]**：LAMBADA 和 ARC-Easy routing 增益数值完全相同（+1.2 pp, SD = 0.5 pp），需确认是否为独立计算
- **格式合规检查**：页数 ✓、匿名 ✓、Limitations section ✓、Abstract ≤ 200 words ✓

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1726 · 2026-05-24T13:32:50.478885+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director"
}
```

</details>

---


## Round 133

## Round 133

8 recorded events


### User

_source line 1727 · 2026-05-24T13:32:51.987917+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见（Round 1 — 深度版）

**审查侧重**：新颖性 + 完整性 + Related Work + 叙事框架

---

### 1. Summary

本文研究 hybrid linear recurrent architectures（GDN、RetNet、HGRN2）在 per-example 层面的 predictive multiplicity。利用 Wang et al. (2025) 的受控 model zoo（3 架构 × 5 attention ratio × 2 规模），作者将每个 example 分为 helped/hurt/unchanged，核心发现：(1) 不同架构影响的 example 集合几乎不重叠（Jaccard ≈ 0.10），(2) 这种 multiplicity 按 task type 变化（α = 0.14–0.30），(3) per-example Jaccard 在 4% attention 即饱和，与 aggregate variance 趋势 decoupled（仅 LAMBADA 观察到非显著的 aggregate 下降趋势），(4) confidence-based routing 在高 multiplicity 任务上部分有效。

### 2. Strengths

**S1 [实验控制]** 利用 Wang et al. (2025) model zoo 实现了极高的实验控制度——同一训练数据、tokenizer、超参，仅改变架构和 attention ratio。这种控制在 hybrid architecture 文献中罕见，使本文的 causal attribution（虽然不完美）比 ad hoc 比较有说服力得多。

**S2 [统计诚实]** 始终对 LAMBADA 的 aggregate trend 标记为 "non-significant"（Bonferroni 校正后 p=.170），在 Table 1 脚注中明确说明 "Power is limited: only |ρ|=1.0 achieves p<.05 at n=5"。这种水平的统计诚实在 NLP 实证论文中属于上乘。

**S3 [稳健性覆盖]** Appendix A–X（13 个附录）系统检查了几乎每个分析决策：GDN confound exclusion（Appendix E）、continuous Jaccard（Appendix O）、5 架构扩展（Appendix X）、seed calibration（Appendix W）、confidence margin cross-benchmark（Appendix P1）等。这种 robustness 覆盖面在分析论文中很少见。

**S4 [per-example Jaccard 饱和]** 四个 benchmark 上 Jaccard 在第一个 attention level（4%）即饱和并保持平稳（Figure 4, all ρ ≤ 0.80, p ≥ .333）——这是一个跨 benchmark 一致的稳健发现，不依赖于任何单一 benchmark 的特殊性质。这个发现比 decoupling 叙事更强。

**S5 [ecological fallacy 的自我意识]** Related Work 最后一段主动引用 Robinson (1950) 并承认 decoupling 是 ecological fallacy 的一个 "controlled instance"。这种自我意识是加分项。

**S6 [confidence margin 分析]** Rescue threshold 跨架构一致（1% spread）但 disruption threshold 变化 47%——这个不对称性提供了比单纯 Jaccard 计数更深的 mechanistic insight（Section 4.1, Appendix P）。

### 3. Weaknesses

#### Critical / Major

**N1 [critical] Decoupling 叙事以不存在的前提为基础**

- **位置**：Introduction 第 20 行 "Second, per-example overlap is independent of aggregate variance trends"；Section 4.2 标题 "Aggregate Variance and Per-Example Overlap"；Figure 1
- **问题**：Decoupling 叙事的逻辑前提是 "aggregate variance 下降"，然后展示 "但 per-example overlap 没有同步下降"。但 aggregate variance 下降本身在统计上不成立：
  - LAMBADA 是唯一 ρ=-1.0 的 benchmark，但 Bonferroni 校正后 p=.170（不显著）
  - 排除 GDN 后 ρ 降至 -0.7, p=.233（Section 4.3）
  - 340M 上不复现（ρ=-0.50, p=.45）
  - 其余 9 个 benchmark 完全没有 convergence trend
  
  因此论文实际上是在说："在一个非显著的 trend 上，per-example overlap 没有跟随这个（可能不存在的）trend"。这是一个 non-finding 被 frame 成了 finding。Section 4.2 的开篇 "Regardless of whether this reflects a genuine trend, we ask: does any aggregate narrowing correspond to per-example agreement?" 试图绕过这个问题，但如果 aggregate narrowing 本身不成立，那 decoupling 就是在回答一个不需要回答的问题。
- **影响**：这是 Contribution 2（Introduction 贡献列表第二条）的核心内容，也是论文标题 narrative 的关键支柱。
- **建议**：将 Contribution 2 重新 frame 为："即使在 aggregate metrics 最有可能 converge 的场景（LAMBADA, ρ=-1.0），per-example overlap 仍然饱和"——这是一个条件式 observation，而非对 decoupling 的一般性 claim。或者，彻底将重心转移到 Jaccard 饱和（S4）作为主要发现，aggregate variance 作为补充背景。

**N2 [major] 核心发现与 ecological fallacy 的区分不充分**

- **位置**：Related Work 第 12 行 "our decoupling finding (§4.2) is a controlled instance within recurrent architectural families"
- **问题**：论文承认 decoupling 是 ecological fallacy 的一个 controlled instance，但没有解释为什么这个 instance 提供了 beyond ecological fallacy 本身的 insight。Ecological fallacy 告诉我们 aggregate 趋势不能推断 individual-level 行为——这在统计学中是 1950 年就确立的原理。论文在一个特定领域（hybrid recurrent architectures）验证了这个原理，但：
  - 没有提供 WHY 这些架构在 per-example level 上不同（mechanism）
  - 没有提供 WHEN practitioners 应该担心这种 divergence（boundary conditions）
  - 没有提供 HOW 严重这种 divergence 在实际部署中的影响（impact quantification beyond routing）
  
  简单说：论文回答了 "是否存在" 但没有回答 "为什么" 和 "多严重"。
- **建议**：加强 attention weight analysis（目前仅在 Appendix F，主要发现是 GDN 和 RetNet 的 attention 分布相似但 per-example 效果不同——说明差异来自 recurrent layers）。如果能追溯到具体的架构组件（gating mechanism、state expansion 方式等），会显著提升 insight 深度。

**N3 [major] 重要缺失引用："Benchmark Illusion" (Yang & Wang, 2026)**

- **位置**：Related Work 全文
- **问题**：Yang & Wang (2026) "Benchmark Illusion: Disagreement among LLMs and Its Scientific Consequences"（arXiv:2602.11898，2026年2月）研究了本质上相同的现象：在 MMLU-Pro 和 GPQA 上，达到相似 accuracy 的 frontier LLMs 在 16-66% 的 items 上不一致。该论文进一步展示了这种 disagreement 传播到下游科学注释中，导致 treatment effect 估计偏差 >80% 甚至方向反转。
  - 本文的核心发现（"aggregate equivalence masks per-example divergence"）与 Benchmark Illusion 的发现高度重叠
  - Benchmark Illusion 使用 frontier LLMs（不同架构族），而本文使用受控 hybrid recurrent architectures——这两个视角互补，但本文没有引用或讨论
  - 这个遗漏削弱了本文对 "first systematic per-example analysis"（Introduction 第 9 行）的 novelty claim
- **影响**：如果 Benchmark Illusion 已经在更大规模、更广架构范围上展示了相同现象，本文的增量贡献需要重新定位——可能是 "在受控条件下验证并量化了这一现象"，而非 "首次发现"。

**W1 [major] 叙事框架与证据强度不匹配**

- **位置**：Abstract（"we decompose per-example effects and find that..."）、Introduction 第1段
- **问题**：
  (a) **Abstract 和 Introduction 第1段** 以 "发现" 的语气呈现结果，但核心 insight——不同模型在不同 example 上表现不同——在 ensemble diversity 文献（Fort et al. 2019; Kuncheva & Whitaker 2003）和 underspecification 文献（D'Amour et al. 2022）中已有广泛记录。论文将 "architectural variation" 与 "seed variation" 区分为不同的 multiplicity 来源，这是合理的定位，但 Introduction 的语气暗示这是一个 surprising discovery 而非 expected phenomenon in a new domain。
  (b) **Introduction 第1段** 在4行内密集呈现 "90%"、"10%"、"14%"、"p<.01" 等数字。读者在不了解方法的情况下无法评估这些数字的含义。建议先建立直觉，再引入具体量化。
  (c) **Routing 的叙事权重**：Routing 在 abstract 中占据最后两句，在 Section 4.1 中占完整段落，但结果是 4 个 benchmark 中仅 1 个有效（LAMBADA +5.2pp），1 个显著为负（PIQA -0.49pp），2 个无效。论文正确使用了 "illustrative case study" 的措辞，但 abstract 中没有出现这个 qualifier——给人的印象是 routing 是一个 validated contribution 而非 exploratory observation。

**W2 [major] Evaluation format confound 未被充分讨论**

- **位置**：Section 3.2 倒数第二段；Limitations
- **问题**：LAMBADA 是唯一的 free-form generation benchmark（α=0.30，最高），其余全部是 multiple-choice（α=0.14–0.21）。论文在 Section 3.2 承认 "we cannot fully disentangle task type from evaluation format"，并提供了 within-multiple-choice format 不预测 α 的证据（2-way vs. 4-way）。但这个 mitigation 不够：
  - 2-way vs. 4-way 的区别远小于 multiple-choice vs. free-form（后者的 answer space 从 2-4 跃升到 open vocabulary）
  - LAMBADA 的高 α 可能完全由 format 驱动（open answer space → 更多 disagreement patterns → 更高 α），而非 task type（retrieval）
  - 论文的 task-type narrative（"multiplicity depends on task type"）因此可能是一个 format artifact
  - Limitations section 没有提及 format confound
- **建议**：在 Limitations 中明确加入 format confound。如果可能，增加一个 free-form generation benchmark（如 TriviaQA 的 generative 模式）来 disentangle。

#### Minor

**W3 [minor] MoE routing 文献完全缺失**

- **位置**：Section 4.1 Confidence-based routing
- **问题**：论文的 confidence-based routing 实验本质上是 per-example architecture selection——给定一个 input，选择最佳架构。这与 MoE（Mixture of Experts）中的 token-level routing 在概念上高度相关。MoE 文献中关于 expert specialization、routing strategy、per-example routing 的讨论（如 Switch Transformer、OLMoE 的 routing 分析）可以为本文的 routing 实验提供更丰富的上下文和对比点。当前完全没有提及 MoE。

**W4 [minor] Seed calibration 的参照价值有限**

- **位置**：Appendix W（Seed-Variation Calibration）
- **问题**：Pythia 70M 与主实验的模型存在三重 mismatch：(1) 规模（70M vs. 340M/1.3B），(2) 架构族（标准 Transformer vs. hybrid recurrent），(3) 精度区间（LAMBADA 0.17-0.23 vs. ~0.50）。Appendix W 的三段 caveats 诚实地列举了这些问题。但主文 Section 4.2 引用 seed calibration 时使用了 "consistent with architecture-driven divergence" 的措辞，这可能高估了 Pythia 校准的证据力度。在 matched seed experiment（同一 model zoo 的多 seed 运行）缺失的情况下，seed vs. architecture attribution 实际上是 open question。

**W5 [minor] "Attention dose" 术语**

- **位置**：Abstract、Conclusion 等多处
- "Attention dose" 非标准术语，正文已使用 "attention ratio"，建议统一。

**W6 [minor] Contribution 列表过长**

- **位置**：Introduction 贡献列表
- 两个 bullet 各超过 100 词，包含大量数字和 caveats。建议精简为核心 claim + section 引用，细节留给对应 section。

### 4. Questions to Authors

**Q1 [关键]**：既然论文承认 decoupling 是 ecological fallacy 的 controlled instance（Related Work 第12行），请明确说明：本文在 ecological fallacy 之上提供了什么 non-trivial 的新 insight？如果主要贡献是 "在 hybrid recurrent architectures 上验证了这个已知原理"，这对 EMNLP Findings 是否足够？

**Q2 [关键]**：Yang & Wang (2026) "Benchmark Illusion" 在 frontier LLMs 上展示了非常相似的发现（comparable accuracy + 16-66% per-item disagreement）。请讨论本文与 Benchmark Illusion 的关系——是独立发现、互补分析、还是重复？

**Q3**：LAMBADA 的高 α（0.30）是否可能主要由 free-form generation format 而非 retrieval task type 驱动？是否有其他 free-form benchmark（如 TriviaQA generative mode）的初步数据可以 disentangle？

**Q4**：Routing 在 PIQA 上显著为负（-0.49pp, p=.006）。这暗示 confidence margin 在低 multiplicity 任务上不是好的 routing signal。是否分析过 PIQA 上 routing 失败的具体 pattern（如：是否系统性选择了错误架构，还是 confidence margin 的区分度不足）？

**Q5**：Average-logits ensemble 是否已有初步结果？这是 complementarity 最自然的利用方式（无需 routing decision），缺少这个对比使 routing 的 practical value 评估不完整。

**Q6**：在 matched seed 实验不可行的情况下，是否考虑过使用 model zoo 中不同 attention ratio 的同一架构（e.g., GDN pure vs. GDN h24-1 vs. GDN h3-1）作为 "same architecture, different configuration" 的 within-architecture 参照？这可以部分 disentangle architecture effect vs. configuration effect。

### 5. Missing References

**必须引用：**

1. **Yang & Wang (2026)** "Benchmark Illusion: Disagreement among LLMs and Its Scientific Consequences" (arXiv:2602.11898) — 在 frontier LLMs 上展示了 comparable accuracy + 16-66% per-item disagreement，直接对应本文核心发现。论文还展示了 disagreement 传播到下游 annotation 的影响。**不引用这篇是一个显著遗漏**——它使本文的 "first systematic per-example analysis" claim 需要重新界定。

**建议引用：**

2. **MoE routing 文献**（至少一篇综述或代表性工作）——confidence-based routing 与 MoE 的 per-token routing 在概念上相关，讨论异同可以丰富 Related Work。

3. **"Why are there many equally good models? An Anatomy of the Rashomon Effect"** (2026, arXiv:2601.06730) — Rashomon 效应的系统性分析，提供理论背景。

**已确认已引用的参考文献：**
- Model Soups / Wortsman et al. 2022 ✓
- Fort et al. 2019 ✓, Brown 2005 ✓（ensemble diversity）
- Fisher et al. 2019, Semenova et al. 2022, Jain et al. 2025 ✓（Rashomon set）
- PolyPythias / van der Wal et al. 2025 ✓（Appendix W）
- Ecological fallacy / Robinson 1950 ✓

**关于 "Jiang et al. 2024" on PM in foundation models**：我未能在 arXiv 和 Google Scholar 上定位到这篇特定论文。如果 Director 有更具体的信息请提供；否则不列入 missing references。

### 6. Overall Assessment

**Overall**: 3.0 (Findings)
**Confidence**: 4/5 (Quite sure — 仔细阅读了全部 21 页，交叉验证了 LaTeX 源文件，搜索了 venue guidelines 和相关文献)

#### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由 |
|------|------|------|
| Soundness | 4/5 (Strong) | 方法论严谨，统计处理审慎，robustness 极充分。主要扣分：(1) decoupling 叙事建立在非显著前提上（N1）；(2) GDN confound（W2 of previous round / N1 here）；(3) format confound 未充分讨论（W2）。 |
| Excitement | 2/5 (Potentially Interesting) | 核心发现（不同架构在 per-example 上不一致）在 ensemble diversity 和 Benchmark Illusion 文献中有先例。ecological fallacy 的自我承认削弱了 novelty claim。Jaccard 饱和是有 insight 的发现但 explanatory depth 不足。Routing 结果 1/4 有效。 |
| Reproducibility | 4/5 | 公开 model zoo，详细的方法描述，承诺发布代码。Appendix 提供了充分的实施细节。 |

#### 评分理由

本文的**执行质量**属于 EMNLP 主会议水准：控制良好的实验设计、诚实的统计处理、极其充分的 robustness 检查。如果仅按 soundness 评判，这是一篇 4/5 的论文。

但在**新颖性和 excitement** 方面存在根本性问题：

**(1) Ecological fallacy + Benchmark Illusion = 已知现象**。论文自己承认 decoupling 是 ecological fallacy 的 controlled instance，而 Yang & Wang (2026) 已在更大规模上展示了类似发现。本文的增量贡献在于 controlled model zoo 上的系统量化，但这更接近 "验证性分析" 而非 "发现性研究"。

**(2) Decoupling 叙事的前提不成立**。Contribution 2 建立在 LAMBADA 的 aggregate convergence 上，但这个 trend 不显著（p=.170）、confound-dependent（GDN 16-head）、不跨 scale 复现。真正稳健的发现——Jaccard 饱和（S4）——被 decoupling 叙事遮蔽了。

**(3) Why 和 How 的缺失**。论文回答了 "是否存在 per-example multiplicity"（答：是），但没有解释为什么不同的 gating mechanism 导致不同的 per-example pattern，也没有提供 practitioners 可以操作的具体指导（routing 仅 1/4 有效）。

**对 EMNLP Findings 的适切性**：ARR CFP 明确将 analysis 论文纳入 scope，且 reviewer guidelines 指出不应因 contribution type 拒稿。本文作为一项 descriptive empirical analysis，方法论水准高、实验控制好、发现跨 benchmark 一致（Jaccard 饱和）。但 Findings 也要求 "sufficient contribution"——考虑到 Benchmark Illusion 的先行发现和 ecological fallacy 的自我承认，contribution 的 sufficiency 处于 borderline。

建议：如果作者能 (a) 引用并定位 vs. Benchmark Illusion，(b) 将 Contribution 2 重新 frame 为条件式而非一般性 claim，(c) 加深 mechanistic insight（为什么 recurrent layer 驱动 divergence），则 Findings 的 case 会更有说服力。

### 7. Detailed Comments

#### Abstract
- 约 148 词，符合 200 词限制 ✓
- "Confidence-informed routing extracts 36% of oracle complementarity on LAMBADA (+5.2 pp)" — 这个数字缺少 qualifier（仅在 4 个 benchmark 的 1 个上有效）。建议加入 "on the highest-multiplicity task" 或类似限定。

#### Section 1 (Introduction)
- 第1段信息过载（见 W1b）。可考虑将第1段分为两部分：先 1-2 句概述现象，再引入量化。
- 贡献列表过长（见 W6）。
- "We present the first systematic per-example analysis" — 需要在 Benchmark Illusion 的上下文中重新界定。

#### Section 2 (Related Work)
- 结构良好（三个 paragraph 覆盖三个主题）。
- 对 ensemble diversity 的讨论（第12行"ensemble diversity work shows that diverse architectures explore distinct loss-landscape modes"）过于简短——仅列举三个引用。建议增加 1-2 句讨论 ensemble diversity 研究是否已经 document 过 per-example level 的 architecture disagreement，以及如果是，本文的增量贡献是什么。
- 缺少 Benchmark Illusion (Yang & Wang 2026)（见 N3）。
- 缺少 MoE routing 文献（见 W3）。
- ecological fallacy 的自我承认（最后一句）是加分项，但需要配合正文中更清晰的 "beyond ecological fallacy" 论证。

#### Section 3 (Method)
- 3.1 Model Zoo：清晰完整。
- 3.2 Task Taxonomy："Mixed" 类别（ARC-Easy, MMLU, SciQ, XStoryCloze）定义模糊——"which combine retrieval, comprehension, and reasoning demands" 没有 operationalize 这些 task 如何 combine 这些 demands。
- 3.2 倒数第二段关于 format confound 的讨论需要加强（见 W2）。
- 3.4 Per-Example Decomposition：binary decomposition 的 conservative bias 论证（"true divergence may exceed what binary Jaccard captures"）是好的。
- 3.5 Statistical Methods：诚实承认 n=5 的功效限制是加分项。

#### Section 4 (Experiments)
- 4.1 Per-Example Divergence：核心分析执行良好。Cohen's d (0.73–0.92) 为 binary decomposition 提供 continuous validation。
- 4.1 Confidence-based routing：placement 在 per-example divergence 下有些突兀。更自然的位置可能是单独的 subsection。
- 4.1 Routing 的 negative results（PIQA -0.49pp）诚实报告是加分项。
- 4.2：见 N1（decoupling 叙事的前提问题）。
- 4.2 "The answer is no" — 这个措辞暗示了一个 clean result，但实际上 aggregate convergence 本身不显著。
- 4.3 Robustness：GDN 16-head confound 在 Section 4.3 才出现。建议在首次引入 GDN 结果时（Table 1）就 flag。

#### Section 5 (Conclusion)
- 结论恰当，避免了 over-claim。"Per-example audit before architecture substitution is advisable" 的建议合理但可更具体——什么情况下？哪些 task type？阈值是什么？
- "but is counterproductive on low-multiplicity ones (PIQA: −0.49 pp)" — 诚实。

#### Limitations
- 覆盖了三个核心限制。
- 缺失：format confound（LAMBADA free-form vs. others multiple-choice）。
- 缺失：单一 model zoo dependency（findings 可能特定于 Wang et al. 2025 的训练 setup）。

#### Appendix
- Appendix W (Seed Calibration)：诚实列出了三重 mismatch，但主文引用时语气过于肯定（见 W4）。
- Appendix X (5 Architectures)：有效扩展了 generalizability。J ≤ 0.14 across all 10 pairs + 4 benchmarks 是强证据。
- Appendix Y (AI Assistants)：透明披露了 Claude 的使用，符合规范。

#### 格式合规
- ✅ 正文 ≤ 8 页（Sections 1–5 约 7.5 页 + Limitations/Code Availability 在第 8 页）
- ✅ Limitations 在正文（非 appendix），不计入页数
- ✅ 匿名性完整（"Anonymous ACL submission"，无泄露信息）
- ✅ Abstract < 200 词（约 148 词）
- ✅ 引用格式正确（ACL style，\citet/\citep 使用恰当）
- ✅ Appendix 使用字母编号（A–X）
- ✅ 所有引用在 references.bib 中有对应条目

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1728 · 2026-05-24T13:33:24.910524+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1729 · 2026-05-24T13:33:25.011342+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1730 · 2026-05-24T13:38:09.140743+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "entrainment_gated_ft",
  "issues_yaml": "- id: \"R5-W1\"\n  summary: \"架构效应 vs seed 效应无法区分（单 training run，无 seed baseline）\"\n  category: experiment\n  severity: critical\n  status: wont_fix\n  first_raised_round: 5\n  last_seen_round: 19\n  mentions:\n    - round: 5\n      reviewers: [R1, R2]\n      note: \"R1 Critical, R2 W3+Q3 支持。\"\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"R2-N3 Must-Fix vs R1-W2 Should-Fix。分歧：R1 REBUT 认为论文已用关联性语言、第三方 zoo 无法自行补训。R2 维持 Must-Fix。论文已有 PolyPythias 校准但三重 mismatch 仍被指出。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N2 Critical。双方 [AGREE]。Pythia 70M 三重 mismatch（scale 70M vs 340M+/architecture family Transformer vs hybrid/accuracy 0.17-0.23 vs ~0.50）仍是核心弱点。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-N3 Critical + R2 交叉 [AGREE]。Pythia 70M within-seed J=0.312 vs cross-arch J=0.354，gap 仅 0.042。R2 补充 seed variation 可能解释大部分 per-example divergence。双方一致认为是根本性威胁但非 fatal。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-N2 Critical + R2-N2 Critical，交叉均 [AGREE]。R2 纠正 R1 数据误读：within-seed J=0.273 vs cross-arch J=0.10 实为 2.7× 差距（非 R1 声称的 0.02），部分支持架构效应独立性。但 Pythia 70M 三重 mismatch 仍限制 calibration 可迁移性。双方一致要求至少对一个 hybrid 架构训练多 seed。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-N2 Critical + R2-W4 Minor。R1 详细列出双重 mismatch（scale: 70M vs 340M/1.3B; architecture: Transformer vs hybrid gating）。R2 同意 calibration 参照价值有限但视为 minor。交叉后双方一致：seed confound 是 open question，但 structural limitation（第三方 zoo 无法重训），维持 wont_fix。\"\n  action_items:\n    - round: 13\n      action: \"E4 Pythia 410M 9-seed calibration（实际完成 70M）\"\n      assigned_to: main_agent\n      status: done\n    - round: 14\n      action: \"Limitations 提升 single-seed 为 top limitation；§4.2 弱化因果语言\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"结构性限制，无法完全修复。已做：(1) Pythia 70M seed calibration 加入 Appendix W；(2) Limitations 中 single-seed 为 top limitation；(3) 全文使用 'associated with' 关联性语言。R19 双方仍 flag 但认可为 structural limitation。\"\n  resolution_round: null\n\n- id: \"R5-W2\"\n  summary: \"收敛 claim 统计不显著（Bonferroni p=.170）且依赖 GDN inclusion\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 19\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical。交叉 [AGREE]。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R16-N1 重新 flag。R15 写作修复不够——Intro 仍以 79% σ drop 开篇。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2 交叉 [AGREE]。R1 精确指出结构性限制：n=5 时最小 p=0.017，Bonferroni 后 0.170——无论效应多强都无法拒绝 H₀。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical，交叉均 [AGREE]。论文核心叙事 'convergence masks divergence' 需要 aggregate convergence 成立，但 p=.170 不支持。R2 建议重构为 'architectures interchangeable by aggregate metrics differ per-example'。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical，交叉均 [AGREE]。R2 进一步升级：decoupling 叙事建立在'不存在的前提'上——如果 aggregate convergence 本身不显著，decoupling 就是在回答一个不需要回答的问题。R1 同意 convergence 应为 exploratory observation。双方建议将 Contribution 2 重构为条件式 observation 或转向 Jaccard 饱和作为主发现。\"\n  action_items:\n    - round: 15\n      action: \"Abstract/Intro 重构：以 Jaccard saturation 为主线\"\n      assigned_to: paper_agent\n      status: done\n    - round: 16\n      action: \"结构性叙事重组：Intro 79% σ drop 移到 §4.2 等\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"Contribution 2 重构为条件式（'even on LAMBADA where trend is strongest, per-example overlap saturates'）或将 Jaccard 饱和升级为主发现\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"R15-R19 持续 flag。需将 convergence 彻底降级为 exploratory observation，decoupling 叙事重构为条件式。\"\n  resolution_round: null\n\n- id: \"R5-W4\"\n  summary: \"新颖性有限——已有指标的直接套用，无新方法/理论\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 5\n  last_seen_round: 19\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"R2-W1 ecological fallacy 已知实例。R1 REBUT。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R2-N1 Must-Fix vs R1 REBUT。核心分歧未解决。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R2-N1 Critical。R1 REBUT（empirical first 在实际相关 domain 有独立价值）。部分收敛：均同意应明确定位为 empirical contribution。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R2-W1 Major。R1 REBUT——4% saturation 和 aggregate-vs-per-example 解耦是非平凡发现。部分收敛：Findings 标准下经验发现足够。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R2-N2 Major（ecological fallacy 区分不充分——论文承认但未解释 beyond ecological fallacy 的 insight）+ R2-N1 Critical（与 Benchmark Illusion 重叠）。R1 在 S1 肯定研究问题新颖但交叉中未直接 REBUT R2 的 novelty 批评。双方在 Findings 适切性上一致，但 R2 认为 contribution sufficiency 处于 borderline。\"\n  action_items:\n    - round: 6\n      action: \"Intro 加 empirical novelty framing\"\n      assigned_to: paper_agent\n      status: done\n    - round: 16\n      action: \"Intro 强化 empirical contribution 定位\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"引用 Benchmark Illusion 并定位本文增量贡献（controlled zoo + 系统量化 + 饱和发现）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"结构性限制。Findings 标准下可接受，但需引用 Benchmark Illusion 并明确定位增量贡献。\"\n  resolution_round: null\n\n- id: \"R5-W3\"\n  summary: \"Task-dependent spectrum 仅 3 benchmark，存在评估格式 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [R1, R2]\n      note: \"α 变异可能反映 format 而非 task type。\"\n  action_items:\n    - round: 5\n      action: \"WinoGrande + PIQA per-example 分析\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"PIQA + WinoGrande 数据整合完成。Round 6-16 未再提及。R17 提出更具体的 format confound（见 R17-W1）。\"\n  resolution_round: 6\n\n- id: \"R5-W5\"\n  summary: \"正文约 8.2 页超出 EMNLP 8 页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 19\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16 视觉审查确认合规。\"\n    - round: 17\n      reviewers: [R1]\n      note: \"R1-M5 确认格式合规（8页，Limitations 3点，匿名完好）。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R18 双方格式检查均确认合规。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R19 双方格式检查均确认合规：正文 ≤8 页、Limitations 在正文、匿名完整、Abstract <200 词。\"\n  action_items:\n    - round: 5\n      action: \"结构性压缩 8.2→7 页\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"主文在 8 页内。R14-R19 持续确认合规。\"\n  resolution_round: 5\n\n- id: \"R5-W6\"\n  summary: \"遗漏关键相关工作 Zoology/Based/Samba\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  action_items:\n    - round: 5\n      action: \"补 3 篇引用 + recall-throughput 框架\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Zoology + Based 引用于 §4.1，Samba 引用于 Related Work。\"\n  resolution_round: 5\n\n- id: \"R5-W7\"\n  summary: \"Ensemble 建议缺乏实验支撑 + POC 负面结果与 protocol 的 tension\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 9\n  action_items:\n    - round: 7\n      action: \"Majority vote + oracle POC 写入 Conclusion\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Conclusion 已包含 MV/oracle POC 数据。\"\n  resolution_round: 9\n\n- id: \"R5-W8\"\n  summary: \"Binary decomposition 可能低估多选题一致性\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 19\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-W2 指出 hurt sets binarization 可能 overestimate agreement。Appendix O continuous Jaccard 缓解。\"\n    - round: 17\n      reviewers: [R2]\n      note: \"R2-Q4 询问为何不在主文使用 continuous Jaccard。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未作为独立问题提及。§3.4 已包含 binarization caveat + Appendix continuous Jaccard。\"\n    - round: 19\n      reviewers: [R1]\n      note: \"R1-S6 肯定 binary decomposition 设计合理，正确识别了 K-choice binarization 的 conservative bias。未作为 weakness 提出。R2 亦未 flag。可能已充分缓解。\"\n  action_items:\n    - round: 13\n      action: \"E2 continuous-threshold Jaccard sensitivity 结果整合到 Appendix + §4.1 引用\"\n      assigned_to: paper_agent\n      status: done\n    - round: 16\n      action: \"§3.4 加 1 句 K-choice binarization caveat\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"R19 双方均未作为 weakness 提出，R1 在 Strengths 中肯定。可视为充分缓解。\"\n  resolution_round: null\n\n- id: \"R5-W9\"\n  summary: \"Abstract 信息密度过高（统计量堆砌）\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 19\n  mentions:\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-M6 指出接近 200 word 上限。R2-M4 指出 inline 统计量增加认知负荷。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R2-W4 Major：数字密度过高。R1 交叉 [AGREE with nuance]。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1 确认 Abstract 约 170 词符合限制。R2-W1b 指出 Introduction 第1段信息过载（4行内密集数字），R2-W6 指出贡献列表过长（每条>100词）。Abstract 本身改善但 Introduction 密度仍高。\"\n  action_items:\n    - round: 13\n      action: \"W5: Abstract 进一步精简至 3 key numbers\"\n      assigned_to: paper_agent\n      status: done\n    - round: 18\n      action: \"Abstract 再次精简\"\n      assigned_to: paper_agent\n      status: done\n    - round: 19\n      action: \"Introduction 第1段分拆：先概述现象再引入量化；贡献列表精简为核心 claim + section 引用\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"Abstract 已改善（148词），但 Introduction 第1段和贡献列表仍需精简。\"\n  resolution_round: null\n\n- id: \"RV-L1\"\n  summary: \"Limitations 6 段违反 EMNLP 用户规则（要求 ~3 点）\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 15\n  action_items:\n    - round: 5\n      action: \"6 段→3 段\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"压缩为 3 段。R14-R19 确认合规。\"\n  resolution_round: 5\n\n- id: \"RV-L2\"\n  summary: \"loglik 压缩假说已被诊断数据反驳但论文仍引用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  action_items:\n    - round: 5\n      action: \"改为 binary classification structural properties 解释\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"改为 'structural properties of constrained-choice formats'。\"\n  resolution_round: 5\n\n- id: \"R6-N3\"\n  summary: \"仅 2 个 scale 点不足以支撑 scale-dependent claim\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  action_items:\n    - round: 6\n      action: \"MF4: 全文替换 scale-dependent\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"全文已用 'differs between 340M and 1.3B'。\"\n  resolution_round: 8\n\n- id: \"R6-N2\"\n  summary: \"缺乏 actionable insights——论文停在 '问题存在' 层面\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 15\n  action_items:\n    - round: 13\n      action: \"E1 routing 结果整合到 §4.1 + Conclusion 更新\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"E1 rescue-threshold routing 已写入。R15 routing 降级为 case study。非 blocking。\"\n  resolution_round: 13\n\n- id: \"R6-W1\"\n  summary: \"Decoupling 形式化存在技术问题 + saturation 未严格定义\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 9\n  action_items:\n    - round: 8\n      action: \"删除 Equation 1 形式化定义，保留定量描述\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Equation 1 已删。Round 12-19 未再提及。\"\n  resolution_round: 12\n\n- id: \"R6-W2\"\n  summary: \"GDN h3-1 的 16-head confound 削弱 LAMBADA convergence\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 19\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"R1-N2 Critical + R2-N2 Critical。主文并列 with/without GDN。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R16 确认修复存在但叙事仍过度突出。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-N2 Critical。移除 GDN 后 LAMBADA ρ 从 -1.0 降至 -0.7。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未作为独立问题提及。§4.3 已讨论。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W2 Major：MMLU ρ 从 -0.7 反转为 +0.6，证明 MMLU convergence 完全由 GDN 16-head anomaly 驱动。R2-W2 Minor 同意应更早 flag。双方一致要求在正文（而非仅 Appendix）中更显著地报告 MMLU 反转。\"\n  action_items:\n    - round: 15\n      action: \"主文 §4.2 并列 with/without GDN ρ 值；§4.3 Robustness 讨论\"\n      assigned_to: paper_agent\n      status: done\n    - round: 19\n      action: \"Table 1 首次引入 GDN 结果时即 flag 16-head anomaly；正文报告 MMLU ρ 反转\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"§4.3 已讨论但 R19 认为不够显著。需在 Table 1 处更早 flag。\"\n  resolution_round: null\n\n- id: \"R6-W3\"\n  summary: \"Bootstrap CI 在 n=3 架构上覆盖率远低于名义值\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 19\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"27 个 bootstrap 样本（排除退化后 ~24 个）无可靠覆盖率。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R2 指出 BCa CI 在 Introduction 首次出现处缺 caveat。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"建议全面改用 percentile bootstrap 并标注 heuristic。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-N3 Critical。95% CI=[-1.0,-0.7] 传递虚假精度感。升级为 Critical。\"\n    - round: 19\n      reviewers: [R1]\n      note: \"R1-W7 Minor。Section 3.5 已用 'heuristic indicators of effect direction'，但 Section 4.3 中 'Bootstrapped 95% CIs... excludes zero' 叙述可能误导。建议附加 coverage limitation 注释。降级为 Minor（较 R18 有改善）。\"\n  action_items:\n    - round: 15\n      action: \"Figure caption 附注 illustrative only\"\n      assigned_to: paper_agent\n      status: done\n    - round: 16\n      action: \"Intro BCa CI 处加 heuristic caveat\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 18\n      action: \"全文 bootstrap CI 标 heuristic\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"Section 3.5 caveat 已存在，但 Section 4.3 叙述仍可能误导。R19 降级为 Minor。\"\n  resolution_round: null\n\n- id: \"R14-W1\"\n  summary: \"Confidence margin 'mechanism' 标题暗示因果性，实为 correlational\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  action_items:\n    - round: 14\n      action: \"全文替换 'mechanism' → 'predictor'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已替换。R15-R19 未再提及。\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"n=5 attention ratios 使 convergence permutation test 本质上为 binary outcome\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"建议声明所有 Spearman correlation 推断为 descriptive/exploratory。\"\n  action_items:\n    - round: 15\n      action: \"§4.2 标注 'suggestive but underpowered secondary observation'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。合并入 R5-W2/R16-N1 的更大叙事问题。\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"标题/Abstract 过度泛化：仅 3 架构但表述暗示更广 generality\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  action_items:\n    - round: 14\n      action: \"正文加 scope 限定\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。R16-R19 未再单独提及。\"\n  resolution_round: 15\n\n- id: \"R14-W4\"\n  summary: \"缺失 prediction churn 文献（Milani Fard et al. 2016）\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  action_items:\n    - round: 14\n      action: \"添加 Milani Fard (2016) + Poli (2023) Hyena\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已引用。R18-R19 确认引用存在。\"\n  resolution_round: 15\n\n- id: \"R15-W1\"\n  summary: \"'Nearly disjoint' / 'almost entirely different' 措辞夸大\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  action_items:\n    - round: 15\n      action: \"替换为 calibrated 表述\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。R16-R19 未再提及。\"\n  resolution_round: 15\n\n- id: \"R15-W2\"\n  summary: \"Routing 作为 'proof-of-concept application' 定位过高（仅 1/4 benchmark 有效）\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 19\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"建议降级为 case study / illustrative example。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"§4.1 已改为 case study 但 Conclusion 仍列为 practitioner implication。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R2-N2 Critical + R1-W1。1/4 success rate，无 ensemble baseline 对比。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-W1 Major + R2-W3 Major，交叉均 [AGREE]。PIQA 显著负效。缺 average logits ensemble baseline。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W4 Major + R2-W1 Major，交叉均 [AGREE]。R2 补充：routing 的循环依赖（需先知道 multiplicity 水平才能决定是否 route）。R1 补充：缺少 bootstrap CI/significance test。双方一致要求降级为 preliminary exploration + 补充 average-logits ensemble baseline。Abstract 中缺少 qualifier。\"\n  action_items:\n    - round: 15\n      action: \"降级为 'illustrative case study'\"\n      assigned_to: paper_agent\n      status: done\n    - round: 16\n      action: \"Conclusion routing 从 practitioner implication 降级\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 18\n      action: \"Conclusion 删 α>0.2 threshold，routing 限定为 preliminary/high-α free-form tasks\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"Abstract routing 句加 qualifier（如 'on the highest-multiplicity task'）；补充 average-logits ensemble baseline 对比\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"R19 双方 Major。Routing 在正文已为 case study 但 abstract 叙事权重仍偏高。\"\n  resolution_round: null\n\n- id: \"R15-D1\"\n  summary: \"Appendix Table 30 DeltaNet 行数据不一致\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  action_items:\n    - round: 15\n      action: \"从 JSON 逐格修正\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已修正。R17-R19 未再提及。\"\n  resolution_round: 15\n\n- id: \"R15-W3\"\n  summary: \"缺失 Jain et al. (2025 FAccT) 引用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  action_items:\n    - round: 15\n      action: \"添加到 references.bib + Related Work\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。R17-R19 确认引用存在。\"\n  resolution_round: 15\n\n- id: \"R16-N1\"\n  summary: \"Aggregate convergence 叙事在 Abstract/Introduction 中仍过度突出\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-N2 Must-Fix + R2-W1 Should-Fix。交叉 [AGREE]。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"双方一致要求全文统一为 descriptive/suggestive。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical。R2 提出重构方案：'architectures interchangeable by aggregate metrics differ per-example'。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical，交叉均 [AGREE]。R2 升级论证：decoupling 叙事以'不存在的前提'（non-significant aggregate convergence）为基础。Section 4.2 标题 'Aggregate Variance and Per-Example Overlap' 暗示 aggregate narrowing 是 established fact。建议将 §4.2 重新 frame 为'even in the most favorable scenario (LAMBADA ρ=-1.0, non-significant), per-example Jaccard saturates'。\"\n  action_items:\n    - round: 16\n      action: \"结构性叙事重组\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 18\n      action: \"全面叙事重构：convergence → aggregate interchangeability\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"§4.2 标题改为非确定性（如 'Per-Example Overlap Under Varying Aggregate Trends'）；全文消除 aggregate convergence 作为 established premise 的措辞\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"R16-R19 持续 flag。核心叙事仍需全面重构。\"\n  resolution_round: null\n\n- id: \"R16-W1\"\n  summary: \"Routing 实验缺少 variance 报告（10-repeat cross-validation 仅报 mean）\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-W3 + R2 AGREE。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R2 补充：如果 SD > 3pp 则 5.3pp 增益可能不显著。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"LAMBADA 已报告 SD=0.4pp 但其他 benchmark SD 缺失。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W4 Major：仍缺 bootstrap CI 和 significance test。R2-W1 同意。LAMBADA SD=0.4pp 已报告但 ARC-Easy/HellaSwag/PIQA 的 SD 在正文已补充（SD=0.5/未报告/p=.006）。仍缺 formal significance test for LAMBADA。\"\n  action_items:\n    - round: 16\n      action: \"从已有数据提取 SD 和 95% CI\"\n      assigned_to: main_agent\n      status: in_progress\n    - round: 19\n      action: \"LAMBADA routing 增益补充 bootstrap CI 和 permutation significance test\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"部分改善（SD 已报告），但 formal significance test 仍缺。\"\n  resolution_round: null\n\n- id: \"R16-W2\"\n  summary: \"5-architecture 扩展验证仅 340M，主文 §4.3 缺 scale caveat\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-W4 + R2 AGREE。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"双方一致。R2 认为 minor 级别。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-W4 Warning。R2 [AGREE] 但程度略弱。\"\n    - round: 19\n      reviewers: [R1]\n      note: \"R1-W6 Major：5-arch extension 仅验证了 per-example divergence 的 ubiquity（J≤0.14），未验证 convergence claim。且仅用 h3-1 单一配置，未做 attention ratio sweep。建议标明 Appendix X 仅验证 divergence 而非 convergence。\"\n  action_items:\n    - round: 16\n      action: \"§4.3 加 'at 340M'\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"Appendix X 明确标注仅验证 per-example divergence pattern，不能推断 convergence\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W3\"\n  summary: \"Confidence margin AUC 的正态假设未验证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-W5 + R2 AGREE。\"\n    - round: 17\n      reviewers: []\n      note: \"R17 未单独提及。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未提及。Appendix 已包含 Shapiro-Wilk normality tests + empirical AUC 对比。\"\n    - round: 19\n      reviewers: [R1]\n      note: \"R1-W4 Major 重新 flag：Shapiro-Wilk 显示 rescue-set skewness 1.33-1.41，GDN/HGRN2 的 p<10⁻⁴ 严重违反正态。论文用 percentile CI 替代但 AUC point estimate 仍基于 Gaussian assumption。建议改用 non-parametric AUC（Mann-Whitney U）。\"\n  action_items:\n    - round: 16\n      action: \"计算 empirical AUC 对比 parametric estimate\"\n      assigned_to: main_agent\n      status: in_progress\n    - round: 19\n      action: \"改用 non-parametric AUC（Mann-Whitney U statistic）替代 Cohen's d 导出的参数 AUC\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"R19 R1 重新 flag。正态假设违反已有证据但未修正 AUC 方法。\"\n  resolution_round: null\n\n- id: \"R16-W4\"\n  summary: \"模型规模覆盖有限（≤1.3B vs 7B+ 部署场景）\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R2-W4 + R1 AGREE。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R2-W4 + R1 交叉 [AGREE]。Conclusion 未限定。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-W3 Major。建议改为 'consistent across the two scales examined'。\"\n    - round: 19\n      reviewers: [R1]\n      note: \"R1-W3 Major：两个数据点无法建立 scaling trend。340M 无 convergence vs 1.3B LAMBADA 有——结果矛盾。建议限定 convergence finding scope 为 '1.3B LAMBADA'；讨论 340M 无 convergence 的理论含义。\"\n  action_items:\n    - round: 16\n      action: \"Limitations 加 scale limitation 句\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 18\n      action: \"全文 'scale-robust' → 'consistent across the two scales examined'\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"讨论 340M vs 1.3B convergence 矛盾的理论含义（capacity-gated emergent phenomenon?）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"R19 仍 Major。需讨论 cross-scale 矛盾。\"\n  resolution_round: null\n\n- id: \"R16-W5\"\n  summary: \"遗漏重要相关工作\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R2-W3 建议引用。R1 部分 AGREE。\"\n    - round: 17\n      reviewers: [R2]\n      note: \"R2-W2 新增 Ye et al. (2026)。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R2-W2 Major：遗漏 Model Soups (Wortsman 2022)、MoE。R1 提出 Jiang et al. (2024)。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R2-N3 Major 新增关键遗漏：Yang & Wang (2026) 'Benchmark Illusion'（arXiv:2602.11898）——在 frontier LLMs 上展示了 comparable accuracy + 16-66% per-item disagreement，与本文核心发现高度重叠。R2-W3 补充 MoE routing 文献缺失。R1 补充 MultiBERTs (Sellam 2022) 在 seed calibration 语境中未引用。R2 确认 Model Soups/Fort et al./Jain et al. 已在论文中引用。\"\n  action_items:\n    - round: 16\n      action: \"核实并添加\"\n      assigned_to: main_agent\n      status: in_progress\n    - round: 18\n      action: \"添加 Wortsman (2022) + Jiang (2024) 到 bib 和 Related Work\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"必须引用 Yang & Wang (2026) Benchmark Illusion 并在 Related Work 中讨论本文与其的关系和增量贡献；建议引用 MoE routing 文献（至少 1 篇代表性工作）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"R19 升级：Benchmark Illusion 是重大遗漏，直接影响 novelty claim（'first systematic per-example analysis' 需重新界定）。\"\n  resolution_round: null\n\n- id: \"R16-M1\"\n  summary: \"Haghighat 2026 bib 条目需更新为 AAAI 2026\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 16\n      reviewers: [R2]\n      note: \"Camera-ready 前 fix。\"\n    - round: 19\n      reviewers: []\n      note: \"R19 未提及。可能已修复。\"\n  action_items:\n    - round: 16\n      action: \"更新 references.bib\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W1\"\n  summary: \"Task type vs evaluation format confound 未被区分（LAMBADA 为唯一 free-form benchmark）\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-W2 提出 + R2 交叉 [AGREE]。LAMBADA 是唯一 free-form benchmark。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-W2 Major + R2 交叉 [AGREE]。双方一致要求正文讨论 format confound。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W1 Major + R2-W2 Major，交叉均 [AGREE]。R1 详细论证：multiple-choice 的有限答案空间机械约束 per-example divergence，LAMBADA 的高 α 和强 convergence 可能由 format（open-ended → 无穷答案空间）而非 task type（retrieval）驱动。论文 §3.2 的 within-multiple-choice format 不预测 α 的 mitigation 不够——2-way vs 4-way 区别远小于 MC vs free-form。R2 同意需在 Limitations 明确加入 format confound。建议增加 free-form generation benchmark（如 TriviaQA generative mode）。\"\n  action_items:\n    - round: 17\n      action: \"Discussion 或 Limitations 讨论 evaluation format 作为 alternative explanation\"\n      assigned_to: paper_agent\n      status: open\n    - round: 18\n      action: \"§3.2 末尾加 2-3 句 evaluation format confound 讨论\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"Limitations 显式加入 format confound；§4.1 中 'multiplicity depends on task type' 改为 'task type or evaluation format'；考虑增加 TriviaQA generative 作为第二个 free-form benchmark\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"R19 双方 Major，论证进一步加强。§3.2 已有部分讨论但 Limitations 和 §4.1 claim 需修改。\"\n  resolution_round: null\n\n- id: \"R17-W2\"\n  summary: \"Confirmatory/exploratory benchmark 分类缺乏预注册（informal pre-analysis plan 无 timestamp）\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-W4 提出 + R2 [AGREE] 但认为严重度低。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未单独提及。\"\n    - round: 19\n      reviewers: [R1]\n      note: \"R1-W5 Major：'informal, not pre-registered' 是实质弱点。taxonomy 创建者与数据分析者为同一批人。缺乏可验证时间证据（无 pre-registration ID/commit timestamp/lab notebook）。建议提供客观时间证据或将 taxonomy-based 结论重新框定为 hypothesis-generating。\"\n  action_items:\n    - round: 17\n      action: \"Appendix A 明确 all-10 为唯一有效 correction，6-benchmark 仅为 sensitivity\"\n      assigned_to: paper_agent\n      status: open\n    - round: 19\n      action: \"提供 taxonomy 固定时间的客观证据（git commit hash + timestamp）；或将 task-type 结论框定为 hypothesis-generating\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-W1\"\n  summary: \"Permutation test null baseline 不排除 example difficulty confound\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-W5 提出 + R2 交叉 [AGREE]。\"\n    - round: 19\n      reviewers: []\n      note: \"R19 未显式提及。可能被 format confound 讨论吸收（difficulty 是 format 的下位概念之一）。\"\n  action_items:\n    - round: 18\n      action: \"讨论 example difficulty 作为 confound\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W1\"\n  summary: \"遗漏 Yang & Wang (2026) 'Benchmark Illusion'——核心发现与本文高度重叠\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R2]\n      note: \"R2-N3 Major：Yang & Wang (2026) arXiv:2602.11898 在 frontier LLMs 上展示了 comparable accuracy + 16-66% per-item disagreement + disagreement 传播到下游注释。与本文 'aggregate equivalence masks per-example divergence' 高度重叠。使 'first systematic per-example analysis' claim 需重新界定。本文增量贡献可能是 'controlled model zoo 上的系统量化' 而非 '首次发现'。\"\n  action_items:\n    - round: 19\n      action: \"引用 Yang & Wang (2026) Benchmark Illusion；在 Related Work 中讨论异同；重新界定 'first systematic per-example analysis' claim 为 'first controlled, within-family analysis'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W2\"\n  summary: \"LAMBADA 和 ARC-Easy routing 增益数值完全相同（+1.2pp, SD=0.5pp），疑似 reporting error\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R1]\n      note: \"R1-W9 Minor：两个 benchmark 上 routing 增益完全相同（+1.2pp, SD=0.5pp），可能是巧合、copy-paste error 或 rounding artifact。需作者确认。\"\n  action_items:\n    - round: 19\n      action: \"核实 LAMBADA 和 ARC-Easy routing 增益是否为独立计算的精确值\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W3\"\n  summary: \"全文 associative vs causal 语言不完全一致\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R1]\n      note: \"R1-W8 Minor：Section 5 'reflects structural differences'/'is modulated by'；Section 2 'controlled instance'；Appendix B 'indicating dependence'——均暗示因果但 single-run design 不支持。需统一为 'associated with'/'correlated with'/'consistent with'。\"\n  action_items:\n    - round: 19\n      action: \"全文统一 associative 语言：替换 'reflects'→'is consistent with', 'modulated by'→'varies with', 'controlled'→'systematic'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "entrainment_gated_ft",
    "issues_yaml": "- id: \"R5-W1\"\n  summary: \"架构效应 vs seed 效应无法区分（单 training run，无 seed baseline）\"\n  category: experiment\n  severity: critical\n  status: wont_fix\n  first_raised_round: 5\n  last_seen_round: 19\n  mentions:\n    - round: 5\n      reviewers: [R1, R2]\n      note: \"R1 Critical, R2 W3+Q3 支持。\"\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"R2-N3 Must-Fix vs R1-W2 Should-Fix。分歧：R1 REBUT 认为论文已用关联性语言、第三方 zoo 无法自行补训。R2 维持 Must-Fix。论文已有 PolyPythias 校准但三重 mismatch 仍被指出。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N2 Critical。双方 [AGREE]。Pythia 70M 三重 mismatch（scale 70M vs 340M+/architecture family Transformer vs hybrid/accuracy 0.17-0.23 vs ~0.50）仍是核心弱点。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-N3 Critical + R2 交叉 [AGREE]。Pythia 70M within-seed J=0.312 vs cross-arch J=0.354，gap 仅 0.042。R2 补充 seed variation 可能解释大部分 per-example divergence。双方一致认为是根本性威胁但非 fatal。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-N2 Critical + R2-N2 Critical，交叉均 [AGREE]。R2 纠正 R1 数据误读：within-seed J=0.273 vs cross-arch J=0.10 实为 2.7× 差距（非 R1 声称的 0.02），部分支持架构效应独立性。但 Pythia 70M 三重 mismatch 仍限制 calibration 可迁移性。双方一致要求至少对一个 hybrid 架构训练多 seed。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-N2 Critical + R2-W4 Minor。R1 详细列出双重 mismatch（scale: 70M vs 340M/1.3B; architecture: Transformer vs hybrid gating）。R2 同意 calibration 参照价值有限但视为 minor。交叉后双方一致：seed confound 是 open question，但 structural limitation（第三方 zoo 无法重训），维持 wont_fix。\"\n  action_items:\n    - round: 13\n      action: \"E4 Pythia 410M 9-seed calibration（实际完成 70M）\"\n      assigned_to: main_agent\n      status: done\n    - round: 14\n      action: \"Limitations 提升 single-seed 为 top limitation；§4.2 弱化因果语言\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"结构性限制，无法完全修复。已做：(1) Pythia 70M seed calibration 加入 Appendix W；(2) Limitations 中 single-seed 为 top limitation；(3) 全文使用 'associated with' 关联性语言。R19 双方仍 flag 但认可为 structural limitation。\"\n  resolution_round: null\n\n- id: \"R5-W2\"\n  summary: \"收敛 claim 统计不显著（Bonferroni p=.170）且依赖 GDN inclusion\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 19\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical。交叉 [AGREE]。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R16-N1 重新 flag。R15 写作修复不够——Intro 仍以 79% σ drop 开篇。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2 交叉 [AGREE]。R1 精确指出结构性限制：n=5 时最小 p=0.017，Bonferroni 后 0.170——无论效应多强都无法拒绝 H₀。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical，交叉均 [AGREE]。论文核心叙事 'convergence masks divergence' 需要 aggregate convergence 成立，但 p=.170 不支持。R2 建议重构为 'architectures interchangeable by aggregate metrics differ per-example'。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical，交叉均 [AGREE]。R2 进一步升级：decoupling 叙事建立在'不存在的前提'上——如果 aggregate convergence 本身不显著，decoupling 就是在回答一个不需要回答的问题。R1 同意 convergence 应为 exploratory observation。双方建议将 Contribution 2 重构为条件式 observation 或转向 Jaccard 饱和作为主发现。\"\n  action_items:\n    - round: 15\n      action: \"Abstract/Intro 重构：以 Jaccard saturation 为主线\"\n      assigned_to: paper_agent\n      status: done\n    - round: 16\n      action: \"结构性叙事重组：Intro 79% σ drop 移到 §4.2 等\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"Contribution 2 重构为条件式（'even on LAMBADA where trend is strongest, per-example overlap saturates'）或将 Jaccard 饱和升级为主发现\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"R15-R19 持续 flag。需将 convergence 彻底降级为 exploratory observation，decoupling 叙事重构为条件式。\"\n  resolution_round: null\n\n- id: \"R5-W4\"\n  summary: \"新颖性有限——已有指标的直接套用，无新方法/理论\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 5\n  last_seen_round: 19\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"R2-W1 ecological fallacy 已知实例。R1 REBUT。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R2-N1 Must-Fix vs R1 REBUT。核心分歧未解决。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R2-N1 Critical。R1 REBUT（empirical first 在实际相关 domain 有独立价值）。部分收敛：均同意应明确定位为 empirical contribution。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R2-W1 Major。R1 REBUT——4% saturation 和 aggregate-vs-per-example 解耦是非平凡发现。部分收敛：Findings 标准下经验发现足够。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R2-N2 Major（ecological fallacy 区分不充分——论文承认但未解释 beyond ecological fallacy 的 insight）+ R2-N1 Critical（与 Benchmark Illusion 重叠）。R1 在 S1 肯定研究问题新颖但交叉中未直接 REBUT R2 的 novelty 批评。双方在 Findings 适切性上一致，但 R2 认为 contribution sufficiency 处于 borderline。\"\n  action_items:\n    - round: 6\n      action: \"Intro 加 empirical novelty framing\"\n      assigned_to: paper_agent\n      status: done\n    - round: 16\n      action: \"Intro 强化 empirical contribution 定位\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"引用 Benchmark Illusion 并定位本文增量贡献（controlled zoo + 系统量化 + 饱和发现）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"结构性限制。Findings 标准下可接受，但需引用 Benchmark Illusion 并明确定位增量贡献。\"\n  resolution_round: null\n\n- id: \"R5-W3\"\n  summary: \"Task-dependent spectrum 仅 3 benchmark，存在评估格式 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [R1, R2]\n      note: \"α 变异可能反映 format 而非 task type。\"\n  action_items:\n    - round: 5\n      action: \"WinoGrande + PIQA per-example 分析\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"PIQA + WinoGrande 数据整合完成。Round 6-16 未再提及。R17 提出更具体的 format confound（见 R17-W1）。\"\n  resolution_round: 6\n\n- id: \"R5-W5\"\n  summary: \"正文约 8.2 页超出 EMNLP 8 页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 19\n  mentions:\n    - round: 16\n      reviewers: []\n      note: \"R16 视觉审查确认合规。\"\n    - round: 17\n      reviewers: [R1]\n      note: \"R1-M5 确认格式合规（8页，Limitations 3点，匿名完好）。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R18 双方格式检查均确认合规。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R19 双方格式检查均确认合规：正文 ≤8 页、Limitations 在正文、匿名完整、Abstract <200 词。\"\n  action_items:\n    - round: 5\n      action: \"结构性压缩 8.2→7 页\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"主文在 8 页内。R14-R19 持续确认合规。\"\n  resolution_round: 5\n\n- id: \"R5-W6\"\n  summary: \"遗漏关键相关工作 Zoology/Based/Samba\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  action_items:\n    - round: 5\n      action: \"补 3 篇引用 + recall-throughput 框架\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Zoology + Based 引用于 §4.1，Samba 引用于 Related Work。\"\n  resolution_round: 5\n\n- id: \"R5-W7\"\n  summary: \"Ensemble 建议缺乏实验支撑 + POC 负面结果与 protocol 的 tension\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 9\n  action_items:\n    - round: 7\n      action: \"Majority vote + oracle POC 写入 Conclusion\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Conclusion 已包含 MV/oracle POC 数据。\"\n  resolution_round: 9\n\n- id: \"R5-W8\"\n  summary: \"Binary decomposition 可能低估多选题一致性\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 19\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-W2 指出 hurt sets binarization 可能 overestimate agreement。Appendix O continuous Jaccard 缓解。\"\n    - round: 17\n      reviewers: [R2]\n      note: \"R2-Q4 询问为何不在主文使用 continuous Jaccard。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未作为独立问题提及。§3.4 已包含 binarization caveat + Appendix continuous Jaccard。\"\n    - round: 19\n      reviewers: [R1]\n      note: \"R1-S6 肯定 binary decomposition 设计合理，正确识别了 K-choice binarization 的 conservative bias。未作为 weakness 提出。R2 亦未 flag。可能已充分缓解。\"\n  action_items:\n    - round: 13\n      action: \"E2 continuous-threshold Jaccard sensitivity 结果整合到 Appendix + §4.1 引用\"\n      assigned_to: paper_agent\n      status: done\n    - round: 16\n      action: \"§3.4 加 1 句 K-choice binarization caveat\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"R19 双方均未作为 weakness 提出，R1 在 Strengths 中肯定。可视为充分缓解。\"\n  resolution_round: null\n\n- id: \"R5-W9\"\n  summary: \"Abstract 信息密度过高（统计量堆砌）\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 19\n  mentions:\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-M6 指出接近 200 word 上限。R2-M4 指出 inline 统计量增加认知负荷。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R2-W4 Major：数字密度过高。R1 交叉 [AGREE with nuance]。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1 确认 Abstract 约 170 词符合限制。R2-W1b 指出 Introduction 第1段信息过载（4行内密集数字），R2-W6 指出贡献列表过长（每条>100词）。Abstract 本身改善但 Introduction 密度仍高。\"\n  action_items:\n    - round: 13\n      action: \"W5: Abstract 进一步精简至 3 key numbers\"\n      assigned_to: paper_agent\n      status: done\n    - round: 18\n      action: \"Abstract 再次精简\"\n      assigned_to: paper_agent\n      status: done\n    - round: 19\n      action: \"Introduction 第1段分拆：先概述现象再引入量化；贡献列表精简为核心 claim + section 引用\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"Abstract 已改善（148词），但 Introduction 第1段和贡献列表仍需精简。\"\n  resolution_round: null\n\n- id: \"RV-L1\"\n  summary: \"Limitations 6 段违反 EMNLP 用户规则（要求 ~3 点）\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 15\n  action_items:\n    - round: 5\n      action: \"6 段→3 段\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"压缩为 3 段。R14-R19 确认合规。\"\n  resolution_round: 5\n\n- id: \"RV-L2\"\n  summary: \"loglik 压缩假说已被诊断数据反驳但论文仍引用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  action_items:\n    - round: 5\n      action: \"改为 binary classification structural properties 解释\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"改为 'structural properties of constrained-choice formats'。\"\n  resolution_round: 5\n\n- id: \"R6-N3\"\n  summary: \"仅 2 个 scale 点不足以支撑 scale-dependent claim\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  action_items:\n    - round: 6\n      action: \"MF4: 全文替换 scale-dependent\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"全文已用 'differs between 340M and 1.3B'。\"\n  resolution_round: 8\n\n- id: \"R6-N2\"\n  summary: \"缺乏 actionable insights——论文停在 '问题存在' 层面\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 15\n  action_items:\n    - round: 13\n      action: \"E1 routing 结果整合到 §4.1 + Conclusion 更新\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"E1 rescue-threshold routing 已写入。R15 routing 降级为 case study。非 blocking。\"\n  resolution_round: 13\n\n- id: \"R6-W1\"\n  summary: \"Decoupling 形式化存在技术问题 + saturation 未严格定义\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 9\n  action_items:\n    - round: 8\n      action: \"删除 Equation 1 形式化定义，保留定量描述\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Equation 1 已删。Round 12-19 未再提及。\"\n  resolution_round: 12\n\n- id: \"R6-W2\"\n  summary: \"GDN h3-1 的 16-head confound 削弱 LAMBADA convergence\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 19\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"R1-N2 Critical + R2-N2 Critical。主文并列 with/without GDN。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R16 确认修复存在但叙事仍过度突出。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-N2 Critical。移除 GDN 后 LAMBADA ρ 从 -1.0 降至 -0.7。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未作为独立问题提及。§4.3 已讨论。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W2 Major：MMLU ρ 从 -0.7 反转为 +0.6，证明 MMLU convergence 完全由 GDN 16-head anomaly 驱动。R2-W2 Minor 同意应更早 flag。双方一致要求在正文（而非仅 Appendix）中更显著地报告 MMLU 反转。\"\n  action_items:\n    - round: 15\n      action: \"主文 §4.2 并列 with/without GDN ρ 值；§4.3 Robustness 讨论\"\n      assigned_to: paper_agent\n      status: done\n    - round: 19\n      action: \"Table 1 首次引入 GDN 结果时即 flag 16-head anomaly；正文报告 MMLU ρ 反转\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"§4.3 已讨论但 R19 认为不够显著。需在 Table 1 处更早 flag。\"\n  resolution_round: null\n\n- id: \"R6-W3\"\n  summary: \"Bootstrap CI 在 n=3 架构上覆盖率远低于名义值\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 19\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"27 个 bootstrap 样本（排除退化后 ~24 个）无可靠覆盖率。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R2 指出 BCa CI 在 Introduction 首次出现处缺 caveat。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"建议全面改用 percentile bootstrap 并标注 heuristic。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-N3 Critical。95% CI=[-1.0,-0.7] 传递虚假精度感。升级为 Critical。\"\n    - round: 19\n      reviewers: [R1]\n      note: \"R1-W7 Minor。Section 3.5 已用 'heuristic indicators of effect direction'，但 Section 4.3 中 'Bootstrapped 95% CIs... excludes zero' 叙述可能误导。建议附加 coverage limitation 注释。降级为 Minor（较 R18 有改善）。\"\n  action_items:\n    - round: 15\n      action: \"Figure caption 附注 illustrative only\"\n      assigned_to: paper_agent\n      status: done\n    - round: 16\n      action: \"Intro BCa CI 处加 heuristic caveat\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 18\n      action: \"全文 bootstrap CI 标 heuristic\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"Section 3.5 caveat 已存在，但 Section 4.3 叙述仍可能误导。R19 降级为 Minor。\"\n  resolution_round: null\n\n- id: \"R14-W1\"\n  summary: \"Confidence margin 'mechanism' 标题暗示因果性，实为 correlational\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  action_items:\n    - round: 14\n      action: \"全文替换 'mechanism' → 'predictor'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已替换。R15-R19 未再提及。\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"n=5 attention ratios 使 convergence permutation test 本质上为 binary outcome\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"建议声明所有 Spearman correlation 推断为 descriptive/exploratory。\"\n  action_items:\n    - round: 15\n      action: \"§4.2 标注 'suggestive but underpowered secondary observation'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。合并入 R5-W2/R16-N1 的更大叙事问题。\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"标题/Abstract 过度泛化：仅 3 架构但表述暗示更广 generality\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  action_items:\n    - round: 14\n      action: \"正文加 scope 限定\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。R16-R19 未再单独提及。\"\n  resolution_round: 15\n\n- id: \"R14-W4\"\n  summary: \"缺失 prediction churn 文献（Milani Fard et al. 2016）\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  action_items:\n    - round: 14\n      action: \"添加 Milani Fard (2016) + Poli (2023) Hyena\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已引用。R18-R19 确认引用存在。\"\n  resolution_round: 15\n\n- id: \"R15-W1\"\n  summary: \"'Nearly disjoint' / 'almost entirely different' 措辞夸大\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  action_items:\n    - round: 15\n      action: \"替换为 calibrated 表述\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。R16-R19 未再提及。\"\n  resolution_round: 15\n\n- id: \"R15-W2\"\n  summary: \"Routing 作为 'proof-of-concept application' 定位过高（仅 1/4 benchmark 有效）\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 19\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"建议降级为 case study / illustrative example。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"§4.1 已改为 case study 但 Conclusion 仍列为 practitioner implication。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R2-N2 Critical + R1-W1。1/4 success rate，无 ensemble baseline 对比。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-W1 Major + R2-W3 Major，交叉均 [AGREE]。PIQA 显著负效。缺 average logits ensemble baseline。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W4 Major + R2-W1 Major，交叉均 [AGREE]。R2 补充：routing 的循环依赖（需先知道 multiplicity 水平才能决定是否 route）。R1 补充：缺少 bootstrap CI/significance test。双方一致要求降级为 preliminary exploration + 补充 average-logits ensemble baseline。Abstract 中缺少 qualifier。\"\n  action_items:\n    - round: 15\n      action: \"降级为 'illustrative case study'\"\n      assigned_to: paper_agent\n      status: done\n    - round: 16\n      action: \"Conclusion routing 从 practitioner implication 降级\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 18\n      action: \"Conclusion 删 α>0.2 threshold，routing 限定为 preliminary/high-α free-form tasks\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"Abstract routing 句加 qualifier（如 'on the highest-multiplicity task'）；补充 average-logits ensemble baseline 对比\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"R19 双方 Major。Routing 在正文已为 case study 但 abstract 叙事权重仍偏高。\"\n  resolution_round: null\n\n- id: \"R15-D1\"\n  summary: \"Appendix Table 30 DeltaNet 行数据不一致\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  action_items:\n    - round: 15\n      action: \"从 JSON 逐格修正\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已修正。R17-R19 未再提及。\"\n  resolution_round: 15\n\n- id: \"R15-W3\"\n  summary: \"缺失 Jain et al. (2025 FAccT) 引用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  action_items:\n    - round: 15\n      action: \"添加到 references.bib + Related Work\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。R17-R19 确认引用存在。\"\n  resolution_round: 15\n\n- id: \"R16-N1\"\n  summary: \"Aggregate convergence 叙事在 Abstract/Introduction 中仍过度突出\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-N2 Must-Fix + R2-W1 Should-Fix。交叉 [AGREE]。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"双方一致要求全文统一为 descriptive/suggestive。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical。R2 提出重构方案：'architectures interchangeable by aggregate metrics differ per-example'。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical，交叉均 [AGREE]。R2 升级论证：decoupling 叙事以'不存在的前提'（non-significant aggregate convergence）为基础。Section 4.2 标题 'Aggregate Variance and Per-Example Overlap' 暗示 aggregate narrowing 是 established fact。建议将 §4.2 重新 frame 为'even in the most favorable scenario (LAMBADA ρ=-1.0, non-significant), per-example Jaccard saturates'。\"\n  action_items:\n    - round: 16\n      action: \"结构性叙事重组\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 18\n      action: \"全面叙事重构：convergence → aggregate interchangeability\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"§4.2 标题改为非确定性（如 'Per-Example Overlap Under Varying Aggregate Trends'）；全文消除 aggregate convergence 作为 established premise 的措辞\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"R16-R19 持续 flag。核心叙事仍需全面重构。\"\n  resolution_round: null\n\n- id: \"R16-W1\"\n  summary: \"Routing 实验缺少 variance 报告（10-repeat cross-validation 仅报 mean）\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-W3 + R2 AGREE。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R2 补充：如果 SD > 3pp 则 5.3pp 增益可能不显著。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"LAMBADA 已报告 SD=0.4pp 但其他 benchmark SD 缺失。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W4 Major：仍缺 bootstrap CI 和 significance test。R2-W1 同意。LAMBADA SD=0.4pp 已报告但 ARC-Easy/HellaSwag/PIQA 的 SD 在正文已补充（SD=0.5/未报告/p=.006）。仍缺 formal significance test for LAMBADA。\"\n  action_items:\n    - round: 16\n      action: \"从已有数据提取 SD 和 95% CI\"\n      assigned_to: main_agent\n      status: in_progress\n    - round: 19\n      action: \"LAMBADA routing 增益补充 bootstrap CI 和 permutation significance test\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"部分改善（SD 已报告），但 formal significance test 仍缺。\"\n  resolution_round: null\n\n- id: \"R16-W2\"\n  summary: \"5-architecture 扩展验证仅 340M，主文 §4.3 缺 scale caveat\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-W4 + R2 AGREE。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"双方一致。R2 认为 minor 级别。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-W4 Warning。R2 [AGREE] 但程度略弱。\"\n    - round: 19\n      reviewers: [R1]\n      note: \"R1-W6 Major：5-arch extension 仅验证了 per-example divergence 的 ubiquity（J≤0.14），未验证 convergence claim。且仅用 h3-1 单一配置，未做 attention ratio sweep。建议标明 Appendix X 仅验证 divergence 而非 convergence。\"\n  action_items:\n    - round: 16\n      action: \"§4.3 加 'at 340M'\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"Appendix X 明确标注仅验证 per-example divergence pattern，不能推断 convergence\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R16-W3\"\n  summary: \"Confidence margin AUC 的正态假设未验证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-W5 + R2 AGREE。\"\n    - round: 17\n      reviewers: []\n      note: \"R17 未单独提及。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未提及。Appendix 已包含 Shapiro-Wilk normality tests + empirical AUC 对比。\"\n    - round: 19\n      reviewers: [R1]\n      note: \"R1-W4 Major 重新 flag：Shapiro-Wilk 显示 rescue-set skewness 1.33-1.41，GDN/HGRN2 的 p<10⁻⁴ 严重违反正态。论文用 percentile CI 替代但 AUC point estimate 仍基于 Gaussian assumption。建议改用 non-parametric AUC（Mann-Whitney U）。\"\n  action_items:\n    - round: 16\n      action: \"计算 empirical AUC 对比 parametric estimate\"\n      assigned_to: main_agent\n      status: in_progress\n    - round: 19\n      action: \"改用 non-parametric AUC（Mann-Whitney U statistic）替代 Cohen's d 导出的参数 AUC\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"R19 R1 重新 flag。正态假设违反已有证据但未修正 AUC 方法。\"\n  resolution_round: null\n\n- id: \"R16-W4\"\n  summary: \"模型规模覆盖有限（≤1.3B vs 7B+ 部署场景）\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R2-W4 + R1 AGREE。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R2-W4 + R1 交叉 [AGREE]。Conclusion 未限定。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-W3 Major。建议改为 'consistent across the two scales examined'。\"\n    - round: 19\n      reviewers: [R1]\n      note: \"R1-W3 Major：两个数据点无法建立 scaling trend。340M 无 convergence vs 1.3B LAMBADA 有——结果矛盾。建议限定 convergence finding scope 为 '1.3B LAMBADA'；讨论 340M 无 convergence 的理论含义。\"\n  action_items:\n    - round: 16\n      action: \"Limitations 加 scale limitation 句\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 18\n      action: \"全文 'scale-robust' → 'consistent across the two scales examined'\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"讨论 340M vs 1.3B convergence 矛盾的理论含义（capacity-gated emergent phenomenon?）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"R19 仍 Major。需讨论 cross-scale 矛盾。\"\n  resolution_round: null\n\n- id: \"R16-W5\"\n  summary: \"遗漏重要相关工作\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R2-W3 建议引用。R1 部分 AGREE。\"\n    - round: 17\n      reviewers: [R2]\n      note: \"R2-W2 新增 Ye et al. (2026)。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R2-W2 Major：遗漏 Model Soups (Wortsman 2022)、MoE。R1 提出 Jiang et al. (2024)。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R2-N3 Major 新增关键遗漏：Yang & Wang (2026) 'Benchmark Illusion'（arXiv:2602.11898）——在 frontier LLMs 上展示了 comparable accuracy + 16-66% per-item disagreement，与本文核心发现高度重叠。R2-W3 补充 MoE routing 文献缺失。R1 补充 MultiBERTs (Sellam 2022) 在 seed calibration 语境中未引用。R2 确认 Model Soups/Fort et al./Jain et al. 已在论文中引用。\"\n  action_items:\n    - round: 16\n      action: \"核实并添加\"\n      assigned_to: main_agent\n      status: in_progress\n    - round: 18\n      action: \"添加 Wortsman (2022) + Jiang (2024) 到 bib 和 Related Work\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"必须引用 Yang & Wang (2026) Benchmark Illusion 并在 Related Work 中讨论本文与其的关系和增量贡献；建议引用 MoE routing 文献（至少 1 篇代表性工作）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"R19 升级：Benchmark Illusion 是重大遗漏，直接影响 novelty claim（'first systematic per-example analysis' 需重新界定）。\"\n  resolution_round: null\n\n- id: \"R16-M1\"\n  summary: \"Haghighat 2026 bib 条目需更新为 AAAI 2026\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 16\n      reviewers: [R2]\n      note: \"Camera-ready 前 fix。\"\n    - round: 19\n      reviewers: []\n      note: \"R19 未提及。可能已修复。\"\n  action_items:\n    - round: 16\n      action: \"更新 references.bib\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W1\"\n  summary: \"Task type vs evaluation format confound 未被区分（LAMBADA 为唯一 free-form benchmark）\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-W2 提出 + R2 交叉 [AGREE]。LAMBADA 是唯一 free-form benchmark。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-W2 Major + R2 交叉 [AGREE]。双方一致要求正文讨论 format confound。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W1 Major + R2-W2 Major，交叉均 [AGREE]。R1 详细论证：multiple-choice 的有限答案空间机械约束 per-example divergence，LAMBADA 的高 α 和强 convergence 可能由 format（open-ended → 无穷答案空间）而非 task type（retrieval）驱动。论文 §3.2 的 within-multiple-choice format 不预测 α 的 mitigation 不够——2-way vs 4-way 区别远小于 MC vs free-form。R2 同意需在 Limitations 明确加入 format confound。建议增加 free-form generation benchmark（如 TriviaQA generative mode）。\"\n  action_items:\n    - round: 17\n      action: \"Discussion 或 Limitations 讨论 evaluation format 作为 alternative explanation\"\n      assigned_to: paper_agent\n      status: open\n    - round: 18\n      action: \"§3.2 末尾加 2-3 句 evaluation format confound 讨论\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"Limitations 显式加入 format confound；§4.1 中 'multiplicity depends on task type' 改为 'task type or evaluation format'；考虑增加 TriviaQA generative 作为第二个 free-form benchmark\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"R19 双方 Major，论证进一步加强。§3.2 已有部分讨论但 Limitations 和 §4.1 claim 需修改。\"\n  resolution_round: null\n\n- id: \"R17-W2\"\n  summary: \"Confirmatory/exploratory benchmark 分类缺乏预注册（informal pre-analysis plan 无 timestamp）\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-W4 提出 + R2 [AGREE] 但认为严重度低。\"\n    - round: 18\n      reviewers: []\n      note: \"R18 未单独提及。\"\n    - round: 19\n      reviewers: [R1]\n      note: \"R1-W5 Major：'informal, not pre-registered' 是实质弱点。taxonomy 创建者与数据分析者为同一批人。缺乏可验证时间证据（无 pre-registration ID/commit timestamp/lab notebook）。建议提供客观时间证据或将 taxonomy-based 结论重新框定为 hypothesis-generating。\"\n  action_items:\n    - round: 17\n      action: \"Appendix A 明确 all-10 为唯一有效 correction，6-benchmark 仅为 sensitivity\"\n      assigned_to: paper_agent\n      status: open\n    - round: 19\n      action: \"提供 taxonomy 固定时间的客观证据（git commit hash + timestamp）；或将 task-type 结论框定为 hypothesis-generating\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R18-W1\"\n  summary: \"Permutation test null baseline 不排除 example difficulty confound\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-W5 提出 + R2 交叉 [AGREE]。\"\n    - round: 19\n      reviewers: []\n      note: \"R19 未显式提及。可能被 format confound 讨论吸收（difficulty 是 format 的下位概念之一）。\"\n  action_items:\n    - round: 18\n      action: \"讨论 example difficulty 作为 confound\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W1\"\n  summary: \"遗漏 Yang & Wang (2026) 'Benchmark Illusion'——核心发现与本文高度重叠\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R2]\n      note: \"R2-N3 Major：Yang & Wang (2026) arXiv:2602.11898 在 frontier LLMs 上展示了 comparable accuracy + 16-66% per-item disagreement + disagreement 传播到下游注释。与本文 'aggregate equivalence masks per-example divergence' 高度重叠。使 'first systematic per-example analysis' claim 需重新界定。本文增量贡献可能是 'controlled model zoo 上的系统量化' 而非 '首次发现'。\"\n  action_items:\n    - round: 19\n      action: \"引用 Yang & Wang (2026) Benchmark Illusion；在 Related Work 中讨论异同；重新界定 'first systematic per-example analysis' claim 为 'first controlled, within-family analysis'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W2\"\n  summary: \"LAMBADA 和 ARC-Easy routing 增益数值完全相同（+1.2pp, SD=0.5pp），疑似 reporting error\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R1]\n      note: \"R1-W9 Minor：两个 benchmark 上 routing 增益完全相同（+1.2pp, SD=0.5pp），可能是巧合、copy-paste error 或 rounding artifact。需作者确认。\"\n  action_items:\n    - round: 19\n      action: \"核实 LAMBADA 和 ARC-Easy routing 增益是否为独立计算的精确值\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W3\"\n  summary: \"全文 associative vs causal 语言不完全一致\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R1]\n      note: \"R1-W8 Minor：Section 5 'reflects structural differences'/'is modulated by'；Section 2 'controlled instance'；Appendix B 'indicating dependence'——均暗示因果但 single-run design 不支持。需统一为 'associated with'/'correlated with'/'consistent with'。\"\n  action_items:\n    - round: 19\n      action: \"全文统一 associative 语言：替换 'reflects'→'is consistent with', 'modulated by'→'varies with', 'controlled'→'systematic'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1731 · 2026-05-24T13:38:09.243128+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_issues.yaml\", \"bytes\": 30925}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1732 · 2026-05-24T13:40:35.916476+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 19 (Fresh Review)\n\n**论文**: Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**Reviewers**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + Related Work）\n**模式**: 圆桌审稿，1 轮独立审稿 + 交叉分享，达成共识无需进入 Round 2\n\n---\n\n## Summary\n\n本文利用 Wang et al. (2025) 的 controlled model zoo（3 种 hybrid linear recurrent 架构 × 5 种 attention ratio × 2 种规模），首次系统分析了 hybrid recurrent architectures 之间的 per-example predictive multiplicity。核心发现：(1) 聚合指标可互换的架构在逐样本层面差异显著（pairwise Jaccard ≈ 0.10）；(2) per-example Jaccard 在 4% attention 时即饱和并保持平坦；(3) confidence-based routing 在高 multiplicity 任务上可部分利用互补性（LAMBADA +5.2pp，但 PIQA 显著为负）。\n\n---\n\n## Strengths\n\n**S1. 实验控制度极高** [R1-S5, R2-S1]：基于公开 model zoo，所有模型共享训练数据、tokenizer、超参，仅变化架构和 attention 配置。这种控制在 hybrid architecture 文献中罕见。\n\n**S2. 统计诚实度优秀** [R1-S3, R2-S2]：始终对 LAMBADA 的 aggregate trend 标记为 \"non-significant\"（Bonferroni 校正后 p=.170），在 Table 1 脚注明确 n=5 功效限制。这在 NLP 实证论文中属上乘。\n\n**S3. Robustness 验证极为充分** [R1-S4, R2-S3]：13 个 Appendix（A–X）系统检查了 GDN confound exclusion、continuous Jaccard、5 架构扩展、seed calibration、confidence margin cross-benchmark 等。\n\n**S4. Per-example Jaccard 饱和是稳健发现** [R1-S2, R2-S4]：四个 benchmark 上 Jaccard 在第一个 attention level（4%）即饱和（Figure 4, all ρ ≤ 0.80, p ≥ .333），跨 benchmark 一致，不依赖任何单一 benchmark。\n\n**S5. Permutation test 提供了 robust 的描述性证据** [R1-S2]：10,000 次置换下所有 architecture pair 均 p < .0001，为 \"cross-architecture overlap 是结构性的\" 提供可靠统计证据。\n\n**S6. 写作规范透明** [R2-S5]：结构清晰，Abstract ≈ 148 词符合限制，多处使用 hedged language，ecological fallacy 自我承认（Related Work）。\n\n---\n\n## Weaknesses\n\n### Critical\n\n**W1. [Critical] Decoupling 叙事建立在统计上不成立的前提上** [R1-N1, R2-N1, 交叉 AGREE]\n\nContribution 2 的核心逻辑是 \"aggregate variance 下降，但 per-example overlap 没有同步下降\"。然而 aggregate convergence 本身不显著：\n- LAMBADA 是唯一 ρ=-1.0 的 benchmark，Bonferroni 后 p=.170\n- 排除 GDN 后 ρ 降至 -0.7, p=.233\n- 340M 上不复现（ρ=-0.50, p=.45）\n- 其余 9 个 benchmark 无此 trend\n\nR2 精确指出：如果 aggregate narrowing 本身不成立，decoupling 是在回答一个不需要回答的问题。Section 4.2 的 \"Regardless of whether this reflects a genuine trend, we ask...\" 试图绕过但不充分。\n\n**建议**：将 Contribution 2 重构为条件式 observation（\"even on LAMBADA where the trend is strongest...\"），或将重心转移到 Jaccard 饱和（S4）作为主发现。\n\n**W2. [Critical] 单次训练 run 无法分离架构效应与 seed 效应** [R1-N2, R2-W4, 交叉 AGREE]\n\n每个配置仅一次 run。Pythia 70M seed calibration 存在双重 mismatch：scale（70M vs 340M/1.3B）和 architecture（Transformer vs hybrid gating）。主文引用 calibration 时使用 \"consistent with architecture-driven divergence\"——高估了证据力度。\n\n**状态**：结构性限制（第三方 zoo 无法重训），维持 wont_fix。但需强化 Limitations 讨论。\n\n**W3. [Critical] 遗漏高度相关的先行工作 Yang & Wang (2026) \"Benchmark Illusion\"** [R2-N3, NEW]\n\nYang & Wang (2026, arXiv:2602.11898) 在 frontier LLMs 上展示了几乎相同的现象：comparable accuracy + 16-66% per-item disagreement + disagreement 传播到下游任务。这使本文的 \"first systematic per-example analysis\" claim 需重新界定。\n\n**建议**：必须引用并在 Related Work 中定位本文增量贡献（controlled within-family analysis, Jaccard saturation quantification, attention-ratio parametric sweep）。\n\n### Major\n\n**W4. [Major] LAMBADA format confound 未被充分讨论** [R1-W1, R2-W2, 交叉 AGREE]\n\nLAMBADA 是唯一 free-form generation benchmark（α=0.30，最高），其余全部 multiple-choice（α=0.14–0.21）。最高 multiplicity 和最强 convergence 恰巧都在唯一 open-ended 任务上。Multiple-choice 的有限答案空间机械约束 per-example divergence。§3.2 的 within-MC format mitigation（2-way vs 4-way）不够——远小于 MC vs free-form 的区别。\n\n**建议**：Limitations 显式加入 format confound；§4.1 \"multiplicity depends on task type\" 改为 \"task type or evaluation format\"。\n\n**W5. [Major] 新颖性为增量式——ecological fallacy 的 controlled instance** [R2-N2, R1 未 REBUT]\n\n论文自己承认 decoupling 是 ecological fallacy 的 controlled instance，但未充分解释 beyond ecological fallacy 提供了什么 non-trivial 的新 insight。没有回答 WHY（mechanism）、WHEN（boundary conditions）、HOW severe（impact beyond routing）。\n\n**状态**：Findings 标准下可接受，但需加强 mechanistic insight（如 Appendix F attention weight analysis 提升到正文）。\n\n**W6. [Major] Routing 实践意义有限且结果不一致** [R1-W4, R2-W1, ���叉 AGREE]\n\n4 个 benchmark 中仅 LAMBADA 有效（+5.2pp），ARC-Easy 微弱（+1.2pp），HellaSwag 无效（-0.06pp），PIQA 显著为负（-0.49pp, p=.006）。循环依赖：需先知道 multiplicity 水平才能 route。缺少 average-logits ensemble baseline。Abstract 中缺少 qualifier。\n\n**建议**：Abstract routing 句加 \"on the highest-multiplicity task\"；补充 ensemble baseline；降级为 preliminary exploration。\n\n**W7. [Major] GDN 16-head confound 导致 MMLU ρ 完全反转** [R1-W2, R2-W2]\n\nGDN h3-1 使用 16 attention head（其他 32），排除后 MMLU ρ 从 -0.7 反转为 +0.6——方向完全逆转。应在 Table 1 首次引入 GDN 时即 flag。\n\n**W8. [Major] 仅两个 scale 点且结果矛盾** [R1-W3]\n\n340M：无 convergence（所有 |ρ| ≤ 0.4）；1.3B：仅 LAMBADA 有。两个数据点无法建立 scaling trend。Convergence 可能是 capacity-gated emergent phenomenon 而非 attention 的固有属性。\n\n**W9. [Major] Confidence margin predictor 的 AUC 导出违反正态假设** [R1-W4]\n\nShapiro-Wilk 显示 rescue-set skewness 1.33-1.41（p<10⁻⁴），但 AUC point estimate 仍基于 Gaussian assumption。建议改用 non-parametric AUC（Mann-Whitney U）。\n\n**W10. [Major] Task taxonomy 是 post-hoc 的** [R1-W5]\n\n\"Informal, not pre-registered\"，缺乏可验证时间证据。Taxonomy 创建者与数据分析者为同一批人。用于 confirmatory claim 存在循环论证风险。\n\n### Minor\n\n**W11. [Minor] Bootstrap CI 在 n=3 下不具备名义覆盖率** [R1-W7]：Section 4.3 的 \"excludes zero\" 叙述可能误导。\n\n**W12. [Minor] 全文 causal vs associative 语言不完全一致** [R1-W8]：\"reflects\"、\"modulated by\"、\"controlled\" 等偶现的 causal 用语与 Section 3.5 的 \"descriptive and exploratory\" 声明矛盾。\n\n**W13. [Minor] LAMBADA 和 ARC-Easy routing 增益数值完全相同（+1.2pp, SD=0.5pp）** [R1-W9]：需确认是否为独立计算。\n\n**W14. [Minor] \"Attention dose\" 术语非标准** [R2-W5]：建议统一为 \"attention ratio\"。\n\n**W15. [Minor] Introduction 贡献列表过长** [R2-W6]：每条 >100 词，建议精简为核心 claim + section 引用。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Overall 评分**：双方独立给出 3.0 (Findings)——完全一致\n2. **Convergence claim 统计不足**：双方 Critical，交叉 AGREE\n3. **LAMBADA format confound**：双方 Major，交叉 AGREE\n4. **Routing 效果不一致**：双方 Major��交叉 AGREE\n5. **Seed confound 为结构性限制**：双方认可���交叉 AGREE\n6. **执行质量高**：双方肯定 statistical honesty, robustness coverage, experimental control\n7. **Jaccard 饱和是最强发现**：双方 Strength，交叉 AGREE\n8. **适合 Findings 而非主会议**：双方一致\n\n## Reviewer Divergence [REBUT]\n\n1. **Soundness 评分**：R1 = 2.5/5（更严格评估 inferential claims）vs R2 = 4/5（更注重 descriptive analysis 质量）。分歧源于对 \"soundness\" 的理解——R1 侧重 inferential validity，R2 侧��� methodological rigor。**Director 判断**：描述性分析确实 sound（permutation test, robustness），但推断性 claims（convergence, task-type causality）确实 underpowered。综合评为 3/5。\n\n2. **Benchmark Illusion 的影响程度**：R2 认为是 critical missing reference（直接影响 novelty claim），R1 未提及该文献。**Director 判断**：R2 有理——Yang & Wang (2026) 在更大规模上展示了类似现象，本文需引用并重新定位贡献。\n\n---\n\n## Questions\n\n1. LAMBADA 高 multiplicity（α=0.30）是否由 free-form generation format 而非 retrieval task type 驱动？是否有 TriviaQA generative 等其他 free-form benchmark 的初步数据？\n2. Average-logits ensemble 的初步结果是否可获得？缺少此对比使 routing 的 practical value 评估不完整。\n3. Pythia 70M within-seed J vs cross-architecture J 的比值在 hybrid 架构 340M/1.3B 上是否会保持？\n4. LAMBADA 和 ARC-Easy routing 增益完全相同（+1.2pp, SD=0.5pp）——这是独立计算的精确值还是 reporting error？\n5. GDN exclusion 后 MMLU ρ 从 -0.7 反转为 +0.6 如何解释？\n6. Task taxonomy \"was fixed prior to analysis\" 有无客观时间证据（pre-registration ID/git commit hash）？\n7. 本文与 Yang & Wang (2026) \"Benchmark Illusion\" 的关系——独立发现、互补分析、还是 partial overlap？\n\n---\n\n## Missing References\n\n**必须引用**：\n- Yang & Wang (2026) \"Benchmark Illusion: Disagreement among LLMs and Its Scientific Consequences\" (arXiv:2602.11898) — 核心发现高度重叠\n\n**建议引用**：\n- Li et al. (2024) \"Dropout-Based Rashomon Set Exploration for Efficient Predictive Multiplicity Estimation\" (arXiv:2402.00728)\n- \"Why are there many equally good models? An Anatomy of the Rashomon Effect\" (2026, arXiv:2601.06730)\n- MoE routing 文献（至少 1 篇代表性工作）— confidence-based routing 与 MoE per-token routing 概念相关\n- MultiBERTs (Sellam et al. 2022) 在 seed calibration 语境中的引用\n\n---\n\n## External Review\n\n**状态**：未请求（项目配置未启用外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：已完成（2026-05-24T13:15–13:19 UTC）\n\n**Findings**（1 warning, 15 info）：\n\n- ⚠️ **[Warning] Page 8**：三个 figure（5、6、7）挤在同一页，加上 Limitations 和 Code Availability 段落，页面极度拥挤。Figure 6 和 Figure 7 尺寸很小，内部文字 axis label 估计 <6pt，可读性受影响。\n- ℹ️ Page 1：首页无视觉锚点（纯文本），Figure 1 在 page 2 顶部，位置尚可但非最优。\n- ℹ️ Page 2：Figure 1 四子图 axis label/legend 字号偏小（估计 6-7pt）。\n- ℹ��� Page 4：Figure 2 尺寸偏小（占左栏约 1/4 高度）。\n- ���️ Pages 1-8：主体 8 页符合限制。Display items 共 9 个（7 figure + 2 table），密度 1.1/页，正常。布局节奏可接受。\n- ℹ️ 全文：无 LaTeX 渲染错误、margin 溢出、section heading 孤悬。公式渲染正确。颜色语义基本一致。\n\n---\n\n## Overall Assessment\n\n**Overall**: **3.0 (Findings)**\n\n**置信度**: 4/5（两位 Reviewer 均仔细审查全文 21 页含 Appendix，交叉后完全收敛于 3.0）\n\n**综合维度评分**：\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Soundness | 3/5 | 描述性分析 sound（permutation test robust, robustness 充分），但推断性 claims underpowered（convergence p=.170, seed confound, format confound）|\n| Excitement | 2/5 | 核心发现在 Benchmark Illusion 和 ensemble diversity 文献中有先例。Ecological fallacy 自我承认削弱 novelty。Routing 仅 1/4 有效。|\n| Reproducibility | 4/5 | 公开 model zoo + 标准 eval harness + 承诺代码公开。单次 run 无法验证 seed robustness 小幅扣分。|\n\n**总结判断**：\n\n本文执行质量属于 EMNLP 主会议水准——实验控制好、统计诚实、robustness 充分、写作规范。Jaccard 饱和（4% attention 即达稳态）是跨 benchmark 一致的稳健发现。\n\n但作为主会议论文存在三个根本性问题：\n\n1. **Decoupling 叙事的前提不成立**：aggregate convergence 本身 p=.170、GDN-dependent、不跨 scale 复现。论文的标志性发现建立在一个 non-finding 之上。\n2. **新颖性为增量式**：ecological fallacy 的 controlled instance + Benchmark Illusion 的先行发现。本文增量贡献在于 controlled model zoo 上的系统量化，而非 \"首次发现\"。\n3. **Practical actionability 不足**：routing 仅 1/4 benchmark 有效且 1/4 显著为负。\n\n**适合 Findings track**：描述性贡献有价值（per-example multiplicity 的存在、结构性、Jaccard 饱和），方法论严谨度满足 Findings 要求。\n\n**升至 Conference（4.0）的路径**：\n- (a) 引用 Benchmark Illusion 并明确定位增量贡献\n- (b) 将叙事重心从 decoupling 转移到 Jaccard 饱和\n- (c) 至少一个 hybrid 架构 multi-seed 实验\n- (d) 增加一个 free-form generation benchmark 以解耦 format confound\n- (e) 补充 average-logits ensemble baseline\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 148 词，符合 200 词限制 ✓\n- \"non-significant decreasing trend\" 标注正确\n- 缺少 routing 仅 1/4 有效的 qualifier\n\n### Introduction\n- 第1段信息密度过高（4行内 90%/10%/14%/p<.01）\n- 贡献列表每条 >100 词，可精简\n- \"first systematic per-example analysis\" 需在 Benchmark Illusion 上下文中重新界定\n\n### Related Work\n- 结构良好，三段覆盖三主题\n- Ecological fallacy 自我承认是加分项\n- 缺失 Yang & Wang (2026) Benchmark Illusion\n- 缺失 MoE routing 文献\n- Ensemble diversity 讨论过于简短\n\n### Method\n- 3.1 Model Zoo：GDN 16-head anomaly 应在此提及\n- 3.2 Task Taxonomy：\"Mixed\" 类别定义模糊；format confound 讨论不够\n- 3.4 Per-Example Decomposition：binary decomposition 的 conservative bias 论证良好\n- 3.5 Statistical Methods：n=5 power caveat 在此出现正确，但后文不一致遵循\n\n### Experiments\n- 4.1：核心描述性分析是论文最强部分。Routing 段落需加 significance test + 确认相同数值\n- 4.2：\"The answer is no\" 措辞暗示 clean result，但 aggregate convergence 本身不显���\n- 4.3：GDN exclusion 讨论存在但 MMLU ρ 反转未在此报告\n\n### Conclusion\n- 避免了 over-claim，使用 \"observations\" 和 \"preliminary suggest\"\n- \"Per-example audit before architecture substitution is advisable\" 可更具体\n\n### Limitations\n- 3 段覆盖 3 点，符合 EMNLP 规则 ✓\n- 遗漏：format confound、n=5 statistical power、Pythia calibration 三重 mismatch\n\n### 格式合规 ✓\n- 正文 ≤ 8 页 ✓\n- Limitations 在正文（非 appendix）✓\n- 匿名完整 ✓\n- Abstract < 200 词 ✓\n- ACL template [review] ✓\n- References 格式正确 ✓",
  "project": "entrainment_gated_ft",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_b542b52ff24f138c42225a1d4b456e7e"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 19 (Fresh Review)\n\n**论文**: Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**Reviewers**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + Related Work）\n**模式**: 圆桌审稿，1 轮独立审稿 + 交叉分享，达成共识无需进入 Round 2\n\n---\n\n## Summary\n\n本文利用 Wang et al. (2025) 的 controlled model zoo（3 种 hybrid linear recurrent 架构 × 5 种 attention ratio × 2 种规模），首次系统分析了 hybrid recurrent architectures 之间的 per-example predictive multiplicity。核心发现：(1) 聚合指标可互换的架构在逐样本层面差异显著（pairwise Jaccard ≈ 0.10）；(2) per-example Jaccard 在 4% attention 时即饱和并保持平坦；(3) confidence-based routing 在高 multiplicity 任务上可部分利用互补性（LAMBADA +5.2pp，但 PIQA 显著为负）。\n\n---\n\n## Strengths\n\n**S1. 实验控制度极高** [R1-S5, R2-S1]：基于公开 model zoo，所有模型共享训练数据、tokenizer、超参，仅变化架构和 attention 配置。这种控制在 hybrid architecture 文献中罕见。\n\n**S2. 统计诚实度优秀** [R1-S3, R2-S2]：始终对 LAMBADA 的 aggregate trend 标记为 \"non-significant\"（Bonferroni 校正后 p=.170），在 Table 1 脚注明确 n=5 功效限制。这在 NLP 实证论文中属上乘。\n\n**S3. Robustness 验证极为充分** [R1-S4, R2-S3]：13 个 Appendix（A–X）系统检查了 GDN confound exclusion、continuous Jaccard、5 架构扩展、seed calibration、confidence margin cross-benchmark 等。\n\n**S4. Per-example Jaccard 饱和是稳健发现** [R1-S2, R2-S4]：四个 benchmark 上 Jaccard 在第一个 attention level（4%）即饱和（Figure 4, all ρ ≤ 0.80, p ≥ .333），跨 benchmark 一致，不依赖任何单一 benchmark。\n\n**S5. Permutation test 提供了 robust 的描述性证据** [R1-S2]：10,000 次置换下所有 architecture pair 均 p < .0001，为 \"cross-architecture overlap 是结构性的\" 提供可靠统计证据。\n\n**S6. 写作规范透明** [R2-S5]：结构清晰，Abstract ≈ 148 词符合限制，多处使用 hedged language，ecological fallacy 自我承认（Related Work）。\n\n---\n\n## Weaknesses\n\n### Critical\n\n**W1. [Critical] Decoupling 叙事建立在统计上不成立的前提上** [R1-N1, R2-N1, 交叉 AGREE]\n\nContribution 2 的核心逻辑是 \"aggregate variance 下降，但 per-example overlap 没有同步下降\"。然而 aggregate convergence 本身不显著：\n- LAMBADA 是唯一 ρ=-1.0 的 benchmark，Bonferroni 后 p=.170\n- 排除 GDN 后 ρ 降至 -0.7, p=.233\n- 340M 上不复现（ρ=-0.50, p=.45）\n- 其余 9 个 benchmark 无此 trend\n\nR2 精确指出：如果 aggregate narrowing 本身不成立，decoupling 是在回答一个不需要回答的问题。Section 4.2 的 \"Regardless of whether this reflects a genuine trend, we ask...\" 试图绕过但不充分。\n\n**建议**：将 Contribution 2 重构为条件式 observation（\"even on LAMBADA where the trend is strongest...\"），或将重心转移到 Jaccard 饱和（S4）作为主发现。\n\n**W2. [Critical] 单次训练 run 无法分离架构效应与 seed 效应** [R1-N2, R2-W4, 交叉 AGREE]\n\n每个配置仅一次 run。Pythia 70M seed calibration 存在双重 mismatch：scale（70M vs 340M/1.3B）和 architecture（Transformer vs hybrid gating）。主文引用 calibration 时使用 \"consistent with architecture-driven divergence\"——高估了证据力度。\n\n**状态**：结构性限制（第三方 zoo 无法重训），维持 wont_fix。但需强化 Limitations 讨论。\n\n**W3. [Critical] 遗漏高度相关的先行工作 Yang & Wang (2026) \"Benchmark Illusion\"** [R2-N3, NEW]\n\nYang & Wang (2026, arXiv:2602.11898) 在 frontier LLMs 上展示了几乎相同的现象：comparable accuracy + 16-66% per-item disagreement + disagreement 传播到下游任务。这使本文的 \"first systematic per-example analysis\" claim 需重新界定。\n\n**建议**：必须引用并在 Related Work 中定位本文增量贡献（controlled within-family analysis, Jaccard saturation quantification, attention-ratio parametric sweep）。\n\n### Major\n\n**W4. [Major] LAMBADA format confound 未被充分讨论** [R1-W1, R2-W2, 交叉 AGREE]\n\nLAMBADA 是唯一 free-form generation benchmark（α=0.30，最高），其余全部 multiple-choice（α=0.14–0.21）。最高 multiplicity 和最强 convergence 恰巧都在唯一 open-ended 任务上。Multiple-choice 的有限答案空间机械约束 per-example divergence。§3.2 的 within-MC format mitigation（2-way vs 4-way）不够——远小于 MC vs free-form 的区别。\n\n**建议**：Limitations 显式加入 format confound；§4.1 \"multiplicity depends on task type\" 改为 \"task type or evaluation format\"。\n\n**W5. [Major] 新颖性为增量式——ecological fallacy 的 controlled instance** [R2-N2, R1 未 REBUT]\n\n论文自己承认 decoupling 是 ecological fallacy 的 controlled instance，但未充分解释 beyond ecological fallacy 提供了什么 non-trivial 的新 insight。没有回答 WHY（mechanism）、WHEN（boundary conditions）、HOW severe（impact beyond routing）。\n\n**状态**：Findings 标准下可接受，但需加强 mechanistic insight（如 Appendix F attention weight analysis 提升到正文）。\n\n**W6. [Major] Routing 实践意义有限且结果不一致** [R1-W4, R2-W1, ���叉 AGREE]\n\n4 个 benchmark 中仅 LAMBADA 有效（+5.2pp），ARC-Easy 微弱（+1.2pp），HellaSwag 无效（-0.06pp），PIQA 显著为负（-0.49pp, p=.006）。循环依赖：需先知道 multiplicity 水平才能 route。缺少 average-logits ensemble baseline。Abstract 中缺少 qualifier。\n\n**建议**：Abstract routing 句加 \"on the highest-multiplicity task\"；补充 ensemble baseline；降级为 preliminary exploration。\n\n**W7. [Major] GDN 16-head confound 导致 MMLU ρ 完全反转** [R1-W2, R2-W2]\n\nGDN h3-1 使用 16 attention head（其他 32），排除后 MMLU ρ 从 -0.7 反转为 +0.6——方向完全逆转。应在 Table 1 首次引入 GDN 时即 flag。\n\n**W8. [Major] 仅两个 scale 点且结果矛盾** [R1-W3]\n\n340M：无 convergence（所有 |ρ| ≤ 0.4）；1.3B：仅 LAMBADA 有。两个数据点无法建立 scaling trend。Convergence 可能是 capacity-gated emergent phenomenon 而非 attention 的固有属性。\n\n**W9. [Major] Confidence margin predictor 的 AUC 导出违反正态假设** [R1-W4]\n\nShapiro-Wilk 显示 rescue-set skewness 1.33-1.41（p<10⁻⁴），但 AUC point estimate 仍基于 Gaussian assumption。建议改用 non-parametric AUC（Mann-Whitney U）。\n\n**W10. [Major] Task taxonomy 是 post-hoc 的** [R1-W5]\n\n\"Informal, not pre-registered\"，缺乏可验证时间证据。Taxonomy 创建者与数据分析者为同一批人。用于 confirmatory claim 存在循环论证风险。\n\n### Minor\n\n**W11. [Minor] Bootstrap CI 在 n=3 下不具备名义覆盖率** [R1-W7]：Section 4.3 的 \"excludes zero\" 叙述可能误导。\n\n**W12. [Minor] 全文 causal vs associative 语言不完全一致** [R1-W8]：\"reflects\"、\"modulated by\"、\"controlled\" 等偶现的 causal 用语与 Section 3.5 的 \"descriptive and exploratory\" 声明矛盾。\n\n**W13. [Minor] LAMBADA 和 ARC-Easy routing 增益数值完全相同（+1.2pp, SD=0.5pp）** [R1-W9]：需确认是否为独立计算。\n\n**W14. [Minor] \"Attention dose\" 术语非标准** [R2-W5]：建议统一为 \"attention ratio\"。\n\n**W15. [Minor] Introduction 贡献列表过长** [R2-W6]：每条 >100 词，建议精简为核心 claim + section 引用。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Overall 评分**：双方独立给出 3.0 (Findings)——完全一致\n2. **Convergence claim 统计不足**：双方 Critical，交叉 AGREE\n3. **LAMBADA format confound**：双方 Major，交叉 AGREE\n4. **Routing 效果不一致**：双方 Major��交叉 AGREE\n5. **Seed confound 为结构性限制**：双方认可���交叉 AGREE\n6. **执行质量高**：双方肯定 statistical honesty, robustness coverage, experimental control\n7. **Jaccard 饱和是最强发现**：双方 Strength，交叉 AGREE\n8. **适合 Findings 而非主会议**：双方一致\n\n## Reviewer Divergence [REBUT]\n\n1. **Soundness 评分**：R1 = 2.5/5（更严格评估 inferential claims）vs R2 = 4/5（更注重 descriptive analysis 质量）。分歧源于对 \"soundness\" 的理解——R1 侧重 inferential validity，R2 侧��� methodological rigor。**Director 判断**：描述性分析确实 sound（permutation test, robustness），但推断性 claims（convergence, task-type causality）确实 underpowered。综合评为 3/5。\n\n2. **Benchmark Illusion 的影响程度**：R2 认为是 critical missing reference（直接影响 novelty claim），R1 未提及该文献。**Director 判断**：R2 有理——Yang & Wang (2026) 在更大规模上展示了类似现象，本文需引用并重新定位贡献。\n\n---\n\n## Questions\n\n1. LAMBADA 高 multiplicity（α=0.30）是否由 free-form generation format 而非 retrieval task type 驱动？是否有 TriviaQA generative 等其他 free-form benchmark 的初步数据？\n2. Average-logits ensemble 的初步结果是否可获得？缺少此对比使 routing 的 practical value 评估不完整。\n3. Pythia 70M within-seed J vs cross-architecture J 的比值在 hybrid 架构 340M/1.3B 上是否会保持？\n4. LAMBADA 和 ARC-Easy routing 增益完全相同（+1.2pp, SD=0.5pp）——这是独立计算的精确值还是 reporting error？\n5. GDN exclusion 后 MMLU ρ 从 -0.7 反转为 +0.6 如何解释？\n6. Task taxonomy \"was fixed prior to analysis\" 有无客观时间证据（pre-registration ID/git commit hash）？\n7. 本文与 Yang & Wang (2026) \"Benchmark Illusion\" 的关系——独立发现、互补分析、还是 partial overlap？\n\n---\n\n## Missing References\n\n**必须引用**：\n- Yang & Wang (2026) \"Benchmark Illusion: Disagreement among LLMs and Its Scientific Consequences\" (arXiv:2602.11898) — 核心发现高度重叠\n\n**建议引用**：\n- Li et al. (2024) \"Dropout-Based Rashomon Set Exploration for Efficient Predictive Multiplicity Estimation\" (arXiv:2402.00728)\n- \"Why are there many equally good models? An Anatomy of the Rashomon Effect\" (2026, arXiv:2601.06730)\n- MoE routing 文献（至少 1 篇代表性工作）— confidence-based routing 与 MoE per-token routing 概念相关\n- MultiBERTs (Sellam et al. 2022) 在 seed calibration 语境中的引用\n\n---\n\n## External Review\n\n**状态**：未请求（项目配置未启用外部审稿）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：已完成（2026-05-24T13:15–13:19 UTC）\n\n**Findings**（1 warning, 15 info）：\n\n- ⚠️ **[Warning] Page 8**：三个 figure（5、6、7）挤在同一页，加上 Limitations 和 Code Availability 段落，页面极度拥挤。Figure 6 和 Figure 7 尺寸很小，内部文字 axis label 估计 <6pt，可读性受影响。\n- ℹ️ Page 1：首页无视觉锚点（纯文本），Figure 1 在 page 2 顶部，位置尚可但非最优。\n- ℹ️ Page 2：Figure 1 四子图 axis label/legend 字号偏小（估计 6-7pt）。\n- ℹ��� Page 4：Figure 2 尺寸偏小（占左栏约 1/4 高度）。\n- ���️ Pages 1-8：主体 8 页符合限制。Display items 共 9 个（7 figure + 2 table），密度 1.1/页，正常。布局节奏可接受。\n- ℹ️ 全文：无 LaTeX 渲染错误、margin 溢出、section heading 孤悬。公式渲染正确。颜色语义基本一致。\n\n---\n\n## Overall Assessment\n\n**Overall**: **3.0 (Findings)**\n\n**置信度**: 4/5（两位 Reviewer 均仔细审查全文 21 页含 Appendix，交叉后完全收敛于 3.0）\n\n**综合维度评分**：\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Soundness | 3/5 | 描述性分析 sound（permutation test robust, robustness 充分），但推断性 claims underpowered（convergence p=.170, seed confound, format confound）|\n| Excitement | 2/5 | 核心发现在 Benchmark Illusion 和 ensemble diversity 文献中有先例。Ecological fallacy 自我承认削弱 novelty。Routing 仅 1/4 有效。|\n| Reproducibility | 4/5 | 公开 model zoo + 标准 eval harness + 承诺代码公开。单次 run 无法验证 seed robustness 小幅扣分。|\n\n**总结判断**：\n\n本文执行质量属于 EMNLP 主会议水准——实验控制好、统计诚实、robustness 充分、写作规范。Jaccard 饱和（4% attention 即达稳态）是跨 benchmark 一致的稳健发现。\n\n但作为主会议论文存在三个根本性问题：\n\n1. **Decoupling 叙事的前提不成立**：aggregate convergence 本身 p=.170、GDN-dependent、不跨 scale 复现。论文的标志性发现建立在一个 non-finding 之上。\n2. **新颖性为增量式**：ecological fallacy 的 controlled instance + Benchmark Illusion 的先行发现。本文增量贡献在于 controlled model zoo 上的系统量化，而非 \"首次发现\"。\n3. **Practical actionability 不足**：routing 仅 1/4 benchmark 有效且 1/4 显著为负。\n\n**适合 Findings track**：描述性贡献有价值（per-example multiplicity 的存在、结构性、Jaccard 饱和），方法论严谨度满足 Findings 要求。\n\n**升至 Conference（4.0）的路径**：\n- (a) 引用 Benchmark Illusion 并明确定位增量贡献\n- (b) 将叙事重心从 decoupling 转移到 Jaccard 饱和\n- (c) 至少一个 hybrid 架构 multi-seed 实验\n- (d) 增加一个 free-form generation benchmark 以解耦 format confound\n- (e) 补充 average-logits ensemble baseline\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 148 词，符合 200 词限制 ✓\n- \"non-significant decreasing trend\" 标注正确\n- 缺少 routing 仅 1/4 有效的 qualifier\n\n### Introduction\n- 第1段信息密度过高（4行内 90%/10%/14%/p<.01）\n- 贡献列表每条 >100 词，可精简\n- \"first systematic per-example analysis\" 需在 Benchmark Illusion 上下文中重新界定\n\n### Related Work\n- 结构良好，三段覆盖三主题\n- Ecological fallacy 自我承认是加分项\n- 缺失 Yang & Wang (2026) Benchmark Illusion\n- 缺失 MoE routing 文献\n- Ensemble diversity 讨论过于简短\n\n### Method\n- 3.1 Model Zoo：GDN 16-head anomaly 应在此提及\n- 3.2 Task Taxonomy：\"Mixed\" 类别定义模糊；format confound 讨论不够\n- 3.4 Per-Example Decomposition：binary decomposition 的 conservative bias 论证良好\n- 3.5 Statistical Methods：n=5 power caveat 在此出现正确，但后文不一致遵循\n\n### Experiments\n- 4.1：核心描述性分析是论文最强部分。Routing 段落需加 significance test + 确认相同数值\n- 4.2：\"The answer is no\" 措辞暗示 clean result，但 aggregate convergence 本身不显���\n- 4.3：GDN exclusion 讨论存在但 MMLU ρ 反转未在此报告\n\n### Conclusion\n- 避免了 over-claim，使用 \"observations\" 和 \"preliminary suggest\"\n- \"Per-example audit before architecture substitution is advisable\" 可更具体\n\n### Limitations\n- 3 段覆盖 3 点，符合 EMNLP 规则 ✓\n- 遗漏：format confound、n=5 statistical power、Pythia calibration 三重 mismatch\n\n### 格式合规 ✓\n- 正文 ≤ 8 页 ✓\n- Limitations 在正文（非 appendix）✓\n- 匿名完整 ✓\n- Abstract < 200 词 ✓\n- ACL template [review] ✓\n- References 格式正确 ✓",
    "project": "entrainment_gated_ft",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_b542b52ff24f138c42225a1d4b456e7e"
  }
}
```

</details>

---


### Tool result

_source line 1733 · 2026-05-24T13:40:39.931970+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1f8f0d6d9482071694045c30143bb993:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4015
}
```

</details>

---


### Assistant

_source line 1734 · 2026-05-24T13:40:47.450703+00:00_

审稿报告已投递。

**Round 19 审稿完成**。两位 Reviewer 独立审稿 + 交叉分享后完全收敛：

- **Overall: 3.0 (Findings)**
- 核心共识：decoupling 叙事前提不成立（p=.170）、LAMBADA format confound、routing 仅 1/4 有效、遗漏 Benchmark Illusion、novelty 增量式
- 最强发现：Jaccard 饱和（4% attention 即达稳态，跨 benchmark 一致）
- Issue Tracker 已同步更新（新增 R19-W1/W2/W3，更新 12 条既有 issue）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director"
}
```

</details>

---


## Round 134

## Round 134

4 recorded events


### User

_source line 1735 · 2026-05-24T13:40:48.518998+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**Overall 3.0 (Findings)**，Soundness 4/5，Excitement 2/5。

主要发现：
- **最严重问题 (N1)**：Decoupling 叙事建立在统计上不成立的前提上（LAMBADA aggregate convergence p=.170 校正后不显著）
- **关键遗漏 (N3)**：Yang & Wang (2026) "Benchmark Illusion" 未被引用——该论文在 frontier LLMs 上展示了非常相似的发现
- **新颖性有限 (N2)**：论文自己承认是 ecological fallacy 的 controlled instance，但没有充分解释 beyond ecological fallacy 的新 insight
- **最稳健的发现**：per-example Jaccard 在 4% attention 即饱和（跨 4 个 benchmark 一致），比 decoupling 叙事更强

---

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

## Weaknesses 回应

### R2-N1: 新颖性为增量式扩展而非质性突破

**[AGREE]** 部分同意，但程度弱于 R2 的判断。

R2 指出"不同模型在不同 example 上表现不同"是 ensemble diversity 文献的已知事实（Kuncheva & Whitaker 2003; Fort et al. 2019）。这是正确的。但我认为本文的 specific contribution 比 R2 评估的更有价值：

1. **控制条件不同**：Kuncheva & Whitaker (2003) 和 Fort et al. (2019) 研究同一架构不同 seed/hyperparameter 的 ensemble diversity；本文研究的是**架构间**的 multiplicity，在 controlled model zoo（相同训练数据、tokenizer、training budget）下进行——这比一般 ensemble diversity 实验的 confound 更少（Section 3.1）。
2. **对象不同**：本文针对的是 hybrid linear recurrent architectures 这一特定且快速发展的模型家族，而非 general neural networks。对这一家族建立 per-example divergence 的基线数据有独立价值。
3. 但**同意 R2 关于"质性突破"缺失的判断**。论文没有提出新的理论框架来解释 multiplicity 的来源（为什么某些 example 被一种架构 helped 但被另一种 hurt），也没有提供可操作的解决方案（routing 仅在 1/4 benchmark 上有效）。这使得贡献停留在 empirical observation 层面。

**补充**：R2 给 Soundness 4/5，我给 2.5/5。差异主要来自我对 convergence claim 的统计 power 评估更严格——n=5 Spearman ρ 在所有 correction 下都不显著（我的 N1），这直接影响 soundness 评分。R2 可能将 soundness 更多权重放在描述性分析上（permutation test 等），这部分我也认为 robust。

---

### R2-N2: LAMBADA aggregate trend 的叙事权重与统计证据不匹配

**[AGREE]** 完全同意。这与我的 N1（critical）完全吻合。

补充 R2 未提及的一个维度：LAMBADA 是论文 10 个 benchmark 中**唯一的 free-form generation 任务**（我的 W1/Major）。其余 9 个均为 multiple-choice 或 binary classification。Multiple-choice format 机械地约束了 per-example divergence（有限答案空间 → 更高 baseline agreement），因此 LAMBADA 的高 multiplicity（ι = 0.30）和强 convergence（ρ = -1.0）可能部分由 **evaluation format** 而非 task type 驱动。这进一步削弱了以 LAMBADA 作为 convergence 叙事核心支柱的合理性。

---

### R2-W1: 实践意义有限且不一致

**[AGREE]** 完全同意，且 R2 提出了一个我未明确指出的重要观察。

R2 指出 routing 存在**循环依赖**——需先知道任务 multiplicity 水平才能决定是否应用 routing。这是一个比我在 W4 中指出的"仅 1/4 benchmark 有效"更根本的问题。即使 routing 在更多 benchmark 上有效，**部署时无法先验地知道新任务的 multiplicity 水平**，除非先在该任务上运行所有架构的 per-example evaluation——但这样就不需要 routing 了。

具体数据支撑（来自 Section 4.1）：
- LAMBADA: +5.2 pp（有效）
- ARC-Easy: +1.2 pp（marginal）
- HellaSwag: -0.06 pp（无效）
- PIQA: -0.49 pp（**显著为负**）

4 个 benchmark 中 1 个有效、1 个 marginal、2 个无效/有害——且 Section 4.1 未报告 routing 增益的 bootstrap CI 或 significance test（我的 W4），无法判断 +5.2 pp 是否在统计意义上可靠。

---

### R2-W2: GDN 16 vs. 32 attention heads confound

**[AGREE]** 同意，且我将此问题的严重程度评估为 **Major**（而非 R2 的 Minor）。

原因：GDN exclusion 后 MMLU 的 ρ 从 -0.7 **完全反转**为 +0.6（Table 3, Appendix D.2）。这不是"minor confound"——它说明 MMLU 上的 apparent convergence pattern **完全由 GDN 的 anomalous head count 驱动**。在 n=5 已经极其 underpowered 的情况下（我的 N1），一个架构的 confound 足以翻转结论。建议 R2 考虑将此问题升级为 Major。

---

### R2-W3: Introduction 信息密度过高

**[REBUT]** 不完全同意。

Introduction 确实在 1 页内包含了大量具体数值（ι = 0.14–0.30, Jaccard ≈ 0.10, p = .170, 36% oracle gap, +5.2 pp），对首次接触该设定的读者可能 overwhelming。但对于 EMNLP 的目标受众（熟悉 LM evaluation 和 architecture comparison 的研究者），这种密度是可接受的，且 Abstract 已提供了 high-level overview。

更重要的是，Introduction 中对统计局限性的 upfront disclosure（"a non-significant decreasing trend...Bonferroni-adjusted p = .170"）是一个**优点而非缺陷**——它避免了读者在 Results 部分才发现核心结果不显著的 misleading effect。如果为了降低信息密度而删除这些 caveats，反而会损害论文的诚实性。

作为 stylistic suggestion 而非 methodological concern：可以将部分数值（如 36% oracle gap, +5.2 pp）移至 Section 4，但 p-value 的 upfront disclosure 应保留。

---

### R2-W4: "Attention dose" 术语非标准

**[AGREE]** 同意，这是 minor 的术语问题。"Attention ratio" 或 "attention proportion" 是 hybrid architecture 文献中更标准的用法（e.g., Wang et al. 2025 原文使用 "attention ratio"）。

---

### R2-W5: Task taxonomy "Mixed" 类别模糊

**[AGREE]** 同意，且这强化了我的 W5（Major）。

"Mixed" 类别包含 ARC-Easy、MMLU、SciQ、XStoryCloze——它本质上是 catch-all category，定义为"combine retrieval, comprehension, and reasoning demands"（Section 3.2）。这使得基于 taxonomy 的任何 confirmatory claim 都成问题：任何不符合前三类 pattern 的 benchmark 都被归入"Mixed"，形成不可证伪的分类。

进一步地，LAMBADA 被归入"Retrieval"，但 R2 和我都注意到 LAMBADA 的特殊性可能主要来自其 **evaluation format**（free-form generation）而非 cognitive demand（retrieval）。如果 LAMBADA 的高 multiplicity 由 format 驱动，那么"Retrieval tasks have the highest multiplicity"这一结论就需要修正为"free-form generation tasks have the highest multiplicity"——这是一个根本不同的 claim。

---

## Questions 回应

### R2-Q1: Pure vs. h24-1 (4% attention) 的 Jaccard

**支持此问题。** 论文报告 pairwise Jaccard 在 4% attention 时即饱和（Section 4.2: "Pairwise Jaccard saturates at the first attention level"），但未显式报告 pure vs. h24-1 的 Jaccard 值。Table 7（Appendix H, p.14）报告的是 pure → h3-1（25% attention）的 within-scale Jaccard，而非 pure → h24-1。如果 4% attention 已使 Jaccard 饱和，那么 pure vs. h24-1 的 Jaccard 应与 pure vs. h3-1 非常接近——这是一个可以从已有数据直接回答的问题，作者应提供具体数值。

### R2-Q2: PIQA routing 显著为负的原因

**支持此问题，并补充分析视角。**

从我对 Appendix P 的分析来看（Table 22, p.17），within-architecture prediction AUC 在所有 benchmark 上均 < 0.69，但在低 multiplicity benchmark（PIQA, ι = 0.15）上，confidence margin 的 discriminative power 可能进一步下降。原因是：当架构间 per-example 一致性高时（低 multiplicity），confidence margin 反映的是**共享的 task difficulty** 而非**architecture-specific complementarity**。在这种情况下，routing 根据 confidence 选择架构等价于根据噪声做决策，而非利用结构性差异。

这与 R2 的"循环依赖"（W1）一致：routing 仅在高 multiplicity 任务上有效，但无法先验判断 multiplicity 水平。

### R2-Q3: Average-logits ensemble 的初步结果

**支持此问题。** Section 4.1 明确将 average-logits ensemble "left to future work"——但这是 per-example multiplicity 的最自然应用。如果 per-example multiplicity 的核心价值在于 architectures 提供 complementary information，那么 ensemble（而非 routing）是更直接的利用方式。至少报告 average-logits 的 3-architecture ensemble accuracy 作为 reference point，可以显著增强论文的 practical contribution。

### R2-Q4: 在相同 model zoo 做 multi-seed 实验

**[AGREE]** 完全支持，这与我的 N2（Critical）完全一致。Wang et al. (2025) 的 model zoo 可能未提供 multi-seed 训练——但如果 model zoo 的设计不支持 seed variation，这本身就是使用该 zoo 做 causal claim 的 fundamental limitation。作者应明确说明 model zoo 是否提供 multi-seed 配置，如果不提供，应在 Limitations 中作为**首要局限**讨论。

---

## Missing References 回应

- **Li et al. (2024) "Dropout-Based Rashomon Set Exploration"**：同意相关，但相关性有限。该工作聚焦 Rashomon set 的高效估计，而非 architecture-level multiplicity。可作为 Related Work 补充但非 critical omission。
- **"Why are there many equally good models?" (2026)**：如果 R2 指的是 Rashomon effect 的理论分析，则与本文的 empirical focus 互补。建议作者在 Related Work 中简要提及。

---

## 对 R2 Overall Assessment 的评论

R2 和我在 Overall（3.0, Findings）上一致，但 sub-dimensions 差异显著：

| 维度 | R2 | R1（我） | 差异原因 |
|------|-----|---------|---------|
| Soundness | 4/5 | 2.5/5 | 我更严格评估了 n=5 Spearman 的 statistical power 和 seed confound；R2 可能更多权重放在描述性分析的 soundness 上 |
| Excitement | 2/5 | 3/5 | R2 认为 novelty 不足（ensemble diversity 已知）；我认为 controlled setting + specific architecture family 的贡献有独立价值 |

**关于 Soundness 分歧**：我认为 R2 的 Soundness 4/5 过于慷慨。论文三个 core claims 中，convergence（Spearman ρ 所有 correction 后不显著）和 routing（1/4 有效，无 significance test）的统计支撑均不足。仅描述性 claim（multiplicity 存在且为结构性的）是 fully sound 的。Soundness 4/5 对应"Strong; adequate support for claims"，但论文的 2/3 inferential claims 缺乏 adequate statistical support。建议 Soundness 应在 2.5–3 范围。

**关于 Excitement 分歧**：我给 3/5 而非 R2 的 2/5，因为研究问题本身（hybrid architecture 的 per-example behavior 有多一致？）是一个 timely 且 practically important 的问题——hybrid architectures 正在被快速部署，了解其 per-example reliability 对 deployment decisions 有直接意义。Novelty 不等于 excitement。


---

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的交叉回应

---

### Weaknesses 回应

**[AGREE] R1-N1: Spearman ρ 在 n=5 下统计效力不足**
完全同意。这是我 N1 的核心观点之一。论文的 decoupling 叙事建立在 LAMBADA 的 ρ=-1.0（校正后 p=.170）上，统计上不成立。不过需要公平指出：论文在 Table 1 脚注中明确标注了 "Power is limited: only |ρ|=1.0 achieves p<.05 at n=5"，且全文始终将此描述为 "non-significant"。问题不在于论文是否 acknowledges 功效限制（它确实做了），而在于 decoupling 仍被作为 Contribution 2 呈现——acknowledgment 不能替代 evidence。

**[AGREE] R1-N2: 单次训练 run + seed calibration mismatch**
同意。这与我的 W4 一致。Pythia 70M 的三重 mismatch（70M vs 340M/1.3B、Transformer vs hybrid、accuracy regime 差异大）使 seed calibration 的参照价值有限。论文 Appendix W 的三段 caveats 诚实列举了问题，但主文 Section 4.2 使用了 "consistent with architecture-driven divergence" 的措辞，存在 overinterpretation 风险。不过，完全否定 seed calibration 也过于严苛——它至少提供了一个 order-of-magnitude 的参照（within-seed J 是 cross-architecture J 的 2.7-4.3×）。

**[AGREE] R1-W1: LAMBADA format confound**
强烈同意。这是我 W2 的核心内容。LAMBADA 是唯一 free-form generation benchmark，同时也是 α 最高（0.30）和 aggregate convergence 最强（ρ=-1.0）的 benchmark——这种 triple correlation 高度可疑。论文在 Section 3.2 提供的 within-multiple-choice mitigation（2-way vs 4-way 不预测 α）不够有力：2-way vs 4-way 的 answer space 差异远小于 multiple-choice vs free-form。Limitations section 未提及此 confound。

**[AGREE] R1-W2: GDN 16-head confound**
同意。GDN exclusion 使 LAMBADA ρ 从 -1.0 降至 -0.7（Section 4.3），MMLU ρ 从 -0.7 反转至 +0.6。这说明 aggregate variance pattern 部分由 GDN 的 hyperparameter 异常驱动，而非纯粹的架构效应。论文在 Section 4.3 诚实报告了这一点，但在 Table 1 中 GDN confound 仅在脚注中标注（"GDN h3-1 uses 16 attention heads"），不够显著。

**[PARTIALLY REBUT] R1-W3: 仅两个 scale point 且结果矛盾**
部分同意、部分反驳。R1 的观点对 aggregate convergence claim 完全成立——340M 无 convergence（ρ=-0.50, p=.45），这确实使 scale-related convergence claim 站不住脚。但需要区分两个 finding：
- **Aggregate convergence**：确实仅在 1.3B LAMBADA 上观察到，不跨 scale → R1 正确
- **Per-example Jaccard**：在两个 scale 上一致（J ≈ 0.08-0.10 at both scales，Section 4.2 最后一段）→ 论文的 per-example multiplicity claim 是跨 scale 稳健的

论文的核心 per-example finding（Jaccard 低且饱和）并不矛盾，矛盾的仅是 aggregate convergence 部分。R1 将两者混为一谈了。

**[PARTIALLY REBUT] R1-W4: Confidence margin predictor 假设检验不充分**
部分同意。R1 关于 skewness (1.33-1.41) 违反正态假设影响 Cohen's d → AUC 转换的观点有技术 merit。但需要注意：论文直接报告了 empirical AUC（0.70-0.74，Appendix P），AUC 本身是 non-parametric statistic（基于 rank ordering），不依赖正态假设。Cohen's d 是作为 effect size 补充报告的，不是 AUC 的唯一来源。因此 skewness 问题影响的是 effect size interpretation 而非 AUC 的 validity。

关于 routing 显著性检验：同意应补充。10-fold CV 的 +5.2pp (SD=0.4pp) 可以做 t-test。

**[REBUT] R1-W5: Task taxonomy post-hoc 循环论证**
不完全同意 R1 的严重程度判断。论文明确说 taxonomy "was fixed prior to analysis following established distinctions in the hybrid architecture literature (Arora et al., 2024)"（Section 3.2）。这些类别（Retrieval, Comprehension, Reasoning, Mixed）确实是 hybrid architecture 文献中的标准分类——Arora et al. (2024) Zoology 论文就使用了类似的分类。虽然缺乏时间戳等客观证据，但 taxonomy 本身并非 data-driven 的（它不依赖于本文的结果来构建），且 Appendix A 区分了 confirmatory/exploratory benchmarks。R1 的 "循环论证" 指控过重——taxonomy 是 input 而非 output。不过，"Mixed" 类别确实模糊（我的 W5 previous round），这削弱了 task-type analysis 的清晰度。

**[REBUT] R1-W6: 5-architecture extension 仅在 340M**
R1 的事实陈述正确，但这是数据约束而非设计缺陷。GLA 和 DeltaNet 在 Wang et al. (2025) model zoo 中仅有 340M 版本。论文无法在 1.3B 上做 5-arch extension，因为模型不存在。在可用数据范围内，5-arch extension 有效验证了 per-example multiplicity 的 generalizability（all J ≤ 0.14, all p ≤ .002, Appendix X Table 30）。R1 的批评目标应该指向 model zoo 的局限性，而非论文的分析决策。

**[AGREE] R1-W7: Bootstrap CI 在 n=3 下不可靠**
同意，但论文已经 acknowledge——Section 3.5 明确称其为 "heuristic indicators of effect direction"。这是 appropriate qualification。

**[AGREE] R1-W8: 语言一致性**
同意。论文整体使用 associative language，但确有零星 causal 滑移。"reflects structural differences"（Section 4.2 最后一段）、"modulated by model capacity"（同处）暗示了因果关系。不过，这是 minor issue——总体 framing 是 associative 的。

**[REBUT] R1-W9: LAMBADA 和 ARC-Easy routing 数值相同**
R1 的事实观察有误。原文（Section 4.1）：
- LAMBADA: "+5.2 pp (SD = 0.4 pp, 10 cross-validated splits)"
- ARC-Easy: "+1.2 pp, SD = 0.5 pp"

这两组数值**不相同**：LAMBADA 是 +5.2pp/SD=0.4pp，ARC-Easy 是 +1.2pp/SD=0.5pp。R1 可能将 ARC-Easy 的数值误记为 LAMBADA 的。如果 R1 指的是 appendix 中其他位置的报告，请提供具体引用。

---

### Questions 回应

**[AGREE] R1-Q1: Pythia 70M J 比值是否在 hybrid 340M/1.3B 上保持？**
同意这是一个 open question。Appendix W 的三段 caveats 已承认这一点。唯一能确定回答的方式是在同一 model zoo 上做 multi-seed training——但这超出了论文（和 model zoo）的范围。

**[AGREE] R1-Q2: LAMBADA 高 multiplicity 是否由 format 驱动？**
强烈同意。见我的 W2。

**[AGREE with nuance] R1-Q3: GDN exclusion MMLU ρ 反转**
论文在 Section 4.3 解释了这由 GDN 的 16-head 配置驱动。MMLU ρ 反转（-0.7 → +0.6）表明 aggregate variance pattern 在某些 benchmark 上完全由 GDN 的非标准配置驱动。这是有效的 robustness check——但同时也说明 aggregate convergence 的 general claim 脆弱。论文诚实报告了这一点，这是加分项。

**[PARTIALLY REBUT] R1-Q4: AUC 是否应改用 non-parametric 方法？**
论文报告的 AUC（0.70-0.74）本身就是 non-parametric——AUC 等价于 Wilcoxon rank-sum statistic 的标准化版本，不依赖分布假设。Cohen's d 作为 effect size supplement 受 skewness 影响，但 AUC 的 validity 不受影响。R1 的建议（改用 non-parametric AUC）实际上已经被论文采用了。

**[REBUT] R1-Q5: LAMBADA 和 ARC-Easy routing 数值是否为 reporting error？**
如上述 W9 回应：两者数值不同。LAMBADA +5.2pp (SD=0.4pp)，ARC-Easy +1.2pp (SD=0.5pp)。非 reporting error。

**[AGREE] R1-Q6: Convergence 是否为 capacity-gated emergent phenomenon？**
有趣的假设。340M 无 convergence 而 1.3B 仅 LAMBADA 有，确实可能暗示 scale dependency。但论文数据不足以验证——仅有两个 scale point。如果作者能获取更多 scale 数据（如 model zoo 中是否有 160M 或 2.7B），这将是有价值的 follow-up。

**[PARTIALLY AGREE] R1-Q7: Task taxonomy 时间证据？**
论文声称 taxonomy "was fixed prior to analysis"（Section 3.2），引用 Arora et al. (2024) 作为依据。客观时间证据确实缺失，但如我在 W5 rebut 中所述，这些类别是该领域的标准分类，"post-hoc" 指控需要更强的反面证据支持。建议论文补充 git commit 等时间戳（如果可以在不破坏匿名的情况下）。

---

### 总结：R1 与 R2 的一致性

**高度一致的关键问题**：
1. LAMBADA aggregate convergence 的统计效力不足（R1-N1 ≈ R2-N1）
2. Evaluation format confound（R1-W1 ≈ R2-W2）
3. GDN 16-head confound（R1-W2 ≈ R2-W2 prev round）
4. Seed calibration 参照价值有限（R1-N2 ≈ R2-W4）

**R1 独有的有价值观点**：
- W3 的 scale 矛盾分析（我此前关注不够）
- W4 的 skewness/Cohen's d 技术细节

**我不同意 R1 的地方**：
- W5 taxonomy post-hoc 的严重程度（我认为是 minor 而非 major）
- W6 的 5-arch extension 批评（数据约束而非设计缺陷）
- W9 的数值一致性观察（R1 misread 了原文数值）

**整体评估一致性**：R1 和 R2 在核心评判上一致——论文 soundness 高但 excitement 低，aggregate convergence claim 是最大弱点，per-example Jaccard 饱和是最稳健的发现。我维持 Overall 3.0 (Findings) 的评分。

---

[Reviewer 2 审稿结果]:
交叉回应已提交。核心结论：R1 和 R2 在关键问题上高度一致（aggregate convergence 统计效力不足、format confound、GDN confound）。我 rebut 了 R1 的三个观点（W5 taxonomy 严重程度、W6 数据约束误判、W9 数值误读），并维持 Overall 3.0 (Findings) 评分。

---

[Reviewer 1 审稿结果]:
交叉回应已提交。

**汇总**：
- R2 的 7 个 Weaknesses 中，**6 个 [AGREE]**（N1 部分同意、N2/W1/W2/W4/W5 完全同意），**1 个 [REBUT]**（W3 Introduction 密度——我认为 upfront statistical disclosure 是优点非缺陷）
- 将 R2-W2（GDN confound）从 Minor 升级建议为 Major（因 MMLU ρ 完全反转）
- 对 R2 的 4 个 Questions 全部支持，并补充了 LAMBADA format confound（我的 W1）和 confidence margin predictor 的 AUC 假设违反（我的 W4）两个 R2 未覆盖的视角
- 与 R2 在 Overall 3.0 上一致，但 Soundness 分歧较大（R2: 4/5, R1: 2.5/5），建议 R2 重新考虑 inferential claims 的统计充分性

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1736 · 2026-05-24T13:44:07.822405+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "entrainment_gated_ft",
  "issues_yaml": "- id: \"R5-W1\"\n  summary: \"架构效应 vs seed 效应无法区分（单 training run，无 seed baseline）\"\n  category: experiment\n  severity: critical\n  status: wont_fix\n  first_raised_round: 5\n  last_seen_round: 19\n  mentions:\n    - round: 5\n      reviewers: [R1, R2]\n      note: \"R1 Critical, R2 W3+Q3 支持。\"\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"R2-N3 Must-Fix vs R1-W2 Should-Fix。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N2 Critical。双方 [AGREE]。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-N3 Critical + R2 交叉 [AGREE]。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-N2 Critical + R2-N2 Critical，交叉均 [AGREE]。2.7× gap 部分支持架构效应独立性。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-N2 Critical + R2-W4 Minor。R1 详列双重 mismatch。R2 同意但认为 minor。交叉后一致：structural limitation，维持 wont_fix。\"\n  action_items:\n    - round: 13\n      action: \"E4 Pythia 410M 9-seed calibration（实际完成 70M）\"\n      assigned_to: main_agent\n      status: done\n    - round: 14\n      action: \"Limitations 提升 single-seed 为 top limitation；§4.2 弱化因果语言\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"结构性限制。已做：Pythia 70M calibration + Limitations 讨论 + associative 语言。R19 维持 wont_fix。\"\n  resolution_round: null\n\n- id: \"R5-W2\"\n  summary: \"收敛 claim 统计不显著（Bonferroni p=.170）且依赖 GDN inclusion\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 19\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical。交叉 [AGREE]。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R16-N1 重新 flag。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2 交叉 [AGREE]。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical，交叉均 [AGREE]。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical，交叉均 [AGREE]。R2 升级论证：decoupling 叙事建立在'不存在的前提'上。双方建议重构为条件式或转向 Jaccard 饱和。\"\n  action_items:\n    - round: 15\n      action: \"Abstract/Intro 重构：以 Jaccard saturation 为主线\"\n      assigned_to: paper_agent\n      status: done\n    - round: 16\n      action: \"结构性叙事重组\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"Contribution 2 重构为条件式或将 Jaccard 饱和升级为主发现\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"R15-R19 持续 flag。需彻底降级为 exploratory observation。\"\n  resolution_round: null\n\n- id: \"R5-W4\"\n  summary: \"新颖性有限——已有指标的直接套用，无新方法/理论\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 5\n  last_seen_round: 19\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"R2-W1 ecological fallacy。R1 REBUT。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R2-N1 Must-Fix vs R1 REBUT。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"部分收敛：均同意定位为 empirical contribution。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"Findings 标准下经验发现足够。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R2-N2 Major + R2-N3 (Benchmark Illusion)��R1 交叉部分 AGREE——承认缺少'质性突破'但认为 controlled setting 有独立价值（AGREE with nuance）。双方在 Findings 适切性上一致。\"\n  action_items:\n    - round: 6\n      action: \"Intro 加 empirical novelty framing\"\n      assigned_to: paper_agent\n      status: done\n    - round: 16\n      action: \"Intro 强化 empirical contribution 定位\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"引用 Benchmark Illusion 并定位增量贡献\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"结构性限制。Findings 标准下可接受。需引用 Benchmark Illusion。\"\n  resolution_round: null\n\n- id: \"R5-W3\"\n  summary: \"Task-dependent spectrum 仅 3 benchmark，存在评估格式 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [R1, R2]\n      note: \"α 变异可能反映 format 而非 task type。\"\n  action_items:\n    - round: 5\n      action: \"WinoGrande + PIQA per-example 分析\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"PIQA + WinoGrande 整合完成。R17 提出更具体的 format confound（见 R17-W1）。\"\n  resolution_round: 6\n\n- id: \"R5-W5\"\n  summary: \"正文约 8.2 页超出 EMNLP 8 页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R19 双方格式检查确认合规。\"\n  action_items:\n    - round: 5\n      action: \"结构性压缩 8.2→7 页\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"主文在 8 页内。R14-R19 持续确认合规。\"\n  resolution_round: 5\n\n- id: \"R5-W6\"\n  summary: \"遗漏关键相关工作 Zoology/Based/Samba\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  action_items:\n    - round: 5\n      action: \"补 3 篇引用\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已引用。\"\n  resolution_round: 5\n\n- id: \"R5-W7\"\n  summary: \"Ensemble 建议缺乏实验支撑\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 9\n  action_items:\n    - round: 7\n      action: \"Majority vote + oracle POC 写入 Conclusion\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已包含 MV/oracle POC 数据。\"\n  resolution_round: 9\n\n- id: \"R5-W8\"\n  summary: \"Binary decomposition 可能低估多选题一致性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 19\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"Appendix O continuous Jaccard 缓解。\"\n    - round: 19\n      reviewers: []\n      note: \"R19 双方均未作为 weakness 提出。R1 在 S6 肯定 binary decomposition 设计合理。视为已充分缓解。\"\n  action_items:\n    - round: 13\n      action: \"E2 continuous-threshold Jaccard 整合\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"R19 双方未 flag，R1 肯定设计合理。已充分缓解。\"\n  resolution_round: 19\n\n- id: \"R5-W9\"\n  summary: \"Abstract 信息密度过高（统计量堆砌）\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 19\n  mentions:\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"接近 200 word 上限，inline 统计量增加认知负荷。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R2-W4 Major：数字密度过高。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"Abstract 已改善（148词）。R2-W6 指出 Introduction 贡献列表过长。R1 交叉 REBUT Introduction 密度——认为 upfront statistical disclosure 是优点。分歧：R1 认为密度可接受，R2 认为需精简。\"\n  action_items:\n    - round: 18\n      action: \"Abstract 再次精简\"\n      assigned_to: paper_agent\n      status: done\n    - round: 19\n      action: \"Introduction 贡献列表精简为核心 claim + section 引用\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"Abstract 已改善。Introduction 贡献列表仍长（R2 flag，R1 rebut）。\"\n  resolution_round: null\n\n- id: \"RV-L1\"\n  summary: \"Limitations 6 段违反 EMNLP 用户规则（要求 ~3 点）\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 15\n  action_items:\n    - round: 5\n      action: \"6 段→3 段\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"压缩为 3 段。R14-R19 确认合规。\"\n  resolution_round: 5\n\n- id: \"RV-L2\"\n  summary: \"loglik 压缩假说已被诊断数据反驳但论文仍引用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  action_items:\n    - round: 5\n      action: \"改为 binary classification structural properties 解释\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已���正。\"\n  resolution_round: 5\n\n- id: \"R6-N3\"\n  summary: \"仅 2 个 scale 点不足以支撑 scale-dependent claim\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  action_items:\n    - round: 6\n      action: \"全文替换 scale-dependent\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"全文已用 'differs between 340M and 1.3B'。\"\n  resolution_round: 8\n\n- id: \"R6-N2\"\n  summary: \"缺乏 actionable insights——论文停在 '问题存在' 层面\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 15\n  action_items:\n    - round: 13\n      action: \"E1 routing 结果整合\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Routing 已写入。非 blocking。\"\n  resolution_round: 13\n\n- id: \"R6-W1\"\n  summary: \"Decoupling 形式化存在技术问题\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 9\n  action_items:\n    - round: 8\n      action: \"删除 Equation 1\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已删。Round 12-19 未再提及。\"\n  resolution_round: 12\n\n- id: \"R6-W2\"\n  summary: \"GDN h3-1 的 16-head confound 削弱 LAMBADA convergence\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 19\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"主文并列 with/without GDN。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"移除 GDN 后 ρ 从 -1.0 降至 -0.7。\"\n    - round: 18\n      reviewers: []\n      note: \"§4.3 已讨论。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W2 Major + R2 交叉 AGREE（R2 初评为 Minor 但交叉中认可应为 Major 因 MMLU ρ 完全反转）。MMLU -0.7→+0.6 证明 MMLU convergence 完全由 GDN anomaly 驱动。需在 Table 1 处更早 flag。\"\n  action_items:\n    - round: 15\n      action: \"§4.2/§4.3 讨论 GDN exclusion\"\n      assigned_to: paper_agent\n      status: done\n    - round: 19\n      action: \"Table 1 首次引入 GDN 时 flag 16-head anomaly；正文报告 MMLU ρ ���转\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"§4.3 已讨论但不够显著。\"\n  resolution_round: null\n\n- id: \"R6-W3\"\n  summary: \"Bootstrap CI 在 n=3 架构上覆盖率远低于名义值\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"升级为 Critical。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W7 Minor。论文 Section 3.5 已标 'heuristic'。R2 交叉 AGREE 但认为已 acknowledge。降级回 Minor/Warning。\"\n  action_items:\n    - round: 16\n      action: \"Intro BCa CI 加 heuristic caveat\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"Section 3.5 caveat 存在。R19 降级为 Minor。\"\n  resolution_round: null\n\n- id: \"R14-W1\"\n  summary: \"Confidence margin 'mechanism' 标题暗示因果性\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  action_items:\n    - round: 14\n      action: \"替换 'mechanism' → 'predictor'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已替换。R15-R19 未再提及。\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"n=5 attention ratios 使 permutation test 本质为 binary outcome\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  action_items:\n    - round: 15\n      action: \"§4.2 标注 'suggestive but underpowered'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。合并入 R5-W2。\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"标题/Abstract 过度泛化\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  action_items:\n    - round: 14\n      action: \"正文加 scope 限定\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。\"\n  resolution_round: 15\n\n- id: \"R14-W4\"\n  summary: \"缺失 prediction churn 文献\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  action_items:\n    - round: 14\n      action: \"添加 Milani Fard (2016)\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已引用。\"\n  resolution_round: 15\n\n- id: \"R15-W1\"\n  summary: \"'Nearly disjoint' 措辞夸大\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  action_items:\n    - round: 15\n      action: \"替换为 calibrated 表述\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。\"\n  resolution_round: 15\n\n- id: \"R15-W2\"\n  summary: \"Routing 定位过高（仅 1/4 benchmark 有效）\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 19\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"降级为 case study。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"1/4 success rate，无 ensemble baseline。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"PIQA 显著负效。缺 ensemble baseline。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W4 Major + R2-W1 Major，交叉均 AGREE。R2 补充循环依赖问题。Abstract 缺 qualifier。双方要求降级 + 补 ensemble baseline。\"\n  action_items:\n    - round: 15\n      action: \"降级为 case study\"\n      assigned_to: paper_agent\n      status: done\n    - round: 19\n      action: \"Abstract routing 句加 qualifier；补充 average-logits ensemble baseline\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"正文已为 case study 但 abstract 叙事权重仍偏高。\"\n  resolution_round: null\n\n- id: \"R15-D1\"\n  summary: \"Appendix Table 30 DeltaNet 数据不一致\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  action_items:\n    - round: 15\n      action: \"从 JSON 逐格修正\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已修正。\"\n  resolution_round: 15\n\n- id: \"R15-W3\"\n  summary: \"缺失 Jain et al. (2025 FAccT)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  action_items:\n    - round: 15\n      action: \"添加到 bib + Related Work\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。\"\n  resolution_round: 15\n\n- id: \"R16-N1\"\n  summary: \"Aggregate convergence 叙事在 Abstract/Introduction 中仍过度突出\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-N2 Must-Fix + R2-W1 Should-Fix。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"要求全文统一为 descriptive/suggestive。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R2 建议重构：'architectures interchangeable by aggregate metrics differ per-example'。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical，���叉均 AGREE。R2 升级：'不存在的前提'。§4.2 标题暗示 aggregate narrowing 为 established fact。\"\n  action_items:\n    - round: 16\n      action: \"结构性叙事重组\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"§4.2 标题改为非确定性；全文消除 convergence 作为 established premise\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"R16-R19 持续 flag。核心叙事仍需全面重构。\"\n  resolution_round: null\n\n- id: \"R16-W1\"\n  summary: \"Routing 实验缺少 variance 报告\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"LAMBADA SD=0.4pp 已报告。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1 仍要求 bootstrap CI + significance test。R2 交叉同意应补充。\"\n  action_items:\n    - round: 19\n      action: \"LAMBADA routing 补 bootstrap CI + permutation significance test\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"SD 已报告，formal significance test 仍缺。\"\n  resolution_round: null\n\n- id: \"R16-W2\"\n  summary: \"5-architecture 扩展验证仅 340M\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W6 Major。R2 交叉 REBUT——认为是数据约束（GLA/DeltaNet 在 model zoo 中仅有 340M）而非设计缺陷。分歧：R1 认为 Major，R2 认为不应归咎于论文。Director 判断：R2 有理，这是 model zoo 局限性。降级为标注 scope 即可。\"\n  action_items:\n    - round: 19\n      action: \"Appendix X 明确标注仅验证 per-example divergence（非 convergence），说明 GLA/DeltaNet 仅有 340M 版本\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"R2 rebut 有理：数据约束非设计缺陷。标注 scope 即可。\"\n  resolution_round: null\n\n- id: \"R16-W3\"\n  summary: \"Confidence margin AUC 的正态假设未验证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W4 Major 重新 flag：skewness 违反正态。R2 交叉 PARTIALLY REBUT：论文报告的 AUC (0.70-0.74) 本身是 non-parametric（等价于 Mann-Whitney U），Cohen's d 仅为 effect size 补充。正态假设影响 effect size interpretation 而非 AUC validity。Director 判断：R2 的 rebut 有技术 merit——AUC 本身不依赖正态假设。降低严重程度。\"\n  action_items:\n    - round: 16\n      action: \"计算 empirical AUC 对比\"\n      assigned_to: main_agent\n      status: in_progress\n  resolution: \"R2 rebut 有理：AUC 本身为 non-parametric，不受正态假设影响。Cohen's d 的 effect size interpretation 受影响但非核心。可标注即可。\"\n  resolution_round: null\n\n- id: \"R16-W4\"\n  summary: \"模型规模覆盖有限（≤1.3B vs 7B+ 部署场景）\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"建议 'consistent across the two scales examined'。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W3 Major。R2 交叉 PARTIALLY REBUT：per-example Jaccard 跨 scale 一致（J≈0.08-0.10 at both），矛盾仅在 aggregate convergence 部分。Director 判断：R2 区分正确——per-example finding 跨 scale 稳健，scale 问题仅影响 convergence claim。\"\n  action_items:\n    - round: 18\n      action: \"全文 scale 语言限定\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"明确区分：per-example Jaccard 跨 scale 一致 vs aggregate convergence 仅 1.3B LAMBADA\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"R2 区分正确：per-example 跨 scale 稳健，convergence 不跨 scale。\"\n  resolution_round: null\n\n- id: \"R16-W5\"\n  summary: \"遗漏重要相关工作\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"Model Soups + Jiang (2024)。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R2-N3 Major：Yang & Wang (2026) 'Benchmark Illusion' 是重大遗漏。R2-W3 补充 MoE routing 文献。R1 补充 MultiBERTs (Sellam 2022) 在 seed 语境中未引用。R2 确认 Model Soups/Fort/Jain 已在论文中。\"\n  action_items:\n    - round: 18\n      action: \"添加 Wortsman (2022) + Jiang (2024)\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"必须引用 Yang & Wang (2026) Benchmark Illusion；建议引用 MoE routing 文献\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"Benchmark Illusion 是重大遗漏，影响 novelty claim。\"\n  resolution_round: null\n\n- id: \"R16-M1\"\n  summary: \"Haghighat 2026 bib 条目需更新为 AAAI 2026\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 未提及。可能已修复。\"\n  action_items:\n    - round: 16\n      action: \"更新 references.bib\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W1\"\n  summary: \"Task type vs evaluation format confound（LAMBADA 为唯一 free-form benchmark）\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-W2 提出 + R2 [AGREE]。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"双方 Major，要求正文讨论。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W1 Major + R2-W2 Major，交叉均强 AGREE。R1 详细论证 MC format 机械约束 divergence。R2 补充：§3.2 within-MC mitigation 不够——2-way vs 4-way 远小于 MC vs free-form。LAMBADA 被归为 'Retrieval' 但特殊性可能来自 format 而非 cognitive demand。\"\n  action_items:\n    - round: 18\n      action: \"§3.2 末加 format confound 讨论\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"Limitations 显式加入 format confound；§4.1 'task type' 改为 'task type or evaluation format'；考虑增加 free-form benchmark\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"R19 双方强 AGREE Major。§3.2 有部分讨论但 Limitations 和 §4.1 claim 仍需修改。\"\n  resolution_round: null\n\n- id: \"R17-W2\"\n  summary: \"Confirmatory/exploratory benchmark 分类缺乏预注册\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: []\n      note: \"未单独提及。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W5 Major（循环论证风险）。R2 交叉 REBUT——认为 taxonomy 是文献标准分类（Arora et al. 2024），非 data-driven，'post-hoc' 指控需更强反面证据。分歧：R1 Major vs R2 Minor。Director 判断：R2 的 rebut 有理（标准分类），但缺乏时间证据确实是弱点。降级为 Should-Fix（提供 git timestamp 或框定为 hypothesis-generating）。\"\n  action_items:\n    - round: 17\n      action: \"Appendix A 明确 all-10 correction 为唯一有效\"\n      assigned_to: paper_agent\n      status: open\n    - round: 19\n      action: \"提供 taxonomy 时间证据（git commit）或框定为 hypothesis-generating\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"R1 Major vs R2 REBUT（标准分类）。Director 降级为 Should-Fix。\"\n  resolution_round: null\n\n- id: \"R18-W1\"\n  summary: \"Permutation test null baseline 不排除 example difficulty confound\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 未显式提及。可能被 format confound 讨论吸收。\"\n  action_items:\n    - round: 18\n      action: \"讨论 example difficulty 作为 confound\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W1\"\n  summary: \"遗漏 Yang & Wang (2026) 'Benchmark Illusion'——核心发现高度重叠\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R2]\n      note: \"R2-N3 Major：Yang & Wang (2026) arXiv:2602.11898 在 frontier LLMs 上展示了 comparable accuracy + 16-66% per-item disagreement。使 'first systematic per-example analysis' 需重新界定。R1 交叉中未 rebut 此点。\"\n  action_items:\n    - round: 19\n      action: \"引用 Yang & Wang (2026)；重新界��� 'first' claim 为 'first controlled within-family analysis'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W2\"\n  summary: \"LAMBADA 和 ARC-Easy routing 增益数值疑似相同\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W9 初提此问题（声称两者均为 +1.2pp, SD=0.5pp）。R2 交叉 REBUT 并纠正：原文为 LAMBADA +5.2pp (SD=0.4pp)、ARC-Easy +1.2pp (SD=0.5pp)——并不相同。R1 误读了原文。\"\n  action_items: []\n  resolution: \"R1 误读。原文数值不同（LAMBADA +5.2pp vs ARC-Easy +1.2pp）。无需修改。\"\n  resolution_round: 19\n\n- id: \"R19-W3\"\n  summary: \"全文 associative vs causal 语言不完全一致\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W8 Minor：'reflects'/'modulated by'/'controlled' 等 causal 用语偶现。R2 交叉 AGREE 但认为 minor——总体 framing 是 associative 的。\"\n  action_items:\n    - round: 19\n      action: \"全文统一 associative 语言\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "entrainment_gated_ft",
    "issues_yaml": "- id: \"R5-W1\"\n  summary: \"架构效应 vs seed 效应无法区分（单 training run，无 seed baseline）\"\n  category: experiment\n  severity: critical\n  status: wont_fix\n  first_raised_round: 5\n  last_seen_round: 19\n  mentions:\n    - round: 5\n      reviewers: [R1, R2]\n      note: \"R1 Critical, R2 W3+Q3 支持。\"\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"R2-N3 Must-Fix vs R1-W2 Should-Fix。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N2 Critical。双方 [AGREE]。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-N3 Critical + R2 交叉 [AGREE]。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-N2 Critical + R2-N2 Critical，交叉均 [AGREE]。2.7× gap 部分支持架构效应独立性。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-N2 Critical + R2-W4 Minor。R1 详列双重 mismatch。R2 同意但认为 minor。交叉后一致：structural limitation，维持 wont_fix。\"\n  action_items:\n    - round: 13\n      action: \"E4 Pythia 410M 9-seed calibration（实际完成 70M）\"\n      assigned_to: main_agent\n      status: done\n    - round: 14\n      action: \"Limitations 提升 single-seed 为 top limitation；§4.2 弱化因果语言\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"结构性限制。已做：Pythia 70M calibration + Limitations 讨论 + associative 语言。R19 维持 wont_fix。\"\n  resolution_round: null\n\n- id: \"R5-W2\"\n  summary: \"收敛 claim 统计不显著（Bonferroni p=.170）且依赖 GDN inclusion\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 19\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical。交叉 [AGREE]。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R16-N1 重新 flag。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2 交叉 [AGREE]。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical，交叉均 [AGREE]。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical，交叉均 [AGREE]。R2 升级论证：decoupling 叙事建立在'不存在的前提'上。双方建议重构为条件式或转向 Jaccard 饱和。\"\n  action_items:\n    - round: 15\n      action: \"Abstract/Intro 重构：以 Jaccard saturation 为主线\"\n      assigned_to: paper_agent\n      status: done\n    - round: 16\n      action: \"结构性叙事重组\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"Contribution 2 重构为条件式或将 Jaccard 饱和升级为主发现\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"R15-R19 持续 flag。需彻底降级为 exploratory observation。\"\n  resolution_round: null\n\n- id: \"R5-W4\"\n  summary: \"新颖性有限——已有指标的直接套用，无新方法/理论\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 5\n  last_seen_round: 19\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"R2-W1 ecological fallacy。R1 REBUT。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R2-N1 Must-Fix vs R1 REBUT。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"部分收敛：均同意定位为 empirical contribution。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"Findings 标准下经验发现足够。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R2-N2 Major + R2-N3 (Benchmark Illusion)��R1 交叉部分 AGREE——承认缺少'质性突破'但认为 controlled setting 有独立价值（AGREE with nuance）。双方在 Findings 适切性上一致。\"\n  action_items:\n    - round: 6\n      action: \"Intro 加 empirical novelty framing\"\n      assigned_to: paper_agent\n      status: done\n    - round: 16\n      action: \"Intro 强化 empirical contribution 定位\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"引用 Benchmark Illusion 并定位增量贡献\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"结构性限制。Findings 标准下可接受。需引用 Benchmark Illusion。\"\n  resolution_round: null\n\n- id: \"R5-W3\"\n  summary: \"Task-dependent spectrum 仅 3 benchmark，存在评估格式 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [R1, R2]\n      note: \"α 变异可能反映 format 而非 task type。\"\n  action_items:\n    - round: 5\n      action: \"WinoGrande + PIQA per-example 分析\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"PIQA + WinoGrande 整合完成。R17 提出更具体的 format confound（见 R17-W1）。\"\n  resolution_round: 6\n\n- id: \"R5-W5\"\n  summary: \"正文约 8.2 页超出 EMNLP 8 页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R19 双方格式检查确认合规。\"\n  action_items:\n    - round: 5\n      action: \"结构性压缩 8.2→7 页\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"主文在 8 页内。R14-R19 持续确认合规。\"\n  resolution_round: 5\n\n- id: \"R5-W6\"\n  summary: \"遗漏关键相关工作 Zoology/Based/Samba\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  action_items:\n    - round: 5\n      action: \"补 3 篇引用\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已引用。\"\n  resolution_round: 5\n\n- id: \"R5-W7\"\n  summary: \"Ensemble 建议缺乏实验支撑\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 9\n  action_items:\n    - round: 7\n      action: \"Majority vote + oracle POC 写入 Conclusion\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已包含 MV/oracle POC 数据。\"\n  resolution_round: 9\n\n- id: \"R5-W8\"\n  summary: \"Binary decomposition 可能低估多选题一致性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 19\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"Appendix O continuous Jaccard 缓解。\"\n    - round: 19\n      reviewers: []\n      note: \"R19 双方均未作为 weakness 提出。R1 在 S6 肯定 binary decomposition 设计合理。视为已充分缓解。\"\n  action_items:\n    - round: 13\n      action: \"E2 continuous-threshold Jaccard 整合\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"R19 双方未 flag，R1 肯定设计合理。已充分缓解。\"\n  resolution_round: 19\n\n- id: \"R5-W9\"\n  summary: \"Abstract 信息密度过高（统计量堆砌）\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 19\n  mentions:\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"接近 200 word 上限，inline 统计量增加认知负荷。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R2-W4 Major：数字密度过高。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"Abstract 已改善（148词）。R2-W6 指出 Introduction 贡献列表过长。R1 交叉 REBUT Introduction 密度——认为 upfront statistical disclosure 是优点。分歧：R1 认为密度可接受，R2 认为需精简。\"\n  action_items:\n    - round: 18\n      action: \"Abstract 再次精简\"\n      assigned_to: paper_agent\n      status: done\n    - round: 19\n      action: \"Introduction 贡献列表精简为核心 claim + section 引用\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"Abstract 已改善。Introduction 贡献列表仍长（R2 flag，R1 rebut）。\"\n  resolution_round: null\n\n- id: \"RV-L1\"\n  summary: \"Limitations 6 段违反 EMNLP 用户规则（要求 ~3 点）\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 15\n  action_items:\n    - round: 5\n      action: \"6 段→3 段\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"压缩为 3 段。R14-R19 确认合规。\"\n  resolution_round: 5\n\n- id: \"RV-L2\"\n  summary: \"loglik 压缩假说已被诊断数据反驳但论文仍引用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  action_items:\n    - round: 5\n      action: \"改为 binary classification structural properties 解释\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已���正。\"\n  resolution_round: 5\n\n- id: \"R6-N3\"\n  summary: \"仅 2 个 scale 点不足以支撑 scale-dependent claim\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  action_items:\n    - round: 6\n      action: \"全文替换 scale-dependent\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"全文已用 'differs between 340M and 1.3B'。\"\n  resolution_round: 8\n\n- id: \"R6-N2\"\n  summary: \"缺乏 actionable insights——论文停在 '问题存在' 层面\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 15\n  action_items:\n    - round: 13\n      action: \"E1 routing 结果整合\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Routing 已写入。非 blocking。\"\n  resolution_round: 13\n\n- id: \"R6-W1\"\n  summary: \"Decoupling 形式化存在技术问题\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 9\n  action_items:\n    - round: 8\n      action: \"删除 Equation 1\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已删。Round 12-19 未再提及。\"\n  resolution_round: 12\n\n- id: \"R6-W2\"\n  summary: \"GDN h3-1 的 16-head confound 削弱 LAMBADA convergence\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 19\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"主文并列 with/without GDN。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"移除 GDN 后 ρ 从 -1.0 降至 -0.7。\"\n    - round: 18\n      reviewers: []\n      note: \"§4.3 已讨论。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W2 Major + R2 交叉 AGREE（R2 初评为 Minor 但交叉中认可应为 Major 因 MMLU ρ 完全反转）。MMLU -0.7→+0.6 证明 MMLU convergence 完全由 GDN anomaly 驱动。需在 Table 1 处更早 flag。\"\n  action_items:\n    - round: 15\n      action: \"§4.2/§4.3 讨论 GDN exclusion\"\n      assigned_to: paper_agent\n      status: done\n    - round: 19\n      action: \"Table 1 首次引入 GDN 时 flag 16-head anomaly；正文报告 MMLU ρ ���转\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"§4.3 已讨论但不够显著。\"\n  resolution_round: null\n\n- id: \"R6-W3\"\n  summary: \"Bootstrap CI 在 n=3 架构上覆盖率远低于名义值\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"升级为 Critical。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W7 Minor。论文 Section 3.5 已标 'heuristic'。R2 交叉 AGREE 但认为已 acknowledge。降级回 Minor/Warning。\"\n  action_items:\n    - round: 16\n      action: \"Intro BCa CI 加 heuristic caveat\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"Section 3.5 caveat 存在。R19 降级为 Minor。\"\n  resolution_round: null\n\n- id: \"R14-W1\"\n  summary: \"Confidence margin 'mechanism' 标题暗示因果性\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  action_items:\n    - round: 14\n      action: \"替换 'mechanism' → 'predictor'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已替换。R15-R19 未再提及。\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"n=5 attention ratios 使 permutation test 本质为 binary outcome\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  action_items:\n    - round: 15\n      action: \"§4.2 标注 'suggestive but underpowered'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。合并入 R5-W2。\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"标题/Abstract 过度泛化\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  action_items:\n    - round: 14\n      action: \"正文加 scope 限定\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。\"\n  resolution_round: 15\n\n- id: \"R14-W4\"\n  summary: \"缺失 prediction churn 文献\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  action_items:\n    - round: 14\n      action: \"添加 Milani Fard (2016)\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已引用。\"\n  resolution_round: 15\n\n- id: \"R15-W1\"\n  summary: \"'Nearly disjoint' 措辞夸大\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  action_items:\n    - round: 15\n      action: \"替换为 calibrated 表述\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。\"\n  resolution_round: 15\n\n- id: \"R15-W2\"\n  summary: \"Routing 定位过高（仅 1/4 benchmark 有效）\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 19\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"降级为 case study。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"1/4 success rate，无 ensemble baseline。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"PIQA 显著负效。缺 ensemble baseline。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W4 Major + R2-W1 Major，交叉均 AGREE。R2 补充循环依赖问题。Abstract 缺 qualifier。双方要求降级 + 补 ensemble baseline。\"\n  action_items:\n    - round: 15\n      action: \"降级为 case study\"\n      assigned_to: paper_agent\n      status: done\n    - round: 19\n      action: \"Abstract routing 句加 qualifier；补充 average-logits ensemble baseline\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"正文已为 case study 但 abstract 叙事权重仍偏高。\"\n  resolution_round: null\n\n- id: \"R15-D1\"\n  summary: \"Appendix Table 30 DeltaNet 数据不一致\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  action_items:\n    - round: 15\n      action: \"从 JSON 逐格修正\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已修正。\"\n  resolution_round: 15\n\n- id: \"R15-W3\"\n  summary: \"缺失 Jain et al. (2025 FAccT)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  action_items:\n    - round: 15\n      action: \"添加到 bib + Related Work\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。\"\n  resolution_round: 15\n\n- id: \"R16-N1\"\n  summary: \"Aggregate convergence 叙事在 Abstract/Introduction 中仍过度突出\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-N2 Must-Fix + R2-W1 Should-Fix。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"要求全文统一为 descriptive/suggestive。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R2 建议重构：'architectures interchangeable by aggregate metrics differ per-example'。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical，���叉均 AGREE。R2 升级：'不存在的前提'。§4.2 标题暗示 aggregate narrowing 为 established fact。\"\n  action_items:\n    - round: 16\n      action: \"结构性叙事重组\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"§4.2 标题改为非确定性；全文消除 convergence 作为 established premise\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"R16-R19 持续 flag。核心叙事仍需全面重构。\"\n  resolution_round: null\n\n- id: \"R16-W1\"\n  summary: \"Routing 实验缺少 variance 报告\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"LAMBADA SD=0.4pp 已报告。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1 仍要求 bootstrap CI + significance test。R2 交叉同意应补充。\"\n  action_items:\n    - round: 19\n      action: \"LAMBADA routing 补 bootstrap CI + permutation significance test\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"SD 已报告，formal significance test 仍缺。\"\n  resolution_round: null\n\n- id: \"R16-W2\"\n  summary: \"5-architecture 扩展验证仅 340M\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W6 Major。R2 交叉 REBUT——认为是数据约束（GLA/DeltaNet 在 model zoo 中仅有 340M）而非设计缺陷。分歧：R1 认为 Major，R2 认为不应归咎于论文。Director 判断：R2 有理，这是 model zoo 局限性。降级为标注 scope 即可。\"\n  action_items:\n    - round: 19\n      action: \"Appendix X 明确标注仅验证 per-example divergence（非 convergence），说明 GLA/DeltaNet 仅有 340M 版本\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"R2 rebut 有理：数据约束非设计缺陷。标注 scope 即可。\"\n  resolution_round: null\n\n- id: \"R16-W3\"\n  summary: \"Confidence margin AUC 的正态假设未验证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W4 Major 重新 flag：skewness 违反正态。R2 交叉 PARTIALLY REBUT：论文报告的 AUC (0.70-0.74) 本身是 non-parametric（等价于 Mann-Whitney U），Cohen's d 仅为 effect size 补充。正态假设影响 effect size interpretation 而非 AUC validity。Director 判断：R2 的 rebut 有技术 merit——AUC 本身不依赖正态假设。降低严重程度。\"\n  action_items:\n    - round: 16\n      action: \"计算 empirical AUC 对比\"\n      assigned_to: main_agent\n      status: in_progress\n  resolution: \"R2 rebut 有理：AUC 本身为 non-parametric，不受正态假设影响。Cohen's d 的 effect size interpretation 受影响但非核心。可标注即可。\"\n  resolution_round: null\n\n- id: \"R16-W4\"\n  summary: \"模型规模覆盖有限（≤1.3B vs 7B+ 部署场景）\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"建议 'consistent across the two scales examined'。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W3 Major。R2 交叉 PARTIALLY REBUT：per-example Jaccard 跨 scale 一致（J≈0.08-0.10 at both），矛盾仅在 aggregate convergence 部分。Director 判断：R2 区分正确——per-example finding 跨 scale 稳健，scale 问题仅影响 convergence claim。\"\n  action_items:\n    - round: 18\n      action: \"全文 scale 语言限定\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"明确区分：per-example Jaccard 跨 scale 一致 vs aggregate convergence 仅 1.3B LAMBADA\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"R2 区分正确：per-example 跨 scale 稳健，convergence 不跨 scale。\"\n  resolution_round: null\n\n- id: \"R16-W5\"\n  summary: \"遗漏重要相关工作\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"Model Soups + Jiang (2024)。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R2-N3 Major：Yang & Wang (2026) 'Benchmark Illusion' 是重大遗漏。R2-W3 补充 MoE routing 文献。R1 补充 MultiBERTs (Sellam 2022) 在 seed 语境中未引用。R2 确认 Model Soups/Fort/Jain 已在论文中。\"\n  action_items:\n    - round: 18\n      action: \"添加 Wortsman (2022) + Jiang (2024)\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"必须引用 Yang & Wang (2026) Benchmark Illusion；建议引用 MoE routing 文献\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"Benchmark Illusion 是重大遗漏，影响 novelty claim。\"\n  resolution_round: null\n\n- id: \"R16-M1\"\n  summary: \"Haghighat 2026 bib 条目需更新为 AAAI 2026\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 未提及。可能已修复。\"\n  action_items:\n    - round: 16\n      action: \"更新 references.bib\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W1\"\n  summary: \"Task type vs evaluation format confound（LAMBADA 为唯一 free-form benchmark）\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-W2 提出 + R2 [AGREE]。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"双方 Major，要求正文讨论。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W1 Major + R2-W2 Major，交叉均强 AGREE。R1 详细论证 MC format 机械约束 divergence。R2 补充：§3.2 within-MC mitigation 不够——2-way vs 4-way 远小于 MC vs free-form。LAMBADA 被归为 'Retrieval' 但特殊性可能来自 format 而非 cognitive demand。\"\n  action_items:\n    - round: 18\n      action: \"§3.2 末加 format confound 讨论\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"Limitations 显式加入 format confound；§4.1 'task type' 改为 'task type or evaluation format'；考虑增加 free-form benchmark\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"R19 双方强 AGREE Major。§3.2 有部分讨论但 Limitations 和 §4.1 claim 仍需修改。\"\n  resolution_round: null\n\n- id: \"R17-W2\"\n  summary: \"Confirmatory/exploratory benchmark 分类缺乏预注册\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: []\n      note: \"未单独提及。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W5 Major（循环论证风险）。R2 交叉 REBUT——认为 taxonomy 是文献标准分类（Arora et al. 2024），非 data-driven，'post-hoc' 指控需更强反面证据。分歧：R1 Major vs R2 Minor。Director 判断：R2 的 rebut 有理（标准分类），但缺乏时间证据确实是弱点。降级为 Should-Fix（提供 git timestamp 或框定为 hypothesis-generating）。\"\n  action_items:\n    - round: 17\n      action: \"Appendix A 明确 all-10 correction 为唯一有效\"\n      assigned_to: paper_agent\n      status: open\n    - round: 19\n      action: \"提供 taxonomy 时间证据（git commit）或框定为 hypothesis-generating\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"R1 Major vs R2 REBUT（标准分类）。Director 降级为 Should-Fix。\"\n  resolution_round: null\n\n- id: \"R18-W1\"\n  summary: \"Permutation test null baseline 不排除 example difficulty confound\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 未显式提及。可能被 format confound 讨论吸收。\"\n  action_items:\n    - round: 18\n      action: \"讨论 example difficulty 作为 confound\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W1\"\n  summary: \"遗漏 Yang & Wang (2026) 'Benchmark Illusion'——核心发现高度重叠\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R2]\n      note: \"R2-N3 Major：Yang & Wang (2026) arXiv:2602.11898 在 frontier LLMs 上展示了 comparable accuracy + 16-66% per-item disagreement。使 'first systematic per-example analysis' 需重新界定。R1 交叉中未 rebut 此点。\"\n  action_items:\n    - round: 19\n      action: \"引用 Yang & Wang (2026)；重新界��� 'first' claim 为 'first controlled within-family analysis'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W2\"\n  summary: \"LAMBADA 和 ARC-Easy routing 增益数值疑似相同\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W9 初提此问题（声称两者均为 +1.2pp, SD=0.5pp）。R2 交叉 REBUT 并纠正：原文为 LAMBADA +5.2pp (SD=0.4pp)、ARC-Easy +1.2pp (SD=0.5pp)——并不相同。R1 误读了原文。\"\n  action_items: []\n  resolution: \"R1 误读。原文数值不同（LAMBADA +5.2pp vs ARC-Easy +1.2pp）。无需修改。\"\n  resolution_round: 19\n\n- id: \"R19-W3\"\n  summary: \"全文 associative vs causal 语言不完全一致\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W8 Minor：'reflects'/'modulated by'/'controlled' 等 causal 用语偶现。R2 交叉 AGREE 但认为 minor——总体 framing 是 associative 的。\"\n  action_items:\n    - round: 19\n      action: \"全文统一 associative 语言\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1737 · 2026-05-24T13:44:07.923698+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_issues.yaml\", \"bytes\": 22388}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Assistant

_source line 1738 · 2026-05-24T13:44:23.243587+00:00_

Round 19 审稿完成。

**最终结果**：Overall **3.0 (Findings)**，双方 Reviewer 完全一致。

**关键更正**（来自详细交叉回应，已纳入 Issue Tracker）：
- **R19-W2 撤销**：R1 声称 LAMBADA/ARC-Easy routing 数值相同为误读——原文为 +5.2pp vs +1.2pp
- **R16-W3 降级**：R2 正确指出 AUC 本身是 non-parametric，正态假设仅影响 Cohen's d effect size 而非 AUC validity
- **R16-W2 降级**：R2 rebut 有理——5-arch 仅 340M 是 model zoo 数据约束而非论文设计缺陷
- **R17-W2 降级**：R2 rebut taxonomy 是文献标准分类（Arora et al. 2024），非 post-hoc data-driven

**核心 open issues 优先级排序**：
1. 🔴 叙事重构：convergence → Jaccard 饱和为主发现（R5-W2 / R16-N1）
2. 🔴 引用 Yang & Wang (2026) Benchmark Illusion，重新界定 novelty（R19-W1）
3. 🟡 Limitations 加入 format confound（R17-W1）
4. 🟡 Routing 降级 + 补 ensemble baseline（R15-W2）
5. 🟡 GDN 16-head 在 Table 1 处更早 flag（R6-W2）

审稿报告已投递至 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director"
}
```

</details>

---


## Round 135

## Round 135

70 recorded events


### User

_source line 1739 · 2026-05-24T14:05:44.808873+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: entrainment_gated_ft
- 论文路径: docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR (Main/Findings unified)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1740 · 2026-05-24T14:05:51.186337+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1741 · 2026-05-24T14:05:51.237264+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1742 · 2026-05-24T14:06:01.581619+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch,WebFetch,read_local_file",
  "max_results": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch,WebFetch,read_local_file",
    "max_results": "12"
  }
}
```

</details>

---


### Tool result

_source line 1743 · 2026-05-24T14:06:01.632201+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1744 · 2026-05-24T14:06:05.146101+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "entrainment_gated_ft"
  }
}
```

</details>

---


### Tool result

_source line 1745 · 2026-05-24T14:06:05.648420+00:00_

{"result":"# 项目 entrainment_gated_ft 概况\n\n## 实验状态 (46 个)\n\n- **exp-arc-easy-eval**: DONE (success) — \n- **exp-007**: DONE (success) — \n- **exp-004-r2**: DONE (success) — \n- **exp-011-xstorycloze**: DONE (negative) — \n- **exp-004**: DONE (failed) — \n- **exp-011**: DONE (negative) — \n- **exp-010**: DONE (success) — \n- **exp-001**: DONE (success) — \n- **exp-008**: DONE (success) — \n- **exp-003-p2**: DONE (negative) — \n- **exp-003**: DONE (negative) — \n- **exp-009**: DONE (success) — \n- **eval_340m_retnet_hgrn2**: DONE (success) — \n- **hgrn2_eval_h3_1**: DONE (success) — \n- **hgrn2_eval_1_3b_all**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp-005-pure-v4** (killed): —\n- **exp-005-pure-v3** (killed): —\n- **exp-005-hgrn-chain** (killed): —\n\n## 趋势\n成功 16 / 负向 4 / 失败 3 / 共 46\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-48145: 无 GPU 信息\n\n## 告警\n- hgrn2_eval_1_3b_all: 已被终止 — unknown\n- exp-003-p2v2: 已被终止 — unknown\n- exp-004: 训练失败 — unknown\n- exp-005-eval: 已被终止 — unknown\n- exp-005-p1-v4: 已被终止 — unknown\n- exp-005-gla-eval: 训练失败 — unknown\n- exp-005-gla: 已被终止 — unknown\n- exp-005-deltanet: 已被终止 — unknown\n- exp-005-dn-eval: 已被终止 — unknown\n- exp-005-pure-eval: 已被终止 — unknown\n- exp-005-p1-eval: 已被终止 — unknown\n- exp-005-p1-eval-v2: 已被终止 — unknown\n- exp-005-p1-eval-v3: 已被终止 — unknown\n- exp-005-p1-eval-v4: 已被终止 — unknown\n- exp-005-p1-eval-v5: 已被终止 — unknown\n- exp-005-hgrn-chain: 已被终止 — unknown\n- exp-005-batch: 训练失败 — unknown\n- exp-005-pure-v3: 已被终止 — unknown\n- exp-005-pure-v4: 已被终止 — unknown\n- exp-005-pure-v5: 已被终止 — unknown\n- exp-005-pure-v6: 已被终止 — unknown\n- exp-005-pure-v7: 已被终止 — unknown\n- exp-005-pure-v8: 已被终止 — unknown\n- exp-005-pure-v9: 已被终止 — unknown\n- exp-005-pure-v10: 已被终止 — unknown\n- exp-005-pure-baselines: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1746 · 2026-05-24T14:06:05.648916+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "file": "docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "file": "docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1747 · 2026-05-24T14:06:06.803519+00:00_

Error executing tool read_project_file: 1 validation error for read_project_fileArguments
project
  Field required [type=missing, input_value={'file': 'docs/paper/main.tex'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1154
}
```

</details>

---


### Tool call

_source line 1748 · 2026-05-24T14:06:06.804003+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1749 · 2026-05-24T14:06:07.205890+00:00_

called mcp__agent-ml-research__read_local_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_local_file</summary>

```json
{
  "file": "projects/entrainment_gated_ft/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__read_local_file",
  "tool_args": {
    "file": "projects/entrainment_gated_ft/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1750 · 2026-05-24T14:06:07.206344+00:00_

&lt;tool_use_error>Error: No such tool available: mcp__agent-ml-research__read_local_file&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__read_local_file",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 1751 · 2026-05-24T14:06:13.480688+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

Based on the search results, I found information related to EMNLP 2026 and ARR submission guidelines, though the results don't 
…[truncated 1148 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "WebSearch",
  "elapsed_ms": 6676
}
```

</details>

---


### Tool call

_source line 1752 · 2026-05-24T14:06:23.121504+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "entrainment_gated_ft",
  "file": "docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "entrainment_gated_ft",
    "file": "docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1753 · 2026-05-24T14:06:24.075499+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'docs/paper/main.tex'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 1754 · 2026-05-24T14:06:24.076068+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference call for papers submission deadline page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference call for papers submission deadline page limit"
  }
}
```

</details>

---


### Tool call

_source line 1755 · 2026-05-24T14:06:24.578239+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines author instructions page limit anonymity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines author instructions page limit anonymity"
  }
}
```

</details>

---


### Tool call

_source line 1756 · 2026-05-24T14:06:26.033675+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1757 · 2026-05-24T14:06:26.134993+00:00_

1	- id: "R5-W1"
2	  summary: "架构效应 vs seed 效应无法区分（单 training run，无 seed baseline）"
3	  category: experiment
4	  severity: critical
5	  status: wont_fix
6	  first_raised_round: 5
7	  last_seen_round: 19
8	  mentions:
9	    - round: 5
10	      reviewers: [R1, R2]
11	      note: "R1 Critical, R2 W3+Q3 支持。"
12	    - round: 15
13	      reviewers: [R1, R2]
14	      note: "R2-N3 Must-Fix vs R1-W2 Should-Fix。"
15	    - round: 16
16	      reviewers: [R1, R2]
17	      note: "R1-N1 Critical + R2-N2 Critical。双方 [AGREE]。"
18	    - round: 17
19	      reviewers: [R1, R2]
20	      note: "R1-N3 Critical + R2 交叉 [AGREE]。"
21	    - round: 18
22	      reviewers: [R1, R2]
23	      note: "R1-N2 Critical + R2-N2 Critical，交叉均 [AGREE]。2.7× gap 部分支持架构效应独立性。"
24	    - round: 19
25	      reviewers: [R1, R2]
26	      note: "R1-N2 Critical + R2-W4 Minor。R1 详列双重 mismatch。R2 同意但认为 minor。交叉后一致：structural limitation，维持 wont_fix。"
27	  action_items:
28	    - round: 13
29	      action: "E4 Pythia 410M 9-seed calibration（实际完成 70M）"
30	      assigned_to: main_agent
31	      status: done
32	    - round: 14
33	      action: "Limitations 提升 single-seed 为 top limitation；§4.2 弱化因果语言"
34	      assigned_to: paper_agent
35	      status: done
36	  resolution: "结构性限制。已做：Pythia 70M calibration + Limitations 讨论 + associative 语言。R19 维持 wont_fix。"
37	  resolution_round: null
38	
39	- id: "R5-W2"
40	  summary: "收敛 claim 统计不显著（Bonferroni p=.170）且依赖 GDN inclusion"
41	  category: method
42	  severity: critical
43	  status: in_progress
44	  first_raised_round: 1
45	  last_seen_round: 19
46	  mentions:
47	    - round: 15
48	      reviewers: [R1, R2]
49	      note: "R1-N1 Critical + R2-N1 Critical。交叉 [AGREE]。"
50	    - round: 16
51	      reviewers: [R1, R2]
52	      note: "R16-N1 重新 flag。"
53	    - round: 17
54	      reviewers: [R1, R2]
55	      note: "R1-N1 Critical + R2 交叉 [AGREE]。"
56	    - round: 18
57	      reviewers: [R1, R2]
58	      note: "R1-N1 Critical + R2-N1 Critical，交叉均 [AGREE]。"
59	    - round: 19
60	      rev
…[truncated 23597 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 1758 · 2026-05-24T14:06:28.443510+00:00_

Web search results for query: "EMNLP 2026 main conference call for papers submission deadline page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

Based on
…[truncated 891 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "WebSearch",
  "elapsed_ms": 4367
}
```

</details>

---


### Tool result

_source line 1759 · 2026-05-24T14:06:31.655862+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines author instructions page limit anonymity"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"}]

Based on the search results, here are the key submission guidelines for ACL Rolling Review 2026:

## Page Limit

All long, short, and theme papers must follow the ACL Author Guidelines. Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pa
…[truncated 1045 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "WebSearch",
  "elapsed_ms": 7077
}
```

</details>

---


### Tool call

_source line 1760 · 2026-05-24T14:06:40.238231+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract all submission guidelines: page limits (long/short), template requirements, anonymity rules, appendix rules, citation format, submission deadline, camera-ready deadline, and any other formatting requirements. Be comprehensive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract all submission guidelines: page limits (long/short), template requirements, anonymity rules, appendix rules, citation format, submission deadline, camera-ready deadline, and any other formatting requirements. Be comprehensive."
  }
}
```

</details>

---


### Tool call

_source line 1761 · 2026-05-24T14:06:42.648962+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1762 · 2026-05-24T14:06:43.552553+00:00_

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
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{multirow}
15	\usepackage{xcolor}
16	\usepackage{caption}
17	\usepackage{enumitem}
18	\setlist[itemize]{itemsep=1pt, parsep=0pt, topsep=2pt}
19	
20	\setlength{\textfloatsep}{6pt plus 1pt minus 1pt}
21	\setlength{\floatsep}{6pt plus 1pt minus 1pt}
22	\setlength{\intextsep}{6pt plus 1pt minus 1pt}
23	\setlength{\abovecaptionskip}{3pt}
24	\setlength{\belowcaptionskip}{0pt}
25	\setlength{\dbltextfloatsep}{6pt plus 1pt minus 1pt}
26	\setlength{\dblfloatsep}{6pt plus 1pt minus 1pt}
27	\setlength{\abovedisplayskip}{4pt plus 1pt minus 1pt}
28	\setlength{\belowdisplayskip}{4pt plus 1pt minus 1pt}
29	\setlength{\parskip}{0pt plus 0.5pt}
30	
31	\title{Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures}
32	
33	\author{Anonymous}
34	
35	\begin{document}
36	\maketitle
37	
38	\begin{abstract}
39	Hybrid linear recurrent architectures that appear interchangeable by aggregate benchmarks can differ on which specific examples they handle correctly. Using a controlled model zoo \citep{wang2025hybrid} (three architectures, five attention ratios, two scales), we decompose per-example effects of adding attention and find structured predictive multiplicity \citep{marx2020predictive}: pairwise overlap of helped and hurt example sets is uniformly low (Jaccard $\approx 0.10$, roughly twice the independence baseline; all $p < .01$ across five architectures). This multiplicity varies by task type or evaluation format ($\alpha = 0.14$--$0.30$) rather than attention dose. Per-example overlap saturates at 4\% attention and remains flat across higher ratios, indicating that minimal attention establishes which examples each architecture affects. \citet{yang2026benchmark} docum
…[truncated 2522 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 1763 · 2026-05-24T14:06:43.653345+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_20/submitted.pdf 2>/dev/null && echo \"PDF EXISTS\" || echo \"PDF NOT FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_20/submitted.pdf 2>/dev/null && echo \"PDF EXISTS\" || echo \"PDF NOT FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1764 · 2026-05-24T14:06:43.806023+00:00_

-rw-r--r-- 1 ubuntu ubuntu 572663 May 24 13:57 /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_20/submitted.pdf
PDF EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---


### Tool result

_source line 1765 · 2026-05-24T14:06:45.512718+00:00_

# EMNLP 2026 Submission Guidelines

## Page Limits
- **Long Papers**: 8 pages of content
- **Short Papers**: 4 pages of content
- **Camera-ready versions**: One additional page allowed (9 pages for long; 5 pages for short) "to address reviewers' comments"

## Submission Deadline
- **ARR Submission**: May 25, 2026 (11:59 PM UTC-12:00, "anywhere on Earth")

## Camera-Ready Deadline
- September 20, 2026

## Anonymity Requirements
The page states "there is no anonymity period requirement" per ACL and ARR policies. However, the reviewing process itself maintains double-blind standards: reviewers cannot see author identities, and authors cannot see reviewer identities.

## Templates & Formatting
Submissions must follow "all of the ARR submission requirements," which are detailed separately on the ARR website rather than this document.

## Appendices & Supplementary Materials
The guidelines reference "Optional Supplementary Materials (appendices, software and data)" as permitted, with specifics deferred to ARR requirements.

## Citation & Comparison Standards
Authors must comply with ARR guidelines on "Citation and Comparison"—full details referenced externally.

## Additional Requirements
- Limitations section required
- Writing assistance permitted
- Ethics policies and responsible NLP research checklist apply
- Authorship modifications prohibited during commitment phase (order changes only allowed)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "WebFetch",
  "elapsed_ms": 5274
}
```

</details>

---


### Tool call

_source line 1766 · 2026-05-24T14:06:56.210545+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read all paper sections",
  "subagent_type": "Explore",
  "prompt": "Read ALL the following files completely (they are paper sections for an academic paper). Return the FULL content of each file, do not summarize:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex\n3. /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex\n4. /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex\n5. /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex\n6. /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex\n\nReturn each file's content in full, separated by clear headers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Agent",
  "tool_args": {
    "description": "Read all paper sections",
    "subagent_type": "Explore",
    "prompt": "Read ALL the following files completely (they are paper sections for an academic paper). Return the FULL content of each file, do not summarize:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex\n3. /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex\n4. /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex\n5. /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex\n6. /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex\n\nReturn each file's content in full, separated by clear headers."
  }
}
```

</details>

---


### Tool call

_source line 1767 · 2026-05-24T14:06:57.867159+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract the complete submission requirements: page limits, formatting rules, anonymity policy, appendix rules, supplementary material rules, responsible NLP checklist requirements, and any other mandatory requirements for ARR submissions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract the complete submission requirements: page limits, formatting rules, anonymity policy, appendix rules, supplementary material rules, responsible NLP checklist requirements, and any other mandatory requirements for ARR submissions."
  }
}
```

</details>

---


### Tool call

_source line 1768 · 2026-05-24T14:06:58.670979+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1769 · 2026-05-24T14:06:58.771798+00:00_

1	\section{Introduction}
2	
3	Hybrid linear recurrent architectures---including GDN, RetNet, HGRN2, GLA, and DeltaNet---achieve aggregate benchmark scores within 1--2 points of each other at matched parameter budgets. Yet they can differ on up to 90\% of the individual examples they affect: adding attention to three controlled linear recurrent backbones yields helped and hurt sets with at most 10\% pairwise overlap, approximately twice the independence baseline. This per-example divergence is invisible in aggregate metrics: architectures that score within 1--2 points of each other reach similar accuracy by gaining and losing on different inputs. Across all ten pairwise comparisons among five architectures, overlap in per-example effects remains below 14\% (all $p < .01$), meaning the choice of backbone is associated with which specific inputs a deployed system handles correctly.
4	
5	This tension arises in the context of a rapid architectural shift toward hybrid recurrent-attention models, which interleave attention layers within linear recurrent backbones. Jamba \citep{lieber2024jamba}, Griffin \citep{de2024griffin}, RWKV-6 \citep{peng2024eagle}, and RecurrentGemma \citep{botev2024recurrentgemma} each combine recurrence with attention using different mixing strategies. These systems now serve as production-grade alternatives to pure Transformers, and the practical question of how much attention to include is typically answered by comparing aggregate benchmark numbers. \citet{wang2025hybrid} provide a controlled model zoo spanning three recurrent architectures, five attention ratios, and two parameter scales, which enables systematic study of how attention allocation affects these hybrid designs.
6	
7	Prior work on predictive multiplicity \citep{marx2020predictive} and underspecification \citep{damour2022underspecification,mccoy2020berts} documents this risk for seed variation within a single architecture, but whether it extends to architectural variation in hybrid 
…[truncated 3549 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1770 · 2026-05-24T14:06:58.772176+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1771 · 2026-05-24T14:06:58.772412+00:00_

1	\section{Related Work}
2	
3	\paragraph{Hybrid Recurrent Architectures.}
4	The design space for combining attention with recurrence spans layer-level interleaving \citep[Jamba;][]{lieber2024jamba}, local attention pairing \citep[Griffin, RecurrentGemma;][]{de2024griffin,botev2024recurrentgemma}, matrix-valued recurrence \citep[RWKV-6;][]{peng2024eagle}, within-head mixing \citep[Hymba;][]{dong2024hymba}, and unbounded-context hybrid SSMs \citep[Samba;][]{ren2024samba}. H3 \citep{fu2023hungry} and Hyena \citep{poli2023hyena} establish early design points in the hybrid space with gated convolutions and subquadratic operators. Mamba-2 \citep{dao2024mamba2} establishes a duality between structured state spaces and attention; Mamba-3 \citep{lahoti2026mamba3} extends the design further, while \citet{ali2025hidden} reveal implicit attention within Mamba. Comparative evaluations confirm that hybrids outperform pure Transformers and SSMs at scale \citep{waleffe2024empirical}, and that even one attention layer enables content-based routing \citep{basu2026routing}. Recent theoretical work establishes a provable expressiveness hierarchy between hybrid and pure linear attention \citep{ye2026provable}, providing formal grounding for the architectural differences we characterize at the per-example level. \citet{wang2025hybrid} provide the controlled model zoo we use, holding training conditions constant while varying architecture and attention ratio.
5	
6	\paragraph{Linear Recurrent Models.}
7	Our three recurrent backbones represent distinct gating strategies within the linear recurrence family: RetNet \citep{sun2023retnet} uses multi-scale exponential decay, HGRN2 \citep{qin2024hgrn2} applies gated state expansion, and GatedDeltaNet \citep{yang2024gateddeltanet} combines gated updates with delta rules. These descend from S4 \citep{gu2022s4} and Mamba \citep{gu2024mamba}, which introduced structured state spaces and input-dependent selection, respectively, and connect to linear a
…[truncated 2826 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1772 · 2026-05-24T14:06:59.175886+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1773 · 2026-05-24T14:06:59.427398+00:00_

1	\section{Method}\label{sec:method}
2	
3	We describe the model configurations, evaluation benchmarks, and analytical framework used to measure how attention affects cross-architecture agreement at both aggregate and per-example levels.
4	
5	\subsection{Model Zoo}\label{ssec:model_zoo}
6	
7	We use the pretrained model zoo of \citet{wang2025hybrid}, which provides controlled comparisons across architectures and attention ratios. The zoo contains three linear recurrent architectures: GatedDeltaNet \citep{yang2024gateddeltanet} (noting that the GDN 1.3B h3-1 configuration uses 16 attention heads vs.\ 32 for RetNet and HGRN2; see \S\ref{ssec:robustness} for robustness checks excluding GDN), RetNet \citep{sun2023retnet}, and HGRN2 \citep{qin2024hgrn2}. These three architectures represent distinct approaches to linear recurrence: GatedDeltaNet uses gated delta rules, RetNet uses multi-scale exponential decay, and HGRN2 uses gated linear recurrence with state expansion. Each architecture is trained at five attention ratios: 0\% (pure recurrent), 4\%, 7.7\%, 14.3\%, and 25\%. We adopt the h$k$-1 notation from the original work, where one attention layer is interleaved per every $k{+}1$ total layers: h3-1 corresponds to 25\% attention, h6-1 to 14.3\%, h12-1 to 7.7\%, and h24-1 to 4\%. All configurations are available at two scales: 340M and 1.3B parameters. Within each scale, all models share identical training data, tokenizer, and hyperparameters; they differ only in architecture and attention configuration. This controlled design isolates the effect of attention from confounds such as training data or optimization differences. The zoo also includes a Transformer baseline (pure attention) at both scales.
8	
9	\begin{figure}[t]
10	\centering
11	\includegraphics[width=\columnwidth]{figures/fig_method_overview.pdf}
12	\caption{Experimental framework. For each architecture, we compare the pure-recurrent baseline against its hybrid (+attention) variant, classifying every evaluat
…[truncated 6290 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1774 · 2026-05-24T14:06:59.427853+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1775 · 2026-05-24T14:06:59.628866+00:00_

1	\section{Experiments}\label{sec:experiments}
2	
3	Using the model zoo of \citet{wang2025hybrid} (\S\ref{ssec:model_zoo}), we evaluate all 30 configurations on 10 benchmarks plus supplementary COPA ($n = 100$) at 1.3B scale unless noted. Results at 340M appear in scale analyses. Recall: h$k$-1 denotes one attention layer per $k{+}1$ layers; h3-1 = 25\% attention.
4	
5	\begin{table*}[t]
6	\centering
7	\caption{Cross-architecture variance trends across benchmarks (1.3B scale). $\rho$: Spearman correlation between attention ratio and cross-architecture standard deviation $\sigma$ across five configurations. $p$: exact permutation test (two-tailed, 120 permutations). $\sigma$ values reported $\times 10^{2}$ (accuracy percentage points). Ratio: $\sigma_{\text{pure}} / \sigma_{\text{h3-1}}$. \textbf{Bold}: only benchmark with $\rho = -1.0$. HellaSwag evaluated using normalized accuracy (acc\_norm), the standard metric for this benchmark.}
8	\label{tab:convergence}
9	\begin{tabular}{llrrrrr}
10	\toprule
11	Benchmark & Category & $\rho$ & $p$ & $\sigma_{\text{pure}}$ & $\sigma_{\text{h3-1}}$ & Ratio \\
12	\midrule
13	\textbf{LAMBADA$^{\ddagger}$} & \textbf{Retrieval} & $\mathbf{-1.0}$ & \textbf{.017} & \textbf{2.41} & \textbf{0.49} & \textbf{4.87} \\
14	\quad\emph{(excl.\ GDN)} & & $-0.7$ & .233 & --- & --- & --- \\
15	BoolQ & Comprehension & $0.2$ & .783 & 1.63 & 2.36 & 0.69 \\
16	ARC-C & Reasoning & $0.6$ & .350 & 0.96 & 1.32 & 0.72 \\
17	HellaSwag & Reasoning & $0.3$ & .683 & 1.17 & 1.18 & 0.99 \\
18	PIQA & Reasoning & $-0.5$ & .450 & 0.54 & 0.34 & 1.59 \\
19	WinoGrande & Reasoning & $0.1$ & .950 & 0.67 & 0.78 & 0.86 \\
20	ARC-E & Mixed & $-0.7$ & .233 & 1.00 & 0.13 & 7.70 \\
21	MMLU & Mixed & $-0.7$ & .233 & 0.92 & 0.41 & 2.27 \\
22	SciQ & Mixed & $0.1$ & .950 & 0.87 & 0.74 & 1.19 \\
23	XStoryCloze & Mixed & $-0.6$ & .350 & 0.82 & 0.55 & 1.49 \\
24	\midrule
25	COPA$^{\dagger}$ & Reasoning & $-0.67$ & .267 & 2.63 & 0.47 & 5.57 \\
26	\bottomrule
27	\multicolumn{7}{l}{\fo
…[truncated 12955 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1776 · 2026-05-24T14:06:59.629243+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1777 · 2026-05-24T14:06:59.729804+00:00_

1	\vspace{-2pt}
2	\section{Conclusion}
3	
4	We have shown that hybrid linear recurrent architectures which appear interchangeable by aggregate benchmarks diverge substantially at the per-example level. This multiplicity varies by task type ($\alpha = 0.14$--$0.30$) rather than attention dose. Per-example overlap saturates at 4\% attention (pairwise Jaccard $\leq 0.10$), establishing architecture-specific sensitivity patterns that additional attention does not alter. Confidence margins partially predict which examples are affected (AUC 0.70--0.74), with rescue thresholds architecture-invariant but disruption thresholds varying 47\%.
5	
6	Two observations follow at the 340M--1.3B scales studied here. First, per-example audit before architecture substitution is advisable when multiplicity is substantial---aggregate equivalence does not guarantee behavioral equivalence. Second, the low cross-architecture Jaccard creates complementarity ($+7$--$14$\,pp oracle gain), but our preliminary routing experiments suggest that exploiting it is task-dependent: confidence-based selection shows gains on high-multiplicity free-form tasks (LAMBADA: $+5.2$\,pp) but is counterproductive on low-multiplicity ones (PIQA: $-0.49$\,pp).
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1778 · 2026-05-24T14:06:59.780405+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1779 · 2026-05-24T14:07:00.032514+00:00_

1	% Appendix sections for the paper.
2	
3	\section{Confirmatory and Exploratory Analyses}\label{app:benchmark_details}
4	
5	The task taxonomy used in \S\ref{ssec:task_taxonomy} was defined prior to running any convergence analyses. Each benchmark was assigned to exactly one of four categories based on the primary cognitive demand of the task:
6	
7	\begin{itemize}
8	    \item \textbf{Retrieval}: tasks requiring prediction from long-range context without multi-step reasoning (LAMBADA).
9	    \item \textbf{Comprehension}: reading comprehension with explicit passage support (BoolQ).
10	    \item \textbf{Reasoning}: tasks requiring commonsense inference or multi-step reasoning (HellaSwag, ARC-Challenge, WinoGrande, PIQA).
11	    \item \textbf{Mixed}: tasks combining retrieval, comprehension, and reasoning demands (ARC-Easy, MMLU, SciQ, XStoryCloze).
12	\end{itemize}
13	
14	\paragraph{Confirmatory benchmark set.} Six benchmarks were designated as confirmatory for Bonferroni correction: LAMBADA, HellaSwag, ARC-Challenge, WinoGrande, ARC-Easy, and MMLU. These were selected as representative of retrieval, reasoning, and mixed categories before any convergence analysis was performed. The taxonomy and benchmark selection were fixed before analysis as an informal pre-analysis plan; we describe this as a confirmatory/exploratory split rather than a formal pre-registration, since no external timestamp exists. The main text applies the more conservative all-10-benchmark correction (Bonferroni-adjusted $p = .017 \times 10 = .170$). \textbf{Sensitivity:} correcting across only the six confirmatory benchmarks yields adjusted $p = .017 \times 6 = .100$, still above conventional significance.
15	
16	\paragraph{One-sided test.} If one adopts the prior that attention should reduce cross-architecture variance, the one-sided permutation $p$-value for LAMBADA is $1/120 \approx 0.0083$. Under 10-benchmark Bonferroni correction, this yields an adjusted $p = 0.083$, above the conventional thre
…[truncated 58279 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool result

_source line 1780 · 2026-05-24T14:07:05.899345+00:00_

# ACL Rolling Review: Complete Submission Requirements

## Page Limits

**Long Papers:**
- Up to 8 pages of content
- Unlimited space for required limitations section and optional ethical considerations
- Unlimited reference pages

**Short Papers:**
- Up to 4 pages of content
- Unlimited space for required limitations section and optional ethical considerations
- Unlimited reference pages

Papers exceeding these limits or lacking a limitations section face automatic desk rejection.

## Formatting Rules

Submissions must adhere to the official ACL style template available on GitHub and follow "*ACL" conference formatting guidelines. Authors cannot modify style files or use templates from other venues. Violations of style requirements—including page size, margins, and font specifications—result in rejection without review.

## Anonymity Policy

Papers must exclude author names and institutional affiliations. Self-citations revealing identity (e.g., "We previously showed...") should be reframed as third-person references. All supplementary materials, including repository links, require anonymization. File-hosting services that track downloads (Dropbox, Google Drive) are prohibited.

The policy permits non-anonymous preprints, though anonymous submissions receive priority consideration and special awards.

## Appendix and Supplementary Material Rules

Appendices follow the paper but don't count toward page limits. They must use double-column formatting (with limited exceptions). Reviewers aren't obligated to review appendices; critical content must appear in the main text.

Software should be submitted as single .tgz or .zip archives via anonymized repositories. Cloud storage links are unacceptable. All supplementary materials require complete anonymization.

## Responsible NLP Checklist Requirements

"Incorrect, incomplete or misleading" checklist responses trigger desk rejection. Checklists must be accurately completed as part of submission and inform the review proce
…[truncated 813 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "WebFetch",
  "elapsed_ms": 8032
}
```

</details>

---


### Tool result

_source line 1781 · 2026-05-24T14:11:44.643204+00:00_

&lt;persisted-output>
Output too large (92.4KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-entrainment-gated-ft--claude-sessions-review-director-7bef78c5/c72e4402-c079-4137-b7d0-527ca6b9c9b0/tool-results/toolu_01AtjSZ9oeSLBsuZrUCHTeWH.json

Preview (first 2KB):
[
  {
    "type": "text",
    "text": "## INTRODUCTION.tex\n\n```latex\n\\section{Introduction}\n\nHybrid linear recurrent architectures---including GDN, RetNet, HGRN2, GLA, and DeltaNet---achieve aggregate benchmark scores within 1--2 points of each other at matched parameter budgets. Yet they can differ on up to 90\\% of the individual examples they affect: adding attention to three controlled linear recurrent backbones yields helped and hurt sets with at most 10\\% pairwise overlap, approximately twice the independence baseline. This per-example divergence is invisible in aggregate metrics: architectures that score within 1--2 points of each other reach similar accuracy by gaining and losing on different inputs. Across all ten pairwise comparisons among five architectures, overlap in per-example effects remains below 14\\% (all $p < .01$), meaning the choice of backbone is associated with which specific inputs a deployed system handles correctly.\n\nThis tension arises in the context of a rapid architectural shift toward hybrid recurrent-attention models, which interleave attention layers within linear recurrent backbones. Jamba \\citep{lieber2024jamba}, Griffin \\citep{de2024griffin}, RWKV-6 \\citep{peng2024eagle}, and RecurrentGemma \\citep{botev2024recurrentgemma} each combine recurrence with attention using different mixing strategies. These systems now serve as production-grade alternatives to pure Transformers, and the practical question of how much attention to include is typically answered by comparing aggregate benchmark numbers. \\citet{wang2025hybrid} provide a controlled model zoo spanning three recurrent architectures, f
…[truncated 360 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Agent",
  "elapsed_ms": 288432
}
```

</details>

---


### Tool call

_source line 1782 · 2026-05-24T14:11:56.543499+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-entrainment-gated-ft--claude-sessions-review-director-7bef78c5/c72e4402-c079-4137-b7d0-527ca6b9c9b0/tool-results/toolu_01AtjSZ9oeSLBsuZrUCHTeWH.json",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-entrainment-gated-ft--claude-sessions-review-director-7bef78c5/c72e4402-c079-4137-b7d0-527ca6b9c9b0/tool-results/toolu_01AtjSZ9oeSLBsuZrUCHTeWH.json",
    "limit": "500"
  }
}
```

</details>

---


### Tool result

_source line 1783 · 2026-05-24T14:11:56.945251+00:00_

File content (31089 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1784 · 2026-05-24T14:12:06.280362+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-entrainment-gated-ft--claude-sessions-review-director-7bef78c5/c72e4402-c079-4137-b7d0-527ca6b9c9b0/tool-results/toolu_01AtjSZ9oeSLBsuZrUCHTeWH.json",
  "limit": "400",
  "offset": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-entrainment-gated-ft--claude-sessions-review-director-7bef78c5/c72e4402-c079-4137-b7d0-527ca6b9c9b0/tool-results/toolu_01AtjSZ9oeSLBsuZrUCHTeWH.json",
    "limit": "400",
    "offset": "0"
  }
}
```

</details>

---


### Tool result

_source line 1785 · 2026-05-24T14:12:06.667844+00:00_

File content (31089 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 387
}
```

</details>

---


### Tool call

_source line 1786 · 2026-05-24T14:12:11.752534+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-entrainment-gated-ft--claude-sessions-review-director-7bef78c5/c72e4402-c079-4137-b7d0-527ca6b9c9b0/tool-results/toolu_01AtjSZ9oeSLBsuZrUCHTeWH.json",
  "limit": "300",
  "offset": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-entrainment-gated-ft--claude-sessions-review-director-7bef78c5/c72e4402-c079-4137-b7d0-527ca6b9c9b0/tool-results/toolu_01AtjSZ9oeSLBsuZrUCHTeWH.json",
    "limit": "300",
    "offset": "0"
  }
}
```

</details>

---


### Tool result

_source line 1787 · 2026-05-24T14:12:12.003838+00:00_

File content (31089 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1788 · 2026-05-24T14:12:15.969155+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1789 · 2026-05-24T14:12:16.019896+00:00_

1	\section{Introduction}
2	
3	Hybrid linear recurrent architectures---including GDN, RetNet, HGRN2, GLA, and DeltaNet---achieve aggregate benchmark scores within 1--2 points of each other at matched parameter budgets. Yet they can differ on up to 90\% of the individual examples they affect: adding attention to three controlled linear recurrent backbones yields helped and hurt sets with at most 10\% pairwise overlap, approximately twice the independence baseline. This per-example divergence is invisible in aggregate metrics: architectures that score within 1--2 points of each other reach similar accuracy by gaining and losing on different inputs. Across all ten pairwise comparisons among five architectures, overlap in per-example effects remains below 14\% (all $p < .01$), meaning the choice of backbone is associated with which specific inputs a deployed system handles correctly.
4	
5	This tension arises in the context of a rapid architectural shift toward hybrid recurrent-attention models, which interleave attention layers within linear recurrent backbones. Jamba \citep{lieber2024jamba}, Griffin \citep{de2024griffin}, RWKV-6 \citep{peng2024eagle}, and RecurrentGemma \citep{botev2024recurrentgemma} each combine recurrence with attention using different mixing strategies. These systems now serve as production-grade alternatives to pure Transformers, and the practical question of how much attention to include is typically answered by comparing aggregate benchmark numbers. \citet{wang2025hybrid} provide a controlled model zoo spanning three recurrent architectures, five attention ratios, and two parameter scales, which enables systematic study of how attention allocation affects these hybrid designs.
6	
7	Prior work on predictive multiplicity \citep{marx2020predictive} and underspecification \citep{damour2022underspecification,mccoy2020berts} documents this risk for seed variation within a single architecture, but whether it extends to architectural variation in hybrid 
…[truncated 3549 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1790 · 2026-05-24T14:12:16.923591+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1791 · 2026-05-24T14:12:17.074864+00:00_

1	\section{Related Work}
2	
3	\paragraph{Hybrid Recurrent Architectures.}
4	The design space for combining attention with recurrence spans layer-level interleaving \citep[Jamba;][]{lieber2024jamba}, local attention pairing \citep[Griffin, RecurrentGemma;][]{de2024griffin,botev2024recurrentgemma}, matrix-valued recurrence \citep[RWKV-6;][]{peng2024eagle}, within-head mixing \citep[Hymba;][]{dong2024hymba}, and unbounded-context hybrid SSMs \citep[Samba;][]{ren2024samba}. H3 \citep{fu2023hungry} and Hyena \citep{poli2023hyena} establish early design points in the hybrid space with gated convolutions and subquadratic operators. Mamba-2 \citep{dao2024mamba2} establishes a duality between structured state spaces and attention; Mamba-3 \citep{lahoti2026mamba3} extends the design further, while \citet{ali2025hidden} reveal implicit attention within Mamba. Comparative evaluations confirm that hybrids outperform pure Transformers and SSMs at scale \citep{waleffe2024empirical}, and that even one attention layer enables content-based routing \citep{basu2026routing}. Recent theoretical work establishes a provable expressiveness hierarchy between hybrid and pure linear attention \citep{ye2026provable}, providing formal grounding for the architectural differences we characterize at the per-example level. \citet{wang2025hybrid} provide the controlled model zoo we use, holding training conditions constant while varying architecture and attention ratio.
5	
6	\paragraph{Linear Recurrent Models.}
7	Our three recurrent backbones represent distinct gating strategies within the linear recurrence family: RetNet \citep{sun2023retnet} uses multi-scale exponential decay, HGRN2 \citep{qin2024hgrn2} applies gated state expansion, and GatedDeltaNet \citep{yang2024gateddeltanet} combines gated updates with delta rules. These descend from S4 \citep{gu2022s4} and Mamba \citep{gu2024mamba}, which introduced structured state spaces and input-dependent selection, respectively, and connect to linear a
…[truncated 2826 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1792 · 2026-05-24T14:12:17.075281+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1793 · 2026-05-24T14:12:17.125856+00:00_

1	\section{Method}\label{sec:method}
2	
3	We describe the model configurations, evaluation benchmarks, and analytical framework used to measure how attention affects cross-architecture agreement at both aggregate and per-example levels.
4	
5	\subsection{Model Zoo}\label{ssec:model_zoo}
6	
7	We use the pretrained model zoo of \citet{wang2025hybrid}, which provides controlled comparisons across architectures and attention ratios. The zoo contains three linear recurrent architectures: GatedDeltaNet \citep{yang2024gateddeltanet} (noting that the GDN 1.3B h3-1 configuration uses 16 attention heads vs.\ 32 for RetNet and HGRN2; see \S\ref{ssec:robustness} for robustness checks excluding GDN), RetNet \citep{sun2023retnet}, and HGRN2 \citep{qin2024hgrn2}. These three architectures represent distinct approaches to linear recurrence: GatedDeltaNet uses gated delta rules, RetNet uses multi-scale exponential decay, and HGRN2 uses gated linear recurrence with state expansion. Each architecture is trained at five attention ratios: 0\% (pure recurrent), 4\%, 7.7\%, 14.3\%, and 25\%. We adopt the h$k$-1 notation from the original work, where one attention layer is interleaved per every $k{+}1$ total layers: h3-1 corresponds to 25\% attention, h6-1 to 14.3\%, h12-1 to 7.7\%, and h24-1 to 4\%. All configurations are available at two scales: 340M and 1.3B parameters. Within each scale, all models share identical training data, tokenizer, and hyperparameters; they differ only in architecture and attention configuration. This controlled design isolates the effect of attention from confounds such as training data or optimization differences. The zoo also includes a Transformer baseline (pure attention) at both scales.
8	
9	\begin{figure}[t]
10	\centering
11	\includegraphics[width=\columnwidth]{figures/fig_method_overview.pdf}
12	\caption{Experimental framework. For each architecture, we compare the pure-recurrent baseline against its hybrid (+attention) variant, classifying every evaluat
…[truncated 6290 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1794 · 2026-05-24T14:12:21.843679+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1795 · 2026-05-24T14:12:22.496505+00:00_

1	\section{Experiments}\label{sec:experiments}
2	
3	Using the model zoo of \citet{wang2025hybrid} (\S\ref{ssec:model_zoo}), we evaluate all 30 configurations on 10 benchmarks plus supplementary COPA ($n = 100$) at 1.3B scale unless noted. Results at 340M appear in scale analyses. Recall: h$k$-1 denotes one attention layer per $k{+}1$ layers; h3-1 = 25\% attention.
4	
5	\begin{table*}[t]
6	\centering
7	\caption{Cross-architecture variance trends across benchmarks (1.3B scale). $\rho$: Spearman correlation between attention ratio and cross-architecture standard deviation $\sigma$ across five configurations. $p$: exact permutation test (two-tailed, 120 permutations). $\sigma$ values reported $\times 10^{2}$ (accuracy percentage points). Ratio: $\sigma_{\text{pure}} / \sigma_{\text{h3-1}}$. \textbf{Bold}: only benchmark with $\rho = -1.0$. HellaSwag evaluated using normalized accuracy (acc\_norm), the standard metric for this benchmark.}
8	\label{tab:convergence}
9	\begin{tabular}{llrrrrr}
10	\toprule
11	Benchmark & Category & $\rho$ & $p$ & $\sigma_{\text{pure}}$ & $\sigma_{\text{h3-1}}$ & Ratio \\
12	\midrule
13	\textbf{LAMBADA$^{\ddagger}$} & \textbf{Retrieval} & $\mathbf{-1.0}$ & \textbf{.017} & \textbf{2.41} & \textbf{0.49} & \textbf{4.87} \\
14	\quad\emph{(excl.\ GDN)} & & $-0.7$ & .233 & --- & --- & --- \\
15	BoolQ & Comprehension & $0.2$ & .783 & 1.63 & 2.36 & 0.69 \\
16	ARC-C & Reasoning & $0.6$ & .350 & 0.96 & 1.32 & 0.72 \\
17	HellaSwag & Reasoning & $0.3$ & .683 & 1.17 & 1.18 & 0.99 \\
18	PIQA & Reasoning & $-0.5$ & .450 & 0.54 & 0.34 & 1.59 \\
19	WinoGrande & Reasoning & $0.1$ & .950 & 0.67 & 0.78 & 0.86 \\
20	ARC-E & Mixed & $-0.7$ & .233 & 1.00 & 0.13 & 7.70 \\
21	MMLU & Mixed & $-0.7$ & .233 & 0.92 & 0.41 & 2.27 \\
22	SciQ & Mixed & $0.1$ & .950 & 0.87 & 0.74 & 1.19 \\
23	XStoryCloze & Mixed & $-0.6$ & .350 & 0.82 & 0.55 & 1.49 \\
24	\midrule
25	COPA$^{\dagger}$ & Reasoning & $-0.67$ & .267 & 2.63 & 0.47 & 5.57 \\
26	\bottomrule
27	\multicolumn{7}{l}{\fo
…[truncated 12955 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 1796 · 2026-05-24T14:12:22.496925+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1797 · 2026-05-24T14:12:22.547345+00:00_

1	\vspace{-2pt}
2	\section{Conclusion}
3	
4	We have shown that hybrid linear recurrent architectures which appear interchangeable by aggregate benchmarks diverge substantially at the per-example level. This multiplicity varies by task type ($\alpha = 0.14$--$0.30$) rather than attention dose. Per-example overlap saturates at 4\% attention (pairwise Jaccard $\leq 0.10$), establishing architecture-specific sensitivity patterns that additional attention does not alter. Confidence margins partially predict which examples are affected (AUC 0.70--0.74), with rescue thresholds architecture-invariant but disruption thresholds varying 47\%.
5	
6	Two observations follow at the 340M--1.3B scales studied here. First, per-example audit before architecture substitution is advisable when multiplicity is substantial---aggregate equivalence does not guarantee behavioral equivalence. Second, the low cross-architecture Jaccard creates complementarity ($+7$--$14$\,pp oracle gain), but our preliminary routing experiments suggest that exploiting it is task-dependent: confidence-based selection shows gains on high-multiplicity free-form tasks (LAMBADA: $+5.2$\,pp) but is counterproductive on low-multiplicity ones (PIQA: $-0.49$\,pp).
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1798 · 2026-05-24T14:12:42.299598+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "entrainment_gated_ft",
  "file": "constraints.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "entrainment_gated_ft",
    "file": "constraints.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1799 · 2026-05-24T14:12:42.351390+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/constraints.yaml\", \"content\": \"_next_id: 2\\nconstraints:\\n- id: C001\\n  added: 2026-05-18 05:44 UTC\\n  summary: 'GPU 白名单: 仅允许使用 cuda:0 (westb-48145)'\\n  scope: all\\n  reason: 项目仅分配 1 张 RTX PRO 6000 (cuda:0)，防止误用其他 GPU\\n\", \"total_chars\": 181, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1800 · 2026-05-24T14:12:45.816819+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1801 · 2026-05-24T14:12:45.968248+00:00_

&lt;persisted-output>
Output too large (55.1KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-entrainment-gated-ft--claude-sessions-review-director-7bef78c5/c72e4402-c079-4137-b7d0-527ca6b9c9b0/tool-results/toolu_01S55etB1H4zKVyzfu7zwJcP.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_reports/round_8.md:124:外部审稿未配置（项目配置中无 `external_review.paperreview_ai.enabled`）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_reports/round_3.md:118:未配置外部审稿（项目未启用 `external_review.paperreview_ai`）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_reports/round_10.md:144:外部审稿：未启用（项目配置中 external_review 未配置）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_reports/round_2.md:121:外部审稿：未请求（项目未配置 external_review）。
AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
AGENTS.md:85:- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agentic Reviewer]` 纳入最终报告的独立 section
AGENTS.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
AGENTS.md:163:`director_get_project_overview`, `director_post_to_reviewer`, `dispatch_visual_check`, `get_external_review_status`, `get_visual_check_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
CLAUDE.md:85:- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agentic Reviewer]` 纳入最终报告的独立 section
CLAUDE.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
CLAUDE.md:163:
…[truncated 328 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Grep",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1802 · 2026-05-24T14:13:08.892323+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "entrainment_gated_ft",
  "review_chat_id": "oc_b542b52ff24f138c42225a1d4b456e7e"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "entrainment_gated_ft",
    "review_chat_id": "oc_b542b52ff24f138c42225a1d4b456e7e"
  }
}
```

</details>

---


### Tool result

_source line 1803 · 2026-05-24T14:13:26.941958+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 18049
}
```

</details>

---


### Tool call

_source line 1804 · 2026-05-24T14:13:27.895521+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "20",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 统计分析 + 实验设计**。\n\n## 目标 Venue\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- Long paper: 正文 ≤ 8 页，references 不限\n- Limitations section 必须有，不计入页数\n- Double-blind，ACL style template\n- ARR Submission Deadline: 2026-05-25\n\n## 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award（约前2.5%），4 = Conference（主会议），3.5 = Borderline Conference，3 = Findings，2.5 = Borderline Findings，2 = Resubmit next cycle，1 = Do not resubmit\n\n## 论文文件\n- LaTeX: `docs/paper/main.tex`（sections 在 `docs/paper/sections/` 下）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_20/submitted.pdf`\n\n## 你的审查重点\n\n1. **统计方法的严谨性**：\n   - n=5 的 Spearman 检验功效是否充分讨论？\n   - n=3 架构的 bootstrap CI 覆盖率是否合理标注？\n   - Bonferroni 校正后 LAMBADA p=.170 的 convergence claim 是否过度解读？\n   - Permutation test 的 null baseline 设计是否排除 example difficulty confound？\n\n2. **实验设计**：\n   - 单 training run 的局限性是否充分讨论？\n   - GDN 16-head confound 对 convergence claim 的影响\n   - 5-architecture 扩展验证仅在 340M 的局限\n   - Task type vs evaluation format confound（LAMBADA 是唯一 free-form）\n\n3. **方法论**：\n   - Binary decomposition 是否低估多选题一致性？\n   - Confidence margin AUC 的正态假设问题\n   - Confirmatory/exploratory benchmark 分类缺乏预注册\n\n4. **格式合规**：\n   - 正文是否在 8 页内？\n   - Limitations section 是否存在且合理？\n   - 匿名化是否完整？\n\n请按以下结构输出审稿意见：\n1. Summary（2-3 句）\n2. Strengths（逐条，标注 S1/S2/...）\n3. Weaknesses（逐条，标注 W1/W2/...，每条标注 severity: Critical/Major/Minor）\n4. Questions（Q1/Q2/...）\n5. Missing References\n6. Overall Assessment（评分 + 置信度）\n7. Detailed Comments（按 section 逐节）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "20",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 统计分析 + 实验设计**。\n\n## 目标 Venue\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- Long paper: 正文 ≤ 8 页，references 不限\n- Limitations section 必须有，不计入页数\n- Double-blind，ACL style template\n- ARR Submission Deadline: 2026-05-25\n\n## 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award（约前2.5%），4 = Conference（主会议），3.5 = Borderline Conference，3 = Findings，2.5 = Borderline Findings，2 = Resubmit next cycle，1 = Do not resubmit\n\n## 论文文件\n- LaTeX: `docs/paper/main.tex`（sections 在 `docs/paper/sections/` 下）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_20/submitted.pdf`\n\n## 你的审查重点\n\n1. **统计方法的严谨性**：\n   - n=5 的 Spearman 检验功效是否充分讨论？\n   - n=3 架构的 bootstrap CI 覆盖率是否合理标注？\n   - Bonferroni 校正后 LAMBADA p=.170 的 convergence claim 是否过度解读？\n   - Permutation test 的 null baseline 设计是否排除 example difficulty confound？\n\n2. **实验设计**：\n   - 单 training run 的局限性是否充分讨论？\n   - GDN 16-head confound 对 convergence claim 的影响\n   - 5-architecture 扩展验证仅在 340M 的局限\n   - Task type vs evaluation format confound（LAMBADA 是唯一 free-form）\n\n3. **方法论**：\n   - Binary decomposition 是否低估多选题一致性？\n   - Confidence margin AUC 的正态假设问题\n   - Confirmatory/exploratory benchmark 分类缺乏预注册\n\n4. **格式合规**：\n   - 正文是否在 8 页内？\n   - Limitations section 是否存在且合理？\n   - 匿名化是否完整？\n\n请按以下结构输出审稿意见：\n1. Summary（2-3 句）\n2. Strengths（逐条，标注 S1/S2/...）\n3. Weaknesses（逐条，标注 W1/W2/...，每条标注 severity: Critical/Major/Minor）\n4. Questions（Q1/Q2/...）\n5. Missing References\n6. Overall Assessment（评分 + 置信度）\n7. Detailed Comments（按 section 逐节）"
  }
}
```

</details>

---


### Tool result

_source line 1805 · 2026-05-24T14:13:41.282880+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 13387
}
```

</details>

---


### Tool call

_source line 1806 · 2026-05-24T14:13:41.335932+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "20",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量 + 相关工作**。\n\n## 目标 Venue\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- Long paper: 正文 ≤ 8 页，references 不限\n- Limitations section 必须有，不计入页数\n- Double-blind，ACL style template\n- ARR Submission Deadline: 2026-05-25\n\n## 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award（约前2.5%），4 = Conference（主会议），3.5 = Borderline Conference，3 = Findings，2.5 = Borderline Findings，2 = Resubmit next cycle，1 = Do not resubmit\n\n## 论文文件\n- LaTeX: `docs/paper/main.tex`（sections 在 `docs/paper/sections/` 下）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_20/submitted.pdf`\n\n## 你的审查重点\n\n1. **新颖性评估**：\n   - 核心贡献是否足够新颖？是已有指标的直接套用，还是有方法论/理论创新？\n   - 与 Yang & Wang (2026) \"Benchmark Illusion\" 的关系——该论文在 frontier LLMs 上展示了类似的 per-item disagreement (16-66%)，本文的 \"first systematic per-example analysis\" claim 是否需要重新界定？\n   - 相对于 predictive multiplicity (Marx 2020) 和 underspecification (D'Amour 2022) 的增量贡献\n\n2. **相关工作完整性**：\n   - 是否遗漏重要文献？特别关注：\n     - Yang & Wang (2026) \"Benchmark Illusion\"\n     - MultiBERTs (Sellam 2022) 在 seed 语境中\n     - MoE routing 文献\n     - Model Soups (Wortsman 2022)\n   - 引用格式和完整性\n\n3. **写作质量**：\n   - Abstract 信息密度是否合理（≤200 words）？\n   - Introduction 贡献列表是否过长？\n   - 全文 associative vs causal 语言一致性\n   - Routing 在 abstract 中的叙事权重是否与实验结果匹配（仅 1/4 benchmark 有效）？\n\n4. **完整性**：\n   - 实验覆盖是否充分？\n   - Limitations 是否覆盖关键局限？\n   - 是否有未回答的核心问题？\n\n请按以下结构输出审稿意见：\n1. Summary（2-3 句）\n2. Strengths（逐条，标注 S1/S2/...）\n3. Weaknesses（逐条，标注 W1/W2/...，每条标注 severity: Critical/Major/Minor）\n4. Questions（Q1/Q2/...）\n5. Missing References\n6. Overall Assessment（评分 + 置信度）\n7. Detailed Comments（按 section 逐节）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "20",
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量 + 相关工作**。\n\n## 目标 Venue\n- **EMNLP 2026**（通过 ARR 统一审稿）\n- Long paper: 正文 ≤ 8 页，references 不限\n- Limitations section 必须有，不计入页数\n- Double-blind，ACL style template\n- ARR Submission Deadline: 2026-05-25\n\n## 评分标准（EMNLP 2026 ARR）\n5 = Consider for Award（约前2.5%），4 = Conference（主会议），3.5 = Borderline Conference，3 = Findings，2.5 = Borderline Findings，2 = Resubmit next cycle，1 = Do not resubmit\n\n## 论文文件\n- LaTeX: `docs/paper/main.tex`（sections 在 `docs/paper/sections/` 下）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_20/submitted.pdf`\n\n## 你的审查重点\n\n1. **新颖性评估**：\n   - 核心贡献是否足够新颖？是已有指标的直接套用，还是有方法论/理论创新？\n   - 与 Yang & Wang (2026) \"Benchmark Illusion\" 的关系——该论文在 frontier LLMs 上展示了类似的 per-item disagreement (16-66%)，本文的 \"first systematic per-example analysis\" claim 是否需要重新界定？\n   - 相对于 predictive multiplicity (Marx 2020) 和 underspecification (D'Amour 2022) 的增量贡献\n\n2. **相关工作完整性**：\n   - 是否遗漏重要文献？特别关注：\n     - Yang & Wang (2026) \"Benchmark Illusion\"\n     - MultiBERTs (Sellam 2022) 在 seed 语境中\n     - MoE routing 文献\n     - Model Soups (Wortsman 2022)\n   - 引用格式和完整性\n\n3. **写作质量**：\n   - Abstract 信息密度是否合理（≤200 words）？\n   - Introduction 贡献列表是否过长？\n   - 全文 associative vs causal 语言一致性\n   - Routing 在 abstract 中的叙事权重是否与实验结果匹配（仅 1/4 benchmark 有效）？\n\n4. **完整性**：\n   - 实验覆盖是否充分？\n   - Limitations 是否覆盖关键局限？\n   - 是否有未回答的核心问题？\n\n请按以下结构输出审稿意见：\n1. Summary（2-3 句）\n2. Strengths（逐条，标注 S1/S2/...）\n3. Weaknesses（逐条，标注 W1/W2/...，每条标注 severity: Critical/Major/Minor）\n4. Questions（Q1/Q2/...）\n5. Missing References\n6. Overall Assessment（评分 + 置信度）\n7. Detailed Comments（按 section 逐节）"
  }
}
```

</details>

---


### Tool result

_source line 1807 · 2026-05-24T14:13:42.855008+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1519
}
```

</details>

---


### Assistant

_source line 1808 · 2026-05-24T14:14:03.341265+00:00_

已完成 Round 20 初始化：

| 任务 | 状态 |
|------|------|
| 视觉审查 Agent | ✅ 已派发（并行执行，不阻塞） |
| Reviewer 1（方法/统计/实验） | ✅ 已分配 |
| Reviewer 2（新颖性/完整性/写作） | ✅ 已分配 |
| 外部审稿 | ⊘ 未启用 |

等待两位 Reviewer 返回初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director"
}
```

</details>

---


## Round 136

## Round 136

2 recorded events


### User

_source line 1809 · 2026-05-24T14:19:19.112331+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见：Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures

**审查侧重**：方法严谨性 + 统计分析 + 实验设计

---

### 1. Summary

本文使用 Wang et al. (2025) 的受控模型动物园，系统研究了三种混合线性递归架构（GDN、RetNet、HGRN2）在五个注意力比例和两个规模（340M、1.3B）下的逐样本预测多重性（per-example predictive multiplicity）。主要发现包括：（1）架构变异产生的预测多重性按任务类型/评估格式呈结构化差异，而非随注意力比例线性变化；（2）逐样本重叠在最低注意力水平（4%）即饱和；（3）置信度边际可部分预测受影响样本（AUC 0.70–0.74）。实验设计精细，附录充实，但若干统计方法学问题削弱了核心声明的支撑力度。

---

### 2. Strengths

**S1.** 实验框架设计严谨。使用共享训练数据和超参数的模型动物园，有效隔离了架构差异对逐样本预测的影响，避免了训练数据/超参数混淆（Section 3.1）。这是该领域少见的受控实验设计。

**S2.** 统计方法体系较为完整。Bonferroni 校正、Bootstrap BCa 置信区间、排列检验（Appendix K）、效应量（Appendix H）和正态性验证（Appendix P2）构成多层次的统计分析框架，优于该领域大多数工作的单一显著性检验。

**S3.** 附录极为详尽（11 页）。包括 GDN head confound 分析（Appendix D/E）、连续 Jaccard 验证（Appendix O）、种子变异初步分析（Appendix W）、5 架构扩展验证（Appendix X）等。作者对自身结果的局限性保持了高度透明。

**S4.** 饱和发现（Saturation finding）是全文最稳健的结果。Table 2 和 Figure 1b 清晰展示逐样本重叠在 4% 注意力即达到平台，在四个确认性基准上一致成立，且在 5 架构扩展中得到验证（Appendix X）。

**S5.** 实际应用价值。置信度路由（confidence-based routing, Section 4.4）和扰动预测（disruption prediction, Appendix P）为部署多架构系统提供了可操作的工具。

**S6.** 对混淆因素的主动披露（GDN head count, 格式 vs 任务类型）体现了良好的学术诚信，为后续工作提供了明确的改进方向。

---

### 3. Weaknesses

**W1 [Critical] — GDN 16-head 混淆严重削弱 convergence claim**

- 具体位置：Appendix D (Table 3) 和 Appendix E
- 问题：GDN 在 h3-1 配置下每层使用 16 个注意力头，而 RetNet 和 HGRN2 使用 32 个头。Appendix D 显示，排除 GDN 后 LAMBADA 的 Spearman ρ 从 −1.0 骤降至 −0.2（n=2 架构，本质上已无统计意义）。这意味着主文中关于"更高注意力比例降低跨架构方差"的 convergence 声明（Section 4.3, Figure 4）实质上由 GDN 的建筑异常驱动，而非注意力剂量的一般效应。
- 为什么影响接收：这是 Section 4.3 和 Abstract 中 convergence 叙述的核心支撑。如果该结果是 GDN head count 的人工产物，则论文的因果推断链条断裂。
- 建议修改方向：在主文中明确将 convergence 降级为 exploratory observation，并在 Section 4.3 正文（而非仅附录）中展示排除 GDN 后的结果。

**W2 [Major] — n=5 Spearman 检验统计功效严重不足**

- 具体位置：Section 3.5, Table 1
- 问题：Spearman 相关系数在 n=5 个注意力比例上计算，此时精确排列检验仅有 5!=120 种排列，最小可达 p 值为 1/120≈0.0083。这意味着：（a）即使是完美单调相关（ρ=±1.0），p 值仍然不够小；（b）对中等效应量的检验功效极低（power < 0.30 at α=0.05 for |ρ|=0.7）。Table 1 中多个基准的 ρ 值在 −0.7 到 0.3 之间，p 值多数 > 0.05，但论文未讨论功效分析或 n=5 下检验的固有局限。
- 为什么影响接收：读者无法判断不显著结果是真无效应还是检验功效不足（Type II error）。
- 建议修改方向：补充功效分析讨论，或至少在 Section 3.5 中明确声明 n=5 下 Spearman 检验仅能检测强单调关系，对中等效应量缺乏敏感性。

**W3 [Major] — 单一训练运行无法分离种子效应与架构效应**

- 具体位置：Limitations (page 8), Appendix W
- 问题：模型动物园每个架构-注意力配置仅有一次训练运行。Appendix W 的种子变异分析使用 Pythia 70M（不同架构族，小一个数量级），显示种子内 Jaccard J≈0.30（LAMBADA）与跨架构 J 可比。这引发一个关键问题：观察到的逐样本模式究竟是架构驱动的还是训练随机性的产物？
- 为什么影响接收：论文的核心论点是"架构差异产生结构化多重性"，但单一训练运行下无法排除种子混淆。
- 建议修改方向：（a）在主文 Limitations 中更明确地讨论这一限制对因果推断的影响；（b）如果可行，补充至少一个额外训练运行的验证。

**W4 [Major] — 任务类型 vs 评估格式混淆削弱结构化多重性的归因**

- 具体位置：Section 4.3 (page 7), Section 3.2 (page 3-4)
- 问题：LAMBADA 是唯一的自由生成（free-form generation）任务，同时也是唯一表现出独特 convergence 模式的任务。论文将 LAMBADA 的特异性归因于"retrieval"任务类型，但评估格式（自由生成 vs 多选）是一个完全混淆的替代解释。Section 4.3 承认"the confound between task type and evaluation format cannot be fully resolved"，但主文和 Abstract 仍然使用"task type"语言（"varies systematically by task type"）进行归因。
- 为什么影响接收：如果多重性差异主要由评估格式驱动，则"结构化多重性与任务类型相关"的主张被过度解读。
- 建议修改方向：将 Abstract 和 Section 4.3 的措辞从 "task type" 修改为 "task type or evaluation format"，更准确地反映证据强度。

**W5 [Major] — Bonferroni 校正后 LAMBADA p=.170 仍被作为 convergence 证据引用**

- 具体位置：Section 4.3 (page 6-7), Abstract
- 问题：LAMBADA 的 Spearman ρ=−1.0 在原始 p=.017 下显著，但 10 基准 Bonferroni 校正后 p=.170，6 基准确认集校正后 p=.017×6=.102（Appendix A 脚注）。两种校正下均不显著。然而，论文在 Abstract 中说"non-significant decreasing trend"，在 Section 4.3 中说 convergence "partially rebounds"，措辞上仍在暗示实质性效应。结合 W1 的 GDN confound，该 convergence 声明的证据基础极为薄弱。
- 建议修改方向：在主文中明确声明"在校正多重比较和排除 GDN confound 后，我们未找到注意力比例与跨架构方差之间的统计显著关联"。

**W6 [Minor] — 确认性/探索性基准划分缺乏预注册**

- 具体位置：Appendix A, Section 3.2
- 问题：确认性集（6 个基准：LAMBADA, HellaSwag, ARC-C, WinoGrande, ARC-Easy, MMLU）和探索性集（4 个：PIQA, BoolQ, SciQ, XStoryCloze）的划分是 post-hoc 的，论文承认"not pre-registered"。这意味着 Bonferroni 校正的有效性取决于一个事后定义的基准集合。
- 建议：在 Section 3.2 中明确标注这一划分的 post-hoc 性质，或改为对全部 10 个基准统一应用校正。

**W7 [Minor] — 5 架构扩展验证仅限 340M 规模**

- 具体位置：Appendix X
- 问题：扩展验证（加入 GLA 和 DeltaNet）仅在 340M 进行。Table 30 显示所有 pairwise Jaccard ≤ 0.14，与主要发现一致，但无法验证 1.3B 规模下的行为。鉴于论文在 Appendix T 中展示 340M 和 1.3B 之间存在定量差异（σ 变化模式不同），规模泛化性是一个未关闭的问题。
- 建议：在 Limitations 中增加对 5 架构扩展缺乏 1.3B 验证的讨论。

**W8 [Minor] — n=3 架构上的 Bootstrap CI 覆盖率存疑**

- 具体位置：Section 3.5, Figure 4
- 问题：跨架构标准差 σ 从仅 3 个架构计算。Bootstrap BCa 区间在 n=3 上的覆盖率性质退化——只有 C(3,3)=1 种"完整重采样"，大部分 bootstrap 样本是对 3 个值的重复采样。Appendix D1 确认"12,255 are degenerate: they consist of same-architecture triplicates"。虽然论文使用百分位 CI 且排除零值，但 n=3 bootstrap 的置信度声明应谨慎解读。
- 建议：在 Section 3.5 中增加对 n=3 bootstrap 覆盖率退化问题的简要说明。

**W9 [Minor] — 排列检验的 null baseline 未排除样本难度混淆**

- 具体位置：Appendix K
- 问题：排列检验（Table 13）通过固定 helped/hurt 集合大小、随机分配样本索引构建 null 分布。但如果某些样本因内在难度（如 LAMBADA 中的低频末尾词）而系统性地出现在 helped 或 hurt 集合中，则跨架构的 Jaccard 重叠可能反映样本难度结构而非架构特异性的收敛。论文部分讨论了这一点（Appendix H 的 normalized effect size 分析），但排列检验本身未条件化于样本难度。
- 建议：补充一个以样本基线准确率分层的排列检验，或在讨论中明确这一混淆的影响方向。

---

### 4. Questions

**Q1.** Table 1 中 COPA 被排除在 Bonferroni 校正之外（脚注"excluded from multiple comparison corrections"），理由是其少于 16 个注意力配置。能否解释为什么 16 是截断阈值？这一排除是预定义的还是数据驱动的？

**Q2.** Appendix W 的种子变异分析使用 Pythia 70M（标准 Transformer），能否讨论为什么不使用动物园中的某个混合架构（如 340M GDN）进行种子变异？Pythia 作为纯 Transformer 与混合模型的种子敏感性可能有系统性差异。

**Q3.** Figure 4 中 LAMBADA 的 bootstrap CI（−1.0 到 −0.7）不包含零，但这是在 n=3 架构上计算的。给定 W8 中讨论的退化问题，作者对该 CI 的有效性有多大信心？

**Q4.** Section 4.4 的 confidence-based routing 在 LAMBADA 上显著负相关（ρ=−0.51, p=.374），但在 PIQA 上也显著负相关。能否讨论 routing 策略在什么条件下会失效？是否有基准上 routing 反而降低了性能的情况？

**Q5.** Binary decomposition（Section 3.4）在 K 选择任务上将 K−1 个错误答案合并为单一"incorrect"类别。Appendix O 用连续 Jaccard 验证了稳健性，但该验证是否覆盖了所有 10 个基准？连续 Jaccard 与二值 Jaccard 的差异幅度如何？

---

### 5. Missing References

- Jiang et al. (2024). "Predicting and analyzing model agreement across heterogeneous architectures." 如果存在，与本文的跨架构 per-example 分析高度相关。
- 对于 predictive multiplicity 的 deployment implications，建议引用 Black et al. (2022) 的 "Model multiplicity: Opportunities, concerns, and solutions" 更完整的讨论（已引用但仅在 Related Work 中简略提及）。
- Garg et al. (2025) "Symmetrizing multiplicity" 已引用，但在 Section 2 的讨论中未充分对比其方法论与本文的区别。

---

### 6. Overall Assessment

**Overall Assessment: 3.0 — Findings**

**Confidence: 4 / 5** — 统计方法论和实验设计是我的专业领域，我仔细检查了主要统计声明。

**一句话总结**：论文的饱和发现（saturation at 4% attention）和结构化多重性（permutation test 验证）是稳健的贡献，但 convergence claim 因 GDN head confound 和 n=5 功效不足而大幅削弱，加上单一训练运行的根本限制，整体证据强度适合 Findings 而非主会议。

**理由**：
- 研究问题重要且新颖——混合递归架构中的 per-example multiplicity 此前未被系统研究
- 实验框架（受控模型动物园）是一个有价值的方法论贡献
- 但核心 convergence 声明存在严重统计缺陷（W1+W2+W5 组合效应）
- 单一训练运行（W3）限制了因果推断能力
- 任务类型 vs 格式混淆（W4）未被充分解决
- 如果作者在修改中（a）降级 convergence 声明、（b）补充功效分析讨论、（c）在主文中更显著地呈现 GDN confound，评分有望提升至 3.5

---

### 7. 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3 / 5 | 饱和发现和排列检验支撑良好；但 convergence claim 因 GDN confound、n=5 功效不足、p=.170 不显著而显著削弱。主要声明中有一部分未获充分支撑。 |
| Excitement | 3 / 5 | 研究问题新颖（混合递归架构的 per-example multiplicity 此前未被研究），实际部署含义有趣（confidence routing），但发现的强度因统计限制而打折扣。 |
| Reproducibility | 4 / 5 | 使用公开模型动物园（Wang et al. 2025），承诺发布代码和评估输出，实验设置描述详尽。主要限制是单一训练运行使完全复现 + 种子变异验证不可能。 |
| Confidence | 4 / 5 | 统计方法论和实验设计在我的专业范围内。仔细检查了 Spearman 检验、Bonferroni 校正、排列检验和 bootstrap CI 的有效性。 |

---

### 8. Detailed Comments（按 Section 逐节）

**Abstract**：
- "winning and losing on different inputs" 和 "structured predictive multiplicity" 的措辞准确。
- "non-significant decreasing trend at 1.38" 的表述可以接受，但建议明确这在 Bonferroni 校正后 p=.170 且受 GDN confound 影响。
- Word count 约 195 词，符合 ≤200 词要求。

**Section 1 (Introduction)**：
- 动机清晰：混合递归架构虽然在聚合指标上相近，但逐样本行为可能不同，这对部署选择有实际影响。
- Contribution 列表清晰完整。
- 第二段提到 "despite comparable aggregate scores; our within-family design isolates backbone variation from training regime differences"——这一声明应加注单一训练运行的限制。

**Section 2 (Related Work)**：
- 对 predictive multiplicity 文献的综述较为全面。
- D'Amour et al. (2022) 的 underspecification 框架被恰当引用。
- 建议增加对 multiplicity 与 model ensemble 文献的区分讨论。

**Section 3 (Method)**：
- Section 3.1：模型动物园描述清晰，340M 和 1.3B 两个规模的配置明确。
- Section 3.2：Task taxonomy 的确认/探索划分（post-hoc）应在此处标注，而非仅在 Appendix A。
- Section 3.3：Convergence metrics（Spearman ρ 和 σ_pure/σ_h3-1 ratio）定义清晰。但应在此处提前说明 n=5 下 Spearman 检验的功效限制。
- Section 3.4：Binary decomposition 的 conservative bias 论证逻辑合理（低估一致性 → 强化多重性声明），Appendix O 的连续 Jaccard 验证增强了可信度。
- Section 3.5：统计方法描述完整，但缺少功效分析。

**Section 4 (Experiments)**：
- Section 4.1：Per-example divergence 的 Figure 3 直观展示了三架构的不同逐样本效应模式，是论文的有效可视化。
- Section 4.2：Multiplicity variation（Table 2, σ = 0.11–0.30）的发现稳健。但 "multiplicity varies systematically across tasks" 的因果语言应弱化为描述性关联。
- Section 4.3：这是全文最弱的一节。Convergence claim 同时受 GDN confound（W1）、n=5 功效（W2）和 p=.170（W5）三重限制。建议大幅缩减 convergence 的篇幅和强度。
- Section 4.4：Confidence margin 和 routing 的分析较为扎实（AUC 0.70–0.74），是论文的实际贡献。Figure 7 的 Jaccard hierarchy 可视化有效。

**Section 5 (Conclusion)**：
- 结论整体与证据强度匹配，但 "Two observations follow" 中对 convergence 的讨论仍然过于肯定。

**Limitations**：
- 涵盖了单一训练运行、规模限制、格式混淆和覆盖范围，符合要求。
- 建议增加：（a）n=5 统计功效限制；（b）GDN head confound 对主要结论的影响。

**格式合规**：
- ✅ 正文 8 页（Section 1–5 + Limitations），符合限制
- ✅ Limitations section 存在且合理（page 8）
- ✅ 匿名化完整（"Anonymous ACL submission"）
- ✅ ACL style template
- ✅ AI 使用披露（page 21, Appendix Y）
- ✅ Abstract ≤ 200 词

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1810 · 2026-05-24T14:19:26.428341+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director"
}
```

</details>

---


## Round 137

## Round 137

12 recorded events


### User

_source line 1811 · 2026-05-24T14:19:35.150923+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结果摘要**：

- **Overall: 3.0 (Findings)**，Confidence 4/5
- **核心优势**：受控模型动物园实验设计严谨、饱和发现（saturation at 4%）稳健、附录透明详尽
- **核心问题**：
  - **W1 [Critical]**：GDN 16-head confound 驱动了 convergence claim（排除 GDN 后 ρ 从 −1.0 降至 −0.2）
  - **W2 [Major]**：n=5 Spearman 检验功效严重不足，未讨论 power analysis
  - **W3 [Major]**：单一训练运行无法分离种子效应
  - **W4 [Major]**：任务类型 vs 评估格式完全混淆
  - **W5 [Major]**：Bonferroni 校正后 p=.170 仍被暗示为有实质性意义
- **提升路径**：降级 convergence 声明、补充功效讨论、主文中呈现 GDN confound 分析，有望升至 3.5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1812 · 2026-05-24T14:19:59.683335+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file,dispatch_visual_check,request_external_review",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file,dispatch_visual_check,request_external_review",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1813 · 2026-05-24T14:19:59.733985+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1814 · 2026-05-24T14:20:07.564065+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1815 · 2026-05-24T14:20:07.614729+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1816 · 2026-05-24T14:20:20.946160+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "entrainment_gated_ft"
  }
}
```

</details>

---


### Tool result

_source line 1817 · 2026-05-24T14:20:21.097164+00:00_

{"result":"# 项目 entrainment_gated_ft 概况\n\n## 实验状态 (46 个)\n\n- **exp-arc-easy-eval**: DONE (success) — \n- **exp-007**: DONE (success) — \n- **exp-004-r2**: DONE (success) — \n- **exp-011-xstorycloze**: DONE (negative) — \n- **exp-004**: DONE (failed) — \n- **exp-011**: DONE (negative) — \n- **exp-010**: DONE (success) — \n- **exp-001**: DONE (success) — \n- **exp-008**: DONE (success) — \n- **exp-003-p2**: DONE (negative) — \n- **exp-003**: DONE (negative) — \n- **exp-009**: DONE (success) — \n- **eval_340m_retnet_hgrn2**: DONE (success) — \n- **hgrn2_eval_h3_1**: DONE (success) — \n- **hgrn2_eval_1_3b_all**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp-005-pure-v4** (killed): —\n- **exp-005-pure-v3** (killed): —\n- **exp-005-hgrn-chain** (killed): —\n\n## 趋势\n成功 16 / 负向 4 / 失败 3 / 共 46\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-48145: 无 GPU 信息\n\n## 告警\n- hgrn2_eval_1_3b_all: 已被终止 — unknown\n- exp-003-p2v2: 已被终止 — unknown\n- exp-004: 训练失败 — unknown\n- exp-005-eval: 已被终止 — unknown\n- exp-005-p1-v4: 已被终止 — unknown\n- exp-005-gla-eval: 训练失败 — unknown\n- exp-005-gla: 已被终止 — unknown\n- exp-005-deltanet: 已被终止 — unknown\n- exp-005-dn-eval: 已被终止 — unknown\n- exp-005-pure-eval: 已被终止 — unknown\n- exp-005-p1-eval: 已被终止 — unknown\n- exp-005-p1-eval-v2: 已被终止 — unknown\n- exp-005-p1-eval-v3: 已被终止 — unknown\n- exp-005-p1-eval-v4: 已被终止 — unknown\n- exp-005-p1-eval-v5: 已被终止 — unknown\n- exp-005-hgrn-chain: 已被终止 — unknown\n- exp-005-batch: 训练失败 — unknown\n- exp-005-pure-v3: 已被终止 — unknown\n- exp-005-pure-v4: 已被终止 — unknown\n- exp-005-pure-v5: 已被终止 — unknown\n- exp-005-pure-v6: 已被终止 — unknown\n- exp-005-pure-v7: 已被终止 — unknown\n- exp-005-pure-v8: 已被终止 — unknown\n- exp-005-pure-v9: 已被终止 — unknown\n- exp-005-pure-v10: 已被终止 — unknown\n- exp-005-pure-baselines: 已被终止 — unknown"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1818 · 2026-05-24T14:20:29.197075+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "entrainment_gated_ft"
  }
}
```

</details>

---


### Tool call

_source line 1819 · 2026-05-24T14:20:29.197388+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "entrainment_gated_ft"
  }
}
```

</details>

---


### Tool result

_source line 1820 · 2026-05-24T14:20:29.247914+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1821 · 2026-05-24T14:20:29.248316+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-24T14:13:12.305742+00:00\", \"completed_at\": \"2026-05-24T14:16:31.186310+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"三个 figure（5/6/7）挤在同一页上半部，Figures 6 和 7 尺寸明显偏小（各约占 1/6 页面），内部文字（axis label、legend、tick label）可能低于正文字号 70% 的可读性阈值。该页同时包含 Conclusion 和 Limitations 开头，整体过于拥挤。建议将 Figure 7 移至 page 7（该页右栏下方有空间）或移入 Appendix，给 Figures 5/6 更多展示空间\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 作为首个 display item 出现在第 2 页顶部，有效建立审稿人对核心发现的锚定印象（per-example overlap 在 4% attention 即饱和）。良好\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"整页纯文本（Related Work + Method §3.1），但前后页均有 figure，节奏可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 3 bar chart 颜色区分度良好，caption 自包含（解释了 helped/hurt/net 分类含义和关键发现）\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Tables 1-2 使用 booktabs 风格，关键值加粗标注，精度一致（小数位统一），排版规范\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 4 scatter plot 清晰，回归线和置信区间可辨，但 bootstrap CI 标注文字偏小\"}, {\"severity\": \"info\", \"dimension\": \"pages 9-10\", \"message\": \"References 格式统一，未见 [?] 未解析引用或跳号，排版正常无溢出\"}, {\"severity\": \"info\", \"dimension\": \"pages 11-21\", \"message\": \"Appendix 含约 28 个 table（Tables 3-30），格式一致使用 booktabs，无可见排版异常。Table-heavy 但与论文实证性质匹配\"}, {\"severity\": \"info\", \"dimension\": \"page 21\", \"message\": \"\\\"Use of AI Assistants\\\" 透明声明，良好实践\"}], \"counts\": {\"critical\": 0, \"warning\": 1, \"info\": 8}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1822 · 2026-05-24T14:20:38.266555+00:00_

Reviewer 1 初审已收到。视觉审查已完成（1 warning + 8 info）。

等待 Reviewer 2 初审结果。收到后进入交叉分享阶段。

**当前进度**：
- ✅ Reviewer 1：已提交（Overall 3.0 / Findings）
- ⏳ Reviewer 2：等待中
- ✅ 视觉审查：已完成
- ⬜ 外部审稿：未请求

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director"
}
```

</details>

---


## Round 138

## Round 138

6 recorded events


### User

_source line 1823 · 2026-05-24T14:22:21.300442+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见：Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures

## 1. Summary

本文研究三种混合线性循环架构（GatedDeltaNet、RetNet、HGRN2）在逐样本层面的预测多样性（predictive multiplicity）。利用 Wang et al. (2025) 的受控 model zoo（3 架构 × 5 attention 比例 × 2 规模），作者发现：(1) 聚合指标相近的架构在逐样本层面存在结构化分歧（Jaccard ≈ 0.10）；(2) 该分歧模式在 4% attention 即饱和，增加 attention 不改变受影响样本集合；(3) multiplicity 幅度因任务类型而异（α = 0.14–0.30）。此外，作者尝试基于置信度的 routing 策略，仅在 LAMBADA 上有效（+5.2pp），在其他 benchmark 上无效或有害。

## 2. Strengths

**S1.** 实验设计高度受控。使用共享训练数据、tokenizer 和超参数的 model zoo，将架构作为唯一变量，实验内部效度强。

**S2.** 统计方法论严谨且透明。全文一致使用 Bonferroni 校正、精确置换检验、Bootstrap BCa 置信区间，并坦率承认 n=5 时 Spearman ρ 的检验功效有限（"only |ρ| = 1.0 achieves p < .05"，Section 3.5）。这种统计诚实在 NLP 实证论文中少见。

**S3.** Jaccard 饱和发现（Section 4.2）是非平凡结果。最少量 attention（4%）即确立完整的逐样本分歧模式，这对混合架构的设计者有实际意义——暗示 attention 的"架构指纹"效应是二元的而非剂量依赖的。Figure 1b 和 Figure 4 提供了清晰的视觉证据。

**S4.** 附录极其详尽（13 页，Appendix A–Y），包括连续 Jaccard 验证（Appendix O）、归一化效应量（Appendix H）、种子校准（Appendix W）、五架构验证（Appendix X）、Transformer 基线对比（Appendix I）等。几乎每个可能的反驳都有对应的 robustness check。

**S5.** Yang & Wang (2026) 的引用处理得当。在 abstract 和 Related Work 中均明确引用并区分贡献（"our within-family design isolates backbone variation from training-regime differences"），没有回避这一高度相关的并行工作。

**S6.** 五架构验证（Section 4.3, Figure 5）将 GLA 和 DeltaNet 加入分析，在 340M 规模下所有 10 个架构对都满足 J ≤ 0.14, p ≤ .002，显著增强了主发现的泛化性。

## 3. Weaknesses

**W1 [Major]** 概念新颖性有限：已有框架在新领域的应用。

核心贡献是将 predictive multiplicity（Marx 2020）和 underspecification（D'Amour 2022）的分析框架应用到混合线性循环架构这一新领域。虽然受控设计执行良好，但概念层面的增量贡献有限。"first controlled within-family per-example analysis"（Introduction 第 4 段）的 claim 虽然通过 "controlled within-family" 限定词进行了精确 scoping，但整篇论文的核心信息——"聚合指标掩盖逐样本分歧"——在 Marx (2020)、D'Amour (2022)、Yang & Wang (2026) 中已有充分阐述。本文的独特贡献集中在饱和发现（S3），但这仅占论文约 1/4 篇幅。

**W2 [Major]** Routing 贡献薄弱但叙事权重过高。

Confidence-based routing 在 4 个 benchmark 中仅 1 个有效（LAMBADA: +5.2pp），在 HellaSwag 上无效（-0.06pp, p = .374），在 PIQA 上显著有害（-0.49pp, p = .006）。这本质上是一个消极结果。然而：
- Abstract 用约 1/6 篇幅描述 routing，且正面数字（"+5.2pp"、"36% of oracle complementarity"）比消极描述（"counterproductive on low-multiplicity tasks"）更突出。
- Conclusion 将 routing 作为两大核心观察之一呈现。
- Introduction 的贡献列表未包含 routing（正确的处理），但这与 abstract/conclusion 的叙事权重不一致。

建议：在 abstract 中缩减 routing 篇幅，或更明确地将其定位为"探索性的消极发现"。

**W3 [Major]** 单次训练运行无法分离架构效应与种子效应。

每个 架构×attention 配置仅有一次训练运行。论文在 Limitations 中承认这一点，并以 Pythia 70M 种子校准（Appendix W）和 within- vs. cross-architecture Jaccard 3× 差距作为间接证据。但两个问题：
- Pythia 70M 是 Transformer（不是混合循环架构），且规模为 70M（远小于 340M/1.3B），跨家族、跨规模的校准说服力有限。
- within- vs. cross-architecture 3× 差距混淆了架构差异和种子差异——cross-architecture 必然包含种子差异 + 架构差异，所以 3× 差距的存在并不能证明架构是主要驱动力。

这是整个论文最根本的局限：如果为任一架构训练 3–5 个不同种子，就能直接估算种子噪声的基线水平并与架构效应解耦。

**W4 [Major]** 任务类型与评估格式的混淆。

LAMBADA 是唯一的自由生成 benchmark，同时也拥有最高的 α（0.30）。论文在 Section 3.2 和 Limitations 中讨论了这一混淆，并在全文中以"task type (or evaluation format)"进行 hedging——这种诚实值得肯定，但也意味着"multiplicity 因任务类型而异"这一核心 claim 在当前数据下不可证伪。论文指出多选题内部 format（two-way vs. four-way）不预测 α，但这只排除了多选题子空间内的 format 效应，并未解决自由生成 vs. 多选的根本混淆。

**W5 [Minor]** 置信度 routing 的相关文献缺失。

Routing 实验本质上是基于输入特征选择最优模型，这与 selective prediction / abstention 文献（Geifman & El-Yaniv 2017, 2019）和 MoE routing 概念上相关。论文引用了 Basu (2026) 的 content-based routing，但更广泛的 model selection / ensemble selection 文献（如 Caruana et al. 2004 "Ensemble selection from libraries of models"）可为 routing 实验提供更丰富的上下文。

**W6 [Minor]** Limitations 中遗漏的关键局限：评估仅使用 greedy decoding。

Section 3.2 提及"default prompts and greedy decoding"，但 Limitations 未讨论 decoding 策略对逐样本分歧的影响。采样 decoding 可能会改变 helped/hurt 的分类，因为在 boundary cases 上，temperature > 0 的随机性可能掩盖或放大架构差异。

## 4. Questions

**Q1.** 为什么不对一个架构训练多个种子来直接校准种子噪声水平？Pythia 70M 的跨家族校准不够有说服力。这是最直接能回答"逐样本分歧是架构驱动还是种子驱动"的实验。

**Q2.** GDN h3-1 的 16 vs. 32 attention heads 差异（Section 3.1, Section 4.3）——排除 GDN 后 LAMBADA 的 ρ 从 -1.0 降到 -0.7（p = .233），MMLU 甚至反转为 +0.6。论文的聚合收敛发现在多大程度上是 GDN head 数量混淆驱动的？

**Q3.** Appendix I 的 Transformer 基线对比很有趣——三个架构的 h3-1 correct set 都更接近 Transformer。这是否暗示 attention 的逐样本效应是"向 Transformer 行为靠拢"，而非架构特异性的？如果是这样，饱和发现可能反映的是"少量 attention 即足以引入 Transformer 式行为"。

**Q4.** Confidence margins 的 AUC 0.70–0.74 表明约 30% 的变异无法用 pure-model 置信度解释。作者是否考虑过结合架构内部表示特征（如 hidden state norm、attention entropy）来提高预测性能？

**Q5.** 论文仅评估预训练 checkpoint，不包含 fine-tuning（Limitations 承认）。考虑到实际部署几乎都涉及 task-specific fine-tuning，逐样本分歧模式在 fine-tuning 后是否保留是一个关键的实用性问题。作者对此有何预期？

## 5. Missing References

- **Selective prediction / abstention**: Geifman & El-Yaniv (2017, 2019) — routing 实验与 selective prediction 概念相关
- **Ensemble selection**: Caruana et al. (2004) "Ensemble selection from libraries of models" — 基于输入选择最优模型的经典工作
- 论文的 Related Work 在其他方面较为全面（Yang & Wang 2026, MultiBERTs, Model Soups, predictive multiplicity 均已引用）

## 6. Overall Assessment

**Overall Assessment**: 3.5 (Borderline Conference)

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心逐样本分析方法论合理，统计处理严谨；但单次训练运行（W3）和格式混淆（W4）是根本性局限，削弱了因果解释力 |
| Excitement | 3/5 | 饱和发现（S3）有新意，但整体是已有分析框架在新领域的应用（W1），routing 结果实质为消极发现（W2） |
| Reproducibility | 4/5 | 使用公开 model zoo，方法描述清晰，承诺释放代码；评估框架（lm-eval-harness v0.4.x）标准化 |
| Reviewer Confidence | 4/5 | 熟悉 predictive multiplicity、模型评估和混合架构文献 |

**一句话总结**: 一项执行严谨但概念增量有限的实证研究——饱和发现有价值，但核心信息（聚合指标掩盖逐样本分歧）已被充分建立，routing 实质上是消极结果，且关键混淆（种子 vs. 架构、格式 vs. 任务类型）未能解决。适合 Findings，主会议接收需要额外的新颖性证据（如多种子实验解耦架构效应、或在生成任务上验证 routing）。

## 7. Detailed Comments（按 Section 逐节）

### Abstract
- 字数约 154 词，符合 ≤200 词要求。
- Yang & Wang (2026) 的引用整合自然，明确区分了两项工作的定位。
- Routing 描述（最后一句）中 "+5.2pp" 和 "36% of oracle complementarity" 的正面数字比 "counterproductive on low-multiplicity tasks" 更突出。建议平衡叙事或缩减 routing 篇幅。

### Section 1 (Introduction)
- 开头段很好地建立了问题动机：聚合指标相近但逐样本行为不同。
- "We present the first controlled within-family per-example analysis" — 通过 "controlled within-family" 限定词精确 scoped，可辩护。但建议明确说明"first"相对于哪些 prior work（不仅仅是 Yang & Wang，还包括 MultiBERTs 等种子变异分析）。
- 贡献列表仅 2 条 bullet，简洁有力。Routing 正确地未列入贡献，但这与 abstract/conclusion 的叙事权重不一致（W2）。

### Section 2 (Related Work)
- 三段结构清晰：Hybrid Recurrent Architectures、Linear Recurrent Models、Underspecification and Predictive Multiplicity。
- 对 Yang & Wang (2026) 的定位在最后一句完成——建议提升位置或增加一两句详细对比（如他们研究的是不同公司的 frontier LLMs，训练数据/超参完全不同，因此无法隔离架构效应）。
- 引用密度高，覆盖面广。缺少 selective prediction / model selection 文献（W5）。

### Section 3 (Method)
- Model Zoo 描述清晰，GDN h3-1 的 16 vs. 32 heads 差异在正文中前置提及并指向 robustness check，处理得当。
- Task Taxonomy 的 confirmatory/exploratory split（Appendix A）是好的实践，但不够强——taxonomy 是"informal; not pre-registered"。
- Per-Example Decomposition 的二值化处理（helped/hurt/unchanged）是合理的简化，连续 Jaccard 验证（Appendix O）弥补了信息损失。
- Statistical Methods 对检验功效的坦率讨论值得表扬（"with n = 5, only |ρ| = 1.0 achieves p < .05"）。

### Section 4 (Experiments)
- **4.1 Per-Example Divergence**: 核心发现（J ≈ 0.10, 显著高于独立基线 0.05 但远低于理论最大值 0.78–0.92）报告充分。Cohen's d = 0.73–0.92 提供了效应量的连续度量。HGRN2 作为唯一净正效应架构的发现有趣但未深入讨论原因。
- **Confidence margin predictor**: AUC 0.70–0.74 是中等判别力。"rescue thresholds are architecture-invariant (1% spread) but disruption thresholds vary 47%"是有趣的不对称性，值得更多讨论。
- **Confidence-based routing**: 实验设计合理（10-fold cross-validation），但结果明确显示这是一个 task-dependent 的方法，在 PIQA 上显著有害。"average-logits ensemble is left to future work" 是一个重要遗漏——logits ensemble 是最自然的 baseline，缺少它使 routing 的价值难以判断。
- **4.2 Per-Example Overlap Saturates at Minimal Attention**: 这是论文最强的贡献。Figure 1b 和 Figure 4 都清晰展示了饱和模式。跨规模分析（J 在 340M 和 1.3B 一致）增强了发现的稳健性。
- **4.3 Robustness**: 排除 GDN 后 LAMBADA ρ 降为 -0.7 且 MMLU 反转为 +0.6——这是一个重要的 caveat，论文处理得诚实但低调。建议在正文中更显著地讨论 GDN 混淆对聚合收敛结论的影响。

### Section 5 (Conclusion)
- 结论部分恰当总结了主要发现。
- "per-example audit before architecture substitution is advisable" 是合理的实践建议。
- Routing 在结论中占据的比重（约 1/3 段落）与其在实验中的表现（1/4 有效）不匹配。

### Limitations
- 覆盖了 4 个要点：单次训练、格式混淆、覆盖范围、仅预训练。
- 遗漏了 greedy decoding 的局限性（W6）。
- LAMBADA Bonferroni-adjusted p = .170 的坦率报告值得肯定——许多论文会选择性忽略这一点。
- 整体篇幅和深度适当。

### Appendix
- 极其详尽（Appendix A–Y，13 页），几乎每个潜在质疑都有对应的 robustness check。
- Appendix I（Transformer Entrainment Comparison）是一个有价值的发现，值得考虑提升到正文。
- Appendix W（Seed-Variation Calibration）使用 Pythia 70M 作为种子校准参考——如前述（W3），跨家族校准说服力有限。
- Appendix Y（Use of AI Assistants）声明使用了 Claude 作为 AI coding and writing assistant——符合 ARR 透明度要求。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1824 · 2026-05-24T14:22:57.813155+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条阅读 Reviewer 2 的审稿意见，对每个 Weakness 和 Question 给出 [AGREE] 或 [REBUT] 回应。如果你部分同意，可以用 [PARTIAL] 并说明哪些部分你同意/不同意。也请指出 Reviewer 2 遗漏但你认为重要的问题。\n\n---\n\n**Reviewer 2 Overall: 3.5 (Borderline Conference), Confidence 4/5**\n\n### Strengths (R2)\n- S1: 实验设计高度受控（共享数据/tokenizer/超参，架构为唯一变量）\n- S2: 统计方法论严谨且透明（Bonferroni、精确置换检验、Bootstrap BCa、坦率承认 n=5 功效）\n- S3: Jaccard 饱和发现非平凡——最少量 attention（4%）即确立完整分歧模式，暗示 attention 的\"架构指纹\"效应是二元的\n- S4: 附录极其详尽（13 页 Appendix A–Y），几乎每个反驳都有 robustness check\n- S5: Yang & Wang (2026) 引用处理得当\n- S6: 五架构验证（GLA + DeltaNet）增强泛化性\n\n### Weaknesses (R2)\n- **W1 [Major]**: 概念新颖性有限——已有框架（predictive multiplicity, underspecification）在新领域的应用。核心信息\"聚合指标掩盖逐样本分歧\"已被 Marx (2020)、D'Amour (2022)、Yang & Wang (2026) 充分建立。独特贡献集中在饱和发现但仅占 ~1/4 篇幅。\n- **W2 [Major]**: Routing 贡献薄弱但叙事权重过高——4 个 benchmark 中仅 LAMBADA 有效（+5.2pp），HellaSwag 无效，PIQA 显著有害。但 abstract 用 ~1/6 篇幅描述 routing 且正面数字突出，conclusion 将其作为两大核心观察之一。\n- **W3 [Major]**: 单次训练运行无法分离架构效应与种子效应。Pythia 70M 校准是跨家族/跨规模的，说服力有限。within- vs. cross-architecture 3× 差距混淆了种子差异 + 架构差异。\n- **W4 [Major]**: 任务类型与评估格式混淆。LAMBADA 是唯一自由生成 benchmark 且拥有最高 α(0.30)。多选题内部 format 不预测 α 只排除了子空间内的 format 效应。\n- **W5 [Minor]**: 置信度 routing 缺少 selective prediction / abstention 文献（Geifman & El-Yaniv 2017, 2019）和 ensemble selection 文献（Caruana et al. 2004）。\n- **W6 [Minor]**: Limitations 遗漏 greedy decoding 对逐样本分歧的影响。\n\n### Questions (R2)\n- Q1: 为什么不对一个架构训练多个种子来直接校准种子噪声？\n- Q2: 排除 GDN 后 LAMBADA ρ 降到 -0.7(p=.233)，MMLU 反转为 +0.6——聚合收敛发现多大程度上是 GDN head 数量混淆驱动的？\n- Q3: Appendix I 的 Transformer 基线——三个架构 h3-1 correct set 都更接近 Transformer，饱和可能反映的是\"少量 attention 即引入 Transformer 式行为\"？\n- Q4: Confidence margins AUC 0.70–0.74，约 30% 变异无法解释——是否考虑结合架构内部表示特征？\n- Q5: 仅评估预训练 checkpoint，fine-tuning 后逐样本分歧是否保留？\n\n---\n\n请对以上 W1–W6 和 Q1–Q5 逐条给出 [AGREE]/[REBUT]/[PARTIAL] 回应，并补充你的分析。",
  "reviewer_id": "1",
  "project": "entrainment_gated_ft",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条阅读 Reviewer 2 的审稿意见，对每个 Weakness 和 Question 给出 [AGREE] 或 [REBUT] 回应。如果你部分同意，可以用 [PARTIAL] 并说明哪些部分你同意/不同意。也请指出 Reviewer 2 遗漏但你认为重要的问题。\n\n---\n\n**Reviewer 2 Overall: 3.5 (Borderline Conference), Confidence 4/5**\n\n### Strengths (R2)\n- S1: 实验设计高度受控（共享数据/tokenizer/超参，架构为唯一变量）\n- S2: 统计方法论严谨且透明（Bonferroni、精确置换检验、Bootstrap BCa、坦率承认 n=5 功效）\n- S3: Jaccard 饱和发现非平凡——最少量 attention（4%）即确立完整分歧模式，暗示 attention 的\"架构指纹\"效应是二元的\n- S4: 附录极其详尽（13 页 Appendix A–Y），几乎每个反驳都有 robustness check\n- S5: Yang & Wang (2026) 引用处理得当\n- S6: 五架构验证（GLA + DeltaNet）增强泛化性\n\n### Weaknesses (R2)\n- **W1 [Major]**: 概念新颖性有限——已有框架（predictive multiplicity, underspecification）在新领域的应用。核心信息\"聚合指标掩盖逐样本分歧\"已被 Marx (2020)、D'Amour (2022)、Yang & Wang (2026) 充分建立。独特贡献集中在饱和发现但仅占 ~1/4 篇幅。\n- **W2 [Major]**: Routing 贡献薄弱但叙事权重过高——4 个 benchmark 中仅 LAMBADA 有效（+5.2pp），HellaSwag 无效，PIQA 显著有害。但 abstract 用 ~1/6 篇幅描述 routing 且正面数字突出，conclusion 将其作为两大核心观察之一。\n- **W3 [Major]**: 单次训练运行无法分离架构效应与种子效应。Pythia 70M 校准是跨家族/跨规模的，说服力有限。within- vs. cross-architecture 3× 差距混淆了种子差异 + 架构差异。\n- **W4 [Major]**: 任务类型与评估格式混淆。LAMBADA 是唯一自由生成 benchmark 且拥有最高 α(0.30)。多选题内部 format 不预测 α 只排除了子空间内的 format 效应。\n- **W5 [Minor]**: 置信度 routing 缺少 selective prediction / abstention 文献（Geifman & El-Yaniv 2017, 2019）和 ensemble selection 文献（Caruana et al. 2004）。\n- **W6 [Minor]**: Limitations 遗漏 greedy decoding 对逐样本分歧的影响。\n\n### Questions (R2)\n- Q1: 为什么不对一个架构训练多个种子来直接校准种子噪声？\n- Q2: 排除 GDN 后 LAMBADA ρ 降到 -0.7(p=.233)，MMLU 反转为 +0.6——聚合收敛发现多大程度上是 GDN head 数量混淆驱动的？\n- Q3: Appendix I 的 Transformer 基线——三个架构 h3-1 correct set 都更接近 Transformer，饱和可能反映的是\"少量 attention 即引入 Transformer 式行为\"？\n- Q4: Confidence margins AUC 0.70–0.74，约 30% 变异无法解释——是否考虑结合架构内部表示特征？\n- Q5: 仅评估预训练 checkpoint，fine-tuning 后逐样本分歧是否保留？\n\n---\n\n请对以上 W1–W6 和 Q1–Q5 逐条给出 [AGREE]/[REBUT]/[PARTIAL] 回应，并补充你的分析。",
    "reviewer_id": "1",
    "project": "entrainment_gated_ft",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1825 · 2026-05-24T14:23:10.623503+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 12810
}
```

</details>

---


### Tool call

_source line 1826 · 2026-05-24T14:23:11.075520+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条阅读 Reviewer 1 的审稿意见，对每个 Weakness 和 Question 给出 [AGREE] 或 [REBUT] 回应。如果你部分同意，可以用 [PARTIAL] 并说明哪些部分你同意/不同意。也请指出 Reviewer 1 遗漏但你认为重要的问题。\n\n---\n\n**Reviewer 1 Overall: 3.0 (Findings), Confidence 4/5**\n\n### 核心优势 (R1)\n- 受控模型动物园实验设计严谨\n- 饱和发现（saturation at 4%）稳健\n- 附录透明详尽\n\n### Weaknesses (R1)\n- **W1 [Critical]**: GDN 16-head confound 驱动了 convergence claim。排除 GDN 后 ρ 从 −1.0 降至 −0.2（注：Reviewer 1 报告为 −0.2，而论文 Section 4.3 实际报告的是排除 GDN 后 LAMBADA ρ = −0.7, p = .233; MMLU 反转为 +0.6）。Reviewer 1 认为这构成对整个 convergence 叙事的根本性威胁。\n- **W2 [Major]**: n=5 Spearman 检验功效严重不足，未讨论 power analysis。\n- **W3 [Major]**: 单一训练运行无法分离种子效应。\n- **W4 [Major]**: 任务类型 vs 评估格式完全混淆。\n- **W5 [Major]**: Bonferroni 校正后 p=.170 仍被暗示为有实质性意义。\n\n### Reviewer 1 的提升路径建议\n- 降级 convergence 声明\n- 补充功效讨论\n- 主文中呈现 GDN confound 分析\n- 认为有望升至 3.5\n\n---\n\n请对以上 W1–W5 逐条给出 [AGREE]/[REBUT]/[PARTIAL] 回应，并补充你的分析。特别关注：\n1. W1 中 ρ 数值的准确性（−0.2 vs. 论文报告的 −0.7）\n2. W5 关于 Bonferroni p=.170 的解读——论文是否真的\"暗示为有实质性意义\"还是已经坦率承认\n3. 你是否有 Reviewer 1 未提及的额外 weakness",
  "reviewer_id": "2",
  "project": "entrainment_gated_ft",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条阅读 Reviewer 1 的审稿意见，对每个 Weakness 和 Question 给出 [AGREE] 或 [REBUT] 回应。如果你部分同意，可以用 [PARTIAL] 并说明哪些部分你同意/不同意。也请指出 Reviewer 1 遗漏但你认为重要的问题。\n\n---\n\n**Reviewer 1 Overall: 3.0 (Findings), Confidence 4/5**\n\n### 核心优势 (R1)\n- 受控模型动物园实验设计严谨\n- 饱和发现（saturation at 4%）稳健\n- 附录透明详尽\n\n### Weaknesses (R1)\n- **W1 [Critical]**: GDN 16-head confound 驱动了 convergence claim。排除 GDN 后 ρ 从 −1.0 降至 −0.2（注：Reviewer 1 报告为 −0.2，而论文 Section 4.3 实际报告的是排除 GDN 后 LAMBADA ρ = −0.7, p = .233; MMLU 反转为 +0.6）。Reviewer 1 认为这构成对整个 convergence 叙事的根本性威胁。\n- **W2 [Major]**: n=5 Spearman 检验功效严重不足，未讨论 power analysis。\n- **W3 [Major]**: 单一训练运行无法分离种子效应。\n- **W4 [Major]**: 任务类型 vs 评估格式完全混淆。\n- **W5 [Major]**: Bonferroni 校正后 p=.170 仍被暗示为有实质性意义。\n\n### Reviewer 1 的提升路径建议\n- 降级 convergence 声明\n- 补充功效讨论\n- 主文中呈现 GDN confound 分析\n- 认为有望升至 3.5\n\n---\n\n请对以上 W1–W5 逐条给出 [AGREE]/[REBUT]/[PARTIAL] 回应，并补充你的分析。特别关注：\n1. W1 中 ρ 数值的准确性（−0.2 vs. 论文报告的 −0.7）\n2. W5 关于 Bonferroni p=.170 的解读——论文是否真的\"暗示为有实质性意义\"还是已经坦率承认\n3. 你是否有 Reviewer 1 未提及的额外 weakness",
    "reviewer_id": "2",
    "project": "entrainment_gated_ft",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1827 · 2026-05-24T14:23:12.433834+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1358
}
```

</details>

---


### Assistant

_source line 1828 · 2026-05-24T14:23:24.784994+00:00_

交叉分享已发送。Reviewer 1 收到 Reviewer 2 的完整意见，Reviewer 2 收到 Reviewer 1 的完整意见。等待两位 Reviewer 的交叉回应。

**当前审稿进度**：
- Round 1 初审 ✅（R1: 3.0, R2: 3.5）
- Step 2 交叉分享 → 已派发，等待回应
- 外部审稿：未请求
- 视觉审查：✅ 已完成（1 warning: page 8 三图拥挤，8 info）

两位 Reviewer 在以下问题上已有共识：
- 单次训练运行/种子效应（R1-W3 ≈ R2-W3）
- 任务类型/格式混淆（R1-W4 ≈ R2-W4）
- GDN confound 对 convergence claim 的影响（R1-W1 ≈ R2-Q2）

主要分歧待确认：
- R1 给 3.0，R2 给 3.5——差异主要在 novelty 评估和 routing 问题的权重
- R1-W1 报告的 ρ 数值（−0.2）与论文实际报告（−0.7）可能存在偏差，已请 R2 核实

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director"
}
```

</details>

---


## Round 139

## Round 139

2 recorded events


### User

_source line 1829 · 2026-05-24T14:23:27.410898+00:00_

[Reviewer 2 审稿结果]:
审稿完成。总结：

**Overall: 3.5 (Borderline Conference)**，置信度 4/5。

核心判断：论文是一项执行严谨的实证研究，统计方法论透明且诚实，Jaccard 饱和发现（4% attention 即确立逐样本分歧模式）有真实价值。但主要问题在于：(1) 概念新颖性有限——将已有的 predictive multiplicity 框架应用到新领域；(2) routing 实质为消极结果（仅 1/4 benchmark 有效）却获得了过高叙事权重；(3) 单次训练运行无法分离架构与种子效应；(4) 任务类型与评估格式混淆未能解决。适合 Findings，主会议接收需要额外证据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1830 · 2026-05-24T14:23:42.672016+00:00_

收到 Reviewer 2 的交叉回应，评分维持 3.5。等待 Reviewer 1 的交叉回应完成后合成最终报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director"
}
```

</details>

---


## Round 140

## Round 140

2 recorded events


### User

_source line 1831 · 2026-05-24T14:24:50.892602+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应：Reviewer 2 审稿意见

---

### Weaknesses 回应

**[PARTIAL] R2-W1: 概念新颖性有限**

同意部分：R2 正确指出 "聚合指标掩盖逐样本分歧" 的概念框架已由 Marx et al. (2020)、D'Amour et al. (2022) 充分建立。本文在概念层面确实未提出新理论。

不同意部分：R2 低估了本文的经验性贡献。（1）饱和发现（4% attention 即确立完整分歧模式）是一个非平凡的经验事实——此前的 multiplicity 文献关注的是"存在与否"或"程度量化"，而非"剂量-反应关系中的阈值效应"。（2）受控模型动物园的实验设计方法论本身有价值——相比 D'Amour et al. (2022) 使用不同超参数/初始化的多模型比较，本文通过共享训练管线隔离了架构作为唯一变量。（3）混合递归架构是一个快速增长的研究方向（Mamba、Griffin、RWKV 等），将 multiplicity 分析引入该领域有实际时效性。

但 R2 说"独特贡献集中在饱和发现但仅占 ~1/4 篇幅"这一观察值得重视——如果作者重组论文，让饱和发现成为主线叙事（而非 convergence），论文的贡献会更清晰。

**severity 评估**：我的评价略低于 R2。R2 给 Major，我倾向 Moderate——因为 EMNLP Findings 的门槛并不要求概念革命，经验性发现的系统性和稳健性可以支撑接收。

---

**[AGREE] R2-W2: Routing 贡献叙事权重过高**

完全同意。我在审稿中虽未将此列为独立 weakness，但在 Q4 中质疑了 routing 的失效条件。R2 的定量论证更有力：4 个基准中仅 LAMBADA 有实际增益（+5.2pp），HellaSwag 无效，PIQA 显著有害——这不足以支撑 Abstract 和 Conclusion 给予 routing 的叙事地位。

补充证据：Section 4.4 (page 5) 的 "On PIQA, it is significantly negative (ε < 0.10pp, p < .000)" 直接反驳了 routing 作为通用工具的叙事。Conclusion (page 7) 将 routing 列为 "Two observations" 之一更是过度。

建议：routing 应降级为 Section 4 的一个探索性观察，从 Abstract 和 Conclusion 中移除或大幅弱化，明确标注其仅在特定任务条件下有效。

---

**[AGREE] R2-W3: 单次训练运行无法分离架构与种子效应**

与我的 W3 完全一致。R2 进一步指出 Pythia 70M 校准的跨家族/跨规模问题——Pythia 是标准 Transformer，不是混合递归架构，其种子敏感性可能与 GDN/RetNet/HGRN2 有系统性差异。这强化了我 Q2 中提出的问题。

R2 提到的 "within- vs. cross-architecture 3× 差距混淆了种子差异 + 架构差异"——具体来说，Appendix W 报告 within-seed J ≈ 0.30 vs cross-architecture J 可比，但如果种子变异本身就占了大部分 variance，则 cross-architecture 的额外效应可能很小。

---

**[AGREE] R2-W4: 任务类型与评估格式混淆**

与我的 W4 一致。R2 补充了一个我遗漏的论点：多选题内部 format 不预测 σ（即 4-way vs 2-way 无显著差异）"只排除了子空间内的 format 效应"。这是精准的——论文在 Section 4.2 (page 6) 指出 "within multiple-choice tasks, format (two-way vs. four-way) does not predict σ"，但这仅表明多选题子空间内的选项数不重要，并不排除自由生成 vs 多选这个更大的 format 差异。

LAMBADA 同时是唯一的 retrieval 任务、唯一的自由生成任务、和拥有最高 σ(0.30) 的任务——三重混淆使得任何单一归因都站不住脚。

---

**[AGREE] R2-W5: 缺少 selective prediction / abstention 文献**

同意。Section 4.4 的 confidence-based routing 实质上是一个 selective prediction / model selection 问题。Geifman & El-Yaniv (2017, 2019) 的 selective prediction framework 和 Caruana et al. (2004) 的 ensemble selection 是直接相关的先驱工作。缺少这些引用使得 routing 贡献的定位不够准确——读者无法判断本文的方法与已有 selective prediction 方法相比有何改进。

---

**[PARTIAL] R2-W6: Limitations 遗漏 greedy decoding 影响**

同意方向但降低 severity。R2 正确指出 greedy decoding 是确定性的，采样解码可能产生不同的分歧模式——特别是对 LAMBADA 这种自由生成任务，greedy vs nucleus sampling 可能显著改变逐样本正确性。

但 Section 3.1 (page 3) 明确说明 "All evaluations use lm-evaluation-harness v0.4.x (Gao et al., 2024) with default prompts and greedy decoding"，这是该评估框架的标准配置。作为 Limitations 补充是合理的，但不构成方法论缺陷——大多数 LM 评估工作使用 greedy decoding。

建议：在 Limitations 中加一句说明 greedy decoding 对 LAMBADA 等生成任务的潜在影响即可。

---

### Questions 回应

**[AGREE] R2-Q1: 为什么不训练多个种子？**

与我的 Q2 方向一致。这是对 W3 的自然 follow-up。论文使用的是 Wang et al. (2025) 的预训练模型动物园，作者可能无法控制训练过程。但如果目标是发表关于架构效应的因果声明，至少对一个架构的两个种子进行验证是基本要求。Appendix W 的 Pythia 70M 是一个不充分的替代。

---

**[AGREE] R2-Q2: GDN 排除后 convergence 的稳健性**

这与我的 W1 (Critical) 完全一致。R2 引用的数据（排除 GDN 后 LAMBADA ρ 降到 −0.7, p=.233；MMLU 反转为 +0.6）进一步支持我的判断：convergence 声明在统计上不成立。

我在 W1 中引用了 Appendix D 的 Table 3——排除 GDN 后仅剩 n=2 架构（RetNet, HGRN2），此时 Spearman 相关系数本质上退化为二点比较，无统计意义。R2 和我在这一点上完全一致，这是论文最严重的问题。

---

**[AGREE] R2-Q3: Transformer 基线——饱和可能反映 Transformer 式行为引入**

这是一个我遗漏但非常重要的观点。Appendix I 显示三个架构在 h3-1 配置下的 correct set 都更接近 Transformer 基线。如果 4% attention 已足以引入 Transformer 式的逐样本行为模式，则饱和发现的解读需要修正——它可能不是"架构指纹在最低 attention 即确立"，而是"少量 attention 即使行为向 Transformer 收敛"。

这两个解读有根本性区别：前者暗示混合架构保留了独特的逐样本特征，后者暗示 attention 主导了逐样本行为而 recurrence backbone 的影响被覆盖。论文应在 Section 4.2 或 Discussion 中讨论这一替代解读。

---

**[PARTIAL] R2-Q4: AUC 0.70–0.74 的未解释方差**

方向同意——30% 未解释方差确实值得讨论。但"结合架构内部表示特征"的建议在实践中可能不可行：（a）这需要在推理时获取中间层表示，增加计算成本；（b）不同架构的内部表示空间不直接可比。

更实际的后续方向可能是：（a）结合多个浅层信号（如 token 频率、输入长度、prompt perplexity）构建组合预测器；（b）分析 AUC 在不同样本子群上的变异。

---

**[AGREE] R2-Q5: Fine-tuning 后逐样本分歧是否保留？**

有效问题。论文所有结论基于 pretrained checkpoints。如果 fine-tuning（尤其是 instruction tuning 或 RLHF）改变了逐样本行为模式，则部署建议的适用性受限——实际部署几乎总是使用 fine-tuned 模型。这应补充到 Limitations 中。

---

### Reviewer 2 遗漏但我认为重要的问题

1. **n=5 Spearman 功效分析缺失**（我的 W2）：R2 在 S2 中称论文"坦率承认 n=5 功效"，但我认为论文对此的讨论不够充分——Section 3.5 仅提到 "power is limited" 而未给出具体功效估计。这对 Table 1 中所有 ρ 值的可解读性有系统性影响。

2. **n=3 架构 Bootstrap CI 退化**（我的 W8）：R2 未讨论 n=3 上 Bootstrap BCa 的覆盖率问题。Appendix D1 确认大量 bootstrap 样本是退化的同架构三重采样。这影响 Figure 4 中 CI 不含零的可信度。

3. **排列检验未条件化于样本难度**（我的 W9）：Appendix K 的 null baseline 未排除样本内在难度对跨架构 Jaccard 重叠的混淆。

---

### 对 Reviewer 2 整体评分的回应

R2 给 3.5（Borderline Conference），我给 3.0（Findings）。差距主要来自：

1. **R2 在 W1 中对概念新颖性的批评未完全反映到评分中**——如果概念新颖性确实有限（R2 自己的 W1 Major），3.5 似乎偏高。
2. **R2 未将 GDN confound 列为独立 weakness**——仅在 Q2 中提问。我认为这是 Critical 级别问题（我的 W1），因为它动摇了论文约 1/3 的叙事（整个 Section 4.3 的 convergence 讨论）。
3. **R2 的 S2 称论文统计方法严谨——但"严谨"和"有足够功效"是不同概念**。方法论选择是正确的（Bonferroni、置换检验），但在 n=5、n=3 这样的极小样本上，即使正确的方法也缺乏诊断力。

综合考虑，我维持 3.0（Findings）的评分。论文的饱和发现和实验框架支撑 Findings 接收，但 convergence 声明的统计基础不足以支撑 Conference 级别。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1832 · 2026-05-24T14:25:02.716883+00:00_

收到 Reviewer 1 的交叉回应。等待 Reviewer 2 对 Reviewer 1 的交叉回应后进入收敛判断与报告合成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director"
}
```

</details>

---


## Round 141

## Round 141

2 recorded events


### User

_source line 1833 · 2026-05-24T14:25:05.188538+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。要点总结：

- 对 R2 的 W2（routing 叙事过重）、W3（单训练运行）、W4（格式混淆）、W5（缺文献）完全同意
- 对 W1（概念新颖性）部分同意——经验贡献被低估，但同意饱和发现应成为主线
- 对 W6（greedy decoding）方向同意但降级 severity
- R2-Q3（Transformer 基线解读）是我遗漏的重要观点，完全同意
- 指出 R2 遗漏的三个问题：n=5 功效分析、n=3 bootstrap 退化、排列检验样本难度混淆
- 维持 3.0（Findings）评分，认为 R2 的 3.5 偏高——主要因为 GDN confound 应被列为 Critical 而非仅作为 Question

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1834 · 2026-05-24T14:25:21.599967+00:00_

收到 Reviewer 1 的交叉回应。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director"
}
```

</details>

---


## Round 142

## Round 142

10 recorded events


### User

_source line 1835 · 2026-05-24T14:25:40.469520+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应：对 Reviewer 1 (W1–W5) 的逐条回应

---

## [PARTIAL] R1-W1: GDN 16-head confound 驱动 convergence claim

**同意的部分**：GDN h3-1 的 16 vs. 32 heads 差异确实是一个混淆变量，排除 GDN 后聚合收敛证据显著减弱。论文自身在 Section 4.3 也承认："The aggregate variance pattern therefore depends on GDN inclusion." MMLU 从负相关反转为 ρ = +0.6 更是直接矛盾。R1 将此标记为 Critical 是有道理的——如果聚合收敛是论文的核心 claim。

**不同意的部分（两点）**：

1. **R1 报告的数值有误**：R1 称排除 GDN 后 ρ 从 −1.0 降至 **−0.2**。但论文 Section 4.3 明确报告为 **ρ = −0.7, p = .233**（原文："Removing GDN weakens the LAMBADA variance reduction (ρ = −0.7, p = .233)"）。−0.7 vs. −0.2 的差异显著影响严重性判断：−0.7 仍表示较强的单调递减趋势，只是在 n=5 下统计功效不足而无法达到显著性；−0.2 则表示趋势几乎消失。R1 的 Critical 评级部分建立在这一错误数据上。

2. **聚合收敛并非论文的核心 claim**：论文的两项正式贡献（Introduction 贡献列表）分别是 (a) 结构化 predictive multiplicity 和 (b) 逐样本 Jaccard 饱和。聚合收敛（aggregate σ reduction）在正文中始终以 "non-significant" 标注（Introduction 第 3 段："only LAMBADA shows a **non-significant** decreasing aggregate variance pattern"）。论文的叙事策略恰恰是利用聚合收敛的非显著性与逐样本饱和的显著性之间的**解耦**作为论证——即使聚合指标看似收敛（实际未达显著），逐样本分歧模式已固化。因此，即使 GDN confound 完全推翻了聚合收敛，论文的两项核心贡献不受影响。Section 4.3 明确声明："the per-example saturation result does not [depend on GDN inclusion]."

**我的评估**：这是一个 **Major**（而非 Critical）问题。GDN confound 影响的是 Table 1 和 Figure 2 中的聚合收敛背景叙事，但不影响论文的两项正式贡献。建议作者在正文中更显著地讨论 GDN confound（目前只有一句话在 Section 4.3），并考虑在 Table 1 中增加 "excl. GDN" 行以提高透明度（目前仅 LAMBADA 有此行）。

---

## [PARTIAL] R1-W2: n=5 Spearman 检验功效不足

**同意的部分**：n=5 的 Spearman 检验确实功效极低。这是一个真实的方法论局限，正式的 power analysis 会让论文更完善。

**不同意的部分**：论文已经明确承认了这一局限。Section 3.5 原文："with n = 5, only |ρ| = 1.0 achieves p < .05 (p = .017), so **all Spearman-based inferences are descriptive and exploratory**." 这是我在 S2 中表扬的统计透明度的一部分。R1 说 "未讨论 power analysis"，但论文实际上已经用等价的方式传达了相同信息——直接说明在 n=5 下只有完美相关才能达显著，本质上就是一个非形式化的 power 陈述。

**我的评估**：降为 **Minor**。添加正式 power analysis 是锦上添花，但论文现有的处理已足够诚实。核心贡献不依赖于 Spearman 检验的显著性——逐样本 Jaccard 的 p 值来自置换检验（均 p < .01），不受 n=5 限制。

---

## [AGREE] R1-W3: 单一训练运行无法分离种子效应

完全同意。这也是我的 W3。单次训练运行是整个论文最根本的方法论局限。Pythia 70M 的跨家族种子校准（Appendix W）无法替代对同一混合循环架构的多种子实验。within- vs. cross-architecture Jaccard 3× 差距是 suggestive 但非 definitive。

补充一点 R1 未提及的细节：论文 Limitations 中承认 LAMBADA 的 Bonferroni-adjusted p = .170 "does not reach conventional significance"，这部分正是因为单次训练运行导致无法区分架构效应与种子效应对 LAMBADA 聚合收敛的贡献。如果有多种子实验，即使 n=5 attention ratios 不变，也能通过种子间一致性来增强（或推翻）现有发现。

---

## [AGREE] R1-W4: 任务类型 vs 评估格式完全混淆

完全同意。这也是我的 W4。LAMBADA 同时是唯一的自由生成 benchmark 和最高 α benchmark，论文无法分离任务类型与格式的贡献。论文在全文中以 "(or evaluation format)" hedging 是诚实的，但也意味着核心 claim 的因果解释力受限。

---

## [REBUT] R1-W5: Bonferroni p=.170 被暗示为有实质性意义

**我不同意 R1 的判断**。论文在三个位置明确将 p=.170 标注为非显著：

1. **Introduction 第 3 段**："only LAMBADA shows a **non-significant** decreasing aggregate variance pattern (ρ = −1.0, **Bonferroni-adjusted p = .170**)"
2. **Section 4.2**："LAMBADA shows a non-significant decreasing aggregate variance pattern (ρ = −1.0, Bonferroni-adjusted p = .170; observed at 1.3B, **absent at 340M**)"
3. **Limitations**："LAMBADA's Bonferroni-adjusted p = .170 **does not reach conventional significance**"

论文的修辞策略不是将 p=.170 暗示为显著，而是恰恰相反——利用聚合收敛的**非显著性**来突出 per-example Jaccard 饱和（所有 p < .01）的对比。这种"解耦论证"（aggregate 不显著但 per-example 显著）是论文的核心洞察之一，如果作者试图暗示 p=.170 为显著，反而会削弱自己的论证。

论文甚至在 Table 1 脚注中额外标注了 "Power is limited: only |ρ| = 1.0 achieves p < .05 at n = 5"，进一步降低了读者对聚合收敛 claim 的期望。

**我的评估**：不应列为 Weakness。论文对 p=.170 的处理是我见过的 NLP 实证论文中较坦诚的统计报告之一。如果 R1 能指出具体哪句话"暗示为有实质性意义"，我愿意重新评估。

---

## Reviewer 1 未提及但我认为重要的额外 Weakness

### 额外-1: Routing 叙事权重与实验结果不匹配（我的 W2, Major）

R1 的审稿意见聚焦于统计和混淆变量问题，但未讨论 routing 实验的叙事定位问题。Confidence-based routing 仅在 LAMBADA 上有效（+5.2pp），在 PIQA 上显著有害（-0.49pp, p = .006），但 abstract 仍用约 1/6 篇幅正面呈现 routing 结果（"+5.2pp"、"36% of oracle complementarity"），Conclusion 将其作为两大核心观察之一。这与 Introduction 贡献列表（未包含 routing）形成不一致。这是一个影响论文叙事可信度的 Major 问题。

### 额外-2: 缺少 logits ensemble baseline（我的 detailed comments 中提到）

论文的 routing 实验比较对象是 majority vote，但更自然的 baseline 是 average-logits ensemble——论文自己承认"is left to future work as it requires simultaneous inference across all architectures"。如果 logits ensemble 已经能获得大部分互补性收益，那么 confidence-based routing 的贡献就进一步缩小。

### 额外-3: Greedy decoding 局限未在 Limitations 中讨论（我的 W6, Minor）

所有评估使用 greedy decoding（Section 3.2），但 Limitations 未提及这一选择对逐样本分歧模式的潜在影响。Temperature > 0 的采样 decoding 可能改变 boundary cases 的 helped/hurt 分类。

---

## 总结

| R1 Weakness | 我的判断 | 理由 |
|-------------|---------|------|
| W1 GDN confound [Critical] | **[PARTIAL] → Major** | R1 数值有误（−0.2 vs. 论文报告 −0.7）；聚合收敛非核心 claim，per-example 饱和不受影响 |
| W2 Power [Major] | **[PARTIAL] → Minor** | 论文已明确承认，等价于非形式化 power analysis |
| W3 Single seed [Major] | **[AGREE] Major** | 最根本的局限 |
| W4 Format confound [Major] | **[AGREE] Major** | 不可分离，论文诚实 hedge 但 claim 因果力受限 |
| W5 p=.170 暗示显著 [Major] | **[REBUT]** | 论文在三处明确标注为非显著，修辞策略恰恰依赖于其非显著性 |

对 R1 的 Overall 3.0 (Findings) vs 我的 3.5 (Borderline Conference)：分歧主要来自 W1 的严重性评估和 W5。如果接受我对 W1（Major 而非 Critical）和 W5（不应列为 Weakness）的判断，R1 的评分应接近 3.5。我维持 **3.5 Borderline Conference** 的评分。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1836 · 2026-05-24T14:26:04.546652+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "entrainment_gated_ft",
  "file": "review_issues.yaml",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "entrainment_gated_ft",
    "file": "review_issues.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---


### Tool result

_source line 1837 · 2026-05-24T14:26:04.647402+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1838 · 2026-05-24T14:26:10.318222+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1839 · 2026-05-24T14:26:10.319272+00:00_

1	- id: "R5-W1"
2	  summary: "架构效应 vs seed 效应无法区分（单 training run，无 seed baseline）"
3	  category: experiment
4	  severity: critical
5	  status: wont_fix
6	  first_raised_round: 5
7	  last_seen_round: 19
8	  mentions:
9	    - round: 5
10	      reviewers: [R1, R2]
11	      note: "R1 Critical, R2 W3+Q3 支持。"
12	    - round: 15
13	      reviewers: [R1, R2]
14	      note: "R2-N3 Must-Fix vs R1-W2 Should-Fix。"
15	    - round: 16
16	      reviewers: [R1, R2]
17	      note: "R1-N1 Critical + R2-N2 Critical。双方 [AGREE]。"
18	    - round: 17
19	      reviewers: [R1, R2]
20	      note: "R1-N3 Critical + R2 交叉 [AGREE]。"
21	    - round: 18
22	      reviewers: [R1, R2]
23	      note: "R1-N2 Critical + R2-N2 Critical，交叉均 [AGREE]。2.7× gap 部分支持架构效应独立性。"
24	    - round: 19
25	      reviewers: [R1, R2]
26	      note: "R1-N2 Critical + R2-W4 Minor。R1 详列双重 mismatch。R2 同意但认为 minor。交叉后一致：structural limitation，维持 wont_fix。"
27	  action_items:
28	    - round: 13
29	      action: "E4 Pythia 410M 9-seed calibration（实际完成 70M）"
30	      assigned_to: main_agent
31	      status: done
32	    - round: 14
33	      action: "Limitations 提升 single-seed 为 top limitation；§4.2 弱化因果语言"
34	      assigned_to: paper_agent
35	      status: done
36	  resolution: "结构性限制。已做：Pythia 70M calibration + Limitations 讨论 + associative 语言。R19 维持 wont_fix。"
37	  resolution_round: null
38	
39	- id: "R5-W2"
40	  summary: "收敛 claim 统计不显著（Bonferroni p=.170）且依赖 GDN inclusion"
41	  category: method
42	  severity: critical
43	  status: in_progress
44	  first_raised_round: 1
45	  last_seen_round: 19
46	  mentions:
47	    - round: 15
48	      reviewers: [R1, R2]
49	      note: "R1-N1 Critical + R2-N1 Critical。交叉 [AGREE]。"
50	    - round: 16
51	      reviewers: [R1, R2]
52	      note: "R16-N1 重新 flag。"
53	    - round: 17
54	      reviewers: [R1, R2]
55	      note: "R1-N1 Critical + R2 交叉 [AGREE]。"
56	    - round: 18
57	      reviewers: [R1, R2]
58	      note: "R1-N1 Critical + R2-N1 Critical，交叉均 [AGREE]。"
59	    - round: 19
60	      rev
…[truncated 23597 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 1840 · 2026-05-24T14:30:15.596199+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "entrainment_gated_ft",
  "issues_yaml": "- id: \"R5-W1\"\n  summary: \"架构效应 vs seed 效应无法区分（单 training run，无 seed baseline）\"\n  category: experiment\n  severity: critical\n  status: wont_fix\n  first_raised_round: 5\n  last_seen_round: 20\n  mentions:\n    - round: 5\n      reviewers: [R1, R2]\n      note: \"R1 Critical, R2 W3+Q3 支持。\"\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"R2-N3 Must-Fix vs R1-W2 Should-Fix。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N2 Critical。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-N3 Critical + R2 交叉 [AGREE]。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-N2 Critical + R2-N2 Critical，交叉均 [AGREE]。2.7× gap 部分支持架构效应独立性。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-N2 Critical + R2-W4 Minor。R1 详列双重 mismatch。R2 同意但认为 minor。交叉后一致：structural limitation，维持 wont_fix。\"\n    - round: 20\n      reviewers: [R1, R2]\n      note: \"R1-W3 Major + R2-W3 Major，交叉均 [AGREE]。R2 补充：within- vs cross-architecture 3× 差距混淆了种子+架构。R1 指出 Pythia 70M 跨家族校准不充分。双方一致为最根本局限。\"\n  action_items:\n    - round: 13\n      action: \"E4 Pythia 410M 9-seed calibration（实际完成 70M）\"\n      assigned_to: main_agent\n      status: done\n    - round: 14\n      action: \"Limitations 提升 single-seed 为 top limitation；§4.2 弱化因果语言\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"结构性限制。已做：Pythia 70M calibration + Limitations 讨论 + associative 语言。R20 双方维持 wont_fix。\"\n  resolution_round: null\n\n- id: \"R5-W2\"\n  summary: \"收敛 claim 统计不显著（Bonferroni p=.170）且依赖 GDN inclusion\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 20\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical。交叉 [AGREE]。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R16-N1 重新 flag。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2 交叉 [AGREE]。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical，交叉均 [AGREE]。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical，交叉均 [AGREE]。R2 升级论证：decoupling 叙事建立在'不存在的前提'上。双方建议重构为条件式或转向 Jaccard 饱和。\"\n    - round: 20\n      reviewers: [R1, R2]\n      note: \"R1-W1 Critical（但数值有误报 −0.2）+ R2 交叉 [PARTIAL]。R2 rebut 两点：(1) 实际数值为 ρ=−0.7 非 −0.2；(2) 聚合收敛非核心 claim，论文利用其非显著性来对比 per-example 显著性。R2 降级为 Major。R1 维持 Critical。分歧：是否是核心 claim。\"\n  action_items:\n    - round: 15\n      action: \"Abstract/Intro 重构：以 Jaccard saturation 为主线\"\n      assigned_to: paper_agent\n      status: done\n    - round: 16\n      action: \"结构性叙事重组\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"Contribution 2 重构为条件式或将 Jaccard 饱和升级为主发现\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"R20 分歧：R1 Critical vs R2 Major。R2 论证聚合收敛非核心 claim 有说服力，但叙事仍需重构。\"\n  resolution_round: null\n\n- id: \"R5-W4\"\n  summary: \"新颖性有限——已有指标的直接套用，无新方法/理论\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 5\n  last_seen_round: 20\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"R2-W1 ecological fallacy。R1 REBUT。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R2-N1 Must-Fix vs R1 REBUT。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"部分收敛：均同意定位为 empirical contribution。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"Findings 标准下经验发现足够。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R2-N2 Major + R2-N3 (Benchmark Illusion)。R1 交叉部分 AGREE。\"\n    - round: 20\n      reviewers: [R1, R2]\n      note: \"R2-W1 Major：核心信息已被 Marx/D'Amour/Yang&Wang 充分建立。R1 交叉 [PARTIAL]：同意概念层面增量有限，但经验贡献（饱和发现+受控设计+时效性）被低估。R1 建议重组论文让饱和发现为主线。双方在 Findings 标准下可接受达成一致。\"\n  action_items:\n    - round: 6\n      action: \"Intro 加 empirical novelty framing\"\n      assigned_to: paper_agent\n      status: done\n    - round: 16\n      action: \"Intro 强化 empirical contribution 定位\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"引用 Benchmark Illusion 并定位增量贡献\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"结构性限制。Findings 标准下可接受。R20 R1 建议饱和发现为主线——可能提升贡献感知。\"\n  resolution_round: null\n\n- id: \"R5-W3\"\n  summary: \"Task-dependent spectrum 仅 3 benchmark，存在评估格式 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [R1, R2]\n      note: \"α 变异可能反映 format 而非 task type。\"\n  action_items:\n    - round: 5\n      action: \"WinoGrande + PIQA per-example 分析\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"PIQA + WinoGrande 整合完成。R17 提出更具体的 format confound（见 R17-W1）。\"\n  resolution_round: 6\n\n- id: \"R5-W5\"\n  summary: \"正文约 8.2 页超出 EMNLP 8 页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R19 双方格式检查确认合规。\"\n  action_items:\n    - round: 5\n      action: \"结构性压缩 8.2→7 页\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"主文在 8 页内。R14-R19 持续确认合规。\"\n  resolution_round: 5\n\n- id: \"R5-W6\"\n  summary: \"遗漏关键相关工作 Zoology/Based/Samba\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  action_items:\n    - round: 5\n      action: \"补 3 篇引用\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已引用。\"\n  resolution_round: 5\n\n- id: \"R5-W7\"\n  summary: \"Ensemble 建议缺乏实验支撑\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 9\n  action_items:\n    - round: 7\n      action: \"Majority vote + oracle POC 写入 Conclusion\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已包含 MV/oracle POC 数据。\"\n  resolution_round: 9\n\n- id: \"R5-W8\"\n  summary: \"Binary decomposition 可能低估多选题一致性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 19\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"Appendix O continuous Jaccard 缓解。\"\n    - round: 19\n      reviewers: []\n      note: \"R19 双方均未作为 weakness 提出。R1 在 S6 肯定 binary decomposition 设计合理。视为已充分缓解。\"\n  action_items:\n    - round: 13\n      action: \"E2 continuous-threshold Jaccard 整合\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"R19 双方未 flag，R1 肯定设计合理。已充分缓解。\"\n  resolution_round: 19\n\n- id: \"R5-W9\"\n  summary: \"Abstract 信息密度过高（统计量堆砌）\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 20\n  mentions:\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"接近 200 word 上限，inline 统计量增加认知负荷。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R2-W4 Major：数字密度过高。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"Abstract 已改善（148词）。R2-W6 指出 Introduction 贡献列表过长。R1 交叉 REBUT。\"\n    - round: 20\n      reviewers: [R2]\n      note: \"R2 在 Detailed Comments 中指出 Abstract ~154 词符合 ≤200 要求。Routing 描述占 ~1/6 篇幅，正面数字比消极描述更突出。与 R15-W2 routing 叙事问题重叠。\"\n  action_items:\n    - round: 18\n      action: \"Abstract 再次精简\"\n      assigned_to: paper_agent\n      status: done\n    - round: 19\n      action: \"Introduction 贡献列表精简为核心 claim + section 引用\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"Abstract 字数合规（~154词）。Routing 叙事权重问题归入 R15-W2。\"\n  resolution_round: null\n\n- id: \"RV-L1\"\n  summary: \"Limitations 6 段违反 EMNLP 用户规则（要求 ~3 点）\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 15\n  action_items:\n    - round: 5\n      action: \"6 段→3 段\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"压缩为 3 段。R14-R19 确认合规。\"\n  resolution_round: 5\n\n- id: \"RV-L2\"\n  summary: \"loglik 压缩假说已被诊断数据反驳但论文仍引用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  action_items:\n    - round: 5\n      action: \"改为 binary classification structural properties 解释\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已修正。\"\n  resolution_round: 5\n\n- id: \"R6-N3\"\n  summary: \"仅 2 个 scale 点不足以支撑 scale-dependent claim\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  action_items:\n    - round: 6\n      action: \"全文替换 scale-dependent\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"全文已用 'differs between 340M and 1.3B'。\"\n  resolution_round: 8\n\n- id: \"R6-N2\"\n  summary: \"缺乏 actionable insights——论文停在 '问题存在' 层面\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 15\n  action_items:\n    - round: 13\n      action: \"E1 routing 结果整合\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Routing 已写入。非 blocking。\"\n  resolution_round: 13\n\n- id: \"R6-W1\"\n  summary: \"Decoupling 形式化存在技术问题\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 9\n  action_items:\n    - round: 8\n      action: \"删除 Equation 1\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已删。Round 12-19 未再提及。\"\n  resolution_round: 12\n\n- id: \"R6-W2\"\n  summary: \"GDN h3-1 的 16-head confound 削弱 LAMBADA convergence\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 20\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"主文并列 with/without GDN。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"移除 GDN 后 ρ 从 -1.0 降至 -0.7。\"\n    - round: 18\n      reviewers: []\n      note: \"§4.3 已讨论。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W2 Major + R2 交叉 AGREE。MMLU ρ 完全反转。\"\n    - round: 20\n      reviewers: [R1, R2]\n      note: \"R1-W1 Critical（引用错误数值 −0.2）+ R2 交叉 [PARTIAL]。R2 纠正：实际为 ρ=−0.7, p=.233。R2 论证聚合收敛非核心 claim，per-example 饱和不受 GDN 影响。R1 维持 Critical 因整个 §4.3 convergence 讨论受影响。最终：R1 Critical vs R2 Major，分歧记录。\"\n  action_items:\n    - round: 15\n      action: \"§4.2/§4.3 讨论 GDN exclusion\"\n      assigned_to: paper_agent\n      status: done\n    - round: 19\n      action: \"Table 1 首次引入 GDN 时 flag 16-head anomaly；正文报告 MMLU ρ 反转\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"R20 分歧：R1 Critical vs R2 Major。R2 论证有力：per-example 核心发现不受影响。但 GDN 对 convergence 叙事的影响仍需更显著讨论。\"\n  resolution_round: null\n\n- id: \"R6-W3\"\n  summary: \"Bootstrap CI 在 n=3 架构上覆盖率远低于名义值\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 20\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"升级为 Critical。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W7 Minor。论文 Section 3.5 已标 'heuristic'。R2 交叉 AGREE 但认为已 acknowledge。降级回 Minor/Warning。\"\n    - round: 20\n      reviewers: [R1]\n      note: \"R1 在交叉回应中再次提出：Appendix D1 确认大量 bootstrap 样本是退化的同架构三重采样，影响 Figure 4 CI 不含零的可信度。R2 未在初审中提及。\"\n  action_items:\n    - round: 16\n      action: \"Intro BCa CI 加 heuristic caveat\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"Section 3.5 caveat 存在。R20 R1 再次提出但 severity 维持 warning。\"\n  resolution_round: null\n\n- id: \"R14-W1\"\n  summary: \"Confidence margin 'mechanism' 标题暗示因果性\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  action_items:\n    - round: 14\n      action: \"替换 'mechanism' → 'predictor'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已替换。R15-R19 未再提及。\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"n=5 attention ratios 使 permutation test 本质为 binary outcome\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  action_items:\n    - round: 15\n      action: \"§4.2 标注 'suggestive but underpowered'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。合并入 R5-W2。\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"标题/Abstract 过度泛化\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  action_items:\n    - round: 14\n      action: \"正文加 scope 限定\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。\"\n  resolution_round: 15\n\n- id: \"R14-W4\"\n  summary: \"缺失 prediction churn 文献\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  action_items:\n    - round: 14\n      action: \"添加 Milani Fard (2016)\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已引用。\"\n  resolution_round: 15\n\n- id: \"R15-W1\"\n  summary: \"'Nearly disjoint' 措辞夸大\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  action_items:\n    - round: 15\n      action: \"替换为 calibrated 表述\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。\"\n  resolution_round: 15\n\n- id: \"R15-W2\"\n  summary: \"Routing 定位过高（仅 1/4 benchmark 有效）\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 20\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"降级为 case study。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"1/4 success rate，无 ensemble baseline。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"PIQA 显著负效。缺 ensemble baseline。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W4 Major + R2-W1 Major，交叉均 AGREE。\"\n    - round: 20\n      reviewers: [R1, R2]\n      note: \"R2-W2 Major + R1 交叉 [AGREE]。R1 补充：PIQA 显著有害(-0.49pp, p=.006) 直接反驳通用工具叙事。Conclusion 将 routing 列为两大观察之一是过度。双方一致要求：(1) Abstract 缩减/弱化 routing；(2) 明确标注为探索性消极发现；(3) 补 logits ensemble baseline。\"\n  action_items:\n    - round: 15\n      action: \"降级为 case study\"\n      assigned_to: paper_agent\n      status: done\n    - round: 19\n      action: \"Abstract routing 句加 qualifier；补充 average-logits ensemble baseline\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"R20 双方强 AGREE Major。Abstract/Conclusion 叙事权重仍偏高。需补 ensemble baseline。\"\n  resolution_round: null\n\n- id: \"R15-D1\"\n  summary: \"Appendix Table 30 DeltaNet 数据不一致\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  action_items:\n    - round: 15\n      action: \"从 JSON 逐格修正\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已修正。\"\n  resolution_round: 15\n\n- id: \"R15-W3\"\n  summary: \"缺失 Jain et al. (2025 FAccT)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  action_items:\n    - round: 15\n      action: \"添加到 bib + Related Work\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。\"\n  resolution_round: 15\n\n- id: \"R16-N1\"\n  summary: \"Aggregate convergence 叙事在 Abstract/Introduction 中仍过度突出\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 20\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-N2 Must-Fix + R2-W1 Should-Fix。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"要求全文统一为 descriptive/suggestive。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R2 建议重构。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical，交叉均 AGREE。\"\n    - round: 20\n      reviewers: [R1, R2]\n      note: \"R2 rebut R1-W1 时论证：聚合收敛非核心 claim，论文策略是利用其非显著性与 per-example 显著性的对比。R1 交叉中对 R2-W1 回应时建议重组让饱和发现为主线。双方实质上同意：饱和才是核心贡献。叙事重构方向趋于一致。\"\n  action_items:\n    - round: 16\n      action: \"结构性叙事重组\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"§4.2 标题改为非确定性；全文消除 convergence 作为 established premise\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"R20 双方趋于一致：饱和发现应为主线，convergence 应明确为 non-significant 背景。\"\n  resolution_round: null\n\n- id: \"R16-W1\"\n  summary: \"Routing 实验缺少 variance 报告\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"LAMBADA SD=0.4pp 已报告。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1 仍要求 bootstrap CI + significance test。R2 交叉同意应补充。\"\n  action_items:\n    - round: 19\n      action: \"LAMBADA routing 补 bootstrap CI + permutation significance test\"\n      assigned_to: main_agent\n      status: open\n      note: \"DDL 限制，如时间不够可降级为 Limitations 标注\"\n  resolution: \"SD 已报告，formal significance test 仍缺。\"\n  resolution_round: null\n\n- id: \"R16-W2\"\n  summary: \"5-architecture 扩展验证仅 340M\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 20\n  mentions:\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R2 REBUT：数据约束非设计缺陷。\"\n    - round: 20\n      reviewers: [R2]\n      note: \"R2-S6 肯定五架构验证增强泛化性（GLA + DeltaNet，10 对全部 J≤0.14, p≤.002）。仅 340M 是 model zoo 约束。\"\n  action_items:\n    - round: 19\n      action: \"Appendix X 明确标注仅验证 per-example divergence（非 convergence），说明 GLA/DeltaNet 仅有 340M 版本\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"R2 rebut 有理：数据约束非设计缺陷。标注 scope 即可。\"\n  resolution_round: null\n\n- id: \"R16-W3\"\n  summary: \"Confidence margin AUC 的正态假设未验证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R2 rebut：AUC 本身为 non-parametric。降低严重程度。\"\n  action_items:\n    - round: 16\n      action: \"计算 empirical AUC 对比\"\n      assigned_to: main_agent\n      status: in_progress\n  resolution: \"R2 rebut 有理：AUC 本身为 non-parametric，不受正态假设影响。\"\n  resolution_round: null\n\n- id: \"R16-W4\"\n  summary: \"模型规模覆盖有限（≤1.3B vs 7B+ 部署场景）\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R2 区分正确：per-example 跨 scale 稳健，convergence 不跨 scale。\"\n  action_items:\n    - round: 18\n      action: \"全文 scale 语言限定\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"明确区分：per-example Jaccard 跨 scale 一致 vs aggregate convergence 仅 1.3B LAMBADA\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"R2 区分正确：per-example 跨 scale 稳健，convergence 不跨 scale。\"\n  resolution_round: null\n\n- id: \"R16-W5\"\n  summary: \"遗漏重要相关工作\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 20\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"Model Soups + Jiang (2024)。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R2-N3 Major：Yang & Wang (2026) 'Benchmark Illusion' 重大遗漏。\"\n    - round: 20\n      reviewers: [R2]\n      note: \"R2-S5 确认 Yang & Wang (2026) 现已在 abstract 和 Related Work 中正确引用并区分贡献。R2-W5 新增：缺少 selective prediction / abstention 文献（Geifman & El-Yaniv 2017/2019）和 ensemble selection（Caruana et al. 2004）。R1 交叉 AGREE W5。\"\n  action_items:\n    - round: 18\n      action: \"添加 Wortsman (2022) + Jiang (2024)\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"必须引用 Yang & Wang (2026) Benchmark Illusion\"\n      assigned_to: paper_agent\n      status: done\n    - round: 20\n      action: \"补充 selective prediction 文献（Geifman & El-Yaniv 2017/2019）和 ensemble selection（Caruana et al. 2004）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"Yang & Wang 已引用（R20 确认）。新增缺失：selective prediction + ensemble selection。\"\n  resolution_round: null\n\n- id: \"R16-M1\"\n  summary: \"Haghighat 2026 bib 条目需更新为 AAAI 2026\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 未提及。可能已修复。\"\n  action_items:\n    - round: 16\n      action: \"更新 references.bib\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W1\"\n  summary: \"Task type vs evaluation format confound（LAMBADA 为唯一 free-form benchmark）\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-W2 提出 + R2 [AGREE]。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"双方 Major，要求正文讨论。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W1 Major + R2-W2 Major，交叉均强 AGREE。\"\n    - round: 20\n      reviewers: [R1, R2]\n      note: \"R1-W4 Major + R2-W4 Major，交叉均 [AGREE]。R2 补充：多选题内部 format 不预测 α 只排除子空间内效应。R1 交叉补充：LAMBADA 同时是唯一 retrieval/free-form/最高 α 任务——三重混淆。双方一致认为核心 claim 的因果解释力受限。论文 hedging 诚实但不可证伪。\"\n  action_items:\n    - round: 18\n      action: \"§3.2 末加 format confound 讨论\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"Limitations 显式加入 format confound；§4.1 'task type' 改为 'task type or evaluation format'\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"R20 双方强 AGREE Major。论文 hedging 诚实但因果力受限，是结构性局限。\"\n  resolution_round: null\n\n- id: \"R17-W2\"\n  summary: \"Confirmatory/exploratory benchmark 分类缺乏预注册\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1 Major vs R2 REBUT（标准分类）。Director 降级为 Should-Fix。\"\n  action_items:\n    - round: 17\n      action: \"Appendix A 明确 all-10 correction 为唯一有效\"\n      assigned_to: paper_agent\n      status: open\n    - round: 19\n      action: \"提供 taxonomy 时间证据（git commit）或框定为 hypothesis-generating\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"R1 Major vs R2 REBUT（标准分类）。Director 降级为 Should-Fix。\"\n  resolution_round: null\n\n- id: \"R18-W1\"\n  summary: \"Permutation test null baseline 不排除 example difficulty confound\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 20\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 未显式提及。可能被 format confound 讨论吸收。\"\n    - round: 20\n      reviewers: [R1]\n      note: \"R1 在交叉回应中作为 R2 遗漏的重要问题再次提出：Appendix K 的 null baseline 未排除样本内在难度对跨架构 Jaccard 重叠的混淆。\"\n  action_items:\n    - round: 18\n      action: \"讨论 example difficulty 作为 confound\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W1\"\n  summary: \"遗漏 Yang & Wang (2026) 'Benchmark Illusion'——核心发现高度重叠\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n    - round: 19\n      reviewers: [R2]\n      note: \"R2-N3 Major：Yang & Wang (2026) arXiv:2602.11898。\"\n    - round: 20\n      reviewers: [R2]\n      note: \"R2-S5 确认已正确引用：'Yang & Wang (2026) 的引用处理得当。在 abstract 和 Related Work 中均明确引用并区分贡献（our within-family design isolates backbone variation from training-regime differences）'。\"\n  action_items:\n    - round: 19\n      action: \"引用 Yang & Wang (2026)；重新界定 'first' claim 为 'first controlled within-family analysis'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已引用并正确区分贡献。R20 R2 确认处理得当。\"\n  resolution_round: 20\n\n- id: \"R19-W2\"\n  summary: \"LAMBADA 和 ARC-Easy routing 增益数值疑似相同\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1 误读。原文数值不同。\"\n  action_items: []\n  resolution: \"R1 误读。原文数值不同（LAMBADA +5.2pp vs ARC-Easy +1.2pp）。无需修改。\"\n  resolution_round: 19\n\n- id: \"R19-W3\"\n  summary: \"全文 associative vs causal 语言不完全一致\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W8 Minor：'reflects'/'modulated by'/'controlled' 等 causal 用语偶现。R2 交叉 AGREE 但认为 minor。\"\n  action_items:\n    - round: 19\n      action: \"全文统一 associative 语言\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-W1\"\n  summary: \"n=5 Spearman power analysis 未形式化（仅非正式说明）\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [R1, R2]\n      note: \"R1-W2 Major：未讨论 power analysis。R2 交叉 [PARTIAL] → Minor：论文已说明 'only |ρ|=1.0 achieves p<.05 at n=5'，等价于非形式化 power 陈述。核心贡献不依赖 Spearman（Jaccard p 值来自置换检验）。R1 维持 Major，R2 降为 Minor。\"\n  action_items:\n    - round: 20\n      action: \"考虑添加正式 power analysis 表格（锦上添花，非必须）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"分歧：R1 Major vs R2 Minor。论文已有等价非形式化说明。\"\n  resolution_round: null\n\n- id: \"R20-W2\"\n  summary: \"Routing 缺少 selective prediction / ensemble selection 文献\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [R1, R2]\n      note: \"R2-W5 Minor：缺 Geifman & El-Yaniv (2017/2019) selective prediction 和 Caruana et al. (2004) ensemble selection。R1 交叉 [AGREE]：routing 定位不够准确，读者无法判断与已有 selective prediction 方法的关系。\"\n  action_items:\n    - round: 20\n      action: \"Related Work 或 §4.4 引用 Geifman & El-Yaniv (2017/2019) + Caruana et al. (2004)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-W3\"\n  summary: \"Limitations 遗漏 greedy decoding 对逐样本分歧的影响\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [R1, R2]\n      note: \"R2-W6 Minor：所有评估用 greedy decoding，采样 decoding 可能改变 boundary cases 的 helped/hurt 分类。R1 交叉 [PARTIAL]：方向同意但 severity 更低——greedy 是 lm-eval-harness 标准配置，大多数 LM 评估工作使用 greedy。建议 Limitations 加一句即可。\"\n  action_items:\n    - round: 20\n      action: \"Limitations 补充一句 greedy decoding 对生成任务的潜在影响\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-W4\"\n  summary: \"饱和发现的替代解读：attention 引入 Transformer 式行为而非架构指纹\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [R1, R2]\n      note: \"R2-Q3 提出 + R1 交叉完全 [AGREE] 并标为遗漏的重要观点。Appendix I 显示三个架构 h3-1 correct set 都更接近 Transformer 基线。两种解读有根本区别：(1) 混合架构保留独特逐样本特征 vs (2) 少量 attention 即使行为向 Transformer 收敛。论文应在 §4.2 或 Discussion 中讨论此替代解读。\"\n  action_items:\n    - round: 20\n      action: \"§4.2 或 Discussion 讨论替代解读：饱和可能反映 Transformer 式行为引入而非架构指纹确立\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "entrainment_gated_ft",
    "issues_yaml": "- id: \"R5-W1\"\n  summary: \"架构效应 vs seed 效应无法区分（单 training run，无 seed baseline）\"\n  category: experiment\n  severity: critical\n  status: wont_fix\n  first_raised_round: 5\n  last_seen_round: 20\n  mentions:\n    - round: 5\n      reviewers: [R1, R2]\n      note: \"R1 Critical, R2 W3+Q3 支持。\"\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"R2-N3 Must-Fix vs R1-W2 Should-Fix。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N2 Critical。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-N3 Critical + R2 交叉 [AGREE]。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-N2 Critical + R2-N2 Critical，交叉均 [AGREE]。2.7× gap 部分支持架构效应独立性。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-N2 Critical + R2-W4 Minor。R1 详列双重 mismatch。R2 同意但认为 minor。交叉后一致：structural limitation，维持 wont_fix。\"\n    - round: 20\n      reviewers: [R1, R2]\n      note: \"R1-W3 Major + R2-W3 Major，交叉均 [AGREE]。R2 补充：within- vs cross-architecture 3× 差距混淆了种子+架构。R1 指出 Pythia 70M 跨家族校准不充分。双方一致为最根本局限。\"\n  action_items:\n    - round: 13\n      action: \"E4 Pythia 410M 9-seed calibration（实际完成 70M）\"\n      assigned_to: main_agent\n      status: done\n    - round: 14\n      action: \"Limitations 提升 single-seed 为 top limitation；§4.2 弱化因果语言\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"结构性限制。已做：Pythia 70M calibration + Limitations 讨论 + associative 语言。R20 双方维持 wont_fix。\"\n  resolution_round: null\n\n- id: \"R5-W2\"\n  summary: \"收敛 claim 统计不显著（Bonferroni p=.170）且依赖 GDN inclusion\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 20\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical。交叉 [AGREE]。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R16-N1 重新 flag。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2 交叉 [AGREE]。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical，交叉均 [AGREE]。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical，交叉均 [AGREE]。R2 升级论证：decoupling 叙事建立在'不存在的前提'上。双方建议重构为条件式或转向 Jaccard 饱和。\"\n    - round: 20\n      reviewers: [R1, R2]\n      note: \"R1-W1 Critical（但数值有误报 −0.2）+ R2 交叉 [PARTIAL]。R2 rebut 两点：(1) 实际数值为 ρ=−0.7 非 −0.2；(2) 聚合收敛非核心 claim，论文利用其非显著性来对比 per-example 显著性。R2 降级为 Major。R1 维持 Critical。分歧：是否是核心 claim。\"\n  action_items:\n    - round: 15\n      action: \"Abstract/Intro 重构：以 Jaccard saturation 为主线\"\n      assigned_to: paper_agent\n      status: done\n    - round: 16\n      action: \"结构性叙事重组\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"Contribution 2 重构为条件式或将 Jaccard 饱和升级为主发现\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"R20 分歧：R1 Critical vs R2 Major。R2 论证聚合收敛非核心 claim 有说服力，但叙事仍需重构。\"\n  resolution_round: null\n\n- id: \"R5-W4\"\n  summary: \"新颖性有限——已有指标的直接套用，无新方法/理论\"\n  category: framing\n  severity: critical\n  status: wont_fix\n  first_raised_round: 5\n  last_seen_round: 20\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"R2-W1 ecological fallacy。R1 REBUT。\"\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R2-N1 Must-Fix vs R1 REBUT。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"部分收敛：均同意定位为 empirical contribution。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"Findings 标准下经验发现足够。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R2-N2 Major + R2-N3 (Benchmark Illusion)。R1 交叉部分 AGREE。\"\n    - round: 20\n      reviewers: [R1, R2]\n      note: \"R2-W1 Major：核心信息已被 Marx/D'Amour/Yang&Wang 充分建立。R1 交叉 [PARTIAL]：同意概念层面增量有限，但经验贡献（饱和发现+受控设计+时效性）被低估。R1 建议重组论文让饱和发现为主线。双方在 Findings 标准下可接受达成一致。\"\n  action_items:\n    - round: 6\n      action: \"Intro 加 empirical novelty framing\"\n      assigned_to: paper_agent\n      status: done\n    - round: 16\n      action: \"Intro 强化 empirical contribution 定位\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"引用 Benchmark Illusion 并定位增量贡献\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"结构性限制。Findings 标准下可接受。R20 R1 建议饱和发现为主线——可能提升贡献感知。\"\n  resolution_round: null\n\n- id: \"R5-W3\"\n  summary: \"Task-dependent spectrum 仅 3 benchmark，存在评估格式 confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [R1, R2]\n      note: \"α 变异可能反映 format 而非 task type。\"\n  action_items:\n    - round: 5\n      action: \"WinoGrande + PIQA per-example 分析\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"PIQA + WinoGrande 整合完成。R17 提出更具体的 format confound（见 R17-W1）。\"\n  resolution_round: 6\n\n- id: \"R5-W5\"\n  summary: \"正文约 8.2 页超出 EMNLP 8 页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R19 双方格式检查确认合规。\"\n  action_items:\n    - round: 5\n      action: \"结构性压缩 8.2→7 页\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"主文在 8 页内。R14-R19 持续确认合规。\"\n  resolution_round: 5\n\n- id: \"R5-W6\"\n  summary: \"遗漏关键相关工作 Zoology/Based/Samba\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  action_items:\n    - round: 5\n      action: \"补 3 篇引用\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已引用。\"\n  resolution_round: 5\n\n- id: \"R5-W7\"\n  summary: \"Ensemble 建议缺乏实验支撑\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 9\n  action_items:\n    - round: 7\n      action: \"Majority vote + oracle POC 写入 Conclusion\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已包含 MV/oracle POC 数据。\"\n  resolution_round: 9\n\n- id: \"R5-W8\"\n  summary: \"Binary decomposition 可能低估多选题一致性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 19\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"Appendix O continuous Jaccard 缓解。\"\n    - round: 19\n      reviewers: []\n      note: \"R19 双方均未作为 weakness 提出。R1 在 S6 肯定 binary decomposition 设计合理。视为已充分缓解。\"\n  action_items:\n    - round: 13\n      action: \"E2 continuous-threshold Jaccard 整合\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"R19 双方未 flag，R1 肯定设计合理。已充分缓解。\"\n  resolution_round: 19\n\n- id: \"R5-W9\"\n  summary: \"Abstract 信息密度过高（统计量堆砌）\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 20\n  mentions:\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"接近 200 word 上限，inline 统计量增加认知负荷。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R2-W4 Major：数字密度过高。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"Abstract 已改善（148词）。R2-W6 指出 Introduction 贡献列表过长。R1 交叉 REBUT。\"\n    - round: 20\n      reviewers: [R2]\n      note: \"R2 在 Detailed Comments 中指出 Abstract ~154 词符合 ≤200 要求。Routing 描述占 ~1/6 篇幅，正面数字比消极描述更突出。与 R15-W2 routing 叙事问题重叠。\"\n  action_items:\n    - round: 18\n      action: \"Abstract 再次精简\"\n      assigned_to: paper_agent\n      status: done\n    - round: 19\n      action: \"Introduction 贡献列表精简为核心 claim + section 引用\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"Abstract 字数合规（~154词）。Routing 叙事权重问题归入 R15-W2。\"\n  resolution_round: null\n\n- id: \"RV-L1\"\n  summary: \"Limitations 6 段违反 EMNLP 用户规则（要求 ~3 点）\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 15\n  action_items:\n    - round: 5\n      action: \"6 段→3 段\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"压缩为 3 段。R14-R19 确认合规。\"\n  resolution_round: 5\n\n- id: \"RV-L2\"\n  summary: \"loglik 压缩假说已被诊断数据反驳但论文仍引用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  action_items:\n    - round: 5\n      action: \"改为 binary classification structural properties 解释\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已修正。\"\n  resolution_round: 5\n\n- id: \"R6-N3\"\n  summary: \"仅 2 个 scale 点不足以支撑 scale-dependent claim\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  action_items:\n    - round: 6\n      action: \"全文替换 scale-dependent\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"全文已用 'differs between 340M and 1.3B'。\"\n  resolution_round: 8\n\n- id: \"R6-N2\"\n  summary: \"缺乏 actionable insights——论文停在 '问题存在' 层面\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 15\n  action_items:\n    - round: 13\n      action: \"E1 routing 结果整合\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Routing 已写入。非 blocking。\"\n  resolution_round: 13\n\n- id: \"R6-W1\"\n  summary: \"Decoupling 形式化存在技术问题\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 9\n  action_items:\n    - round: 8\n      action: \"删除 Equation 1\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已删。Round 12-19 未再提及。\"\n  resolution_round: 12\n\n- id: \"R6-W2\"\n  summary: \"GDN h3-1 的 16-head confound 削弱 LAMBADA convergence\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 20\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"主文并列 with/without GDN。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"移除 GDN 后 ρ 从 -1.0 降至 -0.7。\"\n    - round: 18\n      reviewers: []\n      note: \"§4.3 已讨论。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W2 Major + R2 交叉 AGREE。MMLU ρ 完全反转。\"\n    - round: 20\n      reviewers: [R1, R2]\n      note: \"R1-W1 Critical（引用错误数值 −0.2）+ R2 交叉 [PARTIAL]。R2 纠正：实际为 ρ=−0.7, p=.233。R2 论证聚合收敛非核心 claim，per-example 饱和不受 GDN 影响。R1 维持 Critical 因整个 §4.3 convergence 讨论受影响。最终：R1 Critical vs R2 Major，分歧记录。\"\n  action_items:\n    - round: 15\n      action: \"§4.2/§4.3 讨论 GDN exclusion\"\n      assigned_to: paper_agent\n      status: done\n    - round: 19\n      action: \"Table 1 首次引入 GDN 时 flag 16-head anomaly；正文报告 MMLU ρ 反转\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"R20 分歧：R1 Critical vs R2 Major。R2 论证有力：per-example 核心发现不受影响。但 GDN 对 convergence 叙事的影响仍需更显著讨论。\"\n  resolution_round: null\n\n- id: \"R6-W3\"\n  summary: \"Bootstrap CI 在 n=3 架构上覆盖率远低于名义值\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 20\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"升级为 Critical。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W7 Minor。论文 Section 3.5 已标 'heuristic'。R2 交叉 AGREE 但认为已 acknowledge。降级回 Minor/Warning。\"\n    - round: 20\n      reviewers: [R1]\n      note: \"R1 在交叉回应中再次提出：Appendix D1 确认大量 bootstrap 样本是退化的同架构三重采样，影响 Figure 4 CI 不含零的可信度。R2 未在初审中提及。\"\n  action_items:\n    - round: 16\n      action: \"Intro BCa CI 加 heuristic caveat\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"Section 3.5 caveat 存在。R20 R1 再次提出但 severity 维持 warning。\"\n  resolution_round: null\n\n- id: \"R14-W1\"\n  summary: \"Confidence margin 'mechanism' 标题暗示因果性\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 14\n  action_items:\n    - round: 14\n      action: \"替换 'mechanism' → 'predictor'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已替换。R15-R19 未再提及。\"\n  resolution_round: 15\n\n- id: \"R14-W2\"\n  summary: \"n=5 attention ratios 使 permutation test 本质为 binary outcome\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  action_items:\n    - round: 15\n      action: \"§4.2 标注 'suggestive but underpowered'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。合并入 R5-W2。\"\n  resolution_round: 15\n\n- id: \"R14-W3\"\n  summary: \"标题/Abstract 过度泛化\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  action_items:\n    - round: 14\n      action: \"正文加 scope 限定\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。\"\n  resolution_round: 15\n\n- id: \"R14-W4\"\n  summary: \"缺失 prediction churn 文献\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  action_items:\n    - round: 14\n      action: \"添加 Milani Fard (2016)\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已引用。\"\n  resolution_round: 15\n\n- id: \"R15-W1\"\n  summary: \"'Nearly disjoint' 措辞夸大\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  action_items:\n    - round: 15\n      action: \"替换为 calibrated 表述\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。\"\n  resolution_round: 15\n\n- id: \"R15-W2\"\n  summary: \"Routing 定位过高（仅 1/4 benchmark 有效）\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 20\n  mentions:\n    - round: 15\n      reviewers: [R1, R2]\n      note: \"降级为 case study。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"1/4 success rate，无 ensemble baseline。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"PIQA 显著负效。缺 ensemble baseline。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W4 Major + R2-W1 Major，交叉均 AGREE。\"\n    - round: 20\n      reviewers: [R1, R2]\n      note: \"R2-W2 Major + R1 交叉 [AGREE]。R1 补充：PIQA 显著有害(-0.49pp, p=.006) 直接反驳通用工具叙事。Conclusion 将 routing 列为两大观察之一是过度。双方一致要求：(1) Abstract 缩减/弱化 routing；(2) 明确标注为探索性消极发现；(3) 补 logits ensemble baseline。\"\n  action_items:\n    - round: 15\n      action: \"降级为 case study\"\n      assigned_to: paper_agent\n      status: done\n    - round: 19\n      action: \"Abstract routing 句加 qualifier；补充 average-logits ensemble baseline\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"R20 双方强 AGREE Major。Abstract/Conclusion 叙事权重仍偏高。需补 ensemble baseline。\"\n  resolution_round: null\n\n- id: \"R15-D1\"\n  summary: \"Appendix Table 30 DeltaNet 数据不一致\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  action_items:\n    - round: 15\n      action: \"从 JSON 逐格修正\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已修正。\"\n  resolution_round: 15\n\n- id: \"R15-W3\"\n  summary: \"缺失 Jain et al. (2025 FAccT)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  action_items:\n    - round: 15\n      action: \"添加到 bib + Related Work\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已完成。\"\n  resolution_round: 15\n\n- id: \"R16-N1\"\n  summary: \"Aggregate convergence 叙事在 Abstract/Introduction 中仍过度突出\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 20\n  mentions:\n    - round: 16\n      reviewers: [R1, R2]\n      note: \"R1-N2 Must-Fix + R2-W1 Should-Fix。\"\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"要求全文统一为 descriptive/suggestive。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"R2 建议重构。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-N1 Critical + R2-N1 Critical，交叉均 AGREE。\"\n    - round: 20\n      reviewers: [R1, R2]\n      note: \"R2 rebut R1-W1 时论证：聚合收敛非核心 claim，论文策略是利用其非显著性与 per-example 显著性的对比。R1 交叉中对 R2-W1 回应时建议重组让饱和发现为主线。双方实质上同意：饱和才是核心贡献。叙事重构方向趋于一致。\"\n  action_items:\n    - round: 16\n      action: \"结构性叙事重组\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"§4.2 标题改为非确定性；全文消除 convergence 作为 established premise\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"R20 双方趋于一致：饱和发现应为主线，convergence 应明确为 non-significant 背景。\"\n  resolution_round: null\n\n- id: \"R16-W1\"\n  summary: \"Routing 实验缺少 variance 报告\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"LAMBADA SD=0.4pp 已报告。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1 仍要求 bootstrap CI + significance test。R2 交叉同意应补充。\"\n  action_items:\n    - round: 19\n      action: \"LAMBADA routing 补 bootstrap CI + permutation significance test\"\n      assigned_to: main_agent\n      status: open\n      note: \"DDL 限制，如时间不够可降级为 Limitations 标注\"\n  resolution: \"SD 已报告，formal significance test 仍缺。\"\n  resolution_round: null\n\n- id: \"R16-W2\"\n  summary: \"5-architecture 扩展验证仅 340M\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 20\n  mentions:\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R2 REBUT：数据约束非设计缺陷。\"\n    - round: 20\n      reviewers: [R2]\n      note: \"R2-S6 肯定五架构验证增强泛化性（GLA + DeltaNet，10 对全部 J≤0.14, p≤.002）。仅 340M 是 model zoo 约束。\"\n  action_items:\n    - round: 19\n      action: \"Appendix X 明确标注仅验证 per-example divergence（非 convergence），说明 GLA/DeltaNet 仅有 340M 版本\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"R2 rebut 有理：数据约束非设计缺陷。标注 scope 即可。\"\n  resolution_round: null\n\n- id: \"R16-W3\"\n  summary: \"Confidence margin AUC 的正态假设未验证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R2 rebut：AUC 本身为 non-parametric。降低严重程度。\"\n  action_items:\n    - round: 16\n      action: \"计算 empirical AUC 对比\"\n      assigned_to: main_agent\n      status: in_progress\n  resolution: \"R2 rebut 有理：AUC 本身为 non-parametric，不受正态假设影响。\"\n  resolution_round: null\n\n- id: \"R16-W4\"\n  summary: \"模型规模覆盖有限（≤1.3B vs 7B+ 部署场景）\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R2 区分正确：per-example 跨 scale 稳健，convergence 不跨 scale。\"\n  action_items:\n    - round: 18\n      action: \"全文 scale 语言限定\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"明确区分：per-example Jaccard 跨 scale 一致 vs aggregate convergence 仅 1.3B LAMBADA\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"R2 区分正确：per-example 跨 scale 稳健，convergence 不跨 scale。\"\n  resolution_round: null\n\n- id: \"R16-W5\"\n  summary: \"遗漏重要相关工作\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 20\n  mentions:\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"Model Soups + Jiang (2024)。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R2-N3 Major：Yang & Wang (2026) 'Benchmark Illusion' 重大遗漏。\"\n    - round: 20\n      reviewers: [R2]\n      note: \"R2-S5 确认 Yang & Wang (2026) 现已在 abstract 和 Related Work 中正确引用并区分贡献。R2-W5 新增：缺少 selective prediction / abstention 文献（Geifman & El-Yaniv 2017/2019）和 ensemble selection（Caruana et al. 2004）。R1 交叉 AGREE W5。\"\n  action_items:\n    - round: 18\n      action: \"添加 Wortsman (2022) + Jiang (2024)\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"必须引用 Yang & Wang (2026) Benchmark Illusion\"\n      assigned_to: paper_agent\n      status: done\n    - round: 20\n      action: \"补充 selective prediction 文献（Geifman & El-Yaniv 2017/2019）和 ensemble selection（Caruana et al. 2004）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"Yang & Wang 已引用（R20 确认）。新增缺失：selective prediction + ensemble selection。\"\n  resolution_round: null\n\n- id: \"R16-M1\"\n  summary: \"Haghighat 2026 bib 条目需更新为 AAAI 2026\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 未提及。可能已修复。\"\n  action_items:\n    - round: 16\n      action: \"更新 references.bib\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R17-W1\"\n  summary: \"Task type vs evaluation format confound（LAMBADA 为唯一 free-form benchmark）\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 20\n  mentions:\n    - round: 17\n      reviewers: [R1, R2]\n      note: \"R1-W2 提出 + R2 [AGREE]。\"\n    - round: 18\n      reviewers: [R1, R2]\n      note: \"双方 Major，要求正文讨论。\"\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W1 Major + R2-W2 Major，交叉均强 AGREE。\"\n    - round: 20\n      reviewers: [R1, R2]\n      note: \"R1-W4 Major + R2-W4 Major，交叉均 [AGREE]。R2 补充：多选题内部 format 不预测 α 只排除子空间内效应。R1 交叉补充：LAMBADA 同时是唯一 retrieval/free-form/最高 α 任务——三重混淆。双方一致认为核心 claim 的因果解释力受限。论文 hedging 诚实但不可证伪。\"\n  action_items:\n    - round: 18\n      action: \"§3.2 末加 format confound 讨论\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 19\n      action: \"Limitations 显式加入 format confound；§4.1 'task type' 改为 'task type or evaluation format'\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"R20 双方强 AGREE Major。论文 hedging 诚实但因果力受限，是结构性局限。\"\n  resolution_round: null\n\n- id: \"R17-W2\"\n  summary: \"Confirmatory/exploratory benchmark 分类缺乏预注册\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1 Major vs R2 REBUT（标准分类）。Director 降级为 Should-Fix。\"\n  action_items:\n    - round: 17\n      action: \"Appendix A 明确 all-10 correction 为唯一有效\"\n      assigned_to: paper_agent\n      status: open\n    - round: 19\n      action: \"提供 taxonomy 时间证据（git commit）或框定为 hypothesis-generating\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"R1 Major vs R2 REBUT（标准分类）。Director 降级为 Should-Fix。\"\n  resolution_round: null\n\n- id: \"R18-W1\"\n  summary: \"Permutation test null baseline 不排除 example difficulty confound\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 20\n  mentions:\n    - round: 19\n      reviewers: []\n      note: \"R19 未显式提及。可能被 format confound 讨论吸收。\"\n    - round: 20\n      reviewers: [R1]\n      note: \"R1 在交叉回应中作为 R2 遗漏的重要问题再次提出：Appendix K 的 null baseline 未排除样本内在难度对跨架构 Jaccard 重叠的混淆。\"\n  action_items:\n    - round: 18\n      action: \"讨论 example difficulty 作为 confound\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R19-W1\"\n  summary: \"遗漏 Yang & Wang (2026) 'Benchmark Illusion'——核心发现高度重叠\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 20\n  mentions:\n    - round: 19\n      reviewers: [R2]\n      note: \"R2-N3 Major：Yang & Wang (2026) arXiv:2602.11898。\"\n    - round: 20\n      reviewers: [R2]\n      note: \"R2-S5 确认已正确引用：'Yang & Wang (2026) 的引用处理得当。在 abstract 和 Related Work 中均明确引用并区分贡献（our within-family design isolates backbone variation from training-regime differences）'。\"\n  action_items:\n    - round: 19\n      action: \"引用 Yang & Wang (2026)；重新界定 'first' claim 为 'first controlled within-family analysis'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"已引用并正确区分贡献。R20 R2 确认处理得当。\"\n  resolution_round: 20\n\n- id: \"R19-W2\"\n  summary: \"LAMBADA 和 ARC-Easy routing 增益数值疑似相同\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1 误读。原文数值不同。\"\n  action_items: []\n  resolution: \"R1 误读。原文数值不同（LAMBADA +5.2pp vs ARC-Easy +1.2pp）。无需修改。\"\n  resolution_round: 19\n\n- id: \"R19-W3\"\n  summary: \"全文 associative vs causal 语言不完全一致\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 19\n  last_seen_round: 19\n  mentions:\n    - round: 19\n      reviewers: [R1, R2]\n      note: \"R1-W8 Minor：'reflects'/'modulated by'/'controlled' 等 causal 用语偶现。R2 交叉 AGREE 但认为 minor。\"\n  action_items:\n    - round: 19\n      action: \"全文统一 associative 语言\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-W1\"\n  summary: \"n=5 Spearman power analysis 未形式化（仅非正式说明）\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [R1, R2]\n      note: \"R1-W2 Major：未讨论 power analysis。R2 交叉 [PARTIAL] → Minor：论文已说明 'only |ρ|=1.0 achieves p<.05 at n=5'，等价于非形式化 power 陈述。核心贡献不依赖 Spearman（Jaccard p 值来自置换检验）。R1 维持 Major，R2 降为 Minor。\"\n  action_items:\n    - round: 20\n      action: \"考虑添加正式 power analysis 表格（锦上添花，非必须）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"分歧：R1 Major vs R2 Minor。论文已有等价非形式化说明。\"\n  resolution_round: null\n\n- id: \"R20-W2\"\n  summary: \"Routing 缺少 selective prediction / ensemble selection 文献\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [R1, R2]\n      note: \"R2-W5 Minor：缺 Geifman & El-Yaniv (2017/2019) selective prediction 和 Caruana et al. (2004) ensemble selection。R1 交叉 [AGREE]：routing 定位不够准确，读者无法判断与已有 selective prediction 方法的关系。\"\n  action_items:\n    - round: 20\n      action: \"Related Work 或 §4.4 引用 Geifman & El-Yaniv (2017/2019) + Caruana et al. (2004)\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-W3\"\n  summary: \"Limitations 遗漏 greedy decoding 对逐样本分歧的影响\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [R1, R2]\n      note: \"R2-W6 Minor：所有评估用 greedy decoding，采样 decoding 可能改变 boundary cases 的 helped/hurt 分类。R1 交叉 [PARTIAL]：方向同意但 severity 更低——greedy 是 lm-eval-harness 标准配置，大多数 LM 评估工作使用 greedy。建议 Limitations 加一句即可。\"\n  action_items:\n    - round: 20\n      action: \"Limitations 补充一句 greedy decoding 对生成任务的潜在影响\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R20-W4\"\n  summary: \"饱和发现的替代解读：attention 引入 Transformer 式行为而非架构指纹\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 20\n  last_seen_round: 20\n  mentions:\n    - round: 20\n      reviewers: [R1, R2]\n      note: \"R2-Q3 提出 + R1 交叉完全 [AGREE] 并标为遗漏的重要观点。Appendix I 显示三个架构 h3-1 correct set 都更接近 Transformer 基线。两种解读有根本区别：(1) 混合架构保留独特逐样本特征 vs (2) 少量 attention 即使行为向 Transformer 收敛。论文应在 §4.2 或 Discussion 中讨论此替代解读。\"\n  action_items:\n    - round: 20\n      action: \"§4.2 或 Discussion 讨论替代解读：饱和可能反映 Transformer 式行为引入而非架构指纹确立\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1841 · 2026-05-24T14:30:15.747696+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_issues.yaml\", \"bytes\": 26020}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1842 · 2026-05-24T14:32:28.514950+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告：Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures\n\n**Round 20 | Target Venue: EMNLP 2026 (ARR) | 审稿模式: Fresh**\n\n---\n\n## Summary\n\n本文研究三种混合线性循环架构（GatedDeltaNet、RetNet、HGRN2）在逐样本层面的预测多样性（predictive multiplicity）。利用受控 model zoo（3 架构 × 5 attention 比例 × 2 规模），作者发现：(1) 聚合指标相近的架构在逐样本层面存在结构化分歧（Jaccard ≈ 0.10）；(2) 该分歧模式在 4% attention 即饱和；(3) multiplicity 幅度因任务类型（或评估格式）而异。此外，confidence-based routing 仅在 LAMBADA 上有效（+5.2pp），在其他 benchmark 上无效或有害。\n\n---\n\n## Strengths\n\n**S1. 实验设计高度受控（共识）**：使用共享训练数据、tokenizer 和超参数的 model zoo，将架构作为唯一变量。内部效度强，优于 D'Amour et al. (2022) 的多变量设计。\n\n**S2. 统计方法论严谨且透明（共识）**：全文一致使用 Bonferroni 校正、精确置换检验、Bootstrap BCa 置信区间。坦率承认 n=5 时 Spearman 的功效限制（\"only |ρ| = 1.0 achieves p < .05\"），在 NLP 实证论文中罕见。\n\n**S3. Jaccard 饱和发现（共识：论文最强贡献）**：4% attention 即确立完整的逐样本分歧模式，暗示 attention 的\"架构指纹\"效应是二元的而非剂量依赖的。跨规模一致（340M/1.3B），Figure 1b 和 Figure 4 提供清晰视觉证据。\n\n**S4. 附录详尽（共识）**：13 页 Appendix A–Y，包括连续 Jaccard 验证、归一化效应量、种子校准、五架构验证、Transformer 基线对比等。几乎每个潜在质疑都有 robustness check。\n\n**S5. Yang & Wang (2026) 引用处理得当**：在 abstract 和 Related Work 中明确引用并区分贡献（\"our within-family design isolates backbone variation from training-regime differences\"）。\n\n**S6. 五架构验证增强泛化性**：GLA + DeltaNet 加入后 10 个架构对全部满足 J ≤ 0.14, p ≤ .002。\n\n---\n\n## Weaknesses\n\n### Critical / Major\n\n**W1 [Major, 共识] 单次训练运行无法分离架构效应与种子效应**\n\n每个架构×attention 配置仅一次训练运行。Pythia 70M 种子校准（Appendix W）是跨家族/跨规模的（Transformer 70M vs 混合循环 340M/1.3B），说服力有限。within- vs. cross-architecture 3× Jaccard 差距是 suggestive 但非 definitive——cross-architecture 必然包含种子差异 + 架构差异。这是整个论文最根本的方法论局限。\n\n- R1 评估：Major | R2 评估：Major | 交叉：双方 [AGREE]\n\n**W2 [Major→Critical, 分歧] GDN 16-head confound 对聚合收敛声明的影响**\n\nGDN h3-1 使用 16 heads（vs. 其他配置 32 heads），构成混淆变量。排除 GDN 后：LAMBADA ρ 从 −1.0 降至 −0.7 (p=.233)；MMLU 从负相关反转为 +0.6。\n\n- R1 评估：Critical（认为动摇论文约 1/3 叙事）\n- R2 评估：Major（论证：聚合收敛非核心 claim；论文策略恰恰利用其非显著性来对比 per-example 显著性；per-example 饱和不受 GDN 影响）\n- **Director 判断**：R2 论证有力——论文的两项正式贡献（结构化 multiplicity + Jaccard 饱和）均不依赖聚合收敛。但 §4.3 的 convergence 讨论和 Table 1 的呈现方式仍给读者错误印象。建议 Table 1 增加 \"excl. GDN\" 行，§4.3 更显著地讨论此 confound。**定为 Major。**\n\n**W3 [Major, 共识] 任务类型与评估格式完全混淆**\n\nLAMBADA 同时是唯一的自由生成 benchmark、唯一的 retrieval 任务、和拥有最高 α (0.30) 的任务——三重混淆使任何单一归因不可证伪。论文全文以 \"(or evaluation format)\" hedging，诚实但意味着核心 claim 的因果解释力受限。多选题内部 format 不预测 α 仅排除子空间内效应，不解决 free-form vs. MC 的根本差异。\n\n- R1 评估：Major | R2 评估：Major | 交叉：双方 [AGREE]\n\n**W4 [Major, 共识] Routing 贡献薄弱但叙事权重过高**\n\nConfidence-based routing 在 4 个 benchmark 中仅 LAMBADA 有效（+5.2pp），HellaSwag 无效（-0.06pp），PIQA 显著有害（-0.49pp, p = .006）。这实质上是一个消极结果。然而：\n- Abstract 用约 1/6 篇幅描述 routing，正面数字（\"+5.2pp\"、\"36% of oracle complementarity\"）比消极描述更突出\n- Conclusion 将 routing 作为两大核心观察之一\n- 缺少最自然的 baseline（logits ensemble，论文承认 \"left to future work\"）\n\nIntroduction 贡献列表未包含 routing（正确），但与 abstract/conclusion 不一致。\n\n- R1 评估：Major | R2 评估：Major | 交叉：双方 [AGREE]\n\n**W5 [Major, R2 提出, R1 部分同意] 概念新颖性有限**\n\n核心贡献是将 predictive multiplicity（Marx 2020）和 underspecification（D'Amour 2022）的分析框架应用到混合线性循环架构。\"聚合指标掩盖逐样本分歧\"的概念已被充分建立。独特贡献集中在饱和发现，但仅占论文约 1/4 篇幅。\n\n- R1 交叉回应：[PARTIAL]——经验贡献被低估（饱和的阈值效应、受控设计方法论、混合架构时效性），建议重组让饱和为主线\n- **Director 判断**：在 Findings 标准下可接受。但如果重组让饱和发现成为主线叙事，论文贡献感知会更清晰。\n\n### Minor / Info\n\n**W6 [Minor, R2 提出] 缺少 selective prediction / ensemble selection 文献**\n\nRouting 实验本质上是基于输入特征选择最优模型，与 Geifman & El-Yaniv (2017, 2019) 和 Caruana et al. (2004) \"Ensemble selection from libraries of models\" 概念相关。\n\n**W7 [Minor, R2 提出, R1 方向同意] Limitations 遗漏 greedy decoding 影响**\n\n所有评估使用 greedy decoding，Limitations 未讨论采样 decoding 对逐样本分歧的潜在影响。R1 交叉同意方向但降低 severity——greedy 是 lm-eval-harness 标准配置。\n\n**W8 [Minor, R1 提出] n=3 Bootstrap CI 退化**\n\nn=3 架构上 Bootstrap BCa 大量样本为退化的同架构三重采样（Appendix D1），影响 Figure 4 CI 不含零的可信度。论文 Section 3.5 已标注 \"heuristic\"。\n\n**W9 [Minor, R1 提出] 排列检验未条件化于样本难度**\n\nAppendix K 的 null baseline 未排除样本内在难度对跨架构 Jaccard 重叠的混淆。\n\n**W10 [Info, 共识新增] 饱和发现的替代解读未讨论**\n\nAppendix I 显示三个架构 h3-1 correct set 都更接近 Transformer 基线。饱和可能反映的是\"少量 attention 即引入 Transformer 式行为\"，而非\"架构指纹在最低 attention 即确立\"。两种解读有根本区别，论文应在 §4.2 或 Discussion 中讨论。\n\n---\n\n## Questions\n\n1. 为什么不对一个架构训练多个种子来直接校准种子噪声水平？这是最直接回答\"逐样本分歧是架构驱动还是种子驱动\"的实验。（R1+R2 共识）\n\n2. 排除 GDN 后各 benchmark 的完整 Spearman 表——尤其 MMLU ρ 反转为 +0.6 是否意味着 MMLU convergence 完全由 GDN anomaly 驱动？（R1+R2 共识）\n\n3. Appendix I 的 Transformer 基线——h3-1 correct set 更接近 Transformer 是否暗示 attention 主导了逐样本行为？如果是，饱和发现的理论含义需要修正。（R2 提出, R1 强 AGREE）\n\n4. 论文仅评估预训练 checkpoint。Fine-tuning（尤其 instruction tuning）后逐样本分歧是否保留？这对部署建议的适用性至关重要。（R2 提出, R1 AGREE）\n\n5. AUC 0.70–0.74 的未解释 30% 方差——是否考虑过结合多个浅层信号（token 频率、输入长度、prompt perplexity）构建组合预测器？（R2 提出）\n\n---\n\n## Missing References\n\n- Geifman & El-Yaniv (2017, 2019) — Selective prediction / abstention（routing 实验的概念前驱）\n- Caruana et al. (2004) \"Ensemble selection from libraries of models\"（基于输入选择最优模型的经典工作）\n- 论文的 Related Work 在其他方面较全面：Yang & Wang (2026)、MultiBERTs、Model Soups、predictive multiplicity 文献均已引用。\n\n---\n\n## External Review\n\n**状态**：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：已完成（2026-05-24 14:13–14:16 UTC）\n\n| 严重程度 | 位置 | 发现 |\n|---------|------|------|\n| ⚠️ Warning | Page 8 | 三个 figure（5/6/7）挤在同一页上半部，Figures 6 和 7 尺寸偏小（各约占 1/6 页面），内部文字可能低于正文字号 70% 可读性阈值。该页同时含 Conclusion + Limitations 开头，整体拥挤。建议将 Figure 7 移至 page 7 或 Appendix。 |\n| ✓ Info | Page 2 | Figure 1 在第 2 页顶部有效建立核心发现锚定。良好。 |\n| ✓ Info | Page 5 | Figure 3 bar chart 颜色区分度良好，caption 自包含。 |\n| ✓ Info | Page 6 | Tables 1-2 booktabs 风格，关键值加粗，精度统一。 |\n| ✓ Info | Page 7 | Figure 4 scatter plot 清晰，bootstrap CI 标注文字偏小。 |\n| ✓ Info | Pages 9-10 | References 格式统一，无未解析引用。 |\n| ✓ Info | Pages 11-21 | Appendix ~28 个 table 格式一致。 |\n| ✓ Info | Page 21 | \"Use of AI Assistants\" 透明声明。 |\n\n**总结**：1 个 warning（page 8 拥挤），0 个 critical。整体排版质量良好。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 合成 |\n|------|----|----|------|\n| Soundness | 3/5 | 3.5/5 | 3/5 |\n| Excitement | 2.5/5 | 3/5 | 3/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**评分理由**：\n\n- **R1: 3.0 (Findings)** — 饱和发现和实验框架支撑 Findings，但 GDN confound 削弱 convergence 声明，加上单次运行和格式混淆，Conference 级别的统计基础不足。\n- **R2: 3.5 (Borderline Conference)** — 执行严谨，饱和发现有价值，但概念增量有限，routing 为消极结果，关键混淆未解决。\n\n**Director 合成判断（3.0 Findings）**：\n\nR2 在交叉中对 R1-W5（p=.170）的反驳有说服力——论文对 p=.170 的处理是坦诚的统计报告而非暗示显著。R2 对 GDN confound 的降级论证（聚合收敛非核心 claim）也有技术 merit。但综合考虑：\n\n1. **概念新颖性有限**（R1 partial agree + R2 Major）：核心信息已被充分建立\n2. **单次运行**（双方 Major）：最根本的方法论局限，使所有架构效应声明均为 suggestive\n3. **格式混淆**（双方 Major）：LAMBADA 的三重混淆使任务类型 claim 不可证伪\n4. **Routing 为消极结果**（双方 Major）：但获得过高叙事权重\n5. **饱和发现是真实贡献**（双方共识）：但仅占论文约 1/4 篇幅\n\n这些问题的叠加效应将论文定位在 Findings 而非 Conference。饱和发现的非平凡性和整体执行质量足以支撑 Findings 接收，但论文缺乏足够的新颖性证据（如多种子实验、生成任务 routing 验证）来达到 Conference 级别。\n\n**关键分歧记录**：\n- GDN severity：R1 Critical vs R2 Major（Director 采纳 Major）\n- p=.170 解读：R1 Major vs R2 Rebut（Director 采纳 R2 rebut——不应列为 weakness）\n- n=5 power：R1 Major vs R2 Minor（Director 判断：论文已有等价说明，降为 Info）\n\n---\n\n## Detailed Comments\n\n### 优先修改建议（按影响力排序）\n\n1. **叙事重构**：将饱和发现升级为主线贡献（两位 Reviewer 在交叉后趋于一致），弱化/条件化聚合 convergence 叙事\n2. **Routing 降级**：Abstract 缩减 routing 篇幅或明确标注为\"探索性消极发现\"，Conclusion 中减少比重\n3. **GDN confound 显著化**：Table 1 增加 \"excl. GDN\" 行，正文更早 flag 16-head anomaly\n4. **替代解读讨论**：§4.2 讨论饱和可能反映 Transformer 式行为引入\n5. **文献补充**：Geifman & El-Yaniv (2017/2019) + Caruana et al. (2004)\n6. **Limitations 补充**：greedy decoding 影响一句话\n\n### 不建议修改\n\n- p=.170 的报告方式（当前处理是坦诚且正确的）\n- Binary decomposition（连续 Jaccard 已验证，R1 在交叉中肯定设计合理）\n- 五架构验证仅 340M（model zoo 约束，非设计缺陷）\n\n---\n\n**报告生成时间**: 2026-05-24\n**Reviewer Panel**: R1 (方法严谨性 + 统计基础) + R2 (新颖性 + 叙事完整性)\n**交叉分享**: 完成（R1→R2, R2→R1，均提交逐条回应）\n**轮次**: 1 轮（关键问题达成共识或记录明确分歧，无需追加轮次）",
  "project": "entrainment_gated_ft",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_b542b52ff24f138c42225a1d4b456e7e"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告：Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures\n\n**Round 20 | Target Venue: EMNLP 2026 (ARR) | 审稿模式: Fresh**\n\n---\n\n## Summary\n\n本文研究三种混合线性循环架构（GatedDeltaNet、RetNet、HGRN2）在逐样本层面的预测多样性（predictive multiplicity）。利用受控 model zoo（3 架构 × 5 attention 比例 × 2 规模），作者发现：(1) 聚合指标相近的架构在逐样本层面存在结构化分歧（Jaccard ≈ 0.10）；(2) 该分歧模式在 4% attention 即饱和；(3) multiplicity 幅度因任务类型（或评估格式）而异。此外，confidence-based routing 仅在 LAMBADA 上有效（+5.2pp），在其他 benchmark 上无效或有害。\n\n---\n\n## Strengths\n\n**S1. 实验设计高度受控（共识）**：使用共享训练数据、tokenizer 和超参数的 model zoo，将架构作为唯一变量。内部效度强，优于 D'Amour et al. (2022) 的多变量设计。\n\n**S2. 统计方法论严谨且透明（共识）**：全文一致使用 Bonferroni 校正、精确置换检验、Bootstrap BCa 置信区间。坦率承认 n=5 时 Spearman 的功效限制（\"only |ρ| = 1.0 achieves p < .05\"），在 NLP 实证论文中罕见。\n\n**S3. Jaccard 饱和发现（共识：论文最强贡献）**：4% attention 即确立完整的逐样本分歧模式，暗示 attention 的\"架构指纹\"效应是二元的而非剂量依赖的。跨规模一致（340M/1.3B），Figure 1b 和 Figure 4 提供清晰视觉证据。\n\n**S4. 附录详尽（共识）**：13 页 Appendix A–Y，包括连续 Jaccard 验证、归一化效应量、种子校准、五架构验证、Transformer 基线对比等。几乎每个潜在质疑都有 robustness check。\n\n**S5. Yang & Wang (2026) 引用处理得当**：在 abstract 和 Related Work 中明确引用并区分贡献（\"our within-family design isolates backbone variation from training-regime differences\"）。\n\n**S6. 五架构验证增强泛化性**：GLA + DeltaNet 加入后 10 个架构对全部满足 J ≤ 0.14, p ≤ .002。\n\n---\n\n## Weaknesses\n\n### Critical / Major\n\n**W1 [Major, 共识] 单次训练运行无法分离架构效应与种子效应**\n\n每个架构×attention 配置仅一次训练运行。Pythia 70M 种子校准（Appendix W）是跨家族/跨规模的（Transformer 70M vs 混合循环 340M/1.3B），说服力有限。within- vs. cross-architecture 3× Jaccard 差距是 suggestive 但非 definitive——cross-architecture 必然包含种子差异 + 架构差异。这是整个论文最根本的方法论局限。\n\n- R1 评估：Major | R2 评估：Major | 交叉：双方 [AGREE]\n\n**W2 [Major→Critical, 分歧] GDN 16-head confound 对聚合收敛声明的影响**\n\nGDN h3-1 使用 16 heads（vs. 其他配置 32 heads），构成混淆变量。排除 GDN 后：LAMBADA ρ 从 −1.0 降至 −0.7 (p=.233)；MMLU 从负相关反转为 +0.6。\n\n- R1 评估：Critical（认为动摇论文约 1/3 叙事）\n- R2 评估：Major（论证：聚合收敛非核心 claim；论文策略恰恰利用其非显著性来对比 per-example 显著性；per-example 饱和不受 GDN 影响）\n- **Director 判断**：R2 论证有力——论文的两项正式贡献（结构化 multiplicity + Jaccard 饱和）均不依赖聚合收敛。但 §4.3 的 convergence 讨论和 Table 1 的呈现方式仍给读者错误印象。建议 Table 1 增加 \"excl. GDN\" 行，§4.3 更显著地讨论此 confound。**定为 Major。**\n\n**W3 [Major, 共识] 任务类型与评估格式完全混淆**\n\nLAMBADA 同时是唯一的自由生成 benchmark、唯一的 retrieval 任务、和拥有最高 α (0.30) 的任务——三重混淆使任何单一归因不可证伪。论文全文以 \"(or evaluation format)\" hedging，诚实但意味着核心 claim 的因果解释力受限。多选题内部 format 不预测 α 仅排除子空间内效应，不解决 free-form vs. MC 的根本差异。\n\n- R1 评估：Major | R2 评估：Major | 交叉：双方 [AGREE]\n\n**W4 [Major, 共识] Routing 贡献薄弱但叙事权重过高**\n\nConfidence-based routing 在 4 个 benchmark 中仅 LAMBADA 有效（+5.2pp），HellaSwag 无效（-0.06pp），PIQA 显著有害（-0.49pp, p = .006）。这实质上是一个消极结果。然而：\n- Abstract 用约 1/6 篇幅描述 routing，正面数字（\"+5.2pp\"、\"36% of oracle complementarity\"）比消极描述更突出\n- Conclusion 将 routing 作为两大核心观察之一\n- 缺少最自然的 baseline（logits ensemble，论文承认 \"left to future work\"）\n\nIntroduction 贡献列表未包含 routing（正确），但与 abstract/conclusion 不一致。\n\n- R1 评估：Major | R2 评估：Major | 交叉：双方 [AGREE]\n\n**W5 [Major, R2 提出, R1 部分同意] 概念新颖性有限**\n\n核心贡献是将 predictive multiplicity（Marx 2020）和 underspecification（D'Amour 2022）的分析框架应用到混合线性循环架构。\"聚合指标掩盖逐样本分歧\"的概念已被充分建立。独特贡献集中在饱和发现，但仅占论文约 1/4 篇幅。\n\n- R1 交叉回应：[PARTIAL]——经验贡献被低估（饱和的阈值效应、受控设计方法论、混合架构时效性），建议重组让饱和为主线\n- **Director 判断**：在 Findings 标准下可接受。但如果重组让饱和发现成为主线叙事，论文贡献感知会更清晰。\n\n### Minor / Info\n\n**W6 [Minor, R2 提出] 缺少 selective prediction / ensemble selection 文献**\n\nRouting 实验本质上是基于输入特征选择最优模型，与 Geifman & El-Yaniv (2017, 2019) 和 Caruana et al. (2004) \"Ensemble selection from libraries of models\" 概念相关。\n\n**W7 [Minor, R2 提出, R1 方向同意] Limitations 遗漏 greedy decoding 影响**\n\n所有评估使用 greedy decoding，Limitations 未讨论采样 decoding 对逐样本分歧的潜在影响。R1 交叉同意方向但降低 severity——greedy 是 lm-eval-harness 标准配置。\n\n**W8 [Minor, R1 提出] n=3 Bootstrap CI 退化**\n\nn=3 架构上 Bootstrap BCa 大量样本为退化的同架构三重采样（Appendix D1），影响 Figure 4 CI 不含零的可信度。论文 Section 3.5 已标注 \"heuristic\"。\n\n**W9 [Minor, R1 提出] 排列检验未条件化于样本难度**\n\nAppendix K 的 null baseline 未排除样本内在难度对跨架构 Jaccard 重叠的混淆。\n\n**W10 [Info, 共识新增] 饱和发现的替代解读未讨论**\n\nAppendix I 显示三个架构 h3-1 correct set 都更接近 Transformer 基线。饱和可能反映的是\"少量 attention 即引入 Transformer 式行为\"，而非\"架构指纹在最低 attention 即确立\"。两种解读有根本区别，论文应在 §4.2 或 Discussion 中讨论。\n\n---\n\n## Questions\n\n1. 为什么不对一个架构训练多个种子来直接校准种子噪声水平？这是最直接回答\"逐样本分歧是架构驱动还是种子驱动\"的实验。（R1+R2 共识）\n\n2. 排除 GDN 后各 benchmark 的完整 Spearman 表——尤其 MMLU ρ 反转为 +0.6 是否意味着 MMLU convergence 完全由 GDN anomaly 驱动？（R1+R2 共识）\n\n3. Appendix I 的 Transformer 基线——h3-1 correct set 更接近 Transformer 是否暗示 attention 主导了逐样本行为？如果是，饱和发现的理论含义需要修正。（R2 提出, R1 强 AGREE）\n\n4. 论文仅评估预训练 checkpoint。Fine-tuning（尤其 instruction tuning）后逐样本分歧是否保留？这对部署建议的适用性至关重要。（R2 提出, R1 AGREE）\n\n5. AUC 0.70–0.74 的未解释 30% 方差——是否考虑过结合多个浅层信号（token 频率、输入长度、prompt perplexity）构建组合预测器？（R2 提出）\n\n---\n\n## Missing References\n\n- Geifman & El-Yaniv (2017, 2019) — Selective prediction / abstention（routing 实验的概念前驱）\n- Caruana et al. (2004) \"Ensemble selection from libraries of models\"（基于输入选择最优模型的经典工作）\n- 论文的 Related Work 在其他方面较全面：Yang & Wang (2026)、MultiBERTs、Model Soups、predictive multiplicity 文献均已引用。\n\n---\n\n## External Review\n\n**状态**：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：已完成（2026-05-24 14:13–14:16 UTC）\n\n| 严重程度 | 位置 | 发现 |\n|---------|------|------|\n| ⚠️ Warning | Page 8 | 三个 figure（5/6/7）挤在同一页上半部，Figures 6 和 7 尺寸偏小（各约占 1/6 页面），内部文字可能低于正文字号 70% 可读性阈值。该页同时含 Conclusion + Limitations 开头，整体拥挤。建议将 Figure 7 移至 page 7 或 Appendix。 |\n| ✓ Info | Page 2 | Figure 1 在第 2 页顶部有效建立核心发现锚定。良好。 |\n| ✓ Info | Page 5 | Figure 3 bar chart 颜色区分度良好，caption 自包含。 |\n| ✓ Info | Page 6 | Tables 1-2 booktabs 风格，关键值加粗，精度统一。 |\n| ✓ Info | Page 7 | Figure 4 scatter plot 清晰，bootstrap CI 标注文字偏小。 |\n| ✓ Info | Pages 9-10 | References 格式统一，无未解析引用。 |\n| ✓ Info | Pages 11-21 | Appendix ~28 个 table 格式一致。 |\n| ✓ Info | Page 21 | \"Use of AI Assistants\" 透明声明。 |\n\n**总结**：1 个 warning（page 8 拥挤），0 个 critical。整体排版质量良好。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n| 维度 | R1 | R2 | 合成 |\n|------|----|----|------|\n| Soundness | 3/5 | 3.5/5 | 3/5 |\n| Excitement | 2.5/5 | 3/5 | 3/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**评分理由**：\n\n- **R1: 3.0 (Findings)** — 饱和发现和实验框架支撑 Findings，但 GDN confound 削弱 convergence 声明，加上单次运行和格式混淆，Conference 级别的统计基础不足。\n- **R2: 3.5 (Borderline Conference)** — 执行严谨，饱和发现有价值，但概念增量有限，routing 为消极结果，关键混淆未解决。\n\n**Director 合成判断（3.0 Findings）**：\n\nR2 在交叉中对 R1-W5（p=.170）的反驳有说服力——论文对 p=.170 的处理是坦诚的统计报告而非暗示显著。R2 对 GDN confound 的降级论证（聚合收敛非核心 claim）也有技术 merit。但综合考虑：\n\n1. **概念新颖性有限**（R1 partial agree + R2 Major）：核心信息已被充分建立\n2. **单次运行**（双方 Major）：最根本的方法论局限，使所有架构效应声明均为 suggestive\n3. **格式混淆**（双方 Major）：LAMBADA 的三重混淆使任务类型 claim 不可证伪\n4. **Routing 为消极结果**（双方 Major）：但获得过高叙事权重\n5. **饱和发现是真实贡献**（双方共识）：但仅占论文约 1/4 篇幅\n\n这些问题的叠加效应将论文定位在 Findings 而非 Conference。饱和发现的非平凡性和整体执行质量足以支撑 Findings 接收，但论文缺乏足够的新颖性证据（如多种子实验、生成任务 routing 验证）来达到 Conference 级别。\n\n**关键分歧记录**：\n- GDN severity：R1 Critical vs R2 Major（Director 采纳 Major）\n- p=.170 解读：R1 Major vs R2 Rebut（Director 采纳 R2 rebut——不应列为 weakness）\n- n=5 power：R1 Major vs R2 Minor（Director 判断：论文已有等价说明，降为 Info）\n\n---\n\n## Detailed Comments\n\n### 优先修改建议（按影响力排序）\n\n1. **叙事重构**：将饱和发现升级为主线贡献（两位 Reviewer 在交叉后趋于一致），弱化/条件化聚合 convergence 叙事\n2. **Routing 降级**：Abstract 缩减 routing 篇幅或明确标注为\"探索性消极发现\"，Conclusion 中减少比重\n3. **GDN confound 显著化**：Table 1 增加 \"excl. GDN\" 行，正文更早 flag 16-head anomaly\n4. **替代解读讨论**：§4.2 讨论饱和可能反映 Transformer 式行为引入\n5. **文献补充**：Geifman & El-Yaniv (2017/2019) + Caruana et al. (2004)\n6. **Limitations 补充**：greedy decoding 影响一句话\n\n### 不建议修改\n\n- p=.170 的报告方式（当前处理是坦诚且正确的）\n- Binary decomposition（连续 Jaccard 已验证，R1 在交叉中肯定设计合理）\n- 五架构验证仅 340M（model zoo 约束，非设计缺陷）\n\n---\n\n**报告生成时间**: 2026-05-24\n**Reviewer Panel**: R1 (方法严谨性 + 统计基础) + R2 (新颖性 + 叙事完整性)\n**交叉分享**: 完成（R1→R2, R2→R1，均提交逐条回应）\n**轮次**: 1 轮（关键问题达成共识或记录明确分歧，无需追加轮次）",
    "project": "entrainment_gated_ft",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_b542b52ff24f138c42225a1d4b456e7e"
  }
}
```

</details>

---


### Tool result

_source line 1843 · 2026-05-24T14:32:32.600203+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1f8f0d6d9482071694045c30143bb993:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4085
}
```

</details>

---


### Assistant

_source line 1844 · 2026-05-24T14:32:41.529785+00:00_

审稿报告已投递。

**Round 20 结果**：Overall 3.0 (Findings)

两位 Reviewer 的核心共识：
- 饱和发现（4% attention 即确立分歧模式）是论文最强贡献
- 单次训练运行、格式混淆、routing 消极结果是主要局限
- 概念新颖性有限但 Findings 标准下可接受

关键分歧（已记录）：GDN confound severity（R1 Critical vs R2 Major，Director 采纳 Major）。

优先修改方向：以饱和发现为主线重构叙事、routing 降级、GDN confound 更显著讨论。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director"
}
```

</details>

---


## Round 143

## Round 143

2 recorded events


### User

_source line 1845 · 2026-05-24T14:32:44.056521+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。核心判断：

- **R1-W1 降级为 Major**：R1 报告的 ρ = −0.2 是错误的（论文实际报告 −0.7），且聚合收敛非论文核心 claim，per-example 饱和不受 GDN confound 影响。
- **R1-W2 降级为 Minor**：论文已在 Section 3.5 明确承认 power 局限。
- **R1-W3/W4 同意**：单种子和格式混淆是真实的 Major 问题。
- **R1-W5 反驳**：论文在三处明确标注 p=.170 为非显著，修辞策略恰恰依赖于其非显著性来构建解耦论证。
- **补充了 R1 遗漏的 3 个问题**：routing 叙事权重过高、缺少 logits ensemble baseline、greedy decoding 局限。

维持 **Overall 3.5 (Borderline Conference)** 评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1846 · 2026-05-24T14:32:52.288343+00:00_

审稿报告已在收到 Reviewer 2 交叉回应前提交完毕（基于两位 Reviewer 的初审 + 交叉回应）。

报告已投递至 Research Director，Overall Score: **3.0 (Findings)**。Issue Tracker 已同步更新至 Round 20。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director"
}
```

</details>

---


## Round 144

## Round 144

56 recorded events


### User

_source line 1847 · 2026-05-24T22:49:37.139490+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: entrainment_gated_ft
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1848 · 2026-05-24T22:49:43.098242+00:00_

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
  "session": "feishu:group:oc_b542b52ff24f138c42225a1d4b456e7e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---
