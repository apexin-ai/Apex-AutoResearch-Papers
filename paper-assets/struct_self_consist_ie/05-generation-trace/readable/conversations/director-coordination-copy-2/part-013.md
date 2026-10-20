# Director coordination — Part 13 of 16

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

[← Part 12](part-012.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 14 →](part-014.md) · [Structured JSON](../../../sessions/6a/6a5a1a2f9a2bf6bdf404.json)

## Round 286

### Tool result

_source line 3861 · 2026-05-22T10:55:11.673912+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml\", \"content\": \"_next_id: 240\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:23 UTC\\n  summary: 'MVP 方案: ACE05 上验证 structural consistency vs Fleiss'' Kappa 的 correlation\\n    差异'\\n  rationale: 'PMC12888769 用 surface-level Fleiss'' Kappa 在 zero-shot 模型上得到 ρ=0.20-0.28，我们假设\\n    fine-tuned 模型 + structural consistency (soft Jaccard) 能达到 ρ≥0.40。这是整个论文的基础假设——如果\\n    structural consistency 不能更好地预测准确率，后续的 adaptive gating 无从谈起。Phase 0 pilot 设计: Qwen3-8B\\n    fine-tuned on ACE05, N=8 samples, 200 instances, 对比两种 consistency metric 的 Spearman\\n    ρ。Pass ≥0.40, Fail <0.30。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 04:27 UTC\\n  summary: 采纳 Reviewer 审查意见，收紧 MVP pass/fail 标准\\n  rationale: 'Reviewer 指出 5 个问题，全部合理采纳：(1) PASS 必须要求 EAE (high-headroom subtask) ρ≥0.40，仅\\n    NER 通过不够（ceiling effect 可能虚高）；(2) MARGINAL 区间加 time-boxed protocol: N=16 追加 +\\n    1天上限；(3) 加 fine-tuning 质量门控 (NER≥73, EAE≥45)，模型不行时先修 fine-tuning；(4) ACE05 今天必须确认；(5)\\n    监控 T=1.0 per-sample F1 分布，>30% F1=0 时追加 T=0.7。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 04:53 UTC\\n  summary: SciERC RE 替代 ACE05 EAE 作为 MVP high-headroom subtask\\n  rationale: ACE05 需 LDC 许可，用户未确认。SciERC 公开可得，有 NER+RE 两个 subtask。RE base F1 ~47（与\\n    ACE05 EAE ~52 相当），结构复杂度高（entity pair + relation type），headroom 大，是 EAE 的合理替代。PASS\\n    标准更新为 RE ρ≥0.40。需要补实现 RE 的 consistency + evaluation + pipeline 支持。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:38 UTC\\n  summary: 'Gate 0: NER PASS (60.4%), RE FAIL (33.8%). 执行方案 C——当前模型先跑 pilot + 追训改进版，需修复\\n    RE evaluation'\\n  rationale: RE 33.8% 低于 40% 阈值但不阻塞 pilot：(1) headroom 大，oracle best-of-N 有提升空间；(2)\\n    consistency correlation 不要求高绝对 F1，要求 per-instance variance；(3) 弱模型上验证假设结论更强。但\\n    Reviewer 发
…[truncated 10901 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 3862 · 2026-05-22T10:55:11.875317+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 3863 · 2026-05-22T10:55:11.925968+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3864 · 2026-05-22T10:55:37.513266+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "struct_self_consist_ie",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 3865 · 2026-05-22T10:55:57.291287+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 19778
}
```

</details>

---


### Tool call

_source line 3866 · 2026-05-22T10:55:57.414329+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验有效性**。\n\n## Venue 信息\n- **目标 venue**: EMNLP 2026 (Long Paper, via ACL Rolling Review)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页（ACL 模板双栏），参考文献不限。Limitations 和 Ethics Statement 不计入页数（前提是不含过多额外内容）。\n- **匿名规则**: Double-blind\n- **模板**: ACL 2026（`\\usepackage[review]{acl}`）\n- **附录**: 允许，Reviewer 可参考但不要求阅读\n- **ARR Responsible NLP Checklist**: 应在 OpenReview 提交表单中填写，而非放在论文 PDF 中\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_36/submitted.pdf`\n\n## 你的审查侧重\n\n**方法严谨性：**\n- Diagnostic cascade（degeneracy → oracle headroom → LP compression → signal alignment）的逻辑链是否完整？各阶段的因果/相关关系是否清晰区分？\n- Proposition 1（entity independence 假设）的理论分析是否合理？bound 的松紧程度是否诚实讨论？\n- 统计分析质量：多重比较校正（Holm-Bonferroni k=57, BH FDR）是否恰当？bootstrap CI、paired bootstrap p-values 的使用是否正确？\n- Degeneracy decomposition bound 的实际诊断价值 vs 理论 tightness\n\n**实验有效性：**\n- 4 个 NER 数据集 + RE exploratory 的实验覆盖是否足以支撑 claims？\n- 2 个模型家族（Qwen3-8B, LLaMA-3.1-8B）+ 4B/14B/72B ablation 的 scale 覆盖是否充分？\n- seed 数量和统计 power（特别是 SciERC n=529, 单/双 seed 的部分）\n- 9 个方法类别的 baseline 覆盖是否完整？是否有遗漏的重要 baseline？\n- N-scaling 实验（N=2 到 64）的设计合理性\n- Free-form decoding ablation 的覆盖范围\n- 格式检查：正文是否在 8 页内？Checklist 是否应移出 PDF？\n\n请按 ARR 审稿标准给出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验有效性**。\n\n## Venue 信息\n- **目标 venue**: EMNLP 2026 (Long Paper, via ACL Rolling Review)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页（ACL 模板双栏），参考文献不限。Limitations 和 Ethics Statement 不计入页数（前提是不含过多额外内容）。\n- **匿名规则**: Double-blind\n- **模板**: ACL 2026（`\\usepackage[review]{acl}`）\n- **附录**: 允许，Reviewer 可参考但不要求阅读\n- **ARR Responsible NLP Checklist**: 应在 OpenReview 提交表单中填写，而非放在论文 PDF 中\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_36/submitted.pdf`\n\n## 你的审查侧重\n\n**方法严谨性：**\n- Diagnostic cascade（degeneracy → oracle headroom → LP compression → signal alignment）的逻辑链是否完整？各阶段的因果/相关关系是否清晰区分？\n- Proposition 1（entity independence 假设）的理论分析是否合理？bound 的松紧程度是否诚实讨论？\n- 统计分析质量：多重比较校正（Holm-Bonferroni k=57, BH FDR）是否恰当？bootstrap CI、paired bootstrap p-values 的使用是否正确？\n- Degeneracy decomposition bound 的实际诊断价值 vs 理论 tightness\n\n**实验有效性：**\n- 4 个 NER 数据集 + RE exploratory 的实验覆盖是否足以支撑 claims？\n- 2 个模型家族（Qwen3-8B, LLaMA-3.1-8B）+ 4B/14B/72B ablation 的 scale 覆盖是否充分？\n- seed 数量和统计 power（特别是 SciERC n=529, 单/双 seed 的部分）\n- 9 个方法类别的 baseline 覆盖是否完整？是否有遗漏的重要 baseline？\n- N-scaling 实验（N=2 到 64）的设计合理性\n- Free-form decoding ablation 的覆盖范围\n- 格式检查：正文是否在 8 页内？Checklist 是否应移出 PDF？\n\n请按 ARR 审稿标准给出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。"
  }
}
```

</details>

---


### Tool result

_source line 3867 · 2026-05-22T10:56:12.168924+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 14754
}
```

</details>

---


### Tool call

_source line 3868 · 2026-05-22T10:56:12.319923+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## Venue 信息\n- **目标 venue**: EMNLP 2026 (Long Paper, via ACL Rolling Review)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页（ACL 模板双栏），参考文献不限。Limitations 和 Ethics Statement 不计入页数（前提是不含过多额外内容）。\n- **匿名规则**: Double-blind\n- **模板**: ACL 2026（`\\usepackage[review]{acl}`）\n- **附录**: 允许，Reviewer 可参考但不要求阅读\n- **ARR Responsible NLP Checklist**: 应在 OpenReview 提交表单中填写，而非放在论文 PDF 中\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_36/submitted.pdf`\n\n## 你的审查侧重\n\n**新颖性：**\n- 相对于 Yao & Zhang (2026 consistency for IE)、Yun & Price (2025 diversity collapse)、Chen et al. (2023 SC failures)、Xie et al. (2023 zero-shot entity voting) 的增量贡献是否足够？\n- \"Correlation-selection gap\" 作为核心发现是否真正新颖，还是已知现象的重新包装？\n- Diagnostic cascade 作为方法贡献的新颖性——是否只是将已知因素串联？\n- Capability-diversity tension 的原创性和证据充分性\n- Entity-level construction 与已有 MBR decoding / entity voting 的差异\n\n**完整性：**\n- Scope claims 是否与证据匹配？标题 \"Information Extraction\" 但主要是 NER，RE/SQL 仅 exploratory\n- Related work 覆盖是否充分？特别是 conformal prediction、token-level uncertainty、MBR with entity-level F1、trained verifiers 领域\n- 论文结构是否合理？各 section 的逻辑流是否清晰？\n- Limitations section 的覆盖是否恰当且简洁（EMNLP 规则：3 个点左右即可）\n- Ethics statement 的完整性\n\n**写作质量：**\n- 行文清晰度、术语一致性\n- Figure/Table 的信息密度和可读性\n- Abstract 和 Introduction 的 claim 是否与正文证据一致\n- 符号和记法的一致性\n- 是否有 AI 生成痕迹或不自然的措辞\n- Checklist section 是否应从 PDF 移除（ARR 规定在 OpenReview 表单中填写）\n\n请按 ARR 审稿标准给出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。\n\n## Venue 信息\n- **目标 venue**: EMNLP 2026 (Long Paper, via ACL Rolling Review)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页（ACL 模板双栏），参考文献不限。Limitations 和 Ethics Statement 不计入页数（前提是不含过多额外内容）。\n- **匿名规则**: Double-blind\n- **模板**: ACL 2026（`\\usepackage[review]{acl}`）\n- **附录**: 允许，Reviewer 可参考但不要求阅读\n- **ARR Responsible NLP Checklist**: 应在 OpenReview 提交表单中填写，而非放在论文 PDF 中\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_36/submitted.pdf`\n\n## 你的审查侧重\n\n**新颖性：**\n- 相对于 Yao & Zhang (2026 consistency for IE)、Yun & Price (2025 diversity collapse)、Chen et al. (2023 SC failures)、Xie et al. (2023 zero-shot entity voting) 的增量贡献是否足够？\n- \"Correlation-selection gap\" 作为核心发现是否真正新颖，还是已知现象的重新包装？\n- Diagnostic cascade 作为方法贡献的新颖性——是否只是将已知因素串联？\n- Capability-diversity tension 的原创性和证据充分性\n- Entity-level construction 与已有 MBR decoding / entity voting 的差异\n\n**完整性：**\n- Scope claims 是否与证据匹配？标题 \"Information Extraction\" 但主要是 NER，RE/SQL 仅 exploratory\n- Related work 覆盖是否充分？特别是 conformal prediction、token-level uncertainty、MBR with entity-level F1、trained verifiers 领域\n- 论文结构是否合理？各 section 的逻辑流是否清晰？\n- Limitations section 的覆盖是否恰当且简洁（EMNLP 规则：3 个点左右即可）\n- Ethics statement 的完整性\n\n**写作质量：**\n- 行文清晰度、术语一致性\n- Figure/Table 的信息密度和可读性\n- Abstract 和 Introduction 的 claim 是否与正文证据一致\n- 符号和记法的一致性\n- 是否有 AI 生成痕迹或不自然的措辞\n- Checklist section 是否应从 PDF 移除（ARR 规定在 OpenReview 表单中填写）\n\n请按 ARR 审稿标准给出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。"
  }
}
```

</details>

---


### Tool result

_source line 3869 · 2026-05-22T10:56:13.929075+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1609
}
```

</details>

---


### Assistant

_source line 3870 · 2026-05-22T10:56:26.292566+00:00_

已全部派发：

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性 + 实验有效性）| ✅ 已派发 |
| Reviewer 2（新颖性 + 完整性 + 写作）| ✅ 已派发 |
| 视觉审查 Agent | ✅ 已启动（并行，不阻塞） |
| 外部审稿 | ❌ 未启用（项目未配置） |

等待两位 Reviewer 返回 Round 1 初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 287

## Round 287

2 recorded events


### User

_source line 3871 · 2026-05-22T11:05:06.022061+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 3.5 — Borderline Conference
**一句话总结**: 这是一篇对 NER 任务中 test-time scaling（self-consistency）为何失败进行的极为全面的实证分析，统计方法严谨、报告透明诚实，但正面发现在全局多重比较校正下边缘不显著，且研究范围局限于英文 NER 微调模型。

## 官方维度打分（来自 ACL Rolling Review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 实验设计全面（4 NER 数据集、2 模型家族、9 方法类别、N=2–64 scaling），统计方法严格（Holm-Bonferroni k=57、BH FDR、bootstrap CI、TOST 等效检验），核心负面结论（correlation-selection gap）有充分支撑。Proposition 1 的 entity independence 假设较强但被诚实讨论。 |
| Excitement | 3.5/5 | 研究问题重要且及时——理解 self-consistency 在结构化预测上的失败边界对社区有价值。Diagnostic cascade 框架有实用意义。但论文主要是负面结果的系统化表征，缺乏突破性的解决方案。 |
| Reproducibility | 4/5 | 训练配置完整（Table training config），prompt 模板、constrained decoding 细节、统计检验参数均有详细说明。代码承诺接收后发布。 |
| Confidence | 4/5 | 仔细阅读了全文和附录关键部分，熟悉 self-consistency、MBR decoding、NER 评估方法论。 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 核心正面发现在全局多重比较校正下不显著
- 具体位置：Section 7.5（Prescriptive Results）; Appendix Table 12（Holm enumeration, k=57）
- 问题：论文最重要的正面发现——Few-NERD LP selection (+1.39pp) 和 LP-weighted construction (+1.40pp)——在全局 Holm-Bonferroni 校正下仅达到 p_adj=0.055，未通过 α=0.05。论文虽然诚实地在附录报告了这一点，但在正文中仅使用了 per-family 校正（selection family k=21: p_adj=0.021; construction family k=10: p_adj=0.006），而 family 的划分边界由作者自行决定。
- 为什么影响接收：这意味着论文关于"何时 SC 有效"的处方性建议（prescriptive claims）的统计证据是边缘的。论文的核心贡献是负面结果（SC 失败的边界条件），这些不依赖 p-value，但 Section 7.5 的处方性结论（LP-weighted construction 作为可操作建议）证据强度不足。
- 建议修改方向：(1) 在正文明确讨论全局校正结果，不仅放在附录；(2) 考虑将 prescriptive results 定位为 exploratory 而非 confirmatory；(3) 强调核心贡献是 diagnostic cascade（负面结论），而非 LP construction（正面结论）。

**N2** [critical] SciERC 作为主要测试平台的统计 power 有限
- 具体位置：Section 7.1（n=529, single training seed）; Section 4（selection gap analysis 基于 SciERC）
- 问题：SciERC 是论文多项核心分析的主要测试平台（quality estimation Table 3、selection gap Table 1/Figure 2、LP compression analysis、bound validation），但仅有 n=529 个实例且大部分分析仅使用单个训练 seed。论文自己的 power analysis 显示选择效果的 MDE≈1.5pp（Table power analysis），而观测到的效果量仅为 +0.2pp（LP on SciERC），远低于 MDE。Selection 结论虽然是负面的（"no signal beats greedy"），但统计 power 不足意味着可能存在有意义但未被检测到的小效果。
- 为什么影响接收：这不影响"SC 在 SciERC 上不显著优于 greedy"的结论，但影响了效果量的估计精度和泛化信心。论文在 Limitations 中承认了这一点，但作为实证分析论文，核心数据集的统计 power 是方法论基础。
- 建议修改方向：(1) 在正文（而非仅 Limitations）讨论 power 限制对 SciERC 结论的含义；(2) 报告 TOST 结果（附录已有）在正文中，让读者理解"未显著优于 greedy"≠"等价于 greedy"——在 SciERC 上两者均未被确认；(3) 考虑增加 SciERC 的多 seed 实验以增强说服力。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] "Diagnostic cascade"一词可能误导因果解读
- 具体位置：Section 4（Diagnostic cascade 段落）; Section 9（Discussion）
- 问题：论文将 degeneracy → oracle headroom → LP compression → signal alignment 称为 "cascade"，暗示序列因果关系。但 Section 4 承认 "the cascade stages interact rather than combining into a predictive model (R²<0)" 且 "stages resist decomposition into independent effects"。如果阶段间不独立、不能预测、R²<0，那么 "cascade" 这个比喻有误导性。它更像是对同一潜在现象（capability-diversity tension）的多个相关表征，而非因果序列。
- 建议：改用更谨慎的术语如 "diagnostic decomposition" 或 "diagnostic checklist"，或在首次使用时明确限定 "we use 'cascade' to denote a diagnostic sequence, not a causal chain"。

**W2** [warning] 训练 epoch 差异构成潜在混淆变量
- 具体位置：Section 7.1（Few-NERD 3 epochs vs. 其他 5 epochs）; Appendix epoch_confound
- 问题：Few-NERD（3 epochs）是唯一 LP selection 显著生效的数据集（+1.39pp, p<0.001），而它也是唯一使用不同训练配置的数据集。附录显示 5-epoch 训练使 degeneracy 从 13% 升至 31%，LP 增益减半。这意味着 Few-NERD 的低 degeneracy（使 LP selection 成功的关键条件）可能部分是 undertraining 的产物，而非任务本身的特性。
- 建议：(1) 在正文中明确讨论这一混淆变量（目前仅在附录）；(2) 理想情况下补充 Few-NERD 5-epoch 的完整实验来量化 epoch 效应。

**W3** [warning] 自验证实验使用不同模型家族
- 具体位置：Section 3（Qwen2.5-7B, 而非主要的 Qwen3-8B）
- 问题：ESJ、MRSC、LSC 三项自验证实验均使用 Qwen2.5-7B（"a separate model family"），而非论文的主要模型 Qwen3-8B。Qwen2.5 和 Qwen3 的架构和训练数据有显著差异，自验证能力（如 ESJ AUROC=0.512）可能因模型而异。Section 3 的结论（"models cannot self-verify at the entity level"）可能不直接推广到主模型。
- 建议：至少讨论为什么选择不同模型进行自验证实验，以及为何结论应该推广到 Qwen3-8B。如果有条件，补充 Qwen3-8B 上的 ESJ 实验。

**W4** [warning] 研究范围与标题/摘要的 claim scope 不完全匹配
- 具体位置：Title ("Boundary Conditions for Information Extraction"); Abstract ("whether these gains transfer to information extraction")
- 问题：标题和摘要声称研究 "Information Extraction" 的边界条件，但实际主要证据来自 4 个英文 NER 数据集（2 个模型家族）。RE 仅在单个数据集（SciERC, n=397）上进行了探索性实验，SQL pilot 仅 n=196。论文在 Limitations 中承认了这一点，但标题/摘要的 framing 比证据支撑的范围更宽。
- 建议：(1) 考虑标题改为更精确的 "Boundary Conditions for Named Entity Recognition"；(2) 或在摘要中明确限定 "primarily NER, with exploratory extensions to RE and SQL"。

**W5** [warning] Constrained decoding 对 LP compression 的贡献未充分量化
- 具体位置：Section 4（LP compression analysis）; Appendix free-form ablation
- 问题：论文的核心发现之一是 LP score 在 constrained decoding 下严重压缩（SciERC 60% 实例 LP range < 0.041 nats）。附录的 free-form decoding ablation 显示 degeneracy 在 constrained 和 free-form 间差异不大（CoNLL: 56.7% vs 59.3%），但没有直接比较 LP compression 在两种 decoding 模式下的差异。Free-form ablation 在 LP 方面主要报告了 selection 结果（仍然失败），但 LP range/tied fraction 的对比数据不完整。Page 31 提到 "Free-form decoding reduces the tied fraction" 但具体数值未充分报告。
- 建议：补充 free-form decoding 下的 LP tied fraction 和 LP range 统计量，与 constrained decoding 直接对比，以量化 constrained decoding 对 LP compression 的贡献。

---

## 小问题（不影响接收）

1. **Checklist 格式**：Responsible NLP Research Checklist 被包含在论文 PDF 中（pages 9-10），但按 EMNLP 2026 ARR 规定，checklist 应在 OpenReview 提交表单中填写，不应放在 PDF 内。建议提交时从 PDF 中移除。

2. **摘要措辞不清**："best-of-N yields instance-level selection ρ < 1 pp even at N = 64"——ρ 是相关系数，"< 1 pp" 暗示性能差异，两者混用造成理解困难。应改为 "selection gain < 1 pp"。

3. **GPT-5.5 实验规模有限**：仅 200 个 Few-NERD 实例，零样本。作为 frontier model 证据，样本量偏小。

4. **Figure 1 信息密度过高**：三个子图（Quality Estimation / Sample Selection / Entity Construction）挤在一栏宽内，标注文字较难辨认。

5. **Table 2 中 §column 引用不一致**：部分方法引用 Section 编号，部分引用 Appendix，读者定位不便。

---

## 主要优势

1. **极为全面的实证调查**：9 个方法类别、5 个 confidence signals、4 个 NER 数据集、2 个模型家族、N=2–64 scaling、4B–72B model scale ablation、free-form decoding ablation。46 页附录覆盖了几乎所有可以想到的 robustness check。这种 thoroughness 在 NLP 实证论文中罕见。

2. **统计方法严谨且诚实**：Holm-Bonferroni (k=57)、BH FDR、bootstrap CI、paired bootstrap p-values、TOST 等效检验、power analysis——论文不仅使用了这些方法，还诚实报告了核心发现在全局校正下的边缘状态。这种透明度应该被鼓励。

3. **Correlation-selection gap 的发现有实质贡献**：Quality estimation ρ 可达 0.38-0.45 但不转化为 selection gain，这一发现清晰、可复现，且对 test-time scaling 的实践部署有直接指导意义。

4. **Diagnostic cascade 作为实用框架**：即使术语有待商榷，degeneracy/headroom/compression/alignment 四要素的分解为从业者提供了可操作的预部署检查清单。

5. **负面结果的系统化呈现**：论文系统地排除了多种潜在解决方案（ESJ、MRSC、LSC、supervised combination、trained verifier），充分论证了问题的结构性（structural bottleneck），而非简单的 "method X doesn't work"。

6. **跨模型家族一致性**：Qwen3-8B 和 LLaMA-3.1-8B 的结果高度一致（signal rankings stable, gap persists），加上 4B/14B/72B ablation 和 GPT-5.5 frontier evidence，增强了发现的泛化性。

---

## Questions for Authors

Q1: Few-NERD 使用 3 epochs 而非 5 epochs 是否有特定原因（如过拟合）？是否有 5-epoch Few-NERD 的 LP selection 结果？

Q2: Section 3 的自验证实验选择 Qwen2.5-7B 而非主模型 Qwen3-8B 的原因是什么？是否有 Qwen3-8B 上的 ESJ 结果？

Q3: Free-form decoding ablation 中，LP tied fraction（within-instance LP range < 0.05 的比例）具体是多少？与 constrained decoding 的 60.3% 如何对比？

Q4: 如果 diagnostic cascade 的各阶段不独立（R²<0），那么将 α（signal alignment）识别为 "bottleneck" 的结论是否依赖于各因素可分解的假设？

## Missing References

- Li et al. (2024) "Self-consistency improves chain of thought reasoning in language models" 的后续工作在 structured prediction 上的分析
- 建议引用 Yao et al. (2024) 的 Tree of Thoughts 和 Sel et al. 的 Algorithm of Thoughts 以丰富 Related Work 中对 test-time compute 方法的覆盖（如果空间允许）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 3872 · 2026-05-22T11:05:11.740502+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 288

## Round 288

2 recorded events


### User

_source line 3873 · 2026-05-22T11:05:22.781613+00:00_

[Reviewer 1 审稿结果]:
审稿完成，已提交给 Review Director。

**审稿结论摘要：Overall 3.5（Borderline Conference）**

核心判断：这是一篇对 NER test-time scaling 失败边界的极为全面的实证分析，统计方法严谨、报告透明。主要发现（correlation-selection gap、diagnostic cascade）有充分实验支撑。

两个 Must-Fix 问题：(1) 核心正面发现（LP selection/construction on Few-NERD）在全局 Holm-Bonferroni 校正下仅 p_adj=0.055，应在正文讨论而非仅在附录；(2) SciERC 作为主要测试平台 n=529 且大多仅单 seed，统计 power 有限。

五个 Should-Fix 问题：cascade 术语可能误导因果解读、Few-NERD epoch 差异是混淆变量、自验证实验使用不同模型、标题/摘要 scope 比证据更宽、constrained decoding 对 LP compression 的贡献未充分量化。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 3874 · 2026-05-22T11:05:29.147111+00:00_

Reviewer 1 审稿已收到（3.5 Borderline Conference）。等待 Reviewer 2 返回后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 289

## Round 289

6 recorded events


### User

_source line 3875 · 2026-05-22T11:05:59.639076+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见：新颖性 + 完整性 + 写作质量

### Paper Summary

本文研究 test-time compute scaling（via self-consistency / best-of-N）在信息抽取中何时失效，以 NER 为主要案例。核心发现是 "correlation-selection gap"：质量估计信号（LP, SJ, FK 等）能有效预测输出质量（AUROC ≤0.82），但在 instance-level 选择中增益 <1 pp。论文提出四阶段诊断级联（diagnostic cascade），将失效归因于 output degeneracy（12-68%）和 signal alignment collapse。作为改进方案，提出 LP-weighted entity-level construction（Few-NERD +1.4 pp），并通过 Proposition 1-2 建立与 MBR decoding 的理论联系。实验覆盖 4 个 NER 数据集（SciERC, CoNLL-2003, Few-NERD, WNUT-17）、2 个模型家族（Qwen3, LLaMA-3.1）、以及探索性的 RE 扩展。

---

## 总体评分

**Overall**: 3.0 (Findings)

**一句话总结**: 对 NER 中自一致性失效模式的全面诊断分析，实证极为扎实（46 页附录），但核心发现新颖性有限、标题范围显著超出证据支撑。

---

## 官方维度打分（ACL Rolling Review）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | NER 实验方法论严谨（bootstrap CI、Holm-Bonferroni 校正），但标题声称 "Information Extraction" 而证据 ~95% 是 NER，scope claim 未被充分支撑 |
| Excitement | 3/5 | 重要的实际问题（SC 何时失效），分析细致全面，但核心发现在更广泛 ML 文献中并非全新，insights 偏向系统化梳理而非意外发现 |
| Reproducibility | 4/5 | 公开数据集、开放模型（Qwen3/LLaMA）、详细实验配置（Appendix k, Table 20）、承诺代码发布 |
| Confidence | 4/5 | 仔细阅读全文 46 页（含全部附录），对 NER/SC/test-time scaling 领域熟悉 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 标题和范围声称显著超出实际证据

- 具体位置：Title, Abstract (lines 1-20), §1 Introduction, §9 Discussion
- 问题：标题 "Boundary Conditions for Information Extraction" 暗示对 IE 各子任务的全面研究。实际上 ~95% 的证据是 NER（4 个数据集，细致的多维分析）。RE 仅有 SciERC 1 个数据集的 zero-shot 探索性结果（Appendix o, Table 29-30），LP 选择在 RE 上无正向增益。SQL parsing 仅在 §6.2 提及一次（"SQL parsing (87.2% degeneracy)"），无系统实验。Abstract 说 "NER...as the primary case study and relation extraction as an exploratory extension"，部分承认了这一点，但与标题不匹配。NER 的 set-valued output 结构（partial match, entity-level F1）与 RE 的 tuple-valued output 有本质差异，findings 的迁移性未被验证。
- 为什么影响接收：Reviewer 和读者会期望看到对 IE 各子任务（NER, RE, EE, 至少两种）的系统覆盖。标题设定了论文未兑现的期望，是一个 claim-evidence mismatch。
- 建议修改方向：(1) 将标题改为 "...for Named Entity Recognition"，在 Discussion 中讨论向 RE/EE 的潜在推广；或 (2) 大幅扩展 RE 实验（至少 2 个 RE 数据集，fine-tuned 模型，完整的 diagnostic cascade 分析），使证据匹配 IE 范围。

**N2** [critical] 核心发现 "correlation-selection gap" 的新颖性定位不够准确

- 具体位置：§1 (lines 15-25), §2 (Diagnostic Framework), §4 (Where Single-Signal Selection Fails), §9
- 问题：论文将 correlation-selection gap 定位为核心发现（"we identify a correlation-selection gap"），但 "信号能预测质量但不能改善选择" 这一现象在 ML 文献中有先例：calibration ≠ ranking 在决策理论中是已知的；Chen et al. (2024a) 已记录 SC 在 free-form generation 中的系统性失效；Yun & Price (2025) 已记录 diversity collapse 与 capability 的关联。论文的实际贡献在于：(a) 首次为 NER 提供系统化的失效诊断框架，(b) 识别 entity-level 部分匹配（F1 metric）如何使 SC 选择比 discrete-answer QA 更困难，(c) 量化了 degeneracy 和 alignment 的具体阈值。但这些贡献在论文中的定位不够精确——容易被误读为声称发现了全新现象，而非对已知问题在新领域的系统化深入分析。
- 为什么影响接收：新颖性是 conference-level acceptance 的关键标准。如果审稿人认为核心 finding 是已知现象的重新包装，Overall score 可能降至 2.5-3.0。准确的新颖性定位可以避免这种误判。
- 建议修改方向：在 §1 明确区分：(a) SC 失效作为一般现象是已知的（cite Chen et al., Yun & Price），(b) 本文的贡献是首次为结构化 IE 输出提供完整的量化诊断框架，揭示 entity-level partial match 如何创造 QA 中不存在的特有 failure mode。强调 "systematic diagnosis" 而非 "discovery"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Related Work 缺失几个直接相关方向

- 具体位置：§8 Related Work
- 问题：
  - **Conformal prediction for structured prediction**：直接相关于论文讨论的选择可靠性和 coverage guarantee 问题（e.g., Fisch et al. 2021 on conformal methods for NLP; Angelopoulos & Bates 2023 survey）。论文的 entity-level construction 某种程度上追求 coverage，但未讨论 conformal 框架提供的形式化保证。
  - **Token-level uncertainty estimation**：绕过了论文指出的 entity-level alignment 核心难题。If quality estimation at the token level avoids the compression and alignment issues documented in §4 and Appendix m, this is a directly relevant alternative approach.
  - **Trained verifiers / reward models for generation**：§5.2 测试了 LightGBM entity-level verifier（+0.30 pp），但缺乏对更广泛 learned verification 文献的讨论（Cobbe et al. 2021 for math verification; 以及 NER 场景的 analogues）。
  - **MBR with structured utility functions**：Entity-level construction 本质是以 entity-level F1 为 utility 的 MBR（论文自己通过 Proposition 2 确认），但 §8 对结构化 MBR 的文献讨论不足（e.g., Chen et al. 2025 structure-conditional MBR）。
- 建议：在 §8 增加一段讨论这些方向，说明与本文方法的区别和联系。

**W2** [warning] "Cascade" 框架命名有误导性

- 具体位置：Abstract, §3, §4, §9
- 问题："Diagnostic cascade" 暗示各阶段有严格顺序依赖（前一阶段输出是后一阶段输入）。但 §4 明确说 "degeneracy constrains headroom but does not independently predict whether LP selection gains materialize (§9)"——说明 degeneracy 和 LP-alignment 并非真正的级联关系，而是两个需要同时满足的必要条件。§3 的 ESJ → MRSC → LSC → hidden-probe 虽然有逻辑递进（从表层到深层），但也不构成严格的数据流级联。在信号处理和 ML 中，"cascade" 有明确的技术含义（级联分类器如 Viola-Jones），使用该术语需要更严格的顺序依赖证据。
- 建议：改用 "diagnostic framework" 或 "diagnostic checklist"，或在首次使用时明确定义 "cascade" 在此处的特殊含义。

**W3** [warning] Responsible NLP Research Checklist 不应出现在 PDF 中

- 具体位置：Pages 9-10, §"Responsible NLP Research Checklist"
- 问题：根据 ARR 2026 规定，Responsible NLP Research Checklist 应在 OpenReview 提交表单中由作者填写，不应包含在论文 PDF 中。当前 PDF 中包含完整的 checklist（占约 1.5 页），属于格式不合规。
- 建议：从 PDF 中移除该 section。Checklist 内容迁移至 OpenReview 表单。

**W4** [warning] Capability-diversity tension 的证据基础不足以支撑其 claim 强度

- 具体位置：§6.2, §7.2, §9 ("capability-diversity tension ... extends beyond NER")
- 问题：
  - 模型规模变化有限：同一家族内仅 4B → 8B → 14B（Qwen3），跨家族仅 LLaMA-3.1-8B
  - GPT-5.5 作为 "frontier model" 证据极弱：200 个 Few-NERD 实例、zero-shot、单一数据集（§6.2）
  - 没有测试 >14B 的开放模型（如 Qwen3-72B 仅有 "preliminary cross-scale evidence"，Abstract）
  - §9 将此描述为 "a structural constraint documented across NER configurations"，但证据范围不足以声称是 structural
  - 72B 的证据来自 Qwen2.5-72B（非 Qwen3），且仅有 "preliminary" 观察
- 建议：弱化 claim 为 "observed trend within the tested model scales"，或补充更多模型规模点的系统实验。

**W5** [warning] 理论分析（§6）与实证叙事的衔接和实际指导价值有限

- 具体位置：§6, Appendix p, Table 31
- 问题：
  - Proposition 1 的 Corollary 1（degeneracy threshold for SC gain）给出的 bound 非常松：Table 31 显示 actual/bound ratio 仅 3-12%，意味着理论值高估实际所需 degeneracy rate 约 10 倍
  - Proposition 2 的 entity independence 假设在实践中不成立——SciERC 含嵌套实体，CoNLL 的 entity correlation 在 §6.1 中也被承认（"split-half r=0.578-0.644"）
  - §6 在全文叙事中感觉较突兀——前 5 节是实证诊断，§6 突然转入形式化分析，然后 §7 又回到实验
- 建议：(a) 更明确讨论 bound 的松紧度及其实际 implications；(b) 考虑将部分理论内容移入 Appendix，在正文保留核心直觉和 key results。

---

## 小问题（不影响接收）

- §3 的 ESJ、MRSC、LSC 等缩写定义后在后续正文使用频率很低，增加了阅读认知负担。考虑减少缩写或在后续出现时使用全称。
- Figure 2 的 bar + line 组合在双栏格式的小字号下可读性有限，x 轴标签密集。
- §5 "Adaptive Methods" 的深度与 §3-4 的细致分析不成比例——cross-model SC（§5.1, 2 行）和 trained verifiers（§5.2, 3 行）都值得更多讨论。
- Ethics Statement 提到使用 "GPT-5.5 API" 但未讨论闭源 API 对可复现性的影响，应在 Limitations 中提及。
- Abstract 最后说 "capability-diversity tension likely extends beyond NER but needs further validation"——这句在 abstract 中显得多余，因为 abstract 应聚焦于本文已有证据的 claims。
- Table 1 caption 说 "One score per input" 但具体含义需要回到 §2.2 才能理解——建议在 caption 中自包含。

---

## 主要优势

1. **极为细致的实证分析**：4 个 NER 数据集 × 2 个模型家族 × 5+ 质量信号 × 多种 N/T 配置，加上 46 页附录中包含 60+ 张表格和 10+ 张图，展现了顶级的实验严谨性。这可能是目前对 NER 中 self-consistency 行为最详尽的实证研究。

2. **统计方法论严谨**：Bootstrap 95% CI（Tables 1, 50）、Holm-Bonferroni 校正的 57 项假设检验（Table 12）、跨 3 seeds 的排名稳定性（Table 6）、FK independence test（Table 7）、permutation tests。这种统计严谨性在 NLP 经验性研究中不常见。

3. **实用的诊断视角**：即便各组成部分非全新，将 degeneracy、alignment、convergence、compression 组织为结构化诊断框架对实践者有切实的部署前检查价值——尤其是 "先检查 degeneracy rate，若 >50% 则不值得做 selection" 这类具体可操作的 rule of thumb。

4. **MBR 理论连接**：Proposition 2 将 entity-level majority vote 与 MBR decoding 建立形式化等价关系，虽然 independence 假设较强，但提供了理解 entity construction 何时有效的理论基础。

5. **写作总体清晰**：行文流畅，定量密度高但不晦涩，Figure 1 作为全文 overview 信息效率高，术语和符号使用总体一致（Appendix a, Table 5 提供了完整 notation table）。

6. **透明的 AI 使用声明**：Ethics Statement 明确说明 "AI writing assistants were used for drafting and editing. All scientific claims, experimental results, and analyses are the authors' own work"，符合当前学术规范。

---

## 问题（Questions for Authors）

1. Diagnostic cascade 在使用 learned verifier/selector（而非无监督信号）时会如何变化？§5.2 的 LightGBM 仅 +0.30 pp——这是因为特征不够好还是因为选择问题本身存在信息论上的硬界限？
2. Entity-level construction 增益较小（Few-NERD +1.4 pp，SciERC/CoNLL 不显著，Table 61）。能否给出更清晰的 characterization：在什么样的 degeneracy rate × alignment 条件组合下可以期望显著增益？
3. Proposition 2 的 entity independence 假设在 SciERC（嵌套实体）和 CoNLL（强实体共现模式）下偏离多大？这个偏离是否系统性地解释了 entity construction 在这些数据集上增益有限？
4. 是否考虑过 token-level uncertainty estimation 作为绕过 entity-level alignment 问题的替代路径？这似乎是一个自然的 "escape hatch"，但论文未讨论。

---

## Missing References

- Fisch, A., Schuster, T., Jaakkola, T., & Barzilay, R. (2021). Few-shot conformal prediction with auxiliary tasks. ICML.
- Angelopoulos, A. N., & Bates, S. (2023). Conformal prediction: A gentle introduction. Foundations and Trends in ML.
- Cobbe, K., Kosaraju, V., Bavarian, M., et al. (2021). Training verifiers to solve math word problems. arXiv:2110.14168.（已引用，但未在 §8 Related Work 中讨论其对 NER verification 的启示）
- 更广泛的 token-level uncertainty for sequence labeling 文献
- Chen et al. (2025) Structure-conditional minimum Bayes risk decoding（已引用于 §8，但讨论不足）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 3876 · 2026-05-22T11:06:31.856054+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（Overall: 3.0 Findings）\n\n### Must-Fix 问题\n\n**N1** [critical] 标题和范围声称显著超出实际证据\n- Title \"Boundary Conditions for Information Extraction\" 暗示对 IE 各子任务的全面研究。实际上 ~95% 的证据是 NER。RE 仅有 SciERC 1 个数据集的 zero-shot 探索性结果，SQL parsing 仅一句话提及。NER 的 set-valued output 结构与 RE 的 tuple-valued output 有本质差异，findings 的迁移性未被验证。\n\n**N2** [critical] 核心发现 \"correlation-selection gap\" 的新颖性定位不够准确\n- \"信号能预测质量但不能改善选择\" 在 ML 文献中有先例：calibration ≠ ranking 在决策理论中已知；Chen et al. (2024a) 记录 SC 在 free-form generation 中的系统性失效；Yun & Price (2025) 记录 diversity collapse。论文的实际贡献在于首次为 NER 提供系统化失效诊断框架，但定位为 \"discovery\" 而非 \"systematic diagnosis in a new domain\" 可能被误读为声称全新现象。\n\n### Should-Fix 问题\n\n**W1** [warning] Related Work 缺失几个直接相关方向\n- Conformal prediction for structured prediction（Fisch et al. 2021, Angelopoulos & Bates 2023）\n- Token-level uncertainty estimation\n- Trained verifiers / reward models 的更广泛讨论\n- MBR with structured utility functions（Chen et al. 2025）\n\n**W2** [warning] \"Cascade\" 框架命名有误导性\n- \"Diagnostic cascade\" 暗示严格顺序依赖，但 degeneracy 和 LP-alignment 并非真正级联关系，而是两个需要同时满足的必要条件。在 ML 中 \"cascade\" 有技术含义（Viola-Jones 等）。\n\n**W3** [warning] Responsible NLP Research Checklist 不应出现在 PDF 中\n- ARR 2026 规定 checklist 在 OpenReview 表单中填写，当前 PDF 包含完整 checklist（~1.5 页），格式不合规。\n\n**W4** [warning] Capability-diversity tension 的证据基础不足以支撑其 claim 强度\n- 模型规模变化有限（4B-14B），GPT-5.5 证据极弱（200 实例 zero-shot），72B 仅 preliminary。\n\n**W5** [warning] 理论分析（§6）与实证叙事的衔接和实际指导价值有限\n- Proposition 1 的 bound 非常松（actual/bound ratio 仅 3-12%），entity independence 假设不成立。§6 在全文中感觉突兀。\n\n### 小问题\n- ESJ/MRSC/LSC 等缩写使用频率低增加认知负担\n- Figure 2 可读性有限\n- §5 Adaptive Methods 深度与 §3-4 不成比例\n- Ethics Statement 未讨论闭源 API 对可复现性的影响\n- Abstract 最后一句关于 capability-diversity tension \"extends beyond NER\" 在 abstract 中多余\n\n### Reviewer 2 的 Missing References\n- Fisch et al. (2021) Few-shot conformal prediction with auxiliary tasks\n- Angelopoulos & Bates (2023) Conformal prediction survey\n- Cobbe et al. (2021) Training verifiers（已引用但 §8 讨论不足）\n- Token-level uncertainty for sequence labeling 文献\n- Chen et al. (2025) Structure-conditional MBR（已引用但讨论不足）\n\n---\n\n请对以上每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见（Overall: 3.0 Findings）\n\n### Must-Fix 问题\n\n**N1** [critical] 标题和范围声称显著超出实际证据\n- Title \"Boundary Conditions for Information Extraction\" 暗示对 IE 各子任务的全面研究。实际上 ~95% 的证据是 NER。RE 仅有 SciERC 1 个数据集的 zero-shot 探索性结果，SQL parsing 仅一句话提及。NER 的 set-valued output 结构与 RE 的 tuple-valued output 有本质差异，findings 的迁移性未被验证。\n\n**N2** [critical] 核心发现 \"correlation-selection gap\" 的新颖性定位不够准确\n- \"信号能预测质量但不能改善选择\" 在 ML 文献中有先例：calibration ≠ ranking 在决策理论中已知；Chen et al. (2024a) 记录 SC 在 free-form generation 中的系统性失效；Yun & Price (2025) 记录 diversity collapse。论文的实际贡献在于首次为 NER 提供系统化失效诊断框架，但定位为 \"discovery\" 而非 \"systematic diagnosis in a new domain\" 可能被误读为声称全新现象。\n\n### Should-Fix 问题\n\n**W1** [warning] Related Work 缺失几个直接相关方向\n- Conformal prediction for structured prediction（Fisch et al. 2021, Angelopoulos & Bates 2023）\n- Token-level uncertainty estimation\n- Trained verifiers / reward models 的更广泛讨论\n- MBR with structured utility functions（Chen et al. 2025）\n\n**W2** [warning] \"Cascade\" 框架命名有误导性\n- \"Diagnostic cascade\" 暗示严格顺序依赖，但 degeneracy 和 LP-alignment 并非真正级联关系，而是两个需要同时满足的必要条件。在 ML 中 \"cascade\" 有技术含义（Viola-Jones 等）。\n\n**W3** [warning] Responsible NLP Research Checklist 不应出现在 PDF 中\n- ARR 2026 规定 checklist 在 OpenReview 表单中填写，当前 PDF 包含完整 checklist（~1.5 页），格式不合规。\n\n**W4** [warning] Capability-diversity tension 的证据基础不足以支撑其 claim 强度\n- 模型规模变化有限（4B-14B），GPT-5.5 证据极弱（200 实例 zero-shot），72B 仅 preliminary。\n\n**W5** [warning] 理论分析（§6）与实证叙事的衔接和实际指导价值有限\n- Proposition 1 的 bound 非常松（actual/bound ratio 仅 3-12%），entity independence 假设不成立。§6 在全文中感觉突兀。\n\n### 小问题\n- ESJ/MRSC/LSC 等缩写使用频率低增加认知负担\n- Figure 2 可读性有限\n- §5 Adaptive Methods 深度与 §3-4 不成比例\n- Ethics Statement 未讨论闭源 API 对可复现性的影响\n- Abstract 最后一句关于 capability-diversity tension \"extends beyond NER\" 在 abstract 中多余\n\n### Reviewer 2 的 Missing References\n- Fisch et al. (2021) Few-shot conformal prediction with auxiliary tasks\n- Angelopoulos & Bates (2023) Conformal prediction survey\n- Cobbe et al. (2021) Training verifiers（已引用但 §8 讨论不足）\n- Token-level uncertainty for sequence labeling 文献\n- Chen et al. (2025) Structure-conditional MBR（已引用但讨论不足）\n\n---\n\n请对以上每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 3877 · 2026-05-22T11:06:56.640934+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 24784
}
```

</details>

---


### Tool call

_source line 3878 · 2026-05-22T11:06:56.842148+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（Overall: 3.5 Borderline Conference）\n\n### Must-Fix 问题\n\n**N1** [critical] 核心正面发现在全局多重比较校正下不显著\n- Few-NERD LP selection (+1.39pp) 和 LP-weighted construction (+1.40pp) 在全局 Holm-Bonferroni (k=57) 下仅 p_adj=0.055。正文使用 per-family 校正（selection k=21: p_adj=0.021; construction k=10: p_adj=0.006），family 划分由作者自行决定。论文的 prescriptive claims 统计证据边缘。\n\n**N2** [critical] SciERC 作为主要测试平台的统计 power 有限\n- SciERC 仅 n=529 且大部分分析仅单 seed。Power analysis 显示 MDE≈1.5pp，观测效果 +0.2pp 远低于 MDE。不影响 \"no signal beats greedy\" 结论，但影响效果量估计精度和泛化信心。\n\n### Should-Fix 问题\n\n**W1** [warning] \"Diagnostic cascade\" 术语可能误导因果解读\n- §4 承认 stages interact、R²<0、不能分解为独立效应。\"Cascade\" 比喻有误导性，更像是多个相关表征而非因果序列。\n\n**W2** [warning] 训练 epoch 差异构成潜在混淆变量\n- Few-NERD（3 epochs）是唯一 LP selection 显著的数据集，也是唯一不同训练配置的。5-epoch 使 degeneracy 从 13% 升至 31%，LP 增益减半。Few-NERD 的低 degeneracy 可能部分是 undertraining 产物。\n\n**W3** [warning] 自验证实验使用不同模型家族\n- §3 的 ESJ/MRSC/LSC 使用 Qwen2.5-7B 而非主模型 Qwen3-8B。\"Models cannot self-verify\" 结论可能不直接推广到主模型。\n\n**W4** [warning] 研究范围与标题/摘要的 claim scope 不完全匹配\n- 标题 \"Information Extraction\" 但主要是 NER，RE/SQL 仅 exploratory。\n\n**W5** [warning] Constrained decoding 对 LP compression 的贡献未充分量化\n- LP 在 constrained decoding 下压缩严重（60% 实例 LP range < 0.041 nats），但 free-form ablation 中 LP compression 的直接对比数据不完整。\n\n### Reviewer 1 小问题\n- Checklist 不应在 PDF 中\n- Abstract \"ρ < 1 pp\" 措辞混淆\n- GPT-5.5 仅 200 实例\n- Figure 1 信息密度过高\n- Table 2 引用不一致\n\n### Reviewer 1 的优势评价\n- 极为全面的实证调查（9 方法类别，5 信号，4 数据集，2 模型家族，N=2-64）\n- 统计方法严谨且诚实（k=57 Holm, BH FDR, TOST）\n- Correlation-selection gap 有实质贡献\n- 负面结果的系统化呈现\n\n### Reviewer 1 Missing References\n- Li et al. (2024) SC for structured prediction\n- Yao et al. (2024) Tree of Thoughts, Sel et al. Algorithm of Thoughts\n\n---\n\n请对以上每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix 和 Should-Fix，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿意见（Overall: 3.5 Borderline Conference）\n\n### Must-Fix 问题\n\n**N1** [critical] 核心正面发现在全局多重比较校正下不显著\n- Few-NERD LP selection (+1.39pp) 和 LP-weighted construction (+1.40pp) 在全局 Holm-Bonferroni (k=57) 下仅 p_adj=0.055。正文使用 per-family 校正（selection k=21: p_adj=0.021; construction k=10: p_adj=0.006），family 划分由作者自行决定。论文的 prescriptive claims 统计证据边缘。\n\n**N2** [critical] SciERC 作为主要测试平台的统计 power 有限\n- SciERC 仅 n=529 且大部分分析仅单 seed。Power analysis 显示 MDE≈1.5pp，观测效果 +0.2pp 远低于 MDE。不影响 \"no signal beats greedy\" 结论，但影响效果量估计精度和泛化信心。\n\n### Should-Fix 问题\n\n**W1** [warning] \"Diagnostic cascade\" 术语可能误导因果解读\n- §4 承认 stages interact、R²<0、不能分解为独立效应。\"Cascade\" 比喻有误导性，更像是多个相关表征而非因果序列。\n\n**W2** [warning] 训练 epoch 差异构成潜在混淆变量\n- Few-NERD（3 epochs）是唯一 LP selection 显著的数据集，也是唯一不同训练配置的。5-epoch 使 degeneracy 从 13% 升至 31%，LP 增益减半。Few-NERD 的低 degeneracy 可能部分是 undertraining 产物。\n\n**W3** [warning] 自验证实验使用不同模型家族\n- §3 的 ESJ/MRSC/LSC 使用 Qwen2.5-7B 而非主模型 Qwen3-8B。\"Models cannot self-verify\" 结论可能不直接推广到主模型。\n\n**W4** [warning] 研究范围与标题/摘要的 claim scope 不完全匹配\n- 标题 \"Information Extraction\" 但主要是 NER，RE/SQL 仅 exploratory。\n\n**W5** [warning] Constrained decoding 对 LP compression 的贡献未充分量化\n- LP 在 constrained decoding 下压缩严重（60% 实例 LP range < 0.041 nats），但 free-form ablation 中 LP compression 的直接对比数据不完整。\n\n### Reviewer 1 小问题\n- Checklist 不应在 PDF 中\n- Abstract \"ρ < 1 pp\" 措辞混淆\n- GPT-5.5 仅 200 实例\n- Figure 1 信息密度过高\n- Table 2 引用不一致\n\n### Reviewer 1 的优势评价\n- 极为全面的实证调查（9 方法类别，5 信号，4 数据集，2 模型家族，N=2-64）\n- 统计方法严谨且诚实（k=57 Holm, BH FDR, TOST）\n- Correlation-selection gap 有实质贡献\n- 负面结果的系统化呈现\n\n### Reviewer 1 Missing References\n- Li et al. (2024) SC for structured prediction\n- Yao et al. (2024) Tree of Thoughts, Sel et al. Algorithm of Thoughts\n\n---\n\n请对以上每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 3879 · 2026-05-22T11:06:58.405255+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1563
}
```

</details>

---


### Assistant

_source line 3880 · 2026-05-22T11:07:01.058865+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 290

## Round 290

2 recorded events


### User

_source line 3881 · 2026-05-22T11:07:03.734074+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**要点总结：**

- **Overall: 3.0 (Findings)**——实证工作极为扎实（46 页附录、57 项统计检验），但新颖性定位为系统化梳理而非根本性新发现
- **2 个 Must-Fix**：(1) 标题 "Information Extraction" 与 ~95% NER 证据不匹配；(2) correlation-selection gap 的新颖性需要更准确定位
- **5 个 Should-Fix**：Related Work 缺失（conformal prediction、token-level uncertainty）；"cascade" 命名误导；Checklist 不应在 PDF 中；capability-diversity tension 证据不足；理论分析与实证叙事衔接不够
- **主要优势**：实验严谨性突出、诊断框架有实用价值、MBR 理论连接、统计方法论规范

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 3882 · 2026-05-22T11:07:08.471389+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 291

## Round 291

2 recorded events


### User

_source line 3883 · 2026-05-22T11:08:28.602308+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: 标题和范围声称超出实际证据**

同意 R2 的判断。我在自己的审稿意见中也将此列为 Should-Fix（R1-W4）。论文标题 "Boundary Conditions for Information Extraction" 和摘要措辞暗示对 IE 的全面研究，但实际证据约 95% 来自 NER。具体来看：

- NER：4 个数据集（SciERC, CoNLL, Few-NERD, WNUT-17），2 个模型家族，完整的 N-scaling 和 ablation — 这是充分的。
- RE：仅 SciERC 1 个数据集（n=397），单 seed，论文自己标注为 "exploratory"（Section 7.3, Limitations）。
- SQL：仅在 Discussion 中一句话提及（n=196, "pilot"），无独立章节。

R2 指出 NER 的 set-valued output 与 RE 的 tuple-valued output 有本质结构差异，这一点很到位。NER 的 degeneracy 机制（所有 N 个样本产生相同 entity set）不一定适用于 RE（entity span 错误向下游传播，导致 40% zero-F1 rate — Section 7.3 自己已观察到这一差异）。这恰恰说明 IE 子任务间的迁移不能假设成立。

建议标题改为 "Boundary Conditions for Named Entity Recognition" 或至少 "Boundary Conditions for Information Extraction: Evidence from NER"。

---

**[REBUT] R2-N2: Correlation-selection gap 的新颖性定位**

部分不同意 R2 的严重程度评估。R2 的论点可分解为两部分：

**(a) "calibration ≠ ranking 在决策理论中已知"** — 这是正确的一般性陈述，但论文的贡献不是发现这个抽象原则。论文的贡献是：(1) 在 NER 具体任务上，用 5 个信号 × 4 个数据集系统量化了这个 gap 的程度（ρ 最高 0.45 但 selection gain < 1pp，Table 3/Table 1/Figure 2）；(2) 诊断出 gap 的具体机制——LP compression（60% tied instances, Appendix logprob_ties）和 signal alignment collapse（α→0, Section 6.2）；(3) 通过 9 个方法类别的系统测试（Table 2）证明这是结构性瓶颈而非方法选择问题。这远超 "在新领域观察到已知现象"。

**(b) "Chen et al. (2024a) 和 Yun & Price (2025) 已记录 SC 失效"** — Chen et al. (2024a) 讨论的是 free-form generation 中的 SC 失效，其机制（多样性格式变化 vs. 语义差异）与 NER 的结构化输出完全不同。Yun & Price (2025) 记录的 diversity collapse 更接近，但没有提供系统的诊断框架。论文的 diagnostic cascade（不论名称是否最优）将失效分解为可测量的组件（degeneracy rate, oracle headroom, LP compression, signal alignment），这是方法论层面的原创贡献，不是简单的 "new domain application"。

**但 R2 有一个合理的建议**：论文确实应该更精确地定位贡献——不是 "discovery of a new phenomenon" 而是 "first systematic diagnostic framework for structured prediction"。Introduction 和 Related Work 可以更明确地承认 calibration ≠ ranking 的已知性，然后强调本文的增量在于诊断框架和机制解析。这是 framing 问题，不是 soundness 问题，不应列为 Must-Fix (critical)。建议降级为 Should-Fix。

---

### Should-Fix 问题

**[AGREE] R2-W1: Related Work 缺失方向（部分同意）**

- **Conformal prediction**：同意应讨论。Fisch et al. (2021) 和 Angelopoulos & Bates (2023) 的 conformal prediction 框架提供了不依赖 self-consistency 的不确定性量化方法，与本文的 quality estimation 分析直接相关。特别是 conformal prediction 不需要 calibration = ranking，可能规避本文发现的 correlation-selection gap。
- **Token-level uncertainty**：部分同意。论文通过 LP（mean token log-likelihood）已覆盖了 token-level 信号的一种形式，且附录的 1D CNN token-level LP aggregator 实验（Appendix supervised_combination: "gap closure 56.4% vs 55.8%"）测试了更精细的 token-level 聚合。但确实未讨论 sequence labeling 文献中的 token-level uncertainty 方法。
- **Trained verifiers / reward models**：论文实际上测试了 LightGBM verifier（Section 5.2, AUC=0.923）和 DeBERTa verifier（Appendix supervised_combination, ρ=0.329），且讨论了 cross-dataset transfer 失败（Appendix verifier_transfer, -0.76 to -1.02pp）。R2 可能遗漏了这部分内容。但 Related Work（Section 8）中确实对 verifier 文献（Cobbe et al. 2021 等）讨论不足。
- **MBR with structured utility**：同意。Section 6.1 建立了 entity construction = MBR decoding 的联系（Proposition 2），但对 structured MBR 文献的讨论可以更深入。

**[AGREE] R2-W2: "Cascade" 命名有误导性**

完全同意。我在自己的审稿意见中也将此列为 Should-Fix（R1-W1）。论文自己承认 "stages resist decomposition into independent effects (R²<0)"（Section 4），这直接与 "cascade"（暗示顺序依赖）矛盾。R2 提到的 Viola-Jones cascade 类比很有说服力——ML 社区对 "cascade" 有明确的技术理解（序列筛选器，early rejection），与本文的用法不符。

论文实际描述的是两个需要同时满足的必要条件：(1) 低 degeneracy，(2) 高 LP-F1 alignment。Few-NERD 是唯一两者均满足的数据集（degeneracy 13%, LP ρ=0.220），因此是唯一 LP selection 生效的数据集（Table 4）。这更像一个 conjunction（"both conditions must hold"）而非 cascade（"check in order, reject early"）。

**[AGREE] R2-W3: Checklist 不应在 PDF 中**

完全同意，我也已标记此问题。按 EMNLP 2026 ARR 规定，Responsible NLP Research Checklist 应在 OpenReview 表单中填写，不应出现在 PDF 里。当前 PDF 占 ~1.5 页（pages 9-10），应在提交前移除。

**[AGREE] R2-W4: Capability-diversity tension 的证据基础有限（部分同意）**

同意证据基础有提升空间，但不完全同意 R2 对严重性的评估。具体来看：

- **4B-14B 范围**：论文在 fine-tuned 模型上测试了 Qwen3-4B、Qwen3-8B、Qwen3-14B（Table scale_ablation, Appendix），且 4B QE 与 8B 可比（|Δρ|=0.042, Section 7.4）。范围确实有限但方向一致。
- **72B zero-shot**：附录有 Qwen2.5-72B 的完整 QE 和 construction 结果（mentioned in Holm table, tests #27-30），不仅是 "preliminary"——虽然是 zero-shot 设置，但包含了 SciERC/CoNLL/Few-NERD 三个数据集。
- **GPT-5.5**：确实只有 200 个 Few-NERD 实例（Section 6.2），证据偏弱。但它提供了 frontier model 的验证方向（50% degeneracy, SJ ρ=0.346, MV +1.4pp yet 6.8pp oracle headroom），至少显示现象不局限于开源小模型。
- **跨模型家族一致性**：Qwen3-8B 和 LLaMA-3.1-8B 的结果高度一致（Table 3, Table 10），且 frontier model table（Table frontier_sc_cross，提到 degeneracy 5.5-74%）覆盖了更多模型。

总体而言，"capability-diversity tension" 作为 observed pattern 有一定支撑（跨 2 个模型家族 + 3 个 scale + 1 个 frontier），但作为 general claim 确实需要更多证据。建议论文将其定位为 "observed tendency" 而非 "established principle"。

**[REBUT] R2-W5: 理论分析（§6）价值有限**

不完全同意 R2 的评估。

R2 指出 Proposition 1 的 bound 很松（3-12%）且 entity independence 假设不成立，这些事实是正确的。但 R2 遗漏了 Section 6 的实际使用方式：

1. **Proposition 1 不是用来预测性能的**——论文明确说 "the decomposition is diagnostic rather than predictive"（Section 6.2）。它的价值在于分解出三个可独立测量的因素（D, G_nd, α），并通过实证（Table alpha_crit）显示 α→0 是 binding constraint。这个诊断结论不依赖 bound 的 tightness。

2. **Entity construction = MBR decoding 的联系**（Section 6.1, Proposition 2）为 entity-level aggregation 提供了决策理论基础，将 majority vote 识别为 MBR 在 α=1 下的特例。这个 framing 本身有独立价值。

3. **α_crit（有效精度阈值）**的引入（Proposition 1(c)）在 Table alpha_crit 中被实证验证：CoNLL α_crit,eff = 1.148 > 1 → MV gain structurally impossible → 观测 Δ=-0.04pp 确认。这是理论预测与实证吻合的良好案例。

4. **Section 6.2 的 scaling analysis**（oracle scaling curve R²>0.999, Figure oracle_scaling）和 inverse scaling 发现（40/58 transitions show decreased F1, p<0.05）有独立的实证价值。

但 R2 有一个合理的观察：Section 6 在全文中确实有些突兀，因为它同时包含了 MBR 理论、scaling analysis、degeneracy decomposition 和 Proposition 1，而这些内容的衔接不够流畅。建议作者改善 Section 6 的结构组织，使理论分析与前后的实证叙事更好衔接。

---

### 小问题

- **ESJ/MRSC/LSC 缩写认知负担**：同意，这些缩写仅在 Section 3 使用，后文很少出现，确实增加阅读障碍。但考虑到页数限制，简化表述可能更好。
- **Figure 2 可读性**：同意，我也标记了类似问题（R1 小问题 #4）。
- **§5 深度不成比例**：部分同意。§5 覆盖了 cross-model ensemble 和 trained verifier 两个方向，篇幅受限但核心结果清晰（Table 2）。
- **Ethics Statement 闭源 API**：合理建议，但仅涉及 GPT-5.5 的 200 实例，影响有限。
- **Abstract 最后一句**：同意。"extends beyond NER" 在 abstract 中超出论文证据范围，应移除或加限定词。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 3884 · 2026-05-22T11:08:39.087300+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 292

## Round 292

2 recorded events


### User

_source line 3885 · 2026-05-22T11:08:41.822400+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 的逐条回应。总结：

- **N1（标题范围超出证据）**：[AGREE]，与我自己的 W4 一致
- **N2（新颖性定位）**：[REBUT]，论文贡献是诊断框架而非新现象发现，建议降级为 Should-Fix
- **W1（缺失 related work）**：[AGREE]，特别是 conformal prediction 方向
- **W2（Cascade 命名）**：[AGREE]，与我的 W1 一致
- **W3（Checklist 格式）**：[AGREE]
- **W4（capability-diversity tension 证据）**：[AGREE]，但严重性略低于 R2 评估
- **W5（理论分析价值）**：[REBUT]，Proposition 1 的诊断价值不依赖 bound tightness，且 MBR 联系和 α_crit 有独立贡献

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 3886 · 2026-05-22T11:08:47.861943+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 293

## Round 293

10 recorded events


### User

_source line 3887 · 2026-05-22T11:08:58.419045+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: 核心正面发现在全局多重比较校正下不显著**

同意这是一个需要认真对待的统计关切。Few-NERD LP selection (+1.39pp) 在全局 Holm-Bonferroni (k=57) 下 p_adj=0.055，确实处于边缘。我补充以下观察：

1. **Per-family correction 本身是可辩护的**——统计学标准实践中，per-family correction（在功能相关的假设族内校正）而非全局校正是常见做法（e.g., EMA/FDA 临床试验中 primary endpoint family 和 secondary endpoint family 分开校正）。论文将 57 项检验划分为 selection / construction / calibration 等族，这个划分在逻辑上是合理的。
2. **但边缘 p 值确实削弱了 prescriptive claims 的说服力**。论文 §7.5 的 prescriptive 建议（"entity-level construction...yields +8 pp on Few-NERD where LP-F1 alignment is strong"）建立在这个统计边缘的结果之上。如果核心 positive finding 在更保守的校正下不显著，作者应在正文中明确承认这一局限，而非仅在 Table 12 中隐式呈现。
3. **论文的统计诚实度值得肯定**——Table 12 同时报告了 per-family 和 global 两种校正结果，读者可以自行判断。这比许多论文只报告有利的 p 值更透明。

总结：问题真实存在，但 per-family correction 是标准做法，论文的透明报告值得认可。建议作者在 §7 正文中增加一句说明全局校正下 p_adj=0.055 的边缘性。

---

**[AGREE] R1-N2: SciERC 统计 power 有限**

同意 SciERC (n=529) 作为主要测试平台存在 power 限制。我补充：

1. R1 的 MDE≈1.5pp 估算合理。SciERC 上观测到的 +0.2pp（Table 1）远低于 MDE，说明该数据集上的效果量估计精度很低——无法区分 "真的没效果" 和 "有小效果但检测不到"。
2. **多数据集设计部分缓解了这个问题**。论文在 CoNLL-2003 (n≈3,453) 和 Few-NERD (n=32,560) 上也做了主要分析，这些数据集的 power 显著更高。核心的负面结论（"most signals don't beat greedy"）在这些高-power 数据集上也成立（Table 1: CoNLL 最大增益 +0.25pp，WNUT-17 也无显著增益）。
3. **但 SciERC 的 detailed diagnostic 分析（§4 中大量引用的 SciERC-specific 数字）确实受此限制**。例如 Table 3 中 SciERC NER 的各 signal AUC 和 ρ 值、Table 4 的 LP selection 分析、§4 的 degeneracy 和 compression 分析——这些以 SciERC 为主的细节分析在 power 不足的情况下可靠性打折。

总结：同意这是一个有效限制。不改变核心负面结论，但 SciERC-specific 的诊断细节需要更谨慎的解读。

---

### Should-Fix 问题

**[AGREE] R1-W1: "Diagnostic cascade" 术语可能误导因果解读**

强烈同意。这与我在 R2-W2 中提出的关切完全一致。§4 明确承认 "degeneracy constrains headroom but does not independently predict whether LP selection gains materialize"——这表明 degeneracy 和 LP-alignment 是并行的必要条件，而非 cascade 隐含的顺序依赖。R1 指出 §4 自己承认 R²<0、不能分解为独立效应，进一步支持了这一判断。"Diagnostic framework" 或 "diagnostic checklist" 是更准确的术语。

---

**[AGREE] R1-W2: 训练 epoch 差异构成潜在混淆变量**

同意，这是一个我在自己审稿中未充分注意到的有效关切。具体来说：

1. Few-NERD 是唯一 LP selection 显著正向的数据集（Table 1: +1.39pp），也是唯一使用 3 epochs（而非 5 epochs）训练的（Table 20, Appendix k）。
2. R1 指出 5-epoch 训练使 Few-NERD degeneracy 从 13% 升至 31%、LP 增益减半。这在 Appendix u（Table 55, page 40）中有数据支持：SciERC 5-epoch 的 instance degeneracy 为 6.5%，而 Few-NERD 3-epoch 仅 13%——如果 Few-NERD 也用 5 epochs，degeneracy 可能显著上升。
3. **这构成了一个混淆变量**：Few-NERD 的低 degeneracy（使 LP selection 有操作空间）可能部分是 undertraining 的产物，而非数据集的固有属性。论文将 Few-NERD 的 LP 成功归因于 "sufficient model capability and alignment"（§7.5），但未排除 undertraining 这一替代解释。
4. 论文在 Appendix u 中讨论了 training convergence，但将 epoch 效应框架化为 capability-diversity tension 的证据，而非作为 Few-NERD 正面结果的潜在混淆。

建议：在 Limitations 或 §7 中明确讨论这一混淆变量，并报告 Few-NERD 5-epoch 模型的 LP selection 结果。

---

**[AGREE] R1-W3: 自验证实验使用不同模型家族**

同意这是一个方法论上的不一致。§3 的 ESJ/MRSC/LSC 实验使用 Qwen2.5-7B-Instruct（page 4 注释），而主实验使用 Qwen3-8B 和 LLaMA-3.1-8B。"Models cannot self-correct for NER" 的结论基于 Qwen2.5-7B，但 Qwen3-8B 可能有不同的 self-verification 能力（Qwen3 系列在指令遵循上有显著改进）。

不过，我认为这是一个 **moderate concern** 而非 critical issue：
- §3 的结论方向（自验证困难）与主实验的负面选择结果（§4-7）一致——如果模型能有效自验证，我们预期会看到更好的 selection gains
- ESJ AUROC 仅 0.512（接近随机），即使 Qwen3-8B 有所改善，也不太可能从根本上改变结论
- 但严谨性要求使用相同模型，或至少讨论为何使用不同模型及其影响

---

**[AGREE] R1-W4: 研究范围与标题/摘要的 claim scope 不完全匹配**

强烈同意。这与我在 R2-N1 中的关切完全一致，且我将其列为 critical issue。标题 "Information Extraction" 设定了 NER + RE + EE 等子任务的全面覆盖预期，但论文 ~95% 的证据来自 NER。R1 将此列为 should-fix 而非 must-fix，我认为应该更严格——标题直接影响读者预期和论文的 claim scope。

---

**[AGREE] R1-W5: Constrained decoding 对 LP compression 的贡献未充分量化**

部分同意。论文在 Appendix m（Log-Probability Score Compression）和 Appendix q（Free-Form Decoding Ablation, Table 33）中提供了部分证据：
- §7.3 / Appendix q 的 free-form ablation 表明即使在 free-form 模式下，LP 选择效果有限（"selection remains below single-sample"）
- Appendix m (page 22, Figure 9) 展示了 constrained decoding 下 LP compression 的 CDF——60% 实例 LP range < 0.041 nats

但 R1 的关切是对的：**缺少 constrained vs. free-form 模式下 LP compression 指标（range, variance）的直接定量对比**。Table 33 比较了 F1 结果但未比较 LP 分布特征。如果 free-form decoding 下 LP 的 within-instance variance 显著更高，这将直接证明 constrained decoding 是 compression 的主要原因——但论文未提供这一关键对比。

---

### R1 小问题

- **Checklist 不应在 PDF 中**：[AGREE]，与我的 R2-W3 一致。
- **Abstract "ρ < 1 pp" 措辞混淆**：[AGREE]，ρ 通常表示相关系数，此处用来表示增益幅度容易造成歧义。应考虑改为 "gain < 1 pp" 或 "Δ < 1 pp"。
- **GPT-5.5 仅 200 实例**：[AGREE]，与我的 R2-W4 一致——证据过于单薄，不足以支撑关于 frontier models 的 claims。
- **Figure 1 信息密度过高**：[REBUT]，我认为 Figure 1 的高密度是优势而非劣势——它为全文提供了有效的 roadmap，读者可以在阅读各 section 时回来参考。双栏格式下能在一个 figure 中呈现全貌是有价值的。不过承认在首次阅读时可能需要时间消化。
- **Table 2 引用不一致**：[AGREE]，如果存在引用格式不一致应该修正。

---

### R1 Missing References

- **Li et al. (2024) SC for structured prediction**：[AGREE]，如果该文直接研究 SC 在结构化预测中的行为，属于直接相关工作，应引用。
- **Yao et al. (2024) Tree of Thoughts, Sel et al. Algorithm of Thoughts**：部分同意。ToT/AoT 是 test-time compute scaling 的重要方法，但它们主要针对 reasoning tasks 而非 IE/NER。在 §8 Related Work 中简要提及它们作为 "alternative TTS approaches beyond self-consistency" 是合理的，但不需要深入对比。

---

### 总结

R1 的 7 个 Must-Fix/Should-Fix 中，我 **全部同意或部分同意**。特别值得注意的是：

1. **R1-W2（训练 epoch 混淆变量）** 是一个我在自己审稿中未充分关注的有效观察，直接影响论文唯一正面结果（Few-NERD LP selection）的可信度。
2. **R1-N1（全局多重比较）** 和 **R1-N2（SciERC power）** 共同指向一个更深层的问题：论文的正面发现（"这个方法在某些条件下有效"）在统计上比负面发现（"大多数方法无效"）脆弱得多。
3. **R1-W1（cascade 术语）** 和 **R1-W4（scope mismatch）** 与我自己的 R2-W2 和 R2-N1 完全一致，两位 reviewer 独立发现相同问题增强了这些关切的权重。

R1 的审稿严谨度很高，特别是统计方法论层面的关切（N1, N2, W5）为我的审稿提供了有价值的补充视角。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 3888 · 2026-05-22T11:09:32.840201+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool call

_source line 3889 · 2026-05-22T11:09:32.840697+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 3890 · 2026-05-22T11:09:32.991756+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T10:55:42.325233+00:00\", \"completed_at\": \"2026-05-22T11:00:42.710694+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent timed out after 300s\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 3891 · 2026-05-22T11:09:32.992220+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 3892 · 2026-05-22T11:11:56.079082+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n# ===== ROUND 36 MUST-FIX (共识) =====\n- id: R35-N1\n  summary: \"Scope overclaim: 标题声称 'Information Extraction' 但证据 ~95% 是 NER\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 33\n  last_seen_round: 36\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"R1-W4: RE/SQL 覆盖有限。当时为 warning。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"继续作为 warning。\"\n    - round: 35\n      reviewers: [1, 2]\n      note: \"双方升级为 Critical Must-Fix。标题从 'Structured Prediction' 改为 'Information Extraction'。\"\n    - round: 36\n      reviewers: [1, 2]\n      note: \"双方再次共识为 Critical Must-Fix。标题 'Information Extraction' 仍超出证据范围：NER 4 数据集完整分析，RE 仅 SciERC 1 个数据集 exploratory (n=397)，SQL 仅一句话 (n=196)。建议改为 'Named Entity Recognition' 或 'NER with exploratory IE extensions'。\"\n  action_items:\n    - round: 35\n      action: \"标题改为 'Boundary Conditions for Information Extraction'；全文收窄 scope claims\"\n      assigned_to: paper_agent\n      status: done\n    - round: 36\n      action: \"标题进一步改为 'Boundary Conditions for Named Entity Recognition' 或在标题中限定 NER 为主\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R36-N1\n  summary: \"核心正面发现（LP selection/construction on Few-NERD）在全局 Holm-Bonferroni (k=57) 下仅 p_adj=0.055，应在正文讨论\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"双方共识。R1 首先提出，R2 同意但指出 per-family correction 是标准做法。论文在 Appendix Table 12 报告了全局校正结果但正文仅使用 per-family 校正。Prescriptive claims (§7.5) 建立在统计边缘结果上。\"\n  action_items:\n    - round: 36\n      action: \"在 §7 正文中明确讨论全局 Holm-Bonferroni p_adj=0.055 的边缘性；将 prescriptive results 定位为 exploratory 而非 confirmatory\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-N2\n  summary: \"SciERC 仅 n=529、大部分分析单 seed，统计 power 有限\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - round: 35\n      reviewers: [1, 2]\n      note: \"共识：SciERC 分析最详尽但单 seed + 529 实例 power 有限。\"\n    - round: 36\n      reviewers: [1, 2]\n      note: \"R1 再次提出，R2 同意。MDE≈1.5pp 而观测效果 +0.2pp 远低于 MDE。多数据集设计部分缓解但 SciERC-specific 诊断细节可靠性打折。\"\n  action_items:\n    - round: 35\n      action: \"Discussion 标记 SciERC 结论为 tentative + 尝试补 2 额外 seeds\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 36\n      action: \"在正文（非仅 Limitations）讨论 power 限制对 SciERC 结论的含义；报告 TOST 结果在正文中\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== ROUND 36 SHOULD-FIX (共识) =====\n- id: R36-W1\n  summary: \"'Diagnostic cascade' 术语误导因果解读，应改为 'diagnostic framework/checklist'\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"双方独立发现并强烈共识。§4 承认 R²<0、stages 不可分解为独立效应，与 cascade（暗示顺序依赖）矛盾。Viola-Jones cascade 等技术用法进一步支持改名。实际是两个需同时满足的必要条件（低 degeneracy + 高 LP-F1 alignment），非顺序筛选。\"\n  action_items:\n    - round: 36\n      action: \"全文将 'diagnostic cascade' 改为 'diagnostic framework' 或 'diagnostic checklist'，首次使用时明确定义\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R36-W2\n  summary: \"Few-NERD 使用 3 epochs（其余 5 epochs）构成混淆变量，唯一正面结果的可信度受影响\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"R1 首先发现，R2 交叉回应中同意并补充分析。5-epoch 使 Few-NERD degeneracy 从 13% 升至 31%、LP 增益减半。Few-NERD 的低 degeneracy 可能部分是 undertraining 产物，非数据集固有属性。论文在 Appendix u 有数据但未将其框架化为混淆变量。\"\n  action_items:\n    - round: 36\n      action: \"在正文（§7 或 Limitations）明确讨论 epoch 差异作为混淆变量；报告 Few-NERD 5-epoch LP selection 结果\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R36-W3\n  summary: \"Novelty 定位不够准确：应强调 'systematic diagnosis in new domain' 而非暗示发现全新现象\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"R2 列为 Must-Fix，R1 部分反驳建议降为 Should-Fix。R1 认为诊断框架本身有原创性（9 方法类别系统测试、LP compression 机制解析），但同意论文应更精确定位：不是发现全新现象，而是首次为结构化 IE 输出提供完整量化诊断框架。最终共识：Should-Fix（framing 问题非 soundness 问题）。\"\n  action_items:\n    - round: 36\n      action: \"§1 明确区分：(a) SC 失效作为一般现象是已知的（cite Chen et al., Yun & Price），(b) 本文贡献是 NER 领域首个系统化诊断框架\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-W4\n  summary: \"Related Work 缺失 conformal prediction、token-level uncertainty、structured MBR 等方向\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 36\n  mentions:\n    - round: 35\n      reviewers: [1, 2]\n      note: \"新增：conformal prediction for NLP、token-level uncertainty decomposition、MBR with entity-level F1 utility。\"\n    - round: 36\n      reviewers: [1, 2]\n      note: \"R2 详列 4 个缺失方向：conformal prediction (Fisch et al. 2021, Angelopoulos & Bates 2023)、token-level uncertainty、trained verifiers 更广泛讨论、structured MBR (Chen et al. 2025)。R1 大部分同意，指出 token-level 已有部分覆盖（LP + 1D CNN aggregator）。\"\n  action_items:\n    - round: 35\n      action: \"Section 8 增 1 段覆盖 conformal prediction、token-level uncertainty、MBR\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 36\n      action: \"§8 增加 conformal prediction、token-level uncertainty for sequence labeling、structured MBR 讨论段落\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-W2\n  summary: \"Capability-diversity tension 证据不足以支撑 claim 强度\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - round: 35\n      reviewers: [1, 2]\n      note: \"共识：Figure 3 不够，缺乏可操作定义。\"\n    - round: 36\n      reviewers: [1, 2]\n      note: \"R2 列为 Should-Fix：模型规模 4B-14B 有限，GPT-5.5 仅 200 实例 zero-shot，72B 仅 preliminary。R1 同意但认为严重性略低：跨 2 家族 + 3 scale + frontier 有一定支撑。共识：弱化为 'observed tendency' 而非 'structural constraint'。\"\n  action_items:\n    - round: 35\n      action: \"CDT 从 'central finding' 降级为 'observed pattern'；cascade 升级为 primary contribution\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 36\n      action: \"将 CDT 进一步弱化为 'observed tendency within tested scales'，Abstract 移除 'extends beyond NER' 或加限定\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R36-W4\n  summary: \"§3 自验证实验使用 Qwen2.5-7B 而非主模型 Qwen3-8B，方法论不一致\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"R1 首先提出，R2 同意为 moderate concern。ESJ/MRSC/LSC 使用不同模型家族，结论方向一致但严谨性要求使用相同模型或讨论原因。\"\n  action_items:\n    - round: 36\n      action: \"在 §3 讨论为何使用 Qwen2.5-7B 而非 Qwen3-8B，以及结论的推广性\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R36-W5\n  summary: \"Constrained decoding 对 LP compression 的贡献缺少 constrained vs free-form 直接定量对比\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"R1 首先提出，R2 同意。Appendix q 有 free-form F1 对比但缺少 LP range/tied fraction 的直接定量对比。\"\n  action_items:\n    - round: 36\n      action: \"补充 constrained vs free-form 模式下 LP within-instance variance/range/tied fraction 的直接对比数据\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R36-W6\n  summary: \"Responsible NLP Checklist 不应出现在 PDF 中（ARR 规定在 OpenReview 表单填写）\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"双方共识。当前 PDF pages 9-10 包含完整 checklist（~1.5 页），应移除。\"\n  action_items:\n    - round: 36\n      action: \"从 PDF 移除 Responsible NLP Research Checklist section，内容迁移至 OpenReview 表单\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-W5\n  summary: \"Proposition 1 entity independence 假设与数据不符，bound 过松（actual/bound ratio 3-12%）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 36\n  mentions:\n    - round: 35\n      reviewers: [1, 2]\n      note: \"双方 AGREE。Split-half r=0.578-0.644，bound ratio 0.13-0.63。降格为 illustrative bound。\"\n    - round: 36\n      reviewers: [1, 2]\n      note: \"R2 认为理论分析指导价值有限且 §6 叙事突兀。R1 反驳：诊断价值不依赖 bound tightness，MBR 联系和 α_crit 有独立贡献。分歧存在但双方同意改善 §6 结构组织。\"\n  action_items:\n    - round: 35\n      action: \"Proposition 1 降格为 illustrative upper bound\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 36\n      action: \"改善 §6 结构组织使理论分析与实证叙事更好衔接；更明确讨论 bound 松紧度的 implications\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== ROUND 36 小问题 =====\n- id: R36-M1\n  summary: \"Abstract 'ρ < 1 pp' 措辞混淆（ρ 是相关系数，此处表示增益）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"双方同意。应改为 'gain < 1 pp' 或 'Δ < 1 pp'。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ===== ROUND 35 未被提及（可能已修复） =====\n- id: R35-W1\n  summary: \"正文超出 8 页限制（Conclusion 溢出到 Page 9）\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 35\n  last_seen_round: 35\n  mentions:\n    - round: 35\n      reviewers: [1, 2]\n      note: \"Section 9 Discussion/Conclusion 延续到 p.9 顶部。EMNLP 2026：正文 8 页。\"\n    - round: 36\n      reviewers: []\n      note: \"本轮未提及，可能已修复，待 Research Director 确认。但 checklist 仍在 PDF 中占 ~1.5 页（R36-W6）。\"\n  action_items:\n    - round: 35\n      action: \"压缩 Related Work + Discussion + Limitations 以确保正文在 Page 8 内\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-W3\n  summary: \"与 Yun & Price (2025) 差异化论述不充分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 34\n  last_seen_round: 36\n  mentions:\n    - round: 35\n      reviewers: [1, 2]\n      note: \"'signal alignment collapse' 与 'format diversity collapse' 语义高度重叠。\"\n    - round: 36\n      reviewers: [1, 2]\n      note: \"被 R36-W3（novelty positioning）覆盖。R1 反驳认为诊断框架有原创性，但同意需更精确定位。\"\n  action_items:\n    - round: 35\n      action: \"Section 8 增 1-2 段：alignment collapse vs format diversity collapse 定义级区别 + cascade 增量\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-W6\n  summary: \"Free-form decoding ablation 缺少 Few-NERD\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 34\n  last_seen_round: 35\n  mentions:\n    - round: 35\n      reviewers: [1, 2]\n      note: \"Reviewer #127 认为 CoNLL+SciERC 已充分证明。\"\n    - round: 36\n      reviewers: []\n      note: \"本轮未提及。R36-W5 聚焦于 LP compression 定量对比而非数据集覆盖。\"\n  action_items:\n    - round: 35\n      action: \"降级为 camera-ready 补充。\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-W7\n  summary: \"诊断 cascade 阈值的 task-specificity 未讨论\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 35\n  last_seen_round: 35\n  mentions:\n    - round: 35\n      reviewers: [1, 2]\n      note: \"SciERC 12% vs WNUT-17 51% degeneracy，cascade 阈值稳定性未讨论。\"\n    - round: 36\n      reviewers: []\n      note: \"本轮未直接提及，但 R36-W1（cascade 术语）间接覆盖。\"\n  action_items:\n    - round: 35\n      action: \"Discussion 讨论阈值 task-specificity\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-W8\n  summary: \"Limitations N-budget 描述过时\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 35\n  last_seen_round: 35\n  mentions:\n    - round: 35\n      reviewers: [internal]\n      note: \"Reviewer #127 发现。limitations.tex 写 'N≤32' 但已有 N=64 结果。\"\n    - round: 36\n      reviewers: []\n      note: \"本轮未提及，可能已修复，待确认。\"\n  action_items:\n    - round: 35\n      action: \"更新 limitations.tex 中 N-budget 描述为 N≤64\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-W9\n  summary: \"Limitations 过长（~15 个点），违反用户规则（3 个点左右）\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 35\n  last_seen_round: 35\n  mentions:\n    - round: 35\n      reviewers: [internal]\n      note: \"28 行 ~15 个 limitation 点。\"\n    - round: 36\n      reviewers: []\n      note: \"本轮 Limitations 文本已精简为 ~3 段，可能已修复，待确认。\"\n  action_items:\n    - round: 35\n      action: \"压缩为 3-4 个核心 limitation\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ===== RESOLVED（历史） =====\n- id: R1-N1\n  summary: \"θ_crit=0.70 阈值缺乏 held-out 验证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [1]\n      note: \"R1 认为 Must-Fix。\"\n    - round: 35\n      reviewers: []\n      note: \"未被提及。Reviewer #127 确认：θ sweep 完成。\"\n  action_items:\n    - round: 33\n      action: \"sweep θ∈{0.60,0.65,0.70,0.75,0.80}\"\n      assigned_to: agent\n      status: done\n  resolution: \"θ sweep 完成，结论稳定。\"\n  resolution_round: 35\n\n- id: R1-N3\n  summary: \"Entity construction 作为 prescriptive contribution 证据不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 35\n      reviewers: []\n      note: \"Reviewer #127 确认：已标记为 exploratory。\"\n  action_items:\n    - round: 33\n      action: \"降级 construction 为 exploratory result\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Construction 已标记为 exploratory。\"\n  resolution_round: 35\n\n- id: R2-W1\n  summary: \"Entity-level construction 与 Xie et al. (2023) 差异不清晰\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 35\n      reviewers: []\n      note: \"Reviewer #127 确认：Related work 已有显式差异化段落。\"\n  action_items:\n    - round: 33\n      action: \"§6.1 增加与 Xie et al. 显式对比\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Related Work 已有显式差异化段落。\"\n  resolution_round: 35\n\n- id: R2-W3\n  summary: \"Framework vs empirical study 定位模糊\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 35\n      reviewers: []\n      note: \"被 R35-N1 scope 修复覆盖。\"\n  action_items:\n    - round: 34\n      action: \"Framing 调整：强化 empirical characterization 定位\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"标题已改为 Boundary Conditions。\"\n  resolution_round: 35\n\n- id: R34-N1\n  summary: \"全局 Holm-Bonferroni (k=57) 下核心 claim 不显著\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  mentions:\n    - round: 34\n      reviewers: [1, 2]\n      note: \"双方共识：主文需透明报告。\"\n    - round: 35\n      reviewers: []\n      note: \"Reviewer #127 确认：limitations.tex BH FDR 19/57 讨论完整。\"\n    - round: 36\n      reviewers: [1, 2]\n      note: \"升级为 R36-N1：虽然 Limitations 已讨论，但正文中仍仅使用 per-family 校正，需要在 §7 正文中明确讨论。\"\n  action_items:\n    - round: 34\n      action: \"主文增加全局 Holm-Bonferroni 结果\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Limitations 已报告，但正文讨论不足 → 见 R36-N1\"\n  resolution_round: null\n\n- id: R2-M1\n  summary: \"Table 1 '2-seed' vs 正文 '3-seed' 不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 36\n      reviewers: []\n      note: \"本轮未提及，可能已修复。\"\n  action_items:\n    - round: 33\n      action: \"统一 seed 数量描述\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "issues_yaml": "issues:\n# ===== ROUND 36 MUST-FIX (共识) =====\n- id: R35-N1\n  summary: \"Scope overclaim: 标题声称 'Information Extraction' 但证据 ~95% 是 NER\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 33\n  last_seen_round: 36\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"R1-W4: RE/SQL 覆盖有限。当时为 warning。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"继续作为 warning。\"\n    - round: 35\n      reviewers: [1, 2]\n      note: \"双方升级为 Critical Must-Fix。标题从 'Structured Prediction' 改为 'Information Extraction'。\"\n    - round: 36\n      reviewers: [1, 2]\n      note: \"双方再次共识为 Critical Must-Fix。标题 'Information Extraction' 仍超出证据范围：NER 4 数据集完整分析，RE 仅 SciERC 1 个数据集 exploratory (n=397)，SQL 仅一句话 (n=196)。建议改为 'Named Entity Recognition' 或 'NER with exploratory IE extensions'。\"\n  action_items:\n    - round: 35\n      action: \"标题改为 'Boundary Conditions for Information Extraction'；全文收窄 scope claims\"\n      assigned_to: paper_agent\n      status: done\n    - round: 36\n      action: \"标题进一步改为 'Boundary Conditions for Named Entity Recognition' 或在标题中限定 NER 为主\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R36-N1\n  summary: \"核心正面发现（LP selection/construction on Few-NERD）在全局 Holm-Bonferroni (k=57) 下仅 p_adj=0.055，应在正文讨论\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"双方共识。R1 首先提出，R2 同意但指出 per-family correction 是标准做法。论文在 Appendix Table 12 报告了全局校正结果但正文仅使用 per-family 校正。Prescriptive claims (§7.5) 建立在统计边缘结果上。\"\n  action_items:\n    - round: 36\n      action: \"在 §7 正文中明确讨论全局 Holm-Bonferroni p_adj=0.055 的边缘性；将 prescriptive results 定位为 exploratory 而非 confirmatory\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-N2\n  summary: \"SciERC 仅 n=529、大部分分析单 seed，统计 power 有限\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - round: 35\n      reviewers: [1, 2]\n      note: \"共识：SciERC 分析最详尽但单 seed + 529 实例 power 有限。\"\n    - round: 36\n      reviewers: [1, 2]\n      note: \"R1 再次提出，R2 同意。MDE≈1.5pp 而观测效果 +0.2pp 远低于 MDE。多数据集设计部分缓解但 SciERC-specific 诊断细节可靠性打折。\"\n  action_items:\n    - round: 35\n      action: \"Discussion 标记 SciERC 结论为 tentative + 尝试补 2 额外 seeds\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 36\n      action: \"在正文（非仅 Limitations）讨论 power 限制对 SciERC 结论的含义；报告 TOST 结果在正文中\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== ROUND 36 SHOULD-FIX (共识) =====\n- id: R36-W1\n  summary: \"'Diagnostic cascade' 术语误导因果解读，应改为 'diagnostic framework/checklist'\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"双方独立发现并强烈共识。§4 承认 R²<0、stages 不可分解为独立效应，与 cascade（暗示顺序依赖）矛盾。Viola-Jones cascade 等技术用法进一步支持改名。实际是两个需同时满足的必要条件（低 degeneracy + 高 LP-F1 alignment），非顺序筛选。\"\n  action_items:\n    - round: 36\n      action: \"全文将 'diagnostic cascade' 改为 'diagnostic framework' 或 'diagnostic checklist'，首次使用时明确定义\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R36-W2\n  summary: \"Few-NERD 使用 3 epochs（其余 5 epochs）构成混淆变量，唯一正面结果的可信度受影响\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"R1 首先发现，R2 交叉回应中同意并补充分析。5-epoch 使 Few-NERD degeneracy 从 13% 升至 31%、LP 增益减半。Few-NERD 的低 degeneracy 可能部分是 undertraining 产物，非数据集固有属性。论文在 Appendix u 有数据但未将其框架化为混淆变量。\"\n  action_items:\n    - round: 36\n      action: \"在正文（§7 或 Limitations）明确讨论 epoch 差异作为混淆变量；报告 Few-NERD 5-epoch LP selection 结果\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R36-W3\n  summary: \"Novelty 定位不够准确：应强调 'systematic diagnosis in new domain' 而非暗示发现全新现象\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"R2 列为 Must-Fix，R1 部分反驳建议降为 Should-Fix。R1 认为诊断框架本身有原创性（9 方法类别系统测试、LP compression 机制解析），但同意论文应更精确定位：不是发现全新现象，而是首次为结构化 IE 输出提供完整量化诊断框架。最终共识：Should-Fix（framing 问题非 soundness 问题）。\"\n  action_items:\n    - round: 36\n      action: \"§1 明确区分：(a) SC 失效作为一般现象是已知的（cite Chen et al., Yun & Price），(b) 本文贡献是 NER 领域首个系统化诊断框架\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-W4\n  summary: \"Related Work 缺失 conformal prediction、token-level uncertainty、structured MBR 等方向\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 36\n  mentions:\n    - round: 35\n      reviewers: [1, 2]\n      note: \"新增：conformal prediction for NLP、token-level uncertainty decomposition、MBR with entity-level F1 utility。\"\n    - round: 36\n      reviewers: [1, 2]\n      note: \"R2 详列 4 个缺失方向：conformal prediction (Fisch et al. 2021, Angelopoulos & Bates 2023)、token-level uncertainty、trained verifiers 更广泛讨论、structured MBR (Chen et al. 2025)。R1 大部分同意，指出 token-level 已有部分覆盖（LP + 1D CNN aggregator）。\"\n  action_items:\n    - round: 35\n      action: \"Section 8 增 1 段覆盖 conformal prediction、token-level uncertainty、MBR\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 36\n      action: \"§8 增加 conformal prediction、token-level uncertainty for sequence labeling、structured MBR 讨论段落\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-W2\n  summary: \"Capability-diversity tension 证据不足以支撑 claim 强度\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 35\n  last_seen_round: 36\n  mentions:\n    - round: 35\n      reviewers: [1, 2]\n      note: \"共识：Figure 3 不够，缺乏可操作定义。\"\n    - round: 36\n      reviewers: [1, 2]\n      note: \"R2 列为 Should-Fix：模型规模 4B-14B 有限，GPT-5.5 仅 200 实例 zero-shot，72B 仅 preliminary。R1 同意但认为严重性略低：跨 2 家族 + 3 scale + frontier 有一定支撑。共识：弱化为 'observed tendency' 而非 'structural constraint'。\"\n  action_items:\n    - round: 35\n      action: \"CDT 从 'central finding' 降级为 'observed pattern'；cascade 升级为 primary contribution\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 36\n      action: \"将 CDT 进一步弱化为 'observed tendency within tested scales'，Abstract 移除 'extends beyond NER' 或加限定\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R36-W4\n  summary: \"§3 自验证实验使用 Qwen2.5-7B 而非主模型 Qwen3-8B，方法论不一致\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"R1 首先提出，R2 同意为 moderate concern。ESJ/MRSC/LSC 使用不同模型家族，结论方向一致但严谨性要求使用相同模型或讨论原因。\"\n  action_items:\n    - round: 36\n      action: \"在 §3 讨论为何使用 Qwen2.5-7B 而非 Qwen3-8B，以及结论的推广性\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R36-W5\n  summary: \"Constrained decoding 对 LP compression 的贡献缺少 constrained vs free-form 直接定量对比\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"R1 首先提出，R2 同意。Appendix q 有 free-form F1 对比但缺少 LP range/tied fraction 的直接定量对比。\"\n  action_items:\n    - round: 36\n      action: \"补充 constrained vs free-form 模式下 LP within-instance variance/range/tied fraction 的直接对比数据\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R36-W6\n  summary: \"Responsible NLP Checklist 不应出现在 PDF 中（ARR 规定在 OpenReview 表单填写）\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"双方共识。当前 PDF pages 9-10 包含完整 checklist（~1.5 页），应移除。\"\n  action_items:\n    - round: 36\n      action: \"从 PDF 移除 Responsible NLP Research Checklist section，内容迁移至 OpenReview 表单\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-W5\n  summary: \"Proposition 1 entity independence 假设与数据不符，bound 过松（actual/bound ratio 3-12%）\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 36\n  mentions:\n    - round: 35\n      reviewers: [1, 2]\n      note: \"双方 AGREE。Split-half r=0.578-0.644，bound ratio 0.13-0.63。降格为 illustrative bound。\"\n    - round: 36\n      reviewers: [1, 2]\n      note: \"R2 认为理论分析指导价值有限且 §6 叙事突兀。R1 反驳：诊断价值不依赖 bound tightness，MBR 联系和 α_crit 有独立贡献。分歧存在但双方同意改善 §6 结构组织。\"\n  action_items:\n    - round: 35\n      action: \"Proposition 1 降格为 illustrative upper bound\"\n      assigned_to: paper_agent\n      status: in_progress\n    - round: 36\n      action: \"改善 §6 结构组织使理论分析与实证叙事更好衔接；更明确讨论 bound 松紧度的 implications\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== ROUND 36 小问题 =====\n- id: R36-M1\n  summary: \"Abstract 'ρ < 1 pp' 措辞混淆（ρ 是相关系数，此处表示增益）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 36\n  last_seen_round: 36\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"双方同意。应改为 'gain < 1 pp' 或 'Δ < 1 pp'。\"\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ===== ROUND 35 未被提及（可能已修复） =====\n- id: R35-W1\n  summary: \"正文超出 8 页限制（Conclusion 溢出到 Page 9）\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 35\n  last_seen_round: 35\n  mentions:\n    - round: 35\n      reviewers: [1, 2]\n      note: \"Section 9 Discussion/Conclusion 延续到 p.9 顶部。EMNLP 2026：正文 8 页。\"\n    - round: 36\n      reviewers: []\n      note: \"本轮未提及，可能已修复，待 Research Director 确认。但 checklist 仍在 PDF 中占 ~1.5 页（R36-W6）。\"\n  action_items:\n    - round: 35\n      action: \"压缩 Related Work + Discussion + Limitations 以确保正文在 Page 8 内\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-W3\n  summary: \"与 Yun & Price (2025) 差异化论述不充分\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 34\n  last_seen_round: 36\n  mentions:\n    - round: 35\n      reviewers: [1, 2]\n      note: \"'signal alignment collapse' 与 'format diversity collapse' 语义高度重叠。\"\n    - round: 36\n      reviewers: [1, 2]\n      note: \"被 R36-W3（novelty positioning）覆盖。R1 反驳认为诊断框架有原创性，但同意需更精确定位。\"\n  action_items:\n    - round: 35\n      action: \"Section 8 增 1-2 段：alignment collapse vs format diversity collapse 定义级区别 + cascade 增量\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-W6\n  summary: \"Free-form decoding ablation 缺少 Few-NERD\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 34\n  last_seen_round: 35\n  mentions:\n    - round: 35\n      reviewers: [1, 2]\n      note: \"Reviewer #127 认为 CoNLL+SciERC 已充分证明。\"\n    - round: 36\n      reviewers: []\n      note: \"本轮未提及。R36-W5 聚焦于 LP compression 定量对比而非数据集覆盖。\"\n  action_items:\n    - round: 35\n      action: \"降级为 camera-ready 补充。\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-W7\n  summary: \"诊断 cascade 阈值的 task-specificity 未讨论\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 35\n  last_seen_round: 35\n  mentions:\n    - round: 35\n      reviewers: [1, 2]\n      note: \"SciERC 12% vs WNUT-17 51% degeneracy，cascade 阈值稳定性未讨论。\"\n    - round: 36\n      reviewers: []\n      note: \"本轮未直接提及，但 R36-W1（cascade 术语）间接覆盖。\"\n  action_items:\n    - round: 35\n      action: \"Discussion 讨论阈值 task-specificity\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-W8\n  summary: \"Limitations N-budget 描述过时\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 35\n  last_seen_round: 35\n  mentions:\n    - round: 35\n      reviewers: [internal]\n      note: \"Reviewer #127 发现。limitations.tex 写 'N≤32' 但已有 N=64 结果。\"\n    - round: 36\n      reviewers: []\n      note: \"本轮未提及，可能已修复，待确认。\"\n  action_items:\n    - round: 35\n      action: \"更新 limitations.tex 中 N-budget 描述为 N≤64\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-W9\n  summary: \"Limitations 过长（~15 个点），违反用户规则（3 个点左右）\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 35\n  last_seen_round: 35\n  mentions:\n    - round: 35\n      reviewers: [internal]\n      note: \"28 行 ~15 个 limitation 点。\"\n    - round: 36\n      reviewers: []\n      note: \"本轮 Limitations 文本已精简为 ~3 段，可能已修复，待确认。\"\n  action_items:\n    - round: 35\n      action: \"压缩为 3-4 个核心 limitation\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ===== RESOLVED（历史） =====\n- id: R1-N1\n  summary: \"θ_crit=0.70 阈值缺乏 held-out 验证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [1]\n      note: \"R1 认为 Must-Fix。\"\n    - round: 35\n      reviewers: []\n      note: \"未被提及。Reviewer #127 确认：θ sweep 完成。\"\n  action_items:\n    - round: 33\n      action: \"sweep θ∈{0.60,0.65,0.70,0.75,0.80}\"\n      assigned_to: agent\n      status: done\n  resolution: \"θ sweep 完成，结论稳定。\"\n  resolution_round: 35\n\n- id: R1-N3\n  summary: \"Entity construction 作为 prescriptive contribution 证据不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 35\n      reviewers: []\n      note: \"Reviewer #127 确认：已标记为 exploratory。\"\n  action_items:\n    - round: 33\n      action: \"降级 construction 为 exploratory result\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Construction 已标记为 exploratory。\"\n  resolution_round: 35\n\n- id: R2-W1\n  summary: \"Entity-level construction 与 Xie et al. (2023) 差异不清晰\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 35\n      reviewers: []\n      note: \"Reviewer #127 确认：Related work 已有显式差异化段落。\"\n  action_items:\n    - round: 33\n      action: \"§6.1 增加与 Xie et al. 显式对比\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Related Work 已有显式差异化段落。\"\n  resolution_round: 35\n\n- id: R2-W3\n  summary: \"Framework vs empirical study 定位模糊\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 35\n      reviewers: []\n      note: \"被 R35-N1 scope 修复覆盖。\"\n  action_items:\n    - round: 34\n      action: \"Framing 调整：强化 empirical characterization 定位\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"标题已改为 Boundary Conditions。\"\n  resolution_round: 35\n\n- id: R34-N1\n  summary: \"全局 Holm-Bonferroni (k=57) 下核心 claim 不显著\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 34\n  last_seen_round: 34\n  mentions:\n    - round: 34\n      reviewers: [1, 2]\n      note: \"双方共识：主文需透明报告。\"\n    - round: 35\n      reviewers: []\n      note: \"Reviewer #127 确认：limitations.tex BH FDR 19/57 讨论完整。\"\n    - round: 36\n      reviewers: [1, 2]\n      note: \"升级为 R36-N1：虽然 Limitations 已讨论，但正文中仍仅使用 per-family 校正，需要在 §7 正文中明确讨论。\"\n  action_items:\n    - round: 34\n      action: \"主文增加全局 Holm-Bonferroni 结果\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Limitations 已报告，但正文讨论不足 → 见 R36-N1\"\n  resolution_round: null\n\n- id: R2-M1\n  summary: \"Table 1 '2-seed' vs 正文 '3-seed' 不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 36\n      reviewers: []\n      note: \"本轮未提及，可能已修复。\"\n  action_items:\n    - round: 33\n      action: \"统一 seed 数量描述\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 3893 · 2026-05-22T11:11:56.180236+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 15797}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 3894 · 2026-05-22T11:14:16.137850+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "struct_self_consist_ie",
  "report": "# 审稿报告 — Round 36 (Fresh)\n\n**论文**: \"When Does Test-Time Scaling Fail? Boundary Conditions for Information Extraction\"\n**Venue**: EMNLP 2026 (Long Paper, via ARR)\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性+写作）\n**轮次**: Round 1（1 轮独立审稿 + 1 轮交叉分享，关键问题达成共识）\n\n---\n\n## Summary\n\n本文研究 test-time compute scaling（self-consistency / best-of-N）在信息抽取中何时失效，以 NER 为主要案例（4 数据集、2 模型家族），附带 RE 和 SQL 的探索性扩展。核心发现是 \"correlation-selection gap\"：质量估计信号能预测输出质量（AUROC ≤0.82），但 instance-level 选择增益 <1 pp。论文提出四阶段诊断框架，将失效归因于 output degeneracy（12-68%）和 signal alignment collapse（α→0）。作为探索性改进，LP-weighted entity-level construction 在 Few-NERD 上获得 +1.40 pp（Holm p_adj=0.006, per-family k=10; 全局 k=57 下 p_adj=0.055）。实验覆盖 9 个方法类别、N=2-64 scaling、4B-72B model scale ablation，附录达 46 页。\n\n---\n\n## Strengths\n\n**S1. 极为全面的实证调查 [共识]**\n9 个方法类别、5 个 confidence signals、4 个 NER 数据集、2 个模型家族（Qwen3-8B, LLaMA-3.1-8B）、N=2-64 scaling、4B-72B 规模消融、free-form decoding 消融。46 页附录覆盖 60+ 张表格和 10+ 张图。这可能是目前对 NER 中 self-consistency 行为最详尽的实证研究。\n\n**S2. 统计方法论严谨且诚实 [共识]**\nHolm-Bonferroni (k=57)、BH FDR、bootstrap 95% CI、paired bootstrap p-values、TOST 等效检验、power analysis——论文不仅使用了这些方法，还诚实报告了核心发现在全局校正下的边缘状态（p_adj=0.055）。这种统计透明度在 NLP 实证论文中罕见。\n\n**S3. Correlation-selection gap 有实质贡献 [共识]**\nQuality estimation ρ 可达 0.38-0.45 但不转化为 selection gain（Table 3/Table 1），这一发现清晰、可复现，对 test-time scaling 的实践部署有直接指导意义。\n\n**S4. 实用的诊断框架 [共识]**\n即便术语有待商榷（见 W3），degeneracy/headroom/compression/alignment 四要素分解为从业者提供了可操作的预部署检查清单——\"先检查 degeneracy rate，若 >50% 则不值得做 selection\"。\n\n**S5. 负面结果的系统化呈现 [共识]**\n论文系统排除了 ESJ、MRSC、LSC、supervised combination、trained verifier 等多种潜在方案，充分论证了问题的结构性（structural bottleneck）。\n\n**S6. 跨模型家族一致性 [共识]**\nQwen3-8B 和 LLaMA-3.1-8B 结果高度一致，加上 4B/14B 消融和 GPT-5.5 frontier 证据，增强了发现的泛化性。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [Critical, 共识] 标题范围显著超出实际证据**\n标题 \"Boundary Conditions for Information Extraction\" 暗示对 IE 各子任务的全面研究。实际证据 ~95% 来自 NER（4 数据集 × 2 模型家族完整分析）。RE 仅有 SciERC 1 个数据集的探索性结果（n=397, single seed），SQL 仅在 Discussion 中一句话提及（n=196）。NER 的 set-valued output 与 RE 的 tuple-valued output 有本质结构差异——论文自己在 §7.3 观察到 RE 的失效机制不同（40% zero-F1 来自上游 entity span 错误）。\n→ **建议**: 标题改为 \"Boundary Conditions for Named Entity Recognition\" 或 \"...for Information Extraction: Evidence from NER\"。\n\n**MF2. [Critical, 共识] 核心正面发现在全局多重比较校正下边缘不显著**\nFew-NERD LP selection (+1.39pp) 和 LP-weighted construction (+1.40pp) 在全局 Holm-Bonferroni (k=57) 下 p_adj=0.055，未通过 α=0.05。正文仅使用 per-family 校正（k=21/k=10），全局结果仅在附录 Table 12 中报告。Per-family correction 在统计学中是可辩护的标准做法，但 §7.5 的 prescriptive 建议建立在这个统计边缘的结果之上。\n→ **建议**: (1) 在 §7 正文中明确讨论全局校正下 p_adj=0.055 的边缘性；(2) 将 prescriptive results 定位为 exploratory 而非 confirmatory；(3) 强调核心贡献是 diagnostic framework（负面结论），而非 LP construction（正面结论）。\n\n**MF3. [Critical, 共识] SciERC 作为主要测试平台统计 power 有限**\nSciERC (n=529) 是论文多项核心分析的主要测试平台（Table 3 quality estimation、Table 1 selection gap、§4 diagnostic analysis），但仅单 seed 且 power analysis 显示 MDE≈1.5pp，而观测效果 +0.2pp 远低于 MDE。不影响 \"no signal beats greedy\" 结论，但影响 SciERC-specific 诊断细节的可靠性。多数据集设计（CoNLL n=3453, Few-NERD n=32560）部分缓解。\n→ **建议**: (1) 在正文讨论 power 限制对 SciERC 结论的含义；(2) 报告 TOST 结果在正文中；(3) 补充多 seed 实验增强说服力。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [Warning, 共识] \"Diagnostic cascade\" 术语误导因果解读**\n§4 承认 \"stages resist decomposition into independent effects (R²<0)\" 且 degeneracy 不独立预测 LP gain，这与 \"cascade\"（暗示顺序依赖）矛盾。实际是两个需同时满足的必要条件（低 degeneracy + 高 LP-F1 alignment），非顺序筛选。ML 社区对 \"cascade\" 有明确技术含义（Viola-Jones 等）。\n→ **建议**: 全文改用 \"diagnostic framework\" 或 \"diagnostic checklist\"。\n\n**SF2. [Warning, 共识] Few-NERD 训练 epoch 差异构成混淆变量**\nFew-NERD 是唯一 LP selection 显著正向的数据集（+1.39pp），也是唯一使用 3 epochs（而非 5 epochs）训练的。Appendix u 显示 5-epoch 训练使 degeneracy 从 13% 升至 31%、LP 增益减半。Few-NERD 的低 degeneracy（使 LP selection 成功的关键条件）可能部分是 undertraining 产物。论文在 Appendix 有数据但未将其框架化为混淆变量。\n→ **建议**: 在正文明确讨论 epoch 差异作为混淆变量，报告 Few-NERD 5-epoch LP selection 结果。\n\n**SF3. [Warning, 共识降级] Novelty 定位不够精确**\n\"Correlation-selection gap\" 作为核心发现，calibration ≠ ranking 在决策理论中是已知原则，Chen et al. (2024a) 和 Yun & Price (2025) 已记录 SC 失效。R2 原列为 Must-Fix，R1 反驳认为诊断框架本身有原创性（9 方法类别系统测试、LP compression 机制解析、entity-level partial match 特有 failure mode），非简单 \"新领域应用\"。最终共识降级为 Should-Fix（framing 问题非 soundness 问题）。\n→ **建议**: §1 明确区分：(a) SC 失效作为一般现象是已知的，(b) 本文贡献是 NER 领域首个系统化量化诊断框架。\n\n**SF4. [Warning, 共识] Related Work 缺失直接相关方向**\n缺失：conformal prediction for structured prediction（Fisch et al. 2021, Angelopoulos & Bates 2023）、token-level uncertainty estimation for sequence labeling、trained verifiers 更广泛讨论（Cobbe et al. 2021 在 NER 场景的启示）、structured MBR（Chen et al. 2025）。\n→ **建议**: §8 增加一段覆盖这些方向。\n\n**SF5. [Warning, 共识] Capability-diversity tension 证据不足以支撑 claim 强度**\n模型规模 4B-14B 有限，GPT-5.5 仅 200 实例 zero-shot 单数据集，72B 仅 \"preliminary\"。§9 描述为 \"structural constraint\" 但证据不足。\n→ **建议**: 弱化为 \"observed tendency within tested scales\"，Abstract 移除 \"extends beyond NER\" 或加限定。\n\n**SF6. [Warning, 共识] §3 自验证实验使用不同模型家族**\nESJ/MRSC/LSC 使用 Qwen2.5-7B 而非主模型 Qwen3-8B。\"Models cannot self-verify\" 结论可能不直接推广到主模型。结论方向与主实验负面结果一致，但严谨性要求使用相同模型或讨论原因。\n\n**SF7. [Warning, 共识] Constrained decoding 对 LP compression 贡献未充分量化**\nLP 在 constrained decoding 下压缩严重（60% 实例 LP range < 0.041 nats），但 free-form ablation 中缺少 LP range/tied fraction 的直接定量对比。\n→ **建议**: 补充 constrained vs free-form LP compression 指标对比。\n\n**SF8. [Warning, 共识] Responsible NLP Checklist 不应在 PDF 中**\n按 EMNLP 2026 ARR 规定，checklist 应在 OpenReview 表单中填写。当前 PDF 包含 ~1.5 页 checklist（pages 9-10）。\n→ **建议**: 提交前从 PDF 移除。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 独立发现并完全一致：\n1. 标题范围超出证据（MF1）— 双方列为 critical\n2. Cascade 术语误导（SF1）— 双方独立提出相同关切\n3. Checklist 格式不合规（SF8）— 双方一致\n4. SciERC power 有限（MF3）— R1 提出，R2 完全同意\n5. 全局 Holm 校正边缘（MF2）— R1 提出，R2 同意并补充 per-family 校正辩护\n6. Related Work 缺失（SF4）— R2 详列，R1 大部分同意\n7. Few-NERD epoch 混淆变量（SF2）— R1 发现，R2 交叉回应中高度认可（\"自己审稿中未充分注意到的有效关切\"）\n\n## Reviewer Divergence [REBUT]\n\n1. **R2-N2 (novelty positioning) 的严重性**: R2 列为 Must-Fix (critical)，认为 correlation-selection gap 在更广泛 ML 文献中非全新。R1 反驳（[REBUT]），认为诊断框架本身有原创性——9 个方法类别的系统测试、LP compression 的机制解析远超 \"在新领域观察已知现象\"。R1 建议降级为 Should-Fix。**Director 判断**: 采纳 R1 的降级建议——novelty 问题确实存在但属 framing 层面，非 soundness 缺陷。已在 SF3 中体现。\n\n2. **R2-W5 (理论分析 §6 价值有限)**: R2 认为 Proposition 1 bound 过松（3-12%）、entity independence 假设不成立、§6 叙事突兀。R1 反驳（[REBUT]），认为 bound 的诊断价值不依赖 tightness，MBR 联系和 α_crit 有独立贡献。**Director 判断**: 双方各有道理。Proposition 1 的诊断价值有限但不为零；§6 的结构组织确需改善。已在 SF 中保留为 \"改善 §6 结构衔接\"（issue R35-W5）。\n\n---\n\n## Questions for Authors\n\n1. Few-NERD 使用 3 epochs 而非 5 epochs 是否有特定原因（如过拟合）？是否有 5-epoch Few-NERD 的 LP selection 结果？\n2. §3 的自验证实验选择 Qwen2.5-7B 而非主模型 Qwen3-8B 的原因是什么？\n3. Free-form decoding 下的 LP tied fraction 具体是多少？与 constrained decoding 的 60.3% 如何对比？\n4. 如果 diagnostic cascade 的各阶段不独立（R²<0），那么将 α 识别为 \"bottleneck\" 的结论是否依赖于各因素可分解的假设？\n5. 是否考虑过 token-level uncertainty estimation 作为绕过 entity-level alignment 问题的替代路径？\n6. Entity-level construction 在什么样的 degeneracy rate × alignment 条件组合下可以期望显著增益？\n\n---\n\n## Missing References\n\n- Fisch, A., Schuster, T., Jaakkola, T., & Barzilay, R. (2021). Few-shot conformal prediction with auxiliary tasks. ICML.\n- Angelopoulos, A. N., & Bates, S. (2023). Conformal prediction: A gentle introduction. Foundations and Trends in ML.\n- Token-level uncertainty estimation for sequence labeling 文献（具体文献需作者搜索补充）\n- Chen et al. (2025) Structure-conditional minimum Bayes risk decoding（已引用但 §8 讨论不足）\n- Li et al. (2024) Self-consistency for structured prediction（如直接相关）\n- Yao et al. (2024) Tree of Thoughts / Algorithm of Thoughts（作为 test-time compute 替代方法简要提及）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求（项目未启用外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: Agent 超时（300s timeout）。未产出排版审查结果。如有需要可由用户重新触发。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n**置信度: 4/5**\n\n**评分理由**:\n- R1 给出 3.5（Borderline Conference），R2 给出 3.0（Findings）\n- 交叉分享后共识强化了多项关切：标题 scope overclaim（双方 critical）、正面发现统计边缘性（双方 agree）、SciERC power 限制（双方 agree）、Few-NERD epoch 混淆（R2 交叉后新增认可）\n- 论文的实证严谨性突出（S1-S2），但核心正面发现在全局校正下仅 p_adj=0.055（MF2），且唯一正面数据集存在训练配置混淆（SF2）\n- 新颖性主要体现为系统化诊断分析而非突破性发现（SF3），这更适合 Findings track\n- 标题范围需要收窄以匹配实际证据（MF1）\n\n**Conference vs Findings 判断**:\n论文在 NER 领域提供了极为详尽的 test-time scaling 失效诊断，统计方法论达到高标准。但三个因素使其更适合 Findings 而非主会议：(1) 核心正面发现统计边缘；(2) 新颖性偏向系统化梳理；(3) 标题范围与证据不匹配。修复 MF1（标题收窄）和 MF2（正文讨论全局校正）后，作为 Findings 论文有较强竞争力。如能额外解决 SF2（Few-NERD epoch 混淆）和 SF3（novelty 精确定位），有潜力升至 Borderline Conference (3.5)。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Abstract 和 Introduction 的 claim scope 需与证据匹配（MF1）\n- \"we identify a correlation-selection gap\" 定位为发现已知现象在新领域的系统化诊断更准确（SF3）\n- Abstract \"ρ < 1 pp\" 措辞混淆，应改为 \"gain < 1 pp\"\n- Abstract 末句 \"extends beyond NER\" 超出证据范围，建议移除或加限定\n\n### §2 Diagnostic Framework\n- \"Diagnostic cascade\" → \"diagnostic framework\" 或 \"diagnostic checklist\"（SF1）\n- 首次使用时明确限定 \"we use this term to denote a diagnostic decomposition, not a causal chain\"\n\n### §3 How Self-Verification Fails\n- 使用 Qwen2.5-7B 而非主模型 Qwen3-8B 需要讨论（SF6）\n- ESJ/MRSC/LSC 缩写后续使用频率低，考虑减少缩写\n\n### §4 Where Single-Signal Selection Fails\n- SciERC-specific 分析受 n=529 power 限制（MF3），需在此 section 或 Limitations 中讨论\n- LP compression 需补充 constrained vs free-form 定量对比（SF7）\n\n### §5 Adaptive Methods\n- Cross-model SC（§5.1）和 trained verifiers（§5.2）深度与 §3-4 不成比例，值得更多讨论\n\n### §6 Threshold Regime Analysis\n- §6 在全文叙事中有些突兀，建议改善与前后章节的衔接\n- Proposition 1 bound 松紧度的 implications 需更明确讨论\n- MBR 联系（Proposition 2）有独立价值但可考虑部分内容移入 Appendix\n\n### §7 Experiments\n- §7.5 prescriptive results 需明确为 exploratory（MF2）\n- Few-NERD epoch 差异需在正文讨论（SF2）\n- 全局 Holm-Bonferroni 结果需在 §7 正文出现（MF2）\n\n### §8 Related Work\n- 增加 conformal prediction、token-level uncertainty、structured MBR 讨论（SF4）\n- Yun & Price (2025) 差异化讨论可进一步加强\n- Trained verifiers 文献讨论不足\n\n### §9 Discussion and Conclusion\n- \"Capability-diversity tension\" 弱化为 \"observed tendency\"（SF5）\n- Cascade 阈值的 task-specificity 需讨论\n\n### Limitations\n- 当前长度约 3 段，基本合适\n- 确认 N-budget 描述已更新到 N≤64\n\n### Format\n- Checklist 从 PDF 移除（SF8）\n- 确认正文在 8 页内",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "report": "# 审稿报告 — Round 36 (Fresh)\n\n**论文**: \"When Does Test-Time Scaling Fail? Boundary Conditions for Information Extraction\"\n**Venue**: EMNLP 2026 (Long Paper, via ARR)\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性+写作）\n**轮次**: Round 1（1 轮独立审稿 + 1 轮交叉分享，关键问题达成共识）\n\n---\n\n## Summary\n\n本文研究 test-time compute scaling（self-consistency / best-of-N）在信息抽取中何时失效，以 NER 为主要案例（4 数据集、2 模型家族），附带 RE 和 SQL 的探索性扩展。核心发现是 \"correlation-selection gap\"：质量估计信号能预测输出质量（AUROC ≤0.82），但 instance-level 选择增益 <1 pp。论文提出四阶段诊断框架，将失效归因于 output degeneracy（12-68%）和 signal alignment collapse（α→0）。作为探索性改进，LP-weighted entity-level construction 在 Few-NERD 上获得 +1.40 pp（Holm p_adj=0.006, per-family k=10; 全局 k=57 下 p_adj=0.055）。实验覆盖 9 个方法类别、N=2-64 scaling、4B-72B model scale ablation，附录达 46 页。\n\n---\n\n## Strengths\n\n**S1. 极为全面的实证调查 [共识]**\n9 个方法类别、5 个 confidence signals、4 个 NER 数据集、2 个模型家族（Qwen3-8B, LLaMA-3.1-8B）、N=2-64 scaling、4B-72B 规模消融、free-form decoding 消融。46 页附录覆盖 60+ 张表格和 10+ 张图。这可能是目前对 NER 中 self-consistency 行为最详尽的实证研究。\n\n**S2. 统计方法论严谨且诚实 [共识]**\nHolm-Bonferroni (k=57)、BH FDR、bootstrap 95% CI、paired bootstrap p-values、TOST 等效检验、power analysis——论文不仅使用了这些方法，还诚实报告了核心发现在全局校正下的边缘状态（p_adj=0.055）。这种统计透明度在 NLP 实证论文中罕见。\n\n**S3. Correlation-selection gap 有实质贡献 [共识]**\nQuality estimation ρ 可达 0.38-0.45 但不转化为 selection gain（Table 3/Table 1），这一发现清晰、可复现，对 test-time scaling 的实践部署有直接指导意义。\n\n**S4. 实用的诊断框架 [共识]**\n即便术语有待商榷（见 W3），degeneracy/headroom/compression/alignment 四要素分解为从业者提供了可操作的预部署检查清单——\"先检查 degeneracy rate，若 >50% 则不值得做 selection\"。\n\n**S5. 负面结果的系统化呈现 [共识]**\n论文系统排除了 ESJ、MRSC、LSC、supervised combination、trained verifier 等多种潜在方案，充分论证了问题的结构性（structural bottleneck）。\n\n**S6. 跨模型家族一致性 [共识]**\nQwen3-8B 和 LLaMA-3.1-8B 结果高度一致，加上 4B/14B 消融和 GPT-5.5 frontier 证据，增强了发现的泛化性。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [Critical, 共识] 标题范围显著超出实际证据**\n标题 \"Boundary Conditions for Information Extraction\" 暗示对 IE 各子任务的全面研究。实际证据 ~95% 来自 NER（4 数据集 × 2 模型家族完整分析）。RE 仅有 SciERC 1 个数据集的探索性结果（n=397, single seed），SQL 仅在 Discussion 中一句话提及（n=196）。NER 的 set-valued output 与 RE 的 tuple-valued output 有本质结构差异——论文自己在 §7.3 观察到 RE 的失效机制不同（40% zero-F1 来自上游 entity span 错误）。\n→ **建议**: 标题改为 \"Boundary Conditions for Named Entity Recognition\" 或 \"...for Information Extraction: Evidence from NER\"。\n\n**MF2. [Critical, 共识] 核心正面发现在全局多重比较校正下边缘不显著**\nFew-NERD LP selection (+1.39pp) 和 LP-weighted construction (+1.40pp) 在全局 Holm-Bonferroni (k=57) 下 p_adj=0.055，未通过 α=0.05。正文仅使用 per-family 校正（k=21/k=10），全局结果仅在附录 Table 12 中报告。Per-family correction 在统计学中是可辩护的标准做法，但 §7.5 的 prescriptive 建议建立在这个统计边缘的结果之上。\n→ **建议**: (1) 在 §7 正文中明确讨论全局校正下 p_adj=0.055 的边缘性；(2) 将 prescriptive results 定位为 exploratory 而非 confirmatory；(3) 强调核心贡献是 diagnostic framework（负面结论），而非 LP construction（正面结论）。\n\n**MF3. [Critical, 共识] SciERC 作为主要测试平台统计 power 有限**\nSciERC (n=529) 是论文多项核心分析的主要测试平台（Table 3 quality estimation、Table 1 selection gap、§4 diagnostic analysis），但仅单 seed 且 power analysis 显示 MDE≈1.5pp，而观测效果 +0.2pp 远低于 MDE。不影响 \"no signal beats greedy\" 结论，但影响 SciERC-specific 诊断细节的可靠性。多数据集设计（CoNLL n=3453, Few-NERD n=32560）部分缓解。\n→ **建议**: (1) 在正文讨论 power 限制对 SciERC 结论的含义；(2) 报告 TOST 结果在正文中；(3) 补充多 seed 实验增强说服力。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [Warning, 共识] \"Diagnostic cascade\" 术语误导因果解读**\n§4 承认 \"stages resist decomposition into independent effects (R²<0)\" 且 degeneracy 不独立预测 LP gain，这与 \"cascade\"（暗示顺序依赖）矛盾。实际是两个需同时满足的必要条件（低 degeneracy + 高 LP-F1 alignment），非顺序筛选。ML 社区对 \"cascade\" 有明确技术含义（Viola-Jones 等）。\n→ **建议**: 全文改用 \"diagnostic framework\" 或 \"diagnostic checklist\"。\n\n**SF2. [Warning, 共识] Few-NERD 训练 epoch 差异构成混淆变量**\nFew-NERD 是唯一 LP selection 显著正向的数据集（+1.39pp），也是唯一使用 3 epochs（而非 5 epochs）训练的。Appendix u 显示 5-epoch 训练使 degeneracy 从 13% 升至 31%、LP 增益减半。Few-NERD 的低 degeneracy（使 LP selection 成功的关键条件）可能部分是 undertraining 产物。论文在 Appendix 有数据但未将其框架化为混淆变量。\n→ **建议**: 在正文明确讨论 epoch 差异作为混淆变量，报告 Few-NERD 5-epoch LP selection 结果。\n\n**SF3. [Warning, 共识降级] Novelty 定位不够精确**\n\"Correlation-selection gap\" 作为核心发现，calibration ≠ ranking 在决策理论中是已知原则，Chen et al. (2024a) 和 Yun & Price (2025) 已记录 SC 失效。R2 原列为 Must-Fix，R1 反驳认为诊断框架本身有原创性（9 方法类别系统测试、LP compression 机制解析、entity-level partial match 特有 failure mode），非简单 \"新领域应用\"。最终共识降级为 Should-Fix（framing 问题非 soundness 问题）。\n→ **建议**: §1 明确区分：(a) SC 失效作为一般现象是已知的，(b) 本文贡献是 NER 领域首个系统化量化诊断框架。\n\n**SF4. [Warning, 共识] Related Work 缺失直接相关方向**\n缺失：conformal prediction for structured prediction（Fisch et al. 2021, Angelopoulos & Bates 2023）、token-level uncertainty estimation for sequence labeling、trained verifiers 更广泛讨论（Cobbe et al. 2021 在 NER 场景的启示）、structured MBR（Chen et al. 2025）。\n→ **建议**: §8 增加一段覆盖这些方向。\n\n**SF5. [Warning, 共识] Capability-diversity tension 证据不足以支撑 claim 强度**\n模型规模 4B-14B 有限，GPT-5.5 仅 200 实例 zero-shot 单数据集，72B 仅 \"preliminary\"。§9 描述为 \"structural constraint\" 但证据不足。\n→ **建议**: 弱化为 \"observed tendency within tested scales\"，Abstract 移除 \"extends beyond NER\" 或加限定。\n\n**SF6. [Warning, 共识] §3 自验证实验使用不同模型家族**\nESJ/MRSC/LSC 使用 Qwen2.5-7B 而非主模型 Qwen3-8B。\"Models cannot self-verify\" 结论可能不直接推广到主模型。结论方向与主实验负面结果一致，但严谨性要求使用相同模型或讨论原因。\n\n**SF7. [Warning, 共识] Constrained decoding 对 LP compression 贡献未充分量化**\nLP 在 constrained decoding 下压缩严重（60% 实例 LP range < 0.041 nats），但 free-form ablation 中缺少 LP range/tied fraction 的直接定量对比。\n→ **建议**: 补充 constrained vs free-form LP compression 指标对比。\n\n**SF8. [Warning, 共识] Responsible NLP Checklist 不应在 PDF 中**\n按 EMNLP 2026 ARR 规定，checklist 应在 OpenReview 表单中填写。当前 PDF 包含 ~1.5 页 checklist（pages 9-10）。\n→ **建议**: 提交前从 PDF 移除。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题两位 Reviewer 独立发现并完全一致：\n1. 标题范围超出证据（MF1）— 双方列为 critical\n2. Cascade 术语误导（SF1）— 双方独立提出相同关切\n3. Checklist 格式不合规（SF8）— 双方一致\n4. SciERC power 有限（MF3）— R1 提出，R2 完全同意\n5. 全局 Holm 校正边缘（MF2）— R1 提出，R2 同意并补充 per-family 校正辩护\n6. Related Work 缺失（SF4）— R2 详列，R1 大部分同意\n7. Few-NERD epoch 混淆变量（SF2）— R1 发现，R2 交叉回应中高度认可（\"自己审稿中未充分注意到的有效关切\"）\n\n## Reviewer Divergence [REBUT]\n\n1. **R2-N2 (novelty positioning) 的严重性**: R2 列为 Must-Fix (critical)，认为 correlation-selection gap 在更广泛 ML 文献中非全新。R1 反驳（[REBUT]），认为诊断框架本身有原创性——9 个方法类别的系统测试、LP compression 的机制解析远超 \"在新领域观察已知现象\"。R1 建议降级为 Should-Fix。**Director 判断**: 采纳 R1 的降级建议——novelty 问题确实存在但属 framing 层面，非 soundness 缺陷。已在 SF3 中体现。\n\n2. **R2-W5 (理论分析 §6 价值有限)**: R2 认为 Proposition 1 bound 过松（3-12%）、entity independence 假设不成立、§6 叙事突兀。R1 反驳（[REBUT]），认为 bound 的诊断价值不依赖 tightness，MBR 联系和 α_crit 有独立贡献。**Director 判断**: 双方各有道理。Proposition 1 的诊断价值有限但不为零；§6 的结构组织确需改善。已在 SF 中保留为 \"改善 §6 结构衔接\"（issue R35-W5）。\n\n---\n\n## Questions for Authors\n\n1. Few-NERD 使用 3 epochs 而非 5 epochs 是否有特定原因（如过拟合）？是否有 5-epoch Few-NERD 的 LP selection 结果？\n2. §3 的自验证实验选择 Qwen2.5-7B 而非主模型 Qwen3-8B 的原因是什么？\n3. Free-form decoding 下的 LP tied fraction 具体是多少？与 constrained decoding 的 60.3% 如何对比？\n4. 如果 diagnostic cascade 的各阶段不独立（R²<0），那么将 α 识别为 \"bottleneck\" 的结论是否依赖于各因素可分解的假设？\n5. 是否考虑过 token-level uncertainty estimation 作为绕过 entity-level alignment 问题的替代路径？\n6. Entity-level construction 在什么样的 degeneracy rate × alignment 条件组合下可以期望显著增益？\n\n---\n\n## Missing References\n\n- Fisch, A., Schuster, T., Jaakkola, T., & Barzilay, R. (2021). Few-shot conformal prediction with auxiliary tasks. ICML.\n- Angelopoulos, A. N., & Bates, S. (2023). Conformal prediction: A gentle introduction. Foundations and Trends in ML.\n- Token-level uncertainty estimation for sequence labeling 文献（具体文献需作者搜索补充）\n- Chen et al. (2025) Structure-conditional minimum Bayes risk decoding（已引用但 §8 讨论不足）\n- Li et al. (2024) Self-consistency for structured prediction（如直接相关）\n- Yao et al. (2024) Tree of Thoughts / Algorithm of Thoughts（作为 test-time compute 替代方法简要提及）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**: 未请求（项目未启用外部审稿）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: Agent 超时（300s timeout）。未产出排版审查结果。如有需要可由用户重新触发。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n**置信度: 4/5**\n\n**评分理由**:\n- R1 给出 3.5（Borderline Conference），R2 给出 3.0（Findings）\n- 交叉分享后共识强化了多项关切：标题 scope overclaim（双方 critical）、正面发现统计边缘性（双方 agree）、SciERC power 限制（双方 agree）、Few-NERD epoch 混淆（R2 交叉后新增认可）\n- 论文的实证严谨性突出（S1-S2），但核心正面发现在全局校正下仅 p_adj=0.055（MF2），且唯一正面数据集存在训练配置混淆（SF2）\n- 新颖性主要体现为系统化诊断分析而非突破性发现（SF3），这更适合 Findings track\n- 标题范围需要收窄以匹配实际证据（MF1）\n\n**Conference vs Findings 判断**:\n论文在 NER 领域提供了极为详尽的 test-time scaling 失效诊断，统计方法论达到高标准。但三个因素使其更适合 Findings 而非主会议：(1) 核心正面发现统计边缘；(2) 新颖性偏向系统化梳理；(3) 标题范围与证据不匹配。修复 MF1（标题收窄）和 MF2（正文讨论全局校正）后，作为 Findings 论文有较强竞争力。如能额外解决 SF2（Few-NERD epoch 混淆）和 SF3（novelty 精确定位），有潜力升至 Borderline Conference (3.5)。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- Abstract 和 Introduction 的 claim scope 需与证据匹配（MF1）\n- \"we identify a correlation-selection gap\" 定位为发现已知现象在新领域的系统化诊断更准确（SF3）\n- Abstract \"ρ < 1 pp\" 措辞混淆，应改为 \"gain < 1 pp\"\n- Abstract 末句 \"extends beyond NER\" 超出证据范围，建议移除或加限定\n\n### §2 Diagnostic Framework\n- \"Diagnostic cascade\" → \"diagnostic framework\" 或 \"diagnostic checklist\"（SF1）\n- 首次使用时明确限定 \"we use this term to denote a diagnostic decomposition, not a causal chain\"\n\n### §3 How Self-Verification Fails\n- 使用 Qwen2.5-7B 而非主模型 Qwen3-8B 需要讨论（SF6）\n- ESJ/MRSC/LSC 缩写后续使用频率低，考虑减少缩写\n\n### §4 Where Single-Signal Selection Fails\n- SciERC-specific 分析受 n=529 power 限制（MF3），需在此 section 或 Limitations 中讨论\n- LP compression 需补充 constrained vs free-form 定量对比（SF7）\n\n### §5 Adaptive Methods\n- Cross-model SC（§5.1）和 trained verifiers（§5.2）深度与 §3-4 不成比例，值得更多讨论\n\n### §6 Threshold Regime Analysis\n- §6 在全文叙事中有些突兀，建议改善与前后章节的衔接\n- Proposition 1 bound 松紧度的 implications 需更明确讨论\n- MBR 联系（Proposition 2）有独立价值但可考虑部分内容移入 Appendix\n\n### §7 Experiments\n- §7.5 prescriptive results 需明确为 exploratory（MF2）\n- Few-NERD epoch 差异需在正文讨论（SF2）\n- 全局 Holm-Bonferroni 结果需在 §7 正文出现（MF2）\n\n### §8 Related Work\n- 增加 conformal prediction、token-level uncertainty、structured MBR 讨论（SF4）\n- Yun & Price (2025) 差异化讨论可进一步加强\n- Trained verifiers 文献讨论不足\n\n### §9 Discussion and Conclusion\n- \"Capability-diversity tension\" 弱化为 \"observed tendency\"（SF5）\n- Cascade 阈值的 task-specificity 需讨论\n\n### Limitations\n- 当前长度约 3 段，基本合适\n- 确认 N-budget 描述已更新到 N≤64\n\n### Format\n- Checklist 从 PDF 移除（SF8）\n- 确认正文在 8 页内",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 3895 · 2026-05-22T11:14:20.255400+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4117
}
```

</details>

---


### Assistant

_source line 3896 · 2026-05-22T11:14:28.834926+00:00_

审稿报告已投递给 Research Director。

---

**Round 36 审稿完成。**

**最终评分：3.0 (Findings)**

核心结论：
- **3 个 Must-Fix**：(1) 标题 "Information Extraction" 超出 ~95% NER 证据范围；(2) 核心正面发现全局 Holm p_adj=0.055 需在正文讨论；(3) SciERC n=529 单 seed power 不足
- **8 个 Should-Fix**：cascade 术语误导、Few-NERD epoch 混淆变量、novelty 定位、Related Work 缺失、CDT 证据不足、自验证模型不一致、LP compression 定量对比缺失、Checklist 格式
- **主要优势**：实证极为全面（46 页附录）、统计方法论严谨且诚实、诊断框架有实用价值

修复 MF1（标题收窄）和 MF2（正文讨论全局校正）后作为 Findings 论文有较强竞争力。若额外解决 SF2（epoch 混淆）和 SF3（novelty 定位），有潜力升至 3.5 (Borderline Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 294

## Round 294

2 recorded events


### User

_source line 3897 · 2026-05-22T11:14:31.540506+00:00_

[Reviewer 2 审稿结果]:
已提交对 Reviewer 1 全部 7 个 Must-Fix/Should-Fix 的逐条回应。核心结论：全部同意或部分同意，无反驳项。两位 reviewer 在 "cascade 术语误导"（R1-W1 = R2-W2）和 "scope 超出证据"（R1-W4 = R2-N1）上独立一致。R1 的训练 epoch 混淆变量（W2）和全局多重比较（N1）为我的审稿提供了统计层面的有价值补充。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 3898 · 2026-05-22T11:14:47.498378+00:00_

审稿报告已在收到 Reviewer 1 交叉回应后完成合成并投递。Reviewer 2 的交叉回应确认了与 Reviewer 1 的全面共识（全部同意，无反驳），进一步验证了报告结论的稳健性。

**Round 36 审稿已完成。**

最终评分：**3.0 (Findings)**。3 个 Must-Fix（标题 scope overclaim、全局 Holm p=0.055 边缘性、SciERC power 有限）+ 8 个 Should-Fix。两位 Reviewer 在所有关键问题上达成共识。报告和 Issue Tracker 均已投递/更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 295

## Round 295

58 recorded events


### User

_source line 3899 · 2026-05-22T12:02:14.131881+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (via ARR)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 3900 · 2026-05-22T12:02:24.105862+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3901 · 2026-05-22T12:02:24.106754+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 3902 · 2026-05-22T12:02:35.153372+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 3903 · 2026-05-22T12:02:36.710089+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 1556
}
```

</details>

---


### Tool call

_source line 3904 · 2026-05-22T12:02:41.880278+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 3905 · 2026-05-22T12:02:43.134380+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (324 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-22T11:35:22Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 323 个实验 — ANALYZING 2, DONE 295, PREPARING 20, QUEUED 1, RUNNING 5\n**DONE 分布**: failed 13, killed 35, negative 53, success 194\n\n### GPU 占用\n- **分配**: 8 张 — autodl-5090:cuda:0, autodl-5090:cuda:1, autodl-5090:cuda:2, autodl-5090:cuda:3, autodl-5090-c:cuda:0, autodl-5090-c:cuda:1, autodl-5090-c:cuda:2, autodl-5090-c:cuda:3\n- **实际运行**: 5 张 — autodl-5090-c:cuda:0(exp_fewnerd_mf4_s42), autodl-5090-c:cuda:2(exp_fewnerd_mf4_s456), autodl-5090-c:cuda:3(exp_fewnerd_pretrained_n32_s42), autodl-5090:cuda:2(exp_fewnerd_mf4_s123_v2), autodl-5090:cuda:3(exp_fewnerd_5epoch_lp_s42)\n- **空闲（分配了没跑）**: autodl-5090:cuda:0, autodl-5090:cuda:1\n\n### 💾 磁盘余量\n- **autodl-5090**:\n  - `/autodl-pub`: 8.6T/14T 可用（已用 39%）\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\n  - `/usr/bin/nvidia-smi`: 813G/879G 可用（已用 3%）\n- **autodl-5090-c**:\n  - `/autodl-pub`: 6.4T/14T 可用（已用 55%）\n  - `/autodl-pub/data`: 18T/20T 可用（已用 9%）\n  - `/usr/bin/nvidia-smi`: 813G/879G 可用（已用 3%）\n\n### 🏃 RUNNING\n| exp_id | server | gpu | pid | log |\n|--------|--------|-----|-----|-----|\n| `exp_fewnerd_mf4_s42` | autodl-5090-c | cuda:0 | 426032 | `~/ru
…[truncated 1777 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1254
}
```

</details>

---


### Tool call

_source line 3906 · 2026-05-22T12:02:43.285229+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 3907 · 2026-05-22T12:02:43.335868+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{amsthm}
16	\newtheorem{proposition}{Proposition}
17	\newtheorem{theorem}{Theorem}
18	\newtheorem{corollary}{Corollary}
19	\newtheorem{definition}{Definition}
20	\usepackage{multirow}
21	\usepackage{xcolor}
22	\usepackage{subcaption}
23	\usepackage{alphalph}
24	\usepackage{enumitem}
25	
26	\graphicspath{{figures/}}
27	
28	\title{When Does Test-Time Scaling Fail?\\ Boundary Conditions for Named Entity Recognition}
29	
30	\author{Anonymous}
31	
32	\begin{document}
33	\maketitle
34	
35	\input{sections/abstract}
36	\input{sections/introduction}
37	\input{sections/diagnostic}
38	\input{sections/mechanistic}
39	\input{sections/single_signal}
40	\input{sections/adaptive}
41	\input{sections/theory}
42	\input{sections/experiments_main}
43	\input{sections/background}
44	\input{sections/discussion}
45	
46	\section*{Limitations}
47	\input{sections/limitations}
48	
49	\section*{Ethics Statement}
50	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, Few-NERD, WNUT-17), open-weight models (Qwen3-8B, Qwen3-14B, Qwen3-4B, LLaMA-3.1-8B), and the GPT-5.5 API.
51	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
52	No new human data was collected or annotated for this study.
53	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
54	Code and data will be released upon acceptance at [anonymized URL].
55	
56	\bibliography{references}
57	
58	\appendix
59	\renewcommand{\thesection}{\alphalph{\value{section}}}
60	\input{se
…[truncated 42 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3908 · 2026-05-22T12:02:43.336333+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 3909 · 2026-05-22T12:02:43.436979+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 3910 · 2026-05-22T12:02:47.955885+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 3911 · 2026-05-22T12:02:48.056647+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 3912 · 2026-05-22T12:02:51.000454+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR"
  }
}
```

</details>

---


### Tool call

_source line 3913 · 2026-05-22T12:02:51.402770+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 3914 · 2026-05-22T12:02:51.854982+00:00_

1	\begin{abstract}
2	Test-time compute scaling---repeated sampling with self-consistency or best-of-$N$---yields large gains on discrete-answer reasoning, but whether these gains transfer to NER remains open.
3	Using named entity recognition (four datasets, primarily 7--14B fine-tuned; tentative cross-scale observations to 72B) as the primary case study and relation extraction as an exploratory extension, we characterize when test-time scaling succeeds and fails for set-valued outputs.
4	Quality estimation signals effectively predict output quality (AUROC up to $0.82$ across nine method categories), yet instance-level selection yields ${<}1$\,pp even at $N{=}64$, revealing a \textbf{correlation-selection gap}.
5	A diagnostic framework identifies two boundary conditions: output convergence (degeneracy $12$--$68$\%) and signal alignment collapse ($\alpha{\to}0$), which jointly determine scaling returns.
6	Cross-task validation on RE reveals a distinct bottleneck---$40$\% zero-F1 from upstream errors rather than degeneracy---confirming task-specific failure modes.
7	Exploratory entity-level construction partially bypasses the sample-level bottleneck ($+1.40$\,pp where low degeneracy and signal alignment provide headroom).
8	The diagnostic framework enables predicting test-time scaling failure before investing in repeated inference; the observed \textit{capability-diversity tension}---output convergence increasing with model capability---may extend beyond NER but requires further validation.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 3915 · 2026-05-22T12:02:51.855498+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 3916 · 2026-05-22T12:02:52.357518+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time compute scaling---self-consistency \cite{wang2023selfconsistency}, best-of-$N$ \cite{snell2025scaling, brown2024monkeys}, extended reasoning \cite{muennighoff2025s1}---yields large gains on discrete-answer tasks where outputs admit equivalence classes or execution-based verification.
4	For NER, where outputs are entity sets with partial overlap, the boundary conditions for effective scaling are unknown; prior work \cite{yao2026consistency, yun2025price} provides initial observations but no systematic diagnostic framework quantifying failure mechanisms at entity level across multiple model families.
5	
6	Using NER (four datasets, primarily 7--14B fine-tuned; tentative cross-scale observations to 72B) and RE as case studies, we identify a \textbf{correlation-selection gap}: quality estimation signals predict output quality ($\rho$ up to $0.45$, AUROC $0.82$; Table~\ref{tab:quality_estimation}), yet selection fails---MV gains ${<}1$\,pp even at $N{=}64$ (Figure~\ref{fig:n_scaling}; Table~\ref{tab:selection}).
7	This gap decomposes into a definitional layer---four instance-level signals assign identical scores to all candidates---and an empirical one: LP, the only per-sample signal, also fails through within-instance compression (\S\ref{sec:selection_gap}).
8	A hidden-state probe confirms models encode entity quality internally (AUROC $0.63$\textendash$0.88$; \S\ref{sec:mechanistic}), exposing an \textit{introspection boundary} \cite{huang2024large}.
9	A \textit{diagnostic framework}---simultaneously necessary conditions, not a sequential filter---localizes the failure to output convergence (degeneracy $12$--$68$\%) and signal alignment collapse ($\alpha{\to}0$), which jointly prevent selection (Table~\ref{tab:method_summary}).
10	The optimal strategy is dataset-dependent (LP: $+1.39$\,pp on Few-NERD; MV: $+0.61$\,pp on CoNLL at $N{=}64$), and RE reveals a distinct bottleneck ($40$\% zero-F1 from upstream e
…[truncated 2678 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 3917 · 2026-05-22T12:02:52.408077+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
  }
}
```

</details>

---


### Tool result

_source line 3918 · 2026-05-22T12:02:52.458808+00:00_

1	\section{Experiments}\label{sec:experiments}
2	
3	\subsection{Experimental Setup}\label{sec:setup}
4	
5	\paragraph{Datasets.}
6	We evaluate on four English NER benchmarks spanning a difficulty gradient.
7	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed (${\approx}$65\% F1).
8	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:selection_gap}).
9	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control.
10	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 51\% zero F1) probes the signal-collapse boundary.
11	
12	\paragraph{Models and sampling.}
13	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others; Appendix~\ref{app:epoch_confound}).
14	$N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}; $N {\in} \{16, 32, 64\}$ for scaling (Figure~\ref{fig:n_scaling}; Appendix~\ref{app:n_scaling}).
15	
16	\begin{figure}[t]
17	\centering
18	\includegraphics[width=\columnwidth]{figures/fig_n_scaling_mv.pdf}
19	\caption{MV $\Delta$F1 vs.\ $\log_2 N$ across three datasets (Qwen3-8B FT, seed${=}42$). Dotted gray: $\Delta{=}0$. Gains are dataset-dependent: persistently negative on Few-NERD, near zero on SciERC at higher $N$, marginally positive on CoNLL ($+0.6$\,pp at $N{=}64$).}
20	\label{fig:n_scaling}
21	\end{figure}
22	
23	%% ============================================================
24	\subsection{Quality Estimation Results}\label{sec:qe_results}
25	
26	\begin{table*}[t]
27	\centering
28	\small
29	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed $
…[truncated 7486 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 3919 · 2026-05-22T12:03:04.230054+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026 via ARR:

## Overview
EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

## Paper Types
Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## Important Dates
The ARR submission deadline for long and short papers is May 25, 2026, with a reviewer registration deadline for all authors on May 27, 2026. Author response and author-reviewer discussion will occur July 7-13, 2026, with meta review released July 30, 2026, and the EMNLP commitment dea
…[truncated 834 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 13229
}
```

</details>

---


### Tool call

_source line 3920 · 2026-05-22T12:03:11.114744+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
  }
}
```

</details>

---


### Tool result

_source line 3921 · 2026-05-22T12:03:11.466216+00:00_

1	\section{Diagnostic Framework}\label{sec:method}
2	
3	Our analysis is observational: we characterize statistical associations between agreement signals and output quality without claiming causal mechanisms.
4	
5	\subsection{Problem Formulation}\label{sec:formulation}
6	
7	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
8	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
9	This distinction is consequential: 4 of 5 signals are instance-level aggregates assigning identical scores to all $N$ candidates.
10	Only LP carries per-sample discriminative power: ensemble optimization assigns LP mean weight $0.78$, with structural signals receiving zero weight (Appendix~\ref{app:supervised_combination}).
11	When LP fails---as in few-shot regimes where LP $\rho{\to}0$ (\S\ref{sec:scaling})---no alternative per-sample signal exists.
12	
13	We define the \textbf{capability ceiling} as the practical performance upper bound achievable through self-consistency at realistic sample budgets ($N{\leq}16$), beyond which diminishing returns render further scaling impractical.
14	
15	\subsection{Confidence Signals}\label{sec:signals}
16	
17	Entity matching uses exact span and type match.
18	We distinguish two signal families: four \textit{agreement signals} computed across samples---\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK])---and log-probability [LP] as the sole \textit{model-internal} signal, derived from generation probabilities and providing per-sample discrimination.
19	
20	\paragraph{Log-probability (per-sample).}
21	$c_{\text{lp}}(y_i)
…[truncated 2151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 3922 · 2026-05-22T12:03:11.617002+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex"
  }
}
```

</details>

---


### Tool result

_source line 3923 · 2026-05-22T12:03:12.370291+00:00_

1	\section{How Self-Verification Fails}\label{sec:mechanistic}
2	
3	The diagnostic framework (\S\ref{sec:method}) identifies \textit{where} self-consistency fails; this section probes \textit{why} by testing whether models can self-verify at the entity level.
4	We evaluate self-verification and diagnostic probes on Qwen2.5-7B\footnote{ESJ, MRSC, and LSC use Qwen2.5-7B-Instruct (zero-shot self-verification capability) rather than the fine-tuned Qwen3-8B used in the main experiments. Conclusion direction is consistent with the main experiments' negative results across all fine-tuned selection strategies.} fine-tuned for NER on Few-NERD ($N{=}8$, seed 42; full results in Appendix~\ref{app:self_verification}).
5	
6	\paragraph{Entity Self-Judgment (ESJ).}
7	For each extracted entity, we prompt the generating model: ``Is [\textit{entity}] a [\textit{type}] entity in this sentence?''
8	Entity-level AUROC is $0.512$---indistinguishable from chance---with P(yes$|$correct)${=}0.500$ and P(yes$|$incorrect)${=}0.500$.
9	ESJ-weighted construction degrades F1 to $0.711$ (vs.\ greedy $0.794$).
10	
11	\paragraph{Multi-Round Self-Consistency (MRSC).}
12	Following iterative self-refinement \cite{madaan2023selfrefine}, we re-prompt on disputed entities (agreement ${<}0.6$) with focused verification; P(yes) separation between gold and non-gold entities is $0.0006$ ($0.5003$ vs.\ $0.4997$).
13	MRSC best F1 ($0.763$) falls below greedy.
14	
15	\paragraph{Latent Self-Consistency (LSC).}
16	Mean-pooled final-layer hidden states ($d{=}3584$) provide per-sample latent representations.
17	Centroid selection ($0.759$) underperforms greedy ($0.794$); latent entity confidence ($0.839$) outperforms majority vote ($0.792$) but does not close the oracle gap ($0.882$).
18	
19	\paragraph{Hidden-state probe.}
20	A logistic regression on mean-pooled final-layer hidden states at entity spans achieves AUROC $0.636$ (Few-NERD), $0.882$ (CoNLL), $0.630$ (SciERC), evaluated with GroupKFold CV (5-fold ${\tim
…[truncated 1295 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 3924 · 2026-05-22T12:03:12.420991+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
  }
}
```

</details>

---


### Tool result

_source line 3925 · 2026-05-22T12:03:12.922895+00:00_

1	\section{Where Single-Signal Selection Fails}\label{sec:selection_gap}
2	
3	\paragraph{Definitional vs.\ empirical.}
4	We decompose the correlation-selection gap into two layers.
5	The first is structural: four of five signals are instance-level aggregates that assign identical scores to all $N$ candidates from a given input (\S\ref{sec:formulation}), so they estimate quality across inputs but cannot rank candidates within an instance---selection failure is a design property, not an empirical finding.
6	The second layer is empirical and constitutes the core diagnostic: LP---the only per-sample signal---suffers compression under constrained decoding, with 60\% of SciERC instances showing within-instance LP range below 0.041 nats (Appendix~\ref{app:logprob_ties}), effectively eliminating the variation needed for sample discrimination. This compression is model-intrinsic: free-form decoding yields nearly identical LP distributions (within-instance std ratio $0.97{\times}$; Appendix~\ref{app:freeform_ablation}). Even where LP varies, selection gains depend on LP-quality alignment rather than degeneracy alone.
7	Cross-instance $\rho$ (Table~\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Best-of-$N$ selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$). Selection signals: 2-seed mean${\pm}\sigma$; baselines: 3-seed (Oracle${=}0.781$, Greedy${=}0.667$). LP is per-sample; others use consensus-proximity. $^\dagger$One score per input.}
13	\label{tab:selection}
14	\begin{tabular}{lcc}
15	\toprule
16	Method & NER F1 & $p$ \\
17	\midrule
18	Oracle & $0.775 \pm 0.001$ & --- \\
19	Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
20	\midrule
21	LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
22	SJ           & $0.646 \pm 0.002$ & .67 \\
23	FK      
…[truncated 2873 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 3926 · 2026-05-22T12:03:12.923289+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
  }
}
```

</details>

---


### Tool result

_source line 3927 · 2026-05-22T12:03:13.374898+00:00_

1	\section{Adaptive Methods}\label{sec:adaptive}
2	
3	Since instance-level selection fails (\S\ref{sec:selection_gap}), we present approaches that extract value from multi-sample generation beyond single-signal sample ranking.
4	Table~\ref{tab:method_summary} summarizes all 9 method categories evaluated; only cross-model ensembles yield an unconditional positive result.
5	
6	\begin{table}[t]
7	\centering
8	\small
9	\caption{Summary of 9 method categories tested (including MV baseline, LP selection, and cross-model ensemble beyond the seven verification methods in \S\ref{sec:mechanistic}--\S\ref{sec:adaptive}). $\Delta$F1 vs.\ greedy; dataset in parentheses. Full coverage in Appendix~\ref{app:method_coverage}.}
10	\label{tab:method_summary}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{@{}llrl@{}}
13	\toprule
14	Category & Method & $\Delta$F1 / metric & § \\
15	\midrule
16	Freq.\ voting & MV & baseline & \ref{sec:prescriptive} \\
17	LP selection & Best-of-$N$ (LP) & $+1.39$\,pp (FN)$^\dagger$ & \ref{sec:selection_gap} \\
18	Self-verif.\ (prompt) & ESJ & AUROC $0.51$ & \ref{sec:mechanistic} \\
19	Multi-round refine. & MRSC & $-3.1$\,pp (FN) & \ref{sec:mechanistic} \\
20	Latent aggregation & LSC & $-3.5$\,pp (FN) & \ref{sec:mechanistic} \\
21	Adaptive gating & DALS & $+0.71$\,pp (SciERC)$^\ddagger$ & App.~\ref{app:dals} \\
22	Supervised verifier & LGB & $+0.30$\,pp (OOF) & \ref{sec:verifier} \\
23	Sup.\ combination & LR/MLP/RF & $-0.4$ to $-3.1$\,pp & App.~\ref{app:supervised_combination} \\
24	Cross-model & Qwen$+$LLaMA & $\mathbf{+0.42}$\,pp (FN) & \ref{sec:cross_model} \\
25	\bottomrule
26	\end{tabular}}
27	{\footnotesize $^\dagger$Few-NERD only; SciERC $+0.2$\,pp ($p{=}0.29$). $^\ddagger$Seed-sensitive ($\sigma{=}0.48$\,pp).}
28	\end{table}
29	
30	\subsection{Cross-Model Self-Consistency}\label{sec:cross_model}
31	
32	Mixing samples from architecturally distinct models can partially bypass within-model degeneracy.
33	Combining 4 samples each from Qwen3-8B and
…[truncated 764 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 3928 · 2026-05-22T12:03:13.375316+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
  }
}
```

</details>

---


### Tool result

_source line 3929 · 2026-05-22T12:03:13.676592+00:00_

1	\section{Threshold Regime Analysis}\label{sec:theory_scaling}
2	
3	\subsection{Entity Construction as MBR Decoding}\label{sec:mbr_theory}
4	
5	Entity-level construction selects $\hat{y}_{\textup{MBR}} = \{e \in E_\cup : \hat{p}(e) > \alpha/(\alpha{+}1)\}$ under balanced set-overlap utility; $\alpha{=}1$ recovers majority vote (Proposition~\ref{prop:construction_mbr}; Table~\ref{tab:entity_construction}; Appendix~\ref{app:mbr_proof}).
6	Signal-derived weights $w_i$ yield quality-weighted MBR: $\hat{p}_w(e) = \sum_{i} w_i \, \mathbf{1}[e {\in} y_i] / \sum_{i} w_i$; weighting improves when $w_i$ correlates with instance quality but degrades otherwise (LP on SciERC: $\rho{\approx}0.2$; \S\ref{sec:prescriptive}).
7	We select $\varepsilon{=}0.05$ at the elbow of the compression curve, where LP-best selection advantage transitions from $+1.5$\,pp (compressed) to $+4.6$\,pp (non-compressed; Appendix~\ref{app:fewnerd_epsilon}).
8	
9	\subsection{Scaling and Inverse Scaling}\label{sec:scaling}
10	
11	Oracle F1 follows $F_1(N) = a - b \cdot N^{-c}$ ($R^2 > 0.999$; Figure~\ref{fig:oracle_scaling}): Few-NERD ($c{\approx}0.61$) scales comparably to reasoning tasks \cite{brown2024monkeys}, SciERC converges more slowly ($c{\approx}0.35$), yet confidence-based aggregation recovers ${<}1$\,pp---a persistent gap.
12	The gap persists across scales and families: scaling from 8B to 14B FT increases oracle headroom ($+1.2$\,pp) with minimal greedy gain ($+0.9$\,pp), and GPT-5.5 (200 Few-NERD instances, zero-shot) exhibits the same pattern---50\% degeneracy, SJ $\rho{=}0.346$, MV $+1.4$\,pp yet 6.8\,pp oracle headroom unrealized.\footnote{Of the 10.1\% of GPT-5.5 samples producing empty entity sets, 88\% correspond to gold-empty instances; true parse failures affect only 1.2\% of samples (19/1{,}600) and shift all reported metrics by ${<}0.5$\,pp. See Appendix~\ref{app:frontier_sc}.}
13	Degeneracy is model-family-dependent rather than scale-dependent (Qwen2.5: $31.7$--$46.2$\% vs.\ Qwen3:
…[truncated 3691 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 3930 · 2026-05-22T12:03:13.677009+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 3931 · 2026-05-22T12:03:15.232498+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Test-time compute scaling.}
4	Self-consistency \cite{wang2023selfconsistency} and best-of-$N$ \cite{snell2025scaling, brown2024monkeys} drive large gains on reasoning and code \cite{chen2021codex}.
5	Reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty}, BoN scaling laws \cite{gao2023scaling}, and trained verifiers \cite{cobbe2021verifiers, lightman2024verify} target discrete-answer settings; NER requires different aggregation because degeneracy operates at the entity-set level.
6	
7	\paragraph{SC failure modes.}
8	\citet{chen2023twofailures} identify SC failures where consistent outputs are wrong; free-form \cite{chen2024usc} and atomic \cite{thirukovalluru2024atomic} SC variants face limits where sub-output agreement does not yield selection gain (\S\ref{sec:selection_gap}).
9	
10	\paragraph{Consistency for structured IE.}
11	\citet{yao2026consistency} show task-level QE correlation ($\rho$ up to 0.47) for NER/RE; \citet{xie2023zeroshot} propose entity voting for zero-shot NER and \citet{xie2024selfimproving} report positive SC where zero-shot diversity is high.
12	\paragraph{Uncertainty estimation and MBR.}
13	Our selection instantiates MBR decoding \cite{eikema2022sampling, denero2009fast}; despite success in translation \cite{freitag2022high} and code \cite{jinnai2024mbr}, all variants fail due to instance degeneracy (Appendix~\ref{app:mbr_connection}).
14	\citet{eikema2025structured} find MBR utilities degrade on structured outputs; our framework localizes this to degeneracy and LP compression (\S\ref{sec:selection_gap}).
15	LP is well-calibrated at population level (ECE $0.069$--$0.096$) but too compressed within instances for selection \cite{kadavath2022language, tian2023calibration}.
16	
17	\paragraph{Capability ceiling vs.\ diversity collapse.}\label{sec:yun_contrast}
18	\citet{yun2025price} identify \textit{diversity collapse} under constrained decoding for discrete answers (Tabl
…[truncated 1030 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 1555
}
```

</details>

---


### Tool call

_source line 3932 · 2026-05-22T12:03:19.598118+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 3933 · 2026-05-22T12:03:20.150441+00:00_

1	\section{Discussion and Conclusion}\label{sec:discussion}\label{sec:selection_method}\label{sec:conclusion}
2	
3	\paragraph{Why test-time scaling fails for NER.}
4	For discrete-answer reasoning, sample diversity reflects diverse reasoning paths; for NER, output convergence (degeneracy $12$--$68$\%) eliminates candidate diversity while signal alignment collapse ($\alpha{\to}0$) prevents ranking---a \textit{capability-diversity tension} observed across model families (5.5--74\%; Table~\ref{tab:frontier_sc_cross}) and scales (4B--72B; \S\ref{sec:scaling}).
5	Free-form decoding confirms this is model-intrinsic rather than decoder-induced (within-instance LP std ratio $0.97{\times}$; \S\ref{sec:selection_gap}).
6	
7	\paragraph{Practical implications.}
8	The framework provides a pre-deployment diagnostic: measure degeneracy and LP-F1 alignment with $N{=}8$ samples before investing in $N{\times}$ inference; when degeneracy exceeds $\theta_{\text{crit}}{=}0.70$, aggregation is unlikely to help.
9	Thresholds are empirically stable across our NER datasets but may require task-specific calibration; generalization beyond 7--14B fine-tuned NER requires dedicated investigation.
10	
11	\paragraph{Conclusion.}
12	We characterize when test-time scaling fails for NER, with exploratory RE and SQL extensions.
13	The diagnostic framework---localizing failure to output convergence and signal alignment collapse---is our primary contribution; whether the capability-diversity tension extends beyond NER remains open.
14	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 3934 · 2026-05-22T12:03:20.150783+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 3935 · 2026-05-22T12:03:20.552479+00:00_

1	Our primary evidence is from NER (four English datasets, 7--14B fine-tuned); the RE extension ($n{=}397$, single dataset) and SQL pilot ($n{=}196$) are exploratory. SciERC results are tentative ($n{=}529$, single training seed). Frontier models exhibit markedly different degeneracy profiles (5.5--74\%; Table~\ref{tab:frontier_sc_cross}), suggesting findings from fine-tuned open-weight models may not fully generalize to proprietary systems.
2	Our framework is diagnostic, not causal: stages resist decomposition into independent effects ($R^2{<}0$; \S\ref{sec:selection_gap}). Under global Holm--Bonferroni ($k{=}57$), the most liberal core claim reaches $p_{\text{HB}}{=}0.055$; under BH FDR, $19/57$ tests are significant at FDR${<}0.05$ including $6/10$ construction comparisons (Appendix~\ref{app:holm}).
3	We evaluate at $N{\in}\{2,\ldots,64\}$; entity-level construction requires $N{\times}$ inference cost for modest gains ($+1$--$1.4$\,pp). We use a single prompt template per task; prompt variations may affect entity recall, degeneracy, and LP distributions.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 3936 · 2026-05-22T12:03:20.553010+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 3937 · 2026-05-22T12:03:20.854272+00:00_

File content (66026 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 3938 · 2026-05-22T12:03:25.415596+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 3939 · 2026-05-22T12:03:25.666929+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & $
…[truncated 4982 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 3940 · 2026-05-22T12:03:25.667435+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 3941 · 2026-05-22T12:03:27.222823+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 1555
}
```

</details>

---


### Tool call

_source line 3942 · 2026-05-22T12:03:34.907892+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "decisions.yaml"
  }
}
```

</details>

---


### Tool result

_source line 3943 · 2026-05-22T12:03:34.908865+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml\", \"content\": \"_next_id: 241\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:23 UTC\\n  summary: 'MVP 方案: ACE05 上验证 structural consistency vs Fleiss'' Kappa 的 correlation\\n    差异'\\n  rationale: 'PMC12888769 用 surface-level Fleiss'' Kappa 在 zero-shot 模型上得到 ρ=0.20-0.28，我们假设\\n    fine-tuned 模型 + structural consistency (soft Jaccard) 能达到 ρ≥0.40。这是整个论文的基础假设——如果\\n    structural consistency 不能更好地预测准确率，后续的 adaptive gating 无从谈起。Phase 0 pilot 设计: Qwen3-8B\\n    fine-tuned on ACE05, N=8 samples, 200 instances, 对比两种 consistency metric 的 Spearman\\n    ρ。Pass ≥0.40, Fail <0.30。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 04:27 UTC\\n  summary: 采纳 Reviewer 审查意见，收紧 MVP pass/fail 标准\\n  rationale: 'Reviewer 指出 5 个问题，全部合理采纳：(1) PASS 必须要求 EAE (high-headroom subtask) ρ≥0.40，仅\\n    NER 通过不够（ceiling effect 可能虚高）；(2) MARGINAL 区间加 time-boxed protocol: N=16 追加 +\\n    1天上限；(3) 加 fine-tuning 质量门控 (NER≥73, EAE≥45)，模型不行时先修 fine-tuning；(4) ACE05 今天必须确认；(5)\\n    监控 T=1.0 per-sample F1 分布，>30% F1=0 时追加 T=0.7。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 04:53 UTC\\n  summary: SciERC RE 替代 ACE05 EAE 作为 MVP high-headroom subtask\\n  rationale: ACE05 需 LDC 许可，用户未确认。SciERC 公开可得，有 NER+RE 两个 subtask。RE base F1 ~47（与\\n    ACE05 EAE ~52 相当），结构复杂度高（entity pair + relation type），headroom 大，是 EAE 的合理替代。PASS\\n    标准更新为 RE ρ≥0.40。需要补实现 RE 的 consistency + evaluation + pipeline 支持。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:38 UTC\\n  summary: 'Gate 0: NER PASS (60.4%), RE FAIL (33.8%). 执行方案 C——当前模型先跑 pilot + 追训改进版，需修复\\n    RE evaluation'\\n  rationale: RE 33.8% 低于 40% 阈值但不阻塞 pilot：(1) headroom 大，oracle best-of-N 有提升空间；(2)\\n    consistency correlation 不要求高绝对 F1，要求 per-instance variance；(3) 弱模型上验证假设结论更强。但\\n    Reviewer 发
…[truncated 10901 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 3944 · 2026-05-22T12:03:35.010077+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 3945 · 2026-05-22T12:03:35.161035+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 3946 · 2026-05-22T12:03:35.311957+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 3947 · 2026-05-22T12:03:35.463478+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_0.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_5.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_7.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_7_consistency.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_9.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_10.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/data_integrity_audit_v2.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_11.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_12.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_13.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_14.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_
…[truncated 2228 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 3948 · 2026-05-22T12:03:35.564237+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "output_mode": "content",
  "glob": "*.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "output_mode": "content",
    "glob": "*.yaml"
  }
}
```

</details>

---


### Tool result

_source line 3949 · 2026-05-22T12:03:35.716491+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 3950 · 2026-05-22T12:04:13.099745+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "struct_self_consist_ie",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 3951 · 2026-05-22T12:04:43.168599+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 30068
}
```

</details>

---


### Tool call

_source line 3952 · 2026-05-22T12:04:44.022098+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**审查侧重：方法严谨性 + 实验充分性**\n\n### Venue 信息\n- **目标会议**: EMNLP 2026 (via ARR May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页，参考文献不限，Limitations/Ethics 不计入\n- **模板**: ACL (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **Overall Assessment 标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 论文路径\n- LaTeX 主文件: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_37/submitted.pdf`\n- 各章节在 `sections/` 子目录下\n\n### 论文概述\n标题：\"When Does Test-Time Scaling Fail? Boundary Conditions for Named Entity Recognition\"\n研究 test-time compute scaling（self-consistency, best-of-N）在 NER 上的失败边界条件。核心发现：quality estimation 信号能预测输出质量（AUROC 0.82）但 instance-level selection 几乎无增益（<1pp），这个 correlation-selection gap 归因于 output convergence（degeneracy 12-68%）和 signal alignment collapse（α→0）。\n\n### 你的审查重点\n\n**1. Diagnostic Framework 有效性**\n- \"simultaneously necessary conditions\" 的表述是否准确？degeneracy + alignment collapse 是否真正是 jointly necessary，还是仅仅是 correlated factors？\n- 框架声称是 diagnostic 而非 predictive（$R^2 < 0$），这是否削弱了实际贡献？\n- $\\theta_{\\text{crit}} = 0.70$ 的经验阈值稳定性如何——是否在所有测试配置下一致？\n\n**2. 统计严谨性**\n- 全局 Holm-Bonferroni 下 $p_{\\text{adj}} = 0.055$，作者选择 per-family correction（$k=10$）达到 $p_{\\text{adj}} = 0.006$。这个选择是否合理？是否存在 cherry-picking 风险？\n- 多重比较处理（$k=57$ 全局 vs $k=10/21/9$ 分族）的合理性\n- Bootstrap CI、power analysis 是否充分——SciERC $n=529$ 是否足够支撑 claims？\n- 3-seed 报告的标准差（$\\sigma \\leq 0.026$）是否在所有关键结论上都充分？\n\n**3. 实验设计**\n- Few-NERD 3 epoch vs 其他数据集 5 epoch 的 confound 处理是否充分——作者声称这是 feature 而非 bug，是否令人信服？\n- RE 只有 SciERC 一个数据集（$n=397$），SQL 是 pilot（$n=196$）——exploratory extension 的 claim 是否与呈现方式一致？\n- 主要结果来自 Qwen3-8B 和 LLaMA-3.1-8B，4B/14B 是 ablation，72B 和 GPT-5.5 是 tentative——generalization claim 的支撑是否充分？\n- 评估指标（macro F1 + exact span-and-type match）是否全面？是否遗漏了其他重要度量？\n\n**4. 实验完整性**\n- Hidden-state probe 使用 Qwen2.5-7B 而非主实验的 Qwen3-8B——模型不一致是否被充分 justify？\n- Cross-model ensemble 只测了 Qwen + LLaMA 一个组合——是否足够？\n- Entity-level construction 的 $\\theta = 2/N$ 是否经过充分的 sensitivity analysis？\n- WNUT-17 ($n=1287$, 51% zero F1) 的使用——在这样极端的设定下结论是否可靠？\n\n**5. 公式和定理**\n- Proposition 1 (Entity Selection Diagnostic) 的假设是否合理？entity-wise independence 的简化对结论影响多大？\n- MBR formulation 是否正确——entity construction 作为 MBR decoding 的映射是否准确？\n- Degeneracy bound $(1-D) \\cdot G_{\\text{nd}} \\cdot \\alpha$ 只 capture 3-12% actual gains——这个 bound 是否过于 loose 以至于缺乏实用价值？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**审查侧重：方法严谨性 + 实验充分性**\n\n### Venue 信息\n- **目标会议**: EMNLP 2026 (via ARR May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页，参考文献不限，Limitations/Ethics 不计入\n- **模板**: ACL (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **Overall Assessment 标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 论文路径\n- LaTeX 主文件: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_37/submitted.pdf`\n- 各章节在 `sections/` 子目录下\n\n### 论文概述\n标题：\"When Does Test-Time Scaling Fail? Boundary Conditions for Named Entity Recognition\"\n研究 test-time compute scaling（self-consistency, best-of-N）在 NER 上的失败边界条件。核心发现：quality estimation 信号能预测输出质量（AUROC 0.82）但 instance-level selection 几乎无增益（<1pp），这个 correlation-selection gap 归因于 output convergence（degeneracy 12-68%）和 signal alignment collapse（α→0）。\n\n### 你的审查重点\n\n**1. Diagnostic Framework 有效性**\n- \"simultaneously necessary conditions\" 的表述是否准确？degeneracy + alignment collapse 是否真正是 jointly necessary，还是仅仅是 correlated factors？\n- 框架声称是 diagnostic 而非 predictive（$R^2 < 0$），这是否削弱了实际贡献？\n- $\\theta_{\\text{crit}} = 0.70$ 的经验阈值稳定性如何——是否在所有测试配置下一致？\n\n**2. 统计严谨性**\n- 全局 Holm-Bonferroni 下 $p_{\\text{adj}} = 0.055$，作者选择 per-family correction（$k=10$）达到 $p_{\\text{adj}} = 0.006$。这个选择是否合理？是否存在 cherry-picking 风险？\n- 多重比较处理（$k=57$ 全局 vs $k=10/21/9$ 分族）的合理性\n- Bootstrap CI、power analysis 是否充分——SciERC $n=529$ 是否足够支撑 claims？\n- 3-seed 报告的标准差（$\\sigma \\leq 0.026$）是否在所有关键结论上都充分？\n\n**3. 实验设计**\n- Few-NERD 3 epoch vs 其他数据集 5 epoch 的 confound 处理是否充分——作者声称这是 feature 而非 bug，是否令人信服？\n- RE 只有 SciERC 一个数据集（$n=397$），SQL 是 pilot（$n=196$）——exploratory extension 的 claim 是否与呈现方式一致？\n- 主要结果来自 Qwen3-8B 和 LLaMA-3.1-8B，4B/14B 是 ablation，72B 和 GPT-5.5 是 tentative——generalization claim 的支撑是否充分？\n- 评估指标（macro F1 + exact span-and-type match）是否全面？是否遗漏了其他重要度量？\n\n**4. 实验完整性**\n- Hidden-state probe 使用 Qwen2.5-7B 而非主实验的 Qwen3-8B——模型不一致是否被充分 justify？\n- Cross-model ensemble 只测了 Qwen + LLaMA 一个组合——是否足够？\n- Entity-level construction 的 $\\theta = 2/N$ 是否经过充分的 sensitivity analysis？\n- WNUT-17 ($n=1287$, 51% zero F1) 的使用——在这样极端的设定下结论是否可靠？\n\n**5. 公式和定理**\n- Proposition 1 (Entity Selection Diagnostic) 的假设是否合理？entity-wise independence 的简化对结论影响多大？\n- MBR formulation 是否正确——entity construction 作为 MBR decoding 的映射是否准确？\n- Degeneracy bound $(1-D) \\cdot G_{\\text{nd}} \\cdot \\alpha$ 只 capture 3-12% actual gains——这个 bound 是否过于 loose 以至于缺乏实用价值？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准）。"
  }
}
```

</details>

---


### Tool result

_source line 3953 · 2026-05-22T12:05:10.049315+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 26027
}
```

</details>

---


### Tool call

_source line 3954 · 2026-05-22T12:05:10.247059+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**审查侧重：新颖性 + 完整性 + 写作质量**\n\n### Venue 信息\n- **目标会议**: EMNLP 2026 (via ARR May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页，参考文献不限，Limitations/Ethics 不计入\n- **模板**: ACL (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **Overall Assessment 标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 论文路径\n- LaTeX 主文件: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_37/submitted.pdf`\n- 各章节在 `sections/` 子目录下\n\n### 论文概述\n标题：\"When Does Test-Time Scaling Fail? Boundary Conditions for Named Entity Recognition\"\n以 NER 为主要 case study（4 个数据集，7-14B fine-tuned 模型），辅以 RE 和 SQL 的 exploratory extension，研究 test-time compute scaling 在 structured IE 任务上的失败边界条件。核心贡献是一个 diagnostic framework，定位失败到 output convergence + signal alignment collapse。\n\n### 你的审查重点\n\n**1. 新颖性评估（核心）**\n- 核心发现是 negative result（test-time scaling fails for NER）——negative results 本身有价值，但 diagnostic framework 是否提供了足够新颖的 insight 超越\"it doesn't work\"？\n- 与 Yao et al. (2026) 的区分——他们已报告 task-level QE correlation for NER/RE；本文的 instance-level 诊断 + correlation-selection gap 分析是否构成足够增量？\n- 与 Yun & Kim (2025) 的 \"diversity collapse\" 概念的区分——Table 中声称有 definitional difference，但实际区分是否清晰？\n- \"capability-diversity tension\" 是否是 genuine new insight 还是对已知现象的重新标签？\n- Entity-level construction 作为 bypass 方案——+1.40pp 的增益在 NER 语境下是否有实际意义？\n\n**2. Related Work 覆盖**\n- 搜索并验证以下相关领域是否被充分覆盖：\n  - Conformal prediction for NER / structured prediction\n  - Token-level uncertainty estimation for NER\n  - Ensemble methods for IE (non-SC approaches)\n  - MBR decoding for structured outputs (beyond translation)\n  - Test-time training / adaptation for NER\n  - Prompt-based NER recent advances (2024-2026)\n  - Output calibration for structured prediction\n- 引用数量是否充足？引用是否存在年份偏差（过度偏向某些年份）？\n- 是否遗漏关键的竞争性方法？\n\n**3. 论文结构和叙事**\n- Title \"When Does Test-Time Scaling Fail?\" 是否过于 negative / clickbait？是否准确反映内容？\n- Abstract 信息密度极高——是否可读？关键信息是否遗漏？\n- Introduction 的三阶段结构（Discover → Diagnose → Explore bypasses）是否清晰？\n- Related Work 放在 Section 8（Experiments 之后）是否合适？通常 ACL 论文放在 Section 2\n- Discussion/Conclusion 合并为一节——是否充分总结了贡献和局限？\n- 各 Section 之间的 transition 是否流畅——论文读起来像一个连贯的 story 还是一堆拼接的实验？\n\n**4. 写作质量**\n- 术语一致性：degeneracy / convergence / diversity collapse 是否混用？\n- 数字呈现：论文充满了数字（ρ, AUROC, pp, Δ, σ），是否 overwhelming？哪些可以移到 appendix？\n- Claim hedging 是否恰当：\"tentative\", \"exploratory\", \"observed tendency\" 等词是否用得太多或太少？\n- 论文是否过于依赖 appendix？核心论点是否在正文 8 页内自洽？\n- 是否有 AI-generated 痕迹或不自然的表述？\n\n**5. 格式与合规**\n- Double-blind 是否完整——检查是否有 self-citation leak、代码链接泄露、acknowledgment 泄露\n- 正文是否在 8 页限制内？\n- Limitations section 是否充分但不过长？\n- Ethics statement 是否恰当？\n- 参考文献格式是否一致？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**审查侧重：新颖性 + 完整性 + 写作质量**\n\n### Venue 信息\n- **目标会议**: EMNLP 2026 (via ARR May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **页数限制**: 正文 8 页，参考文献不限，Limitations/Ethics 不计入\n- **模板**: ACL (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **Overall Assessment 标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 论文路径\n- LaTeX 主文件: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_37/submitted.pdf`\n- 各章节在 `sections/` 子目录下\n\n### 论文概述\n标题：\"When Does Test-Time Scaling Fail? Boundary Conditions for Named Entity Recognition\"\n以 NER 为主要 case study（4 个数据集，7-14B fine-tuned 模型），辅以 RE 和 SQL 的 exploratory extension，研究 test-time compute scaling 在 structured IE 任务上的失败边界条件。核心贡献是一个 diagnostic framework，定位失败到 output convergence + signal alignment collapse。\n\n### 你的审查重点\n\n**1. 新颖性评估（核心）**\n- 核心发现是 negative result（test-time scaling fails for NER）——negative results 本身有价值，但 diagnostic framework 是否提供了足够新颖的 insight 超越\"it doesn't work\"？\n- 与 Yao et al. (2026) 的区分——他们已报告 task-level QE correlation for NER/RE；本文的 instance-level 诊断 + correlation-selection gap 分析是否构成足够增量？\n- 与 Yun & Kim (2025) 的 \"diversity collapse\" 概念的区分——Table 中声称有 definitional difference，但实际区分是否清晰？\n- \"capability-diversity tension\" 是否是 genuine new insight 还是对已知现象的重新标签？\n- Entity-level construction 作为 bypass 方案——+1.40pp 的增益在 NER 语境下是否有实际意义？\n\n**2. Related Work 覆盖**\n- 搜索并验证以下相关领域是否被充分覆盖：\n  - Conformal prediction for NER / structured prediction\n  - Token-level uncertainty estimation for NER\n  - Ensemble methods for IE (non-SC approaches)\n  - MBR decoding for structured outputs (beyond translation)\n  - Test-time training / adaptation for NER\n  - Prompt-based NER recent advances (2024-2026)\n  - Output calibration for structured prediction\n- 引用数量是否充足？引用是否存在年份偏差（过度偏向某些年份）？\n- 是否遗漏关键的竞争性方法？\n\n**3. 论文结构和叙事**\n- Title \"When Does Test-Time Scaling Fail?\" 是否过于 negative / clickbait？是否准确反映内容？\n- Abstract 信息密度极高——是否可读？关键信息是否遗漏？\n- Introduction 的三阶段结构（Discover → Diagnose → Explore bypasses）是否清晰？\n- Related Work 放在 Section 8（Experiments 之后）是否合适？通常 ACL 论文放在 Section 2\n- Discussion/Conclusion 合并为一节——是否充分总结了贡献和局限？\n- 各 Section 之间的 transition 是否流畅——论文读起来像一个连贯的 story 还是一堆拼接的实验？\n\n**4. 写作质量**\n- 术语一致性：degeneracy / convergence / diversity collapse 是否混用？\n- 数字呈现：论文充满了数字（ρ, AUROC, pp, Δ, σ），是否 overwhelming？哪些可以移到 appendix？\n- Claim hedging 是否恰当：\"tentative\", \"exploratory\", \"observed tendency\" 等词是否用得太多或太少？\n- 论文是否过于依赖 appendix？核心论点是否在正文 8 页内自洽？\n- 是否有 AI-generated 痕迹或不自然的表述？\n\n**5. 格式与合规**\n- Double-blind 是否完整——检查是否有 self-citation leak、代码链接泄露、acknowledgment 泄露\n- 正文是否在 8 页限制内？\n- Limitations section 是否充分但不过长？\n- Ethics statement 是否恰当？\n- 参考文献格式是否一致？\n\n请给出结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（使用 EMNLP 2026 评分标准）。"
  }
}
```

</details>

---


### Tool result

_source line 3955 · 2026-05-22T12:05:12.165703+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1918
}
```

</details>

---


### Assistant

_source line 3956 · 2026-05-22T12:05:24.865394+00:00_

圆桌审稿已启动。

**Round 37 审稿编排**：

| 角色 | 侧重 | 状态 |
|------|------|------|
| Reviewer 1 | 方法严谨性 + 实验充分性 | ✅ 已派发 |
| Reviewer 2 | 新颖性 + 完整性 + 写作质量 | ✅ 已派发 |
| 视觉审查 Agent | PDF 排版质量 | ✅ 已启动（并行，不阻塞） |
| 外部审稿 | — | ⏭️ 未启用，跳过 |

**论文**："When Does Test-Time Scaling Fail? Boundary Conditions for Named Entity Recognition"
**Venue**：EMNLP 2026 via ARR（Long Paper, 8 页正文限制，double-blind）
**Deadline**：2026-05-25

等待两位 Reviewer 返回初审意见后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 296

## Round 296

2 recorded events


### User

_source line 3957 · 2026-05-22T12:10:07.485728+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — Round 1 审稿意见

**论文**: "When Does Test-Time Scaling Fail? Boundary Conditions for Named Entity Recognition"
**审查侧重**: 方法严谨性 + 实验充分性

---

## 总体评分

**Overall Assessment**: 3.5 / 5 (Borderline Conference)

**一句话总结**: 一项规模罕见的 test-time scaling 负面结果实证研究，diagnostic framework 的分解思路清晰，但核心 claim 的统计支撑存在方法论隐患（Holm-Bonferroni correction 策略选择），且 framework 自身承认无预测力（$R^2 < 0$），削弱了实际贡献。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5 / 5 | 实验设计总体严谨、ablation 极其充分，但 Holm-Bonferroni correction 的 family 划分选择存在 post-hoc cherry-picking 风险；"simultaneously necessary conditions" 的表述超出了相关性证据能支撑的范围 |
| Excitement | 3 / 5 | 研究问题重要且及时（TTS 何时失败），负面结果对社区有价值；但 diagnostic framework 缺乏预测力、bound 过松（3-12%），实际可操作性有限 |
| Reproducibility | 4 / 5 | 代码承诺公开，prompt 模板在 Appendix 中，3-seed 报告，统计检验完整；但 hidden-state probe 模型不一致（Qwen2.5-7B vs Qwen3-8B）降低了部分结果的可复现置信度 |
| Confidence | 4 / 5 | 我熟悉 test-time compute scaling、self-consistency、NER evaluation 方面的文献，仔细阅读了全部 44 页 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **Holm-Bonferroni correction 的 family 划分存在 cherry-picking 风险**
- 具体位置：§4 para 3, §7.5, Appendix f (Table 12)
- 问题：全局 Holm-Bonferroni 在 $k=57$ 下 $p_{\text{adj}}=0.055$，未达到 $\alpha=0.05$ 的常规阈值。作者转而采用 per-family correction（$k=10$ for selection family），得到 $p_{\text{adj}}=0.006$。论文在 §7.5 和 Appendix f 中报告了这一事实，但存在关键方法论问题：
  - **correction 策略是否 pre-registered？** 如果全局 correction 是初始计划，转向 per-family 就构成 post-hoc adjustment。论文没有说明 per-family grouping 是 pre-specified 还是在看到全局结果后选择的。
  - 全局 $p_{\text{adj}}=0.055$ 意味着论文最核心的 claim（"LP is the only signal achieving significant positive selection"）在最保守的多重比较校正下实际上不显著。这直接影响 §4 和 Abstract 中 LP 作为唯一正向 selection signal 的 claim。
  - Per-family correction 在 family 定义合理时是 legitimate 的方法学选择，但论文需要更强的 justification——为什么 selection/construction/calibration 构成独立的 hypothesis families，而不是同一个 umbrella hypothesis（"TTS signals work for NER"）的不同 facets。
- 为什么影响接收：这是论文的 headline statistical claim。如果读者采用全局 correction，核心发现变为 "no signal achieves significant positive selection"，这改变了论文的叙事。
- 建议修改方向：(1) 在 main text 正文中透明报告两种 correction 结果（目前全局 $p$ 只出现在 Appendix f）；(2) 提供 pre-registration 或 a priori 的 family 划分理由；(3) 将 LP 的 selection 优势描述为 "marginally significant under global correction" 而非绝对 claim。

**N2** [critical] **"Simultaneously necessary conditions" 的 claim 超出了证据支撑**
- 具体位置：§4 ("jointly determine"), Abstract ("A diagnostic framework identifies two boundary conditions"), §6.3 ("simultaneously necessary")
- 问题：论文声称 degeneracy 和 signal alignment collapse 是 correlation-selection gap 的 "simultaneously necessary conditions"。但证据结构是：
  - 当两者都不严重时，gains 存在（§5.1 cross-model, §7.5 construction bypass）
  - 当任一严重时，gains 消失
  - 这建立的是 **correlational co-occurrence**，不是 logical necessity。要证明 "necessary"，需要证明移除任一条件总是恢复 gains——但论文承认移除 degeneracy（如 cross-model ensemble）只 "partially bypasses" the bottleneck（§5.1, Table 2）
  - Degeneracy bound $(1-D) \cdot G_{\text{nd}} \cdot \alpha$ 只 capture 3-12% actual gains（§6.3），说明这个分解遗漏了大量 variance。如果 decomposition 只解释 3-12%，声称其组成部分是 "necessary conditions" 是过度的
- 为什么影响接收：这是论文的核心理论贡献。如果降级为 "correlated factors"，framework 的概念新颖性显著降低。
- 建议修改方向：(1) 将 "simultaneously necessary conditions" 改为 "two co-occurring factors that characterize the gap" 或 "jointly sufficient descriptors"；(2) 明确讨论 bound 的 looseness 对 necessity claim 的影响；(3) 说明在什么条件下 necessity 可被 falsified。

**N3** [critical] **Diagnostic framework 自认无预测力——实际贡献的定位需要更诚实的讨论**
- 具体位置：§4 para 4 ("$R^2 < 0$"), §6.3 ("diagnostic rather than predictive"), §9 Discussion
- 问题：论文多处承认 framework 是 "diagnostic not predictive"、$R^2 < 0$、degeneracy "does not predict LP gain across datasets"（§4, Table 4 caption 附近）。但这个自我限定与论文的定位之间存在张力：
  - Title（"Boundary Conditions"）暗示可预测性——"boundary" 暗示一旦条件满足/不满足可以判断 scaling 的成败
  - Abstract 和 Introduction 的 framing 强调 framework 能 "predict when gains vanish"（$\theta_{\text{crit}}=0.70$）
  - 但 $\theta_{\text{crit}}=0.70$ 是从数据中拟合的经验阈值，没有 held-out validation 证明其 generalize 到新 dataset/task
  - 如果 framework 只能 post-hoc 解释已观察到的 pattern，对 practitioner 的指导价值有限——用户无法在实验前判断是否值得投入 TTS compute
- 为什么影响接收：论文的实用价值（practitioner 指导）依赖于某种程度的预测力。如果只是 post-hoc diagnostic，贡献更接近 "detailed empirical analysis" 而非 "framework"。
- 建议修改方向：(1) 在 §1 和 §9 中明确区分 "diagnostic" vs "predictive" 的 scope，不要在 title/abstract 中使用暗示预测力的语言；(2) 讨论将 $\theta_{\text{crit}}$ generalize 到新任务需要什么条件；(3) 提供 leave-one-dataset-out cross-validation 验证 $\theta_{\text{crit}}$ 的稳定性（目前只在 Appendix 中提到 LOO 0.51-1.21 range，但没有系统的 cross-validation）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **Hidden-state probe 的模型不一致缺乏充分 justification**
- 具体位置：§3 ("hidden-state probe"), Appendix h.3
- 问题：主实验使用 Qwen3-8B，但 hidden-state probe 使用 Qwen2.5-7B。Appendix h.3 的解释是 Qwen3-8B checkpoint 带有 empty `&lt;think>&lt;/think>` blocks。但这意味着 probe 结论（"quality information is partially encoded in hidden representations"）实际上只在 Qwen2.5-7B 上验证了，不能直接迁移到 Qwen3-8B——两者的 architecture 和 representation space 可能不同。
- 建议：(1) 在 Qwen3-8B 上也训练 probe（去掉 thinking tokens 后提取 hidden states）；或 (2) 明确将 probe 结论限定为 Qwen2.5 family。

**W2** [warning] **模型多样性不足以支撑 generalization claim**
- 具体位置：§7.1, §9, Abstract ("two model families")
- 问题：主要结果来自 Qwen3-8B 和 LLaMA-3.1-8B（均为 8B 级别开源模型）。4B/14B 是 ablation（Appendix x），72B 是 "tentative"（few-shot only, Table 44），GPT-5.5 仅在 Appendix 中以 zero-shot 出现（Table 44 提到 "GPT-5.5: 5% degeneracy"）。
  - 8B 模型的 degeneracy 特征可能不代表更大模型——Table 44 暗示 72B 的 degeneracy 显著不同
  - 没有测试 instruction-tuned proprietary models（如 Claude/GPT-4 level）的 fine-tuned 变体
  - "capability-diversity tension" 是论文的重要 insight，但几乎完全基于 8B-level 推断
- 建议：(1) 要么扩大模型覆盖，要么将 generalization claim 明确限定为 "7-14B open-weight fine-tuned models"；(2) 讨论为什么 72B/proprietary 的 limited evidence 足够或不足够。

**W3** [warning] **RE extension（n=397, 单数据集）和 SQL pilot（n=196）的证据过薄**
- 具体位置：§7.5, Appendix o (RE), 主文对 SQL 的提及
- 问题：RE 仅用 SciERC RE（n=397 full, n=238 non-zero），SQL 是 Spider 的 pilot（n=196）。论文在正文中将这些标记为 "exploratory"，但：
  - Abstract 提及 "exploratory extensions to RE and SQL parsing"，给读者的印象比实际证据更强
  - RE 结果（Table 29-30, Appendix o）显示 "no signal outperforms greedy"，但 n=397 的 power 不足以排除 moderate effect sizes
  - SQL 的 87.2% degeneracy 是一个极端值，基于单一数据集的单一 split 无法判断是 SQL 任务的固有特征还是 prompt/model 的 artifact
- 建议：(1) 在 abstract 中弱化 RE/SQL 的存在感，或加 "preliminary" 限定词；(2) 为 RE 提供 power analysis 说明 n=397 能检测到多大的 effect。

**W4** [warning] **Few-NERD 3 epoch confound 的讨论不够有力**
- 具体位置：§7.3, Appendix ab (Tables 55-56)
- 问题：Few-NERD 使用 3 epoch（其他数据集 5 epoch），论文声称这是 "feature not bug" 因为不同 training convergence 揭示不同 degeneracy regime（Appendix ab, Table 55）。但：
  - 3 vs 5 epoch 同时改变了 degeneracy 和 model quality，无法 disentangle 两者的效应
  - Table 55 显示 5-epoch Few-NERD 的 greedy F1 (0.798) vs 3-epoch (0.791) 差异不大，但 degeneracy 从 8.8% 升到 ≈17.8%——这本身就是一个值得解释的现象
  - 如果 "training convergence modulates degeneracy" 是论文的 claim（§ab, Appendix），那这应该是一个独立的 controlled experiment 而非作为 default 设置的 confound
- 建议：在 main text 中简要承认这个 confound 并引用 Appendix 的 ablation，而不仅仅是在 Appendix 中讨论。

**W5** [warning] **$\theta_{\text{crit}} = 0.70$ 的 stability 未经系统验证**
- 具体位置：§4, §6.1 ("where headroom allows; $\theta_{\text{crit}}=0.70$")
- 问题：$\theta_{\text{crit}}=0.70$ 在不同 dataset/model 上是否稳定？论文没有提供 $\theta_{\text{crit}}$ 在各 configuration 下的变异分析。Appendix 中的 LOO cross-validation（§ah.1）报告 LOO regret 从 0.51 到 1.21 pp，但这不等于验证 $\theta_{\text{crit}}$ 本身的稳定性。
  - Table 22 的 ε sensitivity sweep（ε=0.01 到 0.20）只在 SciERC NER 上做了
  - 不同 dataset 的 degeneracy 分布差异很大（SciERC 12.2% vs Few-NERD 68%）——在如此不同的 regime 下同一 $\theta_{\text{crit}}$ 是否合理？
- 建议：提供 $\theta_{\text{crit}}$ 在所有 dataset × model 组合上的 calibration 结果，或讨论为什么单一阈值在不同 degeneracy regime 下仍然有效。

---

## 小问题（不影响接收）

- **M1**: Figure 1 信息密度很高，但 "Selection Fails" 和 "Construction Works" 的因果箭头暗示了论文尚未 fully establish 的因果关系。建议改为 "associated with" 或 "coincides with" 的视觉表达。
- **M2**: §2.1 中 "A per-sample signal $s_i$" 的定义提到 4/5 signals 是 instance-level aggregates（对 N 个 candidate 的所有 entities 聚合），只有 LP 是 per-sample 的。但直到 §2.2 才解释各 signal 的具体定义——前向引用造成理解中断。
- **M3**: Proposition 1 的 entity-wise independence 假设（Appendix p.5）在论文自己的数据中被 entity correlation 数据部分违反（Appendix p.5 报告 "actual entity correlations (split-half) ≈0.576-0.634"），bound 因此从理论值衰减到 3-12%。这个 gap 值得在主文中至少一句话提及（目前只在 Appendix 讨论）。
- **M4**: Table 3（§7.2, p.7）的 AUROC binarizes at per-dataset median F1。这个 binarization 阈值的选择会影响 AUROC 值，但论文没有报告 sensitivity（如用 quartile 或 mean 作为阈值时 AUROC 如何变化）。
- **M5**: §8 Related Work 的 "Capability ceiling vs. diversity collapse" 段落引用 Yun et al. (2025)，但对比不够具体——Yun 的 "diversity collapse" 与本文的 "degeneracy" 有何异同？measurement 方式不同时，结论的可比性需要讨论。

---

## 主要优势

1. **研究问题的重要性和及时性**：TTS 在 reasoning tasks 上的成功推动了大量后续工作，系统研究其在 structured prediction 上的失败模式对社区极有价值。这是一个需要有人回答的问题。

2. **实证规模和严谨性极为突出**：44 页包含 66 张表格、11 张图，覆盖 4 NER + 1 RE + 1 SQL 数据集、9 种方法、7 种 verification 模式。每个 claim 都有 bootstrap CI、permutation test、多重比较校正。这种 thoroughness 在 NLP 论文中非常罕见。

3. **诚实的自我限定**：论文多处坦承 framework 是 diagnostic 而非 predictive、bound 过松、RE/SQL 是 exploratory。这种 intellectual honesty 增强了 credibility，即使也暴露了贡献的边界。

4. **Correlation-selection gap 的分解思路有洞察力**：将 "signals predict quality but can't select better outputs" 分解为 degeneracy (输出空间坍缩) + alignment collapse (信号与 gain 脱耦)，这个 decomposition 即使不是 "necessary conditions" 也提供了有用的分析框架。

5. **Entity-level construction 的正面结果**：§7.5 的 entity-level construction（$\theta = 2/N$, LP-weighted）部分绕过 instance-level 瓶颈的发现是有建设性的 positive contribution，不仅仅是报告 failure。

6. **实验基础设施的完整性**：44 页 Appendix 中的 failure mode gallery（Appendix ag）、per-type LP analysis（Tables 51-53）、free-form decoding ablation（Appendix q）等展示了对 edge case 的 thorough investigation。

---

## 缺失引用 / 相关工作覆盖

- 论文引用了主要的 TTS/SC 文献（Wang et al. 2023, Brown et al. 2024, Chen et al. 2024a/b），但在 structured prediction 的 uncertainty estimation 方面可以补充：
  - **Xiao & Wang (2021)** "Hallucination and Beyond: A Survey on Large Language Models" 中对 LLM calibration 在 structured outputs 上的讨论
  - 论文提到了 conformal prediction (Fisch et al. 2021; Angelopoulos and Bates 2023) 但没有讨论 recent work on **conformal prediction for structured outputs**（如 sequence labeling 的 coverage guarantees），这与论文的 entity-level construction 有关
  - **Self-consistency for IE** 的更广泛 context：Wadhwa et al. (2023) 在 RE 上的 self-consistency 结果（如果存在的话）是否与本文 RE extension 的发现一致？

---

## Questions to Authors

Q1: 全局 Holm-Bonferroni 的 $p_{\text{adj}}=0.055$ 是否是在看到 per-family 结果之后才报告的？能否确认 family 划分是 pre-specified 的？

Q2: 如果一个 practitioner 拿到一个新的 structured prediction task，diagnostic framework 能告诉他什么？他需要先跑完 N=8 samples 的 full experiment 才能计算 degeneracy 和 alignment——但到那时他已经有了结果，framework 的 post-hoc diagnosis 还有什么价值？

Q3: Entity-wise independence 假设下 bound 只 capture 3-12%——这意味着 88-97% 的 variance 来自 entity 间的 correlation。是否考虑过 entity-group level 的 decomposition（如按 sentence 内 entity 组分解）来 tighten the bound？

Q4: Cross-model ensemble（§5.1）只测了 Qwen + LLaMA。如果用两个 Qwen 变体（如 Qwen3-8B + Qwen3-4B）做 ensemble，degeneracy 的 reduction 是否类似？这能帮助区分 "architectural diversity" vs "random initialization diversity" 的效应。

Q5: WNUT-17 51% zero-F1 samples 的结论推广性如何？这些 zero-F1 instances 主要是因为 entity type 本身 rare（social media entities）还是因为 model failure？如果是前者，结论对 mainstream NER 的意义有限。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 3958 · 2026-05-22T12:10:16.344435+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 297

## Round 297

2 recorded events


### User

_source line 3959 · 2026-05-22T12:10:30.909397+00:00_

[Reviewer 1 审稿结果]:
Round 1 审稿意见已提交给 Review Director。

核心判断：**Overall 3.5（Borderline Conference）**。

三个 Must-Fix 问题：
1. **Holm-Bonferroni correction 策略选择**——全局 $k=57$ 下 $p_{\text{adj}}=0.055$ 不显著，per-family $k=10$ 下才达到 0.006，缺乏 pre-registration 证据，核心 LP selection claim 的统计基础不够稳固
2. **"Simultaneously necessary conditions" 过度 claim**——证据结构是 correlational co-occurrence，bound 只 capture 3-12% variance，不足以支撑 logical necessity
3. **Diagnostic framework 无预测力（$R^2<0$）与 title/abstract 暗示的预测性之间的张力**——$\theta_{\text{crit}}=0.70$ 缺乏 cross-dataset held-out validation

五个 Should-Fix：hidden-state probe 模型不一致、模型多样性不足、RE/SQL 证据过薄、Few-NERD epoch confound、$\theta_{\text{crit}}$ stability 未系统验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 3960 · 2026-05-22T12:10:36.396451+00:00_

Reviewer 1 意见已收到。等待 Reviewer 2 返回后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 298

## Round 298

6 recorded events


### User

_source line 3961 · 2026-05-22T12:14:02.233727+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见

**论文**: "When Does Test-Time Scaling Fail? Boundary Conditions for Named Entity Recognition"
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审查侧重**: 新颖性 + 完整性 + 写作质量

---

## 总体评分

**Overall**: 3.0 (Findings)
**一句话总结**: 实验扎实、框架清晰的 negative result 研究，但核心 insight 的增量新颖性不足以达到主会议水平——诊断框架本质上是对"SC 在高 degeneracy 下失效"这一可预期结论的系统化量化，而非根本性新发现。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计系统全面（4 NER 数据集、2 模型族、9 方法类别），统计分析严谨（bootstrap CI、Holm-Bonferroni 校正）。但框架自承"diagnostic, not causal"（Limitations），且最严格校正下核心 claim 仅达 p_HB=0.055（Limitations 第2段），未过 0.05 阈值。 |
| Excitement | 2.5/5 | 研究问题有实际意义，但核心结论（SC 对 NER 效果差）在直觉上可预期——fine-tuned NER 模型输出高度收敛是已知现象。"capability-diversity tension" 更像是对已知现象的重新标签而非 genuine new insight。Entity-level construction 的 +1.40 pp 增益在 NER 语境下实际意义有限。 |
| Reproducibility | 4/5 | 模型名称、超参数、prompt 模板（Appendix k）、数据集配置均有详细记录。承诺代码开源。唯一扣分：SciERC 仅单一 training seed（Limitations 提及）。 |
| Overall Assessment | 3.0/5 | Findings 水平。实验工作量大且诚实，但新颖性增量有限——在 Yao et al. (2026) 已报告 task-level QE correlation 的基础上，instance-level 诊断的额外贡献不足以支撑主会议录用。 |
| Confidence | 4/5 | 对 test-time scaling、self-consistency、NER 评估方法论均较熟悉，仔细阅读了全文 44 页。 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 核心新颖性声明与 Yao et al. (2026) 的区分不充分

- 具体位置：Section 8 "What is new" 段落；Section 1 第1段
- 问题：论文声称提供"the first instance-level diagnostic framework for NER"（Section 8 最后一段），与 Yao et al. (2026) 的 task-level correlations 形成对比。但 Yao et al. 已经报告了 NER/RE 上的 QE correlation（ρ up to 0.47），且结论方向一致：SC 对结构化 IE 效果有限。本文的 instance-level 分析确实更细粒度，但核心 insight 并无质变——仍然是"质量信号能预测但不能有效选择"。论文需要更明确地论证为什么 instance-level 诊断比 task-level 观察提供了根本不同的理解，而非仅仅是更精细的量化。
- 为什么影响接收：如果增量新颖性不被认可，论文的核心贡献将大幅缩水。
- 建议修改方向：在 Introduction 中用 1-2 句明确说明 instance-level 诊断揭示了哪些 task-level 分析**无法发现**的现象（例如：degeneracy 分布的双峰性、per-instance LP compression 等），而不仅仅说"更细粒度"。

**N2** [critical] "Capability-diversity tension" 概念的原创性存疑

- 具体位置：Section 9 第1段；Abstract 倒数第2句
- 问题：论文将"模型能力越强，输出越收敛，多样性越低"命名为 "capability-diversity tension"，作为 key insight 之一。但这本质上是一个 well-known 现象：更强的模型在 fine-tuning 后输出更确定，temperature sampling 下的有效多样性降低。Yun & Kim (2025) 的 "diversity collapse" 已从格式约束角度描述了类似现象。Table 66（Appendix ag）试图做区分，但 "definitional difference"（response-level vs entity-set convergence）显得表面——底层机制（模型在格式/任务约束下输出收敛）是相同的。将已知现象赋予新名称并不构成新贡献。
- 为什么影响接收：如果此概念不被视为新贡献，论文的理论深度将进一步降低。
- 建议修改方向：(1) 明确承认这与 capacity-confidence 的已知关系，说明本文的贡献是**量化了这一关系在 NER 上的具体边界条件**（如 θ_crit=0.70），而非声称发现了新张力；(2) 或者提供 causal evidence 证明这确实是一个独立于模型 confidence 的机制。

**N3** [critical] Related Work 覆盖存在显著缺口

- 具体位置：Section 8
- 问题：以下直接相关的研究方向覆盖不足或完全缺失：

  (a) **Conformal prediction for NER**：论文仅用一个从句提及 Fisch et al. (2021) 和 Angelopoulos & Bates (2023)（Section 8 "Complementary approaches"），但完全忽略了 2025 年的重要进展：
  - "Conformal Structured Prediction" (ICLR 2025) — 提供了结构化输出的 coverage 保证
  - "Uncertainty Quantification for NER via Full-Sequence and Subsequence Conformal Prediction" (arXiv 2601.16999) — 直接针对 NER 的不确定性量化
  这些工作提供了替代性的理论框架来理解 NER 的不确定性，与本文的诊断框架形成互补或竞争。

  (b) **Token-level uncertainty for sequence labeling**：He et al. (NAACL 2024 Findings) 的 uncertainty transmission 方法直接相关。论文用一个从句 "token-level uncertainty operates below entity level" 打发了整个方向，但没有引用任何具体工作，也没有讨论 token-level 到 entity-level 的聚合方法。

  (c) **Prompt-based NER 的最新进展**：论文使用 prompt-based NER 但不讨论 prompt 设计对输出多样性/质量的影响。GPT-NER (ACL 2025) 的 self-verification 策略与本文的 entity self-judgment probe 有方法论相似性，值得讨论。

- 为什么影响接收：Related work 不完整会影响论文的学术定位和贡献声明的可信度。
- 建议修改方向：补充上述引用，并讨论本文框架与 conformal prediction 方法的关系（一个提供 coverage 保证，一个提供 diagnostic 框架——这本可以是一个有趣的对比）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Entity-level construction 的实际意义不足

- 具体位置：Section 7.5；Table 4
- 问题：Entity-level construction 作为 bypass 方案仅获得 +1.40 pp（Few-NERD，Table 4），且仅在 "low degeneracy and signal alignment provide headroom" 的条件下有效（Abstract）。在 SciERC 上增益更小（+0.32 pp），在 CoNLL 上无显著增益（Table 4）。在 NER 研究中，<1.5 pp 的增益通常被认为在 practical significance 边界上。论文将此作为贡献之一，但增益太小且条件限制太强，使得这个 "bypass" 在实际部署中价值有限。
- 建议：更诚实地讨论这一增益的实际意义，或从贡献列表中降低其位置（目前在 Abstract 中占据显著篇幅）。

**W2** [warning] Abstract 信息密度过高，可读性差

- 具体位置：Abstract（全文）
- 问题：Abstract 9 句话中包含：AUROC 0.82、<1 pp、N=64、12-68%、α→0、40%、+1.40 pp、0.70 等至少 8 个数字/符号。这使得 abstract 读起来像一个 result summary 而非 paper overview。关键 message（SC 对 NER 失效的原因诊断）被淹没在数字中。对比典型 EMNLP best paper 的 abstract，通常仅包含 2-3 个关键数字。
- 建议：减少 abstract 中的数字（保留 AUROC 0.82 和 <1 pp 即可说明 correlation-selection gap），将其他数字移入 introduction。

**W3** [warning] Related Work 放置在 Section 8（Experiments 之后）的影响

- 具体位置：Section 8
- 问题：这种布局意味着读者在读完 6 个 section 的方法和实验后才了解到与 prior work 的关系。虽然 Introduction 简要提及了 Wang et al. (2023) 和 Snell et al. (2025)，但对 Yao et al. (2026)、Yun & Kim (2025)、Eikema & Aziz (2025) 等关键竞争性工作的讨论全部延后到 Section 8。这使得读者在阅读过程中无法即时评估本文的增量贡献。
- 建议：在 Introduction 末尾增加一段简要的 positioning 段落，概括本文与 3-4 个最相关 prior works 的区分，即使 detailed discussion 保留在 Section 8。

**W4** [warning] Discussion/Conclusion 过于单薄

- 具体位置：Section 9（3 个段落，约 15 行）
- 问题：对于一篇包含 4 个 NER 数据集 + RE/SQL 扩展 + 9 种方法比较 + 诊断框架的论文，Discussion 部分极短。缺乏以下讨论：
  - 框架对其他结构化预测任务（IE 之外）的潜在适用性
  - 与 closed-source 模型（GPT-5.5 在 Table 44 中有数据但未在 discussion 中讨论）的行为差异
  - 实际部署中 θ_crit=0.70 阈值的鲁棒性和可推广性
- 建议：扩展 discussion 至 5-6 段，讨论上述 open questions。

**W5** [warning] 术语不完全一致

- 具体位置：全文多处
- 问题："degeneracy"（Section 2.1, 3, 4）、"output convergence"（Abstract, Section 9）、"convergence"（Section 4 标题暗示）三个术语交替使用指代同一概念。Section 8 又引入 "diversity collapse"（Yun & Kim 的术语）进行对比，但有时 degeneracy 和 diversity collapse 的边界模糊。建议在首次定义后统一使用一个术语，其他作为同义词在括号中注明。

---

## 小问题（不影响接收）

- **数字呈现过载**：正文充满 ρ、AUROC、pp、Δ、σ 等数字，几乎每句话都有定量 claim。建议将部分中间结果（如 Table 1 的所有信号 ρ 值）移至 appendix，正文仅保留最关键的 comparison。
- **Claim hedging 适度但偶有过度**："tentative cross-scale observations to 72B"（Abstract）的 hedging 合理，但 "observed tendency"、"exploratory extension" 等在正文中出现频率偏高，可能削弱读者对 NER 核心结果（4 个数据集、2 个模型族）的信心。NER 的结果支撑力已足够，不必每处都加限定词。
- **Appendix 体量**：36 页 appendix 对 8 页正文。虽然 ARR 允许 unlimited appendix，但比例（4.5:1）暗示正文可能遗漏了重要信息。特别是 Holm-Bonferroni 分析（Appendix f, Table 12）对核心 claim 的统计显著性至关重要，应在正文中至少用 1 句话总结关键结论。
- **Figure 1 排版**：Figure 1 的三个 panel 信息密度极高，左中右各包含一个独立的信息流。建议增加 panel 间距或增加 caption 中对阅读顺序的引导。
- **引用数量**：62 篇引用对于这个交叉主题是合理的，但年份分布偏向 2021-2025，缺少对 NER 评估方法论（如 Ratinov & Roth 2009 已引、但 Segura-Bedmar et al. 和其他 shared task evaluation 文献未引）的历史覆盖。

---

## Missing References（建议补充）

1. **Conformal Structured Prediction** (ICLR 2025) — 结构化输出的 conformal prediction 通用算法
2. **Uncertainty Quantification for NER via Full-Sequence and Subsequence Conformal Prediction** (arXiv 2601.16999, 2025) — 直接针对 NER 的 conformal prediction
3. **He et al. (NAACL 2024 Findings)** "Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission" — token-level 不确定性在序列标注中的传播
4. **GPT-NER** (ACL 2025 Findings) — LLM-based NER 的 self-verification 策略，与本文 entity self-judgment probe 方法论相关
5. **Calibrating Structured Output Predictors for NLP** (相关综述) — 结构化输出的校准方法

---

## 主要优势

1. **研究问题定义精确且有实际意义**：在 test-time scaling 被广泛采用的背景下，系统研究其在结构化 IE 上的失败条件是有价值的。
2. **实验设计系统全面**：4 个 NER 数据集（SciERC, CoNLL, Few-NERD, WNUT-17）覆盖了不同领域和难度；2 个模型族（Qwen3, LLaMA-3.1）；9 种方法类别（Table 2）；多种统计检验。
3. **诊断框架的两个维度（degeneracy + signal alignment）分解清晰**：correlation-selection gap 概念（Figure 1）将一个复杂现象分解为可量化的组件。
4. **统计分析严谨诚实**：全局 Holm-Bonferroni 校正（Table 12, k=57）、bootstrap CI（Table 11）、TOST 等价检验（Table 15）。作者坦承最严格校正下 p_HB=0.055 的边界情况。
5. **Negative result 价值**：根据 ARR Reviewer Guidelines (H6)，"If something systematically does not work where it could be expected to, the community does need to know about it." 本文提供了 SC 在 NER 上系统失效的证据。
6. **MBR 理论连接**（Appendix p, Proposition 1）将 entity-level construction 置于 principled 框架下。

---

## 格式合规检查

| 项目 | 状态 | 备注 |
|------|------|------|
| Double-blind | ✓ | `\author{Anonymous}`，代码路径为 "[anonymized URL]" |
| 正文页数 | ✓ | Section 1-9 在 8 页内（pages 1-8） |
| Limitations | ✓ | 3 个要点，覆盖范围（NER-centric）、因果性、成本，长度适当 |
| Ethics Statement | ✓ | 覆盖数据来源、模型类型、无人类标注、实际应用影响 |
| ACL 模板 | ✓ | `\usepackage[review]{acl}` |
| 参考文献格式 | ✓ | 基本一致，混合 inproceedings/article 格式正确 |
| Self-citation leak | 未发现 | 未检测到作者身份泄露 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 3962 · 2026-05-22T12:14:54.156349+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## Step 2 交叉分享 — Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix (N1-N3)、Should-Fix (W1-W5) 和 Minor (M1-M5) 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 — Round 1 审稿意见\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n\n**一句话总结**: 一项规模罕见的 test-time scaling 负面结果实证研究，diagnostic framework 的分解思路清晰，但核心 claim 的统计支撑存在方法论隐患（Holm-Bonferroni correction 策略选择），且 framework 自身承认无预测力（$R^2 < 0$），削弱了实际贡献。\n\n## Must-Fix 问题\n\n**N1** [critical] **Holm-Bonferroni correction 的 family 划分存在 cherry-picking 风险**\n- 全局 Holm-Bonferroni 在 $k=57$ 下 $p_{\\text{adj}}=0.055$，未达到 $\\alpha=0.05$。作者转而采用 per-family correction（$k=10$ for selection family），得到 $p_{\\text{adj}}=0.006$。\n- correction 策略是否 pre-registered？转向 per-family 就构成 post-hoc adjustment。\n- 核心 claim \"LP is the only signal achieving significant positive selection\" 在最保守校正下不显著。\n- 建议：正文中透明报告两种 correction 结果；提供 pre-registration 或 a priori 的 family 划分理由。\n\n**N2** [critical] **\"Simultaneously necessary conditions\" 的 claim 超出了证据支撑**\n- 证据结构是 correlational co-occurrence，不是 logical necessity。\n- Degeneracy bound $(1-D) \\cdot G_{\\text{nd}} \\cdot \\alpha$ 只 capture 3-12% actual gains——如果 decomposition 只解释 3-12%，声称其组成部分是 \"necessary conditions\" 过度。\n- 建议：改为 \"two co-occurring factors that characterize the gap\"。\n\n**N3** [critical] **Diagnostic framework 自认无预测力——实际贡献的定位需要更诚实的讨论**\n- Title \"Boundary Conditions\" 暗示可预测性，但 $R^2 < 0$，$\\theta_{\\text{crit}}=0.70$ 缺乏 held-out validation。\n- 如果 framework 只能 post-hoc 解释已观察到的 pattern，对 practitioner 的指导价值有限。\n- 建议：区分 diagnostic vs predictive scope，提供 leave-one-dataset-out cross-validation。\n\n## Should-Fix 问题\n\n**W1** Hidden-state probe 使用 Qwen2.5-7B 而非主实验 Qwen3-8B，模型不一致缺乏充分 justification。\n\n**W2** 模型多样性不足——主要结果来自两个 8B 级别开源模型，generalization claim 过强。\n\n**W3** RE extension（n=397, 单数据集）和 SQL pilot（n=196）的证据过薄，但 abstract 的呈现方式可能给读者更强的印象。\n\n**W4** Few-NERD 3 epoch confound 讨论不够有力——\"feature not bug\" 的论证不完全令人信服。\n\n**W5** $\\theta_{\\text{crit}} = 0.70$ 的 stability 未经系统验证，不同 degeneracy regime 下同一阈值是否合理。\n\n## Minor 问题\n\n**M1**: Figure 1 的因果箭头暗示了尚未 fully establish 的因果关系。\n**M2**: §2.1 的前向引用造成理解中断。\n**M3**: Proposition 1 的 entity-wise independence 假设被自身数据部分违反（split-half r≈0.58-0.64），应在主文中提及。\n**M4**: Table 3 的 AUROC binarization threshold 选择缺乏 sensitivity 分析。\n**M5**: §8 对 Yun et al. (2025) \"diversity collapse\" 与本文 \"degeneracy\" 的异同对比不够具体。\n\n## 主要优势\n1. 研究问题的重要性和及时性\n2. 实证规模和严谨性极为突出（44 页，66 张表格）\n3. 诚实的自我限定\n4. Correlation-selection gap 的分解思路有洞察力\n5. Entity-level construction 的正面结果\n6. Failure mode gallery 等对 edge case 的 thorough investigation\n\n## Questions\nQ1: 全局 Holm-Bonferroni 的 family 划分是否 pre-specified？\nQ2: 新任务上 diagnostic framework 的 post-hoc diagnosis 还有什么价值？\nQ3: 是否考虑过 entity-group level decomposition 来 tighten the bound？\nQ4: 两个 Qwen 变体 ensemble 是否能区分 architectural vs random initialization diversity？\nQ5: WNUT-17 zero-F1 instances 的成因分析？\n\n---\n\n请逐条 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "## Step 2 交叉分享 — Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix (N1-N3)、Should-Fix (W1-W5) 和 Minor (M1-M5) 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 1 — Round 1 审稿意见\n\n**Overall Assessment**: 3.5 / 5 (Borderline Conference)\n\n**一句话总结**: 一项规模罕见的 test-time scaling 负面结果实证研究，diagnostic framework 的分解思路清晰，但核心 claim 的统计支撑存在方法论隐患（Holm-Bonferroni correction 策略选择），且 framework 自身承认无预测力（$R^2 < 0$），削弱了实际贡献。\n\n## Must-Fix 问题\n\n**N1** [critical] **Holm-Bonferroni correction 的 family 划分存在 cherry-picking 风险**\n- 全局 Holm-Bonferroni 在 $k=57$ 下 $p_{\\text{adj}}=0.055$，未达到 $\\alpha=0.05$。作者转而采用 per-family correction（$k=10$ for selection family），得到 $p_{\\text{adj}}=0.006$。\n- correction 策略是否 pre-registered？转向 per-family 就构成 post-hoc adjustment。\n- 核心 claim \"LP is the only signal achieving significant positive selection\" 在最保守校正下不显著。\n- 建议：正文中透明报告两种 correction 结果；提供 pre-registration 或 a priori 的 family 划分理由。\n\n**N2** [critical] **\"Simultaneously necessary conditions\" 的 claim 超出了证据支撑**\n- 证据结构是 correlational co-occurrence，不是 logical necessity。\n- Degeneracy bound $(1-D) \\cdot G_{\\text{nd}} \\cdot \\alpha$ 只 capture 3-12% actual gains——如果 decomposition 只解释 3-12%，声称其组成部分是 \"necessary conditions\" 过度。\n- 建议：改为 \"two co-occurring factors that characterize the gap\"。\n\n**N3** [critical] **Diagnostic framework 自认无预测力——实际贡献的定位需要更诚实的讨论**\n- Title \"Boundary Conditions\" 暗示可预测性，但 $R^2 < 0$，$\\theta_{\\text{crit}}=0.70$ 缺乏 held-out validation。\n- 如果 framework 只能 post-hoc 解释已观察到的 pattern，对 practitioner 的指导价值有限。\n- 建议：区分 diagnostic vs predictive scope，提供 leave-one-dataset-out cross-validation。\n\n## Should-Fix 问题\n\n**W1** Hidden-state probe 使用 Qwen2.5-7B 而非主实验 Qwen3-8B，模型不一致缺乏充分 justification。\n\n**W2** 模型多样性不足——主要结果来自两个 8B 级别开源模型，generalization claim 过强。\n\n**W3** RE extension（n=397, 单数据集）和 SQL pilot（n=196）的证据过薄，但 abstract 的呈现方式可能给读者更强的印象。\n\n**W4** Few-NERD 3 epoch confound 讨论不够有力——\"feature not bug\" 的论证不完全令人信服。\n\n**W5** $\\theta_{\\text{crit}} = 0.70$ 的 stability 未经系统验证，不同 degeneracy regime 下同一阈值是否合理。\n\n## Minor 问题\n\n**M1**: Figure 1 的因果箭头暗示了尚未 fully establish 的因果关系。\n**M2**: §2.1 的前向引用造成理解中断。\n**M3**: Proposition 1 的 entity-wise independence 假设被自身数据部分违反（split-half r≈0.58-0.64），应在主文中提及。\n**M4**: Table 3 的 AUROC binarization threshold 选择缺乏 sensitivity 分析。\n**M5**: §8 对 Yun et al. (2025) \"diversity collapse\" 与本文 \"degeneracy\" 的异同对比不够具体。\n\n## 主要优势\n1. 研究问题的重要性和及时性\n2. 实证规模和严谨性极为突出（44 页，66 张表格）\n3. 诚实的自我限定\n4. Correlation-selection gap 的分解思路有洞察力\n5. Entity-level construction 的正面结果\n6. Failure mode gallery 等对 edge case 的 thorough investigation\n\n## Questions\nQ1: 全局 Holm-Bonferroni 的 family 划分是否 pre-specified？\nQ2: 新任务上 diagnostic framework 的 post-hoc diagnosis 还有什么价值？\nQ3: 是否考虑过 entity-group level decomposition 来 tighten the bound？\nQ4: 两个 Qwen 变体 ensemble 是否能区分 architectural vs random initialization diversity？\nQ5: WNUT-17 zero-F1 instances 的成因分析？\n\n---\n\n请逐条 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 3963 · 2026-05-22T12:15:14.162463+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20006
}
```

</details>

---


### Tool call

_source line 3964 · 2026-05-22T12:15:14.415700+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "struct_self_consist_ie",
  "text": "## Step 2 交叉分享 — Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix (N1-N3)、Should-Fix (W1-W5) 和 Minor 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 — Round 1 审稿意见\n\n**Overall Assessment**: 3.0 / 5 (Findings)\n\n**一句话总结**: 实验扎实、框架清晰的 negative result 研究，但核心 insight 的增量新颖性不足以达到主会议水平——诊断框架本质上是对\"SC 在高 degeneracy 下失效\"这一可预期结论的系统化量化，而非根本性新发现。\n\n## Must-Fix 问题\n\n**N1** [critical] **核心新颖性声明与 Yao et al. (2026) 的区分不充分**\n- Yao et al. 已报告 NER/RE 上的 QE correlation（ρ up to 0.47），结论方向一致。\n- 本文的 instance-level 分析更细粒度，但核心 insight 并无质变——仍然是\"质量信号能预测但不能有效选择\"。\n- 建议：明确说明 instance-level 诊断揭示了哪些 task-level 分析无法发现的现象。\n\n**N2** [critical] **\"Capability-diversity tension\" 概念的原创性存疑**\n- \"模型能力越强，输出越收敛\" 是 well-known 现象。Yun & Kim (2025) 的 \"diversity collapse\" 已描述类似现象。\n- Table 66 的 \"definitional difference\" 显得表面——底层机制（模型在格式/任务约束下输出收敛）相同。\n- 建议：承认与 capacity-confidence 已知关系的联系，明确本文贡献是量化了 NER 上的具体边界条件。\n\n**N3** [critical] **Related Work 覆盖存在显著缺口**\n- (a) Conformal prediction for NER：仅一句话提及 Fisch et al. (2021)，完全忽略 2025 年的进展（Conformal Structured Prediction ICLR 2025; arXiv 2601.16999）\n- (b) Token-level uncertainty for sequence labeling：He et al. (NAACL 2024 Findings) 未引\n- (c) Prompt-based NER 进展：GPT-NER (ACL 2025) 的 self-verification 与本文 ESJ probe 方法论相关\n- 建议：补充引用，讨论框架与 conformal prediction 方法的关系。\n\n## Should-Fix 问题\n\n**W1** Entity-level construction 仅 +1.40 pp（且条件限制强），在 NER 中实际意义有限。\n\n**W2** Abstract 信息密度过高（9 句话含 8+ 数字/符号），可读性差。\n\n**W3** Related Work 放在 Section 8（Experiments 后），读者无法即时评估增量贡献。建议在 Introduction 末尾增加 positioning 段落。\n\n**W4** Discussion/Conclusion 过于单薄（3 段约 15 行），缺少框架对其他结构化预测任务的适用性讨论、GPT-5.5 行为差异讨论等。\n\n**W5** 术语不完全一致：degeneracy / output convergence / convergence 交替使用。\n\n## 格式合规\n- Double-blind ✓, 正文 8 页 ✓, Limitations ✓, Ethics ✓, ACL 模板 ✓\n\n## 主要优势\n1. 研究问题定义精确且有实际意义\n2. 实验设计系统全面\n3. 诊断框架的两个维度分解清晰\n4. 统计分析严谨诚实\n5. Negative result 价值（符合 ARR H6 guideline）\n6. MBR 理论连接\n\n## Missing References\n1. Conformal Structured Prediction (ICLR 2025)\n2. Uncertainty Quantification for NER via Conformal Prediction (arXiv 2601.16999)\n3. He et al. (NAACL 2024 Findings) — token-level uncertainty transmission\n4. GPT-NER (ACL 2025 Findings) — self-verification for NER\n5. Calibrating Structured Output Predictors for NLP\n\n---\n\n请逐条 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "struct_self_consist_ie",
    "text": "## Step 2 交叉分享 — Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix (N1-N3)、Should-Fix (W1-W5) 和 Minor 问题，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n# Reviewer 2 — Round 1 审稿意见\n\n**Overall Assessment**: 3.0 / 5 (Findings)\n\n**一句话总结**: 实验扎实、框架清晰的 negative result 研究，但核心 insight 的增量新颖性不足以达到主会议水平——诊断框架本质上是对\"SC 在高 degeneracy 下失效\"这一可预期结论的系统化量化，而非根本性新发现。\n\n## Must-Fix 问题\n\n**N1** [critical] **核心新颖性声明与 Yao et al. (2026) 的区分不充分**\n- Yao et al. 已报告 NER/RE 上的 QE correlation（ρ up to 0.47），结论方向一致。\n- 本文的 instance-level 分析更细粒度，但核心 insight 并无质变——仍然是\"质量信号能预测但不能有效选择\"。\n- 建议：明确说明 instance-level 诊断揭示了哪些 task-level 分析无法发现的现象。\n\n**N2** [critical] **\"Capability-diversity tension\" 概念的原创性存疑**\n- \"模型能力越强，输出越收敛\" 是 well-known 现象。Yun & Kim (2025) 的 \"diversity collapse\" 已描述类似现象。\n- Table 66 的 \"definitional difference\" 显得表面——底层机制（模型在格式/任务约束下输出收敛）相同。\n- 建议：承认与 capacity-confidence 已知关系的联系，明确本文贡献是量化了 NER 上的具体边界条件。\n\n**N3** [critical] **Related Work 覆盖存在显著缺口**\n- (a) Conformal prediction for NER：仅一句话提及 Fisch et al. (2021)，完全忽略 2025 年的进展（Conformal Structured Prediction ICLR 2025; arXiv 2601.16999）\n- (b) Token-level uncertainty for sequence labeling：He et al. (NAACL 2024 Findings) 未引\n- (c) Prompt-based NER 进展：GPT-NER (ACL 2025) 的 self-verification 与本文 ESJ probe 方法论相关\n- 建议：补充引用，讨论框架与 conformal prediction 方法的关系。\n\n## Should-Fix 问题\n\n**W1** Entity-level construction 仅 +1.40 pp（且条件限制强），在 NER 中实际意义有限。\n\n**W2** Abstract 信息密度过高（9 句话含 8+ 数字/符号），可读性差。\n\n**W3** Related Work 放在 Section 8（Experiments 后），读者无法即时评估增量贡献。建议在 Introduction 末尾增加 positioning 段落。\n\n**W4** Discussion/Conclusion 过于单薄（3 段约 15 行），缺少框架对其他结构化预测任务的适用性讨论、GPT-5.5 行为差异讨论等。\n\n**W5** 术语不完全一致：degeneracy / output convergence / convergence 交替使用。\n\n## 格式合规\n- Double-blind ✓, 正文 8 页 ✓, Limitations ✓, Ethics ✓, ACL 模板 ✓\n\n## 主要优势\n1. 研究问题定义精确且有实际意义\n2. 实验设计系统全面\n3. 诊断框架的两个维度分解清晰\n4. 统计分析严谨诚实\n5. Negative result 价值（符合 ARR H6 guideline）\n6. MBR 理论连接\n\n## Missing References\n1. Conformal Structured Prediction (ICLR 2025)\n2. Uncertainty Quantification for NER via Conformal Prediction (arXiv 2601.16999)\n3. He et al. (NAACL 2024 Findings) — token-level uncertainty transmission\n4. GPT-NER (ACL 2025 Findings) — self-verification for NER\n5. Calibrating Structured Output Predictors for NLP\n\n---\n\n请逐条 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 3965 · 2026-05-22T12:15:15.978863+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1563
}
```

</details>

---


### Assistant

_source line 3966 · 2026-05-22T12:15:19.483355+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 299

## Round 299

2 recorded events


### User

_source line 3967 · 2026-05-22T12:15:22.132248+00:00_

[Reviewer 2 审稿结果]:
Round 1 审稿完成。已向 Review Director 提交完整结构化审稿意见，评分 Overall 3.0 (Findings)，包含 3 个 Must-Fix、5 个 Should-Fix 和 5 条 missing references。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 3968 · 2026-05-22T12:15:27.532245+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 300

## Round 300

2 recorded events


### User

_source line 3969 · 2026-05-22T12:16:57.391020+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — 交叉回应 Reviewer 2

---

## Must-Fix 问题

**[REBUT] R2-N1: 核心新颖性声明与 Yao et al. (2026) 的区分不充分**

R2 认为 Yao et al. 已报告 NER/RE 上的 QE correlation（ρ up to 0.47），核心 insight 无质变。我不完全同意：

1. **分析粒度确实不同，且差异有实质意义。** Yao et al. 的 ρ=0.47 是 task-level（跨 dataset 的宏观相关），而本文的核心发现是 **instance-level** 的 correlation-selection gap——AUROC 高达 0.82（Table 3, §7.2）但 selection gain <1pp（Table 1, §7.1）。这个 gap 在 task-level 分析中是不可见的：task-level 只能说"相关性中等"，无法揭示"在 instance 层面信号能区分好坏但选不出更好的"这个更精细的 paradox。

2. **Decomposition 是本文的真正增量。** Yao et al. 没有提供 failure 的机制解释。本文将 gap 分解为 degeneracy + alignment collapse 两个可独立度量的因素（§4, §6.3），并通过 cross-model ensemble（§5.1, Table 2）和 entity-level construction（§7.5）展示了 partially bypassing 这些 bottleneck 的路径。这不是对"SC 在 NER 上差"的重复确认，而是对 **为什么差** 的系统诊断。

3. **但 R2 的关切有合理之处**：论文确实应该在 §1 Introduction 中更 explicitly 说明 "Yao et al. showed task-level correlation; we reveal that this correlation does not translate to instance-level selection gains, and diagnose why"。目前 Yao et al. 的引用主要出现在 §8 Related Work，在 Introduction 中缺乏直接对比。

**结论**：新颖性存在但论文的 positioning 可以更 explicit。建议在 §1 增加 1-2 句与 Yao et al. 的直接对比，不需要降级为 N1-level critical issue。

---

**[AGREE] R2-N2: "Capability-diversity tension" 概念的原创性存疑**

R2 指出 "模型能力越强，输出越收敛" 是 well-known 现象，Yun & Kim (2025) 已描述 "diversity collapse"。我同意这个 concern：

1. 论文在 Appendix（Table 66 附近区域，§8 末尾）提供了与 Yun et al. 的对比表，区分了 measurement 方式（instance degeneracy via exact match vs. output diversity via n-gram），但 R2 正确指出这是 **"definitional difference"** 而非 **mechanistic distinction**。底层现象相同：强模型在高约束任务上收敛到相似输出。

2. 然而，我认为论文的贡献不在于发现 capability-diversity tension 本身，而在于 **量化了这个 tension 在 NER 上的具体边界**——degeneracy 12-68% across datasets（Table 13, Appendix g），以及它如何具体阻断 selection gain（§6.3 的 degeneracy bound）。论文应该更诚实地承认概念层面并非原创，同时强调量化贡献。

3. 建议与 R2 一致：承认 capability-diversity tension 是 known phenomenon，明确本文贡献是为 NER 提供了精确的量化刻画和 diagnostic 工具，而非声称发现了新现象。

---

**[REBUT] R2-N3: Related Work 覆盖存在显著缺口**

R2 列举了 5 篇 missing references。我逐条评估：

1. **(a) Conformal Structured Prediction (ICLR 2025) / arXiv 2601.16999**：我在自己的 review 中也指出了 conformal prediction 的覆盖不足（R1 Missing References），所以 **部分同意** conformal prediction 方向需要补充。但需要注意：本文的 entity-level construction 本质上是 MBR decoding（§6.1, Proposition 1），与 conformal prediction 的 coverage guarantee 目标不同。补充引用是合理的，但不需要深度方法论对比。

2. **(b) He et al. (NAACL 2024 Findings) — token-level uncertainty**：如果存在，与本文的 per-entity signal 设计相关，值得引用。但这不是"显著缺口"——本文关注的是 instance-level selection 的 failure mechanism，不是 token-level uncertainty 的 propagation。

3. **(c) GPT-NER (ACL 2025) — self-verification**：本文的 ESJ（Entity Self-Judgment）probe（Table 18, Appendix h）确实与 self-verification 方法论相关。如果 GPT-NER 提出了类似的 self-verification 机制用于 NER，应该引用并讨论方法差异。

4. **总体判断**：Related work 的覆盖确实可以更全面，但我不同意这是 **"显著缺口"** 级别的问题。论文的 Related Work（§8）已经覆盖了 test-time scaling、self-consistency、MBR decoding、structured prediction sampling 等核心方向。缺少的主要是 2024-2025 年的 conformal prediction 和 self-verification 的最新进展——这属于 **W-level（Should-Fix）补充**，不应构成 N-level critical issue。R2 将此列为 N3 (critical) 我认为过重了。

---

## Should-Fix 问题

**[REBUT] R2-W1: Entity-level construction 仅 +1.40 pp，实际意义有限**

R2 低估了这个结果的意义：

1. +1.40 pp 来自 Few-NERD（§7.5），但论文报告的 entity-level construction 在 **有 headroom 的条件子集** 上有更大的 gain——Table 2 最后一行 entity-level LP-weighted construction 在 Few-NERD 上达到 +1.30 pp（相对于 greedy baseline），而 CoNLL 上是 +0.4 pp。关键在于论文明确指出这个 gain 是 **conditional**（$\theta_{\text{crit}}=0.70$ 以下），并非声称 universal improvement。

2. 这个结果的价值不在于绝对增益大小，而在于 **proof of concept**：它证明了绕过 instance-level bottleneck（通过转向 entity-level construction）是可行的技术路径。在一篇以 negative result 为主的论文中，提供 constructive 的正面方向是重要的贡献。

3. 但我承认 +1.40 pp 在 NER 实际应用中确实不大，论文不应过度宣传这个结果。

---

**[AGREE] R2-W2: Abstract 信息密度过高**

同意。Abstract 的 9 句话中包含 AUROC 0.82、<1pp、degeneracy 12-68%、α→0、$\theta_{\text{crit}}=0.70$ 等大量数字。对于一篇 negative result 论文，abstract 应该优先传达 insight 的直觉，数字可以精简到 2-3 个最关键的（如 AUROC vs selection gain 的 gap，以及 degeneracy range）。

---

**[REBUT] R2-W3: Related Work 放在 Section 8，读者无法即时评估增量贡献**

不同意这是一个问题：

1. Related Work 放在 Experiments 后是 *ACL 论文的 **常见且被接受的格式**。EMNLP/ACL 近年的 best paper（如 ACL 2024 best paper）多采用这种结构。ARR review form 没有对 Related Work 位置的硬性要求。

2. R2 建议在 Introduction 末尾增加 positioning 段落——这我 **部分同意**。论文 §1 的最后部分（"Our analysis is observational..."）确实可以增加 1-2 句 positioning，说明与 Yao et al. 和 Yun et al. 的区分（呼应 R2-N1/N2）。但移动整个 Related Work section 不必要。

---

**[AGREE] R2-W4: Discussion/Conclusion 过于单薄**

同意。§9 Discussion 仅 3 段，对于一篇以 diagnostic framework 为核心贡献的论文来说确实不够。具体缺失：
- 框架对其他 structured prediction 任务（如 parsing、code generation）的适用性预测
- GPT-5.5 / 72B 的行为差异意味着什么——是 scale 能解决 degeneracy 吗？
- 对 practitioner 的具体 actionable guidance（何时不值得投入 TTS compute）

这与我的 R1-N3（framework 缺乏预测力的定位问题）相关——更充分的 Discussion 可以部分缓解这个 concern。

---

**[AGREE] R2-W5: 术语不完全一致**

同意。我在通读中也注意到 degeneracy / output convergence / convergence 在不同 section 交替出现。§2.1 定义了 "degeneracy rate D"，但 §5、§6 在 prose 中切换为 "output convergence"。对 diagnostic framework 论文来说，术语一致性尤为重要。建议在 §2 首次定义后统一使用 "degeneracy (D)" 并在 parenthetical 中注明 "also referred to as output convergence"。

---

## R2 Overall Assessment 的评价

R2 给 3.0 (Findings)，理由是"增量新颖性不足以达到主会议水平"。我认为这个评分 **略低**：

1. R2 的核心论点是 "诊断框架本质上是对可预期结论的系统化量化"。但 "可预期" 是 hindsight bias——在本文之前，没有人系统量化过 TTS 在 NER 上的 failure mode，也没有人提出 correlation-selection gap 的 decomposition。

2. R2 认为与 Yao et al. 和 Yun et al. 的增量不足。但如我在 R2-N1 rebut 中指出，instance-level 分析和 mechanistic decomposition 是本文的真正增量，Yao et al. 只有 task-level correlation。

3. 然而，我自己给 3.5 (Borderline Conference) 也不是无条件的——N1（Holm-Bonferroni correction）和 N3（framework 预测力）是我的核心 concerns。如果这两个问题在 revision 中被 adequately addressed（transparent reporting + honest framing），论文可以达到 Conference 水平。

**我维持 3.5 (Borderline Conference) 的评分**，但理解 R2 给 3.0 的 reasoning。最终差异可能取决于 AC 对 "systematic negative result with diagnostic framework" 这类贡献的 venue fit 判断。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 3970 · 2026-05-22T12:17:02.435674+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 301

## Round 301

2 recorded events


### User

_source line 3971 · 2026-05-22T12:17:07.880676+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **N1 (Yao et al. novelty)**: REBUT — instance-level decomposition 是真正增量，但建议在 Introduction 中更 explicit 地对比
- **N2 (capability-diversity originality)**: AGREE — 概念层面非原创，应承认并强调量化贡献
- **N3 (Related Work gaps)**: REBUT — 缺口存在但 R2 列为 critical 过重，应降为 Should-Fix
- **W1 (entity construction +1.40pp)**: REBUT — 价值在于 proof of concept，非绝对增益
- **W2 (Abstract 密度)**: AGREE
- **W3 (Related Work 位置)**: REBUT — *ACL 常见格式，但同意 §1 加 positioning
- **W4 (Discussion 单薄)**: AGREE — 缺少 generalizability 和 practitioner guidance 讨论
- **W5 (术语不一致)**: AGREE

维持 3.5 (Borderline Conference) 评分，与 R2 的 3.0 差异主要在于对 instance-level diagnostic 增量价值的判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 3972 · 2026-05-22T12:17:13.182602+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 302

## Round 302

14 recorded events


### User

_source line 3973 · 2026-05-22T12:17:22.507482+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 交叉回应 Reviewer 1 审稿意见

---

### Must-Fix 问题

**[AGREE] R1-N1: Holm-Bonferroni correction 的 family 划分存在 cherry-picking 风险**

同意这是一个实质性方法论问题。论文在 Limitations 中坦承全局 HB 下 p_HB=0.055（k=57），但正文中引用的显著性结论（如 Section 5.2 "LP-best selection yields +0.28 pp, p_adj=0.006"）依赖 per-family correction（k=10）。从全局 k=57 切换到 per-family k=10 是一个 post-hoc 决策，使得 correction 力度降低约 5.7 倍。如果 family 划分是 pre-specified 的，需要在方法部分明确声明；如果不是，应默认报告全局校正结果。

补充我的发现：Table 12（Appendix f）的 57 项检验中，BH FDR 下仅 19/57 显著（包括 6/10 construction comparisons），进一步表明论文的统计证据在保守校正下处于边界。正文需要更透明地呈现这一事实，而非将最保守结果藏在 Limitations 的一句话中。

---

**[AGREE] R1-N2: "Simultaneously necessary conditions" 的 claim 超出证据**

同意。我在审阅 Section 6.2（Degeneracy Decomposition）时也注意到 decomposition bound $(1-D) \cdot G_{\text{nd}} \cdot \alpha$ 仅解释 3-12% 的实际增益变异。如果一个分解框架只能 capture 不到 12% 的目标变量，其组成部分称为 "necessary conditions" 在逻辑上不成立——"necessary" 意味着去掉任一条件增益就消失，但数据并未支撑这种强因果结论。

R1 的建议 "two co-occurring factors that characterize the gap" 更准确。论文自身在 Limitations 中已承认 "diagnostic, not causal"（Limitations 第2句），但正文多处的表述未能贯彻这一自限（如 Section 6.2 标题 "Degeneracy Decomposition" 暗示了 decomposition 的完整性）。

---

**[REBUT] R1-N3: Diagnostic framework 无预测力——部分同意但严重性被高估**

部分同意 R1 的表面观察，但不同意将此列为 Must-Fix 级别。理由：

1. **Post-hoc diagnostic ≠ 无价值**：医学诊断中，病理分析也是 post-hoc 的（先观察症状再定位原因），但仍有指导价值。论文的 practical implication（Section 9 第2段）——"measure degeneracy and LP-F1 alignment with N=8 samples before investing in N× inference; when degeneracy exceeds θ_crit=0.70, aggregation is unlikely to help"——是一个可操作的 deployment guideline，不依赖 R²>0。

2. **R²<0 的语境**：R²<0 出现在 Limitations 中，指的是 decomposition 各 stage 无法独立分解为加性效应（"stages resist decomposition into independent effects"），而非整个框架无预测力。θ_crit=0.70 的阈值在 Table 22（Appendix e）中展示了 cross-configuration 的稳定性——0.60 阈值下 >60.9% 的 non-trivial instances 信号仍显著，0.40 阈值下 LP gain 为 +0.28 pp（p=0.004）。虽然不是严格的 held-out validation，但 cross-dataset 一致性（SciERC、CoNLL、Few-NERD、WNUT-17 上阈值表现一致）提供了 partial evidence。

3. **标题措辞**：同意 "Boundary Conditions" 可能暗示了过强的预测性。但 "boundary conditions" 在物理/工程中也常用于描述系统行为变化的条件阈值，不一定暗示预测模型。建议改为 "Failure Conditions" 或在 abstract 中更明确地说明框架的 diagnostic（而非 predictive）定位即可。

**总结**：R1 对标题和 R² 的关切有道理，但将此升级为 Must-Fix 过重。建议降为 Should-Fix：修改标题措辞 + 在 Introduction 中明确 diagnostic scope + 提供 leave-one-dataset-out 结果（如果数据允许）。

---

### Should-Fix 问题

**[AGREE] R1-W1: Hidden-state probe 模型不一致**

这是一个值得注意的实验设计问题。如果 hidden-state probe 使用 Qwen2.5-7B 而主实验用 Qwen3-8B，则 probe 结论（如 internal representation 中信号的存在性）不能直接推广到主模型。应至少讨论两个模型架构的差异对 probe 结论的潜在影响，或在 Qwen3-8B 上重复 probe 实验。

---

**[AGREE] R1-W2: 模型多样性不足**

同意。我在自己的审稿中也指出了这一问题（Excitement 评分理由）。两个 8B 级开源模型（Qwen3-8B, LLaMA-3.1-8B）是主要结果的基础。虽然论文包含了 Qwen3-4B/14B 的 scale ablation（Section 6.2, Appendix x）和 GPT-5.5 的 frontier comparison（Table 44, Appendix），但这些都是补充性的。generalization claim 应限定在 "7-14B fine-tuned open-weight models" 范围内——论文在部分地方做了这一限定（如 Discussion 第2段），但 Abstract 和 Introduction 的措辞更宽泛。

---

**[AGREE] R1-W3: RE/SQL 证据过薄但 abstract 呈现过强**

同意。我在 Should-Fix W1（entity-level construction 实际意义）中讨论了类似问题。Abstract 第3句 "relation extraction as an exploratory extension" 的 hedging 适当，但第5句 "Cross-task validation on RE reveals a distinct bottleneck" 用了 "validation" 一词，对 n=397 单数据集的结果偏强。建议改为 "Cross-task exploration on RE suggests..."。

---

**[AGREE] R1-W4: Few-NERD 3 epoch confound**

同意这需要更强的讨论。论文在 Section 8（page 8 顶部）讨论了 Few-NERD 的 3 epoch 设置导致更低的 degeneracy（13% vs 31% at 5-epoch），并将其视为框架的支持证据（favorable conditions → SC works better）。但 R1 的隐含关切是正确的：如果 Few-NERD 的 "positive" 结果主要来自 undertrained model 而非 intrinsic task property，那么框架观察到的不是 NER 的 boundary condition，而是 training regime 的 artifact。

论文应明确讨论：如果将 Few-NERD 训练到 5 epoch 使 degeneracy 从 13% 升至 31%，SC 增益是否相应消失？如果是，这支持框架（degeneracy → SC failure）；如果否，则框架遗漏了重要变量。目前论文只展示了 3 vs 5 epoch 的 degeneracy 差异，未展示对应的 SC selection gain 变化。

---

**[AGREE] R1-W5: θ_crit=0.70 稳定性未系统验证**

同意。Table 22（Appendix e）提供了不同阈值下的 sensitivity 分析，显示 LP selection gain 在 θ=0.40-0.60 范围内保持正向。但这是 within-dataset 的 sensitivity，不是 cross-dataset 或 cross-model 的 stability。θ_crit=0.70 是否在不同模型族（Qwen vs LLaMA）或不同 entity type distribution 下稳定？论文未回答。

---

### Minor 问题

**[AGREE] R1-M1: Figure 1 因果箭头**

Figure 1 的 pipeline 流（Discover → Diagnose → Explore）可能暗示因果链条，但框架只建立了 correlational/diagnostic 关系。建议改用 "diagnostic flow" 而非箭头暗示的因果方向。

---

**[AGREE] R1-M2: §2.1 前向引用**

前向引用确实中断阅读。这是论文将 Related Work 放在 Section 8 的连锁效应之一——方法部分不得不 forward-reference 尚未定义的概念。

---

**[AGREE] R1-M3: Proposition 1 独立性假设被数据部分违反**

这是一个重要的理论-实证脱节。Proposition 1 假设 entity-wise independence，但 split-half correlation r≈0.58-0.64 表明 entities 在同一 instance 内有中等相关性。这不一定使 Proposition 1 无效（它可能仍是一个 useful approximation），但应在主文中注明这一限制，而非仅在 appendix 中隐含。

---

**[AGREE] R1-M4: Table 3 AUROC binarization threshold 缺 sensitivity 分析**

AUROC 的计算依赖于 binarization threshold（what counts as "good" output），不同阈值可能改变 signal ranking。这是一个标准的 robustness check，应该提供。

---

**[AGREE] R1-M5: Yun et al. (2025) 对比不够具体**

强烈同意。这也是我 Must-Fix N2 的核心关切之一。Table 66（Appendix ag）的 definitional difference 过于表面——两者的底层机制（模型在约束下输出收敛）高度相似，仅在 measurement level（response-level vs entity-set）上有区别。论文需要更深入地论证为什么 entity-set convergence 构成一个独立于 response-level diversity collapse 的概念。

---

### 对 R1 Questions 的补充意见

**Q1（HB family 划分是否 pre-specified）**: 关键问题。如果不是 pre-specified，per-family correction 的结论需要加 caveat。

**Q2（post-hoc diagnosis 的价值）**: 如我在 R1-N3 rebut 中所述，diagnostic 价值存在但需要诚实定位。

**Q3（entity-group level decomposition）**: 有趣方向。Per-type LP analysis（Table 51-53, Appendix z）显示不同 entity type 的 degeneracy 和 LP 行为差异显著（如 CoNLL LOC vs MISC），entity-group decomposition 可能 tighten the bound。

**Q4（Qwen 变体 ensemble）**: 好问题。两个 Qwen 变体（2.5 vs 3）如果 ensemble 能提升 diversity，这将直接测试 capability-diversity tension 的核心 claim。

**Q5（WNUT-17 zero-F1 instances）**: 论文在 Appendix a（Training Configuration, prompt template）中讨论了 WNUT-17 的 low performance，但对 zero-F1 instances 的成因分析确实不足。

---

### 与 R1 总体评分的对比

R1 给出 3.5（Borderline Conference），我给出 3.0（Findings）。差异主要在于：

1. **新颖性权重**：我更强调核心 insight 的增量新颖性不足（我的 N1, N2），R1 更看重实验规模和严谨性。
2. **统计问题的严重性**：R1 和我都识别了 HB correction 问题，但 R1 同时更关注 R²<0 的框架定位问题。
3. **共识点**：我们对 Related Work 覆盖不足、RE/SQL 证据薄弱、术语不一致等问题有高度一致。

我维持 3.0（Findings）的评分。论文的实验工作量和诚实性值得肯定（也是 R1 的 strengths 1-3），但在新颖性维度上不足以达到 Borderline Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 3974 · 2026-05-22T12:17:49.883843+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool call

_source line 3975 · 2026-05-22T12:17:49.884235+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 3976 · 2026-05-22T12:17:51.239083+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T12:04:16.896554+00:00\", \"completed_at\": \"2026-05-22T12:08:39.836531+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1-2\", \"message\": \"前两页为纯文本（Title/Abstract/Introduction），首个视觉锚点 Figure 1 出现在第 3 页顶部。ACL 论文中常见，但审稿人需读完 2 页密集文字才看到第一个 display item。Figure 1 本身传达核心 message（correlation-selection gap 的三阶段诊断框架），锚定效果良好。\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Title/Author/Abstract 排版整洁，符合 ACL 匿名投稿格式，无拥挤感。Abstract 信息密度高，含关键数字（AUROC 0.82, +1.4pp 等），专业。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8-9\", \"message\": \"主正文末尾连续 2 页纯文本：第 8 页为 Related Work + Discussion and Conclusion，第 9 页为 Limitations + Ethics Statement + References 开头。主正文在 Section 7（Experimental Setup）之后无 display item 收尾，审稿人最后印象是大段文字。考虑在 Discussion 中加一个总结性 figure 或 compact table 回顾核心发现。\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 为三面板概览图（Quality Estimation / Sample Selection / Entity-Level Construction），颜色方案用绿/蓝/橙，区分度好，caption 自包含。作为第一个 display item，有效传达论文核心 idea。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 2 为单栏柱状图，字号偏小但在 150dpi 下仍可读。柱状图使用灰/绿填充 + 虚线标记，色盲友好。Table 1 使用 booktabs 风格，最优值加粗，格式规范。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 2（9 种方法分类汇总）信息密集且有效，使用缩写名（MRSC, DALS 等），表内有脚注解释，格式合理。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 3（MV ΔF1 vs log₂ N）清晰，三条线用不同颜色 + marker 区分，灰度打印时仍可通过 marker shape 辨别。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"单页包含 Table 3 + Table 4 + Figure 4，密度高但不拥挤，布局合理。Figure 4 为单栏小图，轴标签字号接近可读下限（约正文 70%），建议略微增大。\"}, {\"severity\": \"info\", \"dimension\": \"page 14\", \"message\": \"Figure 6（Reliability diagrams）使用 figure* 跨双栏，全宽展示两组 calibration 热图，颜色方案合理（蓝/橙），分辨率充足。\"}, {\"severity\": \"info\", \"dimension\": \"page 15\", \"message\": \"Figure 7（Quality estimation heatmap
…[truncated 1664 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 1355
}
```

</details>

---


### Tool result

_source line 3977 · 2026-05-22T12:17:51.239483+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1355
}
```

</details>

---


### Tool call

_source line 3978 · 2026-05-22T12:17:51.340027+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 3979 · 2026-05-22T12:17:51.441596+00:00_

1	issues:
2	# ===== CRITICAL / MUST-FIX =====
3	- id: R36-MF1
4	  summary: "标题 'Information Extraction' 仍 overclaim，必须改为 NER"
5	  category: framing
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 33
9	  last_seen_round: 36
10	  mentions:
11	    - round: 35
12	      reviewers: [1, 2]
13	      note: "从 Structured Prediction 改为 IE，仍被指出 overclaim"
14	    - round: 36
15	      reviewers: [1, 2]
16	      note: "双方 CRITICAL。RE 仅 n=397 单 seed 单数据集，不足以支撑 IE scope"
17	  action_items:
18	    - round: 36
19	      action: "标题改为 'Boundary Conditions for Named Entity Recognition'，全文收窄"
20	      assigned_to: paper_agent
21	      status: done
22	  resolution: "标题已改为 'Boundary Conditions for Named Entity Recognition'，全文 scope 收窄至 NER"
23	  resolution_round: 37
24	
25	- id: R36-MF2
26	  summary: "全局 Holm-Bonferroni p_adj=0.055 需在 §7 正文讨论"
27	  category: method
28	  severity: critical
29	  status: resolved
30	  first_raised_round: 34
31	  last_seen_round: 36
32	  mentions:
33	    - round: 34
34	      reviewers: [1, 2]
35	      note: "首次提出。论文在 Limitations 中讨论但不够显眼。"
36	    - round: 36
37	      reviewers: [1, 2]
38	      note: "需要在 §7 正文 construction 段明确讨论 + prescriptive 标为 exploratory"
39	  action_items:
40	    - round: 36
41	      action: "§7 construction 段增加全局校正讨论 + exploratory 标记"
42	      assigned_to: paper_agent
43	      status: done
44	  resolution: "§7 正文 line 104-105 明确讨论 p_adj=0.055 + BH FDR 6/10 + per-family justification"
45	  resolution_round: 37
46	
47	- id: R36-MF3
48	  summary: "SciERC single seed power 限制需正文讨论"
49	  category: experiment
50	  severity: critical
51	  status: in_progress
52	  first_raised_round: 35
53	  last_seen_round: 36
54	  mentions:
55	    - round: 35
56	      reviewers: [1, 2]
57	      note: "建议补 seeds 或标 tentative"
58	    - round: 36
59	      reviewers: [1, 2]
60	      note: "MDE≈1.5pp vs observed +0.2pp。需正文 power discussion。"
61	  action_items:
62	    - round: 36
63	      action: "§4/§7 增加 power limitation 讨论 + SciERC extra seeds 
…[truncated 1110 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 3980 · 2026-05-22T12:17:57.213241+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "100",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "offset": "100",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 3981 · 2026-05-22T12:17:57.316487+00:00_

100	  action_items:
101	    - round: 36
102	      action: "全文 'diagnostic cascade' → 'diagnostic framework'（~10 处）"
103	      assigned_to: paper_agent
104	      status: done
105	  resolution: "全文 cascade→framework，grep 确认 0 残留"
106	  resolution_round: 37
107	
108	- id: R36-SF3
109	  summary: "Novelty 定位不够精确——correlation-selection gap 非全新"
110	  category: framing
111	  severity: warning
112	  status: resolved
113	  first_raised_round: 35
114	  last_seen_round: 36
115	  mentions:
116	    - round: 36
117	      reviewers: [1, 2]
118	      note: "降级为 Should-Fix。需 §1 明确区分已知现象 vs 本文诊断框架贡献。"
119	  action_items:
120	    - round: 36
121	      action: "§1 增加 1 句区分已知现象和本文系统化诊断贡献"
122	      assigned_to: paper_agent
123	      status: done
124	  resolution: "§1 line 4: 'no systematic diagnostic framework quantifying failure mechanisms at entity level across multiple model families'"
125	  resolution_round: 37
126	
127	- id: R36-SF4
128	  summary: "Related Work 缺 conformal prediction、token-level uncertainty、structured MBR"
129	  category: writing
130	  severity: warning
131	  status: resolved
132	  first_raised_round: 33
133	  last_seen_round: 36
134	  mentions:
135	    - round: 36
136	      reviewers: [1, 2]
137	      note: "Fisch et al. 2021, Angelopoulos & Bates 2023 需引用。"
138	  action_items:
139	    - round: 36
140	      action: "§8 补充 bib 条目 + \\cite"
141	      assigned_to: paper_agent
142	      status: done
143	  resolution: "background.tex line 23: conformal prediction paragraph with fisch2021conformal + angelopoulos2023conformal"
144	  resolution_round: 37
145	
146	- id: R36-SF5
147	  summary: "CDT 'structural constraint' 仍太强"
148	  category: framing
149	  severity: warning
150	  status: resolved
151	  first_raised_round: 35
152	  last_seen_round: 36
153	  mentions:
154	    - round: 36
155	      reviewers: [1, 2]
156	      note: "4B-14B 有限，GPT-5.5 仅 200 实例。弱化为 observed tendency。"
157	  action_items:
158	    - round: 36
159	      action: "'structural constraint' → 'observed 
…[truncated 2804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 3982 · 2026-05-22T12:19:42.561446+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n# ===== ROUND 37 CRITICAL / MUST-FIX =====\n- id: R37-MF1\n  summary: \"Holm-Bonferroni correction per-family 划分缺乏 pre-registration，核心 LP claim 在全局校正下不显著\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 34\n  last_seen_round: 37\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"R36-MF2: 需在 §7 正文讨论。标记 resolved round 37。\"\n    - round: 37\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均列为 CRITICAL [AGREE]。§7 已讨论 p_adj=0.055 但 per-family justification 仍不充分——缺乏 pre-registration 证据，k=57→k=10 的切换构成 post-hoc adjustment。正文引用 p_adj=0.006 而全局 0.055 仅在 Appendix/Limitations。\"\n  action_items:\n    - round: 37\n      action: \"正文 §7 透明报告两种 correction 结果；提供 a priori family 划分理由或承认 post-hoc；将 LP selection 描述为 'marginally significant under global correction'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R37-MF2\n  summary: \"'Simultaneously necessary conditions' 的 claim 超出 correlational co-occurrence 证据\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 37\n  last_seen_round: 37\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均 AGREE。Bound (1-D)·G_nd·α 只 capture 3-12% actual gains。'necessary' 要求移除条件后 gains 总是恢复，但 cross-model ensemble 只 partially bypasses。证据支撑 co-occurrence 而非 logical necessity。\"\n  action_items:\n    - round: 37\n      action: \"'simultaneously necessary conditions' → 'two co-occurring factors that characterize the gap'；讨论 bound looseness 对 necessity claim 的影响\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R37-MF3\n  summary: \"Diagnostic framework 无预测力（R²<0）与 title/abstract 暗示预测性的张力\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 37\n  last_seen_round: 37\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"R1 列为 Must-Fix，R2 认为应降为 Should-Fix 但承认关切有道理。Title 'Boundary Conditions' 暗示可预测性；θ_crit=0.70 缺乏 held-out cross-dataset validation。分歧在严重性定级而非事实。\"\n  action_items:\n    - round: 37\n      action: \"§1/§9 明确 diagnostic vs predictive scope；Title 考虑改为 'Failure Conditions'；提供 leave-one-dataset-out θ_crit validation\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R37-MF4\n  summary: \"与 Yao et al. (2026) 的增量新颖性区分不充分\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 35\n  last_seen_round: 37\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"R36-SF3: 降级为 Should-Fix，§1 增加 1 句区分。\"\n    - round: 37\n      reviewers: [1, 2]\n      note: \"R2 升级回 CRITICAL：instance-level 分析更细粒度但核心 insight 无质变。R1 REBUT：decomposition 是实质增量，但同意 §1 positioning 不足。分歧未完全收敛。\"\n  action_items:\n    - round: 37\n      action: \"§1 增加 1-2 句明确说明 instance-level 诊断揭示了哪些 task-level 分析无法发现的现象（如 degeneracy 分布双峰性、per-instance LP compression）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R37-MF5\n  summary: \"Related Work 缺 2025 conformal prediction for NER、token-level uncertainty、GPT-NER self-verification\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 37\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"R36-SF4: 补充了 Fisch 2021 + Angelopoulos 2023。标记 resolved。\"\n    - round: 37\n      reviewers: [1, 2]\n      note: \"R2 列为 CRITICAL，R1 认为 Should-Fix 更合适。新缺口：Conformal Structured Prediction (ICLR 2025)、arXiv 2601.16999 (NER conformal)、He et al. (NAACL 2024)、GPT-NER (ACL 2025)。收敛定为 Should-Fix。\"\n  action_items:\n    - round: 37\n      action: \"§8 补充 4-5 篇 2024-2025 引用；讨论 conformal prediction 与本文 diagnostic framework 的互补关系\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== ROUND 37 SHOULD-FIX =====\n- id: R37-SF1\n  summary: \"'Capability-diversity tension' 概念层面非原创，与 Yun & Kim (2025) diversity collapse 区分表面\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 35\n  last_seen_round: 37\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"R36-SF5: 弱化为 observed tendency。标记 resolved。\"\n    - round: 37\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均 AGREE 概念非原创。Table 66 的 definitional difference 过于表面。需承认已知现象+强调量化贡献。\"\n  action_items:\n    - round: 37\n      action: \"承认 capability-diversity tension 是 known phenomenon；明确贡献是 NER 上的量化刻画而非新概念\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R37-SF2\n  summary: \"Hidden-state probe 使用 Qwen2.5-7B 而非主模型 Qwen3-8B\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 37\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"R36-SF6: 增加 footnote 说明。标记 resolved。\"\n    - round: 37\n      reviewers: [1, 2]\n      note: \"Footnote 不够——probe 结论不能直接迁移到 Qwen3-8B。建议 Qwen3-8B 上重复 probe 或限定结论范围。\"\n  action_items:\n    - round: 37\n      action: \"在 Qwen3-8B 上训练 probe（去掉 thinking tokens）或明确限定为 Qwen2.5 family\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R37-SF3\n  summary: \"模型多样性不足，generalization claim 过强（主要 8B 级别开源模型）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 37\n  last_seen_round: 37\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"两位 Reviewer AGREE。72B/GPT-5.5 仅 tentative，capability-diversity tension 几乎全基于 8B 推断。\"\n  action_items:\n    - round: 37\n      action: \"generalization claim 限定为 '7-14B fine-tuned open-weight models'；讨论 scale/proprietary 的 limited evidence\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R37-SF4\n  summary: \"RE (n=397 单数据集) 和 SQL pilot (n=196) 证据过薄但 abstract 呈现偏强\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 37\n  last_seen_round: 37\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"AGREE。Abstract 'Cross-task validation on RE' 用词偏强，n=397 power 不足。建议 'validation' → 'exploration'。\"\n  action_items:\n    - round: 37\n      action: \"Abstract 弱化 RE/SQL 呈现；为 RE 提供 power analysis；'validation' → 'exploration'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R37-SF5\n  summary: \"Few-NERD 3 epoch vs 5 epoch confound 讨论不充分\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 37\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"R36-SF2: 5-epoch LP Δ=+0.12±0.04pp collapse 数据已有。in_progress。\"\n    - round: 37\n      reviewers: [1, 2]\n      note: \"AGREE。5-epoch degeneracy 13%→31% 数据存在但 SC selection gain 变化未展示。'Feature not bug' 论证不完全令人信服。\"\n  action_items:\n    - round: 37\n      action: \"主文简要承认 confound + 展示 3 vs 5 epoch 的 SC gain 变化数据；引用 Appendix ablation\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R37-SF6\n  summary: \"θ_crit=0.70 稳定性未经 cross-dataset/cross-model 系统验证\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 37\n  mentions:\n    - round: 35\n      reviewers: [1]\n      note: \"R1-N1: θ sweep 完成。标记 resolved。\"\n    - round: 37\n      reviewers: [1, 2]\n      note: \"AGREE。Appendix Table 22 的 ε sensitivity 仅 SciERC。不同 degeneracy regime 下同一阈值合理性未论证。\"\n  action_items:\n    - round: 37\n      action: \"提供 θ_crit 在所有 dataset × model 上的 calibration 结果或讨论为什么单一阈值有效\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R37-SF7\n  summary: \"Abstract 信息密度过高（9 句含 8+ 数字），可读性差\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 37\n  last_seen_round: 37\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"AGREE。典型 EMNLP best paper abstract 仅 2-3 个关键数字。\"\n  action_items:\n    - round: 37\n      action: \"精简 abstract 数字至 2-3 个（保留 AUROC 0.82 和 <1pp），其余移入 §1\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R37-SF8\n  summary: \"Discussion/Conclusion 过于单薄（3 段约 15 行），缺少 generalizability 讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 37\n  last_seen_round: 37\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"AGREE。缺少：框架对其他 structured prediction 的适用性、GPT-5.5 行为差异、practitioner actionable guidance。\"\n  action_items:\n    - round: 37\n      action: \"扩展 §9 至 5-6 段，讨论 open questions 和 practical guidelines\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R37-SF9\n  summary: \"术语不一致：degeneracy / output convergence / convergence 交替使用\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 37\n  last_seen_round: 37\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"AGREE。§2 定义 degeneracy rate D 后，§5/§6 切换为 output convergence。建议统一。\"\n  action_items:\n    - round: 37\n      action: \"§2 首次定义后统一使用 'degeneracy (D)'，parenthetical 注明 'also referred to as output convergence'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== EARLIER ISSUES — STATUS CARRIED FORWARD =====\n- id: R36-MF1\n  summary: \"标题 'Information Extraction' 仍 overclaim，必须改为 NER\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 33\n  last_seen_round: 37\n  mentions:\n    - round: 35\n      reviewers: [1, 2]\n      note: \"从 Structured Prediction 改为 IE，仍被指出 overclaim\"\n    - round: 36\n      reviewers: [1, 2]\n      note: \"双方 CRITICAL。RE 仅 n=397 单 seed 单数据集\"\n    - round: 37\n      reviewers: [1, 2]\n      note: \"本轮未提及，标题已为 NER。确认 resolved。\"\n  action_items:\n    - round: 36\n      action: \"标题改为 'Boundary Conditions for Named Entity Recognition'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"标题已改为 'Boundary Conditions for Named Entity Recognition'\"\n  resolution_round: 37\n\n- id: R36-MF3\n  summary: \"SciERC single seed power 限制需正文讨论\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 35\n  last_seen_round: 37\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"MDE≈1.5pp vs observed +0.2pp。需正文 power discussion。\"\n    - round: 37\n      reviewers: [1, 2]\n      note: \"本轮未单独提及，但 R1-N1 隐含涉及（SciERC n=529 是否足够）。维持 in_progress。\"\n  action_items:\n    - round: 36\n      action: \"§4/§7 增加 power limitation 讨论\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R36-SF1\n  summary: \"'Diagnostic cascade' 术语误导因果解读\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 36\n  last_seen_round: 37\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"本轮未提及 cascade 术语。确认 resolved。\"\n  action_items:\n    - round: 36\n      action: \"全文 cascade → framework\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"全文 cascade→framework，grep 确认 0 残留\"\n  resolution_round: 37\n\n- id: R36-SF6\n  summary: \"§3 自验证实验使用 Qwen2.5-7B 而非主模型 Qwen3-8B\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 37\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"增加 footnote。标记 resolved。\"\n    - round: 37\n      reviewers: [1, 2]\n      note: \"复发。Footnote 不够，需 Qwen3-8B probe 或限定结论。升级跟踪为 R37-SF2。\"\n  action_items:\n    - round: 37\n      action: \"见 R37-SF2\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R36-SF8\n  summary: \"Responsible NLP Checklist 不应在 PDF 中\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 36\n  last_seen_round: 37\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"本轮未提及。确认 resolved。\"\n  resolution: \"main.tex 中 checklist 已移除\"\n  resolution_round: 37\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "issues_yaml": "issues:\n# ===== ROUND 37 CRITICAL / MUST-FIX =====\n- id: R37-MF1\n  summary: \"Holm-Bonferroni correction per-family 划分缺乏 pre-registration，核心 LP claim 在全局校正下不显著\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 34\n  last_seen_round: 37\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"R36-MF2: 需在 §7 正文讨论。标记 resolved round 37。\"\n    - round: 37\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均列为 CRITICAL [AGREE]。§7 已讨论 p_adj=0.055 但 per-family justification 仍不充分——缺乏 pre-registration 证据，k=57→k=10 的切换构成 post-hoc adjustment。正文引用 p_adj=0.006 而全局 0.055 仅在 Appendix/Limitations。\"\n  action_items:\n    - round: 37\n      action: \"正文 §7 透明报告两种 correction 结果；提供 a priori family 划分理由或承认 post-hoc；将 LP selection 描述为 'marginally significant under global correction'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R37-MF2\n  summary: \"'Simultaneously necessary conditions' 的 claim 超出 correlational co-occurrence 证据\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 37\n  last_seen_round: 37\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均 AGREE。Bound (1-D)·G_nd·α 只 capture 3-12% actual gains。'necessary' 要求移除条件后 gains 总是恢复，但 cross-model ensemble 只 partially bypasses。证据支撑 co-occurrence 而非 logical necessity。\"\n  action_items:\n    - round: 37\n      action: \"'simultaneously necessary conditions' → 'two co-occurring factors that characterize the gap'；讨论 bound looseness 对 necessity claim 的影响\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R37-MF3\n  summary: \"Diagnostic framework 无预测力（R²<0）与 title/abstract 暗示预测性的张力\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 37\n  last_seen_round: 37\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"R1 列为 Must-Fix，R2 认为应降为 Should-Fix 但承认关切有道理。Title 'Boundary Conditions' 暗示可预测性；θ_crit=0.70 缺乏 held-out cross-dataset validation。分歧在严重性定级而非事实。\"\n  action_items:\n    - round: 37\n      action: \"§1/§9 明确 diagnostic vs predictive scope；Title 考虑改为 'Failure Conditions'；提供 leave-one-dataset-out θ_crit validation\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R37-MF4\n  summary: \"与 Yao et al. (2026) 的增量新颖性区分不充分\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 35\n  last_seen_round: 37\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"R36-SF3: 降级为 Should-Fix，§1 增加 1 句区分。\"\n    - round: 37\n      reviewers: [1, 2]\n      note: \"R2 升级回 CRITICAL：instance-level 分析更细粒度但核心 insight 无质变。R1 REBUT：decomposition 是实质增量，但同意 §1 positioning 不足。分歧未完全收敛。\"\n  action_items:\n    - round: 37\n      action: \"§1 增加 1-2 句明确说明 instance-level 诊断揭示了哪些 task-level 分析无法发现的现象（如 degeneracy 分布双峰性、per-instance LP compression）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R37-MF5\n  summary: \"Related Work 缺 2025 conformal prediction for NER、token-level uncertainty、GPT-NER self-verification\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 37\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"R36-SF4: 补充了 Fisch 2021 + Angelopoulos 2023。标记 resolved。\"\n    - round: 37\n      reviewers: [1, 2]\n      note: \"R2 列为 CRITICAL，R1 认为 Should-Fix 更合适。新缺口：Conformal Structured Prediction (ICLR 2025)、arXiv 2601.16999 (NER conformal)、He et al. (NAACL 2024)、GPT-NER (ACL 2025)。收敛定为 Should-Fix。\"\n  action_items:\n    - round: 37\n      action: \"§8 补充 4-5 篇 2024-2025 引用；讨论 conformal prediction 与本文 diagnostic framework 的互补关系\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== ROUND 37 SHOULD-FIX =====\n- id: R37-SF1\n  summary: \"'Capability-diversity tension' 概念层面非原创，与 Yun & Kim (2025) diversity collapse 区分表面\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 35\n  last_seen_round: 37\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"R36-SF5: 弱化为 observed tendency。标记 resolved。\"\n    - round: 37\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均 AGREE 概念非原创。Table 66 的 definitional difference 过于表面。需承认已知现象+强调量化贡献。\"\n  action_items:\n    - round: 37\n      action: \"承认 capability-diversity tension 是 known phenomenon；明确贡献是 NER 上的量化刻画而非新概念\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R37-SF2\n  summary: \"Hidden-state probe 使用 Qwen2.5-7B 而非主模型 Qwen3-8B\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 37\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"R36-SF6: 增加 footnote 说明。标记 resolved。\"\n    - round: 37\n      reviewers: [1, 2]\n      note: \"Footnote 不够——probe 结论不能直接迁移到 Qwen3-8B。建议 Qwen3-8B 上重复 probe 或限定结论范围。\"\n  action_items:\n    - round: 37\n      action: \"在 Qwen3-8B 上训练 probe（去掉 thinking tokens）或明确限定为 Qwen2.5 family\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R37-SF3\n  summary: \"模型多样性不足，generalization claim 过强（主要 8B 级别开源模型）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 37\n  last_seen_round: 37\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"两位 Reviewer AGREE。72B/GPT-5.5 仅 tentative，capability-diversity tension 几乎全基于 8B 推断。\"\n  action_items:\n    - round: 37\n      action: \"generalization claim 限定为 '7-14B fine-tuned open-weight models'；讨论 scale/proprietary 的 limited evidence\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R37-SF4\n  summary: \"RE (n=397 单数据集) 和 SQL pilot (n=196) 证据过薄但 abstract 呈现偏强\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 37\n  last_seen_round: 37\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"AGREE。Abstract 'Cross-task validation on RE' 用词偏强，n=397 power 不足。建议 'validation' → 'exploration'。\"\n  action_items:\n    - round: 37\n      action: \"Abstract 弱化 RE/SQL 呈现；为 RE 提供 power analysis；'validation' → 'exploration'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R37-SF5\n  summary: \"Few-NERD 3 epoch vs 5 epoch confound 讨论不充分\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 37\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"R36-SF2: 5-epoch LP Δ=+0.12±0.04pp collapse 数据已有。in_progress。\"\n    - round: 37\n      reviewers: [1, 2]\n      note: \"AGREE。5-epoch degeneracy 13%→31% 数据存在但 SC selection gain 变化未展示。'Feature not bug' 论证不完全令人信服。\"\n  action_items:\n    - round: 37\n      action: \"主文简要承认 confound + 展示 3 vs 5 epoch 的 SC gain 变化数据；引用 Appendix ablation\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R37-SF6\n  summary: \"θ_crit=0.70 稳定性未经 cross-dataset/cross-model 系统验证\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 37\n  mentions:\n    - round: 35\n      reviewers: [1]\n      note: \"R1-N1: θ sweep 完成。标记 resolved。\"\n    - round: 37\n      reviewers: [1, 2]\n      note: \"AGREE。Appendix Table 22 的 ε sensitivity 仅 SciERC。不同 degeneracy regime 下同一阈值合理性未论证。\"\n  action_items:\n    - round: 37\n      action: \"提供 θ_crit 在所有 dataset × model 上的 calibration 结果或讨论为什么单一阈值有效\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R37-SF7\n  summary: \"Abstract 信息密度过高（9 句含 8+ 数字），可读性差\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 37\n  last_seen_round: 37\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"AGREE。典型 EMNLP best paper abstract 仅 2-3 个关键数字。\"\n  action_items:\n    - round: 37\n      action: \"精简 abstract 数字至 2-3 个（保留 AUROC 0.82 和 <1pp），其余移入 §1\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R37-SF8\n  summary: \"Discussion/Conclusion 过于单薄（3 段约 15 行），缺少 generalizability 讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 37\n  last_seen_round: 37\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"AGREE。缺少：框架对其他 structured prediction 的适用性、GPT-5.5 行为差异、practitioner actionable guidance。\"\n  action_items:\n    - round: 37\n      action: \"扩展 §9 至 5-6 段，讨论 open questions 和 practical guidelines\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R37-SF9\n  summary: \"术语不一致：degeneracy / output convergence / convergence 交替使用\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 37\n  last_seen_round: 37\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"AGREE。§2 定义 degeneracy rate D 后，§5/§6 切换为 output convergence。建议统一。\"\n  action_items:\n    - round: 37\n      action: \"§2 首次定义后统一使用 'degeneracy (D)'，parenthetical 注明 'also referred to as output convergence'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== EARLIER ISSUES — STATUS CARRIED FORWARD =====\n- id: R36-MF1\n  summary: \"标题 'Information Extraction' 仍 overclaim，必须改为 NER\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 33\n  last_seen_round: 37\n  mentions:\n    - round: 35\n      reviewers: [1, 2]\n      note: \"从 Structured Prediction 改为 IE，仍被指出 overclaim\"\n    - round: 36\n      reviewers: [1, 2]\n      note: \"双方 CRITICAL。RE 仅 n=397 单 seed 单数据集\"\n    - round: 37\n      reviewers: [1, 2]\n      note: \"本轮未提及，标题已为 NER。确认 resolved。\"\n  action_items:\n    - round: 36\n      action: \"标题改为 'Boundary Conditions for Named Entity Recognition'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"标题已改为 'Boundary Conditions for Named Entity Recognition'\"\n  resolution_round: 37\n\n- id: R36-MF3\n  summary: \"SciERC single seed power 限制需正文讨论\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 35\n  last_seen_round: 37\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"MDE≈1.5pp vs observed +0.2pp。需正文 power discussion。\"\n    - round: 37\n      reviewers: [1, 2]\n      note: \"本轮未单独提及，但 R1-N1 隐含涉及（SciERC n=529 是否足够）。维持 in_progress。\"\n  action_items:\n    - round: 36\n      action: \"§4/§7 增加 power limitation 讨论\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R36-SF1\n  summary: \"'Diagnostic cascade' 术语误导因果解读\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 36\n  last_seen_round: 37\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"本轮未提及 cascade 术语。确认 resolved。\"\n  action_items:\n    - round: 36\n      action: \"全文 cascade → framework\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"全文 cascade→framework，grep 确认 0 残留\"\n  resolution_round: 37\n\n- id: R36-SF6\n  summary: \"§3 自验证实验使用 Qwen2.5-7B 而非主模型 Qwen3-8B\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 37\n  mentions:\n    - round: 36\n      reviewers: [1, 2]\n      note: \"增加 footnote。标记 resolved。\"\n    - round: 37\n      reviewers: [1, 2]\n      note: \"复发。Footnote 不够，需 Qwen3-8B probe 或限定结论。升级跟踪为 R37-SF2。\"\n  action_items:\n    - round: 37\n      action: \"见 R37-SF2\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R36-SF8\n  summary: \"Responsible NLP Checklist 不应在 PDF 中\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 36\n  last_seen_round: 37\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"本轮未提及。确认 resolved。\"\n  resolution: \"main.tex 中 checklist 已移除\"\n  resolution_round: 37\n"
  }
}
```

</details>

---


### Tool result

_source line 3983 · 2026-05-22T12:19:42.663364+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 11674}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 3984 · 2026-05-22T12:21:45.023774+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 37 (Fresh Review)\n\n**论文**: \"When Does Test-Time Scaling Fail? Boundary Conditions for Named Entity Recognition\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle, Long Paper)\n**Reviewer 编排**: R1（方法严谨性 + 实验充分性）、R2（新颖性 + 完整性 + 写作质量）\n**审稿模式**: 重新审稿（fresh）\n\n---\n\n## Summary\n\n本文以 NER 为主要 case study（4 个英文数据集、主要使用 7-14B fine-tuned 模型），辅以 RE 和 SQL 的 exploratory extension，系统研究 test-time compute scaling（self-consistency, best-of-N）在 structured IE 上的失败边界条件。核心发现是一个 **correlation-selection gap**：quality estimation 信号能预测输出质量（AUROC 最高 0.82），但 instance-level selection 几乎无增益（<1pp even at N=64）。论文提出一个 diagnostic framework，将失败归因于 output convergence（degeneracy 12-68%）和 signal alignment collapse（α→0）两个 co-occurring factors。Entity-level construction 在特定条件下部分绕过了 sample-level bottleneck（+1.40pp on Few-NERD）。\n\n---\n\n## Strengths\n\n**S1. 研究问题重要且及时 [R1, R2 共识]**\n在 test-time scaling 被广泛应用于 reasoning tasks 的背景下，系统研究其在 structured prediction 上的失败模式对社区有明确价值。这是一个需要有人回答的问题。\n\n**S2. 实证规模和统计严谨性罕见 [R1, R2 共识]**\n44 页含 66 张表格、11 张图，覆盖 4 NER + 1 RE + 1 SQL 数据集、9 种方法类别、7 种 verification 模式。每个 claim 配有 bootstrap CI、permutation test、多重比较校正（Holm-Bonferroni + BH FDR）。这种 thoroughness 在 NLP 论文中极为罕见。\n\n**S3. 诚实的自我限定 [R1, R2 共识]**\n论文多处坦承 framework 是 diagnostic 而非 predictive（$R^2 < 0$）、bound 过松（3-12%）、RE/SQL 是 exploratory。这种 intellectual honesty 增强了 credibility。\n\n**S4. Correlation-selection gap 分解有洞察力 [R1, R2 共识]**\n将 \"signals predict quality but can't select better outputs\" 分解为 degeneracy（输出空间坍缩）+ alignment collapse（信号与 gain 脱耦），这个 decomposition 即使降级为 \"co-occurring factors\" 也提供了有用的分析框架。\n\n**S5. Negative result 符合 ARR H6 guideline [R2]**\n\"If something systematically does not work where it could be expected to, the community does need to know about it.\"\n\n**S6. Entity-level construction 提供了 constructive positive direction [R1]**\n在以 negative result 为主的论文中，§7.5 的 entity-level construction 证明了绕过 instance-level bottleneck 的可行路径（proof of concept）。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. Holm-Bonferroni correction 策略选择存在 cherry-picking 风险 [R1 N1, R2 AGREE]**\n全局 Holm-Bonferroni 在 k=57 下 $p_{\\text{adj}}=0.055$，未达 α=0.05。论文转而采用 per-family correction（k=10），得到 $p_{\\text{adj}}=0.006$。正文引用 per-family 结果，全局结果仅出现在 Appendix/Limitations。两位 Reviewer 一致认为：\n- 缺乏 pre-registration 证据证明 family 划分是 pre-specified 的\n- 从 k=57 切换到 k=10 降低校正力度约 5.7 倍，构成 post-hoc adjustment\n- 核心 claim \"LP is the only signal achieving significant positive selection\" 在最保守校正下不成立\n- 正文需透明报告两种结果并承认边界情况\n\n**MF2. \"Simultaneously necessary conditions\" 过度 claim [R1 N2, R2 AGREE]**\n论文声称 degeneracy 和 signal alignment collapse 是 \"simultaneously necessary conditions\"（§4, §6.3, Abstract），但：\n- 证据结构是 correlational co-occurrence，非 logical necessity\n- Bound $(1-D) \\cdot G_{\\text{nd}} \\cdot \\alpha$ 只 capture 3-12% actual gains——88-97% 的 variance 未被解释\n- 移除 degeneracy（如 cross-model ensemble）只 \"partially bypasses\" bottleneck，不能完全恢复 gains\n- 建议改为 \"two co-occurring factors that characterize the gap\"\n\n**MF3. Framework 无预测力与 title/abstract 暗示的预测性存在张力 [R1 N3; R2 部分同意但认为严重性低于 Must-Fix]**\n- Title \"Boundary Conditions\" 暗示可预测性，但 $R^2 < 0$\n- $\\theta_{\\text{crit}}=0.70$ 是从数据拟合的经验阈值，缺乏 held-out cross-dataset validation\n- 论文的 practitioner guidance（\"measure degeneracy with N=8 before investing\"）依赖某种预测力，但 framework 实际只能 post-hoc 解释\n- R2 认为 post-hoc diagnostic 仍有价值（类比医学病理分析），建议降级为 Should-Fix + 修改标题措辞\n- **Director 判断**：定为 Must-Fix——title/abstract 的 framing 与实际能力的 mismatch 是可修复的，但不修复会误导读者\n\n**MF4. 与 Yao et al. (2026) 的增量新颖性区分不充分 [R2 N1; R1 部分 REBUT]**\n- Yao et al. 已报告 NER/RE 上的 QE correlation（ρ up to 0.47），结论方向一致\n- R2 认为：instance-level 分析更细粒度但核心 insight 无质变\n- R1 反驳：decomposition（degeneracy + alignment collapse）是实质增量，Yao et al. 没有 failure mechanism 解释\n- **Director 判断**：论文确实提供了超越 Yao et al. 的 mechanistic decomposition，但 §1 对此区分严重不足。定为 Must-Fix（positioning 问题可修复）。需在 Introduction 明确说明 instance-level 诊断揭示了哪些 task-level 分析无法发现的现象。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. \"Capability-diversity tension\" 概念非原创 [R2 N2, R1 AGREE]**\n\"模型能力越强，输出越收敛\" 是 well-known 现象。Yun & Kim (2025) 的 \"diversity collapse\" 已描述类似机制。Table 66 的 \"definitional difference\" 过于表面。建议承认已知现象，明确贡献是 NER 上的量化刻画。\n\n**SF2. Related Work 覆盖存在缺口 [R2 N3, R1 部分 AGREE]**\n缺少 2024-2025 年的重要进展：\n- Conformal Structured Prediction (ICLR 2025)\n- NER conformal prediction (arXiv 2601.16999)\n- Token-level uncertainty transmission (He et al., NAACL 2024 Findings)\n- GPT-NER self-verification (ACL 2025)\nR1 认为缺口存在但不应列为 critical——论文核心方向（TTS/SC/MBR）已覆盖。**Director 定为 Should-Fix**。\n\n**SF3. Hidden-state probe 模型不一致 [R1 W1, R2 AGREE]**\n主实验用 Qwen3-8B，probe 用 Qwen2.5-7B。Footnote 不充分——probe 结论（\"quality information encoded in hidden representations\"）未在主模型上验证。\n\n**SF4. 模型多样性不足以支撑 generalization claim [R1 W2, R2 AGREE]**\n主要结果来自两个 8B 级别开源模型。4B/14B 是 ablation，72B 是 tentative，GPT-5.5 仅 200 instances。generalization claim 应限定为 \"7-14B fine-tuned open-weight models\"。\n\n**SF5. RE/SQL 证据过薄但 abstract 呈现偏强 [R1 W3, R2 AGREE]**\nRE 仅 SciERC（n=397），SQL 是 pilot（n=196）。Abstract \"Cross-task validation on RE\" 用词偏强（建议 → \"exploration\"）。\n\n**SF6. Few-NERD 3 epoch confound [R1 W4, R2 AGREE]**\nFew-NERD 唯一使用 3 epoch（其他 5 epoch），也是唯一 positive LP selection 结果。5-epoch degeneracy 从 13% 升至 31%，LP Δ 从 +1.39 降至 +0.12pp。\"Feature not bug\" 的论证不完全令人信服——需展示 3 vs 5 epoch 的 SC selection gain 变化全貌。\n\n**SF7. θ_crit=0.70 稳定性未系统验证 [R1 W5, R2 AGREE]**\nTable 22 的 sensitivity analysis 仅在 SciERC 上做。不同 degeneracy regime（SciERC 12.2% vs Few-NERD 68%）下同一阈值是否合理未论证。\n\n**SF8. Abstract 信息密度过高 [R2 W2, R1 AGREE]**\n9 句话含 8+ 数字/符号。建议精简至 2-3 个关键数字。\n\n**SF9. Discussion/Conclusion 过于单薄 [R2 W4, R1 AGREE]**\n仅 3 段约 15 行，缺少：框架对其他 structured prediction 的适用性、GPT-5.5 行为差异、practitioner actionable guidance。\n\n**SF10. 术语不一致 [R2 W5, R1 AGREE]**\ndegeneracy / output convergence / convergence 交替使用。建议统一。\n\n### Minor（不影响接收）\n\n- **M1**: Figure 1 因果箭头暗示了未建立的因果关系\n- **M2**: §2.1 前向引用造成理解中断\n- **M3**: Proposition 1 entity-wise independence 假设被自身数据部分违反（split-half r≈0.58-0.64），应在主文中注明\n- **M4**: Table 3 AUROC binarization threshold 缺 sensitivity analysis\n- **M5**: §8 Yun et al. (2025) 对比不够具体\n- **M6**: Figure 4 轴标签字号接近可读下限\n- **M7**: Appendix 比例 4.5:1（36 页 vs 8 页正文）暗示正文可能遗漏重要信息（如 Holm 分析应在正文总结）\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Holm-Bonferroni correction 策略需要更透明的处理**——核心 LP claim 在全局校正下处于边界\n2. **\"Simultaneously necessary conditions\" 应降级为 \"co-occurring factors\"**\n3. **Capability-diversity tension 不应声称为新概念**——贡献在于量化而非发现\n4. **Abstract 信息过载、Discussion 过薄、术语不一致**需要修复\n5. **Hidden-state probe 模型不一致、RE/SQL 证据薄、Few-NERD confound、θ_crit 稳定性**均需改善\n6. **实验规模、统计严谨性、诚实的自我限定**是论文的突出优势\n\n## Reviewer Divergence [分歧]\n\n1. **与 Yao et al. 的新颖性区分**：R2 认为增量不足以达主会议水平；R1 认为 instance-level decomposition 是实质增量，需更好 positioning\n2. **Related Work 缺口的严重性**：R2 列为 critical；R1 认为是 should-fix\n3. **Framework 预测力问题的严重性**：R1 列为 must-fix；R2 认为 post-hoc diagnostic 有独立价值，建议 should-fix\n4. **Entity-level construction 的意义**：R2 认为 +1.40pp 实际意义有限；R1 认为 proof of concept 价值不应低估\n\n---\n\n## Questions（需要作者澄清）\n\nQ1. 全局 Holm-Bonferroni 的 family 划分是 pre-specified 还是 post-hoc？\nQ2. 新任务上 diagnostic framework 的具体使用流程是什么？需要多少 compute 才能得出诊断？\nQ3. Entity-wise independence 假设下 bound 只 capture 3-12%——是否考虑过 entity-group level decomposition 来 tighten the bound？\nQ4. Qwen 同族变体（如 Qwen3-8B + Qwen3-4B）ensemble 是否能区分 architectural vs random initialization diversity？\nQ5. WNUT-17 51% zero-F1 instances 的成因是 entity type rarity 还是 model failure？\nQ6. 如果将 Few-NERD 训练到 5 epoch 使 degeneracy 从 13% 升至 31%，对应的 LP selection gain 变化全貌如何？\n\n---\n\n## Missing References\n\n1. Conformal Structured Prediction (ICLR 2025)\n2. Uncertainty Quantification for NER via Full-Sequence and Subsequence Conformal Prediction (arXiv 2601.16999, 2025)\n3. He et al. (NAACL 2024 Findings) — Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\n4. GPT-NER (ACL 2025 Findings) — LLM-based NER self-verification\n5. Xiao & Wang (2021) — LLM Calibration on Structured Outputs（如存在）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未启用（项目配置 external_review 未开启）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 2 warning, 16 info）。\n\n**Warnings**:\n1. **Page 8-9**: 主正文末尾连续 2 页纯文本（Related Work + Discussion + Limitations + Ethics + References），无 display item 收尾。建议在 Discussion 中加总结性 figure/table。\n2. **Page 17-20**: Appendix 连续 4 页纯文本（Appendices h-m），无 figure/table 穿插。\n\n**Positive findings**:\n- Figure 1 有效传达核心 message，颜色方案色盲友好\n- 主正文 8 页含 4 figures + 4 tables = 8 display items（1.0/页），密度合理\n- 所有表格使用 booktabs 风格，格式规范\n- 无 LaTeX 错误、无 margin overflow、无未解析引用\n- Double-blind 合规\n\n---\n\n## Overall Assessment\n\n**评分**: 3.0–3.5 (Findings – Borderline Conference)\n- R1: 3.5 (Borderline Conference)\n- R2: 3.0 (Findings)\n\n**Director 综合判断**: **3.0 (Findings)**\n\n理由：\n1. **统计基础处于边界**（MF1）：论文最核心的 positive claim（LP selection）在最保守校正下 p=0.055，这不是致命缺陷但限制了 claim 的强度\n2. **新颖性增量存在但需更好 positioning**（MF4）：instance-level decomposition 超越 Yao et al.，但论文未能在 Introduction 中清晰建立这一区分\n3. **Framework 定位存在 mismatch**（MF2, MF3）：title/abstract 暗示的预测性与实际 diagnostic 能力之间的张力需要修复\n4. **核心 negative result 有社区价值**：SC 在 NER 上系统失效的证据、correlation-selection gap 的分解、9 种方法的系统比较——这些对 Findings track 有充分贡献\n5. **修复路径清晰**：4 个 Must-Fix 均为 framing/reporting 问题而非实验缺陷，revision 可在不增加实验的情况下 address\n\n**置信度**: 4/5（两位 Reviewer 均熟悉 TTS/SC/NER 方法论，仔细阅读了全文 44 页）\n\n**对 Research Director 的建议**（仅为参考，非审稿人职责范围）：\n- MF1-MF4 均为 framing/statistical reporting 问题，不需要新实验\n- SF6（Few-NERD confound）和 SF7（θ_crit validation）可能需要少量补充分析\n- 如果 revision 能 (1) 透明报告全局 HB 结果、(2) 降级 necessity claim、(3) 修正 title/abstract framing、(4) 在 §1 清晰定位 vs Yao et al.，论文可冲击 3.5 (Borderline Conference)",
  "project": "struct_self_consist_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 37 (Fresh Review)\n\n**论文**: \"When Does Test-Time Scaling Fail? Boundary Conditions for Named Entity Recognition\"\n**Venue**: EMNLP 2026 (ARR May 2026 cycle, Long Paper)\n**Reviewer 编排**: R1（方法严谨性 + 实验充分性）、R2（新颖性 + 完整性 + 写作质量）\n**审稿模式**: 重新审稿（fresh）\n\n---\n\n## Summary\n\n本文以 NER 为主要 case study（4 个英文数据集、主要使用 7-14B fine-tuned 模型），辅以 RE 和 SQL 的 exploratory extension，系统研究 test-time compute scaling（self-consistency, best-of-N）在 structured IE 上的失败边界条件。核心发现是一个 **correlation-selection gap**：quality estimation 信号能预测输出质量（AUROC 最高 0.82），但 instance-level selection 几乎无增益（<1pp even at N=64）。论文提出一个 diagnostic framework，将失败归因于 output convergence（degeneracy 12-68%）和 signal alignment collapse（α→0）两个 co-occurring factors。Entity-level construction 在特定条件下部分绕过了 sample-level bottleneck（+1.40pp on Few-NERD）。\n\n---\n\n## Strengths\n\n**S1. 研究问题重要且及时 [R1, R2 共识]**\n在 test-time scaling 被广泛应用于 reasoning tasks 的背景下，系统研究其在 structured prediction 上的失败模式对社区有明确价值。这是一个需要有人回答的问题。\n\n**S2. 实证规模和统计严谨性罕见 [R1, R2 共识]**\n44 页含 66 张表格、11 张图，覆盖 4 NER + 1 RE + 1 SQL 数据集、9 种方法类别、7 种 verification 模式。每个 claim 配有 bootstrap CI、permutation test、多重比较校正（Holm-Bonferroni + BH FDR）。这种 thoroughness 在 NLP 论文中极为罕见。\n\n**S3. 诚实的自我限定 [R1, R2 共识]**\n论文多处坦承 framework 是 diagnostic 而非 predictive（$R^2 < 0$）、bound 过松（3-12%）、RE/SQL 是 exploratory。这种 intellectual honesty 增强了 credibility。\n\n**S4. Correlation-selection gap 分解有洞察力 [R1, R2 共识]**\n将 \"signals predict quality but can't select better outputs\" 分解为 degeneracy（输出空间坍缩）+ alignment collapse（信号与 gain 脱耦），这个 decomposition 即使降级为 \"co-occurring factors\" 也提供了有用的分析框架。\n\n**S5. Negative result 符合 ARR H6 guideline [R2]**\n\"If something systematically does not work where it could be expected to, the community does need to know about it.\"\n\n**S6. Entity-level construction 提供了 constructive positive direction [R1]**\n在以 negative result 为主的论文中，§7.5 的 entity-level construction 证明了绕过 instance-level bottleneck 的可行路径（proof of concept）。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. Holm-Bonferroni correction 策略选择存在 cherry-picking 风险 [R1 N1, R2 AGREE]**\n全局 Holm-Bonferroni 在 k=57 下 $p_{\\text{adj}}=0.055$，未达 α=0.05。论文转而采用 per-family correction（k=10），得到 $p_{\\text{adj}}=0.006$。正文引用 per-family 结果，全局结果仅出现在 Appendix/Limitations。两位 Reviewer 一致认为：\n- 缺乏 pre-registration 证据证明 family 划分是 pre-specified 的\n- 从 k=57 切换到 k=10 降低校正力度约 5.7 倍，构成 post-hoc adjustment\n- 核心 claim \"LP is the only signal achieving significant positive selection\" 在最保守校正下不成立\n- 正文需透明报告两种结果并承认边界情况\n\n**MF2. \"Simultaneously necessary conditions\" 过度 claim [R1 N2, R2 AGREE]**\n论文声称 degeneracy 和 signal alignment collapse 是 \"simultaneously necessary conditions\"（§4, §6.3, Abstract），但：\n- 证据结构是 correlational co-occurrence，非 logical necessity\n- Bound $(1-D) \\cdot G_{\\text{nd}} \\cdot \\alpha$ 只 capture 3-12% actual gains——88-97% 的 variance 未被解释\n- 移除 degeneracy（如 cross-model ensemble）只 \"partially bypasses\" bottleneck，不能完全恢复 gains\n- 建议改为 \"two co-occurring factors that characterize the gap\"\n\n**MF3. Framework 无预测力与 title/abstract 暗示的预测性存在张力 [R1 N3; R2 部分同意但认为严重性低于 Must-Fix]**\n- Title \"Boundary Conditions\" 暗示可预测性，但 $R^2 < 0$\n- $\\theta_{\\text{crit}}=0.70$ 是从数据拟合的经验阈值，缺乏 held-out cross-dataset validation\n- 论文的 practitioner guidance（\"measure degeneracy with N=8 before investing\"）依赖某种预测力，但 framework 实际只能 post-hoc 解释\n- R2 认为 post-hoc diagnostic 仍有价值（类比医学病理分析），建议降级为 Should-Fix + 修改标题措辞\n- **Director 判断**：定为 Must-Fix——title/abstract 的 framing 与实际能力的 mismatch 是可修复的，但不修复会误导读者\n\n**MF4. 与 Yao et al. (2026) 的增量新颖性区分不充分 [R2 N1; R1 部分 REBUT]**\n- Yao et al. 已报告 NER/RE 上的 QE correlation（ρ up to 0.47），结论方向一致\n- R2 认为：instance-level 分析更细粒度但核心 insight 无质变\n- R1 反驳：decomposition（degeneracy + alignment collapse）是实质增量，Yao et al. 没有 failure mechanism 解释\n- **Director 判断**：论文确实提供了超越 Yao et al. 的 mechanistic decomposition，但 §1 对此区分严重不足。定为 Must-Fix（positioning 问题可修复）。需在 Introduction 明确说明 instance-level 诊断揭示了哪些 task-level 分析无法发现的现象。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. \"Capability-diversity tension\" 概念非原创 [R2 N2, R1 AGREE]**\n\"模型能力越强，输出越收敛\" 是 well-known 现象。Yun & Kim (2025) 的 \"diversity collapse\" 已描述类似机制。Table 66 的 \"definitional difference\" 过于表面。建议承认已知现象，明确贡献是 NER 上的量化刻画。\n\n**SF2. Related Work 覆盖存在缺口 [R2 N3, R1 部分 AGREE]**\n缺少 2024-2025 年的重要进展：\n- Conformal Structured Prediction (ICLR 2025)\n- NER conformal prediction (arXiv 2601.16999)\n- Token-level uncertainty transmission (He et al., NAACL 2024 Findings)\n- GPT-NER self-verification (ACL 2025)\nR1 认为缺口存在但不应列为 critical——论文核心方向（TTS/SC/MBR）已覆盖。**Director 定为 Should-Fix**。\n\n**SF3. Hidden-state probe 模型不一致 [R1 W1, R2 AGREE]**\n主实验用 Qwen3-8B，probe 用 Qwen2.5-7B。Footnote 不充分——probe 结论（\"quality information encoded in hidden representations\"）未在主模型上验证。\n\n**SF4. 模型多样性不足以支撑 generalization claim [R1 W2, R2 AGREE]**\n主要结果来自两个 8B 级别开源模型。4B/14B 是 ablation，72B 是 tentative，GPT-5.5 仅 200 instances。generalization claim 应限定为 \"7-14B fine-tuned open-weight models\"。\n\n**SF5. RE/SQL 证据过薄但 abstract 呈现偏强 [R1 W3, R2 AGREE]**\nRE 仅 SciERC（n=397），SQL 是 pilot（n=196）。Abstract \"Cross-task validation on RE\" 用词偏强（建议 → \"exploration\"）。\n\n**SF6. Few-NERD 3 epoch confound [R1 W4, R2 AGREE]**\nFew-NERD 唯一使用 3 epoch（其他 5 epoch），也是唯一 positive LP selection 结果。5-epoch degeneracy 从 13% 升至 31%，LP Δ 从 +1.39 降至 +0.12pp。\"Feature not bug\" 的论证不完全令人信服——需展示 3 vs 5 epoch 的 SC selection gain 变化全貌。\n\n**SF7. θ_crit=0.70 稳定性未系统验证 [R1 W5, R2 AGREE]**\nTable 22 的 sensitivity analysis 仅在 SciERC 上做。不同 degeneracy regime（SciERC 12.2% vs Few-NERD 68%）下同一阈值是否合理未论证。\n\n**SF8. Abstract 信息密度过高 [R2 W2, R1 AGREE]**\n9 句话含 8+ 数字/符号。建议精简至 2-3 个关键数字。\n\n**SF9. Discussion/Conclusion 过于单薄 [R2 W4, R1 AGREE]**\n仅 3 段约 15 行，缺少：框架对其他 structured prediction 的适用性、GPT-5.5 行为差异、practitioner actionable guidance。\n\n**SF10. 术语不一致 [R2 W5, R1 AGREE]**\ndegeneracy / output convergence / convergence 交替使用。建议统一。\n\n### Minor（不影响接收）\n\n- **M1**: Figure 1 因果箭头暗示了未建立的因果关系\n- **M2**: §2.1 前向引用造成理解中断\n- **M3**: Proposition 1 entity-wise independence 假设被自身数据部分违反（split-half r≈0.58-0.64），应在主文中注明\n- **M4**: Table 3 AUROC binarization threshold 缺 sensitivity analysis\n- **M5**: §8 Yun et al. (2025) 对比不够具体\n- **M6**: Figure 4 轴标签字号接近可读下限\n- **M7**: Appendix 比例 4.5:1（36 页 vs 8 页正文）暗示正文可能遗漏重要信息（如 Holm 分析应在正文总结）\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Holm-Bonferroni correction 策略需要更透明的处理**——核心 LP claim 在全局校正下处于边界\n2. **\"Simultaneously necessary conditions\" 应降级为 \"co-occurring factors\"**\n3. **Capability-diversity tension 不应声称为新概念**——贡献在于量化而非发现\n4. **Abstract 信息过载、Discussion 过薄、术语不一致**需要修复\n5. **Hidden-state probe 模型不一致、RE/SQL 证据薄、Few-NERD confound、θ_crit 稳定性**均需改善\n6. **实验规模、统计严谨性、诚实的自我限定**是论文的突出优势\n\n## Reviewer Divergence [分歧]\n\n1. **与 Yao et al. 的新颖性区分**：R2 认为增量不足以达主会议水平；R1 认为 instance-level decomposition 是实质增量，需更好 positioning\n2. **Related Work 缺口的严重性**：R2 列为 critical；R1 认为是 should-fix\n3. **Framework 预测力问题的严重性**：R1 列为 must-fix；R2 认为 post-hoc diagnostic 有独立价值，建议 should-fix\n4. **Entity-level construction 的意义**：R2 认为 +1.40pp 实际意义有限；R1 认为 proof of concept 价值不应低估\n\n---\n\n## Questions（需要作者澄清）\n\nQ1. 全局 Holm-Bonferroni 的 family 划分是 pre-specified 还是 post-hoc？\nQ2. 新任务上 diagnostic framework 的具体使用流程是什么？需要多少 compute 才能得出诊断？\nQ3. Entity-wise independence 假设下 bound 只 capture 3-12%——是否考虑过 entity-group level decomposition 来 tighten the bound？\nQ4. Qwen 同族变体（如 Qwen3-8B + Qwen3-4B）ensemble 是否能区分 architectural vs random initialization diversity？\nQ5. WNUT-17 51% zero-F1 instances 的成因是 entity type rarity 还是 model failure？\nQ6. 如果将 Few-NERD 训练到 5 epoch 使 degeneracy 从 13% 升至 31%，对应的 LP selection gain 变化全貌如何？\n\n---\n\n## Missing References\n\n1. Conformal Structured Prediction (ICLR 2025)\n2. Uncertainty Quantification for NER via Full-Sequence and Subsequence Conformal Prediction (arXiv 2601.16999, 2025)\n3. He et al. (NAACL 2024 Findings) — Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\n4. GPT-NER (ACL 2025 Findings) — LLM-based NER self-verification\n5. Xiao & Wang (2021) — LLM Calibration on Structured Outputs（如存在）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未启用（项目配置 external_review 未开启）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical, 2 warning, 16 info）。\n\n**Warnings**:\n1. **Page 8-9**: 主正文末尾连续 2 页纯文本（Related Work + Discussion + Limitations + Ethics + References），无 display item 收尾。建议在 Discussion 中加总结性 figure/table。\n2. **Page 17-20**: Appendix 连续 4 页纯文本（Appendices h-m），无 figure/table 穿插。\n\n**Positive findings**:\n- Figure 1 有效传达核心 message，颜色方案色盲友好\n- 主正文 8 页含 4 figures + 4 tables = 8 display items（1.0/页），密度合理\n- 所有表格使用 booktabs 风格，格式规范\n- 无 LaTeX 错误、无 margin overflow、无未解析引用\n- Double-blind 合规\n\n---\n\n## Overall Assessment\n\n**评分**: 3.0–3.5 (Findings – Borderline Conference)\n- R1: 3.5 (Borderline Conference)\n- R2: 3.0 (Findings)\n\n**Director 综合判断**: **3.0 (Findings)**\n\n理由：\n1. **统计基础处于边界**（MF1）：论文最核心的 positive claim（LP selection）在最保守校正下 p=0.055，这不是致命缺陷但限制了 claim 的强度\n2. **新颖性增量存在但需更好 positioning**（MF4）：instance-level decomposition 超越 Yao et al.，但论文未能在 Introduction 中清晰建立这一区分\n3. **Framework 定位存在 mismatch**（MF2, MF3）：title/abstract 暗示的预测性与实际 diagnostic 能力之间的张力需要修复\n4. **核心 negative result 有社区价值**：SC 在 NER 上系统失效的证据、correlation-selection gap 的分解、9 种方法的系统比较——这些对 Findings track 有充分贡献\n5. **修复路径清晰**：4 个 Must-Fix 均为 framing/reporting 问题而非实验缺陷，revision 可在不增加实验的情况下 address\n\n**置信度**: 4/5（两位 Reviewer 均熟悉 TTS/SC/NER 方法论，仔细阅读了全文 44 页）\n\n**对 Research Director 的建议**（仅为参考，非审稿人职责范围）：\n- MF1-MF4 均为 framing/statistical reporting 问题，不需要新实验\n- SF6（Few-NERD confound）和 SF7（θ_crit validation）可能需要少量补充分析\n- 如果 revision 能 (1) 透明报告全局 HB 结果、(2) 降级 necessity claim、(3) 修正 title/abstract framing、(4) 在 §1 清晰定位 vs Yao et al.，论文可冲击 3.5 (Borderline Conference)",
    "project": "struct_self_consist_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 3985 · 2026-05-22T12:21:49.140899+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4117
}
```

</details>

---


### Assistant

_source line 3986 · 2026-05-22T12:21:56.124322+00:00_

审稿报告已投递。

---

**Round 37 审稿完成。**

**Overall: 3.0 (Findings)**，R1 给 3.5、R2 给 3.0，综合取 3.0。

**4 个 Must-Fix**（均为 framing/reporting，不需新实验）：
1. Holm-Bonferroni 全局 p=0.055 需正文透明报告
2. "Simultaneously necessary conditions" → "co-occurring factors"
3. Title/Abstract 暗示预测力 vs 实际 diagnostic 能力的 mismatch
4. 与 Yao et al. (2026) 的区分需在 §1 明确建立

**10 个 Should-Fix**（capability-diversity tension 非原创、Related Work 缺口、probe 模型不一致、模型多样性、RE/SQL 证据、Few-NERD confound、θ_crit 稳定性、Abstract 密度、Discussion 单薄、术语不一致）。

**修复路径清晰**：所有 Must-Fix 为 framing/reporting 问题，revision 后可冲击 3.5 (Borderline Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 303

## Round 303

2 recorded events


### User

_source line 3987 · 2026-05-22T12:21:58.932768+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

**回应摘要**：

- **13/13 条中 AGREE 12 条，REBUT 1 条**（R1-N3）
- 对 R1-N1（HB cherry-picking）和 R1-N2（necessary conditions overclaim）**完全同意**，补充了 Table 12 的 BH FDR 证据
- 对 R1-N3（无预测力）**部分反驳**：post-hoc diagnostic 仍有 deployment 指导价值（θ_crit=0.70 的 cross-configuration 一致性），建议从 Must-Fix 降为 Should-Fix
- R1 的 5 个 Should-Fix 和 5 个 Minor **全部同意**，在 W4（Few-NERD confound）上补充了 3 vs 5 epoch 对 SC gain 影响的追问
- 维持 Overall 3.0 (Findings)，与 R1 的 3.5 差异主要在新颖性权重上

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 3988 · 2026-05-22T12:22:09.082571+00:00_

审稿报告已投递至 Research Director。

**Round 37 审稿完成**，汇总如下：

| 维度 | 结果 |
|------|------|
| R1 评分 | 3.5 (Borderline Conference) |
| R2 评分 | 3.0 (Findings) |
| **综合评分** | **3.0 (Findings)** |
| Must-Fix | 4 项（HB correction 透明度、necessity claim 降级、framework 定位 mismatch、vs Yao et al. positioning） |
| Should-Fix | 10 项 |
| Minor | 7 项 |
| 交叉共识率 | 26 条中 AGREE 23 条（88.5%） |

**核心结论**：论文实验规模突出、统计处理严谨、negative result 有社区价值，但 4 个 Must-Fix 均为 framing/statistical reporting 问题——修复路径清晰，不需要新实验。如果 revision 能透明报告全局 HB 结果、降级 necessity claim、修正 title/abstract framing、在 §1 清晰定位 vs Yao et al.，可冲击 3.5 (Borderline Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 304

## Round 304

80 recorded events


### User

_source line 3989 · 2026-05-22T12:40:58.157432+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 3990 · 2026-05-22T12:41:04.970346+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3991 · 2026-05-22T12:41:05.139193+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 168
}
```

</details>

---


### Tool call

_source line 3992 · 2026-05-22T12:41:11.361898+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 3993 · 2026-05-22T12:41:11.362461+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 3994 · 2026-05-22T12:41:16.434529+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 3995 · 2026-05-22T12:41:16.486179+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 3996 · 2026-05-22T12:41:31.677918+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 3997 · 2026-05-22T12:41:33.485915+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (324 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp_fewnerd_pretrained_n16_s42 | Pretrained N-scaling: FewNERD N=16 with Qwen2.5-7B-Instruct. Fills pretrained N-scaling curve (N=8/16/32) for FewNERD. FewNERD pretrained N=8 showed +3.90pp MV gain. Tests monotonic scaling. | — | — | — |\n| exp_fewnerd_5epoch_lp_s42 | FewNERD 5-epoch checkpoint with LP selection will show improved F1 over majority voting, similar to the 3-epoch results, validating that LP selection is robust across training epochs | — | — | — |\n| exp_fewnerd_mf4_s123_v2 | MF4 pipeline fix retry: FewNERD N=8 T=1.0 seed=123 using run_mvp_pilot.py (micro-F1). Replaces exp_fewnerd_mf4_s123 which failed due to GPU contention on autodl-5090. Required for 3-seed statistical power with unified pipeline. | — | — | — |\n\n## 待处理\n- exp_fewnerd_freeform_n8_s42: R35-W6 free-form decoding ablation: FewNERD N=8 T=1.0 seed=42 without grammar constraints. FewNERD has lowest degeneracy (12% at N=8). If free-form degeneracy remains low (~12%), confirms degeneracy is model-intrinsic, not a constrained decoding artifact. Complements CoNLL free-form ablation (59.3% vs 56.7% constrained).（准备中）\n- exp_conll_freefo
…[truncated 1744 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1807
}
```

</details>

---


### Tool call

_source line 3998 · 2026-05-22T12:41:33.537280+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 3999 · 2026-05-22T12:41:33.587916+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{amsthm}
16	\newtheorem{proposition}{Proposition}
17	\newtheorem{theorem}{Theorem}
18	\newtheorem{corollary}{Corollary}
19	\newtheorem{definition}{Definition}
20	\usepackage{multirow}
21	\usepackage{xcolor}
22	\usepackage{subcaption}
23	\usepackage{alphalph}
24	\usepackage{enumitem}
25	
26	\graphicspath{{figures/}}
27	
28	\title{When Does Test-Time Scaling Fail?\\ Boundary Conditions for Named Entity Recognition}
29	
30	\author{Anonymous}
31	
32	\begin{document}
33	\maketitle
34	
35	\input{sections/abstract}
36	\input{sections/introduction}
37	\input{sections/diagnostic}
38	\input{sections/mechanistic}
39	\input{sections/single_signal}
40	\input{sections/adaptive}
41	\input{sections/theory}
42	\input{sections/experiments_main}
43	\input{sections/background}
44	\input{sections/discussion}
45	
46	\section*{Limitations}
47	\input{sections/limitations}
48	
49	\section*{Ethics Statement}
50	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, Few-NERD, WNUT-17), open-weight models (Qwen3-8B, Qwen3-14B, Qwen3-4B, LLaMA-3.1-8B), and the GPT-5.5 API.
51	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
52	No new human data was collected or annotated for this study.
53	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
54	Code and data will be released upon acceptance at [anonymized URL].
55	
56	\bibliography{references}
57	
58	\appendix
59	\renewcommand{\thesection}{\alphalph{\value{section}}}
60	\input{se
…[truncated 42 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4000 · 2026-05-22T12:41:33.789283+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/submitted.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/submitted.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 4001 · 2026-05-22T12:41:33.940468+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_33/submitted.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_34/submitted.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_35/submitted.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_36/submitted.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_37/submitted.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_38/submitted.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 4002 · 2026-05-22T12:41:45.125313+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 4003 · 2026-05-22T12:41:45.175826+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4004 · 2026-05-22T12:41:47.987744+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines"
  }
}
```

</details>

---


### Tool call

_source line 4005 · 2026-05-22T12:41:49.093465+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 author guidelines page limit format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 author guidelines page limit format requirements"
  }
}
```

</details>

---


### Tool call

_source line 4006 · 2026-05-22T12:41:49.595465+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 4007 · 2026-05-22T12:41:56.273891+00:00_

Web search results for query: "ACL Rolling Review 2026 author guidelines page limit format requirements"

Links: [{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Instructions for *ACL Proceedings","url":"https://arxiv.org/html/2506.06751v2"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"}]

Based on the search results, here are the key author guidelines for ACL Rolling Review 2026:

**Format Requirements:**

Papers must follow ACL formatting, and authors are encouraged to use the ACL pubcheck tool to check for common problems. ARR has abandoned the MS Word template for conference submissions, and submissions based on the Word template will be desk-rejected starting from March 2026.

**Page Limits:**

For final versions, accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

**Limitations Section:**

Since D
…[truncated 857 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 7180
}
```

</details>

---


### Tool result

_source line 4008 · 2026-05-22T12:42:02.215340+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"}]

I found comprehensive information about the EMNLP 2026 call for papers and ARR submission guidelines. Here's a summary:

## Call for Papers Overview

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. EMNLP 2026 has a goal of curating a diverse technical program—in addition to traditional research results, papers may contribute negative findings, survey an area, announce the creation of a new resour
…[truncated 1554 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 14227
}
```

</details>

---


### Tool result

_source line 4009 · 2026-05-22T12:42:02.266141+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 12670
}
```

</details>

---


### Tool call

_source line 4010 · 2026-05-22T12:42:07.195834+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,TodoWrite",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,TodoWrite",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 4011 · 2026-05-22T12:42:07.196320+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 4012 · 2026-05-22T12:42:14.551330+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: Venue 调研 + 资料检查', 'status': 'completed', 'activeForm': '完成 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'in_progress', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 外部审稿 + 视觉审查派发', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: Venue 调研 + 资料检查', 'status': 'completed', 'activeForm': '完成 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'in_progress', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6/0.7: 外部审稿 + 视觉审查派发', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 4013 · 2026-05-22T12:42:14.702271+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 4014 · 2026-05-22T12:42:19.671931+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 4015 · 2026-05-22T12:42:20.174905+00:00_

1	\begin{abstract}
2	Test-time compute scaling---repeated sampling with self-consistency or best-of-$N$---yields large gains on discrete-answer reasoning, but whether these gains transfer to NER remains open.
3	We characterize when scaling succeeds and fails, using NER (four datasets, primarily 7--14B fine-tuned) as the primary case study with exploratory RE and SQL extensions.
4	Quality estimation signals predict output quality (AUROC up to $0.82$), yet instance-level selection yields ${<}1$\,pp even at $N{=}64$, revealing a \textbf{correlation-selection gap}.
5	A diagnostic framework identifies two co-occurring conditions---high output convergence (hereafter \textit{degeneracy}) and signal alignment collapse---that jointly determine scaling returns; cross-task exploration confirms task-specific failure modes.
6	Exploratory entity-level construction partially bypasses the bottleneck ($+1.40$\,pp where low degeneracy and signal alignment provide headroom).
7	The framework guides practitioners on what to measure before investing in repeated inference; the observed capability-diversity tension may extend beyond NER but requires further validation.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 4016 · 2026-05-22T12:42:20.225665+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 4017 · 2026-05-22T12:42:21.128866+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time compute scaling---self-consistency \cite{wang2023selfconsistency}, best-of-$N$ \cite{snell2025scaling, brown2024monkeys}, extended reasoning \cite{muennighoff2025s1}---yields large gains on discrete-answer tasks where outputs admit equivalence classes or execution-based verification.
4	For NER, where outputs are entity sets with partial overlap, the boundary conditions for effective scaling are unknown; prior work \cite{yao2026consistency, yun2025price} provides initial observations but no systematic diagnostic framework quantifying failure mechanisms at entity level across multiple model families.
5	Prior work \cite{yao2026consistency} observes this gap at the task level; we decompose it at the instance level, revealing that degeneracy eliminates candidates while LP compression eliminates discriminability.
6	
7	Using NER (four datasets, primarily 7--14B fine-tuned; tentative cross-scale observations to 72B) and RE as case studies, we identify a \textbf{correlation-selection gap}: quality estimation signals predict output quality ($\rho$ up to $0.45$, AUROC $0.82$; Table~\ref{tab:quality_estimation}), yet selection fails---MV gains ${<}1$\,pp even at $N{=}64$ (Figure~\ref{fig:n_scaling}; Table~\ref{tab:selection}).
8	This gap decomposes into a definitional layer---four instance-level signals assign identical scores to all candidates---and an empirical one: LP, the only per-sample signal, also fails through within-instance compression (\S\ref{sec:selection_gap}).
9	A hidden-state probe confirms models encode entity quality internally (AUROC $0.63$\textendash$0.88$; \S\ref{sec:mechanistic}), exposing an \textit{introspection boundary} \cite{huang2024large}.
10	A \textit{diagnostic framework}---co-occurring conditions that jointly characterize the gap, not a sequential filter---localizes the failure to degeneracy ($12$--$68$\%) and signal alignment collapse ($\alpha{\to}0$), which jointly prevent selection
…[truncated 2595 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 4018 · 2026-05-22T12:42:21.129408+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
  }
}
```

</details>

---


### Tool result

_source line 4019 · 2026-05-22T12:42:21.781730+00:00_

1	\section{Experiments}\label{sec:experiments}
2	
3	\subsection{Experimental Setup}\label{sec:setup}
4	
5	\paragraph{Datasets.}
6	We evaluate on four English NER benchmarks spanning a difficulty gradient.
7	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed (${\approx}$65\% F1).
8	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:selection_gap}).
9	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control.
10	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 51\% zero F1) probes the signal-collapse boundary.
11	
12	\paragraph{Models and sampling.}
13	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others; Appendix~\ref{app:epoch_confound}).
14	$N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}; $N {\in} \{16, 32, 64\}$ for scaling (Figure~\ref{fig:n_scaling}; Appendix~\ref{app:n_scaling}).
15	
16	\begin{figure}[t]
17	\centering
18	\includegraphics[width=\columnwidth]{figures/fig_n_scaling_mv.pdf}
19	\caption{MV $\Delta$F1 vs.\ $\log_2 N$ across three datasets (Qwen3-8B FT, seed${=}42$). Dotted gray: $\Delta{=}0$. Gains are dataset-dependent: persistently negative on Few-NERD, near zero on SciERC at higher $N$, marginally positive on CoNLL ($+0.6$\,pp at $N{=}64$).}
20	\label{fig:n_scaling}
21	\end{figure}
22	
23	%% ============================================================
24	\subsection{Quality Estimation Results}\label{sec:qe_results}
25	
26	\begin{table*}[t]
27	\centering
28	\small
29	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed $
…[truncated 7285 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 4020 · 2026-05-22T12:42:22.785214+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 4021 · 2026-05-22T12:42:22.938883+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 4022 · 2026-05-22T12:42:27.507814+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 4023 · 2026-05-22T12:42:28.460910+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 4024 · 2026-05-22T12:42:28.611781+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
  }
}
```

</details>

---


### Tool result

_source line 4025 · 2026-05-22T12:42:28.762604+00:00_

1	\section{Diagnostic Framework}\label{sec:method}
2	
3	Our analysis is observational: we characterize statistical associations between agreement signals and output quality without claiming causal mechanisms.
4	
5	\subsection{Problem Formulation}\label{sec:formulation}
6	
7	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
8	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
9	This distinction is consequential: 4 of 5 signals are instance-level aggregates assigning identical scores to all $N$ candidates.
10	Only LP carries per-sample discriminative power: ensemble optimization assigns LP mean weight $0.78$, with structural signals receiving zero weight (Appendix~\ref{app:supervised_combination}).
11	When LP fails---as in few-shot regimes where LP $\rho{\to}0$ (\S\ref{sec:scaling})---no alternative per-sample signal exists.
12	
13	We define the \textbf{capability ceiling} as the practical performance upper bound achievable through self-consistency at realistic sample budgets ($N{\leq}16$), beyond which diminishing returns render further scaling impractical.
14	
15	\subsection{Confidence Signals}\label{sec:signals}
16	
17	Entity matching uses exact span and type match.
18	We distinguish two signal families: four \textit{agreement signals} computed across samples---\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK])---and log-probability [LP] as the sole \textit{model-internal} signal, derived from generation probabilities and providing per-sample discrimination.
19	
20	\paragraph{Log-probability (per-sample).}
21	$c_{\text{lp}}(y_i)
…[truncated 2151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 4026 · 2026-05-22T12:42:28.863412+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex"
  }
}
```

</details>

---


### Tool result

_source line 4027 · 2026-05-22T12:42:28.863836+00:00_

1	\section{How Self-Verification Fails}\label{sec:mechanistic}
2	
3	The diagnostic framework (\S\ref{sec:method}) identifies \textit{where} self-consistency fails; this section probes \textit{why} by testing whether models can self-verify at the entity level.
4	We evaluate self-verification and diagnostic probes on Qwen2.5-7B\footnote{ESJ, MRSC, and LSC use Qwen2.5-7B-Instruct (zero-shot self-verification capability) rather than the fine-tuned Qwen3-8B used in the main experiments. Conclusion direction is consistent with the main experiments' negative results across all fine-tuned selection strategies. The pattern---selection failure across all signals---is independently confirmed in the Qwen3-8B main experiments, making the introspection boundary a model-independent finding within our tested scale. Probe conclusions are limited to the Qwen2.5 architecture; linear probes may underestimate representational capacity (nonlinear alternatives are left to future work).} fine-tuned for NER on Few-NERD ($N{=}8$, seed 42; full results in Appendix~\ref{app:self_verification}).
5	
6	\paragraph{Entity Self-Judgment (ESJ).}
7	For each extracted entity, we prompt the generating model: ``Is [\textit{entity}] a [\textit{type}] entity in this sentence?''
8	Entity-level AUROC is $0.512$---indistinguishable from chance---with P(yes$|$correct)${=}0.500$ and P(yes$|$incorrect)${=}0.500$.
9	ESJ-weighted construction degrades F1 to $0.711$ (vs.\ greedy $0.794$).
10	
11	\paragraph{Multi-Round Self-Consistency (MRSC).}
12	Following iterative self-refinement \cite{madaan2023selfrefine}, we re-prompt on disputed entities (agreement ${<}0.6$) with focused verification; P(yes) separation between gold and non-gold entities is $0.0006$ ($0.5003$ vs.\ $0.4997$).
13	MRSC best F1 ($0.763$) falls below greedy.
14	
15	\paragraph{Latent Self-Consistency (LSC).}
16	Mean-pooled final-layer hidden states ($d{=}3584$) provide per-sample latent representations.
17	Centroid selection ($0.759$) underperforms 
…[truncated 1663 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 4028 · 2026-05-22T12:42:36.006769+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
  }
}
```

</details>

---


### Tool result

_source line 4029 · 2026-05-22T12:42:36.027062+00:00_

1	\section{Where Single-Signal Selection Fails}\label{sec:selection_gap}
2	
3	\paragraph{Definitional vs.\ empirical.}
4	We decompose the correlation-selection gap into two layers.
5	The first is structural: four of five signals are instance-level aggregates that assign identical scores to all $N$ candidates from a given input (\S\ref{sec:formulation}), so they estimate quality across inputs but cannot rank candidates within an instance---selection failure is a design property, not an empirical finding.
6	The second layer is empirical and constitutes the core diagnostic: LP---the only per-sample signal---suffers compression under constrained decoding, with 60\% of SciERC instances showing within-instance LP range below 0.041 nats (Appendix~\ref{app:logprob_ties}), effectively eliminating the variation needed for sample discrimination. This compression is model-intrinsic: free-form decoding yields nearly identical LP distributions (within-instance std ratio $0.97{\times}$; Appendix~\ref{app:freeform_ablation}). Even where LP varies, selection gains depend on LP-quality alignment rather than degeneracy alone.
7	Cross-instance $\rho$ (Table~\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Best-of-$N$ selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$). Selection signals: 2-seed mean${\pm}\sigma$; baselines: 3-seed (Oracle${=}0.781$, Greedy${=}0.667$). LP is per-sample; others use consensus-proximity. $^\dagger$One score per input.}
13	\label{tab:selection}
14	\begin{tabular}{lcc}
15	\toprule
16	Method & NER F1 & $p$ \\
17	\midrule
18	Oracle & $0.775 \pm 0.001$ & --- \\
19	Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
20	\midrule
21	LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
22	SJ           & $0.646 \pm 0.002$ & .67 \\
23	FK      
…[truncated 2439 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 20
}
```

</details>

---


### Tool call

_source line 4030 · 2026-05-22T12:42:36.078463+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
  }
}
```

</details>

---


### Tool result

_source line 4031 · 2026-05-22T12:42:36.078819+00:00_

1	\section{Adaptive Methods}\label{sec:adaptive}
2	
3	Since instance-level selection fails (\S\ref{sec:selection_gap}), we present approaches that extract value from multi-sample generation beyond single-signal sample ranking.
4	Table~\ref{tab:method_summary} summarizes all 9 method categories evaluated; only cross-model ensembles yield an unconditional positive result.
5	
6	\begin{table}[t]
7	\centering
8	\small
9	\caption{Summary of 9 method categories tested (including MV baseline, LP selection, and cross-model ensemble beyond the seven verification methods in \S\ref{sec:mechanistic}--\S\ref{sec:adaptive}). $\Delta$F1 vs.\ greedy; dataset in parentheses. Full coverage in Appendix~\ref{app:method_coverage}.}
10	\label{tab:method_summary}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{@{}llrl@{}}
13	\toprule
14	Category & Method & $\Delta$F1 / metric & § \\
15	\midrule
16	Freq.\ voting & MV & baseline & \ref{sec:prescriptive} \\
17	LP selection & Best-of-$N$ (LP) & $+1.39$\,pp (FN)$^\dagger$ & \ref{sec:selection_gap} \\
18	Self-verif.\ (prompt) & ESJ & AUROC $0.51$ & \ref{sec:mechanistic} \\
19	Multi-round refine. & MRSC & $-3.1$\,pp (FN) & \ref{sec:mechanistic} \\
20	Latent aggregation & LSC & $-3.5$\,pp (FN) & \ref{sec:mechanistic} \\
21	Adaptive gating & DALS & $+0.71$\,pp (SciERC)$^\ddagger$ & App.~\ref{app:dals} \\
22	Supervised verifier & LGB & $+0.30$\,pp (OOF) & \ref{sec:verifier} \\
23	Sup.\ combination & LR/MLP/RF & $-0.4$ to $-3.1$\,pp & App.~\ref{app:supervised_combination} \\
24	Cross-model & Qwen$+$LLaMA & $\mathbf{+0.42}$\,pp (FN) & \ref{sec:cross_model} \\
25	\bottomrule
26	\end{tabular}}
27	{\footnotesize $^\dagger$Few-NERD only; SciERC $+0.2$\,pp ($p{=}0.29$). $^\ddagger$Seed-sensitive ($\sigma{=}0.48$\,pp).}
28	\end{table}
29	
30	\subsection{Cross-Model Self-Consistency}\label{sec:cross_model}
31	
32	Mixing samples from architecturally distinct models can partially bypass within-model degeneracy.
33	Combining 4 samples each from Qwen3-8B and
…[truncated 764 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 4032 · 2026-05-22T12:42:36.179385+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
  }
}
```

</details>

---


### Tool result

_source line 4033 · 2026-05-22T12:42:36.179808+00:00_

1	\section{Threshold Regime Analysis}\label{sec:theory_scaling}
2	
3	\subsection{Entity Construction as MBR Decoding}\label{sec:mbr_theory}
4	
5	Entity-level construction selects $\hat{y}_{\textup{MBR}} = \{e \in E_\cup : \hat{p}(e) > \alpha/(\alpha{+}1)\}$ under balanced set-overlap utility; $\alpha{=}1$ recovers majority vote (Proposition~\ref{prop:construction_mbr}; Table~\ref{tab:entity_construction}; Appendix~\ref{app:mbr_proof}).
6	Signal-derived weights $w_i$ yield quality-weighted MBR: $\hat{p}_w(e) = \sum_{i} w_i \, \mathbf{1}[e {\in} y_i] / \sum_{i} w_i$; weighting improves when $w_i$ correlates with instance quality but degrades otherwise (LP on SciERC: $\rho{\approx}0.2$; \S\ref{sec:prescriptive}).
7	We select $\varepsilon{=}0.05$ at the elbow of the compression curve, where LP-best selection advantage transitions from $+1.5$\,pp (compressed) to $+4.6$\,pp (non-compressed; Appendix~\ref{app:fewnerd_epsilon}).
8	
9	\subsection{Scaling and Inverse Scaling}\label{sec:scaling}
10	
11	Oracle F1 follows $F_1(N) = a - b \cdot N^{-c}$ ($R^2 > 0.999$; Figure~\ref{fig:oracle_scaling}): Few-NERD ($c{\approx}0.61$) scales comparably to reasoning tasks \cite{brown2024monkeys}, SciERC converges more slowly ($c{\approx}0.35$), yet confidence-based aggregation recovers ${<}1$\,pp---a persistent gap.
12	The gap persists across scales and families: scaling from 8B to 14B FT increases oracle headroom ($+1.2$\,pp) with minimal greedy gain ($+0.9$\,pp), and GPT-5.5 (200 Few-NERD instances, zero-shot) exhibits the same pattern---50\% degeneracy, SJ $\rho{=}0.346$, MV $+1.4$\,pp yet 6.8\,pp oracle headroom unrealized.\footnote{Of the 10.1\% of GPT-5.5 samples producing empty entity sets, 88\% correspond to gold-empty instances; true parse failures affect only 1.2\% of samples (19/1{,}600) and shift all reported metrics by ${<}0.5$\,pp. See Appendix~\ref{app:frontier_sc}.}
13	Degeneracy is model-family-dependent rather than scale-dependent (Qwen2.5: $31.7$--$46.2$\% vs.\ Qwen3:
…[truncated 3691 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 4034 · 2026-05-22T12:42:36.230256+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 4035 · 2026-05-22T12:42:36.283952+00:00_

1	\section{Discussion and Conclusion}\label{sec:discussion}\label{sec:selection_method}\label{sec:conclusion}
2	
3	\paragraph{Why test-time scaling fails for NER.}
4	For discrete-answer reasoning, sample diversity reflects diverse reasoning paths; for NER, degeneracy ($12$--$68$\%) eliminates candidate diversity while signal alignment collapse ($\alpha{\to}0$) prevents ranking.
5	We quantify how the well-known capability-diversity tradeoff \cite{yun2025price} manifests in NER, observing this across model families (5.5--74\%; Table~\ref{tab:frontier_sc_cross}) and scales (4B--72B; \S\ref{sec:scaling}).
6	Free-form decoding confirms this is model-intrinsic (within-instance LP std ratio $0.97{\times}$; \S\ref{sec:selection_gap}).
7	
8	\paragraph{Relation to prior work.}
9	Our framework differs from \citet{yao2026consistency} in granularity (instance- vs.\ task-level), mechanism (causal decomposition vs.\ aggregate statistics), and actionability (pre-deployment diagnostics; \S\ref{sec:related}).
10	
11	\paragraph{Practical implications.}
12	Measuring degeneracy and LP-F1 alignment at $N{=}8$ sufficed to predict scaling returns on our benchmarks: degeneracy ${>}50$\% indicates repeated sampling is unlikely to help; below $20$\%, LP-F1 correlation assesses viability ($\theta_{\text{crit}}{=}0.70$, stable across four NER datasets). Whether the decomposition generalizes beyond NER requires independent investigation.
13	
14	\paragraph{Conclusion.}
15	The diagnostic framework---localizing failure to degeneracy and signal alignment collapse---is our primary contribution; extensions to RE and SQL are exploratory, and whether the capability-diversity tension generalizes beyond NER remains open.
16	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 4036 · 2026-05-22T12:42:42.340978+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 4037 · 2026-05-22T12:42:43.044173+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Test-time compute scaling.}
4	Self-consistency \cite{wang2023selfconsistency} and best-of-$N$ \cite{snell2025scaling, brown2024monkeys} drive large gains on reasoning and code \cite{chen2021codex}.
5	Reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty}, BoN scaling laws \cite{gao2023scaling}, and trained verifiers \cite{cobbe2021verifiers, lightman2024verify} target discrete-answer settings; NER requires different aggregation because degeneracy operates at the entity-set level.
6	
7	\paragraph{SC failure modes.}
8	\citet{chen2023twofailures} identify SC failures where consistent outputs are wrong; free-form \cite{chen2024usc} and atomic \cite{thirukovalluru2024atomic} SC variants face limits where sub-output agreement does not yield selection gain (\S\ref{sec:selection_gap}).
9	
10	\paragraph{Consistency for structured IE.}
11	\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE at the task level ($\rho$ up to 0.47); we extend this to instance-level analysis, diagnosing \textit{why} correlation does not transfer to selection gains. Key distinctions: (1)~granularity---task-level $\rho$ masks instance-level degeneracy; (2)~mechanism---we decompose failure into degeneracy and LP compression; (3)~actionability---pre-deployment diagnostics (measure degeneracy at $N{=}8$) that task-level correlation cannot provide.
12	\citet{xie2023zeroshot} propose entity voting for zero-shot NER and \citet{xie2024selfimproving} report positive SC where zero-shot diversity is high.
13	\paragraph{Uncertainty estimation and MBR.}
14	Our selection instantiates MBR decoding \cite{eikema2022sampling, denero2009fast}; despite success in translation \cite{freitag2022high} and code \cite{jinnai2024mbr}, all variants fail due to instance degeneracy (Appendix~\ref{app:mbr_connection}).
15	\citet{eikema2025structured} find MBR utilities degrade on structured outputs; our framework loca
…[truncated 1513 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 4038 · 2026-05-22T12:42:43.144922+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 4039 · 2026-05-22T12:42:43.145325+00:00_

1	Our primary evidence is from NER (four English datasets, 7--14B fine-tuned); the RE extension ($n{=}397$, single dataset) and SQL pilot ($n{=}196$) are exploratory. SciERC results are validated across three training seeds ($n{=}529$ test instances; $\Delta_{\text{SC}}{=}{-}0.74{\pm}0.57$\,pp, consistent negative). Frontier models exhibit markedly different degeneracy profiles (5.5--74\%; Table~\ref{tab:frontier_sc_cross}), suggesting findings from fine-tuned open-weight models may not fully generalize to proprietary systems.
2	Our framework is diagnostic, not causal: stages resist decomposition into independent effects ($R^2{<}0$; \S\ref{sec:selection_gap}). Under global Holm--Bonferroni ($k{=}57$), the most liberal core claim reaches $p_{\text{HB}}{=}0.055$; under BH FDR, $19/57$ tests are significant at FDR${<}0.05$ including $6/10$ construction comparisons (Appendix~\ref{app:holm}).
3	We evaluate at $N{\in}\{2,\ldots,64\}$; entity-level construction requires $N{\times}$ inference cost for modest gains ($+1$--$1.4$\,pp). We use a single prompt template per task; prompt variations may affect entity recall, degeneracy, and LP distributions.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 4040 · 2026-05-22T12:42:43.396520+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "120"
  }
}
```

</details>

---


### Tool result

_source line 4041 · 2026-05-22T12:42:43.397193+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & $
…[truncated 6378 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 4042 · 2026-05-22T12:42:49.269858+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"*.yaml\" -o -name \"*.yml\" | head -20",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"*.yaml\" -o -name \"*.yml\" | head -20",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 4043 · 2026-05-22T12:42:50.173738+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T225436/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_202
…[truncated 644 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 4044 · 2026-05-22T12:42:50.224429+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "120",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "120",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 4045 · 2026-05-22T12:42:50.325392+00:00_

120	The higher FK means on CoNLL ($0.720$--$0.927$) vs.\ SciERC ($0.402$) mirror the difficulty gradient observed in the main quality estimation results.
121	
122	\section{Calibration Analysis}\label{app:calibration}
123	
124	\begin{figure*}[t]
125	\centering
126	\includegraphics[width=\textwidth]{fig_reliability}
127	\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), RE calibration remains challenging for compound extraction tasks.}
128	\label{fig:reliability}
129	\end{figure*}
130	
131	Reliability diagrams use 10 equal-width bins.
132	NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.
133	
134	\section{Additional Analyses}\label{app:additional}
135	
136	\begin{figure*}[t]
137	\centering
138	\includegraphics[width=\textwidth]{fig_signal_heatmap}
139	\caption{Quality estimation heatmap (Spearman $\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while LP RE collapses to near-zero ($\rho{=}0.011$).}
140	\label{fig:signal_heatmap}
141	\end{figure*}
142	
143	\paragraph{Per-relation diagnostic.}
144	RE signal degradation is relation-specific.
145	\textsc{Feature-Of} has near-zero correlation ($\rho{=}0.004$), while \textsc{Hyponym-Of} achieves $\rho{=}0.646$.
146	The primary bottleneck is entity span errors, which account for 55.5\% o
…[truncated 15615 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 4046 · 2026-05-22T12:42:55.096307+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1 -maxdepth 2 -name \"config.yaml\" -o -name \"project_config.yaml\" | head -10",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1 -maxdepth 2 -name \"config.yaml\" -o -name \"project_config.yaml\" | head -10",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 4047 · 2026-05-22T12:42:55.197068+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 4048 · 2026-05-22T12:42:59.011210+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1 -maxdepth 3 -name \"*.yaml\" | grep -i config | head -10",
  "description": "Find config yaml files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1 -maxdepth 3 -name \"*.yaml\" | grep -i config | head -10",
    "description": "Find config yaml files"
  }
}
```

</details>

---


### Tool result

_source line 4049 · 2026-05-22T12:42:59.112059+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/crons.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/projects/struct_self_consist_ie.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/venue_rules/corl-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/venue_rules/emnlp-2026.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/venue_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/resources.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/pending_approval_notifications.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 4050 · 2026-05-22T12:43:02.833292+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/projects/struct_self_consist_ie.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/projects/struct_self_consist_ie.yaml"
  }
}
```

</details>

---


### Tool result

_source line 4051 · 2026-05-22T12:43:02.868315+00:00_

1	execution:
2	  account: root
3	  gpu_constraint:
4	    autodl-5090:
5	    - cuda:0
6	    - cuda:1
7	    - cuda:2
8	    - cuda:3
9	    autodl-5090-c:
10	    - cuda:0
11	    - cuda:1
12	    - cuda:2
13	    - cuda:3
14	  gpu_ids:
15	  - cuda:0
16	  - cuda:1
17	  - cuda:2
18	  - cuda:3
19	  project_path: /root/autodl-tmp/struct_self_consist_ie
20	  servers:
21	  - autodl-5090
22	  - autodl-5090-c
23	feishu:
24	  chat_id: oc_1b56445332d8ca2b4964b30f300f0e00
25	  check_references: false
26	  operational_chat_id: oc_523053f5a039428dc15666668fa856b3
27	  review_mode: fresh
28	  review_paper_path: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
29	  review_paper_pdf_path: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_38/submitted.pdf
30	  review_round: 38
31	  review_supplementary_paths: ''
32	  submission_chat_id: oc_3897c2857f11615119e277e820eae311
33	project:
34	  created_at: '2026-05-14T04:20:56.331Z'
35	  description: When Does Test-Time Scaling Help Structured Prediction? Adaptive Structural
36	    Self-Consistency with Learned Aggregation
37	  name: struct_self_consist_ie
38	  phase: research
39	  source_idea_id: idea_010
40	venue: emnlp-2026
41	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 35
}
```

</details>

---


### Tool call

_source line 4052 · 2026-05-22T12:43:06.965889+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/venue_rules/emnlp-2026.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/config/venue_rules/emnlp-2026.yaml"
  }
}
```

</details>

---


### Tool result

_source line 4053 · 2026-05-22T12:43:07.001563+00:00_

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
11	  - created_at: '2026-05-19T12:23:13Z'
12	    id: bd0516
13	    text: EMNLP 2026 restricts long paper submissions to a strict 8-page limit for
14	      main text, with unlimited space for references. Mandatory limitations and optional
15	      ethical considerations do not count towards this page limit, provided they do
16	      not contain excessive additional content.
17	  writing:
18	  - created_at: '2026-05-21T06:49:14Z'
19	    id: 2468a8
20	    text: Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长
21	  - created_at: '2026-05-21T17:05:54Z'
22	    id: 0b1d8f
23	    text: ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面
24	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 35
}
```

</details>

---


### Tool call

_source line 4054 · 2026-05-22T12:43:11.394471+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 4055 · 2026-05-22T12:43:11.582301+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 187
}
```

</details>

---


### Tool call

_source line 4056 · 2026-05-22T12:43:14.617191+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 4057 · 2026-05-22T12:43:14.668169+00:00_

issues:
# ===== ROUND 37 CRITICAL / MUST-FIX =====
- id: R37-MF1
  summary: "Holm-Bonferroni correction per-family 划分缺乏 pre-registration，核心 LP claim 在全局校正下不显著"
  category: method
  severity: critical
  status: in_progress
  first_raised_round: 34
  last_seen_round: 37
  mentions:
    - round: 36
      reviewers: [1, 2]
      note: "R36-MF2: 需在 §7 正文讨论。标记 resolved round 37。"
    - round: 37
      reviewers: [1, 2]
      note: "两位 Reviewer 均列为 CRITICAL [AGREE]。§7 已讨论 p_adj=0.055 但 per-family justification 仍不充分——缺乏 pre-registration 证据，k=57→k=10 的切换构成 post-hoc adjustment。正文引用 p_adj=0.006 而全局 0.055 仅在 Appendix/Limitations。"
  action_items:
    - round: 37
      action: "正文 §7 透明报告两种 correction 结果；提供 a priori family 划分理由或承认 post-hoc；将 LP selection 描述为 'marginally significant under global correction'"
      assigned_to: paper_agent
      status: in_progress
  resolution: "§7 正文增加两层 defense：per-family k=10 p_adj=0.006 + global k=57 p_adj=0.055，明确承认 'not pre-registered'，global figure 作为 conservative bound"
  resolution_round: null

- id: R37-MF2
  summary: "'Simultaneously necessary conditions' 的 claim 超出 correlational co-occurrence 证据"
  category: framing
  severity: critical
  status: in_progress
  first_raised_round: 37
  last_seen_round: 37
  mentions:
    - round: 37
      reviewers: [1, 2]
      note: "两位 Reviewer 均 AGREE。Bound (1-D)·G_nd·α 只 capture 3-12% actual gains。'necessary' 要求移除条件后 gains 总是恢复，但 cross-model ensemble 只 partially bypasses。证据支撑 co-occurrence 而非 logical necessity。"
  action_items:
    - round: 37
      action: "'simultaneously necessary conditions' → 'two co-occurring factors that characterize the gap'；讨论 bound looseness 对 necessity claim 的影响"
      assigned_to: paper_agent
      status: in_progress
  resolution: "全文替换为 'co-occurring conditions that jointly characterize the gap, not a sequential filter'（intro, single_signal, abstract）"
  resolution_round: null

- id: R37-MF3
  summary: "Diagnostic framework 无预测力（R²<0）与 title/abstract 暗示预测性的张力"
  cate
…[truncated 11318 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4058 · 2026-05-22T12:43:42.282171+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: Venue 调研 + 资料检查', 'status': 'completed', 'activeForm': '完成 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 视觉审查派发', 'status': 'in_progress', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: Venue 调研 + 资料检查', 'status': 'completed', 'activeForm': '完成 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 视觉审查派发', 'status': 'in_progress', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 4059 · 2026-05-22T12:43:42.282925+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 4060 · 2026-05-22T12:43:43.838859+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "struct_self_consist_ie",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 4061 · 2026-05-22T12:43:50.090865+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 6252
}
```

</details>

---


### Tool call

_source line 4062 · 2026-05-22T12:43:57.939537+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: Venue 调研 + 资料检查', 'status': 'completed', 'activeForm': '完成 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 视觉审查派发', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: Venue 调研 + 资料检查', 'status': 'completed', 'activeForm': '完成 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 视觉审查派发', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 4063 · 2026-05-22T12:43:57.940009+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 4064 · 2026-05-22T12:44:26.547732+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**审查。\n\n## 论文信息\n- **标题**: When Does Test-Time Scaling Fail? Boundary Conditions for Named Entity Recognition\n- **Venue**: EMNLP 2026 Long Paper (ARR May cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL LaTeX 模板, 正文 8 页, 参考文献不限, Limitations 必需 (≤1 页不计入), Ethics 可选不计入, Double-blind\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_38/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. Diagnostic Framework 定义与逻辑\n- §2 的 problem formulation 是否 self-consistent？per-sample vs instance-level signal 的区分是否严谨？\n- \"Co-occurring conditions\" 的表述是否有足够的定义精度？degeneracy + signal alignment collapse 的 co-occurrence 是否有统计刻画（不仅是例示）？\n- Degeneracy decomposition bound $(1-D) \\cdot G_{\\text{nd}} \\cdot \\alpha$ 只 capture 3-12% actual gains——bound 的 looseness 是否在正文充分讨论？这是否削弱了 framework 的诊断价值？\n\n### 2. 统计检验与 Multiple Testing\n- Holm-Bonferroni correction: per-family (k=10) vs global (k=57) 的选择——per-family 划分是否 pre-registered？正文对两种 correction 结果的报告是否透明？\n- Few-NERD LP selection p_adj=0.006 (k=10) vs p_adj=0.055 (k=57)——核心 claim 对 correction 选择的敏感性是否 acknowledged？\n- Power analysis: SciERC n=529 的 MDE，Few-NERD 3-seed 统计，RE n=397 power 是否充分？\n- Bootstrap CI、permutation test 的使用是否 appropriate？\n\n### 3. 实验 Coverage 与 Confounds\n- 模型多样性：主要 Qwen3-8B + LLaMA-3.1-8B (8B 级别)，4B/14B/72B/GPT-5.5 仅 ablation/pilot——generalization claim 是否与证据匹配？\n- Few-NERD 3-epoch vs 5-epoch confound: degeneracy 13%→31%, LP Δ +1.39→+0.12pp——这是否动摇了 Few-NERD 作为 \"positive contrast\" 的可信度？\n- Constrained decoding: free-form ablation 仅 CoNLL（LP std ratio 0.97×）——是否需要更多 dataset 验证？\n- RE extension (n=397, single dataset) 和 SQL pilot (n=196)——证据强度是否与呈现匹配？\n\n### 4. Entity Construction 与 MBR 连接\n- θ=2/N 的选择理据？θ_crit=0.70 在多 dataset/model 上的稳定性验证？\n- Entity-level construction as MBR 的理论推导是否 tight？Proposition 1 的简化假设是否 acknowledged？\n- Inverse scaling (40/58 transitions) 的严重性——是否意味着 entity construction 方法不可靠？\n\n### 5. Hidden-State Probe\n- Qwen2.5-7B vs Qwen3-8B 差异——probe 结论能否迁移？\n- GroupKFold CV 设计是否防止了 entity-level leakage？\n- LODO transfer drops (0.56-0.67)——\"dataset-specific\" 结论是否有替代解释？\n\n请按 ARR Overall Assessment 评分标准给出评分（1-5 分制）和置信度（1-5）。输出格式：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Nit) → Questions → Missing References → Overall Assessment。",
  "project": "struct_self_consist_ie",
  "chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责**方法严谨性 + 实验设计**审查。\n\n## 论文信息\n- **标题**: When Does Test-Time Scaling Fail? Boundary Conditions for Named Entity Recognition\n- **Venue**: EMNLP 2026 Long Paper (ARR May cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL LaTeX 模板, 正文 8 页, 参考文献不限, Limitations 必需 (≤1 页不计入), Ethics 可选不计入, Double-blind\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_38/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. Diagnostic Framework 定义与逻辑\n- §2 的 problem formulation 是否 self-consistent？per-sample vs instance-level signal 的区分是否严谨？\n- \"Co-occurring conditions\" 的表述是否有足够的定义精度？degeneracy + signal alignment collapse 的 co-occurrence 是否有统计刻画（不仅是例示）？\n- Degeneracy decomposition bound $(1-D) \\cdot G_{\\text{nd}} \\cdot \\alpha$ 只 capture 3-12% actual gains——bound 的 looseness 是否在正文充分讨论？这是否削弱了 framework 的诊断价值？\n\n### 2. 统计检验与 Multiple Testing\n- Holm-Bonferroni correction: per-family (k=10) vs global (k=57) 的选择——per-family 划分是否 pre-registered？正文对两种 correction 结果的报告是否透明？\n- Few-NERD LP selection p_adj=0.006 (k=10) vs p_adj=0.055 (k=57)——核心 claim 对 correction 选择的敏感性是否 acknowledged？\n- Power analysis: SciERC n=529 的 MDE，Few-NERD 3-seed 统计，RE n=397 power 是否充分？\n- Bootstrap CI、permutation test 的使用是否 appropriate？\n\n### 3. 实验 Coverage 与 Confounds\n- 模型多样性：主要 Qwen3-8B + LLaMA-3.1-8B (8B 级别)，4B/14B/72B/GPT-5.5 仅 ablation/pilot——generalization claim 是否与证据匹配？\n- Few-NERD 3-epoch vs 5-epoch confound: degeneracy 13%→31%, LP Δ +1.39→+0.12pp——这是否动摇了 Few-NERD 作为 \"positive contrast\" 的可信度？\n- Constrained decoding: free-form ablation 仅 CoNLL（LP std ratio 0.97×）——是否需要更多 dataset 验证？\n- RE extension (n=397, single dataset) 和 SQL pilot (n=196)——证据强度是否与呈现匹配？\n\n### 4. Entity Construction 与 MBR 连接\n- θ=2/N 的选择理据？θ_crit=0.70 在多 dataset/model 上的稳定性验证？\n- Entity-level construction as MBR 的理论推导是否 tight？Proposition 1 的简化假设是否 acknowledged？\n- Inverse scaling (40/58 transitions) 的严重性——是否意味着 entity construction 方法不可靠？\n\n### 5. Hidden-State Probe\n- Qwen2.5-7B vs Qwen3-8B 差异——probe 结论能否迁移？\n- GroupKFold CV 设计是否防止了 entity-level leakage？\n- LODO transfer drops (0.56-0.67)——\"dataset-specific\" 结论是否有替代解释？\n\n请按 ARR Overall Assessment 评分标准给出评分（1-5 分制）和置信度（1-5）。输出格式：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Nit) → Questions → Missing References → Overall Assessment。",
    "project": "struct_self_consist_ie",
    "chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 4065 · 2026-05-22T12:44:49.351359+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22803
}
```

</details>

---


### Tool call

_source line 4066 · 2026-05-22T12:44:49.804902+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性 + 论文完整性 + 写作质量**审查。\n\n## 论文信息\n- **标题**: When Does Test-Time Scaling Fail? Boundary Conditions for Named Entity Recognition\n- **Venue**: EMNLP 2026 Long Paper (ARR May cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL LaTeX 模板, 正文 8 页, 参考文献不限, Limitations 必需 (≤1 页不计入), Ethics 可选不计入, Double-blind\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_38/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献评估\n- 与 Yao et al. (2026) 的增量新颖性：instance-level 分析 vs task-level 分析——能否清晰区分？是否质变还是量变？\n- \"Correlation-selection gap\" 是本文的核心发现——这个概念是否足够 novel？是否已有 MBR/BoN 文献暗含类似观察？\n- \"Capability-diversity tension\" 与 Yun & Kim (2025) \"diversity collapse\" 的关系——本文贡献是新概念还是已知现象的量化？\n- Diagnostic framework 的实用价值——practitioner 真的会用 degeneracy + α 来决定是否 scale？\n\n### 2. Claim-Evidence 匹配\n- Abstract/Introduction 中的 claim 是否每条都有对应的实验支撑？特别关注：\n  - \"cross-task exploration confirms task-specific failure modes\"——RE n=397, SQL n=196 够不够？\n  - \"framework guides practitioners on what to measure\"——有无用户研究或 case study？\n  - \"exploratory entity-level construction partially bypasses the bottleneck\"——global Holm p=0.055\n- Title \"Boundary Conditions\" 的含义——是描述性的 diagnostic conditions 还是暗示 necessary/sufficient conditions？\n- \"Diagnostic rather than predictive\" 的定位是否贯穿全文？是否有段落暗含预测性？\n\n### 3. Related Work 完整性\n- 2024-2025 年的 conformal prediction for structured output 是否覆盖？\n- Token-level uncertainty estimation 文献？\n- GPT-NER / LLM-based NER self-verification 相关工作？\n- MBR decoding for structured prediction 最新进展？\n- Eikema et al. (2025) structured MBR 是否充分讨论？\n\n### 4. 论文结构与写作质量\n- Abstract 信息密度：数字数量是否合适？narrative flow 是否清晰？\n- §1 Introduction 的 story arc——从 gap identification → diagnostic → bypass 的逻辑是否顺畅？\n- §2 Diagnostic Framework 放在 experiments 之前——是否影响可读性？\n- §3 Mechanistic Analysis 使用 Qwen2.5-7B 而主实验用 Qwen3-8B——读者困惑度？\n- §8 Discussion/Conclusion 长度和深度——generalizability、open questions、practical guidance 是否充分？\n- 术语一致性：degeneracy / output convergence / convergence 是否统一？\n- Limitations 段落长度和覆盖面——是否符合 ARR 要求？\n\n### 5. 格式合规（EMNLP 2026 / ARR）\n- 正文是否≤8 页？\n- Limitations section 是否在 references 之前？长度是否合理？\n- Ethics statement 存在且合理？\n- 匿名合规？是否有 self-citation 泄露身份？\n- \"Code and data will be released upon acceptance at [anonymized URL]\"——是否合规？\n- References 格式是否符合 ACL style？\n\n请按 ARR Overall Assessment 评分标准给出评分（1-5 分制）和置信度（1-5）。输出格式：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Nit) → Questions → Missing References → Overall Assessment。",
  "project": "struct_self_consist_ie",
  "chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责**新颖性 + 论文完整性 + 写作质量**审查。\n\n## 论文信息\n- **标题**: When Does Test-Time Scaling Fail? Boundary Conditions for Named Entity Recognition\n- **Venue**: EMNLP 2026 Long Paper (ARR May cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL LaTeX 模板, 正文 8 页, 参考文献不限, Limitations 必需 (≤1 页不计入), Ethics 可选不计入, Double-blind\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_38/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献评估\n- 与 Yao et al. (2026) 的增量新颖性：instance-level 分析 vs task-level 分析——能否清晰区分？是否质变还是量变？\n- \"Correlation-selection gap\" 是本文的核心发现——这个概念是否足够 novel？是否已有 MBR/BoN 文献暗含类似观察？\n- \"Capability-diversity tension\" 与 Yun & Kim (2025) \"diversity collapse\" 的关系——本文贡献是新概念还是已知现象的量化？\n- Diagnostic framework 的实用价值——practitioner 真的会用 degeneracy + α 来决定是否 scale？\n\n### 2. Claim-Evidence 匹配\n- Abstract/Introduction 中的 claim 是否每条都有对应的实验支撑？特别关注：\n  - \"cross-task exploration confirms task-specific failure modes\"——RE n=397, SQL n=196 够不够？\n  - \"framework guides practitioners on what to measure\"——有无用户研究或 case study？\n  - \"exploratory entity-level construction partially bypasses the bottleneck\"——global Holm p=0.055\n- Title \"Boundary Conditions\" 的含义——是描述性的 diagnostic conditions 还是暗示 necessary/sufficient conditions？\n- \"Diagnostic rather than predictive\" 的定位是否贯穿全文？是否有段落暗含预测性？\n\n### 3. Related Work 完整性\n- 2024-2025 年的 conformal prediction for structured output 是否覆盖？\n- Token-level uncertainty estimation 文献？\n- GPT-NER / LLM-based NER self-verification 相关工作？\n- MBR decoding for structured prediction 最新进展？\n- Eikema et al. (2025) structured MBR 是否充分讨论？\n\n### 4. 论文结构与写作质量\n- Abstract 信息密度：数字数量是否合适？narrative flow 是否清晰？\n- §1 Introduction 的 story arc——从 gap identification → diagnostic → bypass 的逻辑是否顺畅？\n- §2 Diagnostic Framework 放在 experiments 之前——是否影响可读性？\n- §3 Mechanistic Analysis 使用 Qwen2.5-7B 而主实验用 Qwen3-8B——读者困惑度？\n- §8 Discussion/Conclusion 长度和深度——generalizability、open questions、practical guidance 是否充分？\n- 术语一致性：degeneracy / output convergence / convergence 是否统一？\n- Limitations 段落长度和覆盖面——是否符合 ARR 要求？\n\n### 5. 格式合规（EMNLP 2026 / ARR）\n- 正文是否≤8 页？\n- Limitations section 是否在 references 之前？长度是否合理？\n- Ethics statement 存在且合理？\n- 匿名合规？是否有 self-citation 泄露身份？\n- \"Code and data will be released upon acceptance at [anonymized URL]\"——是否合规？\n- References 格式是否符合 ACL style？\n\n请按 ARR Overall Assessment 评分标准给出评分（1-5 分制）和置信度（1-5）。输出格式：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Nit) → Questions → Missing References → Overall Assessment。",
    "project": "struct_self_consist_ie",
    "chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 4067 · 2026-05-22T12:44:51.646578+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1841
}
```

</details>

---


### Assistant

_source line 4068 · 2026-05-22T12:44:57.326609+00:00_

两位 Reviewer 已分配，等待独立审稿结果返回。

- **Reviewer 1**（方法严谨性 + 实验设计）：已启动
- **Reviewer 2**（新颖性 + 完整性 + 写作）：已启动
- **视觉审查 Agent**：已启动（并行，不阻塞）

审稿结果返回后进入 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 305

## Round 305

2 recorded events


### User

_source line 4069 · 2026-05-22T12:50:49.390887+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见：方法严谨性 + 实验设计

**论文**: When Does Test-Time Scaling Fail? Boundary Conditions for Named Entity Recognition
**Venue**: EMNLP 2026 Long Paper (ARR May cycle)

---

## 总体评分

**Overall Assessment**: 3.5 / 5 (Borderline Conference)
**一句话总结**: 论文提出了一个重要且有时效性的研究问题（test-time scaling 在结构化任务上何时失败），核心发现"correlation-selection gap"有实证支撑，但理论贡献（degeneracy decomposition bound）过于松弛、entity construction 在 69% 配置上出现 inverse scaling、统计检验对 correction 选择敏感，这些问题叠加后削弱了 framework 作为"可操作诊断工具"的 claim。

---

## 官方维度打分（ACL ARR Review Form, Feb 2025+）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 (Acceptable) | 主 claim（correlation-selection gap）有充分支撑；但 degeneracy bound 仅 capture 3-12% actual gains，entity construction inverse scaling 69%，probe 模型不匹配，多项支撑性 claim 的证据强度不足 |
| Excitement | 4/5 (Exciting) | 研究问题高度 timely——TTS 在结构化任务上的 failure mode 此前缺乏系统研究；diagnostic framework 概念上有价值，correlation-selection gap 是 genuine 新发现 |
| Overall Assessment | 3.5 (Borderline Conference) | 详见下方分析 |
| Confidence | 4/5 (Quite sure) | 仔细核查了主要技术 claim、统计检验、bound 推导和实验覆盖度 |
| Reproducibility | 4/5 (Mostly reproducible) | 承诺开源代码/checkpoints，实验细节完备（Appendix k），但部分关键细节需要代码验证 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Degeneracy decomposition bound 过于松弛，削弱 framework 的定量诊断价值

- 具体位置：§6.3, Figure 10, Appendix p.4
- 问题：Bound $(1-D) \cdot G_{\text{nd}} \cdot \alpha$ 仅 capture actual gains 的 3–12%（正文 §6.3 承认："the best signal recovers only 6.8% of the non-degenerate oracle gap on average"）。所有 16 个 positive-gain 配置的 actual/bound ratio 在 Figure 10 右侧面板均远低于 1.0。论文声称 framework "guides practitioners on what to measure before committing to repeated inference"（Abstract），但一个 off by an order of magnitude 的 bound 实际上无法指导实践决策——practitioners 无法据此判断是否值得投入 N 次采样。
- 为什么影响接收：这是论文的核心理论贡献之一（Corollary 1）。如果 bound 不够 tight，则 framework 退化为纯定性描述，与"diagnostic framework"的定位不匹配。
- 建议修改方向：(a) 正文应明确讨论 bound looseness 的来源（entity independence 假设？α 的保守性？），量化每个因素的贡献；(b) 降低对 bound 实践指导意义的 claim——将其定位为"illustrative upper bound"而非"diagnostic tool"；(c) 或者寻找更 tight 的 bound formulation。

**N2** [critical] Entity construction inverse scaling 率 69%（40/58），严重削弱 "bypass" framing

- 具体位置：§6.2, Table 4, Appendix ab.7 (Table 62)
- 问题：Table 4 显示 LP-weighted entity construction 在 4 数据集 × Qwen3-8B 的配置中，从 N=8 到 N=16，正面 LP Δ 仅在 Few-NERD 上（+1.39pp），其余均 negative 或 negligible。§6.2 说 "40 of 58 transitions show inverse scaling"。论文将 entity construction 定位为 "partially bypasses the bottleneck"（§1, Abstract），但 69% 的 inverse scaling 率意味着这个 bypass 在大多数实践场景下是不可靠的。Appendix ab.7 (Table 62) 进一步显示 threshold sensitivity——在很多 θ 值下 CoNLL 和 SciERC 均无正面 gain。
- 为什么影响接收：论文的叙事结构是 "diagnose failure → find bypass"，如果 bypass 本身在多数情况下也失败（甚至 worse than greedy），则整个 prescriptive 价值大打折扣。
- 建议修改方向：(a) 明确将 entity construction 定位为"conditional bypass"——仅在低 degeneracy + LP-F1 alignment 条件下有效，而非笼统的 "bypass"；(b) 在 abstract/introduction 中调低对 entity construction 的 claim，不要暗示它是通用解决方案；(c) 讨论 inverse scaling 的 practical implications——什么时候 practitioners 应该放弃 entity construction？

**N3** [critical] 统计检验对 multiple testing correction 选择敏感，核心 claim 跨越显著性边界

- 具体位置：§7.3, Table 12 (Appendix f), Table 4
- 问题：Few-NERD LP selection 是论文的关键 positive result——"the definitive contrast"（§7.3）。Per-family Holm-Bonferroni (k=10) 给出 p_adj=0.006，但 global correction (k=57) 给出 p_adj=0.055（Table 12, row 5）。论文以 per-family 结果为主要报告（§7.3 说 "Holm p_adj=0.006"），但 per-family 的划分（NER selection, construction, calibration, etc.）未被描述为 pre-registered。当核心 claim 的显著性取决于 correction 方案选择时，这削弱了结论的稳健性。
- 为什么影响接收：Few-NERD 是唯一一个 LP selection 产生实质性正面 gain 的数据集。如果这个结果在更保守的 correction 下不 significant，则论文的"positive contrast"叙事基础动摇。
- 建议修改方向：(a) 在正文 §7.3 同时报告两种 correction 结果，不要只在 Appendix f 报告 global correction；(b) 讨论 per-family partition 的 rationale——是否 pre-specified？如果不是，应承认 researcher degrees of freedom；(c) 考虑用 permutation-based FDR 作为 robustness check。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Hidden-state probe 使用 Qwen2.5-7B，而非主实验模型 Qwen3-8B

- 具体位置：§3, footnote 3 (p.3), Appendix i.3
- 问题：Probe 在 Qwen2.5-7B 上训练（因为 Qwen3-8B 有 thinking tokens 干扰），但主实验全部用 Qwen3-8B 生成样本。Probe AUROC 0.63–0.88 的结论是否迁移到 Qwen3-8B 的 hidden states 是未验证的假设。论文承认 "Probe conclusions are limited to the Qwen2.5 architecture; linear probes may only underestimate representational capacity"（§3），但这个 limitation 对核心 claim 的影响未被充分讨论。
- 建议：(a) 至少做一组 Qwen3-8B post-thinking hidden state 的 probe 实验作为 sanity check；(b) 或更明确地 scope probe 结论为 "Qwen2.5 specific"，不要在 §9 Discussion 中作为 general conclusion 使用。

**W2** [warning] Few-NERD 作为 "positive contrast" 受 under-training confound 影响

- 具体位置：§7.3, §7.5, Appendix ab (Tables 55-56)
- 问题：Few-NERD 3-epoch model 是 LP selection 有效的唯一数据集（+1.39pp），但 Appendix ab Table 55 显示 5-epoch model 上 degeneracy 从 8.8% 升至 20.4%，LP gain 消失。论文将此解读为 "training convergence modulates degeneracy"——这是合理的，但同时意味着 Few-NERD 的 positive result 可能仅在模型 under-trained 时成立。如果实践中模型通常训练至收敛，则 Few-NERD 的 positive contrast 不代表典型使用场景。
- 建议：在 §7.3 或 §7.5 明确讨论 epoch confound 对 Few-NERD positive result 的 ecological validity 影响。

**W3** [warning] 模型多样性不足以支撑 "across multiple model families" claim

- 具体位置：Abstract, §7.1, Appendix t (Table 40-41)
- 问题：主实验用 Qwen3-8B + LLaMA-3.1-8B（同为 8B 级别）。Scale ablation（4B/14B: Table 41; 72B: Table 40; GPT-5.5: §6.2）在 Appendix 中但覆盖有限——72B 仅在 SciERC 上测试，GPT-5.5 仅 200 instances pilot。Abstract 说 "two model families (Qwen3-8B, LLaMA-3.1-8B) with 4B/14B ablations"，但核心发现是否适用于 >14B 模型并未 systematically 验证。Table 40 72B 结果实际上显示 LP ρ drops（无 fine-tuning），Table 41 14B 显示 gap 依然存在但 magnitude 变化。
- 建议：(a) 弱化 abstract/conclusion 中的 generalization scope——承认主要发现基于 8B 级别模型；(b) 在 Limitations 中更突出讨论 scale 限制。

**W4** [warning] Constrained decoding ablation 覆盖不足

- 具体位置：§4, Appendix q
- 问题：Free-form decoding ablation 仅在 CoNLL 和 SciERC 上进行（Appendix q, Table 33）。LP std ratio 0.97× 显示 constrained decoding 对 LP 信号影响小，但 degeneracy 变化可能在不同数据集上不同。论文称 "compression persists, is pervasive rather than a bimodal split"（Appendix q），但仅 2 个数据集的证据不够充分。
- 建议：在 Few-NERD 和/或 RE 上补充 free-form ablation，或明确讨论为什么 2 个数据集足够代表。

**W5** [warning] RE extension 和 SQL pilot 证据强度与呈现不匹配

- 具体位置：§6.2 (SQL), Appendix o (RE), §9 Discussion
- 问题：RE extension 用 n=397 单数据集（SciERC RE），SQL pilot 用 n=196。论文在 §9 Discussion 中说 "extensions to RE and SQL are exploratory"，这是诚实的。但 §1 Introduction 和 Abstract 提到 "with exploratory RE and SQL extensions" 的方式可能让读者高估这些 extensions 的证据强度。Table 66 (Prior Work Differentiation Matrix) 将 RE + SQL 列为论文的 coverage 优势，但证据基础是很薄弱的 pilot。
- 建议：确保 abstract/introduction 的措辞清楚传达 RE/SQL 的 exploratory 性质，避免 "validated extension" 的暗示。

---

## 小问题（不影响接收）

- §2.1 "A per-sample signal r_{p,i} : [x, y_i] → R scores each output independently" 中 R 的范围未定义（是实数？概率？），可加简要说明。
- Figure 1 caption 说 "not causal chain"，这个 disclaimer 放在 caption 里有点突兀，建议放到正文相关段落。
- §6.1 θ=2/N 的 notation 和 §2 的 notation 不完全一致（§2 用 T 表示 temperature，§6 引入 θ 作为 threshold），可统一术语。
- Table 2 Summary 中 "Few-NERD only" 标注在某些行出现但不在所有 applicable 行出现，一致性可改善。
- Limitations 中未提及 prompt template sensitivity（仅在 Appendix k 中提到 "single prompt template per task"），而 §7.5 的 prescriptive claims 隐含假设 prompt 不影响结论。

---

## Questions for Authors

**Q1**: Degeneracy decomposition bound 的 looseness 主要来自哪里？是 entity independence 假设（实际 split-half correlation 0.578-0.644），还是 α（signal alignment）的保守估计？能否 quantify 每个因素的贡献？

**Q2**: 如果在 global Holm-Bonferroni correction (k=57) 下 Few-NERD LP selection p_adj=0.055 不 significant，论文的核心叙事如何调整？是否有其他数据集/配置可以替代 Few-NERD 作为 positive contrast？

**Q3**: Entity construction inverse scaling 69% 的情况下，论文建议 practitioners 在什么具体条件下使用 entity construction？degeneracy <30% 且 LP-F1 ρ >0.4 是充分条件吗？

**Q4**: Probe 使用 Qwen2.5-7B 而非 Qwen3-8B——是否尝试过用 Qwen3-8B 的 hidden states（去掉 thinking tokens 后）训练 probe？如果没有，是否可以论证 Qwen2.5-7B 的 representational structure 与 Qwen3-8B 足够相似？

**Q5**: Few-NERD 5-epoch model 的 degeneracy 从 8.8% 升至 20.4% 后 LP gain 消失——这是否意味着 LP selection 仅在模型 under-converged 时有效？这对论文 §7.5 的 prescriptive guidance 有什么影响？

---

## Missing References

- **Malinin and Gales (2021)** "Uncertainty Estimation in Autoregressive Structured Prediction" — 与本文的 structured prediction uncertainty 直接相关但未引用。
- **Xiao and Wang (2021)** "On Hallucination and Predictive Uncertainty in Conditional Language Generation" — hallucination 与 degeneracy 的关系值得讨论。
- 论文引用了 Eikema and Aziz (2022) 关于 MBR，但未引用 **Müller and Sennrich (2021)** 更早的 MBR for NMT 分析（注意：这篇实际在 References p.11 中已引用——撤回此 missing reference）。

---

## 主要优势

1. **研究问题的 timeliness 和重要性**：TTS 在 reasoning 上的成功已被广泛验证，但在结构化输出任务上的 failure mode 缺乏系统研究。论文填补了一个真实的知识 gap。

2. **Correlation-selection gap 是 genuine 且 well-documented 的新发现**：AUROC up to 0.82 但 selection gain <1pp 的 disconnect 在 4 个 NER 数据集 + 2 个模型上一致复现（Table 3, Table 4），这不是 cherry-picked 结果。

3. **实验规模和透明度**：44 页论文（含 36 页 Appendix）展示了 exceptional thoroughness。Table 12 枚举所有 57 个统计检验并报告两种 correction，这种透明度在同行评审论文中罕见。

4. **Diagnostic framework 的概念价值**：即使定量 bound 松弛，degeneracy + signal alignment collapse 的 decomposition 提供了有用的概念语言来讨论 TTS 失败。

5. **诚实的 scope 控制**：论文对 RE/SQL 明确标记 "exploratory"，对 probe 承认模型限制，对 entity construction 承认 inverse scaling——这种诚实值得肯定。

---

## 总评

这是一篇 ambitious 且 thorough 的实证研究论文。核心发现（correlation-selection gap for NER）有价值且得到充分支撑。主要问题在于：(1) 理论贡献（degeneracy bound）过于松弛以至于定量诊断价值存疑；(2) 提出的解决方案（entity construction）在多数配置上反而有害；(3) 唯一的 positive contrast（Few-NERD LP selection）在统计上对 correction 选择敏感且受 under-training confound 影响。这些问题并非致命——论文的 negative result 本身就有价值——但论文的 framing 需要调整以匹配实际证据强度。如果 N1-N3 得到妥善处理（主要是 re-framing + 补充分析），论文有潜力达到 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 4070 · 2026-05-22T12:50:56.699276+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成独立审稿后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 306

## Round 306

2 recorded events


### User

_source line 4071 · 2026-05-22T12:51:06.278673+00:00_

[Reviewer 1 审稿结果]:
审稿完成。总结：

- **Overall: 3.5 (Borderline Conference)**，Soundness 3/5，Excitement 4/5
- **3 个 Must-Fix**：degeneracy bound 仅 capture 3-12% actual gains 削弱理论贡献；entity construction 69% inverse scaling 削弱 bypass framing；Few-NERD LP selection 核心 positive result 在 global Holm-Bonferroni (k=57) 下 p_adj=0.055 跨越显著性边界
- **5 个 Should-Fix**：probe 模型不匹配（Qwen2.5-7B vs Qwen3-8B）、Few-NERD epoch confound、模型 scale 覆盖不足、constrained decoding ablation 仅 2 数据集、RE/SQL pilot 证据薄弱
- **核心判断**：correlation-selection gap 本身是 genuine 发现，但论文的 prescriptive claims（diagnostic framework + entity construction bypass）与实际证据强度之间存在 gap，需要 re-framing

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 4072 · 2026-05-22T12:51:12.475328+00:00_

Reviewer 1 意见已收到。等待 Reviewer 2 完成后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 307

## Round 307

8 recorded events


### User

_source line 4073 · 2026-05-22T12:51:42.340682+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告：新颖性 + 论文完整性 + 写作质量

**论文**: When Does Test-Time Scaling Fail? Boundary Conditions for Named Entity Recognition
**Venue**: EMNLP 2026 Long Paper (ARR May cycle)

---

## 总体评分

**Overall Assessment**: 3.5 / 5 — Borderline Conference
**Confidence**: 4 / 5 — Quite sure. I tried to check the important points carefully.
**一句话总结**: 实验体量扎实（44页、4数据集、2模型族），核心发现 "correlation-selection gap" 对社区有价值，但与并发工作的增量区分不够清晰，标题承诺超出实际交付，entity construction 的旗舰结果 borderline non-significant。

---

## ARR 官方维度打分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 实验方法论严谨（bootstrap CI、Holm-Bonferroni 校正、permutation test），但核心 claim "entity construction bypasses bottleneck" 的 global Holm p=0.055 未达显著；cross-task extension 样本量偏小（RE n=397, SQL n=196）且承认 exploratory；§3 mechanistic analysis 用 Qwen2.5-7B 而非主实验 Qwen3-8B |
| **Excitement** | 3/5 | 研究问题重要且及时（structured output 的 test-time scaling），但 "correlation-selection gap" 概念在并发 BoN 文献中已有类似发现（见 W2 below）；diagnostic framework 实用价值存疑——需跑完全部采样才能诊断，这与"决定是否 scale 之前先评估"的初衷矛盾 |
| **Reproducibility** | 4/5 | 承诺公开代码/数据，prompt 模板在 Appendix k 中给出，实验配置详尽（Appendix a, Table 5），种子/温度 sweep 覆盖充分 |

---

## Summary

本文研究 test-time compute scaling（self-consistency/best-of-N）在 NER 任务上的失败条件。在 4 个 NER 数据集上使用 Qwen3-8B 和 LLaMA-3.1-8B 进行 7-14B 规模实验，发现质量估计信号（LP、SJ、FK 等）能预测输出质量（AUROC 最高 0.82），但 instance-level 信号无法转化为有效选择（MV gain <1pp，即使 N=64）。作者将此定义为 "correlation-selection gap"，并提出一个 diagnostic framework，识别出两个共同出现的失败条件：高 output degeneracy 和 signal alignment collapse。exploratory entity-level construction 在 Few-NERD 上获得 +1.4pp 提升。框架扩展到 RE 和 SQL parsing 作为 exploratory analysis。

---

## Strengths（主要优势）

**S1. 实验体量与统计严谨性出色。** 44 页论文（含 35 页附录）覆盖 4 NER 数据集 × 2 模型族 × 多种信号/选择策略的全排列，附有 bootstrap 95% CI（Table 11）、Holm-Bonferroni 全局校正（Table 12）、TOST 等价性检验（Table 15）、permutation test、split-half reliability 等统计工具。这在 NLP 实证研究中属于上乘水准。

**S2. 问题定位精准且重要。** "Test-time scaling 何时失败" 是一个社区急需回答的问题。对于 structured prediction 这类 partial-overlap output space 的任务，self-consistency 的适用性边界确实缺乏系统性研究。本文填补了这一空白。

**S3. 多层次分析框架。** 从 population-level (QE → AUROC) → instance-level (ranking → selection) → entity-level (construction) 三个粒度递进分析，逻辑清晰。Discover → Diagnose → Explore bypasses 的叙事结构有效。

**S4. Negative result 的诚实报告。** Cross-dataset transfer 为负（§7.3）、entity construction 在 CoNLL 无增益、Holm 全局校正后 p=0.055 等 negative/borderline 结果均如实报告，没有选择性展示。

**S5. MBR 连接的理论深度。** Appendix p.2 将 entity construction 形式化为 MBR decoding 的特例，Proposition 2 给出了 balanced set-overlap utility 下的最优解刻画，这为经验发现提供了理论支撑。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **Title "Boundary Conditions" 误导读者——实际交付是 diagnostic correlations，非 necessary/sufficient conditions**
- 具体位置：Title, §1 ¶1, §9 Conclusion
- 问题："Boundary conditions" 在数学和科学中暗示 necessary and/or sufficient conditions。但论文 §6.3 明确承认 "the decomposition is diagnostic rather than predictive"（p.5），§9 也说 "diagnostic rather than predictive"。论文交付的是一组 co-occurring statistical associations（degeneracy + alignment collapse），不是逻辑上严格的边界条件。
- 为什么影响接收：Reviewer 和读者会基于 title 形成预期。当 title 承诺 "boundary conditions" 而正文反复承认只是 "diagnostic"，这构成 claim-evidence mismatch，是 ARR soundness 维度的核心问题。
- 建议修改方向：改为 "When Does Test-Time Scaling Fail? Diagnostic Conditions for Named Entity Recognition" 或 "Failure Modes of Test-Time Scaling for Named Entity Recognition"。

**N2** [critical] **核心 bypass 结果（entity-level construction）统计显著性不足**
- 具体位置：§5.1, §7.5, Table 2, Appendix ab (Table 62)
- 问题：Entity construction 的旗舰结果是 Few-NERD +1.4pp，但 global Holm-Bonferroni 校正后 p=0.055（§7.5, p.7），未达 α=0.05。Abstract 中 "+1.4 pp" 未附任何 significance caveat。在 Table 2 中 entity construction 的 gain 标注为 "+0.42 pp (p<0.01)" 但这是 Few-NERD only 的数据；而论文说 "global Holm p=0.055" 则是跨数据集校正后的结果。这两个不同 scope 的 p-value 并列容易误导。
- 为什么影响接收：论文将 entity construction 作为 "partially bypasses the bottleneck" 的核心 positive finding（§1, §5, §9 均强调），但最严格的统计检验显示这一 claim 不 significant。这影响整篇文章的 contribution narrative。
- 建议修改方向：(a) Abstract 和 Introduction 中必须明确标注 "under global correction, the improvement is borderline non-significant (Holm p=0.055)"；(b) 将 entity construction 明确定位为 "exploratory/suggestive" 而非 confirmed finding；(c) 或提供更多数据集的结果以增强统计功效。

**N3** [critical] **与并发工作的新颖性区分不充分**
- 具体位置：§8 Related Work, §9 Discussion
- 问题：
  (a) **"Correlation-selection gap" 概念**: 2026年3月 arxiv 上已有 "When LLM Judge Scores Look Good but Best-of-N Decisions Fail"（arxiv 2603.12520）一文，在 LLM judge + BoN 设置下发现了本质相同的现象：全局 correlation 看起来不错但 within-prompt selection 失败（global r=0.47 → within-prompt r_within=0.27，recovery 仅 21%）。该文在本文 ARR May 截止日前 2+ 个月已公开。本文未讨论此并发工作。
  (b) **vs. Yao et al. (2026)**: §8 提到本文 "extend this to instance-level analysis"，但 instance-level 分析是 degree 上的差异还是 kind 上的差异，论证不够有力。Yao et al. 如果已发现 task-level 的 scaling failure，那 instance-level decomposition 的增量贡献需要更清晰的 articulation。
  (c) **"Capability-diversity tension"**: §8 讨论了 Yun et al. (2025) "diversity collapse"，但本文的 "capability-diversity tension" 与之的区别主要是 domain（NER vs. open-ended generation）和量化方式，概念本身不算新颖。
- 为什么影响接收：Novelty 是 ARR excitement 维度的核心。如果 correlation-selection gap 这一核心发现已在并发工作中被独立发现，则本文的 novelty 被显著削弱。
- 建议修改方向：(a) 必须添加对 arxiv 2603.12520 的讨论，明确本文在 structured prediction/NER 特有语境下的增量贡献（如 degeneracy decomposition 是 NER-specific 的分析）；(b) 强化 vs. Yao et al. 的 differentiation matrix（如 Appendix af Table 66 已有，应在主文 §8 更prominently 呈现）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **§3 Mechanistic Analysis 使用 Qwen2.5-7B，与主实验 Qwen3-8B 不一致**
- 具体位置：§3 (p.3), footnote 2
- 问题：§3 的 hidden-state probe、introspection boundary 分析全部基于 Qwen2.5-7B（fine-tuned），而 §4-7 主实验使用 Qwen3-8B。脚注2 解释 "Probe conclusions are limited to the Qwen2.5 architecture"，但读者很容易忽略这个 caveat。这导致的困惑：§3 发现的 introspection boundary（AUROC 0.63-0.88）是否适用于 Qwen3-8B？hidden-state 的 LP 信号结构是否一致？
- 建议：要么在 Qwen3-8B 上重做 probe 分析（至少 key experiment），要么在 §3 开头用显眼的方式（如一个 boxed note）声明模型差异，并在 §9 Discussion 讨论这一 generalizability limitation。

**W2** [warning] **Cross-task extension 的样本量和深度不足以支撑其在 abstract 中的权重**
- 具体位置：Abstract ("extensions to RE and SQL parsing"), §6.2, Appendix o
- 问题：RE (n=397) 和 SQL (n=196) 的 cross-task 扩展被 abstract 和 introduction 作为贡献之一提及，但论文自身承认 "exploratory"（§7.3, Limitations）。样本量较小，RE 只用了 SciERC 数据集的一个 split，SQL 只测了 196 个例子。这与 NER 实验的 4 数据集 × 多配置的规模不成比例。
- 建议：(a) Abstract 中将 RE/SQL 降格为 "preliminary cross-task exploration"；(b) 或增加更多 RE/SQL 数据集和配置。

**W3** [warning] **Diagnostic framework 的实用价值论证不足**
- 具体位置：§6.3, §9 Practical Implications, Appendix ac (Evaluation Protocol)
- 问题：论文声称 "framework guides practitioners on what to measure before committing to repeated inference"（Abstract, p.1）。但实际使用这个 framework 需要：(1) 先采 N 个样本计算 degeneracy；(2) 计算 α (signal alignment)。这意味着 practitioner 已经投入了 test-time compute 来诊断是否应该投入 test-time compute，构成循环。Appendix ac 的 "Evaluation Protocol" 描述了三步流程但没有 cost-benefit 分析（诊断成本 vs. 全量 scaling 成本），也没有用户研究或实际 practitioner feedback。
- 建议：(a) 添加 cost analysis（如：诊断只需 N=8 样本 vs. full scaling N=64，节省 8× compute）；(b) 讨论是否可以用 pre-deployment signals（如模型 perplexity on task format）作为 proxy，避免采样开销。

**W4** [warning] **Abstract 数字密度过高，narrative flow 受影响**
- 具体位置：Abstract (p.1)
- 问题：Abstract 在约 200 词内塞入了 AUROC 0.82、72B、N=64、+1.4pp、p<0.01、46%、α≈0 等大量数字。对于首次阅读的 reviewer 来说，难以快速把握 big picture。与 "story-first, numbers-second" 的顶会 abstract 写作范式不符。
- 建议：精简数字至 3-4 个最关键的（如 AUROC 上界、selection gain 上界、construction gain），其余用 qualitative language 替代。

**W5** [warning] **术语不一致：degeneracy vs. output convergence vs. convergence**
- 具体位置：通篇
- 问题：§2 标题使用 "high output convergence (hereafter degeneracy)"（p.2），此后正文交替使用 "degeneracy"、"output convergence"、"convergence"。例如 §4 "where LP discriminates" (p.4) vs. §6.3 "the failure to degeneracy" (p.5) vs. Table 6 "Instance degeneracy"。对于一个作者定义的核心概念，应统一术语。
- 建议：引入 "degeneracy" 后在全文统一使用这一个术语，仅在首次出现时注明等价表述。

---

## 小问题（不影响接收）

- **Nit-1**: §2.2 "Confidence Signals" 中列出 4 个信号族（SJ, VC, EM, FK），但 LP 在 §2.1 中单独引入。这 5 个信号之间的层次关系在第一次阅读时不够清晰。建议用一个表格或 bullet list 统一列出。
- **Nit-2**: Figure 1 caption 非常密集（3 行描述 3 个 panel + 多个数字），考虑简化 caption 并将部分描述移入正文。
- **Nit-3**: §7.1 "Models and sampling. Qwen3-8B and LLaMA-3.1-8B-Instruct"——这里首次提到 LLaMA 是 Instruct 版本，但 abstract 只说 "LLaMA-3.1-8B"。应保持一致。
- **Nit-4**: Table 5 notation table 放在 Appendix a (p.11)，但 §2 使用的符号需要读者翻到 11 页才能查到。考虑在 §2 首次使用时内联定义所有符号。
- **Nit-5**: Appendix 编号从 a 到 ag（33 个 appendix section），但正文中交叉引用频繁（几乎每段都有 "Appendix x" 引用），导致正文阅读时需要频繁跳转。考虑将最关键的 appendix 内容（如 Proposition 1 的完整陈述）提升到主文。

---

## Questions for Authors

**Q1**: Diagnostic framework 要求先采 N 个样本才能计算 degeneracy 和 α——你们设想的 practitioner 工作流是什么？是 "先用 N=8 诊断，再决定是否 scale 到 N=64"，还是别的场景？能否给出具体的 cost-benefit 数字？

**Q2**: §3 的 Qwen2.5-7B probe 结果是否已在 Qwen3-8B 上做了任何验证？如果没有，你们有多大信心认为 introspection boundary 的结论可以跨模型迁移？

**Q3**: 关于 Holm p=0.055——如果增加一个数据集（如 WNUT-17 的 entity construction 实验），是否有可能达到 significance？目前的 power analysis 是否支持这一点？

**Q4**: Title 为什么用 "Boundary Conditions" 而非 "Diagnostic Conditions" 或 "Failure Modes"？你们认为 degeneracy + α≈0 是 test-time scaling 失败的充分条件还是必要条件？

**Q5**: arxiv 2603.12520（"When LLM Judge Scores Look Good but Best-of-N Decisions Fail", March 2026）讨论了在 LLM judge 设置下几乎相同的 correlation-selection gap 现象——你们是否知悉此工作？如何界定本文的独立贡献？

---

## Missing References

1. **[必须添加]** "When LLM Judge Scores Look Good but Best-of-N Decisions Fail" (arxiv 2603.12520, March 2026) — 讨论了在 BoN selection 中几乎相同的 correlation-selection gap 现象
2. **[推荐添加]** "Conformal Structured Prediction" (Angelopoulos et al., ICLR 2025, arxiv 2410.06296) — 结构化输出的 conformal prediction，与本文的 confidence/uncertainty 框架互补
3. **[推荐添加]** "Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission" (He et al., NAACL Findings 2024) — token-level uncertainty estimation for NER，直接相关
4. **[推荐添加]** "Conformal Prediction for Natural Language Processing: A Survey" (TACL 2024/2025, arxiv 2405.01976) — 综述 conformal prediction 在 NLP 中的应用
5. **[推荐添加]** "LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty" (WWW 2024) — uncertainty-based NER 与 LLM 协作

---

## Related Work 覆盖度评估

- **Conformal prediction for structured output**: §8 提到 Angelopoulos and Bates (2023) 的 gentle introduction，但未讨论 ICLR 2025 的 Conformal Structured Prediction paper。这是一个缺口，因为 conformal prediction 提供 exchangeability-based guarantees，而本文的 degeneracy 现象恰恰违反了这一假设。
- **Token-level uncertainty estimation**: 论文讨论了 token-level LP aggregation（Appendix m, §6.3），但未引用 He et al. (2024) 等专门研究 NER uncertainty 传播的工作。
- **GPT-NER / self-verification**: §8 引用了 Xie et al. (2023) 的 entity voting 和 Chen et al. (2024a) 的 SC failure modes，GPT-NER (Wang et al., 2023) 在 references 中出现。覆盖尚可。
- **MBR decoding**: §8 和 Appendix p.2 对 MBR 文献的讨论相当充分，包括 Eikema and Aziz (2022)、Eikema et al. (2025)、Freitag et al. (2022/2023) 等。这是一个 strength。
- **Yao et al. (2026)**: §1 和 §8 均有讨论，Appendix af Table 66 有详细 differentiation matrix。讨论存在但主文 visibility 不够。

---

## Overall Assessment

**Overall**: 3.5 / 5 — Borderline Conference
**Confidence**: 4 / 5

**判断依据**:
本文在实验 thoroughness 上表现优秀（S1），研究问题重要（S2），negative results 报告诚实（S4）。这些是值得肯定的优点。

但有三个核心问题将其拉到 borderline：(1) Title "Boundary Conditions" 与实际交付 "diagnostic correlations" 之间的 mismatch（N1）；(2) 核心 positive finding（entity construction）在最严格统计检验下 borderline non-significant（N2）；(3) 核心概念 "correlation-selection gap" 与 2026 年 3 月并发工作的新颖性区分不足（N3）。

如果作者能在 rebuttal 中：(a) 调整 title 定位；(b) 提供 entity construction 的额外实验或更强的 significance 证据；(c) 清晰 articulate vs. 并发工作的差异化贡献，则论文有望升至 Conference 接收水平。目前定位为 Findings 较为稳妥。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 4074 · 2026-05-22T12:51:58.419767+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: Venue 调研 + 资料检查', 'status': 'completed', 'activeForm': '完成 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 视觉审查派发', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'in_progress', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: Venue 调研 + 资料检查', 'status': 'completed', 'activeForm': '完成 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 视觉审查派发', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'in_progress', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 4075 · 2026-05-22T12:51:58.420289+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 4076 · 2026-05-22T12:52:15.711316+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应其 Must-Fix 和 Should-Fix：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的 Must-Fix 问题\n\n**N1** [critical] Title \"Boundary Conditions\" 误导读者——实际交付是 diagnostic correlations，非 necessary/sufficient conditions\n- \"Boundary conditions\" 在数学和科学中暗示 necessary and/or sufficient conditions。但论文 §6.3 明确承认 \"the decomposition is diagnostic rather than predictive\"，§9 也说 \"diagnostic rather than predictive\"。论文交付的是一组 co-occurring statistical associations，不是逻辑上严格的边界条件。建议改为 \"Diagnostic Conditions\" 或 \"Failure Modes\"。\n\n**N2** [critical] 核心 bypass 结果（entity-level construction）统计显著性不足\n- Entity construction 的旗舰结果 Few-NERD +1.4pp，global Holm-Bonferroni 校正后 p=0.055，未达 α=0.05。Abstract 中 \"+1.4 pp\" 未附任何 significance caveat。论文将 entity construction 作为 \"partially bypasses the bottleneck\" 的核心 positive finding，但最严格统计检验显示不 significant。\n\n**N3** [critical] 与并发工作的新颖性区分不充分\n- (a) arxiv 2603.12520 \"When LLM Judge Scores Look Good but Best-of-N Decisions Fail\" 在 BoN 设置下发现本质相同的 correlation-selection gap；\n- (b) vs. Yao et al. (2026) 的 instance-level vs task-level 分析增量贡献不够清晰；\n- (c) \"capability-diversity tension\" 与 Yun & Kim (2025) \"diversity collapse\" 概念非原创。\n\n## Reviewer 2 的 Should-Fix 问题\n\n**W1** §3 Mechanistic Analysis 使用 Qwen2.5-7B，与主实验 Qwen3-8B 不一致\n**W2** Cross-task extension (RE n=397, SQL n=196) 样本量和深度不足以支撑 abstract 权重\n**W3** Diagnostic framework 实用价值论证不足——需先采样才能诊断，构成循环\n**W4** Abstract 数字密度过高\n**W5** 术语不一致：degeneracy vs output convergence vs convergence\n\n---\n\n请对以上每条给出 [AGREE] 或 [REBUT] 回应。",
  "project": "struct_self_consist_ie",
  "chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应其 Must-Fix 和 Should-Fix：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 的 Must-Fix 问题\n\n**N1** [critical] Title \"Boundary Conditions\" 误导读者——实际交付是 diagnostic correlations，非 necessary/sufficient conditions\n- \"Boundary conditions\" 在数学和科学中暗示 necessary and/or sufficient conditions。但论文 §6.3 明确承认 \"the decomposition is diagnostic rather than predictive\"，§9 也说 \"diagnostic rather than predictive\"。论文交付的是一组 co-occurring statistical associations，不是逻辑上严格的边界条件。建议改为 \"Diagnostic Conditions\" 或 \"Failure Modes\"。\n\n**N2** [critical] 核心 bypass 结果（entity-level construction）统计显著性不足\n- Entity construction 的旗舰结果 Few-NERD +1.4pp，global Holm-Bonferroni 校正后 p=0.055，未达 α=0.05。Abstract 中 \"+1.4 pp\" 未附任何 significance caveat。论文将 entity construction 作为 \"partially bypasses the bottleneck\" 的核心 positive finding，但最严格统计检验显示不 significant。\n\n**N3** [critical] 与并发工作的新颖性区分不充分\n- (a) arxiv 2603.12520 \"When LLM Judge Scores Look Good but Best-of-N Decisions Fail\" 在 BoN 设置下发现本质相同的 correlation-selection gap；\n- (b) vs. Yao et al. (2026) 的 instance-level vs task-level 分析增量贡献不够清晰；\n- (c) \"capability-diversity tension\" 与 Yun & Kim (2025) \"diversity collapse\" 概念非原创。\n\n## Reviewer 2 的 Should-Fix 问题\n\n**W1** §3 Mechanistic Analysis 使用 Qwen2.5-7B，与主实验 Qwen3-8B 不一致\n**W2** Cross-task extension (RE n=397, SQL n=196) 样本量和深度不足以支撑 abstract 权重\n**W3** Diagnostic framework 实用价值论证不足——需先采样才能诊断，构成循环\n**W4** Abstract 数字密度过高\n**W5** 术语不一致：degeneracy vs output convergence vs convergence\n\n---\n\n请对以上每条给出 [AGREE] 或 [REBUT] 回应。",
    "project": "struct_self_consist_ie",
    "chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 4077 · 2026-05-22T12:52:33.141261+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17429
}
```

</details>

---


### Tool call

_source line 4078 · 2026-05-22T12:52:33.342530+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应其 Must-Fix 和 Should-Fix：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的 Must-Fix 问题\n\n**N1** [critical] Degeneracy decomposition bound 过于松弛，削弱 framework 的定量诊断价值\n- Bound (1-D)·G_nd·α 仅 capture actual gains 的 3-12%。论文声称 framework \"guides practitioners on what to measure before committing to repeated inference\"，但一个 off by an order of magnitude 的 bound 无法指导实践决策。建议 (a) 讨论 looseness 来源（entity independence 假设？α 保守性？）；(b) 降低实践指导 claim；(c) 或寻找更 tight bound。\n\n**N2** [critical] Entity construction inverse scaling 率 69%（40/58），严重削弱 \"bypass\" framing\n- LP-weighted entity construction 在 4 数据集 × Qwen3-8B 中，从 N=8 到 N=16，正面 LP Δ 仅在 Few-NERD 上。§6.2 说 \"40 of 58 transitions show inverse scaling\"。论文将 entity construction 定位为 \"partially bypasses the bottleneck\"，但 69% inverse scaling 率意味着在大多数实践场景下不可靠。\n\n**N3** [critical] 统计检验对 multiple testing correction 选择敏感，核心 claim 跨越显著性边界\n- Few-NERD LP selection: per-family Holm (k=10) p_adj=0.006 vs global (k=57) p_adj=0.055。per-family 划分未 pre-registered。核心 claim 的显著性取决于 correction 方案选择。\n\n## Reviewer 1 的 Should-Fix 问题\n\n**W1** Hidden-state probe 使用 Qwen2.5-7B，而非主实验模型 Qwen3-8B\n**W2** Few-NERD 作为 \"positive contrast\" 受 under-training confound 影响（3-epoch vs 5-epoch, degeneracy 8.8%→20.4%, LP gain 消失）\n**W3** 模型多样性不足以支撑 \"across multiple model families\" claim（主要 8B 级别）\n**W4** Constrained decoding ablation 覆盖不足（仅 CoNLL + SciERC）\n**W5** RE extension 和 SQL pilot 证据强度与呈现不匹配\n\n---\n\n请对以上每条给出 [AGREE] 或 [REBUT] 回应。",
  "project": "struct_self_consist_ie",
  "chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应其 Must-Fix 和 Should-Fix：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 的 Must-Fix 问题\n\n**N1** [critical] Degeneracy decomposition bound 过于松弛，削弱 framework 的定量诊断价值\n- Bound (1-D)·G_nd·α 仅 capture actual gains 的 3-12%。论文声称 framework \"guides practitioners on what to measure before committing to repeated inference\"，但一个 off by an order of magnitude 的 bound 无法指导实践决策。建议 (a) 讨论 looseness 来源（entity independence 假设？α 保守性？）；(b) 降低实践指导 claim；(c) 或寻找更 tight bound。\n\n**N2** [critical] Entity construction inverse scaling 率 69%（40/58），严重削弱 \"bypass\" framing\n- LP-weighted entity construction 在 4 数据集 × Qwen3-8B 中，从 N=8 到 N=16，正面 LP Δ 仅在 Few-NERD 上。§6.2 说 \"40 of 58 transitions show inverse scaling\"。论文将 entity construction 定位为 \"partially bypasses the bottleneck\"，但 69% inverse scaling 率意味着在大多数实践场景下不可靠。\n\n**N3** [critical] 统计检验对 multiple testing correction 选择敏感，核心 claim 跨越显著性边界\n- Few-NERD LP selection: per-family Holm (k=10) p_adj=0.006 vs global (k=57) p_adj=0.055。per-family 划分未 pre-registered。核心 claim 的显著性取决于 correction 方案选择。\n\n## Reviewer 1 的 Should-Fix 问题\n\n**W1** Hidden-state probe 使用 Qwen2.5-7B，而非主实验模型 Qwen3-8B\n**W2** Few-NERD 作为 \"positive contrast\" 受 under-training confound 影响（3-epoch vs 5-epoch, degeneracy 8.8%→20.4%, LP gain 消失）\n**W3** 模型多样性不足以支撑 \"across multiple model families\" claim（主要 8B 级别）\n**W4** Constrained decoding ablation 覆盖不足（仅 CoNLL + SciERC）\n**W5** RE extension 和 SQL pilot 证据强度与呈现不匹配\n\n---\n\n请对以上每条给出 [AGREE] 或 [REBUT] 回应。",
    "project": "struct_self_consist_ie",
    "chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 4079 · 2026-05-22T12:52:34.918970+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1576
}
```

</details>

---


### Assistant

_source line 4080 · 2026-05-22T12:52:37.970429+00:00_

交叉分享已发送给两位 Reviewer，等待回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 308

## Round 308

2 recorded events


### User

_source line 4081 · 2026-05-22T12:52:40.742734+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心判断：**Overall 3.5（Borderline Conference）**，Confidence 4/5。

三个 Must-Fix 问题：
1. Title "Boundary Conditions" 与实际 "diagnostic correlations" 之间存在 claim-evidence mismatch
2. Entity construction 旗舰结果 Holm p=0.055 borderline non-significant，但 abstract 未标注
3. "Correlation-selection gap" 核心概念与 2026年3月并发工作（arxiv 2603.12520）的增量区分不足

主要 strengths：实验体量出色（44页、4数据集、2模型族），统计方法严谨，negative results 诚实报告，MBR 理论连接有深度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 4082 · 2026-05-22T12:52:45.768619+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 309

## Round 309

2 recorded events


### User

_source line 4083 · 2026-05-22T12:55:24.250543+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

### Must-Fix 逐条回应

**[AGREE] R2-N1: Title "Boundary Conditions" 用词误导**

同意 R2 的核心判断。论文自身在 §6.3 和 §9 中反复使用 "diagnostic rather than predictive" 来限定 framework 的性质，这与标题暗示的 formal necessary/sufficient conditions 存在 tension。"Boundary conditions" 在物理学和数学中指定义明确的边界约束（e.g., Dirichlet/Neumann conditions），而论文交付的是 co-occurring statistical associations——degeneracy 和 signal alignment collapse 的联合出现与 selection failure 相关，但并未证明它们是逻辑上的 necessary 或 sufficient conditions。

补充一个 R2 未提到的证据：§6.3 Corollary 1 给出了 degeneracy 的 critical threshold（D < 1 − 1/(G_nd · α)），但 bound 仅 capture 3–12% actual gains（Figure 10），说明这个"boundary"本身精度很低。

不过我认为 R2 建议的 "Diagnostic Conditions" 过于温和，可能削弱论文的 selling point。建议 **"Failure Modes"** 或 **"When and Why Test-Time Scaling Fails"**——既准确反映内容（识别失败的条件和机制），又保持足够的 impact。

---

**[REBUT] R2-N2: "Entity construction 旗舰结果 Few-NERD +1.4pp" 的归属和统计显著性**

R2 此条存在一个重要的事实性混淆：**+1.39pp 是 LP selection 的结果，不是 entity construction 的结果。**

具体证据：
- Abstract（p.1）明确将两者分开：LP selection 是 "the only per-sample signal achieving positive selection"，而 entity construction 是 "partially bypasses the bottleneck (≤1.0 pp where low degeneracy and LP-F1 alignment provide headroom)"
- Table 4（§7.3, p.6）："Few-NERD LP Δ +1.39pp" 出现在 Selection 列（LP 行），而 Construction 列数据不同
- Table 12（Appendix f, p.22）中 Few-NERD LP selection 和 entity construction 是不同的 test rows——Row 5 为 LP selection（family 1, NER selection），而 construction 属于 family 2

因此 R2 将 "+1.4pp, global Holm-Bonferroni p=0.055" 归于 entity construction 是错误的——这是 LP selection 在 Few-NERD 上的数据。Entity construction 的统计检验是独立的行（Table 12 family 2）。

**但是**，R2 的底层关切（核心 positive finding 的统计稳健性）是成立的，我在自己的 N3 中也独立提出了同样的问题：Few-NERD LP selection 在 per-family correction (k=10) 下 p_adj=0.006，但 global correction (k=57) 下 p_adj=0.055，跨越 α=0.05 边界。这确实是一个需要正文直面的问题。

总结：R2-N2 的统计关切有效，但将其归于 entity construction 而非 LP selection 是事实错误，应予纠正。建议 R2 修正指向。

---

**[REBUT] R2-N3: 与并发工作的新颖性区分**

分三个子点回应：

**(a) arxiv 2603.12520 "When LLM Judge Scores Look Good but Best-of-N Decisions Fail"**

[REBUT] 即使此并发工作在 BoN reasoning 设置下发现了类似的 correlation-selection gap，本文的贡献在于揭示了 **结构化输出任务中一个根本不同的失败机制**。NER 的 correlation-selection gap 源于 **degeneracy**（12–68% 的样本产生完全相同的 entity set，§6.3, Table 4），这是离散答案 reasoning 任务中不存在的现象——reasoning 的 BoN 面对的是连续评分空间中的区分度问题，而非输出坍缩。论文 §8 Related Work 和 Table 66（Appendix，Prior Work Differentiation Matrix）已明确定位：本文的独特贡献是 (1) structured output 的 degeneracy 机制，(2) entity-level construction 作为 bypass，(3) signal alignment collapse 的诊断框架。这些维度在 BoN-for-reasoning 的并发工作中不存在。

**(b) vs. Yao et al. (2026) 的 instance-level vs task-level 分析**

[AGREE（部分）] 正文确实应更明确区分增量贡献。论文 §1 引用了 Yao et al. 并指出 "observes this gap at the task level; we decompose it at the instance level, revealing that degeneracy..."——这个一句话区分对非专家读者不够清晰。建议在 §8 Related Work 中用一个专门段落对比：Yao et al. 做了什么 → 本文在哪些维度上 extend/deepen → 具体哪些发现是全新的。但这是 presentation 问题，非 novelty 问题——instance-level decomposition 加上 NER-specific 的 degeneracy 分析确实是实质性的增量。

**(c) "Capability-diversity tension" vs. Yun & Kim (2025) "diversity collapse"**

[REBUT] 概念相似不等于缺乏原创性。论文的 "capability-diversity tension" 有精确的 operationalization：degeneracy rate D（Definition 1, Appendix p.3）× signal alignment α（§6.3）的 decomposition，给出了 quantitative threshold（Corollary 1, θ_crit = 0.70）。这远比泛泛的 "diversity collapse" 概念具体——后者是定性观察，前者是有 mathematical formulation 的 diagnostic 工具。论文在 §8 中也引用了 diversity 相关的先前工作并做了区分。

---

### Should-Fix 逐条回应

**[AGREE] R2-W1: §3 Probe 使用 Qwen2.5-7B 与主实验 Qwen3-8B 不一致**

完全同意，这与我自己的 W1 一致。Footnote 3（p.3）的解释（Qwen3-8B 有 thinking tokens）是合理的工程理由，但不能替代实证验证。至少需要一组 Qwen3-8B hidden state（去掉 thinking tokens 后）的 probe 实验作为 sanity check，否则 §9 Discussion 中将 probe 结论作为 general finding 使用是 over-reaching。

---

**[AGREE] R2-W2: Cross-task extension (RE n=397, SQL n=196) 样本量不足以支撑 abstract 权重**

同意，这与我的 W5 一致。Abstract 提到 "exploratory RE and SQL extensions"，措辞本身是诚实的，但放在 abstract 中会让读者高估证据强度。特别是 SQL pilot 仅 n=196 且来自单一数据集，Table 66 将其列为 coverage 优势是过度。建议 abstract 中删除 SQL，或在 introduction 更明确标记 pilot 性质。

---

**[REBUT] R2-W3: 诊断 framework 需先采样才能诊断，构成循环**

R2 的关切可以理解，但论文的 prescriptive framework 并不要求全量采样后再决策。

具体证据：
1. §7.5（p.8）的 prescriptive guidance 明确提出 **分阶段策略**：先用小 N（N=8）采样计算 degeneracy 和 LP-F1 correlation，再决定是否 scale to N=64。Table 6（Appendix e, p.12）shows sample size robustness：N=8 到 N=16 的信号排名已经稳定（"signal rankings are difficulty-dependent... consistent across tasks and models"）。
2. §6.3 Corollary 1 给出了 degeneracy threshold（D < 1 − 1/(G_nd · α)），这是一个不依赖于大 N 的 ex-ante 可检查条件——只需要小 pilot 就能估计 D。
3. 更根本地，所有基于 sampling 的方法（包括 BoN、self-consistency、MBR）都面临相同的"需要先采样才能评估"问题。论文的贡献在于 **降低了评估所需的采样量**（从全量到 pilot），而非声称零成本诊断。

因此这不是 "循环"，而是"用小成本 pilot 避免大成本全量采样"的分阶段决策框架。论文可以在 §7.5 中更明确说明这个 pilot → decide → scale/abort 的流程。

---

**[AGREE] R2-W4: Abstract 数字密度过高**

同意。Abstract 中出现了 AUROC 0.82, <1pp, N=64, 12-68%, 3-12%, ≤1.0pp, θ_crit=0.70, 4B/14B/72B, 0.63-0.88 等大量数字。对首次阅读的读者来说 cognitive load 过高。建议精简至 3-4 个最关键数字，其余移至 Introduction 展开。

---

**[AGREE] R2-W5: 术语不一致——degeneracy vs output convergence vs convergence**

同意这是一个 editorial 问题。"Degeneracy" 是论文的核心术语（§2, Definition 1），但正文和附录中混用 "output convergence"（多处）和 "convergence"（Few-NERD epoch 讨论中既指 training convergence 又指 output convergence），容易造成混淆。建议统一：output collapse 现象一律用 "degeneracy"，training 收敛一律用 "training convergence"，避免裸用 "convergence"。

---

### 总结性评价

R2 的审稿整体质量较高，提出了几个我也独立发现的问题（W1/probe 模型不匹配，W2/cross-task 证据不足）。但 **N2 存在事实错误**（将 LP selection 结果误归于 entity construction），这需要纠正。N3 关于 novelty 的质疑在 (b) Yao et al. differentiation 上有道理，但 (a) 和 (c) 未充分考虑本文在 structured prediction 维度上的独特贡献。W3 的 "circularity" 论点在表面成立但忽略了 pilot-based 分阶段决策的实际可操作性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 4084 · 2026-05-22T12:55:29.670483+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 310

## Round 310

2 recorded events


### User

_source line 4085 · 2026-05-22T12:55:38.533497+00:00_

[Reviewer 1 审稿结果]:
对 R2 的 8 条意见逐条回应完毕：

- **N1 (title misleading)**: [AGREE]，但建议改为 "Failure Modes" 而非 R2 提议的 "Diagnostic Conditions"
- **N2 (entity construction significance)**: [REBUT]——R2 将 LP selection +1.4pp 误归于 entity construction（Table 4 和 Abstract 明确区分了两者），但底层统计关切有效（与我的 N3 一致）
- **N3 (novelty)**: [REBUT] on (a) 结构化输出的 degeneracy 机制与 BoN reasoning 根本不同；[AGREE 部分] on (b) 与 Yao et al. 的区分应更明确；[REBUT] on (c) capability-diversity tension 有精确 operationalization
- **W1-W5**: [AGREE] W1/W2/W4/W5；[REBUT] W3（pilot-based 分阶段决策不构成循环）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 4086 · 2026-05-22T12:55:45.233711+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 311

## Round 311

14 recorded events


### User

_source line 4087 · 2026-05-22T12:55:57.744525+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 的逐条回应

---

### Must-Fix 问题

---

**[AGREE] R1-N1: Degeneracy decomposition bound 过于松弛**

同意 R1 的核心判断。从 Appendix p.4 Table 31 和 Figure 10 可以确认：bound (1−D)·G_nd·α 仅 capture 实际 gain 的 3–12%，off by an order of magnitude。论文 §6.3 (p.5) 自己承认 "the decomposition is diagnostic rather than predictive: the three factors (D, G_nd, α) localize where aggregation fails rather than forecasting performance"，这本身是合理的。

但问题在于 **claim 与 delivery 的不一致**：Abstract (p.1) 声称 "framework guides practitioners on what to measure before committing to repeated inference"，§9 Practical Implications (p.8) 也重复了这一指导性定位。一个 off by 10× 的 bound 做不到 quantitative guidance。

**补充 R1 未提到的一点**：bound 的 looseness 可能主要来自 entity independence 假设——Proposition 1 的推导 (p.28) 假设 entity-level 得分独立，但 §5.2 的 cross-dataset transfer 实验 (p.5) 显示 "near-perfect entity classification cannot close the gap, indicating a structural bottleneck"，这暗示 entity 之间存在 correlation structure（共现 pattern、类型依赖），正是 independence 假设失效的地方。论文应显式讨论此 looseness 来源。

**建议**：同意 R1 的三条建议——(a) 讨论 looseness 来源；(b) 降低实践指导 claim 至 "directional diagnostic"；(c) 最好能给出 tighter bound 或至少 empirical calibration factor。

---

**[AGREE] R1-N2: Entity construction inverse scaling 率 69%，严重削弱 "bypass" framing**

同意。§6.2 (p.5) 明确报告 "Increasing N decreases construction F1 in 40 of 58 transitions"，即 69% 的 N-scaling transitions 上 entity construction 反而恶化。这个数字与 "partially bypasses the bottleneck"（Abstract, §1, §5, §9 多处使用）的 narrative 直接矛盾。

进一步查证：Table 2 (p.5) 中 entity construction 的 gain 列，除了 Few-NERD 上的 LP-weighted construction (+0.42 pp, p<0.01) 之外，SciERC 仅 +0.32 pp (non-significant)，CoNLL 无 gain (−0.38 pp)。这意味着 "bypass" 仅在 1/4 的数据集上 consistently positive，且该数据集（Few-NERD）恰好受 under-training confound 影响（见 W2 回应）。

**关键矛盾**：论文同时报告了两个相互矛盾的 narrative——§5 "Adaptive Methods" 将 entity construction 作为 bypass solution 呈现，§6.2 则报告 69% inverse scaling。读者需要自己在 35 页 appendix 中拼凑完整图景。主文应直面这一矛盾，将 entity construction 明确定位为 "works only under specific low-degeneracy configurations" 而非 general bypass。

---

**[AGREE] R1-N3: 统计检验对 multiple testing correction 选择敏感**

强烈同意，这与我自己的 N2 完全一致。核心事实：
- Per-family Holm (k=10): p_adj = 0.006 → significant
- Global Holm (k=57): p_adj = 0.055 → non-significant

从 §7.5 (p.7) 和 Table 12 (Appendix f, p.17) 可以确认这两个数字。论文在 §7.5 中用 per-family correction (k=10) 报告 "Holm p_adj=0.006"，但在下一句才提到 "Under global Holm-Bonferroni (k=57), p_adj=0.055"。这种呈现顺序（先显著后不显著）在写作上有 framing bias 嫌疑。

R1 正确指出 per-family 划分未 pre-registered。论文 §7.5 的辩护是 "we retain per-family correction (k=10) as quality estimation, selection, and construction test independent mechanisms"——但这个 rationale 是 post-hoc 的，且 "independent mechanisms" 的论证并不充分（三者共享相同的 sampling pipeline 和 instance population）。

**建议**：(a) 以 global correction 为主要报告，per-family 作为 sensitivity analysis；(b) 在 abstract 中附 global p-value caveat；(c) 或进行 pre-registered replication。

---

### Should-Fix 问题

---

**[AGREE] R1-W1: Hidden-state probe 使用 Qwen2.5-7B 而非 Qwen3-8B**

同意，这与我的 W1 一致。§3 的 mechanistic analysis（hidden-state probes, introspection boundary, AUROC 0.63-0.88）全部基于 Qwen2.5-7B-SciERC checkpoint，而 §4-7 主实验使用 Qwen3-8B。footnote 2 的 caveat ("Probe conclusions are limited to the Qwen2.5 architecture") 容易被忽略。

核心风险：Qwen3 架构与 Qwen2.5 有显著差异（如 Qwen3 默认启用 thinking mode、不同的 attention 实现）。§3 发现的 "hidden states encode partial entity quality signal inaccessible through the prompt interface"（p.8 §9）这一结论能否迁移到 Qwen3 是未验证的。

建议不变：至少在 Qwen3-8B 上做一个 key probe 实验，或在 §3 开头显著标注模型差异。

---

**[AGREE with nuance] R1-W2: Few-NERD under-training confound**

同意 confound 存在，但论文实际上已部分 address 了这个问题。

§7.5 (p.7) 明确写道："Few-NERD uses 3 training epochs (vs. 5), yielding lower degeneracy (11.9% vs. 31%) and stronger LP selection (+1.3 vs. +0.12±0.18 pp, Appendix ab); this sensitivity—favorable conditions are fragile—reinforces the framework's diagnostic value." Appendix ab (p.37) 还提供了 3-epoch vs 5-epoch 的详细比较（Table 55）。

论文的 defense 策略是将 confound 转化为 supporting evidence："favorable conditions are fragile" → framework correctly diagnoses that conditions matter。这在逻辑上是自洽的。

但 **R1 的核心问题仍然成立**：Few-NERD 在全文中被反复用作 "positive contrast"（§4 "Where Single-Signal Selection Fails", §5.1 "positive contrast", Figure 3, Figure 4 等），而这个 positive status 本身是 confounded 的。如果 Few-NERD 训练到 5 epochs 使 degeneracy 升至 31%，LP gain 消失，那 §4-5 的叙事结构就失去了 anchor。论文应更 prominent 地在主文中标注这一 confound（目前藏在 §7.5 的两行中），并考虑是否应以 SciERC 低 degeneracy 配置作为替代 anchor。

---

**[REBUT] R1-W3: 模型多样性不足**

部分不同意。R1 称 "主要 8B 级别" 不足以支撑 "across multiple model families" claim，但需注意：

1. **主实验**确实是 Qwen3-8B + LLaMA-3.1-8B-Instruct（两个不同架构族的 8B 模型），这已经是 "multiple families" 了——family 指架构族（Qwen vs LLaMA），不是 scale。
2. **Scale 覆盖**并非空白：§6.2 (p.5) 报告了 8B→14B→72B 的 scaling 分析——"Oracle F1 follows F_1(N) = a − b · N^{−c} (R² > 0.999; Figure 11)"，"scaling from 8B to 14B FT increases oracle headroom (+1.2 pp)"；Appendix h 有 Qwen2.5-72B 零样本结果；Appendix x 有 LLaMA-3.2-3B 的 scale ablation。
3. 论文 Limitations (p.9) 已承认 "four English datasets, 7-14B fine-tuned"。

但我同意 R1 的方向：主文的 **Qwen3-8B 和 LLaMA-3.1-8B 都是 8B 级别**，这限制了关于 scale-dependent 现象（degeneracy 随 model size 变化）的推广性。72B 和 14B 实验仅在 appendix 且覆盖不完整。建议在 Limitations 中更明确标注 scale 限制。

---

**[AGREE] R1-W4: Constrained decoding ablation 覆盖不足**

同意。Table 33 (p.30) 的 constrained vs. free-form decoding 比较仅覆盖 SciERC，且只在 NER 和 RE 两个 task 上做了对比。考虑到 constrained decoding 直接影响 output distribution（从而影响 degeneracy 的核心机制），这个 ablation 在仅 1 个数据集上的结果不足以得出通用结论。

尤其是 §6.3 关于 LP compression 的分析（"LP compression limits exploitation"）——constrained decoding 可能通过改变 token probability distribution 来缓解 LP compression。如果 constrained decoding 在 CoNLL 或 Few-NERD 上也测试了，结论会更有说服力。

---

**[AGREE] R1-W5: RE/SQL 证据强度与呈现不匹配**

同意，这与我的 W2 一致。RE (n=397, 仅 SciERC 的 RE split) 和 SQL (n=196) 的样本量和配置多样性远不如 NER 实验。但 Abstract 将 "extensions to RE and SQL parsing" 与 NER 实验并列呈现，给人等权重的印象。

---

## 总结

8 条意见中我同意 7 条（含 2 条带 nuance），反驳 1 条（W3 模型多样性，但仅部分反驳）。

**R1 和我的共识点**：
- N2 (entity construction) 和 N3 (multiple testing) 是最严重的问题，两位 reviewer 独立发现了相同的 statistical significance 隐患
- Title "Boundary Conditions" overclaims（R1-N1 的 bound looseness + 我的 N1 的 title mismatch 是同一问题的两面）
- §3 Qwen2.5-7B probe 的 generalizability gap 是共识 concern
- RE/SQL 呈现权重过高是共识

**我与 R1 的差异**：
- R1 更关注 bound 的数学 tightness（N1），我更关注 title-level 的 framing mismatch（我的 N1）
- R1 对模型多样性的要求更高（W3），我认为 two families 已满足 "multiple families" 但 scale diversity 不足
- R1 提出了 Few-NERD under-training confound（W2），这是我未重点关注但认同的 insight

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 4088 · 2026-05-22T12:56:31.924533+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: Venue 调研 + 资料检查', 'status': 'completed', 'activeForm': '完成 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 视觉审查派发', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断审稿意见是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'in_progress', 'activeForm': '汇总并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: Venue 调研 + 资料检查', 'status': 'completed', 'activeForm': '完成 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 视觉审查派发', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断审稿意见是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'in_progress', 'activeForm': '汇总并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 4089 · 2026-05-22T12:56:31.925026+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 4090 · 2026-05-22T12:56:32.730290+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool call

_source line 4091 · 2026-05-22T12:56:32.730573+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 4092 · 2026-05-22T12:56:32.781424+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T12:43:49.545562+00:00\", \"completed_at\": \"2026-05-22T12:48:35.353956+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无 display item，Figure 1 在第 2 页顶部出现。ACL 格式下 abstract 占据大部分首页空间，属正常情况，但若空间允许可考虑将概览图提前至首页底部以强化审稿人第一印象\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"单页 3 个 display items（Table 3 + Table 4 + Figure 4），视觉密度极高。信息组织合理但页面较拥挤，审稿人快速扫描时可能感到压迫感\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"正文最后一页纯文本（Related Work + Discussion/Conclusion），无 display item。这是常见做法，但如果 Conclusion 中能嵌一个总结性 figure 或 takeaway box 会更有锚定效果\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 2（全宽 9 类方法汇总表）列数较多，部分缩写列（GP/Cutoff 等）字号偏小，快速扫描时可读性一般。建议 caption 或脚注中解释所有缩写\"}, {\"severity\": \"info\", \"dimension\": \"page 15\", \"message\": \"Figure 7 heatmap 使用连续色阶（紫→蓝→绿→黄），各单元格内嵌数值。色阶本身接近 viridis（色盲安全），但低值区域的紫色与蓝色区分度有限；因有数值标注，实际影响很小\"}, {\"severity\": \"info\", \"dimension\": \"page 22\", \"message\": \"Table 12（Holm-Bonferroni 统计检验全表，57 行）字号较小，为 appendix 材料可接受，但接近可读性下限\"}, {\"severity\": \"info\", \"dimension\": \"pages 23-24\", \"message\": \"多个小型 tables（13–16, 18–22）密集排列，字号偏小。Appendix 材料标准，但阅读舒适度一般\"}, {\"severity\": \"info\", \"dimension\": \"page 32\", \"message\": \"Figure 11 + Table 40 下方有少量空白（约 1/6 页），Appendix 内不影响审稿评价\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 8}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 4093 · 2026-05-22T12:56:32.781920+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 4094 · 2026-05-22T12:58:25.945492+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n# ===== ROUND 38 MUST-FIX =====\n- id: R38-MF1\n  summary: \"Title 'Boundary Conditions' 与实际交付 'diagnostic correlations' 之间存在 claim-evidence mismatch\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 37\n  last_seen_round: 38\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"R37-MF3: diagnostic vs predictive scope 张力。标题保留但正文多处加 caveat。\"\n    - round: 38\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均 AGREE。'Boundary conditions' 在数学/科学中暗示 necessary/sufficient conditions，但论文交付的是 co-occurring statistical associations。§6.3 和 §9 反复说 'diagnostic rather than predictive'，与标题矛盾。R1 建议 'Failure Modes'，R2 建议 'Diagnostic Conditions'。\"\n  action_items:\n    - round: 38\n      action: \"标题改为 'When Does Test-Time Scaling Fail? Failure Modes for Named Entity Recognition' 或类似措辞\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R38-MF2\n  summary: \"Degeneracy decomposition bound (1-D)·G_nd·α 仅 capture 3-12% actual gains，定量诊断价值存疑\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 38\n  last_seen_round: 38\n  mentions:\n    - round: 38\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均 AGREE。Bound off by 10×，无法提供 quantitative guidance。R2 补充：looseness 可能源于 entity independence 假设（split-half r=0.578-0.644 显示 entity 间有 correlation structure）。Abstract 'guides practitioners' claim 与 bound 精度不匹配。\"\n  action_items:\n    - round: 38\n      action: \"(a) 正文讨论 bound looseness 来源（entity independence 假设、α 保守性）；(b) 将 bound 定位为 'illustrative upper bound' 而非 'diagnostic tool'；(c) 降低 Abstract/§9 中的实践指导 claim\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R38-MF3\n  summary: \"Entity construction 69% inverse scaling (40/58 transitions)，'bypass' framing 严重过度\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 38\n  last_seen_round: 38\n  mentions:\n    - round: 38\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均 AGREE。§6.2 报告 40/58 transitions 出现 inverse scaling。LP-weighted construction 仅 Few-NERD 上 consistently positive，SciERC non-significant (+0.32pp)，CoNLL negative (-0.39pp)。Abstract/§1/§5/§9 多处 'partially bypasses the bottleneck' 与 69% failure 率直接矛盾。\"\n  action_items:\n    - round: 38\n      action: \"将 entity construction 明确定位为 'conditional bypass: works only under low-degeneracy + LP-F1 alignment'；Abstract/Introduction 调低 claim；讨论 inverse scaling 的 practical implications\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R38-MF4\n  summary: \"核心 positive result (Few-NERD LP selection) 在 global Holm-Bonferroni (k=57) 下 p_adj=0.055，跨越显著性边界\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 34\n  last_seen_round: 38\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"R37-MF1: per-family 划分缺乏 pre-registration。§7 已讨论但 justification 仍不充分。\"\n    - round: 38\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 再次独立发现同一问题并 AGREE。Per-family (k=10) p=0.006 vs global (k=57) p=0.055。§7.5 先报告显著后报告不显著的呈现顺序有 framing bias。per-family 划分 'independent mechanisms' 论证不充分——三者共享 sampling pipeline 和 instance population。\"\n  action_items:\n    - round: 38\n      action: \"(a) 以 global correction 为主要报告，per-family 作为 sensitivity analysis；(b) Abstract 附 global p-value caveat；(c) 承认 per-family 划分未 pre-registered\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== ROUND 38 SHOULD-FIX =====\n- id: R38-SF1\n  summary: \"§3 Hidden-state probe 使用 Qwen2.5-7B 而非主实验 Qwen3-8B，generalizability gap 未验证\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 38\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"R37-SF2: Footnote 不够，需 Qwen3-8B probe 或限定结论范围。\"\n    - round: 38\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 再次 AGREE。Qwen3 架构（thinking mode、不同 attention）与 Qwen2.5 有显著差异。§9 将 probe 结论作为 general finding 使用是 over-reaching。\"\n  action_items:\n    - round: 38\n      action: \"至少在 Qwen3-8B 上做 1 组 key probe 实验（去掉 thinking tokens），或在 §3 开头显著标注模型限制\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R38-SF2\n  summary: \"Few-NERD 'positive contrast' 受 3-epoch under-training confound 影响，ecological validity 存疑\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 38\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"R37-SF5: 5-epoch 数据存在但 confound 讨论不充分。\"\n    - round: 38\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 AGREE with nuance。5-epoch degeneracy 升至 31%，LP gain 消失（+1.39→+0.12pp）。Few-NERD 在全文被反复用作 positive anchor，但此 anchor 是 confounded 的。§7.5 仅两行讨论，不够 prominent。\"\n  action_items:\n    - round: 38\n      action: \"主文更 prominent 讨论 epoch confound；考虑是否以 SciERC 低 degeneracy 配置作为替代 anchor\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R38-SF3\n  summary: \"与并发工作 arxiv 2603.12520 (correlation-selection gap in BoN) 的新颖性区分缺失\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 38\n  last_seen_round: 38\n  mentions:\n    - round: 38\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 REBUT——认为结构化输出的 degeneracy 机制与 BoN reasoning 根本不同。分歧未完全收敛。R1 的 rebut 有道理（NER degeneracy 是 entity-set level collapse，reasoning BoN 是评分区分度问题），但并发工作仍应被引用和讨论。\"\n  action_items:\n    - round: 38\n      action: \"§8 Related Work 添加对 arxiv 2603.12520 的讨论，明确结构化输出 degeneracy 机制的独特性\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R38-SF4\n  summary: \"模型 scale 覆盖不足以支撑 cross-scale generalization claim（主要 8B 级别）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 37\n  last_seen_round: 38\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"R37-SF3: generalization claim 限定为 7-14B open-weight。\"\n    - round: 38\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 partial REBUT（two families 满足 'multiple families' 但 scale diversity 不足）。72B/GPT-5.5 仅 pilot/appendix，14B 覆盖不完整。\"\n  action_items:\n    - round: 38\n      action: \"Limitations 更明确标注 scale 限制；弱化 cross-scale generalization claim\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R38-SF5\n  summary: \"RE (n=397) / SQL (n=196) 证据强度与 abstract/intro 呈现权重不匹配\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 37\n  last_seen_round: 38\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"R37-SF4: 'validation' → 'exploration' 已改。\"\n    - round: 38\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 再次 AGREE。Abstract 将 RE/SQL 与 NER 并列给人等权重印象。SQL pilot n=196 单数据集。\"\n  action_items:\n    - round: 38\n      action: \"Abstract 进一步降格 RE/SQL 为 'preliminary pilot'；或在 intro 更明确标记证据强度\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R38-SF6\n  summary: \"Constrained decoding ablation 仅 2 数据集 (CoNLL + SciERC)，覆盖不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 38\n  last_seen_round: 38\n  mentions:\n    - round: 38\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均 AGREE。Constrained decoding 直接影响 output distribution 和 degeneracy 核心机制。Table 33 仅覆盖 SciERC (+ RE)。Few-NERD/CoNLL 的 free-form ablation 缺失。\"\n  action_items:\n    - round: 38\n      action: \"补充 Few-NERD free-form ablation，或明确讨论 2 数据集覆盖的代表性\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R38-SF7\n  summary: \"Abstract 数字密度过高，narrative flow 受影响\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 37\n  last_seen_round: 38\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"R37-SF7: 已精简至 7 句 3 个核心数字。\"\n    - round: 38\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 再次 AGREE。当前 abstract 仍然塞入过多数字（AUROC 0.82、<1pp、N=64、12-68%、+1.40pp 等）。\"\n  action_items:\n    - round: 38\n      action: \"进一步精简至 3-4 个最关键数字，其余用 qualitative language\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R38-SF8\n  summary: \"术语不一致：degeneracy / output convergence / convergence 交替使用\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 37\n  last_seen_round: 38\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"R37-SF9: abstract 定义为 'high output convergence (hereafter degeneracy)'。\"\n    - round: 38\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 再次 AGREE。定义后仍有混用。'convergence' 还与 training convergence 歧义。\"\n  action_items:\n    - round: 38\n      action: \"全文统一：output collapse 用 'degeneracy'，training 收敛用 'training convergence'，避免裸用 'convergence'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R38-SF9\n  summary: \"与 Yao et al. (2026) 的增量新颖性区分不够清晰\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 35\n  last_seen_round: 38\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"R37-MF4: §1 三层区分 + §8 对比段落已添加。\"\n    - round: 38\n      reviewers: [1, 2]\n      note: \"R2 提出 (R2-N3b)，R1 部分 AGREE——instance-level 分析是实质增量但主文 §8 visibility 不够。\"\n  action_items:\n    - round: 38\n      action: \"§8 更 prominently 呈现 vs Yao et al. 的 differentiation matrix\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R38-SF10\n  summary: \"Diagnostic framework 实用价值论证不足——缺乏 cost-benefit analysis\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 38\n  last_seen_round: 38\n  mentions:\n    - round: 38\n      reviewers: [1, 2]\n      note: \"R2 提出 (W3)，R1 REBUT——pilot-based 分阶段决策不构成循环。分歧存在：R2 认为缺乏 cost-benefit 数字，R1 认为 N=8 pilot → decide → scale/abort 流程已合理。\"\n  action_items:\n    - round: 38\n      action: \"§7.5 或 §9 添加简要 cost analysis（N=8 诊断 vs N=64 全量）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== EARLIER ISSUES — STATUS UPDATE =====\n- id: R36-MF1\n  summary: \"标题 'Information Extraction' overclaim → 已改为 NER\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 33\n  last_seen_round: 37\n  mentions:\n    - round: 38\n      reviewers: [1, 2]\n      note: \"标题已为 NER，本轮未提及此问题。确认 resolved。但 R38 发现新标题 'Boundary Conditions' 有新的 overclaim 问题（见 R38-MF1）。\"\n  resolution: \"标题已改为 NER scope\"\n  resolution_round: 37\n\n- id: R36-SF1\n  summary: \"'Diagnostic cascade' 术语误导因果解读\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 36\n  last_seen_round: 37\n  mentions:\n    - round: 38\n      reviewers: []\n      note: \"本轮未提及。确认 resolved。\"\n  resolution: \"全文 cascade→framework\"\n  resolution_round: 37\n\n- id: R36-SF8\n  summary: \"Responsible NLP Checklist 不应在 PDF 中\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 36\n  last_seen_round: 37\n  mentions:\n    - round: 38\n      reviewers: []\n      note: \"本轮未提及。确认 resolved。\"\n  resolution: \"main.tex 中 checklist 已移除\"\n  resolution_round: 37\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "issues_yaml": "issues:\n# ===== ROUND 38 MUST-FIX =====\n- id: R38-MF1\n  summary: \"Title 'Boundary Conditions' 与实际交付 'diagnostic correlations' 之间存在 claim-evidence mismatch\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 37\n  last_seen_round: 38\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"R37-MF3: diagnostic vs predictive scope 张力。标题保留但正文多处加 caveat。\"\n    - round: 38\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均 AGREE。'Boundary conditions' 在数学/科学中暗示 necessary/sufficient conditions，但论文交付的是 co-occurring statistical associations。§6.3 和 §9 反复说 'diagnostic rather than predictive'，与标题矛盾。R1 建议 'Failure Modes'，R2 建议 'Diagnostic Conditions'。\"\n  action_items:\n    - round: 38\n      action: \"标题改为 'When Does Test-Time Scaling Fail? Failure Modes for Named Entity Recognition' 或类似措辞\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R38-MF2\n  summary: \"Degeneracy decomposition bound (1-D)·G_nd·α 仅 capture 3-12% actual gains，定量诊断价值存疑\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 38\n  last_seen_round: 38\n  mentions:\n    - round: 38\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均 AGREE。Bound off by 10×，无法提供 quantitative guidance。R2 补充：looseness 可能源于 entity independence 假设（split-half r=0.578-0.644 显示 entity 间有 correlation structure）。Abstract 'guides practitioners' claim 与 bound 精度不匹配。\"\n  action_items:\n    - round: 38\n      action: \"(a) 正文讨论 bound looseness 来源（entity independence 假设、α 保守性）；(b) 将 bound 定位为 'illustrative upper bound' 而非 'diagnostic tool'；(c) 降低 Abstract/§9 中的实践指导 claim\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R38-MF3\n  summary: \"Entity construction 69% inverse scaling (40/58 transitions)，'bypass' framing 严重过度\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 38\n  last_seen_round: 38\n  mentions:\n    - round: 38\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均 AGREE。§6.2 报告 40/58 transitions 出现 inverse scaling。LP-weighted construction 仅 Few-NERD 上 consistently positive，SciERC non-significant (+0.32pp)，CoNLL negative (-0.39pp)。Abstract/§1/§5/§9 多处 'partially bypasses the bottleneck' 与 69% failure 率直接矛盾。\"\n  action_items:\n    - round: 38\n      action: \"将 entity construction 明确定位为 'conditional bypass: works only under low-degeneracy + LP-F1 alignment'；Abstract/Introduction 调低 claim；讨论 inverse scaling 的 practical implications\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R38-MF4\n  summary: \"核心 positive result (Few-NERD LP selection) 在 global Holm-Bonferroni (k=57) 下 p_adj=0.055，跨越显著性边界\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 34\n  last_seen_round: 38\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"R37-MF1: per-family 划分缺乏 pre-registration。§7 已讨论但 justification 仍不充分。\"\n    - round: 38\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 再次独立发现同一问题并 AGREE。Per-family (k=10) p=0.006 vs global (k=57) p=0.055。§7.5 先报告显著后报告不显著的呈现顺序有 framing bias。per-family 划分 'independent mechanisms' 论证不充分——三者共享 sampling pipeline 和 instance population。\"\n  action_items:\n    - round: 38\n      action: \"(a) 以 global correction 为主要报告，per-family 作为 sensitivity analysis；(b) Abstract 附 global p-value caveat；(c) 承认 per-family 划分未 pre-registered\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== ROUND 38 SHOULD-FIX =====\n- id: R38-SF1\n  summary: \"§3 Hidden-state probe 使用 Qwen2.5-7B 而非主实验 Qwen3-8B，generalizability gap 未验证\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 38\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"R37-SF2: Footnote 不够，需 Qwen3-8B probe 或限定结论范围。\"\n    - round: 38\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 再次 AGREE。Qwen3 架构（thinking mode、不同 attention）与 Qwen2.5 有显著差异。§9 将 probe 结论作为 general finding 使用是 over-reaching。\"\n  action_items:\n    - round: 38\n      action: \"至少在 Qwen3-8B 上做 1 组 key probe 实验（去掉 thinking tokens），或在 §3 开头显著标注模型限制\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R38-SF2\n  summary: \"Few-NERD 'positive contrast' 受 3-epoch under-training confound 影响，ecological validity 存疑\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 36\n  last_seen_round: 38\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"R37-SF5: 5-epoch 数据存在但 confound 讨论不充分。\"\n    - round: 38\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 AGREE with nuance。5-epoch degeneracy 升至 31%，LP gain 消失（+1.39→+0.12pp）。Few-NERD 在全文被反复用作 positive anchor，但此 anchor 是 confounded 的。§7.5 仅两行讨论，不够 prominent。\"\n  action_items:\n    - round: 38\n      action: \"主文更 prominent 讨论 epoch confound；考虑是否以 SciERC 低 degeneracy 配置作为替代 anchor\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R38-SF3\n  summary: \"与并发工作 arxiv 2603.12520 (correlation-selection gap in BoN) 的新颖性区分缺失\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 38\n  last_seen_round: 38\n  mentions:\n    - round: 38\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 REBUT——认为结构化输出的 degeneracy 机制与 BoN reasoning 根本不同。分歧未完全收敛。R1 的 rebut 有道理（NER degeneracy 是 entity-set level collapse，reasoning BoN 是评分区分度问题），但并发工作仍应被引用和讨论。\"\n  action_items:\n    - round: 38\n      action: \"§8 Related Work 添加对 arxiv 2603.12520 的讨论，明确结构化输出 degeneracy 机制的独特性\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R38-SF4\n  summary: \"模型 scale 覆盖不足以支撑 cross-scale generalization claim（主要 8B 级别）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 37\n  last_seen_round: 38\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"R37-SF3: generalization claim 限定为 7-14B open-weight。\"\n    - round: 38\n      reviewers: [1, 2]\n      note: \"R1 提出，R2 partial REBUT（two families 满足 'multiple families' 但 scale diversity 不足）。72B/GPT-5.5 仅 pilot/appendix，14B 覆盖不完整。\"\n  action_items:\n    - round: 38\n      action: \"Limitations 更明确标注 scale 限制；弱化 cross-scale generalization claim\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R38-SF5\n  summary: \"RE (n=397) / SQL (n=196) 证据强度与 abstract/intro 呈现权重不匹配\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 37\n  last_seen_round: 38\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"R37-SF4: 'validation' → 'exploration' 已改。\"\n    - round: 38\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 再次 AGREE。Abstract 将 RE/SQL 与 NER 并列给人等权重印象。SQL pilot n=196 单数据集。\"\n  action_items:\n    - round: 38\n      action: \"Abstract 进一步降格 RE/SQL 为 'preliminary pilot'；或在 intro 更明确标记证据强度\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R38-SF6\n  summary: \"Constrained decoding ablation 仅 2 数据集 (CoNLL + SciERC)，覆盖不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 38\n  last_seen_round: 38\n  mentions:\n    - round: 38\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 均 AGREE。Constrained decoding 直接影响 output distribution 和 degeneracy 核心机制。Table 33 仅覆盖 SciERC (+ RE)。Few-NERD/CoNLL 的 free-form ablation 缺失。\"\n  action_items:\n    - round: 38\n      action: \"补充 Few-NERD free-form ablation，或明确讨论 2 数据集覆盖的代表性\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R38-SF7\n  summary: \"Abstract 数字密度过高，narrative flow 受影响\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 37\n  last_seen_round: 38\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"R37-SF7: 已精简至 7 句 3 个核心数字。\"\n    - round: 38\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 再次 AGREE。当前 abstract 仍然塞入过多数字（AUROC 0.82、<1pp、N=64、12-68%、+1.40pp 等）。\"\n  action_items:\n    - round: 38\n      action: \"进一步精简至 3-4 个最关键数字，其余用 qualitative language\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R38-SF8\n  summary: \"术语不一致：degeneracy / output convergence / convergence 交替使用\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 37\n  last_seen_round: 38\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"R37-SF9: abstract 定义为 'high output convergence (hereafter degeneracy)'。\"\n    - round: 38\n      reviewers: [1, 2]\n      note: \"两位 Reviewer 再次 AGREE。定义后仍有混用。'convergence' 还与 training convergence 歧义。\"\n  action_items:\n    - round: 38\n      action: \"全文统一：output collapse 用 'degeneracy'，training 收敛用 'training convergence'，避免裸用 'convergence'\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R38-SF9\n  summary: \"与 Yao et al. (2026) 的增量新颖性区分不够清晰\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 35\n  last_seen_round: 38\n  mentions:\n    - round: 37\n      reviewers: [1, 2]\n      note: \"R37-MF4: §1 三层区分 + §8 对比段落已添加。\"\n    - round: 38\n      reviewers: [1, 2]\n      note: \"R2 提出 (R2-N3b)，R1 部分 AGREE——instance-level 分析是实质增量但主文 §8 visibility 不够。\"\n  action_items:\n    - round: 38\n      action: \"§8 更 prominently 呈现 vs Yao et al. 的 differentiation matrix\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R38-SF10\n  summary: \"Diagnostic framework 实用价值论证不足——缺乏 cost-benefit analysis\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 38\n  last_seen_round: 38\n  mentions:\n    - round: 38\n      reviewers: [1, 2]\n      note: \"R2 提出 (W3)，R1 REBUT——pilot-based 分阶段决策不构成循环。分歧存在：R2 认为缺乏 cost-benefit 数字，R1 认为 N=8 pilot → decide → scale/abort 流程已合理。\"\n  action_items:\n    - round: 38\n      action: \"§7.5 或 §9 添加简要 cost analysis（N=8 诊断 vs N=64 全量）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== EARLIER ISSUES — STATUS UPDATE =====\n- id: R36-MF1\n  summary: \"标题 'Information Extraction' overclaim → 已改为 NER\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 33\n  last_seen_round: 37\n  mentions:\n    - round: 38\n      reviewers: [1, 2]\n      note: \"标题已为 NER，本轮未提及此问题。确认 resolved。但 R38 发现新标题 'Boundary Conditions' 有新的 overclaim 问题（见 R38-MF1）。\"\n  resolution: \"标题已改为 NER scope\"\n  resolution_round: 37\n\n- id: R36-SF1\n  summary: \"'Diagnostic cascade' 术语误导因果解读\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 36\n  last_seen_round: 37\n  mentions:\n    - round: 38\n      reviewers: []\n      note: \"本轮未提及。确认 resolved。\"\n  resolution: \"全文 cascade→framework\"\n  resolution_round: 37\n\n- id: R36-SF8\n  summary: \"Responsible NLP Checklist 不应在 PDF 中\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 36\n  last_seen_round: 37\n  mentions:\n    - round: 38\n      reviewers: []\n      note: \"本轮未提及。确认 resolved。\"\n  resolution: \"main.tex 中 checklist 已移除\"\n  resolution_round: 37\n"
  }
}
```

</details>

---


### Tool result

_source line 4095 · 2026-05-22T12:58:26.048684+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 10976}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 4096 · 2026-05-22T13:00:50.994962+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 38\n\n**论文**: When Does Test-Time Scaling Fail? Boundary Conditions for Named Entity Recognition\n**Venue**: EMNLP 2026 Long Paper (ARR May cycle)\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计；R2: 新颖性+完整性+写作）\n**圆桌轮次**: 1 轮（Round 1 后交叉分享，关键问题已收敛）\n\n---\n\n## Summary\n\n本文研究 test-time compute scaling（self-consistency / best-of-N）在 NER 上的失败条件。在 4 个 NER 数据集（SciERC、CoNLL-2003、Few-NERD、WNUT-17）上使用 Qwen3-8B 和 LLaMA-3.1-8B 进行实验，发现质量估计信号能预测输出质量（AUROC 最高 0.82），但 instance-level selection gain <1pp（即使 N=64），定义为 \"correlation-selection gap\"。提出 diagnostic framework 识别两个 co-occurring 失败条件：high output degeneracy（12–68%）和 signal alignment collapse（α→0）。Exploratory entity-level construction 在 Few-NERD 上获得 +1.40pp 提升（per-family Holm p=0.006; global Holm p=0.055）。扩展到 RE 和 SQL parsing 作为 exploratory pilot。\n\n---\n\n## Strengths\n\n**S1. 研究问题的 timeliness 和重要性。** TTS 在 reasoning 上的成功已被广泛验证，但在结构化输出任务上的 failure mode 缺乏系统研究。论文填补了真实的知识 gap。[R1 Excitement 4/5, R2 Excitement 3/5]\n\n**S2. 实验体量与统计严谨性出色。** 44 页论文（含 35 页 Appendix），4 NER 数据集 × 2 模型族 × 多种信号/选择策略全排列。统计方法覆盖 bootstrap 95% CI、Holm-Bonferroni 全局校正（k=57 全部 57 个检验枚举于 Table 12）、TOST 等价性检验、permutation test、split-half reliability。这在 NLP 实证研究中属上乘水准。[R1, R2 共识]\n\n**S3. Correlation-selection gap 是 genuine 且 well-documented 的新发现。** AUROC up to 0.82 但 selection gain <1pp 的 disconnect 在 4 个 NER 数据集 + 2 个模型上一致复现（Table 1, Table 3, Table 4），非 cherry-picked 结果。[R1, R2 共识]\n\n**S4. Negative results 的诚实报告。** Cross-dataset transfer 为负（§5.2）、entity construction 在 CoNLL 无增益、Holm 全局校正后 p=0.055、69% inverse scaling 等均如实报告。这种透明度值得肯定。[R1, R2 共识]\n\n**S5. MBR 理论连接有深度。** Appendix 将 entity construction 形式化为 MBR decoding 特例（Proposition 2），balanced set-overlap utility 下最优解刻画为理论发现提供了 formal grounding。[R2 highlighted]\n\n**S6. 多层次分析框架。** 从 population-level (QE → AUROC) → instance-level (ranking → selection) → entity-level (construction) 三个粒度递进分析，Discover → Diagnose → Explore bypasses 叙事结构有效。[R2 highlighted]\n\n---\n\n## Weaknesses\n\n### Must-Fix（4 项，两位 Reviewer 均达成共识）\n\n**MF1. [CRITICAL] Title \"Boundary Conditions\" 与实际交付 \"diagnostic correlations\" 之间存在 claim-evidence mismatch。** [R1 AGREE, R2 AGREE]\n\n\"Boundary conditions\" 在数学和科学中暗示 necessary/sufficient conditions。论文自身在 §6.3 和 §9 中反复使用 \"diagnostic rather than predictive\" 限定 framework 性质，与标题矛盾。Corollary 1 给出的 degeneracy threshold 精度极低（bound 仅 capture 3–12% actual gains），进一步削弱 \"boundary\" 的含义。\n\n→ **建议**：改为 \"Failure Modes\" (R1 建议) 或 \"Diagnostic Conditions\" (R2 建议)。两位 Reviewer 对替代措辞有分歧但对核心判断完全一致。\n\n**MF2. [CRITICAL] Degeneracy decomposition bound $(1-D) \\cdot G_{\\text{nd}} \\cdot \\alpha$ 仅 capture 3–12% actual gains，削弱 framework 的定量诊断价值。** [R1 raised, R2 AGREE]\n\nBound off by an order of magnitude（Figure 10）。Abstract 声称 \"guides practitioners on what to measure\" 但一个 10× loose 的 bound 无法提供 quantitative guidance。R2 补充：looseness 主要源于 entity independence 假设（split-half r=0.578–0.644 显示 entity 间有 correlation structure）。\n\n→ **建议**：(a) 正文显式讨论 looseness 来源（entity independence 假设 vs α 保守性），量化各因素贡献；(b) 将 bound 定位为 \"illustrative upper bound\" 而非 \"diagnostic tool\"；(c) 降低 Abstract/§9 的实践指导 claim。\n\n**MF3. [CRITICAL] Entity construction 69% inverse scaling (40/58 transitions)，\"bypass\" framing 严重过度。** [R1 raised, R2 AGREE]\n\n§6.2 报告 \"Increasing N decreases construction F1 in 40 of 58 transitions\"。LP-weighted construction 仅 Few-NERD 上 consistently positive (+1.40pp)，SciERC non-significant (+0.32pp)，CoNLL negative (−0.39pp)。Abstract/§1/§5/§9 多处 \"partially bypasses the bottleneck\" 与 69% failure 率直接矛盾。论文同时报告两个相互矛盾的 narrative——§5 将 entity construction 作为 bypass solution，§6.2 则报告 69% inverse scaling——读者需自行拼凑。\n\n→ **建议**：将 entity construction 明确定位为 \"conditional bypass: works only under low-degeneracy + LP-F1 alignment\"；Abstract/Introduction 调低 claim；主文直面 inverse scaling 矛盾。\n\n**MF4. [CRITICAL] 核心 positive result (Few-NERD LP selection) 在 global Holm-Bonferroni (k=57) 下 p_adj=0.055，跨越显著性边界。** [R1 raised, R2 AGREE; 跨轮复发——R34 首次提出]\n\nPer-family Holm (k=10): p_adj=0.006 → significant；Global Holm (k=57): p_adj=0.055 → non-significant。§7.5 先报告显著后报告不显著的呈现顺序有 framing bias（R2 指出）。Per-family 划分 \"independent mechanisms\" 论证不充分——三者共享 sampling pipeline 和 instance population，且未 pre-registered（R1 指出）。Few-NERD 是唯一 LP selection 产生实质性正面 gain 的数据集。\n\n→ **建议**：(a) 以 global correction 为主要报告，per-family 作为 sensitivity analysis；(b) Abstract 附 global p-value caveat；(c) 明确承认 per-family 划分未 pre-registered。\n\n### Should-Fix（10 项）\n\n**SF1. [WARNING] §3 Hidden-state probe 使用 Qwen2.5-7B 而非主实验 Qwen3-8B。** [R1, R2 共识; 跨轮复发——R36 首次提出]\n\nQwen3 架构（thinking mode、不同 attention）与 Qwen2.5 有显著差异。Probe AUROC 0.63–0.88 能否迁移到 Qwen3-8B 未验证。§9 将 probe 结论作为 general finding 使用是 over-reaching。建议至少在 Qwen3-8B 上做 1 组 key probe 或更显著地限定结论 scope。\n\n**SF2. [WARNING] Few-NERD \"positive contrast\" 受 3-epoch under-training confound 影响。** [R1 raised, R2 AGREE with nuance; 跨轮复发]\n\n5-epoch model degeneracy 从 ~13% 升至 31%，LP gain 从 +1.39 消失至 +0.12±0.04pp。Few-NERD 在全文被反复用作 positive anchor，但此 anchor 是 confounded 的。§7.5 仅两行讨论，不够 prominent。论文的 defense (\"sensitivity reinforces diagnostic value\") 逻辑上自洽，但应更突出讨论 ecological validity。\n\n**SF3. [WARNING] 与并发工作 arxiv 2603.12520 (correlation-selection gap in BoN reasoning) 的新颖性区分缺失。** [R2 raised; R1 REBUT——认为结构化输出 degeneracy 机制根本不同; 分歧未完全收敛]\n\nR1 的 rebut 有合理性——NER degeneracy 是 entity-set level collapse，与 reasoning BoN 的评分区分度问题机制不同。但该并发工作仍应被引用并讨论，以明确本文在 structured prediction 维度上的独特贡献。\n\n**SF4. [WARNING] 模型 scale 覆盖不足以支撑 cross-scale generalization claim。** [R1 raised, R2 partial REBUT; 跨轮复发]\n\n主实验 Qwen3-8B + LLaMA-3.1-8B 均为 8B 级别。72B 仅 SciERC 零样本，GPT-5.5 仅 200 instances pilot。R2 认为 \"two families\" 满足 \"multiple families\" 但 scale diversity 不足。建议 Limitations 更明确标注 scale 限制。\n\n**SF5. [WARNING] RE (n=397) / SQL (n=196) 证据强度与 abstract/intro 呈现权重不匹配。** [R1, R2 共识; 跨轮复发]\n\nAbstract 将 RE/SQL 与 NER 并列给人等权重印象。SQL pilot n=196 单数据集。建议进一步降格为 \"preliminary pilot\"。\n\n**SF6. [WARNING] Constrained decoding ablation 仅 2 数据集 (CoNLL + SciERC)，覆盖不足。** [R1, R2 共识]\n\nConstrained decoding 直接影响 output distribution 和 degeneracy 核心机制。Table 33 仅覆盖 SciERC + RE。Few-NERD free-form ablation 缺失。建议补充或讨论代表性。\n\n**SF7. [WARNING] Abstract 数字密度过高。** [R1, R2 共识; 跨轮复发]\n\nAbstract 塞入 AUROC 0.82、<1pp、N=64、12–68%、+1.40pp 等大量数字。建议精简至 3-4 个最关键数字。\n\n**SF8. [WARNING] 术语不一致：degeneracy / output convergence / convergence 交替使用。** [R1, R2 共识; 跨轮复发]\n\n§2 定义 \"degeneracy\" 后仍有混用，且与 \"training convergence\" 歧义。建议全文统一。\n\n**SF9. [WARNING] 与 Yao et al. (2026) 的增量新颖性区分在主文中不够 prominent。** [R2 raised, R1 partial AGREE; 跨轮复发]\n\n§1 三层区分存在但对非专家读者不够清晰。Table 66 differentiation matrix 在 Appendix，主文 §8 visibility 不足。\n\n**SF10. [WARNING] Diagnostic framework 实用价值缺乏 cost-benefit analysis。** [R2 raised, R1 REBUT; 分歧存在]\n\nR2 认为需先采样才能诊断，构成循环。R1 反驳：pilot-based 分阶段决策（N=8 诊断 → decide → scale/abort）不构成循环。两方都有道理——建议 §7.5 添加简要 cost analysis（N=8 pilot 成本 vs N=64 全量 scaling 成本）即可化解。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Title overclaims** — \"Boundary Conditions\" 暗示 formal necessary/sufficient conditions，但论文交付 diagnostic correlations\n2. **统计显著性敏感** — 核心 positive result 在 global correction 下 borderline non-significant (p=0.055)\n3. **Entity construction \"bypass\" 过度 framing** — 69% inverse scaling 与 \"partially bypasses\" narrative 矛盾\n4. **Bound looseness** — $(1-D) \\cdot G_{\\text{nd}} \\cdot \\alpha$ 仅 capture 3–12% actual gains\n5. **Probe 模型不匹配** — Qwen2.5-7B probe 结论不能无条件迁移至 Qwen3-8B\n6. **RE/SQL 证据薄弱** — n=397/n=196 不足以支撑 abstract 级别呈现\n7. **Abstract 数字过密 + 术语不一致** — 写作质量可改善\n\n## Reviewer Divergence [REBUT]\n\n1. **并发工作 novelty** (R38-SF3) — R2 认为 arxiv 2603.12520 发现了本质相同的 correlation-selection gap；R1 REBUT 认为结构化输出的 degeneracy 机制（entity-set collapse）与 BoN reasoning（评分区分度）根本不同。**Director 判断**：R1 的 rebut 合理，但该工作仍应被引用讨论。降为 Should-Fix。\n2. **Diagnostic circularity** (R38-SF10) — R2 认为需先采样才能诊断构成循环；R1 REBUT 认为 pilot-based 分阶段决策合理。**Director 判断**：R1 rebut 有效，但论文应添加 cost-benefit 数字以增强说服力。降为 Should-Fix。\n3. **模型 scale 多样性** (R38-SF4) — R1 认为不足以支撑 \"multiple families\" claim；R2 partial REBUT 认为 two architecture families 已满足但 scale 不足。**Director 判断**：claim 范围应限定为 \"7–14B open-weight\"，scale generalization 在 Limitations 中明确标注。\n\n---\n\n## Questions for Authors\n\n**Q1** (from R1): Degeneracy bound looseness 主要来自 entity independence 假设还是 α 保守估计？能否量化各因素贡献？\n\n**Q2** (from R1): 如果 global Holm p=0.055 下 Few-NERD LP selection 不 significant，论文核心叙事如何调整？\n\n**Q3** (from R1): Entity construction inverse scaling 69% 的情况下，practitioners 在什么具体条件下应使用 entity construction？degeneracy <20% 且 LP-F1 ρ >0.2 是充分条件吗？\n\n**Q4** (from R1, R2): 是否尝试过 Qwen3-8B hidden states（去掉 thinking tokens）训练 probe？\n\n**Q5** (from R1): Few-NERD 5-epoch degeneracy 升至 31% 后 LP gain 消失——LP selection 是否仅在模型 under-converged 时有效？\n\n**Q6** (from R2): Title 为什么用 \"Boundary Conditions\" 而非 \"Failure Modes\" 或 \"Diagnostic Conditions\"？\n\n**Q7** (from R2): arxiv 2603.12520 在 BoN 设置下发现了几乎相同的 correlation-selection gap 现象——如何界定本文的独立贡献？\n\n---\n\n## Missing References\n\n**必须添加**:\n1. \"When LLM Judge Scores Look Good but Best-of-N Decisions Fail\" (arxiv 2603.12520, March 2026) — 并发工作，correlation-selection gap in BoN reasoning [R2 raised, R1 认为应引用但机制不同]\n\n**推荐添加**:\n2. \"Conformal Structured Prediction\" (Angelopoulos et al., ICLR 2025) — 结构化输出 conformal prediction [R2]\n3. \"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\" (He et al., NAACL Findings 2024) — token-level uncertainty for NER [R2]\n4. \"Conformal Prediction for Natural Language Processing: A Survey\" (TACL 2024/2025) [R2]\n5. \"LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty\" (WWW 2024) [R2]\n6. Malinin and Gales (2021) \"Uncertainty Estimation in Autoregressive Structured Prediction\" [R1]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未启用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（耗时约 5 分钟）。0 critical / 0 warning / 8 info。\n\n主要发现：\n- 首页无 display item（Figure 1 在第 2 页顶部），ACL 格式下正常\n- Page 7 视觉密度极高（单页 3 个 display items：Table 3 + Table 4 + Figure 4）\n- Page 8（最后一页正文）纯文本，无 display item\n- Table 2 部分缩写列字号偏小，快速扫描可读性一般\n- Appendix 中 Table 12（57 行）和 Tables 13–22 字号接近可读性下限，appendix 标准可接受\n\n无排版硬伤，不影响评分。\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 — Findings**\n**置信度: 4/5**\n\n**评分依据**:\n\n两位 Reviewer 独立给出 3.5 (Borderline Conference)，但交叉分享后多个 Must-Fix 问题得到强化确认，综合考虑后下调至 3.0：\n\n1. **核心 negative finding 有价值但 framing 系统性过度**：correlation-selection gap 本身是 genuine 且 well-documented 的发现（S3），但论文在 title（\"Boundary Conditions\"）、theoretical contribution（bound 仅 capture 3-12%）、prescriptive contribution（entity construction 69% inverse scaling）三个维度上均存在 claim-evidence mismatch。这不是单点问题，而是全文 framing 与实际证据强度之间的系统性 gap。\n\n2. **唯一的 positive contrast 统计上脆弱且 confounded**：Few-NERD LP selection 是论文叙事的核心 anchor，但 (a) 在 global correction 下 borderline non-significant (p=0.055)，(b) 受 3-epoch under-training confound 影响（5-epoch 下 LP gain 消失），(c) entity construction 的 Few-NERD gain 也在多数 N-scaling 配置上 inverse scaling。\n\n3. **跨轮复发问题未彻底解决**：multiple testing sensitivity（首次 R34）、probe 模型不匹配（首次 R36）、Yao et al. 区分（首次 R35）、abstract 密度（首次 R37）等问题在本轮再次被独立发现。\n\n**Conference vs Findings 判断**：论文的实验 thoroughness（S2）和问题重要性（S1）使其具备 Findings 水平。但 4 个 Must-Fix 问题（title overclaim、bound looseness、bypass over-framing、statistical sensitivity）均涉及 contribution narrative 的根基，在这些问题解决之前，论文的 contribution 定位不够清晰——读者难以判断应该 take away 什么。如果 re-framing 为 \"comprehensive negative result + conditional positive finding\" 并调低 prescriptive claims，论文可达 Conference 水平。当前版本定为 Findings。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"correlation-selection gap\" 的定义清晰有效，但 \"partially bypasses the bottleneck\" (+1.40pp) 需要附 global Holm p=0.055 caveat\n- 三阶段 (Discover → Diagnose → Explore bypasses) 结构好，但第三阶段的 delivery 不足以支撑 \"bypass\" 的含义\n\n### §2 Diagnostic Framework\n- Per-sample vs instance-level signal 的区分（§2.1）是重要的方法论贡献\n- Instance degeneracy 的定义（§2.3）清晰，但后续使用中术语不一致\n\n### §3 How Self-Verification Fails\n- ESJ/MRSC/LSC 的 negative results 有诊断价值\n- **核心问题**：全部基于 Qwen2.5-7B，§9 将其作为 general conclusion 使用是 over-reaching\n- Introspection boundary 概念有趣，但 LODO transfer drops (0.56–0.67) 已削弱其通用性\n\n### §4 Where Single-Signal Selection Fails\n- Table 3 的 correlation-selection gap 呈现清晰有效\n- \"Definitional vs empirical\" 两层分解是论文的亮点\n\n### §5 Adaptive Methods\n- Table 2 的 9 类方法汇总有参考价值\n- Cross-model self-consistency (+0.42pp) 是唯一 unconditional positive result，值得更多讨论\n\n### §6 Threshold Regime Analysis\n- MBR 连接（§6.1）理论上优雅\n- **核心问题**：§6.2 inverse scaling 69% 与 §5 的 bypass narrative 矛盾\n- §6.3 bound looseness 需要正文级别的讨论\n\n### §7 Experiments\n- 实验设计 thorough，4 数据集覆盖 difficulty gradient\n- Few-NERD epoch confound 需更 prominent 讨论\n- Robustness analysis (§7.4) 展示了 signal ranking 的稳定性，是 strength\n\n### §8 Related Work\n- 与 Yao et al. 和 Yun et al. 的区分存在但 visibility 不足\n- 缺少 arxiv 2603.12520 的讨论\n- Conformal prediction 覆盖不够（仅引用 gentle introduction，未讨论 structured prediction 最新进展）\n\n### §9 Discussion/Conclusion\n- \"Diagnostic rather than predictive\" 定位合适，但与 title \"Boundary Conditions\" 矛盾\n- Practical implications 段落缺 cost-benefit analysis\n- 作为论文的 conclusion，对 open questions 和 generalizability 的讨论可以更深入\n",
  "project": "struct_self_consist_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 — Findings",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 38\n\n**论文**: When Does Test-Time Scaling Fail? Boundary Conditions for Named Entity Recognition\n**Venue**: EMNLP 2026 Long Paper (ARR May cycle)\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计；R2: 新颖性+完整性+写作）\n**圆桌轮次**: 1 轮（Round 1 后交叉分享，关键问题已收敛）\n\n---\n\n## Summary\n\n本文研究 test-time compute scaling（self-consistency / best-of-N）在 NER 上的失败条件。在 4 个 NER 数据集（SciERC、CoNLL-2003、Few-NERD、WNUT-17）上使用 Qwen3-8B 和 LLaMA-3.1-8B 进行实验，发现质量估计信号能预测输出质量（AUROC 最高 0.82），但 instance-level selection gain <1pp（即使 N=64），定义为 \"correlation-selection gap\"。提出 diagnostic framework 识别两个 co-occurring 失败条件：high output degeneracy（12–68%）和 signal alignment collapse（α→0）。Exploratory entity-level construction 在 Few-NERD 上获得 +1.40pp 提升（per-family Holm p=0.006; global Holm p=0.055）。扩展到 RE 和 SQL parsing 作为 exploratory pilot。\n\n---\n\n## Strengths\n\n**S1. 研究问题的 timeliness 和重要性。** TTS 在 reasoning 上的成功已被广泛验证，但在结构化输出任务上的 failure mode 缺乏系统研究。论文填补了真实的知识 gap。[R1 Excitement 4/5, R2 Excitement 3/5]\n\n**S2. 实验体量与统计严谨性出色。** 44 页论文（含 35 页 Appendix），4 NER 数据集 × 2 模型族 × 多种信号/选择策略全排列。统计方法覆盖 bootstrap 95% CI、Holm-Bonferroni 全局校正（k=57 全部 57 个检验枚举于 Table 12）、TOST 等价性检验、permutation test、split-half reliability。这在 NLP 实证研究中属上乘水准。[R1, R2 共识]\n\n**S3. Correlation-selection gap 是 genuine 且 well-documented 的新发现。** AUROC up to 0.82 但 selection gain <1pp 的 disconnect 在 4 个 NER 数据集 + 2 个模型上一致复现（Table 1, Table 3, Table 4），非 cherry-picked 结果。[R1, R2 共识]\n\n**S4. Negative results 的诚实报告。** Cross-dataset transfer 为负（§5.2）、entity construction 在 CoNLL 无增益、Holm 全局校正后 p=0.055、69% inverse scaling 等均如实报告。这种透明度值得肯定。[R1, R2 共识]\n\n**S5. MBR 理论连接有深度。** Appendix 将 entity construction 形式化为 MBR decoding 特例（Proposition 2），balanced set-overlap utility 下最优解刻画为理论发现提供了 formal grounding。[R2 highlighted]\n\n**S6. 多层次分析框架。** 从 population-level (QE → AUROC) → instance-level (ranking → selection) → entity-level (construction) 三个粒度递进分析，Discover → Diagnose → Explore bypasses 叙事结构有效。[R2 highlighted]\n\n---\n\n## Weaknesses\n\n### Must-Fix（4 项，两位 Reviewer 均达成共识）\n\n**MF1. [CRITICAL] Title \"Boundary Conditions\" 与实际交付 \"diagnostic correlations\" 之间存在 claim-evidence mismatch。** [R1 AGREE, R2 AGREE]\n\n\"Boundary conditions\" 在数学和科学中暗示 necessary/sufficient conditions。论文自身在 §6.3 和 §9 中反复使用 \"diagnostic rather than predictive\" 限定 framework 性质，与标题矛盾。Corollary 1 给出的 degeneracy threshold 精度极低（bound 仅 capture 3–12% actual gains），进一步削弱 \"boundary\" 的含义。\n\n→ **建议**：改为 \"Failure Modes\" (R1 建议) 或 \"Diagnostic Conditions\" (R2 建议)。两位 Reviewer 对替代措辞有分歧但对核心判断完全一致。\n\n**MF2. [CRITICAL] Degeneracy decomposition bound $(1-D) \\cdot G_{\\text{nd}} \\cdot \\alpha$ 仅 capture 3–12% actual gains，削弱 framework 的定量诊断价值。** [R1 raised, R2 AGREE]\n\nBound off by an order of magnitude（Figure 10）。Abstract 声称 \"guides practitioners on what to measure\" 但一个 10× loose 的 bound 无法提供 quantitative guidance。R2 补充：looseness 主要源于 entity independence 假设（split-half r=0.578–0.644 显示 entity 间有 correlation structure）。\n\n→ **建议**：(a) 正文显式讨论 looseness 来源（entity independence 假设 vs α 保守性），量化各因素贡献；(b) 将 bound 定位为 \"illustrative upper bound\" 而非 \"diagnostic tool\"；(c) 降低 Abstract/§9 的实践指导 claim。\n\n**MF3. [CRITICAL] Entity construction 69% inverse scaling (40/58 transitions)，\"bypass\" framing 严重过度。** [R1 raised, R2 AGREE]\n\n§6.2 报告 \"Increasing N decreases construction F1 in 40 of 58 transitions\"。LP-weighted construction 仅 Few-NERD 上 consistently positive (+1.40pp)，SciERC non-significant (+0.32pp)，CoNLL negative (−0.39pp)。Abstract/§1/§5/§9 多处 \"partially bypasses the bottleneck\" 与 69% failure 率直接矛盾。论文同时报告两个相互矛盾的 narrative——§5 将 entity construction 作为 bypass solution，§6.2 则报告 69% inverse scaling——读者需自行拼凑。\n\n→ **建议**：将 entity construction 明确定位为 \"conditional bypass: works only under low-degeneracy + LP-F1 alignment\"；Abstract/Introduction 调低 claim；主文直面 inverse scaling 矛盾。\n\n**MF4. [CRITICAL] 核心 positive result (Few-NERD LP selection) 在 global Holm-Bonferroni (k=57) 下 p_adj=0.055，跨越显著性边界。** [R1 raised, R2 AGREE; 跨轮复发——R34 首次提出]\n\nPer-family Holm (k=10): p_adj=0.006 → significant；Global Holm (k=57): p_adj=0.055 → non-significant。§7.5 先报告显著后报告不显著的呈现顺序有 framing bias（R2 指出）。Per-family 划分 \"independent mechanisms\" 论证不充分——三者共享 sampling pipeline 和 instance population，且未 pre-registered（R1 指出）。Few-NERD 是唯一 LP selection 产生实质性正面 gain 的数据集。\n\n→ **建议**：(a) 以 global correction 为主要报告，per-family 作为 sensitivity analysis；(b) Abstract 附 global p-value caveat；(c) 明确承认 per-family 划分未 pre-registered。\n\n### Should-Fix（10 项）\n\n**SF1. [WARNING] §3 Hidden-state probe 使用 Qwen2.5-7B 而非主实验 Qwen3-8B。** [R1, R2 共识; 跨轮复发——R36 首次提出]\n\nQwen3 架构（thinking mode、不同 attention）与 Qwen2.5 有显著差异。Probe AUROC 0.63–0.88 能否迁移到 Qwen3-8B 未验证。§9 将 probe 结论作为 general finding 使用是 over-reaching。建议至少在 Qwen3-8B 上做 1 组 key probe 或更显著地限定结论 scope。\n\n**SF2. [WARNING] Few-NERD \"positive contrast\" 受 3-epoch under-training confound 影响。** [R1 raised, R2 AGREE with nuance; 跨轮复发]\n\n5-epoch model degeneracy 从 ~13% 升至 31%，LP gain 从 +1.39 消失至 +0.12±0.04pp。Few-NERD 在全文被反复用作 positive anchor，但此 anchor 是 confounded 的。§7.5 仅两行讨论，不够 prominent。论文的 defense (\"sensitivity reinforces diagnostic value\") 逻辑上自洽，但应更突出讨论 ecological validity。\n\n**SF3. [WARNING] 与并发工作 arxiv 2603.12520 (correlation-selection gap in BoN reasoning) 的新颖性区分缺失。** [R2 raised; R1 REBUT——认为结构化输出 degeneracy 机制根本不同; 分歧未完全收敛]\n\nR1 的 rebut 有合理性——NER degeneracy 是 entity-set level collapse，与 reasoning BoN 的评分区分度问题机制不同。但该并发工作仍应被引用并讨论，以明确本文在 structured prediction 维度上的独特贡献。\n\n**SF4. [WARNING] 模型 scale 覆盖不足以支撑 cross-scale generalization claim。** [R1 raised, R2 partial REBUT; 跨轮复发]\n\n主实验 Qwen3-8B + LLaMA-3.1-8B 均为 8B 级别。72B 仅 SciERC 零样本，GPT-5.5 仅 200 instances pilot。R2 认为 \"two families\" 满足 \"multiple families\" 但 scale diversity 不足。建议 Limitations 更明确标注 scale 限制。\n\n**SF5. [WARNING] RE (n=397) / SQL (n=196) 证据强度与 abstract/intro 呈现权重不匹配。** [R1, R2 共识; 跨轮复发]\n\nAbstract 将 RE/SQL 与 NER 并列给人等权重印象。SQL pilot n=196 单数据集。建议进一步降格为 \"preliminary pilot\"。\n\n**SF6. [WARNING] Constrained decoding ablation 仅 2 数据集 (CoNLL + SciERC)，覆盖不足。** [R1, R2 共识]\n\nConstrained decoding 直接影响 output distribution 和 degeneracy 核心机制。Table 33 仅覆盖 SciERC + RE。Few-NERD free-form ablation 缺失。建议补充或讨论代表性。\n\n**SF7. [WARNING] Abstract 数字密度过高。** [R1, R2 共识; 跨轮复发]\n\nAbstract 塞入 AUROC 0.82、<1pp、N=64、12–68%、+1.40pp 等大量数字。建议精简至 3-4 个最关键数字。\n\n**SF8. [WARNING] 术语不一致：degeneracy / output convergence / convergence 交替使用。** [R1, R2 共识; 跨轮复发]\n\n§2 定义 \"degeneracy\" 后仍有混用，且与 \"training convergence\" 歧义。建议全文统一。\n\n**SF9. [WARNING] 与 Yao et al. (2026) 的增量新颖性区分在主文中不够 prominent。** [R2 raised, R1 partial AGREE; 跨轮复发]\n\n§1 三层区分存在但对非专家读者不够清晰。Table 66 differentiation matrix 在 Appendix，主文 §8 visibility 不足。\n\n**SF10. [WARNING] Diagnostic framework 实用价值缺乏 cost-benefit analysis。** [R2 raised, R1 REBUT; 分歧存在]\n\nR2 认为需先采样才能诊断，构成循环。R1 反驳：pilot-based 分阶段决策（N=8 诊断 → decide → scale/abort）不构成循环。两方都有道理——建议 §7.5 添加简要 cost analysis（N=8 pilot 成本 vs N=64 全量 scaling 成本）即可化解。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Title overclaims** — \"Boundary Conditions\" 暗示 formal necessary/sufficient conditions，但论文交付 diagnostic correlations\n2. **统计显著性敏感** — 核心 positive result 在 global correction 下 borderline non-significant (p=0.055)\n3. **Entity construction \"bypass\" 过度 framing** — 69% inverse scaling 与 \"partially bypasses\" narrative 矛盾\n4. **Bound looseness** — $(1-D) \\cdot G_{\\text{nd}} \\cdot \\alpha$ 仅 capture 3–12% actual gains\n5. **Probe 模型不匹配** — Qwen2.5-7B probe 结论不能无条件迁移至 Qwen3-8B\n6. **RE/SQL 证据薄弱** — n=397/n=196 不足以支撑 abstract 级别呈现\n7. **Abstract 数字过密 + 术语不一致** — 写作质量可改善\n\n## Reviewer Divergence [REBUT]\n\n1. **并发工作 novelty** (R38-SF3) — R2 认为 arxiv 2603.12520 发现了本质相同的 correlation-selection gap；R1 REBUT 认为结构化输出的 degeneracy 机制（entity-set collapse）与 BoN reasoning（评分区分度）根本不同。**Director 判断**：R1 的 rebut 合理，但该工作仍应被引用讨论。降为 Should-Fix。\n2. **Diagnostic circularity** (R38-SF10) — R2 认为需先采样才能诊断构成循环；R1 REBUT 认为 pilot-based 分阶段决策合理。**Director 判断**：R1 rebut 有效，但论文应添加 cost-benefit 数字以增强说服力。降为 Should-Fix。\n3. **模型 scale 多样性** (R38-SF4) — R1 认为不足以支撑 \"multiple families\" claim；R2 partial REBUT 认为 two architecture families 已满足但 scale 不足。**Director 判断**：claim 范围应限定为 \"7–14B open-weight\"，scale generalization 在 Limitations 中明确标注。\n\n---\n\n## Questions for Authors\n\n**Q1** (from R1): Degeneracy bound looseness 主要来自 entity independence 假设还是 α 保守估计？能否量化各因素贡献？\n\n**Q2** (from R1): 如果 global Holm p=0.055 下 Few-NERD LP selection 不 significant，论文核心叙事如何调整？\n\n**Q3** (from R1): Entity construction inverse scaling 69% 的情况下，practitioners 在什么具体条件下应使用 entity construction？degeneracy <20% 且 LP-F1 ρ >0.2 是充分条件吗？\n\n**Q4** (from R1, R2): 是否尝试过 Qwen3-8B hidden states（去掉 thinking tokens）训练 probe？\n\n**Q5** (from R1): Few-NERD 5-epoch degeneracy 升至 31% 后 LP gain 消失——LP selection 是否仅在模型 under-converged 时有效？\n\n**Q6** (from R2): Title 为什么用 \"Boundary Conditions\" 而非 \"Failure Modes\" 或 \"Diagnostic Conditions\"？\n\n**Q7** (from R2): arxiv 2603.12520 在 BoN 设置下发现了几乎相同的 correlation-selection gap 现象——如何界定本文的独立贡献？\n\n---\n\n## Missing References\n\n**必须添加**:\n1. \"When LLM Judge Scores Look Good but Best-of-N Decisions Fail\" (arxiv 2603.12520, March 2026) — 并发工作，correlation-selection gap in BoN reasoning [R2 raised, R1 认为应引用但机制不同]\n\n**推荐添加**:\n2. \"Conformal Structured Prediction\" (Angelopoulos et al., ICLR 2025) — 结构化输出 conformal prediction [R2]\n3. \"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\" (He et al., NAACL Findings 2024) — token-level uncertainty for NER [R2]\n4. \"Conformal Prediction for Natural Language Processing: A Survey\" (TACL 2024/2025) [R2]\n5. \"LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty\" (WWW 2024) [R2]\n6. Malinin and Gales (2021) \"Uncertainty Estimation in Autoregressive Structured Prediction\" [R1]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未启用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（耗时约 5 分钟）。0 critical / 0 warning / 8 info。\n\n主要发现：\n- 首页无 display item（Figure 1 在第 2 页顶部），ACL 格式下正常\n- Page 7 视觉密度极高（单页 3 个 display items：Table 3 + Table 4 + Figure 4）\n- Page 8（最后一页正文）纯文本，无 display item\n- Table 2 部分缩写列字号偏小，快速扫描可读性一般\n- Appendix 中 Table 12（57 行）和 Tables 13–22 字号接近可读性下限，appendix 标准可接受\n\n无排版硬伤，不影响评分。\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 — Findings**\n**置信度: 4/5**\n\n**评分依据**:\n\n两位 Reviewer 独立给出 3.5 (Borderline Conference)，但交叉分享后多个 Must-Fix 问题得到强化确认，综合考虑后下调至 3.0：\n\n1. **核心 negative finding 有价值但 framing 系统性过度**：correlation-selection gap 本身是 genuine 且 well-documented 的发现（S3），但论文在 title（\"Boundary Conditions\"）、theoretical contribution（bound 仅 capture 3-12%）、prescriptive contribution（entity construction 69% inverse scaling）三个维度上均存在 claim-evidence mismatch。这不是单点问题，而是全文 framing 与实际证据强度之间的系统性 gap。\n\n2. **唯一的 positive contrast 统计上脆弱且 confounded**：Few-NERD LP selection 是论文叙事的核心 anchor，但 (a) 在 global correction 下 borderline non-significant (p=0.055)，(b) 受 3-epoch under-training confound 影响（5-epoch 下 LP gain 消失），(c) entity construction 的 Few-NERD gain 也在多数 N-scaling 配置上 inverse scaling。\n\n3. **跨轮复发问题未彻底解决**：multiple testing sensitivity（首次 R34）、probe 模型不匹配（首次 R36）、Yao et al. 区分（首次 R35）、abstract 密度（首次 R37）等问题在本轮再次被独立发现。\n\n**Conference vs Findings 判断**：论文的实验 thoroughness（S2）和问题重要性（S1）使其具备 Findings 水平。但 4 个 Must-Fix 问题（title overclaim、bound looseness、bypass over-framing、statistical sensitivity）均涉及 contribution narrative 的根基，在这些问题解决之前，论文的 contribution 定位不够清晰——读者难以判断应该 take away 什么。如果 re-framing 为 \"comprehensive negative result + conditional positive finding\" 并调低 prescriptive claims，论文可达 Conference 水平。当前版本定为 Findings。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"correlation-selection gap\" 的定义清晰有效，但 \"partially bypasses the bottleneck\" (+1.40pp) 需要附 global Holm p=0.055 caveat\n- 三阶段 (Discover → Diagnose → Explore bypasses) 结构好，但第三阶段的 delivery 不足以支撑 \"bypass\" 的含义\n\n### §2 Diagnostic Framework\n- Per-sample vs instance-level signal 的区分（§2.1）是重要的方法论贡献\n- Instance degeneracy 的定义（§2.3）清晰，但后续使用中术语不一致\n\n### §3 How Self-Verification Fails\n- ESJ/MRSC/LSC 的 negative results 有诊断价值\n- **核心问题**：全部基于 Qwen2.5-7B，§9 将其作为 general conclusion 使用是 over-reaching\n- Introspection boundary 概念有趣，但 LODO transfer drops (0.56–0.67) 已削弱其通用性\n\n### §4 Where Single-Signal Selection Fails\n- Table 3 的 correlation-selection gap 呈现清晰有效\n- \"Definitional vs empirical\" 两层分解是论文的亮点\n\n### §5 Adaptive Methods\n- Table 2 的 9 类方法汇总有参考价值\n- Cross-model self-consistency (+0.42pp) 是唯一 unconditional positive result，值得更多讨论\n\n### §6 Threshold Regime Analysis\n- MBR 连接（§6.1）理论上优雅\n- **核心问题**：§6.2 inverse scaling 69% 与 §5 的 bypass narrative 矛盾\n- §6.3 bound looseness 需要正文级别的讨论\n\n### §7 Experiments\n- 实验设计 thorough，4 数据集覆盖 difficulty gradient\n- Few-NERD epoch confound 需更 prominent 讨论\n- Robustness analysis (§7.4) 展示了 signal ranking 的稳定性，是 strength\n\n### §8 Related Work\n- 与 Yao et al. 和 Yun et al. 的区分存在但 visibility 不足\n- 缺少 arxiv 2603.12520 的讨论\n- Conformal prediction 覆盖不够（仅引用 gentle introduction，未讨论 structured prediction 最新进展）\n\n### §9 Discussion/Conclusion\n- \"Diagnostic rather than predictive\" 定位合适，但与 title \"Boundary Conditions\" 矛盾\n- Practical implications 段落缺 cost-benefit analysis\n- 作为论文的 conclusion，对 open questions 和 generalizability 的讨论可以更深入\n",
    "project": "struct_self_consist_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 — Findings",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 4097 · 2026-05-22T13:00:55.756349+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4761
}
```

</details>

---


### Tool call

_source line 4098 · 2026-05-22T13:01:07.840250+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: Venue 调研 + 资料检查', 'status': 'completed', 'activeForm': '完成 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 视觉审查派发', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断审稿意见是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'completed', 'activeForm': '汇总并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: Venue 调研 + 资料检查', 'status': 'completed', 'activeForm': '完成 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 视觉审查派发', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断审稿意见是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'completed', 'activeForm': '汇总并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 4099 · 2026-05-22T13:01:07.991324+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 151
}
```

</details>

---


### Assistant

_source line 4100 · 2026-05-22T13:01:17.165985+00:00_

**Round 38 审稿完成。**

审稿报告已投递至 Research Director。

**最终评分：3.0 — Findings**

核心判断：
- **4 个 Must-Fix**：title overclaim ("Boundary Conditions" vs diagnostic correlations)、bound looseness (3-12%)、entity construction 69% inverse scaling 与 "bypass" framing 矛盾、核心 positive result global Holm p=0.055
- **10 个 Should-Fix**：probe 模型不匹配、Few-NERD epoch confound、并发工作引用缺失、scale 覆盖不足、RE/SQL 证据薄弱、constrained decoding ablation 不足、abstract 数字过密、术语不一致、Yao et al. 区分不够、缺 cost-benefit analysis
- **2 个分歧点**（已在报告中标注）：并发工作 novelty 评估（R1 rebut 有效）、diagnostic circularity（R1 rebut 有效但需补数字）
- Issue Tracker 已同步更新（`review_issues.yaml`），含 4 critical + 10 warning，3 个历史 issue 确认 resolved

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 312

## Round 312

2 recorded events


### User

_source line 4101 · 2026-05-22T13:01:19.851102+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。8 条中同意 7 条（含 2 条 nuanced agree），仅对 W3（模型多样性）部分反驳——认为 two families 已构成 "multiple families"，但 scale diversity 确实不足。与 R1 最大的共识集中在 entity construction 的 statistical significance（N2/N3）和 title overclaim 两个核心问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 4102 · 2026-05-22T13:01:27.456456+00:00_

Round 38 审稿流程全部完成。

**最终结果**：Overall **3.0 — Findings**，置信度 4/5。

审稿报告已投递至 Research Director。核心判断：correlation-selection gap 是 genuine 发现，但论文在 title（"Boundary Conditions"）、理论贡献（bound 仅 3-12%）、prescriptive 贡献（entity construction 69% inverse scaling）三个维度上 framing 系统性过度。4 个 Must-Fix + 10 个 Should-Fix。Issue Tracker 已同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 313

## Round 313

70 recorded events


### User

_source line 4103 · 2026-05-22T13:31:27.430443+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 4104 · 2026-05-22T13:31:33.614307+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 4105 · 2026-05-22T13:31:33.715969+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 4106 · 2026-05-22T13:31:38.948918+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,director_post_to_reviewer,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,director_post_to_reviewer,request_external_review,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 4107 · 2026-05-22T13:31:38.949415+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 4108 · 2026-05-22T13:31:42.613321+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 4109 · 2026-05-22T13:31:42.613746+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 4110 · 2026-05-22T13:31:45.475942+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 4111 · 2026-05-22T13:31:45.476296+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 4112 · 2026-05-22T13:31:50.495283+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 4113 · 2026-05-22T13:31:51.448967+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (324 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp_conll_freeform_n8_s42 | Free-form decoding ablation: CoNLL N=8 T=1.0 seed=42 with use_grammar=False. Tests whether removing XGrammar constrained decoding degrades extraction quality and consistency scores, quantifying the contribution of grammar constraints to the structured self-consistency pipeline. | — | — | — |\n| exp_fewnerd_freeform_n8_s42 | R35-W6 free-form decoding ablation: FewNERD N=8 T=1.0 seed=42 without grammar constraints. FewNERD has lowest degeneracy (12% at N=8). If free-form degeneracy remains low (~12%), confirms degeneracy is model-intrinsic, not a constrained decoding artifact. Complements CoNLL free-form ablation (59.3% vs 56.7% constrained). | — | — | — |\n| exp_fewnerd_5epoch_lp_s42 | FewNERD 5-epoch checkpoint with LP selection will show improved F1 over majority voting, similar to the 3-epoch results, validating that LP selection is robust across training epochs | — | — | — |\n\n## 待处理\n- exp_fewnerd_mf4v2_s123_v4: FewNERD MF4v2 s123 v4: regenerate finetuned FewNERD seed=123 instance-level samples.jsonl on autodl-5090-c for v4 MV unified recompute. N=8, T=1.0, seed=123. Model: qw
…[truncated 1744 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 4114 · 2026-05-22T13:31:51.599977+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 4115 · 2026-05-22T13:31:51.951756+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{amsthm}
16	\newtheorem{proposition}{Proposition}
17	\newtheorem{theorem}{Theorem}
18	\newtheorem{corollary}{Corollary}
19	\newtheorem{definition}{Definition}
20	\usepackage{multirow}
21	\usepackage{xcolor}
22	\usepackage{subcaption}
23	\usepackage{alphalph}
24	\usepackage{enumitem}
25	
26	\graphicspath{{figures/}}
27	
28	\title{When Does Test-Time Scaling Fail?\\ A Diagnostic Framework for Named Entity Recognition}
29	
30	\author{Anonymous}
31	
32	\begin{document}
33	\maketitle
34	
35	\input{sections/abstract}
36	\input{sections/introduction}
37	\input{sections/diagnostic}
38	\input{sections/mechanistic}
39	\input{sections/single_signal}
40	\input{sections/adaptive}
41	\input{sections/theory}
42	\input{sections/experiments_main}
43	\input{sections/background}
44	\input{sections/discussion}
45	
46	\section*{Limitations}
47	\input{sections/limitations}
48	
49	\section*{Ethics Statement}
50	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, Few-NERD, WNUT-17), open-weight models (Qwen3-8B, Qwen3-14B, Qwen3-4B, LLaMA-3.1-8B), and the GPT-5.5 API.
51	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
52	No new human data was collected or annotated for this study.
53	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
54	Code and data will be released upon acceptance at [anonymized URL].
55	
56	\bibliography{references}
57	
58	\appendix
59	\renewcommand{\thesection}{\alphalph{\value{section}}}
60	\input
…[truncated 45 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 4116 · 2026-05-22T13:31:53.106208+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool call

_source line 4117 · 2026-05-22T13:31:53.307418+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 4118 · 2026-05-22T13:31:53.408252+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 4119 · 2026-05-22T13:32:01.287622+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"EMNLP 2026 Workshop WiNLP ARR Commitment | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FWorkshop%2FWiNLP_ARR_Commitment"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"}]

Based on the search results, here's information about EMNLP 2026 call for papers and ARR submission gui
…[truncated 1794 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 8181
}
```

</details>

---


### Tool call

_source line 4120 · 2026-05-22T13:32:11.833505+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool call

_source line 4121 · 2026-05-22T13:32:11.833844+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool call

_source line 4122 · 2026-05-22T13:32:11.834068+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
  }
}
```

</details>

---


### Tool result

_source line 4123 · 2026-05-22T13:32:11.934710+00:00_

1	\begin{abstract}
2	Test-time compute scaling---repeated sampling with self-consistency or best-of-$N$---yields large gains on discrete-answer reasoning, but whether these gains transfer to NER remains open.
3	We characterize when scaling succeeds and fails, using NER (four datasets, primarily 7--14B fine-tuned) as the primary case study with preliminary RE and SQL pilots.
4	Quality estimation signals predict output quality (AUROC up to $0.82$), yet instance-level selection yields ${<}1$\,pp, revealing a \textbf{correlation-selection gap}.
5	A diagnostic framework identifies two co-occurring conditions---\textit{degeneracy} (i.e., multiple outputs collapsing to identical predictions) and signal alignment collapse---that jointly determine scaling returns; cross-task exploration confirms task-specific failure modes.
6	Entity-level construction yields conditional gains ($+1.40$\,pp on Few-NERD under low degeneracy and LP alignment) but exhibits inverse scaling in most configurations (69\% of $N$-transitions), underscoring the framework's diagnostic value over prescriptive remedy.
7	The framework is diagnostic rather than predictive, informing resource allocation decisions before investing in repeated inference.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 4124 · 2026-05-22T13:32:11.935172+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time compute scaling---self-consistency \cite{wang2023selfconsistency}, best-of-$N$ \cite{snell2025scaling, brown2024monkeys}, extended reasoning \cite{muennighoff2025s1}---yields large gains on discrete-answer tasks where outputs admit equivalence classes or execution-based verification.
4	For NER, where outputs are entity sets with partial overlap, the boundary conditions for effective scaling are unknown; prior work \cite{yao2026consistency, yun2025price} provides initial observations but no systematic diagnostic framework quantifying failure mechanisms at entity level across multiple model families.
5	While \citet{yao2026consistency} demonstrate that scaling returns plateau at the task level, our contribution operates at a different granularity: instance-level diagnostic decomposition revealing \emph{why} specific instances resist scaling (degeneracy $+$ LP compression), with actionable per-instance signals.
6	
7	Using NER (four datasets, primarily 7--14B fine-tuned; tentative cross-scale observations to 72B) and RE as case studies, we identify a \textbf{correlation-selection gap}: quality estimation signals predict output quality ($\rho$ up to $0.45$, AUROC $0.82$; Table~\ref{tab:quality_estimation}), yet selection fails---MV gains ${<}1$\,pp even at $N{=}64$ (Figure~\ref{fig:n_scaling}; Table~\ref{tab:selection}).
8	This gap decomposes into a definitional layer---four instance-level signals assign identical scores to all candidates---and an empirical one: LP, the only per-sample signal, also fails through within-instance compression (\S\ref{sec:selection_gap}).
9	A hidden-state probe confirms models encode entity quality internally (AUROC $0.63$\textendash$0.88$; \S\ref{sec:mechanistic}), exposing an \textit{introspection boundary} \cite{huang2024large}.
10	A \textit{diagnostic framework}---co-occurring conditions that jointly characterize the gap, not a sequential filter---localizes the failure to deg
…[truncated 2980 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 4125 · 2026-05-22T13:32:11.935463+00:00_

1	\section{Diagnostic Framework}\label{sec:method}
2	
3	Our analysis is observational: we characterize statistical associations between agreement signals and output quality without claiming causal mechanisms.
4	
5	\subsection{Problem Formulation}\label{sec:formulation}
6	
7	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
8	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
9	This distinction is consequential: 4 of 5 signals are instance-level aggregates assigning identical scores to all $N$ candidates.
10	Only LP carries per-sample discriminative power: ensemble optimization assigns LP mean weight $0.78$, with structural signals receiving zero weight (Appendix~\ref{app:supervised_combination}).
11	When LP fails---as in few-shot regimes where LP $\rho{\to}0$ (\S\ref{sec:scaling})---no alternative per-sample signal exists.
12	
13	We define the \textbf{capability ceiling} as the practical performance upper bound achievable through self-consistency at realistic sample budgets ($N{\leq}16$), beyond which diminishing returns render further scaling impractical.
14	
15	\subsection{Confidence Signals}\label{sec:signals}
16	
17	Entity matching uses exact span and type match.
18	We distinguish two signal families: four \textit{agreement signals} computed across samples---\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK])---and log-probability [LP] as the sole \textit{model-internal} signal, derived from generation probabilities and providing per-sample discrimination.
19	
20	\paragraph{Log-probability (per-sample).}
21	$c_{\text{lp}}(y_i)
…[truncated 2151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 4126 · 2026-05-22T13:32:11.935697+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex"
  }
}
```

</details>

---


### Tool call

_source line 4127 · 2026-05-22T13:32:11.935930+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
  }
}
```

</details>

---


### Tool call

_source line 4128 · 2026-05-22T13:32:11.936255+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
  }
}
```

</details>

---


### Tool result

_source line 4129 · 2026-05-22T13:32:12.087117+00:00_

1	\section{How Self-Verification Fails}\label{sec:mechanistic}
2	
3	The diagnostic framework (\S\ref{sec:method}) identifies \textit{where} self-consistency fails; this section probes \textit{why} by testing whether models can self-verify at the entity level.
4	Probe experiments use Qwen2.5-7B (not the fine-tuned Qwen3-8B used in main experiments); conclusions are architecture-specific.
5	We evaluate self-verification and diagnostic probes on Qwen2.5-7B\footnote{ESJ, MRSC, and LSC use Qwen2.5-7B-Instruct (zero-shot self-verification capability) rather than the fine-tuned Qwen3-8B used in the main experiments. Conclusion direction is consistent with the main experiments' negative results across all fine-tuned selection strategies. The pattern---selection failure across all signals---is independently confirmed in the Qwen3-8B main experiments, making the introspection boundary a model-independent finding within our tested scale. Probe conclusions are limited to the Qwen2.5 architecture; linear probes may underestimate representational capacity (nonlinear alternatives are left to future work).} fine-tuned for NER on Few-NERD ($N{=}8$, seed 42; full results in Appendix~\ref{app:self_verification}).
6	
7	\paragraph{Entity Self-Judgment (ESJ).}
8	For each extracted entity, we prompt the generating model: ``Is [\textit{entity}] a [\textit{type}] entity in this sentence?''
9	Entity-level AUROC is $0.512$---indistinguishable from chance---with P(yes$|$correct)${=}0.500$ and P(yes$|$incorrect)${=}0.500$.
10	ESJ-weighted construction degrades F1 to $0.711$ (vs.\ greedy $0.794$).
11	
12	\paragraph{Multi-Round Self-Consistency (MRSC).}
13	Following iterative self-refinement \cite{madaan2023selfrefine}, we re-prompt on disputed entities (agreement ${<}0.6$) with focused verification; P(yes) separation between gold and non-gold entities is $0.0006$ ($0.5003$ vs.\ $0.4997$).
14	MRSC best F1 ($0.763$) falls below greedy.
15	
16	\paragraph{Latent Self-Consistency (LSC).}
17	Mean-pool
…[truncated 1794 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 4130 · 2026-05-22T13:32:12.087720+00:00_

1	\section{Where Single-Signal Selection Fails}\label{sec:selection_gap}
2	
3	\paragraph{Definitional vs.\ empirical.}
4	We decompose the correlation-selection gap into two layers.
5	The first is structural: four of five signals are instance-level aggregates that assign identical scores to all $N$ candidates from a given input (\S\ref{sec:formulation}), so they estimate quality across inputs but cannot rank candidates within an instance---selection failure is a design property, not an empirical finding.
6	The second layer is empirical and constitutes the core diagnostic: LP---the only per-sample signal---suffers compression under constrained decoding, with 60\% of SciERC instances showing within-instance LP range below 0.041 nats (Appendix~\ref{app:logprob_ties}), effectively eliminating the variation needed for sample discrimination. This compression is model-intrinsic: free-form decoding yields nearly identical LP distributions (within-instance std ratio $0.97{\times}$; Appendix~\ref{app:freeform_ablation}). Even where LP varies, selection gains depend on LP-quality alignment rather than degeneracy alone.
7	Cross-instance $\rho$ (Table~\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Best-of-$N$ selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$). Selection signals: 2-seed mean${\pm}\sigma$; baselines: 3-seed (Oracle${=}0.781$, Greedy${=}0.667$). LP is per-sample; others use consensus-proximity. $^\dagger$One score per input.}
13	\label{tab:selection}
14	\begin{tabular}{lcc}
15	\toprule
16	Method & NER F1 & $p$ \\
17	\midrule
18	Oracle & $0.775 \pm 0.001$ & --- \\
19	Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
20	\midrule
21	LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
22	SJ           & $0.646 \pm 0.002$ & .67 \\
23	FK      
…[truncated 2439 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 4131 · 2026-05-22T13:32:12.088082+00:00_

1	\section{Adaptive Methods}\label{sec:adaptive}
2	
3	Since instance-level selection fails (\S\ref{sec:selection_gap}), we present approaches that extract value from multi-sample generation beyond single-signal sample ranking.
4	Table~\ref{tab:method_summary} summarizes all 9 method categories evaluated; only cross-model ensembles yield an unconditional positive result.
5	
6	\begin{table}[t]
7	\centering
8	\small
9	\caption{Summary of 9 method categories tested (including MV baseline, LP selection, and cross-model ensemble beyond the seven verification methods in \S\ref{sec:mechanistic}--\S\ref{sec:adaptive}). $\Delta$F1 vs.\ greedy; dataset in parentheses. Full coverage in Appendix~\ref{app:method_coverage}.}
10	\label{tab:method_summary}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{@{}llrl@{}}
13	\toprule
14	Category & Method & $\Delta$F1 / metric & § \\
15	\midrule
16	Freq.\ voting & MV & baseline & \ref{sec:prescriptive} \\
17	LP selection & Best-of-$N$ (LP) & $+1.39$\,pp (FN)$^\dagger$ & \ref{sec:selection_gap} \\
18	Self-verif.\ (prompt) & ESJ & AUROC $0.51$ & \ref{sec:mechanistic} \\
19	Multi-round refine. & MRSC & $-3.1$\,pp (FN) & \ref{sec:mechanistic} \\
20	Latent aggregation & LSC & $-3.5$\,pp (FN) & \ref{sec:mechanistic} \\
21	Adaptive gating & DALS & $+0.71$\,pp (SciERC)$^\ddagger$ & App.~\ref{app:dals} \\
22	Supervised verifier & LGB & $+0.30$\,pp (OOF) & \ref{sec:verifier} \\
23	Sup.\ combination & LR/MLP/RF & $-0.4$ to $-3.1$\,pp & App.~\ref{app:supervised_combination} \\
24	Cross-model & Qwen$+$LLaMA & $\mathbf{+0.42}$\,pp (FN) & \ref{sec:cross_model} \\
25	\bottomrule
26	\end{tabular}}
27	{\footnotesize $^\dagger$Few-NERD only; SciERC $+0.2$\,pp ($p{=}0.29$). $^\ddagger$Seed-sensitive ($\sigma{=}0.48$\,pp).}
28	\end{table}
29	
30	\subsection{Cross-Model Self-Consistency}\label{sec:cross_model}
31	
32	Mixing samples from architecturally distinct models can partially bypass within-model degeneracy.
33	Combining 4 samples each from Qwen3-8B and
…[truncated 764 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 4132 · 2026-05-22T13:32:12.138612+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
  }
}
```

</details>

---


### Tool result

_source line 4133 · 2026-05-22T13:32:12.490422+00:00_

1	\section{Threshold Regime Analysis}\label{sec:theory_scaling}
2	
3	\subsection{Entity Construction as MBR Decoding}\label{sec:mbr_theory}
4	
5	Entity-level construction selects $\hat{y}_{\textup{MBR}} = \{e \in E_\cup : \hat{p}(e) > \alpha/(\alpha{+}1)\}$ under balanced set-overlap utility; $\alpha{=}1$ recovers majority vote (Proposition~\ref{prop:construction_mbr}; Table~\ref{tab:entity_construction}; Appendix~\ref{app:mbr_proof}).
6	Signal-derived weights $w_i$ yield quality-weighted MBR: $\hat{p}_w(e) = \sum_{i} w_i \, \mathbf{1}[e {\in} y_i] / \sum_{i} w_i$; weighting improves when $w_i$ correlates with instance quality but degrades otherwise (LP on SciERC: $\rho{\approx}0.2$; \S\ref{sec:prescriptive}).
7	We select $\varepsilon{=}0.05$ at the elbow of the compression curve, where LP-best selection advantage transitions from $+1.5$\,pp (compressed) to $+4.6$\,pp (non-compressed; Appendix~\ref{app:fewnerd_epsilon}).
8	
9	\subsection{Scaling and Inverse Scaling}\label{sec:scaling}
10	
11	Oracle F1 follows $F_1(N) = a - b \cdot N^{-c}$ ($R^2 > 0.999$; Figure~\ref{fig:oracle_scaling}): Few-NERD ($c{\approx}0.61$) scales comparably to reasoning tasks \cite{brown2024monkeys}, SciERC converges more slowly ($c{\approx}0.35$), yet confidence-based aggregation recovers ${<}1$\,pp---a persistent gap.
12	The gap persists across scales and families: scaling from 8B to 14B FT increases oracle headroom ($+1.2$\,pp) with minimal greedy gain ($+0.9$\,pp), and GPT-5.5 (200 Few-NERD instances, zero-shot) exhibits the same pattern---50\% degeneracy, SJ $\rho{=}0.346$, MV $+1.4$\,pp yet 6.8\,pp oracle headroom unrealized.\footnote{Of the 10.1\% of GPT-5.5 samples producing empty entity sets, 88\% correspond to gold-empty instances; true parse failures affect only 1.2\% of samples (19/1{,}600) and shift all reported metrics by ${<}0.5$\,pp. See Appendix~\ref{app:frontier_sc}.}
13	Degeneracy is model-family-dependent rather than scale-dependent (Qwen2.5: $31.7$--$46.2$\% vs.\ Qwen3:
…[truncated 4179 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 4134 · 2026-05-22T13:32:12.490889+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
  }
}
```

</details>

---


### Tool result

_source line 4135 · 2026-05-22T13:32:13.444162+00:00_

1	\section{Experiments}\label{sec:experiments}
2	
3	\subsection{Experimental Setup}\label{sec:setup}
4	
5	\paragraph{Datasets.}
6	We evaluate on four English NER benchmarks spanning a difficulty gradient.
7	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed (${\approx}$65\% F1).
8	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:selection_gap}).
9	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control.
10	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 51\% zero F1) probes the signal-collapse boundary.
11	
12	\paragraph{Models and sampling.}
13	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others; Appendix~\ref{app:epoch_confound}).
14	$N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}; $N {\in} \{16, 32, 64\}$ for scaling (Figure~\ref{fig:n_scaling}; Appendix~\ref{app:n_scaling}).
15	
16	\begin{figure}[t]
17	\centering
18	\includegraphics[width=\columnwidth]{figures/fig_n_scaling_mv.pdf}
19	\caption{MV $\Delta$F1 vs.\ $\log_2 N$ across three datasets (Qwen3-8B FT, seed${=}42$). Dotted gray: $\Delta{=}0$. Gains are dataset-dependent: persistently negative on Few-NERD, near zero on SciERC at higher $N$, marginally positive on CoNLL ($+0.6$\,pp at $N{=}64$).}
20	\label{fig:n_scaling}
21	\end{figure}
22	
23	%% ============================================================
24	\subsection{Quality Estimation Results}\label{sec:qe_results}
25	
26	\begin{table*}[t]
27	\centering
28	\small
29	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed $
…[truncated 7313 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 4136 · 2026-05-22T13:32:13.494715+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 4137 · 2026-05-22T13:32:14.046995+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Test-time compute scaling.}
4	Self-consistency \cite{wang2023selfconsistency} and best-of-$N$ \cite{snell2025scaling, brown2024monkeys} drive large gains on reasoning and code \cite{chen2021codex}.
5	Reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty}, BoN scaling laws \cite{gao2023scaling}, and trained verifiers \cite{cobbe2021verifiers, lightman2024verify} target discrete-answer settings; NER requires different aggregation because degeneracy operates at the entity-set level.
6	
7	\paragraph{SC failure modes.}
8	\citet{chen2023twofailures} identify SC failures where consistent outputs are wrong; free-form \cite{chen2024usc} and atomic \cite{thirukovalluru2024atomic} SC variants face limits where sub-output agreement does not yield selection gain (\S\ref{sec:selection_gap}).
9	
10	\paragraph{Consistency for structured IE.}
11	\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE at the task level ($\rho$ up to 0.47); we extend this to instance-level analysis, diagnosing \textit{why} correlation does not transfer to selection gains. Key distinctions: (1)~granularity---task-level $\rho$ masks instance-level degeneracy; (2)~mechanism---we decompose failure into degeneracy and LP compression; (3)~actionability---pre-deployment diagnostics (measure degeneracy at $N{=}8$) that task-level correlation cannot provide.
12	\citet{xie2023zeroshot} propose entity voting for zero-shot NER and \citet{xie2024selfimproving} report positive SC where zero-shot diversity is high.
13	\paragraph{Uncertainty estimation and MBR.}
14	Our selection instantiates MBR decoding \cite{eikema2022sampling, denero2009fast}; despite success in translation \cite{freitag2022high} and code \cite{jinnai2024mbr}, all variants fail due to instance degeneracy (Appendix~\ref{app:mbr_connection}).
15	\citet{eikema2025structured} find MBR utilities degrade on structured outputs; our framework loca
…[truncated 2096 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 4138 · 2026-05-22T13:32:14.198162+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 4139 · 2026-05-22T13:32:14.404394+00:00_

1	\section{Discussion and Conclusion}\label{sec:discussion}\label{sec:selection_method}\label{sec:conclusion}
2	
3	\paragraph{Why test-time scaling fails for NER.}
4	For discrete-answer reasoning, sample diversity reflects diverse reasoning paths; for NER, degeneracy ($12$--$68$\%) eliminates candidate diversity while signal alignment collapse ($\alpha{\to}0$) prevents ranking.
5	We quantify how the well-known capability-diversity tradeoff \cite{yun2025price} manifests in NER, observing this across model families (5.5--74\%; Table~\ref{tab:frontier_sc_cross}) and scales (4B--72B; \S\ref{sec:scaling}).
6	Free-form decoding confirms this is model-intrinsic (within-instance LP std ratio $0.97{\times}$; \S\ref{sec:selection_gap}).
7	Our work differs from \citet{yao2026consistency} along three dimensions: (1)~\textbf{Granularity}---task-level plateau observation vs.\ instance-level failure decomposition; (2)~\textbf{Mechanism}---they document diminishing returns without diagnosing causes, while we identify degeneracy and LP compression as co-occurring failure conditions; (3)~\textbf{Actionability}---our per-instance diagnostic signals enable selective resource allocation (entity-level construction yields $+1.40$\,pp where conditions are favorable, though inverse scaling in $69$\% of $N$-transitions limits general applicability).
8	
9	\paragraph{Concurrent evidence.}
10	\citet{landesberg2026bon} independently document a correlation-selection gap in best-of-$N$ reasoning: judge scores correlate with quality globally ($r{=}0.47$) but fail within-prompt ($r{=}0.27$). Their mechanism differs---scoring granularity collapse in a single-score setting---but the parallel is striking: global signal quality does not guarantee instance-level selection utility across both structured prediction and reasoning domains.
11	
12	\paragraph{Practical implications.}
13	Measuring degeneracy and LP-F1 alignment at $N{=}8$---requiring only $8{\times}$ inference cost (12.5\% of $N{=}64$ full scal
…[truncated 1872 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 206
}
```

</details>

---


### Tool call

_source line 4140 · 2026-05-22T13:32:14.505196+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 4141 · 2026-05-22T13:32:14.856771+00:00_

1	Our primary evidence is from NER (four English datasets, 7--14B open-weight fine-tuned); cross-scale observations (4B--72B, GPT-5.5) are tentative. The RE extension ($n{=}397$, single dataset) and SQL pilot ($n{=}196$) are exploratory. SciERC results are validated across three training seeds ($n{=}529$ test instances; $\Delta_{\text{SC}}{=}{-}0.74{\pm}0.57$\,pp, consistent negative). Frontier models exhibit markedly different degeneracy profiles (5.5--74\%; Table~\ref{tab:frontier_sc_cross}), suggesting findings from fine-tuned open-weight models may not fully generalize to proprietary systems.
2	Our framework is diagnostic, not causal: stages resist decomposition into independent effects ($R^2{<}0$; \S\ref{sec:selection_gap}). Under global Holm--Bonferroni ($k{=}57$), the most liberal core claim reaches $p_{\text{HB}}{=}0.055$; under BH FDR, $19/57$ tests are significant at FDR${<}0.05$ including $6/10$ construction comparisons (Appendix~\ref{app:holm}).
3	We evaluate at $N{\in}\{2,\ldots,64\}$; entity-level construction requires $N{\times}$ inference cost for modest gains ($+1$--$1.4$\,pp). We use a single prompt template per task; prompt variations may affect entity recall, degeneracy, and LP distributions.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 4142 · 2026-05-22T13:32:14.857115+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 4143 · 2026-05-22T13:32:15.358943+00:00_

File content (66023 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 4144 · 2026-05-22T13:32:15.359296+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 4145 · 2026-05-22T13:32:16.312571+00:00_

1	issues:
2	# ===== ROUND 38 CRITICAL / MUST-FIX =====
3	- id: R38-MF1
4	  summary: "Title 'Boundary Conditions' 暗示数学 necessary/sufficient conditions，与 diagnostic framework 矛盾"
5	  category: framing
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 35
9	  last_seen_round: 38
10	  mentions:
11	    - round: 38
12	      reviewers: [1, 2]
13	      note: "4轮连续攻击。'Boundary Conditions' 在数学中暗示 formal conditions，但论文交付 diagnostic correlations。"
14	  action_items:
15	    - round: 38
16	      action: "Title → 'When Does Test-Time Scaling Fail? A Diagnostic Framework for Named Entity Recognition'"
17	      assigned_to: paper_agent
18	      status: done
19	  resolution: "Title changed to 'A Diagnostic Framework for Named Entity Recognition'"
20	  resolution_round: 39
21	
22	- id: R38-MF2
23	  summary: "Degeneracy bound (1-D)·G_nd·α 仅 capture 3-12% actual gains，定量诊断价值存疑"
24	  category: method
25	  severity: critical
26	  status: resolved
27	  first_raised_round: 38
28	  last_seen_round: 38
29	  mentions:
30	    - round: 38
31	      reviewers: [1, 2]
32	      note: "Bound off by 10x (Figure 10)。Looseness 源于 entity independence 假设 (split-half r=0.578-0.644) + α 保守估计。"
33	  action_items:
34	    - round: 38
35	      action: "§6.3 增加 looseness 讨论；bound 重定位为 illustrative directional decomposition"
36	      assigned_to: paper_agent
37	      status: done
38	  resolution: "theory.tex already has 'illustrative upper bound under simplifying assumptions' + split-half correlation + 3-12% recovery discussion"
39	  resolution_round: 39
40	
41	- id: R38-MF3
42	  summary: "Entity construction 69% inverse scaling 与 'partially bypasses' framing 严重矛盾"
43	  category: framing
44	  severity: critical
45	  status: resolved
46	  first_raised_round: 38
47	  last_seen_round: 38
48	  mentions:
49	    - round: 38
50	      reviewers: [1, 2]
51	      note: "40/58 N-transitions inverse scaling。Abstract/§1/§5/§9 多处 'bypass' 与 69% failure 矛盾。"
52	  action_items:
53	    - round: 38
54	      action
…[truncated 8461 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 4146 · 2026-05-22T13:32:16.513634+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR submission format page limit long paper short paper template double blind",
  "allowed_domains": "['2026.emnlp.org', 'aclweb.org', 'aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR submission format page limit long paper short paper template double blind",
    "allowed_domains": "['2026.emnlp.org', 'aclweb.org', 'aclrollingreview.org']"
  }
}
```

</details>

---


### Tool result

_source line 4147 · 2026-05-22T13:32:27.148349+00:00_

Web search results for query: "EMNLP 2026 ARR submission format page limit long paper short paper template double blind"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"}]

Let me search for more specific information about EMNLP 2026 ARR submission requirements including page limits and templates.

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclw
…[truncated 3724 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 10634
}
```

</details>

---


### Tool call

_source line 4148 · 2026-05-22T13:32:51.821306+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_39/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_39/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 4149 · 2026-05-22T13:32:52.374079+00:00_

-rw-r--r-- 1 ubuntu ubuntu 988175 May 22 13:14 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_39/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 4150 · 2026-05-22T13:32:52.374416+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 4151 · 2026-05-22T13:32:52.424958+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml\", \"content\": \"_next_id: 241\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:23 UTC\\n  summary: 'MVP 方案: ACE05 上验证 structural consistency vs Fleiss'' Kappa 的 correlation\\n    差异'\\n  rationale: 'PMC12888769 用 surface-level Fleiss'' Kappa 在 zero-shot 模型上得到 ρ=0.20-0.28，我们假设\\n    fine-tuned 模型 + structural consistency (soft Jaccard) 能达到 ρ≥0.40。这是整个论文的基础假设——如果\\n    structural consistency 不能更好地预测准确率，后续的 adaptive gating 无从谈起。Phase 0 pilot 设计: Qwen3-8B\\n    fine-tuned on ACE05, N=8 samples, 200 instances, 对比两种 consistency metric 的 Spearman\\n    ρ。Pass ≥0.40, Fail <0.30。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 04:27 UTC\\n  summary: 采纳 Reviewer 审查意见，收紧 MVP pass/fail 标准\\n  rationale: 'Reviewer 指出 5 个问题，全部合理采纳：(1) PASS 必须要求 EAE (high-headroom subtask) ρ≥0.40，仅\\n    NER 通过不够（ceiling effect 可能虚高）；(2) MARGINAL 区间加 time-boxed protocol: N=16 追加 +\\n    1天上限；(3) 加 fine-tuning 质量门控 (NER≥73, EAE≥45)，模型不行时先修 fine-tuning；(4) ACE05 今天必须确认；(5)\\n    监控 T=1.0 per-sample F1 分布，>30% F1=0 时追加 T=0.7。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 04:53 UTC\\n  summary: SciERC RE 替代 ACE05 EAE 作为 MVP high-headroom subtask\\n  rationale: ACE05 需 LDC 许可，用户未确认。SciERC 公开可得，有 NER+RE 两个 subtask。RE base F1 ~47（与\\n    ACE05 EAE ~52 相当），结构复杂度高（entity pair + relation type），headroom 大，是 EAE 的合理替代。PASS\\n    标准更新为 RE ρ≥0.40。需要补实现 RE 的 consistency + evaluation + pipeline 支持。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:38 UTC\\n  summary: 'Gate 0: NER PASS (60.4%), RE FAIL (33.8%). 执行方案 C——当前模型先跑 pilot + 追训改进版，需修复\\n    RE evaluation'\\n  rationale: RE 33.8% 低于 40% 阈值但不阻塞 pilot：(1) headroom 大，oracle best-of-N 有提升空间；(2)\\n    consistency correlation 不要求高绝对 F1，要求 per-instance variance；(3) 弱模型上验证假设结论更强。但\\n    Reviewer 发
…[truncated 1441 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4152 · 2026-05-22T13:32:57.409006+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool call

_source line 4153 · 2026-05-22T13:32:57.409436+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 4154 · 2026-05-22T13:32:57.459899+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 4155 · 2026-05-22T13:32:58.262833+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (324 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp_conll_freeform_n8_s42 | Free-form decoding ablation: CoNLL N=8 T=1.0 seed=42 with use_grammar=False. Tests whether removing XGrammar constrained decoding degrades extraction quality and consistency scores, quantifying the contribution of grammar constraints to the structured self-consistency pipeline. | — | — | — |\n| exp_fewnerd_freeform_n8_s42 | R35-W6 free-form decoding ablation: FewNERD N=8 T=1.0 seed=42 without grammar constraints. FewNERD has lowest degeneracy (12% at N=8). If free-form degeneracy remains low (~12%), confirms degeneracy is model-intrinsic, not a constrained decoding artifact. Complements CoNLL free-form ablation (59.3% vs 56.7% constrained). | — | — | — |\n| exp_fewnerd_5epoch_lp_s42 | FewNERD 5-epoch checkpoint with LP selection will show improved F1 over majority voting, similar to the 3-epoch results, validating that LP selection is robust across training epochs | — | — | — |\n\n## 待处理\n- exp_fewnerd_mf4v2_s123_v4: FewNERD MF4v2 s123 v4: regenerate finetuned FewNERD seed=123 instance-level samples.jsonl on autodl-5090-c for v4 MV unified recompute. N=8, T=1.0, seed=123. Model: qw
…[truncated 1744 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 4156 · 2026-05-22T13:33:02.794988+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "output_mode": "content",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 4157 · 2026-05-22T13:33:15.394666+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260516T094957_715546.jsonl:1676:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260516T094957_715546.jsonl:2402:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T102033_395761.jsonl:2106:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T102033_395761.jsonl:2207:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_523053f5a039428dc15666668fa856b3_20260515T183358_453446.jsonl:905:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260521T014101_505360.jsonl:3912:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260521T014101_505360.jsonl:4240:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260521T014101_505360.jsonl:7181:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260521T014101_505360.jsonl:7375:[Omitted long matching line]
/home/ubuntu/.agent-ml-researc
…[truncated 3537 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 12599
}
```

</details>

---


### Tool call

_source line 4158 · 2026-05-22T13:33:19.966066+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "glob": "config*.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "glob": "config*.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 4159 · 2026-05-22T13:33:20.116972+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 4160 · 2026-05-22T13:33:23.027316+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 4161 · 2026-05-22T13:33:23.128153+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 4162 · 2026-05-22T13:33:25.888492+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 4163 · 2026-05-22T13:33:25.989525+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/worst/review_context.yaml
/hom
…[truncated 12161 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 4164 · 2026-05-22T13:33:30.286628+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1",
  "glob": "**/config.yaml",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1",
    "glob": "**/config.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 4165 · 2026-05-22T13:33:30.439576+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 4166 · 2026-05-22T13:33:58.403121+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "struct_self_consist_ie",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 4167 · 2026-05-22T13:34:20.342575+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 21939
}
```

</details>

---


### Tool call

_source line 4168 · 2026-05-22T13:34:21.305853+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 初审任务 — Reviewer 1（方法严谨性 + 实验设计）\n\n### Venue 信息\n- **目标 venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板，long paper 正文 8 页严格限制，参考文献不限，Limitations/Ethics 不计入页数\n- **匿名规则**: Double-blind（无 anonymity period）\n- **评分标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 论文路径\n- LaTeX 源文件: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_39/submitted.pdf`\n\n### 你的审查侧重\n\n**方法严谨性 + 实验设计**。具体关注：\n\n1. **诊断框架有效性**：degeneracy + signal alignment collapse 作为联合诊断条件是否有充分实证支持？框架声称是 diagnostic 而非 predictive——这一定位是否合理、是否回避了更强的可检验假设？\n\n2. **统计严谨性**：\n   - Global Holm-Bonferroni k=57 下 p_adj=0.055 的处理是否恰当？\n   - 多重比较校正的 family 划分是否合理（未 pre-registered）？\n   - 效应量是否足够（+1.40pp with 69% inverse scaling）？\n   - Power analysis 是否充分？\n\n3. **Bound 分析**：\n   - (1-D)·G_nd·α bound 仅 capture 3-12% of actual gains——这对定量诊断的价值有何影响？\n   - Bound looseness 讨论（entity independence assumption, conservative α estimation）是否充分？\n   - Proposition 1 的简化假设是否过于 restrictive？\n\n4. **消融完整性**：\n   - Free-form decoding ablation 仅覆盖部分数据集是否构成方法缺陷？\n   - 3-epoch vs 5-epoch confound 如何影响主结论？\n   - Probe 使用 Qwen2.5-7B 而非主实验 Qwen3-8B 的 architecture gap 是否构成 validity threat？\n\n5. **实验设计**：\n   - 4 个 NER 数据集 + RE pilot (n=397) + SQL pilot (n=196) 的覆盖是否足以支撑 claims？\n   - Cross-model ensemble（Qwen+LLaMA）仅 Few-NERD 一个数据集是否充分？\n   - Trained verifier (LightGBM) cross-dataset transfer negative 是否合理解释？\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n1. **Summary**（2-3 句概述论文）\n2. **Strengths**（逐条，标注 S1, S2, ...）\n3. **Weaknesses**（逐条，标注 W1, W2, ...，区分 Must-Fix / Should-Fix / Minor）\n4. **Questions**（标注 Q1, Q2, ...）\n5. **Missing References**（如有）\n6. **Overall Assessment**（评分 + 置信度 + 1-2 句总评）",
  "project": "struct_self_consist_ie",
  "chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 初审任务 — Reviewer 1（方法严谨性 + 实验设计）\n\n### Venue 信息\n- **目标 venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板，long paper 正文 8 页严格限制，参考文献不限，Limitations/Ethics 不计入页数\n- **匿名规则**: Double-blind（无 anonymity period）\n- **评分标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 论文路径\n- LaTeX 源文件: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_39/submitted.pdf`\n\n### 你的审查侧重\n\n**方法严谨性 + 实验设计**。具体关注：\n\n1. **诊断框架有效性**：degeneracy + signal alignment collapse 作为联合诊断条件是否有充分实证支持？框架声称是 diagnostic 而非 predictive——这一定位是否合理、是否回避了更强的可检验假设？\n\n2. **统计严谨性**：\n   - Global Holm-Bonferroni k=57 下 p_adj=0.055 的处理是否恰当？\n   - 多重比较校正的 family 划分是否合理（未 pre-registered）？\n   - 效应量是否足够（+1.40pp with 69% inverse scaling）？\n   - Power analysis 是否充分？\n\n3. **Bound 分析**：\n   - (1-D)·G_nd·α bound 仅 capture 3-12% of actual gains——这对定量诊断的价值有何影响？\n   - Bound looseness 讨论（entity independence assumption, conservative α estimation）是否充分？\n   - Proposition 1 的简化假设是否过于 restrictive？\n\n4. **消融完整性**：\n   - Free-form decoding ablation 仅覆盖部分数据集是否构成方法缺陷？\n   - 3-epoch vs 5-epoch confound 如何影响主结论？\n   - Probe 使用 Qwen2.5-7B 而非主实验 Qwen3-8B 的 architecture gap 是否构成 validity threat？\n\n5. **实验设计**：\n   - 4 个 NER 数据集 + RE pilot (n=397) + SQL pilot (n=196) 的覆盖是否足以支撑 claims？\n   - Cross-model ensemble（Qwen+LLaMA）仅 Few-NERD 一个数据集是否充分？\n   - Trained verifier (LightGBM) cross-dataset transfer negative 是否合理解释？\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n1. **Summary**（2-3 句概述论文）\n2. **Strengths**（逐条，标注 S1, S2, ...）\n3. **Weaknesses**（逐条，标注 W1, W2, ...，区分 Must-Fix / Should-Fix / Minor）\n4. **Questions**（标注 Q1, Q2, ...）\n5. **Missing References**（如有）\n6. **Overall Assessment**（评分 + 置信度 + 1-2 句总评）",
    "project": "struct_self_consist_ie",
    "chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 4169 · 2026-05-22T13:34:40.194248+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18888
}
```

</details>

---


### Tool call

_source line 4170 · 2026-05-22T13:34:40.728420+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 初审任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### Venue 信息\n- **目标 venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板，long paper 正文 8 页严格限制，参考文献不限，Limitations/Ethics 不计入页数\n- **匿名规则**: Double-blind（无 anonymity period）\n- **评分标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 论文路径\n- LaTeX 源文件: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_39/submitted.pdf`\n\n### 你的审查侧重\n\n**新颖性 + 完整性 + 写作质量**。具体关注：\n\n1. **新颖性评估**：\n   - 与 Yao et al. (2026) 的区分是否充分？他们已展示 consistency 与 accuracy 在 NER/RE 的 task-level correlation（ρ up to 0.47）。本文声称的 instance-level 延伸是否是 incremental extension 还是 substantial contribution？\n   - 与 Yun & Sun (2025) 的 diversity collapse 概念是否有实质区别（degeneracy vs diversity collapse）？\n   - 与 Landesberg et al. (2026) concurrent work 的 correlation-selection gap 如何体现独立贡献？\n   - \"诊断框架\"的新颖性：识别 degeneracy + LP compression 是否构成 novel insight 还是对已知现象的 repackaging？\n\n2. **Related Work 完整性**：\n   - 是否遗漏重要相关工作？特别是：\n     - Token-level uncertainty for NER\n     - Conformal prediction for structured prediction\n     - MBR decoding for structured outputs\n     - Entity-level calibration\n   - 并发工作覆盖是否充分？\n\n3. **Claims-Evidence 对齐**：\n   - Abstract 中的每个 claim 是否都有充分实验支持？\n   - \"diagnostic rather than predictive\" 的反复强调是否是对框架局限性的过度辩护？\n   - Entity construction +1.40pp（global Holm p=0.055）——在统计意义上这算 positive result 还是 null result？\n   - 69% inverse scaling 与 \"conditional gains\" framing 是否公平？\n\n4. **写作质量**：\n   - 术语一致性（degeneracy 用法是否明确、无歧义）\n   - 论文结构（章节顺序：Diagnostic → Mechanistic → Single Signal → Adaptive → Theory → Experiments → Related Work → Discussion 是否合理？Related Work 放在 Experiments 后面是否恰当？）\n   - 数字密度：正文中的统计数字是否过多导致可读性下降？\n   - Notation 一致性（per-sample vs instance-level 区分是否贯穿全文？）\n\n5. **格式合规**：\n   - 正文是否超过 8 页？\n   - Limitations section 是否充分覆盖主要局限？\n   - Ethics statement 是否合规？\n   - 匿名性：是否有任何去匿名化线索？\n   - 引用格式是否一致？\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n1. **Summary**（2-3 句概述论文）\n2. **Strengths**（逐条，标注 S1, S2, ...）\n3. **Weaknesses**（逐条，标注 W1, W2, ...，区分 Must-Fix / Should-Fix / Minor）\n4. **Questions**（标注 Q1, Q2, ...）\n5. **Missing References**（如有）\n6. **Overall Assessment**（评分 + 置信度 + 1-2 句总评）",
  "project": "struct_self_consist_ie",
  "chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 初审任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### Venue 信息\n- **目标 venue**: EMNLP 2026（通过 ARR 统一审稿）\n- **截止日期**: 2026-05-25\n- **格式**: ACL 模板，long paper 正文 8 页严格限制，参考文献不限，Limitations/Ethics 不计入页数\n- **匿名规则**: Double-blind（无 anonymity period）\n- **评分标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 论文路径\n- LaTeX 源文件: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_39/submitted.pdf`\n\n### 你的审查侧重\n\n**新颖性 + 完整性 + 写作质量**。具体关注：\n\n1. **新颖性评估**：\n   - 与 Yao et al. (2026) 的区分是否充分？他们已展示 consistency 与 accuracy 在 NER/RE 的 task-level correlation（ρ up to 0.47）。本文声称的 instance-level 延伸是否是 incremental extension 还是 substantial contribution？\n   - 与 Yun & Sun (2025) 的 diversity collapse 概念是否有实质区别（degeneracy vs diversity collapse）？\n   - 与 Landesberg et al. (2026) concurrent work 的 correlation-selection gap 如何体现独立贡献？\n   - \"诊断框架\"的新颖性：识别 degeneracy + LP compression 是否构成 novel insight 还是对已知现象的 repackaging？\n\n2. **Related Work 完整性**：\n   - 是否遗漏重要相关工作？特别是：\n     - Token-level uncertainty for NER\n     - Conformal prediction for structured prediction\n     - MBR decoding for structured outputs\n     - Entity-level calibration\n   - 并发工作覆盖是否充分？\n\n3. **Claims-Evidence 对齐**：\n   - Abstract 中的每个 claim 是否都有充分实验支持？\n   - \"diagnostic rather than predictive\" 的反复强调是否是对框架局限性的过度辩护？\n   - Entity construction +1.40pp（global Holm p=0.055）——在统计意义上这算 positive result 还是 null result？\n   - 69% inverse scaling 与 \"conditional gains\" framing 是否公平？\n\n4. **写作质量**：\n   - 术语一致性（degeneracy 用法是否明确、无歧义）\n   - 论文结构（章节顺序：Diagnostic → Mechanistic → Single Signal → Adaptive → Theory → Experiments → Related Work → Discussion 是否合理？Related Work 放在 Experiments 后面是否恰当？）\n   - 数字密度：正文中的统计数字是否过多导致可读性下降？\n   - Notation 一致性（per-sample vs instance-level 区分是否贯穿全文？）\n\n5. **格式合规**：\n   - 正文是否超过 8 页？\n   - Limitations section 是否充分覆盖主要局限？\n   - Ethics statement 是否合规？\n   - 匿名性：是否有任何去匿名化线索？\n   - 引用格式是否一致？\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n1. **Summary**（2-3 句概述论文）\n2. **Strengths**（逐条，标注 S1, S2, ...）\n3. **Weaknesses**（逐条，标注 W1, W2, ...，区分 Must-Fix / Should-Fix / Minor）\n4. **Questions**（标注 Q1, Q2, ...）\n5. **Missing References**（如有）\n6. **Overall Assessment**（评分 + 置信度 + 1-2 句总评）",
    "project": "struct_self_consist_ie",
    "chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 4171 · 2026-05-22T13:34:43.273935+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 2545
}
```

</details>

---


### Assistant

_source line 4172 · 2026-05-22T13:34:56.495176+00:00_

**Step 1 已启动**，等待两位 Reviewer 独立初审完成：

| 角色 | 侧重 | 状态 |
|------|------|------|
| Reviewer 1 | 方法严谨性 + 实验设计 + 统计分析 | 🔄 审稿中 |
| Reviewer 2 | 新颖性 + 完整性 + 写作质量 | 🔄 审稿中 |
| 视觉审查 Agent | PDF 排版/布局质量 | 🔄 运行中 |

收到 Reviewer 结果后将进入 Step 2（交叉分享 + 逐条回应）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 314

## Round 314

2 recorded events


### User

_source line 4173 · 2026-05-22T13:40:35.865552+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 初审意见（方法严谨性 + 实验设计）

---

### Summary

本文研究 test-time compute scaling（重复采样 + self-consistency / best-of-N）在 NER 任务上何时成功、何时失败。作者在 4 个英文 NER 数据集（ScIERC、CoNLL-2003、Few-NERD、WNUT-17）和 2 个模型家族（Qwen3-8B、LLaMA-3.1-8B）上进行了大规模实证研究，发现质量估计信号（AUROC 最高 0.82）能预测输出质量，但 instance-level selection 大多失败（MV gain < 1pp）。论文提出以 degeneracy + signal alignment collapse (σ→0) 作为联合诊断条件的框架，并给出 entity construction 在有利条件下可获得 +1.40pp 的微弱正向增益。论文还包括对 RE 和 SQL 的探索性扩展。

---

### Strengths

**S1. 研究问题重要且切入点好。** 论文精确定位了一个被忽略的问题：test-time scaling 在 structured prediction（尤其是 NER）上的 correlation-selection gap——质量估计有效但选择失败。这对日益依赖 SC 的 LLM pipeline 有实际指导意义。

**S2. 实证工作极为详尽。** 45 页的论文（含 36 页附录）覆盖了 4 个 NER 数据集、2 个模型家族、9 类方法、7 种验证机制（Table 2）。附录包括 temperature/seed/sample-size sensitivity（Appendix b）、calibration analysis（Appendix c）、N-scaling detailed analysis（Appendix e）、per-entity-type analysis（Appendix z）等，展现了远超一般 EMNLP 投稿的实验深度。

**S3. 负面结果诚实报告。** 69% 的 N-transitions 出现 inverse scaling（§6.2）、cross-dataset transfer negative（§5.2, −0.76 to −0.70pp）、5-epoch 训练消除 LP gains（91% collapse, §8/Appendix ab）。这些对后续研究极有价值。

**S4. Diagnostic vs. predictive 的定位清晰合理。** 论文明确声明框架是 diagnostic 而非 predictive（§1, §9），避免了 overclaim。与 MBR decoding 的理论联系（§6.1, Proposition 2）也为该方向提供了有价值的 bridge。

**S5. Robustness 检查全面。** Temperature sensitivity（Appendix b, Figure 5）、seed stability（Table 36）、sample size effects（Table 35, 37）、FK independence test（Table 7）、bootstrap significance（Table 39）、permutation tests（Table 15）均有覆盖。

**S6. 实用指导明确。** §9 "When not to scale" 和 Appendix ae "Evaluation Protocol" 提供了可操作的实践建议（degeneracy < 20% 时考虑 LP selection，ρ > 0.70 时选 LP）。

---

### Weaknesses

#### Must-Fix（影响接收决定）

**W1. [critical] Proposition 1 的 bound 过于宽松，削弱了定量诊断的核心价值。**
- 具体位置：§6.3, Proposition 1 (p.6), Table 31 (p.29), Appendix p.4-p.5
- 问题：(1−D)·G_nd·α bound 仅 capture actual gains 的 3–12%（Table 31, Ratio 列：ScIERC 12.1%, CoNLL −0.42 即方向相反, Few-NERD 6.0%）。论文讨论了两个 looseness 来源——entity independence assumption（split-half r=0.578–0.644）和 conservative α estimation——但这意味着 bound 在实践中几乎没有诊断价值：它既不能 tightly predict gains，也不能可靠地判断是否值得做 scaling。
- 为什么影响接收：论文将 Proposition 1 作为理论贡献之一（§1 "Explore conditionals"），但 3–12% 的 capture rate 使得这一 bound 的实际 insight 非常有限。如果 bound 的主要作用只是"定性确认 degeneracy 和 alignment 是 bottleneck"（§6.3 "illustrative directional analysis"），那它与纯 empirical observation 相比并无显著增量。
- 建议修改方向：(a) 更明确地将 bound 降级为 "illustrative lower bound"，不在 §1 contribution 列表中突出；(b) 讨论是否存在可以收紧 bound 的方向（如 relaxing entity independence via copula models）；(c) 或提供 empirical tighter bound（如 bootstrap-based bound）。

**W2. [critical] Probe 使用 Qwen2.5-7B 而非主实验 Qwen3-8B，存在 architecture validity gap。**
- 具体位置：§3 (p.3), Appendix b.3 (p.19-20)
- 问题：Hidden-state probe（§3, "hidden-state probe"）和 entity-level self-verification（§3）均在 Qwen2.5-7B 上进行，但主实验全部使用 Qwen3-8B。论文承认"Probe conclusions are limited to the Qwen2.5 architecture"（p.3），但这一 gap 比简单的 "limitation" 更严重：Qwen2.5-7B 和 Qwen3-8B 在 architecture（如 attention mechanism、vocabulary size）和 training data 上可能有显著差异。Probe 的核心结论——"entity quality is partially encoded in hidden representations"（AUROC 0.63–0.88）——可能在 Qwen3-8B 上不成立或程度不同。
- 为什么影响接收：Probe 结果是 §3 "introspection boundary" 论证的关键支撑（"a supervised probe reveals an introspection boundary"），而 introspection boundary 是框架的重要组成部分。Architecture mismatch 削弱了这一论证链。
- 建议修改方向：在 Qwen3-8B 上重新运行 probe（至少 ScIERC 一个数据集），或者明确讨论为什么 Qwen2.5→Qwen3 的 architecture gap 不太可能改变定性结论（如 cite 其他工作证明 probe transferability）。

**W3. [critical] 3-epoch vs. 5-epoch confound 严重威胁 Few-NERD 主结论的鲁棒性。**
- 具体位置：§8 (p.8), Appendix ab (Table 55, p.39), Table 56 (p.39)
- 问题：Few-NERD 是论文最核心的正面结果来源（唯一 p_adj < 0.05 的 LP selection，+1.39pp），但 5-epoch 训练使 LP gains 从 +1.38 降至 +0.12±0.04pp（91% collapse, Table 55）。论文将此归因为"training convergence moderates degeneracy"（degeneracy: 8.8%→10.4%），但这意味着论文的 favorable condition 极度脆弱——它依赖于一个 under-trained model（3-epoch）。论文承认"conditions are fragile and training-dependent"（p.8），但这一承认不足以抵消对主结论的冲击：如果最佳实践是 train to convergence，那么 LP selection 的 practical applicability 将大幅受限。
- 为什么影响接收：Few-NERD 的 3-epoch 结果占据了论文正面发现的核心位置（Table 1, Table 4, §7.5 prescriptive results），如果这些结果在正常训练条件下不可复现，框架的 "entity construction yields conditional improvement" claim 的 scope 将大幅缩减。
- 建议修改方向：(a) 在主文 §7 或 §9 中更 prominently 讨论 epoch confound（不只是 §8 Related Work 的一句话和 Appendix ab），明确说明 Few-NERD 3-epoch 是一个 under-converged regime；(b) 在 ScIERC 上报告类似的 epoch ablation（ScIERC 使用 5-epoch，Table 56 显示 10-epoch degeneracy 也增加到 17.8%），确认 epoch effect 的一般性；(c) 考虑将 Few-NERD 5-epoch 结果纳入主文 Table 1 或 Table 4 作为 paired comparison。

#### Should-Fix（影响评分但不一票否决）

**W4. [warning] Cross-model ensemble 仅在 Few-NERD 一个数据集上验证，generalization 不足。**
- 具体位置：§5.1 (p.5), Appendix h.4 (p.20)
- 问题："Mixing samples from architecturally distinct models can partially bypass within-model degeneracy"（§5.1）是一个重要 claim，但仅在 Few-NERD 上用 Qwen3-8B + LLaMA-3.1-8B 验证（4+4 samples, ρ=0.42pp improvement）。未在其他 3 个 NER 数据集上验证。
- 建议：至少在 ScIERC 或 CoNLL 上补充 cross-model 结果，或明确将此 claim 降级为 "preliminary observation on Few-NERD"。

**W5. [warning] RE/SQL pilot 覆盖太薄，无法支撑 "extensions to RE and SQL are exploratory" 以外的任何结论。**
- 具体位置：§9 (p.9), Appendix o (p.27), Limitations (p.9)
- 问题：RE 仅 ScIERC（n=397），SQL 仅 n=196。RE 的 diagnostic framework application（Appendix o, Table 29-30）仅一个数据集、一个模型。论文在 Limitations 中已承认这些是 exploratory，但 Abstract 和 §1 中 "exploratory extensions to RE and SQL" 的措辞可能给读者过强的 generalization 印象。
- 建议：在 Abstract 中更明确标注 RE/SQL 的 sample size limitation，或考虑将 SQL pilot 移至 Appendix only（目前 SQL 在主文提及但无主文 table/figure）。

**W6. [warning] Global Holm-Bonferroni p_adj=0.055 的 borderline 处理需更透明讨论。**
- 具体位置：Table 12 (p.23), §7.5 (p.7), Footnote 4 (p.7)
- 问题：在 NER selection family (k=21) 下 p_adj=0.021（significant），但在 global family (k=57) 下 p_adj=0.055（borderline）。论文在脚注中报告了两个数字，但对 family partition choice 未充分讨论。由于实验非 pre-registered，family partition 存在 analyst degrees of freedom：将 k=57 拆分为 4 个 families 会降低每个 family 的校正强度，使更多结果达到显著。
- 建议：在 §7.5 或 Appendix 中增加一段讨论 family partition 的 rationale（为什么 k=21 的 NER selection family 是合理的 analytical unit），并明确说明未 pre-register 这一 partition。

**W7. [warning] LightGBM trained verifier 的 cross-dataset transfer 失败未充分解释 root cause。**
- 具体位置：§5.2 (p.5), Appendix b.2 (p.19)
- 问题：Trained verifier（LightGBM, 5 features）的 cross-dataset transfer 为 negative（−0.76 to −0.70pp）。论文将此归因为 "dataset-specific feature mappings"（§5.2），但未深入分析：是哪些 features 导致 transfer failure？是 dataset-specific entity type distributions 还是 signal distribution shifts？Feature importance analysis 或 leave-one-feature-out ablation 可以提供更清晰的 insight。
- 建议：增加 feature importance breakdown 或简单的 ablation，帮助读者理解 verifier transfer failure 的具体原因。

#### Minor（不影响接收）

**W8. [minor] Figure 1 的 "not causal chain" disclaimer 容易被忽略。**
- 具体位置：Figure 1 caption (p.3)
- 问题：Figure 1 展示了 QE → Selection → Construction 的三阶段 pipeline 流程，caption 中虽注明 "diagnostic sequence, not causal chain"，但视觉呈现（箭头连接）强烈暗示因果关系。读者可能误以为三个阶段有 causal dependency。
- 建议：考虑用不同的视觉编码（如虚线箭头或并列布局）来更好地传达 "diagnostic decomposition" 的含义。

**W9. [minor] Table 3 的 signal family 列标题 "Family" 不直观。**
- 具体位置：Table 3 (p.7)
- "Structural" 和 "Surface" 作为 family 名称首次出现在 Table 3 但未在主文 §2.2 之外充分定义这一 taxonomy。

**W10. [minor] §8 Related Work 的 "Concurrent work" 段引用了 Landesberg (2026) 但描述过于简略。**
- 具体位置：§8 (p.8), §9 (p.9)
- Landesberg (2026) 被描述为 "documents a correlation-selection gap in best-of-N reasoning"（§8），但未充分区分该工作的 setting（global judge, r=0.27 within-prompt ranking）与本文 structured IE setting 的差异。

---

### Questions

**Q1.** §6.3 Proposition 1 假设 entity independence，但 NER 中同一句子的 entities 往往 structurally correlated（shared context, entity type co-occurrence）。Table 31 中 CoNLL 的 bound ratio 为负（−0.42），是否说明 entity dependence 在某些 dataset 上严重违反假设？作者是否考虑过 clustered bootstrap 或 within-sentence correlation 的分析？

**Q2.** 3-epoch vs. 5-epoch ablation（Table 55）显示 LP gains 几乎完全消失。如果 practitioners 正常训练模型到 convergence（5+ epochs），本文的 entity construction 策略在什么条件下仍能提供正增益？论文是否有数据表明某些 task/dataset 在 converged models 上仍有可观的 selection/construction gains？

**Q3.** Hidden-state probe 在 Qwen2.5-7B 上的 AUROC 为 0.63–0.88（Appendix b.3）。Qwen3-8B 的 architecture 变化（如 thinking tokens, §l）是否可能显著改变 hidden-state 的 quality encoding？Table 42（Appendix l.1）显示 pretrained vs. finetuned 的 MV 差异较大——这是否暗示 training configuration 对 probe 结论的影响可能大于 architecture？

**Q4.** Cross-model ensemble（§5.1）仅在 Few-NERD 上测试。Few-NERD 的 degeneracy 相对较低（13.0%），是否意味着 cross-model ensemble 在高 degeneracy datasets（如 CoNLL 61.7%）上效果更差？有没有初步数据？

**Q5.** §7.5 中 "global Holm-Bonferroni (k=57)" 的 family 包含了 NER selection、construction、calibration 和 Δ_p tests。如果按 Šidák 方法或 Benjamini-Hochberg (FDR) 校正，结果是否会有实质性变化？论文在 Table 12 脚注提到 "BH FDR: 19/57 tests are significant at FDR < 0.05"——这一差异是否值得在主文中更 prominently 讨论？

**Q6.** Appendix ag (Failure Mode Gallery, p.45) 展示的 "Consensus-based verification failures" 中，LP 在两个方向上都 fail。这是否意味着 LP 作为 primary quality signal 的可靠性取决于 calibration quality？如果是，为什么 calibration analysis（Appendix c）显示 LP 是 "reasonably well-calibrated" 却不能保证 selection success？

---

### Missing References

1. **Minimum Bayes Risk decoding for structured prediction** — 论文连接了 MBR 和 SC（§6.1, Proposition 2），但未引用 structured prediction 领域的 MBR 经典工作，如 Smith & Eisner (2006) "Minimum Risk Annealing for Training Log-Linear Models" 或 Goel & Byrne (2000) MBR for speech recognition，这些可以加强 theoretical grounding。

2. **Test-time compute scaling** — Snell et al. (2025) 已引用，但 Welleck et al. (2024) "Decoding with Plan" 和 Lightman et al. (2024) "Let's Verify Step by Step"（process reward models）可以丰富 §8 的 Related Work on when/why SC fails。（注：Lightman 已在 References 中但未在 §8 充分讨论。）

---

### Overall Assessment

## 总体评分
**Overall**: 3.5 / 5（Borderline Conference）
**Confidence**: 4 / 5（Quite sure; familiar with self-consistency, test-time scaling, and NER evaluation）
**一句话总结**: 一项极为详尽的实证研究，正确识别了 test-time scaling 在 structured IE 上的 correlation-selection gap，但核心理论贡献（bound）过于宽松、关键正面结果依赖 under-converged model（3-epoch confound）、probe 的 architecture gap 削弱了 introspection boundary 论证。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 主要 claims 有实验支撑，但 Proposition 1 bound 仅 capture 3–12% gains，probe architecture gap 和 epoch confound 各自削弱一条关键论证链。统计方法基本合理但 borderline significance (p_adj=0.055 global) 需更透明讨论。 |
| Excitement | 3/5 | 研究问题重要，correlation-selection gap 是有价值的发现。但 diagnostic（非 predictive）定位、bound 过松、正面增益微弱（+1.40pp）且条件脆弱，限制了 impact。负面结果（69% inverse scaling）有价值但 excitement 上限有限。 |
| Reproducibility | 4/5 | 实验细节极为丰富（Appendix k 报告了 hyperparameters, Table 20），承诺 release code/data/checkpoints。Prompts 在 Appendix k 有展示。部分缺失：exact prompts for all 4 datasets 的完整模板未全部展示。 |
| Overall Assessment | 3.5/5 | Borderline Conference。论文的实验深度和诚实报告值得肯定，但三个 critical issues（bound looseness、architecture gap、epoch confound）各自独立地削弱核心论证。如能在 revision 中：(a) 在 Qwen3-8B 上补 probe 验证，(b) 在主文更充分讨论 epoch confound 及其对 practical applicability 的影响，(c) 将 bound 降级或收紧，则有望达到 4.0（Conference）。 |

## Must-Fix 问题（影响接收决定）
- **W1** Proposition 1 bound 仅 capture 3–12% actual gains（Table 31），定量诊断价值有限
- **W2** Probe 在 Qwen2.5-7B 上运行而非主实验 Qwen3-8B，introspection boundary 论证链有 gap
- **W3** 3-epoch vs. 5-epoch confound：Few-NERD 核心正面结果依赖 under-converged model，91% gain collapse

## Should-Fix 问题
- **W4** Cross-model ensemble 仅 Few-NERD 一个数据集
- **W5** RE (n=397) / SQL (n=196) pilot 太薄
- **W6** Global Holm-Bonferroni family partition 未讨论 rationale
- **W7** LightGBM transfer failure 未做 feature-level root cause analysis

## 主要优势
- 极为详尽的多数据集、多模型实证研究（S1-S2）
- 负面结果的诚实报告对社区有价值（S3）
- Diagnostic vs. predictive 定位清晰、与 MBR 的理论连接有价值（S4）
- 全面的 robustness analysis（S5）
- 可操作的实践指导（S6）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 4174 · 2026-05-22T13:40:41.743325+00:00_

Reviewer 1 初审意见已收到。等待 Reviewer 2 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 315

## Round 315

2 recorded events


### User

_source line 4175 · 2026-05-22T13:40:55.686557+00:00_

[Reviewer 1 审稿结果]:
Round 1 初审完成。

**评分**: Overall 3.5/5（Borderline Conference），Soundness 3.5，Excitement 3，Reproducibility 4，Confidence 4。

**三个 Must-Fix 问题**：
1. Proposition 1 bound 仅 capture 3–12% actual gains，定量诊断价值有限
2. Probe 在 Qwen2.5-7B 而非主实验 Qwen3-8B 上运行，introspection boundary 论证链存在 architecture gap
3. Few-NERD 核心正面结果依赖 3-epoch under-converged model，5-epoch 训练导致 91% gain collapse

**主要优势**：极为详尽的实证工作（45 页）、负面结果诚实报告、diagnostic 定位合理、robustness 检查全面。如能在 revision 中补 Qwen3-8B probe、充分讨论 epoch confound、将 bound 降级或收紧，有望达到 Conference（4.0）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 4176 · 2026-05-22T13:41:00.864333+00:00_

Reviewer 1 初审已收到。等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 316

## Round 316

6 recorded events


### User

_source line 4177 · 2026-05-22T13:41:55.046412+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — Round 1 审稿意见

**论文**: "When Does Test-Time Scaling Fail? A Diagnostic Framework for Named Entity Recognition"
**Venue**: EMNLP 2026 (via ACL Rolling Review)
**审查侧重**: 新颖性 + 完整性 + 写作质量

---

## Summary

本文系统性地研究了 test-time compute scaling（self-consistency）在 NER 任务上何时成功、何时失败。作者在 4 个英文 NER 数据集、2 个模型家族（Qwen3-8B, LLaMA-3.1-8B）上发现了一个 "correlation-selection gap"：质量估计信号（AUROC 达 0.82）能预测输出质量，但 instance-level 选择几乎无法带来增益（MV <1pp，多数情况为负）。论文提出诊断框架，识别两个共现失败机制——degeneracy（多样本坍缩为相同输出）和 LP compression（对数概率方差在 instance 内被压缩），并探索了 entity-level construction 作为缓解策略（+1.40pp on Few-NERD，global Holm p=0.055）。

---

## Strengths

**S1. 系统性与实验规模令人印象深刻。** 论文覆盖 4 个 NER 数据集（SciERC, CoNLL, Few-NERD, WNUT-17）、2 个模型家族（fine-tuned）、多种 N 值（8-64）和采样温度（0.7-1.0），并包含 RE 扩展、temperature/seed robustness（§7.4, Appendix b）、OOD 分析（Appendix v, Table 47）、free-form decoding 消融（Appendix q）等大量补充实验。实验设计的 thoroughness 在分析型论文中属于上乘。

**S2. Correlation-selection gap 的识别清晰且有洞察力。** 论文通过 Figure 1 直观展示了质量估计（左）和选择失败（中）的反差，Table 1 量化了 oracle headroom 与实际选择增益的巨大差距（e.g., SciERC: oracle +7 vs. LP best +0.29）。这一发现对 NER 领域应用 self-consistency 具有直接的实践指导意义。

**S3. 诊断框架的分层结构设计合理。** §2-§6 按 "Discover → Diagnose → Explore conditionals" 三阶段组织，从质量估计到机制诊断到条件性增益，逻辑层层递进。Degeneracy 与 LP compression 作为 co-occurring conditions 的识别（§4, Figure 2）以及 degeneracy decomposition（§6.3）为理解 SC 失败提供了有用的 diagnostic lens。

**S4. 理论连接增加了深度。** Proposition 1（Entity Selection Diagnostic, §6.1）建立了 MV gain 与 entity recall/precision 的关系；Proposition 2（MBR 连接, Appendix p.2）将 entity construction 与 MBR decoding 联系起来。Corollary 1（Critical Degeneracy Threshold）给出了 SC 增益的必要条件。这些理论结果虽然相对简单，但为经验发现提供了形式化支撑。

**S5. 诚实的 framing。** 论文反复强调框架是 "diagnostic rather than predictive"（Abstract, §1, §9），没有过度宣称。Limitations 部分坦诚承认了模型家族局限性、frontier 模型不适用、因果性不足等。

---

## Weaknesses

### Must-Fix 问题（影响接收决定）

**W1** [critical] **正文超过 8 页限制**
- 具体位置：§9 Discussion and Conclusion 起始于 PDF 第 9 页顶部，Limitations 始于第 9 页下半部分
- 问题：EMNLP 2026 long paper 正文严格限制 8 页（Limitations/Ethics/References 不计）。§1-§9 的 main text 约占 8.6 页（§8 Related Work 占满第 8 页，§9 Discussion 延伸到第 9 页约 60-70%），明显超出 8 页限制。
- 为什么影响接收：格式违规是 desk reject 的硬理由，即使 Area Chair 不 desk reject，也会被 reviewer 标记为 format issue 影响评分。
- 建议修改方向：压缩 §8 Related Work（当前密度过高，可精简 "Complementary approaches" 和 "What is new" 子节）；或将部分 §9 Discussion 的 "Open questions" 内容移至 Appendix。

**W2** [critical] **核心定量结果统计显著性不足**
- 具体位置：§7.5, page 7（"Entity-level construction yields conditional improvement (+1.40pp on Few-NERD; global Holm p_adj=0.055"）；Abstract 中 "+1.40pp"
- 问题：Entity construction 是论文唯一提出的改进策略，但 global Holm-Bonferroni 校正后 p=0.055，未达到 0.05 的显著性阈值。论文在 §9（page 9）也承认 "the most liberal claim reaches p_adj=0.055"。更重要的是，该增益仅在 Few-NERD 上显著（p<0.001），在 SciERC 和 CoNLL 上中性甚至微负（Table 65, page 43: SciERC <0.2pp, CoNLL −0.85pp）。
- 为什么影响接收：作为论文从诊断到处方的唯一桥梁，这一结果的 borderline significance 严重削弱了论文的实际贡献。如果这是一篇纯 negative/diagnostic 论文，可以不需要 positive result；但论文在 Abstract 和 §7.5 中将其作为 positive contribution 呈现，这就要求更强的统计支持。
- 建议修改方向：（1）明确将其定位为 exploratory finding 而非 confirmed contribution；（2）补充 effect size 的 confidence interval 和 power analysis；（3）考虑在 Abstract 中降调此结果的表述。

**W3** [critical] **新颖性相对于并发/近期工作的边际贡献偏弱**
- 具体位置：§8 Related Work (page 8), §9 Discussion (page 9), Extended Discussion (page 43-44, Table 66)
- 问题：
  - **Yao et al. (2026)**：已展示 consistency 与 accuracy 在 NER/RE 的 task-level correlation（ρ up to 0.47）。本文声称的 instance-level 延伸——"correlation at task level does not transfer to selection gains at instance level"——虽然是有意义的观察，但本质上是将已知的 calibration 困难（好的 ranking ≠ 好的 selection）应用到了 NER 场景。
  - **Landesberg et al. (2026)**：几乎同时且独立地发现了 best-of-N reasoning 中的 correlation-selection gap（r=0.27 in-prompt ranking vs. quality），且覆盖了更广泛的推理任务。本文的结构化预测视角是差异化的，但核心发现高度重叠。
  - **Yun & Sun (2025)**：diversity collapse 概念与本文的 degeneracy 在机制上相似（output 多样性丧失导致 SC 失败），只是 domain 不同（discrete-answer vs. structured IE）。
  - Table 66（page 44）的 differentiation matrix 显示本文在 "Tasks", "Theoretical content", "Mechanistic probe" 上有差异，但在 "Root cause" 和 "Methods tested" 上与前人工作重叠度较高。
- 为什么影响接收：对于 Conference 级别的接收，reviewer 需要判断贡献是 substantial 还是 incremental。当核心发现（correlation-selection gap）已被并发工作独立发现，且机制解释（degeneracy/diversity collapse）在概念上与前人相似时，本文的增量贡献主要在于 NER-specific 的细粒度诊断，这可能更适合 Findings。
- 建议修改方向：（1）更明确地论述为什么 structured IE 的 instance-level 分析不能从 Yao et al. 的 task-level 结果或 Landesberg et al. 的推理任务结果中推导出来；（2）强调哪些发现是 NER-specific 且无法从已有工作中预测的（e.g., LP compression 的具体机制、entity construction 的条件性增益模式）。

### Should-Fix 问题（影响评分但不一票否决）

**W4** [warning] **69% inverse scaling 与 "conditional gains" framing 之间的紧张关系**
- 具体位置：§6.2 (page 6): "inverse scaling in 69% of N-transitions"；§7.5 (page 7): "conditional improvement (+1.40pp)"；Abstract: "conditional gains"
- 问题：论文的主要发现是 SC 在 NER 上大面积失败（69% 的 N-transition 表现为 inverse scaling，§6.2），但叙事重心却放在条件性增益上。这造成了一种 framing bias：读者可能误以为论文提供了一个可操作的解决方案，但实际上大多数场景下 scaling 是有害的。Discussion（§9, page 9）中的实践建议（"practitioners should measure instance degeneracy at N=8 before committing to repeated inference"）暗示了这一点，但不够突出。
- 建议：在 Abstract 和 Introduction 中更平衡地呈现 negative finding（69% inverse scaling）和 conditional positive finding 的比重。

**W5** [warning] **Related Work 位置和密度**
- 具体位置：§8 Related Work (page 8)
- 问题：Related Work 放在 §8（Experiments 之后、Discussion 之前），这在 *ACL 会议论文中较为少见（通常放在 §2 或论文末尾紧接 Conclusion 之前）。更重要的是，§8 信息密度极高——在约 1 页的空间内覆盖了 6 个子主题（test-time compute scaling, SC failure modes, consistency for structured IE, capability ceiling vs. diversity collapse, complementary approaches, concurrent work, what is new），导致每个方向的讨论都偏表面。
- 建议：考虑将 Related Work 的部分内容前移到 Introduction，以便早期建立与前人工作的 differentiation。

**W6** [warning] **数字密度导致可读性下降**
- 具体位置：贯穿全文，尤其 §4 (page 4), §6 (page 6), §7 (pages 7-8)
- 问题：正文中的统计数字密度极高。例如 §4（page 4）单段中出现 "ρ up to 0.38", "σ≈0.000-0.161", "α=0.068", "S=33", "12-68%", "12.2-67.9%"。§6.2（page 6）单段内 "+1.39pp", "+0.61pp", "p<0.001", "p_adj=0.021", "ℓ=21", "13.0% vs. 12.2-67.9%" 等。这使得 narrative thread 难以跟踪。
- 建议：将更多数字移入表格或 Appendix，正文保留关键数字并用文字描述趋势。

**W7** [warning] **Token-level uncertainty 和 entity-level calibration 的 Related Work 覆盖不足**
- 具体位置：§8 Related Work (page 8)
- 问题：论文使用 5 种 entity/instance-level 信号（SJ, FK, EM, VC, LP），但未充分讨论 NER 领域已有的 token-level uncertainty 方法。具体而言：
  - Token-level uncertainty estimation for sequence labeling（e.g., Vazhentsev et al., 2022; He et al., 2024 等）——论文在 Appendix ab.4 (page 41) 提到了 entity-token LP，但主文缺乏与 token-level uncertainty 文献的系统对比。
  - Entity-level calibration 的先前工作（论文虽引用了 Tian et al. 2023 和 Xie et al. 2023 的 verbalized confidence，但未讨论 NER-specific calibration 如 Ye et al. 2022 或类似工作）。
- 建议：在 §8 或 §2.2 中补充一段讨论 token-level 和 entity-level uncertainty estimation 的已有方法，说明本文选择 instance-level 信号的 motivation。

**W8** [warning] **"Degeneracy" 术语的歧义性**
- 具体位置：§2.1 (page 2) 定义；全文使用
- 问题："Degeneracy" 在不同学科有不同含义（数学中的 degenerate distribution、物理中的 energy degeneracy、机器学习中的 degenerate solution）。本文定义为 "all N samples yield identical F1"（§2.1, page 2），后续又引入 "instance degeneracy"（§2.1）、"per-type degeneracy"（Appendix z, page 38）、"cross-dataset degeneracy"（§6.2）等多个变体。虽然每处都有上下文限定，但对非专家读者可能造成困惑。
- 建议：在首次定义时明确说明为什么选择 "degeneracy" 而非 "output collapse" 或 "diversity loss" 等更直观的术语，或至少在首次出现时给出一个直觉性的解释。

### Minor Issues（不影响接收）

**M1.** §2.3 (page 2)："Spearman ρ between signal and instance-level F1 (exact span-and-type match)" — 但 Table 3 (page 7) 报告的是 per-dataset median F1 binarized at AUROC。Metric 在质量估计和选择评估之间切换（连续 ρ vs. 二值化 AUROC），增加了理解难度。

**M2.** Notation inconsistency："per-sample" (§2.1, page 2) vs. "instance-level" (§1, page 1) vs. "per-instance" (§4, page 4) — 这三个术语在论文中交替使用，Table 5 (page 12) 的 notation 表有助于澄清但仅在 Appendix 中出现。

**M3.** Figure 1 caption (page 3) 中 "diagnostic sequence, not causal chain" 的说明很重要但容易被忽略。

**M4.** §5.3 "Degeneracy Decomposition" (page 5) 的标题可能更适合放在 §6 而非 §5（Adaptive Methods），因为它更偏向分析而非方法。

**M5.** Table 2 (page 5) 的 "GF Criteria" 列使用了缩写（e.g., "n_s≥0.5"），但完整定义直到 Appendix 才出现。

---

## Questions

**Q1.** Entity construction 在 Few-NERD 上的增益（+1.40pp）与 SciERC/CoNLL 上的中性结果之间的差异，作者认为主要驱动因素是什么？是 Few-NERD 的 entity type 多样性（66 fine-grained types）还是其他 dataset-specific 因素？Table 65 (page 43) 的扩展讨论提到了这一点但没有给出明确解释。

**Q2.** 论文在 §3 (page 3) 中发现 entity self-judgment (ESJ) 的 entity-level AUROC 仅为 0.512（与 chance 无异）。这是否意味着 LLM 在 entity-level 完全缺乏 self-verification 能力？还是这个 finding 受限于特定的 prompting 方式？作者是否尝试过其他 self-verification prompt 设计？

**Q3.** Degeneracy 在 Qwen3-8B（Fine-tuned）上为 13.0%，但在 GPT-5.5 上为 12-68%（§1, page 1）。为什么 frontier API model 的 degeneracy 反而更高？这是否与 API 的 temperature 实现有关？

**Q4.** Proposition 1 (§6.1, page 6) 的 "independence assumption" 在实际 NER 样本中成立吗？同一 instance 的不同 samples 之间的 entity predictions 是否存在显著相关性？作者在 Table 7 (page 13) 的 FK independence test 中验证了这一点，但 split-half reliability 仅为 0.395 on SciERC——这是否暗示独立性假设是一个较强的近似？

**Q5.** 论文限于 fine-tuned open-weight models。如果在 instruction-tuned（非 fine-tuned）模型上运行同样的分析，是否预期 degeneracy 模式会有本质不同？§9 (page 9) 提到 "findings from fine-tuned open-weight models may not fully generalize to proprietary systems"，但缺少更具体的 hypothesis。

---

## Missing References

1. **Token-level uncertainty for sequence labeling**: Vazhentsev et al. (2022, "Uncertainty Estimation of Transformer Predictions for Misclassification Detection", ACL) 和相关工作——论文虽有 entity-token LP 分析（Appendix ab.4），但未在 Related Work 中讨论这一研究线。

2. **Structured prediction calibration**: 论文引用了 Angelopoulos & Bates (2023) 但主要在 coverage guarantee 语境下。缺少对 structured output calibration 的更广泛讨论（e.g., Kuleshov et al., 2022 for structured calibration）。

3. **Self-evaluation reliability**: Kadavath et al. (2022, "Language Models (Mostly) Know What They Know") — 论文的 ESJ probe (§3) 与 self-evaluation 文献直接相关但未引用此工作。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 方法论严谨，实验设计全面，但核心 entity construction 结果统计显著性不足（p=0.055）；degeneracy decomposition 的 bound looseness 问题作者自己也承认（§6.3, page 6）；正文超页是硬伤 |
| **Excitement** | 3.0/5 | Correlation-selection gap 的诊断有价值，但核心发现与并发工作（Landesberg et al., 2026; Yao et al., 2026）重叠度高；框架定位为 diagnostic 限制了 actionable impact；对 NER community 有参考价值但难以激发广泛兴趣 |
| **Reproducibility** | 4.0/5 | Appendix 极为详尽（35 页），包含完整的 hyperparameter 配置（Table 20）、prompt templates（Appendix k, page 21）、统计检验细节（Table 12, page 23）。承诺 release code/data upon acceptance |
| **Confidence** | 4/5 | 仔细阅读了全部 45 页，熟悉 self-consistency、NER evaluation、test-time compute 相关文献 |

---

## Overall Assessment

**Overall**: **3.0** (Findings)
**Confidence**: 4/5

**一句话总评**: 这是一篇方法论严谨、实验规模可观的分析型论文，成功识别了 self-consistency 在 NER 上的 correlation-selection gap 并提出了有用的诊断框架，但（1）核心发现与多项并发工作重叠、（2）唯一的改进策略（entity construction）统计显著性不足、（3）正文超出 8 页限制，这些因素共同将论文定位在 Findings 级别。

**详细理由**:
- 论文的核心贡献——诊断 SC 在 structured IE 中的失败模式——是有价值的，但 Landesberg et al. (2026) 同时独立发现了 correlation-selection gap（在 reasoning 任务上），Yao et al. (2026) 已展示了 task-level correlation，Yun & Sun (2025) 已提出 diversity collapse 概念。本文的增量贡献主要在 NER-specific 的细粒度诊断（degeneracy + LP compression 的共现机制），这更接近 targeted analysis 而非 broad contribution。
- Entity construction 作为从诊断到处方的桥梁，在全局统计检验后仅达 borderline significance（p=0.055），且仅在 Few-NERD 上显著。这削弱了论文的实践贡献。
- 正文超页（约 8.6 页）是需要在提交前解决的格式问题。
- 如果作者能（1）压缩到 8 页、（2）更清晰地论证相对于并发工作的独立贡献、（3）对 entity construction 的统计结论做更审慎的表述，本文有潜力上升到 Borderline Conference (3.5)。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 4178 · 2026-05-22T13:42:42.399353+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应：对每个 Weakness 和 Question，标注 **[AGREE]** 并说明理由，或 **[REBUT]** 并提供具体证据（cite Section/Table/Figure）。\n\n特别关注以下分歧点：\n1. Reviewer 2 给出 3.0（Findings），你给出 3.5（Borderline Conference）——你是否同意新颖性不足以达到 Conference 级别？\n2. Reviewer 2 认为正文超 8 页是 Must-Fix（desk reject 风险），你的意见？\n3. Reviewer 2 认为 entity construction p=0.055 应定位为 exploratory finding 而非 confirmed contribution，你是否同意？\n\n---\n\n以下是 Reviewer 2 完整原文：\n\n## Summary\n\n本文系统性地研究了 test-time compute scaling（self-consistency）在 NER 任务上何时成功、何时失败。作者在 4 个英文 NER 数据集、2 个模型家族（Qwen3-8B, LLaMA-3.1-8B）上发现了一个 \"correlation-selection gap\"：质量估计信号（AUROC 达 0.82）能预测输出质量，但 instance-level 选择几乎无法带来增益（MV <1pp，多数情况为负）。论文提出诊断框架，识别两个共现失败机制——degeneracy（多样本坍缩为相同输出）和 LP compression（对数概率方差在 instance 内被压缩），并探索了 entity-level construction 作为缓解策略（+1.40pp on Few-NERD，global Holm p=0.055）。\n\n## Strengths\n\n**S1. 系统性与实验规模令人印象深刻。**\n**S2. Correlation-selection gap 的识别清晰且有洞察力。**\n**S3. 诊断框架的分层结构设计合理。**\n**S4. 理论连接增加了深度。**\n**S5. 诚实的 framing。**\n\n## Weaknesses\n\n### Must-Fix\n\n**W1** [critical] **正文超过 8 页限制**\n- §9 Discussion and Conclusion 起始于 PDF 第 9 页顶部，Limitations 始于第 9 页下半部分。EMNLP 2026 long paper 正文严格限制 8 页。约 8.6 页，明显超出。格式违规是 desk reject 的硬理由。\n- 建议：压缩 §8 Related Work 或将部分 §9 Discussion 移至 Appendix。\n\n**W2** [critical] **核心定量结果统计显著性不足**\n- Entity construction global Holm-Bonferroni p=0.055，未达 0.05。该增益仅在 Few-NERD 上显著，SciERC 和 CoNLL 中性甚至微负。作为论文唯一的改进策略，borderline significance 严重削弱实际贡献。\n- 建议：明确定位为 exploratory finding；补充 effect size CI 和 power analysis；Abstract 降调。\n\n**W3** [critical] **新颖性相对于并发/近期工作的边际贡献偏弱**\n- Yao et al. (2026) 已展示 task-level correlation（ρ up to 0.47），instance-level 延伸可能是 incremental extension。\n- Landesberg et al. (2026) 独立发现 correlation-selection gap，核心发现高度重叠。\n- Yun & Sun (2025) diversity collapse 与 degeneracy 概念上相似。\n- 增量贡献主要在 NER-specific 细粒度诊断，可能更适合 Findings。\n\n### Should-Fix\n\n**W4** [warning] **69% inverse scaling 与 \"conditional gains\" framing 紧张关系** — framing bias。\n**W5** [warning] **Related Work 位置和密度** — 放在 §8 较少见，密度过高。\n**W6** [warning] **数字密度导致可读性下降** — 正文统计数字过多。\n**W7** [warning] **Token-level uncertainty 和 entity-level calibration Related Work 覆盖不足**\n**W8** [warning] **\"Degeneracy\" 术语歧义性** — 建议解释术语选择。\n\n### Minor\nM1-M5（metric 切换理解难度、notation inconsistency、Figure 1 caption、§5.3 标题位置、Table 2 缩写）\n\n## Questions\nQ1. Few-NERD vs SciERC/CoNLL 增益差异的驱动因素？\nQ2. ESJ AUROC 0.512 是否受限于 prompting 方式？\nQ3. GPT-5.5 degeneracy 更高的原因？\nQ4. Proposition 1 independence assumption 在 NER 中成立吗？\nQ5. Instruction-tuned（非 fine-tuned）模型的 degeneracy 模式预期？\n\n## Missing References\n1. Vazhentsev et al. (2022) token-level uncertainty\n2. Kuleshov et al. (2022) structured calibration\n3. Kadavath et al. (2022) self-evaluation reliability\n\n## Overall Assessment\n**Overall**: 3.0 (Findings), Confidence 4/5",
  "project": "struct_self_consist_ie",
  "chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应：对每个 Weakness 和 Question，标注 **[AGREE]** 并说明理由，或 **[REBUT]** 并提供具体证据（cite Section/Table/Figure）。\n\n特别关注以下分歧点：\n1. Reviewer 2 给出 3.0（Findings），你给出 3.5（Borderline Conference）——你是否同意新颖性不足以达到 Conference 级别？\n2. Reviewer 2 认为正文超 8 页是 Must-Fix（desk reject 风险），你的意见？\n3. Reviewer 2 认为 entity construction p=0.055 应定位为 exploratory finding 而非 confirmed contribution，你是否同意？\n\n---\n\n以下是 Reviewer 2 完整原文：\n\n## Summary\n\n本文系统性地研究了 test-time compute scaling（self-consistency）在 NER 任务上何时成功、何时失败。作者在 4 个英文 NER 数据集、2 个模型家族（Qwen3-8B, LLaMA-3.1-8B）上发现了一个 \"correlation-selection gap\"：质量估计信号（AUROC 达 0.82）能预测输出质量，但 instance-level 选择几乎无法带来增益（MV <1pp，多数情况为负）。论文提出诊断框架，识别两个共现失败机制——degeneracy（多样本坍缩为相同输出）和 LP compression（对数概率方差在 instance 内被压缩），并探索了 entity-level construction 作为缓解策略（+1.40pp on Few-NERD，global Holm p=0.055）。\n\n## Strengths\n\n**S1. 系统性与实验规模令人印象深刻。**\n**S2. Correlation-selection gap 的识别清晰且有洞察力。**\n**S3. 诊断框架的分层结构设计合理。**\n**S4. 理论连接增加了深度。**\n**S5. 诚实的 framing。**\n\n## Weaknesses\n\n### Must-Fix\n\n**W1** [critical] **正文超过 8 页限制**\n- §9 Discussion and Conclusion 起始于 PDF 第 9 页顶部，Limitations 始于第 9 页下半部分。EMNLP 2026 long paper 正文严格限制 8 页。约 8.6 页，明显超出。格式违规是 desk reject 的硬理由。\n- 建议：压缩 §8 Related Work 或将部分 §9 Discussion 移至 Appendix。\n\n**W2** [critical] **核心定量结果统计显著性不足**\n- Entity construction global Holm-Bonferroni p=0.055，未达 0.05。该增益仅在 Few-NERD 上显著，SciERC 和 CoNLL 中性甚至微负。作为论文唯一的改进策略，borderline significance 严重削弱实际贡献。\n- 建议：明确定位为 exploratory finding；补充 effect size CI 和 power analysis；Abstract 降调。\n\n**W3** [critical] **新颖性相对于并发/近期工作的边际贡献偏弱**\n- Yao et al. (2026) 已展示 task-level correlation（ρ up to 0.47），instance-level 延伸可能是 incremental extension。\n- Landesberg et al. (2026) 独立发现 correlation-selection gap，核心发现高度重叠。\n- Yun & Sun (2025) diversity collapse 与 degeneracy 概念上相似。\n- 增量贡献主要在 NER-specific 细粒度诊断，可能更适合 Findings。\n\n### Should-Fix\n\n**W4** [warning] **69% inverse scaling 与 \"conditional gains\" framing 紧张关系** — framing bias。\n**W5** [warning] **Related Work 位置和密度** — 放在 §8 较少见，密度过高。\n**W6** [warning] **数字密度导致可读性下降** — 正文统计数字过多。\n**W7** [warning] **Token-level uncertainty 和 entity-level calibration Related Work 覆盖不足**\n**W8** [warning] **\"Degeneracy\" 术语歧义性** — 建议解释术语选择。\n\n### Minor\nM1-M5（metric 切换理解难度、notation inconsistency、Figure 1 caption、§5.3 标题位置、Table 2 缩写）\n\n## Questions\nQ1. Few-NERD vs SciERC/CoNLL 增益差异的驱动因素？\nQ2. ESJ AUROC 0.512 是否受限于 prompting 方式？\nQ3. GPT-5.5 degeneracy 更高的原因？\nQ4. Proposition 1 independence assumption 在 NER 中成立吗？\nQ5. Instruction-tuned（非 fine-tuned）模型的 degeneracy 模式预期？\n\n## Missing References\n1. Vazhentsev et al. (2022) token-level uncertainty\n2. Kuleshov et al. (2022) structured calibration\n3. Kadavath et al. (2022) self-evaluation reliability\n\n## Overall Assessment\n**Overall**: 3.0 (Findings), Confidence 4/5",
    "project": "struct_self_consist_ie",
    "chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 4179 · 2026-05-22T13:43:16.666353+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 34267
}
```

</details>

---


### Tool call

_source line 4180 · 2026-05-22T13:43:16.868528+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1 的完整 Round 1 审稿意见。请逐条回应：对每个 Weakness 和 Question，标注 **[AGREE]** 并说明理由，或 **[REBUT]** 并提供具体证据（cite Section/Table/Figure）。\n\n特别关注以下分歧点：\n1. Reviewer 1 给出 3.5（Borderline Conference），你给出 3.0（Findings）——你是否认为 Reviewer 1 对方法严谨性的评价过于宽容？\n2. Reviewer 1 将 Proposition 1 bound looseness 列为 Must-Fix，你虽未将其列为独立 weakness 但在 Soundness 评语中提及——你对 bound 的诊断价值如何评估？\n3. Reviewer 1 认为 probe architecture gap 是 critical issue，你未提及此点——你是否同意这是 Must-Fix？\n\n---\n\n以下是 Reviewer 1 完整原文：\n\n## Summary\n\n本文研究 test-time compute scaling（重复采样 + self-consistency / best-of-N）在 NER 任务上何时成功、何时失败。作者在 4 个英文 NER 数据集和 2 个模型家族上进行了大规模实证研究，发现质量估计信号（AUROC 最高 0.82）能预测输出质量，但 instance-level selection 大多失败（MV gain < 1pp）。论文提出以 degeneracy + signal alignment collapse 作为联合诊断条件的框架，并给出 entity construction 在有利条件下可获得 +1.40pp 的微弱正向增益。\n\n## Strengths\n\n**S1. 研究问题重要且切入点好。**\n**S2. 实证工作极为详尽（45 页含 36 页附录）。**\n**S3. 负面结果诚实报告（69% inverse scaling, cross-dataset transfer negative, 5-epoch collapse）。**\n**S4. Diagnostic vs. predictive 定位清晰，MBR 理论联系有价值。**\n**S5. Robustness 检查全面。**\n**S6. 实用指导明确（§9 \"When not to scale\"）。**\n\n## Weaknesses\n\n### Must-Fix\n\n**W1** [critical] **Proposition 1 bound 过于宽松，削弱定量诊断核心价值**\n- (1−D)·G_nd·α 仅 capture 3–12% actual gains（Table 31）。\n- Entity independence assumption（split-half r=0.578–0.644）和 conservative α estimation 导致 bound 几乎无实践诊断价值。\n- 建议：降级为 illustrative lower bound，不在 §1 突出；讨论收紧方向；或提供 empirical tighter bound。\n\n**W2** [critical] **Probe 使用 Qwen2.5-7B 而非主实验 Qwen3-8B，architecture validity gap**\n- Hidden-state probe 和 entity self-verification 均在 Qwen2.5-7B 上运行。\n- Introspection boundary 是框架重要组成，architecture mismatch 削弱论证链。\n- 建议：在 Qwen3-8B 上重新运行 probe（至少一个数据集），或论证 architecture gap 不改变定性结论。\n\n**W3** [critical] **3-epoch vs. 5-epoch confound 威胁 Few-NERD 主结论**\n- 5-epoch 使 LP gains 从 +1.38 降至 +0.12±0.04pp（91% collapse）。\n- Few-NERD 正面结果依赖 under-converged model。如果最佳实践是 train to convergence，LP selection practical applicability 大幅受限。\n- 建议：主文更 prominently 讨论；ScIERC 补 epoch ablation；Few-NERD 5-epoch 纳入主文 Table。\n\n### Should-Fix\n\n**W4** [warning] Cross-model ensemble 仅 Few-NERD 一个数据集。\n**W5** [warning] RE (n=397) / SQL (n=196) pilot 太薄。\n**W6** [warning] Global Holm-Bonferroni family partition 未讨论 rationale。\n**W7** [warning] LightGBM transfer failure 未做 feature-level root cause analysis。\n\n### Minor\nW8 (Figure 1 causal implication), W9 (Table 3 Family label), W10 (Landesberg description).\n\n## Questions\nQ1. CoNLL bound ratio 负值是否说明 entity dependence 严重违反假设？\nQ2. 在 converged models 上 entity construction 仍能获正增益的条件？\nQ3. Qwen3 architecture 变化是否可能改变 probe 结论？\nQ4. Cross-model ensemble 在高 degeneracy datasets 上效果？\nQ5. BH FDR 19/57 significant 是否值得 prominently 讨论？\nQ6. LP calibration vs. selection success 的关系？\n\n## Missing References\n1. Smith & Eisner (2006), Goel & Byrne (2000) — MBR for structured prediction\n2. Welleck et al. (2024), Lightman et al. (2024) — SC failure / process reward\n\n## Overall Assessment\n**Overall**: 3.5 (Borderline Conference), Confidence 4/5\n\n核心判断：极详尽的实证研究，3 个 critical issues（bound, probe gap, epoch confound）各自独立削弱核心论证。如能 revision 修复，有望达 4.0。",
  "project": "struct_self_consist_ie",
  "chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1 的完整 Round 1 审稿意见。请逐条回应：对每个 Weakness 和 Question，标注 **[AGREE]** 并说明理由，或 **[REBUT]** 并提供具体证据（cite Section/Table/Figure）。\n\n特别关注以下分歧点：\n1. Reviewer 1 给出 3.5（Borderline Conference），你给出 3.0（Findings）——你是否认为 Reviewer 1 对方法严谨性的评价过于宽容？\n2. Reviewer 1 将 Proposition 1 bound looseness 列为 Must-Fix，你虽未将其列为独立 weakness 但在 Soundness 评语中提及——你对 bound 的诊断价值如何评估？\n3. Reviewer 1 认为 probe architecture gap 是 critical issue，你未提及此点——你是否同意这是 Must-Fix？\n\n---\n\n以下是 Reviewer 1 完整原文：\n\n## Summary\n\n本文研究 test-time compute scaling（重复采样 + self-consistency / best-of-N）在 NER 任务上何时成功、何时失败。作者在 4 个英文 NER 数据集和 2 个模型家族上进行了大规模实证研究，发现质量估计信号（AUROC 最高 0.82）能预测输出质量，但 instance-level selection 大多失败（MV gain < 1pp）。论文提出以 degeneracy + signal alignment collapse 作为联合诊断条件的框架，并给出 entity construction 在有利条件下可获得 +1.40pp 的微弱正向增益。\n\n## Strengths\n\n**S1. 研究问题重要且切入点好。**\n**S2. 实证工作极为详尽（45 页含 36 页附录）。**\n**S3. 负面结果诚实报告（69% inverse scaling, cross-dataset transfer negative, 5-epoch collapse）。**\n**S4. Diagnostic vs. predictive 定位清晰，MBR 理论联系有价值。**\n**S5. Robustness 检查全面。**\n**S6. 实用指导明确（§9 \"When not to scale\"）。**\n\n## Weaknesses\n\n### Must-Fix\n\n**W1** [critical] **Proposition 1 bound 过于宽松，削弱定量诊断核心价值**\n- (1−D)·G_nd·α 仅 capture 3–12% actual gains（Table 31）。\n- Entity independence assumption（split-half r=0.578–0.644）和 conservative α estimation 导致 bound 几乎无实践诊断价值。\n- 建议：降级为 illustrative lower bound，不在 §1 突出；讨论收紧方向；或提供 empirical tighter bound。\n\n**W2** [critical] **Probe 使用 Qwen2.5-7B 而非主实验 Qwen3-8B，architecture validity gap**\n- Hidden-state probe 和 entity self-verification 均在 Qwen2.5-7B 上运行。\n- Introspection boundary 是框架重要组成，architecture mismatch 削弱论证链。\n- 建议：在 Qwen3-8B 上重新运行 probe（至少一个数据集），或论证 architecture gap 不改变定性结论。\n\n**W3** [critical] **3-epoch vs. 5-epoch confound 威胁 Few-NERD 主结论**\n- 5-epoch 使 LP gains 从 +1.38 降至 +0.12±0.04pp（91% collapse）。\n- Few-NERD 正面结果依赖 under-converged model。如果最佳实践是 train to convergence，LP selection practical applicability 大幅受限。\n- 建议：主文更 prominently 讨论；ScIERC 补 epoch ablation；Few-NERD 5-epoch 纳入主文 Table。\n\n### Should-Fix\n\n**W4** [warning] Cross-model ensemble 仅 Few-NERD 一个数据集。\n**W5** [warning] RE (n=397) / SQL (n=196) pilot 太薄。\n**W6** [warning] Global Holm-Bonferroni family partition 未讨论 rationale。\n**W7** [warning] LightGBM transfer failure 未做 feature-level root cause analysis。\n\n### Minor\nW8 (Figure 1 causal implication), W9 (Table 3 Family label), W10 (Landesberg description).\n\n## Questions\nQ1. CoNLL bound ratio 负值是否说明 entity dependence 严重违反假设？\nQ2. 在 converged models 上 entity construction 仍能获正增益的条件？\nQ3. Qwen3 architecture 变化是否可能改变 probe 结论？\nQ4. Cross-model ensemble 在高 degeneracy datasets 上效果？\nQ5. BH FDR 19/57 significant 是否值得 prominently 讨论？\nQ6. LP calibration vs. selection success 的关系？\n\n## Missing References\n1. Smith & Eisner (2006), Goel & Byrne (2000) — MBR for structured prediction\n2. Welleck et al. (2024), Lightman et al. (2024) — SC failure / process reward\n\n## Overall Assessment\n**Overall**: 3.5 (Borderline Conference), Confidence 4/5\n\n核心判断：极详尽的实证研究，3 个 critical issues（bound, probe gap, epoch confound）各自独立削弱核心论证。如能 revision 修复，有望达 4.0。",
    "project": "struct_self_consist_ie",
    "chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 4181 · 2026-05-22T13:43:18.377329+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1508
}
```

</details>

---


### Assistant

_source line 4182 · 2026-05-22T13:43:20.979307+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 317

## Round 317

2 recorded events


### User

_source line 4183 · 2026-05-22T13:43:23.647121+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结果摘要**：

- **Overall: 3.0 (Findings)**，Confidence 4/5
- **3 个 Must-Fix**：正文超 8 页限制（~8.6 页）、entity construction 核心结果 p=0.055 统计显著性不足、相对于 Landesberg et al./Yao et al./Yun & Sun 的并发工作新颖性偏弱
- **5 个 Should-Fix**：69% inverse scaling 与 conditional gains 的 framing 失衡、Related Work 密度过高且位置不佳、数字密度影响可读性、token-level uncertainty 文献覆盖不足、degeneracy 术语歧义
- **5 个 Minor**：metric 切换、notation 不一致、figure caption 细节、section 归属、缩写定义位置
- **5 个 Questions**：Few-NERD 增益的 dataset-specific 驱动因素、ESJ 的 prompting 限制、frontier model degeneracy 成因、独立性假设强度、instruction-tuned 模型的预期差异

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 4184 · 2026-05-22T13:43:28.282675+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 318

## Round 318

2 recorded events
