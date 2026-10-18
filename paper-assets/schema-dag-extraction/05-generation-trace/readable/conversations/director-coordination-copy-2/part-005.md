# Director coordination — Part 5 of 10

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

[← Part 4](part-004.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 6 →](part-006.md) · [Structured JSON](../../../sessions/0f/0fa49ecfe50583d66f9a.json)

## Round 122

### Tool result

_source line 1265 · 2026-05-18T03:08:48.059749+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1266 · 2026-05-18T03:12:18.094471+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "schema-dag-extraction",
  "issues_yaml": "# Round 13 Review Issues Tracker\n# Updated: 2026-05-18 (Round 13 review completed)\n\n# ============================================================\n# CRITICAL — Must-Fix\n# ============================================================\n\n- id: R3-C2\n  summary: \"'Empirically separable channels' 缺乏 formal 统计支撑 — TOST margin ±3pp > typical effect 2.2pp\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 9\n  mentions:\n    - {round: 3, reviewers: [R1, R2], note: \"因果语言过强\"}\n    - {round: 4, reviewers: [R1, R2], note: \"Title 'Drive' + §4.3 暗示因果\"}\n    - {round: 5, reviewers: [R1, R2, R3], note: \"三人共识改措辞\"}\n    - {round: 6, reviewers: [R1, R2, R3], note: \"factorial p=0.50; 建议 'mechanistically distinguishable'\"}\n    - {round: 7, reviewers: [R1, R2], note: \"三项 factorial 检验中两项失败\"}\n    - {round: 8, reviewers: [R1, R2], note: \"R1-N1 critical: 3/4 tests 失败; 共识: 需限定\"}\n    - {round: 9, reviewers: [R1, R2, R3], note: \"三人共识: TOST ±3pp margin 用 prompt variation 锚定不合逻辑; margin > typical main effect; ±1pp inconclusive\"}\n  action_items:\n    - {round: 9, action: \"D051: 'additive separability' → 'bounded interaction' 全文统一; SESOI effect-size anchored\", assigned_to: agent, status: done}\n  resolution: \"D051 W1: 全文 'bounded interaction' 统一; SESOI effect-size anchored; sensitivity table in Appendix\"\n  resolution_round: 9\n\n- id: R10-N1\n  summary: \"因果语言 ('driven', 'channels', 'shape') 超出 observational/quasi-experimental 证据边界\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - {round: 10, reviewers: [R1, R2], note: \"R1 critical N3 + R2 AGREE with qualification; 共识: Title 'shape' 暗示因果\"}\n    - {round: 11, reviewers: [R1, R2], note: \"R1 W4 + R2 AGREE: Title 'Shape' + Limitations 承认 no interventional causality = 不匹配\"}\n    - {round: 12, reviewers: [R2], note: \"MOSTLY FIXED: Title 改为 'Predict'; 正文主体无 'channels'/'driven'; 仅 Appendix N/P 残余 'count-driven'/'BCS-driven' — 降级为 R12-W2\"}\n  action_items:\n    - {round: 10, action: \"分层替换 (D052): correlational → 'predicts'/'associated with'\", assigned_to: agent, status: done}\n    - {round: 11, action: \"D054: Title 'Shape' → 'Predict'; 全文因果语言 grep 扫描清零\", assigned_to: agent, status: done}\n  resolution: \"Title 改为 'Predict'; 正文因果语言已清理; Appendix 残余为 R12-W2 追踪\"\n  resolution_round: 12\n\n- id: R10-N2\n  summary: \"Pair-level→batch-level 聚合推理链叙事误导 — unconditional sim R²=0.044 vs 观测 0.218\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - {round: 10, reviewers: [R1, R2], note: \"R1 critical N1; R2 AGREE with nuance\"}\n    - {round: 11, reviewers: [R1, R2], note: \"叙事链暗示因果中介\"}\n    - {round: 12, reviewers: [R2], note: \"FIXED: Discussion §6 分层叙述 unconditional→conditional→batch; Appendix I 明确标注 'illustrative explanatory model'; 与直接实证 R²=0.218 明确区分\"}\n  action_items:\n    - {round: 10, action: \"§4.3: R²=0.218 direct OLS 作 primary claim; simulation 标注 post-hoc\", assigned_to: agent, status: done}\n    - {round: 11, action: \"D054: Discussion 区分 pair r²=1.3% vs batch R²=22%\", assigned_to: agent, status: done}\n  resolution: \"叙事链清晰分层; simulation 明确为 illustrative; R²=0.218 为独立实证\"\n  resolution_round: 12\n\n- id: R10-N3\n  summary: \"TOST ±3pp margin 的 external anchoring 不足 — 130% amplification threshold 为 arbitrary judgment call\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - {round: 10, reviewers: [R1, R2], note: \"R1 critical N2: margin循环, ±1pp inconclusive\"}\n    - {round: 11, reviewers: [R1, R2], note: \"±3pp = typical effect 136%; 共识: 以 ±2pp 为 primary\"}\n    - {round: 12, reviewers: [R1, R2], note: \"R2 确认 FIXED: Appendix D 三重 anchoring (empirical/practical/statistical) + sensitivity table; R1 经重审 Appendix C 后从 critical 下调为 should-fix; 但 logit-scale inconclusive (p=0.209) 仍需讨论 → R12-W3\"}\n  action_items:\n    - {round: 10, action: \"三条 anchor: empirical + practical + statistical\", assigned_to: agent, status: done}\n    - {round: 11, action: \"D054: sensitivity analysis in Appendix\", assigned_to: agent, status: done}\n  resolution: \"三重 anchoring + sensitivity table 已到位; logit-scale 不一致性追踪于 R12-W3\"\n  resolution_round: 12\n\n- id: R10-N4\n  summary: \"SCS/BCS Contribution #2 framing 暗示 metric novelty — 实际增量是 controlled validation\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: \"Contribution #2 已 reframe 为 controlled validation; §2 SCS novelty 段明确界定增量\"\n  resolution_round: 11\n\n- id: R11-N1\n  summary: \"NER Dimension 2 batch-level 证据方向相反（r=+0.50~+0.58），但论文 title/abstract 泛化为 cross-task\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Abstract/Intro/Contribution/Discussion 均已精确限定 batch-level Dim2 = RE-specific; pairwise cross-task 正确区分\"\n  resolution_round: 12\n\n- id: R11-N2\n  summary: \"核心效应量过小 (typical gap 2.2pp, pairwise r²=1.3%) — practical significance 存疑\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - {round: 11, reviewers: [R1, R2], note: \"2.2pp CI [0.4, 4.0] 在部署中几乎不可察觉; 需更强论证 practical significance\"}\n    - {round: 12, reviewers: [R1, R2], note: \"降级为 should-fix, 更多是 findings 本身的局限而非写作缺陷\"}\n    - {round: 13, reviewers: [R1, R2], note: \"R1-W2 + R2-N1 双方再次确认; R2 交叉 AGREE R1-W2; 共识: extreme-batch gap (25-31pp) 在叙事中占比过高, typical gap 2.2pp 应前置; Abstract 虽诚实但 Results/Introduction 节奏偏向极端值\"}\n  action_items:\n    - {round: 11, action: \"D054 Phase 3: Discussion reframe '2.2pp negligible IS the finding'\", assigned_to: agent, status: done}\n    - {round: 12, action: \"Discussion 补充: 在什么部署条件下 2.2pp 有实际价值; BCS screening vs few-shot augmentation 成本效益对比\", assigned_to: agent, status: in_progress}\n    - {round: 13, action: \"Introduction/Results 叙事调整: extreme-batch 数字仅作对比锚点, typical gap 前置; 补充 BCS threshold ROC/precision-recall analysis\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING — Should-Fix\n# ============================================================\n\n- id: R11-W1\n  summary: \"Discussion/Conclusion 过于简短 (~15 行) — 缺 actionable recommendations\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - {round: 11, reviewers: [R1, R2], note: \"analysis paper 需更充分的 Discussion\"}\n    - {round: 12, reviewers: [R1, R2], note: \"Discussion MOSTLY FIXED; Conclusion 仅 3 句, 无 future work\"}\n    - {round: 13, reviewers: [R1, R2], note: \"R2-W2 [major]: Conclusion ~120 words, 缺 future work/broader implications/training-based IE 对比; R1 交叉 AGREE 但认为 minor (篇幅限制下 Discussion 已充分); 共识: Conclusion 需扩展\"}\n  action_items:\n    - {round: 11, action: \"D054 Phase 3a: Discussion 扩展\", assigned_to: agent, status: done}\n    - {round: 12, action: \"Conclusion 扩展至 5-8 句\", assigned_to: agent, status: in_progress}\n    - {round: 13, action: \"Conclusion 扩展: (1) 核心发现 (2) training-based IE 对比 (3) future directions (4) broader implications\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W2\n  summary: \"TOST (Two One-Sided Tests) 术语首次出现未展开\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - {round: 11, reviewers: [R1, R2], note: \"NLP 社区对 TOST 不熟悉\"}\n    - {round: 12, reviewers: [R2], note: \"Introduction L15 首次使用 'TOST p=0.003' 未展开\"}\n    - {round: 13, reviewers: [], note: \"本轮未直接提及, 但 Introduction finding (1) 仍含未展开 TOST\"}\n  action_items:\n    - {round: 13, action: \"Introduction 首次使用处展开 'Two One-Sided Tests (TOST)'\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-N1\n  summary: \"Introduction Finding (1) 仍过于密集 — 56 词复合句含多层嵌套\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - {round: 12, reviewers: [R2], note: \"Finding (1) 含冒号、两个括号插入、分号、and/but 转折\"}\n    - {round: 13, reviewers: [], note: \"本轮未直接提及此具体问题\"}\n  action_items:\n    - {round: 12, action: \"拆 Finding (1) 为 2-3 句\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-N2\n  summary: \"Conclusion 仅 3 句话 — 缺 future work、broader impact、training-based IE 对比\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - {round: 12, reviewers: [R1, R2], note: \"Conclusion 像 TL;DR 而非有洞察的收尾\"}\n    - {round: 13, reviewers: [R1, R2], note: \"R2-W2 再次确认; R1 AGREE 但 severity 分歧 (R1:minor, R2:major)\"}\n  action_items:\n    - {round: 13, action: \"同 R11-W1 action\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W1\n  summary: \"Contribution 3 将 NER null result 包装为正面贡献\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - {round: 12, reviewers: [R1, R2], note: \"后半句 'NER shows no batch-level BCS signal' 是 null result 正面包装\"}\n    - {round: 13, reviewers: [R1, R2], note: \"R2-N2 [critical] 再次提出; R1 [REBUT]: task-dependent diagnosis (missed entity dominance) 超出简单 null result, 但同意措辞需更 transparent; 共识: 保留独立 contribution 但改 framing, 如 'We demonstrate that batch-level confusability prediction is task-dependent: effective for RE but absent in NER, and diagnose this asymmetry'\"}\n  action_items:\n    - {round: 13, action: \"Contribution 3 改写: 强调诊断性发现而非包装 null result; 参考 R1 建议措辞\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W2\n  summary: \"Appendix N/P 残余因果语言 ('count-driven', 'BCS-driven')\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - {round: 12, reviewers: [R2], note: \"main.tex L502/L508 'count-driven decline'; L513 'BCS-driven confusability effect'\"}\n    - {round: 13, reviewers: [], note: \"本轮未直接提及\"}\n  action_items:\n    - {round: 12, action: \"替换为 'count-related decline' / 'BCS-associated confusability effect'\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W3\n  summary: \"TOST logit-scale inconclusive (p=0.209) 未在正文充分讨论; 仅 FewRel 支持\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - {round: 12, reviewers: [R1, R2], note: \"logit-scale TOST p=0.209, 2×2 factorial p=0.56, ±1pp inconclusive\"}\n    - {round: 13, reviewers: [R1, R2], note: \"R1-W1 [major] 核心问题: linear-scale favorable 但 logit-scale unfavorable, 选择 primary scale 看起来 outcome-driven; R2 交叉 AGREE: 透明但有偏好; 共识: 正文需更显著报告 logit-scale 不一致, claim 弱化为 'under primary linear specification; inconclusive on logit scale'; 建议 mixed-effects logistic regression (但 n=69 可能 underpowered)\"}\n  action_items:\n    - {round: 12, action: \"正文 §4.4 或 Discussion 补充 logit-scale 不一致性讨论\", assigned_to: agent, status: in_progress}\n    - {round: 13, action: \"§4.4 正文显著报告 logit-scale 结果; 措辞从 'confirms bounded association' → 'evidence for bounded association under primary specification; logit-scale inconclusive'\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W4\n  summary: \"Introduction 五发现 vs 四贡献不对齐\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - {round: 12, reviewers: [R1, R2], note: \"Finding (4) centrality confound 和 Finding (5) decomposition failure 映射到哪条 contribution 不明\"}\n    - {round: 13, reviewers: [R1, R2], note: \"R2-W5 再次确认; R1 交叉 AGREE; 具体: Finding (3) 'cross-scale consistency' 无对应 contribution\"}\n  action_items:\n    - {round: 13, action: \"统一 findings 和 contributions 数量/映射; 或在 contribution list 中标注对应 findings (§X)\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W5\n  summary: \"Orphan bib entries (wellek2010testing, perneger-1998, llm-calibration-survey-2024)\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - {round: 12, reviewers: [R1, R2], note: \"3 个 bib entries 未被 \\\\cite\"}\n    - {round: 13, reviewers: [R2], note: \"确认这三个条目已不存在于 references.bib 中\"}\n  resolution: \"Orphan entries 已删除\"\n  resolution_round: 13\n\n- id: R13-W1\n  summary: \"Gemini 2.5 Flash 引用错误: bib gemini-team-2024 指向 Gemini 1.5 论文 (arXiv:2403.05530)\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - {round: 13, reviewers: [R1, R2], note: \"R1-W5 + R2-W1 双方确认; 事实性错误, 论文使用 Gemini 2.5 Flash 但引用 Gemini 1.5 tech report\"}\n  action_items:\n    - {round: 13, action: \"替换为 Gemini 2.5 正确引用 (tech report 或博客); 若无可用引用则标注 'Gemini 2.5 Flash (Google, 2025)' 不带具体 citation\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W2\n  summary: \"BCS > 0.59 阈值缺乏 formal derivation (无 ROC/threshold sensitivity/precision-recall)\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - {round: 13, reviewers: [R1, R2], note: \"R1-W2 (partial) + R2-W4 [major]; Discussion practical implications 推荐 0.59 阈值但无推导过程; 跨数据集一致性未验证\"}\n  action_items:\n    - {round: 13, action: \"在正文或 Appendix 提供 BCS threshold 的推导 (如 ROC, sensitivity curve); 报告不同阈值下的 accuracy gap; 说明数字来源\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W3\n  summary: \"SCS §3.2 'We introduce' 措辞暗示指标新颖性, 但与 LLM-PEE 形式相同\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - {round: 13, reviewers: [R1, R2], note: \"R1-W8 + R2-N1; §3.2 'We introduce the Schema Confusability Score' vs Related Work 承认 = LLM-PEE; 建议改为 'We operationalize...' 或 'We adopt...'\"}\n  action_items:\n    - {round: 13, action: \"§3.2 改 'We introduce' → 'We operationalize confusability as the Schema Confusability Score' 或类似措辞\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W4\n  summary: \"Abstract 偏短 (~115-140 words), 缺 motivation 和 cross-model generalization\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - {round: 13, reviewers: [R2], note: \"R2-W3 [major]; R1 交叉 AGREE with nuance (标 minor): 信息密度高但缺 framing; 共识: 补充 1-2 句 motivation + cross-model evidence, 扩至 ~200 words\"}\n  action_items:\n    - {round: 13, action: \"Abstract 补充: (1) training-free LLM IE 问题重要性 (2) cross-model validation 提及; 目标 ~200 words\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W5\n  summary: \"FewRel closed-set classification + constrained decoding 格式特殊性, 泛化性不确定\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - {round: 13, reviewers: [R1], note: \"R1-W7 [minor]; enum constraint 保证每个实例产生 prediction, 消除 none 影响; Limitations item 6 承认但不够 prominent; R2 交叉 AGREE: DocRED 提供部分泛化证据\"}\n  action_items:\n    - {round: 13, action: \"Discussion 或 Limitations 更显著讨论 closed-set format 对 Dimension separation 的影响\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# INFO — Minor\n# ============================================================\n\n- id: R10-m1\n  summary: \"Cross-seed variance (2.7pp at count 16) 与 typical effect (2.2pp) 量级相当\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - {round: 10, reviewers: [R1, R2], note: \"R1 W2; R2 REBUT: batch sampling variance\"}\n    - {round: 11, reviewers: [R1, R2], note: \"seed SD=0.88pp at count 80 在 greedy mode 下不应存在\"}\n    - {round: 12, reviewers: [], note: \"本轮未直接提及\"}\n    - {round: 13, reviewers: [], note: \"本轮未直接提及\"}\n  action_items:\n    - {round: 11, action: \"修正 'eliminates randomness' 措辞; 注明 FP8 non-determinism\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R10-m2\n  summary: \"NER U-shape mechanistic 解释 (dual-task burden) 未经验证 — 应标注为 hypothesis\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - {round: 10, reviewers: [R1, R2], note: \"indirect evidence plausible 但不构成 definitive proof\"}\n    - {round: 13, reviewers: [R1, R2], note: \"R2-Q3 + R1-Q4: 建议通过 full-schema false positive 检查或 dummy-padded schema 实验验证; R1 交叉 AGREE R2-Q3\"}\n  action_items:\n    - {round: 10, action: \"U-shape 解释标注为 hypothesis\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R10-m3\n  summary: \"Missing references\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - {round: 10, reviewers: [R1, R2], note: \"NuNER 应补\"}\n    - {round: 11, reviewers: [R1, R2], note: \"Levy 2024, Dror 2018, GenRES/ULTRA, Zhao 2021\"}\n    - {round: 12, reviewers: [R1, R2], note: \"Outlines (Willard & Louf 2023), Cheng 2023 Batch Prompting, Lu 2022\"}\n    - {round: 13, reviewers: [R1, R2], note: \"R1: structured prediction calibration (Kuleshov 2018, Desai & Durrett 2020); R2: embedding similarity for label confusion (Prototypical Networks confusion analysis); R1 交叉: Müller et al. 2019 (Label Smoothing), Peterson et al. 2019\"}\n  action_items:\n    - {round: 13, action: \"补充 constrained decoding calibration 文献; 考虑补充 embedding similarity for confusion 文献\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R10-m5\n  summary: \"1000 instances 对 long-tail types 充分性\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - {round: 10, reviewers: [R1], note: \"低频 types 个位数 instances\"}\n    - {round: 11, reviewers: [R1, R2], note: \"cluster bootstrap 部分 addresses\"}\n    - {round: 13, reviewers: [], note: \"本轮未直接提及\"}\n  action_items:\n    - {round: 11, action: \"频率分层 SCS-confusion analysis 或 discuss as limitation\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-m1\n  summary: \"FP8 + vLLM greedy decoding 残余非确定性 (seed SD=0.88pp at count 80)\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - {round: 11, reviewers: [R1], note: \"greedy mode 下 SD 应为 0\"}\n    - {round: 13, reviewers: [], note: \"本轮未直接提及\"}\n  action_items:\n    - {round: 11, action: \"调查 vLLM FP8 non-determinism; 修正 'eliminates randomness'\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-m1\n  summary: \"Abstract 偏短 (~130-140 words), 低于 150-250 words 建议范围\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - {round: 12, reviewers: [R2], note: \"可增加一句 practical implications\"}\n    - {round: 13, reviewers: [R1, R2], note: \"升级为 R13-W4 (warning), 实际约 115 words\"}\n  resolution: \"升级追踪于 R13-W4\"\n  resolution_round: 13\n\n- id: R12-m2\n  summary: \"-ing 分词短语和 'Notably' 使用 — AI 写作痕迹残余\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - {round: 12, reviewers: [R2], note: \"Results §4.1 'indicating...'; Discussion §5 'suggesting...'\"}\n    - {round: 13, reviewers: [R1, R2], note: \"R2-W6 确认约 10-15 处; R1 交叉 AGREE\"}\n  action_items:\n    - {round: 13, action: \"全文 grep 'ing,' 模式, 改写 participial phrases 为独立句子\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-m3\n  summary: \"DocRED count curve 仅引用未在 Appendix 呈现\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - {round: 12, reviewers: [R2], note: \"§4.1 引用 'Appendix' 但无 DocRED count curve\"}\n    - {round: 13, reviewers: [], note: \"本轮未直接提及\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-m1\n  summary: \"MAVEN validation set 是否用于 hyperparameter 选择未声明\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - {round: 13, reviewers: [R2], note: \"R2-W7 [minor]; R1 交叉 AGREE: 应声明 validation set 是否用于任何实验设计决策\"}\n  action_items:\n    - {round: 13, action: \"§3.1 MAVEN 段补充声明 validation set 未用于 hyperparameter 选择 (如适用)\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-m2\n  summary: \"多重比较处理: prompt variant 8 tests 用 directional consistency 代替正式检验\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - {round: 13, reviewers: [R1], note: \"R1-W6 [minor]; 7/8 negative 隐式 sign test p=0.035; R2 交叉 AGREE: 建议显式报告 sign test p-value\"}\n  action_items:\n    - {round: 13, action: \"Appendix prompt variant section 显式报告 sign test p-value (0.035)\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-m3\n  summary: \"FewRel contamination 风险: R1 标 major, R2 REBUT 认为现有分析充分\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - {round: 13, reviewers: [R1, R2], note: \"R1-W4 [major]: train-origin p=0.06 仅 suggestive, non-uniform contamination 未排除; R2 [REBUT]: 反向差异 + covariate control + DocRED replication 已充分, 建议降为 minor; 未达共识, 记录分歧\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# RESOLVED (历史)\n# ============================================================\n\n- id: R9-W1\n  summary: \"Single-seed evaluation — count curve 每 level 仅 5 batches\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"D051 completed: 3-seed × 25-batch count curves with ±1SD error bars\"\n  resolution_round: 10\n\n- id: R10-W1\n  summary: \"\\\\enlargethispage*{9\\\\baselineskip} 操纵页面布局\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"\\\\enlargethispage 已删除; 当前版本格式合规\"\n  resolution_round: 11\n\n- id: R10-W2\n  summary: \"Negative results (§5) 占 ~1.5 页但缺乏 constructive next steps\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"§5 Future directions paragraph added with 3 concrete avenues\"\n  resolution_round: 11\n\n- id: R10-W3\n  summary: \"Abstract 数字密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"Abstract 精简至 3 个核心数字\"\n  resolution_round: 12\n\n- id: R10-W4\n  summary: \"Introduction Contribution list 含未铺垫概念且每条过长\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"Contribution list 改为方法论声明格式, 每条 1-2 行\"\n  resolution_round: 12\n\n- id: R10-W5\n  summary: \"BCS 'generalizes across tasks' (Contribution #3) 过强 — batch-level 仅在 RE 直接支持\"\n  category: framing\n  severity: warning\n  status: resolved\n  resolution: \"Contribution 3 限定为 RE-specific\"\n  resolution_round: 12\n\n- id: R10-W6\n  summary: \"Em-dash (---) 使用偏高 — AI 写作痕迹\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"Em-dash 已清理\"\n  resolution_round: 11\n\n- id: R10-W7\n  summary: \"Supplementary 三处 placeholder sections 未完成\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"无独立 supplementary; 所有补充材料在 main.tex Appendix\"\n  resolution_round: 12\n\n- id: R11-W3\n  summary: \"Prompt variant analysis (n=10) underpowered + 无 multiple comparison correction\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Rothman (1990) 论证 + directional consistency 充分; prompt analysis 定位为 robustness check\"\n  resolution_round: 12\n\n- id: R10-m4\n  summary: \"Multiple comparisons: Rothman (1990) 适用于 conceptual replications\"\n  category: method\n  severity: info\n  status: resolved\n  resolution: \"R12 交叉共识: Rothman 论证 + directional consistency 对 robustness checks 充分\"\n  resolution_round: 12\n\n- id: R2-N3-80rel\n  summary: \"Abstract/Intro 以 extreme-batch 31.2pp 为 headline, typical 2.2pp 被弱化\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"D051 W2: Intro typical-first; Discussion IQR caveat; R² range corrected\"\n  resolution_round: 9\n\n- id: R4-N1\n  summary: \"RE batch composition +1.4pp (p≈0.19) — Contribution #4 framing\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"D051 W4: Contribution #4 → 'structural barriers' with specific numbers\"\n  resolution_round: 9\n\n- id: R6-N1\n  summary: \"Two-channel decomposition 概念贡献有限 — Findings-level\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"D051 W4: 4 contributions rewritten emphasizing non-obvious findings\"\n  resolution_round: 9\n\n- id: MW2\n  summary: \"Pairwise r²=1.3-1.7% 到 batch R²=22% 聚合: conditioning bias\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"D051 W3 + MW2 compute: simulation → illustrative; unconditional MC R²=0.044; observed R²=0.218 primary\"\n  resolution_round: 9\n\n- id: R5-W1\n  summary: \"FewRel train+val 合并 — data contamination 风险\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Split-origin covariate confirms BCS partial effect unchanged\"\n  resolution_round: 9\n\n- id: R5-N1\n  summary: \"SCS novelty — metric 与 LLM-PEE 形式相同\"\n  category: framing\n  severity: warning\n  status: resolved\n  resolution: \"D051 W4: Contribution #2 reframed as empirical validation + centrality confound\"\n  resolution_round: 9\n\n- id: R6-W1\n  summary: \"'首次 controlled study' 声称需限定\"\n  category: framing\n  severity: warning\n  status: resolved\n  resolution: \"D051 S7: 'To our knowledge' added\"\n  resolution_round: 9\n\n- id: R6-N2\n  summary: \"正文可能超过 8 页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"编译确认 Conclusion 在 p8\"\n  resolution_round: 9\n\n- id: R10-PS\n  summary: \"Prompt sensitivity 实验结果需整合入论文\"\n  category: experiment\n  severity: warning\n  status: resolved\n  resolution: \"Prompt sensitivity results integrated into §4.3 + Appendix H\"\n  resolution_round: 11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "schema-dag-extraction",
    "issues_yaml": "# Round 13 Review Issues Tracker\n# Updated: 2026-05-18 (Round 13 review completed)\n\n# ============================================================\n# CRITICAL — Must-Fix\n# ============================================================\n\n- id: R3-C2\n  summary: \"'Empirically separable channels' 缺乏 formal 统计支撑 — TOST margin ±3pp > typical effect 2.2pp\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 9\n  mentions:\n    - {round: 3, reviewers: [R1, R2], note: \"因果语言过强\"}\n    - {round: 4, reviewers: [R1, R2], note: \"Title 'Drive' + §4.3 暗示因果\"}\n    - {round: 5, reviewers: [R1, R2, R3], note: \"三人共识改措辞\"}\n    - {round: 6, reviewers: [R1, R2, R3], note: \"factorial p=0.50; 建议 'mechanistically distinguishable'\"}\n    - {round: 7, reviewers: [R1, R2], note: \"三项 factorial 检验中两项失败\"}\n    - {round: 8, reviewers: [R1, R2], note: \"R1-N1 critical: 3/4 tests 失败; 共识: 需限定\"}\n    - {round: 9, reviewers: [R1, R2, R3], note: \"三人共识: TOST ±3pp margin 用 prompt variation 锚定不合逻辑; margin > typical main effect; ±1pp inconclusive\"}\n  action_items:\n    - {round: 9, action: \"D051: 'additive separability' → 'bounded interaction' 全文统一; SESOI effect-size anchored\", assigned_to: agent, status: done}\n  resolution: \"D051 W1: 全文 'bounded interaction' 统一; SESOI effect-size anchored; sensitivity table in Appendix\"\n  resolution_round: 9\n\n- id: R10-N1\n  summary: \"因果语言 ('driven', 'channels', 'shape') 超出 observational/quasi-experimental 证据边界\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - {round: 10, reviewers: [R1, R2], note: \"R1 critical N3 + R2 AGREE with qualification; 共识: Title 'shape' 暗示因果\"}\n    - {round: 11, reviewers: [R1, R2], note: \"R1 W4 + R2 AGREE: Title 'Shape' + Limitations 承认 no interventional causality = 不匹配\"}\n    - {round: 12, reviewers: [R2], note: \"MOSTLY FIXED: Title 改为 'Predict'; 正文主体无 'channels'/'driven'; 仅 Appendix N/P 残余 'count-driven'/'BCS-driven' — 降级为 R12-W2\"}\n  action_items:\n    - {round: 10, action: \"分层替换 (D052): correlational → 'predicts'/'associated with'\", assigned_to: agent, status: done}\n    - {round: 11, action: \"D054: Title 'Shape' → 'Predict'; 全文因果语言 grep 扫描清零\", assigned_to: agent, status: done}\n  resolution: \"Title 改为 'Predict'; 正文因果语言已清理; Appendix 残余为 R12-W2 追踪\"\n  resolution_round: 12\n\n- id: R10-N2\n  summary: \"Pair-level→batch-level 聚合推理链叙事误导 — unconditional sim R²=0.044 vs 观测 0.218\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - {round: 10, reviewers: [R1, R2], note: \"R1 critical N1; R2 AGREE with nuance\"}\n    - {round: 11, reviewers: [R1, R2], note: \"叙事链暗示因果中介\"}\n    - {round: 12, reviewers: [R2], note: \"FIXED: Discussion §6 分层叙述 unconditional→conditional→batch; Appendix I 明确标注 'illustrative explanatory model'; 与直接实证 R²=0.218 明确区分\"}\n  action_items:\n    - {round: 10, action: \"§4.3: R²=0.218 direct OLS 作 primary claim; simulation 标注 post-hoc\", assigned_to: agent, status: done}\n    - {round: 11, action: \"D054: Discussion 区分 pair r²=1.3% vs batch R²=22%\", assigned_to: agent, status: done}\n  resolution: \"叙事链清晰分层; simulation 明确为 illustrative; R²=0.218 为独立实证\"\n  resolution_round: 12\n\n- id: R10-N3\n  summary: \"TOST ±3pp margin 的 external anchoring 不足 — 130% amplification threshold 为 arbitrary judgment call\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - {round: 10, reviewers: [R1, R2], note: \"R1 critical N2: margin循环, ±1pp inconclusive\"}\n    - {round: 11, reviewers: [R1, R2], note: \"±3pp = typical effect 136%; 共识: 以 ±2pp 为 primary\"}\n    - {round: 12, reviewers: [R1, R2], note: \"R2 确认 FIXED: Appendix D 三重 anchoring (empirical/practical/statistical) + sensitivity table; R1 经重审 Appendix C 后从 critical 下调为 should-fix; 但 logit-scale inconclusive (p=0.209) 仍需讨论 → R12-W3\"}\n  action_items:\n    - {round: 10, action: \"三条 anchor: empirical + practical + statistical\", assigned_to: agent, status: done}\n    - {round: 11, action: \"D054: sensitivity analysis in Appendix\", assigned_to: agent, status: done}\n  resolution: \"三重 anchoring + sensitivity table 已到位; logit-scale 不一致性追踪于 R12-W3\"\n  resolution_round: 12\n\n- id: R10-N4\n  summary: \"SCS/BCS Contribution #2 framing 暗示 metric novelty — 实际增量是 controlled validation\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: \"Contribution #2 已 reframe 为 controlled validation; §2 SCS novelty 段明确界定增量\"\n  resolution_round: 11\n\n- id: R11-N1\n  summary: \"NER Dimension 2 batch-level 证据方向相反（r=+0.50~+0.58），但论文 title/abstract 泛化为 cross-task\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Abstract/Intro/Contribution/Discussion 均已精确限定 batch-level Dim2 = RE-specific; pairwise cross-task 正确区分\"\n  resolution_round: 12\n\n- id: R11-N2\n  summary: \"核心效应量过小 (typical gap 2.2pp, pairwise r²=1.3%) — practical significance 存疑\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - {round: 11, reviewers: [R1, R2], note: \"2.2pp CI [0.4, 4.0] 在部署中几乎不可察觉; 需更强论证 practical significance\"}\n    - {round: 12, reviewers: [R1, R2], note: \"降级为 should-fix, 更多是 findings 本身的局限而非写作缺陷\"}\n    - {round: 13, reviewers: [R1, R2], note: \"R1-W2 + R2-N1 双方再次确认; R2 交叉 AGREE R1-W2; 共识: extreme-batch gap (25-31pp) 在叙事中占比过高, typical gap 2.2pp 应前置; Abstract 虽诚实但 Results/Introduction 节奏偏向极端值\"}\n  action_items:\n    - {round: 11, action: \"D054 Phase 3: Discussion reframe '2.2pp negligible IS the finding'\", assigned_to: agent, status: done}\n    - {round: 12, action: \"Discussion 补充: 在什么部署条件下 2.2pp 有实际价值; BCS screening vs few-shot augmentation 成本效益对比\", assigned_to: agent, status: in_progress}\n    - {round: 13, action: \"Introduction/Results 叙事调整: extreme-batch 数字仅作对比锚点, typical gap 前置; 补充 BCS threshold ROC/precision-recall analysis\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# WARNING — Should-Fix\n# ============================================================\n\n- id: R11-W1\n  summary: \"Discussion/Conclusion 过于简短 (~15 行) — 缺 actionable recommendations\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - {round: 11, reviewers: [R1, R2], note: \"analysis paper 需更充分的 Discussion\"}\n    - {round: 12, reviewers: [R1, R2], note: \"Discussion MOSTLY FIXED; Conclusion 仅 3 句, 无 future work\"}\n    - {round: 13, reviewers: [R1, R2], note: \"R2-W2 [major]: Conclusion ~120 words, 缺 future work/broader implications/training-based IE 对比; R1 交叉 AGREE 但认为 minor (篇幅限制下 Discussion 已充分); 共识: Conclusion 需扩展\"}\n  action_items:\n    - {round: 11, action: \"D054 Phase 3a: Discussion 扩展\", assigned_to: agent, status: done}\n    - {round: 12, action: \"Conclusion 扩展至 5-8 句\", assigned_to: agent, status: in_progress}\n    - {round: 13, action: \"Conclusion 扩展: (1) 核心发现 (2) training-based IE 对比 (3) future directions (4) broader implications\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W2\n  summary: \"TOST (Two One-Sided Tests) 术语首次出现未展开\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - {round: 11, reviewers: [R1, R2], note: \"NLP 社区对 TOST 不熟悉\"}\n    - {round: 12, reviewers: [R2], note: \"Introduction L15 首次使用 'TOST p=0.003' 未展开\"}\n    - {round: 13, reviewers: [], note: \"本轮未直接提及, 但 Introduction finding (1) 仍含未展开 TOST\"}\n  action_items:\n    - {round: 13, action: \"Introduction 首次使用处展开 'Two One-Sided Tests (TOST)'\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-N1\n  summary: \"Introduction Finding (1) 仍过于密集 — 56 词复合句含多层嵌套\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - {round: 12, reviewers: [R2], note: \"Finding (1) 含冒号、两个括号插入、分号、and/but 转折\"}\n    - {round: 13, reviewers: [], note: \"本轮未直接提及此具体问题\"}\n  action_items:\n    - {round: 12, action: \"拆 Finding (1) 为 2-3 句\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-N2\n  summary: \"Conclusion 仅 3 句话 — 缺 future work、broader impact、training-based IE 对比\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - {round: 12, reviewers: [R1, R2], note: \"Conclusion 像 TL;DR 而非有洞察的收尾\"}\n    - {round: 13, reviewers: [R1, R2], note: \"R2-W2 再次确认; R1 AGREE 但 severity 分歧 (R1:minor, R2:major)\"}\n  action_items:\n    - {round: 13, action: \"同 R11-W1 action\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W1\n  summary: \"Contribution 3 将 NER null result 包装为正面贡献\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - {round: 12, reviewers: [R1, R2], note: \"后半句 'NER shows no batch-level BCS signal' 是 null result 正面包装\"}\n    - {round: 13, reviewers: [R1, R2], note: \"R2-N2 [critical] 再次提出; R1 [REBUT]: task-dependent diagnosis (missed entity dominance) 超出简单 null result, 但同意措辞需更 transparent; 共识: 保留独立 contribution 但改 framing, 如 'We demonstrate that batch-level confusability prediction is task-dependent: effective for RE but absent in NER, and diagnose this asymmetry'\"}\n  action_items:\n    - {round: 13, action: \"Contribution 3 改写: 强调诊断性发现而非包装 null result; 参考 R1 建议措辞\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W2\n  summary: \"Appendix N/P 残余因果语言 ('count-driven', 'BCS-driven')\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - {round: 12, reviewers: [R2], note: \"main.tex L502/L508 'count-driven decline'; L513 'BCS-driven confusability effect'\"}\n    - {round: 13, reviewers: [], note: \"本轮未直接提及\"}\n  action_items:\n    - {round: 12, action: \"替换为 'count-related decline' / 'BCS-associated confusability effect'\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W3\n  summary: \"TOST logit-scale inconclusive (p=0.209) 未在正文充分讨论; 仅 FewRel 支持\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - {round: 12, reviewers: [R1, R2], note: \"logit-scale TOST p=0.209, 2×2 factorial p=0.56, ±1pp inconclusive\"}\n    - {round: 13, reviewers: [R1, R2], note: \"R1-W1 [major] 核心问题: linear-scale favorable 但 logit-scale unfavorable, 选择 primary scale 看起来 outcome-driven; R2 交叉 AGREE: 透明但有偏好; 共识: 正文需更显著报告 logit-scale 不一致, claim 弱化为 'under primary linear specification; inconclusive on logit scale'; 建议 mixed-effects logistic regression (但 n=69 可能 underpowered)\"}\n  action_items:\n    - {round: 12, action: \"正文 §4.4 或 Discussion 补充 logit-scale 不一致性讨论\", assigned_to: agent, status: in_progress}\n    - {round: 13, action: \"§4.4 正文显著报告 logit-scale 结果; 措辞从 'confirms bounded association' → 'evidence for bounded association under primary specification; logit-scale inconclusive'\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W4\n  summary: \"Introduction 五发现 vs 四贡献不对齐\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - {round: 12, reviewers: [R1, R2], note: \"Finding (4) centrality confound 和 Finding (5) decomposition failure 映射到哪条 contribution 不明\"}\n    - {round: 13, reviewers: [R1, R2], note: \"R2-W5 再次确认; R1 交叉 AGREE; 具体: Finding (3) 'cross-scale consistency' 无对应 contribution\"}\n  action_items:\n    - {round: 13, action: \"统一 findings 和 contributions 数量/映射; 或在 contribution list 中标注对应 findings (§X)\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W5\n  summary: \"Orphan bib entries (wellek2010testing, perneger-1998, llm-calibration-survey-2024)\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - {round: 12, reviewers: [R1, R2], note: \"3 个 bib entries 未被 \\\\cite\"}\n    - {round: 13, reviewers: [R2], note: \"确认这三个条目已不存在于 references.bib 中\"}\n  resolution: \"Orphan entries 已删除\"\n  resolution_round: 13\n\n- id: R13-W1\n  summary: \"Gemini 2.5 Flash 引用错误: bib gemini-team-2024 指向 Gemini 1.5 论文 (arXiv:2403.05530)\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - {round: 13, reviewers: [R1, R2], note: \"R1-W5 + R2-W1 双方确认; 事实性错误, 论文使用 Gemini 2.5 Flash 但引用 Gemini 1.5 tech report\"}\n  action_items:\n    - {round: 13, action: \"替换为 Gemini 2.5 正确引用 (tech report 或博客); 若无可用引用则标注 'Gemini 2.5 Flash (Google, 2025)' 不带具体 citation\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W2\n  summary: \"BCS > 0.59 阈值缺乏 formal derivation (无 ROC/threshold sensitivity/precision-recall)\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - {round: 13, reviewers: [R1, R2], note: \"R1-W2 (partial) + R2-W4 [major]; Discussion practical implications 推荐 0.59 阈值但无推导过程; 跨数据集一致性未验证\"}\n  action_items:\n    - {round: 13, action: \"在正文或 Appendix 提供 BCS threshold 的推导 (如 ROC, sensitivity curve); 报告不同阈值下的 accuracy gap; 说明数字来源\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W3\n  summary: \"SCS §3.2 'We introduce' 措辞暗示指标新颖性, 但与 LLM-PEE 形式相同\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - {round: 13, reviewers: [R1, R2], note: \"R1-W8 + R2-N1; §3.2 'We introduce the Schema Confusability Score' vs Related Work 承认 = LLM-PEE; 建议改为 'We operationalize...' 或 'We adopt...'\"}\n  action_items:\n    - {round: 13, action: \"§3.2 改 'We introduce' → 'We operationalize confusability as the Schema Confusability Score' 或类似措辞\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W4\n  summary: \"Abstract 偏短 (~115-140 words), 缺 motivation 和 cross-model generalization\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - {round: 13, reviewers: [R2], note: \"R2-W3 [major]; R1 交叉 AGREE with nuance (标 minor): 信息密度高但缺 framing; 共识: 补充 1-2 句 motivation + cross-model evidence, 扩至 ~200 words\"}\n  action_items:\n    - {round: 13, action: \"Abstract 补充: (1) training-free LLM IE 问题重要性 (2) cross-model validation 提及; 目标 ~200 words\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W5\n  summary: \"FewRel closed-set classification + constrained decoding 格式特殊性, 泛化性不确定\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - {round: 13, reviewers: [R1], note: \"R1-W7 [minor]; enum constraint 保证每个实例产生 prediction, 消除 none 影响; Limitations item 6 承认但不够 prominent; R2 交叉 AGREE: DocRED 提供部分泛化证据\"}\n  action_items:\n    - {round: 13, action: \"Discussion 或 Limitations 更显著讨论 closed-set format 对 Dimension separation 的影响\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# INFO — Minor\n# ============================================================\n\n- id: R10-m1\n  summary: \"Cross-seed variance (2.7pp at count 16) 与 typical effect (2.2pp) 量级相当\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - {round: 10, reviewers: [R1, R2], note: \"R1 W2; R2 REBUT: batch sampling variance\"}\n    - {round: 11, reviewers: [R1, R2], note: \"seed SD=0.88pp at count 80 在 greedy mode 下不应存在\"}\n    - {round: 12, reviewers: [], note: \"本轮未直接提及\"}\n    - {round: 13, reviewers: [], note: \"本轮未直接提及\"}\n  action_items:\n    - {round: 11, action: \"修正 'eliminates randomness' 措辞; 注明 FP8 non-determinism\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R10-m2\n  summary: \"NER U-shape mechanistic 解释 (dual-task burden) 未经验证 — 应标注为 hypothesis\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - {round: 10, reviewers: [R1, R2], note: \"indirect evidence plausible 但不构成 definitive proof\"}\n    - {round: 13, reviewers: [R1, R2], note: \"R2-Q3 + R1-Q4: 建议通过 full-schema false positive 检查或 dummy-padded schema 实验验证; R1 交叉 AGREE R2-Q3\"}\n  action_items:\n    - {round: 10, action: \"U-shape 解释标注为 hypothesis\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R10-m3\n  summary: \"Missing references\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - {round: 10, reviewers: [R1, R2], note: \"NuNER 应补\"}\n    - {round: 11, reviewers: [R1, R2], note: \"Levy 2024, Dror 2018, GenRES/ULTRA, Zhao 2021\"}\n    - {round: 12, reviewers: [R1, R2], note: \"Outlines (Willard & Louf 2023), Cheng 2023 Batch Prompting, Lu 2022\"}\n    - {round: 13, reviewers: [R1, R2], note: \"R1: structured prediction calibration (Kuleshov 2018, Desai & Durrett 2020); R2: embedding similarity for label confusion (Prototypical Networks confusion analysis); R1 交叉: Müller et al. 2019 (Label Smoothing), Peterson et al. 2019\"}\n  action_items:\n    - {round: 13, action: \"补充 constrained decoding calibration 文献; 考虑补充 embedding similarity for confusion 文献\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R10-m5\n  summary: \"1000 instances 对 long-tail types 充分性\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - {round: 10, reviewers: [R1], note: \"低频 types 个位数 instances\"}\n    - {round: 11, reviewers: [R1, R2], note: \"cluster bootstrap 部分 addresses\"}\n    - {round: 13, reviewers: [], note: \"本轮未直接提及\"}\n  action_items:\n    - {round: 11, action: \"频率分层 SCS-confusion analysis 或 discuss as limitation\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-m1\n  summary: \"FP8 + vLLM greedy decoding 残余非确定性 (seed SD=0.88pp at count 80)\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n    - {round: 11, reviewers: [R1], note: \"greedy mode 下 SD 应为 0\"}\n    - {round: 13, reviewers: [], note: \"本轮未直接提及\"}\n  action_items:\n    - {round: 11, action: \"调查 vLLM FP8 non-determinism; 修正 'eliminates randomness'\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-m1\n  summary: \"Abstract 偏短 (~130-140 words), 低于 150-250 words 建议范围\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - {round: 12, reviewers: [R2], note: \"可增加一句 practical implications\"}\n    - {round: 13, reviewers: [R1, R2], note: \"升级为 R13-W4 (warning), 实际约 115 words\"}\n  resolution: \"升级追踪于 R13-W4\"\n  resolution_round: 13\n\n- id: R12-m2\n  summary: \"-ing 分词短语和 'Notably' 使用 — AI 写作痕迹残余\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - {round: 12, reviewers: [R2], note: \"Results §4.1 'indicating...'; Discussion §5 'suggesting...'\"}\n    - {round: 13, reviewers: [R1, R2], note: \"R2-W6 确认约 10-15 处; R1 交叉 AGREE\"}\n  action_items:\n    - {round: 13, action: \"全文 grep 'ing,' 模式, 改写 participial phrases 为独立句子\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-m3\n  summary: \"DocRED count curve 仅引用未在 Appendix 呈现\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n    - {round: 12, reviewers: [R2], note: \"§4.1 引用 'Appendix' 但无 DocRED count curve\"}\n    - {round: 13, reviewers: [], note: \"本轮未直接提及\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-m1\n  summary: \"MAVEN validation set 是否用于 hyperparameter 选择未声明\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - {round: 13, reviewers: [R2], note: \"R2-W7 [minor]; R1 交叉 AGREE: 应声明 validation set 是否用于任何实验设计决策\"}\n  action_items:\n    - {round: 13, action: \"§3.1 MAVEN 段补充声明 validation set 未用于 hyperparameter 选择 (如适用)\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-m2\n  summary: \"多重比较处理: prompt variant 8 tests 用 directional consistency 代替正式检验\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - {round: 13, reviewers: [R1], note: \"R1-W6 [minor]; 7/8 negative 隐式 sign test p=0.035; R2 交叉 AGREE: 建议显式报告 sign test p-value\"}\n  action_items:\n    - {round: 13, action: \"Appendix prompt variant section 显式报告 sign test p-value (0.035)\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-m3\n  summary: \"FewRel contamination 风险: R1 标 major, R2 REBUT 认为现有分析充分\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - {round: 13, reviewers: [R1, R2], note: \"R1-W4 [major]: train-origin p=0.06 仅 suggestive, non-uniform contamination 未排除; R2 [REBUT]: 反向差异 + covariate control + DocRED replication 已充分, 建议降为 minor; 未达共识, 记录分歧\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# RESOLVED (历史)\n# ============================================================\n\n- id: R9-W1\n  summary: \"Single-seed evaluation — count curve 每 level 仅 5 batches\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"D051 completed: 3-seed × 25-batch count curves with ±1SD error bars\"\n  resolution_round: 10\n\n- id: R10-W1\n  summary: \"\\\\enlargethispage*{9\\\\baselineskip} 操纵页面布局\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"\\\\enlargethispage 已删除; 当前版本格式合规\"\n  resolution_round: 11\n\n- id: R10-W2\n  summary: \"Negative results (§5) 占 ~1.5 页但缺乏 constructive next steps\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"§5 Future directions paragraph added with 3 concrete avenues\"\n  resolution_round: 11\n\n- id: R10-W3\n  summary: \"Abstract 数字密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"Abstract 精简至 3 个核心数字\"\n  resolution_round: 12\n\n- id: R10-W4\n  summary: \"Introduction Contribution list 含未铺垫概念且每条过长\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"Contribution list 改为方法论声明格式, 每条 1-2 行\"\n  resolution_round: 12\n\n- id: R10-W5\n  summary: \"BCS 'generalizes across tasks' (Contribution #3) 过强 — batch-level 仅在 RE 直接支持\"\n  category: framing\n  severity: warning\n  status: resolved\n  resolution: \"Contribution 3 限定为 RE-specific\"\n  resolution_round: 12\n\n- id: R10-W6\n  summary: \"Em-dash (---) 使用偏高 — AI 写作痕迹\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"Em-dash 已清理\"\n  resolution_round: 11\n\n- id: R10-W7\n  summary: \"Supplementary 三处 placeholder sections 未完成\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"无独立 supplementary; 所有补充材料在 main.tex Appendix\"\n  resolution_round: 12\n\n- id: R11-W3\n  summary: \"Prompt variant analysis (n=10) underpowered + 无 multiple comparison correction\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Rothman (1990) 论证 + directional consistency 充分; prompt analysis 定位为 robustness check\"\n  resolution_round: 12\n\n- id: R10-m4\n  summary: \"Multiple comparisons: Rothman (1990) 适用于 conceptual replications\"\n  category: method\n  severity: info\n  status: resolved\n  resolution: \"R12 交叉共识: Rothman 论证 + directional consistency 对 robustness checks 充分\"\n  resolution_round: 12\n\n- id: R2-N3-80rel\n  summary: \"Abstract/Intro 以 extreme-batch 31.2pp 为 headline, typical 2.2pp 被弱化\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"D051 W2: Intro typical-first; Discussion IQR caveat; R² range corrected\"\n  resolution_round: 9\n\n- id: R4-N1\n  summary: \"RE batch composition +1.4pp (p≈0.19) — Contribution #4 framing\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"D051 W4: Contribution #4 → 'structural barriers' with specific numbers\"\n  resolution_round: 9\n\n- id: R6-N1\n  summary: \"Two-channel decomposition 概念贡献有限 — Findings-level\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"D051 W4: 4 contributions rewritten emphasizing non-obvious findings\"\n  resolution_round: 9\n\n- id: MW2\n  summary: \"Pairwise r²=1.3-1.7% 到 batch R²=22% 聚合: conditioning bias\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"D051 W3 + MW2 compute: simulation → illustrative; unconditional MC R²=0.044; observed R²=0.218 primary\"\n  resolution_round: 9\n\n- id: R5-W1\n  summary: \"FewRel train+val 合并 — data contamination 风险\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Split-origin covariate confirms BCS partial effect unchanged\"\n  resolution_round: 9\n\n- id: R5-N1\n  summary: \"SCS novelty — metric 与 LLM-PEE 形式相同\"\n  category: framing\n  severity: warning\n  status: resolved\n  resolution: \"D051 W4: Contribution #2 reframed as empirical validation + centrality confound\"\n  resolution_round: 9\n\n- id: R6-W1\n  summary: \"'首次 controlled study' 声称需限定\"\n  category: framing\n  severity: warning\n  status: resolved\n  resolution: \"D051 S7: 'To our knowledge' added\"\n  resolution_round: 9\n\n- id: R6-N2\n  summary: \"正文可能超过 8 页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"编译确认 Conclusion 在 p8\"\n  resolution_round: 9\n\n- id: R10-PS\n  summary: \"Prompt sensitivity 实验结果需整合入论文\"\n  category: experiment\n  severity: warning\n  status: resolved\n  resolution: \"Prompt sensitivity results integrated into §4.3 + Appendix H\"\n  resolution_round: 11"
  }
}
```

</details>

---


### Tool result

_source line 1267 · 2026-05-18T03:12:18.195959+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml\", \"bytes\": 25783}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1268 · 2026-05-18T03:14:43.915322+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "schema-dag-extraction",
  "report": "# Round 13 Consolidated Review Report\n\n**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n**Venue**: EMNLP 2026 via ACL ARR May 2026 cycle\n**审稿模式**: 2 Reviewers × 1 Round + 交叉回应\n**Reviewer 分工**: R1 (方法严谨性 + 实验设计) / R2 (新颖性 + 写作完整性 + 格式合规)\n\n---\n\n## Summary\n\n本文对 training-free LLM IE 中 schema 复杂度如何预测性能退化进行了系统性的 controlled study。将退化分解为两个维度（type count 和 type confusability），提出 SCS/BCS 指标量化 confusability，在四个数据集（Few-NERD, FewRel, DocRED, MAVEN）和四个模型（Qwen3-32B, Llama-3.1-8B/70B, Gemini 2.5 Flash）上验证。论文同时报告了 schema decomposition (SDGD) 的负面结果及其失败诊断。这是一篇实验设计极为严谨的 analysis paper，方法论示范价值突出，但核心贡献受限于 SCS 与 LLM-PEE 指标形式相同、confusability 效应量小（typical 2.2pp）、且 batch-level 信号仅对 RE 有效。\n\n---\n\n## Strengths\n\n**S1. [共识] BCS-controlled quasi-experimental design 是本文最强的方法论贡献。** 固定 count 变化 BCS 的设计在 NLP 实证研究中罕见。FewRel balanced design 消除 type frequency 混淆；within-pool 分析控制 pool composition；TOST equivalence testing 形式化检验 bounded association。两位 Reviewer 一致认为该设计具有方法论示范价值。\n\n**S2. [共识] Robustness checks 的广度和深度在该领域论文中属于上乘水平。** 跨模型 (8B/32B/70B/Gemini)、跨 prompt variant (4 种)、跨数据集 (4 个)、BCS 聚合方式 (mean vs max)、SCS embedding ablation、cross-seed variance decomposition、logit-scale sensitivity。两位 Reviewer 均高度评价。\n\n**S3. [共识] 负面结果的诚实报告和系统诊断。** SDGD 失败不仅被报告，还被系统诊断：NER merge amplification（precision 0.563→0.210）、RE routing failure（73.4% 实例在 3-5 个 sub-schema 同时产生 positive prediction）。Oracle routing +29.8pp 证明理论上限存在，问题在 merge/routing 实现。\n\n**S4. [共识] Limitations section 极为详尽。** 8 项具体限制 + multiple comparisons 声明，覆盖 model coverage、effect size、factorial tests、metric scope、causal mechanism、data contamination。两位 Reviewer 均评价为同领域最佳之一。\n\n**S5. [共识] MAVEN centrality confound 的识别。** 发现 per-type BCS 在同源 schema 上与 centrality 混淆（raw positive correlation 控制 log frequency + degree centrality 后消失），提出 pairwise SCS 作为替代。这是一个有独立价值的方法论贡献，对后续使用 embedding similarity 做 schema 分析的工作有警示价值。\n\n**S6. [共识] 跨模型验证覆盖度好。** Dimension 1 在所有模型上复现（RE 斜率 -30.1pp vs -30.7pp，几乎一致），包括私有 API 模型 Gemini 2.5 Flash。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**[共识] W1. SCS 增量贡献有限 + \"We introduce\" 措辞有误导性**\n- Severity: R1 标 major, R2 标 critical; 交叉后 R1 上调至 major\n- 论文承认 SCS = LLM-PEE 的 partitioning criterion（§2 SCS novelty 段），但 §3.2 仍以 \"We introduce the Schema Confusability Score\" 开头，给读者造成指标新颖性的错误印象\n- 贡献实质是 analysis framework + 实验发现，而非新指标\n- 核心问题：如果 practitioner takeaway 仅为 \"RE schema 设计时检查 BCS，预期改善 3-5pp\"，这更接近 \"系统验证直觉\" 而非 \"发现新机制\"\n- R1 补充：centrality confound 发现、few-shot 不缓解 confusability gap (+4.3pp widening)、merge amplification 诊断是 non-obvious 贡献，部分缓解新颖性不足\n- **修改要求**：§3.2 改 \"We introduce\" → \"We operationalize\" 或 \"We adopt\"；更好地 frame 哪些发现是 counter-intuitive\n\n**[共识] W2. Dimension 2 效应量小，叙事过度强调 extreme-batch gap**\n- Severity: R1 major, R2 critical; 交叉后共识为 major\n- Typical-batch BCS gap 仅 2.2pp（95% CI: [0.4, 4.0]），pairwise r² = 1.3-1.7%。CI 下界 0.4pp 接近于零\n- 叙事频繁强调 extreme-batch gap（25-31pp），但这些来自人工构造的极端 batch\n- Abstract 层面的 framing 是诚实的（\"≈2.2pp in typical batches\"），但 Introduction/Results 的叙事节奏偏向极端值\n- BCS > 0.59 阈值缺乏 formal derivation（无 ROC/threshold sensitivity/precision-recall）\n- **修改要求**：(1) Introduction/Results 叙事中 extreme-batch 数字仅作对比锚点，typical gap 前置；(2) 补充 BCS threshold ROC/precision-recall 分析或删除具体阈值推荐\n\n**[共识] W3. NER batch-level null result 限制泛化性**\n- Severity: R1 major, R2 critical; 交叉后共识为 major\n- Batch-level BCS-F1 correlation 在 NER 为零（r = 0.004, p = 0.94, n = 450），使得 BCS 作为 pre-hoc screening tool 仅适用于 RE\n- 论文 Title/Abstract 包含 \"Information Extraction\"（跨任务），但 Dimension 2 batch-level 发现仅限 RE\n- Abstract 已诚实报告（\"but not in NER, where the signal is absent despite significant pairwise effects\"），但 Title 无 qualifier\n- MAVEN batch-level BCS 分析未报告（可能因 centrality confound 而回避，但应明确说明）\n- **修改要求**：(1) MAVEN batch-level 分析要么报告要么明确说明为何省略；(2) 考虑 Title 是否需要限定\n\n**[共识] W4. Logit-scale TOST 不一致，削弱 \"bounded association\" 核心 claim**\n- Severity: R1 major; R2 在交叉中 AGREE\n- Linear-scale TOST p = 0.003 通过，但 logit-scale（对 ~50% accuracy 更合适）交互项 marginally significant (p = 0.047)，TOST inconclusive (p = 0.209)\n- 论文将 logit-scale 结果放在 Appendix，选择 linear-scale 为 primary specification，可被视为 outcome-driven\n- Back-transformation argument（2.53-2.78pp 仍在 ±3pp margin 内）提供部分辩护\n- 两位 Reviewer 共识：不足以推翻核心 claim（back-transformed magnitude 仍远小于 count 主效应），但正文需更显著报告不一致\n- **修改要求**：§4.4 正文显著报告 logit-scale 结果；claim 弱化为 \"evidence for bounded association under primary linear specification; logit-scale inconclusive due to limited power\"\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**[共识] W5. Gemini 2.5 Flash 引用错误**\n- bib 条目 `gemini-team-2024` 指向 \"Gemini 1.5\"（arXiv:2403.05530），但论文实际使用 Gemini 2.5 Flash\n- 事实性错误，两位 Reviewer 一致确认\n- **修改要求**：替换为正确引用或标注 \"Gemini 2.5 Flash (Google, 2025)\"\n\n**[共识] W6. Conclusion 过短，缺 future work**\n- Severity: R2 major, R1 minor; 共识至少 should-fix\n- Conclusion 约 120-130 words，基本重复 Abstract 内容，缺 future work/broader implications/training-based IE 对比\n- §5 末尾有三个 future directions，但不够系统\n- **修改要求**：扩展至 2-3 段，含 future work + broader implications + training-based IE 对比\n\n**[共识] W7. Abstract 偏短，缺 motivation**\n- Severity: R2 major, R1 minor; 共识 should-fix\n- 实际约 115-140 words，低于 ARR 通常期望的 150-250 words\n- 缺少问题重要性 framing 和 cross-model generalization 提及\n- **修改要求**：补充 1-2 句 motivation + cross-model evidence，扩至 ~200 words\n\n**[共识] W8. Contribution 3 NER null result framing**\n- R2 标 critical (packaging null result), R1 REBUT (task-dependent diagnosis has value)\n- 交叉后部分共识：保留独立 contribution 但改措辞更 transparent\n- R1 建议措辞：\"We demonstrate that batch-level confusability prediction is task-dependent: effective for RE but absent in NER, and diagnose this asymmetry\"\n- **修改要求**：Contribution 3 改写，强调诊断性发现而非包装 null result\n\n**[共识] W9. Findings-contributions 映射不清**\n- Introduction 4 findings vs 4 contributions 映射关系非 1:1（Finding 3 \"cross-scale consistency\" 无对应 contribution）\n- **修改要求**：统一数量或在 contribution list 中标注对应 findings (§X)\n\n**[共识] W10. -ing participial phrases 残留**\n- 约 10-15 处 AI 写作痕迹（\"indicating...\", \"confirming...\", \"highlighting...\"）\n- **修改要求**：改写为独立句子\n\n---\n\n### Minor 问题（不影响接收）\n\n- MAVEN validation set 是否用于 hyperparameter 选择未声明\n- FewRel closed-set classification + constrained decoding 格式特殊性，泛化性不确定\n- 多重比较：prompt variant 8 tests 的 directional consistency 应显式报告 sign test p-value\n- Appendix N/P 残余因果语言 (\"count-driven\", \"BCS-driven\") 与 Limitations \"correlational evidence\" 不一致\n- DocRED count curve 在正文引用但 Appendix 未呈现\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成共识 [AGREE]：\n\n1. SCS 与 LLM-PEE 形式相同，\"We introduce\" 措辞有误导性\n2. Dimension 2 效应量小 (2.2pp typical)，叙事过度强调 extreme-batch gap\n3. NER batch-level null result 限制 \"跨 IE 任务\" 泛化性声称\n4. Gemini 2.5 Flash 引用错误（事实性问题）\n5. BCS > 0.59 阈值无 formal derivation\n6. Conclusion 过短，缺 future work\n7. Abstract 偏短，缺 motivation\n8. Findings-contributions 映射不清\n9. -ing phrases AI 写作痕迹残留\n10. 实验设计严谨度在该领域属上乘（最强共识点）\n11. Robustness checks 广度和深度堪称典范\n12. 负面结果诚实报告有社区价值\n13. MAVEN centrality confound 发现有方法论贡献\n\n---\n\n## Reviewer Divergence\n\n**分歧 1：Contribution 3 NER null result 的定性**\n- R2 [critical]：将 \"BCS 在 NER 上不 work\" 包装为 contribution，建议合并到 Contribution 2\n- R1 [REBUT]：task-dependent diagnosis（missed entity dominance + centrality confound 机制分析）超出简单 null result，值得独立 contribution，但同意措辞需更 transparent\n- 结果：部分收敛——保留独立 contribution 但改 framing\n\n**分歧 2：FewRel contamination 风险严重度**\n- R1 [major]：train-origin p=0.06 仅 suggestive，non-uniform contamination 未排除，DocRED 每 count 仅 5 batches\n- R2 [REBUT → minor]：反向差异 + covariate control ($\\Delta R^2 = 0.005$) + DocRED replication ($R^2 = 0.53$) 已充分\n- 结果：未收敛——记录分歧。Director 评估：论文的 contamination 分析在当前 NLP 标准下属充分，但确实无法 100% 排除 non-uniform contamination\n\n**分歧 3：Overall score**\n- R1: 3.5 (Borderline Conference)\n- R2: 3.0 (Findings)\n- 差异来源：Excitement (R1: 3/5, R2: 2.5/5)——R1 认为方法论示范价值 + centrality confound + few-shot widening gap 值 0.5 分区分\n\n---\n\n## Questions for Authors\n\n**Q1. [R1, AGREE by R2]** 能否报告 mixed-effects logistic regression 结果（accuracy as binomial outcome, count + BCS as fixed effects, batch as random effect）？这可解决 scale-dependence concern。\n\n**Q2. [R1]** Count 80（full FewRel schema）时 natural BCS variation 太小 (IQR = 0.033)，confusability 效应不可检测。这是否意味着 confusability 只在 schema 被人工 partition 时 matter？\n\n**Q3. [R2, AGREE by R1]** NER U-shape 能否通过 full-schema false positive 检查直接验证 \"type-filtering overhead\" 假设？\n\n**Q4. [R2]** Pairwise NER signal 存在 (r = 0.112) 但 batch-level 完全消失 (r ≈ 0)——是否存在 cancellation effect（confusable types 同时增加 IntraSub 和减少 missed rate）？Table 8 NER missed rates 的 non-monotonic pattern 部分支持此假设。\n\n**Q5. [R1, AGREE by R2]** Dimension 2 为何未在 Gemini 2.5 Flash 上测试？这将显著加强 cross-model generalization claim。\n\n**Q6. [R2]** BCS > 0.59 阈值如何推导？跨数据集 (FewRel vs DocRED) 是否一致？\n\n---\n\n## Missing References\n\n1. **[共识] Gemini 2.5 Flash 正确技术报告**（当前 `gemini-team-2024` 指向 Gemini 1.5）\n2. **[R1]** Structured prediction calibration 文献（与 constrained decoding + routing failure 分析相关）\n3. **[R2]** Embedding similarity for label confusion 文献（如 Prototypical Networks 的 confusion-with-distance 分析）\n4. **[R1]** Müller et al. 2019 (\"When Does Label Smoothing Help?\")、Peterson et al. 2019 (\"Human Uncertainty Makes Classification More Human\")\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目配置未启用 `external_review.paperreview_ai.enabled`）。\n\n---\n\n## Overall Assessment\n\n### 官方维度评分\n\n| 维度 | R1 | R2 | 加权评估 |\n|------|----|----|----------|\n| Soundness | 3.5/5 | 4.0/5 | 3.5/5 — 实验设计扎实但 logit-scale TOST inconsistency 是真实的方法论问题 |\n| Excitement | 3.0/5 | 2.5/5 | 2.5/5 — 核心发现 incremental (count > confusability 是 intuitive 的; SCS = LLM-PEE); 方法论示范价值存在但不足以弥补 |\n| Reproducibility | 4.0/5 | 4.5/5 | 4.0/5 — 代码承诺 release; 实验参数和 prompt templates 完整公开 |\n\n### Overall Score: **3.0 (Findings)**\n\n**一句话判断**: 一篇实验设计严谨、统计分析全面的 analysis paper，方法论示范价值突出（quasi-experimental BCS control + centrality confound 发现 + SDGD failure diagnosis），但 Dimension 2 confusability 效应量小（typical 2.2pp, CI 含 0.4pp）、SCS 指标非新颖（= LLM-PEE）、batch-level 信号仅对 RE 有效（NER 为 null），加上 logit-scale separability 不一致，整体贡献力度和泛化性更适合 Findings 而非主会议。\n\n**上调路径（3.0 → 3.5+ 可能的修改）：**\n1. 解决 logit-scale TOST concern（通过 mixed-effects logistic regression 或正文 prominently 报告 + claim 弱化）\n2. 提供 BCS threshold 的 formal analysis（ROC 或 precision-recall）\n3. 改善 SCS framing（\"We operationalize\" 而非 \"We introduce\"）\n4. Conclusion 扩展 + Abstract 扩充\n5. 修正 Gemini 引用\n6. 更好地 frame non-obvious findings（centrality confound, few-shot gap widening, merge amplification diagnosis）为核心贡献\n\n**Confidence: 4/5** — 基于两位 Reviewer 的仔细阅读（含所有 Appendix 和 references.bib），交叉回应中的共识和分歧分析。",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "schema-dag-extraction",
    "report": "# Round 13 Consolidated Review Report\n\n**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n**Venue**: EMNLP 2026 via ACL ARR May 2026 cycle\n**审稿模式**: 2 Reviewers × 1 Round + 交叉回应\n**Reviewer 分工**: R1 (方法严谨性 + 实验设计) / R2 (新颖性 + 写作完整性 + 格式合规)\n\n---\n\n## Summary\n\n本文对 training-free LLM IE 中 schema 复杂度如何预测性能退化进行了系统性的 controlled study。将退化分解为两个维度（type count 和 type confusability），提出 SCS/BCS 指标量化 confusability，在四个数据集（Few-NERD, FewRel, DocRED, MAVEN）和四个模型（Qwen3-32B, Llama-3.1-8B/70B, Gemini 2.5 Flash）上验证。论文同时报告了 schema decomposition (SDGD) 的负面结果及其失败诊断。这是一篇实验设计极为严谨的 analysis paper，方法论示范价值突出，但核心贡献受限于 SCS 与 LLM-PEE 指标形式相同、confusability 效应量小（typical 2.2pp）、且 batch-level 信号仅对 RE 有效。\n\n---\n\n## Strengths\n\n**S1. [共识] BCS-controlled quasi-experimental design 是本文最强的方法论贡献。** 固定 count 变化 BCS 的设计在 NLP 实证研究中罕见。FewRel balanced design 消除 type frequency 混淆；within-pool 分析控制 pool composition；TOST equivalence testing 形式化检验 bounded association。两位 Reviewer 一致认为该设计具有方法论示范价值。\n\n**S2. [共识] Robustness checks 的广度和深度在该领域论文中属于上乘水平。** 跨模型 (8B/32B/70B/Gemini)、跨 prompt variant (4 种)、跨数据集 (4 个)、BCS 聚合方式 (mean vs max)、SCS embedding ablation、cross-seed variance decomposition、logit-scale sensitivity。两位 Reviewer 均高度评价。\n\n**S3. [共识] 负面结果的诚实报告和系统诊断。** SDGD 失败不仅被报告，还被系统诊断：NER merge amplification（precision 0.563→0.210）、RE routing failure（73.4% 实例在 3-5 个 sub-schema 同时产生 positive prediction）。Oracle routing +29.8pp 证明理论上限存在，问题在 merge/routing 实现。\n\n**S4. [共识] Limitations section 极为详尽。** 8 项具体限制 + multiple comparisons 声明，覆盖 model coverage、effect size、factorial tests、metric scope、causal mechanism、data contamination。两位 Reviewer 均评价为同领域最佳之一。\n\n**S5. [共识] MAVEN centrality confound 的识别。** 发现 per-type BCS 在同源 schema 上与 centrality 混淆（raw positive correlation 控制 log frequency + degree centrality 后消失），提出 pairwise SCS 作为替代。这是一个有独立价值的方法论贡献，对后续使用 embedding similarity 做 schema 分析的工作有警示价值。\n\n**S6. [共识] 跨模型验证覆盖度好。** Dimension 1 在所有模型上复现（RE 斜率 -30.1pp vs -30.7pp，几乎一致），包括私有 API 模型 Gemini 2.5 Flash。\n\n---\n\n## Weaknesses\n\n### Must-Fix 问题（影响接收决定）\n\n**[共识] W1. SCS 增量贡献有限 + \"We introduce\" 措辞有误导性**\n- Severity: R1 标 major, R2 标 critical; 交叉后 R1 上调至 major\n- 论文承认 SCS = LLM-PEE 的 partitioning criterion（§2 SCS novelty 段），但 §3.2 仍以 \"We introduce the Schema Confusability Score\" 开头，给读者造成指标新颖性的错误印象\n- 贡献实质是 analysis framework + 实验发现，而非新指标\n- 核心问题：如果 practitioner takeaway 仅为 \"RE schema 设计时检查 BCS，预期改善 3-5pp\"，这更接近 \"系统验证直觉\" 而非 \"发现新机制\"\n- R1 补充：centrality confound 发现、few-shot 不缓解 confusability gap (+4.3pp widening)、merge amplification 诊断是 non-obvious 贡献，部分缓解新颖性不足\n- **修改要求**：§3.2 改 \"We introduce\" → \"We operationalize\" 或 \"We adopt\"；更好地 frame 哪些发现是 counter-intuitive\n\n**[共识] W2. Dimension 2 效应量小，叙事过度强调 extreme-batch gap**\n- Severity: R1 major, R2 critical; 交叉后共识为 major\n- Typical-batch BCS gap 仅 2.2pp（95% CI: [0.4, 4.0]），pairwise r² = 1.3-1.7%。CI 下界 0.4pp 接近于零\n- 叙事频繁强调 extreme-batch gap（25-31pp），但这些来自人工构造的极端 batch\n- Abstract 层面的 framing 是诚实的（\"≈2.2pp in typical batches\"），但 Introduction/Results 的叙事节奏偏向极端值\n- BCS > 0.59 阈值缺乏 formal derivation（无 ROC/threshold sensitivity/precision-recall）\n- **修改要求**：(1) Introduction/Results 叙事中 extreme-batch 数字仅作对比锚点，typical gap 前置；(2) 补充 BCS threshold ROC/precision-recall 分析或删除具体阈值推荐\n\n**[共识] W3. NER batch-level null result 限制泛化性**\n- Severity: R1 major, R2 critical; 交叉后共识为 major\n- Batch-level BCS-F1 correlation 在 NER 为零（r = 0.004, p = 0.94, n = 450），使得 BCS 作为 pre-hoc screening tool 仅适用于 RE\n- 论文 Title/Abstract 包含 \"Information Extraction\"（跨任务），但 Dimension 2 batch-level 发现仅限 RE\n- Abstract 已诚实报告（\"but not in NER, where the signal is absent despite significant pairwise effects\"），但 Title 无 qualifier\n- MAVEN batch-level BCS 分析未报告（可能因 centrality confound 而回避，但应明确说明）\n- **修改要求**：(1) MAVEN batch-level 分析要么报告要么明确说明为何省略；(2) 考虑 Title 是否需要限定\n\n**[共识] W4. Logit-scale TOST 不一致，削弱 \"bounded association\" 核心 claim**\n- Severity: R1 major; R2 在交叉中 AGREE\n- Linear-scale TOST p = 0.003 通过，但 logit-scale（对 ~50% accuracy 更合适）交互项 marginally significant (p = 0.047)，TOST inconclusive (p = 0.209)\n- 论文将 logit-scale 结果放在 Appendix，选择 linear-scale 为 primary specification，可被视为 outcome-driven\n- Back-transformation argument（2.53-2.78pp 仍在 ±3pp margin 内）提供部分辩护\n- 两位 Reviewer 共识：不足以推翻核心 claim（back-transformed magnitude 仍远小于 count 主效应），但正文需更显著报告不一致\n- **修改要求**：§4.4 正文显著报告 logit-scale 结果；claim 弱化为 \"evidence for bounded association under primary linear specification; logit-scale inconclusive due to limited power\"\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**[共识] W5. Gemini 2.5 Flash 引用错误**\n- bib 条目 `gemini-team-2024` 指向 \"Gemini 1.5\"（arXiv:2403.05530），但论文实际使用 Gemini 2.5 Flash\n- 事实性错误，两位 Reviewer 一致确认\n- **修改要求**：替换为正确引用或标注 \"Gemini 2.5 Flash (Google, 2025)\"\n\n**[共识] W6. Conclusion 过短，缺 future work**\n- Severity: R2 major, R1 minor; 共识至少 should-fix\n- Conclusion 约 120-130 words，基本重复 Abstract 内容，缺 future work/broader implications/training-based IE 对比\n- §5 末尾有三个 future directions，但不够系统\n- **修改要求**：扩展至 2-3 段，含 future work + broader implications + training-based IE 对比\n\n**[共识] W7. Abstract 偏短，缺 motivation**\n- Severity: R2 major, R1 minor; 共识 should-fix\n- 实际约 115-140 words，低于 ARR 通常期望的 150-250 words\n- 缺少问题重要性 framing 和 cross-model generalization 提及\n- **修改要求**：补充 1-2 句 motivation + cross-model evidence，扩至 ~200 words\n\n**[共识] W8. Contribution 3 NER null result framing**\n- R2 标 critical (packaging null result), R1 REBUT (task-dependent diagnosis has value)\n- 交叉后部分共识：保留独立 contribution 但改措辞更 transparent\n- R1 建议措辞：\"We demonstrate that batch-level confusability prediction is task-dependent: effective for RE but absent in NER, and diagnose this asymmetry\"\n- **修改要求**：Contribution 3 改写，强调诊断性发现而非包装 null result\n\n**[共识] W9. Findings-contributions 映射不清**\n- Introduction 4 findings vs 4 contributions 映射关系非 1:1（Finding 3 \"cross-scale consistency\" 无对应 contribution）\n- **修改要求**：统一数量或在 contribution list 中标注对应 findings (§X)\n\n**[共识] W10. -ing participial phrases 残留**\n- 约 10-15 处 AI 写作痕迹（\"indicating...\", \"confirming...\", \"highlighting...\"）\n- **修改要求**：改写为独立句子\n\n---\n\n### Minor 问题（不影响接收）\n\n- MAVEN validation set 是否用于 hyperparameter 选择未声明\n- FewRel closed-set classification + constrained decoding 格式特殊性，泛化性不确定\n- 多重比较：prompt variant 8 tests 的 directional consistency 应显式报告 sign test p-value\n- Appendix N/P 残余因果语言 (\"count-driven\", \"BCS-driven\") 与 Limitations \"correlational evidence\" 不一致\n- DocRED count curve 在正文引用但 Appendix 未呈现\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成共识 [AGREE]：\n\n1. SCS 与 LLM-PEE 形式相同，\"We introduce\" 措辞有误导性\n2. Dimension 2 效应量小 (2.2pp typical)，叙事过度强调 extreme-batch gap\n3. NER batch-level null result 限制 \"跨 IE 任务\" 泛化性声称\n4. Gemini 2.5 Flash 引用错误（事实性问题）\n5. BCS > 0.59 阈值无 formal derivation\n6. Conclusion 过短，缺 future work\n7. Abstract 偏短，缺 motivation\n8. Findings-contributions 映射不清\n9. -ing phrases AI 写作痕迹残留\n10. 实验设计严谨度在该领域属上乘（最强共识点）\n11. Robustness checks 广度和深度堪称典范\n12. 负面结果诚实报告有社区价值\n13. MAVEN centrality confound 发现有方法论贡献\n\n---\n\n## Reviewer Divergence\n\n**分歧 1：Contribution 3 NER null result 的定性**\n- R2 [critical]：将 \"BCS 在 NER 上不 work\" 包装为 contribution，建议合并到 Contribution 2\n- R1 [REBUT]：task-dependent diagnosis（missed entity dominance + centrality confound 机制分析）超出简单 null result，值得独立 contribution，但同意措辞需更 transparent\n- 结果：部分收敛——保留独立 contribution 但改 framing\n\n**分歧 2：FewRel contamination 风险严重度**\n- R1 [major]：train-origin p=0.06 仅 suggestive，non-uniform contamination 未排除，DocRED 每 count 仅 5 batches\n- R2 [REBUT → minor]：反向差异 + covariate control ($\\Delta R^2 = 0.005$) + DocRED replication ($R^2 = 0.53$) 已充分\n- 结果：未收敛——记录分歧。Director 评估：论文的 contamination 分析在当前 NLP 标准下属充分，但确实无法 100% 排除 non-uniform contamination\n\n**分歧 3：Overall score**\n- R1: 3.5 (Borderline Conference)\n- R2: 3.0 (Findings)\n- 差异来源：Excitement (R1: 3/5, R2: 2.5/5)——R1 认为方法论示范价值 + centrality confound + few-shot widening gap 值 0.5 分区分\n\n---\n\n## Questions for Authors\n\n**Q1. [R1, AGREE by R2]** 能否报告 mixed-effects logistic regression 结果（accuracy as binomial outcome, count + BCS as fixed effects, batch as random effect）？这可解决 scale-dependence concern。\n\n**Q2. [R1]** Count 80（full FewRel schema）时 natural BCS variation 太小 (IQR = 0.033)，confusability 效应不可检测。这是否意味着 confusability 只在 schema 被人工 partition 时 matter？\n\n**Q3. [R2, AGREE by R1]** NER U-shape 能否通过 full-schema false positive 检查直接验证 \"type-filtering overhead\" 假设？\n\n**Q4. [R2]** Pairwise NER signal 存在 (r = 0.112) 但 batch-level 完全消失 (r ≈ 0)——是否存在 cancellation effect（confusable types 同时增加 IntraSub 和减少 missed rate）？Table 8 NER missed rates 的 non-monotonic pattern 部分支持此假设。\n\n**Q5. [R1, AGREE by R2]** Dimension 2 为何未在 Gemini 2.5 Flash 上测试？这将显著加强 cross-model generalization claim。\n\n**Q6. [R2]** BCS > 0.59 阈值如何推导？跨数据集 (FewRel vs DocRED) 是否一致？\n\n---\n\n## Missing References\n\n1. **[共识] Gemini 2.5 Flash 正确技术报告**（当前 `gemini-team-2024` 指向 Gemini 1.5）\n2. **[R1]** Structured prediction calibration 文献（与 constrained decoding + routing failure 分析相关）\n3. **[R2]** Embedding similarity for label confusion 文献（如 Prototypical Networks 的 confusion-with-distance 分析）\n4. **[R1]** Müller et al. 2019 (\"When Does Label Smoothing Help?\")、Peterson et al. 2019 (\"Human Uncertainty Makes Classification More Human\")\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目配置未启用 `external_review.paperreview_ai.enabled`）。\n\n---\n\n## Overall Assessment\n\n### 官方维度评分\n\n| 维度 | R1 | R2 | 加权评估 |\n|------|----|----|----------|\n| Soundness | 3.5/5 | 4.0/5 | 3.5/5 — 实验设计扎实但 logit-scale TOST inconsistency 是真实的方法论问题 |\n| Excitement | 3.0/5 | 2.5/5 | 2.5/5 — 核心发现 incremental (count > confusability 是 intuitive 的; SCS = LLM-PEE); 方法论示范价值存在但不足以弥补 |\n| Reproducibility | 4.0/5 | 4.5/5 | 4.0/5 — 代码承诺 release; 实验参数和 prompt templates 完整公开 |\n\n### Overall Score: **3.0 (Findings)**\n\n**一句话判断**: 一篇实验设计严谨、统计分析全面的 analysis paper，方法论示范价值突出（quasi-experimental BCS control + centrality confound 发现 + SDGD failure diagnosis），但 Dimension 2 confusability 效应量小（typical 2.2pp, CI 含 0.4pp）、SCS 指标非新颖（= LLM-PEE）、batch-level 信号仅对 RE 有效（NER 为 null），加上 logit-scale separability 不一致，整体贡献力度和泛化性更适合 Findings 而非主会议。\n\n**上调路径（3.0 → 3.5+ 可能的修改）：**\n1. 解决 logit-scale TOST concern（通过 mixed-effects logistic regression 或正文 prominently 报告 + claim 弱化）\n2. 提供 BCS threshold 的 formal analysis（ROC 或 precision-recall）\n3. 改善 SCS framing（\"We operationalize\" 而非 \"We introduce\"）\n4. Conclusion 扩展 + Abstract 扩充\n5. 修正 Gemini 引用\n6. 更好地 frame non-obvious findings（centrality confound, few-shot gap widening, merge amplification diagnosis）为核心贡献\n\n**Confidence: 4/5** — 基于两位 Reviewer 的仔细阅读（含所有 Appendix 和 references.bib），交叉回应中的共识和分歧分析。",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0"
  }
}
```

</details>

---


### Tool result

_source line 1269 · 2026-05-18T03:14:48.434244+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_51326259fe46fbae9da26b81cf03f1f8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4518
}
```

</details>

---


### Tool call

_source line 1270 · 2026-05-18T03:15:01.135064+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性和搜索 EMNLP 2026 投稿要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重点'}, {'content': 'Step 0.6: 检查外部审稿配置', 'status': 'completed', 'activeForm': '检查外部审稿线配置'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '收集两位 Reviewer 独立审稿结果'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享审稿意见并收集回应'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '分析交叉回应，确认收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'completed', 'activeForm': '汇总审稿报告已投递至 Research Director'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性和搜索 EMNLP 2026 投稿要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 数量和侧重点'}, {'content': 'Step 0.6: 检查外部审稿配置', 'status': 'completed', 'activeForm': '检查外部审稿线配置'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '收集两位 Reviewer 独立审稿结果'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享审稿意见并收集回应'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '分析交叉回应，确认收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'completed', 'activeForm': '汇总审稿报告已投递至 Research Director'}]"
  }
}
```

</details>

---


### Tool result

_source line 1271 · 2026-05-18T03:15:01.135690+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 1272 · 2026-05-18T03:15:08.895259+00:00_

Round 13 审稿完成。

**审稿报告已投递至 Research Director。**

汇总：
- **Overall: 3.0 (Findings)**，R1=3.5 / R2=3.0
- **4 个 Must-Fix**：SCS "We introduce" 误导性 framing、Dim2 效应量小+叙事偏向极端值、NER batch-level null 限制泛化性、logit-scale TOST 不一致需正文报告
- **6 个 Should-Fix**：Gemini 引用错误、Conclusion 过短、Abstract 偏短、Contribution 3 null result framing、findings-contributions 映射、-ing phrases
- **上调路径**：解决 logit-scale concern + BCS threshold formal analysis + SCS framing + Conclusion/Abstract 扩展 + Gemini 引用修正后可达 3.5

Issue Tracker 已同步更新（`review_issues.yaml`），新增 8 个 open issues，1 个历史 issue 确认 resolved。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 123

## Round 123

2 recorded events


### User

_source line 1273 · 2026-05-18T03:15:10.404560+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

**核心共识点**：R1 和我在 SCS novelty 有限、effect size framing 偏差、NER null result 限制泛化、Gemini 引用错误这四个问题上高度一致。

**主要分歧**：
- FewRel contamination (R1-W4): 我认为论文的 existing analysis 已够充分，建议从 major 降为 minor
- Overall 评分: R1 给 3.5 (Borderline Conference)，我维持 3.0 (Findings)，差异在 excitement 判断——论文核心发现验证了直觉而非颠覆直觉，更适合 Findings track

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1274 · 2026-05-18T03:15:19.526406+00:00_

Round 13 审稿流程已完成。

**最终结果**：Overall 3.0 (Findings)

审稿报告已投递至 Research Director。Issue Tracker 已同步更新（13 个 open/in_progress issues）。

**核心判断**：实验设计严谨度在该领域属上乘（两位 Reviewer 最强共识），但 SCS 指标非新颖（= LLM-PEE）、confusability 效应量小（typical 2.2pp）、batch-level 信号仅对 RE 有效，整体更适合 Findings track。报告中列出了 6 项具体修改可推动评分至 3.5+。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 124

## Round 124

58 recorded events


### User

_source line 1275 · 2026-05-18T04:13:10.708447+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema-dag-extraction
- 论文路径: projects/schema-dag-extraction/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2025
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1276 · 2026-05-18T04:13:18.503528+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1277 · 2026-05-18T04:13:18.604985+00:00_

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
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1278 · 2026-05-18T04:13:23.129519+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1279 · 2026-05-18T04:13:23.385821+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 256
}
```

</details>

---


### Tool call

_source line 1280 · 2026-05-18T04:13:31.927216+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,request_external_review,get_external_review_status,read_project_file,submit_review_report_to_research_director,update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,request_external_review,get_external_review_status,read_project_file,submit_review_report_to_research_director,update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 1281 · 2026-05-18T04:13:31.978366+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1282 · 2026-05-18T04:13:36.619021+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 1283 · 2026-05-18T04:13:36.619367+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1284 · 2026-05-18T04:13:42.146661+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 1285 · 2026-05-18T04:13:43.201511+00:00_

{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (60 个)\n\n- **exp012_llama_8b_r2_exp2**: DONE (negative) — \n- **exp012_llama_8b_r2**: DONE (success) — \n- **exp006_interaction_2x2**: DONE (negative) — \n- **exp012_llama_awq**: DONE (killed) — \n- **exp012_llama_8b_r3**: DONE (failed) — \n- **exp012_llama_8b**: DONE (killed) — \n- **exp_fewrel_40rel_r3**: DONE (failed) — \n- **exp_fewrel_40rel_r2**: DONE (failed) — \n- **exp012_llama_fewnerd_r4**: DONE (failed) — \n- **exp012_llama_8b_fewnerd**: DONE (failed) — \n- **exp_fewrel_40rel**: DONE (failed) — \n- **exp012_llama_fewnerd_r3**: DONE (failed) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- prompt_sensitivity（准备中）\n- prompt_sensitivity_dry4（准备中）\n- prompt_sensitivity_dry3（准备中）\n- prompt_sensitivity_dry2（准备中）\n- prompt_sensitivity_dry（准备中）\n- exp_aggregation_monte_carlo（准备中）\n- exp_scs_name_def_ablation（准备中）\n- exp_fewrel_contamination_check（准备中）\n- exp017_gpt4o_mini_fewrel（准备中）\n- exp_cross_embedding_sensitivity（准备中）\n- …另有 2 项\n\n## 近期结论\n- **exp_gemini_flash_cross_model** (failed): The two-dimensional degradation pattern (count-related decline + confusability-related type confusion) generalizes beyond open-weight models to proprietary API models. Gemini 2.5 Flash should show: (1) monotonic RE accuracy decline with count, and (2) significant BCS-accuracy correlation on extreme batches. If confirmed, the pattern is architecture-family-independent (open-weight Qwen/LLaMA + proprietary Gemini).\n- **exp_schema_intervention** (negative): If type confusability is a causal driver of extraction errors, then renaming high-BCS type pairs to reduce embedding similarity (while preserving semantic equivalence) should improve accuracy on high-BCS batches. This tests the causal direction: SCS → confusion, not merely corre
…[truncated 1823 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 1286 · 2026-05-18T04:13:43.654454+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1287 · 2026-05-18T04:13:44.407973+00:00_

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
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B, 70B-Instruct (FP8), and Gemini 2.5 Flash (API). Dimension~1 (count-associated decline) has been validated on a proprietary model (Gemini 2.5 Flash, $\rho = -0.900$, $p = 0.037$; Appendix~\ref{sec:appendix_cross_model_gemini}); Dimension~2 (confusability-associated type substitution) has been verified only on open-weight models. Dimension~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
41	
42	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
43	
44	\item \textbf{Factorial interaction tests.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\ref{sec:appendix_factorial}). However, a FewRel factorial with TOST equivalence testing confirms bounded association ($p_{\text{TOST}} = 0.003$ at $\pm 3$\,pp, interaction = 0.47\,pp; Appendix~\ref{sec:appendix_factorial}), and cross-pool slope consistency ($p = 0.60$) corroborates stable rat
…[truncated 5181 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 1288 · 2026-05-18T04:13:44.408361+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2025 2026 submission guidelines author instructions page limit template"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2025 2026 submission guidelines author instructions page limit template"
  }
}
```

</details>

---


### Tool result

_source line 1289 · 2026-05-18T04:13:50.835743+00:00_

Web search results for query: "ACL Rolling Review ARR 2025 2026 submission guidelines author instructions page limit template"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, here are the key submission guidelines for ACL Rolling Review (ARR) for 2025-2026:

## Author Instructions and Requirements

All long, short, and theme papers must follow the ACL Author Guidelines.

Paper submissions must use the official ACL style template, which is available here. The submission must adhere to the formatting in the submiss
…[truncated 1058 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 6427
}
```

</details>

---


### Tool call

_source line 1290 · 2026-05-18T04:13:57.717578+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "100",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "100",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1291 · 2026-05-18T04:13:59.124119+00:00_

100	\label{tab:cross_model_bcs}
101	\end{table}
102	
103	\begin{table}[h]
104	\centering
105	\small
106	\resizebox{\columnwidth}{!}{%
107	\begin{tabular}{llrrrrrrr}
108	\toprule
109	 & & \multicolumn{5}{c}{\textbf{BCS Bin}} & & \\
110	\cmidrule(lr){3-7}
111	\textbf{Task} & \textbf{Error} & \textbf{Solo} & \textbf{Low} & \textbf{Mid} & \textbf{High} & \textbf{V.High} & \textbf{$\rho$} & \textbf{$p$} \\
112	\midrule
113	NER & IntraSub & 0\% & 1.6\% & 10.6\% & 49.4\% & --- & 1.000 & ${<}0.001$ \\
114	RE  & IntraSub & 0\% & 4.2\% & 13.0\% & 20.3\% & 32.3\% & 0.954 & ${<}\,0.001$ \\
115	\midrule
116	NER & Missed & --- & 42.8\% & 64.8\% & 49.9\% & --- & --- & --- \\
117	RE  & Missed & --- & 10.4\% & 11.3\% & 13.1\% & 15.7\% & --- & --- \\
118	\bottomrule
119	\end{tabular}}
120	\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}
121	\label{tab:error_taxonomy}
122	\end{table}
123	
124	\section{SDGD Full Protocol and Results}
125	\label{sec:appendix_sdgd}
126	
127	We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, the extreme case where each type is extracted in isolation.
128	
129	Single-pass extraction achieves F1\,=\,0.445 (P\,=\,0.563, R\,=\,0.368). SDGD obtains F1\,=\,0.251 (P\,=\,0.210, R\,=\,0.314), a 44\% relative drop. Random batching reache
…[truncated 16178 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool call

_source line 1292 · 2026-05-18T04:13:59.124515+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline ARR commitment"
  }
}
```

</details>

---


### Tool call

_source line 1293 · 2026-05-18T04:13:59.476113+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1294 · 2026-05-18T04:14:05.676008+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline ARR commitment"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"}]

Based on the search results, here is the key information about EMNLP 2026's call for papers submission deadline and ARR commitment:

## ARR Submission Deadline

The ARR submission 
…[truncated 1042 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 6551
}
```

</details>

---


### Tool result

_source line 1295 · 2026-05-18T04:14:05.676507+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'schema-dag-extraction'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6200
}
```

</details>

---


### Tool call

_source line 1296 · 2026-05-18T04:14:15.942713+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1297 · 2026-05-18T04:14:16.848656+00:00_

1	\begin{abstract}
2	As large language models are increasingly deployed for information extraction without task-specific training, understanding how schema design affects extraction quality becomes critical for reliable deployment. Training-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: having more types (count) and having semantically similar types (confusability). We present the first controlled study isolating these factors across NER, RE, and event detection on four datasets and operationalize confusability via the Schema Confusability Score (SCS) and its batch-level aggregation (BCS). Degradation operates along two dimensions: count-related recall decline (up to $-$49\,pp) dominates confusability-related type substitution (${\approx}\,2.2$\,pp in typical batches); BCS explains 22--53\% of cross-batch RE accuracy variance but not NER, where boundary detection failures overwhelm the signal. Few-shot demonstrations do not reduce the gap (+4.3\,pp under 5-shot). Schema decomposition fails due to merge amplification (NER) and routing failure (RE). These patterns replicate across model scales (8B to 70B) and architecture families (Qwen, LLaMA, Gemini), which suggests schema-induced degradation is a fundamental property of in-context learning rather than a model-specific artifact.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 1298 · 2026-05-18T04:14:16.899601+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1299 · 2026-05-18T04:14:17.357152+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance. Anonymous review materials: \url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 49.5\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accur
…[truncated 3254 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 457
}
```

</details>

---


### Tool call

_source line 1300 · 2026-05-18T04:14:17.458330+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "memory.md",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "memory.md",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1301 · 2026-05-18T04:14:17.509149+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/memory.md\", \"content\": \"# Memory — schema-dag-extraction\\n\\n## exp_schema_intervention: renaming 不是有效干预手段 (2026-05-17, negative)\\n- Renaming 降低两组 accuracy：high-BCS -8.83pp, low-BCS -2.96pp (both p<0.001)\\n- Interaction 显著 (-5.88pp, p<0.001)：high-BCS 受损更大，但方向是 renaming 损害而非改善\\n- 根因：LLM 对 original type names 有 strong prior，renaming 引入 label unfamiliarity confound\\n- Solo sanity check 11/12 通过，但 multi-type batch 中 compound effect 出现 (r=-0.625)\\n- **教训**：post-hoc renaming 无法分离 SCS 降低效果与 label unfamiliarity，不可用作因果干预\\n- D059 (Greedy auto-renaming) 基于相同逻辑，也已停止\\n\\n## TUM proxy 不是运行中的服务 (2026-05-17)\\n- TUM 是飞书 key 收集机制，不是 API proxy server\\n- localhost:8001 没有进程监听\\n- `tum_` 前缀的 token 不是有效的 Google/OpenAI API key\\n- 本机能直连 Google API（需要真实 Gemini key, 格式 AIza...）\\n- **教训**：API 实验前必须先验证 (a) proxy 是否运行 (b) key 格式是否匹配目标 API\\n\\n## Q3 held-out validation: FewRel val-origin SCS-confusion (2026-05-17, CORRECTED)\\n- 从 80-type confusion matrix 提取 16 val-origin types 的 C(16,2)=120 pairs\\n- 16 val types 与 64 train types PIDs 完全不重叠\\n- Val-only Spearman ρ = 0.216, p = 0.018 (显著)\\n- All-80 Spearman ρ = 0.218, p = 2.2e-35\\n- Val-only 与全集几乎一致，排除 training-set contamination\\n- Nonzero subset: val ρ = 0.600 (n=11, p=0.051), all-80 ρ = 0.128 (n=272, p=0.035)\\n- Top confused val pairs: child↔mother (500, SCS=0.84), child↔spouse (100, SCS=0.71), member of↔part of (100, SCS=0.90)\\n- 数据源: `/root/schema-dag-extraction/artifacts/q3_val_scs_confusion/q3_val_scs_confusion.json`\\n- **教训**: 第一个 Q3 worker 做错了（做了 SCS 分布对比而非 confusion correlation），第二个 worker 才做对\\n\\n## 跨模型 appendix 数据必须同 seed 同批次 (2026-05-17)\\n- d051 Qwen3 FewRel 有 3 seeds (s42/s123/s456)，每个 seed 不同的 960 samples 和 batch compositions\\n- 70B 只有 s42。论文 appendix 曾错用三 seed 平均值与 70B s42 并列\\n- **修正**: 统一用 s42 单 seed（确保同 samples 同 batches）\\n- 数据源: `artifacts/d051_fewrel_n25_s42/count_cur
…[truncated 2033 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1302 · 2026-05-18T04:14:21.733039+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1303 · 2026-05-18T04:14:22.687287+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025,willard2023efficient}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, and bidirectional encoders \cite{gliner-2024,gliner2-2025}. For RE, recent work examines zero-shot relation triplet extraction via prompting \cite{relationprompt-2022} and revisits relation extraction in the LLM era \cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. LLM-PEE's union merge suffers the same precision collapse (0.56$\to$0.21 in NER) that our \S\ref{sec:sdgd} analysis identifies as the fundamental bottleneck. Other approaches address schema complexity via hard negative mining \cite{iepile-2024}, schema definition optimization \cite{parse-2025}, multi-agent debate \cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \cite{dee-2024}, and active prompting 
…[truncated 3002 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1304 · 2026-05-18T04:14:22.687784+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 1305 · 2026-05-18T04:14:23.190470+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains and is suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\sim$10 per type) from the DocRED development set and formulate th
…[truncated 7852 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1306 · 2026-05-18T04:14:23.241381+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/schema-dag-extraction/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/schema-dag-extraction/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
  }
}
```

</details>

---


### Tool result

_source line 1307 · 2026-05-18T04:14:23.292265+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1308 · 2026-05-18T04:14:28.223257+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/schema-dag-extraction/**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/schema-dag-extraction/**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
  }
}
```

</details>

---


### Tool result

_source line 1309 · 2026-05-18T04:14:28.775936+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1310 · 2026-05-18T04:14:28.776364+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 1311 · 2026-05-18T04:14:28.877179+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	\begin{figure}[t]
10	\centering
11	\begin{minipage}[t]{0.48\columnwidth}
12	\centering
13	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
14	\end{minipage}
15	\hfill
16	\begin{minipage}[t]{0.48\columnwidth}
17	\centering
18	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
19	\end{minipage}
20	\caption{\textbf{(a)} Count-degradation curves for NER and RE. Error bars show $\pm 1$\,SD across 3 seeds (42, 123, 456) $\times$ 25 batches per seed. RE accuracy declines monotonically with count; NER recall exhibits a U-shaped pattern with minimum at intermediate counts. Full-schema points (rightmost, hollow markers) represent the complete type inventory with no batch sampling variance. \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}
21	\label{fig:main_results}
22	\end{figure}
23	
24	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}), ; schema configu
…[truncated 11014 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1312 · 2026-05-18T04:14:34.957739+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 1313 · 2026-05-18T04:14:34.958256+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention against confusability-related degradation is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches.
5	
6	\paragraph{NER: merge amplification.}
7	All decomposition modes fall below the single-pass NER baseline (F1\,=\,0.445): SDGD obtains 0.251, random batching 0.320, per-type 0.292 (Appendix~\ref{sec:appendix_sdgd}). The core failure is \emph{merge amplification}: presenting text to the model $k$ times with different type subsets is associated with precision collapsing (0.563$\to$0.210--0.249) as false positives scale with $k$, while true positives remain bounded. Confidence gating does not recover net F1. RE avoids this failure because closed-set classification requires no span reconciliation across passes.
8	
9	\paragraph{RE: oracle routing.}
10	Oracle routing achieves 0.802 accuracy versus 0.504 single-pass on FewRel 80-relation RE (+29.8\,pp; Table~\ref{tab:batch_composition}); type separation thus recovers performance absent merge amplification. Confusability-aware grouping yields only +1.4\,pp over random ($p \approx 0.19$, n.s.); all practical routing strategies fall below the single-pass baseline because constrained decoding forces confident predictions in every sub-schema (Appendix~\ref{sec:appendix_routing}).
11	
12	\paragraph{Future directions.}
13	Three avenues may address these bottlenecks: (1)~coarse-to-fine pipelines that screen with the full schema then refine with targeted sub-schemas; (2)~retrieval-based routing using document retrieval rather than LLM confidence for sub-schema assignment; (3)~calibrated generation \citep{jagannatha2020calibrating} to recover confidence signals eliminated by constrained decoding.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\re
…[truncated 535 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1314 · 2026-05-18T04:14:35.172420+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1315 · 2026-05-18T04:14:35.242092+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-dimensional decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). High-BCS accuracy converges to $\approx$51\% across models; at count 80, BCS is fixed and ceases to be a predictor. The effect generalizes to document-level RE (DocRED slope $-$0.71) and persists across prompt designs (Appendix~\ref{sec:appendix_prompt_sensitivity}). Dimension~1 replicates across scales (8B--70B); Dimension~2 attenuates on smaller models.
6	
7	\paragraph{Why does embedding similarity predict LLM confusion?}
8	SCS captures semantic proximity in LLMs' type-resolution space. The unconditional pairwise $R^2$ is modest (1.3\%) because ${\sim}89\%$ of type pairs never confuse; among the 11\% with nonzero confusion, conditional $R^2$ rises to 7\%. Correlated pair-level signals aggregate at batch level: a Monte Carlo simulation (Appendix~\ref{app:aggregation-sim}) predicts batch $R^2$ of 18--25\%, consistent with the observed 22--53\% in RE. SCS is thus a weak pair-level predictor but a useful batch-level screen. The NER U-shape (\S\ref{sec:count_curves}) likely reflects a dual-task burden absent in RE: partial schemas require simultaneous span detection and type-membership filtering; at full-schema, filtering becomes vacuous and recall recovers.
9	
10	\paragraph{Task-dependent batch-level effects.}
11	The batch-level BCS--performance relationship is RE-specific: BCS explains 22--53\% of cross-batch accuracy variance in RE but shows no correlation with NER F1 ($r \approx 0$, $n = 450$). RE errors are dominated by type substitution (IntraSub scales with BCS; \S\ref{sec:multi_channel}), so batch confusability directly predicts accuracy. NER errors are dominated by missed entities (43--65\%); the pairwise signal is diluted at batch level by boundary detection failures.
12	
13	\paragraph{Practical implications.}
14	The bound
…[truncated 1543 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 69
}
```

</details>

---


### Tool call

_source line 1316 · 2026-05-18T04:14:39.007729+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 1317 · 2026-05-18T04:14:39.460264+00:00_

1	\section*{Responsible NLP Research Checklist}
2	
3	For each question, the answer is \textbf{Yes}, \textbf{No}, or \textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.
4	
5	\subsection*{A \quad For Every Submission}
6	
7	\begin{enumerate}[label=\textbf{A\arabic*.},leftmargin=*,itemsep=4pt]
8	
9	\item \textbf{Did you describe the limitations of your work?}
10	
11	Yes. The Limitations section (after \S\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, factorial interaction tests with TOST equivalence, decomposition scope, and metric scope.
12	
13	\item \textbf{Did you discuss any potential risks of your work?}
14	
15	N/A. This is a purely analytical study of schema-induced degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
16	
17	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
18	
19	Yes. The abstract and \S\ref{sec:introduction} state the two-dimensional degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.
20	
21	\item \textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}
22	
23	Yes. We used Claude (Anthropic) for writing assistance and experimental code development. All scientific claims, experimental designs, and analyses were conducted by the authors.
24	
25	\end{enumerate}
26	
27	\subsection*{B \quad Scientific Artifacts}
28	
29	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=*,itemsep=4pt]
30	
31	\item \textbf{Did you cite the creators of artifacts you used?}
32	
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-70B-Instruct and Meta-Llama-3.1-8B-Instruct \cite{llama3
…[truncated 4519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1318 · 2026-05-18T04:14:39.762323+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/schema-dag-extraction/agent/project_config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/schema-dag-extraction/agent/project_config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
  }
}
```

</details>

---


### Tool result

_source line 1319 · 2026-05-18T04:14:39.813009+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1320 · 2026-05-18T04:14:43.930951+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/schema-dag-extraction/**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/schema-dag-extraction/**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects"
  }
}
```

</details>

---


### Tool result

_source line 1321 · 2026-05-18T04:14:43.981621+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/project
…[truncated 3357 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1322 · 2026-05-18T04:14:49.002865+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/constraints.yaml",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/constraints.yaml",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1323 · 2026-05-18T04:14:49.304663+00:00_

1	_next_id: 3
2	constraints:
3	- id: C001
4	  added: 2026-05-15 22:03 UTC
5	  summary: 论文中 count_40 子集必须明确说明 "40-rel subsets sampled from the 80-relation pool"，不能暗示是独立的
6	    40-type pool
7	  scope: all
8	  reason: count_40 实际是从 80-type pool 中采样的子集，不是独立构建的 pool。Reviewer 指出如果表述不清会误导读者认为存在三个独立
9	    pool size
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1324 · 2026-05-18T04:14:49.305073+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1325 · 2026-05-18T04:14:49.606939+00:00_

1	# Round 13 Review Issues Tracker
2	# Updated: 2026-05-18 (Round 13 Action Matrix dispatched, issues marked in_progress)
3	
4	# ============================================================
5	# CRITICAL — Must-Fix
6	# ============================================================
7	
8	- id: R3-C2
9	  summary: "'Empirically separable channels' 缺乏 formal 统计支撑 — TOST margin ±3pp > typical effect 2.2pp"
10	  category: framing
11	  severity: critical
12	  status: resolved
13	  first_raised_round: 3
14	  last_seen_round: 9
15	  mentions:
16	    - {round: 3, reviewers: [R1, R2], note: "因果语言过强"}
17	    - {round: 4, reviewers: [R1, R2], note: "Title 'Drive' + §4.3 暗示因果"}
18	    - {round: 5, reviewers: [R1, R2, R3], note: "三人共识改措辞"}
19	    - {round: 6, reviewers: [R1, R2, R3], note: "factorial p=0.50; 建议 'mechanistically distinguishable'"}
20	    - {round: 7, reviewers: [R1, R2], note: "三项 factorial 检验中两项失败"}
21	    - {round: 8, reviewers: [R1, R2], note: "R1-N1 critical: 3/4 tests 失败; 共识: 需限定"}
22	    - {round: 9, reviewers: [R1, R2, R3], note: "三人共识: TOST ±3pp margin 用 prompt variation 锚定不合逻辑; margin > typical main effect; ±1pp inconclusive"}
23	  action_items:
24	    - {round: 9, action: "D051: 'additive separability' → 'bounded interaction' 全文统一; SESOI effect-size anchored", assigned_to: agent, status: done}
25	  resolution: "D051 W1: 全文 'bounded interaction' 统一; SESOI effect-size anchored; sensitivity table in Appendix"
26	  resolution_round: 9
27	
28	- id: R10-N1
29	  summary: "因果语言 ('driven', 'channels', 'shape') 超出 observational/quasi-experimental 证据边界"
30	  category: framing
31	  severity: critical
32	  status: resolved
33	  first_raised_round: 10
34	  last_seen_round: 12
35	  mentions:
36	    - {round: 10, reviewers: [R1, R2], note: "R1 critical N3 + R2 AGREE with qualification; 共识: Title 'shape' 暗示因果"}
37	    - {round: 11, reviewers: [R1, R2], note: "R1 W4 + R2 AGREE: Title 'Shape' + Limitations 承认 no interventional causality = 不匹配"}
38	    - {round: 12, reviewers: [
…[truncated 26442 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1326 · 2026-05-18T04:14:57.102019+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1327 · 2026-05-18T04:14:57.559413+00:00_

&lt;persisted-output>
Output too large (39.7KB). Full output saved to: /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-director-338aa0a5/ca98d132-3c51-4056-b6ed-fb0798bedbbc/tool-results/toolu_01NQh4xC1wAudV73StKvn6Ms.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_9.md:112:状态：**skipped**（用户未在规定时间内提交至 paperreview.ai）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_8.md:179:项目配置 `external_review.paperreview_ai.enabled: false`。未请求外部审稿。
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_5.md:181:未配置（`external_review.paperreview_ai.enabled` not set in project config）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_13.md:190:外部审稿：未请求（项目配置未启用 `external_review.paperreview_ai.enabled`）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_12.md:144:外部审稿：未请求（项目配置未启用 `external_review.paperreview_ai.enabled`）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_6.md:140:项目配置 `external_review.paperreview_ai.enabled: false`。未请求外部审稿。
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_11.md:156:外部审稿：未配置（项目 config 中无 `external_review.paperreview_ai.enabled` 设置）。
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_4.md:161:项目配置 `external_review.paperreview_ai.enabled: false`。未请求外部审稿。
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_10.md:144:项目配置 `external_review.paperreview_ai.enabled: false`。未请求外部审稿。
/home/ubuntu/.age
…[truncated 334 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "elapsed_ms": 457
}
```

</details>

---


### Tool call

_source line 1328 · 2026-05-18T04:15:45.414436+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性）\n\n### Venue 信息\n- **目标**: EMNLP 2026 (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper, 8 页正文 + 无限参考文献/附录\n- **模板**: ACL 官方模板 (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n\n### 论文路径\n`projects/schema-dag-extraction/docs/paper/main.tex`（多文件结构：abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex, checklist.tex）\n\n### 你的审查侧重\n\n**方法严谨性**，重点关注：\n\n1. **实验设计充分性**: \n   - Count curves 和 BCS-controlled 两个实验范式的设计是否严谨\n   - 样本量是否足够支撑 claims（25 batches per condition, 1000 eval instances）\n   - 控制变量是否充分（count vs confusability 的隔离是否可信）\n\n2. **统计推断正确性**:\n   - TOST equivalence testing 的 margin 选择（±3pp）是否合理\n   - Linear-scale vs logit-scale TOST 不一致性（p=0.003 vs p=0.209）的处理\n   - Bootstrap CI、permutation tests 的使用是否恰当\n   - 多重比较问题的处理\n\n3. **效应量与 Claim 对齐**:\n   - Typical gap 2.2pp (CI [0.4, 4.0]) vs extreme-batch gap 25-31pp 的叙事平衡\n   - Pairwise r²=1.3-1.7% 的 practical significance\n   - \"BCS explains 22-53% of cross-batch RE accuracy variance\" 的解读是否过度\n\n4. **跨模型/跨数据集泛化性**:\n   - 主实验仅 Qwen3-32B，cross-model 验证（8B/70B/Gemini Flash）的深度\n   - NER batch-level null result 的处理\n   - FewRel closed-set classification + constrained decoding 的格式特殊性\n\n5. **数据完整性**:\n   - FewRel train+val 合并的 contamination 风险\n   - MAVEN validation set 使用声明\n   - Single-seed + greedy decoding 的非确定性声明\n\n### 评分标准 (EMNLP 2026 ARR)\n5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. Summary (2-3 句)\n2. Strengths (逐条, 标 [S1], [S2], ...)\n3. Weaknesses (逐条, 标 [W1], [W2], ..., 每条标 severity: critical/major/minor)\n4. Questions (标 [Q1], [Q2], ...)\n5. Missing References\n6. Overall Assessment (评分 + 置信度 1-5)\n7. Detailed Comments (逐节)",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性）\n\n### Venue 信息\n- **目标**: EMNLP 2026 (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper, 8 页正文 + 无限参考文献/附录\n- **模板**: ACL 官方模板 (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n\n### 论文路径\n`projects/schema-dag-extraction/docs/paper/main.tex`（多文件结构：abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex, checklist.tex）\n\n### 你的审查侧重\n\n**方法严谨性**，重点关注：\n\n1. **实验设计充分性**: \n   - Count curves 和 BCS-controlled 两个实验范式的设计是否严谨\n   - 样本量是否足够支撑 claims（25 batches per condition, 1000 eval instances）\n   - 控制变量是否充分（count vs confusability 的隔离是否可信）\n\n2. **统计推断正确性**:\n   - TOST equivalence testing 的 margin 选择（±3pp）是否合理\n   - Linear-scale vs logit-scale TOST 不一致性（p=0.003 vs p=0.209）的处理\n   - Bootstrap CI、permutation tests 的使用是否恰当\n   - 多重比较问题的处理\n\n3. **效应量与 Claim 对齐**:\n   - Typical gap 2.2pp (CI [0.4, 4.0]) vs extreme-batch gap 25-31pp 的叙事平衡\n   - Pairwise r²=1.3-1.7% 的 practical significance\n   - \"BCS explains 22-53% of cross-batch RE accuracy variance\" 的解读是否过度\n\n4. **跨模型/跨数据集泛化性**:\n   - 主实验仅 Qwen3-32B，cross-model 验证（8B/70B/Gemini Flash）的深度\n   - NER batch-level null result 的处理\n   - FewRel closed-set classification + constrained decoding 的格式特殊性\n\n5. **数据完整性**:\n   - FewRel train+val 合并的 contamination 风险\n   - MAVEN validation set 使用声明\n   - Single-seed + greedy decoding 的非确定性声明\n\n### 评分标准 (EMNLP 2026 ARR)\n5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. Summary (2-3 句)\n2. Strengths (逐条, 标 [S1], [S2], ...)\n3. Weaknesses (逐条, 标 [W1], [W2], ..., 每条标 severity: critical/major/minor)\n4. Questions (标 [Q1], [Q2], ...)\n5. Missing References\n6. Overall Assessment (评分 + 置信度 1-5)\n7. Detailed Comments (逐节)",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 1329 · 2026-05-18T04:15:59.909411+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 14494
}
```

</details>

---


### Tool call

_source line 1330 · 2026-05-18T04:15:59.961056+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性/完整性）\n\n### Venue 信息\n- **目标**: EMNLP 2026 (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper, 8 页正文 + 无限参考文献/附录\n- **模板**: ACL 官方模板 (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n\n### 论文路径\n`projects/schema-dag-extraction/docs/paper/main.tex`（多文件结构：abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex, checklist.tex）\n\n### 你的审查侧重\n\n**新颖性/完整性**，重点关注：\n\n1. **贡献增量评估**:\n   - SCS/BCS metric 与 LLM-PEE (2025) 的 partitioning criterion 形式相同，论文的增量贡献是什么\n   - \"First controlled study\" 声称的有效性\n   - 负面结果（SDGD failure）作为贡献是否充分\n   - NER batch-level null result 作为独立贡献（Contribution #3）的合理性\n\n2. **Related Work 完整性**:\n   - Schema complexity in IE 领域的覆盖是否充分\n   - 是否遗漏关键竞争方法或相关分析工作\n   - 引用密度是否达到 EMNLP 标准\n\n3. **写作质量**:\n   - Abstract 是否满足 150-250 words 且回答四个必答问题\n   - Introduction 故事线是否清晰连贯（问题→洞察→方法→验证）\n   - Findings 与 Contributions 数量/映射是否对齐\n   - AI 写作痕迹检查（em-dash、-ing phrases、过度分段、连续过渡词）\n   - 专有名词首次出现是否定义（TOST 等）\n\n4. **结构完整性**:\n   - Discussion 是否充分（不是 3 句 Conclusion）\n   - Limitations 覆盖是否全面\n   - Checklist 填写质量\n   - 因果语言 vs 实际证据等级的匹配\n\n5. **格式合规性**:\n   - 8 页正文限制\n   - 匿名化（无自引泄漏）\n   - 引用格式\n   - 图表质量和信息密度\n\n### 评分标准 (EMNLP 2026 ARR)\n5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. Summary (2-3 句)\n2. Strengths (逐条, 标 [S1], [S2], ...)\n3. Weaknesses (逐条, 标 [W1], [W2], ..., 每条标 severity: critical/major/minor)\n4. Questions (标 [Q1], [Q2], ...)\n5. Missing References\n6. Overall Assessment (评分 + 置信度 1-5)\n7. Detailed Comments (逐节)",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性/完整性）\n\n### Venue 信息\n- **目标**: EMNLP 2026 (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper, 8 页正文 + 无限参考文献/附录\n- **模板**: ACL 官方模板 (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n\n### 论文路径\n`projects/schema-dag-extraction/docs/paper/main.tex`（多文件结构：abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex, checklist.tex）\n\n### 你的审查侧重\n\n**新颖性/完整性**，重点关注：\n\n1. **贡献增量评估**:\n   - SCS/BCS metric 与 LLM-PEE (2025) 的 partitioning criterion 形式相同，论文的增量贡献是什么\n   - \"First controlled study\" 声称的有效性\n   - 负面结果（SDGD failure）作为贡献是否充分\n   - NER batch-level null result 作为独立贡献（Contribution #3）的合理性\n\n2. **Related Work 完整性**:\n   - Schema complexity in IE 领域的覆盖是否充分\n   - 是否遗漏关键竞争方法或相关分析工作\n   - 引用密度是否达到 EMNLP 标准\n\n3. **写作质量**:\n   - Abstract 是否满足 150-250 words 且回答四个必答问题\n   - Introduction 故事线是否清晰连贯（问题→洞察→方法→验证）\n   - Findings 与 Contributions 数量/映射是否对齐\n   - AI 写作痕迹检查（em-dash、-ing phrases、过度分段、连续过渡词）\n   - 专有名词首次出现是否定义（TOST 等）\n\n4. **结构完整性**:\n   - Discussion 是否充分（不是 3 句 Conclusion）\n   - Limitations 覆盖是否全面\n   - Checklist 填写质量\n   - 因果语言 vs 实际证据等级的匹配\n\n5. **格式合规性**:\n   - 8 页正文限制\n   - 匿名化（无自引泄漏）\n   - 引用格式\n   - 图表质量和信息密度\n\n### 评分标准 (EMNLP 2026 ARR)\n5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. Summary (2-3 句)\n2. Strengths (逐条, 标 [S1], [S2], ...)\n3. Weaknesses (逐条, 标 [W1], [W2], ..., 每条标 severity: critical/major/minor)\n4. Questions (标 [Q1], [Q2], ...)\n5. Missing References\n6. Overall Assessment (评分 + 置信度 1-5)\n7. Detailed Comments (逐节)",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 1331 · 2026-05-18T04:16:01.635354+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1674
}
```

</details>

---


### Assistant

_source line 1332 · 2026-05-18T04:16:06.539173+00:00_

Round 1 审稿任务已分配：
- **Reviewer 1** (方法严谨性): 实验设计、统计推断、效应量解读、跨模型泛化、数据完整性
- **Reviewer 2** (新颖性/完整性): 贡献增量、相关工作覆盖、写作质量、结构完整性、格式合规

等待两位 Reviewer 返回独立审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 125

## Round 125

2 recorded events


### User

_source line 1333 · 2026-05-18T04:22:32.967330+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 — Round 1 审稿意见（方法严谨性）

**论文**: "How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?"
**Venue**: EMNLP 2026 (ARR May 2026 cycle)

---

### Summary

本文将 training-free LLM 信息抽取的 schema 复杂度分解为两个维度：type count 和 type confusability（通过 SCS/BCS 量化），在 4 个数据集、3 个任务上进行了控制实验。主要发现包括：count 导致 recall 下降，confusability 导致 type substitution（RE 中 BCS 解释 22-53% batch-level variance），两者在 RE 中呈 bounded association，在 NER 中耦合；schema decomposition 因 merge amplification 和 routing failure 而失败。统计方法论在 NLP 论文中属于异常严谨的水平，但若干核心 claim 的统计支撑存在值得关注的问题。

---

### Strengths

**[S1] 实验设计精巧，隔离设计有方法论贡献。** BCS-controlled 实验通过固定 count、变化 BCS 来隔离 confusability 效应，是对 prior work（如 LLM-PEE）中 count 与 confusability 混淆的实质性改进。Within-pool 分析（从 80-relation pool 抽取 16-relation subsets）进一步控制了 pool composition confound，permutation test 验证 slope consistency（p=0.60）。这个设计范式对后续研究有参考价值。

**[S2] 负面结果诚实且有诊断深度。** SDGD 的失败结果（§6）不是简单报告"不 work"，而是诊断了 merge amplification 的具体机制（precision 从 0.563 降至 0.210），并区分了 NER（merge 问题）和 RE（routing 问题）的不同失败模式。Oracle routing 恢复 +29.8pp 的对比进一步精确定位了瓶颈。NER batch-level null result 也没有被掩盖，而是在 Discussion 中与 pairwise 结果的差异做了合理解释。

**[S3] 统计分析在 NLP 领域中异常全面。** 使用了 TOST equivalence testing、permutation tests、bootstrap CIs（pair-level B=10,000, batch-level B=1,000）、cluster bootstrap、Jonckheere-Terpstra trend test、variance decomposition、partial correlation 等方法。TOST margin justification 给出了 empirical/practical/statistical 三个锚点，并做了 ±1pp 到 ±5pp 的 sensitivity analysis。这种统计严谨度远超领域平均水平。

**[S4] 多层次 robustness checks 覆盖面广。** 包括 4 种 prompt variants（Appendix §K）、2 种 embedding models（MiniLM vs Qwen3）、BCS aggregation ablation（mean vs max，Appendix §I）、name-only vs name+definition SCS ablation（Appendix §G）、cross-seed variance decomposition（Appendix §L）、split-origin covariate analysis（Appendix §N）。每个 robustness check 都对准了一个具体的 potential confound。

**[S5] Limitations section 是我见过的 NLP 论文中最详尽的之一。** 8 条 limitations + 1 段 multiple comparisons 讨论，覆盖了 model coverage、effect size、factorial interaction、decomposition scope、evaluation metric、format specificity、causal mechanism、data contamination 等方面。这种自我审视的深度显示了作者的学术诚信。

---

### Weaknesses

**[W1] [critical] Linear-scale vs logit-scale TOST 不一致性动摇了核心 claim。**

- 具体位置：§5.4（Multi-Dimensional Degradation）, Appendix §C（Factorial Analysis）
- 问题：论文的核心 claim 之一是 count 和 confusability 两个维度在 RE 中呈"bounded association"（TOST p=0.003, ±3pp margin）。但 logit-scale TOST 不一致（p_TOST=0.209, inconclusive），论文将此归因为"limited power (n=69, wide CI)"。然而：
  - (a) 高 BCS batch 的 accuracy 集中在 ~51%（Table 5, Table 3），接近 50% 时 linear scale 系统性压缩 interaction effects。Logit scale 在此区间是更合适的分析尺度。
  - (b) 论文没有提供 formal power analysis 来支撑"limited power"的解释。对于 n=69 的样本量，如果 interaction effect 在 logit scale 上确实 bounded，应该可以计算检测 ±0.156 logit interaction 所需的 power。
  - (c) Logit-scale interaction 的 point estimate 是 0.111 logit units (p=0.047, marginally significant)，90% CI [0.019, 0.203]，CI 上界（0.203）超过了 equivalence bound（0.156）。这不是"power 不足"可以解释的；这是 CI 本身覆盖了"非等价"区域。
  - (d) 论文选择 linear-scale 作为 primary test，但没有给出 a priori justification（为什么 linear scale 比 logit scale 更合适作为 primary analysis）。这个选择本身似乎是 post-hoc 的。
- 为什么影响接收：如果 bounded association 不成立（即 count 和 confusability 存在交互作用），论文的"two-dimensional decomposition"框架的核心假设就被削弱——两个维度不再是独立的，而是 multiplicative 的。这不会完全推翻论文结论，但显著改变了 framing。
- 建议：(1) 提供 logit-scale TOST 的 power analysis；(2) 或者将 claim 弱化为"linear-scale bounded, logit-scale inconclusive"，并讨论两种尺度的 implications 差异；(3) 或者增加样本量至足以在 logit scale 上也达到 equivalence conclusion。

**[W2] [critical] "BCS explains 22-53% of cross-batch RE accuracy variance" 的 claim 范围过宽。**

- 具体位置：Abstract, §1 Introduction (Finding 2), §5.3 (Practical magnitude)
- 问题：
  - (a) 22% 来自 FewRel 100 个 random 16-type batches（§5.3），这是 well-powered 的估计。但 53% 来自 DocRED（§5.3, "scaling to 53% at DocRED 96-rel"），DocRED count-curve 实验仅用 5 batches per count level（§3.3），BCS-controlled 实验用 n=25 batches。论文没有讨论 DocRED 的 R²=0.53 是否受小样本 overfitting 影响——在 25 个观测值上回归一个 predictor，R²=0.53 的 adjusted R² 是多少？R² 的 bootstrap CI 是多少？
  - (b) 这个 claim 暗示 BCS 是 IE 性能的强预测因子，但 NER batch-level R²≈0（§5.3, r≈0, n=450）。Abstract 虽然提到了"but not NER"，但"22-53%"的区间仍然给人以 BCS 在 IE 领域普遍有效的印象。
  - (c) FewRel 的 R²=0.22 在 practical terms 上对应 typical-batch gap 仅 2.2pp (CI [0.4, 4.0])。22% 的 variance explained 听起来很大，但实际 accuracy difference 很小。
- 为什么影响接收：Abstract/Introduction 中的这个 claim 是审稿人判断 contribution 价值的关键数字。如果 53% 是不稳定的估计，或如果读者理解为 BCS 在 IE 领域广泛解释 22-53% variance（而实际仅限于 RE，且 NER 为 0），这将构成 overclaim。
- 建议：(1) 报告 DocRED R²=0.53 的 bootstrap CI 和 adjusted R²；(2) 在 Abstract 中更精确地表述为"RE accuracy variance"而不是暗示 IE 通用性；(3) 讨论 R²=0.22 对应 2.2pp typical gap 的 practical significance。

**[W3] [major] 跨模型验证深度不足以支撑"fundamental property of in-context learning"的 claim。**

- 具体位置：Abstract ("suggests schema-induced degradation is a fundamental property of in-context learning"), §5.3 (Cross-model validation), Appendix §O, §P
- 问题：
  - Dimension 1（count）: 在 Qwen3-32B, Llama-8B, Llama-70B, Gemini Flash 上验证。Gemini 的 count-64 是 partial data（13/25 batches）。这是可接受的覆盖度。
  - Dimension 2（confusability）: 仅在 Qwen3-32B 和 Llama-8B（RE only）、Llama-70B（FewRel count 16 only, 单个 count level）上验证。没有在 Gemini 上验证。NER 在 8B 上 Dimension 2 floor effects。
  - 没有任何 closed-source frontier model（GPT-4, Claude 等）的验证。
  - "fundamental property of in-context learning" 是一个非常强的 claim，需要 across architectures, scales, AND tasks 的系统性验证。当前证据只能支撑"consistent across tested open-weight models on RE"。
- 建议：将 claim 弱化为"consistent across tested model families"，或增加至少一个 closed-source model 的 Dimension 2 验证。

**[W4] [major] FewRel constrained decoding 的格式特殊性影响 confusability 效应的可推广性。**

- 具体位置：§3.4 (Model and Inference), Appendix §F (Prompt Templates), Limitations item 6
- 问题：FewRel 使用 constrained decoding（enum constraint 强制模型从候选 relation 中选择），这是一个 closed-set classification 设置。在这个设置下：
  - 模型必须从候选类型中选择一个，不能表达 uncertainty 或给出 schema 外的答案。
  - Constrained decoding 消除了 calibration signal（Appendix §F, Table 7: none-rate 仅 20-40%），这与 open-ended extraction 的行为可能非常不同。
  - 论文的 RE 结论——包括 BCS 解释 22-53% variance 的核心 claim——严重依赖这个特定设置。如果不使用 constrained decoding，模型可能通过输出 "none" 或 schema 外类型来避免 confusability-driven errors。
  - Limitations item 6 仅一句话提及这个问题，没有讨论 constrained decoding 如何与 confusability 效应交互。
- 建议：(1) 增加 unconstrained decoding 的对比实验（至少在一个 count level 上）；(2) 或者在论文正文中更显著地讨论这个边界条件——RE 结论的适用范围应限定为 closed-set classification with constrained decoding。

**[W5] [major] Few-NERD 使用 Qwen3 embedding 计算 SCS 引入 shared-representation dependency。**

- 具体位置：§3.2 (SCS), Limitations item 4
- 问题：Few-NERD 的 SCS 使用 extraction model 自身的 embeddings（Qwen3-32B），即用于预测的模型同时也是度量 confusability 的模型。这构成了 circular dependency：如果 Qwen3 的 embedding space 中两个类型相近，它们既会有高 SCS 又会被模型混淆，但这可能是同一个现象的两个表现，而非 SCS "预测"了混淆。
  - 论文提到 MiniLM cross-check 给出了"directionally consistent"的结果（r=0.172 vs r=0.138），且指出"independent MiniLM embedding yields a stronger SCS-confusion correlation"（§5.2），暗示 shared-representation bias 是 conservative 的。
  - 但 MiniLM 的 r=0.172 仅 marginally 高于 Qwen3 的 r=0.138，差异不显著。更重要的是，confusion matrix correlation = 0.894 表明两个 embedding space 的 SCS 高度一致——这也可能意味着两者都在 capture 同一个 artifact。
- 建议：这个问题在 Limitations 中已部分讨论，但论文可以更明确地说明 Few-NERD 的 SCS 分析是 exploratory/correlational 而非 predictive，或提供基于完全独立 embedding（如 GloVe 或 random embeddings 作为 null baseline）的消融。

**[W6] [minor] Variance decomposition 中 cross-seed 分析仅用 3 个 seeds。**

- 具体位置：§5.1 (Count Curves), Appendix §L (Cross-Seed Variance Decomposition)
- 问题：3 个 seeds（42, 123, 456）的 variance decomposition 在统计上非常有限。Appendix Table 11 中 count=16 的 seed SD (0.027) 与其他 count levels 不成比例地高（batch SD ratio 仅 5.4 vs 其他 levels 的 26-474），但论文没有讨论这个异常值。
- 建议：说明 3 seeds 的 limitation，或提供更多 seeds 的支持数据。

**[W7] [minor] DocRED 和 MAVEN 的 5 batches per count level 与 FewRel/Few-NERD 的 25 batches 不对称。**

- 具体位置：§3.3 (Experimental Design)
- 问题：5 batches 的 count-curve 实验 power 明显不足。虽然 DocRED 的 BCS-controlled 实验用了 25 batches（足够），但 count-curve 的 5 batches 使得 DocRED/MAVEN 的 trend analysis 可靠性降低。论文没有解释这个不对称的原因（计算成本？）。
- 建议：简要说明原因并讨论对结论的影响。

---

### Questions

**[Q1]** §5.3 中 DocRED R²=0.525 (count 16) 和 R²=0.53 的 adjusted R² 和 bootstrap CI 是多少？在 n=25 观测值上，R²=0.53 的稳定性如何？

**[Q2]** TOST ±3pp margin 的 justification 中提到 "3pp ≈ 0.5 × batch SD"，但 batch SD 在不同 count levels 上变化很大（Table 11: 从 0.025 到 0.089）。选择哪个 count level 的 SD 作为锚点？如果用 count=8 的 SD（0.082），3pp ≈ 0.37 × SD，远小于 Cohen's d=0.5。

**[Q3]** FewRel constrained decoding 下，模型是否有 "none" 选项？Prompt 中有 `"none"` in enum（Appendix §F），但 Table 7 报告 none-rate 仅 20-40%。如果大多数 sub-schema 都产生 positive prediction，这是否意味着 confusability 效应被 forced-choice 人为放大了？

**[Q4]** Pairwise SCS-confusion correlation 在 FewRel 上报告为 r=0.187（§3.2），但在 Table 2 中 FewRel 被排除，理由是"RE's per-instance format precludes direct comparison of confusion rates"。那 r=0.187 是如何计算的？与 Table 2 中 Few-NERD/MAVEN 的计算方法有何不同？

**[Q5]** NER U-shape（count 22-44 plateau 后 count 66 recovery 至 0.41）的解释是"full-schema 消除了 type-filtering overhead"，但为什么这个效应在 RE 中不存在（RE 呈单调下降）？RE 也使用 enum constraint 进行 type filtering，但没有 U-shape。这个不对称暗示 NER U-shape 可能有其他解释。

---

### Missing References

1. **Structured prediction calibration**: 论文讨论了 constrained decoding 消除 calibration signal（§6），但没有引用 calibration in structured prediction 的相关工作（如 Kuleshov & Liang 2015, "Calibrated Structured Prediction"）。
2. **Label space reduction**: 论文引用了 Haystack-to-Needle (2025)，但 label space 的 hierarchical reduction 在传统 multi-label 分类中有大量先驱工作（如 Bengio et al. 2010, "Label Embedding Trees"），可以进一步 contextualize。
3. **Schema complexity in knowledge graphs**: KG completion 中的 relation schema complexity 与本文高度相关（如 Bordes et al. 2013 的 relation cardinality 分析），但 Related Work 未涉及。

---

### Overall Assessment

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 方法论设计精巧、统计分析严谨、负面结果诚实，但核心 "bounded association" claim 的 scale-sensitivity 问题和跨任务/跨模型 generality 的 overclaim 需要修正。

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计和统计方法整体扎实（TOST、permutation tests、bootstrap CIs），但 TOST 的 linear/logit scale 不一致性和 DocRED R² 估计的稳定性未充分 addressed。不足以完全支撑所有核心 claims（bounded association 在 logit scale 不成立），但也没有 major flaws 使结论无效。 |
| Excitement | 3/5 | 分析性贡献（量化 schema 复杂度的两个维度）有方法论价值，但 practical impact 有限（typical-batch gap 仅 2.2pp），且负面结果（decomposition 失败）限制了 actionable takeaways。对理解 in-context learning 的 failure modes 有价值，但不足以显著改变现有实践。 |
| Reproducibility | 4/5 | 实验细节充分（vLLM v0.20.2, greedy decoding, seed 42, 具体 count levels, batch construction 方法），prompt templates 完整公开。但 code/data 尚未释出（承诺 upon acceptance）。 |
| Confidence | 4/5 | 我仔细阅读了论文并熟悉 zero-shot IE 和 equivalence testing 文献。对 TOST 分析和 experimental design 的评估有较高置信度。 |

## Must-Fix 问题（影响接收决定）

**N1** [critical] **TOST linear/logit scale 不一致性未充分解决**
- 具体位置：§5.4, Appendix §C
- 核心 claim "bounded association" 在 logit scale 上 inconclusive (p=0.209)。Logit scale 在 accuracy 接近 50% 时是更合适的分析尺度。论文将此归因于 "limited power" 但未提供 power analysis，且 logit-scale 90% CI 上界 (0.203) 超过 equivalence bound (0.156)。
- 建议：提供 power analysis、弱化 claim、或增加样本量。

**N2** [critical] **"22-53% variance explained" claim 中 53% 的稳定性和整体 framing 问题**
- 具体位置：Abstract, §1, §5.3
- DocRED R²=0.53 在 n=25 上可能不稳定（未报告 adjusted R² 和 CI）；NER batch-level R²≈0 但 Abstract 中的 framing 暗示 IE 通用性；22% 对应 typical gap 仅 2.2pp 但 presentation 暗示 strong predictive power。
- 建议：报告 DocRED R² 的 CI、限定 claim 为 "RE-specific"、讨论 practical significance。

## Should-Fix 问题（影响评分但不一票否决）

**W3** [major] 跨模型 generality claim 超出证据范围（Dimension 2 仅在 open-weight RE 上充分验证）
**W4** [major] FewRel constrained decoding 特殊性未在正文充分讨论（Limitations 仅一句话）
**W5** [major] Few-NERD SCS 的 shared-representation dependency 需要更 explicit 的 qualification

## 小问题（不影响接收）
- [W6] 3 seeds 的 variance decomposition 统计力度有限
- [W7] DocRED/MAVEN 5 batches vs FewRel/Few-NERD 25 batches 不对称未解释
- Abstract 中 "up to −49pp" 来自 DocRED document-level RE，但主实验以 FewRel 为主，存在 cherry-picking 最大数字的嫌疑

## 主要优势
- [S1] 实验设计精巧，count/confusability 隔离方法有方法论贡献
- [S2] 负面结果诚实且有深度诊断
- [S3] 统计分析在 NLP 领域中异常全面严谨
- [S4] 多层次 robustness checks 系统性覆盖 potential confounds
- [S5] Limitations section 详尽且体现学术诚信


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1334 · 2026-05-18T04:22:41.557273+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 126

## Round 126

2 recorded events


### User

_source line 1335 · 2026-05-18T04:22:47.750434+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

审稿结论：**Overall 3.5 (Borderline Conference)**。

核心发现：
- 论文方法论设计精巧，统计分析在 NLP 领域中少见地严谨，负面结果诚实
- **2 个 critical 问题**：(1) TOST equivalence claim 在 logit scale 上不成立（p=0.209），而 logit scale 在 accuracy 接近 50% 时是更合适的分析尺度，论文缺乏 power analysis 来支撑"power 不足"的解释；(2) "BCS explains 22-53% variance" 中 53% 的 DocRED 估计稳定性存疑，且 NER batch-level R²=0 使得 IE 通用性 framing 不成立
- **3 个 major 问题**：跨模型 generality claim 超出证据范围、FewRel constrained decoding 特殊性讨论不足、Few-NERD shared-representation dependency

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1336 · 2026-05-18T04:22:53.845166+00:00_

Reviewer 1 意见已收到。等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 127

## Round 127

6 recorded events


### User

_source line 1337 · 2026-05-18T04:23:58.432231+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见（新颖性/完整性）

**论文**: "How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?"

---

### 1. Summary

本文研究 training-free LLM 信息抽取中 schema 复杂度对性能的影响，将退化分解为两个维度：type count（数量）和 confusability（语义相似度）。通过 SCS/BCS 指标量化 confusability，在 NER、RE、ED 三个任务四个数据集上进行受控实验。主要发现：count 主导 recall 下降（最高 −49pp），confusability 驱动的类型替换效应较小（~2.2pp）；BCS 在 RE 上解释 22-53% 跨 batch 精度方差，但在 NER 上无 batch 级信号；schema 分解（SDGD）因 merge amplification 和 routing failure 而失败。

---

### 2. Strengths

**[S1] 实验设计严谨**：受控实验方法论是本文最大亮点。通过固定 type count 变化 BCS（Experiment 2）和反过来固定 BCS 变化 count（Experiment 1）的 factorial design，有效隔离了两个维度的效应。TOST 等价检验、permutation tests、bootstrap CI 等统计工具的使用也超过了该领域的一般水准。

**[S2] 全面的 Limitations 讨论**：Limitations section 列出 8 项具体局限（page 9），包括单模型依赖、pairwise 效应量小、MAVEN centrality confound、因果推断限制等，诚实程度在 NLP 论文中少见。

**[S3] 跨任务对比揭示的任务不对称性**：NER 和 RE 对 confusability 的响应模式截然不同（RE 有 batch 级信号，NER 没有）这一发现具有一定洞察价值，boundary detection failure 的解释也有说服力（Section 4.4, Figure 2）。

**[S4] 负面结果的报告**：SDGD schema 分解失败的报告（Section 5）是对社区的有价值贡献，尤其是 merge amplification 和 routing failure 两个失败模式的诊断。

**[S5] 可复现性高**：实验细节充分（模型版本、prompt 模板、数据集构建细节全部公开），Checklist 填写认真。

---

### 3. Weaknesses

**[W1] [major] SCS/BCS 指标新颖性不足，与 LLM-PEE 的差异化不清晰**

论文自身承认 "SCS shares its formal definition (pairwise cosine similarity of type name embeddings) with the partitioning criterion used in LLM-PEE" (Section 2, page 3)。SCS 本质上就是 type name embedding 的 pairwise cosine similarity，这是一个非常标准的操作。虽然论文声称贡献在于"controlled experimental framework"而非 metric 本身，但 Abstract 和 Contribution #1-2 均以 SCS/BCS 作为核心卖点（"operationalize confusability via the Schema Confusability Score"）。这造成了宣传与实际的错位：如果 metric 不是贡献，就不应在 Abstract 中如此突出地呈现它；如果它是贡献，需要更清楚地说明相对于 LLM-PEE pairwise similarity 的增量。

目前的增量论证（"the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation, distinguishing it from the engineering use in prior work"）偏弱——因为 LLM-PEE 的 partitioning 正是基于相同原理（高相似度类型分开放）来改善抽取效果的，只是实验验证的深度不同。

**[W2] [major] Confusability 效应量过小，实际意义存疑**

核心发现之一是 confusability 驱动的类型替换效应仅 ~2.2pp（典型 batch）。即使在 extreme-batch 对比中，BCS gap 也仅 ~25pp（FewRel RE，Table 13 in appendix）。与此同时，count 效应高达 −49pp。论文将大量篇幅（SCS 定义、BCS aggregation、pairwise correlation 分析、TOST 检验）用于分析一个 ~2pp 的效应。虽然统计显著性存在（p < 0.001），但在实际应用中，这个效应量是否值得 practitioners 关注？论文 Discussion 中的 "Practical implications" (page 8) 称 "type pairs in the upper SCS quartile are associated with 3-5 pp accuracy differences"，但这只是关联，不是因果。

这引出一个更根本的问题：如果 confusability 效应如此之小，整个双维度框架的实际价值在哪里？论文需要更有力地论证为什么 2pp 的效应值得一篇完整的长论文来分析。

**[W3] [major] 因果语言与证据等级不匹配**

Abstract 和正文大量使用因果性语言——"schema-induced degradation" (title/abstract/conclusion), "count-related recall decline", "confusability-related type substitution", "BCS explains 22-53% of variance"。但实际证据是 correlational + controlled stratification，不是 interventional。Limitations #7 (page 9) 承认 "controlled stratification provides evidence consistent with a directional relationship but does not establish interventional causality"，但这一关键 caveat 只出现在 Limitations 中，没有反映到 Abstract 或 Introduction 的措辞中。

建议：正文用 "associated with" 替代 "explains"；title 中 "predict" 是合适的，但 "schema-induced" 应改为 "schema-associated" 或明确说是 predictive relationship。

**[W4] [major] SDGD 负面结果分析深度不足**

Section 5 作为 Contribution #4 仅占约 1 column 正文 + Table 3。NER 的 merge amplification 和 RE 的 routing failure 是两个有趣的发现，但分析停留在表面描述层。具体不足：
- merge amplification 的机制描述很简短（"the same text is presented to the model k times with different type subsets"），没有定量分析 k 值与 amplification 程度的关系
- routing failure 仅报告了 oracle routing 的上界（Table 3），没有分析失败案例
- "Future directions" 列出 3 个方向但均未验证
- 对一个 claimed contribution，这个深度不够——要么删除作为独立贡献，要么补充更深入的分析

**[W5] [minor] NER batch-level null result 作为独立 Contribution (#3) 的合理性**

Contribution #3 ("Discover a task asymmetry: BCS explains 22-53% of RE accuracy variance through type substitution, yet shows no batch-level signal in NER despite significant pairwise effects") 本质上是主实验的一个 sub-finding，不是一个方法论或框架层面的独立贡献。将其升级为 numbered contribution 有膨胀之嫌。建议将其并入 Contribution #2 的发现描述中。

**[W6] [minor] MAVEN 数据集的 centrality confound 削弱了广度声称**

论文声称覆盖 "four datasets"，但 MAVEN 因 centrality confound (Section 4.5, page 7; Appendix E) 被单独报告，不参与主分析框架。这意味着核心发现实际上只在 Few-NERD (NER) + FewRel (RE) + DocRED (RE) 三个数据集上成立。对于一个以"受控实验"为核心卖点的论文，数据覆盖面相对有限。

**[W7] [minor] "First controlled study" 声称需要更谨慎的限定**

"To our knowledge, we present the first controlled study isolating type confusability from type count" (Introduction, page 2)。虽然我未找到直接矛盾的先行工作，但：
- LLM-PEE (2025) 通过 partitioning 已隐式研究了 confusability 对抽取的影响
- PARSE (Shrimal et al., 2025) 的 schema optimization 也涉及 confusability 管理
- "First" 声称在 review 中容易引发审稿人反感，建议改为 "a systematic controlled study" 或加更强的 qualifying language

**[W8] [minor] Cross-model validation 规模有限**

主实验用 Qwen3-32B，验证模型仅 LLaMA-3.1-70B-Instruct 和 LLaMA-3.1-8B-Instruct (+ Gemini 2.5 Flash API)。声称 "architecture families" 多样性（Qwen, LLaMA, Gemini），但实际只有 3 个 family，且 Gemini 仅做了 proprietary model 验证（Appendix R），不在主分析中。

---

### 4. Questions

**[Q1]** SCS 使用 name-only embedding（Table 15, Appendix L: "name+definition" 没有系统性改善）。但 type confusion 直觉上应该更依赖 definition 语义而非 name 表面形式。为什么 definition embedding 没有帮助？这是否说明 SCS 捕获的是 name-level 的表面相似度而非深层语义 confusability？

**[Q2]** BCS 在 RE 上有 22-53% explanatory power，在 NER 上为 null。论文将此归因于 "boundary detection failures overwhelm the signal" (Abstract)。但是否有可能 BCS 本身作为 metric 就不适用于 NER（因为 NER 的 error mode 根本不同），而不是说 confusability 在 NER 中不存在？如果是后者，SCS/BCS framework 的 generality 声称需要大幅修改。

**[Q3]** Experiment 2（BCS-Controlled）中 low-BCS 和 high-BCS batch 的构建方法是什么？如何保证 low-BCS batch 中的 types 不是 trivially easy（如 Person vs Organization vs Location），而 high-BCS batch 中的 types 不是 trivially hard（如 Person vs Character vs Individual）？batch 构建是否控制了 type difficulty 之外的其他因素？

**[Q4]** Table 3 (Section 5) 中 oracle routing 在 RE 上达到 0.802 accuracy vs single-pass baseline 0.504。但论文称 "all practical routing strategies fall below the single-pass baseline"——这意味着实际 routing 比不 decompose 还差。这是否说明 SDGD 框架本身就不适用于 RE，而不仅仅是 routing 需要改进？

**[Q5]** Abstract 中 "Few-shot demonstrations do not reduce the gap (+4.3pp under 5-shot)" 的 "gap" 指什么 gap？是 count-degradation gap 还是 confusability gap？这句话在 Abstract 中出现时缺少上下文。

---

### 5. Missing References

1. **GoLLIE** (Sainz et al., ICLR 2024): Annotation guidelines improve zero-shot information extraction。这是 schema-aware IE 的重要 baseline，论文未引用。
2. **Schema as Parameterized Tools for Universal IE** (2025): 将 schema 参数化为工具的框架，与本文 schema complexity 讨论直接相关。
3. 论文引用数量（~60 unique cited keys）在 EMNLP 长论文中偏低但可接受。引用覆盖了主要 baseline 和数据集论文。

---

### 6. Overall Assessment

**Overall**: 3.0 (Findings)

**Soundness**: 3.5/5 — 实验方法论扎实，统计工具使用恰当，但因果语言超出证据水平，confusability 效应量很小。

**Excitement**: 2.5/5 — 问题重要且时机合适，但核心发现 "count 远比 confusability 重要" 某种程度上是预期之内的；confusability 维度的效应太小（~2pp），难以令人兴奋；SDGD 负面结果有价值但分析不够深入。

**Reproducibility**: 4/5 — 实验细节充分，prompt templates 完整，承诺代码开源。

**Confidence**: 4/5 — 熟悉 LLM-based IE 和 schema complexity 文献，仔细阅读了全文及附录。

**理由**：本文的实验设计严谨程度在 NLP empirical study 中属于上乘，统计分析方法值得肯定。然而，新颖性受限（SCS 本质上是标准 cosine similarity；核心发现——count 主导退化——在直觉上可预期），confusability 效应过小（~2pp），SDGD 分析深度不足以支撑独立贡献声称，且因果语言与实际证据等级存在错位。作为 Findings 论文是合适的——方法论扎实，发现有参考价值——但 excitement 和 novelty 不足以支撑主会议接收。

---

### 7. Detailed Comments by Section

**Abstract**: 约 170 words，在 150-250 范围内。四个必答问题基本回答，但 "为什么重要" 只有半句话（"becomes critical for reliable deployment"），可以更有力。"Few-shot demonstrations do not reduce the gap" 中 "the gap" 指代不明（见 Q5）。

**Introduction**: 故事线清晰（问题→现状不足→本文方法→发现→贡献），但贡献列表 4 条偏多，建议合并 #2/#3 为一条、#4 降级为 additional finding。Introduction 中 "first controlled study" 声称的 hedging（"to our knowledge"）恰当但仍有风险。

**Related Work**: 分类合理（Training-free LLM IE / Schema complexity / SCS novelty / Embedding anisotropy），但 "SCS novelty" 小节更像 contribution positioning 而非 related work survey。缺少 GoLLIE 引用。引用密度勉强可接受。

**Experimental Setup (Section 3)**: 最扎实的部分。数据集选择有理有据，SCS/BCS 定义清晰，两个互补实验设计（count curves + BCS-controlled）巧妙。Table 1 信息密度高。

**Results (Section 4)**: 实验结果呈现系统全面。Figure 1 的 degradation curves 直观有效。Table 2 的 pairwise correlation 较弱（r = 0.11-0.19）但论文诚实报告并解释了 batch-level amplification 机制。Section 4.3 (BCS-Controlled) 是核心证据，设计合理。Section 4.5 (MAVEN confound) 的处理是诚实的但削弱了广度声称。

**SDGD Section (Section 5)**: 篇幅过短，分析不够深入（见 W4）。

**Discussion (Section 6)**: Boundary conditions 讨论有价值。"Why does embedding similarity predict LLM confusion?" 段落提供了合理的机制解释。Practical implications 段落太短（2 句话），需要扩展。

**Conclusion (Section 7)**: 简洁准确地总结了发现，future work 方向合理。

**格式合规性**: ✓ 8 页正文；✓ "Anonymous ACL submission"；✓ 行号开启；✓ 引用格式正确；✓ 无明显匿名化违规。

**AI 写作痕迹**: 几乎无 em-dash/en-dash；无 "Furthermore/Moreover/Additionally" 过度使用；无 -ing phrase 结尾模式；段落长度自然。写作质量在 AI 辅助论文中属于上乘。

**引用验证**: 65 条 bib entry，60 条被引用，5 条 orphan（未引用）。4 条 online not found（gemini-2025, dror-2018-significance, sclar-sensitivity-2024, li2023evaluating），均为已知论文但 OpenAlex 匹配失败，非虚假引用。9 条 mismatch 均为 minor（作者排序/大小写/年份偏差）。无虚假引用问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1338 · 2026-05-18T04:24:36.099825+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2（新颖性/完整性）的完整审稿意见。请逐条回应：**[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 2 的审稿意见\n\n**Overall**: 3.0 (Findings)\n\n**Strengths**:\n[S1] 实验设计严谨：受控实验方法论是最大亮点\n[S2] 全面的 Limitations 讨论\n[S3] 跨任务对比揭示的任务不对称性有洞察价值\n[S4] 负面结果的报告有价值\n[S5] 可复现性高\n\n**Weaknesses**:\n\n**[W1] [major] SCS/BCS 指标新颖性不足，与 LLM-PEE 的差异化不清晰**\n- SCS 本质上就是 type name embedding 的 pairwise cosine similarity，非常标准\n- Abstract/Contribution #1-2 以 SCS/BCS 为核心卖点，但 Related Work 承认与 LLM-PEE 形式相同\n- 增量论证偏弱：LLM-PEE 的 partitioning 基于相同原理，只是实验验证深度不同\n\n**[W2] [major] Confusability 效应量过小，实际意义存疑**\n- 典型 batch gap 仅 ~2.2pp，extreme-batch 对比 ~25pp\n- Count 效应高达 −49pp，相比之下 confusability 效应极小\n- 论文用大量篇幅分析 ~2pp 效应，practical significance 不足\n- \"Practical implications\" 段仅声称 3-5pp 关联，不是因果\n\n**[W3] [major] 因果语言与证据等级不匹配**\n- \"schema-induced degradation\"、\"count-related recall decline\"、\"BCS explains 22-53%\"\n- 实际证据是 correlational + controlled stratification，非 interventional\n- Limitations #7 承认 no interventional causality，但 Abstract/Introduction 未反映\n- 建议 \"associated with\" 替代 \"explains\"；\"schema-induced\" → \"schema-associated\"\n\n**[W4] [major] SDGD 负面结果分析深度不足**\n- Section 5 仅约 1 column 正文 + Table 3\n- merge amplification 机制描述简短，无 k 值与 amplification 定量分析\n- routing failure 仅报告 oracle 上界，无失败案例分析\n- Future directions 均未验证\n- 作为 claimed contribution 深度不够\n\n**[W5] [minor] NER batch-level null result 作为独立 Contribution (#3) 有膨胀之嫌**\n- 本质是主实验 sub-finding，不是方法论或框架层面的独立贡献\n- 建议并入 Contribution #2\n\n**[W6] [minor] MAVEN centrality confound 削弱广度声称**\n- MAVEN 不参与主分析框架，核心发现实际只在 3 个数据集成立\n\n**[W7] [minor] \"First controlled study\" 声称需要更谨慎限定**\n- LLM-PEE 和 PARSE 隐式涉及 confusability 影响\n- \"First\" 声称容易引发反感\n\n**[W8] [minor] Cross-model validation 规模有限**\n- 仅 3 个 architecture family，Gemini 不在主分析中\n\n**Questions**:\n[Q1] Name-only vs name+definition SCS: 为什么 definition embedding 没帮助？是否说明 SCS 捕获的是 name-level 表面相似度？\n[Q2] BCS 在 NER 上为 null 是否说明 BCS 本身不适用于 NER（因 error mode 根本不同），而非 confusability 在 NER 中不存在？\n[Q3] BCS-Controlled batch 构建如何保证不是 trivially easy vs trivially hard 的对比？\n[Q4] Oracle routing 在 RE 上恢复 +29.8pp 但 practical routing 全部低于 single-pass——这是否说明 SDGD 本身不适用于 RE？\n[Q5] Abstract 中 \"Few-shot demonstrations do not reduce the gap\" 的 \"the gap\" 指代不明。\n\n**Missing References**: GoLLIE (Sainz et al., ICLR 2024); Schema as Parameterized Tools for Universal IE (2025)\n\n---\n\n请逐条给出你的 [AGREE] 或 [REBUT] 回应。",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2（新颖性/完整性）的完整审稿意见。请逐条回应：**[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 2 的审稿意见\n\n**Overall**: 3.0 (Findings)\n\n**Strengths**:\n[S1] 实验设计严谨：受控实验方法论是最大亮点\n[S2] 全面的 Limitations 讨论\n[S3] 跨任务对比揭示的任务不对称性有洞察价值\n[S4] 负面结果的报告有价值\n[S5] 可复现性高\n\n**Weaknesses**:\n\n**[W1] [major] SCS/BCS 指标新颖性不足，与 LLM-PEE 的差异化不清晰**\n- SCS 本质上就是 type name embedding 的 pairwise cosine similarity，非常标准\n- Abstract/Contribution #1-2 以 SCS/BCS 为核心卖点，但 Related Work 承认与 LLM-PEE 形式相同\n- 增量论证偏弱：LLM-PEE 的 partitioning 基于相同原理，只是实验验证深度不同\n\n**[W2] [major] Confusability 效应量过小，实际意义存疑**\n- 典型 batch gap 仅 ~2.2pp，extreme-batch 对比 ~25pp\n- Count 效应高达 −49pp，相比之下 confusability 效应极小\n- 论文用大量篇幅分析 ~2pp 效应，practical significance 不足\n- \"Practical implications\" 段仅声称 3-5pp 关联，不是因果\n\n**[W3] [major] 因果语言与证据等级不匹配**\n- \"schema-induced degradation\"、\"count-related recall decline\"、\"BCS explains 22-53%\"\n- 实际证据是 correlational + controlled stratification，非 interventional\n- Limitations #7 承认 no interventional causality，但 Abstract/Introduction 未反映\n- 建议 \"associated with\" 替代 \"explains\"；\"schema-induced\" → \"schema-associated\"\n\n**[W4] [major] SDGD 负面结果分析深度不足**\n- Section 5 仅约 1 column 正文 + Table 3\n- merge amplification 机制描述简短，无 k 值与 amplification 定量分析\n- routing failure 仅报告 oracle 上界，无失败案例分析\n- Future directions 均未验证\n- 作为 claimed contribution 深度不够\n\n**[W5] [minor] NER batch-level null result 作为独立 Contribution (#3) 有膨胀之嫌**\n- 本质是主实验 sub-finding，不是方法论或框架层面的独立贡献\n- 建议并入 Contribution #2\n\n**[W6] [minor] MAVEN centrality confound 削弱广度声称**\n- MAVEN 不参与主分析框架，核心发现实际只在 3 个数据集成立\n\n**[W7] [minor] \"First controlled study\" 声称需要更谨慎限定**\n- LLM-PEE 和 PARSE 隐式涉及 confusability 影响\n- \"First\" 声称容易引发反感\n\n**[W8] [minor] Cross-model validation 规模有限**\n- 仅 3 个 architecture family，Gemini 不在主分析中\n\n**Questions**:\n[Q1] Name-only vs name+definition SCS: 为什么 definition embedding 没帮助？是否说明 SCS 捕获的是 name-level 表面相似度？\n[Q2] BCS 在 NER 上为 null 是否说明 BCS 本身不适用于 NER（因 error mode 根本不同），而非 confusability 在 NER 中不存在？\n[Q3] BCS-Controlled batch 构建如何保证不是 trivially easy vs trivially hard 的对比？\n[Q4] Oracle routing 在 RE 上恢复 +29.8pp 但 practical routing 全部低于 single-pass——这是否说明 SDGD 本身不适用于 RE？\n[Q5] Abstract 中 \"Few-shot demonstrations do not reduce the gap\" 的 \"the gap\" 指代不明。\n\n**Missing References**: GoLLIE (Sainz et al., ICLR 2024); Schema as Parameterized Tools for Universal IE (2025)\n\n---\n\n请逐条给出你的 [AGREE] 或 [REBUT] 回应。",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 1339 · 2026-05-18T04:25:02.223965+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 26124
}
```

</details>

---


### Tool call

_source line 1340 · 2026-05-18T04:25:02.678684+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1（方法严谨性）的完整审稿意见。请逐条回应：**[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 1 的审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n\n**Strengths**:\n[S1] 实验设计精巧，count/confusability 隔离设计有方法论贡献\n[S2] 负面结果诚实且有诊断深度\n[S3] 统计分析在 NLP 领域中异常全面\n[S4] 多层次 robustness checks 覆盖面广\n[S5] Limitations section 是 NLP 论文中最详尽的之一\n\n**Weaknesses**:\n\n**[W1] [critical] Linear-scale vs logit-scale TOST 不一致性动摇核心 claim**\n- Logit-scale TOST p=0.209 (inconclusive)，而论文将 linear-scale p=0.003 作为 primary\n- 高 BCS batch accuracy 集中在 ~51%，接近 50% 时 linear scale 系统性压缩 interaction effects\n- 未提供 formal power analysis 支撑 \"limited power\" 解释\n- Logit-scale 90% CI 上界 (0.203) 超过 equivalence bound (0.156)\n- Linear-scale 作为 primary test 的选择似乎 post-hoc\n- 如果 bounded association 不成立，two-dimensional decomposition 框架核心假设被削弱\n\n**[W2] [critical] \"BCS explains 22-53% variance\" claim 范围过宽**\n- 53% 来自 DocRED n=25 batches，未报告 adjusted R² 和 bootstrap CI\n- NER batch-level R²≈0 但 Abstract framing 暗示 IE 通用性\n- 22% 对应 typical gap 仅 2.2pp (CI [0.4, 4.0])，practical significance 存疑\n- 建议：报告 DocRED CI、限定为 \"RE-specific\"、讨论 practical significance\n\n**[W3] [major] 跨模型 generality claim 超出证据范围**\n- \"fundamental property of in-context learning\" 是非常强的 claim\n- Dimension 2 仅在 open-weight RE 上充分验证\n- 无 closed-source frontier model 验证\n- 建议弱化为 \"consistent across tested model families\"\n\n**[W4] [major] FewRel constrained decoding 格式特殊性**\n- Constrained decoding 消除 calibration signal\n- Confusability 效应可能被 forced-choice 人为放大\n- Limitations item 6 仅一句话，正文讨论不足\n- 建议增加 unconstrained decoding 对比或更显著讨论边界条件\n\n**[W5] [major] Few-NERD Qwen3 embedding SCS 的 shared-representation dependency**\n- 用 extraction model 自身 embeddings 计算 SCS = circular dependency\n- MiniLM cross-check r=0.172 vs Qwen3 r=0.138，差异不显著\n- Confusion matrix correlation=0.894 可能意味着两者 capture 同一 artifact\n- 建议提供完全独立 embedding（GloVe/random）的消融\n\n**[W6] [minor] 3 seeds 的 variance decomposition 统计力度有限**\n\n**[W7] [minor] DocRED/MAVEN 5 batches vs FewRel/Few-NERD 25 batches 不对称未解释**\n\n**Questions**:\n[Q1] DocRED R²=0.525 的 adjusted R² 和 bootstrap CI？\n[Q2] TOST ±3pp margin 中 batch SD 锚点选择问题\n[Q3] FewRel constrained decoding 下 confusability 效应是否被 forced-choice 放大？\n[Q4] FewRel r=0.187 如何计算？与 Table 2 方法有何不同？\n[Q5] NER U-shape 在 RE 中不存在的原因？\n\n**Missing References**: Structured prediction calibration; Label space hierarchical reduction; Schema complexity in KGs\n\n---\n\n请逐条给出你的 [AGREE] 或 [REBUT] 回应。",
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1（方法严谨性）的完整审稿意见。请逐条回应：**[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 1 的审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n\n**Strengths**:\n[S1] 实验设计精巧，count/confusability 隔离设计有方法论贡献\n[S2] 负面结果诚实且有诊断深度\n[S3] 统计分析在 NLP 领域中异常全面\n[S4] 多层次 robustness checks 覆盖面广\n[S5] Limitations section 是 NLP 论文中最详尽的之一\n\n**Weaknesses**:\n\n**[W1] [critical] Linear-scale vs logit-scale TOST 不一致性动摇核心 claim**\n- Logit-scale TOST p=0.209 (inconclusive)，而论文将 linear-scale p=0.003 作为 primary\n- 高 BCS batch accuracy 集中在 ~51%，接近 50% 时 linear scale 系统性压缩 interaction effects\n- 未提供 formal power analysis 支撑 \"limited power\" 解释\n- Logit-scale 90% CI 上界 (0.203) 超过 equivalence bound (0.156)\n- Linear-scale 作为 primary test 的选择似乎 post-hoc\n- 如果 bounded association 不成立，two-dimensional decomposition 框架核心假设被削弱\n\n**[W2] [critical] \"BCS explains 22-53% variance\" claim 范围过宽**\n- 53% 来自 DocRED n=25 batches，未报告 adjusted R² 和 bootstrap CI\n- NER batch-level R²≈0 但 Abstract framing 暗示 IE 通用性\n- 22% 对应 typical gap 仅 2.2pp (CI [0.4, 4.0])，practical significance 存疑\n- 建议：报告 DocRED CI、限定为 \"RE-specific\"、讨论 practical significance\n\n**[W3] [major] 跨模型 generality claim 超出证据范围**\n- \"fundamental property of in-context learning\" 是非常强的 claim\n- Dimension 2 仅在 open-weight RE 上充分验证\n- 无 closed-source frontier model 验证\n- 建议弱化为 \"consistent across tested model families\"\n\n**[W4] [major] FewRel constrained decoding 格式特殊性**\n- Constrained decoding 消除 calibration signal\n- Confusability 效应可能被 forced-choice 人为放大\n- Limitations item 6 仅一句话，正文讨论不足\n- 建议增加 unconstrained decoding 对比或更显著讨论边界条件\n\n**[W5] [major] Few-NERD Qwen3 embedding SCS 的 shared-representation dependency**\n- 用 extraction model 自身 embeddings 计算 SCS = circular dependency\n- MiniLM cross-check r=0.172 vs Qwen3 r=0.138，差异不显著\n- Confusion matrix correlation=0.894 可能意味着两者 capture 同一 artifact\n- 建议提供完全独立 embedding（GloVe/random）的消融\n\n**[W6] [minor] 3 seeds 的 variance decomposition 统计力度有限**\n\n**[W7] [minor] DocRED/MAVEN 5 batches vs FewRel/Few-NERD 25 batches 不对称未解释**\n\n**Questions**:\n[Q1] DocRED R²=0.525 的 adjusted R² 和 bootstrap CI？\n[Q2] TOST ±3pp margin 中 batch SD 锚点选择问题\n[Q3] FewRel constrained decoding 下 confusability 效应是否被 forced-choice 放大？\n[Q4] FewRel r=0.187 如何计算？与 Table 2 方法有何不同？\n[Q5] NER U-shape 在 RE 中不存在的原因？\n\n**Missing References**: Structured prediction calibration; Label space hierarchical reduction; Schema complexity in KGs\n\n---\n\n请逐条给出你的 [AGREE] 或 [REBUT] 回应。",
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 1341 · 2026-05-18T04:25:04.246049+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1567
}
```

</details>

---


### Assistant

_source line 1342 · 2026-05-18T04:25:07.469424+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 128

## Round 128

2 recorded events


### User

_source line 1343 · 2026-05-18T04:25:10.130102+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿完成摘要**：

- **Overall**: 3.0 (Findings)，Soundness 3.5，Excitement 2.5，Reproducibility 4，Confidence 4
- **核心优势**：实验设计严谨（factorial design + TOST + permutation tests），Limitations 诚实全面，任务不对称性发现有洞察价值
- **主要问题**：
  - SCS/BCS 与 LLM-PEE 的增量不清晰（cosine similarity 是标准操作）
  - Confusability 效应过小（~2pp），实际意义存疑
  - 因果语言超出 correlational 证据水平
  - SDGD 负面结果分析深度不足以支撑独立贡献
  - NER null result 和 MAVEN confound 削弱了框架的广度声称

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1344 · 2026-05-18T04:25:16.044929+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 129

## Round 129

2 recorded events


### User

_source line 1345 · 2026-05-18T04:26:59.268674+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

### Weaknesses 逐条回应

**[AGREE] R2-W1: SCS/BCS 指标新颖性不足**

同意 R2 的核心判断。论文自身在 Related Work §2 最后一段（"SCS novelty"）已明确承认"SCS shares its formal definition (pairwise cosine similarity of type name embeddings) with the partitioning criterion used in LLM-PEE"，并声明"Our contribution is not the metric itself but the controlled experimental framework"。然而 Abstract 和 Contribution #2 的措辞（"We validate that pairwise embedding similarity predicts type confusion"）仍以 SCS/BCS 为核心卖点，与 Related Work 中的自我定位不一致。建议在 Contribution 列表中将重心从 metric 本身转移到 experimental framework 和 findings 上。

不过，需要补充的是：LLM-PEE 使用 embedding similarity 做 partitioning 工程，但没有做 controlled experiments 来验证 confusability 是否独立于 count 预测 degradation。论文的增量不在指标本身，而在 BCS-controlled 实验范式（固定 count 变化 BCS，§3.3 Experiment 2）和 within-pool 分析（Table 6）。这个方法论增量是实质性的，但论文的 framing 未能突出这一点。

**[PARTIALLY AGREE] R2-W2: Confusability 效应量过小**

部分同意。R2 指出 typical-batch gap 仅 2.2pp（§5.3, CI [0.4, 4.0]），相比 count 效应的 -49pp 确实很小，实际意义有限。这与我在 N2 中的 concern 一致。

但我认为 R2 的论述忽略了两点：(1) 本文是 analytical study 而非 engineering paper——目标是 characterize degradation 的成因而非提供大幅度改进方案。小但 real 的效应在分析性研究中是可接受的 contribution（ACL ARR reviewer guidelines 明确反对 H5: "treating SOTA achievement as necessary"）。(2) Batch-level R²=0.22 意味着在 schema design 时 BCS 是一个 non-trivial predictor，即使 typical gap 小，对大规模部署（数万次抽取）来说累积效应可能有意义。

R2 的合理建议是论文应更坦诚地在 Abstract/Introduction 中呈现 typical-batch magnitude（2.2pp），而非以 extreme-batch 数字（25-31pp）为主导叙事。这点我在 N2 中已独立提出。

**[PARTIALLY AGREE] R2-W3: 因果语言与证据不匹配**

部分同意。R2 区分了两类用语：
- "BCS explains 22-53% of variance"：这是标准回归术语（R² 字面意思就是 "variance explained"），在统计学中不暗示因果关系。R2 建议改为 "associated with" 会使语言不够精确——R² 就是 "explained variance"。**此处 REBUT。**
- "schema-induced degradation"（title 和全文多次出现）：这确实暗示因果方向。论文的证据是 correlational + controlled stratification，不是 interventional。Limitations §7 承认 "The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway"。但 title 和 Abstract 未反映这个 qualification。**此处 AGREE。**

建议：title 中的 "schema-induced" 可弱化为 "schema-associated" 或保持 "schema complexity" 的 predictive framing（当前 title "How Does Schema Complexity Predict Performance" 实际上已经是 predictive 而非 causal 的措辞，比正文中的 "schema-induced" 更准确）。正文中 "schema-induced degradation" 改为 "schema-associated degradation" 更准确。

**[PARTIALLY AGREE] R2-W4: SDGD 负面结果分析深度不足**

部分同意 R2 的观察但不同意严重程度判断。

同意：(1) merge amplification 的 quantitative analysis 确实不足——论文仅报告了 precision 从 0.563→0.210 的整体下降，但没有分析 k 值（decomposition passes 数量）与 false positive 增长的定量关系。如果 merge amplification 随 k 线性增长 vs 超线性增长，对 future mitigation 策略的指导完全不同。(2) Routing failure 仅报告了 5 种 strategy 的 accuracy（Table 7），没有 error analysis（哪些 instances 被错误路由？是 BCS 最高的 sub-schema 间的 confusion 还是 uniform failure？）。

反驳严重程度：作为 Contribution #4 的负面结果，§6 + Appendix B/C 的深度在 NLP 论文中已属充分。负面结果的价值在于 (a) 证明 naive decomposition 不 work，(b) 诊断出 bottleneck（merge vs routing），(c) 量化 upper bound（oracle +29.8pp）。R2 要求的 k-value analysis 和 failure case analysis 是 reasonable suggestions 但不构成 rejection-level concern。

**[REBUT] R2-W5: NER batch-level null result 不应作为独立 Contribution**

不同意。Contribution #3 不仅仅是"NER 上 BCS 不 work"这个 null result，而是揭示了一个结构性的 task asymmetry：pairwise SCS-confusion correlation 在 NER 上显著（r=0.112, p<0.001, Table 2），但这个 signal 在 batch level 消失（r≈0, n=450, §5.3）。这个"pairwise signal exists but doesn't aggregate"的现象有独立的分析价值，它的解释（missed entities 43-65% overwhelm type substitution signal, §5.4 和 Figure 3）揭示了 NER 和 RE 的 error mode 根本差异。

如果把这个并入 Contribution #2，会弱化"BCS 的 task-dependent applicability"这个 finding——这对想使用 BCS 做 schema design 的 practitioners 是重要的边界信息。

**[AGREE] R2-W6: MAVEN centrality confound 削弱广度声称**

同意。MAVEN 的 per-type/batch-level BCS 分析因 centrality confound 实际不可用（§5.5），仅 pairwise SCS-confusion 仍显著（r=0.129, Table 2）。论文声称"four datasets"但 MAVEN 的参与度明显弱于其他三个。我在审稿中未单独提出此问题，但 R2 的观察准确。

建议在 Contribution 措辞中将"four datasets"改为"three primary datasets (Few-NERD, FewRel, DocRED) with supplementary evidence from MAVEN"，更准确地反映 MAVEN 的角色。

**[REBUT] R2-W7: "First controlled study" 声称需更谨慎限定**

不同意。论文的 claim 是 "first controlled study isolating type confusability from type count via stratified design in zero-shot LLM IE"（§1），不是 "first study of confusability"。R2 提到 LLM-PEE 和 PARSE "隐式涉及 confusability 影响"，但：
- LLM-PEE（§2, Related Work）使用 embedding similarity 做 partitioning，但没有 controlled experiments 隔离 count 和 confusability。它的实验是 engineering evaluation（decomposition 后性能是否提升），不是 analytical isolation。
- PARSE 优化 schema definitions，更不涉及 confusability 的 controlled analysis。

"First controlled study isolating X from Y" 是一个 sufficiently qualified claim，因为它限定了方法（controlled isolation via stratified design）和范围（zero-shot LLM IE）。当然，如果有已发表工作确实做了同样的 controlled isolation，这个 claim 就不成立——但 R2 未给出这样的 counterexample。

**[AGREE] R2-W8: Cross-model validation 规模有限**

同意，与我的 W3 一致。3 个 architecture family（Qwen3, LLaMA, Gemini）对于 "fundamental property of in-context learning" 的 claim 不足。Gemini 仅验证 Dimension 1，Dimension 2 在 proprietary models 上完全未验证。

---

### Questions 逐条回应

**[Q1] Name-only vs definition SCS**

R2 的推测有道理但论文提供了 partial evidence against。Appendix §G Table 8 显示 matrix correlation 0.66-0.89，说明 name-only 和 name+definition SCS 高度一致。论文解释（§3.2）是 MAVEN/FewRel prompts 本身就只使用 type names，所以 name-only SCS 直接匹配 model input。只有 Few-NERD 的 prompts 包含 definitions。但 R2 的更深层问题——SCS 是否只 capture surface-level name similarity 而非 semantic confusability——是 valid concern，可以通过 random-label experiments 来测试。

**[Q2] BCS 不适用于 NER**

R2 的解读与论文一致。§5.4 和 Discussion 明确指出 NER errors dominated by missed entities (43-65%)，batch-level confusability 被 boundary detection failures 淹没。论文的结论确实是"BCS 不适用于 NER batch-level prediction"（不是"confusability 在 NER 中不存在"），因为 pairwise SCS-confusion 仍然显著（Table 2, r=0.112）。R2 的表述准确。

**[Q3] BCS-Controlled batch 的 trivially easy/hard 问题**

论文在 Appendix §M 提供了明确回答：variance decomposition 显示 BCS unique R²=0.259 (36.8%), composition unique R²=0.298 (42.3%), shared R²=0.147 (20.9%)，VIF=1.06，r(BCS, difficulty)=-0.21。这表明 BCS 和 type difficulty 近乎正交，extreme-batch 对比不是 trivially easy vs hard。Within-pool 分析（Table 6）进一步控制了 pool composition。我认为这个问题论文已充分 address。

**[Q4] SDGD 不适用于 RE**

R2 的解读本质上正确，这也是论文的结论（§6: "all practical routing strategies fall below the single-pass baseline because constrained decoding forces confident predictions in every sub-schema"）。但论文的 framing 是"routing failure"而非"SDGD 不适用于 RE"——前者暗示 routing 可以改进，后者暗示 fundamental limitation。考虑到 constrained decoding 消除了 calibration signal（none-rate 仅 20-40%），这更像是 constrained decoding 的问题而非 SDGD 的 inherent limitation。

**[Q5] Abstract 中 "the gap" 指代不明**

同意。Abstract 中 "Few-shot demonstrations do not reduce the gap (+4.3pp under 5-shot)" 的 "the gap" 指 BCS gap（低 BCS vs 高 BCS accuracy 差异），但 Abstract 前文讨论的是 count-related decline 和 confusability-related substitution 两种 gap，读者无法确定指哪个。应改为 "Few-shot demonstrations do not reduce the confusability gap" 或类似更明确的表述。

---

### Missing References

**GoLLIE (Sainz et al., ICLR 2024)**：已在 references.bib 中引用（gollie-2024），且在 Related Work §2 第一段被引用。R2 可能遗漏了这个引用。

**"Schema as Parameterized Tools for Universal IE"**：不确定 R2 指的是哪篇具体论文。如果是指 OneKE (Luo et al., 2025) 或类似的 schema-as-tools 框架，论文已引用 oneke-2025。如果是另一篇 2025 年论文，需要 R2 提供具体 citation 以核实。

---

### 总体评估

R2 给出 Overall 3.0 (Findings)。我认为 R2 的评分偏低。R2 的核心 concerns 可归纳为：(1) SCS 新颖性（valid but the novelty is in the experimental framework, not the metric）；(2) 效应量小（valid concern about framing but acceptable for an analytical study）；(3) 因果语言（partially valid, mostly a writing fix）；(4) SDGD 深度（valid suggestion but not rejection-level）。

这些问题大多可通过 revision 修复（reframing claims, weakening causal language, adding DocRED CI），不构成 fundamental methodological flaws。我维持 3.5 (Borderline Conference) 的评分——论文的实验设计精巧度和统计严谨性在 NLP 领域中突出，但 framing/overclaim 问题拉低了整体印象。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1346 · 2026-05-18T04:27:05.186065+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 130

## Round 130

2 recorded events


### User

_source line 1347 · 2026-05-18T04:27:11.669025+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

总结：对 R2 的 8 条 Weaknesses，我的回应分布为：
- **AGREE**: W1 (SCS 新颖性)、W6 (MAVEN 广度)、W8 (cross-model 有限)
- **PARTIALLY AGREE**: W2 (效应量 framing)、W3 (因果语言)、W4 (SDGD 深度)
- **REBUT**: W5 (NER null 作为独立 Contribution 有独立分析价值)、W7 ("First controlled study" 限定足够)

核心分歧在 Overall 评分：R2 给 3.0 (Findings)，我维持 3.5 (Borderline Conference)。R2 的主要 concerns 多为 framing/writing 问题，可通过 revision 修复，不构成 fundamental methodological flaws。论文的实验设计和统计严谨性是实质性优势。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1348 · 2026-05-18T04:27:16.863439+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 131

## Round 131

8 recorded events


### User

_source line 1349 · 2026-05-18T04:28:19.851286+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 交叉回应 Reviewer 1 审稿意见

---

### Strengths 回应

**[AGREE] R1-S1 至 R1-S5**: 全部同意。R1 对本文实验设计、统计分析、Limitations 质量的肯定与我的独立评估一致。特别是 S3（统计分析全面性）和 S5（Limitations 详尽性）是本文最突出的优点。补充：我在自己的审稿中也独立认定了相同的优势（我的 S1 对应 R1-S1，我的 S2 对应 R1-S5）。

---

### Weaknesses 逐条回应

**[AGREE] R1-W1: Linear-scale vs logit-scale TOST 不一致性**

同意这是一个严肃的方法论问题。核心要点：

1. 论文在 Appendix C (page 15) 确实报告了两种 scale 的结果：linear-scale TOST p=0.003（equivalence），logit-scale TOST p=0.209（inconclusive）。论文选择 linear-scale 作为 primary 并将 logit-scale 报告为 sensitivity check。

2. R1 指出高 BCS batch accuracy 集中在 ~51%（接近 50%）时 linear scale 系统性压缩 interaction effects，这个论点成立。在 accuracy ≈ 0.5 处，logit 变换的导数最大（=4），微小的 linear-scale 差异对应更大的 logit-scale 差异。论文的 0.47pp linear interaction 在 logit scale 上对应 back-transformed 2.53pp（Appendix C），更接近 ±3pp bound。

3. 论文的 "limited power" 辩护（n=0.65 post-hoc power）在没有 formal a priori power analysis 的情况下说服力不足。R1 要求 formal power analysis 是合理的。

4. **补充我的独立发现**：我注意到 Table 8（Section 4.4, page 8）的 TOST sensitivity analysis 显示在 ±1pp margin 时 equivalence 不成立（p=0.278），意味着 interaction 可能达到主效应的约一半量级。这进一步支持了 R1 的担忧——bounded association 的结论高度依赖 margin 的选择。

5. 但我认为 R1 说 "动摇核心 claim" 略显极端——即使 logit-scale TOST inconclusive，双维度分解框架本身仍有描述性价值。问题在于 "bounded association" 这一特定 quantitative claim 的可靠性，不是整个框架失效。两个维度的主效应（count decline 和 BCS-accuracy regression）不受 TOST 结果影响。

**严重程度**：我评为 major（非 critical）。TOST 是一个 supporting analysis，不是核心 claim 的唯一支柱。

---

**[AGREE] R1-W2: "BCS explains 22-53% variance" claim 范围过宽**

完全同意。这与我的 W2（confusability 效应量过小）和 W3（因果语言与证据等级不匹配）相互印证。具体补充：

1. **53% 来自 DocRED 仅 n=25 batches**：小样本 R² 天然上偏。R1 要求 adjusted R² 和 bootstrap CI 完全合理。以 k=1 predictor、n=25 估算，adjusted R² ≈ 0.525 − (1−0.525)×1/(25−2) ≈ 0.504，下降不大，但 bootstrap CI 的缺失确实是一个遗漏。

2. **Abstract 用 "22-53%" 的范围表述暗示跨任务 generality**：但 NER batch-level R²≈0（Section 4.3, page 6: "BCS shows no batch-level signal in NER"），这意味着 22-53% 仅适用于 RE。Abstract 应明确标注 "in RE tasks"。

3. **22% 对应 typical gap ~2.2pp**：这个实际效应量确实小到令人质疑 practical significance。我在自己的 W2 中独立提出了同样的担忧。

4. **"explains" 用词问题**：R² 描述 variance accounted for by the model，用 "explains" 在统计学上不算错，但在因果推断语境下容易误导。建议改为 "accounts for" 或 "is associated with"。

---

**[AGREE] R1-W3: 跨模型 generality claim 超出证据**

同意。"fundamental property of in-context learning" 需要更广泛的证据支撑。我在自己的 W8 中也独立指出了 cross-model validation 的局限性。

补充：
- 论文实际验证了 Qwen3-32B (primary) + LLaMA-3.1-70B/8B + Gemini 2.5 Flash (Appendix R)
- Gemini 仅做了 count curves 验证（Appendix R, page 22），未做 BCS-controlled 实验
- 3 个 architecture family 不足以支撑 "fundamental property" 的 universal claim
- R1 建议弱化为 "consistent across tested model families" 是合理的最低修改要求
- 更好的表述可能是 "these patterns are consistent across the model families we tested (Qwen, LLaMA, Gemini), suggesting but not establishing that schema-induced degradation may be a general property of in-context learning"

---

**[AGREE with nuance] R1-W4: FewRel constrained decoding格式特殊性**

部分同意，但认为 R1 可能高估了这个问题的严重程度。

**同意的部分**：
- Constrained decoding 确实消除了 "refuse to answer" 或 "hallucinate new types" 的可能性，将所有 error 压缩到 type confusion channel
- 这可能人为放大了 confusability 的可观测效应
- Limitations #6 (page 9) 仅一句话确实不够

**不完全同意的部分**：
- 对于 RE 的 closed-set classification 设定，constrained decoding 是合理的实验选择（Section 3.5, page 5）。实际部署中，当 schema 固定时，constrained decoding 是常见做法
- 论文同时报告了 NER 结果（unconstrained，text-matching evaluation），NER 上 confusability pairwise 效应显著但 batch-level 为 null。这提供了一个自然的 unconstrained 对照
- 问题不是 constrained decoding 本身不合理，而是论文没有充分讨论其对 effect size 的影响

**建议**：不需要重做 unconstrained decoding 实验，但正文（不仅 Limitations）应讨论 constrained decoding 如何影响 confusability effect 的可观测性，并在 claim 中加入 caveat。

---

**[REBUT] R1-W5: Shared-representation dependency / circular dependency**

不完全同意 R1 对 circular dependency 的诊断。

**关键事实**：
1. 论文 Section 3.2 (page 4) 明确指出 **MiniLM 是 primary embedding**（"We use MiniLM as the primary embedding for BCS computation because sentence-transformers are specifically trained for semantic similarity"），不是 Qwen3
2. MiniLM (384-d sentence-transformer) 与 Qwen3-32B (causal LM) 是完全不同的模型架构、不同的训练目标、不同的参数量级
3. Qwen3 embedding 是 cross-check，不是 primary。论文报告 MiniLM r=0.112 (Few-NERD) vs Qwen3 r=0.138，两者的相似结论说明信号不依赖特定 embedding choice

**R1 的合理之处**：
- confusion matrix correlation=0.894 确实高，但这更可能说明 type confusability 是 schema 的内在属性（被不同 embedding 一致捕获），而非 circular artifact
- 如果要彻底排除 shared representation concern，GloVe 或 random baseline 确实有价值——但这是 "nice to have"，不是方法论缺陷

**R1 的表述有误导性**：R1 称 "用 extraction model 自身 embeddings 计算 SCS = circular dependency"。但实际上论文的 primary SCS 用的是 MiniLM，不是 extraction model (Qwen3-32B)。R1 可能把 Qwen3 cross-check 误读为 primary method。

---

**[AGREE] R1-W6: 3 seeds 的 variance decomposition 统计力度有限**

同意这是一个 minor limitation。Table 16 (Appendix P, page 21) 显示 count 80 时 batch SD = 0 因为只有一个 batch composition，这从侧面说明了 seed 数量的限制。但 count-level effects 的 magnitude（−49pp）远大于 seed variance，主要结论应该是 robust 的。

---

**[AGREE] R1-W7: Batch 数量不对称未充分解释**

同意。这是一个 editorial issue。论文应在 Section 3.3 中解释：DocRED 仅 96 relation types（vs FewRel 80 但 pool 更小？不对，FewRel 也是 80），不同的 batch count 是因为 type pool 大小和 BCS range 的限制。Few-NERD 有 66 types，FewRel 80 types，但 BCS-controlled batches 的构建依赖于 sufficient BCS contrast，这在某些数据集上更难实现。

不过这是 minor issue，不影响结论。

---

### Questions 回应

**[Q1] DocRED R²=0.525 的 adjusted R² 和 bootstrap CI**：
同意应报告。如上估算 adjusted R² ≈ 0.504。这是 R1 要求的合理补充。

**[Q2] TOST ±3pp margin 选择**：
论文 Appendix C (page 15) 说明 margin 基于 "three converging anchors"：(1) half the within-pool SD, (2) medium effect threshold, (3) Cohen's d = 0.5。Table 8 提供了 ±1pp 到 ±5pp 的 sensitivity analysis。我认为锚点选择有一定合理性，但 R1 指出的 "batch SD 可能因 confusability 本身而变化" 这一 concern 是 valid 的。

**[Q3] FewRel constrained decoding下 confusability 效应是否被放大**：
见上方 W4 回应。总结：可能被放大，但 constrained decoding 是 RE 的合理设定。

**[Q4] FewRel r=0.187 计算方法**：
Table 2 (page 6) 报告 FewRel MiniLM r=0.187, p<0.001。这是 pairwise SCS-confusion correlation。计算方法应与其他数据集一致（Pearson correlation between SCS(i,j) and confusion rate f_j for type pairs）。如果 R1 认为此处有方法不一致，需要作者澄清。

**[Q5] NER U-shape 在 RE 中不存在的原因**：
论文 Section 4.1 (page 5) 提到 NER 的 U-shaped 曲线（intermediate counts 处 recall 下降后部分恢复）。R1 问为什么 RE 没有。论文称 "The NER U-shape (at 44.1) likely reflects a dual-task burden absent in RE" (page 8, Discussion)。这个解释合理但 speculative——NER 需要同时做 boundary detection 和 type classification，中间 count 时两个 subtask 可能互相干扰。RE 只需做 classification（boundary 已给定），所以 monotonic decline。

---

### Missing References 回应

**[AGREE]** R1 提到的三个方向（structured prediction calibration; label space hierarchical reduction; schema complexity in KGs）在论文中确实覆盖不足。我在自己的审稿中也独立指出了 GoLLIE (Sainz et al., ICLR 2024) 的缺失。这些方向与本文 schema complexity 主题直接相关，补充引用会加强 Related Work 的完整性。

---

### 总结：与 R1 的评分差异

R1 给 3.5 (Borderline Conference)，我给 3.0 (Findings)。差异来源：

1. **R1 更重视方法论贡献**（factorial design + 统计分析），我更重视 **novelty/excitement**。R1 的 W1 (TOST inconsistency) 如果是 critical，理应拉低到 3.0 而非保持 3.5。

2. **我对 SCS/BCS 新颖性有更严格的评判**：R1 没有明确讨论 SCS 与 LLM-PEE 的 formal identity 问题，这在我看来是影响 novelty 评分的 major factor。

3. **我对 confusability 效应量 (~2pp) 的 practical significance 更 skeptical**：R1 提到了这个问题（W2 中 "practical significance 存疑"），但似乎没有将其权重到最终评分中。

4. **共识点**：两位 reviewer 都认为因果语言超出证据水平、cross-model claim 需弱化、SDGD 分析可以更深入。论文作为 Findings 论文是合适的，但主会议接收需要更显著的 novelty 或更大的效应量。

**建议 meta-reviewer**：R1 的 W1 (TOST 不一致) 和我的 W1 (SCS 新颖性) + W2 (效应量) 是 rebuttal 中需要重点回应的问题。如果作者能 (a) 提供 logit-scale power analysis 或 larger-sample factorial 验证, (b) 更清晰地区分 SCS 与 LLM-PEE 的增量, 评分可能上调至 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1350 · 2026-05-18T04:28:50.925587+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1351 · 2026-05-18T04:28:50.976409+00:00_

1	# Round 13 Review Issues Tracker
2	# Updated: 2026-05-18 (Round 13 Action Matrix dispatched, issues marked in_progress)
3	
4	# ============================================================
5	# CRITICAL — Must-Fix
6	# ============================================================
7	
8	- id: R3-C2
9	  summary: "'Empirically separable channels' 缺乏 formal 统计支撑 — TOST margin ±3pp > typical effect 2.2pp"
10	  category: framing
11	  severity: critical
12	  status: resolved
13	  first_raised_round: 3
14	  last_seen_round: 9
15	  mentions:
16	    - {round: 3, reviewers: [R1, R2], note: "因果语言过强"}
17	    - {round: 4, reviewers: [R1, R2], note: "Title 'Drive' + §4.3 暗示因果"}
18	    - {round: 5, reviewers: [R1, R2, R3], note: "三人共识改措辞"}
19	    - {round: 6, reviewers: [R1, R2, R3], note: "factorial p=0.50; 建议 'mechanistically distinguishable'"}
20	    - {round: 7, reviewers: [R1, R2], note: "三项 factorial 检验中两项失败"}
21	    - {round: 8, reviewers: [R1, R2], note: "R1-N1 critical: 3/4 tests 失败; 共识: 需限定"}
22	    - {round: 9, reviewers: [R1, R2, R3], note: "三人共识: TOST ±3pp margin 用 prompt variation 锚定不合逻辑; margin > typical main effect; ±1pp inconclusive"}
23	  action_items:
24	    - {round: 9, action: "D051: 'additive separability' → 'bounded interaction' 全文统一; SESOI effect-size anchored", assigned_to: agent, status: done}
25	  resolution: "D051 W1: 全文 'bounded interaction' 统一; SESOI effect-size anchored; sensitivity table in Appendix"
26	  resolution_round: 9
27	
28	- id: R10-N1
29	  summary: "因果语言 ('driven', 'channels', 'shape') 超出 observational/quasi-experimental 证据边界"
30	  category: framing
31	  severity: critical
32	  status: resolved
33	  first_raised_round: 10
34	  last_seen_round: 12
35	  mentions:
36	    - {round: 10, reviewers: [R1, R2], note: "R1 critical N3 + R2 AGREE with qualification; 共识: Title 'shape' 暗示因果"}
37	    - {round: 11, reviewers: [R1, R2], note: "R1 W4 + R2 AGREE: Title 'Shape' + Limitations 承认 no interventional causality = 不匹配"}
38	    - {round: 12, reviewers: [
…[truncated 698 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1352 · 2026-05-18T04:32:08.765629+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "schema-dag-extraction",
  "issues_yaml": "# Round 14 Review Issues Tracker\n# Updated: 2026-05-18 (Round 14 fresh review)\n\n# ============================================================\n# CRITICAL — Must-Fix\n# ============================================================\n\n- id: R3-C2\n  summary: \"'Empirically separable channels' 缺乏 formal 统计支撑 — TOST margin ±3pp > typical effect 2.2pp\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 9\n  mentions:\n    - {round: 3, reviewers: [R1, R2], note: \"因果语言过强\"}\n    - {round: 4, reviewers: [R1, R2], note: \"Title 'Drive' + §4.3 暗示因果\"}\n    - {round: 5, reviewers: [R1, R2, R3], note: \"三人共识改措辞\"}\n    - {round: 6, reviewers: [R1, R2, R3], note: \"factorial p=0.50; 建议 'mechanistically distinguishable'\"}\n    - {round: 7, reviewers: [R1, R2], note: \"三项 factorial 检验中两项失败\"}\n    - {round: 8, reviewers: [R1, R2], note: \"R1-N1 critical: 3/4 tests 失败; 共识: 需限定\"}\n    - {round: 9, reviewers: [R1, R2, R3], note: \"三人共识: TOST ±3pp margin 用 prompt variation 锚定不合逻辑; margin > typical main effect; ±1pp inconclusive\"}\n  action_items:\n    - {round: 9, action: \"D051: 'additive separability' → 'bounded interaction' 全文统一; SESOI effect-size anchored\", assigned_to: agent, status: done}\n  resolution: \"D051 W1: 全文 'bounded interaction' 统一; SESOI effect-size anchored; sensitivity table in Appendix\"\n  resolution_round: 9\n\n- id: R10-N1\n  summary: \"因果语言 ('driven', 'channels', 'shape') 超出 observational/quasi-experimental 证据边界\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - {round: 10, reviewers: [R1, R2], note: \"R1 critical N3 + R2 AGREE with qualification; 共识: Title 'shape' 暗示因果\"}\n    - {round: 11, reviewers: [R1, R2], note: \"R1 W4 + R2 AGREE: Title 'Shape' + Limitations 承认 no interventional causality = 不匹配\"}\n    - {round: 12, reviewers: [R2], note: \"MOSTLY FIXED: Title 改为 'Predict'; 正文主体无 'channels'/'driven'; 仅 Appendix N/P 残余 'count-driven'/'BCS-driven' — 降级为 R12-W2\"}\n  action_items:\n    - {round: 10, action: \"分层替换 (D052): correlational → 'predicts'/'associated with'\", assigned_to: agent, status: done}\n    - {round: 11, action: \"D054: Title 'Shape' → 'Predict'; 全文因果语言 grep 扫描清零\", assigned_to: agent, status: done}\n  resolution: \"Title 改为 'Predict'; 正文因果语言已清理; Appendix 残余为 R12-W2 追踪\"\n  resolution_round: 12\n\n- id: R10-N2\n  summary: \"Pair-level→batch-level 聚合推理链叙事误导 — unconditional sim R²=0.044 vs 观测 0.218\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 12\n  resolution: \"叙事链清晰分层; simulation 明确为 illustrative; R²=0.218 为独立实证\"\n  resolution_round: 12\n\n- id: R10-N3\n  summary: \"TOST ±3pp margin 的 external anchoring 不足 — 130% amplification threshold 为 arbitrary judgment call\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 12\n  resolution: \"三重 anchoring + sensitivity table 已到位; logit-scale 不一致性追踪于 R12-W3\"\n  resolution_round: 12\n\n- id: R10-N4\n  summary: \"SCS/BCS Contribution #2 framing 暗示 metric novelty — 实际增量是 controlled validation\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: \"Contribution #2 已 reframe 为 controlled validation; §2 SCS novelty 段明确界定增量\"\n  resolution_round: 11\n\n- id: R11-N1\n  summary: \"NER Dimension 2 batch-level 证据方向相反（r=+0.50~+0.58），但论文 title/abstract 泛化为 cross-task\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Abstract/Intro/Contribution/Discussion 均已精确限定 batch-level Dim2 = RE-specific; pairwise cross-task 正确区分\"\n  resolution_round: 12\n\n# ============================================================\n# WARNING — Should-Fix (Open / In-Progress)\n# ============================================================\n\n- id: R11-N2\n  summary: \"核心效应量过小 (typical gap 2.2pp, pairwise r²=1.3%) — practical significance 存疑\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - {round: 11, reviewers: [R1, R2], note: \"2.2pp CI [0.4, 4.0] 在部署中几乎不可察觉; 需更强论证 practical significance\"}\n    - {round: 12, reviewers: [R1, R2], note: \"降级为 should-fix, 更多是 findings 本身的局限而非写作缺陷\"}\n    - {round: 13, reviewers: [R1, R2], note: \"R1-W2 + R2-N1 双方再次确认; extreme-batch gap 在叙事中占比过高, typical gap 2.2pp 应前置\"}\n    - {round: 14, reviewers: [R1, R2], note: \"R1-W2 + R2-W2 双方共识: 22% R² 对应 2.2pp typical gap, practical significance 有限; extreme-batch 数字 (25-31pp) 在叙事中权重仍过高; R1 partially agree R2 但认为 analytical study 中 small effect 可接受\"}\n  action_items:\n    - {round: 11, action: \"D054 Phase 3: Discussion reframe '2.2pp negligible IS the finding'\", assigned_to: agent, status: done}\n    - {round: 12, action: \"Discussion 补充: 在什么部署条件下 2.2pp 有实际价值\", assigned_to: agent, status: in_progress}\n    - {round: 14, action: \"Introduction/Results 叙事进一步前置 typical-batch magnitude; Abstract 确保 typical vs extreme 平衡\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W1\n  summary: \"Discussion/Conclusion 过于简短 — 缺 actionable recommendations 和 future work\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - {round: 11, reviewers: [R1, R2], note: \"analysis paper 需更充分的 Discussion\"}\n    - {round: 12, reviewers: [R1, R2], note: \"Discussion MOSTLY FIXED; Conclusion 仅 3 句\"}\n    - {round: 13, reviewers: [R1, R2], note: \"Conclusion ~120 words, 缺 future work/broader implications\"}\n    - {round: 14, reviewers: [], note: \"本轮未直接提及, Conclusion 已有 future work 句但仍偏短\"}\n  action_items:\n    - {round: 13, action: \"Conclusion 扩展\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W2\n  summary: \"TOST (Two One-Sided Tests) 术语首次出现未展开\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - {round: 11, reviewers: [R1, R2], note: \"NLP 社区对 TOST 不熟悉\"}\n    - {round: 12, reviewers: [R2], note: \"Introduction L15 首次使用 'TOST p=0.003' 未展开\"}\n    - {round: 14, reviewers: [], note: \"本轮未直接提及但 Introduction finding (1) 仍含未展开 TOST\"}\n  action_items:\n    - {round: 13, action: \"Introduction 首次使用处展开 'Two One-Sided Tests (TOST)'\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-N1\n  summary: \"Introduction Finding (1) 仍过于密集 — 56 词复合句含多层嵌套\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - {round: 12, reviewers: [R2], note: \"Finding (1) 含冒号、两个括号插入、分号\"}\n    - {round: 14, reviewers: [], note: \"本轮未直接提及\"}\n  action_items:\n    - {round: 12, action: \"拆 Finding (1) 为 2-3 句\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W1\n  summary: \"Contribution 3 将 NER null result 包装为正面贡献\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - {round: 12, reviewers: [R1, R2], note: \"后半句 'NER shows no batch-level BCS signal' 是 null result 正面包装\"}\n    - {round: 13, reviewers: [R1, R2], note: \"共识: 保留独立 contribution 但改 framing\"}\n    - {round: 14, reviewers: [R1, R2], note: \"R2-W5 再次提出应并入 C2; R1 REBUT: task-dependent diagnosis 有独立分析价值; 分歧记录\"}\n  action_items:\n    - {round: 13, action: \"Contribution 3 改写: 强调诊断性发现而非包装 null result\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W2\n  summary: \"Appendix 残余因果语言 ('count-driven', 'BCS-driven') + 正文 'schema-induced'\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - {round: 12, reviewers: [R2], note: \"Appendix 'count-driven decline'; 'BCS-driven confusability effect'\"}\n    - {round: 14, reviewers: [R1, R2], note: \"R2-W3 再次提出: 'schema-induced degradation' 全文多处出现, 超出 correlational 证据; R1 partially agree: title 'predict' 合适但正文 'schema-induced' 应改 'schema-associated'\"}\n  action_items:\n    - {round: 12, action: \"替换为 'count-related' / 'BCS-associated'\", assigned_to: agent, status: in_progress}\n    - {round: 14, action: \"全文 grep 'schema-induced' 替换为 'schema-associated degradation'\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W3\n  summary: \"TOST logit-scale inconclusive (p=0.209) — linear vs logit scale 选择缺乏 a priori justification\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - {round: 12, reviewers: [R1, R2], note: \"logit-scale TOST p=0.209, 2×2 factorial p=0.56, ±1pp inconclusive\"}\n    - {round: 13, reviewers: [R1, R2], note: \"正文需更显著报告 logit-scale 不一致\"}\n    - {round: 14, reviewers: [R1, R2], note: \"R1-W1 [critical]: logit-scale 90% CI 上界 0.203 > bound 0.156, 不是 power 能解释的; linear-scale primary 选择似 post-hoc; R2 AGREE 但降级为 major: bounded association 是 supporting claim 非核心, 双维度主效应不受影响; 共识: 需 formal power analysis 或弱化 claim 为 'bounded under linear specification; inconclusive on logit'\"}\n  action_items:\n    - {round: 14, action: \"§4.4 正文: (1) bounded association claim 加限定 'under the primary linear-scale specification'; (2) 提供 logit-scale power analysis 或明确标注 inconclusive; (3) 讨论 scale choice 的 a priori rationale\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W4\n  summary: \"Introduction findings vs contributions 不对齐\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - {round: 12, reviewers: [R1, R2], note: \"Finding (4) centrality confound 和 Finding (5) decomposition failure 映射不明\"}\n    - {round: 13, reviewers: [R1, R2], note: \"Finding (3) 'cross-scale consistency' 无对应 contribution\"}\n    - {round: 14, reviewers: [], note: \"本轮未直接提及\"}\n  action_items:\n    - {round: 13, action: \"统一 findings 和 contributions 数量/映射\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W1\n  summary: \"Gemini 2.5 Flash 引用错误: bib gemini-team-2024 指向 Gemini 1.5 论文\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - {round: 13, reviewers: [R1, R2], note: \"事实性错误\"}\n    - {round: 14, reviewers: [], note: \"本轮未直接提及, 可能已修复待确认\"}\n  action_items:\n    - {round: 13, action: \"替换为 Gemini 2.5 正确引用\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W3\n  summary: \"SCS §3.2 'We introduce' 措辞暗示指标新颖性, 但与 LLM-PEE 形式相同\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - {round: 13, reviewers: [R1, R2], note: \"§3.2 'We introduce' vs Related Work 承认 = LLM-PEE\"}\n    - {round: 14, reviewers: [R1, R2], note: \"R2-W1 [major] 再次指出: Abstract/Contribution 以 SCS/BCS 为核心卖点但增量仅在 experimental framework; R1 AGREE: 建议重心从 metric 转移到 experimental design\"}\n  action_items:\n    - {round: 13, action: \"§3.2 改 'We introduce' → 'We operationalize'\", assigned_to: agent, status: in_progress}\n    - {round: 14, action: \"Contribution #1-2 措辞从 metric-centric 转向 framework-centric; Abstract 降低 SCS/BCS 作为卖点的权重\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W4\n  summary: \"Abstract 偏短且缺 motivation 和 cross-model generalization 提及\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - {round: 13, reviewers: [R2], note: \"约 115-140 words, 共识补至 ~200 words\"}\n    - {round: 14, reviewers: [R2], note: \"R2 评价 '约 170 words, 四个必答问题基本回答, 但 why important 仅半句话'; Abstract 中 'the gap' 指代不明 (R2-Q5, R1 AGREE)\"}\n  action_items:\n    - {round: 14, action: \"Abstract: (1) 加强 'why important' 动机句; (2) 'the gap' → 'the confusability gap' 明确指代\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W5\n  summary: \"FewRel closed-set classification + constrained decoding 格式特殊性, 泛化性不确定\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - {round: 13, reviewers: [R1], note: \"Limitations item 6 承认但不够 prominent\"}\n    - {round: 14, reviewers: [R1, R2], note: \"R1-W4 [major]: constrained decoding 消除 calibration signal, confusability 可能被 forced-choice 放大; R2 AGREE with nuance: constrained decoding 合理但需讨论对 effect size 影响; NER unconstrained 结果提供自然对照; 共识: 正文 (非仅 Limitations) 应讨论此边界条件\"}\n  action_items:\n    - {round: 14, action: \"Discussion 或 §4.3 正文补充: constrained decoding 如何影响 RE confusability effect 的可观测性; 在 RE claim 中加入 caveat\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W1\n  summary: \"'BCS explains 22-53% variance' claim 中 53% (DocRED) 稳定性未验证, 且 framing 暗示 IE 通用性\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - {round: 14, reviewers: [R1, R2], note: \"R1-W2 [critical] + R2 AGREE: DocRED R²=0.53 在 n=25 上未报告 adjusted R²/bootstrap CI; Abstract '22-53%' 暗示跨任务但 NER=0; 22% 对应 typical gap 仅 2.2pp\"}\n  action_items:\n    - {round: 14, action: \"(1) 报告 DocRED R² 的 adjusted R² 和 bootstrap CI; (2) Abstract/Introduction 明确限定为 'RE accuracy variance'; (3) 讨论 R²=0.22 对应 2.2pp 的 practical significance\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W2\n  summary: \"'fundamental property of in-context learning' claim 跨模型证据不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - {round: 14, reviewers: [R1, R2], note: \"R1-W3 [major] + R2 AGREE: Dimension 2 仅在 open-weight RE 验证, 无 closed-source frontier model; 3 families 不足以支撑 'fundamental property'; 建议 'consistent across tested model families'\"}\n  action_items:\n    - {round: 14, action: \"Abstract/Conclusion 弱化: 'fundamental property of in-context learning' → 'consistent across tested model families, suggesting schema-induced degradation may be a general property of in-context learning'\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W3\n  summary: \"SDGD (§5) 分析深度不足以支撑独立贡献 — 缺 k-value quantitative analysis 和 failure case analysis\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - {round: 14, reviewers: [R1, R2], note: \"R2-W4 [major]: merge amplification 无 k vs FP 定量关系; routing failure 无 error analysis; R1 PARTIALLY AGREE: 作为负面结果深度已可接受, 但 k-value analysis 和 failure cases 是 reasonable suggestions\"}\n  action_items:\n    - {round: 14, action: \"§5 或 Appendix 补充: (1) merge amplification 与 k 的定量关系 (2) routing failure 的代表性 error cases\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# INFO — Minor\n# ============================================================\n\n- id: R10-m2\n  summary: \"NER U-shape mechanistic 解释 (dual-task burden) 未经验证 — 应标注为 hypothesis\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - {round: 10, reviewers: [R1, R2], note: \"indirect evidence plausible 但不构成 definitive proof\"}\n    - {round: 14, reviewers: [R1], note: \"R1-Q5: NER U-shape 在 RE 中不存在 — 论文的 dual-task burden 解释合理但 speculative\"}\n  action_items:\n    - {round: 10, action: \"U-shape 解释标注为 hypothesis\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R10-m3\n  summary: \"Missing references — 持续追踪\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - {round: 10, reviewers: [R1, R2], note: \"NuNER 应补\"}\n    - {round: 11, reviewers: [R1, R2], note: \"Levy 2024, Dror 2018, GenRES/ULTRA, Zhao 2021\"}\n    - {round: 12, reviewers: [R1, R2], note: \"Outlines (Willard & Louf 2023), Cheng 2023, Lu 2022\"}\n    - {round: 13, reviewers: [R1, R2], note: \"calibration lit, embedding similarity for confusion lit\"}\n    - {round: 14, reviewers: [R1, R2], note: \"R1: structured prediction calibration (Kuleshov & Liang 2015), label embedding trees (Bengio 2010), KG relation cardinality (Bordes 2013); R2: GoLLIE 已引用 (R2 遗漏), Schema as Parameterized Tools 未确认具体论文\"}\n  action_items:\n    - {round: 14, action: \"考虑补充: structured prediction calibration, label embedding trees, KG schema complexity 文献\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R10-m5\n  summary: \"1000 instances 对 long-tail types 充分性\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - {round: 10, reviewers: [R1], note: \"低频 types 个位数 instances\"}\n    - {round: 11, reviewers: [R1, R2], note: \"cluster bootstrap 部分 addresses\"}\n  action_items:\n    - {round: 11, action: \"频率分层 SCS-confusion analysis 或 discuss as limitation\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-m1\n  summary: \"FP8 + vLLM greedy decoding 残余非确定性 (seed SD=0.88pp at count 80)\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - {round: 11, reviewers: [R1], note: \"greedy mode 下 SD 应为 0\"}\n    - {round: 14, reviewers: [R1], note: \"R1-W6: 3 seeds variance decomposition 统计力度有限\"}\n  action_items:\n    - {round: 11, action: \"调查 vLLM FP8 non-determinism; 修正 'eliminates randomness'\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-m2\n  summary: \"-ing 分词短语和 'Notably' 使用 — AI 写作痕迹残余\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - {round: 12, reviewers: [R2], note: \"Results §4.1 'indicating...'; Discussion §5 'suggesting...'\"}\n    - {round: 13, reviewers: [R1, R2], note: \"约 10-15 处\"}\n    - {round: 14, reviewers: [R2], note: \"R2 cross-check 评价: '几乎无 em-dash; 无过度分段; 段落长度自然; 写作质量在 AI 辅助论文中属于上乘'\"}\n  action_items:\n    - {round: 13, action: \"全文 grep 'ing,' 模式, 改写 participial phrases\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-m3\n  summary: \"DocRED count curve 仅引用未在 Appendix 呈现\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - {round: 12, reviewers: [R2], note: \"§4.1 引用 'Appendix' 但无 DocRED count curve\"}\n    - {round: 14, reviewers: [R1], note: \"R1-W7: DocRED/MAVEN 5 batches vs FewRel/Few-NERD 25 batches 不对称未解释\"}\n  action_items:\n    - {round: 14, action: \"§3.3 解释 batch count 不对称的原因 (计算成本/type pool constraints)\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-m1\n  summary: \"MAVEN validation set 是否用于 hyperparameter 选择未声明\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - {round: 13, reviewers: [R2], note: \"应声明 validation set 未用于 design decisions\"}\n    - {round: 14, reviewers: [], note: \"本轮未直接提及\"}\n  action_items:\n    - {round: 13, action: \"§3.1 MAVEN 段补充声明\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-m2\n  summary: \"多重比较处理: prompt variant 8 tests 用 directional consistency 代替正式检验\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - {round: 13, reviewers: [R1], note: \"7/8 negative 隐式 sign test p=0.035; 建议显式报告\"}\n  action_items:\n    - {round: 13, action: \"Appendix prompt variant section 显式报告 sign test p-value\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-m3\n  summary: \"FewRel contamination 风险: R1 标 major, R2 REBUT 认为现有分析充分\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - {round: 13, reviewers: [R1, R2], note: \"未达共识, 记录分歧\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-m1\n  summary: \"MAVEN 应降级为 supplementary dataset — '4 datasets' 声称中 MAVEN 参与度弱\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - {round: 14, reviewers: [R1, R2], note: \"R2-W6 + R1 AGREE: MAVEN centrality confound 使其不参与主分析; 建议 '3 primary datasets + supplementary MAVEN'\"}\n  action_items:\n    - {round: 14, action: \"Contribution 措辞中将 'four datasets' 改为 'three primary datasets with supplementary evidence from MAVEN'\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-m2\n  summary: \"Abstract 'up to -49pp' 来自 DocRED doc-level RE (非主实验) — cherry-picking 最大数字嫌疑\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - {round: 14, reviewers: [R1], note: \"R1 小问题: 主实验以 FewRel 为主 (-36pp), -49pp 来自 DocRED\"}\n  action_items:\n    - {round: 14, action: \"Abstract 中 count-decline 数字考虑用 FewRel 主实验值或标注来源\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# RESOLVED (历史)\n# ============================================================\n\n- id: R9-W1\n  summary: \"Single-seed evaluation — count curve 每 level 仅 5 batches\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"D051 completed: 3-seed × 25-batch count curves with ±1SD error bars\"\n  resolution_round: 10\n\n- id: R10-W1\n  summary: \"\\\\enlargethispage*{9\\\\baselineskip} 操纵页面布局\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"\\\\enlargethispage 已删除; 当前版本格式合规\"\n  resolution_round: 11\n\n- id: R10-W2\n  summary: \"Negative results (§5) 占 ~1.5 页但缺乏 constructive next steps\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"§5 Future directions paragraph added with 3 concrete avenues\"\n  resolution_round: 11\n\n- id: R10-W3\n  summary: \"Abstract 数字密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"Abstract 精简至 3 个核心数字\"\n  resolution_round: 12\n\n- id: R10-W4\n  summary: \"Introduction Contribution list 含未铺垫概念且每条过长\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"Contribution list 改为方法论声明格式, 每条 1-2 行\"\n  resolution_round: 12\n\n- id: R10-W5\n  summary: \"BCS 'generalizes across tasks' (Contribution #3) 过强 — batch-level 仅在 RE 直接支持\"\n  category: framing\n  severity: warning\n  status: resolved\n  resolution: \"Contribution 3 限定为 RE-specific\"\n  resolution_round: 12\n\n- id: R10-W6\n  summary: \"Em-dash 使用偏高 — AI 写作痕迹\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"Em-dash 已清理\"\n  resolution_round: 11\n\n- id: R10-W7\n  summary: \"Supplementary 三处 placeholder sections 未完成\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"无独立 supplementary; 所有补充材料在 main.tex Appendix\"\n  resolution_round: 12\n\n- id: R11-W3\n  summary: \"Prompt variant analysis (n=10) underpowered + 无 multiple comparison correction\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Rothman (1990) 论证 + directional consistency 充分\"\n  resolution_round: 12\n\n- id: R10-m4\n  summary: \"Multiple comparisons: Rothman (1990) 适用于 conceptual replications\"\n  category: method\n  severity: info\n  status: resolved\n  resolution: \"R12 交叉共识\"\n  resolution_round: 12\n\n- id: R2-N3-80rel\n  summary: \"Abstract/Intro 以 extreme-batch 31.2pp 为 headline, typical 2.2pp 被弱化\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"D051 W2: Intro typical-first; Discussion IQR caveat; R² range corrected\"\n  resolution_round: 9\n\n- id: R4-N1\n  summary: \"RE batch composition +1.4pp (p≈0.19) — Contribution #4 framing\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"D051 W4: Contribution #4 → 'structural barriers' with specific numbers\"\n  resolution_round: 9\n\n- id: R6-N1\n  summary: \"Two-channel decomposition 概念贡献有限 — Findings-level\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"D051 W4: 4 contributions rewritten\"\n  resolution_round: 9\n\n- id: MW2\n  summary: \"Pairwise r²=1.3-1.7% 到 batch R²=22% 聚合: conditioning bias\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"simulation → illustrative; R²=0.218 primary\"\n  resolution_round: 9\n\n- id: R5-W1\n  summary: \"FewRel train+val 合并 — data contamination 风险\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Split-origin covariate confirms BCS partial effect unchanged\"\n  resolution_round: 9\n\n- id: R5-N1\n  summary: \"SCS novelty — metric 与 LLM-PEE 形式相同\"\n  category: framing\n  severity: warning\n  status: resolved\n  resolution: \"Contribution #2 reframed as empirical validation\"\n  resolution_round: 9\n\n- id: R6-W1\n  summary: \"'首次 controlled study' 声称需限定\"\n  category: framing\n  severity: warning\n  status: resolved\n  resolution: \"'To our knowledge' added\"\n  resolution_round: 9\n\n- id: R6-N2\n  summary: \"正文可能超过 8 页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"编译确认 Conclusion 在 p8\"\n  resolution_round: 9\n\n- id: R10-PS\n  summary: \"Prompt sensitivity 实验结果需整合入论文\"\n  category: experiment\n  severity: warning\n  status: resolved\n  resolution: \"Prompt sensitivity results integrated into §4.3 + Appendix H\"\n  resolution_round: 11\n\n- id: R12-W5\n  summary: \"Orphan bib entries\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"Orphan entries 已删除\"\n  resolution_round: 13\n\n- id: R10-m1\n  summary: \"Cross-seed variance (2.7pp at count 16) 与 typical effect (2.2pp) 量级相当\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - {round: 14, reviewers: [], note: \"R14 未直接提及; greedy decoding + FP8 non-determinism 已在 §3.4 说明\"}\n  resolution: \"§3.4 说明 greedy decoding 残余 SD=0.88pp 归因于 FP8 quantization non-determinism\"\n  resolution_round: 14\n\n- id: R13-W2\n  summary: \"BCS > 0.59 阈值缺乏 formal derivation\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - {round: 13, reviewers: [R1, R2], note: \"建议删除\"}\n    - {round: 14, reviewers: [], note: \"本轮未直接提及\"}\n  action_items:\n    - {round: 13, action: \"删除 0.59 阈值\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-m1\n  summary: \"Abstract 偏短 (~130-140 words)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"升级追踪于 R13-W4; R14 评价 ~170 words 在范围内\"\n  resolution_round: 14\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "schema-dag-extraction",
    "issues_yaml": "# Round 14 Review Issues Tracker\n# Updated: 2026-05-18 (Round 14 fresh review)\n\n# ============================================================\n# CRITICAL — Must-Fix\n# ============================================================\n\n- id: R3-C2\n  summary: \"'Empirically separable channels' 缺乏 formal 统计支撑 — TOST margin ±3pp > typical effect 2.2pp\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 9\n  mentions:\n    - {round: 3, reviewers: [R1, R2], note: \"因果语言过强\"}\n    - {round: 4, reviewers: [R1, R2], note: \"Title 'Drive' + §4.3 暗示因果\"}\n    - {round: 5, reviewers: [R1, R2, R3], note: \"三人共识改措辞\"}\n    - {round: 6, reviewers: [R1, R2, R3], note: \"factorial p=0.50; 建议 'mechanistically distinguishable'\"}\n    - {round: 7, reviewers: [R1, R2], note: \"三项 factorial 检验中两项失败\"}\n    - {round: 8, reviewers: [R1, R2], note: \"R1-N1 critical: 3/4 tests 失败; 共识: 需限定\"}\n    - {round: 9, reviewers: [R1, R2, R3], note: \"三人共识: TOST ±3pp margin 用 prompt variation 锚定不合逻辑; margin > typical main effect; ±1pp inconclusive\"}\n  action_items:\n    - {round: 9, action: \"D051: 'additive separability' → 'bounded interaction' 全文统一; SESOI effect-size anchored\", assigned_to: agent, status: done}\n  resolution: \"D051 W1: 全文 'bounded interaction' 统一; SESOI effect-size anchored; sensitivity table in Appendix\"\n  resolution_round: 9\n\n- id: R10-N1\n  summary: \"因果语言 ('driven', 'channels', 'shape') 超出 observational/quasi-experimental 证据边界\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - {round: 10, reviewers: [R1, R2], note: \"R1 critical N3 + R2 AGREE with qualification; 共识: Title 'shape' 暗示因果\"}\n    - {round: 11, reviewers: [R1, R2], note: \"R1 W4 + R2 AGREE: Title 'Shape' + Limitations 承认 no interventional causality = 不匹配\"}\n    - {round: 12, reviewers: [R2], note: \"MOSTLY FIXED: Title 改为 'Predict'; 正文主体无 'channels'/'driven'; 仅 Appendix N/P 残余 'count-driven'/'BCS-driven' — 降级为 R12-W2\"}\n  action_items:\n    - {round: 10, action: \"分层替换 (D052): correlational → 'predicts'/'associated with'\", assigned_to: agent, status: done}\n    - {round: 11, action: \"D054: Title 'Shape' → 'Predict'; 全文因果语言 grep 扫描清零\", assigned_to: agent, status: done}\n  resolution: \"Title 改为 'Predict'; 正文因果语言已清理; Appendix 残余为 R12-W2 追踪\"\n  resolution_round: 12\n\n- id: R10-N2\n  summary: \"Pair-level→batch-level 聚合推理链叙事误导 — unconditional sim R²=0.044 vs 观测 0.218\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 12\n  resolution: \"叙事链清晰分层; simulation 明确为 illustrative; R²=0.218 为独立实证\"\n  resolution_round: 12\n\n- id: R10-N3\n  summary: \"TOST ±3pp margin 的 external anchoring 不足 — 130% amplification threshold 为 arbitrary judgment call\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 12\n  resolution: \"三重 anchoring + sensitivity table 已到位; logit-scale 不一致性追踪于 R12-W3\"\n  resolution_round: 12\n\n- id: R10-N4\n  summary: \"SCS/BCS Contribution #2 framing 暗示 metric novelty — 实际增量是 controlled validation\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: \"Contribution #2 已 reframe 为 controlled validation; §2 SCS novelty 段明确界定增量\"\n  resolution_round: 11\n\n- id: R11-N1\n  summary: \"NER Dimension 2 batch-level 证据方向相反（r=+0.50~+0.58），但论文 title/abstract 泛化为 cross-task\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Abstract/Intro/Contribution/Discussion 均已精确限定 batch-level Dim2 = RE-specific; pairwise cross-task 正确区分\"\n  resolution_round: 12\n\n# ============================================================\n# WARNING — Should-Fix (Open / In-Progress)\n# ============================================================\n\n- id: R11-N2\n  summary: \"核心效应量过小 (typical gap 2.2pp, pairwise r²=1.3%) — practical significance 存疑\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - {round: 11, reviewers: [R1, R2], note: \"2.2pp CI [0.4, 4.0] 在部署中几乎不可察觉; 需更强论证 practical significance\"}\n    - {round: 12, reviewers: [R1, R2], note: \"降级为 should-fix, 更多是 findings 本身的局限而非写作缺陷\"}\n    - {round: 13, reviewers: [R1, R2], note: \"R1-W2 + R2-N1 双方再次确认; extreme-batch gap 在叙事中占比过高, typical gap 2.2pp 应前置\"}\n    - {round: 14, reviewers: [R1, R2], note: \"R1-W2 + R2-W2 双方共识: 22% R² 对应 2.2pp typical gap, practical significance 有限; extreme-batch 数字 (25-31pp) 在叙事中权重仍过高; R1 partially agree R2 但认为 analytical study 中 small effect 可接受\"}\n  action_items:\n    - {round: 11, action: \"D054 Phase 3: Discussion reframe '2.2pp negligible IS the finding'\", assigned_to: agent, status: done}\n    - {round: 12, action: \"Discussion 补充: 在什么部署条件下 2.2pp 有实际价值\", assigned_to: agent, status: in_progress}\n    - {round: 14, action: \"Introduction/Results 叙事进一步前置 typical-batch magnitude; Abstract 确保 typical vs extreme 平衡\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W1\n  summary: \"Discussion/Conclusion 过于简短 — 缺 actionable recommendations 和 future work\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - {round: 11, reviewers: [R1, R2], note: \"analysis paper 需更充分的 Discussion\"}\n    - {round: 12, reviewers: [R1, R2], note: \"Discussion MOSTLY FIXED; Conclusion 仅 3 句\"}\n    - {round: 13, reviewers: [R1, R2], note: \"Conclusion ~120 words, 缺 future work/broader implications\"}\n    - {round: 14, reviewers: [], note: \"本轮未直接提及, Conclusion 已有 future work 句但仍偏短\"}\n  action_items:\n    - {round: 13, action: \"Conclusion 扩展\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W2\n  summary: \"TOST (Two One-Sided Tests) 术语首次出现未展开\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - {round: 11, reviewers: [R1, R2], note: \"NLP 社区对 TOST 不熟悉\"}\n    - {round: 12, reviewers: [R2], note: \"Introduction L15 首次使用 'TOST p=0.003' 未展开\"}\n    - {round: 14, reviewers: [], note: \"本轮未直接提及但 Introduction finding (1) 仍含未展开 TOST\"}\n  action_items:\n    - {round: 13, action: \"Introduction 首次使用处展开 'Two One-Sided Tests (TOST)'\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-N1\n  summary: \"Introduction Finding (1) 仍过于密集 — 56 词复合句含多层嵌套\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - {round: 12, reviewers: [R2], note: \"Finding (1) 含冒号、两个括号插入、分号\"}\n    - {round: 14, reviewers: [], note: \"本轮未直接提及\"}\n  action_items:\n    - {round: 12, action: \"拆 Finding (1) 为 2-3 句\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W1\n  summary: \"Contribution 3 将 NER null result 包装为正面贡献\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - {round: 12, reviewers: [R1, R2], note: \"后半句 'NER shows no batch-level BCS signal' 是 null result 正面包装\"}\n    - {round: 13, reviewers: [R1, R2], note: \"共识: 保留独立 contribution 但改 framing\"}\n    - {round: 14, reviewers: [R1, R2], note: \"R2-W5 再次提出应并入 C2; R1 REBUT: task-dependent diagnosis 有独立分析价值; 分歧记录\"}\n  action_items:\n    - {round: 13, action: \"Contribution 3 改写: 强调诊断性发现而非包装 null result\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W2\n  summary: \"Appendix 残余因果语言 ('count-driven', 'BCS-driven') + 正文 'schema-induced'\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - {round: 12, reviewers: [R2], note: \"Appendix 'count-driven decline'; 'BCS-driven confusability effect'\"}\n    - {round: 14, reviewers: [R1, R2], note: \"R2-W3 再次提出: 'schema-induced degradation' 全文多处出现, 超出 correlational 证据; R1 partially agree: title 'predict' 合适但正文 'schema-induced' 应改 'schema-associated'\"}\n  action_items:\n    - {round: 12, action: \"替换为 'count-related' / 'BCS-associated'\", assigned_to: agent, status: in_progress}\n    - {round: 14, action: \"全文 grep 'schema-induced' 替换为 'schema-associated degradation'\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W3\n  summary: \"TOST logit-scale inconclusive (p=0.209) — linear vs logit scale 选择缺乏 a priori justification\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - {round: 12, reviewers: [R1, R2], note: \"logit-scale TOST p=0.209, 2×2 factorial p=0.56, ±1pp inconclusive\"}\n    - {round: 13, reviewers: [R1, R2], note: \"正文需更显著报告 logit-scale 不一致\"}\n    - {round: 14, reviewers: [R1, R2], note: \"R1-W1 [critical]: logit-scale 90% CI 上界 0.203 > bound 0.156, 不是 power 能解释的; linear-scale primary 选择似 post-hoc; R2 AGREE 但降级为 major: bounded association 是 supporting claim 非核心, 双维度主效应不受影响; 共识: 需 formal power analysis 或弱化 claim 为 'bounded under linear specification; inconclusive on logit'\"}\n  action_items:\n    - {round: 14, action: \"§4.4 正文: (1) bounded association claim 加限定 'under the primary linear-scale specification'; (2) 提供 logit-scale power analysis 或明确标注 inconclusive; (3) 讨论 scale choice 的 a priori rationale\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W4\n  summary: \"Introduction findings vs contributions 不对齐\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - {round: 12, reviewers: [R1, R2], note: \"Finding (4) centrality confound 和 Finding (5) decomposition failure 映射不明\"}\n    - {round: 13, reviewers: [R1, R2], note: \"Finding (3) 'cross-scale consistency' 无对应 contribution\"}\n    - {round: 14, reviewers: [], note: \"本轮未直接提及\"}\n  action_items:\n    - {round: 13, action: \"统一 findings 和 contributions 数量/映射\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W1\n  summary: \"Gemini 2.5 Flash 引用错误: bib gemini-team-2024 指向 Gemini 1.5 论文\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - {round: 13, reviewers: [R1, R2], note: \"事实性错误\"}\n    - {round: 14, reviewers: [], note: \"本轮未直接提及, 可能已修复待确认\"}\n  action_items:\n    - {round: 13, action: \"替换为 Gemini 2.5 正确引用\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W3\n  summary: \"SCS §3.2 'We introduce' 措辞暗示指标新颖性, 但与 LLM-PEE 形式相同\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - {round: 13, reviewers: [R1, R2], note: \"§3.2 'We introduce' vs Related Work 承认 = LLM-PEE\"}\n    - {round: 14, reviewers: [R1, R2], note: \"R2-W1 [major] 再次指出: Abstract/Contribution 以 SCS/BCS 为核心卖点但增量仅在 experimental framework; R1 AGREE: 建议重心从 metric 转移到 experimental design\"}\n  action_items:\n    - {round: 13, action: \"§3.2 改 'We introduce' → 'We operationalize'\", assigned_to: agent, status: in_progress}\n    - {round: 14, action: \"Contribution #1-2 措辞从 metric-centric 转向 framework-centric; Abstract 降低 SCS/BCS 作为卖点的权重\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W4\n  summary: \"Abstract 偏短且缺 motivation 和 cross-model generalization 提及\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - {round: 13, reviewers: [R2], note: \"约 115-140 words, 共识补至 ~200 words\"}\n    - {round: 14, reviewers: [R2], note: \"R2 评价 '约 170 words, 四个必答问题基本回答, 但 why important 仅半句话'; Abstract 中 'the gap' 指代不明 (R2-Q5, R1 AGREE)\"}\n  action_items:\n    - {round: 14, action: \"Abstract: (1) 加强 'why important' 动机句; (2) 'the gap' → 'the confusability gap' 明确指代\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W5\n  summary: \"FewRel closed-set classification + constrained decoding 格式特殊性, 泛化性不确定\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - {round: 13, reviewers: [R1], note: \"Limitations item 6 承认但不够 prominent\"}\n    - {round: 14, reviewers: [R1, R2], note: \"R1-W4 [major]: constrained decoding 消除 calibration signal, confusability 可能被 forced-choice 放大; R2 AGREE with nuance: constrained decoding 合理但需讨论对 effect size 影响; NER unconstrained 结果提供自然对照; 共识: 正文 (非仅 Limitations) 应讨论此边界条件\"}\n  action_items:\n    - {round: 14, action: \"Discussion 或 §4.3 正文补充: constrained decoding 如何影响 RE confusability effect 的可观测性; 在 RE claim 中加入 caveat\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W1\n  summary: \"'BCS explains 22-53% variance' claim 中 53% (DocRED) 稳定性未验证, 且 framing 暗示 IE 通用性\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - {round: 14, reviewers: [R1, R2], note: \"R1-W2 [critical] + R2 AGREE: DocRED R²=0.53 在 n=25 上未报告 adjusted R²/bootstrap CI; Abstract '22-53%' 暗示跨任务但 NER=0; 22% 对应 typical gap 仅 2.2pp\"}\n  action_items:\n    - {round: 14, action: \"(1) 报告 DocRED R² 的 adjusted R² 和 bootstrap CI; (2) Abstract/Introduction 明确限定为 'RE accuracy variance'; (3) 讨论 R²=0.22 对应 2.2pp 的 practical significance\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W2\n  summary: \"'fundamental property of in-context learning' claim 跨模型证据不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - {round: 14, reviewers: [R1, R2], note: \"R1-W3 [major] + R2 AGREE: Dimension 2 仅在 open-weight RE 验证, 无 closed-source frontier model; 3 families 不足以支撑 'fundamental property'; 建议 'consistent across tested model families'\"}\n  action_items:\n    - {round: 14, action: \"Abstract/Conclusion 弱化: 'fundamental property of in-context learning' → 'consistent across tested model families, suggesting schema-induced degradation may be a general property of in-context learning'\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W3\n  summary: \"SDGD (§5) 分析深度不足以支撑独立贡献 — 缺 k-value quantitative analysis 和 failure case analysis\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - {round: 14, reviewers: [R1, R2], note: \"R2-W4 [major]: merge amplification 无 k vs FP 定量关系; routing failure 无 error analysis; R1 PARTIALLY AGREE: 作为负面结果深度已可接受, 但 k-value analysis 和 failure cases 是 reasonable suggestions\"}\n  action_items:\n    - {round: 14, action: \"§5 或 Appendix 补充: (1) merge amplification 与 k 的定量关系 (2) routing failure 的代表性 error cases\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# INFO — Minor\n# ============================================================\n\n- id: R10-m2\n  summary: \"NER U-shape mechanistic 解释 (dual-task burden) 未经验证 — 应标注为 hypothesis\"\n  category: framing\n  severity: info\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - {round: 10, reviewers: [R1, R2], note: \"indirect evidence plausible 但不构成 definitive proof\"}\n    - {round: 14, reviewers: [R1], note: \"R1-Q5: NER U-shape 在 RE 中不存在 — 论文的 dual-task burden 解释合理但 speculative\"}\n  action_items:\n    - {round: 10, action: \"U-shape 解释标注为 hypothesis\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R10-m3\n  summary: \"Missing references — 持续追踪\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - {round: 10, reviewers: [R1, R2], note: \"NuNER 应补\"}\n    - {round: 11, reviewers: [R1, R2], note: \"Levy 2024, Dror 2018, GenRES/ULTRA, Zhao 2021\"}\n    - {round: 12, reviewers: [R1, R2], note: \"Outlines (Willard & Louf 2023), Cheng 2023, Lu 2022\"}\n    - {round: 13, reviewers: [R1, R2], note: \"calibration lit, embedding similarity for confusion lit\"}\n    - {round: 14, reviewers: [R1, R2], note: \"R1: structured prediction calibration (Kuleshov & Liang 2015), label embedding trees (Bengio 2010), KG relation cardinality (Bordes 2013); R2: GoLLIE 已引用 (R2 遗漏), Schema as Parameterized Tools 未确认具体论文\"}\n  action_items:\n    - {round: 14, action: \"考虑补充: structured prediction calibration, label embedding trees, KG schema complexity 文献\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R10-m5\n  summary: \"1000 instances 对 long-tail types 充分性\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  mentions:\n    - {round: 10, reviewers: [R1], note: \"低频 types 个位数 instances\"}\n    - {round: 11, reviewers: [R1, R2], note: \"cluster bootstrap 部分 addresses\"}\n  action_items:\n    - {round: 11, action: \"频率分层 SCS-confusion analysis 或 discuss as limitation\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-m1\n  summary: \"FP8 + vLLM greedy decoding 残余非确定性 (seed SD=0.88pp at count 80)\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - {round: 11, reviewers: [R1], note: \"greedy mode 下 SD 应为 0\"}\n    - {round: 14, reviewers: [R1], note: \"R1-W6: 3 seeds variance decomposition 统计力度有限\"}\n  action_items:\n    - {round: 11, action: \"调查 vLLM FP8 non-determinism; 修正 'eliminates randomness'\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-m2\n  summary: \"-ing 分词短语和 'Notably' 使用 — AI 写作痕迹残余\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - {round: 12, reviewers: [R2], note: \"Results §4.1 'indicating...'; Discussion §5 'suggesting...'\"}\n    - {round: 13, reviewers: [R1, R2], note: \"约 10-15 处\"}\n    - {round: 14, reviewers: [R2], note: \"R2 cross-check 评价: '几乎无 em-dash; 无过度分段; 段落长度自然; 写作质量在 AI 辅助论文中属于上乘'\"}\n  action_items:\n    - {round: 13, action: \"全文 grep 'ing,' 模式, 改写 participial phrases\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-m3\n  summary: \"DocRED count curve 仅引用未在 Appendix 呈现\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - {round: 12, reviewers: [R2], note: \"§4.1 引用 'Appendix' 但无 DocRED count curve\"}\n    - {round: 14, reviewers: [R1], note: \"R1-W7: DocRED/MAVEN 5 batches vs FewRel/Few-NERD 25 batches 不对称未解释\"}\n  action_items:\n    - {round: 14, action: \"§3.3 解释 batch count 不对称的原因 (计算成本/type pool constraints)\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-m1\n  summary: \"MAVEN validation set 是否用于 hyperparameter 选择未声明\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - {round: 13, reviewers: [R2], note: \"应声明 validation set 未用于 design decisions\"}\n    - {round: 14, reviewers: [], note: \"本轮未直接提及\"}\n  action_items:\n    - {round: 13, action: \"§3.1 MAVEN 段补充声明\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-m2\n  summary: \"多重比较处理: prompt variant 8 tests 用 directional consistency 代替正式检验\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - {round: 13, reviewers: [R1], note: \"7/8 negative 隐式 sign test p=0.035; 建议显式报告\"}\n  action_items:\n    - {round: 13, action: \"Appendix prompt variant section 显式报告 sign test p-value\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-m3\n  summary: \"FewRel contamination 风险: R1 标 major, R2 REBUT 认为现有分析充分\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - {round: 13, reviewers: [R1, R2], note: \"未达共识, 记录分歧\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-m1\n  summary: \"MAVEN 应降级为 supplementary dataset — '4 datasets' 声称中 MAVEN 参与度弱\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - {round: 14, reviewers: [R1, R2], note: \"R2-W6 + R1 AGREE: MAVEN centrality confound 使其不参与主分析; 建议 '3 primary datasets + supplementary MAVEN'\"}\n  action_items:\n    - {round: 14, action: \"Contribution 措辞中将 'four datasets' 改为 'three primary datasets with supplementary evidence from MAVEN'\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-m2\n  summary: \"Abstract 'up to -49pp' 来自 DocRED doc-level RE (非主实验) — cherry-picking 最大数字嫌疑\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - {round: 14, reviewers: [R1], note: \"R1 小问题: 主实验以 FewRel 为主 (-36pp), -49pp 来自 DocRED\"}\n  action_items:\n    - {round: 14, action: \"Abstract 中 count-decline 数字考虑用 FewRel 主实验值或标注来源\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# RESOLVED (历史)\n# ============================================================\n\n- id: R9-W1\n  summary: \"Single-seed evaluation — count curve 每 level 仅 5 batches\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"D051 completed: 3-seed × 25-batch count curves with ±1SD error bars\"\n  resolution_round: 10\n\n- id: R10-W1\n  summary: \"\\\\enlargethispage*{9\\\\baselineskip} 操纵页面布局\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"\\\\enlargethispage 已删除; 当前版本格式合规\"\n  resolution_round: 11\n\n- id: R10-W2\n  summary: \"Negative results (§5) 占 ~1.5 页但缺乏 constructive next steps\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"§5 Future directions paragraph added with 3 concrete avenues\"\n  resolution_round: 11\n\n- id: R10-W3\n  summary: \"Abstract 数字密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"Abstract 精简至 3 个核心数字\"\n  resolution_round: 12\n\n- id: R10-W4\n  summary: \"Introduction Contribution list 含未铺垫概念且每条过长\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"Contribution list 改为方法论声明格式, 每条 1-2 行\"\n  resolution_round: 12\n\n- id: R10-W5\n  summary: \"BCS 'generalizes across tasks' (Contribution #3) 过强 — batch-level 仅在 RE 直接支持\"\n  category: framing\n  severity: warning\n  status: resolved\n  resolution: \"Contribution 3 限定为 RE-specific\"\n  resolution_round: 12\n\n- id: R10-W6\n  summary: \"Em-dash 使用偏高 — AI 写作痕迹\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"Em-dash 已清理\"\n  resolution_round: 11\n\n- id: R10-W7\n  summary: \"Supplementary 三处 placeholder sections 未完成\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"无独立 supplementary; 所有补充材料在 main.tex Appendix\"\n  resolution_round: 12\n\n- id: R11-W3\n  summary: \"Prompt variant analysis (n=10) underpowered + 无 multiple comparison correction\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Rothman (1990) 论证 + directional consistency 充分\"\n  resolution_round: 12\n\n- id: R10-m4\n  summary: \"Multiple comparisons: Rothman (1990) 适用于 conceptual replications\"\n  category: method\n  severity: info\n  status: resolved\n  resolution: \"R12 交叉共识\"\n  resolution_round: 12\n\n- id: R2-N3-80rel\n  summary: \"Abstract/Intro 以 extreme-batch 31.2pp 为 headline, typical 2.2pp 被弱化\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"D051 W2: Intro typical-first; Discussion IQR caveat; R² range corrected\"\n  resolution_round: 9\n\n- id: R4-N1\n  summary: \"RE batch composition +1.4pp (p≈0.19) — Contribution #4 framing\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"D051 W4: Contribution #4 → 'structural barriers' with specific numbers\"\n  resolution_round: 9\n\n- id: R6-N1\n  summary: \"Two-channel decomposition 概念贡献有限 — Findings-level\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"D051 W4: 4 contributions rewritten\"\n  resolution_round: 9\n\n- id: MW2\n  summary: \"Pairwise r²=1.3-1.7% 到 batch R²=22% 聚合: conditioning bias\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"simulation → illustrative; R²=0.218 primary\"\n  resolution_round: 9\n\n- id: R5-W1\n  summary: \"FewRel train+val 合并 — data contamination 风险\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Split-origin covariate confirms BCS partial effect unchanged\"\n  resolution_round: 9\n\n- id: R5-N1\n  summary: \"SCS novelty — metric 与 LLM-PEE 形式相同\"\n  category: framing\n  severity: warning\n  status: resolved\n  resolution: \"Contribution #2 reframed as empirical validation\"\n  resolution_round: 9\n\n- id: R6-W1\n  summary: \"'首次 controlled study' 声称需限定\"\n  category: framing\n  severity: warning\n  status: resolved\n  resolution: \"'To our knowledge' added\"\n  resolution_round: 9\n\n- id: R6-N2\n  summary: \"正文可能超过 8 页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"编译确认 Conclusion 在 p8\"\n  resolution_round: 9\n\n- id: R10-PS\n  summary: \"Prompt sensitivity 实验结果需整合入论文\"\n  category: experiment\n  severity: warning\n  status: resolved\n  resolution: \"Prompt sensitivity results integrated into §4.3 + Appendix H\"\n  resolution_round: 11\n\n- id: R12-W5\n  summary: \"Orphan bib entries\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"Orphan entries 已删除\"\n  resolution_round: 13\n\n- id: R10-m1\n  summary: \"Cross-seed variance (2.7pp at count 16) 与 typical effect (2.2pp) 量级相当\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - {round: 14, reviewers: [], note: \"R14 未直接提及; greedy decoding + FP8 non-determinism 已在 §3.4 说明\"}\n  resolution: \"§3.4 说明 greedy decoding 残余 SD=0.88pp 归因于 FP8 quantization non-determinism\"\n  resolution_round: 14\n\n- id: R13-W2\n  summary: \"BCS > 0.59 阈值缺乏 formal derivation\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - {round: 13, reviewers: [R1, R2], note: \"建议删除\"}\n    - {round: 14, reviewers: [], note: \"本轮未直接提及\"}\n  action_items:\n    - {round: 13, action: \"删除 0.59 阈值\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-m1\n  summary: \"Abstract 偏短 (~130-140 words)\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 13\n  resolution: \"升级追踪于 R13-W4; R14 评价 ~170 words 在范围内\"\n  resolution_round: 14\n"
  }
}
```

</details>

---


### Tool result

_source line 1353 · 2026-05-18T04:32:08.918200+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml\", \"bytes\": 26379}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 1354 · 2026-05-18T04:34:15.022137+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 14 审稿报告 — schema-dag-extraction\n\n**论文**: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**截止日期**: 2026-05-25\n**Reviewer 编排**: R1（方法严谨性）+ R2（新颖性/完整性），1 轮独立审稿 + 1 轮交叉回应\n**审稿模式**: Fresh（重新审稿，无历史轮次记忆）\n\n---\n\n## Summary\n\n本文研究 training-free LLM 信息抽取中 schema 复杂度对性能的影响，将退化分解为两个维度：type count（数量导致 recall 下降，最高 −49pp）和 confusability（语义相似度导致 type substitution，典型 batch 约 2.2pp）。通过 SCS/BCS 指标量化 confusability，在 NER (Few-NERD)、RE (FewRel/DocRED)、ED (MAVEN) 上进行受控实验。BCS 在 RE 上解释 22-53% 跨 batch 精度方差但在 NER 上无 batch 级信号；schema 分解因 merge amplification 和 routing failure 而失败。\n\n---\n\n## Strengths\n\n**[S1] 实验设计精巧，count/confusability 隔离方法有方法论贡献** [共识]\nBCS-controlled 实验（固定 count 变化 BCS）有效隔离两个维度，within-pool 分析进一步控制 pool composition confound（permutation p=0.60）。这个设计范式对后续 schema complexity 研究有参考价值。\n\n**[S2] 统计分析在 NLP 领域中异常全面** [共识]\nTOST equivalence testing、permutation tests、bootstrap CIs（pair-level B=10,000）、cluster bootstrap、Jonckheere-Terpstra trend test、variance decomposition、partial correlation。多层次 robustness checks（4 种 prompt variants、2 种 embeddings、name-only vs name+definition ablation、cross-seed decomposition）系统性覆盖 potential confounds。\n\n**[S3] 负面结果诚实且有诊断深度** [共识]\nSDGD 失败不是简单的\"不 work\"报告，而是诊断了 merge amplification（NER, precision 0.563→0.210）和 routing failure（RE）两种不同机制，并量化了 oracle upper bound (+29.8pp)。NER batch-level null result 也未被掩盖。\n\n**[S4] Limitations section 详尽** [共识]\n8 条 limitations + multiple comparisons 讨论，覆盖 model coverage、effect size、factorial interaction、causal mechanism、data contamination 等。在 NLP 论文中属于极少见的自我审视深度。\n\n**[S5] 跨任务不对称性发现有洞察价值** [共识]\nNER 和 RE 对 confusability 的响应模式截然不同（RE 有 batch 级信号，NER 没有），boundary detection failure 的解释有说服力。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**[N1] \"BCS explains 22-53% of cross-batch variance\" claim 范围过宽且 DocRED R² 稳定性未验证** [R1 critical, R2 AGREE]\n- 53% 来自 DocRED 仅 n=25 batches，未报告 adjusted R² 和 bootstrap CI，小样本 R² 天然上偏\n- NER batch-level R²≈0，但 Abstract \"22-53%\" 的区间表述暗示跨任务 generality\n- 22% R² 对应 typical-batch gap 仅 2.2pp (CI [0.4, 4.0])，presentation 暗示 strong predictive power 但实际 accuracy difference 很小\n- **要求**: (1) 报告 DocRED R² 的 adjusted R² 和 bootstrap CI; (2) Abstract/Introduction 明确限定为 \"RE accuracy variance\"; (3) 讨论 R²=0.22 对应 2.2pp 的 practical significance\n\n**[N2] TOST linear/logit scale 不一致性未充分解决** [R1 critical→R2 降级为 major; 最终评定: major-to-critical]\n- Linear-scale TOST p=0.003 (equivalence) vs logit-scale TOST p=0.209 (inconclusive)\n- 高 BCS batch accuracy 集中在 ~51%，接近 50% 时 linear scale 系统性压缩 interaction effects，logit scale 是更合适的分析尺度\n- Logit-scale 90% CI 上界 (0.203) 超过 equivalence bound (0.156)，不是 \"limited power\" 能解释的\n- Linear-scale 作为 primary test 缺乏 a priori justification\n- R2 观点: bounded association 是 supporting claim 非核心，双维度主效应不受影响，因此 severity 应为 major\n- **要求**: (1) 提供 logit-scale formal power analysis; (2) 或弱化 claim 为 \"bounded under primary linear specification; inconclusive on logit scale\"; (3) 讨论 scale choice rationale\n\n### Should-Fix（影响评分）\n\n**[W1] SCS/BCS 指标新颖性不足，与 LLM-PEE 差异化不清晰** [R2 major, R1 AGREE]\n- SCS = pairwise cosine similarity of type name embeddings，与 LLM-PEE partitioning criterion 形式相同\n- Abstract/Contribution #1-2 以 SCS/BCS 为核心卖点，与 Related Work 中自我定位（\"contribution is not the metric itself\"）不一致\n- 实际增量在于 BCS-controlled 实验范式（experimental framework），而非 metric 本身\n- **要求**: Contribution 措辞从 metric-centric 转向 framework-centric; §3.2 \"We introduce\" → \"We operationalize\"\n\n**[W2] Confusability 效应量过小 (~2pp)，extreme-batch 叙事权重过高** [R2 major, R1 PARTIALLY AGREE]\n- Typical-batch gap 2.2pp vs extreme-batch 25-31pp；count 效应 −49pp\n- Introduction/Results 叙事偏向 extreme-batch 数字，typical gap 被弱化\n- R1 辩护：analytical study 中 small but real effect 可接受；R2 认为需更有力论证 practical significance\n- **共识**: 不构成 rejection 理由，但 Abstract/Introduction 应前置 typical-batch magnitude，extreme-batch 仅作对比锚点\n\n**[W3] 因果语言残余** [R2 major (partial), R1 PARTIALLY AGREE]\n- \"schema-induced degradation\" 全文多处出现，超出 correlational + controlled stratification 证据\n- Title \"predict\" 合适，但正文 \"schema-induced\" 应改 \"schema-associated\"\n- R² \"explains\" 在统计学中不暗示因果（R1 REBUT R2），但 \"schema-induced\" 确实超越\n- Appendix 残余 \"count-driven\" / \"BCS-driven\" 未清理\n- **要求**: 全文 grep \"schema-induced\" 替换; Appendix 因果语言清零\n\n**[W4] 跨模型 generality claim 超出证据** [R1 major, R2 AGREE]\n- \"fundamental property of in-context learning\" 仅验证了 3 families (Qwen/LLaMA/Gemini)\n- Dimension 2 仅在 open-weight RE 上充分验证，Gemini 仅验证 Dimension 1\n- 无 closed-source frontier model (GPT-4/Claude) 的 Dimension 2 验证\n- **要求**: 弱化为 \"consistent across tested model families, suggesting but not establishing generality\"\n\n**[W5] FewRel constrained decoding 格式特殊性讨论不足** [R1 major, R2 AGREE with nuance]\n- Constrained decoding 消除 calibration signal，confusability 效应可能被 forced-choice 放大\n- Limitations item 6 仅一句话，正文讨论不足\n- R2 nuance: constrained decoding 对 RE closed-set classification 合理；NER unconstrained 结果提供自然对照\n- **共识**: 不需重做实验，但正文需讨论 constrained decoding 对 effect size 的影响\n\n**[W6] SDGD 分析深度不足** [R2 major, R1 PARTIALLY AGREE]\n- Merge amplification 无 k 值与 FP 增长的定量分析\n- Routing failure 无 error case analysis\n- R1 认为作为负面结果深度已可接受，但补充分析是 reasonable suggestion\n- **共识**: minor-to-major; 作为 Contribution #4 需更深入分析\n\n### 小问题\n\n- **[m1]** MAVEN 应降级为 supplementary dataset——\"four datasets\" 声称中 MAVEN 参与度弱 [R2-W6, R1 AGREE]\n- **[m2]** Abstract \"up to −49pp\" 来自 DocRED 非主实验，有 cherry-picking 最大数字嫌疑 [R1]\n- **[m3]** Abstract \"the gap\" 指代不明——应改为 \"the confusability gap\" [R2-Q5, R1 AGREE]\n- **[m4]** Introduction Finding (1) 过于密集（56 词复合句）[R12-N1 遗留]\n- **[m5]** TOST 术语首次出现未展开 [R11-W2 遗留]\n- **[m6]** Introduction findings vs contributions 数量不对齐 [R12-W4 遗留]\n- **[m7]** DocRED/MAVEN 5 batches vs FewRel/Few-NERD 25 batches 不对称未解释 [R1-W7]\n- **[m8]** Conclusion 偏短，缺 future work 和 broader implications [R11-W1 遗留]\n- **[m9]** NER U-shape \"dual-task burden\" 解释标注为 hypothesis [R10-m2 遗留]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **实验设计是本文最大优势** — 双 Reviewer 独立认定 BCS-controlled 实验范式有方法论价值\n2. **\"22-53% variance\" 需限定为 RE-specific** — NER batch-level R²=0 不应被 Abstract 的 framing 掩盖\n3. **跨模型 generality claim 过强** — \"fundamental property of in-context learning\" 需弱化\n4. **SCS/BCS 增量在 experimental framework 而非 metric** — Contribution 需 reframe\n5. **因果语言需继续清理** — \"schema-induced\" → \"schema-associated\"\n6. **Typical-batch 2.2pp 应前置于叙事** — extreme-batch 数字仅作对比锚点\n7. **Constrained decoding 边界条件需在正文讨论** — 不仅限 Limitations 一句话\n8. **Limitations section 和负面结果报告是罕见优点** — 学术诚信值得肯定\n\n## Reviewer Divergence [REBUT]\n\n1. **TOST 严重程度**: R1 评 critical（动摇核心 claim），R2 评 major（supporting analysis 非核心支柱）。**Director 判定**: major-to-critical——bounded association 不是唯一核心 claim，但作为论文框架的关键组件，其不确定性需要在正文中 prominently 呈现。\n2. **NER Contribution #3 独立性**: R1 认为 task-dependent diagnosis 有独立分析价值（pairwise signal 存在但不 aggregate 的现象值得独立报告）；R2 认为应并入 Contribution #2。**Director 判定**: 保留为独立 contribution 但需改 framing——强调诊断性发现。\n3. **\"First controlled study\" 声称**: R1 认为限定足够（qualified by \"to our knowledge\" + specific scope）；R2 认为 LLM-PEE 和 PARSE 已隐式涉及。**Director 判定**: 当前限定可接受，无需进一步修改。\n4. **R1-W5 Shared-representation dependency**: R2 有效反驳——MiniLM 是 primary embedding（§3.2 明确说明），非 Qwen3。R1 的 \"circular dependency\" 前提部分有误。**Director 判定**: 此 weakness 降级为 info——MiniLM 与 Qwen3 是独立模型，不构成 circular dependency；confusion matrix correlation=0.894 更可能反映 confusability 是 schema 内在属性。\n\n---\n\n## Questions（需作者澄清）\n\n1. DocRED R²=0.525 (count 16) 的 adjusted R² 和 bootstrap CI 是多少？n=25 上的稳定性如何？\n2. FewRel pairwise SCS-confusion r=0.187（§3.2）的计算方法与 Table 2 有何不同？为什么 FewRel 被排除在 Table 2 之外？\n3. BCS-Controlled batch 构建如何控制 type difficulty 之外的因素（即 low-BCS ≠ trivially easy, high-BCS ≠ trivially hard）？\n4. Name-only SCS vs name+definition SCS 差异极小（Δr: −0.023 to +0.035）——这是否说明 SCS 捕获的是 name-level 表面相似度而非深层 semantic confusability？\n5. NER U-shape 在 RE 中不存在的原因？\"Dual-task burden\" 解释是否有额外证据支持？\n\n---\n\n## Missing References\n\nR1 和 R2 共同建议补充：\n1. Structured prediction calibration (Kuleshov & Liang 2015)\n2. Label embedding trees for hierarchical label space reduction (Bengio et al. 2010)\n3. KG relation schema complexity (Bordes et al. 2013 relation cardinality 分析)\n4. Label smoothing exploits inter-class similarity (Müller et al. 2019) — 已在 Related Work 引用\n5. GoLLIE (Sainz et al., ICLR 2024) — R2 提出但 R1 确认已引用 (gollie-2024)\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目配置未启用 `external_review.paperreview_ai.enabled`）。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**评分理由**:\n\n论文的实验设计和统计分析在 NLP empirical study 中属于上乘水平，count/confusability 隔离的方法论有参考价值，负面结果报告诚实。然而：\n\n1. **Novelty 受限**: SCS/BCS 是标准 cosine similarity，与 LLM-PEE 形式相同；核心发现\"count 远比 confusability 重要\"在直觉上可预期\n2. **Effect size 小**: Confusability 的 typical-batch 效应仅 2.2pp，practical significance 有限\n3. **Claims 需收窄**: \"22-53% variance\" 需限定为 RE-specific + 报告 DocRED CI；\"fundamental property of in-context learning\" 超出 3-family 证据；TOST bounded association 在 logit scale 上 inconclusive\n4. **分析深度**: SDGD 负面结果和 constrained decoding 边界条件的讨论有提升空间\n\n作为 **Findings 论文**是合适的——方法论扎实，发现有参考价值，对 schema design practitioners 和后续研究者提供了有意义的 characterization。但 **excitement 和 novelty 不足以支撑主会议接收**——核心 confusability 效应太小，SCS 指标无增量，且主要 claim 需显著收窄。\n\n**Confidence: 4/5** — 两位 Reviewer 均仔细阅读全文及附录，熟悉 zero-shot IE、equivalence testing 和 schema complexity 文献。\n\n---\n\n## Rebuttal 建议重点\n\n如果作者进行 rebuttal/revision，以下是最能影响评分的修改：\n1. 报告 DocRED R² 的 bootstrap CI 并在 Abstract 限定为 \"RE\"（N1，可立即执行）\n2. 提供 logit-scale power analysis 或弱化 bounded association claim（N2，可立即执行）\n3. Contribution 重心从 SCS metric 转向 experimental framework（W1，revision 可修复）\n4. 正文讨论 constrained decoding 对 RE effect size 的影响（W5，revision 可修复）\n5. \"fundamental property\" → \"consistent across tested families\"（W4，一句话修改）\n\n上述 1-2 如能充分回应，评分可能上调至 3.5 (Borderline Conference)。\n\n---\n\n## 维度评分汇总\n\n| 维度 | R1 | R2 | 加权 |\n|------|-----|-----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.0 | 2.5 | 2.75 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Overall | 3.5 | 3.0 | **3.0** |\n\nOverall 取偏保守值（3.0）：Excitement 分歧（R1=3.0 vs R2=2.5）和 Novelty 评判（R2 更严格且有理有据）倾向于 Findings 而非 Borderline Conference。\n",
  "project": "schema-dag-extraction",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 14 审稿报告 — schema-dag-extraction\n\n**论文**: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**截止日期**: 2026-05-25\n**Reviewer 编排**: R1（方法严谨性）+ R2（新颖性/完整性），1 轮独立审稿 + 1 轮交叉回应\n**审稿模式**: Fresh（重新审稿，无历史轮次记忆）\n\n---\n\n## Summary\n\n本文研究 training-free LLM 信息抽取中 schema 复杂度对性能的影响，将退化分解为两个维度：type count（数量导致 recall 下降，最高 −49pp）和 confusability（语义相似度导致 type substitution，典型 batch 约 2.2pp）。通过 SCS/BCS 指标量化 confusability，在 NER (Few-NERD)、RE (FewRel/DocRED)、ED (MAVEN) 上进行受控实验。BCS 在 RE 上解释 22-53% 跨 batch 精度方差但在 NER 上无 batch 级信号；schema 分解因 merge amplification 和 routing failure 而失败。\n\n---\n\n## Strengths\n\n**[S1] 实验设计精巧，count/confusability 隔离方法有方法论贡献** [共识]\nBCS-controlled 实验（固定 count 变化 BCS）有效隔离两个维度，within-pool 分析进一步控制 pool composition confound（permutation p=0.60）。这个设计范式对后续 schema complexity 研究有参考价值。\n\n**[S2] 统计分析在 NLP 领域中异常全面** [共识]\nTOST equivalence testing、permutation tests、bootstrap CIs（pair-level B=10,000）、cluster bootstrap、Jonckheere-Terpstra trend test、variance decomposition、partial correlation。多层次 robustness checks（4 种 prompt variants、2 种 embeddings、name-only vs name+definition ablation、cross-seed decomposition）系统性覆盖 potential confounds。\n\n**[S3] 负面结果诚实且有诊断深度** [共识]\nSDGD 失败不是简单的\"不 work\"报告，而是诊断了 merge amplification（NER, precision 0.563→0.210）和 routing failure（RE）两种不同机制，并量化了 oracle upper bound (+29.8pp)。NER batch-level null result 也未被掩盖。\n\n**[S4] Limitations section 详尽** [共识]\n8 条 limitations + multiple comparisons 讨论，覆盖 model coverage、effect size、factorial interaction、causal mechanism、data contamination 等。在 NLP 论文中属于极少见的自我审视深度。\n\n**[S5] 跨任务不对称性发现有洞察价值** [共识]\nNER 和 RE 对 confusability 的响应模式截然不同（RE 有 batch 级信号，NER 没有），boundary detection failure 的解释有说服力。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**[N1] \"BCS explains 22-53% of cross-batch variance\" claim 范围过宽且 DocRED R² 稳定性未验证** [R1 critical, R2 AGREE]\n- 53% 来自 DocRED 仅 n=25 batches，未报告 adjusted R² 和 bootstrap CI，小样本 R² 天然上偏\n- NER batch-level R²≈0，但 Abstract \"22-53%\" 的区间表述暗示跨任务 generality\n- 22% R² 对应 typical-batch gap 仅 2.2pp (CI [0.4, 4.0])，presentation 暗示 strong predictive power 但实际 accuracy difference 很小\n- **要求**: (1) 报告 DocRED R² 的 adjusted R² 和 bootstrap CI; (2) Abstract/Introduction 明确限定为 \"RE accuracy variance\"; (3) 讨论 R²=0.22 对应 2.2pp 的 practical significance\n\n**[N2] TOST linear/logit scale 不一致性未充分解决** [R1 critical→R2 降级为 major; 最终评定: major-to-critical]\n- Linear-scale TOST p=0.003 (equivalence) vs logit-scale TOST p=0.209 (inconclusive)\n- 高 BCS batch accuracy 集中在 ~51%，接近 50% 时 linear scale 系统性压缩 interaction effects，logit scale 是更合适的分析尺度\n- Logit-scale 90% CI 上界 (0.203) 超过 equivalence bound (0.156)，不是 \"limited power\" 能解释的\n- Linear-scale 作为 primary test 缺乏 a priori justification\n- R2 观点: bounded association 是 supporting claim 非核心，双维度主效应不受影响，因此 severity 应为 major\n- **要求**: (1) 提供 logit-scale formal power analysis; (2) 或弱化 claim 为 \"bounded under primary linear specification; inconclusive on logit scale\"; (3) 讨论 scale choice rationale\n\n### Should-Fix（影响评分）\n\n**[W1] SCS/BCS 指标新颖性不足，与 LLM-PEE 差异化不清晰** [R2 major, R1 AGREE]\n- SCS = pairwise cosine similarity of type name embeddings，与 LLM-PEE partitioning criterion 形式相同\n- Abstract/Contribution #1-2 以 SCS/BCS 为核心卖点，与 Related Work 中自我定位（\"contribution is not the metric itself\"）不一致\n- 实际增量在于 BCS-controlled 实验范式（experimental framework），而非 metric 本身\n- **要求**: Contribution 措辞从 metric-centric 转向 framework-centric; §3.2 \"We introduce\" → \"We operationalize\"\n\n**[W2] Confusability 效应量过小 (~2pp)，extreme-batch 叙事权重过高** [R2 major, R1 PARTIALLY AGREE]\n- Typical-batch gap 2.2pp vs extreme-batch 25-31pp；count 效应 −49pp\n- Introduction/Results 叙事偏向 extreme-batch 数字，typical gap 被弱化\n- R1 辩护：analytical study 中 small but real effect 可接受；R2 认为需更有力论证 practical significance\n- **共识**: 不构成 rejection 理由，但 Abstract/Introduction 应前置 typical-batch magnitude，extreme-batch 仅作对比锚点\n\n**[W3] 因果语言残余** [R2 major (partial), R1 PARTIALLY AGREE]\n- \"schema-induced degradation\" 全文多处出现，超出 correlational + controlled stratification 证据\n- Title \"predict\" 合适，但正文 \"schema-induced\" 应改 \"schema-associated\"\n- R² \"explains\" 在统计学中不暗示因果（R1 REBUT R2），但 \"schema-induced\" 确实超越\n- Appendix 残余 \"count-driven\" / \"BCS-driven\" 未清理\n- **要求**: 全文 grep \"schema-induced\" 替换; Appendix 因果语言清零\n\n**[W4] 跨模型 generality claim 超出证据** [R1 major, R2 AGREE]\n- \"fundamental property of in-context learning\" 仅验证了 3 families (Qwen/LLaMA/Gemini)\n- Dimension 2 仅在 open-weight RE 上充分验证，Gemini 仅验证 Dimension 1\n- 无 closed-source frontier model (GPT-4/Claude) 的 Dimension 2 验证\n- **要求**: 弱化为 \"consistent across tested model families, suggesting but not establishing generality\"\n\n**[W5] FewRel constrained decoding 格式特殊性讨论不足** [R1 major, R2 AGREE with nuance]\n- Constrained decoding 消除 calibration signal，confusability 效应可能被 forced-choice 放大\n- Limitations item 6 仅一句话，正文讨论不足\n- R2 nuance: constrained decoding 对 RE closed-set classification 合理；NER unconstrained 结果提供自然对照\n- **共识**: 不需重做实验，但正文需讨论 constrained decoding 对 effect size 的影响\n\n**[W6] SDGD 分析深度不足** [R2 major, R1 PARTIALLY AGREE]\n- Merge amplification 无 k 值与 FP 增长的定量分析\n- Routing failure 无 error case analysis\n- R1 认为作为负面结果深度已可接受，但补充分析是 reasonable suggestion\n- **共识**: minor-to-major; 作为 Contribution #4 需更深入分析\n\n### 小问题\n\n- **[m1]** MAVEN 应降级为 supplementary dataset——\"four datasets\" 声称中 MAVEN 参与度弱 [R2-W6, R1 AGREE]\n- **[m2]** Abstract \"up to −49pp\" 来自 DocRED 非主实验，有 cherry-picking 最大数字嫌疑 [R1]\n- **[m3]** Abstract \"the gap\" 指代不明——应改为 \"the confusability gap\" [R2-Q5, R1 AGREE]\n- **[m4]** Introduction Finding (1) 过于密集（56 词复合句）[R12-N1 遗留]\n- **[m5]** TOST 术语首次出现未展开 [R11-W2 遗留]\n- **[m6]** Introduction findings vs contributions 数量不对齐 [R12-W4 遗留]\n- **[m7]** DocRED/MAVEN 5 batches vs FewRel/Few-NERD 25 batches 不对称未解释 [R1-W7]\n- **[m8]** Conclusion 偏短，缺 future work 和 broader implications [R11-W1 遗留]\n- **[m9]** NER U-shape \"dual-task burden\" 解释标注为 hypothesis [R10-m2 遗留]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **实验设计是本文最大优势** — 双 Reviewer 独立认定 BCS-controlled 实验范式有方法论价值\n2. **\"22-53% variance\" 需限定为 RE-specific** — NER batch-level R²=0 不应被 Abstract 的 framing 掩盖\n3. **跨模型 generality claim 过强** — \"fundamental property of in-context learning\" 需弱化\n4. **SCS/BCS 增量在 experimental framework 而非 metric** — Contribution 需 reframe\n5. **因果语言需继续清理** — \"schema-induced\" → \"schema-associated\"\n6. **Typical-batch 2.2pp 应前置于叙事** — extreme-batch 数字仅作对比锚点\n7. **Constrained decoding 边界条件需在正文讨论** — 不仅限 Limitations 一句话\n8. **Limitations section 和负面结果报告是罕见优点** — 学术诚信值得肯定\n\n## Reviewer Divergence [REBUT]\n\n1. **TOST 严重程度**: R1 评 critical（动摇核心 claim），R2 评 major（supporting analysis 非核心支柱）。**Director 判定**: major-to-critical——bounded association 不是唯一核心 claim，但作为论文框架的关键组件，其不确定性需要在正文中 prominently 呈现。\n2. **NER Contribution #3 独立性**: R1 认为 task-dependent diagnosis 有独立分析价值（pairwise signal 存在但不 aggregate 的现象值得独立报告）；R2 认为应并入 Contribution #2。**Director 判定**: 保留为独立 contribution 但需改 framing——强调诊断性发现。\n3. **\"First controlled study\" 声称**: R1 认为限定足够（qualified by \"to our knowledge\" + specific scope）；R2 认为 LLM-PEE 和 PARSE 已隐式涉及。**Director 判定**: 当前限定可接受，无需进一步修改。\n4. **R1-W5 Shared-representation dependency**: R2 有效反驳——MiniLM 是 primary embedding（§3.2 明确说明），非 Qwen3。R1 的 \"circular dependency\" 前提部分有误。**Director 判定**: 此 weakness 降级为 info——MiniLM 与 Qwen3 是独立模型，不构成 circular dependency；confusion matrix correlation=0.894 更可能反映 confusability 是 schema 内在属性。\n\n---\n\n## Questions（需作者澄清）\n\n1. DocRED R²=0.525 (count 16) 的 adjusted R² 和 bootstrap CI 是多少？n=25 上的稳定性如何？\n2. FewRel pairwise SCS-confusion r=0.187（§3.2）的计算方法与 Table 2 有何不同？为什么 FewRel 被排除在 Table 2 之外？\n3. BCS-Controlled batch 构建如何控制 type difficulty 之外的因素（即 low-BCS ≠ trivially easy, high-BCS ≠ trivially hard）？\n4. Name-only SCS vs name+definition SCS 差异极小（Δr: −0.023 to +0.035）——这是否说明 SCS 捕获的是 name-level 表面相似度而非深层 semantic confusability？\n5. NER U-shape 在 RE 中不存在的原因？\"Dual-task burden\" 解释是否有额外证据支持？\n\n---\n\n## Missing References\n\nR1 和 R2 共同建议补充：\n1. Structured prediction calibration (Kuleshov & Liang 2015)\n2. Label embedding trees for hierarchical label space reduction (Bengio et al. 2010)\n3. KG relation schema complexity (Bordes et al. 2013 relation cardinality 分析)\n4. Label smoothing exploits inter-class similarity (Müller et al. 2019) — 已在 Related Work 引用\n5. GoLLIE (Sainz et al., ICLR 2024) — R2 提出但 R1 确认已引用 (gollie-2024)\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目配置未启用 `external_review.paperreview_ai.enabled`）。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**评分理由**:\n\n论文的实验设计和统计分析在 NLP empirical study 中属于上乘水平，count/confusability 隔离的方法论有参考价值，负面结果报告诚实。然而：\n\n1. **Novelty 受限**: SCS/BCS 是标准 cosine similarity，与 LLM-PEE 形式相同；核心发现\"count 远比 confusability 重要\"在直觉上可预期\n2. **Effect size 小**: Confusability 的 typical-batch 效应仅 2.2pp，practical significance 有限\n3. **Claims 需收窄**: \"22-53% variance\" 需限定为 RE-specific + 报告 DocRED CI；\"fundamental property of in-context learning\" 超出 3-family 证据；TOST bounded association 在 logit scale 上 inconclusive\n4. **分析深度**: SDGD 负面结果和 constrained decoding 边界条件的讨论有提升空间\n\n作为 **Findings 论文**是合适的——方法论扎实，发现有参考价值，对 schema design practitioners 和后续研究者提供了有意义的 characterization。但 **excitement 和 novelty 不足以支撑主会议接收**——核心 confusability 效应太小，SCS 指标无增量，且主要 claim 需显著收窄。\n\n**Confidence: 4/5** — 两位 Reviewer 均仔细阅读全文及附录，熟悉 zero-shot IE、equivalence testing 和 schema complexity 文献。\n\n---\n\n## Rebuttal 建议重点\n\n如果作者进行 rebuttal/revision，以下是最能影响评分的修改：\n1. 报告 DocRED R² 的 bootstrap CI 并在 Abstract 限定为 \"RE\"（N1，可立即执行）\n2. 提供 logit-scale power analysis 或弱化 bounded association claim（N2，可立即执行）\n3. Contribution 重心从 SCS metric 转向 experimental framework（W1，revision 可修复）\n4. 正文讨论 constrained decoding 对 RE effect size 的影响（W5，revision 可修复）\n5. \"fundamental property\" → \"consistent across tested families\"（W4，一句话修改）\n\n上述 1-2 如能充分回应，评分可能上调至 3.5 (Borderline Conference)。\n\n---\n\n## 维度评分汇总\n\n| 维度 | R1 | R2 | 加权 |\n|------|-----|-----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.0 | 2.5 | 2.75 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Overall | 3.5 | 3.0 | **3.0** |\n\nOverall 取偏保守值（3.0）：Excitement 分歧（R1=3.0 vs R2=2.5）和 Novelty 评判（R2 更严格且有理有据）倾向于 Findings 而非 Borderline Conference。\n",
    "project": "schema-dag-extraction",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)"
  }
}
```

</details>

---


### Tool result

_source line 1355 · 2026-05-18T04:34:19.546099+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_51326259fe46fbae9da26b81cf03f1f8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4523
}
```

</details>

---


### Assistant

_source line 1356 · 2026-05-18T04:34:27.919783+00:00_

Round 14 审稿完成。

**结果**: Overall **3.0 (Findings)**

**核心问题**:
- **N1** [must-fix]: "22-53% variance" claim 需限定为 RE-specific + 报告 DocRED R² 的 CI
- **N2** [must-fix]: TOST 在 logit scale 上 inconclusive，需 power analysis 或弱化 claim
- **W1-W6** [should-fix]: SCS 新颖性 framing、效应量叙事、因果语言、跨模型 claim、constrained decoding 讨论、SDGD 分析深度

**主要优势**: 实验设计精巧、统计分析异常严谨、负面结果诚实、Limitations 详尽

**评分逻辑**: 方法论扎实但 novelty 受限（SCS = 标准 cosine similarity）、confusability 效应过小（typical 2.2pp）、excitement 不足以支撑主会议。如 N1/N2 充分回应，可上调至 3.5。

审稿报告已投递至 Research Director，issue tracker 已同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 132

## Round 132

2 recorded events


### User

_source line 1357 · 2026-05-18T04:34:30.545291+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

**回应摘要**：

| R1 Issue | 我的判断 | 关键理由 |
|----------|--------|--------|
| W1 TOST 不一致 | **AGREE**（降为 major） | logit-scale inconclusive 是真实问题，但不动摇整个双维度框架 |
| W2 R² claim 过宽 | **AGREE** | 53% 来自 n=25 小样本，NER 完全 null，Abstract 应限定为 RE |
| W3 generality claim | **AGREE** | 3 个 model family 不够支撑 "fundamental property" |
| W4 constrained decoding | **AGREE with nuance** | 可能放大效应，但 RE closed-set 设定下 constrained decoding 是合理选择 |
| W5 circular dependency | **REBUT** | R1 误读了 primary embedding：论文用 MiniLM 而非 Qwen3，不存在 circular dependency |
| W6 3 seeds | **AGREE**（minor） | 效应量远大于 seed variance |
| W7 batch 不对称 | **AGREE**（minor） | editorial issue |

R1 给 3.5 vs 我给 3.0，差异主要在于我对 SCS 新颖性和 ~2pp 效应量的 practical significance 更 skeptical。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1358 · 2026-05-18T04:34:39.647182+00:00_

审稿报告已投递完成。

**Round 14 审稿结论**:

- **Overall Score: 3.0 (Findings)**
- R1: 3.5 (Borderline Conference), R2: 3.0 (Findings)，取偏保守值
- **2 个 Must-Fix**: (1) "22-53% variance" 需限定为 RE + 报告 DocRED CI; (2) TOST logit-scale 不一致需正面处理
- **6 个 Should-Fix**: SCS novelty reframe、effect size 叙事调整、因果语言清理、跨模型 claim 弱化、constrained decoding 讨论、SDGD 分析深度
- **9 个小问题**

Issue Tracker 已同步更新至 `artifacts/review_issues.yaml`（Round 14）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 133

## Round 133

154 recorded events


### User

_source line 1359 · 2026-05-18T05:22:03.035476+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema-dag-extraction
- 论文路径: projects/schema-dag-extraction/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1360 · 2026-05-18T05:22:09.204471+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1361 · 2026-05-18T05:22:09.255547+00:00_

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
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1362 · 2026-05-18T05:22:13.642817+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1363 · 2026-05-18T05:22:13.793907+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1364 · 2026-05-18T05:22:16.817014+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 1365 · 2026-05-18T05:22:17.219239+00:00_

{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (60 个)\n\n- **exp012_llama_8b_r2_exp2**: DONE (negative) — \n- **exp012_llama_8b_r2**: DONE (success) — \n- **exp006_interaction_2x2**: DONE (negative) — \n- **exp012_llama_awq**: DONE (killed) — \n- **exp012_llama_8b_r3**: DONE (failed) — \n- **exp012_llama_8b**: DONE (killed) — \n- **exp_fewrel_40rel_r3**: DONE (failed) — \n- **exp_fewrel_40rel_r2**: DONE (failed) — \n- **exp012_llama_fewnerd_r4**: DONE (failed) — \n- **exp012_llama_8b_fewnerd**: DONE (failed) — \n- **exp_fewrel_40rel**: DONE (failed) — \n- **exp012_llama_fewnerd_r3**: DONE (failed) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- prompt_sensitivity（准备中）\n- prompt_sensitivity_dry4（准备中）\n- prompt_sensitivity_dry3（准备中）\n- prompt_sensitivity_dry2（准备中）\n- prompt_sensitivity_dry（准备中）\n- exp_aggregation_monte_carlo（准备中）\n- exp_scs_name_def_ablation（准备中）\n- exp_fewrel_contamination_check（准备中）\n- exp017_gpt4o_mini_fewrel（准备中）\n- exp_cross_embedding_sensitivity（准备中）\n- …另有 2 项\n\n## 近期结论\n- **exp_gemini_flash_cross_model** (failed): The two-dimensional degradation pattern (count-related decline + confusability-related type confusion) generalizes beyond open-weight models to proprietary API models. Gemini 2.5 Flash should show: (1) monotonic RE accuracy decline with count, and (2) significant BCS-accuracy correlation on extreme batches. If confirmed, the pattern is architecture-family-independent (open-weight Qwen/LLaMA + proprietary Gemini).\n- **exp_schema_intervention** (negative): If type confusability is a causal driver of extraction errors, then renaming high-BCS type pairs to reduce embedding similarity (while preserving semantic equivalence) should improve accuracy on high-BCS batches. This tests the causal direction: SCS → confusion, not merely corre
…[truncated 1823 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1366 · 2026-05-18T05:22:17.370501+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
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

_source line 1367 · 2026-05-18T05:22:17.370952+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1368 · 2026-05-18T05:22:21.640455+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 call for papers author guidelines submission format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 call for papers author guidelines submission format"
  }
}
```

</details>

---


### Tool call

_source line 1369 · 2026-05-18T05:22:22.143229+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline commitment deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline commitment deadline"
  }
}
```

</details>

---


### Tool call

_source line 1370 · 2026-05-18T05:22:24.051337+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1371 · 2026-05-18T05:22:24.554879+00:00_

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
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B, 70B-Instruct (FP8), and Gemini 2.5 Flash (API). Dimension~1 (count-associated decline) has been validated on a proprietary model (Gemini 2.5 Flash, $\rho = -0.900$, $p = 0.037$; Appendix~\ref{sec:appendix_cross_model_gemini}); Dimension~2 (confusability-associated type substitution) has been verified only on open-weight models. Dimension~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
41	
42	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
43	
44	\item \textbf{Factorial interaction tests.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\ref{sec:appendix_factorial}). However, a FewRel factorial with TOST equivalence testing confirms bounded association ($p_{\text{TOST}} = 0.003$ at $\pm 3$\,pp, interaction = 0.47\,pp; Appendix~\ref{sec:appendix_factorial}), and cross-pool slope consistency ($p = 0.60$) corroborates stable rat
…[truncated 12851 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 1372 · 2026-05-18T05:22:24.605563+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "literature_map.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "literature_map.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1373 · 2026-05-18T05:22:27.672487+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline commitment deadline"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp
…[truncated 1135 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 5529
}
```

</details>

---


### Tool result

_source line 1374 · 2026-05-18T05:22:28.829158+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 call for papers author guidelines submission format"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the web search results, here's information about ACL Rolling Review (ARR) 2026 call for papers, author guidelines, and submission format:

## Call for Papers

ACL Rolling Review (ARR) invites the submission of long and short papers on substantial, original, and unpublished research in all aspects of Computational Linguistics and Natural Language Processing.

## Author Guidelines

All submitted papers are 
…[truncated 1181 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 7188
}
```

</details>

---


### Tool result

_source line 1375 · 2026-05-18T05:22:28.829690+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml\", \"content\": \"# Literature Map for schema-dag-extraction\\n# Updated: 2026-05-15\\n# Paper: Multi-channel Degradation Model + SDGD Framework for Training-free LLM IE\\n\\n# =============================================================================\\n# DIRECT COMPETITORS — schema decomposition for LLM-based IE\\n# =============================================================================\\n\\n- id: llm-pee-2025\\n  title: \\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\"\\n  year: 2025\\n  venue: arXiv\\n  url: https://arxiv.org/abs/2503.02628\\n  role: direct-competitor\\n  relevance_note: >\\n    Similarity-based type recall + type-partitioning prompting for massive event types.\\n    Divides candidate types into partitions to reduce prompt length.\\n    +5.4% event detection, +6.1% argument extraction, +12.9% F1 over mainstream LLMs zero-shot.\\n    KEY DIFF: partitions by similarity-based recall, NOT confusability-aware.\\n    Our DAG decomposition is confusability-driven, not just similarity-driven.\\n\\n- id: parse-2025\\n  title: \\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\"\\n  authors: [Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla]\\n  year: 2025\\n  venue: EMNLP 2025 Industry\\n  url: https://arxiv.org/abs/2510.08623\\n  role: direct-competitor\\n  relevance_note: >\\n    ARCHITECT autonomously rewrites JSON schemas for LLM consumption.\\n    SCOPE uses reflection-based extraction with guardrails. +64.7% on SWDE.\\n    Treats schema optimization as black-box LLM rewriting, not principled decomposition.\\n    Does NOT model type confusability explicitly.\\n\\n- id: dee-2024\\n  title: \\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\"\\n  year: 2024\\
…[truncated 3590 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 4224
}
```

</details>

---


### Tool call

_source line 1376 · 2026-05-18T05:22:33.601399+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "200"
  }
}
```

</details>

---


### Tool result

_source line 1377 · 2026-05-18T05:22:34.053834+00:00_

200	\midrule
201	$\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\
202	$\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\
203	$\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\
204	$\pm 5$ & $-5.02$ & ${<}\,0.001$ & Equivalent \\
205	\bottomrule
206	\end{tabular}
207	\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\,pp, 90\% CI [$-$1.0, 2.0]\,pp) is bounded below 2\,pp at marginal significance ($p = 0.047$), confirming that the $\pm 3$\,pp choice does not drive the equivalence conclusion. At $\pm 1$\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}
208	\label{tab:tost_sensitivity}
209	\end{table}
210	
211	\paragraph{Logit-scale sensitivity.}
212	Because accuracy near 50\% compresses interaction effects on the linear scale, we refit the regression on logit-transformed accuracy. The logit-scale interaction (0.111 logit units, $p = 0.047$, 90\% CI [0.019, 0.203]) is marginally significant, and TOST at the equivalent $\pm 3$\,pp margin ($\pm 0.156$ logit at median accuracy) is inconclusive ($p_{\text{TOST}} = 0.209$). However, back-transforming the interaction to the probability scale at the observed floor ($p = 0.51$) yields 2.78\,pp, still within the $\pm 3$\,pp margin; at the median baseline ($p = 0.65$), the back-transformed effect is 2.53\,pp. The logit TOST is inconclusive due to limited power ($n = 69$, wide CI) rather than a large effect size: the point estimate remains below the equivalence bound at all observed baselines. We retain the linear-scale TOST as the primary test and report this logit analysis as a sensitivity check.
213	
214	\section{Within-Pool CI Details}
215	\label{sec:appendix_within_pool}
216	
217	The quartile $\Delta$ for 80-pool 16-relation subsets ($-$3.92\,pp, 95\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\ 0.48--0.71 for the independent pool). Within this narrow band, the quar
…[truncated 33988 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1378 · 2026-05-18T05:22:34.054263+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1379 · 2026-05-18T05:22:34.556441+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1380 · 2026-05-18T05:22:35.009097+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1381 · 2026-05-18T05:22:35.059705+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'schema-dag-extraction'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1382 · 2026-05-18T05:22:38.976567+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1383 · 2026-05-18T05:22:39.480224+00:00_

1	\begin{abstract}
2	As large language models are increasingly deployed for information extraction without task-specific training, understanding how schema design affects extraction quality becomes critical for reliable deployment. Training-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: having more types (count) and having semantically similar types (confusability). We present the first controlled study isolating these factors across NER, RE, and event detection on four datasets and operationalize confusability via the Schema Confusability Score (SCS) and its batch-level aggregation (BCS). Degradation operates along two dimensions: count-related recall decline (up to $-$49\,pp, document-level RE at full schema) dominates confusability-related type substitution (${\approx}\,2.2$\,pp in typical batches); BCS explains 22--53\% of cross-batch RE accuracy variance but not NER, where boundary detection failures overwhelm the signal. Few-shot demonstrations do not reduce the confusability gap (+4.3\,pp under 5-shot). Schema decomposition fails due to merge amplification (NER) and routing failure (RE). These patterns replicate across model scales (8B to 70B) and architecture families (Qwen, LLaMA, Gemini), which suggests schema-associated degradation is consistent across tested model families rather than a model-specific artifact.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 1384 · 2026-05-18T05:22:39.480570+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1385 · 2026-05-18T05:22:39.932594+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance. Anonymous review materials: \url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 49.5\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accur
…[truncated 3254 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1386 · 2026-05-18T05:22:39.933131+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1387 · 2026-05-18T05:22:39.983692+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025,willard2023efficient}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, and bidirectional encoders \cite{gliner-2024,gliner2-2025}. For RE, recent work examines zero-shot relation triplet extraction via prompting \cite{relationprompt-2022} and revisits relation extraction in the LLM era \cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. LLM-PEE's union merge suffers the same precision collapse (0.56$\to$0.21 in NER) that our \S\ref{sec:sdgd} analysis identifies as the fundamental bottleneck. Other approaches address schema complexity via hard negative mining \cite{iepile-2024}, schema definition optimization \cite{parse-2025}, multi-agent debate \cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \cite{dee-2024}, and active prompting 
…[truncated 3002 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1388 · 2026-05-18T05:22:40.436134+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 1389 · 2026-05-18T05:22:40.938576+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains and is suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\sim$10 per type) from the DocRED development set and formulate th
…[truncated 8143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1390 · 2026-05-18T05:22:40.989252+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 1391 · 2026-05-18T05:22:41.844425+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	\begin{figure}[t]
10	\centering
11	\begin{minipage}[t]{0.48\columnwidth}
12	\centering
13	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
14	\end{minipage}
15	\hfill
16	\begin{minipage}[t]{0.48\columnwidth}
17	\centering
18	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
19	\end{minipage}
20	\caption{\textbf{(a)} Count-degradation curves for NER and RE. Error bars show $\pm 1$\,SD across 3 seeds (42, 123, 456) $\times$ 25 batches per seed. RE accuracy declines monotonically with count; NER recall exhibits a U-shaped pattern with minimum at intermediate counts. Full-schema points (rightmost, hollow markers) represent the complete type inventory with no batch sampling variance. \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}
21	\label{fig:main_results}
22	\end{figure}
23	
24	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}), ; schema configu
…[truncated 11051 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 1392 · 2026-05-18T05:22:41.844776+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 1393 · 2026-05-18T05:22:42.297776+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention against confusability-related degradation is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches.
5	
6	\paragraph{NER: merge amplification.}
7	All decomposition modes fall below the single-pass NER baseline (F1\,=\,0.445): SDGD obtains 0.251, random batching 0.320, per-type 0.292 (Appendix~\ref{sec:appendix_sdgd}). The core failure is \emph{merge amplification}: presenting text to the model $k$ times with different type subsets is associated with precision collapsing (0.563$\to$0.210--0.249) as false positives scale with $k$, while true positives remain bounded. Confidence gating does not recover net F1. RE avoids this failure because closed-set classification requires no span reconciliation across passes.
8	
9	\paragraph{RE: oracle routing.}
10	Oracle routing achieves 0.802 accuracy versus 0.504 single-pass on FewRel 80-relation RE (+29.8\,pp; Table~\ref{tab:batch_composition}); type separation thus recovers performance absent merge amplification. Confusability-aware grouping yields only +1.4\,pp over random ($p \approx 0.19$, n.s.); all practical routing strategies fall below the single-pass baseline because constrained decoding forces confident predictions in every sub-schema (Appendix~\ref{sec:appendix_routing}).
11	
12	\paragraph{Future directions.}
13	Three avenues may address these bottlenecks: (1)~coarse-to-fine pipelines that screen with the full schema then refine with targeted sub-schemas; (2)~retrieval-based routing using document retrieval rather than LLM confidence for sub-schema assignment; (3)~calibrated generation \citep{jagannatha2020calibrating} to recover confidence signals eliminated by constrained decoding.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\re
…[truncated 535 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1394 · 2026-05-18T05:22:42.298313+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1395 · 2026-05-18T05:22:42.750493+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-dimensional decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). The effect generalizes to document-level RE (DocRED slope $-$0.71, adjusted $R^2 = 0.51$, 95\% CI [0.27, 0.73]) and persists across prompt designs (Appendix~\ref{sec:appendix_prompt_sensitivity}). Dimension~1 replicates across scales (8B--70B); Dimension~2 attenuates on smaller models.
6	
7	\paragraph{Why does embedding similarity predict LLM confusion?}
8	SCS captures semantic proximity in LLMs' type-resolution space. The unconditional pairwise $R^2$ is modest (1.3\%) because ${\sim}89\%$ of type pairs never confuse; among the 11\% with nonzero confusion, conditional $R^2$ rises to 7\%. Correlated pair-level signals aggregate at batch level: a Monte Carlo simulation (Appendix~\ref{app:aggregation-sim}) predicts batch $R^2$ of 18--25\%, consistent with the observed 22--53\% in RE. SCS is thus a weak pair-level predictor but a useful batch-level screen.
9	
10	\paragraph{Task-dependent effects and format dependency.}
11	The batch-level BCS--performance relationship is RE-specific: BCS explains 22--53\% of cross-batch accuracy variance in RE but shows no correlation with NER F1 ($r \approx 0$, $n = 450$). RE's constrained decoding (enum constraint over valid type labels) channels all errors into type substitution (IntraSub scales with BCS; \S\ref{sec:multi_channel}), so batch confusability directly predicts accuracy. NER uses unconstrained generation, where errors scatter across missed entities (43--65\%), boundary misalignment, and hallucinated types, diluting the pairwise signal at batch level.
12	
13	\paragraph{Practical implications.}
14	The bounded count$\times$confusability interaction (0.47\,pp, TOST $p = 0.003$) implies no confusability amplification at scale. For RE, upper-SCS-quartile type pairs show 3--5\,pp accuracy diff
…[truncated 1309 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1396 · 2026-05-18T05:22:42.750891+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 1397 · 2026-05-18T05:22:43.265706+00:00_

1	\section*{Responsible NLP Research Checklist}
2	
3	For each question, the answer is \textbf{Yes}, \textbf{No}, or \textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.
4	
5	\subsection*{A \quad For Every Submission}
6	
7	\begin{enumerate}[label=\textbf{A\arabic*.},leftmargin=*,itemsep=4pt]
8	
9	\item \textbf{Did you describe the limitations of your work?}
10	
11	Yes. The Limitations section (after \S\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, factorial interaction tests with TOST equivalence, decomposition scope, and metric scope.
12	
13	\item \textbf{Did you discuss any potential risks of your work?}
14	
15	N/A. This is a purely analytical study of schema-associated degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
16	
17	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
18	
19	Yes. The abstract and \S\ref{sec:introduction} state the two-dimensional degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.
20	
21	\item \textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}
22	
23	Yes. We used Claude (Anthropic) for writing assistance and experimental code development. All scientific claims, experimental designs, and analyses were conducted by the authors.
24	
25	\end{enumerate}
26	
27	\subsection*{B \quad Scientific Artifacts}
28	
29	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=*,itemsep=4pt]
30	
31	\item \textbf{Did you cite the creators of artifacts you used?}
32	
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-70B-Instruct and Meta-Llama-3.1-8B-Instruct \cite{lla
…[truncated 4522 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 514
}
```

</details>

---


### Tool call

_source line 1398 · 2026-05-18T05:22:43.416884+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "decisions.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "decisions.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1399 · 2026-05-18T05:22:43.519310+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/decisions.yaml\", \"content\": \"_next_id: 61\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 16:10 UTC\\n  summary: 项目立项，MVP 验证方案：Experiment 2 (Confusability Controlled) 为核心验证实验\\n  rationale: 'IDEA_BRIEF 的核心假设是 type confusability 独立于 type count 驱动 LLM IE 质量下降。Experiment\\n    2（固定 count 变 BCS）是最直接的假设检验。Pass 标准: |r|≥0.3 且 p<0.05。ACE05 RE + Few-NERD 双数据集验证。ARR\\n    May 25 DDL（11天），MVP 需 1-2 天完成。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 16:15 UTC\\n  summary: 修正 MVP 统计设计：random samples 从 10 增至 25/档，加入 per-type solo baseline 控制变量，核心指标改为\\n    Δ(solo_F1 - batch_F1)\\n  rationale: Reviewer 指出 n=12 下 |r|=0.3 对应 p≈0.34，无法同时满足 |r|≥0.3 且 p<0.05。增至 25 random\\n    batches/档 → n≈54，|r|≥0.27 即可达 p<0.05。同时加入 solo F1 控制 type 固有难度，避免将\\\"类型本身难抽取\\\"误归因于\\\"confusability\\n    效应\\\"。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 23:11 UTC\\n  summary: MVP 分析方法从 Δ(solo-batch) 切换到 within-count Pearson r(F1, BCS)，pass 标准更新为\\n    |r|≥0.3 at fixed count\\n  rationale: Exp 1 发现 count curve 方向反转（F1 随 count 上升），根因是低 count 时模型过度 hallucinate（pred/gold=8x\\n    at count=1）。solo baseline 处于极端行为模式，Δ 被跨 count 行为差异污染。改为 within-count 对比更干净：同一\\n    count 下比较不同 BCS 的 F1，直接检验 confusability 独立效应。\\n  related_experiments:\\n  - exp_id: exp001_count_baseline\\n    role: evidence\\n    result: count curve reversed, hallucination at low count\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 23:31 UTC\\n  summary: MVP 主指标更新为 within-count r(recall, BCS)，F1 因 over-prediction confound 降为补充指标\\n  rationale: Exp 1 text-match 重评估发现：recall 单调下降（0.72→0.42，符合预期），precision 单调上升（0.11→0.52，over-prediction\\n    减少），F1 受 precision 主导而反转。within-count 分析中 precision confound 在同一 count 下近似恒定，F1\\n    仍可用；但 recall 更干净且直接反映 type confusion。WrongType 错误（text 正确但 type 错标）随 count 从 0\\n    升至 2434，直
…[truncated 3541 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1400 · 2026-05-18T05:22:48.057418+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1401 · 2026-05-18T05:22:49.012474+00:00_

File unchanged since last read. The content from the earlier Read tool_result in this conversation is still current — refer to that instead of re-reading.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 1402 · 2026-05-18T05:22:49.012990+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1403 · 2026-05-18T05:22:49.616178+00:00_

1	% DEPRECATED — this file is no longer included in main.tex.
2	% The active conclusion is in discussion.tex (\input{discussion}).
3	% Kept for reference only; safe to delete.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 1404 · 2026-05-18T05:22:49.616550+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1405 · 2026-05-18T05:22:50.019223+00:00_

1	\lstset{
2	  basicstyle=\ttfamily\small,
3	  breaklines=true,
4	  breakatwhitespace=true,
5	  columns=fullflexible
6	}
7	
8	\section{Prompt Templates}
9	\label{sec:appendix_prompts}
10	
11	This appendix reproduces the complete prompt templates used for all three extraction tasks.
12	All prompts are injected into a single \texttt{user} message (no system prompt); the model's chat template adds the system/assistant framing.
13	Both versions provide a JSON-formatted type schema to the vLLM constrained-decoding engine; the schema is \emph{not} included in the natural-language prompt itself.
14	We use greedy decoding (\texttt{temperature=0}, \texttt{seed=42}) throughout.
15	
16	\medskip\noindent
17	\textbf{Notation.}
18	Placeholders are shown in \texttt{\{braces\}}.
19	Text \textbf{added in v2} (relative to v1) is marked with $\triangleright$.
20	Text \textbf{removed in v2} is marked with \sout{strikethrough}.
21	
22	\subsection{Named Entity Recognition (Few-NERD)}
23	
24	\paragraph{v1 prompt (with character offsets).}
25	
26	\begin{small}
27	\begin{lstlisting}
28	Extract all named entities from the following text.
29	Only extract entities of the following types:
30	- {type_1}: {definition_1}
31	- {type_2}: {definition_2}
32	  ...
33	
34	Text: {input_text}
35	
36	Output as JSON: [{"text": "...", "type": "...",
37	                  "start": ..., "end": ...}]
38	\end{lstlisting}
39	\end{small}
40	
41	\noindent
42	\textbf{v1 constrained-decoding schema:}
43	\begin{small}
44	\begin{lstlisting}
45	{"type": "array",
46	 "items": {"type": "object",
47	   "properties": {
48	     "text":  {"type": "string"},
49	     "type":  {"type": "string",
50	               "enum": [&lt;sorted_types>]},
51	     "start": {"type": "integer"},
52	     "end":   {"type": "integer"}},
53	   "required": ["text","type","start","end"]}}
54	\end{lstlisting}
55	\end{small}
56	
57	\paragraph{v2 prompt (text+type only).}
58	
59	\begin{small}
60	\begin{lstlisting}
61	Extract all named entities from the foll
…[truncated 5208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1406 · 2026-05-18T05:22:50.019896+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 1407 · 2026-05-18T05:22:50.421875+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 1408 · 2026-05-18T05:22:50.674040+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 1409 · 2026-05-18T05:22:50.724811+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1410 · 2026-05-18T05:22:53.641662+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
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

_source line 1411 · 2026-05-18T05:22:53.642138+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1412 · 2026-05-18T05:22:57.716169+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1413 · 2026-05-18T05:22:58.671391+00:00_

1	# Round 14 Review Issues Tracker
2	# Updated: 2026-05-18 (Round 14 Action Matrix dispatched, issues marked in_progress)
3	
4	# ============================================================
5	# CRITICAL — Must-Fix
6	# ============================================================
7	
8	- id: R3-C2
9	  summary: "'Empirically separable channels' 缺乏 formal 统计支撑 — TOST margin ±3pp > typical effect 2.2pp"
10	  category: framing
11	  severity: critical
12	  status: resolved
13	  first_raised_round: 3
14	  last_seen_round: 9
15	  mentions:
16	    - {round: 3, reviewers: [R1, R2], note: "因果语言过强"}
17	    - {round: 4, reviewers: [R1, R2], note: "Title 'Drive' + §4.3 暗示因果"}
18	    - {round: 5, reviewers: [R1, R2, R3], note: "三人共识改措辞"}
19	    - {round: 6, reviewers: [R1, R2, R3], note: "factorial p=0.50; 建议 'mechanistically distinguishable'"}
20	    - {round: 7, reviewers: [R1, R2], note: "三项 factorial 检验中两项失败"}
21	    - {round: 8, reviewers: [R1, R2], note: "R1-N1 critical: 3/4 tests 失败; 共识: 需限定"}
22	    - {round: 9, reviewers: [R1, R2, R3], note: "三人共识: TOST ±3pp margin 用 prompt variation 锚定不合逻辑; margin > typical main effect; ±1pp inconclusive"}
23	  action_items:
24	    - {round: 9, action: "D051: 'additive separability' → 'bounded interaction' 全文统一; SESOI effect-size anchored", assigned_to: agent, status: done}
25	  resolution: "D051 W1: 全文 'bounded interaction' 统一; SESOI effect-size anchored; sensitivity table in Appendix"
26	  resolution_round: 9
27	
28	- id: R10-N1
29	  summary: "因果语言 ('driven', 'channels', 'shape') 超出 observational/quasi-experimental 证据边界"
30	  category: framing
31	  severity: critical
32	  status: resolved
33	  first_raised_round: 10
34	  last_seen_round: 12
35	  mentions:
36	    - {round: 10, reviewers: [R1, R2], note: "R1 critical N3 + R2 AGREE with qualification; 共识: Title 'shape' 暗示因果"}
37	    - {round: 11, reviewers: [R1, R2], note: "R1 W4 + R2 AGREE: Title 'Shape' + Limitations 承认 no interventional causality = 不匹配"}
38	    - {round: 12, reviewers: [
…[truncated 27172 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 1414 · 2026-05-18T05:22:58.822390+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit long paper short paper format requirements",
  "allowed_domains": "['aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit long paper short paper format requirements",
    "allowed_domains": "['aclrollingreview.org']"
  }
}
```

</details>

---


### Tool result

_source line 1415 · 2026-05-18T05:23:06.912123+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit long paper short paper format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"}]

I found information about ACL Rolling Review submission guidelines, but the search results don't explicitly state the spec
…[truncated 3256 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 8089
}
```

</details>

---


### Tool call

_source line 1416 · 2026-05-18T05:23:15.560025+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Find project config file",
  "subagent_type": "Explore",
  "prompt": "Find the project configuration file for schema-dag-extraction project. Look in /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ for files like config.yaml, project.yaml, settings.yaml or similar configuration files. Also check /home/ubuntu/.agent-ml-research-idea_gen_0509_18/ root for a projects config. I need to find the external_review.paperreview_ai.enabled setting. Report the file path and contents (especially the external_review section)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Agent",
  "tool_args": {
    "description": "Find project config file",
    "subagent_type": "Explore",
    "prompt": "Find the project configuration file for schema-dag-extraction project. Look in /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ for files like config.yaml, project.yaml, settings.yaml or similar configuration files. Also check /home/ubuntu/.agent-ml-research-idea_gen_0509_18/ root for a projects config. I need to find the external_review.paperreview_ai.enabled setting. Report the file path and contents (especially the external_review section)."
  }
}
```

</details>

---


### Tool call

_source line 1417 · 2026-05-18T05:23:18.375074+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "pattern": "**/*.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
    "pattern": "**/*.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1418 · 2026-05-18T05:23:18.576425+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T113743/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/project
…[truncated 3357 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1419 · 2026-05-18T05:23:18.576936+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "pattern": "**/*.yml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
    "pattern": "**/*.yml"
  }
}
```

</details>

---


### Tool result

_source line 1420 · 2026-05-18T05:23:18.778743+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1421 · 2026-05-18T05:23:18.830074+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "pattern": "*.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
    "pattern": "*.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1422 · 2026-05-18T05:23:18.981204+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/workspace.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/manifest.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/collapse-aware-mixing.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/s
…[truncated 5014 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1423 · 2026-05-18T05:23:18.981723+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "pattern": "*.yml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
    "pattern": "*.yml"
  }
}
```

</details>

---


### Tool result

_source line 1424 · 2026-05-18T05:23:19.032967+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1425 · 2026-05-18T05:23:20.541893+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/schema-dag-extraction.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/schema-dag-extraction.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1426 · 2026-05-18T05:23:20.542359+00:00_

1	execution:
2	  project_path: /root/schema-dag-extraction
3	  servers:
4	  - account: root
5	    server: cqa1-38874
6	  - account: root
7	    server: westd-24295
8	feishu:
9	  chat_id: oc_51326259fe46fbae9da26b81cf03f1f8
10	  operational_chat_id: oc_04544c3b7bc497e1d098ba47fb56a6c2
11	  review_paper_path: projects/schema-dag-extraction/docs/paper/main.tex
12	  review_round: 15
13	  review_supplementary_paths: ''
14	  submission_chat_id: oc_ac7ab7270b6b5caecee04f89b11aab3e
15	project:
16	  created_at: '2026-05-14T16:07:46.825Z'
17	  description: Does Type Confusability Drive Schema-Induced Degradation in LLM Information
18	    Extraction? An Empirical Study and Principled Decomposition Framework
19	  name: schema-dag-extraction
20	  phase: research
21	  source_idea_id: idea_007
22	venue: emnlp-2026
23	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1427 · 2026-05-18T05:23:22.151507+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/workspace.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/workspace.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1428 · 2026-05-18T05:23:22.355046+00:00_

1	projects: {}
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 203
}
```

</details>

---


### Tool call

_source line 1429 · 2026-05-18T05:23:22.405947+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/backend.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/backend.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1430 · 2026-05-18T05:23:22.758727+00:00_

1	manager:
2	  enabled: true
3	  url: http://172.31.31.59:8700
4	  my_id: be-prod9-0512
5	  my_token: 48d731d4ffca61bec8a11c3919f9bf537a2999bc36e98c14fb7d1577b327534e
6	  ingest_token: e1dc1e287cb57d2e8411481f152c3cfb22d694b1bc8043b04a543cc7f0e08b82
7	  api:
8	    listen_host: 0.0.0.0
9	    listen_port: 8420
10	    allowed_source_cidrs:
11	    - 10.0.0.0/8
12	    - 192.168.0.0/16
13	    - 172.16.0.0/12
14	    - 127.0.0.0/8
15	  capabilities:
16	    read: true
17	    bootstrap_project: true
18	    archive_project: true
19	    allocate_gpus: true
20	    release_gpus: true
21	    read_chat_history: true
22	    claude_account_login: true
23	    read_claude_pool: true
24	  local_approvals:
25	    bootstrap_project: false
26	    archive_project: false
27	    allocate_gpus: false
28	  heartbeat:
29	    enabled: true
30	    interval_sec: 60
31	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1431 · 2026-05-18T05:23:22.810063+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -maxdepth 3 -type f \\( -name \"*config*\" -o -name \"*settings*\" \\) ! -path \"*/artifacts/*\" ! -path \"*/.git/*\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -maxdepth 3 -type f \\( -name \"*config*\" -o -name \"*settings*\" \\) ! -path \"*/artifacts/*\" ! -path \"*/.git/*\" 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 1432 · 2026-05-18T05:23:23.018307+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_review_director.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_review_reviewer_1.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_no_project.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_worker_116db043ffcfd41b2805e6feba9eb07d.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_worker_f265de7a9796688b878083fef59f9d4c.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_worker_f5d680d1394a02be4b502c5606a34a84.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_worker_943f40256720b8f6634ec1980a24acc1.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_worker_c30177f46da5cf01b357f2bf0953c325.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_worker_b5b42865db9e25c090239f4ff8686b1b.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_worker_df2e41002dd8105738105d86d87fc2f8.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_paper_agent.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_dream_review_director.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_review_reviewer_3.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_director.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_review_reviewer_2.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_worker_ba2a0cf1144287de9c1c6e3ac925733d.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_worker_0aa51d591547913249ab7a68dc681be8.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_worker_0df49881059e9f493ee8cd1e899565bb.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_worker_6f0b694c30c8a0575c498898ae58e765.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_w
…[truncated 2852 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 208
}
```

</details>

---


### Tool call

_source line 1433 · 2026-05-18T05:23:24.675352+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/resources.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/resources.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1434 · 2026-05-18T05:23:24.776154+00:00_

1	default_model: claude-opus-4-6
2	default_model_claude_code: claude-opus-4-6
3	idea_model: claude-opus-4-6
4	servers:
5	  cqa1-38874:
6	    accounts:
7	    - gpus:
8	      - cuda:0
9	      name: root
10	      password_encrypted: gAAAAABqAuvPRnsR1TtY3nMeh4mVCYkvCSF7_wdLf-0R0bfkxwoGlInSGv3dLgBMCNw2jcYb4Wdztu3hlMLhkpq9hKnRirdTGw==
11	      user: root
12	      work_dir: /root
13	    - gpus: []
14	      name: ''
15	      user: ''
16	    detected_image:
17	      detected: false
18	      image: ''
19	      status: unknown
20	      version: ''
21	    env_activate: ''
22	    host: connect.cqa1.seetacloud.com
23	    port: 38874
24	    total_gpus:
25	    - cuda:0
26	    user_rules_excluded: []
27	    work_dir: /root
28	  home-1x5090:
29	    accounts:
30	    - gpus: []
31	      name: sonny
32	      password_encrypted: gAAAAABqAs98OWvzWtk-wjILplCl-xG8f6sbL0GMIHCqjHs4LD83BaT56W8D4iW7g3UJTcyFGxiYqIy44LDYO4oxAE_ptGirBg==
33	      user: sonny
34	      work_dir: /root
35	    env_activate: ''
36	    host: implicit5638.xyfu.me
37	    port: 22
38	    total_gpus:
39	    - cuda:0
40	    user_rules_excluded: []
41	    work_dir: /root
42	  westd-24295:
43	    accounts:
44	    - gpus: []
45	      name: root
46	      password_encrypted: gAAAAABqCUPK4KEQWs-G2-zP9PqmQZsghbyISHKoqXnPCXwftsxti4lidbskdEyh3NfHQ1tTJCYAKHTZNc2CHKBJ8L4Cirn3YA==
47	      user: root
48	      work_dir: /root
49	    detected_image:
50	      detected: false
51	      image: ''
52	      status: unknown
53	      version: ''
54	    env_activate: ''
55	    host: connect.westd.seetacloud.com
56	    port: 24295
57	    total_gpus:
58	    - cuda:0
59	    - cuda:1
60	    user_rules_excluded: []
61	    work_dir: /root
62	user_rules: []
63	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1435 · 2026-05-18T05:23:24.827057+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
  }
}
```

</details>

---


### Tool result

_source line 1436 · 2026-05-18T05:23:25.181354+00:00_

Found 20 files
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/chats/feishu_group_oc_ac7ab7270b6b5caecee04f89b11aab3e_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/global/logs/system.log
AGENTS.md
CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/chats/feishu_group_oc_51326259fe46fbae9da26b81cf03f1f8_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_14.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_13.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_research_missing_references_mr1_4_20260517T145447.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_12.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_11.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/chats/archive/feishu_group_oc_51326259fe46fbae9da26b81cf03f1f8_director_20260517T074950_564926.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_10.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/chats/archive/feishu_group_oc_51326259fe46fbae9da26b81cf03f1f8_director_20260516T190837_502176.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_8.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/chats/archive/feishu_group_oc_51326259fe46fbae9da26b81cf03f1f8_director_20260516T144003_568314.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/proje
…[truncated 479 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "elapsed_ms": 354
}
```

</details>

---


### Tool call

_source line 1437 · 2026-05-18T05:23:27.240190+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/*.yaml 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/*.yaml 2>/dev/null"
  }
}
```

</details>

---


### Tool call

_source line 1438 · 2026-05-18T05:23:27.290870+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/ 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/ 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 1439 · 2026-05-18T05:23:27.291301+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 1440 · 2026-05-18T05:23:27.341784+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1441 · 2026-05-18T05:23:28.998761+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -maxdepth 2 -type f -name \"*.yaml\" | grep -v artifacts | grep -v logs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -maxdepth 2 -type f -name \"*.yaml\" | grep -v artifacts | grep -v logs"
  }
}
```

</details>

---


### Tool result

_source line 1442 · 2026-05-18T05:23:29.149783+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/experiment_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1443 · 2026-05-18T05:23:29.250589+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -l \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/*.yaml 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -l \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/*.yaml 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 1444 · 2026-05-18T05:23:29.301317+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1445 · 2026-05-18T05:23:30.759698+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/venue_registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/venue_registry.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1446 · 2026-05-18T05:23:30.810812+00:00_

1	venues:
2	  corl-2026:
3	    display_name: CoRL 2026
4	  emnlp-2026:
5	    display_name: EMNLP 2026
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1447 · 2026-05-18T05:23:30.863081+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/ | grep -E \"\\.yaml|\\.yml\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/ | grep -E \"\\.yaml|\\.yml\""
  }
}
```

</details>

---


### Tool result

_source line 1448 · 2026-05-18T05:23:30.913776+00:00_

-rw-rw-r-- 1 ubuntu ubuntu 2901 May  9 09:00 approvals.yaml
-rw------- 1 ubuntu ubuntu  764 May 11 17:59 backend.yaml
-rw------- 1 ubuntu ubuntu 9357 May 17 14:03 crons.yaml
-rw------- 1 ubuntu ubuntu  104 May 15 09:17 feishu.yaml
-rw-r--r-- 1 ubuntu ubuntu 1521 May 17 15:11 resources.yaml
-rw-r--r-- 1 ubuntu ubuntu   92 May 17 12:02 venue_registry.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1449 · 2026-05-18T05:23:32.071329+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/approvals.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/approvals.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1450 · 2026-05-18T05:23:32.222517+00:00_

1	# 审批类型注册表
2	# 此文件位于 WORKSPACE_ROOT/config/approvals.yaml
3	# hook 名由 Python (core/approvals/hooks.py) 绑定，不在此文件里定义
4	
5	approval_types:
6	
7	  experiment:
8	    display_name: "实验审批"
9	    description: "高风险实验变更，需要人工审批后才能提交训练"
10	    always_require: false
11	    auto_approve_rule: "all_not_high"   # 枚举：all_low | all_not_high | always | never
12	    risk_dimensions:
13	      - name: gpu_hours
14	        label: "GPU 时长（小时）"
15	        type: numeric
16	        thresholds: { low: 2.0, medium: 8.0 }
17	        hard_limit: 4.0            # 超过直接触发审批，无视其他维度
18	      - name: change_scope
19	        label: "代码变更文件数"
20	        type: numeric
21	        thresholds: { low: 1, medium: 3 }
22	      - name: history_success
23	        label: "历史成功次数"
24	        type: numeric
25	        thresholds: { low: 2, medium: 1 }   # 0 次 → medium（不再是 high）
26	        invert: true                         # 数值越大风险越低
27	    pending_timeout_hours: 48
28	
29	  worker:
30	    display_name: "Worker 任务审批"
31	    description: "高风险后台任务需要确认后才启动"
32	    always_require: false
33	    auto_approve_rule: "all_low"
34	    risk_dimensions:
35	      - name: task_type
36	        label: "任务类型"
37	        type: enum
38	        high_values: ["code_rewrite", "bulk_delete"]
39	        medium_values: ["code_modify"]
40	        low_values: ["doc_gen", "analysis", "exploration"]
41	      - name: file_scope
42	        label: "涉及文件数"
43	        type: numeric
44	        thresholds: { low: 3, medium: 10 }
45	    pending_timeout_hours: 24
46	
47	  deployment:
48	    display_name: "部署审批"
49	    description: "生产部署不可逆，必须人工确认"
50	    always_require: true
51	    auto_approve_rule: "never"
52	    risk_dimensions:
53	      - name: service_tier
54	        label: "服务等级"
55	        type: enum
56	        high_values: ["production"]
57	        medium_values: ["staging"]
58	        low_values: ["dev"]
59	    pending_timeout_hours: 24
60	
61	  submission:
62	    display_name: "投稿审批"
63	    description: "Director 提交审稿请求后，发卡片到 A 群让用户选择审稿模式（co
…[truncated 626 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1451 · 2026-05-18T05:23:32.223105+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/crons.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/crons.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1452 · 2026-05-18T05:23:32.273688+00:00_

1	active_crons: []
2	completed_crons:
3	- chat_id: null
4	  completed_at: '2026-05-12T14:53:02Z'
5	  created_at: '2026-05-12T14:47:01.196Z'
6	  exp_id: mvp_pilot_v4
7	  hooks: null
8	  interval_seconds: 120
9	  last_checked: '2026-05-12T14:51:01.197Z'
10	  log_path: ~/runs/collapse-aware-mixing/mvp_pilot_v4.log
11	  pid: mvp_pilot_v4
12	  project: collapse-aware-mixing
13	  server: cqa1-38874
14	  status: completed
15	  tracked_metrics: null
16	  wandb_run_id: null
17	- chat_id: null
18	  completed_at: '2026-05-12T15:23:20Z'
19	  created_at: '2026-05-12T14:54:35.794Z'
20	  exp_id: mvp_pilot_v4
21	  hooks: null
22	  interval_seconds: 120
23	  last_checked: '2026-05-12T15:21:18.314Z'
24	  log_path: /tmp/pilot_v4.log
25	  pid: '28147'
26	  project: collapse-aware-mixing
27	  server: cqa1-38874
28	  status: completed
29	  tracked_metrics: null
30	  wandb_run_id: null
31	- chat_id: null
32	  completed_at: '2026-05-13T02:22:16Z'
33	  created_at: '2026-05-12T16:05:26.014Z'
34	  exp_id: mvp_pilot_v5
35	  hooks: null
36	  interval_seconds: 120
37	  last_checked: '2026-05-13T02:19:59.330Z'
38	  log_path: ~/runs/collapse-aware-mixing/mvp_pilot_v5.log
39	  pid: '32154'
40	  project: collapse-aware-mixing
41	  server: cqa1-38874
42	  status: completed
43	  tracked_metrics: null
44	  wandb_run_id: null
45	- chat_id: null
46	  completed_at: '2026-05-13T17:42:39Z'
47	  created_at: '2026-05-13T03:50:14.008Z'
48	  exp_id: mvp_pilot_v7
49	  hooks: null
50	  interval_seconds: 1800
51	  last_checked: '2026-05-13T17:12:18.208Z'
52	  log_path: /root/autodl-tmp/pilot_v7.log
53	  pid: '60104'
54	  project: collapse-aware-mixing
55	  server: cqa1-38874
56	  status: completed
57	  tracked_metrics: null
58	  wandb_run_id: null
59	- chat_id: null
60	  completed_at: '2026-05-14T15:55:18Z'
61	  created_at: '2026-05-14T05:46:42.474Z'
62	  exp_id: mvp_seed0_replication_r2
63	  hooks: null
64	  interval_seconds: 300
65	  last_checked: '2026-05-14T15:50:57.499Z'
66	  log_path: null
67	  pid: '122208'
…[truncated 8605 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1453 · 2026-05-18T05:23:34.736872+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -name \"settings.yaml\" -o -name \"settings.yml\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -name \"settings.yaml\" -o -name \"settings.yml\" 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 1454 · 2026-05-18T05:23:35.089260+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1455 · 2026-05-18T05:23:35.240407+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"paperreview_ai\\|external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction --include=\"*.yaml\" --include=\"*.yml\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"paperreview_ai\\|external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction --include=\"*.yaml\" --include=\"*.yml\" 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 1456 · 2026-05-18T05:23:35.341269+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1457 · 2026-05-18T05:23:39.170117+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/chats --include=\"*.jsonl\" 2>/dev/null | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/chats --include=\"*.jsonl\" 2>/dev/null | head -5"
  }
}
```

</details>

---


### Tool call

_source line 1458 · 2026-05-18T05:23:39.170594+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -type f -name \"*.json\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -type f -name \"*.json\" | head -20"
  }
}
```

</details>

---


### Tool result

_source line 1459 · 2026-05-18T05:23:39.272298+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/scripts/test_types.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_cleanup_awq_scripts_delete_20260515T231834_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_paper_d047_round2_discussion_20260516T124707_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_ssh_exp008-analysis-prep_20260515T111102_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_check_d051_experiment_progress_20260516T205108_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_paper_r11-d054-phase1-3_20260517T100308_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_ssh_env-setup-and-data_20260514T163452_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_diagnose_exp012_vllm_blackwell_20260515T171340_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_ssh_exp008-diagnosis_20260515T114006_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_compute_r5w1_split_origin_covariate_20260516T175323_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_ssh_sdgd-v2-integration_20260515T120937_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_monitor_exp012_progress_20260515T191405_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_research_literature_survey_v2_20260515T161104_result.json
/home/ubuntu/.agent-ml-research-ide
…[truncated 1077 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 1460 · 2026-05-18T05:23:39.272689+00:00_

&lt;persisted-output>
Output too large (62KB). Full output saved to: /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-director-338aa0a5/e34ba28f-af7f-44e0-8b15-e13d198dd227/tool-results/bth1m0p22.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/chats/feishu_group_oc_51326259fe46fbae9da26b81cf03f1f8_director.jsonl:{"ts": "2026-05-17T09:13:45.811573+00:00", "role": "user", "session": "feishu:group:oc_51326259fe46fbae9da26b81cf03f1f8:director", "text": "[审稿报告]\nOverall: borderline\n\n# Round 11 审稿报告 — schema-dag-extraction\n\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n**审稿人**: Reviewer 1（方法严谨性）+ Reviewer 2（新颖性/写作/格式）\n**日期**: 2026-05-17\n\n---\n\n## Summary\n\n本文通过 Schema Confusability Score (SCS) 及其 batch 聚合 BCS，在 NER/RE/ED 四个数据集上将 zero-shot LLM IE 的 schema-induced degradation 分解为两个维度：count-related recall decline（主导）和 confusability-related type substitution（次要）。实验设计系统且 sensitivity analyses 充分，negative results（SDGD 失败）诚实报告并提供了 merge amplification 的机制性解释。但核心 confusability effect 极小（typical gap 仅 2.2pp），且仅在 RE 任务的 batch-level 上可靠——NER batch-level 方向相反，MAVEN 被 centrality confound 完全解释。\n\n---\n\n## Strengths\n\n1. **实验设计系统且互补**：Count curves + BCS-controlled 两种范式构成合理的准实验策略；within-pool 控制有效隔离 pool composition confound。\n2. **统计工具箱完整**：Bootstrap CI、permutation tests、TOST equivalence、cluster bootstrap、variance decomposition、partial correlation——选择得当且报告透明。\n3. **负结果诚实且有诊断价值**：SDGD 失败的根因分析（merge amplification 导致 precision 崩塌；constrained decoding 消除 confidence signal）是对社区有直接价值的发现。\n4. **Centrality confound 发现**：MAVEN per-type BCS 正相关是 centrality artifact 的分析是方法论贡献，对后续使用 embedding similarity 做 label analysis 的工作有直接 warning。\n5. **多层次 sensitivity analyses**：四种 prompt variant、两种 embedding、SCS ablation、split-origin covariate、cross-seed variance decomposition——覆盖主要潜在 confound。\n6. **Limitations 极其透明**：8 条
…[truncated 346 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1461 · 2026-05-18T05:23:41.030916+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/ | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/ | head -30"
  }
}
```

</details>

---


### Tool result

_source line 1462 · 2026-05-18T05:23:41.232464+00:00_

total 268
drwxrwxr-x 5 ubuntu ubuntu 4096 May 17 15:06 .
drwxrwxr-x 9 ubuntu ubuntu 4096 May 12 08:37 ..
-rw-rw-r-- 1 ubuntu ubuntu 2901 May  9 09:00 approvals.yaml
-rw------- 1 ubuntu ubuntu  764 May 11 17:59 backend.yaml
-rw-r--r-- 1 ubuntu ubuntu 1855 May 18 05:22 claude_sessions.json
-rw------- 1 ubuntu ubuntu 9357 May 17 14:03 crons.yaml
-rw------- 1 ubuntu ubuntu  364 May 15 04:13 email_tokens.json
-rw------- 1 ubuntu ubuntu  104 May 15 09:17 feishu.yaml
-rw-r--r-- 1 ubuntu ubuntu 4769 May 18 05:21 keepalive.json
-rw-r--r-- 1 ubuntu ubuntu  342 May 11 05:47 mcp_config.json
-rw-r--r-- 1 ubuntu ubuntu  392 May 17 10:56 mcp_config_briefer.json
-rw-r--r-- 1 ubuntu ubuntu  394 May 12 08:44 mcp_config_director.json
-rw-r--r-- 1 ubuntu ubuntu  420 May 15 06:10 mcp_config_dream_review_director.json
-rw-r--r-- 1 ubuntu ubuntu  398 May 12 08:37 mcp_config_no_project.json
-rw-r--r-- 1 ubuntu ubuntu  400 May 15 16:03 mcp_config_paper_agent.json
-rw-r--r-- 1 ubuntu ubuntu  408 May 16 00:50 mcp_config_review_director.json
-rw-r--r-- 1 ubuntu ubuntu  436 May 16 00:53 mcp_config_review_reviewer_1.json
-rw-r--r-- 1 ubuntu ubuntu  436 May 16 00:53 mcp_config_review_reviewer_2.json
-rw-r--r-- 1 ubuntu ubuntu  436 May 16 11:17 mcp_config_review_reviewer_3.json
-rw-r--r-- 1 ubuntu ubuntu  394 May 12 08:46 mcp_config_reviewer.json
-rw-r--r-- 1 ubuntu ubuntu  417 May 12 10:55 mcp_config_worker_0aa51d591547913249ab7a68dc681be8.json
-rw-r--r-- 1 ubuntu ubuntu  471 May 16 01:50 mcp_config_worker_0df49881059e9f493ee8cd1e899565bb.json
-rw-r--r-- 1 ubuntu ubuntu  465 May 15 05:06 mcp_config_worker_116db043ffcfd41b2805e6feba9eb07d.json
-rw-r--r-- 1 ubuntu ubuntu  477 May 15 15:54 mcp_config_worker_12093ef55c63229acbf88fd2b9106dce.json
-rw-r--r-- 1 ubuntu ubuntu  383 May 15 16:10 mcp_config_worker_14d296b01755362efedfab08bc7a4e38.json
-rw-r--r-- 1 ubuntu ubuntu  465 May 12 15:24 mcp_config_worker_33c066fe8f41bfaa9b9c844bb47eca4f.json
-rw-r--r-- 1 ubuntu ubuntu  433 May 16 01:56 mcp_config_w
…[truncated 245 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1463 · 2026-05-18T05:23:41.284011+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -l \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/*.json 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -l \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/*.json 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 1464 · 2026-05-18T05:23:41.334548+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1465 · 2026-05-18T05:23:44.374588+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_review_director.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_review_director.json"
  }
}
```

</details>

---


### Tool result

_source line 1466 · 2026-05-18T05:23:44.575890+00:00_

1	{
2	  "mcpServers": {
3	    "agent-ml-research": {
4	      "command": "/home/ubuntu/agent-ml-research/.venv/bin/python",
5	      "args": [
6	        "-m",
7	        "core.mcp_server",
8	        "--review-director"
9	      ],
10	      "cwd": "/home/ubuntu/agent-ml-research",
11	      "env": {
12	        "AGENT_ML_WORKSPACE": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
13	        "REVIEW_DIRECTOR_MODE": "1"
14	      }
15	    }
16	  }
17	}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1467 · 2026-05-18T05:23:44.576280+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -type d -name \"config\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -type d -name \"config\" 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 1468 · 2026-05-18T05:23:44.626804+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/fontTools/config
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1469 · 2026-05-18T05:23:46.835889+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/venue_rules/emnlp-2026.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/venue_rules/emnlp-2026.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1470 · 2026-05-18T05:23:46.836387+00:00_

1	rules:
2	  research: []
3	  review:
4	  - created_at: '2026-05-17T12:02:15Z'
5	    id: c9bba9
6	    text: “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall
7	      Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 =
8	      Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5
9	      = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit
10	      after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”
11	  writing: []
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1471 · 2026-05-18T05:23:46.886928+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/venue_rules/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/venue_rules/"
  }
}
```

</details>

---


### Tool result

_source line 1472 · 2026-05-18T05:23:46.937745+00:00_

total 16
drwxr-xr-x 2 ubuntu ubuntu 4096 May 17 12:02 .
drwxrwxr-x 5 ubuntu ubuntu 4096 May 17 15:06 ..
-rw-r--r-- 1 ubuntu ubuntu   49 May 17 12:02 corl-2026.yaml
-rw-r--r-- 1 ubuntu ubuntu  737 May 17 12:02 emnlp-2026.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1473 · 2026-05-18T05:23:48.547636+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/global/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/global/"
  }
}
```

</details>

---


### Tool result

_source line 1474 · 2026-05-18T05:23:48.749334+00:00_

total 52
drwxr-xr-x 4 ubuntu ubuntu  4096 May 18 05:22 .
drwxrwxr-x 9 ubuntu ubuntu  4096 May 12 08:37 ..
-rw------- 1 ubuntu ubuntu 27524 May 18 05:22 approvals.yaml
drwxr-xr-x 2 ubuntu ubuntu  4096 May 15 15:55 checkpoints
drwxr-xr-x 6 ubuntu ubuntu  4096 May 13 07:09 logs
-rw-r--r-- 1 ubuntu ubuntu     0 May 15 15:55 registry.lock
-rw------- 1 ubuntu ubuntu   771 May 15 15:55 registry.yaml
-rw-r--r-- 1 ubuntu ubuntu   459 May 15 15:55 report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1475 · 2026-05-18T05:23:48.801087+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -maxdepth 2 -type f -name \"*.yaml\" | grep -v config | grep -v projects | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -maxdepth 2 -type f -name \"*.yaml\" | grep -v config | grep -v projects | head -20"
  }
}
```

</details>

---


### Tool result

_source line 1476 · 2026-05-18T05:23:48.851749+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/global/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/global/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1477 · 2026-05-18T05:23:50.258028+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/global/approvals.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/global/approvals.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1478 · 2026-05-18T05:23:50.258530+00:00_

1	approvals:
2	  apr_20260516T002122_tjdw:
3	    approval_id: apr_20260516T002122_tjdw
4	    context:
5	      chat_id: oc_51326259fe46fbae9da26b81cf03f1f8
6	      deadline: '2026-05-25'
7	      has_prior_review: true
8	      mode_reason: 论文处于连续迭代中（3 轮写作对抗循环刚收敛），Reviewer 需要验证此前多轮修复是否全部到位，continue 模式可对照历史问题。
9	      paper_path: projects/schema-dag-extraction/paper/main.tex
10	      paper_title: EMNLP 2026
11	      reason: 写作对抗循环 3 轮收敛至 8/10，全部 critical/warning 已清除。全部 P0 实验完成，exp012 跨模型验证强复现，图文一致性验证通过。距
12	        DDL 10 天，需正式预审发现剩余问题。
13	      recommended_review_mode: continue
14	      review_chat_id: oc_ac7ab7270b6b5caecee04f89b11aab3e
15	      review_mode: fresh
16	      review_round: 0
17	      supplementary_paths: ''
18	      track: main conference
19	      venue: EMNLP 2026
20	    created_at: '2026-05-16T00:21:22.410Z'
21	    feishu_card_message_id: om_x100b6f4fc6e678a4b167b78615a91cd
22	    project: schema-dag-extraction
23	    reject_reason: null
24	    resolved_at: '2026-05-16T00:50:27.601516+00:00'
25	    resolved_by: feishu:ou_0692132359d3a1f74288c489861e30b6
26	    risk_score:
27	      auto_approve: false
28	      dimensions: []
29	      overall: low
30	      reason: 需要人工审批。（无维度数据）
31	    status: approved
32	    subject_id: schema-dag-extraction-emnlp-2026
33	    type: submission
34	  apr_20260516T024519_ukr1:
35	    approval_id: apr_20260516T024519_ukr1
36	    context:
37	      chat_id: oc_51326259fe46fbae9da26b81cf03f1f8
38	      deadline: '2026-05-25'
39	      has_prior_review: true
40	      mode_reason: Table 3→4 重构 + 核心叙事从 amplification 转为 slope consistency，变动幅度大，需要无偏重新审阅。
41	      paper_path: projects/schema-dag-extraction/docs/paper/main.tex
42	      paper_title: EMNLP 2026
43	      reason: D036 叙事重构完成：Table 4 从 quartile Δ 转为 regression slope 为主指标，3.4× amplification
44	        全文清除，替换为 slope consistency (permutation p=0.436)。5 个文件修改，Reviewer 数据一致性审查
45	        PASS (22/22)。需要 fresh review 评估新叙事的说服力和 soundness。
46	      recommended_review_mode: fresh

…[truncated 2104 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1479 · 2026-05-18T05:23:52.219070+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research -type f -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | grep -i \"config\\|settings\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/agent-ml-research -type f -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null | grep -i \"config\\|settings\" | head -20"
  }
}
```

</details>

---


### Tool call

_source line 1480 · 2026-05-18T05:23:52.320371+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/agent-ml-research --include=\"*.py\" 2>/dev/null | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\" /home/ubuntu/agent-ml-research --include=\"*.py\" 2>/dev/null | head -10"
  }
}
```

</details>

---


### Tool result

_source line 1481 · 2026-05-18T05:23:52.521925+00:00_

/home/ubuntu/agent-ml-research/workspace/config/approvals.yaml
/home/ubuntu/agent-ml-research/workspace/config/projects/LLM-Calibration.yaml
/home/ubuntu/agent-ml-research/workspace/config/resources.yaml
/home/ubuntu/agent-ml-research/config/ralph_loop.yaml
/home/ubuntu/agent-ml-research/config/images.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 302
}
```

</details>

---


### Tool result

_source line 1482 · 2026-05-18T05:23:52.673266+00:00_

/home/ubuntu/agent-ml-research/tests/test_review_phase_isolation.py:  2. fresh mode wipes `external_review_state.json` so prior-round pending /
/home/ubuntu/agent-ml-research/tests/test_review_phase_isolation.py:# Fix 2: external_review.reset_state
/home/ubuntu/agent-ml-research/tests/test_review_phase_isolation.py:        from core.tools.external_review import _save_state, reset_state, _load_state
/home/ubuntu/agent-ml-research/tests/test_review_phase_isolation.py:        state_file = _paths.project_dir(project) / "external_review_state.json"
/home/ubuntu/agent-ml-research/tests/test_review_phase_isolation.py:        from core.tools.external_review import reset_state
/home/ubuntu/agent-ml-research/tests/test_paper_review_handoff.py:            "core.tools.external_review.reset_state",
/home/ubuntu/agent-ml-research/tests/test_dream_review_session_isolation.py:        assert "request_external_review" not in tools
/home/ubuntu/agent-ml-research/tests/test_dream_review_session_isolation.py:        assert "get_external_review_status" not in tools
/home/ubuntu/agent-ml-research/tests/test_dream_review_simple.py:        assert "request_external_review" in prompt
/home/ubuntu/agent-ml-research/tests/test_dream_review_no_continue.py:        assert "request_external_review" not in tools

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1483 · 2026-05-18T05:23:54.129092+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research -type f -name \"*external*review*\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/agent-ml-research -type f -name \"*external*review*\" 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 1484 · 2026-05-18T05:23:54.433022+00:00_

/home/ubuntu/agent-ml-research/core/tools/__pycache__/external_review.cpython-314.pyc
/home/ubuntu/agent-ml-research/core/tools/external_review.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 1485 · 2026-05-18T05:23:54.433504+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research -path \"*/core/tools*\" -type f -name \"*.py\" 2>/dev/null | grep -i review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/agent-ml-research -path \"*/core/tools*\" -type f -name \"*.py\" 2>/dev/null | grep -i review"
  }
}
```

</details>

---


### Tool result

_source line 1486 · 2026-05-18T05:23:54.634573+00:00_

/home/ubuntu/agent-ml-research/core/tools/external_review.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1487 · 2026-05-18T05:23:55.940186+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/core/tools/external_review.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/core/tools/external_review.py"
  }
}
```

</details>

---


### Tool result

_source line 1488 · 2026-05-18T05:23:55.940970+00:00_

1	"""External review tools — request human-assisted submission to external review services.
2	
3	Currently supports: Stanford Agentic Reviewer (paperreview.ai).
4	The user handles the actual submission manually; this module sends Feishu cards
5	to request the submission and Cron reminders to follow up.
6	"""
7	
8	from __future__ import annotations
9	
10	import json
11	import logging
12	from datetime import datetime, timezone
13	
14	from core.tools.result import ToolResult
15	
16	logger = logging.getLogger(__name__)
17	
18	# ---------------------------------------------------------------------------
19	# State persistence — lightweight YAML file per project
20	# ---------------------------------------------------------------------------
21	
22	_PENDING = "pending"       # Card sent, waiting for user action
23	_SUBMITTED = "submitted"   # User clicked [已提交]
24	_RECEIVED = "received"     # Review text pasted back
25	_SKIPPED = "skipped"       # User clicked [跳过]
26	
27	
28	def _state_path(project: str) -> "Path":
29	    from core import paths as _paths
30	    return _paths.project_dir(project) / "external_review_state.json"
31	
32	
33	def _load_state(project: str) -> dict:
34	    p = _state_path(project)
35	    if not p.exists():
36	        return {}
37	    try:
38	        return json.loads(p.read_text(encoding="utf-8"))
39	    except Exception:
40	        return {}
41	
42	
43	def _save_state(project: str, state: dict) -> None:
44	    p = _state_path(project)
45	    p.parent.mkdir(parents=True, exist_ok=True)
46	    p.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
47	
48	
49	def reset_state(project: str) -> None:
50	    """Drop the external review state file. Called on fresh review round start
51	    so Round N-1's pending/received/skipped state does not leak forward."""
52	    p = _state_path(project)
53	    if p.exists():
54	        try:
55	            p.unlink()
56	            logger.info("[external_review] reset state for project=%s",
…[truncated 14491 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1489 · 2026-05-18T05:23:58.803040+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"paperreview_ai\" /home/ubuntu/agent-ml-research --include=\"*.py\" --include=\"*.yaml\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"paperreview_ai\" /home/ubuntu/agent-ml-research --include=\"*.py\" --include=\"*.yaml\" 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool call

_source line 1490 · 2026-05-18T05:23:59.104907+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"enabled.*external\\|external.*enabled\" /home/ubuntu/agent-ml-research --include=\"*.yaml\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"enabled.*external\\|external.*enabled\" /home/ubuntu/agent-ml-research --include=\"*.yaml\" 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 1491 · 2026-05-18T05:23:59.256142+00:00_

/home/ubuntu/agent-ml-research/core/tools/project_config.py:    Reads ``external_review.paperreview_ai.enabled`` from project config.
/home/ubuntu/agent-ml-research/core/tools/project_config.py:    return bool(ext.get("paperreview_ai", {}).get("enabled", False))
/home/ubuntu/agent-ml-research/core/api/routers/projects.py:        if "paperreview_ai" in body["external_review"]:
/home/ubuntu/agent-ml-research/core/api/routers/projects.py:            ext.setdefault("paperreview_ai", {}).update(body["external_review"]["paperreview_ai"])

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 453
}
```

</details>

---


### Tool result

_source line 1492 · 2026-05-18T05:23:59.306860+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1493 · 2026-05-18T05:24:00.764439+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/core/tools/project_config.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/core/tools/project_config.py"
  }
}
```

</details>

---


### Tool result

_source line 1494 · 2026-05-18T05:24:01.067039+00:00_

1	"""Project configuration loader — reads config/projects/{name}.yaml.
2	
3	Each project config declares server, codebase paths, evaluation metrics,
4	and W&B settings. The orchestrator injects this into the system prompt
5	and MCP tool defaults at session startup.
6	"""
7	
8	from __future__ import annotations
9	
10	from pathlib import Path
11	
12	import yaml
13	
14	from core.tools.result import ToolResult
15	
16	# ---------------------------------------------------------------------------
17	# Paths
18	# ---------------------------------------------------------------------------
19	
20	from core import paths as _paths
21	
22	
23	# ---------------------------------------------------------------------------
24	# Path expansion — resolve ~ in config values so non-interactive shells work
25	# ---------------------------------------------------------------------------
26	
27	# Top-level keys whose string values may contain ~
28	_PATH_KEYS = {"root", "project_path", "log_dir"}
29	
30	
31	def _expand_paths(config: dict) -> None:
32	    """In-place expand ~ in known path fields using the remote account's home.
33	
34	    These paths refer to remote servers, NOT the local machine.
35	    ``~`` is resolved to ``/home/{account}`` (standard Linux layout)
36	    using the account from ``execution.servers[0].account`` or
37	    ``execution.account``.
38	    """
39	    # Determine remote account for ~ expansion
40	    exec_cfg = config.get("execution", {})
41	    account = exec_cfg.get("account", "")
42	    if not account:
43	        servers = exec_cfg.get("servers")
44	        if isinstance(servers, list) and servers:
45	            first = servers[0]
46	            if isinstance(first, dict):
47	                account = first.get("account", "")
48	    # Fallback: extract account from resources.yaml server host (user@ip)
49	    if not account:
50	        server_name = exec_cfg.get("server", "")
51	        if server_name:
52	            try:
53	                resources_path = _
…[truncated 40953 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1495 · 2026-05-18T05:24:03.529709+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/schema-dag-extraction.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/schema-dag-extraction.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1496 · 2026-05-18T05:24:03.580592+00:00_

File unchanged since last read. The content from the earlier Read tool_result in this conversation is still current — refer to that instead of re-reading.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1497 · 2026-05-18T05:24:03.631806+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/schema-dag-extraction.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/schema-dag-extraction.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1498 · 2026-05-18T05:24:03.683676+00:00_

execution:
  project_path: /root/schema-dag-extraction
  servers:
  - account: root
    server: cqa1-38874
  - account: root
    server: westd-24295
feishu:
  chat_id: oc_51326259fe46fbae9da26b81cf03f1f8
  operational_chat_id: oc_04544c3b7bc497e1d098ba47fb56a6c2
  review_paper_path: projects/schema-dag-extraction/docs/paper/main.tex
  review_round: 15
  review_supplementary_paths: ''
  submission_chat_id: oc_ac7ab7270b6b5caecee04f89b11aab3e
project:
  created_at: '2026-05-14T16:07:46.825Z'
  description: Does Type Confusability Drive Schema-Induced Degradation in LLM Information
    Extraction? An Empirical Study and Principled Decomposition Framework
  name: schema-dag-extraction
  phase: research
  source_idea_id: idea_007
venue: emnlp-2026

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1499 · 2026-05-18T05:24:05.341744+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/ 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 1500 · 2026-05-18T05:24:05.442644+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1501 · 2026-05-18T05:24:05.443128+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/"
  }
}
```

</details>

---


### Tool result

_source line 1502 · 2026-05-18T05:24:05.493653+00:00_

total 16
drwxrwxr-x 2 ubuntu ubuntu 4096 May 17 08:28 .
drwxrwxr-x 5 ubuntu ubuntu 4096 May 17 15:06 ..
-rw-r--r-- 1 ubuntu ubuntu  508 May 14 15:55 collapse-aware-mixing.yaml
-rw-r--r-- 1 ubuntu ubuntu  753 May 18 05:22 schema-dag-extraction.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1503 · 2026-05-18T05:24:07.000856+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/collapse-aware-mixing.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/collapse-aware-mixing.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1504 · 2026-05-18T05:24:07.001285+00:00_

1	execution:
2	  gpu_ids:
3	  - cuda:0
4	  project_path: /root/collapse-aware-mixing
5	  servers:
6	  - cqa1-38874
7	feishu:
8	  chat_id: oc_97115bb0dc57ec1a9a4a1e11cecd1625
9	  operational_chat_id: oc_bec9d64c496a2e90db706ca16ed6c1f3
10	project:
11	  created_at: '2026-05-12T08:44:19.166Z'
12	  description: Spectral Collapse-Aware Adaptive Mixing via Entropy-Reservoir PI Control
13	    for Iterative Synthetic-Real LLM Pretraining
14	  name: collapse-aware-mixing
15	  phase: archived
16	  source_idea_id: idea_012
17	ralph_loop:
18	  enabled: false
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1505 · 2026-05-18T05:24:08.457022+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A 10 -B 10 \"external_review\" /home/ubuntu/agent-ml-research/core/api/routers/projects.py | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A 10 -B 10 \"external_review\" /home/ubuntu/agent-ml-research/core/api/routers/projects.py | head -50"
  }
}
```

</details>

---


### Tool result

_source line 1506 · 2026-05-18T05:24:08.507705+00:00_

    if "model" in body:
        cfg["model"] = body["model"]
    if "feishu" in body:
        cfg.setdefault("feishu", {}).update(body["feishu"])
    if "evaluation" in body:
        eval_cfg = cfg.setdefault("evaluation", {})
        if "wandb" in body["evaluation"]:
            eval_cfg.setdefault("wandb", {}).update(body["evaluation"]["wandb"])
    if "project" in body:
        cfg.setdefault("project", {}).update(body["project"])
    if "external_review" in body:
        ext = cfg.setdefault("external_review", {})
        if "paperreview_ai" in body["external_review"]:
            ext.setdefault("paperreview_ai", {}).update(body["external_review"]["paperreview_ai"])
    _save_project_config(name, cfg)
    return {"ok": True}


@router.get("/projects/{name}/readiness")
def get_project_readiness(name: str):
    """Check project readiness: server, SSH account, connectivity, git credentials.

    Returns a checklist of items with pass/fail status for the Dashboard
    completeness indicator and Director awareness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1507 · 2026-05-18T05:24:18.449680+00:00_

Perfect! Now I have a complete picture. Let me create a summary of my findings:

## Summary

Based on my thorough search of the schema-dag-extraction project configuration, here are my findings:

### Project Configuration File Location:
**File Path**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/schema-dag-extraction.yaml`

### Current Configuration Contents:
The file currently contains the following sections:
- `execution` (servers and project paths)
- `feishu` (chat IDs and review round information)
- `project` (metadata)
- `venue` (EMNLP-2026)

**Important Finding**: The `external_review.paperreview_ai.enabled` setting **is NOT currently defined** in the schema-dag-extraction.yaml configuration file.

### How External Review Configuration Works:

Based on my analysis of the source code:

1. **Configuration Key Location**: When enabled, the setting should appear in the project config YAML at this path:
   ```yaml
   external_review:
     paperreview_ai:
       enabled: true|false
   ```

2. **Code Reference**: The function `is_external_review_enabled()` in `/home/ubuntu/agent-ml-research/core/tools/project_config.py` (lines 420-430) reads this setting:
   ```python
   def is_external_review_enabled(project_name: str) -> bool:
       """Check if external review (paperreview.ai) is enabled for a project.
       Reads ``external_review.paperreview_ai.enabled`` from project config.
       Returns False if not configured."""
       result = load_project_config(project_name)
       if not result.success:
           return False
       ext = result.data["config"].get("external_review", {})
       return bool(ext.get("paperreview_ai", {}).get("enabled", False))
   ```

3. **Default Behavior**: If the setting is not defined, it defaults to `False` (external review is disabled).

4. **External Review Module**: The implementation is located at `/home/ubuntu/agent-ml-research/core/tools/external_review.py`, which handles requesting manual submission to St
…[truncated 358 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Agent",
  "elapsed_ms": 62889
}
```

</details>

---


### Tool call

_source line 1508 · 2026-05-18T05:25:07.685051+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计 + 统计论证**。\n\n## 论文信息\n- **标题**: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n- **论文路径**: `projects/schema-dag-extraction/docs/paper/main.tex`（含 \\input 的 abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex, checklist.tex, prompt_appendix.tex）\n- **目标 venue**: EMNLP 2026 via ARR May 2026 cycle\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板 long paper, 正文 ≤ 8 页 (不含 references + Limitations), double-blind, Limitations section 必填\n- **匿名**: double-blind (论文 \\author{Anonymous})\n\n## 你的审查侧重\n\n**核心关注**:\n1. **统计方法论**: TOST equivalence testing (±3pp margin) 的合理性; linear vs logit scale 选择; 等价检验 power 是否充分; 多重比较处理\n2. **实验设计**: BCS-controlled 实验的 confound 控制; count curve 设计; within-pool vs independent pool 对比的有效性; 样本量 (n=25 vs n=5) 对结论的影响\n3. **效应量与实际意义**: pairwise r²=1.3-1.7% 和 typical batch gap 2.2pp 的 practical significance; 22-53% R² claim 的稳健性 (尤其 DocRED n=25 的 53%)\n4. **跨模型验证**: 3 个模型 family 是否充分支撑 generalizability claim; Dimension 2 仅在 open-weight RE 验证的局限\n5. **因果语言**: Title \"Predict\" vs 正文中是否有残余因果措辞 (\"induced\", \"driven\", \"shape\" 等)\n6. **SDGD 负面结果**: merge amplification 和 routing failure 的诊断深度\n\n**交付物**: 完整审稿报告, 含 Summary (2-3 句), Strengths (逐条), Weaknesses (逐条, severity 标注 critical/major/minor), Questions, Missing References, Overall Assessment (用 ARR/EMNLP 评分标准 1-5 分)。\n\n严格、客观、不留情面。你是评审人, 不是投稿人的盟友。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "schema-dag-extraction",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计 + 统计论证**。\n\n## 论文信息\n- **标题**: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n- **论文路径**: `projects/schema-dag-extraction/docs/paper/main.tex`（含 \\input 的 abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex, checklist.tex, prompt_appendix.tex）\n- **目标 venue**: EMNLP 2026 via ARR May 2026 cycle\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板 long paper, 正文 ≤ 8 页 (不含 references + Limitations), double-blind, Limitations section 必填\n- **匿名**: double-blind (论文 \\author{Anonymous})\n\n## 你的审查侧重\n\n**核心关注**:\n1. **统计方法论**: TOST equivalence testing (±3pp margin) 的合理性; linear vs logit scale 选择; 等价检验 power 是否充分; 多重比较处理\n2. **实验设计**: BCS-controlled 实验的 confound 控制; count curve 设计; within-pool vs independent pool 对比的有效性; 样本量 (n=25 vs n=5) 对结论的影响\n3. **效应量与实际意义**: pairwise r²=1.3-1.7% 和 typical batch gap 2.2pp 的 practical significance; 22-53% R² claim 的稳健性 (尤其 DocRED n=25 的 53%)\n4. **跨模型验证**: 3 个模型 family 是否充分支撑 generalizability claim; Dimension 2 仅在 open-weight RE 验证的局限\n5. **因果语言**: Title \"Predict\" vs 正文中是否有残余因果措辞 (\"induced\", \"driven\", \"shape\" 等)\n6. **SDGD 负面结果**: merge amplification 和 routing failure 的诊断深度\n\n**交付物**: 完整审稿报告, 含 Summary (2-3 句), Strengths (逐条), Weaknesses (逐条, severity 标注 critical/major/minor), Questions, Missing References, Overall Assessment (用 ARR/EMNLP 评分标准 1-5 分)。\n\n严格、客观、不留情面。你是评审人, 不是投稿人的盟友。"
  }
}
```

</details>

---


### Tool result

_source line 1509 · 2026-05-18T05:25:21.576514+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 13891
}
```

</details>

---


### Tool call

_source line 1510 · 2026-05-18T05:25:21.627311+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量 + 格式合规**。\n\n## 论文信息\n- **标题**: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n- **论文路径**: `projects/schema-dag-extraction/docs/paper/main.tex`（含 \\input 的 abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex, checklist.tex, prompt_appendix.tex）\n- **目标 venue**: EMNLP 2026 via ARR May 2026 cycle\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板 long paper, 正文 ≤ 8 页 (不含 references + Limitations), double-blind, Limitations section 必填\n- **匿名**: double-blind (论文 \\author{Anonymous})\n\n## 你的审查侧重\n\n**核心关注**:\n1. **新颖性评估**: SCS/BCS metric 与 LLM-PEE 形式相同的增量在哪? \"首次 controlled study\" claim 是否成立? 对 EMNLP 2026 的 novelty bar 是否足够?\n2. **叙事完整性**: Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成连贯主线? Findings 与 Contributions 是否一一对应? NER null result 如何处理?\n3. **Related Work 定位**: 是否覆盖所有直接竞争者 (LLM-PEE, PARSE, CrossAgentIE, DEE, CMAS-NER, ZeroNER, DLiSC, SPT 等)? positioning 是否准确? 遗漏的重要相关工作?\n4. **写作质量**: AI 写作痕迹 (em-dash, -ing phrases, 过度分段); 术语首次定义; 段落逻辑衔接; Abstract 是否回答四个必答问题 (问题/重要性/方法/结果)\n5. **格式合规**: 页数是否 ≤ 8 页正文? Limitations section 存在? Checklist 完整? 匿名化 (无 author 泄漏)?  引用格式? 图表质量 (字体 ≥ 7pt, 无遮挡)?\n6. **Framing 风险**: extreme-batch gap (25-31pp) vs typical gap (2.2pp) 的叙事权重; \"four datasets\" 中 MAVEN 的参与度; Abstract \"up to -49pp\" 是否 cherry-picking\n\n**交付物**: 完整审稿报告, 含 Summary (2-3 句), Strengths (逐条), Weaknesses (逐条, severity 标注 critical/major/minor), Questions, Missing References, Overall Assessment (用 ARR/EMNLP 评分标准 1-5 分)。\n\n严格、客观、不留情面。你是评审人, 不是投稿人的盟友。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "schema-dag-extraction",
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量 + 格式合规**。\n\n## 论文信息\n- **标题**: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n- **论文路径**: `projects/schema-dag-extraction/docs/paper/main.tex`（含 \\input 的 abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex, checklist.tex, prompt_appendix.tex）\n- **目标 venue**: EMNLP 2026 via ARR May 2026 cycle\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板 long paper, 正文 ≤ 8 页 (不含 references + Limitations), double-blind, Limitations section 必填\n- **匿名**: double-blind (论文 \\author{Anonymous})\n\n## 你的审查侧重\n\n**核心关注**:\n1. **新颖性评估**: SCS/BCS metric 与 LLM-PEE 形式相同的增量在哪? \"首次 controlled study\" claim 是否成立? 对 EMNLP 2026 的 novelty bar 是否足够?\n2. **叙事完整性**: Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成连贯主线? Findings 与 Contributions 是否一一对应? NER null result 如何处理?\n3. **Related Work 定位**: 是否覆盖所有直接竞争者 (LLM-PEE, PARSE, CrossAgentIE, DEE, CMAS-NER, ZeroNER, DLiSC, SPT 等)? positioning 是否准确? 遗漏的重要相关工作?\n4. **写作质量**: AI 写作痕迹 (em-dash, -ing phrases, 过度分段); 术语首次定义; 段落逻辑衔接; Abstract 是否回答四个必答问题 (问题/重要性/方法/结果)\n5. **格式合规**: 页数是否 ≤ 8 页正文? Limitations section 存在? Checklist 完整? 匿名化 (无 author 泄漏)?  引用格式? 图表质量 (字体 ≥ 7pt, 无遮挡)?\n6. **Framing 风险**: extreme-batch gap (25-31pp) vs typical gap (2.2pp) 的叙事权重; \"four datasets\" 中 MAVEN 的参与度; Abstract \"up to -49pp\" 是否 cherry-picking\n\n**交付物**: 完整审稿报告, 含 Summary (2-3 句), Strengths (逐条), Weaknesses (逐条, severity 标注 critical/major/minor), Questions, Missing References, Overall Assessment (用 ARR/EMNLP 评分标准 1-5 分)。\n\n严格、客观、不留情面。你是评审人, 不是投稿人的盟友。"
  }
}
```

</details>

---


### Tool result

_source line 1511 · 2026-05-18T05:25:23.141032+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1513
}
```

</details>

---


### Assistant

_source line 1512 · 2026-05-18T05:25:27.035053+00:00_

Round 1 审稿任务已分配:
- **Reviewer 1** (方法/实验/统计): 已触发
- **Reviewer 2** (新颖性/完整性/写作): 已触发

等待两位 Reviewer 返回独立审稿报告后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 134

## Round 134

2 recorded events


### User

_source line 1513 · 2026-05-18T05:29:46.331481+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿报告：方法严谨性 + 实验设计 + 统计论证

**论文**: "How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?"
**Venue**: EMNLP 2026 via ARR May 2026
**审查侧重**: 统计方法论、实验设计、效应量与实际意义、跨模型验证、因果语言、SDGD 负面结果

---

## 总体评分

**Overall**: 3.5 / 5（Borderline Conference）
**一句话总结**: 一篇严谨的实证分析论文，实验设计精细、负面结果诚实，但核心贡献受限于效应量的实际意义偏弱，且 logit-scale 等价检验的不确定性削弱了"bounded association"这一关键 claim 的稳健性。

---

## 官方维度打分（来自 ARR Review Form, Feb 2025 onwards）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5 / 5 | 主要 claim 有充分支撑，但 logit-scale TOST 不确定性（p=0.209）与线性 scale 选择的 framing 偏差构成方法论弱点；部分核心数字（DocRED R²=0.53）CI 极宽 |
| **Excitement** | 3 / 5 | 对 training-free IE 的 failure mode 提供了有价值的系统化理解，但 actionability 有限（2.2pp typical gap 难以驱动实际 schema 设计决策），负面 SDGD 结果有意义但缺乏替代方案 |
| **Reproducibility** | 4 / 5 | 实验细节充分（decoding 参数、seed、batch 构造协议均有说明），prompt 模板完整给出，代码承诺 release；但 FewRel train+val 合并的具体 sampling 细节和 BCS batch 构造算法需要代码才能完全复现 |
| **Confidence** | 4 / 5 | 统计方法论和实验设计是我的核心专长，我仔细检查了论文的所有统计 claim |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Logit-scale TOST 不确定性被低估，"bounded association" claim 需要重新表述

- 具体位置：§5.4 Multi-Dimensional Degradation, Appendix §F (Factorial Analysis)
- 问题：论文的核心 claim 之一是 count 和 confusability 在 RE 上具有"bounded association"（TOST p=0.003 at ±3pp）。然而 Appendix 明确报告 logit-scale interaction 为 0.111 logit units（p=0.047, marginally significant），logit-scale TOST inconclusive（p=0.209）。论文选择 linear scale 作为"primary test"并将 logit 分析降级为 sensitivity check，但这一选择本身就有利于作者的结论。在 accuracy 接近 50%（high-BCS batches 的 floor 就在 ~51%）时，linear scale 压缩 interaction effects 是已知的统计特性。论文虽然承认了这一点（"accuracy near 50% compresses interaction effects on the linear scale"），但随后仍以 linear-scale 结论为主导叙事。
- 为什么影响接收：如果 logit scale 上 interaction 是 marginally significant，那么 Dimension 1 和 Dimension 2 的独立性在 RE 上就不是"bounded"而是"inconclusive"，这直接影响 §5.4 的"two independent dimensions"框架和 Discussion 中"no confusability amplification at scale"的实践建议。
- 建议修改方向：（1）正文中（不仅是 Appendix）报告 logit-scale 结果，将 bounded association claim 降级为"bounded under linear specification, inconclusive under logit"；（2）承认 scale 选择是一个分析自由度；（3）或者增加样本量（n=69 对于 TOST 偏低）以提供更有力的检验。

**N2** [critical] DocRED R²=0.53 的 claim 稳健性不足

- 具体位置：§5.3 BCS-Controlled Experiments, Appendix §I (BCS-Controlled Detailed Results)
- 问题：论文多处引用"BCS explains 22-53% of cross-batch RE accuracy variance"（Abstract, §1 Introduction contribution 2, §5.3, §7 Discussion），其中 53% 来自 DocRED count=16 的 n=35 batches OLS 回归。Appendix 报告 adjusted R²=0.511，Fisher z CI=[0.27, 0.73]。这个 CI 跨度 46 个百分点，意味着真实 R² 可能低至 27%（与 FewRel 的 22% 相近）或高至 73%。用 n=35 的 point estimate 0.53 作为范围上界（"22-53%"）在叙事中反复出现，给读者一种 BCS 解释力可达一半以上的印象，但实际不确定性极大。
- 为什么影响接收：这是论文 contribution 2 的核心数字之一，如果审稿人注意到 CI 宽度，会质疑 claim 的 precision。
- 建议修改方向：（1）正文中报告 CI（不只在 Appendix）；（2）将"22-53%"改为更保守的表述，如"22% on FewRel (n=100), up to 53% on DocRED (n=35, CI [0.27, 0.73])"，让读者自行判断；（3）或增加 DocRED 的 batch 数量以缩窄 CI。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] 缺乏 formal power analysis

- 具体位置：§3.3 Experimental Design, Appendix §F (Factorial)
- 问题：论文多处承认 power 不足（2×2 factorial p_TOST=0.56 "due to limited power"; 80-relation full condition n=25 "underpowered"；NER BCS batch-level r≈0 可能因 boundary errors 淹没信号也可能因 power 不足），但从未报告事前或事后 power analysis。TOST 检验的 power 直接取决于样本量和效应量；n=69 的 TOST 对 ±3pp margin 的 power 是多少？如果 power 不足 80%，则 equivalence conclusion 本身就不可靠。
- 建议：报告 TOST 的 post-hoc power（或 sensitivity analysis 给出在当前 n 下可探测的最小等价 margin）；对 NER 的 null batch-level result，报告在当前 n=450 下可探测的最小 effect size。

**W2** [major] Pairwise r²=1.3-1.7% 的实际意义论证薄弱

- 具体位置：§5.2 Pairwise Confusability (Table 2), §6.2 Related Work (SCS novelty paragraph)
- 问题：论文将 r²=1.3-1.7% 援引 Cohen (1988) 称为"small but real"，并论证其在 batch-level 聚合后放大到 R²=22%。Cohen 的分类本身在心理学界已有争议（Funder & Ozer, 2019），且 Cohen 本人警告不应机械套用。更关键的是：论文从 unconditional r²=1.3% 到 conditional r²=7%（只看非零混淆对）再到 batch R²=22% 的链条，虽然 Monte Carlo 模拟验证了数学一致性，但这依赖于 inter-pair SCS correlation ρ=0.35 的估计，该估计的 uncertainty 未被讨论。如果 ρ 偏低（如 0.20），simulated batch R² 会显著低于 22%。
- 建议：（1）报告 ρ=0.35 的 CI；（2）在 simulation 中做 ρ 的 sensitivity analysis；（3）弱化"小效应聚合为大效应"的叙事语气，让数据更中立地说话。

**W3** [major] 单 seed 实验设计对绝对值 claim 的限制

- 具体位置：§3.5 Model and Inference
- 问题：主实验使用 greedy decoding (temperature=0, seed=42)，论文论证 inter-seed variance 小（SD=0.88pp at count 80, Appendix §K）。但 cross-seed analysis 仅在 FewRel count curves 上做了 3 seeds（§5.1），BCS-controlled experiments、DocRED、MAVEN、cross-model validation 均为单 seed。论文报告的绝对数字（如 extreme-batch gap 31.2pp, BCS slope -0.509）的 uncertainty 因此被低估——bootstrap CI 只捕获了 batch composition variance，没有捕获 seed variance。
- 建议：至少对核心 BCS-controlled RE 实验跑 3 seeds 并报告 seed-level variance，或在 Limitations 中明确说明单 seed 设计对绝对值估计的影响。

**W4** [major] Dimension 2 跨模型验证不充分

- 具体位置：Appendix §L (Cross-Model 70B), §M (Cross-Model Gemini), Limitations item 1
- 问题：Dimension 1（count decline）在 4 个模型上验证（Qwen3-32B, Llama-8B, Llama-70B, Gemini Flash），但 Dimension 2（BCS-controlled confusability）仅在 Qwen3-32B（主模型）和 Llama-8B（Table A2 的 cross-model BCS）上有完整验证，Llama-70B 只有 count=16 的一个 BCS gap 数据点（§L），Gemini 没有 Dimension 2 数据。论文 Abstract 和 Conclusion 的措辞"patterns replicate across model scales (8B to 70B) and architecture families (Qwen, LLaMA, Gemini)"暗示两个 dimension 均已验证，但实际上 Dimension 2 的跨架构证据仅限于两个 open-weight 模型。
- 建议：Abstract/Conclusion 中区分两个 dimension 的验证范围；或补充 Llama-70B 和 Gemini 的 BCS-controlled 实验。

**W5** [moderate] TOST ±3pp margin 的 justification 存在循环论证风险

- 具体位置：Appendix §F "Equivalence margin justification"
- 问题：三个 anchor 中，"Empirical" anchor 基于"typical random-batch confusability variation produces 2-5pp accuracy differences (batch SD ≈ 4.6pp at count 32)"，即用数据本身的变异性来定义等价 margin。"Statistical" anchor 将 3pp 等价于 0.5×batch SD ≈ Cohen's d=0.5，但 Cohen's d=0.5 是 "medium effect" 的门槛，用它来定义"negligible interaction"逻辑上说不通（medium effect 怎么能算 negligible？）。论文随后补充"A 3pp interaction atop the 2.2pp confusability main effect would represent >130% amplification"，这个论证更有说服力，应该作为主要 justification。
- 建议：重组 margin justification，以 130% amplification 论证为主线，弱化 Cohen's d=0.5 的类比（或正确引用 d=0.5 意味着 medium 而非 small effect）。

**W6** [moderate] NER 评估指标的局限性影响 Dimension 2 的 NER null result 解读

- 具体位置：Limitations item 5, §5.4
- 问题：论文使用 exact-match NER 评估，但 Limitations item 5 承认这"conflates boundary errors with type errors"。如果 NER 的 batch-level BCS null result（r≈0）部分因为 exact-match 将 type confusion 和 boundary errors 混在一起，那么更宽松的匹配标准可能会揭示 NER 也存在 batch-level confusability signal。这使得"BCS explains RE but not NER"这一 task asymmetry claim 的确定性降低。
- 建议：补充 relaxed-match（如 type-only 或 partial-span）NER 评估下的 BCS--F1 相关性，或将 task asymmetry claim 表述为"under exact-match evaluation"。

---

## 小问题（不影响接收）

- **M1**: Table 2 只报告了 Few-NERD 和 MAVEN 的 pairwise correlation，FewRel 的 r=0.187 在 §3.4 提及但未入表（caption 解释了原因），建议统一呈现或在 table caption 中加入 FewRel 数字。
- **M2**: Appendix §F 中"Logit-scale sensitivity"段落用"logit-transformed accuracy"但未给出 logit 变换的具体公式（log(p/(1-p))），对非统计背景读者不友好。
- **M3**: §5.1 中"plateauing across counts 22-44 before partial recovery at full-schema (0.41)"——这个 U-shaped NER 曲线的解释（"elimination of type-filtering overhead"）缺乏实验证据支持，更像是猜测。
- **M4**: Gemini count 64 基于 13/25 batches（Table A8），partial data 的 Spearman ρ 可信度打折扣，建议删除或标注更显著。
- **M5**: Appendix §J 的 aggregation simulation 声称"not the evidence base for our claims"，但正文 §5.3 和 §7 均引用了 "~3× pair-to-batch amplification" 这一 simulation 结果来解释 R² 的 scaling——如果 simulation 不是证据，就不应在论证链中使用。
- **M6**: Few-NERD 使用 Qwen3 自身的 embedding 计算 SCS（§3.3），存在 shared-representation dependency。虽然 MiniLM cross-check 结果一致（r=0.172 vs 0.138），但 Qwen3 embedding 产生更低的 r 反而削弱了 SCS 的解释力，这一 counterintuitive 结果值得讨论。
- **M7**: References 中 Gemini 2025 的 arXiv ID 是 2507.06261——这个 ID 对应 2025 年 7 月的论文，但论文投稿日期是 2026 年 5 月 ARR cycle，时间线上没问题，但请确认引用的正确性（arXiv 2507 = 2025 July）。

---

## 主要优势

1. **实验设计精细且系统化**：Count curves + BCS-controlled 的双范式设计有效隔离了 count 和 confusability 两个因素（§3.3）。Within-pool analysis（从 80-relation pool 抽取 16-relation subsets）控制了 pool composition confound（Table 5），permutation test p=0.60 有说服力。

2. **统计严谨性高于同类工作**：使用 TOST 等价检验（而非仅靠 NHST 的 non-significance）、bootstrap CI、cluster bootstrap、permutation tests、variance decomposition。Rothman (1990) 关于多重比较的引用虽有争议但有理论依据。TOST sensitivity analysis across margins（Table A4）和 logit-scale sensitivity check 均体现了审慎态度。

3. **负面结果的诊断深度出色**：SDGD failure 不仅报告了"不 work"，还诊断了 merge amplification（precision collapse 0.563→0.210）和 routing failure（constrained decoding 导致 73.4% instances 在 3-5 个 sub-schemas 同时获得 positive predictions），并区分了 NER（merge 问题）和 RE（routing 问题）的不同 failure mode（§6, Appendix §E）。

4. **Centrality confound 的发现和处理（§5.5）**：MAVEN 上 BCS-F1 正相关的发现、centrality confound 的诊断、partial correlation 控制后效应消失（p>0.2），以及"mean BCS 只适用于 cross-domain schemas"的结论，是一个有价值的方法论贡献。

5. **Limitations 极为坦诚**：8 条 Limitations + Multiple comparisons 讨论，涵盖了几乎所有我能想到的弱点（包括 causal mechanism、data contamination、NER metric、RE format specificity）。这在 NLP 论文中不常见。

6. **多层 robustness check**：Cross-model (4 models)、cross-prompt (4 variants, Table A6)、cross-embedding (MiniLM vs Qwen3, Appendix §H)、cross-seed (3 seeds, Appendix §K)、cross-dataset (FewRel→DocRED replication)。

---

## Questions for Authors

Q1: TOST 在 n=69 下对 ±3pp margin 的 statistical power 是多少？如果 power < 0.8，equivalence conclusion 的可信度如何？

Q2: Aggregation simulation（Appendix §J）中 inter-pair SCS correlation ρ=0.35 的估计方法是什么？其 CI 是多少？如果 ρ=0.20，simulated batch R² 大约是多少？

Q3: 论文是否尝试过在 NER 上使用 type-only matching（忽略 boundary）来检测 batch-level confusability signal？如果没有，这是否是一个值得做的实验？

Q4: Few-NERD U-shaped count curve 的 partial recovery（count 66, recall=0.41 vs count 22-44 plateau ~0.27）有没有更具体的解释？"elimination of type-filtering overhead"是什么机制？

Q5: Oracle routing 在 RE 上恢复了 +29.8pp（Table 6），但所有 practical routing strategies 都 fail。作者是否尝试过 embedding-based routing（用 SCS 将 test instance 路由到最相关的 sub-schema）而非 confidence-based routing？

---

## Missing References

- Funder & Ozer (2019), "Evaluating Effect Size in Psychological Research: Sense and Nonsense"——关于 Cohen's effect size 分类的批判性讨论，与 §6.2 的 "small but real" claim 相关。
- Wellek (2010), "Testing Statistical Hypotheses of Equivalence and Noninferiority"——TOST 方法论的权威教材，比 Lakens (2017) 更 comprehensive。
- Schuirmann (1987), "A comparison of the Two One-Sided Tests Procedure..."——TOST 的原始论文，论文只引用了 Lakens (2017) 的 primer。
- 关于 constrained decoding 对 calibration 影响的文献（论文 §6 中 routing failure 归因于 constrained decoding 消除了 confidence signal，但缺乏这方面的 citation）。

---

## 格式合规检查

- ✅ ACL 模板 `\usepackage[review]{acl}`
- ✅ `\author{Anonymous}`（double-blind）
- ✅ Limitations section 在正文末尾（References 之前）
- ✅ Responsible NLP Research Checklist 完整
- ⚠️ 页数限制需编译确认（正文内容较多，§1-§7 + Limitations + Checklist，可能接近或超过 8 页）
- ✅ 行号已启用（review option）

---

## 总结

这是一篇高于平均水平的实证分析论文。实验设计的 sophistication（BCS-controlled, within-pool, TOST, variance decomposition）和负面结果的诊断深度值得肯定。主要 concern 是：（1）logit-scale TOST inconclusive 结果削弱了 core claim 的稳健性但论文 framing 偏向有利结论；（2）R²=22-53% 的上界 CI 极宽；（3）typical effect size（2.2pp）的 practical actionability 有限。如果作者能在 rebuttal 中（a）报告 TOST power analysis，（b）正文中报告 DocRED R² 的 CI，（c）明确区分 Dimension 2 的跨模型验证范围，我会考虑上调至 4。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1514 · 2026-05-18T05:29:53.248288+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 提交后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 135

## Round 135

2 recorded events


### User

_source line 1515 · 2026-05-18T05:29:58.604127+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

核心评判：**Overall 3.5（Borderline Conference）**。

主要发现：

**2 个 Must-Fix 问题**：
1. Logit-scale TOST inconclusive (p=0.209) 与论文主导叙事的 linear-scale "bounded association" 存在矛盾，scale 选择构成分析自由度，需在正文中透明报告
2. DocRED R²=0.53 的 CI 极宽 [0.27, 0.73]，"22-53%" 这一反复使用的 claim 上界不够稳健

**6 个 Should-Fix 问题**涉及：缺乏 formal power analysis、pairwise r²=1.3% 实际意义的论证链薄弱（ρ=0.35 估计未报 CI）、单 seed 设计对绝对值 claim 的限制、Dimension 2 跨模型验证不充分（Abstract/Conclusion 措辞暗示全面验证但实际仅 2 个 open-weight 模型）、TOST margin justification 中 Cohen's d=0.5 类比有误（medium≠negligible）、NER exact-match 指标可能掩盖 batch-level confusability signal。

**主要优势**：实验设计精细（BCS-controlled + within-pool 控制 confound）、统计严谨性高于同类工作、SDGD 负面结果诊断深度出色、centrality confound 处理有方法论价值、Limitations 极其坦诚。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1516 · 2026-05-18T05:30:05.634201+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 提交后启动交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 136

## Round 136

6 recorded events


### User

_source line 1517 · 2026-05-18T05:32:35.206208+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告

**论文**: "How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?"
**Venue**: EMNLP 2026 via ARR May 2026 cycle
**评分标准来源**: [ACL ARR Review Form](https://aclrollingreview.org/reviewform) + [ARR Reviewer Guidelines](https://aclrollingreview.org/reviewerguidelines)

---

## 总体评分

**Overall Assessment**: 3.0 / 5 (Findings)
**一句话总结**: 实验方法论出色的 empirical study，但 SCS/BCS metric 无新颖性（与 LLM-PEE 形式相同），强结果集中在 RE 任务且 typical-batch effect size 仅 2.2pp，novelty 和 practical significance 均不足以支撑主会议接收。

---

## 官方维度打分（来自 ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5 / 5 | BCS-controlled quasi-experiments 设计合理，统计方法（TOST, permutation tests, bootstrap CIs）高于平均水平；但 logit-scale TOST inconclusive 削弱 bounded-association claim，single-seed 实验在 2.2pp effect size 下 variance 不充分 |
| **Excitement** | 2.5 / 5 | 研究问题有实际意义，但核心发现——schema 越大性能越差——已是共识；confusability 维度的 practical effect 很小（2.2pp），强结果局限于 RE，缺乏 actionable takeaway |
| **Reviewer Confidence** | 4 / 5 | 仔细阅读了全文及所有 appendix，熟悉 zero-shot IE 和 schema complexity 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **SCS/BCS 无独立新颖性，"first controlled study" claim 需要更严格 qualify**
- 具体位置：Abstract line 3 ("operationalize confusability via the Schema Confusability Score (SCS)")；§2 "SCS novelty" paragraph；§1 Contribution 2
- 问题：SCS 就是 pairwise cosine similarity of type name embeddings，论文自己承认 "SCS shares its formal definition (pairwise cosine similarity of type name embeddings) with the partitioning criterion used in LLM-PEE" (§2)。BCS 是其 mean aggregation。这两个 metric 在形式上完全没有增量。论文的新颖性完全在于 experimental framework 和 findings，但 Abstract 和 Contribution list 的措辞 ("operationalize confusability via SCS") 暗示 SCS 本身是贡献。"first controlled study" 也需 qualify——基本现象（schema size degrades performance）已有 Li et al. (2023)、LLM-PEE 等报告，真正 first 的是通过 stratified BCS-controlled design 隔离 count 与 confusability。
- 为什么影响接收：novelty 是 EMNLP 接收的核心标准。如果审稿人认为 metric 是 prior work 的重复而 framing 不够诚实，会导致 reject。
- 建议修改方向：在 Abstract 和 Contribution 2 中明确说 "SCS uses the same cosine-similarity metric as LLM-PEE; our contribution is the controlled experimental framework that isolates its predictive role"。

**N2** [critical] **Confusability effect size 在典型条件下非常小（2.2pp），Abstract framing 有 cherry-picking 嫌疑**
- 具体位置：Abstract ("up to −49pp, document-level RE at full schema"；"BCS explains 22–53% of cross-batch RE accuracy variance")；§5.3 practical magnitude
- 问题：Abstract 领衔数字 "−49pp" 来自 DocRED 全 schema 极端条件，而 typical-batch BCS gap 仅 2.2pp（§5.3），pairwise $r^2$ 仅 1.3–1.7%（Table 2）。"BCS explains 22–53%" 技术上准确，但 22% 是 random batches 的 $R^2$，practical IQR gap 只有 2.2pp。极端 batch 的 25–31pp gap 来自刻意构造的 extreme-BCS batches（最高/最低 BCS），不代表自然场景。论文 §5.3 有交代（"roughly 7% of the extreme-batch gap"），但 Abstract 不体现这一点。
- 为什么影响接收：审稿人会质疑 practical significance——如果 confusability 在典型使用中只带来 2.2pp 差异，这个 factor 对从业者有多大意义？
- 建议修改方向：Abstract 应报告 typical-batch magnitude（2.2pp）和 extreme-batch magnitude 两者，而非只报最大值。将 "up to −49pp" 改为 count-related decline 的标签（这实际是 Dimension 1 而非 Dimension 2 的数字）。

**N3** [critical] **NER 和 ED 结果本质上是 null result，削弱 "three tasks, four datasets" 的 generality claim**
- 具体位置：§5.3 ("BCS explains 22–53% of cross-batch RE accuracy variance but not NER")；§5.5 ("batch-level BCS–performance relationship is RE-specific: … shows no correlation with NER F1")；§5.6 (MAVEN positive correlation attributable to confounds)
- 问题：BCS 对 NER F1 的 batch-level 相关为 $r \approx 0$（n=450）。MAVEN per-type BCS 被 centrality confound 完全解释（controlling 后 $p > 0.2$）。Pairwise SCS 在 NER 上 $r = 0.112$，虽显著但极弱（$r^2 = 1.3\%$）。论文标题 "Training-Free LLM Information Extraction"（无限定词）暗示跨任务通用性，但实质上 confusability 的 strong story 仅在 RE（FewRel + DocRED）成立。NER 和 ED 更像是框架的 failure cases 而非成功验证。Contribution 3 将此 framing 为 "discover a task asymmetry"，这是合理的补救，但 Abstract/title 的 generality 暗示需要调整。
- 为什么影响接收：如果核心发现仅适用于 RE classification 这一种 format，paper 的 scope 和 impact 显著缩小。
- 建议修改方向：标题或 Abstract 中加入 RE-specificity 的限定。或者，将 NER/ED null results 作为同等重要的 findings 在 Abstract 中平衡呈现。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] **MAVEN 参与度极低，不支撑 "event detection" 和 "four datasets" 的 claim**
- 具体位置：Table 2（MAVEN 贡献 1 行 pairwise 数据）；§5.1（count curve 仅描述为 "reversed trend"）；§5.6（centrality confound 使 batch-level 分析不可用）
- 问题：MAVEN 在全文中仅贡献了 Table 2 中一行 pairwise 相关（$r = 0.129$）和一个 centrality confound 分析。它的 count curve 未在主结果中展示，batch-level BCS 分析因 confound 被排除。"四个数据集" 的 claim 在形式上成立，但 MAVEN 的实质贡献极为有限。
- 建议：要么增加 MAVEN 的 count-curve 分析（即使结果反向），要么降低 "four datasets" 的表述力度（如 "three primary datasets with supplementary event detection analysis"）。

**W2** [major] **Logit-scale TOST inconclusive 削弱 bounded-association 核心 claim**
- 具体位置：§5.5；Appendix E（logit-scale interaction 0.111 logit units, $p_{TOST} = 0.209$）
- 问题：RE accuracy 很多在 50% 附近（high-BCS ≈ 51%），线性尺度在此处压缩 interaction effects。Logit scale 更适合 accuracy 数据，但 TOST 在 logit scale 上 inconclusive。论文选择 linear scale 作为 primary 因为 "direct interpretability in percentage points"，但这是一个 methodological choice 而非 methodological necessity。如果 interaction 在 logit scale 上不能被 bounded，则 count × confusability independence 的 claim 不够 robust。
- 建议：至少将 logit-scale 结果提升到正文而非仅在 appendix，并讨论 scale choice 对 conclusion 的影响。当前正文 §5.5 提及但过于简略。

**W3** [major] **Single-seed (seed=42) 实验，effect size 与 seed variance 可比**
- 具体位置：§4.5 "single-seed evaluation with greedy decoding"；Appendix L Table 12（seed SD up to 2.7pp at count 16）
- 问题：Appendix L 显示 count 16 的 seed SD = 2.7pp，与 typical confusability effect（2.2pp）可比。虽然 greedy decoding 减少了 inference stochasticity，seed variance 反映的是 "differences in which random batch compositions each seed generates"（Appendix L），而 typical BCS gap 2.2pp 恰好在这个量级内。这意味着 2.2pp 的 confusability effect 可能在某些 seed 下不显著。
- 建议：增加 multi-seed replication of the BCS-controlled experiment（不仅是 count curves），或在讨论中明确承认 typical effect size 与 seed variance 的可比性。

**W4** [minor-major] **Abstract "up to −49pp" 混淆了 Dimension 1 和 Dimension 2**
- 具体位置：Abstract ("count-related recall decline (up to −49pp, document-level RE at full schema)")
- 问题：−49pp 是 DocRED 的 count-related decline（88.0% → 38.7%），属于 Dimension 1（count）。但 Abstract 的叙事结构让读者可能将此与 confusability 效应混淆。这个数字描述的是 schema size 从小到全（1 → 96 types）的 total degradation，包含 count 和 confusability 的混合效应，而非 controlled confusability effect。
- 建议：在 Abstract 中区分 total degradation（count + confusability mixed）和 isolated confusability effect（2.2pp typical），避免二者混淆。

**W5** [minor] **缺失相关工作：DLiSC 和 SPT**
- DLiSC (Dual-LoRA with Incremental Schema Caching, arXiv:2505.14992, 2025)：通过 identification-extraction 两阶段分解处理 schema complexity，直接相关。
- SPT (Schema as Parameterized Tools, arXiv:2506.01276, 2025)：将 schema 作为 parameterized tokens，与 schema-aware IE 相关。
- 这两篇均较新，不 cite 不影响 novelty claim，但 Related Work 的完整性会受质疑。

**W6** [minor] **5 个 orphan bib entries**
- bogdanov2024nuner, cheng2023batch, levy-2024-same-task, xie2024selfimproving, zhang2023llmaaa 在 .bib 文件中但未被 cite。应清理。

---

## 小问题（不影响接收）

- §5.1 NER U-shaped recovery（full schema 比中间 schema 好）解释为 "type-filtering overhead elimination"，但这仅是推测，缺乏 evidence。
- Limitations section 非常长（8 items + multiple comparisons paragraph），内容充实但可精简。这实际是论文的亮点——transparency 远超平均水平。
- 引用验证：60 个 cited keys 中 4 个在 OpenAlex 中未找到（gemini-2025, dror-2018-significance, sclar-sensitivity-2024, li2023evaluating），多为 API 匹配限制而非虚假引用。
- AI 写作痕迹检查：**非常干净**。全文无 em-dash，无 "Furthermore/Moreover/Additionally" 连续使用，无 -ing phrase 结尾，无 AI 典型词汇（leverage/utilize/facilitate 等）。写作质量优于多数 submission。
- 格式合规：正文恰好 8 页 ✓，Limitations section 存在 ✓，Checklist 完整 ✓，匿名化正确 ✓，line numbers 可见（review mode）✓，ACL template 使用正确 ✓。

---

## 主要优势

1. **实验设计严谨**：BCS-controlled quasi-experiments 通过固定 count 变化 BCS 来隔离 confusability，within-pool analysis 排除 pool composition confound，permutation test 验证 slope consistency。这是方法论上的 best practice。

2. **统计方法高于平均水平**：TOST equivalence testing（而非仅 null significance testing），bootstrap CIs（percentile method, B=10,000），cluster bootstrap for pairwise correlations，variance decomposition。多数 EMNLP submissions 不会做到这个程度。

3. **Cross-model validation 充分**：Qwen3-32B → Llama-3.1-8B → Llama-3.1-70B → Gemini 2.5 Flash (API)，覆盖 open-weight 和 proprietary models，8B 到 70B+ scales。Dimension 1 在所有模型上复制。

4. **负面结果报告诚实**：SDGD failure（§6）不仅报告失败，还诊断了具体机制（merge amplification in NER, routing failure in RE）。Few-shot demonstrations 反而扩大 confusability gap 的发现（+4.3pp）也是有价值的负面结果。

5. **Limitations section 模范级别**：8 条 limitation 覆盖 model coverage, effect size, factorial interaction, decomposition scope, evaluation metric, format specificity, causal mechanism, data contamination，每条都有具体数字和 evidence。远超平均水平。

6. **写作质量高**：无 AI 写作痕迹，叙事清晰，段落逻辑衔接好。术语首次出现均有定义。

---

## 给 Director 的总结判断

**推荐：Findings (3.0)**

这是一篇方法论扎实的 empirical study，statistical rigor 和 experimental design 显著高于平均水平，Limitations 的 transparency 值得表扬。但存在三个结构性问题：(1) SCS/BCS metric 无新颖性（与 LLM-PEE 形式相同），incremental contribution 仅在 experimental framework；(2) confusability 的 practical effect size 在 typical conditions 下很小（2.2pp），Abstract framing 偏向 extreme-condition 数字，有 overclaiming 风险；(3) 强结果集中在 RE classification，NER 和 ED 基本是 null results，"three tasks, four datasets" 的 generality 虚高。

Soundness 没有硬伤（3.5），但 excitement 不足（2.5）。总体适合 Findings track 而非主会议。如果作者能 (a) 更诚实地 frame SCS/BCS 的 novelty 来源，(b) 在 Abstract 中平衡报告 typical vs extreme effect sizes，(c) 降低跨任务 generality 的 claim 力度，论文会更 convincing。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1518 · 2026-05-18T05:32:57.192134+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W6) 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告\n\n**Overall Assessment**: 3.0 / 5 (Findings)\n\n### Must-Fix 问题\n\n**N1** [critical] SCS/BCS 无独立新颖性，\"first controlled study\" claim 需要更严格 qualify\n- SCS 就是 pairwise cosine similarity of type name embeddings，论文自己承认与 LLM-PEE 形式相同 (§2)。BCS 是其 mean aggregation。metric 无增量，新颖性完全在 experimental framework 和 findings。但 Abstract/Contribution 措辞 (\"operationalize confusability via SCS\") 暗示 SCS 本身是贡献。\n\n**N2** [critical] Confusability effect size 在典型条件下非常小（2.2pp），Abstract framing 有 cherry-picking 嫌疑\n- Abstract 领衔数字 \"−49pp\" 来自 DocRED 全 schema 极端条件（Dimension 1），typical-batch BCS gap 仅 2.2pp。极端 batch 的 25–31pp gap 来自刻意构造的 extreme-BCS batches。Abstract 不体现 practical magnitude。\n\n**N3** [critical] NER 和 ED 结果本质上是 null result，削弱 \"three tasks, four datasets\" 的 generality claim\n- BCS 对 NER F1 batch-level r≈0 (n=450)。MAVEN per-type BCS 被 centrality confound 完全解释。Pairwise SCS 在 NER 上 r=0.112 (r²=1.3%)。标题无限定词暗示跨任务通用性，但 confusability strong story 仅在 RE 成立。\n\n### Should-Fix 问题\n\n**W1** [major] MAVEN 参与度极低，不支撑 \"event detection\" 和 \"four datasets\" claim\n**W2** [major] Logit-scale TOST inconclusive 削弱 bounded-association 核心 claim\n**W3** [major] Single-seed (seed=42) 实验，effect size 与 seed variance 可比 (seed SD=2.7pp at count 16 vs typical gap 2.2pp)\n**W4** [minor-major] Abstract \"up to −49pp\" 混淆了 Dimension 1 和 Dimension 2\n**W5** [minor] 缺失相关工作：DLiSC 和 SPT\n**W6** [minor] 5 个 orphan bib entries\n\n### 主要优势\n实验设计严谨、统计方法高于平均、cross-model validation 充分、负面结果诚实、Limitations 模范级别、写作质量高（无 AI 痕迹）\n\n### 总结判断\n推荐 Findings (3.0)。Soundness 3.5 但 Excitement 2.5。强结果集中在 RE，NER/ED 基本 null results，SCS/BCS metric 无新颖性，typical effect size 2.2pp practical significance 有限。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "schema-dag-extraction",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个 Must-Fix (N1-N3) 和 Should-Fix (W1-W6) 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告\n\n**Overall Assessment**: 3.0 / 5 (Findings)\n\n### Must-Fix 问题\n\n**N1** [critical] SCS/BCS 无独立新颖性，\"first controlled study\" claim 需要更严格 qualify\n- SCS 就是 pairwise cosine similarity of type name embeddings，论文自己承认与 LLM-PEE 形式相同 (§2)。BCS 是其 mean aggregation。metric 无增量，新颖性完全在 experimental framework 和 findings。但 Abstract/Contribution 措辞 (\"operationalize confusability via SCS\") 暗示 SCS 本身是贡献。\n\n**N2** [critical] Confusability effect size 在典型条件下非常小（2.2pp），Abstract framing 有 cherry-picking 嫌疑\n- Abstract 领衔数字 \"−49pp\" 来自 DocRED 全 schema 极端条件（Dimension 1），typical-batch BCS gap 仅 2.2pp。极端 batch 的 25–31pp gap 来自刻意构造的 extreme-BCS batches。Abstract 不体现 practical magnitude。\n\n**N3** [critical] NER 和 ED 结果本质上是 null result，削弱 \"three tasks, four datasets\" 的 generality claim\n- BCS 对 NER F1 batch-level r≈0 (n=450)。MAVEN per-type BCS 被 centrality confound 完全解释。Pairwise SCS 在 NER 上 r=0.112 (r²=1.3%)。标题无限定词暗示跨任务通用性，但 confusability strong story 仅在 RE 成立。\n\n### Should-Fix 问题\n\n**W1** [major] MAVEN 参与度极低，不支撑 \"event detection\" 和 \"four datasets\" claim\n**W2** [major] Logit-scale TOST inconclusive 削弱 bounded-association 核心 claim\n**W3** [major] Single-seed (seed=42) 实验，effect size 与 seed variance 可比 (seed SD=2.7pp at count 16 vs typical gap 2.2pp)\n**W4** [minor-major] Abstract \"up to −49pp\" 混淆了 Dimension 1 和 Dimension 2\n**W5** [minor] 缺失相关工作：DLiSC 和 SPT\n**W6** [minor] 5 个 orphan bib entries\n\n### 主要优势\n实验设计严谨、统计方法高于平均、cross-model validation 充分、负面结果诚实、Limitations 模范级别、写作质量高（无 AI 痕迹）\n\n### 总结判断\n推荐 Findings (3.0)。Soundness 3.5 但 Excitement 2.5。强结果集中在 RE，NER/ED 基本 null results，SCS/BCS metric 无新颖性，typical effect size 2.2pp practical significance 有限。"
  }
}
```

</details>

---


### Tool result

_source line 1519 · 2026-05-18T05:33:19.470283+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22278
}
```

</details>

---


### Tool call

_source line 1520 · 2026-05-18T05:33:19.671784+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix (N1-N2) 和 Should-Fix (W1-W6) 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] Logit-scale TOST 不确定性被低估，\"bounded association\" claim 需要重新表述\n- Appendix 明确报告 logit-scale interaction 0.111 logit units (p=0.047, marginally significant)，logit-scale TOST inconclusive (p=0.209)。论文选择 linear scale 作为 primary test，但 accuracy 接近 50% 时 linear scale 压缩 interaction effects。如果 logit scale 上 interaction 是 marginally significant，Dimension 1 和 Dimension 2 的独立性就是 \"inconclusive\" 而非 \"bounded\"。\n\n**N2** [critical] DocRED R²=0.53 的 claim 稳健性不足\n- 论文多处引用 \"BCS explains 22-53%\"，其中 53% 来自 DocRED n=35 的 OLS 回归，adjusted R²=0.511，Fisher z CI=[0.27, 0.73]。CI 跨度 46 个百分点。用 n=35 的 point estimate 作为范围上界在叙事中反复出现，给读者 BCS 解释力可达一半以上的印象。\n\n### Should-Fix 问题\n\n**W1** [major] 缺乏 formal power analysis — TOST n=69 的 power 是多少？NER null result n=450 可探测最小 effect size？\n**W2** [major] Pairwise r²=1.3-1.7% 实际意义论证薄弱 — Cohen \"small but real\" 分类有争议；ρ=0.35 估计的 CI 未报告\n**W3** [major] 单 seed 实验设计对绝对值 claim 的限制 — BCS-controlled experiments, DocRED, MAVEN, cross-model 均为单 seed\n**W4** [major] Dimension 2 跨模型验证不充分 — BCS-controlled 仅在 Qwen3 和 Llama-8B 有完整验证，Llama-70B 仅 1 个数据点，Gemini 无 Dim2 数据\n**W5** [moderate] TOST ±3pp margin justification 中 Cohen's d=0.5 类比有误（medium≠negligible）\n**W6** [moderate] NER exact-match 指标可能掩盖 batch-level confusability signal\n\n### 主要优势\n实验设计精细系统化、统计严谨性高、负面结果诊断深度出色、centrality confound 处理有方法论价值、Limitations 极坦诚、多层 robustness check\n\n### Missing References\nFunder & Ozer (2019) effect size 批判、Wellek (2010) TOST 教材、Schuirmann (1987) TOST 原始论文、constrained decoding 对 calibration 影响的文献\n\n### 总结判断\nBorderline Conference (3.5)。主要 concern: (1) logit-scale TOST inconclusive 削弱 core claim 但 framing 偏向有利结论；(2) R²=22-53% 上界 CI 极宽；(3) typical effect size 2.2pp 的 practical actionability 有限。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "schema-dag-extraction",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Must-Fix (N1-N2) 和 Should-Fix (W1-W6) 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n\n### Must-Fix 问题\n\n**N1** [critical] Logit-scale TOST 不确定性被低估，\"bounded association\" claim 需要重新表述\n- Appendix 明确报告 logit-scale interaction 0.111 logit units (p=0.047, marginally significant)，logit-scale TOST inconclusive (p=0.209)。论文选择 linear scale 作为 primary test，但 accuracy 接近 50% 时 linear scale 压缩 interaction effects。如果 logit scale 上 interaction 是 marginally significant，Dimension 1 和 Dimension 2 的独立性就是 \"inconclusive\" 而非 \"bounded\"。\n\n**N2** [critical] DocRED R²=0.53 的 claim 稳健性不足\n- 论文多处引用 \"BCS explains 22-53%\"，其中 53% 来自 DocRED n=35 的 OLS 回归，adjusted R²=0.511，Fisher z CI=[0.27, 0.73]。CI 跨度 46 个百分点。用 n=35 的 point estimate 作为范围上界在叙事中反复出现，给读者 BCS 解释力可达一半以上的印象。\n\n### Should-Fix 问题\n\n**W1** [major] 缺乏 formal power analysis — TOST n=69 的 power 是多少？NER null result n=450 可探测最小 effect size？\n**W2** [major] Pairwise r²=1.3-1.7% 实际意义论证薄弱 — Cohen \"small but real\" 分类有争议；ρ=0.35 估计的 CI 未报告\n**W3** [major] 单 seed 实验设计对绝对值 claim 的限制 — BCS-controlled experiments, DocRED, MAVEN, cross-model 均为单 seed\n**W4** [major] Dimension 2 跨模型验证不充分 — BCS-controlled 仅在 Qwen3 和 Llama-8B 有完整验证，Llama-70B 仅 1 个数据点，Gemini 无 Dim2 数据\n**W5** [moderate] TOST ±3pp margin justification 中 Cohen's d=0.5 类比有误（medium≠negligible）\n**W6** [moderate] NER exact-match 指标可能掩盖 batch-level confusability signal\n\n### 主要优势\n实验设计精细系统化、统计严谨性高、负面结果诊断深度出色、centrality confound 处理有方法论价值、Limitations 极坦诚、多层 robustness check\n\n### Missing References\nFunder & Ozer (2019) effect size 批判、Wellek (2010) TOST 教材、Schuirmann (1987) TOST 原始论文、constrained decoding 对 calibration 影响的文献\n\n### 总结判断\nBorderline Conference (3.5)。主要 concern: (1) logit-scale TOST inconclusive 削弱 core claim 但 framing 偏向有利结论；(2) R²=22-53% 上界 CI 极宽；(3) typical effect size 2.2pp 的 practical actionability 有限。"
  }
}
```

</details>

---


### Tool result

_source line 1521 · 2026-05-18T05:33:21.199087+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1527
}
```

</details>

---


### Assistant

_source line 1522 · 2026-05-18T05:33:26.816304+00:00_

交叉分享已发出。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 137

## Round 137

2 recorded events


### User

_source line 1523 · 2026-05-18T05:33:29.492887+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**审稿摘要**：

- **Overall**: 3.0 / 5（Findings level）
- **Soundness**: 3.5 / 5，**Excitement**: 2.5 / 5

**三个核心问题**：
1. SCS/BCS 与 LLM-PEE 的分区标准形式相同，metric 本身无新颖性，"first controlled study" claim 需更严格 qualify
2. Typical-batch confusability effect 仅 2.2pp，Abstract 偏向报告极端条件数字（-49pp, 25-31pp），有 cherry-picking 嫌疑
3. NER 和 ED 的 batch-level 结果实质上是 null，"三任务四数据集"的 generality 主要靠 RE 支撑

**主要优势**：实验设计严谨（BCS-controlled quasi-experiments），统计方法高于 venue 平均水平（TOST, permutation tests, bootstrap），cross-model validation 充分（4 个模型），负面结果诚实报告，写作无 AI 痕迹，格式完全合规（正文恰好 8 页）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1524 · 2026-05-18T05:33:34.362372+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 138

## Round 138

2 recorded events


### User

_source line 1525 · 2026-05-18T05:35:25.633638+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 交叉回应 Reviewer 2 审稿意见

---

## Must-Fix 问题

**[AGREE with qualification] R2-N1: SCS/BCS 无独立新颖性**

同意 SCS 在形式上就是 pairwise cosine similarity，论文 §2 "SCS novelty" 段落自己承认了这一点（"SCS shares its formal definition ... with the partitioning criterion used in LLM-PEE"）。Contribution list item 2 的措辞 "We validate that pairwise embedding similarity predicts type confusion" 实际上比 Abstract 的 "operationalize confusability via SCS" 更准确。

但我要补充一个 nuance：§2 末尾的论述 "Our contribution is not the metric itself but the controlled experimental framework that isolates confusability's predictive relationship with extraction degradation" 是一个合理的 positioning。给已有 metric 命名（SCS/BCS）以便论文内部一致引用是写作上的实用选择，不算 overclaim。问题在于 Abstract 的 "operationalize" 一词暗示了 SCS 是本文引入的操作化方式，建议改为 "quantify confusability using pairwise embedding similarity (SCS)" 或类似措辞以降低新颖性暗示。

**[REBUT partially] R2-N2: Abstract framing 有 cherry-picking 嫌疑**

R2 称 Abstract 领衔 -49pp 造成误导。我认为这一批评部分成立但整体过重。

证据：Abstract 原文为 "Degradation operates along two dimensions: count-related recall decline (up to −49pp, document-level RE at full schema) dominates confusability-related type substitution (≈2.2pp in typical batches)"。这一句明确做了三件事：（1）将 -49pp 归于 Dimension 1（count），不是 confusability；（2）用 "dominates" 正确传达了两个 dimension 的相对重要性；（3）紧随其后报告了 typical-batch 2.2pp。Abstract 还补充了 "BCS explains 22-53% of cross-batch RE accuracy variance but not NER"，明确说了 NER null。

R2 的核心合理关切是：读者的注意力会被 -49pp 吸引，忽略 2.2pp 才是 confusability 的 practical magnitude。这是 framing 偏好问题，不是 factual misrepresentation。我的建议是在 Abstract 中更突出 2.2pp 的实际含义（如加入"below deployment-relevant thresholds"的表述），而非删除 -49pp（它准确反映了 Dimension 1 的严重性）。

但我同意 R2 的一个隐含批评：Introduction (§1) 的 findings summary 反复强调极端 batch gap（"extreme-batch construction amplifies this to −31.2pp"）而将 2.2pp practical magnitude 放在 §5.3 的一个 paragraph 中，叙事重心确实偏向了戏剧性数字。

**[AGREE substantially] R2-N3: NER 和 ED 本质是 null result，削弱 generality claim**

这是 R2 审稿意见中最有力的一条。

证据：
- NER batch-level BCS--F1: r≈0, n=450, §5.3 prompt sensitivity
- MAVEN per-type BCS--F1: 正相关被 centrality confound 完全解释，partial correlation p>0.2, Appendix §G
- NER pairwise SCS: r=0.112, r²=1.3%, Table 2
- 论文标题 "How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?" 无任务限定

然而我要区分两个层面：
1. **Dimension 1（count decline）**: 跨任务成立。NER recall 0.72→~0.27（§5.1），MAVEN 有 count-dependent 变化（虽然方向受 centrality confound 影响）。这不是 null result。
2. **Dimension 2（confusability）**: 仅 RE 在 batch-level 成立。NER pairwise signal 存在但极弱且不聚合到 batch level。MAVEN pairwise signal 存在但 batch/per-type aggregation 被 confound。ED 本质上只有 supplementary 角色。

论文 Contribution 3 将此称为 "task asymmetry"（"BCS explains 22-53% of RE accuracy variance ... yet shows no batch-level signal in NER"），这是诚实的。但 R2 正确指出标题和 "three tasks, four datasets" 的 framing 给读者造成了 confusability 跨任务通用的错误期待。

建议：标题加入 RE-specific 限定，或在 Abstract 中更前置地说明 confusability 的强效应限于 RE。

---

## Should-Fix 问题

**[AGREE] R2-W1: MAVEN 参与度极低**

同意。MAVEN 的有效贡献仅限于：（1）pairwise SCS--confusion r=0.129, Table 2；（2）centrality confound 的发现（§5.5, Appendix §G），这本身是一个方法论贡献但不是 IE 实验贡献。Count curve 使用了仅 5 batches/level（§3.3 脚注），且未被正文图表充分展示。MAVEN 更适合 positioned as a case study for centrality confound，而非第四个平等的评估数据集。将 "four datasets" 改为 "three primary datasets + one supplementary case study" 更准确。

**[AGREE] R2-W2: Logit-scale TOST inconclusive**

与我的 N1 一致。Logit-scale interaction marginally significant（p=0.047），TOST inconclusive（p=0.209）。论文选择 linear scale 作为 primary specification 有利于结论。这是两位 reviewer 的共识 critical issue。

**[AGREE with nuance] R2-W3: Seed SD vs typical BCS gap**

R2 指出 FewRel count=16 的 seed SD=2.7pp（Appendix Table A10）vs typical BCS gap 2.2pp，量级可比。这个比较有启发性但需要 nuance：
- Seed SD=2.7pp 反映的是 3 个 seeds 的 per-seed mean accuracy 的标准差，sample size 仅 n=3。这个估计本身非常不稳定。
- 2.2pp 的 typical BCS gap 来自 100 random batches 的回归（§5.3），是 within-seed 的 BCS-attributable 效应。
- 这两个数字的 measurement 层级不同（between-seed variance vs within-seed regression），直接比较有概念上的问题。

但 R2 的核心 point 成立：如果换一个 seed，2.2pp 的 gap 估计可能波动到比如 0pp 或 5pp，这说明 practical magnitude claim 的 precision 被单 seed 设计限制了。这与我的 W3 一致。

**[REBUT partially] R2-W4: Abstract "-49pp" 混淆 Dimension 1 和 2**

Abstract 明确标注 "-49pp, document-level RE at full schema" 为 "count-related recall decline"，并以 "dominates" 连接 "confusability-related type substitution (≈2.2pp)"。两个 dimension 在语法上是 parallel 结构中的独立成分，没有混淆。不过我同意 R2 的隐含批评：对不仔细阅读的读者，-49pp 的数字冲击力可能遮盖结构化区分。这是 minor presentation issue，不是 factual error。

**[CANNOT ASSESS] R2-W5: 缺失 DLiSC 和 SPT**

R2 未提供 DLiSC 和 SPT 的完整引用信息（全称、作者、年份、venue）。如果 R2 能提供具体文献信息，我可以评估其相关性。在此之前无法判断。

**[AGREE] R2-W6: Orphan bib entries**

经确认，references.bib 中至少 5 个条目在任何 .tex 文件中未被引用：bogdanov2024nuner、xie2024selfimproving、zhang2023llmaaa、cheng2023batch、levy-2024-same-task。这是格式问题，应在提交前清理。

---

## 对 R2 Overall Assessment 的评论

R2 给出 Soundness 3.5 / Excitement 2.5 / Overall 3.0 (Findings)。

我同意 Soundness 3.5 的判断（与我一致）。对于 Excitement，R2 给 2.5 理由是"强结果集中在 RE，NER/ED 基本 null results，SCS/BCS 无新颖性，typical effect size 2.2pp practical significance 有限"。

我对 Excitement 给 3.0 而非 2.5，原因如下：
1. **Task asymmetry 本身是一个有价值的发现**（Contribution 3）。BCS predicts RE but not NER 不仅是 null result，而是揭示了 constrained decoding vs unconstrained generation 的 error channeling 差异（§7 Discussion），这对理解 training-free IE 的 failure modes 有实质价值。
2. **Centrality confound 的发现和诊断**（§5.5）对后续使用 embedding-based metrics 做 IE 研究的人有方法论指导意义。
3. **SDGD 负面结果的诊断深度**（merge amplification + routing failure）比简单报告 "decomposition doesn't work" 有更高的信息价值。

但我理解 R2 的 perspective：如果把论文定位为 "confusability predicts IE degradation" 的正面故事，那确实 excitement 有限（因为强效应仅 RE，且 practical gap 2.2pp）。如果定位为 "understanding failure modes of training-free IE" 的分析性论文，excitement 更高。

我的 Overall 3.5 vs R2 的 3.0，差距主要在对负面结果价值的判断上。

---

## R1-R2 共识总结

两位 Reviewer 达成共识的 critical/major issues：
1. **Logit-scale TOST inconclusive**（R1-N1, R2-W2）: bounded association claim 需重新表述
2. **NER/ED generality 被 overclaim**（R1-W4 部分, R2-N3）: confusability 的强故事限于 RE
3. **Single-seed 对 practical magnitude 的限制**（R1-W3, R2-W3）
4. **DocRED R²=0.53 的 CI 极宽**（R1-N2）: R2 未直接提及但其 N2 的 practical significance 批评隐含了对这一数字稳健性的怀疑

两位 Reviewer 意见分歧：
- **SCS novelty**（R2-N1）：R2 将此列为 critical，我认为是 moderate presentation issue（论文已在 §2 self-qualify）
- **Abstract framing**（R2-N2）：R2 认为 cherry-picking，我认为 Abstract 在事实上做了正确的 Dim1/Dim2 区分，但叙事重心确实偏向戏剧性数字


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1526 · 2026-05-18T05:35:30.557353+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 139

## Round 139

2 recorded events


### User

_source line 1527 · 2026-05-18T05:35:35.105785+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

总结：
- **R2-N1 (SCS novelty)**: 部分同意，SCS 形式无新颖性，但 "operationalize" 措辞修改即可解决
- **R2-N2 (Abstract cherry-picking)**: 部分反驳，Abstract 已明确区分 Dim1/Dim2 并报告 2.2pp，但叙事重心确实偏向戏剧性数字
- **R2-N3 (NER/ED null results)**: 实质同意，这是 R2 最有力的批评，confusability 强故事仅限 RE，标题和 framing 应加限定
- **R2-W1-W6**: W1(MAVEN)同意, W2(logit TOST)同意(与我的N1一致), W3(seed SD)有nuance地同意, W4(Abstract混淆)部分反驳, W5(DLiSC/SPT)缺信息无法评估, W6(orphan bib)确认存在

两位 Reviewer 的共识 critical issues: logit-scale TOST 不确定性、NER/ED generality overclaim、single-seed 限制。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1528 · 2026-05-18T05:35:39.623776+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 140

## Round 140

6 recorded events


### User

_source line 1529 · 2026-05-18T05:35:41.131023+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 Reviewer 1 审稿意见

---

### Must-Fix 问题

**[AGREE] R1-N1: Logit-scale TOST inconclusive 削弱 "bounded association" claim**

同意这是实质性问题，我在自己的审稿中将其列为 W2 (major)。

补充证据：§5.5 正文已承认 "the logit-scale TOST is inconclusive ($p_{TOST} = 0.209$)"，Appendix E 报告 logit-scale interaction 0.111 logit units (p=0.047, marginally significant)。论文选择 linear scale 为 primary 的理由是 "direct interpretability in percentage points"，但这是一个 convenience choice，不是 methodological necessity。当 accuracy 集中在 50% 附近时（high-BCS ≈ 51%，Table in Appendix F），linear scale 会系统性地压缩 interaction effects。

不过，我认为 R1 的 severity 评估稍偏高。论文的 back-transformation argument（Appendix E："back-transforming the interaction to the probability scale at the observed floor (p = 0.51) yields 2.78pp, still within the ±3pp margin"）提供了 partial mitigation。Inconclusive 不等于 rejected——它意味着 n=69 的 power 不足以在 logit scale 上 bound the interaction，而非 interaction 实际很大。正确的修改方向是：将 claim 从 "bounded association" 降级为 "consistent with bounded association under the primary linear specification; logit-scale test is inconclusive due to limited power"。不需要撤回整个 separability finding，但措辞必须调整。

---

**[AGREE with nuance] R1-N2: DocRED R²=0.53 的 claim 稳健性不足**

同意 CI 宽度（[0.27, 0.73]）是一个问题。n=35 的 OLS 回归点估计作为 "22–53%" 范围上界在 Abstract、§1 Finding (3)、§5.2、Discussion 中反复出现，cumulative effect 给读者一种 BCS 解释力高达一半以上的印象。

但我认为这个问题的 severity 低于 R1 的判断，原因是：

1. DocRED 在论文叙事中是 replication dataset，不是 primary evidence。Primary $R^2$ 来自 FewRel (0.218)，这是基于 n=100 random batches 的更可靠估计。
2. Adjusted $R^2 = 0.511$（Appendix F），shrinkage 仅 0.014，表明 overfitting 不严重。
3. DocRED slope ($-0.71$, $\rho = -0.661$, $p < 0.001$) 本身是高度显著的；CI 宽是因为 n 小，不是因为 effect 不稳定。

建议修改：在 "22–53%" 表述后加注 CI（如 "22% [FewRel, n=100] to 53% [DocRED, n=35; 95% CI: 27–73%]"），让读者自行判断 upper bound 的可靠性。不需要移除 DocRED 数据，但需要降低其在 summary framing 中的权重。

---

### Should-Fix 问题

**[AGREE] R1-W1: 缺乏 formal power analysis**

完全同意。论文使用 TOST 但不报告 power 是方法论缺陷。具体地：
- TOST n=69 at ±3pp：应报告能探测到的最小可排除 interaction size（post-hoc power）
- NER null (n=450, r≈0)：应报告 minimum detectable $r$ at 80% power，以区分 "no effect" 和 "undetectable effect"
- 这是 §5.5 bounded-association claim 和 §5.3 NER null claim 的关键支撑缺失

这个问题与 N1 紧密相关——如果 power analysis 显示 TOST n=69 对 ±3pp margin 的 power 不足，则 linear-scale p=0.003 的说服力也会下降。

---

**[REBUT] R1-W2: Pairwise r²=1.3-1.7% 实际意义论证薄弱**

部分不同意 R1 的严重性判断。

R1 批评 Cohen "small but real" 分类有争议，这是对的。但论文的 practical significance argument 不依赖 Cohen 分类——它依赖 pair-to-batch aggregation（§5.3）：pairwise $r^2 = 1.3\%$ 通过 correlated aggregation 放大到 batch-level $R^2 = 22\%$，后者的 practical significance 体现为 quartile gap 3.9–5.3pp（§5.3 "Practical magnitude"）。论文明确说 "SCS is thus a weak pair-level predictor but a useful batch-level screen"（§7 Discussion）。

真正的问题不是 pairwise $r^2$ 小（这是 expected，论文也承认），而是 batch-level 的 typical gap (2.2pp) 是否对 practitioners 有意义。这我在自己的审稿中已 raised 为 N2。

关于 $\rho = 0.35$ 的 CI 未报告：同意这个批评。Appendix K 的 Monte Carlo simulation 使用 $\rho_{SCS} = 0.35$ 作为 inter-pair SCS correlation，但未报告该估计的 CI。如果 $\rho$ 的真值偏离 0.35，simulated batch $R^2$ 也会偏移。这应该做 sensitivity analysis。

---

**[AGREE] R1-W3: 单 seed 实验设计对绝对值 claim 的限制**

完全同意，我在自己的审稿中将其列为 W3。补充一点：Appendix L 显示 count 16 的 seed SD = 2.7pp，恰好与 typical confusability gap 2.2pp 同量级。这意味着在某些 seed 下 BCS effect 可能不显著。BCS-controlled experiments（§5.2）是论文的核心证据，但仅用 seed 42 运行。至少应增加 BCS-controlled 的 multi-seed replication。

---

**[AGREE with nuance] R1-W4: Dimension 2 跨模型验证不充分**

同意方向，但 severity 判断略有分歧。

R1 说 "Llama-70B 仅 1 个数据点"——准确。Appendix P Table 显示 70B 在 count 16 有 low-BCS 0.708 vs high-BCS 0.599（$\Delta = +10.9$pp, CI [+3.0, +20.1]）。虽然只有 1 个 count level，但 CI excludes zero，这比 "inconclusive" 要强。

Gemini 无 Dim2 数据——论文明确承认（Appendix Q: "cross-architecture Dimension 2 validation remains for future work"）。

总体上 Dim2 跨模型证据是：Qwen3-32B（完整）、Llama-8B（完整，Table 7）、Llama-70B（1 个 count level，显著）、Gemini（无）。这对于 EMNLP submission 来说不算充分——至少应在 70B 上增加 1-2 个 count level。但考虑到论文已经在 Limitations 中承认，且主 claim 是 "consistent across tested models" 而非 "universally validated"，我认为这是 major 而非 critical。

---

**[REBUT] R1-W5: TOST ±3pp margin justification 中 Cohen's d=0.5 类比有误**

不同意 R1 的核心批评。

R1 的论点是 Cohen's d=0.5 对应 "medium effect"，而 equivalence margin 应对应 "negligible effect"。但这误解了 TOST 的设计逻辑。TOST equivalence margin 不要求对应 "negligible"——它定义的是 "smallest effect of practical significance" (SESOI)。论文的 margin justification（Appendix E）基于三个 converging anchors：
1. **Empirical**: batch SD ≈ 4.6pp，3pp ≈ 0.5 × SD
2. **Practical**: "a 3pp interaction atop the 2.2pp confusability main effect would represent >130% amplification, fundamentally changing whether confusability warrants mitigation"
3. **Statistical**: Cohen's d ≈ 0.5 as a reference point

关键是 anchor #2：如果 interaction > 3pp，则 confusability effect 会随 count 翻倍以上增长，改变整个论文的 practical implication。这是一个合理的 SESOI。Cohen's d=0.5 只是辅助参照，不是 primary justification。R1 聚焦于 "medium ≠ negligible" 是对 margin 选择逻辑的误读。

不过，d=0.5 类比确实容易产生误导，建议删除这个类比或明确说 "we use Cohen's d = 0.5 as a scaling reference, not as a negligibility claim"。

---

**[AGREE] R1-W6: NER exact-match 指标可能掩盖 batch-level confusability signal**

同意，论文自己在 Limitations item 5 也承认："Relaxed matching may yield different confusability effect sizes, as boundary ambiguity may correlate with schema complexity independently of type similarity." 这是一个合理的 concern。

但我认为这不太可能改变核心结论。NER batch-level BCS–F1 correlation = 0 (n=450) 而非微弱正相关——即使 relaxed matching 能恢复一些 signal，从 r≈0 到 significant positive correlation 需要 exact-match 系统性地 suppress 大量 true positives correlated with BCS，这不太可能。更可能的效果是 effect size 从 ≈0 略增到 small positive but still non-significant。

---

### 对 R1 优势评价的回应

完全同意 R1 对优势的评价。特别是：
- "centrality confound 处理有方法论价值"——§5.6 的 residualized BCS 分析确实是论文的 methodological highlight。
- "Limitations 极坦诚"——8 条 limitation 的深度和具体性远超 venue 平均水平。

### 对 R1 Missing References 的回应

同意 Funder & Ozer (2019) 和 TOST 原始文献（Schuirmann 1987, Wellek 2010）的缺失是合理批评。特别是 Funder & Ozer 对 "small effect sizes" 的讨论框架会 strengthen 论文在 §5.3 的 practical significance argument。

### 对 R1 总评的回应

R1 给 3.5 (Borderline Conference)，我给 3.0 (Findings)。差异主要在 novelty 评估：R1 侧重 soundness concerns（logit TOST, R² CI），但没有 weight novelty deficit。我认为 SCS/BCS 与 LLM-PEE 形式相同（§2 承认）、typical effect size 2.2pp 的 practical significance 有限、强结果集中在 RE 这三个结构性问题共同将论文 ceiling 限制在 Findings level，即使 soundness concerns 全部修复也不足以升到 Conference。

**我维持 Overall Assessment 3.0 (Findings)。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1530 · 2026-05-18T05:39:07.240520+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "schema-dag-extraction",
  "issues_yaml": "# Round 15 Review Issues Tracker\n# Updated: 2026-05-18 (Round 15 fresh review)\n\n# ============================================================\n# CRITICAL — Must-Fix\n# ============================================================\n\n- id: R3-C2\n  summary: \"'Empirically separable channels' 缺乏 formal 统计支撑 — TOST margin ±3pp > typical effect 2.2pp\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 9\n  mentions:\n    - {round: 3, reviewers: [R1, R2], note: \"因果语言过强\"}\n    - {round: 5, reviewers: [R1, R2, R3], note: \"三人共识改措辞\"}\n    - {round: 9, reviewers: [R1, R2, R3], note: \"三人共识: TOST ±3pp margin 用 prompt variation 锚定不合逻辑\"}\n  action_items:\n    - {round: 9, action: \"D051: 'additive separability' → 'bounded interaction' 全文统一\", assigned_to: agent, status: done}\n  resolution: \"D051 W1: 全文 'bounded interaction' 统一; SESOI effect-size anchored; sensitivity table in Appendix\"\n  resolution_round: 9\n\n- id: R10-N1\n  summary: \"因果语言 ('driven', 'channels', 'shape') 超出 observational/quasi-experimental 证据边界\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 12\n  resolution: \"Title 改为 'Predict'; 正文因果语言已清理; Appendix 残余为 R12-W2 追踪\"\n  resolution_round: 12\n\n- id: R10-N2\n  summary: \"Pair-level→batch-level 聚合推理链叙事误导 — unconditional sim R²=0.044 vs 观测 0.218\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 12\n  resolution: \"叙事链清晰分层; simulation 明确为 illustrative; R²=0.218 为独立实证\"\n  resolution_round: 12\n\n- id: R10-N3\n  summary: \"TOST ±3pp margin 的 external anchoring 不足\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 12\n  resolution: \"三重 anchoring + sensitivity table 已到位\"\n  resolution_round: 12\n\n- id: R10-N4\n  summary: \"SCS/BCS Contribution #2 framing 暗示 metric novelty\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: \"Contribution #2 已 reframe 为 controlled validation\"\n  resolution_round: 11\n\n- id: R11-N1\n  summary: \"NER Dimension 2 batch-level 证据方向相反, 但论文泛化为 cross-task\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Abstract/Intro/Contribution/Discussion 均已精确限定 batch-level Dim2 = RE-specific\"\n  resolution_round: 12\n\n# ============================================================\n# WARNING — Should-Fix (Open / In-Progress)\n# ============================================================\n\n- id: R15-N1\n  summary: \"Logit-scale TOST inconclusive (p=0.209) 与 linear-scale 'bounded association' claim 矛盾 — scale 选择构成分析自由度\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - {round: 12, reviewers: [R1, R2], note: \"R12-W3 首次提出 logit-scale 不一致\"}\n    - {round: 14, reviewers: [R1, R2], note: \"R14 共识: 需 formal power analysis 或弱化 claim\"}\n    - {round: 15, reviewers: [R1, R2], note: \"R1 列为 critical N1; R2 列为 major W2; 交叉共识: bounded association claim 需限定为 'under primary linear specification; logit inconclusive'; scale 选择是分析自由度非 methodological necessity\"}\n  action_items:\n    - {round: 15, action: \"§4.4 正文提升 logit-scale 结果报告 (非仅 Appendix); claim 降级为 'consistent with bounded association under linear specification; inconclusive on logit scale'\", assigned_to: agent, status: open}\n    - {round: 15, action: \"报告 TOST n=69 at ±3pp 的 post-hoc power (R1-W1 + R2 cross AGREE)\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-N2\n  summary: \"DocRED R²=0.53 (n=35) CI 极宽 [0.27, 0.73] — '22-53%' 上界在叙事中权重过高\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - {round: 14, reviewers: [R1, R2], note: \"R14-W1 首次提出 DocRED R² 稳定性\"}\n    - {round: 15, reviewers: [R1, R2], note: \"R1 critical N2; R2 cross AGREE with nuance (replication dataset, lower severity); 共识: 需在正文报告 CI, 降低 53% 在 summary framing 中的权重\"}\n  action_items:\n    - {round: 15, action: \"Abstract/Introduction 中 '22-53%' 改为带 CI 的表述: '22% [FewRel, n=100] to 53% [DocRED, n=35; CI: 27-73%]'\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-N3\n  summary: \"NER/ED batch-level 结果实质为 null — 'three tasks, four datasets' generality claim 虚高; confusability 强故事仅限 RE\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - {round: 11, reviewers: [R1, R2], note: \"R11-N1 首次提出 NER batch-level null\"}\n    - {round: 14, reviewers: [R1, R2], note: \"R14-m1 MAVEN 应降级为 supplementary\"}\n    - {round: 15, reviewers: [R1, R2], note: \"R2 critical N3; R1 cross 'substantially agree'; 共识: Dim1 跨任务成立, Dim2 仅 RE batch-level; 标题/Abstract 需加 RE-specificity 限定或平衡呈现 null results\"}\n  action_items:\n    - {round: 15, action: \"标题或 Abstract 加入 confusability 效应的 RE-specificity 限定; 'four datasets' → 'three primary + supplementary MAVEN'\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W1\n  summary: \"SCS/BCS metric 与 LLM-PEE 形式相同, Abstract 'operationalize' 措辞暗示独立新颖性\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - {round: 13, reviewers: [R1, R2], note: \"R13-W3 首次提出 '§3.2 We introduce' 措辞\"}\n    - {round: 14, reviewers: [R1, R2], note: \"R14 共识: Contribution 应从 metric-centric 转向 framework-centric\"}\n    - {round: 15, reviewers: [R1, R2], note: \"R2 critical N1; R1 cross 'AGREE with qualification' (presentation issue not structural); 分歧: R2 认为是 novelty ceiling, R1 认为措辞修改可解决\"}\n  action_items:\n    - {round: 15, action: \"Abstract 'operationalize confusability via SCS' → 'quantify confusability using pairwise embedding similarity (SCS)' 或类似措辞; Contribution 2 明确说 'SCS uses the same metric as LLM-PEE; our contribution is the controlled framework'\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-N2\n  summary: \"核心效应量过小 (typical gap 2.2pp, pairwise r²=1.3%) — practical significance 存疑\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - {round: 11, reviewers: [R1, R2], note: \"2.2pp CI [0.4, 4.0] 在部署中几乎不可察觉\"}\n    - {round: 14, reviewers: [R1, R2], note: \"extreme-batch 数字在叙事中占比过高, typical gap 2.2pp 应前置\"}\n    - {round: 15, reviewers: [R1, R2], note: \"R2 N2 + R1 cross partial rebut: Abstract 已区分 Dim1/Dim2 但叙事重心偏向戏剧性数字; 共识: Abstract 应更突出 typical magnitude\"}\n  action_items:\n    - {round: 15, action: \"Abstract 中 typical-batch 2.2pp 的呈现需更突出; Introduction findings 叙事平衡 extreme vs typical\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W2\n  summary: \"Single-seed (seed=42) 实验, typical effect 2.2pp 与 seed variance 2.7pp 可比 — practical magnitude 精度不足\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1, R2], note: \"R1 W3 major + R2 W3 major + 交叉共识; seed SD=2.7pp at count 16 vs typical BCS gap 2.2pp; BCS-controlled experiments 仅 seed 42\"}\n  action_items:\n    - {round: 15, action: \"至少对核心 BCS-controlled RE 实验增加 multi-seed replication; 或在 Limitations 中明确说明 single-seed 对 practical magnitude 估计的影响\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W3\n  summary: \"Dimension 2 跨模型验证不充分 — BCS-controlled 仅 Qwen3+Llama-8B 完整, 70B 仅 1 count level, Gemini 无 Dim2 数据\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - {round: 14, reviewers: [R1, R2], note: \"R14-W2 首次提出跨模型证据不足\"}\n    - {round: 15, reviewers: [R1, R2], note: \"R1 W4 major + R2 cross AGREE with nuance (70B CI excludes zero, major not critical); Abstract/Conclusion 'across architectures' 措辞暗示全面验证但实际 Dim2 仅 2 个 open-weight 模型\"}\n  action_items:\n    - {round: 15, action: \"Abstract/Conclusion 区分 Dim1 和 Dim2 的跨模型验证范围; 'consistent across tested model families' 需明确哪些 claim 适用于哪些模型\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W2\n  summary: \"残余因果/过强语言 ('schema-induced', 'count-driven', 'BCS-driven')\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - {round: 12, reviewers: [R2], note: \"Appendix 'count-driven decline'\"}\n    - {round: 14, reviewers: [R1, R2], note: \"'schema-induced degradation' 全文多处出现\"}\n    - {round: 15, reviewers: [], note: \"本轮未作为独立 issue 提出, 但 R15-N1 logit TOST 共识隐含要求弱化 association claim 语言\"}\n  action_items:\n    - {round: 14, action: \"全文 grep 'schema-induced' 替换为 'schema-associated'\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W1\n  summary: \"Discussion/Conclusion 过于简短\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - {round: 14, reviewers: [], note: \"Conclusion 已有 future work 句但仍偏短\"}\n    - {round: 15, reviewers: [], note: \"本轮未直接提及\"}\n  action_items:\n    - {round: 13, action: \"Conclusion 扩展\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-N1\n  summary: \"Introduction Finding (1) 过于密集 — 56 词复合句含多层嵌套\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - {round: 15, reviewers: [], note: \"本轮未直接提及\"}\n  action_items:\n    - {round: 12, action: \"拆 Finding (1) 为 2-3 句\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W1\n  summary: \"Contribution 3 将 NER null result 包装为正面贡献\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - {round: 14, reviewers: [R1, R2], note: \"R2-W5 应并入 C2; R1 REBUT: 独立分析价值; 分歧\"}\n    - {round: 15, reviewers: [R1, R2], note: \"R2-N3 reinforces: NER null = task asymmetry, 但仍被包装为正面贡献\"}\n  action_items:\n    - {round: 13, action: \"Contribution 3 改写: 强调诊断性发现\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W3\n  summary: \"TOST logit-scale inconclusive — linear vs logit scale 选择缺 a priori justification\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1, R2], note: \"升级追踪于 R15-N1\"}\n  action_items:\n    - {round: 15, action: \"见 R15-N1 action items\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W5\n  summary: \"FewRel constrained decoding 格式特殊性, 泛化性不确定\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - {round: 14, reviewers: [R1, R2], note: \"共识: 正文应讨论 constrained decoding 对 RE confusability effect 的影响\"}\n    - {round: 15, reviewers: [], note: \"本轮未直接提及, 但 R1-W6 NER exact-match 相关\"}\n  action_items:\n    - {round: 14, action: \"Discussion 补充 constrained decoding caveat\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W3\n  summary: \"SDGD (§5) 分析深度不足 — 缺 k-value quantitative analysis 和 failure case analysis\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - {round: 15, reviewers: [], note: \"本轮未直接提及\"}\n  action_items:\n    - {round: 14, action: \"§5 或 Appendix 补充 merge amplification 与 k 的定量关系\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# INFO — Minor\n# ============================================================\n\n- id: R15-m1\n  summary: \"Aggregation simulation (Appendix J) 声称 'not evidence base' 但正文 §5.3/§7 引用其 ~3x amplification 作为论证 — 定位矛盾\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1], note: \"R1-M5: 如果不是证据就不应在论证链中使用\"}\n  action_items:\n    - {round: 15, action: \"统一 simulation 定位: 要么删除 'not evidence base' caveat, 要么正文不引用 simulation 结果作论证\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-m2\n  summary: \"ρ=0.35 inter-pair SCS correlation 估计未报告 CI — aggregation simulation sensitivity 不足\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1, R2], note: \"R1-W2 + R2 cross AGREE on ρ CI; R2 rebuts Cohen r² framing but agrees ρ sensitivity needed\"}\n  action_items:\n    - {round: 15, action: \"Appendix J 报告 ρ=0.35 的 CI 并做 ρ sensitivity analysis\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-m3\n  summary: \"Table 2 缺 FewRel pairwise r=0.187 — 三数据集数据不完整呈现\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1], note: \"R1-M1: FewRel r=0.187 在 §3.4 但未入 Table 2\"}\n  action_items:\n    - {round: 15, action: \"Table 2 补充 FewRel 行 或 caption 中显式报告数字\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-m4\n  summary: \"NER U-shaped recovery 解释 ('type-filtering overhead elimination') 缺实验证据 — 标注为 speculative\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1, R2], note: \"R1-M3 + R2 小问题: §5.1 解释缺 evidence\"}\n  action_items:\n    - {round: 15, action: \"§5.1 U-shape 解释加 'we hypothesize' 或类似限定\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-m5\n  summary: \"Orphan bib entries (bogdanov2024nuner, xie2024selfimproving, zhang2023llmaaa, cheng2023batch, levy-2024-same-task)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1, R2], note: \"R2-W6 + R1 cross AGREE: 5 个未引用条目\"}\n  action_items:\n    - {round: 15, action: \"清理 references.bib 中未引用的条目\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-m6\n  summary: \"Gemini count 64 仅 13/25 batches — partial data 的统计 claim 可信度打折\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1], note: \"R1-M4\"}\n  action_items:\n    - {round: 15, action: \"Appendix Table A8 更显著标注 partial data; 或补齐剩余 12 batches\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R10-m3\n  summary: \"Missing references — 持续追踪\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - {round: 14, reviewers: [R1, R2], note: \"structured prediction calibration, label embedding trees\"}\n    - {round: 15, reviewers: [R1, R2], note: \"R1: Funder & Ozer (2019) effect size critique, Wellek (2010) TOST, Schuirmann (1987) TOST original; R2: DLiSC (2505.14992), SPT (2506.01276); constrained decoding + calibration 文献\"}\n  action_items:\n    - {round: 15, action: \"补充: Funder & Ozer 2019, Schuirmann 1987, constrained decoding calibration lit, DLiSC, SPT\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R10-m5\n  summary: \"1000 instances 对 long-tail types 充分性\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-m1\n  summary: \"FP8 + vLLM greedy decoding 残余非确定性\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1], note: \"R1-W3 提及但非核心; seed variance 问题追踪于 R15-W2\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-m2\n  summary: \"-ing 分词短语和 'Notably' 使用 — AI 写作痕迹残余\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R2], note: \"R2 评价: '非常干净, 无 em-dash, 无 AI 典型词汇, 写作质量优于多数 submission'\"}\n  action_items:\n    - {round: 13, action: \"全文 grep 'ing,' 模式\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-m1\n  summary: \"MAVEN validation set 是否用于 hyperparameter 选择未声明\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-m2\n  summary: \"多重比较处理: prompt variant 8 tests 用 directional consistency 代替正式检验\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-m3\n  summary: \"FewRel contamination 风险: 未达共识\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-m2\n  summary: \"Abstract 'up to -49pp' 来自 DocRED (非主实验) — cherry-picking 嫌疑\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1, R2], note: \"R2-N2 升级为 critical framing issue; R1 partial rebut: Abstract 已正确区分 Dim1/Dim2; 分歧记录\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-m3\n  summary: \"DocRED count curve 仅引用未在 Appendix 呈现\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W1\n  summary: \"Gemini 2.5 Flash 引用错误: bib 可能指向旧版本\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1], note: \"R1-M7: arXiv 2507.06261 时间线核实\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W3\n  summary: \"SCS §3.2 措辞暗示指标新颖性\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1, R2], note: \"升级追踪于 R15-W1\"}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# RESOLVED (历史)\n# ============================================================\n\n- id: R9-W1\n  summary: \"Single-seed evaluation — count curve 每 level 仅 5 batches\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"3-seed × 25-batch count curves with ±1SD error bars\"\n  resolution_round: 10\n\n- id: R10-W1\n  summary: \"\\\\enlargethispage 操纵页面布局\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"已删除\"\n  resolution_round: 11\n\n- id: R10-W2\n  summary: \"Negative results (§5) 缺 constructive next steps\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"§5 Future directions added\"\n  resolution_round: 11\n\n- id: R10-W3\n  summary: \"Abstract 数字密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"精简至 3 个核心数字\"\n  resolution_round: 12\n\n- id: R10-W4\n  summary: \"Introduction Contribution list 含未铺垫概念\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"改为方法论声明格式\"\n  resolution_round: 12\n\n- id: R10-W5\n  summary: \"BCS 'generalizes across tasks' 过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  resolution: \"Contribution 3 限定为 RE-specific\"\n  resolution_round: 12\n\n- id: R10-W6\n  summary: \"Em-dash 使用偏高\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"已清理\"\n  resolution_round: 11\n\n- id: R10-W7\n  summary: \"Supplementary placeholder sections\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"所有补充材料在 main.tex Appendix\"\n  resolution_round: 12\n\n- id: R11-W3\n  summary: \"Prompt variant analysis underpowered\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Rothman 1990 + directional consistency\"\n  resolution_round: 12\n\n- id: R10-m4\n  summary: \"Multiple comparisons: Rothman 1990\"\n  category: method\n  severity: info\n  status: resolved\n  resolution: \"R12 交叉共识\"\n  resolution_round: 12\n\n- id: R2-N3-80rel\n  summary: \"extreme-batch 31.2pp 为 headline, typical 2.2pp 被弱化\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"Intro typical-first; Discussion IQR caveat\"\n  resolution_round: 9\n\n- id: R4-N1\n  summary: \"RE batch composition +1.4pp (p≈0.19) Contribution #4 framing\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"Contribution #4 → 'structural barriers'\"\n  resolution_round: 9\n\n- id: R6-N1\n  summary: \"Two-channel decomposition 概念贡献有限\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"4 contributions rewritten\"\n  resolution_round: 9\n\n- id: MW2\n  summary: \"Pairwise r²=1.3% 到 batch R²=22% 聚合 conditioning bias\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"simulation → illustrative; R²=0.218 primary\"\n  resolution_round: 9\n\n- id: R5-W1\n  summary: \"FewRel train+val 合并 contamination 风险\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Split-origin covariate confirms BCS partial effect unchanged\"\n  resolution_round: 9\n\n- id: R5-N1\n  summary: \"SCS novelty — metric 与 LLM-PEE 形式相同\"\n  category: framing\n  severity: warning\n  status: resolved\n  resolution: \"Contribution #2 reframed as empirical validation\"\n  resolution_round: 9\n\n- id: R6-W1\n  summary: \"'首次 controlled study' 声称需限定\"\n  category: framing\n  severity: warning\n  status: resolved\n  resolution: \"'To our knowledge' added\"\n  resolution_round: 9\n\n- id: R6-N2\n  summary: \"正文可能超过 8 页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"编译确认 Conclusion 在 p8\"\n  resolution_round: 9\n\n- id: R10-PS\n  summary: \"Prompt sensitivity 实验结果需整合入论文\"\n  category: experiment\n  severity: warning\n  status: resolved\n  resolution: \"Integrated into §4.3 + Appendix H\"\n  resolution_round: 11\n\n- id: R12-W5\n  summary: \"Orphan bib entries\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"已删除\"\n  resolution_round: 13\n\n- id: R10-m1\n  summary: \"Cross-seed variance vs typical effect\"\n  category: method\n  severity: info\n  status: resolved\n  resolution: \"§3.4 说明 FP8 non-determinism\"\n  resolution_round: 14\n\n- id: R10-m2\n  summary: \"NER U-shape mechanistic 解释未验证\"\n  category: framing\n  severity: info\n  status: resolved\n  resolution: \"'likely reflects' 表述\"\n  resolution_round: 14\n\n- id: R11-W2\n  summary: \"TOST 术语首次出现未展开\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"Introduction 已展开 'Two One-Sided Tests [TOST]'\"\n  resolution_round: 14\n\n- id: R12-W4\n  summary: \"Introduction findings vs contributions 不对齐\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - {round: 15, reviewers: [], note: \"本轮未直接提及\"}\n  action_items:\n    - {round: 13, action: \"统一 findings 和 contributions 数量/映射\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W2\n  summary: \"BCS > 0.59 阈值缺乏 formal derivation\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  action_items:\n    - {round: 13, action: \"删除 0.59 阈值\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W4\n  summary: \"Abstract 偏短且缺 motivation\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R2], note: \"R2 未再次明确提出 length 问题; 但 N2 关注 framing balance\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-m1\n  summary: \"Abstract 偏短 (~130-140 words)\"\n  category: writing\n  severity: info\n  status: resolved\n  resolution: \"升级追踪于 R13-W4; R14 评价 ~170 words 在范围内\"\n  resolution_round: 14\n\n- id: R14-W1\n  summary: \"'BCS explains 22-53%' 中 53% 稳定性未验证\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1, R2], note: \"升级追踪于 R15-N2\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W2\n  summary: \"'fundamental property of in-context learning' claim 跨模型证据不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1, R2], note: \"升级追踪于 R15-W3\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-m1\n  summary: \"MAVEN 应降级为 supplementary dataset\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1, R2], note: \"升级追踪于 R15-N3\"}\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "schema-dag-extraction",
    "issues_yaml": "# Round 15 Review Issues Tracker\n# Updated: 2026-05-18 (Round 15 fresh review)\n\n# ============================================================\n# CRITICAL — Must-Fix\n# ============================================================\n\n- id: R3-C2\n  summary: \"'Empirically separable channels' 缺乏 formal 统计支撑 — TOST margin ±3pp > typical effect 2.2pp\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 9\n  mentions:\n    - {round: 3, reviewers: [R1, R2], note: \"因果语言过强\"}\n    - {round: 5, reviewers: [R1, R2, R3], note: \"三人共识改措辞\"}\n    - {round: 9, reviewers: [R1, R2, R3], note: \"三人共识: TOST ±3pp margin 用 prompt variation 锚定不合逻辑\"}\n  action_items:\n    - {round: 9, action: \"D051: 'additive separability' → 'bounded interaction' 全文统一\", assigned_to: agent, status: done}\n  resolution: \"D051 W1: 全文 'bounded interaction' 统一; SESOI effect-size anchored; sensitivity table in Appendix\"\n  resolution_round: 9\n\n- id: R10-N1\n  summary: \"因果语言 ('driven', 'channels', 'shape') 超出 observational/quasi-experimental 证据边界\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 12\n  resolution: \"Title 改为 'Predict'; 正文因果语言已清理; Appendix 残余为 R12-W2 追踪\"\n  resolution_round: 12\n\n- id: R10-N2\n  summary: \"Pair-level→batch-level 聚合推理链叙事误导 — unconditional sim R²=0.044 vs 观测 0.218\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 12\n  resolution: \"叙事链清晰分层; simulation 明确为 illustrative; R²=0.218 为独立实证\"\n  resolution_round: 12\n\n- id: R10-N3\n  summary: \"TOST ±3pp margin 的 external anchoring 不足\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 12\n  resolution: \"三重 anchoring + sensitivity table 已到位\"\n  resolution_round: 12\n\n- id: R10-N4\n  summary: \"SCS/BCS Contribution #2 framing 暗示 metric novelty\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: \"Contribution #2 已 reframe 为 controlled validation\"\n  resolution_round: 11\n\n- id: R11-N1\n  summary: \"NER Dimension 2 batch-level 证据方向相反, 但论文泛化为 cross-task\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"Abstract/Intro/Contribution/Discussion 均已精确限定 batch-level Dim2 = RE-specific\"\n  resolution_round: 12\n\n# ============================================================\n# WARNING — Should-Fix (Open / In-Progress)\n# ============================================================\n\n- id: R15-N1\n  summary: \"Logit-scale TOST inconclusive (p=0.209) 与 linear-scale 'bounded association' claim 矛盾 — scale 选择构成分析自由度\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - {round: 12, reviewers: [R1, R2], note: \"R12-W3 首次提出 logit-scale 不一致\"}\n    - {round: 14, reviewers: [R1, R2], note: \"R14 共识: 需 formal power analysis 或弱化 claim\"}\n    - {round: 15, reviewers: [R1, R2], note: \"R1 列为 critical N1; R2 列为 major W2; 交叉共识: bounded association claim 需限定为 'under primary linear specification; logit inconclusive'; scale 选择是分析自由度非 methodological necessity\"}\n  action_items:\n    - {round: 15, action: \"§4.4 正文提升 logit-scale 结果报告 (非仅 Appendix); claim 降级为 'consistent with bounded association under linear specification; inconclusive on logit scale'\", assigned_to: agent, status: open}\n    - {round: 15, action: \"报告 TOST n=69 at ±3pp 的 post-hoc power (R1-W1 + R2 cross AGREE)\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-N2\n  summary: \"DocRED R²=0.53 (n=35) CI 极宽 [0.27, 0.73] — '22-53%' 上界在叙事中权重过高\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - {round: 14, reviewers: [R1, R2], note: \"R14-W1 首次提出 DocRED R² 稳定性\"}\n    - {round: 15, reviewers: [R1, R2], note: \"R1 critical N2; R2 cross AGREE with nuance (replication dataset, lower severity); 共识: 需在正文报告 CI, 降低 53% 在 summary framing 中的权重\"}\n  action_items:\n    - {round: 15, action: \"Abstract/Introduction 中 '22-53%' 改为带 CI 的表述: '22% [FewRel, n=100] to 53% [DocRED, n=35; CI: 27-73%]'\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-N3\n  summary: \"NER/ED batch-level 结果实质为 null — 'three tasks, four datasets' generality claim 虚高; confusability 强故事仅限 RE\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - {round: 11, reviewers: [R1, R2], note: \"R11-N1 首次提出 NER batch-level null\"}\n    - {round: 14, reviewers: [R1, R2], note: \"R14-m1 MAVEN 应降级为 supplementary\"}\n    - {round: 15, reviewers: [R1, R2], note: \"R2 critical N3; R1 cross 'substantially agree'; 共识: Dim1 跨任务成立, Dim2 仅 RE batch-level; 标题/Abstract 需加 RE-specificity 限定或平衡呈现 null results\"}\n  action_items:\n    - {round: 15, action: \"标题或 Abstract 加入 confusability 效应的 RE-specificity 限定; 'four datasets' → 'three primary + supplementary MAVEN'\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W1\n  summary: \"SCS/BCS metric 与 LLM-PEE 形式相同, Abstract 'operationalize' 措辞暗示独立新颖性\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - {round: 13, reviewers: [R1, R2], note: \"R13-W3 首次提出 '§3.2 We introduce' 措辞\"}\n    - {round: 14, reviewers: [R1, R2], note: \"R14 共识: Contribution 应从 metric-centric 转向 framework-centric\"}\n    - {round: 15, reviewers: [R1, R2], note: \"R2 critical N1; R1 cross 'AGREE with qualification' (presentation issue not structural); 分歧: R2 认为是 novelty ceiling, R1 认为措辞修改可解决\"}\n  action_items:\n    - {round: 15, action: \"Abstract 'operationalize confusability via SCS' → 'quantify confusability using pairwise embedding similarity (SCS)' 或类似措辞; Contribution 2 明确说 'SCS uses the same metric as LLM-PEE; our contribution is the controlled framework'\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-N2\n  summary: \"核心效应量过小 (typical gap 2.2pp, pairwise r²=1.3%) — practical significance 存疑\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - {round: 11, reviewers: [R1, R2], note: \"2.2pp CI [0.4, 4.0] 在部署中几乎不可察觉\"}\n    - {round: 14, reviewers: [R1, R2], note: \"extreme-batch 数字在叙事中占比过高, typical gap 2.2pp 应前置\"}\n    - {round: 15, reviewers: [R1, R2], note: \"R2 N2 + R1 cross partial rebut: Abstract 已区分 Dim1/Dim2 但叙事重心偏向戏剧性数字; 共识: Abstract 应更突出 typical magnitude\"}\n  action_items:\n    - {round: 15, action: \"Abstract 中 typical-batch 2.2pp 的呈现需更突出; Introduction findings 叙事平衡 extreme vs typical\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W2\n  summary: \"Single-seed (seed=42) 实验, typical effect 2.2pp 与 seed variance 2.7pp 可比 — practical magnitude 精度不足\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1, R2], note: \"R1 W3 major + R2 W3 major + 交叉共识; seed SD=2.7pp at count 16 vs typical BCS gap 2.2pp; BCS-controlled experiments 仅 seed 42\"}\n  action_items:\n    - {round: 15, action: \"至少对核心 BCS-controlled RE 实验增加 multi-seed replication; 或在 Limitations 中明确说明 single-seed 对 practical magnitude 估计的影响\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W3\n  summary: \"Dimension 2 跨模型验证不充分 — BCS-controlled 仅 Qwen3+Llama-8B 完整, 70B 仅 1 count level, Gemini 无 Dim2 数据\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - {round: 14, reviewers: [R1, R2], note: \"R14-W2 首次提出跨模型证据不足\"}\n    - {round: 15, reviewers: [R1, R2], note: \"R1 W4 major + R2 cross AGREE with nuance (70B CI excludes zero, major not critical); Abstract/Conclusion 'across architectures' 措辞暗示全面验证但实际 Dim2 仅 2 个 open-weight 模型\"}\n  action_items:\n    - {round: 15, action: \"Abstract/Conclusion 区分 Dim1 和 Dim2 的跨模型验证范围; 'consistent across tested model families' 需明确哪些 claim 适用于哪些模型\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W2\n  summary: \"残余因果/过强语言 ('schema-induced', 'count-driven', 'BCS-driven')\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - {round: 12, reviewers: [R2], note: \"Appendix 'count-driven decline'\"}\n    - {round: 14, reviewers: [R1, R2], note: \"'schema-induced degradation' 全文多处出现\"}\n    - {round: 15, reviewers: [], note: \"本轮未作为独立 issue 提出, 但 R15-N1 logit TOST 共识隐含要求弱化 association claim 语言\"}\n  action_items:\n    - {round: 14, action: \"全文 grep 'schema-induced' 替换为 'schema-associated'\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W1\n  summary: \"Discussion/Conclusion 过于简短\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - {round: 14, reviewers: [], note: \"Conclusion 已有 future work 句但仍偏短\"}\n    - {round: 15, reviewers: [], note: \"本轮未直接提及\"}\n  action_items:\n    - {round: 13, action: \"Conclusion 扩展\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-N1\n  summary: \"Introduction Finding (1) 过于密集 — 56 词复合句含多层嵌套\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - {round: 15, reviewers: [], note: \"本轮未直接提及\"}\n  action_items:\n    - {round: 12, action: \"拆 Finding (1) 为 2-3 句\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W1\n  summary: \"Contribution 3 将 NER null result 包装为正面贡献\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - {round: 14, reviewers: [R1, R2], note: \"R2-W5 应并入 C2; R1 REBUT: 独立分析价值; 分歧\"}\n    - {round: 15, reviewers: [R1, R2], note: \"R2-N3 reinforces: NER null = task asymmetry, 但仍被包装为正面贡献\"}\n  action_items:\n    - {round: 13, action: \"Contribution 3 改写: 强调诊断性发现\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W3\n  summary: \"TOST logit-scale inconclusive — linear vs logit scale 选择缺 a priori justification\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1, R2], note: \"升级追踪于 R15-N1\"}\n  action_items:\n    - {round: 15, action: \"见 R15-N1 action items\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W5\n  summary: \"FewRel constrained decoding 格式特殊性, 泛化性不确定\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - {round: 14, reviewers: [R1, R2], note: \"共识: 正文应讨论 constrained decoding 对 RE confusability effect 的影响\"}\n    - {round: 15, reviewers: [], note: \"本轮未直接提及, 但 R1-W6 NER exact-match 相关\"}\n  action_items:\n    - {round: 14, action: \"Discussion 补充 constrained decoding caveat\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W3\n  summary: \"SDGD (§5) 分析深度不足 — 缺 k-value quantitative analysis 和 failure case analysis\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - {round: 15, reviewers: [], note: \"本轮未直接提及\"}\n  action_items:\n    - {round: 14, action: \"§5 或 Appendix 补充 merge amplification 与 k 的定量关系\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# INFO — Minor\n# ============================================================\n\n- id: R15-m1\n  summary: \"Aggregation simulation (Appendix J) 声称 'not evidence base' 但正文 §5.3/§7 引用其 ~3x amplification 作为论证 — 定位矛盾\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1], note: \"R1-M5: 如果不是证据就不应在论证链中使用\"}\n  action_items:\n    - {round: 15, action: \"统一 simulation 定位: 要么删除 'not evidence base' caveat, 要么正文不引用 simulation 结果作论证\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-m2\n  summary: \"ρ=0.35 inter-pair SCS correlation 估计未报告 CI — aggregation simulation sensitivity 不足\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1, R2], note: \"R1-W2 + R2 cross AGREE on ρ CI; R2 rebuts Cohen r² framing but agrees ρ sensitivity needed\"}\n  action_items:\n    - {round: 15, action: \"Appendix J 报告 ρ=0.35 的 CI 并做 ρ sensitivity analysis\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-m3\n  summary: \"Table 2 缺 FewRel pairwise r=0.187 — 三数据集数据不完整呈现\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1], note: \"R1-M1: FewRel r=0.187 在 §3.4 但未入 Table 2\"}\n  action_items:\n    - {round: 15, action: \"Table 2 补充 FewRel 行 或 caption 中显式报告数字\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-m4\n  summary: \"NER U-shaped recovery 解释 ('type-filtering overhead elimination') 缺实验证据 — 标注为 speculative\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1, R2], note: \"R1-M3 + R2 小问题: §5.1 解释缺 evidence\"}\n  action_items:\n    - {round: 15, action: \"§5.1 U-shape 解释加 'we hypothesize' 或类似限定\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-m5\n  summary: \"Orphan bib entries (bogdanov2024nuner, xie2024selfimproving, zhang2023llmaaa, cheng2023batch, levy-2024-same-task)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1, R2], note: \"R2-W6 + R1 cross AGREE: 5 个未引用条目\"}\n  action_items:\n    - {round: 15, action: \"清理 references.bib 中未引用的条目\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-m6\n  summary: \"Gemini count 64 仅 13/25 batches — partial data 的统计 claim 可信度打折\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1], note: \"R1-M4\"}\n  action_items:\n    - {round: 15, action: \"Appendix Table A8 更显著标注 partial data; 或补齐剩余 12 batches\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R10-m3\n  summary: \"Missing references — 持续追踪\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - {round: 14, reviewers: [R1, R2], note: \"structured prediction calibration, label embedding trees\"}\n    - {round: 15, reviewers: [R1, R2], note: \"R1: Funder & Ozer (2019) effect size critique, Wellek (2010) TOST, Schuirmann (1987) TOST original; R2: DLiSC (2505.14992), SPT (2506.01276); constrained decoding + calibration 文献\"}\n  action_items:\n    - {round: 15, action: \"补充: Funder & Ozer 2019, Schuirmann 1987, constrained decoding calibration lit, DLiSC, SPT\", assigned_to: agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R10-m5\n  summary: \"1000 instances 对 long-tail types 充分性\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 12\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-m1\n  summary: \"FP8 + vLLM greedy decoding 残余非确定性\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1], note: \"R1-W3 提及但非核心; seed variance 问题追踪于 R15-W2\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-m2\n  summary: \"-ing 分词短语和 'Notably' 使用 — AI 写作痕迹残余\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R2], note: \"R2 评价: '非常干净, 无 em-dash, 无 AI 典型词汇, 写作质量优于多数 submission'\"}\n  action_items:\n    - {round: 13, action: \"全文 grep 'ing,' 模式\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-m1\n  summary: \"MAVEN validation set 是否用于 hyperparameter 选择未声明\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-m2\n  summary: \"多重比较处理: prompt variant 8 tests 用 directional consistency 代替正式检验\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-m3\n  summary: \"FewRel contamination 风险: 未达共识\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-m2\n  summary: \"Abstract 'up to -49pp' 来自 DocRED (非主实验) — cherry-picking 嫌疑\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1, R2], note: \"R2-N2 升级为 critical framing issue; R1 partial rebut: Abstract 已正确区分 Dim1/Dim2; 分歧记录\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-m3\n  summary: \"DocRED count curve 仅引用未在 Appendix 呈现\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W1\n  summary: \"Gemini 2.5 Flash 引用错误: bib 可能指向旧版本\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1], note: \"R1-M7: arXiv 2507.06261 时间线核实\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W3\n  summary: \"SCS §3.2 措辞暗示指标新颖性\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1, R2], note: \"升级追踪于 R15-W1\"}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# RESOLVED (历史)\n# ============================================================\n\n- id: R9-W1\n  summary: \"Single-seed evaluation — count curve 每 level 仅 5 batches\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"3-seed × 25-batch count curves with ±1SD error bars\"\n  resolution_round: 10\n\n- id: R10-W1\n  summary: \"\\\\enlargethispage 操纵页面布局\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"已删除\"\n  resolution_round: 11\n\n- id: R10-W2\n  summary: \"Negative results (§5) 缺 constructive next steps\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"§5 Future directions added\"\n  resolution_round: 11\n\n- id: R10-W3\n  summary: \"Abstract 数字密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"精简至 3 个核心数字\"\n  resolution_round: 12\n\n- id: R10-W4\n  summary: \"Introduction Contribution list 含未铺垫概念\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"改为方法论声明格式\"\n  resolution_round: 12\n\n- id: R10-W5\n  summary: \"BCS 'generalizes across tasks' 过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  resolution: \"Contribution 3 限定为 RE-specific\"\n  resolution_round: 12\n\n- id: R10-W6\n  summary: \"Em-dash 使用偏高\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"已清理\"\n  resolution_round: 11\n\n- id: R10-W7\n  summary: \"Supplementary placeholder sections\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"所有补充材料在 main.tex Appendix\"\n  resolution_round: 12\n\n- id: R11-W3\n  summary: \"Prompt variant analysis underpowered\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Rothman 1990 + directional consistency\"\n  resolution_round: 12\n\n- id: R10-m4\n  summary: \"Multiple comparisons: Rothman 1990\"\n  category: method\n  severity: info\n  status: resolved\n  resolution: \"R12 交叉共识\"\n  resolution_round: 12\n\n- id: R2-N3-80rel\n  summary: \"extreme-batch 31.2pp 为 headline, typical 2.2pp 被弱化\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"Intro typical-first; Discussion IQR caveat\"\n  resolution_round: 9\n\n- id: R4-N1\n  summary: \"RE batch composition +1.4pp (p≈0.19) Contribution #4 framing\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"Contribution #4 → 'structural barriers'\"\n  resolution_round: 9\n\n- id: R6-N1\n  summary: \"Two-channel decomposition 概念贡献有限\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"4 contributions rewritten\"\n  resolution_round: 9\n\n- id: MW2\n  summary: \"Pairwise r²=1.3% 到 batch R²=22% 聚合 conditioning bias\"\n  category: framing\n  severity: critical\n  status: resolved\n  resolution: \"simulation → illustrative; R²=0.218 primary\"\n  resolution_round: 9\n\n- id: R5-W1\n  summary: \"FewRel train+val 合并 contamination 风险\"\n  category: method\n  severity: warning\n  status: resolved\n  resolution: \"Split-origin covariate confirms BCS partial effect unchanged\"\n  resolution_round: 9\n\n- id: R5-N1\n  summary: \"SCS novelty — metric 与 LLM-PEE 形式相同\"\n  category: framing\n  severity: warning\n  status: resolved\n  resolution: \"Contribution #2 reframed as empirical validation\"\n  resolution_round: 9\n\n- id: R6-W1\n  summary: \"'首次 controlled study' 声称需限定\"\n  category: framing\n  severity: warning\n  status: resolved\n  resolution: \"'To our knowledge' added\"\n  resolution_round: 9\n\n- id: R6-N2\n  summary: \"正文可能超过 8 页限制\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"编译确认 Conclusion 在 p8\"\n  resolution_round: 9\n\n- id: R10-PS\n  summary: \"Prompt sensitivity 实验结果需整合入论文\"\n  category: experiment\n  severity: warning\n  status: resolved\n  resolution: \"Integrated into §4.3 + Appendix H\"\n  resolution_round: 11\n\n- id: R12-W5\n  summary: \"Orphan bib entries\"\n  category: format\n  severity: warning\n  status: resolved\n  resolution: \"已删除\"\n  resolution_round: 13\n\n- id: R10-m1\n  summary: \"Cross-seed variance vs typical effect\"\n  category: method\n  severity: info\n  status: resolved\n  resolution: \"§3.4 说明 FP8 non-determinism\"\n  resolution_round: 14\n\n- id: R10-m2\n  summary: \"NER U-shape mechanistic 解释未验证\"\n  category: framing\n  severity: info\n  status: resolved\n  resolution: \"'likely reflects' 表述\"\n  resolution_round: 14\n\n- id: R11-W2\n  summary: \"TOST 术语首次出现未展开\"\n  category: writing\n  severity: warning\n  status: resolved\n  resolution: \"Introduction 已展开 'Two One-Sided Tests [TOST]'\"\n  resolution_round: 14\n\n- id: R12-W4\n  summary: \"Introduction findings vs contributions 不对齐\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - {round: 15, reviewers: [], note: \"本轮未直接提及\"}\n  action_items:\n    - {round: 13, action: \"统一 findings 和 contributions 数量/映射\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W2\n  summary: \"BCS > 0.59 阈值缺乏 formal derivation\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  action_items:\n    - {round: 13, action: \"删除 0.59 阈值\", assigned_to: agent, status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W4\n  summary: \"Abstract 偏短且缺 motivation\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R2], note: \"R2 未再次明确提出 length 问题; 但 N2 关注 framing balance\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-m1\n  summary: \"Abstract 偏短 (~130-140 words)\"\n  category: writing\n  severity: info\n  status: resolved\n  resolution: \"升级追踪于 R13-W4; R14 评价 ~170 words 在范围内\"\n  resolution_round: 14\n\n- id: R14-W1\n  summary: \"'BCS explains 22-53%' 中 53% 稳定性未验证\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1, R2], note: \"升级追踪于 R15-N2\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W2\n  summary: \"'fundamental property of in-context learning' claim 跨模型证据不足\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1, R2], note: \"升级追踪于 R15-W3\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-m1\n  summary: \"MAVEN 应降级为 supplementary dataset\"\n  category: framing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - {round: 15, reviewers: [R1, R2], note: \"升级追踪于 R15-N3\"}\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 1531 · 2026-05-18T05:39:07.341926+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml\", \"bytes\": 24430}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1532 · 2026-05-18T05:41:58.472234+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "schema-dag-extraction",
  "report": "# Round 15 审稿报告：schema-dag-extraction\n\n**论文**: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n**Venue**: EMNLP 2026 via ARR May 2026 cycle\n**审稿编排**: 2 名 Reviewer（R1: 方法严谨性+实验设计+统计论证；R2: 新颖性+完整性+写作质量+格式合规）\n**流程**: Round 1 独立审稿 → 交叉分享（逐条 AGREE/REBUT） → 收敛判断 → 汇总报告\n\n---\n\n## Summary\n\n本文对 training-free LLM 信息抽取中 schema 复杂度如何预测性能下降进行了系统性实证研究。作者将性能下降分解为两个维度——count-related recall decline 和 confusability-related type substitution——并通过 BCS-controlled quasi-experiments 在 FewRel、DocRED、Few-NERD、MAVEN 四个数据集上验证。论文还报告了 schema decomposition (SDGD) 的负面结果及其机制诊断。实验设计精细、统计方法严谨（TOST、bootstrap CI、permutation tests），负面结果诊断深度出色，Limitations 极为坦诚。但核心 confusability metric (SCS/BCS) 与 LLM-PEE 形式相同、practical effect size 小（typical 2.2pp）、强结果集中在 RE 任务，novelty 和 practical significance 不足以支撑主会议接收。\n\n---\n\n## Strengths\n\n**S1. 实验设计精细且系统化** [共识]\nCount curves + BCS-controlled 的双范式设计有效隔离 count 和 confusability。Within-pool analysis（80-relation pool → 16-relation subsets）控制 pool composition confound（permutation p=0.60）。BCS-controlled 跨 FewRel 和 DocRED 的一致性提供了 replication 证据。\n\n**S2. 统计方法论高于 venue 平均水平** [共识]\nTOST equivalence testing（而非仅靠 NHST non-significance）、percentile bootstrap CI (B=10,000)、cluster bootstrap for pairwise correlations、variance decomposition、permutation tests。TOST sensitivity analysis across margins 和 logit-scale sensitivity check 体现审慎态度。在 EMNLP submissions 中不常见。\n\n**S3. 负面结果报告诚实且诊断深刻** [共识]\nSDGD failure 不仅报告失败，还精确诊断 merge amplification（NER precision 0.563→0.210）和 routing failure（constrained decoding 导致 73.4% instances 在 3-5 sub-schemas 同时获正预测）。Few-shot 反而扩大 confusability gap (+4.3pp) 也是有价值的负面发现。\n\n**S4. Centrality confound 发现有方法论价值** [共识]\nMAVEN 上 BCS-F1 正相关的发现、centrality confound 的诊断、partial correlation 控制后效应消失（p>0.2），以及 \"mean BCS 只适用于 cross-domain schemas\" 的结论，对后续使用 embedding-based metrics 的研究有方法论指导意义。\n\n**S5. Cross-model validation 覆盖面广** [共识]\nQwen3-32B → Llama-8B → Llama-70B → Gemini Flash (API)，覆盖 open-weight 和 proprietary，8B-70B+ scales。Dimension 1 在所有模型上复制。\n\n**S6. Limitations 模范级别** [共识]\n8 条 limitation + multiple comparisons 讨论，覆盖 model coverage、effect size、factorial interaction、decomposition scope、evaluation metric、format specificity、causal mechanism、data contamination。远超 venue 平均水平。\n\n**S7. 写作质量高、格式合规** [R2]\n无 AI 写作痕迹（无 em-dash、无 -ing 短语结尾、无过度分段），术语首次出现均有定义，正文恰好 8 页，Limitations section 存在，Checklist 完整，匿名化正确。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1. [critical] [共识] Logit-scale TOST inconclusive (p=0.209) 削弱 \"bounded association\" 核心 claim**\n- 位置：§4.4 Multi-Dimensional Degradation, Appendix F\n- Linear-scale TOST p=0.003 at ±3pp，但 logit-scale interaction 0.111 logit units (p=0.047, marginally significant)，logit-scale TOST p=0.209 (inconclusive)。Accuracy 接近 50%（high-BCS ≈ 51%）时 linear scale 系统性压缩 interaction effects。选择 linear scale 作为 \"primary test\" 是 convenience choice，不是 methodological necessity，构成分析自由度。\n- 论文的 back-transformation argument (2.78pp at floor p=0.51, within ±3pp) 提供 partial mitigation。Inconclusive ≠ rejected，但 claim 必须降级。\n- **要求**: 正文（非仅 Appendix）报告 logit-scale 结果；claim 改为 \"consistent with bounded association under the primary linear specification; inconclusive on logit scale\"；报告 TOST n=69 at ±3pp 的 post-hoc power。\n\n**W2. [critical] [共识] NER/ED batch-level 结果实质为 null，\"three tasks, four datasets\" generality claim 虚高**\n- 位置：§4.3, §4.5, §4.6, Title, Abstract\n- NER batch-level BCS-F1: r≈0, n=450。MAVEN per-type BCS-F1: centrality confound 完全解释 (p>0.2 after control)。NER pairwise SCS: r=0.112, r²=1.3%。\n- Dimension 1 (count decline) 跨任务成立（NER 0.72→~0.27, RE monotonic）。Dimension 2 (confusability) 仅 RE batch-level 成立。标题 \"Training-Free LLM Information Extraction\"（无限定词）暗示跨任务通用性。\n- Contribution 3 将此称为 \"task asymmetry\" 是诚实的，但 R2 正确指出这实质上是 NER/ED 的 null result。MAVEN 仅贡献 1 行 pairwise 数据 + centrality confound 分析，不支撑 \"event detection\" 和 \"four datasets\" claim。\n- **要求**: 标题或 Abstract 加入 confusability 效应的 RE-specificity 限定；\"four datasets\" → \"three primary datasets with supplementary MAVEN analysis\"；或在 Abstract 中平衡呈现 null results。\n\n**W3. [critical→warning] [基本共识，severity 分歧] DocRED R²=0.53 (n=35) CI 极宽 [0.27, 0.73]，\"22-53%\" 上界在叙事中权重过高**\n- 位置：Abstract, §1 Contribution 2, §4.3, §5 Discussion\n- R1 列为 critical，R2 认为 lower severity（DocRED 是 replication dataset，primary R²=0.218 from FewRel n=100 更可靠）。Adjusted R²=0.511，shrinkage 仅 0.014，slope 高度显著 (p<0.001)。CI 宽因 n 小，非 effect 不稳定。\n- **要求**: \"22-53%\" 表述后加注 CI 和样本量：如 \"22% [FewRel, n=100] to 53% [DocRED, n=35; 95% CI: 27-73%]\"。降低 53% 在 summary framing 中的权重。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W4. [major] [共识] Formal power analysis 缺失**\n- TOST n=69 at ±3pp 的 power 未报告。NER null (n=450, r≈0) 的 minimum detectable effect size 未报告。Power 不足会直接影响 linear-scale equivalence conclusion (p=0.003) 的可信度和 NER null claim 的解读。\n- **要求**: 报告 TOST post-hoc power；NER null 的 minimum detectable r at 80% power。\n\n**W5. [major] [共识] Single-seed (seed=42) 实验，typical effect 2.2pp 与 seed variance 2.7pp 可比**\n- BCS-controlled experiments、DocRED、MAVEN、cross-model validation 均为单 seed。Count curves 有 3 seeds。Seed SD=2.7pp at count 16（Appendix K）与 typical BCS gap 2.2pp 量级可比，意味着某些 seed 下 effect 可能不显著。Bootstrap CI 只捕获 batch composition variance，不含 seed variance。\n- **要求**: 核心 BCS-controlled RE 实验增加 multi-seed replication；或在 Limitations 中明确说明影响。\n\n**W6. [major] [共识] Dimension 2 跨模型验证不充分**\n- BCS-controlled 完整验证仅 Qwen3-32B 和 Llama-8B。Llama-70B 仅 count=16 一个数据点（$\\Delta=+10.9$pp, CI excludes zero）。Gemini 无 Dim2 数据。Abstract/Conclusion \"patterns replicate across model scales and architecture families\" 暗示全面验证。\n- **要求**: Abstract/Conclusion 区分 Dim1 和 Dim2 的验证范围。\n\n**W7. [major] [R2 raised, R1 partially agrees] SCS/BCS 与 LLM-PEE 形式相同，Abstract \"operationalize\" 措辞暗示独立新颖性**\n- SCS = pairwise cosine similarity of type name embeddings，论文 §2 自承与 LLM-PEE 相同。BCS = mean aggregation。Novelty 完全在 experimental framework 和 findings。但 Abstract/Contribution 措辞给读者 metric 本身是贡献的印象。\n- R1 认为是 presentation issue（§2 self-qualification 已充分），R2 认为是 structural novelty deficit（capping the paper at Findings）。\n- **要求**: Abstract \"operationalize confusability via SCS\" → 更中性措辞（如 \"quantify confusability using pairwise embedding similarity\"）；Contribution 2 明确声明 metric 与 LLM-PEE 相同，贡献在于 controlled framework。\n\n**W8. [major] [共识] Practical effect size 小 (2.2pp typical gap, r²=1.3%)，Abstract 叙事重心偏向极端条件数字**\n- Typical-batch BCS gap 2.2pp (CI [0.4, 4.0])，quartile gap 3.9-5.3pp。Abstract 领衔 -49pp (Dimension 1, DocRED full-schema) 和 \"22-53%\" R²。虽 Abstract 已区分 Dim1/Dim2 并报告 2.2pp，但叙事重心在戏剧性数字。Introduction findings summary 反复强调 extreme-batch gap，practical magnitude 放在 §4.3 的一个 paragraph。\n- R1 认为 Abstract 的事实区分正确（partial rebut），但同意叙事重心偏移。R2 认为 cherry-picking。\n- **要求**: Abstract 更突出 typical-batch magnitude；Introduction findings 平衡 extreme vs typical。\n\n### Minor\n\n**W9.** [info] Aggregation simulation (Appendix J) 声称 \"not evidence base\" 但正文 §4.3/§5 引用 ~3× amplification 作论证——定位矛盾。\n**W10.** [info] ρ=0.35 inter-pair SCS correlation 未报告 CI，aggregation simulation 缺 sensitivity analysis。\n**W11.** [info] Table 2 缺 FewRel pairwise r=0.187。\n**W12.** [info] NER U-shaped recovery 解释 (\"type-filtering overhead elimination\") 缺实验证据。\n**W13.** [info] Orphan bib entries: bogdanov2024nuner, xie2024selfimproving, zhang2023llmaaa, cheng2023batch, levy-2024-same-task。\n**W14.** [info] Gemini count 64 仅 13/25 batches，partial data 可信度打折。\n\n---\n\n## Reviewer Consensus\n\n以下为两位 Reviewer 达成共识的关键问题：\n\n1. **[AGREE] Logit-scale TOST inconclusive**: bounded association claim 需限定为 \"under linear specification; inconclusive on logit\"。R1 列为 critical N1，R2 列为 major W2，交叉后 R2 AGREE。\n2. **[AGREE] NER/ED generality overclaim**: confusability strong story 限于 RE。R2 列为 critical N3，R1 交叉 \"substantially agree\"。Dim1 跨任务成立，Dim2 batch-level 仅 RE。\n3. **[AGREE] Single-seed limitation**: typical 2.2pp 与 seed SD 2.7pp 可比。R1 W3 + R2 W3，交叉共识。\n4. **[AGREE] Power analysis 缺失**: TOST 和 NER null 均需 power 报告。R1 W1，R2 交叉 AGREE。\n5. **[AGREE] DocRED R² CI 宽**: 需在正文报告 CI，降低 53% 在 framing 中权重。R1 N2，R2 交叉 AGREE with nuance。\n6. **[AGREE] Dim2 跨模型验证不充分**: Abstract/Conclusion 需区分两个 dimension 的验证范围。R1 W4，R2 交叉 AGREE with nuance。\n7. **[AGREE] MAVEN 参与度极低**: \"four datasets\" → \"three primary + supplementary\"。R2 W1，R1 交叉 AGREE。\n8. **[AGREE] Orphan bib entries**: 5 个未引用条目需清理。R2 W6，R1 交叉 AGREE。\n\n---\n\n## Reviewer Divergence\n\n1. **SCS novelty severity**: R2 认为 SCS/BCS 无独立新颖性是 structural problem，将论文 ceiling 限制在 Findings（即使 soundness 全修也不升 Conference）。R1 认为是 presentation issue（§2 self-qualification 已充分，修改 Abstract 措辞即可）。**Review Director 评估**: R2 的批评有道理——metric 形式等同于 prior work 是客观事实，但论文的核心贡献在 experimental framework 和 findings 而非 metric 本身，positioning 调整可以部分缓解。这更接近 R1 的判断（presentation issue），但对 novelty-sensitive 的 reviewer 确实构成 acceptance barrier。\n\n2. **Abstract framing / cherry-picking**: R2 认为 Abstract 以 -49pp 领衔构成 cherry-picking。R1 反驳：Abstract 已明确区分 Dim1(-49pp)/Dim2(2.2pp) 且用 \"dominates\" 连接。**Review Director 评估**: 事实层面 R1 正确（Abstract 确实区分了），但 R2 的阅读体验反馈有效——审稿人快速扫描时 -49pp 的数字冲击力遮盖结构化区分。叙事调整而非事实纠正。\n\n3. **TOST margin Cohen's d=0.5**: R1 认为用 d=0.5 (medium) 定义 equivalence margin 逻辑不通（medium ≠ negligible）。R2 反驳：TOST SESOI 不要求 \"negligible\"，论文的 130% amplification argument 是主要 justification，Cohen's d 仅辅助参照。**Review Director 评估**: R2 的 TOST 方法论理解更准确。SESOI = smallest effect of practical significance，不等于 negligible。但 d=0.5 的类比确实容易误导，建议弱化或删除。\n\n4. **Overall score**: R1 给 3.5 (Borderline Conference)，R2 给 3.0 (Findings)。核心分歧在 novelty 权重和负面结果的价值评估。R1 认为 task asymmetry、centrality confound、SDGD 诊断有独立的分析价值 (Excitement 3.0)。R2 认为这些不改变 novelty deficit (Excitement 2.5)。\n\n---\n\n## Questions for Authors\n\nQ1. TOST 在 n=69 下对 ±3pp margin 的 statistical power 是多少？如果 power < 0.8，linear-scale equivalence conclusion 的可信度如何？\n\nQ2. Aggregation simulation (Appendix J) 中 ρ=0.35 的 CI 是多少？如果 ρ=0.20，simulated batch R² 大约是多少？\n\nQ3. 是否尝试过在 NER 上使用 type-only matching（忽略 boundary）来检测 batch-level confusability signal？\n\nQ4. 论文多处出现 \"schema-associated degradation\" 和 \"schema-induced degradation\"——请确认全文是否已统一为 correlational 措辞。\n\nQ5. SCS 与 LLM-PEE 的 partitioning criterion 形式相同，论文的 incremental contribution 如何 beyond controlled experimentation？是否有 evidence 表明 SCS/BCS 在 schema design guidance 方面有 practical utility（超出分析意义）？\n\n---\n\n## Missing References\n\n**R1 提出**: Funder & Ozer (2019) effect size critique; Wellek (2010) TOST 教材; Schuirmann (1987) TOST 原始论文; constrained decoding 对 calibration 影响的文献。\n**R2 提出**: DLiSC (arXiv:2505.14992, Dual-LoRA with Incremental Schema Caching); SPT (arXiv:2506.01276, Schema as Parameterized Tools)。\n**共同建议**: structured prediction calibration 文献。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.0 (Findings)\n\n**EMNLP 2026 评分标准对照**:\n- 5 = Consider for Award (前 2.5%)\n- 4 = Conference (可被主会议接收)\n- 3.5 = Borderline Conference\n- 3 = Findings (可被 Findings 接收)\n- 2.5 = Borderline Findings\n\n**R1**: 3.5 (Borderline Conference) — Soundness 3.5, Excitement 3.0\n**R2**: 3.0 (Findings) — Soundness 3.5, Excitement 2.5\n**Director 综合**: 3.0 (Findings)\n\n**综合评分理由**:\n\nSoundness 维度两位 Reviewer 一致给 3.5，这反映了论文在实验设计和统计方法论上的高水准。Logit-scale TOST inconclusive 是最大的方法论弱点，但它影响的是一个 supporting claim（bounded association），不动摇两个维度各自的主效应。\n\nExcitement/Novelty 是关键分歧和决定性因素。论文面临三个结构性约束：\n1. **Metric 新颖性为零**: SCS/BCS 与 LLM-PEE 形式相同，这是客观事实。贡献完全在 experimental framework 和 findings。对 novelty 敏感的 reviewer 会将此视为 hard constraint。\n2. **Practical effect size 小**: Typical-batch confusability gap 2.2pp (CI [0.4, 4.0]) 低于多数部署场景的显著性阈值。极端 batch 的 25-31pp gap 来自刻意构造，不代表自然条件。这限制了从业者的 actionable takeaway。\n3. **跨任务通用性有限**: Confusability 的 batch-level 强效应仅限于 RE classification format；NER 和 ED 实质上是 null results。\"Three tasks, four datasets\" 的 generality framing 虚高。\n\n论文的正面价值——精细的实验设计、诚实的负面结果报告、centrality confound 的方法论贡献、task asymmetry 的诊断性发现——使其成为一篇高质量的分析性 Findings 论文。但上述三个结构性约束共同决定了它难以达到主会议的 novelty 和 impact bar。\n\n**置信度**: 4/5（两位 Reviewer 均仔细审阅全文及 Appendix，统计方法论和 NLP IE 文献覆盖充分）\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"operationalize confusability via the Schema Confusability Score (SCS)\" → 需降低 metric novelty 暗示\n- \"up to −49pp\" 为 Dimension 1 DocRED，叙事与 confusability 的关联可能误导快速阅读者\n- 2.2pp typical gap 需更突出呈现\n- \"BCS explains 22-53%\" 需附 CI\n\n### Introduction\n- Finding (1) 仍为 56 词复合句，可拆为 2-3 句\n- Findings 与 Contributions 的映射不完全一一对应\n- \"first controlled study\" 需 qualify（基本现象已有 Li et al. 2023, LLM-PEE 报告）\n\n### §2 Related Work\n- SCS novelty paragraph positioning 合理，但与 Abstract/Contribution 的 metric-centric 措辞不一致\n- 缺 DLiSC, SPT 引用；缺 TOST 原始文献 (Schuirmann 1987)\n\n### §3 Experimental Setup\n- §3.2 \"We define\" → 需与 §2 \"SCS shares its formal definition with LLM-PEE\" 统一\n- FewRel balanced design 是 BCS analysis 的关键优势，值得更强调\n- DocRED/MAVEN 5 batches vs FewRel/Few-NERD 25 batches 的不对称需解释\n\n### §4 Results\n- §4.4: \"bounded association\" claim 需加限定 \"under linear specification\"；logit-scale 结果需提升到正文\n- §4.3 practical magnitude paragraph 是论文最重要的 honest framing，应考虑前置\n- §4.6 centrality confound 分析出色\n\n### §5 SDGD\n- Merge amplification 诊断清晰\n- 缺 k vs false positive 率的定量关系\n- Routing failure 缺代表性 error cases\n\n### §6 Discussion\n- \"no confusability amplification at scale\" 需加 \"under linear-scale specification\" 限定\n- 残余因果语言（\"schema-induced\"）需替换为 \"schema-associated\"\n\n### Conclusion\n- 偏短，future work 方向可扩展\n- \"consistent across tested model families\" 比 \"fundamental property\" 更准确\n\n### Limitations\n- 模范级别，8 条 + multiple comparisons 讨论\n- 坦诚度远超 venue 平均\n\n### Checklist\n- 完整，A4 声明 AI 使用合理\n\n### Format\n- ✅ 正文 8 页, ACL template, review mode, anonymous\n- ⚠️ 5 个 orphan bib entries 需清理\n",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0",
  "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "schema-dag-extraction",
    "report": "# Round 15 审稿报告：schema-dag-extraction\n\n**论文**: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n**Venue**: EMNLP 2026 via ARR May 2026 cycle\n**审稿编排**: 2 名 Reviewer（R1: 方法严谨性+实验设计+统计论证；R2: 新颖性+完整性+写作质量+格式合规）\n**流程**: Round 1 独立审稿 → 交叉分享（逐条 AGREE/REBUT） → 收敛判断 → 汇总报告\n\n---\n\n## Summary\n\n本文对 training-free LLM 信息抽取中 schema 复杂度如何预测性能下降进行了系统性实证研究。作者将性能下降分解为两个维度——count-related recall decline 和 confusability-related type substitution——并通过 BCS-controlled quasi-experiments 在 FewRel、DocRED、Few-NERD、MAVEN 四个数据集上验证。论文还报告了 schema decomposition (SDGD) 的负面结果及其机制诊断。实验设计精细、统计方法严谨（TOST、bootstrap CI、permutation tests），负面结果诊断深度出色，Limitations 极为坦诚。但核心 confusability metric (SCS/BCS) 与 LLM-PEE 形式相同、practical effect size 小（typical 2.2pp）、强结果集中在 RE 任务，novelty 和 practical significance 不足以支撑主会议接收。\n\n---\n\n## Strengths\n\n**S1. 实验设计精细且系统化** [共识]\nCount curves + BCS-controlled 的双范式设计有效隔离 count 和 confusability。Within-pool analysis（80-relation pool → 16-relation subsets）控制 pool composition confound（permutation p=0.60）。BCS-controlled 跨 FewRel 和 DocRED 的一致性提供了 replication 证据。\n\n**S2. 统计方法论高于 venue 平均水平** [共识]\nTOST equivalence testing（而非仅靠 NHST non-significance）、percentile bootstrap CI (B=10,000)、cluster bootstrap for pairwise correlations、variance decomposition、permutation tests。TOST sensitivity analysis across margins 和 logit-scale sensitivity check 体现审慎态度。在 EMNLP submissions 中不常见。\n\n**S3. 负面结果报告诚实且诊断深刻** [共识]\nSDGD failure 不仅报告失败，还精确诊断 merge amplification（NER precision 0.563→0.210）和 routing failure（constrained decoding 导致 73.4% instances 在 3-5 sub-schemas 同时获正预测）。Few-shot 反而扩大 confusability gap (+4.3pp) 也是有价值的负面发现。\n\n**S4. Centrality confound 发现有方法论价值** [共识]\nMAVEN 上 BCS-F1 正相关的发现、centrality confound 的诊断、partial correlation 控制后效应消失（p>0.2），以及 \"mean BCS 只适用于 cross-domain schemas\" 的结论，对后续使用 embedding-based metrics 的研究有方法论指导意义。\n\n**S5. Cross-model validation 覆盖面广** [共识]\nQwen3-32B → Llama-8B → Llama-70B → Gemini Flash (API)，覆盖 open-weight 和 proprietary，8B-70B+ scales。Dimension 1 在所有模型上复制。\n\n**S6. Limitations 模范级别** [共识]\n8 条 limitation + multiple comparisons 讨论，覆盖 model coverage、effect size、factorial interaction、decomposition scope、evaluation metric、format specificity、causal mechanism、data contamination。远超 venue 平均水平。\n\n**S7. 写作质量高、格式合规** [R2]\n无 AI 写作痕迹（无 em-dash、无 -ing 短语结尾、无过度分段），术语首次出现均有定义，正文恰好 8 页，Limitations section 存在，Checklist 完整，匿名化正确。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1. [critical] [共识] Logit-scale TOST inconclusive (p=0.209) 削弱 \"bounded association\" 核心 claim**\n- 位置：§4.4 Multi-Dimensional Degradation, Appendix F\n- Linear-scale TOST p=0.003 at ±3pp，但 logit-scale interaction 0.111 logit units (p=0.047, marginally significant)，logit-scale TOST p=0.209 (inconclusive)。Accuracy 接近 50%（high-BCS ≈ 51%）时 linear scale 系统性压缩 interaction effects。选择 linear scale 作为 \"primary test\" 是 convenience choice，不是 methodological necessity，构成分析自由度。\n- 论文的 back-transformation argument (2.78pp at floor p=0.51, within ±3pp) 提供 partial mitigation。Inconclusive ≠ rejected，但 claim 必须降级。\n- **要求**: 正文（非仅 Appendix）报告 logit-scale 结果；claim 改为 \"consistent with bounded association under the primary linear specification; inconclusive on logit scale\"；报告 TOST n=69 at ±3pp 的 post-hoc power。\n\n**W2. [critical] [共识] NER/ED batch-level 结果实质为 null，\"three tasks, four datasets\" generality claim 虚高**\n- 位置：§4.3, §4.5, §4.6, Title, Abstract\n- NER batch-level BCS-F1: r≈0, n=450。MAVEN per-type BCS-F1: centrality confound 完全解释 (p>0.2 after control)。NER pairwise SCS: r=0.112, r²=1.3%。\n- Dimension 1 (count decline) 跨任务成立（NER 0.72→~0.27, RE monotonic）。Dimension 2 (confusability) 仅 RE batch-level 成立。标题 \"Training-Free LLM Information Extraction\"（无限定词）暗示跨任务通用性。\n- Contribution 3 将此称为 \"task asymmetry\" 是诚实的，但 R2 正确指出这实质上是 NER/ED 的 null result。MAVEN 仅贡献 1 行 pairwise 数据 + centrality confound 分析，不支撑 \"event detection\" 和 \"four datasets\" claim。\n- **要求**: 标题或 Abstract 加入 confusability 效应的 RE-specificity 限定；\"four datasets\" → \"three primary datasets with supplementary MAVEN analysis\"；或在 Abstract 中平衡呈现 null results。\n\n**W3. [critical→warning] [基本共识，severity 分歧] DocRED R²=0.53 (n=35) CI 极宽 [0.27, 0.73]，\"22-53%\" 上界在叙事中权重过高**\n- 位置：Abstract, §1 Contribution 2, §4.3, §5 Discussion\n- R1 列为 critical，R2 认为 lower severity（DocRED 是 replication dataset，primary R²=0.218 from FewRel n=100 更可靠）。Adjusted R²=0.511，shrinkage 仅 0.014，slope 高度显著 (p<0.001)。CI 宽因 n 小，非 effect 不稳定。\n- **要求**: \"22-53%\" 表述后加注 CI 和样本量：如 \"22% [FewRel, n=100] to 53% [DocRED, n=35; 95% CI: 27-73%]\"。降低 53% 在 summary framing 中的权重。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W4. [major] [共识] Formal power analysis 缺失**\n- TOST n=69 at ±3pp 的 power 未报告。NER null (n=450, r≈0) 的 minimum detectable effect size 未报告。Power 不足会直接影响 linear-scale equivalence conclusion (p=0.003) 的可信度和 NER null claim 的解读。\n- **要求**: 报告 TOST post-hoc power；NER null 的 minimum detectable r at 80% power。\n\n**W5. [major] [共识] Single-seed (seed=42) 实验，typical effect 2.2pp 与 seed variance 2.7pp 可比**\n- BCS-controlled experiments、DocRED、MAVEN、cross-model validation 均为单 seed。Count curves 有 3 seeds。Seed SD=2.7pp at count 16（Appendix K）与 typical BCS gap 2.2pp 量级可比，意味着某些 seed 下 effect 可能不显著。Bootstrap CI 只捕获 batch composition variance，不含 seed variance。\n- **要求**: 核心 BCS-controlled RE 实验增加 multi-seed replication；或在 Limitations 中明确说明影响。\n\n**W6. [major] [共识] Dimension 2 跨模型验证不充分**\n- BCS-controlled 完整验证仅 Qwen3-32B 和 Llama-8B。Llama-70B 仅 count=16 一个数据点（$\\Delta=+10.9$pp, CI excludes zero）。Gemini 无 Dim2 数据。Abstract/Conclusion \"patterns replicate across model scales and architecture families\" 暗示全面验证。\n- **要求**: Abstract/Conclusion 区分 Dim1 和 Dim2 的验证范围。\n\n**W7. [major] [R2 raised, R1 partially agrees] SCS/BCS 与 LLM-PEE 形式相同，Abstract \"operationalize\" 措辞暗示独立新颖性**\n- SCS = pairwise cosine similarity of type name embeddings，论文 §2 自承与 LLM-PEE 相同。BCS = mean aggregation。Novelty 完全在 experimental framework 和 findings。但 Abstract/Contribution 措辞给读者 metric 本身是贡献的印象。\n- R1 认为是 presentation issue（§2 self-qualification 已充分），R2 认为是 structural novelty deficit（capping the paper at Findings）。\n- **要求**: Abstract \"operationalize confusability via SCS\" → 更中性措辞（如 \"quantify confusability using pairwise embedding similarity\"）；Contribution 2 明确声明 metric 与 LLM-PEE 相同，贡献在于 controlled framework。\n\n**W8. [major] [共识] Practical effect size 小 (2.2pp typical gap, r²=1.3%)，Abstract 叙事重心偏向极端条件数字**\n- Typical-batch BCS gap 2.2pp (CI [0.4, 4.0])，quartile gap 3.9-5.3pp。Abstract 领衔 -49pp (Dimension 1, DocRED full-schema) 和 \"22-53%\" R²。虽 Abstract 已区分 Dim1/Dim2 并报告 2.2pp，但叙事重心在戏剧性数字。Introduction findings summary 反复强调 extreme-batch gap，practical magnitude 放在 §4.3 的一个 paragraph。\n- R1 认为 Abstract 的事实区分正确（partial rebut），但同意叙事重心偏移。R2 认为 cherry-picking。\n- **要求**: Abstract 更突出 typical-batch magnitude；Introduction findings 平衡 extreme vs typical。\n\n### Minor\n\n**W9.** [info] Aggregation simulation (Appendix J) 声称 \"not evidence base\" 但正文 §4.3/§5 引用 ~3× amplification 作论证——定位矛盾。\n**W10.** [info] ρ=0.35 inter-pair SCS correlation 未报告 CI，aggregation simulation 缺 sensitivity analysis。\n**W11.** [info] Table 2 缺 FewRel pairwise r=0.187。\n**W12.** [info] NER U-shaped recovery 解释 (\"type-filtering overhead elimination\") 缺实验证据。\n**W13.** [info] Orphan bib entries: bogdanov2024nuner, xie2024selfimproving, zhang2023llmaaa, cheng2023batch, levy-2024-same-task。\n**W14.** [info] Gemini count 64 仅 13/25 batches，partial data 可信度打折。\n\n---\n\n## Reviewer Consensus\n\n以下为两位 Reviewer 达成共识的关键问题：\n\n1. **[AGREE] Logit-scale TOST inconclusive**: bounded association claim 需限定为 \"under linear specification; inconclusive on logit\"。R1 列为 critical N1，R2 列为 major W2，交叉后 R2 AGREE。\n2. **[AGREE] NER/ED generality overclaim**: confusability strong story 限于 RE。R2 列为 critical N3，R1 交叉 \"substantially agree\"。Dim1 跨任务成立，Dim2 batch-level 仅 RE。\n3. **[AGREE] Single-seed limitation**: typical 2.2pp 与 seed SD 2.7pp 可比。R1 W3 + R2 W3，交叉共识。\n4. **[AGREE] Power analysis 缺失**: TOST 和 NER null 均需 power 报告。R1 W1，R2 交叉 AGREE。\n5. **[AGREE] DocRED R² CI 宽**: 需在正文报告 CI，降低 53% 在 framing 中权重。R1 N2，R2 交叉 AGREE with nuance。\n6. **[AGREE] Dim2 跨模型验证不充分**: Abstract/Conclusion 需区分两个 dimension 的验证范围。R1 W4，R2 交叉 AGREE with nuance。\n7. **[AGREE] MAVEN 参与度极低**: \"four datasets\" → \"three primary + supplementary\"。R2 W1，R1 交叉 AGREE。\n8. **[AGREE] Orphan bib entries**: 5 个未引用条目需清理。R2 W6，R1 交叉 AGREE。\n\n---\n\n## Reviewer Divergence\n\n1. **SCS novelty severity**: R2 认为 SCS/BCS 无独立新颖性是 structural problem，将论文 ceiling 限制在 Findings（即使 soundness 全修也不升 Conference）。R1 认为是 presentation issue（§2 self-qualification 已充分，修改 Abstract 措辞即可）。**Review Director 评估**: R2 的批评有道理——metric 形式等同于 prior work 是客观事实，但论文的核心贡献在 experimental framework 和 findings 而非 metric 本身，positioning 调整可以部分缓解。这更接近 R1 的判断（presentation issue），但对 novelty-sensitive 的 reviewer 确实构成 acceptance barrier。\n\n2. **Abstract framing / cherry-picking**: R2 认为 Abstract 以 -49pp 领衔构成 cherry-picking。R1 反驳：Abstract 已明确区分 Dim1(-49pp)/Dim2(2.2pp) 且用 \"dominates\" 连接。**Review Director 评估**: 事实层面 R1 正确（Abstract 确实区分了），但 R2 的阅读体验反馈有效——审稿人快速扫描时 -49pp 的数字冲击力遮盖结构化区分。叙事调整而非事实纠正。\n\n3. **TOST margin Cohen's d=0.5**: R1 认为用 d=0.5 (medium) 定义 equivalence margin 逻辑不通（medium ≠ negligible）。R2 反驳：TOST SESOI 不要求 \"negligible\"，论文的 130% amplification argument 是主要 justification，Cohen's d 仅辅助参照。**Review Director 评估**: R2 的 TOST 方法论理解更准确。SESOI = smallest effect of practical significance，不等于 negligible。但 d=0.5 的类比确实容易误导，建议弱化或删除。\n\n4. **Overall score**: R1 给 3.5 (Borderline Conference)，R2 给 3.0 (Findings)。核心分歧在 novelty 权重和负面结果的价值评估。R1 认为 task asymmetry、centrality confound、SDGD 诊断有独立的分析价值 (Excitement 3.0)。R2 认为这些不改变 novelty deficit (Excitement 2.5)。\n\n---\n\n## Questions for Authors\n\nQ1. TOST 在 n=69 下对 ±3pp margin 的 statistical power 是多少？如果 power < 0.8，linear-scale equivalence conclusion 的可信度如何？\n\nQ2. Aggregation simulation (Appendix J) 中 ρ=0.35 的 CI 是多少？如果 ρ=0.20，simulated batch R² 大约是多少？\n\nQ3. 是否尝试过在 NER 上使用 type-only matching（忽略 boundary）来检测 batch-level confusability signal？\n\nQ4. 论文多处出现 \"schema-associated degradation\" 和 \"schema-induced degradation\"——请确认全文是否已统一为 correlational 措辞。\n\nQ5. SCS 与 LLM-PEE 的 partitioning criterion 形式相同，论文的 incremental contribution 如何 beyond controlled experimentation？是否有 evidence 表明 SCS/BCS 在 schema design guidance 方面有 practical utility（超出分析意义）？\n\n---\n\n## Missing References\n\n**R1 提出**: Funder & Ozer (2019) effect size critique; Wellek (2010) TOST 教材; Schuirmann (1987) TOST 原始论文; constrained decoding 对 calibration 影响的文献。\n**R2 提出**: DLiSC (arXiv:2505.14992, Dual-LoRA with Incremental Schema Caching); SPT (arXiv:2506.01276, Schema as Parameterized Tools)。\n**共同建议**: structured prediction calibration 文献。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.0 (Findings)\n\n**EMNLP 2026 评分标准对照**:\n- 5 = Consider for Award (前 2.5%)\n- 4 = Conference (可被主会议接收)\n- 3.5 = Borderline Conference\n- 3 = Findings (可被 Findings 接收)\n- 2.5 = Borderline Findings\n\n**R1**: 3.5 (Borderline Conference) — Soundness 3.5, Excitement 3.0\n**R2**: 3.0 (Findings) — Soundness 3.5, Excitement 2.5\n**Director 综合**: 3.0 (Findings)\n\n**综合评分理由**:\n\nSoundness 维度两位 Reviewer 一致给 3.5，这反映了论文在实验设计和统计方法论上的高水准。Logit-scale TOST inconclusive 是最大的方法论弱点，但它影响的是一个 supporting claim（bounded association），不动摇两个维度各自的主效应。\n\nExcitement/Novelty 是关键分歧和决定性因素。论文面临三个结构性约束：\n1. **Metric 新颖性为零**: SCS/BCS 与 LLM-PEE 形式相同，这是客观事实。贡献完全在 experimental framework 和 findings。对 novelty 敏感的 reviewer 会将此视为 hard constraint。\n2. **Practical effect size 小**: Typical-batch confusability gap 2.2pp (CI [0.4, 4.0]) 低于多数部署场景的显著性阈值。极端 batch 的 25-31pp gap 来自刻意构造，不代表自然条件。这限制了从业者的 actionable takeaway。\n3. **跨任务通用性有限**: Confusability 的 batch-level 强效应仅限于 RE classification format；NER 和 ED 实质上是 null results。\"Three tasks, four datasets\" 的 generality framing 虚高。\n\n论文的正面价值——精细的实验设计、诚实的负面结果报告、centrality confound 的方法论贡献、task asymmetry 的诊断性发现——使其成为一篇高质量的分析性 Findings 论文。但上述三个结构性约束共同决定了它难以达到主会议的 novelty 和 impact bar。\n\n**置信度**: 4/5（两位 Reviewer 均仔细审阅全文及 Appendix，统计方法论和 NLP IE 文献覆盖充分）\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"operationalize confusability via the Schema Confusability Score (SCS)\" → 需降低 metric novelty 暗示\n- \"up to −49pp\" 为 Dimension 1 DocRED，叙事与 confusability 的关联可能误导快速阅读者\n- 2.2pp typical gap 需更突出呈现\n- \"BCS explains 22-53%\" 需附 CI\n\n### Introduction\n- Finding (1) 仍为 56 词复合句，可拆为 2-3 句\n- Findings 与 Contributions 的映射不完全一一对应\n- \"first controlled study\" 需 qualify（基本现象已有 Li et al. 2023, LLM-PEE 报告）\n\n### §2 Related Work\n- SCS novelty paragraph positioning 合理，但与 Abstract/Contribution 的 metric-centric 措辞不一致\n- 缺 DLiSC, SPT 引用；缺 TOST 原始文献 (Schuirmann 1987)\n\n### §3 Experimental Setup\n- §3.2 \"We define\" → 需与 §2 \"SCS shares its formal definition with LLM-PEE\" 统一\n- FewRel balanced design 是 BCS analysis 的关键优势，值得更强调\n- DocRED/MAVEN 5 batches vs FewRel/Few-NERD 25 batches 的不对称需解释\n\n### §4 Results\n- §4.4: \"bounded association\" claim 需加限定 \"under linear specification\"；logit-scale 结果需提升到正文\n- §4.3 practical magnitude paragraph 是论文最重要的 honest framing，应考虑前置\n- §4.6 centrality confound 分析出色\n\n### §5 SDGD\n- Merge amplification 诊断清晰\n- 缺 k vs false positive 率的定量关系\n- Routing failure 缺代表性 error cases\n\n### §6 Discussion\n- \"no confusability amplification at scale\" 需加 \"under linear-scale specification\" 限定\n- 残余因果语言（\"schema-induced\"）需替换为 \"schema-associated\"\n\n### Conclusion\n- 偏短，future work 方向可扩展\n- \"consistent across tested model families\" 比 \"fundamental property\" 更准确\n\n### Limitations\n- 模范级别，8 条 + multiple comparisons 讨论\n- 坦诚度远超 venue 平均\n\n### Checklist\n- 完整，A4 声明 AI 使用合理\n\n### Format\n- ✅ 正文 8 页, ACL template, review mode, anonymous\n- ⚠️ 5 个 orphan bib entries 需清理\n",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0",
    "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
  }
}
```

</details>

---


### Tool result

_source line 1533 · 2026-05-18T05:42:03.197591+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_51326259fe46fbae9da26b81cf03f1f8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4725
}
```

</details>

---


### Assistant

_source line 1534 · 2026-05-18T05:42:11.739674+00:00_

审稿报告已投递至 Research Director。

---

**Round 15 审稿完成。**

**Overall: 3.0 / 5 (Findings)**

核心结论：
- **Soundness 3.5**: 实验设计和统计方法论高于 venue 平均水平，logit-scale TOST inconclusive 是最大方法论弱点但仅影响 supporting claim
- **Excitement 2.5-3.0**: 三个结构性约束——metric 无新颖性 (=LLM-PEE)、practical effect size 小 (2.2pp)、confusability 强效应仅限 RE——共同限制 novelty 和 impact

**Reviewer 共识**: logit-scale TOST 需限定、NER/ED generality overclaim、single-seed 限制、DocRED R² CI 需报告、MAVEN 应降级为 supplementary、power analysis 缺失

**Reviewer 分歧**: SCS novelty 的 severity（presentation issue vs structural deficit）、Overall score（R1: 3.5 vs R2: 3.0）

**Issue Tracker** 已同步更新至 `artifacts/review_issues.yaml`（Round 15）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 141

## Round 141

2 recorded events


### User

_source line 1535 · 2026-05-18T05:42:14.440996+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

总结：对 R1 的 12 条意见，我标注了 7 条 AGREE（N1, N2 with nuance, W1, W3, W4 with nuance, W6）和 2 条 REBUT（W2 severity 过高, W5 对 TOST margin 逻辑的误读）。我维持 Overall 3.0 (Findings)，与 R1 的 3.5 (Borderline Conference) 的主要分歧在于 novelty 评估——即使 soundness concerns 全修复，SCS/BCS 无独立新颖性 + typical effect 仅 2.2pp + 强结果局限 RE 这三个结构性问题限制了论文 ceiling。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1536 · 2026-05-18T05:42:27.137175+00:00_

审稿报告已投递至 Research Director。

**Round 15 审稿完成总结**：

- **Overall**: 3.0 / 5 (Findings)
- **R1**: 3.5 (Borderline Conference), **R2**: 3.0 (Findings), **Director 综合**: 3.0

**三个结构性约束决定了评分**：
1. SCS/BCS metric 与 LLM-PEE 形式相同，novelty 完全依赖 experimental framework
2. Typical confusability effect 仅 2.2pp，practical actionability 有限
3. Batch-level 强结果集中在 RE，NER/ED 实质为 null

**Must-Fix 共识**：logit-scale TOST claim 需限定、NER/ED generality overclaim 需修正、DocRED R² CI 需在正文报告

**主要优势**：实验设计精细、统计方法高于 venue 平均、负面结果诊断出色、Limitations 模范级别、写作无 AI 痕迹、格式完全合规

Issue Tracker 已同步更新至 `artifacts/review_issues.yaml`（Round 15）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 142

## Round 142

142 recorded events


### User

_source line 1537 · 2026-05-18T07:00:21.216318+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema-dag-extraction
- 论文路径: projects/schema-dag-extraction/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1538 · 2026-05-18T07:00:27.547813+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1539 · 2026-05-18T07:00:27.549068+00:00_

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
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 1540 · 2026-05-18T07:00:30.162422+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1541 · 2026-05-18T07:00:30.213122+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1542 · 2026-05-18T07:00:34.886367+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,read_project_file,request_external_review,get_external_review_status,submit_review_report_to_research_director,update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,read_project_file,request_external_review,get_external_review_status,submit_review_report_to_research_director,update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 1543 · 2026-05-18T07:00:34.886718+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1544 · 2026-05-18T07:00:38.351436+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 1545 · 2026-05-18T07:00:38.452271+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1546 · 2026-05-18T07:00:42.524085+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 1547 · 2026-05-18T07:00:43.530561+00:00_

{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (61 个)\n\n- **exp012_llama_8b_r2_exp2**: DONE (negative) — \n- **exp012_llama_8b_r2**: DONE (success) — \n- **exp006_interaction_2x2**: DONE (negative) — \n- **exp012_llama_awq**: DONE (killed) — \n- **exp012_llama_8b_r3**: DONE (failed) — \n- **exp012_llama_8b**: DONE (killed) — \n- **exp_fewrel_40rel_r3**: DONE (failed) — \n- **exp_fewrel_40rel_r2**: DONE (failed) — \n- **exp012_llama_fewnerd_r4**: DONE (failed) — \n- **exp012_llama_8b_fewnerd**: DONE (failed) — \n- **exp_fewrel_40rel**: DONE (failed) — \n- **exp012_llama_fewnerd_r3**: DONE (failed) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp_multiseed_bcs_re: The BCS-accuracy correlation observed in FewRel BCS-controlled experiments (R²=0.22-0.53) is robust across random seeds. If seed=123 and seed=456 replicate the negative BCS-accuracy correlation direction and significance observed with seed=42, this confirms the finding is not a single-seed artifact. Rebuttal material for R15-W2 single-seed concern.（等待人工审批）\n- prompt_sensitivity（准备中）\n- prompt_sensitivity_dry4（准备中）\n- prompt_sensitivity_dry3（准备中）\n- prompt_sensitivity_dry2（准备中）\n- prompt_sensitivity_dry（准备中）\n- exp_aggregation_monte_carlo（准备中）\n- exp_scs_name_def_ablation（准备中）\n- exp_fewrel_contamination_check（准备中）\n- exp017_gpt4o_mini_fewrel（准备中）\n- …另有 3 项\n\n## 近期结论\n- **exp_gemini_flash_cross_model** (success): The two-dimensional degradation pattern (count-related decline + confusability-related type confusion) generalizes beyond open-weight models to proprietary API models. Gemini 2.5 Flash should show: (1) monotonic RE accuracy decline with count, and (2) significant BCS-accuracy correlation on extreme batches. If confirmed, the pattern is architecture-family-independent (open-weight Qwen/LLaMA 
…[truncated 1814 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 1548 · 2026-05-18T07:00:43.984325+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1549 · 2026-05-18T07:00:44.336308+00:00_

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
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B, 70B-Instruct (FP8), and Gemini 2.5 Flash (API). Dimension~1 (count-associated decline) has been validated on a proprietary model (Gemini 2.5 Flash, $\rho = -0.900$, $p = 0.037$; Appendix~\ref{sec:appendix_cross_model_gemini}); Dimension~2 (confusability-associated type substitution) has been verified only on open-weight models. Dimension~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
41	
42	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
43	
44	\item \textbf{Factorial interaction tests.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance ($p = 0.50$; Appendix~\ref{sec:appendix_factorial}). A FewRel factorial with TOST equivalence testing is consistent with bounded association under the primary linear specification ($p_{\text{TOST}} = 0.003$ at $\pm 3$\,pp, interaction = 0.47\,pp); however, the logit-scale TOST is inconclusive ($p = 0.209$). At $n =
…[truncated 5461 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1550 · 2026-05-18T07:00:44.437269+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 1551 · 2026-05-18T07:00:49.418599+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"}]

I found the search results. Here's what the search revealed about EMNLP 2026:

The search results primarily show information ab
…[truncated 1126 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 4981
}
```

</details>

---


### Tool call

_source line 1552 · 2026-05-18T07:00:56.722784+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 submission guidelines page limit template"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 submission guidelines page limit template"
  }
}
```

</details>

---


### Tool call

_source line 1553 · 2026-05-18T07:00:58.230794+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference call for papers Budapest submission deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference call for papers Budapest submission deadline"
  }
}
```

</details>

---


### Tool call

_source line 1554 · 2026-05-18T07:00:58.686399+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "literature_map.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "literature_map.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1555 · 2026-05-18T07:01:03.320152+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 submission guidelines page limit template"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"}]

Based on the search results, I found information about ACL Rolling Review (ARR) submission guidelines for 2026. Here are the key details:

## Template

The submission must adhere to the formatting in the submission templates, which is available as an Overleaf template. Additionally, ARR abandons the MS Word Template for conference submissions, with submissions based on the W
…[truncated 1030 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 6597
}
```

</details>

---


### Tool result

_source line 1556 · 2026-05-18T07:01:05.178911+00:00_

Web search results for query: "EMNLP 2026 main conference call for papers Budapest submission deadline"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 - Conference on Empirical Methods in Natural Language Processing Deadline | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/venue/emnlp"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"When is EMNLP 2026? Dates, Deadline & Location | ConferenceDeadlines.com","url":"https://www.conferencedeadlines.com/conference/emnlp"}]

Based on the search results, here is the key information about EMNLP 2026:

## Conference Details
EMNLP 2026 is being held in Budapest, Hungary on October 24 - 29, 2026.

## Main Conference Call for Papers

EMNLP 2026 invites the
…[truncated 1188 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 6948
}
```

</details>

---


### Tool result

_source line 1557 · 2026-05-18T07:01:05.179585+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml\", \"content\": \"# Literature Map for schema-dag-extraction\\n# Updated: 2026-05-15\\n# Paper: Multi-channel Degradation Model + SDGD Framework for Training-free LLM IE\\n\\n# =============================================================================\\n# DIRECT COMPETITORS — schema decomposition for LLM-based IE\\n# =============================================================================\\n\\n- id: llm-pee-2025\\n  title: \\\"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction\\\"\\n  year: 2025\\n  venue: arXiv\\n  url: https://arxiv.org/abs/2503.02628\\n  role: direct-competitor\\n  relevance_note: >\\n    Similarity-based type recall + type-partitioning prompting for massive event types.\\n    Divides candidate types into partitions to reduce prompt length.\\n    +5.4% event detection, +6.1% argument extraction, +12.9% F1 over mainstream LLMs zero-shot.\\n    KEY DIFF: partitions by similarity-based recall, NOT confusability-aware.\\n    Our DAG decomposition is confusability-driven, not just similarity-driven.\\n\\n- id: parse-2025\\n  title: \\\"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\\\"\\n  authors: [Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla]\\n  year: 2025\\n  venue: EMNLP 2025 Industry\\n  url: https://arxiv.org/abs/2510.08623\\n  role: direct-competitor\\n  relevance_note: >\\n    ARCHITECT autonomously rewrites JSON schemas for LLM consumption.\\n    SCOPE uses reflection-based extraction with guardrails. +64.7% on SWDE.\\n    Treats schema optimization as black-box LLM rewriting, not principled decomposition.\\n    Does NOT model type confusability explicitly.\\n\\n- id: dee-2024\\n  title: \\\"Decompose, Enrich, and Extract! Schema-aware Event Extraction using LLMs\\\"\\n  year: 2024\\
…[truncated 1466 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6493
}
```

</details>

---


### Tool call

_source line 1558 · 2026-05-18T07:01:10.155615+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "aclrollingreview.org CFP 2026 long paper short paper page limit 8 pages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "aclrollingreview.org CFP 2026 long paper short paper page limit 8 pages"
  }
}
```

</details>

---


### Tool call

_source line 1559 · 2026-05-18T07:01:10.207034+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
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

_source line 1560 · 2026-05-18T07:01:10.308684+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 1561 · 2026-05-18T07:01:14.982747+00:00_

Web search results for query: "aclrollingreview.org CFP 2026 long paper short paper page limit 8 pages"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"دعوة لتقديم أوراق المؤتمر الرئيسية -","url":"https://translate.google.com/translate?u=https%3A%2F%2F2026.eacl.org%2Fcalls%2Fpapers%2F&hl=ar&sl=en&tl=ar&client=srp"},{"title":"LINGUIST List 36.2627 Confs: 19th Conference of the European Chapter of the Association for Computational Linguistics (Morocco)","url":"https://linguistlist.org/issues/36/2627/"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Frequently Asked Questions for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/faq/"}]

Based on the search results for the ACL Rolling Review CFP 2026 information, here's what I found regarding page limits for long and short papers:

## Page Limits for 2026 Submissions

Long papers have a page limit of 8 pages, while short papers have a limit of 4 pages, not including limitations and ethical considerations.

More specifically:
- Long papers may consist of up to 8 pages of content, plus unlimited pages for references and appendices
- The limitations section, the optional ethical considerations section, references, and appendices should be included in the pdf for the paper (not counting towards the page limit)

For papers accepted to conferences like ACL 2026, final versions of 
…[truncated 259 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 4827
}
```

</details>

---


### Tool call

_source line 1562 · 2026-05-18T07:01:20.372160+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract all submission guidelines: page limits (long/short), template requirements, anonymity rules, appendix rules, citation format, responsible NLP checklist requirements, any specific formatting rules. Also extract all important dates especially ARR submission deadline."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract all submission guidelines: page limits (long/short), template requirements, anonymity rules, appendix rules, citation format, responsible NLP checklist requirements, any specific formatting rules. Also extract all important dates especially ARR submission deadline."
  }
}
```

</details>

---


### Tool call

_source line 1563 · 2026-05-18T07:01:21.376809+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract all submission guidelines: page limits for long and short papers, template requirements, anonymity/double-blind rules, appendix rules, limitations section requirements, responsible NLP checklist, formatting requirements. Include any desk reject criteria."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/cfp",
    "prompt": "Extract all submission guidelines: page limits for long and short papers, template requirements, anonymity/double-blind rules, appendix rules, limitations section requirements, responsible NLP checklist, formatting requirements. Include any desk reject criteria."
  }
}
```

</details>

---


### Tool result

_source line 1564 · 2026-05-18T07:01:25.846871+00:00_

# EMNLP 2026 Submission Guidelines & Important Dates

## Page Limits
- **Long Papers:** 8 pages (9 pages in camera-ready with reviewer feedback)
- **Short Papers:** 4 pages (5 pages in camera-ready with reviewer feedback)

## Key Submission Requirements
The call references "all of the ARR submission requirements" including:
- Two-way anonymized review instructions
- Authorship documentation
- Citation and comparison guidelines
- Multiple submission, resubmission, and withdrawal policies
- ACL Publication Ethics Policy compliance
- ARR Ethics Policy including "responsible NLP research checklist"
- ACL Disclosure Policy adherence
- Limitations section requirement
- Writing assistance permitted (AI tools allowed)
- Optional supplementary materials, appendices, software, and data

## Anonymity Rules
"The reviewing process will continue to be double-blind. Reviewers will not see authors, nor will authors see reviewers." Reviews remain confidential on ARR, though authors may voluntarily make anonymized submissions publicly visible.

## Critical Important Dates
- **ARR Submission Deadline:** May 25, 2026 (11:59PM UTC-12:00)
- **Reviewer Registration Deadline:** May 27, 2026
- **Author Response Period:** July 7-13, 2026
- **Meta-review Release:** July 30, 2026
- **EMNLP Commitment Deadline:** August 2, 2026
- **Acceptance Notification:** August 20, 2026
- **Camera-ready Due:** September 20, 2026
- **Conference Dates:** October 24-29, 2026

## Template & Citation Details
The document directs authors to ARR's templates and submission platform but doesn't specify particular citation formats or template names.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebFetch",
  "elapsed_ms": 5474
}
```

</details>

---


### Tool result

_source line 1565 · 2026-05-18T07:01:28.459803+00:00_

# ACL Rolling Review Submission Guidelines

## Page Limits

**Long Papers:**
- Up to 8 pages of content
- Unlimited space for limitations section (required) and optional ethical considerations
- Unlimited reference pages

**Short Papers:**
- Up to 4 pages of content
- Unlimited space for limitations section (required) and optional ethical considerations
- Unlimited reference pages

Submissions exceeding length requirements are desk rejected.

## Template & Formatting Requirements

Papers must follow "the official ACL style template" and conform to ACL Author Guidelines. Submissions must adhere to specific restrictions on "paper size, margin width, and font size" or face rejection without review. The style files are available on GitHub and cannot be modified.

## Anonymity Rules (Double-Blind Review)

Papers must exclude author names and affiliations. Authors should avoid self-citations revealing identity (e.g., write "Smith previously showed..." instead of "We previously showed..."). Papers cannot reference non-public materials unavailable to reviewers. Supplementary materials, including repository links, must be anonymized. Cloud services like Dropbox are prohibited due to download tracking. Violations result in desk rejection.

## Appendix Requirements

Appendices follow main content and references, do not count toward page limits, and must maintain two-way anonymization. They should follow double-column formatting per ACLPUB guidelines, with limited exceptions. Key technical contributions must appear in main papers, not appendices—using appendices to circumvent page limits risks desk rejection.

## Limitations Section (Required)

A dedicated "Limitations" section must appear before references and outside the page count. It cannot introduce new methods, analysis, or results. Papers lacking this section face automatic desk rejection.

## Responsible NLP Checklist

Authors must complete this checklist as part of submission. "Incorrect, incomplete or misleading infor
…[truncated 492 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebFetch",
  "elapsed_ms": 7082
}
```

</details>

---


### Tool call

_source line 1566 · 2026-05-18T07:01:34.790919+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1567 · 2026-05-18T07:01:35.243436+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1568 · 2026-05-18T07:01:35.344308+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1569 · 2026-05-18T07:01:35.395009+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'schema-dag-extraction'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1570 · 2026-05-18T07:01:38.267462+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1571 · 2026-05-18T07:01:38.719688+00:00_

1	\begin{abstract}
2	As large language models are increasingly deployed for information extraction without task-specific training, understanding how schema design affects extraction quality becomes critical for reliable deployment. Training-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: having more types (count) and having semantically similar types (confusability). We present the first controlled study isolating these factors across NER, RE, and event detection on four datasets and quantify confusability via the Schema Confusability Score (SCS) and its batch-level aggregation (BCS). Degradation operates along two dimensions: count-related recall decline (up to $-$49\,pp, document-level RE at full schema) dominates confusability-related type substitution (${\approx}\,2.2$\,pp in typical batches); BCS explains 22--53\% of cross-batch RE accuracy variance but not NER, where boundary detection failures overwhelm the signal (confusability operates at the pair level across tasks but aggregates to batch-level predictive power only in RE). Few-shot demonstrations do not reduce the confusability gap (+4.3\,pp under 5-shot). Schema decomposition fails due to merge amplification (NER) and routing failure (RE). Count-related decline (Dimension~1) replicates across model scales (8B to 70B) and architecture families including Gemini 2.5 Flash; confusability effects (Dimension~2) are verified on open-weight models (Qwen, LLaMA).
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1572 · 2026-05-18T07:01:38.770436+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1573 · 2026-05-18T07:01:39.172592+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance. Anonymous review materials: \url{https://anonymous.4open.science/r/schema-dag-extraction}} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 49.5\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near-halving or worse. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \cite{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.
…[truncated 3260 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1574 · 2026-05-18T07:01:39.323702+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1575 · 2026-05-18T07:01:39.525147+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \cite{instructuie-2023}, code-style schema encoding \cite{knowcoder-2024,codeie-2023}, annotation-guided extraction \cite{gollie-2024,adelie-2024}, schema-driven decoding \cite{slot-2025,oneke-2025}, and constrained JSON decoding \cite{json-schema-bench-2025,willard2023efficient}. For NER, methods include zero-shot decomposition \cite{xie-zeroshot-ner-2023,promptner-2023}, distillation \cite{uniner-2024}, and bidirectional encoders \cite{gliner-2024,gliner2-2025}. For RE, recent work examines zero-shot relation triplet extraction via prompting \cite{relationprompt-2022} and revisits relation extraction in the LLM era \cite{wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \cite{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. LLM-PEE's union merge suffers the same precision collapse (0.56$\to$0.21 in NER) that our \S\ref{sec:sdgd} analysis identifies as the fundamental bottleneck. Other approaches address schema complexity via hard negative mining \cite{iepile-2024}, schema definition optimization \cite{parse-2025}, multi-agent debate \cite{crossagentie-2025,cmas-ner-2025}, schema-aware decomposition for event extraction \cite{dee-2024}, and active prompting 
…[truncated 3068 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1576 · 2026-05-18T07:01:39.576000+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 1577 · 2026-05-18T07:01:39.576691+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \cite{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains and is suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \cite{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \cite{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\sim$10 per type) from the DocRED development set and formulate th
…[truncated 8143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1578 · 2026-05-18T07:01:43.352655+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 1579 · 2026-05-18T07:01:44.357534+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	\begin{figure}[t]
10	\centering
11	\begin{minipage}[t]{0.48\columnwidth}
12	\centering
13	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
14	\end{minipage}
15	\hfill
16	\begin{minipage}[t]{0.48\columnwidth}
17	\centering
18	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
19	\end{minipage}
20	\caption{\textbf{(a)} Count-degradation curves for NER and RE. Error bars show $\pm 1$\,SD across 3 seeds (42, 123, 456) $\times$ 25 batches per seed. RE accuracy declines monotonically with count; NER recall exhibits a U-shaped pattern with minimum at intermediate counts. Full-schema points (rightmost, hollow markers) represent the complete type inventory with no batch sampling variance. \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.60$); the wider BCS range available at 80 relations produces larger absolute gaps.}
21	\label{fig:main_results}
22	\end{figure}
23	
24	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}); schema configura
…[truncated 10981 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1580 · 2026-05-18T07:01:44.358110+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---


### Tool result

_source line 1581 · 2026-05-18T07:01:44.810041+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention against confusability-related degradation is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches.
5	
6	\paragraph{NER: merge amplification.}
7	All decomposition modes fall below the single-pass NER baseline (F1\,=\,0.445): SDGD obtains 0.251, random batching 0.320, per-type 0.292 (Appendix~\ref{sec:appendix_sdgd}). The core failure is \emph{merge amplification}: presenting text to the model $k$ times with different type subsets is associated with precision collapse (0.563$\to$0.210--0.249) as false positives scale with $k$, while true positives remain bounded. Confidence gating does not recover net F1. RE avoids this failure because closed-set classification requires no span reconciliation across passes.
8	
9	\paragraph{RE: oracle routing.}
10	Oracle routing achieves 0.802 accuracy versus 0.504 single-pass on FewRel 80-relation RE (+29.8\,pp; Table~\ref{tab:batch_composition}); type separation thus recovers performance absent merge amplification. Confusability-aware grouping yields only +1.4\,pp over random ($p \approx 0.19$, n.s.); all practical routing strategies fall below the single-pass baseline because constrained decoding forces confident predictions in every sub-schema (Appendix~\ref{sec:appendix_routing}).
11	
12	\paragraph{Future directions.}
13	Three avenues may address these bottlenecks: (1)~coarse-to-fine pipelines that screen with the full schema then refine with targeted sub-schemas; (2)~retrieval-based routing using document retrieval rather than LLM confidence for sub-schema assignment; (3)~calibrated generation \citep{jagannatha2020calibrating} to recover confidence signals eliminated by constrained decoding.
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\resi
…[truncated 533 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1582 · 2026-05-18T07:01:44.810541+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1583 · 2026-05-18T07:01:45.314498+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-dimensional decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). The effect generalizes to document-level RE (DocRED slope $-$0.71, adjusted $R^2 = 0.51$, 95\% CI [0.27, 0.73]) and persists across prompt designs (Appendix~\ref{sec:appendix_prompt_sensitivity}). Dimension~1 replicates across scales (8B--70B); Dimension~2 attenuates on smaller models.
6	
7	\paragraph{Why does embedding similarity predict LLM confusion?}
8	SCS captures semantic proximity in LLMs' type-resolution space. The unconditional pairwise $R^2$ is modest (1.3\%); conditional on nonzero confusion (${\sim}11\%$ of pairs), $R^2$ rises to 7\%. Correlated aggregation amplifies this to batch-level $R^2$ of 18--25\% (Monte Carlo simulation, Appendix~\ref{app:aggregation-sim}), consistent with the observed 22--53\% in RE.
9	
10	\paragraph{Task-dependent effects and format dependency.}
11	The batch-level BCS--performance relationship is RE-specific ($R^2 = 0.22$--$0.53$ vs.\ $r \approx 0$ for NER, $n = 450$). RE's constrained decoding (enum constraint) channels all errors into type substitution, so batch confusability directly predicts accuracy; these effect sizes may represent upper bounds specific to the constrained-classification format. NER uses unconstrained generation, where errors scatter across missed entities (43--65\%), boundary misalignment, and hallucinated types, diluting the pairwise signal. We hypothesize the NER U-shape (\S\ref{sec:count_curves}) reflects a dual-task burden: partial schemas require simultaneous span detection and type-membership filtering; at full schema, filtering becomes vacuous and recall recovers.
12	
13	\paragraph{Practical implications.}
14	The bounded count$\times$confusability interaction (0.47\,pp, TOST $p = 0.003$) implies no confusability amplification at scale. For RE, upper-SCS-quartile
…[truncated 1277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 1584 · 2026-05-18T07:01:45.465982+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1585 · 2026-05-18T07:01:45.617234+00:00_

1	\section*{Responsible NLP Research Checklist}
2	
3	For each question, the answer is \textbf{Yes}, \textbf{No}, or \textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.
4	
5	\subsection*{A \quad For Every Submission}
6	
7	\begin{enumerate}[label=\textbf{A\arabic*.},leftmargin=*,itemsep=4pt]
8	
9	\item \textbf{Did you describe the limitations of your work?}
10	
11	Yes. The Limitations section (after \S\ref{sec:conclusion}) discusses single-model reliance, modest pairwise effect sizes, cross-pool slope consistency, factorial interaction tests with TOST equivalence, decomposition scope, and metric scope.
12	
13	\item \textbf{Did you discuss any potential risks of your work?}
14	
15	N/A. This is a purely analytical study of schema-associated degradation in existing LLM IE systems. It does not introduce new models, datasets, or deployment-facing artifacts. The findings characterize failure modes and are intended to inform safer schema design.
16	
17	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
18	
19	Yes. The abstract and \S\ref{sec:introduction} state the two-dimensional degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.
20	
21	\item \textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}
22	
23	Yes. We used Claude (Anthropic) for writing assistance and experimental code development. All scientific claims, experimental designs, and analyses were conducted by the authors.
24	
25	\end{enumerate}
26	
27	\subsection*{B \quad Scientific Artifacts}
28	
29	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=*,itemsep=4pt]
30	
31	\item \textbf{Did you cite the creators of artifacts you used?}
32	
33	Yes. Few-NERD \cite{fewnerd-2021}, FewRel \cite{fewrel-2018}, DocRED \cite{docred-2019}, MAVEN \cite{maven-2020}, Qwen3-32B \cite{qwen3-2025}, Meta-Llama-3.1-70B-Instruct and Meta-Llama-3.1-8B-Instruct \cite{lla
…[truncated 1344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1586 · 2026-05-18T07:01:51.302484+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 1587 · 2026-05-18T07:01:51.754977+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	
11	\title{Supplementary Material for: How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
12	
13	\author{Anonymous}
14	
15	\begin{document}
16	\maketitle
17	
18	All supplementary material is included in the appendix of the main paper.
19	
20	\end{document}
21	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1588 · 2026-05-18T07:01:52.257445+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex",
  "offset": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex",
    "offset": "50"
  }
}
```

</details>

---


### Tool result

_source line 1589 · 2026-05-18T07:01:52.609624+00:00_

50	
51	\item \textbf{Did you report relevant statistics for your dataset(s)?}
52	
53	Yes. \S\ref{sec:datasets} and Table~\ref{tab:datasets} report evaluation set sizes, type counts, and sampling methodology. Count levels and batch sizes are specified in \S\ref{sec:exp_design}.
54	
55	\end{enumerate}
56	
57	\subsection*{C \quad Computational Experiments}
58	
59	\begin{enumerate}[label=\textbf{C\arabic*.},leftmargin=*,itemsep=4pt]
60	
61	\item \textbf{Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?}
62	
63	Yes. \S\ref{sec:model}: Qwen3-32B (32B parameters, FP8), Meta-Llama-3.1-70B-Instruct (70B parameters, FP8), and Meta-Llama-3.1-8B-Instruct (8B parameters). Inference was conducted on NVIDIA RTX PRO 6000 GPUs (96\,GB) served via vLLM. Total compute was approximately 72 GPU-hours of inference (no training).
64	
65	\item \textbf{Did you discuss the experimental setup, including hyperparameter search and best-found values?}
66	
67	Yes. \S\ref{sec:exp_design} describes both experimental paradigms (count curves and BCS-controlled). \S\ref{sec:model} reports decoding parameters (greedy, temperature${}=0$, seed${}=42$) and prompt versions. No hyperparameter search was conducted as this is a zero-shot evaluation study.
68	
69	\item \textbf{Did you report descriptive statistics about your results?}
70	
71	Yes. All key metrics include 95\% bootstrap confidence intervals (10{,}000 resamples, percentile method) as stated in \S\ref{sec:model}. Spearman correlations are reported with $p$-values throughout \S\ref{sec:count_curves}--\ref{sec:centrality_confound}. Permutation tests are used for slope comparisons.
72	
73	\item \textbf{Did you report implementation details, e.g., versions of packages?}
74	
75	Yes. \S\ref{sec:model} specifies vLLM v0.20.2 for model serving. Embedding models are named with version identifiers (\S\ref{sec:scs}). Code and scripts will be released upon acceptance.
76	
77	\end{enumerat
…[truncated 1181 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1590 · 2026-05-18T07:01:52.610142+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
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

_source line 1591 · 2026-05-18T07:01:52.660642+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1592 · 2026-05-18T07:01:55.528934+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "100"
  }
}
```

</details>

---


### Tool result

_source line 1593 · 2026-05-18T07:01:55.982108+00:00_

100	\end{tabular}}
101	\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\approx$51\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\Delta$, in pp) is 77--87\% as large on Llama-3.1-8B as on Qwen3-32B.}
102	\label{tab:cross_model_bcs}
103	\end{table}
104	
105	\begin{table}[h]
106	\centering
107	\small
108	\resizebox{\columnwidth}{!}{%
109	\begin{tabular}{llrrrrrrr}
110	\toprule
111	 & & \multicolumn{5}{c}{\textbf{BCS Bin}} & & \\
112	\cmidrule(lr){3-7}
113	\textbf{Task} & \textbf{Error} & \textbf{Solo} & \textbf{Low} & \textbf{Mid} & \textbf{High} & \textbf{V.High} & \textbf{$\rho$} & \textbf{$p$} \\
114	\midrule
115	NER & IntraSub & 0\% & 1.6\% & 10.6\% & 49.4\% & --- & 1.000 & ${<}0.001$ \\
116	RE  & IntraSub & 0\% & 4.2\% & 13.0\% & 20.3\% & 32.3\% & 0.954 & ${<}\,0.001$ \\
117	\midrule
118	NER & Missed & --- & 42.8\% & 64.8\% & 49.9\% & --- & --- & --- \\
119	RE  & Missed & --- & 10.4\% & 11.3\% & 13.1\% & 15.7\% & --- & --- \\
120	\bottomrule
121	\end{tabular}}
122	\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin, with Spearman $\rho$ computed over $n=154$ individual batches (RE) and $n=148$ batches (NER). NER has 4 BCS bins; RE has 5.}
123	\label{tab:error_taxonomy}
124	\end{table}
125	
126	\section{SDGD Full Protocol and Results}
127	\label{sec:appendix_sdgd}
128	
129	We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union. We compare four modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partition
…[truncated 42470 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1594 · 2026-05-18T07:01:59.001308+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Check project config for external review",
  "subagent_type": "Explore",
  "prompt": "Search for project configuration files for \"schema-dag-extraction\" that might contain external_review or paperreview_ai settings. Look in:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ for any yaml/json config files\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/ for any global config\n\nSearch breadth: medium. Report whether external_review.paperreview_ai.enabled is true or false."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Agent",
  "tool_args": {
    "description": "Check project config for external review",
    "subagent_type": "Explore",
    "prompt": "Search for project configuration files for \"schema-dag-extraction\" that might contain external_review or paperreview_ai settings. Look in:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ for any yaml/json config files\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/ for any global config\n\nSearch breadth: medium. Report whether external_review.paperreview_ai.enabled is true or false."
  }
}
```

</details>

---


### Tool call

_source line 1595 · 2026-05-18T07:01:59.303041+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1596 · 2026-05-18T07:01:59.354086+00:00_

1	\lstset{
2	  basicstyle=\ttfamily\small,
3	  breaklines=true,
4	  breakatwhitespace=true,
5	  columns=fullflexible
6	}
7	
8	\section{Prompt Templates}
9	\label{sec:appendix_prompts}
10	
11	This appendix reproduces the complete prompt templates used for all three extraction tasks.
12	All prompts are injected into a single \texttt{user} message (no system prompt); the model's chat template adds the system/assistant framing.
13	Both versions provide a JSON-formatted type schema to the vLLM constrained-decoding engine; the schema is \emph{not} included in the natural-language prompt itself.
14	We use greedy decoding (\texttt{temperature=0}, \texttt{seed=42}) throughout.
15	
16	\medskip\noindent
17	\textbf{Notation.}
18	Placeholders are shown in \texttt{\{braces\}}.
19	Text \textbf{added in v2} (relative to v1) is marked with $\triangleright$.
20	Text \textbf{removed in v2} is marked with \sout{strikethrough}.
21	
22	\subsection{Named Entity Recognition (Few-NERD)}
23	
24	\paragraph{v1 prompt (with character offsets).}
25	
26	\begin{small}
27	\begin{lstlisting}
28	Extract all named entities from the following text.
29	Only extract entities of the following types:
30	- {type_1}: {definition_1}
31	- {type_2}: {definition_2}
32	  ...
33	
34	Text: {input_text}
35	
36	Output as JSON: [{"text": "...", "type": "...",
37	                  "start": ..., "end": ...}]
38	\end{lstlisting}
39	\end{small}
40	
41	\noindent
42	\textbf{v1 constrained-decoding schema:}
43	\begin{small}
44	\begin{lstlisting}
45	{"type": "array",
46	 "items": {"type": "object",
47	   "properties": {
48	     "text":  {"type": "string"},
49	     "type":  {"type": "string",
50	               "enum": [&lt;sorted_types>]},

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1597 · 2026-05-18T07:02:00.913860+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/**/*.{yaml,yml,json}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/**/*.{yaml,yml,json}"
  }
}
```

</details>

---


### Tool result

_source line 1598 · 2026-05-18T07:02:00.964731+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/checkpoints/exp001_count_baseline_PREPARING_20260514T161340.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/checkpoints/exp002_confusability_controlled_PREPARING_20260514T161342.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_code_mvp-pipeline_20260514T161549_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_code_fix-reviewer-critical_20260514T163331_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/configs/few_nerd_types.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_ssh_env-setup-and-data_20260514T163452_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_ssh_env-setup_20260514T161431_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_ssh_code-preflight_20260514T173030_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_code_fix-few-nerd-loader_20260514T173444_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_ssh_rollback-and-run-all_20260514T184153_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/checkpoints/exp001_count_baseline_PENDING_20260514T193801.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/checkpoints/exp001_count_baseline_QUEUED_20260514T193805.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/checkpoints/exp001_count_baseline_ALLOCATED_20260514T193808.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/checkpoints/exp001_count_baseline_R
…[truncated 12753 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1599 · 2026-05-18T07:02:01.065680+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/*.{yaml,yml,json}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/*.{yaml,yml,json}"
  }
}
```

</details>

---


### Tool result

_source line 1600 · 2026-05-18T07:02:01.317561+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/workspace.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_no_project.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_director.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_reviewer.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/checkpoints/mvp_pilot_PREPARING_20260512T090500.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_worker_ddf919c12f9233b9c1be7884efc37bb6.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/checkpoints/mvp_pilot_QUEUED_20260512T103215.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/checkpoints/mvp_pilot_ALLOCATED_20260512T105446.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_worker_0aa51d591547913249ab7a68dc681be8.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/logs/workers/worker_fix_install_tmux_20260512T105529_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/checkpoints/mvp_pilot_RUNNING_20260512T105712.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_config_worker_943f40256720b8f6634ec1980a24acc1.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/logs/workers/worker_code_pi_controller_20260512T110004_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/checkpoints/mvp_pilot_RUNNING_20260512T112133.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/checkpoints/mvp_pilot_DONE_20260512T112136.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/mcp_confi
…[truncated 11708 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1601 · 2026-05-18T07:02:01.370051+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -maxdepth 2 -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" -o -name \"config*\" -o -name \"settings*\" \\)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -maxdepth 2 -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" -o -name \"config*\" -o -name \"settings*\" \\)"
  }
}
```

</details>

---


### Tool result

_source line 1602 · 2026-05-18T07:02:01.571198+00:00_

&lt;persisted-output>
Output too large (46.6KB). Full output saved to: /home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction--claude-sessions-review-director-338aa0a5/d5679aae-14e1-4f01-984e-8846189e3262/tool-results/byquvbeu8.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/scripts/test_types.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/checkpoints/exp001_count_baseline_DONE_20260515T050646.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/checkpoints/exp012_llama_8b_fewnerd_PREPARING_20260515T162610.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/checkpoints/exp012_llama_8b_r2_DONE_20260515T194807.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/checkpoints/exp001_count_baseline_PENDING_20260514T193801.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/checkpoints/exp_fewrel_40rel_r3_PENDING_20260515T165726.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/checkpoints/exp017_gpt4o_mini_fewrel_PREPARING_20260516T065708.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/checkpoints/exp_fewrel_contamination_check_PR
…[truncated 332 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1603 · 2026-05-18T07:02:03.934053+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/registry.yaml"
  }
}
```

</details>

---


### Tool call

_source line 1604 · 2026-05-18T07:02:04.087229+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/backend.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/backend.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1605 · 2026-05-18T07:02:04.338818+00:00_

File content (40258 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 404
}
```

</details>

---


### Tool result

_source line 1606 · 2026-05-18T07:02:04.339631+00:00_

1	manager:
2	  enabled: true
3	  url: http://172.31.31.59:8700
4	  my_id: be-prod9-0512
5	  my_token: 48d731d4ffca61bec8a11c3919f9bf537a2999bc36e98c14fb7d1577b327534e
6	  ingest_token: e1dc1e287cb57d2e8411481f152c3cfb22d694b1bc8043b04a543cc7f0e08b82
7	  api:
8	    listen_host: 0.0.0.0
9	    listen_port: 8420
10	    allowed_source_cidrs:
11	    - 10.0.0.0/8
12	    - 192.168.0.0/16
13	    - 172.16.0.0/12
14	    - 127.0.0.0/8
15	  capabilities:
16	    read: true
17	    bootstrap_project: true
18	    archive_project: true
19	    allocate_gpus: true
20	    release_gpus: true
21	    read_chat_history: true
22	    claude_account_login: true
23	    read_claude_pool: true
24	  local_approvals:
25	    bootstrap_project: false
26	    archive_project: false
27	    allocate_gpus: false
28	  heartbeat:
29	    enabled: true
30	    interval_sec: 60
31	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 1607 · 2026-05-18T07:02:04.390479+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ | grep -E \"yaml|json|config\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ | grep -E \"yaml|json|config\""
  }
}
```

</details>

---


### Tool result

_source line 1608 · 2026-05-18T07:02:04.441180+00:00_

drwxr-xr-x  2 ubuntu ubuntu   4096 May 17 16:07 configs
-rw-------  1 ubuntu ubuntu    411 May 16 02:39 constraints.yaml
-rw-------  1 ubuntu ubuntu  48861 May 18 02:47 decisions.yaml
-rw-------  1 ubuntu ubuntu   3545 May 16 08:23 dream_registry.yaml
-rw-r--r--  1 ubuntu ubuntu   3550 May 16 08:23 dream_registry.yaml.bak
-rw-------  1 ubuntu ubuntu   5379 May 15 17:09 experiment_plan.yaml
-rw-r--r--  1 ubuntu ubuntu  19038 May 15 07:59 literature_map.yaml
-rw-------  1 ubuntu ubuntu   6211 May 17 16:23 mistakes.yaml
-rw-------  1 ubuntu ubuntu  22206 May 16 04:06 paper_provenance.yaml
-rw-------  1 ubuntu ubuntu 108313 May 18 06:44 registry.yaml
-rw-r--r--  1 ubuntu ubuntu  22363 May 15 16:26 writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1609 · 2026-05-18T07:02:06.704622+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai|paperreview|external.*review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai|paperreview|external.*review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
  }
}
```

</details>

---


### Tool call

_source line 1610 · 2026-05-18T07:02:06.906541+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai|paperreview|external.*review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai|paperreview|external.*review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config"
  }
}
```

</details>

---


### Tool result

_source line 1611 · 2026-05-18T07:02:07.210008+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "elapsed_ms": 303
}
```

</details>

---


### Tool result

_source line 1612 · 2026-05-18T07:02:07.261727+00:00_

Found 33 files
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/chats/feishu_group_oc_ac7ab7270b6b5caecee04f89b11aab3e_director.jsonl
AGENTS.md
CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/chats/feishu_group_oc_51326259fe46fbae9da26b81cf03f1f8_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_15.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/chats/feishu_group_oc_ac7ab7270b6b5caecee04f89b11aab3e_reviewer_2.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/chats/feishu_group_oc_ac7ab7270b6b5caecee04f89b11aab3e_reviewer_1.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_14.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_13.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/data/fewrel/val_wiki.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/data/fewrel/train_wiki.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_research_missing_references_mr1_4_20260517T145447.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_12.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/workers/worker_code_exp_fewshot_bcs_mitigation_20260517T115312.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_reports/round_11.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/logs/chats/archive/feishu_group_oc_51326259fe46fbae9da26b81cf03f1f8_director_20260517T074950_564926.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/p
…[truncated 2370 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "elapsed_ms": 557
}
```

</details>

---


### Tool call

_source line 1613 · 2026-05-18T07:02:09.523409+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/registry.yaml",
  "output_mode": "content",
  "context": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/registry.yaml",
    "output_mode": "content",
    "context": "5"
  }
}
```

</details>

---


### Tool result

_source line 1614 · 2026-05-18T07:02:09.523885+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1615 · 2026-05-18T07:02:11.384901+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"external\\|paperreview\\|review_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/registry.yaml | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"external\\|paperreview\\|review_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/registry.yaml | head -30"
  }
}
```

</details>

---


### Tool result

_source line 1616 · 2026-05-18T07:02:11.536336+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1617 · 2026-05-18T07:02:11.536777+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/approvals.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/approvals.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1618 · 2026-05-18T07:02:11.587318+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1619 · 2026-05-18T07:02:13.244720+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/workspace.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/workspace.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1620 · 2026-05-18T07:02:13.295443+00:00_

1	projects: {}
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1621 · 2026-05-18T07:02:13.296077+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/approvals.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/approvals.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1622 · 2026-05-18T07:02:13.296641+00:00_

1	# 审批类型注册表
2	# 此文件位于 WORKSPACE_ROOT/config/approvals.yaml
3	# hook 名由 Python (core/approvals/hooks.py) 绑定，不在此文件里定义
4	
5	approval_types:
6	
7	  experiment:
8	    display_name: "实验审批"
9	    description: "高风险实验变更，需要人工审批后才能提交训练"
10	    always_require: false
11	    auto_approve_rule: "all_not_high"   # 枚举：all_low | all_not_high | always | never
12	    risk_dimensions:
13	      - name: gpu_hours
14	        label: "GPU 时长（小时）"
15	        type: numeric
16	        thresholds: { low: 2.0, medium: 8.0 }
17	        hard_limit: 4.0            # 超过直接触发审批，无视其他维度
18	      - name: change_scope
19	        label: "代码变更文件数"
20	        type: numeric
21	        thresholds: { low: 1, medium: 3 }
22	      - name: history_success
23	        label: "历史成功次数"
24	        type: numeric
25	        thresholds: { low: 2, medium: 1 }   # 0 次 → medium（不再是 high）
26	        invert: true                         # 数值越大风险越低
27	    pending_timeout_hours: 48
28	
29	  worker:
30	    display_name: "Worker 任务审批"
31	    description: "高风险后台任务需要确认后才启动"
32	    always_require: false
33	    auto_approve_rule: "all_low"
34	    risk_dimensions:
35	      - name: task_type
36	        label: "任务类型"
37	        type: enum
38	        high_values: ["code_rewrite", "bulk_delete"]
39	        medium_values: ["code_modify"]
40	        low_values: ["doc_gen", "analysis", "exploration"]
41	      - name: file_scope
42	        label: "涉及文件数"
43	        type: numeric
44	        thresholds: { low: 3, medium: 10 }
45	    pending_timeout_hours: 24
46	
47	  deployment:
48	    display_name: "部署审批"
49	    description: "生产部署不可逆，必须人工确认"
50	    always_require: true
51	    auto_approve_rule: "never"
52	    risk_dimensions:
53	      - name: service_tier
54	        label: "服务等级"
55	        type: enum
56	        high_values: ["production"]
57	        medium_values: ["staging"]
58	        low_values: ["dev"]
59	    pending_timeout_hours: 24
60	
61	  submission:
62	    display_name: "投稿审批"
63	    description: "Director 提交审稿请求后，发卡片到 A 群让用户选择审稿模式（co
…[truncated 626 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1623 · 2026-05-18T07:02:15.863178+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"external_review\\|paperreview\\|review_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/decisions.yaml | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"external_review\\|paperreview\\|review_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/decisions.yaml | head -30"
  }
}
```

</details>

---


### Tool result

_source line 1624 · 2026-05-18T07:02:15.913893+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1625 · 2026-05-18T07:02:19.332207+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -maxdepth 1 -name \"*config*\" -o -name \"*project.yaml*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -maxdepth 1 -name \"*config*\" -o -name \"*project.yaml*\""
  }
}
```

</details>

---


### Tool result

_source line 1626 · 2026-05-18T07:02:19.483701+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/configs

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1627 · 2026-05-18T07:02:19.537089+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/ 2>/dev/null || echo \"No .claude directory\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/ 2>/dev/null || echo \"No .claude directory\""
  }
}
```

</details>

---


### Tool result

_source line 1628 · 2026-05-18T07:02:19.592765+00:00_

total 32
drwxr-xr-x  3 ubuntu ubuntu  4096 May 14 16:07 .
drwxr-xr-x 14 ubuntu ubuntu  4096 May 18 06:46 ..
-rw-r--r--  1 ubuntu ubuntu 16395 May 18 07:00 CLAUDE.md
drwxr-xr-x 18 ubuntu ubuntu  4096 May 17 14:03 sessions

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 55
}
```

</details>

---


### Tool call

_source line 1629 · 2026-05-18T07:02:21.754061+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview|review_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/CLAUDE.md",
  "output_mode": "content",
  "context": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview|review_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/CLAUDE.md",
    "output_mode": "content",
    "context": "3"
  }
}
```

</details>

---


### Tool result

_source line 1630 · 2026-05-18T07:02:21.804757+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1631 · 2026-05-18T07:02:23.835813+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/ | grep -v worker | grep -v mcp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/ | grep -v worker | grep -v mcp"
  }
}
```

</details>

---


### Tool result

_source line 1632 · 2026-05-18T07:02:23.887533+00:00_

total 268
drwxrwxr-x 5 ubuntu ubuntu 4096 May 17 15:06 .
drwxrwxr-x 9 ubuntu ubuntu 4096 May 12 08:37 ..
-rw-rw-r-- 1 ubuntu ubuntu 2901 May  9 09:00 approvals.yaml
-rw------- 1 ubuntu ubuntu  764 May 11 17:59 backend.yaml
-rw-r--r-- 1 ubuntu ubuntu 1855 May 18 07:00 claude_sessions.json
-rw------- 1 ubuntu ubuntu 9357 May 17 14:03 crons.yaml
-rw------- 1 ubuntu ubuntu  364 May 15 04:13 email_tokens.json
-rw------- 1 ubuntu ubuntu  104 May 15 09:17 feishu.yaml
-rw-r--r-- 1 ubuntu ubuntu 4656 May 18 06:43 keepalive.json
-rw-rw-r-- 1 ubuntu ubuntu   51 May 13 17:02 pool.json
drwxrwxr-x 2 ubuntu ubuntu 4096 May 17 08:28 projects
-rw-r--r-- 1 ubuntu ubuntu 1521 May 17 15:11 resources.yaml
drwxr-xr-x 3 ubuntu ubuntu 4096 May 16 05:12 secrets
-rw-r--r-- 1 ubuntu ubuntu  720 May 18 07:00 session_state.json
-rw-r--r-- 1 ubuntu ubuntu  141 May 16 05:11 tum_pending_tum_20260516_openai_exp017.json
-rw-r--r-- 1 ubuntu ubuntu  147 May 17 14:57 tum_pending_tum_20260517_gemini_flash.json
-rw-r--r-- 1 ubuntu ubuntu   92 May 17 12:02 venue_registry.yaml
drwxr-xr-x 2 ubuntu ubuntu 4096 May 17 12:02 venue_rules

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1633 · 2026-05-18T07:02:25.494349+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/"
  }
}
```

</details>

---


### Tool result

_source line 1634 · 2026-05-18T07:02:25.545016+00:00_

total 16
drwxrwxr-x 2 ubuntu ubuntu 4096 May 17 08:28 .
drwxrwxr-x 5 ubuntu ubuntu 4096 May 17 15:06 ..
-rw-r--r-- 1 ubuntu ubuntu  508 May 14 15:55 collapse-aware-mixing.yaml
-rw-r--r-- 1 ubuntu ubuntu  753 May 18 07:00 schema-dag-extraction.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1635 · 2026-05-18T07:02:27.403713+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/schema-dag-extraction.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/schema-dag-extraction.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1636 · 2026-05-18T07:02:27.404342+00:00_

1	execution:
2	  project_path: /root/schema-dag-extraction
3	  servers:
4	  - account: root
5	    server: cqa1-38874
6	  - account: root
7	    server: westd-24295
8	feishu:
9	  chat_id: oc_51326259fe46fbae9da26b81cf03f1f8
10	  operational_chat_id: oc_04544c3b7bc497e1d098ba47fb56a6c2
11	  review_paper_path: projects/schema-dag-extraction/docs/paper/main.tex
12	  review_round: 16
13	  review_supplementary_paths: ''
14	  submission_chat_id: oc_ac7ab7270b6b5caecee04f89b11aab3e
15	project:
16	  created_at: '2026-05-14T16:07:46.825Z'
17	  description: Does Type Confusability Drive Schema-Induced Degradation in LLM Information
18	    Extraction? An Empirical Study and Principled Decomposition Framework
19	  name: schema-dag-extraction
20	  phase: research
21	  source_idea_id: idea_007
22	venue: emnlp-2026
23	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1637 · 2026-05-18T07:02:29.714076+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/ --include=\"*.yaml\" --include=\"*.json\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/ --include=\"*.yaml\" --include=\"*.json\" 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 1638 · 2026-05-18T07:02:29.966581+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 1639 · 2026-05-18T07:02:31.827521+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -name \"settings.json\" -o -name \"config.json\" | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -name \"settings.json\" -o -name \"config.json\" | head -10"
  }
}
```

</details>

---


### Tool result

_source line 1640 · 2026-05-18T07:02:31.882730+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 55
}
```

</details>

---


### Tool call

_source line 1641 · 2026-05-18T07:02:33.691032+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -200 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/registry.yaml | tail -100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "head -200 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/registry.yaml | tail -100"
  }
}
```

</details>

---


### Tool result

_source line 1642 · 2026-05-18T07:02:33.791994+00:00_

      gpu: cuda:0
      pid: 197321
    log_path: /root/schema-dag-extraction/logs/exp2.log
    metrics:
      data_source: exp2_reeval_results.json (text_match, CLEAN)
      primary_recall_vs_bcs:
        count_6:
          r: 0.2754
          p: 0.1644
          n: 27
          verdict: FAIL
        count_12:
          r: 0.2219
          p: 0.266
          n: 27
          verdict: FAIL
        partial:
          r: 0.2522
          p: 0.0658
          n: 54
          verdict: FAIL
      secondary_f1_vs_bcs:
        count_6:
          r: 0.1754
          p: 0.3814
          n: 27
          verdict: FAIL
        count_12:
          r: 0.5012
          p: 0.0077
          n: 27
          verdict: PASS
        partial:
          r: 0.3025
          p: 0.0262
          n: 54
          verdict: PASS
      mechanistic_confusion_rate:
        random_batches:
          count_6_high: 0.0157
          count_6_low: 0.0088
          ratio_6: 1.7
          count_12_high: 0.0304
          count_12_low: 0.0131
          ratio_12: 2.4
        extreme_batches:
          count_6_high: 0.0728
          count_6_low: 0.0014
          ratio_6: 27.5
          count_12_high: 0.048
          count_12_low: 0.0061
          ratio_12: 9.9
        verdict: PASS
      pairwise_confusion_analysis:
        all:
          n_pairs: 1953
          pearson_r: 0.156
          pearson_p: 4.6e-12
          spearman_rho: 0.16
          spearman_p: 1.3e-12
        count_6:
          n_pairs: 1770
          pearson_r: 0.078
          pearson_p: 0.001
        count_12:
          n_pairs: 1953
          pearson_r: 0.147
          pearson_p: 6.7e-11
        nonzero_only:
          all_spearman_rho: 0.254
          all_spearman_p: 1.1e-06
          count_12_pearson_r: 0.212
          count_12_p: 0.00034
        top_confused_pair: person-other <-> person-politician (BCS=0.934, confusion=156)
      per_type_analysis:
        n_types: 63
        filter: freq>=5
        micro_f1_vs_bcs:
          pearson_r: -0.18
…[truncated 636 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1643 · 2026-05-18T07:02:36.253521+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"enabled.*true\\|enabled.*false\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/ --include=\"*.yaml\" --include=\"*.json\" 2>/dev/null | grep -i \"review\\|paperreview\\|external\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"enabled.*true\\|enabled.*false\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/ --include=\"*.yaml\" --include=\"*.json\" 2>/dev/null | grep -i \"review\\|paperreview\\|external\""
  }
}
```

</details>

---


### Tool result

_source line 1644 · 2026-05-18T07:02:36.304232+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1645 · 2026-05-18T07:02:37.610383+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/crons.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/crons.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1646 · 2026-05-18T07:02:37.661202+00:00_

1	active_crons: []
2	completed_crons:
3	- chat_id: null
4	  completed_at: '2026-05-12T14:53:02Z'
5	  created_at: '2026-05-12T14:47:01.196Z'
6	  exp_id: mvp_pilot_v4
7	  hooks: null
8	  interval_seconds: 120
9	  last_checked: '2026-05-12T14:51:01.197Z'
10	  log_path: ~/runs/collapse-aware-mixing/mvp_pilot_v4.log
11	  pid: mvp_pilot_v4
12	  project: collapse-aware-mixing
13	  server: cqa1-38874
14	  status: completed
15	  tracked_metrics: null
16	  wandb_run_id: null
17	- chat_id: null
18	  completed_at: '2026-05-12T15:23:20Z'
19	  created_at: '2026-05-12T14:54:35.794Z'
20	  exp_id: mvp_pilot_v4
21	  hooks: null
22	  interval_seconds: 120
23	  last_checked: '2026-05-12T15:21:18.314Z'
24	  log_path: /tmp/pilot_v4.log
25	  pid: '28147'
26	  project: collapse-aware-mixing
27	  server: cqa1-38874
28	  status: completed
29	  tracked_metrics: null
30	  wandb_run_id: null
31	- chat_id: null
32	  completed_at: '2026-05-13T02:22:16Z'
33	  created_at: '2026-05-12T16:05:26.014Z'
34	  exp_id: mvp_pilot_v5
35	  hooks: null
36	  interval_seconds: 120
37	  last_checked: '2026-05-13T02:19:59.330Z'
38	  log_path: ~/runs/collapse-aware-mixing/mvp_pilot_v5.log
39	  pid: '32154'
40	  project: collapse-aware-mixing
41	  server: cqa1-38874
42	  status: completed
43	  tracked_metrics: null
44	  wandb_run_id: null
45	- chat_id: null
46	  completed_at: '2026-05-13T17:42:39Z'
47	  created_at: '2026-05-13T03:50:14.008Z'
48	  exp_id: mvp_pilot_v7
49	  hooks: null
50	  interval_seconds: 1800
51	  last_checked: '2026-05-13T17:12:18.208Z'
52	  log_path: /root/autodl-tmp/pilot_v7.log
53	  pid: '60104'
54	  project: collapse-aware-mixing
55	  server: cqa1-38874
56	  status: completed
57	  tracked_metrics: null
58	  wandb_run_id: null
59	- chat_id: null
60	  completed_at: '2026-05-14T15:55:18Z'
61	  created_at: '2026-05-14T05:46:42.474Z'
62	  exp_id: mvp_seed0_replication_r2
63	  hooks: null
64	  interval_seconds: 300
65	  last_checked: '2026-05-14T15:50:57.499Z'
66	  log_path: null
67	  pid: '122208'
…[truncated 8605 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---
