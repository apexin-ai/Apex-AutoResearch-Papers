# Director coordination — Part 8 of 10

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

[← Part 7](part-007.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 9 →](part-009.md) · [Structured JSON](../../../sessions/0f/0fa49ecfe50583d66f9a.json)

## Round 194

### Tool call

_source line 2346 · 2026-05-19T17:46:17.000096+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026（通过 ACL Rolling Review May 2026 提交）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，正文严格 8 页，参考文献不限，Limitations + Ethics 不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（无作者名、无非匿名链接）\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n**新颖性与完整性**，具体包括：\n\n1. **贡献定位**：SCS/BCS 的 formal definition 与 LLM-PEE 的 partitioning criterion 相同（论文自己承认），novelty 是否足够支撑 EMNLP 接收？\"controlled experimental framework\" 作为主要贡献是否足够？\n2. **Related Work 覆盖**：是否遗漏了重要的 schema complexity / LLM IE / error analysis 相关工作？concurrent work 的引用是否充分？\n3. **Title 与 Abstract 准确性**：Title \"Information Extraction\" 是否过宽（NER Dim2 batch-level null）？Abstract 中的数字和 claims 是否都有充分支撑？\"first controlled study\" 的 claim 是否站得住脚？\n4. **论文结构与叙事**：8 页正文是否分配合理？是否有过度压缩或过度展开的部分？负面结果（SDGD）的呈现是否平衡？\n5. **写作质量**：语言是否清晰简洁？是否有 AI 写作痕迹（过度 hedging、-ing 分词串、redundant qualifiers）？符号使用是否一致？\n6. **格式合规**：页数是否在 8 页限制内？引用格式是否符合 ACL 标准？图表是否清晰可读？匿名是否完整？\n7. **MAVEN / ED 的贡献**：MAVEN 作为第四个数据集，受 centrality confound 影响 batch-level null，其实质贡献是什么？ED 在论文中的地位是否边缘化？\n8. **Practical implications**：论文建议 \"flag type pairs with SCS > 0.85\"，但 renaming 失败、decomposition 失败、few-shot 加剧——实际可操作建议是什么？\n9. **Missing references 审查**：重点检查 2024-2026 年间的 LLM IE、schema complexity、error taxonomy 相关工作。\n\n请给出完整审稿报告，按 Strengths → Weaknesses（逐条编号，标注 [Must-Fix] / [Should-Fix] / [Minor]） → Questions → Missing References 的结构。"
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
    "text": "你是 Reviewer 2，负责**新颖性与完整性**审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026（通过 ACL Rolling Review May 2026 提交）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，正文严格 8 页，参考文献不限，Limitations + Ethics 不计入页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind（无作者名、无非匿名链接）\n\n## 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf`\n\n## 你的审查侧重\n\n**新颖性与完整性**，具体包括：\n\n1. **贡献定位**：SCS/BCS 的 formal definition 与 LLM-PEE 的 partitioning criterion 相同（论文自己承认），novelty 是否足够支撑 EMNLP 接收？\"controlled experimental framework\" 作为主要贡献是否足够？\n2. **Related Work 覆盖**：是否遗漏了重要的 schema complexity / LLM IE / error analysis 相关工作？concurrent work 的引用是否充分？\n3. **Title 与 Abstract 准确性**：Title \"Information Extraction\" 是否过宽（NER Dim2 batch-level null）？Abstract 中的数字和 claims 是否都有充分支撑？\"first controlled study\" 的 claim 是否站得住脚？\n4. **论文结构与叙事**：8 页正文是否分配合理？是否有过度压缩或过度展开的部分？负面结果（SDGD）的呈现是否平衡？\n5. **写作质量**：语言是否清晰简洁？是否有 AI 写作痕迹（过度 hedging、-ing 分词串、redundant qualifiers）？符号使用是否一致？\n6. **格式合规**：页数是否在 8 页限制内？引用格式是否符合 ACL 标准？图表是否清晰可读？匿名是否完整？\n7. **MAVEN / ED 的贡献**：MAVEN 作为第四个数据集，受 centrality confound 影响 batch-level null，其实质贡献是什么？ED 在论文中的地位是否边缘化？\n8. **Practical implications**：论文建议 \"flag type pairs with SCS > 0.85\"，但 renaming 失败、decomposition 失败、few-shot 加剧——实际可操作建议是什么？\n9. **Missing references 审查**：重点检查 2024-2026 年间的 LLM IE、schema complexity、error taxonomy 相关工作。\n\n请给出完整审稿报告，按 Strengths → Weaknesses（逐条编号，标注 [Must-Fix] / [Should-Fix] / [Minor]） → Questions → Missing References 的结构。"
  }
}
```

</details>

---


### Tool result

_source line 2347 · 2026-05-19T17:46:18.672563+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1672
}
```

</details>

---


### Assistant

_source line 2348 · 2026-05-19T17:46:27.494770+00:00_

任务已全部派发：

- **视觉审查 Agent**：已启动（fire-and-forget，不阻塞）
- **Reviewer 1**（方法严谨性）：已分配 Round 1 任务
- **Reviewer 2**（新颖性/完整性）：已分配 Round 1 任务
- **外部审稿**：跳过（项目未启用 `external_review.paperreview_ai`）

等待两位 Reviewer 返回初审报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 195

## Round 195

4 recorded events


### User

_source line 2349 · 2026-05-19T17:54:29.739397+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告：方法严谨性审查

### 总体评分
**Overall**: 3.5 / 5 — Borderline Conference
**一句话总结**: 本文提出了一个重要且未被充分研究的问题，实验设计用心、附录详尽，但单种子设计导致置信区间低估不确定性、TOST 等价性 margin 选择存在循环论证倾向、部分结论超出证据支撑力度，这些方法论问题需要修复后才能给出可靠的量化结论。

### 官方维度打分（ACL Rolling Review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心实验设计（count-curve + BCS-controlled）互补且合理，附录提供了大量鲁棒性检验。但单种子+FP8噪声使CI偏窄；TOST margin选择有循环性；部分ablation样本量不足却得出过强结论。 |
| Excitement | 3.5/5 | 首次系统研究schema complexity对zero-shot LLM IE的影响，SCS/BCS度量体系有新意。但pair-level效应量极小（r²~1-3%），实际可操作建议有限。 |
| Overall Assessment | 3.5/5 | Borderline Conference。修复N1/N2后可达Conference水平。 |
| Confidence | 4/5 | 仔细阅读全文26页含17个Appendix，熟悉TOST、bootstrap CI、相关/因果推断方法论。 |
| Reproducibility | 3.5/5 | 实验设置描述详细，代码承诺release。但单种子+FP8量化使精确复现有难度。 |

---

### Must-Fix 问题（影响接收决定）

**N1** [critical] 单种子设计 + FP8非确定性噪声导致CI系统性偏窄

- 位置：§3.5（seed 42, greedy decoding）；Appendix Q（residual SD = 0.88pp）
- 全部bootstrap CI仅捕获batch composition variance，未纳入模型级方差（不同种子/FP8实现）。0.88pp噪声占TOST ±3pp margin的~30%；pairwise r²仅1-3%时此噪声不可忽视。BCS-controlled实验在FewRel上仅用27个batch且无种子变异→CI不含模型级不确定性。
- 建议：补充3-5个种子实验，或将FP8噪声传播进bootstrap产生保守CI。

**N2** [critical] TOST等价性margin（±3pp）选择存在循环论证倾向

- 位置：Appendix C, Table 8；§4.1
- ±3pp的首要理由是"approximates the typical BCS-predicted accuracy gap"——用BCS自身预测力校准"count效应可忽略"的阈值，而TOST目的正是验证BCS独立于count的预测力。灵敏度分析显示±2pp时FewRel仅勉强通过（p=0.047），DocRED inconclusive，说明结论对margin高度敏感。
- 建议：将Cohen's δ作为首要理由；在正文报告±2pp结果；提供外部基准anchor。

---

### Should-Fix 问题

**W1** [warning] Pair-to-batch R²放大（1.7%→22-58%）理论解释不够solid
- 位置：§4.2-4.3；Appendix M
- Simulation假设pair-level效应独立（但同batch types共享prompt上下文）；observed batch R²超出simulation预测；论文自身分析（§4.5）表明并非所有pairs均等贡献。
- 建议：补充非独立性讨论；参考ecological inference文献。

**W2** [warning] DocRED factorial range-matching消除interaction但未做power analysis
- 位置：Appendix C, p.16
- Full-range: −9.4pp (CI [-12.9, -6.01])，显著。Range-matched: 0.93pp (CI [-7.13, 7.44])，CI跨零但宽度~14pp→power严重不足。Non-significance ≠ absence of effect。
- 建议：报告range-matched子集n和post-hoc power；诚实讨论两个分析的张力。

**W3** [warning] Dimension 2 cross-model验证不足但claim过宽
- 位置：§4.1, Appendix S/T
- BCS-controlled仅在Llama-3.1-8B验证，NER上8B模型floor effects。Abstract/Intro措辞未区分两个维度的验证范围。
- 建议：在Abstract/Intro限定Dimension 2验证范围。

**W4** [warning] 因果语言超出相关性证据
- Title "Predict"、§5 "degradation due to"、renaming experiment的familiarity confound（同时改变embedding similarity和label familiarity两个变量）。
- 建议：统一predictive语言；讨论renaming的familiarity confound。

**W5** [warning] Unconstrained decoding ablation结论过强
- 位置：§5
- n=25，未做Fisher z-test比较constrained vs unconstrained的ρ差异。Non-significance at n=25 ≠ absence of correlation。
- 建议：补充formal comparison；降低结论语气。

**W6** [warning] Few-shot实验confounding控制不足
- 位置：Appendix U
- 高BCS batch中随机few-shot examples可能对高混淆types区分度更低。未控制example discriminativeness。"structural property not addressable by prompt engineering"结论过强。

---

### Minor Issues

- **M1**: Rothman (1990)作为不做多重比较校正的唯一理由不足。建议补充讨论为何不做Holm校正。
- **M2**: Logit-scale TOST inconclusive但被低估。Logit scale对bounded data更合理。
- **M3**: Appendix M中EF=3.35如为从observed R²反推，则公式为同义反复。
- **M4**: MAVEN同质schema限制了其对general confusability claim的支撑力。

---

### 主要优势

- **S1**: 研究问题重要且填补明确空白（zero-shot LLM IE中schema complexity影响的首次系统研究）
- **S2**: Count-curve + BCS-controlled两种范式互补设计精巧
- **S3**: 17个Appendix的深度和透明度罕见，Limitations section非常诚实
- **S4**: 四数据集跨三任务的cross-dataset一致性
- **S5**: 负面结果（SDGD失败）的诚实报告
- **S6**: Prompt sensitivity验证（v1/v2一致）增强核心finding credibility

---

### Questions to Authors

1. 能否提供至少3个种子的BCS-controlled实验结果（即使仅FewRel）以回应N1？
2. TOST ±3pp margin是否有来自先前LLM IE工作的external benchmark？
3. DocRED显著交互（−9.4pp）与FewRel TOST通过之间的张力如何调和？是否应限定"bounded interaction"的适用范围？
4. Appendix M中EF=3.35是independent estimate还是从observed R²反推？

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


### Tool call

_source line 2350 · 2026-05-19T17:54:54.596231+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6: 外部审稿线 — 跳过（未配置）', 'status': 'completed', 'activeForm': '跳过外部审稿'}, {'content': 'Step 0.7: 视觉审查派发', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿 — R1 已返回，等待 R2', 'status': 'in_progress', 'activeForm': '等待 Reviewer 2 返回'}, {'content': 'Step 2: 交叉分享 — 转发审稿意见给对方 Reviewer', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
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
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '执行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6: 外部审稿线 — 跳过（未配置）', 'status': 'completed', 'activeForm': '跳过外部审稿'}, {'content': 'Step 0.7: 视觉审查派发', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿 — R1 已返回，等待 R2', 'status': 'in_progress', 'activeForm': '等待 Reviewer 2 返回'}, {'content': 'Step 2: 交叉分享 — 转发审稿意见给对方 Reviewer', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2351 · 2026-05-19T17:54:54.647040+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 2352 · 2026-05-19T17:54:56.992713+00:00_

Reviewer 1 审稿报告已收到。记录关键发现，等待 Reviewer 2 返回后进入交叉分享。

**Reviewer 1 核心发现摘要：**
- Overall: 3.5（Borderline Conference）
- **N1** [critical]: 单种子 + FP8 噪声 → CI 系统性偏窄
- **N2** [critical]: TOST ±3pp margin 循环论证
- 6 个 Should-Fix（R² 放大解释、DocRED range-match power、Dim2 验证范围、因果语言、unconstrained ablation 结论过强、few-shot confounding）
- 4 个 Minor

等待 Reviewer 2 报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 196

## Round 196

2 recorded events


### User

_source line 2353 · 2026-05-19T17:54:59.636203+00:00_

[Reviewer 1 审稿结果]:
审稿报告已完成并发送给 Review Director。

总结：Overall 3.5（Borderline Conference）。两个 Must-Fix：(N1) 单种子+FP8噪声使全文CI偏窄，需补种子实验或传播噪声；(N2) TOST ±3pp margin以BCS自身预测力为锚存在循环性，且结论对margin选择高度敏感。六个 Should-Fix 涵盖 pair-to-batch R²放大理论缺口、DocRED factorial power不足、Dim2 cross-model验证缺口、因果语言越界、unconstrained decoding ablation过强结论、few-shot confounding。核心优势是研究问题重要、两范式互补设计精巧、附录透明度罕见。修复N1/N2后可达Conference水平。

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

_source line 2354 · 2026-05-19T17:55:05.423163+00:00_

已收到 Reviewer 1 确认。等待 Reviewer 2 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 197

## Round 197

8 recorded events


### User

_source line 2355 · 2026-05-19T17:55:17.307434+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告：新颖性与完整性

### 总体评分
**Overall Assessment**: 3.0 — Findings（可被 Findings 接收）
**一句话总结**: 方法论严谨的实证分析，准确刻画了 schema complexity 的两维度退化模式，但核心发现（confusable types hurt performance）的新颖性有限，标题声称覆盖 "Information Extraction" 而实际仅 RE 全面支持 batch-level confusability 效应，且未找到任何有效 mitigation，excitement 不足以达到主会议水平。

### 官方维度打分（ACL ARR Review Form）
| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 实验设计严谨，统计方法规范（TOST/bootstrap CI/permutation），负面结果诚实报告 |
| Excitement | 2.5/5 | 核心发现直觉上可预期；SCS/BCS 无技术新意（cosine sim + mean）；无有效 mitigation |
| Reproducibility | 4/5 | 模型/数据集/prompt/超参数明确；18页appendix；代码承诺公开 |
| Confidence | 4/5 | 全文26页（含appendix）仔细阅读，引用已核查 |

---

### Strengths
**S1.** 精心设计的控制实验框架（count curves + BCS-controlled batches），在 LLM IE 领域少见的严谨受控实验方法论
**S2.** 诚实报告 null/负面结果（NER batch-level null, MAVEN centrality confound, SDGD全面失败）
**S3.** 统计方法论规范（TOST equivalence tests, bootstrap CIs, permutation tests），显著优于领域平均水平
**S4.** 多任务覆盖（NER/RE/DocRE/ED）+ 跨模型复现（Llama-3.1-8B/70B, Gemini 2.5 Flash）
**S5.** Error taxonomy（§4.4 Figure 2）有独立价值

---

### Must-Fix 问题

**N1** [critical] **Title/Abstract scope 与实际发现不匹配**
Title 声称 "Information Extraction" 但 batch-level confusability（Dimension 2）仅在 RE（FewRel, DocRED）上完整验证。NER 无 batch-level BCS-F1 correlation（§4.2: r ≈ 0），MAVEN ED 被 centrality confound（§4.5）。二维退化叙事仅 2/4 数据集成立。建议：缩窄 title 或在 Abstract 中明确 task-dependent boundaries。

**N2** [critical] **Novelty 定位不清晰**
SCS = cosine similarity of type-name embeddings, BCS = mean pairwise SCS——无技术创新。论文自承与 LLM-PEE 的 partitioning criterion 一致（§2）。"Controlled experimental framework" 作为主贡献需更充分论证其方法论创新性（相比 ablation study 的差异何在）。core finding "confusable types hurt performance" 在直觉上可预期。建议：强调 non-obvious findings（如22-58% variance explained），或补充 BCS 的实际应用案例。

### Should-Fix 问题

**W1** [warning] **无有效 mitigation——SDGD失败（§5），renaming降低准确率（Appendix W, Table 24: -8.8pp），few-shot扩大gap（Appendix U）。唯一建议是 "flag SCS > 0.85"，为监控非解决方案。**

**W2** [warning] **BCS 聚合方式（mean）未与 max/median/top-k 对比。degradation可能由batch内最confusable的single pair驱动。**

**W3** [warning] **SCS 仅基于 type name embeddings。v2 prompt包含definitions但Table 15分析仅在appendix，"definitions无帮助"本身是重要发现值得正文讨论。**

**W4** [warning] **页数限制潜在违规——Section 7 (Conclusion) 开始于第9页，正文技术上超8页。**

### Minor 问题
- M1: all-MiniLM-L6-v2 可能无法捕捉 LLM 内部 type similarity 表征
- M2: MAVEN trigger matches 评估指标与其他数据集不同
- M3: "first controlled study" 表述过绝对，建议 "among the first"
- M4: 4个bib条目未被OpenAlex匹配（工具局限但应确保信息正确）

### Questions
Q1. 为什么选 mean 而非 max 作 BCS 聚合？
Q2. NER 无 batch-level effect 但 RE 有——假设是什么？
Q3. Renaming 下降是否因丢失语义信息而非 confusability reduction 无效？
Q4. 是否考虑过 hierarchical clustering 等替代 decomposition？
Q5. Abstract 数字（85.7%, 49.5%, 88.0%, 38.7%）具体来源条件？

### Missing References
MR1. GLiREL (Boylan et al., NAACL 2025) — zero-shot RE via shared embedding space, 与SCS概念高度一致
MR2. Grasping the Essentials (Wan et al., 2024) — LLMs对relation definitions利用不充分，相关于Table 15
MR3. GLiNER-Relex / ASEE 等 schema matching + extraction 解耦工作，与SDGD动机相关

### 核心判断
执行质量很高的"问题刻画"论文，但 novelty（指标+发现）和 practical impact（无有效方案）不足以达到 EMNLP main。修正 title/scope overclaim 并加入 promising mitigation 可提升到 3.5（Borderline Conference）。

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

_source line 2356 · 2026-05-19T17:55:45.109486+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-0.7: 初始化完成', 'status': 'completed', 'activeForm': '初始化完成'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '独立审稿完成'}, {'content': 'Step 2: 交叉分享 — 转发审稿意见给对方 Reviewer', 'status': 'in_progress', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
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
    "todos": "[{'content': 'Step 0-0.7: 初始化完成', 'status': 'completed', 'activeForm': '初始化完成'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '独立审稿完成'}, {'content': 'Step 2: 交叉分享 — 转发审稿意见给对方 Reviewer', 'status': 'in_progress', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2357 · 2026-05-19T17:55:45.110060+00:00_

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

_source line 2358 · 2026-05-19T17:56:02.677051+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告：新颖性与完整性\n\n### 总体评分\n**Overall Assessment**: 3.0 — Findings（可被 Findings 接收）\n**一句话总结**: 方法论严谨的实证分析，准确刻画了 schema complexity 的两维度退化模式，但核心发现（confusable types hurt performance）的新颖性有限，标题声称覆盖 \"Information Extraction\" 而实际仅 RE 全面支持 batch-level confusability 效应，且未找到任何有效 mitigation，excitement 不足以达到主会议水平。\n\n### 官方维度打分（ACL ARR Review Form）\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4/5 | 实验设计严谨，统计方法规范（TOST/bootstrap CI/permutation），负面结果诚实报告 |\n| Excitement | 2.5/5 | 核心发现直觉上可预期；SCS/BCS 无技术新意（cosine sim + mean）；无有效 mitigation |\n| Reproducibility | 4/5 | 模型/数据集/prompt/超参数明确；18页appendix；代码承诺公开 |\n| Confidence | 4/5 | 全文26页（含appendix）仔细阅读，引用已核查 |\n\n### Strengths\nS1. 精心设计的控制实验框架（count curves + BCS-controlled batches），在 LLM IE 领域少见的严谨受控实验方法论\nS2. 诚实报告 null/负面结果（NER batch-level null, MAVEN centrality confound, SDGD全面失败）\nS3. 统计方法论规范（TOST equivalence tests, bootstrap CIs, permutation tests），显著优于领域平均水平\nS4. 多任务覆盖（NER/RE/DocRE/ED）+ 跨模型复现（Llama-3.1-8B/70B, Gemini 2.5 Flash）\nS5. Error taxonomy（§4.4 Figure 2）有独立价值\n\n### Must-Fix 问题\n\n**N1** [critical] **Title/Abstract scope 与实际发现不匹配**\nTitle 声称 \"Information Extraction\" 但 batch-level confusability（Dimension 2）仅在 RE（FewRel, DocRED）上完整验证。NER 无 batch-level BCS-F1 correlation（§4.2: r ≈ 0），MAVEN ED 被 centrality confound（§4.5）。二维退化叙事仅 2/4 数据集成立。建议：缩窄 title 或在 Abstract 中明确 task-dependent boundaries。\n\n**N2** [critical] **Novelty 定位不清晰**\nSCS = cosine similarity of type-name embeddings, BCS = mean pairwise SCS——无技术创新。论文自承与 LLM-PEE 的 partitioning criterion 一致（§2）。\"Controlled experimental framework\" 作为主贡献需更充分论证其方法论创新性（相比 ablation study 的差异何在）。core finding \"confusable types hurt performance\" 在直觉上可预期。建议：强调 non-obvious findings（如22-58% variance explained），或补充 BCS 的实际应用案例。\n\n### Should-Fix 问题\n\n**W1** [warning] 无有效 mitigation——SDGD失败（§5），renaming降低准确率（Appendix W, Table 24: -8.8pp），few-shot扩大gap（Appendix U）。唯一建议是 \"flag SCS > 0.85\"，为监控非解决方案。\n\n**W2** [warning] BCS 聚合方式（mean）未与 max/median/top-k 对比。degradation可能由batch内最confusable的single pair驱动。\n\n**W3** [warning] SCS 仅基于 type name embeddings。v2 prompt包含definitions但Table 15分析仅在appendix，\"definitions无帮助\"本身是重要发现值得正文讨论。\n\n**W4** [warning] 页数限制潜在违规——Section 7 (Conclusion) 开始于第9页，正文技术上超8页。\n\n### Minor 问题\n- M1: all-MiniLM-L6-v2 可能无法捕捉 LLM 内部 type similarity 表征\n- M2: MAVEN trigger matches 评估指标与其他数据集不同\n- M3: \"first controlled study\" 表述过绝对，建议 \"among the first\"\n- M4: 4个bib条目未被OpenAlex匹配（工具局限但应确保信息正确）\n\n### Questions\nQ1. 为什么选 mean 而非 max 作 BCS 聚合？\nQ2. NER 无 batch-level effect 但 RE 有——假设是什么？\nQ3. Renaming 下降是否因丢失语义信息而非 confusability reduction 无效？\nQ4. 是否考虑过 hierarchical clustering 等替代 decomposition？\nQ5. Abstract 数字（85.7%, 49.5%, 88.0%, 38.7%）具体来源条件？\n\n### Missing References\nMR1. GLiREL (Boylan et al., NAACL 2025) — zero-shot RE via shared embedding space, 与SCS概念高度一致\nMR2. Grasping the Essentials (Wan et al., 2024) — LLMs对relation definitions利用不充分，相关于Table 15\nMR3. GLiNER-Relex / ASEE 等 schema matching + extraction 解耦工作，与SDGD动机相关"
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
    "text": "以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告：新颖性与完整性\n\n### 总体评分\n**Overall Assessment**: 3.0 — Findings（可被 Findings 接收）\n**一句话总结**: 方法论严谨的实证分析，准确刻画了 schema complexity 的两维度退化模式，但核心发现（confusable types hurt performance）的新颖性有限，标题声称覆盖 \"Information Extraction\" 而实际仅 RE 全面支持 batch-level confusability 效应，且未找到任何有效 mitigation，excitement 不足以达到主会议水平。\n\n### 官方维度打分（ACL ARR Review Form）\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4/5 | 实验设计严谨，统计方法规范（TOST/bootstrap CI/permutation），负面结果诚实报告 |\n| Excitement | 2.5/5 | 核心发现直觉上可预期；SCS/BCS 无技术新意（cosine sim + mean）；无有效 mitigation |\n| Reproducibility | 4/5 | 模型/数据集/prompt/超参数明确；18页appendix；代码承诺公开 |\n| Confidence | 4/5 | 全文26页（含appendix）仔细阅读，引用已核查 |\n\n### Strengths\nS1. 精心设计的控制实验框架（count curves + BCS-controlled batches），在 LLM IE 领域少见的严谨受控实验方法论\nS2. 诚实报告 null/负面结果（NER batch-level null, MAVEN centrality confound, SDGD全面失败）\nS3. 统计方法论规范（TOST equivalence tests, bootstrap CIs, permutation tests），显著优于领域平均水平\nS4. 多任务覆盖（NER/RE/DocRE/ED）+ 跨模型复现（Llama-3.1-8B/70B, Gemini 2.5 Flash）\nS5. Error taxonomy（§4.4 Figure 2）有独立价值\n\n### Must-Fix 问题\n\n**N1** [critical] **Title/Abstract scope 与实际发现不匹配**\nTitle 声称 \"Information Extraction\" 但 batch-level confusability（Dimension 2）仅在 RE（FewRel, DocRED）上完整验证。NER 无 batch-level BCS-F1 correlation（§4.2: r ≈ 0），MAVEN ED 被 centrality confound（§4.5）。二维退化叙事仅 2/4 数据集成立。建议：缩窄 title 或在 Abstract 中明确 task-dependent boundaries。\n\n**N2** [critical] **Novelty 定位不清晰**\nSCS = cosine similarity of type-name embeddings, BCS = mean pairwise SCS——无技术创新。论文自承与 LLM-PEE 的 partitioning criterion 一致（§2）。\"Controlled experimental framework\" 作为主贡献需更充分论证其方法论创新性（相比 ablation study 的差异何在）。core finding \"confusable types hurt performance\" 在直觉上可预期。建议：强调 non-obvious findings（如22-58% variance explained），或补充 BCS 的实际应用案例。\n\n### Should-Fix 问题\n\n**W1** [warning] 无有效 mitigation——SDGD失败（§5），renaming降低准确率（Appendix W, Table 24: -8.8pp），few-shot扩大gap（Appendix U）。唯一建议是 \"flag SCS > 0.85\"，为监控非解决方案。\n\n**W2** [warning] BCS 聚合方式（mean）未与 max/median/top-k 对比。degradation可能由batch内最confusable的single pair驱动。\n\n**W3** [warning] SCS 仅基于 type name embeddings。v2 prompt包含definitions但Table 15分析仅在appendix，\"definitions无帮助\"本身是重要发现值得正文讨论。\n\n**W4** [warning] 页数限制潜在违规——Section 7 (Conclusion) 开始于第9页，正文技术上超8页。\n\n### Minor 问题\n- M1: all-MiniLM-L6-v2 可能无法捕捉 LLM 内部 type similarity 表征\n- M2: MAVEN trigger matches 评估指标与其他数据集不同\n- M3: \"first controlled study\" 表述过绝对，建议 \"among the first\"\n- M4: 4个bib条目未被OpenAlex匹配（工具局限但应确保信息正确）\n\n### Questions\nQ1. 为什么选 mean 而非 max 作 BCS 聚合？\nQ2. NER 无 batch-level effect 但 RE 有——假设是什么？\nQ3. Renaming 下降是否因丢失语义信息而非 confusability reduction 无效？\nQ4. 是否考虑过 hierarchical clustering 等替代 decomposition？\nQ5. Abstract 数字（85.7%, 49.5%, 88.0%, 38.7%）具体来源条件？\n\n### Missing References\nMR1. GLiREL (Boylan et al., NAACL 2025) — zero-shot RE via shared embedding space, 与SCS概念高度一致\nMR2. Grasping the Essentials (Wan et al., 2024) — LLMs对relation definitions利用不充分，相关于Table 15\nMR3. GLiNER-Relex / ASEE 等 schema matching + extraction 解耦工作，与SDGD动机相关"
  }
}
```

</details>

---


### Tool result

_source line 2359 · 2026-05-19T17:56:42.022031+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 39344
}
```

</details>

---


### Tool call

_source line 2360 · 2026-05-19T17:56:42.374249+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告：方法严谨性审查\n\n### 总体评分\n**Overall**: 3.5 / 5 — Borderline Conference\n**一句话总结**: 本文提出了一个重要且未被充分研究的问题，实验设计用心、附录详尽，但单种子设计导致置信区间低估不确定性、TOST 等价性 margin 选择存在循环论证倾向、部分结论超出证据支撑力度，这些方法论问题需要修复后才能给出可靠的量化结论。\n\n### 官方维度打分（ACL Rolling Review form）\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心实验设计互补且合理，附录大量鲁棒性检验。但单种子+FP8噪声使CI偏窄；TOST margin选择有循环性；部分ablation样本量不足却得出过强结论。 |\n| Excitement | 3.5/5 | 首次系统研究schema complexity对zero-shot LLM IE的影响，SCS/BCS度量体系有新意。但pair-level效应量极小（r²~1-3%），实际可操作建议有限。 |\n| Overall Assessment | 3.5/5 | Borderline Conference。修复N1/N2后可达Conference水平。 |\n| Confidence | 4/5 | 仔细阅读全文26页含17个Appendix。 |\n| Reproducibility | 3.5/5 | 实验设置描述详细，代码承诺release。但单种子+FP8量化使精确复现有难度。 |\n\n### Must-Fix 问题\n\n**N1** [critical] 单种子设计 + FP8非确定性噪声导致CI系统性偏窄\n- 全部bootstrap CI仅捕获batch composition variance，未纳入模型级方差。0.88pp噪声占TOST ±3pp margin的~30%。BCS-controlled实验仅用27个batch且无种子变异→CI不含模型级不确定性。\n- 建议：补充3-5个种子实验，或将FP8噪声传播进bootstrap产生保守CI。\n\n**N2** [critical] TOST等价性margin（±3pp）选择存在循环论证倾向\n- ±3pp的首要理由是\"approximates the typical BCS-predicted accuracy gap\"——用BCS自身预测力校准阈值。灵敏度分析显示±2pp时FewRel仅勉强通过（p=0.047），DocRED inconclusive。\n- 建议：将Cohen's δ作为首要理由；在正文报告±2pp结果；提供外部基准anchor。\n\n### Should-Fix 问题\n\n**W1** [warning] Pair-to-batch R²放大（1.7%→22-58%）理论解释不够solid\n- Simulation假设pair-level效应独立（但同batch types共享prompt上下文）。\n- 建议：补充非独立性讨论；参考ecological inference文献。\n\n**W2** [warning] DocRED factorial range-matching消除interaction但未做power analysis\n- Range-matched: 0.93pp (CI [-7.13, 7.44])，CI跨零但宽度~14pp→power严重不足。Non-significance ≠ absence of effect。\n- 建议：报告range-matched子集n和post-hoc power。\n\n**W3** [warning] Dimension 2 cross-model验证不足但claim过宽\n- BCS-controlled仅在Llama-3.1-8B验证，NER上8B模型floor effects。Abstract/Intro措辞未区分两个维度的验证范围。\n\n**W4** [warning] 因果语言超出相关性证据\n- Title \"Predict\"、§5 \"degradation due to\"、renaming experiment的familiarity confound。\n\n**W5** [warning] Unconstrained decoding ablation结论过强\n- n=25，未做Fisher z-test比较ρ差异。Non-significance at n=25 ≠ absence of correlation。\n\n**W6** [warning] Few-shot实验confounding控制不足\n- 高BCS batch中随机few-shot examples可能对高混淆types区分度更低。\n\n### Minor Issues\n- M1: Rothman (1990) 作为不做多重比较校正的唯一理由不足。\n- M2: Logit-scale TOST inconclusive但被低估。\n- M3: Appendix M中EF=3.35如从observed R²反推则为同义反复。\n- M4: MAVEN同质schema限制其对general confusability claim的支撑力。\n\n### 主要优势\nS1. 研究问题重要且填补明确空白\nS2. Count-curve + BCS-controlled两种范式互补设计精巧\nS3. 17个Appendix的深度和透明度罕见\nS4. 四数据集跨三任务的cross-dataset一致性\nS5. 负面结果的诚实报告\nS6. Prompt sensitivity验证增强核心finding credibility\n\n### Questions to Authors\n1. 能否提供至少3个种子的BCS-controlled实验结果以回应N1？\n2. TOST ±3pp margin是否有external benchmark？\n3. DocRED显著交互（−9.4pp）与FewRel TOST通过之间的张力如何调和？\n4. Appendix M中EF=3.35是independent estimate还是从observed R²反推？"
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
    "text": "以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个观点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 审稿报告：方法严谨性审查\n\n### 总体评分\n**Overall**: 3.5 / 5 — Borderline Conference\n**一句话总结**: 本文提出了一个重要且未被充分研究的问题，实验设计用心、附录详尽，但单种子设计导致置信区间低估不确定性、TOST 等价性 margin 选择存在循环论证倾向、部分结论超出证据支撑力度，这些方法论问题需要修复后才能给出可靠的量化结论。\n\n### 官方维度打分（ACL Rolling Review form）\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心实验设计互补且合理，附录大量鲁棒性检验。但单种子+FP8噪声使CI偏窄；TOST margin选择有循环性；部分ablation样本量不足却得出过强结论。 |\n| Excitement | 3.5/5 | 首次系统研究schema complexity对zero-shot LLM IE的影响，SCS/BCS度量体系有新意。但pair-level效应量极小（r²~1-3%），实际可操作建议有限。 |\n| Overall Assessment | 3.5/5 | Borderline Conference。修复N1/N2后可达Conference水平。 |\n| Confidence | 4/5 | 仔细阅读全文26页含17个Appendix。 |\n| Reproducibility | 3.5/5 | 实验设置描述详细，代码承诺release。但单种子+FP8量化使精确复现有难度。 |\n\n### Must-Fix 问题\n\n**N1** [critical] 单种子设计 + FP8非确定性噪声导致CI系统性偏窄\n- 全部bootstrap CI仅捕获batch composition variance，未纳入模型级方差。0.88pp噪声占TOST ±3pp margin的~30%。BCS-controlled实验仅用27个batch且无种子变异→CI不含模型级不确定性。\n- 建议：补充3-5个种子实验，或将FP8噪声传播进bootstrap产生保守CI。\n\n**N2** [critical] TOST等价性margin（±3pp）选择存在循环论证倾向\n- ±3pp的首要理由是\"approximates the typical BCS-predicted accuracy gap\"——用BCS自身预测力校准阈值。灵敏度分析显示±2pp时FewRel仅勉强通过（p=0.047），DocRED inconclusive。\n- 建议：将Cohen's δ作为首要理由；在正文报告±2pp结果；提供外部基准anchor。\n\n### Should-Fix 问题\n\n**W1** [warning] Pair-to-batch R²放大（1.7%→22-58%）理论解释不够solid\n- Simulation假设pair-level效应独立（但同batch types共享prompt上下文）。\n- 建议：补充非独立性讨论；参考ecological inference文献。\n\n**W2** [warning] DocRED factorial range-matching消除interaction但未做power analysis\n- Range-matched: 0.93pp (CI [-7.13, 7.44])，CI跨零但宽度~14pp→power严重不足。Non-significance ≠ absence of effect。\n- 建议：报告range-matched子集n和post-hoc power。\n\n**W3** [warning] Dimension 2 cross-model验证不足但claim过宽\n- BCS-controlled仅在Llama-3.1-8B验证，NER上8B模型floor effects。Abstract/Intro措辞未区分两个维度的验证范围。\n\n**W4** [warning] 因果语言超出相关性证据\n- Title \"Predict\"、§5 \"degradation due to\"、renaming experiment的familiarity confound。\n\n**W5** [warning] Unconstrained decoding ablation结论过强\n- n=25，未做Fisher z-test比较ρ差异。Non-significance at n=25 ≠ absence of correlation。\n\n**W6** [warning] Few-shot实验confounding控制不足\n- 高BCS batch中随机few-shot examples可能对高混淆types区分度更低。\n\n### Minor Issues\n- M1: Rothman (1990) 作为不做多重比较校正的唯一理由不足。\n- M2: Logit-scale TOST inconclusive但被低估。\n- M3: Appendix M中EF=3.35如从observed R²反推则为同义反复。\n- M4: MAVEN同质schema限制其对general confusability claim的支撑力。\n\n### 主要优势\nS1. 研究问题重要且填补明确空白\nS2. Count-curve + BCS-controlled两种范式互补设计精巧\nS3. 17个Appendix的深度和透明度罕见\nS4. 四数据集跨三任务的cross-dataset一致性\nS5. 负面结果的诚实报告\nS6. Prompt sensitivity验证增强核心finding credibility\n\n### Questions to Authors\n1. 能否提供至少3个种子的BCS-controlled实验结果以回应N1？\n2. TOST ±3pp margin是否有external benchmark？\n3. DocRED显著交互（−9.4pp）与FewRel TOST通过之间的张力如何调和？\n4. Appendix M中EF=3.35是independent estimate还是从observed R²反推？"
  }
}
```

</details>

---


### Tool result

_source line 2361 · 2026-05-19T17:56:43.787081+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1412
}
```

</details>

---


### Assistant

_source line 2362 · 2026-05-19T17:56:47.883020+00:00_

交叉分享已派发。两位 Reviewer 各收到对方完整审稿原文，正在逐条回应（[AGREE]/[REBUT]）。等待交叉回应返回后进入 Step 3 收敛判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 198

## Round 198

2 recorded events


### User

_source line 2363 · 2026-05-19T17:56:50.474183+00:00_

[Reviewer 2 审稿结果]:
审稿报告已完成并提交给 Review Director。

**核心结论**: Overall 3.0（Findings），Soundness 4/5，Excitement 2.5/5。

两个 critical 问题：
1. Title/Abstract 声称 "Information Extraction" 但 batch-level confusability 仅在 RE 上成立（2/4 数据集）
2. SCS/BCS 无技术新意，"controlled framework" 作为主贡献的 novelty 论证不充分

四个 should-fix：无有效 mitigation、BCS 聚合未对比 alternatives、type definitions 分析应提升至正文、页数限制潜在违规。

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

_source line 2364 · 2026-05-19T17:56:55.801663+00:00_

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


## Round 199

## Round 199

2 recorded events


### User

_source line 2365 · 2026-05-19T18:01:01.989401+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Strengths

**[AGREE] S1-S5**: R2 对论文优势的识别准确。特别是 S1（受控实验框架）和 S3（统计方法论）——在 LLM IE 领域确实少见。S2（诚实报告负面结果）也值得肯定。

---

### Must-Fix 问题

**[REBUT] R2-N1: Title/Abstract scope 与实际发现不匹配**

R2 称 batch-level confusability "仅在 RE 上完整验证"，过度简化了论文的发现结构。需区分两个层次：

1. **Type-pair 级别的 SCS-confusion 相关性**（Dimension 2 的核心）在所有任务上均成立：Few-NERD (r=0.069, p<0.001)、FewRel (r=0.187, p<0.001)、MAVEN (r=0.081, p<0.185 但受 centrality confound)——见 Table 2, §4.2。
2. **Batch-level BCS→F1 聚合**仅在 RE forced-choice 格式下显著——论文在 §4.2 和 Limitations #3 中已明确承认。

Title 用 "Schema Complexity" 涵盖 count（Dimension 1，全4任务成立）和 type confusability（SCS，跨任务成立）。NER batch-level 无效是 aggregation 局限，非 confusability 维度本身失败。

**但部分同意**：Abstract 中 BCS 叙述确实容易误导，建议加 task-format qualifier。是 framing 问题而非 scope 问题。

---

**[REBUT] R2-N2: Novelty 定位不清晰**

R2 误解了贡献类型。这是 controlled empirical study，核心创新在于：
1. count curves + BCS-controlled batches 实验范式是新的（§3.3-3.4），与 ablation 的区别在于操纵的是 schema 属性而非模型/方法
2. 22-58% variance explained（§4.3）、extreme-batch gap 25-31pp（§6）等定量发现无法靠直觉预测
3. Renaming 降低准确率（Table 24）直接反驳了朴素假设
4. NER batch-level null result 是反直觉的

R2 给 Excitement 2.5/5 过低，建议至少 3/5。

---

### Should-Fix 问题

**[AGREE] R2-W1: 无有效 mitigation** — 同意这是论文最显著弱点。但补充：SDGD 失败揭示了 decomposition 范式的结构性困难（merge amplification + routing failure），负面结果本身约束了未来解决方案空间，有独立价值。建议 Discussion 中更深入分析失败原因。

**[REBUT] R2-W2: BCS 聚合未与 max/median 对比** — R2 遗漏了 **Appendix I, Table 12**（p.20），论文已比较 mean vs. max pairwise SCS，两种定义均显著，max 稍强但 permutation test 无显著差异。

**[AGREE] R2-W3: Definitions 分析值得正文讨论** — Table 15 "definitions 无帮助"是重要发现，目前仅在 Appendix L，应在 §6 practical implications 增加总结。

**[AGREE] R2-W4: 页数违规** — 已验证 PDF：Section 7 (Conclusion) 起始于第9页，属主体正文，违反 EMNLP 2026 的8页限制。必须修复。

---

### Minor 问题

**[AGREE] M1-M4**: 均为合理的小建议。M1（嵌入模型局限）被双嵌入策略部分缓解但不完全消除；M3 ("first" → "among the first") 更谨慎。

---

### Questions 回应要点

- **Q1**: Appendix I Table 12 已回答 mean vs max 对比。R2 似乎未阅读此部分。
- **Q2**: §4.2 和 Appendix H 解释了 NER exact match 评估将 boundary/type error 混合，稀释了 batch-level SCS 信号。
- **Q3**: 精彩问题。Table 24 交互效应（Δ_high - Δ_low = -5.9pp, p<0.001）支持语义信息丢失解读。§6 末尾 "SCS as proxy for conceptual similarity" 讨论了此点。
- **Q5**: Abstract 数字可追溯至 Figure 1/§4.1，但建议标注具体 dataset 和 condition。

---

### Missing References

**[AGREE] MR1-MR3**: 三篇均与论文相关，值得引用——GLiREL 与 SCS 概念呼应，Wan et al. 支持 Table 15 发现，schema matching 解耦工作与 SDGD 动机相关。

---

### 对 R2 总体评分

R2 给 Overall 3.0 (Findings)，我认为**基本合理但略偏保守**。N1 是 framing 问题可快速修复，N2 低估了方法论创新。真正制约评分的是 W1（无 mitigation）和 W4（页数违规）。

**我的评估：Overall 3.0-3.5，倾向 3.0 (Findings)**。修复页数、深化 mitigation 失败分析、提入 definitions 发现后，可能达到 3.5。

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

_source line 2366 · 2026-05-19T18:01:21.259341+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 的交叉回应。

**R1 交叉回应要点：**
- **R2-N1 (Title scope)**: [REBUT] pairwise SCS 跨任务成立，batch-level 是聚合局限非维度失败；但部分同意 Abstract 需加 qualifier
- **R2-N2 (Novelty)**: [REBUT] 方法论创新在实验范式而非指标；R2 给 Excitement 2.5 过低
- **R2-W1 (无 mitigation)**: [AGREE] 论文最显著弱点
- **R2-W2 (BCS 聚合)**: [REBUT] Appendix I Table 12 已对比 mean vs max
- **R2-W3 (Definitions)**: [AGREE] 应提升至正文
- **R2-W4 (页数违规)**: [AGREE] 确认违规，必须修复
- **R1 修正后评分**：Overall 3.0-3.5，倾向 3.0 (Findings)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 200

## Round 200

2 recorded events


### User

_source line 2367 · 2026-05-19T18:01:25.429114+00:00_

[Reviewer 1 审稿结果]:
已完成对 Reviewer 2 全部意见的逐条回应，并通过 `review_reviewer_post_to_director` 提交给 Review Director。

核心判断摘要：

- **N1 (scope mismatch)**: [REBUT] — R2 混淆了 type-pair 级 SCS 相关性（跨任务成立）与 batch-level BCS 聚合（仅 RE），但同意 Abstract framing 需加 qualifier
- **N2 (novelty)**: [REBUT] — 贡献是受控实验方法论+定量发现，非新指标；Excitement 2.5 偏低
- **W1 (无 mitigation)**: [AGREE] — 论文最实质弱点，但负面结果有独立价值
- **W2 (mean vs max BCS)**: [REBUT] — Appendix I Table 12 已做对比，R2 遗漏
- **W3 (definitions 分析)**: [AGREE] — 值得提入正文
- **W4 (页数违规)**: [AGREE] — Section 7 起始于第9页，确认违规
- **M1-M4, MR1-MR3**: 全部 [AGREE]
- **总体评分共识**: 倾向 3.0 (Findings)，与 R2 一致

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

_source line 2368 · 2026-05-19T18:01:30.514165+00:00_

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


## Round 201

## Round 201

16 recorded events


### User

_source line 2369 · 2026-05-19T18:02:32.408790+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### 总体评分意见

R1 给出 3.5 (Borderline Conference)，我基本认同这个区间（我倾向 3.5–4.0）。核心判断"方法论有可修复问题，修复后可达 Conference 水平"是合理的，但我认为 R1 对部分问题的严重性有高估。

---

### Must-Fix 问题回应

**[REBUT] R1-N1: 单种子 + FP8 噪声导致 CI 系统性偏窄**

R1 的核心论点是 bootstrap CI 仅捕获 batch composition variance，遗漏了 model-level variance，并声称 0.88pp 噪声占 TOST ±3pp margin 的 ~30%，因此 CI "系统性偏窄"。

我认为该问题被高估，理由如下：

1. **Greedy decoding 下 seed variance ≈ FP8 noise**。论文使用 temperature=0 的贪心解码（§3.5），此时模型行为是确定性的，唯一的随机性来源就是 FP8 量化噪声。R1 建议跑 3-5 个种子，但在 greedy decoding 下，不同种子的输出差异本质上就是 FP8 噪声——论文已经量化了这一噪声（residual SD = 0.88pp）。多种子实验会重复测量同一个噪声源，不会带来新的方差分量。

2. **0.88pp 噪声的 framing 有误导性**。R1 称"0.88pp 占 ±3pp 的 30%"，但这是将噪声的标准差与 TOST margin 做除法，统计上不对等。TOST 检验的 p 值已经通过 bootstrap 分布的宽度纳入了这一噪声。真正的问题是 0.88pp 噪声是否会导致 TOST 的 rejection 不可靠——从灵敏度分析看（Table 8, Appendix C），即使在 ±2pp margin 下 FewRel 仍通过（p=0.047），说明结论对噪声有一定鲁棒性。

3. **BCS-controlled 的 27 batch 实验**。R1 说"无种子变异→CI 不含模型级不确定性"。但该实验的设计目的是测量 BCS 对 batch 间准确率的预测力（R²=22-58%），CI 捕获的是 batch 间 accuracy 的 sampling variance，这是该设计的目标方差分量。FP8 噪声在每个 batch 内独立实现，bootstrap 重采样已隐式纳入。

4. **跨模型验证提供了间接种子鲁棒性**。Appendix S（LLaMA-3.1-70B-Instruct, FP8）和 Appendix T（Gemini 2.5 Flash, API）在不同模型/架构/量化设置下复现了 Dimension 1 的方向性一致结果（Table 18: RE 斜率近乎一致 ~-30.7pp vs. -31pp）。不同模型间的一致性远比同模型多种子更能说明结论的鲁棒性。

**我的判断**：这是一个 should-fix 而非 must-fix。建议作者在 Limitations 中更明确讨论 FP8 噪声传播对 CI 宽度的影响，并考虑用 R1 建议的"将 FP8 噪声传播进 bootstrap"方法提供保守 CI 作为补充。但不应要求多种子实验——在 greedy decoding 下这不会增加实质性信息。

---

**[AGREE] R1-N2: TOST ±3pp margin 选择存在循环论证倾向**（部分同意）

R1 指出 ±3pp 的首要理由是"approximates the typical BCS-predicted accuracy gap"，这确实构成一定程度的循环性——用 BCS 的预测力来校准检验 BCS 效应是否可忽略的阈值。

但我认为 R1 对循环性程度有夸大：

1. 论文实际提供了**多个独立锚点**：(a) BCS-predicted gap（R1 关注的循环部分）；(b) Cohen's δ 等价（§4.3 提到 0.3 SD）；(c) 实践显著性（3pp 准确率差异在 IE 应用中是否有实际影响）。(b)(c) 是独立于 BCS 的。

2. **灵敏度分析是透明的**。Table 8 报告了 ±1/±2/±3/±5 四个 margin 的完整结果。读者可以自行判断在哪个 margin 下等价性成立。这种透明度部分弥补了 margin 选择的主观性。

3. 但 R1 说得对的是：**±2pp 下 FewRel 仅勉强通过（p=0.047），DocRED inconclusive**。这意味着等价性结论对 margin 选择敏感，论文应在正文（而非仅 Appendix C）更突出地讨论这一敏感性。

**建议**：同意 R1 的修改方向——将 Cohen's δ 作为首要理由，在正文报告 ±2pp 结果。但不需要外部基准 anchor（学科内缺乏统一的"可忽略效应"标准）。

---

### Should-Fix 问题回应

**[AGREE] R1-W1: Pair-to-batch R² 放大理论解释的独立性假设**

R1 指出 Appendix M 的模拟假设 pair-level 效应独立，但同 batch 内的 types 共享 prompt context，可能引入相关性。这是一个合理的统计关切。

不过我要补充：**核心发现不依赖模拟**。BCS-accuracy 的 batch-level 相关性（R²=22-58%）是直接观测到的（Table 2, §4.3），不是从 pair-level 模拟推导的。模拟只是提供了一个解释机制（为什么小的 pair-level 效应能产生大的 batch-level 效应）。即使模拟的独立性假设有问题，empirical finding 本身不受影响。

**建议**：在 Appendix M 中加入非独立性讨论，说明 prompt context 共享可能使实际放大倍数与模拟偏离，并引用 ecological inference 文献。

---

**[AGREE] R1-W2: DocRED range-matching 的 power 不足**

同意。Range-matched 结果 CI [-7.13, 7.44] 宽度 ~14pp，power 严重不足。论文应报告 range-matched 子集的 n 和 post-hoc power。

但我要指出：**这一结果的解释方向是对的**。Range-matching 的目的是检验移除 BCS 范围差异后交互效应是否消失。宽 CI 说明证据不足以下结论（无论是有交互还是无交互），论文应明确说"insufficient power to detect"，而非暗示交互效应被消除。

---

**[AGREE] R1-W3: Dimension 2 跨模型验证不足但 claim 过宽**（同意，但补充重要 nuance）

同意 BCS-controlled 实验（Dimension 2）仅在 Qwen3-32B 上验证，NER 在 8B 模型上有 floor effects。论文 Limitations §7 第3点已承认："Dimension 2 (BCS) has not been verified on proprietary models at the batch level."

但我认为 R1 遗漏了一个支撑性证据：**Table 15（Appendix K）** 显示 SCS-confusion Spearman ρ 在 Few-NERD 上跨 embedding 模型（MiniLM、Qwen3）和跨控制条件一致显著。这虽然是 pair-level 而非 batch-level 验证，但表明 confusability 的预测力不限于单一模型。

**建议**：Abstract/Intro 区分两个维度的验证范围：Dimension 1（count）有跨模型支持，Dimension 2（BCS）仅在主模型验证。

---

**[REBUT] R1-W4: 因果语言超出相关性证据**（部分反驳）

1. **Title "Predict"**：这是标准的统计用语（"X predicts Y" = X 是 Y 的统计预测因子），不暗示因果关系。学术写作中 "predict" 常用于回归/相关分析语境，不需要修改。

2. **§5 "degradation due to"**：BCS-controlled 实验是准实验设计（固定 count，操纵 BCS），比纯相关分析有更强的因果推断力。该实验通过 balanced design（700 instances per type, 匹配 count）控制了主要混淆变量。使用 "due to" 在准实验语境下是可接受的，但可以加一个 qualifier（如 "largely attributable to"）以示谨慎。

3. **Renaming experiment 的 familiarity confound**（Appendix W）：R1 的关切有道理——改名确实同时改变了 embedding similarity 和 label familiarity。但 Table 24 显示 high-BCS batch 的下降幅度（-8.8pp）远大于 low-BCS（-3.0pp），交互效应显著（t=-7.23, p<0.001）。如果仅是 familiarity confound，两组应下降相近。差异化效应支持 confusability 是驱动因素，尽管不能完全排除 familiarity。

**建议**：§5 中 "due to" 加 hedge（"largely attributable to"）；在 Appendix W 中明确讨论 familiarity confound 并解释为何交互效应支持 confusability 解释。但 Title 不需要修改。

---

**[AGREE] R1-W5: Unconstrained decoding ablation 结论过强**

同意。n=25 样本量下 non-significance（p=0.200）不能等同于 absence of correlation。Fisher z-test 在 n=25 时 power 很低。

具体看论文描述：Appendix L（§L）中称 unconstrained decoding "eliminates the BCS-accuracy correlation"，这个措辞确实过强。应改为"insufficient evidence to detect a significant BCS-accuracy correlation at n=25"并报告检测中等效应（如 r=0.4）所需的最小样本量。

---

**[REBUT] R1-W6: Few-shot 实验 confounding 控制不足**（部分反驳）

R1 的担忧是：高 BCS batch 中随机 few-shot examples 对高混淆 types 的区分度更低。这在理论上成立，但 Appendix U 的实证结果不支持这一担忧：

1. **0-shot 到 5-shot 的 BCS gap 没有缩小**：论文报告 0-shot extreme-batch BCS gap 为 +18.5pp，而加入 few-shot 后 BCS-associated 效应持续存在（Table 20 显示 low-BCS 组准确率从 ~90% 到 high-BCS 组 ~60%，5-shot 不改变方向）。如果 R1 假设的 confound 是主要驱动因素（即高 BCS batch 的 few-shot examples 区分度低），我们应该看到 few-shot 加剧 BCS gap——但实际上 gap 变化很小。

2. **Few-shot 的控制方式合理**：examples 从 FewRel 训练集按 target type 采样，每个 condition 使用相同的 BCS-controlled batch 设计（§U, 50 batches per condition）。

**建议**：可以在 Appendix U 中加一句 disclaimer 说明 few-shot example quality 可能与 BCS 相关的理论可能性，但现有数据不支持这是一个实际问题。

---

### Minor Issues 回应

**[AGREE] R1-M1: Rothman (1990) 作为不做多重比较校正的唯一理由不足**

同意这个引用过于单薄。但论文 Limitations §7 实际还引用了 Dror et al. (2018) 和 Cael et al. (2020)，并说明"within-study secondary analyses involve correlated observations rather than independent tests"。这个论证框架合理，但应在方法部分更早说明，而非仅在 Limitations 中提及。

**[AGREE] R1-M2: Logit-scale TOST inconclusive 被低估**

同意。线性尺度 TOST 通过（p=0.003）而 logit 尺度 TOST 不通过（p=0.200），这一分歧应在正文讨论。logit 变换在比例数据分析中通常更合适（方差稳定化），因此 logit 尺度结果 inconclusive 削弱了等价性结论的可靠性。这是一个比 R1 标记的 "minor" 更严重的问题，我认为应提升为 should-fix。

**[AGREE] R1-M3: Appendix M 中 EF=3.35 的独立性**

同意需要澄清。从论文描述看，EF=3.35 似乎是从 observed R² 反推的（"confirms: SNR × EF/(SNR × EF + 1) = 0.042"），如果是这样则确实是同义反复。作者应说明 EF 是独立估计的（如从 batch 内有效自由度直接计算）还是从 R² 反推的，两种情况的解释力完全不同。

**[AGREE] R1-M4: MAVEN 同质 schema 限制**

同意。MAVEN 168 types 全来自 FrameNet 单一本体，§4.5 报告 BCS-F1 correlation 异常正相关（r=+0.184），论文已注意到这一 anomaly 并归因于 centrality confound。但应更明确指出 MAVEN 对 general confusability claim 的支撑力有限。

---

### 对 R1 主要优势评价的回应

全部同意（S1-S6）。特别补充：

**S2（双范式互补设计）我认为是本文最核心的方法论贡献**。Count-curve 建立现象学事实（更多 types → 更低准确率），BCS-controlled 隔离因果机制（confusability 独立于 count 影响准确率）。这种设计在 LLM IE 分析性研究中很少见。

**S5（负面结果的诚实报告）**值得额外肯定。§5 的 SGDG 分解实验全面失败（NER merge amplification, RE routing failure, ED 无改善），论文没有回避这些结果，反而将其作为重要发现讨论。这种透明度在投稿论文中不常见。

---

### 对 R1 Questions to Authors 的回应

**Q1（多种子实验）**：如上述 N1 反驳，greedy decoding 下多种子主要重复测量 FP8 噪声。更有价值的补充是报告 FP8 噪声传播后的保守 CI。

**Q2（TOST external benchmark）**：同意需要更好的 anchoring，但外部基准在 IE 领域确实缺乏。Cohen's δ 是最实际的替代锚点。

**Q3（DocRED 交互 vs. FewRel TOST 的张力）**：这是一个真正的 tension。论文在 Appendix C 通过 range-matching 尝试调和，但 power 不足（如 W2 所述）。我认为这个 tension 目前无法完全解决，论文应更坦诚地承认。

**Q4（EF=3.35 来源）**：如 M3 所述，需要作者澄清。

---

### Reviewer 2 总结性意见

R1 的审稿整体质量高，对方法论问题的识别准确。但我有以下分歧：

1. **N1 应从 must-fix 降级为 should-fix**。在 greedy decoding 下，单种子的影响远小于 R1 的描述。真正需要的是 FP8 噪声传播分析，而非多种子实验。

2. **N2 的循环性被部分夸大**。论文提供了多个独立锚点，灵敏度分析透明。真正的问题是正文对 ±2pp 结果的讨论不够充分。

3. **W4 的因果语言问题**。Title "Predict" 不需要修改；BCS-controlled 设计支持准因果推断；但 §5 的 "due to" 和 renaming 的 familiarity confound 需要 hedge。

4. **M2 应从 minor 提升为 should-fix**。logit-scale TOST inconclusive 对等价性结论有实质影响。

我的 Overall Assessment 倾向 **3.5（Borderline Conference）**，与 R1 一致。如果 N2 和 M2（logit-scale TOST）得到妥善处理，可提升至 4.0。

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

_source line 2370 · 2026-05-19T18:03:16.010502+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-1: 初始化+独立审稿完成', 'status': 'completed', 'activeForm': '初始化+独立审稿完成'}, {'content': 'Step 2: 交叉分享完成', 'status': 'completed', 'activeForm': '交叉分享完成'}, {'content': 'Step 3: 收敛判断', 'status': 'in_progress', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
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
    "todos": "[{'content': 'Step 0-1: 初始化+独立审稿完成', 'status': 'completed', 'activeForm': '初始化+独立审稿完成'}, {'content': 'Step 2: 交叉分享完成', 'status': 'completed', 'activeForm': '交叉分享完成'}, {'content': 'Step 3: 收敛判断', 'status': 'in_progress', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2371 · 2026-05-19T18:03:16.061253+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2372 · 2026-05-19T18:03:29.375587+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-2: 初始化+审稿+交叉完成', 'status': 'completed', 'activeForm': '初始化+审稿+交叉完成'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '收敛判断完成'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'in_progress', 'activeForm': '汇总审稿报告并投递'}]"
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
    "todos": "[{'content': 'Step 0-2: 初始化+审稿+交叉完成', 'status': 'completed', 'activeForm': '初始化+审稿+交叉完成'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '收敛判断完成'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'in_progress', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2373 · 2026-05-19T18:03:29.376221+00:00_

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

_source line 2374 · 2026-05-19T18:03:33.447314+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

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
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 2375 · 2026-05-19T18:03:33.750702+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"timeout\", \"elapsed_seconds\": 1068}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 2376 · 2026-05-19T18:03:33.751146+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

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
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 2377 · 2026-05-19T18:03:33.851788+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2378 · 2026-05-19T18:05:34.750153+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "schema-dag-extraction",
  "issues_yaml": "# Review Issues Tracker\n# Updated: 2026-05-19 (Round 22 fresh review)\n\n# ============================================================\n# R22 CRITICAL\n# ============================================================\n\n- id: R22-C1\n  summary: \"Title/Abstract scope overclaim: 'Information Extraction' 但 batch-level Dim2 仅 RE 成立\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 22\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R21-W1: NER Dim2 batch-level null, Title IE 过宽\"}\n    - {round: 22, reviewers: [R2], note: \"R2 Must-Fix N1。batch-level BCS 仅 RE (FewRel/DocRED) 成立，NER r≈0，MAVEN centrality confound。R1 部分 rebut：pairwise SCS 跨任务成立，batch-level 是聚合局限。交叉后共识：Abstract 需加 task-format qualifier。\"}\n  action_items:\n    - {round: 22, action: \"Abstract 加 task-dependent qualifier，区分 pairwise (跨任务) vs batch-level (RE only)\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R22-C2\n  summary: \"SCS/BCS novelty 不足，与 LLM-PEE partitioning criterion 一致\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 22\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R21-C4: SCS 借自 LLM-PEE，novelty framing 不清晰\"}\n    - {round: 22, reviewers: [R2], note: \"R2 Must-Fix N2。SCS=cosine sim, BCS=mean，无技术创新。'controlled framework' 作主贡献论证不充分。R1 rebut：方法论创新在实验范式非指标，22-58% R² 无法靠直觉预测。交叉后分歧保留。\"}\n  action_items:\n    - {round: 22, action: \"强化 non-obvious findings (22-58% R², renaming 反直觉, NER null)，或补 BCS 实际应用案例\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R22-C3\n  summary: \"TOST ±3pp margin 循环论证 + logit-scale inconclusive\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 22\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R21-C1: margin 来自 BCS 自身预测力\"}\n    - {round: 22, reviewers: [R1, R2], note: \"R1 Must-Fix N2。±3pp 首要理由是 BCS-predicted gap→循环。±2pp FewRel p=0.047 勉强，DocRED inconclusive。R2 部分同意：多个独立锚点存在但正文未充分展示。R2 额外提升 logit-scale TOST inconclusive 至 should-fix。交叉后共识：Cohen's δ 作首要理由，±2pp 入正文，logit 分歧需讨论。\"}\n  action_items:\n    - {round: 22, action: \"正文重构 margin justification：Cohen's δ 为首要锚点，报告 ±2pp 结果，讨论 logit-scale 分歧\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R22-C4\n  summary: \"页数违规：Section 7 (Conclusion) 起始于第9页，超 EMNLP 8页限制\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - {round: 22, reviewers: [R1, R2], note: \"R2 Should-Fix W4，R1 交叉 AGREE 确认违规。双方共识必须修复。\"}\n  action_items:\n    - {round: 22, action: \"压缩正文至8页内（Conclusion 必须在第8页结束前）\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R22 WARNING\n# ============================================================\n\n- id: R22-W1\n  summary: \"无有效 mitigation：SDGD/renaming/few-shot 全部失败\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 22\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R21-W4/C5: 无有效干预，typical ~2pp\"}\n    - {round: 22, reviewers: [R1, R2], note: \"R2 Should-Fix W1，R1 交叉 AGREE。论文最显著弱点。R1 补充：负面结果有独立价值。双方共识。\"}\n  action_items:\n    - {round: 22, action: \"Discussion 深化 mitigation 失败的结构性分析（merge amplification/routing failure 的根本原因）\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R22-W2\n  summary: \"单种子+FP8 噪声→CI 未含模型级方差\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - {round: 22, reviewers: [R1, R2], note: \"R1 Must-Fix N1（CI 偏窄，0.88pp 噪声占 margin 30%）。R2 rebut 降级为 should-fix：greedy decoding 下多种子≈重复测量 FP8 噪声，跨模型验证提供间接鲁棒性。交叉后 R1 未进一步坚持 must-fix。Director 判定：should-fix。\"}\n  action_items:\n    - {round: 22, action: \"Limitations 讨论 FP8 噪声传播对 CI 宽度影响，考虑提供 noise-propagated 保守 CI\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R22-W3\n  summary: \"Dim2 cross-model 验证不足，Abstract claim 过宽\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 22\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R21-C3: Dim2 proprietary gap\"}\n    - {round: 22, reviewers: [R1, R2], note: \"R1 Should-Fix W3，R2 交叉 AGREE。BCS-controlled 仅 Qwen3-32B 主模型验证。Abstract 需区分 Dim1（跨模型）vs Dim2（主模型 only）。\"}\n  action_items:\n    - {round: 22, action: \"Abstract/Intro 区分两个维度的验证范围\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R22-W4\n  summary: \"Unconstrained decoding ablation 结论过强 (n=25)\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - {round: 22, reviewers: [R1, R2], note: \"R1 Should-Fix W5，R2 交叉 AGREE。'eliminates the correlation' 措辞过强，n=25 power 不足。应改为 'insufficient evidence to detect'。\"}\n  action_items:\n    - {round: 22, action: \"§5 和 Limitations 弱化 unconstrained ablation 结论措辞\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R22-W5\n  summary: \"DocRED range-matching power 不足，不能声称消除 interaction\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - {round: 22, reviewers: [R1, R2], note: \"R1 Should-Fix W2，R2 交叉 AGREE。CI [-7.13, 7.44] 宽14pp，power 严重不足。non-significance ≠ absence。DocRED 显著交互 vs FewRel TOST 通过的张力未充分调和。\"}\n  action_items:\n    - {round: 22, action: \"报告 range-matched 子集 n 和 post-hoc power，诚实讨论 FewRel/DocRED 张力\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R22-W6\n  summary: \"Pair-to-batch R² 放大 simulation 独立性假设有问题\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - {round: 22, reviewers: [R1, R2], note: \"R1 Should-Fix W1，R2 交叉 AGREE。Simulation 假设 pair 独立但同 batch types 共享 prompt context。R2 补充：核心 batch-level R² 是直接观测值不依赖 simulation。\"}\n  action_items:\n    - {round: 22, action: \"Appendix M 加非独立性讨论，引用 ecological inference 文献\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R22-W7\n  summary: \"Type definitions 分析 (Table 15) 应提升至正文\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - {round: 22, reviewers: [R1, R2], note: \"R2 Should-Fix W3，R1 交叉 AGREE。'definitions 无帮助'是重要发现，目前仅在 Appendix L。\"}\n  action_items:\n    - {round: 22, action: \"§6 practical implications 增加 definitions 分析总结\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R22 INFO / FORMAT\n# ============================================================\n\n- id: R22-F1\n  summary: \"因果语言需 hedge：§5 'due to' → 'largely attributable to'\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - {round: 22, reviewers: [R1, R2], note: \"R1 Should-Fix W4，R2 部分 rebut：Title 'Predict' OK（标准统计用语），BCS-controlled 支持准因果，但 §5 'due to' 和 renaming familiarity confound 需 hedge。\"}\n  action_items:\n    - {round: 22, action: \"§5 加 hedge；Appendix W 讨论 familiarity confound + 交互效应\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R22-F2\n  summary: \"'first controlled study' 措辞过绝对\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - {round: 22, reviewers: [R2], note: \"R2 Minor M3，R1 交叉 AGREE。建议改为 'among the first' 或 'to our knowledge, the first'。\"}\n  action_items:\n    - {round: 22, action: \"检查并统一 'first' claim 措辞\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R22-MR1\n  summary: \"Missing: GLiREL (Boylan et al., NAACL 2025)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - {round: 22, reviewers: [R2], note: \"zero-shot RE via shared embedding space, 与 SCS 概念高度一致。R1 交叉 AGREE。\"}\n  action_items:\n    - {round: 22, action: \"验证并补充引用\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R22-MR2\n  summary: \"Missing: Wan et al. (2024) Grasping the Essentials\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - {round: 22, reviewers: [R2], note: \"LLMs 对 relation definitions 利用不充分，与 Table 15 相关。R1 交叉 AGREE。\"}\n  action_items:\n    - {round: 22, action: \"验证并补充引用\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R22-MR3\n  summary: \"Missing: GLiNER-Relex / ASEE 等 schema matching + extraction 解耦工作\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - {round: 22, reviewers: [R2], note: \"与 SDGD 动机相关。R1 交叉 AGREE。\"}\n  action_items:\n    - {round: 22, action: \"验证并补充引用\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R21 以前 RESOLVED（精简保留）\n# ============================================================\n\n- id: R21-F1\n  summary: \"-ing 分词短语残留（Abstract/Results）\"\n  category: format\n  severity: info\n  status: done\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"R21 编辑批次已清理 7 处 -ing 分词。\"\n  resolution_round: 21\n\n- id: R21-F2\n  summary: \"P-value 报告格式不一致\"\n  category: format\n  severity: info\n  status: done\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"R21 编辑批次已统一为 p<0.001 格式。\"\n  resolution_round: 21\n\n- id: R20-N1\n  summary: \"'Largely additive' overclaim\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 20\n  resolution: \"全文删除 'largely additive'，改为 'two dimensions'。\"\n  resolution_round: 20\n\n- id: R20-N2\n  summary: \"'across NER/RE/ED' framing 超出证据\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 20\n  resolution: \"加 'task-dependent effect structures'。\"\n  resolution_round: 20\n\n- id: R20-N3\n  summary: \"Cohen (1988) effect size 标准不当\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 20\n  resolution: \"Cohen/Lakens 完全删除。\"\n  resolution_round: 20\n\n- id: R20-W1\n  summary: \"Title 'Predict'\"\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 22\n  mentions:\n    - {round: 22, reviewers: [R1, R2], note: \"R1 仍 flag，R2 rebut：'Predict' 是标准统计用语。Director 维持 wont_fix。\"}\n  resolution: \"保留。R2 rebut 有理（标准统计用语），R1 未在交叉中坚持。\"\n  resolution_round: 20"
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
    "issues_yaml": "# Review Issues Tracker\n# Updated: 2026-05-19 (Round 22 fresh review)\n\n# ============================================================\n# R22 CRITICAL\n# ============================================================\n\n- id: R22-C1\n  summary: \"Title/Abstract scope overclaim: 'Information Extraction' 但 batch-level Dim2 仅 RE 成立\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 22\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R21-W1: NER Dim2 batch-level null, Title IE 过宽\"}\n    - {round: 22, reviewers: [R2], note: \"R2 Must-Fix N1。batch-level BCS 仅 RE (FewRel/DocRED) 成立，NER r≈0，MAVEN centrality confound。R1 部分 rebut：pairwise SCS 跨任务成立，batch-level 是聚合局限。交叉后共识：Abstract 需加 task-format qualifier。\"}\n  action_items:\n    - {round: 22, action: \"Abstract 加 task-dependent qualifier，区分 pairwise (跨任务) vs batch-level (RE only)\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R22-C2\n  summary: \"SCS/BCS novelty 不足，与 LLM-PEE partitioning criterion 一致\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 22\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R21-C4: SCS 借自 LLM-PEE，novelty framing 不清晰\"}\n    - {round: 22, reviewers: [R2], note: \"R2 Must-Fix N2。SCS=cosine sim, BCS=mean，无技术创新。'controlled framework' 作主贡献论证不充分。R1 rebut：方法论创新在实验范式非指标，22-58% R² 无法靠直觉预测。交叉后分歧保留。\"}\n  action_items:\n    - {round: 22, action: \"强化 non-obvious findings (22-58% R², renaming 反直觉, NER null)，或补 BCS 实际应用案例\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R22-C3\n  summary: \"TOST ±3pp margin 循环论证 + logit-scale inconclusive\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 21\n  last_seen_round: 22\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R21-C1: margin 来自 BCS 自身预测力\"}\n    - {round: 22, reviewers: [R1, R2], note: \"R1 Must-Fix N2。±3pp 首要理由是 BCS-predicted gap→循环。±2pp FewRel p=0.047 勉强，DocRED inconclusive。R2 部分同意：多个独立锚点存在但正文未充分展示。R2 额外提升 logit-scale TOST inconclusive 至 should-fix。交叉后共识：Cohen's δ 作首要理由，±2pp 入正文，logit 分歧需讨论。\"}\n  action_items:\n    - {round: 22, action: \"正文重构 margin justification：Cohen's δ 为首要锚点，报告 ±2pp 结果，讨论 logit-scale 分歧\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R22-C4\n  summary: \"页数违规：Section 7 (Conclusion) 起始于第9页，超 EMNLP 8页限制\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - {round: 22, reviewers: [R1, R2], note: \"R2 Should-Fix W4，R1 交叉 AGREE 确认违规。双方共识必须修复。\"}\n  action_items:\n    - {round: 22, action: \"压缩正文至8页内（Conclusion 必须在第8页结束前）\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R22 WARNING\n# ============================================================\n\n- id: R22-W1\n  summary: \"无有效 mitigation：SDGD/renaming/few-shot 全部失败\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 22\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R21-W4/C5: 无有效干预，typical ~2pp\"}\n    - {round: 22, reviewers: [R1, R2], note: \"R2 Should-Fix W1，R1 交叉 AGREE。论文最显著弱点。R1 补充：负面结果有独立价值。双方共识。\"}\n  action_items:\n    - {round: 22, action: \"Discussion 深化 mitigation 失败的结构性分析（merge amplification/routing failure 的根本原因）\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R22-W2\n  summary: \"单种子+FP8 噪声→CI 未含模型级方差\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - {round: 22, reviewers: [R1, R2], note: \"R1 Must-Fix N1（CI 偏窄，0.88pp 噪声占 margin 30%）。R2 rebut 降级为 should-fix：greedy decoding 下多种子≈重复测量 FP8 噪声，跨模型验证提供间接鲁棒性。交叉后 R1 未进一步坚持 must-fix。Director 判定：should-fix。\"}\n  action_items:\n    - {round: 22, action: \"Limitations 讨论 FP8 噪声传播对 CI 宽度影响，考虑提供 noise-propagated 保守 CI\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R22-W3\n  summary: \"Dim2 cross-model 验证不足，Abstract claim 过宽\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 21\n  last_seen_round: 22\n  mentions:\n    - {round: 21, reviewers: [R1, R2], note: \"R21-C3: Dim2 proprietary gap\"}\n    - {round: 22, reviewers: [R1, R2], note: \"R1 Should-Fix W3，R2 交叉 AGREE。BCS-controlled 仅 Qwen3-32B 主模型验证。Abstract 需区分 Dim1（跨模型）vs Dim2（主模型 only）。\"}\n  action_items:\n    - {round: 22, action: \"Abstract/Intro 区分两个维度的验证范围\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R22-W4\n  summary: \"Unconstrained decoding ablation 结论过强 (n=25)\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - {round: 22, reviewers: [R1, R2], note: \"R1 Should-Fix W5，R2 交叉 AGREE。'eliminates the correlation' 措辞过强，n=25 power 不足。应改为 'insufficient evidence to detect'。\"}\n  action_items:\n    - {round: 22, action: \"§5 和 Limitations 弱化 unconstrained ablation 结论措辞\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R22-W5\n  summary: \"DocRED range-matching power 不足，不能声称消除 interaction\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - {round: 22, reviewers: [R1, R2], note: \"R1 Should-Fix W2，R2 交叉 AGREE。CI [-7.13, 7.44] 宽14pp，power 严重不足。non-significance ≠ absence。DocRED 显著交互 vs FewRel TOST 通过的张力未充分调和。\"}\n  action_items:\n    - {round: 22, action: \"报告 range-matched 子集 n 和 post-hoc power，诚实讨论 FewRel/DocRED 张力\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R22-W6\n  summary: \"Pair-to-batch R² 放大 simulation 独立性假设有问题\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - {round: 22, reviewers: [R1, R2], note: \"R1 Should-Fix W1，R2 交叉 AGREE。Simulation 假设 pair 独立但同 batch types 共享 prompt context。R2 补充：核心 batch-level R² 是直接观测值不依赖 simulation。\"}\n  action_items:\n    - {round: 22, action: \"Appendix M 加非独立性讨论，引用 ecological inference 文献\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R22-W7\n  summary: \"Type definitions 分析 (Table 15) 应提升至正文\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - {round: 22, reviewers: [R1, R2], note: \"R2 Should-Fix W3，R1 交叉 AGREE。'definitions 无帮助'是重要发现，目前仅在 Appendix L。\"}\n  action_items:\n    - {round: 22, action: \"§6 practical implications 增加 definitions 分析总结\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R22 INFO / FORMAT\n# ============================================================\n\n- id: R22-F1\n  summary: \"因果语言需 hedge：§5 'due to' → 'largely attributable to'\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - {round: 22, reviewers: [R1, R2], note: \"R1 Should-Fix W4，R2 部分 rebut：Title 'Predict' OK（标准统计用语），BCS-controlled 支持准因果，但 §5 'due to' 和 renaming familiarity confound 需 hedge。\"}\n  action_items:\n    - {round: 22, action: \"§5 加 hedge；Appendix W 讨论 familiarity confound + 交互效应\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R22-F2\n  summary: \"'first controlled study' 措辞过绝对\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - {round: 22, reviewers: [R2], note: \"R2 Minor M3，R1 交叉 AGREE。建议改为 'among the first' 或 'to our knowledge, the first'。\"}\n  action_items:\n    - {round: 22, action: \"检查并统一 'first' claim 措辞\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R22-MR1\n  summary: \"Missing: GLiREL (Boylan et al., NAACL 2025)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - {round: 22, reviewers: [R2], note: \"zero-shot RE via shared embedding space, 与 SCS 概念高度一致。R1 交叉 AGREE。\"}\n  action_items:\n    - {round: 22, action: \"验证并补充引用\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R22-MR2\n  summary: \"Missing: Wan et al. (2024) Grasping the Essentials\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - {round: 22, reviewers: [R2], note: \"LLMs 对 relation definitions 利用不充分，与 Table 15 相关。R1 交叉 AGREE。\"}\n  action_items:\n    - {round: 22, action: \"验证并补充引用\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R22-MR3\n  summary: \"Missing: GLiNER-Relex / ASEE 等 schema matching + extraction 解耦工作\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 22\n  last_seen_round: 22\n  mentions:\n    - {round: 22, reviewers: [R2], note: \"与 SDGD 动机相关。R1 交叉 AGREE。\"}\n  action_items:\n    - {round: 22, action: \"验证并补充引用\", assigned_to: main_agent, status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R21 以前 RESOLVED（精简保留）\n# ============================================================\n\n- id: R21-F1\n  summary: \"-ing 分词短语残留（Abstract/Results）\"\n  category: format\n  severity: info\n  status: done\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"R21 编辑批次已清理 7 处 -ing 分词。\"\n  resolution_round: 21\n\n- id: R21-F2\n  summary: \"P-value 报告格式不一致\"\n  category: format\n  severity: info\n  status: done\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"R21 编辑批次已统一为 p<0.001 格式。\"\n  resolution_round: 21\n\n- id: R20-N1\n  summary: \"'Largely additive' overclaim\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 20\n  resolution: \"全文删除 'largely additive'，改为 'two dimensions'。\"\n  resolution_round: 20\n\n- id: R20-N2\n  summary: \"'across NER/RE/ED' framing 超出证据\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 20\n  resolution: \"加 'task-dependent effect structures'。\"\n  resolution_round: 20\n\n- id: R20-N3\n  summary: \"Cohen (1988) effect size 标准不当\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 20\n  resolution: \"Cohen/Lakens 完全删除。\"\n  resolution_round: 20\n\n- id: R20-W1\n  summary: \"Title 'Predict'\"\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 20\n  last_seen_round: 22\n  mentions:\n    - {round: 22, reviewers: [R1, R2], note: \"R1 仍 flag，R2 rebut：'Predict' 是标准统计用语。Director 维持 wont_fix。\"}\n  resolution: \"保留。R2 rebut 有理（标准统计用语），R1 未在交叉中坚持。\"\n  resolution_round: 20"
  }
}
```

</details>

---


### Tool result

_source line 2379 · 2026-05-19T18:05:34.801024+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml\", \"bytes\": 10712}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2380 · 2026-05-19T18:07:37.707222+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 22 (Fresh Review)\n\n**项目**: schema-dag-extraction\n**论文**: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n**目标 Venue**: EMNLP 2026 (ARR May 2026)\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性/完整性）\n**轮次**: 1 轮（交叉后收敛）\n\n---\n\n## Summary\n\n本文研究 training-free LLM information extraction 中 schema complexity 如何预测性能退化，提出 Schema Confusability Score (SCS) 和 Batch Confusability Score (BCS) 两个度量，在 Few-NERD (NER)、FewRel (RE)、DocRED (DocRE)、MAVEN (ED) 四个数据集上开展受控实验。核心发现：退化沿两个维度运作——type count 驱动 recall 下降（Dim1），type confusability 驱动 type substitution（Dim2）；BCS 解释 22-58% 的跨 batch RE accuracy variance，但 NER 无 batch-level 信号。所有 mitigation 尝试（schema decomposition、label renaming、few-shot）均失败。\n\n---\n\n## Strengths\n\n**S1.** 研究问题重要且填补明确空白——zero-shot LLM IE 中 schema complexity 影响的首次系统受控研究，count-curve + BCS-controlled 双范式互补设计在该领域罕见 [R1, R2 共识]\n\n**S2.** 统计方法论显著优于领域平均水平：TOST equivalence tests、bootstrap CIs (B=10,000)、permutation tests、cross-seed variance decomposition、range-matched robustness checks [R1 Soundness 3.5, R2 Soundness 4]\n\n**S3.** 负面结果的诚实报告具有独立价值：NER batch-level null、MAVEN centrality confound、SDGD 全面失败（merge amplification + routing failure）、renaming 降低准确率、few-shot 扩大 confusability gap [R1, R2 共识]\n\n**S4.** 17 个 Appendix 的深度和透明度罕见，Limitations section 全面诚实 [R1, R2 共识]\n\n**S5.** 跨模型验证（Llama-3.1-8B/70B, Gemini 2.5 Flash API）增强 Dimension 1 结论可信度 [R1, R2 共识]\n\n**S6.** Error taxonomy（Figure 2, Table 3）将 confusability 与具体错误类型（IntraSub）建立因果链，有独立分析价值 [R2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1. [Must-Fix] Title/Abstract scope 与实际发现不匹配** [R2 N1, R1 部分同意]\n- Title 声称 \"Information Extraction\" 但 batch-level confusability（Dim2 核心叙事）仅在 RE (FewRel, DocRED) 上完整成立\n- NER batch-level BCS-F1 correlation r ≈ 0（§4.2, n=450）\n- MAVEN ED 受 centrality confound（§4.5）\n- R1 rebut：pairwise SCS 跨任务成立，batch-level 是聚合局限非维度失败。但 R1 也同意 Abstract framing 需加 task-format qualifier\n- **共识**：Abstract 必须区分 pairwise (跨任务) vs batch-level (RE only)；建议 Abstract 加 \"task-dependent effect structures\" 和 \"under RE's forced-choice format\" qualifier\n\n**C2. [Must-Fix] SCS/BCS 核心度量的 novelty 论证不充分** [R2 N2, R1 rebut 但下调评分]\n- SCS = cosine similarity of type-name embeddings，BCS = mean pairwise SCS——无技术创新\n- 论文自承与 LLM-PEE 的 partitioning criterion 一致（§2 最后一段）\n- \"Controlled experimental framework\" 作为主贡献，需更有力地论证与 standard ablation study 的区别\n- R1 rebut：方法论创新在实验范式，22-58% R²、renaming 反直觉结果、NER null 无法靠直觉预测。但 R1 交叉后也将评分下调至 3.0-3.5\n- **共识**：需更突出 non-obvious findings 和定量发现的价值，或补充 BCS 的实际应用案例\n\n**C3. [Must-Fix] TOST ±3pp margin 循环论证 + logit-scale 分歧** [R1 N2, R2 部分同意]\n- ±3pp 首要理由是 \"approximates the typical BCS-predicted accuracy gap\"——用 BCS 自身预测力校准检验 BCS 效应是否可忽略的阈值\n- 灵敏度分析：±2pp 时 FewRel 仅勉强通过（p=0.047）；logit-scale TOST inconclusive（p=0.209）\n- R2 补充：logit 变换对 bounded data 更合理，logit inconclusive 削弱等价性结论（从 minor 升级为 should-fix）\n- 论文提供了 Cohen's δ 和实践显著性等独立锚点，但正文未充分展示\n- **共识**：Cohen's δ 作为首要理由，±2pp 结果入正文，logit-scale 分歧需正文讨论\n\n**C4. [Must-Fix] 页数违规** [R2 W4, R1 交叉 AGREE]\n- Section 7 (Conclusion) 起始于第9页，正文超出 EMNLP 2026 的 8 页限制\n- **双方确认违规，必须压缩**\n\n### Should-Fix（影响论文质量）\n\n**W1. 无有效 mitigation** [R1, R2 共识]\n- SDGD 失败（NER merge amplification, RE routing failure, ED 同）\n- Renaming 降低准确率（-3.0pp low-BCS, -8.8pp high-BCS; Table 24）\n- Few-shot 扩大 confusability gap (+4.3pp from 0-shot to 5-shot)\n- 唯一建议 \"flag SCS > 0.85\" 为监控非解决方案\n- R1 补充：负面结果有独立价值，约束了未来解决方案空间\n\n**W2. 单种子+FP8 噪声→CI 未含模型级方差** [R1 N1→降级, R2 rebut]\n- Bootstrap CI 仅捕获 batch composition variance；FP8 residual SD=0.88pp（Appendix Q）\n- R2 rebut 有效：greedy decoding 下多种子≈重复测量 FP8 噪声；跨模型验证提供间接鲁棒性\n- **Director 判定**：降为 should-fix。建议 FP8 噪声传播进 bootstrap 产生保守 CI\n\n**W3. Dim2 cross-model 验证不足** [R1 W3, R2 AGREE]\n- BCS-controlled（Dim2）仅在 Qwen3-32B 上验证，NER 在 8B 模型有 floor effects\n- Dim2 (BCS) 未在 proprietary models 验证（Limitations §7 已承认）\n- Abstract/Intro 措辞未充分区分两个维度的验证范围\n\n**W4. Unconstrained decoding ablation 结论过强** [R1 W5, R2 AGREE]\n- n=25，\"eliminates the BCS-accuracy correlation\" 措辞过强\n- 未做 Fisher z-test 正式比较 constrained vs unconstrained 的 ρ 差异\n- 应改为 \"insufficient evidence to detect\" 并报告 power\n\n**W5. DocRED range-matching power 不足** [R1 W2, R2 AGREE]\n- Range-matched CI [-7.13, 7.44]，宽度~14pp，power 严重不足\n- Non-significance ≠ absence of interaction\n- DocRED 显著交互 (−9.4pp) 与 FewRel TOST 通过之间的张力未充分调和\n\n**W6. Pair-to-batch R² 放大 simulation 独立性假设** [R1 W1, R2 AGREE]\n- Simulation 假设 pair-level 效应独立，但同 batch types 共享 prompt context\n- R2 补充：核心 batch-level R² 是直接观测值不依赖 simulation\n- 需补充非独立性讨论和 ecological inference 文献\n\n**W7. Type definitions 分析应提升至正文** [R2 W3, R1 AGREE]\n- \"definitions 无帮助\"（Table 15, Δr: −0.023 to +0.035）是重要发现，目前仅在 Appendix L\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **页数违规必须修复**（C4）\n2. **Abstract 需加 task-format qualifier**（C1）——pairwise 跨任务成立，batch-level 仅 RE\n3. **TOST margin 需重构 justification**（C3）——Cohen's δ 为首要锚点\n4. **无有效 mitigation 是最实质弱点**（W1）——但负面结果有独立价值\n5. **Unconstrained ablation 结论需弱化**（W4）\n6. **DocRED range-matching 需报告 power**（W5）\n7. **Definitions 分析应入正文**（W7）\n8. **Missing references 均应补充**（MR1-MR3）\n9. **Execution quality 高**（Soundness 3.5-4），统计方法论优于领域平均\n10. **负面结果报告值得肯定**\n\n## Reviewer Divergence [REBUT]\n\n1. **单种子 CI 严重性**：R1 认为 must-fix（需多种子）；R2 rebut 降级为 should-fix（greedy decoding 下多种子无新信息，FP8 噪声传播即可）。**Director 采纳 R2 立场**——R2 关于 greedy decoding 的论证有效。\n\n2. **Novelty 是否足够**：R2 认为 SCS/BCS 无技术新意 + core finding 可预期→Excitement 2.5；R1 认为方法论创新在实验范式→Excitement 3.5。**Director 判断**：novelty 确实有限（SCS = cosine sim），但定量发现（22-58% R²）超出直觉，合理区间 3.0。\n\n3. **Title \"Predict\"**：R1 认为暗示因果需修改；R2 rebut \"Predict\" 是标准统计用语，BCS-controlled 是准实验设计。**Director 采纳 R2 立场**——Title 无需修改。\n\n4. **Few-shot confounding**：R1 认为高 BCS batch 的 few-shot example 区分度可能更低；R2 rebut 实证数据不支持此担忧（gap 未按 confound 预测方向变化）。**Director 采纳 R2 立场**——添加 disclaimer 即可。\n\n---\n\n## Questions to Authors\n\n1. 能否提供 FP8 噪声传播后的保守 CI（即使仅 FewRel BCS-controlled）？这比多种子实验更有信息量。\n2. TOST ±3pp margin 是否有来自先前 LLM IE 工作的 external benchmark？如无，Cohen's δ 应作为首要理由。\n3. DocRED 显著交互（−9.4pp）与 FewRel TOST 通过之间的张力如何调和？\"bounded interaction\" 的适用范围是否应限定为 sentence-level RE？\n4. Appendix M 中 EF=3.35 是从 batch 内有效自由度独立计算，还是从 observed R² 反推？如果是后者，simulation 论证为同义反复。\n5. NER batch-level null 的根本假设是什么？exact-match 评估将 boundary/type error 混合是唯一解释吗？\n6. Abstract 数字（85.7%, 49.5%, 88.0%, 38.7%）的具体来源条件（dataset, count level, prompt version）应标注。\n\n---\n\n## Missing References\n\n以下引用经两位 Reviewer 共识确认应补充：\n\n1. **GLiREL** (Boylan et al., NAACL 2025) — zero-shot RE via shared embedding space，与 SCS 概念一致\n2. **Grasping the Essentials** (Wan et al., 2024) — LLMs 对 relation definitions 利用不充分，与 Table 15 发现相关\n3. **GLiNER-Relex / ASEE** 等 schema matching + extraction 解耦工作，与 SDGD 动机相关\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求**（项目未启用 `external_review.paperreview_ai`）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：timeout**（elapsed 1068s）。视觉审查 Agent 超时未完成。用户可手动重新触发 `dispatch_visual_check`。本报告不因视觉审查推迟投递。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 — Findings**\n**Confidence: 4/5**\n\n| 维度 | R1 | R2 | Director 综合 |\n|------|----|----|--------------|\n| Soundness | 3.5 | 4.0 | **3.75** |\n| Excitement | 3.5 | 2.5 | **3.0** |\n| Reproducibility | 3.5 | 4.0 | **3.75** |\n| Overall | 3.0-3.5 | 3.5 | **3.0** |\n\n**评分理由**：\n\n执行质量高的实证分析论文。双范式受控实验设计（count-curve + BCS-controlled）在 LLM IE 领域少见，统计方法论规范，负面结果报告透明。Soundness 接近 4 分水平。\n\n但以下因素制约其达到主会议水平：\n1. **Novelty 有限**：SCS/BCS 无技术创新（cosine similarity + mean），与 LLM-PEE 一致；core finding \"confusable types hurt performance\" 方向可预期\n2. **Scope 不匹配**：Title 声称 IE，但 batch-level Dim2 仅 RE 成立（2/4 数据集）\n3. **无有效 mitigation**：所有干预尝试失败，实际可操作建议有限\n4. **统计敏感性**：TOST 等价性对 margin 选择敏感（±2pp 勉强，logit inconclusive），DocRED interaction 张力未解决\n5. **页数违规**：正文超8页\n\n**达到 3.5 (Borderline Conference) 的路径**：修复页数违规 + 重构 TOST margin justification + Abstract 加 task-dependent qualifier + 强化 non-obvious findings 作为 novelty 论证 + 正文纳入 definitions 分析。\n\n**达到 4.0 (Conference) 的路径**：以上全部 + 补充至少一个 promising mitigation 方向（即使初步）+ 多模型 BCS-controlled 验证 + FP8 保守 CI。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"first controlled study\" → 建议改为 \"to our knowledge, the first controlled study\"（论文部分已使用此措辞，但不一致）\n- 四个 findings 的 (2) 应更明确区分 pairwise (跨任务) vs batch-level (RE only)\n\n### §3 Experimental Setup\n- §3.2 SCS 定义：应在正文（而非仅 Appendix L）提及 name-only vs name+definition 对比结果\n- §3.5 Model：FP8 噪声传播对 CI 的影响应在此处或 Limitations 讨论\n\n### §4 Results\n- §4.2 BCS-Controlled：practical magnitude（IQR Δ=2.2pp）应更突出——这是典型场景下的预期效应量，极端 batch gap（25-31pp）是设计上放大的\n- §4.4 Multi-Dimensional：TOST margin justification 需重构；±2pp 结果和 logit-scale 分歧需入正文\n- §4.4 DocRED factorial：range-matched 分析需报告 n 和 power；诚实讨论与 FewRel 的张力\n\n### §5 SDGD\n- \"eliminates the BCS-accuracy correlation\" → \"insufficient evidence to detect a significant correlation at n=25\"\n- 因果语言 \"due to\" → 加 hedge \"largely attributable to\"\n- MAVEN ED 结果（merge amplification 确认）是有价值的新增，但应说明其对 general IE claim 的支撑有限\n\n### §6 Discussion\n- \"SCS as a proxy for conceptual overlap\" 段落很好，但应与 renaming 的 familiarity confound 更明确关联\n- Practical implications 应纳入 definitions 分析（Table 15）和 Rothman multiple comparison 策略的更早讨论\n\n### Appendix\n- Appendix M (Simulation): 澄清 EF=3.35 来源（独立估计 vs 反推）；加非独立性讨论\n- Appendix C (Factorial): 报告 range-matched n 和 post-hoc power\n\n### 格式\n- 压缩正文至8页（Conclusion 必须在第8页内结束）\n- 补充 3 篇 missing references",
  "project": "schema-dag-extraction",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 — Findings",
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
    "report": "# 审稿报告 — Round 22 (Fresh Review)\n\n**项目**: schema-dag-extraction\n**论文**: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n**目标 Venue**: EMNLP 2026 (ARR May 2026)\n**审稿模式**: Fresh (重新审稿)\n**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性/完整性）\n**轮次**: 1 轮（交叉后收敛）\n\n---\n\n## Summary\n\n本文研究 training-free LLM information extraction 中 schema complexity 如何预测性能退化，提出 Schema Confusability Score (SCS) 和 Batch Confusability Score (BCS) 两个度量，在 Few-NERD (NER)、FewRel (RE)、DocRED (DocRE)、MAVEN (ED) 四个数据集上开展受控实验。核心发现：退化沿两个维度运作——type count 驱动 recall 下降（Dim1），type confusability 驱动 type substitution（Dim2）；BCS 解释 22-58% 的跨 batch RE accuracy variance，但 NER 无 batch-level 信号。所有 mitigation 尝试（schema decomposition、label renaming、few-shot）均失败。\n\n---\n\n## Strengths\n\n**S1.** 研究问题重要且填补明确空白——zero-shot LLM IE 中 schema complexity 影响的首次系统受控研究，count-curve + BCS-controlled 双范式互补设计在该领域罕见 [R1, R2 共识]\n\n**S2.** 统计方法论显著优于领域平均水平：TOST equivalence tests、bootstrap CIs (B=10,000)、permutation tests、cross-seed variance decomposition、range-matched robustness checks [R1 Soundness 3.5, R2 Soundness 4]\n\n**S3.** 负面结果的诚实报告具有独立价值：NER batch-level null、MAVEN centrality confound、SDGD 全面失败（merge amplification + routing failure）、renaming 降低准确率、few-shot 扩大 confusability gap [R1, R2 共识]\n\n**S4.** 17 个 Appendix 的深度和透明度罕见，Limitations section 全面诚实 [R1, R2 共识]\n\n**S5.** 跨模型验证（Llama-3.1-8B/70B, Gemini 2.5 Flash API）增强 Dimension 1 结论可信度 [R1, R2 共识]\n\n**S6.** Error taxonomy（Figure 2, Table 3）将 confusability 与具体错误类型（IntraSub）建立因果链，有独立分析价值 [R2]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1. [Must-Fix] Title/Abstract scope 与实际发现不匹配** [R2 N1, R1 部分同意]\n- Title 声称 \"Information Extraction\" 但 batch-level confusability（Dim2 核心叙事）仅在 RE (FewRel, DocRED) 上完整成立\n- NER batch-level BCS-F1 correlation r ≈ 0（§4.2, n=450）\n- MAVEN ED 受 centrality confound（§4.5）\n- R1 rebut：pairwise SCS 跨任务成立，batch-level 是聚合局限非维度失败。但 R1 也同意 Abstract framing 需加 task-format qualifier\n- **共识**：Abstract 必须区分 pairwise (跨任务) vs batch-level (RE only)；建议 Abstract 加 \"task-dependent effect structures\" 和 \"under RE's forced-choice format\" qualifier\n\n**C2. [Must-Fix] SCS/BCS 核心度量的 novelty 论证不充分** [R2 N2, R1 rebut 但下调评分]\n- SCS = cosine similarity of type-name embeddings，BCS = mean pairwise SCS——无技术创新\n- 论文自承与 LLM-PEE 的 partitioning criterion 一致（§2 最后一段）\n- \"Controlled experimental framework\" 作为主贡献，需更有力地论证与 standard ablation study 的区别\n- R1 rebut：方法论创新在实验范式，22-58% R²、renaming 反直觉结果、NER null 无法靠直觉预测。但 R1 交叉后也将评分下调至 3.0-3.5\n- **共识**：需更突出 non-obvious findings 和定量发现的价值，或补充 BCS 的实际应用案例\n\n**C3. [Must-Fix] TOST ±3pp margin 循环论证 + logit-scale 分歧** [R1 N2, R2 部分同意]\n- ±3pp 首要理由是 \"approximates the typical BCS-predicted accuracy gap\"——用 BCS 自身预测力校准检验 BCS 效应是否可忽略的阈值\n- 灵敏度分析：±2pp 时 FewRel 仅勉强通过（p=0.047）；logit-scale TOST inconclusive（p=0.209）\n- R2 补充：logit 变换对 bounded data 更合理，logit inconclusive 削弱等价性结论（从 minor 升级为 should-fix）\n- 论文提供了 Cohen's δ 和实践显著性等独立锚点，但正文未充分展示\n- **共识**：Cohen's δ 作为首要理由，±2pp 结果入正文，logit-scale 分歧需正文讨论\n\n**C4. [Must-Fix] 页数违规** [R2 W4, R1 交叉 AGREE]\n- Section 7 (Conclusion) 起始于第9页，正文超出 EMNLP 2026 的 8 页限制\n- **双方确认违规，必须压缩**\n\n### Should-Fix（影响论文质量）\n\n**W1. 无有效 mitigation** [R1, R2 共识]\n- SDGD 失败（NER merge amplification, RE routing failure, ED 同）\n- Renaming 降低准确率（-3.0pp low-BCS, -8.8pp high-BCS; Table 24）\n- Few-shot 扩大 confusability gap (+4.3pp from 0-shot to 5-shot)\n- 唯一建议 \"flag SCS > 0.85\" 为监控非解决方案\n- R1 补充：负面结果有独立价值，约束了未来解决方案空间\n\n**W2. 单种子+FP8 噪声→CI 未含模型级方差** [R1 N1→降级, R2 rebut]\n- Bootstrap CI 仅捕获 batch composition variance；FP8 residual SD=0.88pp（Appendix Q）\n- R2 rebut 有效：greedy decoding 下多种子≈重复测量 FP8 噪声；跨模型验证提供间接鲁棒性\n- **Director 判定**：降为 should-fix。建议 FP8 噪声传播进 bootstrap 产生保守 CI\n\n**W3. Dim2 cross-model 验证不足** [R1 W3, R2 AGREE]\n- BCS-controlled（Dim2）仅在 Qwen3-32B 上验证，NER 在 8B 模型有 floor effects\n- Dim2 (BCS) 未在 proprietary models 验证（Limitations §7 已承认）\n- Abstract/Intro 措辞未充分区分两个维度的验证范围\n\n**W4. Unconstrained decoding ablation 结论过强** [R1 W5, R2 AGREE]\n- n=25，\"eliminates the BCS-accuracy correlation\" 措辞过强\n- 未做 Fisher z-test 正式比较 constrained vs unconstrained 的 ρ 差异\n- 应改为 \"insufficient evidence to detect\" 并报告 power\n\n**W5. DocRED range-matching power 不足** [R1 W2, R2 AGREE]\n- Range-matched CI [-7.13, 7.44]，宽度~14pp，power 严重不足\n- Non-significance ≠ absence of interaction\n- DocRED 显著交互 (−9.4pp) 与 FewRel TOST 通过之间的张力未充分调和\n\n**W6. Pair-to-batch R² 放大 simulation 独立性假设** [R1 W1, R2 AGREE]\n- Simulation 假设 pair-level 效应独立，但同 batch types 共享 prompt context\n- R2 补充：核心 batch-level R² 是直接观测值不依赖 simulation\n- 需补充非独立性讨论和 ecological inference 文献\n\n**W7. Type definitions 分析应提升至正文** [R2 W3, R1 AGREE]\n- \"definitions 无帮助\"（Table 15, Δr: −0.023 to +0.035）是重要发现，目前仅在 Appendix L\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **页数违规必须修复**（C4）\n2. **Abstract 需加 task-format qualifier**（C1）——pairwise 跨任务成立，batch-level 仅 RE\n3. **TOST margin 需重构 justification**（C3）——Cohen's δ 为首要锚点\n4. **无有效 mitigation 是最实质弱点**（W1）——但负面结果有独立价值\n5. **Unconstrained ablation 结论需弱化**（W4）\n6. **DocRED range-matching 需报告 power**（W5）\n7. **Definitions 分析应入正文**（W7）\n8. **Missing references 均应补充**（MR1-MR3）\n9. **Execution quality 高**（Soundness 3.5-4），统计方法论优于领域平均\n10. **负面结果报告值得肯定**\n\n## Reviewer Divergence [REBUT]\n\n1. **单种子 CI 严重性**：R1 认为 must-fix（需多种子）；R2 rebut 降级为 should-fix（greedy decoding 下多种子无新信息，FP8 噪声传播即可）。**Director 采纳 R2 立场**——R2 关于 greedy decoding 的论证有效。\n\n2. **Novelty 是否足够**：R2 认为 SCS/BCS 无技术新意 + core finding 可预期→Excitement 2.5；R1 认为方法论创新在实验范式→Excitement 3.5。**Director 判断**：novelty 确实有限（SCS = cosine sim），但定量发现（22-58% R²）超出直觉，合理区间 3.0。\n\n3. **Title \"Predict\"**：R1 认为暗示因果需修改；R2 rebut \"Predict\" 是标准统计用语，BCS-controlled 是准实验设计。**Director 采纳 R2 立场**——Title 无需修改。\n\n4. **Few-shot confounding**：R1 认为高 BCS batch 的 few-shot example 区分度可能更低；R2 rebut 实证数据不支持此担忧（gap 未按 confound 预测方向变化）。**Director 采纳 R2 立场**——添加 disclaimer 即可。\n\n---\n\n## Questions to Authors\n\n1. 能否提供 FP8 噪声传播后的保守 CI（即使仅 FewRel BCS-controlled）？这比多种子实验更有信息量。\n2. TOST ±3pp margin 是否有来自先前 LLM IE 工作的 external benchmark？如无，Cohen's δ 应作为首要理由。\n3. DocRED 显著交互（−9.4pp）与 FewRel TOST 通过之间的张力如何调和？\"bounded interaction\" 的适用范围是否应限定为 sentence-level RE？\n4. Appendix M 中 EF=3.35 是从 batch 内有效自由度独立计算，还是从 observed R² 反推？如果是后者，simulation 论证为同义反复。\n5. NER batch-level null 的根本假设是什么？exact-match 评估将 boundary/type error 混合是唯一解释吗？\n6. Abstract 数字（85.7%, 49.5%, 88.0%, 38.7%）的具体来源条件（dataset, count level, prompt version）应标注。\n\n---\n\n## Missing References\n\n以下引用经两位 Reviewer 共识确认应补充：\n\n1. **GLiREL** (Boylan et al., NAACL 2025) — zero-shot RE via shared embedding space，与 SCS 概念一致\n2. **Grasping the Essentials** (Wan et al., 2024) — LLMs 对 relation definitions 利用不充分，与 Table 15 发现相关\n3. **GLiNER-Relex / ASEE** 等 schema matching + extraction 解耦工作，与 SDGD 动机相关\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：未请求**（项目未启用 `external_review.paperreview_ai`）\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：timeout**（elapsed 1068s）。视觉审查 Agent 超时未完成。用户可手动重新触发 `dispatch_visual_check`。本报告不因视觉审查推迟投递。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 — Findings**\n**Confidence: 4/5**\n\n| 维度 | R1 | R2 | Director 综合 |\n|------|----|----|--------------|\n| Soundness | 3.5 | 4.0 | **3.75** |\n| Excitement | 3.5 | 2.5 | **3.0** |\n| Reproducibility | 3.5 | 4.0 | **3.75** |\n| Overall | 3.0-3.5 | 3.5 | **3.0** |\n\n**评分理由**：\n\n执行质量高的实证分析论文。双范式受控实验设计（count-curve + BCS-controlled）在 LLM IE 领域少见，统计方法论规范，负面结果报告透明。Soundness 接近 4 分水平。\n\n但以下因素制约其达到主会议水平：\n1. **Novelty 有限**：SCS/BCS 无技术创新（cosine similarity + mean），与 LLM-PEE 一致；core finding \"confusable types hurt performance\" 方向可预期\n2. **Scope 不匹配**：Title 声称 IE，但 batch-level Dim2 仅 RE 成立（2/4 数据集）\n3. **无有效 mitigation**：所有干预尝试失败，实际可操作建议有限\n4. **统计敏感性**：TOST 等价性对 margin 选择敏感（±2pp 勉强，logit inconclusive），DocRED interaction 张力未解决\n5. **页数违规**：正文超8页\n\n**达到 3.5 (Borderline Conference) 的路径**：修复页数违规 + 重构 TOST margin justification + Abstract 加 task-dependent qualifier + 强化 non-obvious findings 作为 novelty 论证 + 正文纳入 definitions 分析。\n\n**达到 4.0 (Conference) 的路径**：以上全部 + 补充至少一个 promising mitigation 方向（即使初步）+ 多模型 BCS-controlled 验证 + FP8 保守 CI。\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"first controlled study\" → 建议改为 \"to our knowledge, the first controlled study\"（论文部分已使用此措辞，但不一致）\n- 四个 findings 的 (2) 应更明确区分 pairwise (跨任务) vs batch-level (RE only)\n\n### §3 Experimental Setup\n- §3.2 SCS 定义：应在正文（而非仅 Appendix L）提及 name-only vs name+definition 对比结果\n- §3.5 Model：FP8 噪声传播对 CI 的影响应在此处或 Limitations 讨论\n\n### §4 Results\n- §4.2 BCS-Controlled：practical magnitude（IQR Δ=2.2pp）应更突出——这是典型场景下的预期效应量，极端 batch gap（25-31pp）是设计上放大的\n- §4.4 Multi-Dimensional：TOST margin justification 需重构；±2pp 结果和 logit-scale 分歧需入正文\n- §4.4 DocRED factorial：range-matched 分析需报告 n 和 power；诚实讨论与 FewRel 的张力\n\n### §5 SDGD\n- \"eliminates the BCS-accuracy correlation\" → \"insufficient evidence to detect a significant correlation at n=25\"\n- 因果语言 \"due to\" → 加 hedge \"largely attributable to\"\n- MAVEN ED 结果（merge amplification 确认）是有价值的新增，但应说明其对 general IE claim 的支撑有限\n\n### §6 Discussion\n- \"SCS as a proxy for conceptual overlap\" 段落很好，但应与 renaming 的 familiarity confound 更明确关联\n- Practical implications 应纳入 definitions 分析（Table 15）和 Rothman multiple comparison 策略的更早讨论\n\n### Appendix\n- Appendix M (Simulation): 澄清 EF=3.35 来源（独立估计 vs 反推）；加非独立性讨论\n- Appendix C (Factorial): 报告 range-matched n 和 post-hoc power\n\n### 格式\n- 压缩正文至8页（Conclusion 必须在第8页内结束）\n- 补充 3 篇 missing references",
    "project": "schema-dag-extraction",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 — Findings",
    "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
  }
}
```

</details>

---


### Tool result

_source line 2381 · 2026-05-19T18:07:42.392756+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_51326259fe46fbae9da26b81cf03f1f8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4685
}
```

</details>

---


### Tool call

_source line 2382 · 2026-05-19T18:07:48.726253+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0-3: 完成全部审稿流程', 'status': 'completed', 'activeForm': '完成全部审稿流程'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'completed', 'activeForm': '审稿报告已投递'}]"
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
    "todos": "[{'content': 'Step 0-3: 完成全部审稿流程', 'status': 'completed', 'activeForm': '完成全部审稿流程'}, {'content': 'Step 4: 汇总报告 + 同步 Issue Tracker + 投递', 'status': 'completed', 'activeForm': '审稿报告已投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2383 · 2026-05-19T18:07:48.726976+00:00_

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

_source line 2384 · 2026-05-19T18:07:56.676996+00:00_

**Round 22 审稿完成。**

审稿报告已投递给 Research Director。

**最终评分：3.0 — Findings**

核心判断：
- **Soundness 3.75**：双范式受控设计精巧，统计方法优于领域平均
- **Excitement 3.0**：SCS/BCS 无技术新意，core finding 方向可预期，无有效 mitigation
- 4 个 Must-Fix（Title scope overclaim、novelty 论证、TOST margin 循环论证、页数违规）
- 7 个 Should-Fix（无 mitigation、单种子 CI、Dim2 验证范围、ablation 结论过强、DocRED power、simulation 独立性、definitions 入正文）
- 3 篇 Missing References
- Issue Tracker 已同步（15 个 R22 issues + 历史 resolved）
- 视觉审查超时（未阻塞报告）；外部审稿未配置

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 202

## Round 202

2 recorded events


### User

_source line 2385 · 2026-05-19T18:07:59.301386+00:00_

[Reviewer 2 审稿结果]:
已完成。逐条回应已提交给 Review Director，核心分歧点：

1. **N1 降级**：greedy decoding 下单种子问题被 R1 高估，建议从 must-fix 降为 should-fix
2. **N2 部分同意**：循环性存在但被夸大，多个独立锚点可用，关键是正文应充分讨论 ±2pp 灵敏度
3. **W4 部分反驳**：Title "Predict" 是标准统计用语无需改；BCS-controlled 是准实验设计，支持方向性因果推断
4. **M2 提升**：logit-scale TOST inconclusive 应从 minor 升级为 should-fix，对等价性结论有实质影响

Overall Assessment 与 R1 一致：**3.5（Borderline Conference）**，处理好 N2 + M2 后可达 4.0。

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

_source line 2386 · 2026-05-19T18:08:09.872280+00:00_

审稿报告已投递完成。

**Round 22 审稿总结：**

- **Overall: 3.0 (Findings)**，Soundness 3.75，Excitement 3.0
- **4 个 Must-Fix**：Title/Abstract scope 过宽、SCS/BCS novelty 论证不充分、TOST margin 循环论证 + logit 分歧、页数违规
- **7 个 Should-Fix**：无有效 mitigation、FP8 CI 传播、Dim2 跨模型验证、unconstrained ablation 过强、DocRED power 不足、simulation 独立性、definitions 应入正文
- **Issue Tracker 已同步**（22 条活跃 issue）
- **视觉审查**：超时未完成
- **外部审稿**：未配置

报告已通过 `submit_review_report_to_research_director` 投递至 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 203

## Round 203

72 recorded events


### User

_source line 2387 · 2026-05-21T06:28:28.623214+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema-dag-extraction
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (via ARR May 2026)
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

_source line 2388 · 2026-05-21T06:28:34.440662+00:00_

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

_source line 2389 · 2026-05-21T06:28:34.492452+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2390 · 2026-05-21T06:28:41.620922+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2391 · 2026-05-21T06:28:41.621473+00:00_



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

_source line 2392 · 2026-05-21T06:28:44.636008+00:00_

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

_source line 2393 · 2026-05-21T06:28:45.791979+00:00_

{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (68 个)\n\n- **exp012_llama_8b_r2_exp2**: DONE (negative) — \n- **exp012_llama_8b_r2**: DONE (success) — \n- **exp006_interaction_2x2**: DONE (negative) — \n- **exp012_llama_awq**: DONE (killed) — \n- **exp012_llama_8b_r3**: DONE (failed) — \n- **exp012_llama_8b**: DONE (killed) — \n- **exp_fewrel_40rel_r3**: DONE (failed) — \n- **exp_fewrel_40rel_r2**: DONE (failed) — \n- **exp012_llama_fewnerd_r4**: DONE (failed) — \n- **exp012_llama_8b_fewnerd**: DONE (failed) — \n- **exp_fewrel_40rel**: DONE (failed) — \n- **exp012_llama_fewnerd_r3**: DONE (failed) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-19\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- prompt_sensitivity（准备中）\n- prompt_sensitivity_dry4（准备中）\n- prompt_sensitivity_dry3（准备中）\n- prompt_sensitivity_dry2（准备中）\n- prompt_sensitivity_dry（准备中）\n- exp_aggregation_monte_carlo（准备中）\n- exp_scs_name_def_ablation（准备中）\n- exp_fewrel_contamination_check（准备中）\n- exp017_gpt4o_mini_fewrel（准备中）\n- exp_cross_embedding_sensitivity（准备中）\n- …另有 2 项\n\n## 近期结论\n- **exp_gemini_flash_bcs_controlled** (success): BCS-accuracy negative correlation observed on open-weight models (Qwen3-32B, LLaMA) generalizes to proprietary API models. Gemini 2.5 Flash should show significant BCS gap on extreme-BCS batches at count 8 and count 16, confirming Dimension 2 is architecture-family-independent. ← 基于 exp_gemini_flash_cross_model\n- **exp_gemini_flash_cross_model** (success): The two-dimensional degradation pattern (count-related decline + confusability-related type confusion) generalizes beyond open-weight models to proprietary API models. Gemini 2.5 Flash should show: (1) monotonic RE accuracy decline with count, and (2) significant BCS-accuracy correlation on extreme batches. If confirmed, the pattern is architecture-family-independent (open
…[truncated 1331 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1155
}
```

</details>

---


### Tool call

_source line 2394 · 2026-05-21T06:28:45.792456+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 2395 · 2026-05-21T06:28:46.195191+00:00_

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
40	\item \textbf{Model coverage.} Primary experiments use a single model (Qwen3-32B); cross-model validation covers the core extreme-BCS setting but does not replicate all secondary analyses (error taxonomy, prompt sensitivity, TOST equivalence tests). Whether these secondary findings generalize beyond Qwen3-32B remains open; see Appendix~\ref{sec:appendix_cross_model_gemini} and Table~\ref{tab:cross_model_bcs} for detailed model-wise results.
41	
42	\item \textbf{Effect size and statistical design.} Pairwise SCS explains a small fraction of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\times$ BCS interaction is bounded on FewRel but nonzero on DocRED, partially confounded by BCS range restriction at higher counts (Appendix~\ref{sec:appendix_factorial}); logit-scale evidence remains inconclusive. DocRED count curves use 5 batches per level due to higher per-batch evaluation cost. BCS-controlled experiments use a single seed with greedy decoding; residual variance is small (Appendix~\ref{app:variance-decomposition}) but precise magnitudes may vary.
43	
44	\item \textbf{Task scope.} Format independence is confirmed
…[truncated 66915 chars]

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

_source line 2396 · 2026-05-21T06:28:54.576730+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
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

_source line 2397 · 2026-05-21T06:28:54.577141+00:00_



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

_source line 2398 · 2026-05-21T06:28:57.487985+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines"
  }
}
```

</details>

---


### Tool call

_source line 2399 · 2026-05-21T06:28:59.850048+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if paper PDF exists"
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
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if paper PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 2400 · 2026-05-21T06:29:00.102409+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf
PDF_EXISTS

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

_source line 2401 · 2026-05-21T06:29:00.102741+00:00_

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

_source line 2402 · 2026-05-21T06:29:00.153241+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex

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


### Tool result

_source line 2403 · 2026-05-21T06:29:08.542109+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"}]

Based on the search results, here's comprehensive information about the EMNLP 2026 Call for Papers and ARR submission guidelines:

## Overview

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and repro
…[truncated 1724 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 11054
}
```

</details>

---


### Tool call

_source line 2404 · 2026-05-21T06:29:14.868931+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format requirements page limit template anonymity"
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
    "query": "ACL Rolling Review 2026 submission format requirements page limit template anonymity"
  }
}
```

</details>

---


### Tool call

_source line 2405 · 2026-05-21T06:29:15.321261+00:00_

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

_source line 2406 · 2026-05-21T06:29:15.774203+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: type count and type confusability. We present what is, to our knowledge, the first controlled study isolating these factors across NER, RE, and event detection on four datasets. We quantify confusability via the Schema Confusability Score (SCS) and its batch-level aggregation, the Batch Confusability Score (BCS). Degradation operates along two dimensions with task-dependent effect structures: count-related recall decline (up to $-$49\,pp on DocRED 96-relation RE) and confusability-related type substitution. In RE, BCS explains 22--58\% of cross-batch accuracy variance (FewRel/DocRED), independent of output format (paired constrained/unconstrained comparison yields identical correlations); NER shows no batch-level BCS signal, as errors scatter across missed entities and boundary failures. Schema decomposition fails due to merge amplification (NER, ED) and routing failure (RE). Both dimensions replicate across four models spanning three architecture families (Qwen, LLaMA, Gemini; 8B--70B), two decoding formats, and four prompt designs.
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

_source line 2407 · 2026-05-21T06:29:15.824861+00:00_

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

_source line 2408 · 2026-05-21T06:29:16.277121+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance.} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \citep{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 49.5\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near-halving or worse. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \citep{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.
9	
10	We ask three questions. \textbf{RQ1}: Does type confusability independently predi
…[truncated 3233 chars]

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

_source line 2409 · 2026-05-21T06:29:16.277482+00:00_

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

_source line 2410 · 2026-05-21T06:29:16.729573+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \citep{instructuie-2023}, code-style schema encoding \citep{knowcoder-2024,codeie-2023}, annotation-guided extraction \citep{gollie-2024,adelie-2024}, schema-driven decoding \citep{slot-2025,oneke-2025}, and constrained JSON decoding \citep{json-schema-bench-2025,willard2023efficient}. For NER, methods include zero-shot decomposition \citep{xie-zeroshot-ner-2023,promptner-2023}, distillation \citep{uniner-2024}, bidirectional encoders \citep{gliner-2024,gliner2-2025}, and fine-grained entity typing \citep{gillick-2014-entity-typing}. For RE, recent work examines zero-shot relation triplet extraction via prompting \citep{relationprompt-2022}, constrained generative extraction \citep{josifoski-2022-genie}, revisits relation extraction in the LLM era \citep{wadhwa-re-llm-2023}, and zero-shot RE via shared embedding spaces \citep{boylan-2025-glirel}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability. \citet{wei-2023-chatie} reformulate zero-shot IE as multi-turn QA with ChatGPT but do not analyze schema-size effects.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \citep{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. LLM-PEE's union merge suffers the same precision collapse (0.56$\to$0.21; \S\ref{sec:sdgd}). In short, LLM-PEE ass
…[truncated 3785 chars]

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

_source line 2411 · 2026-05-21T06:29:16.780344+00:00_

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

_source line 2412 · 2026-05-21T06:29:16.781095+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \citep{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains and is suitable for cross-domain evaluation. We sample 1{,}000 test instances uniformly across test instances; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \citep{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). A held-out validation confirms SCS--confusion generalization across the split boundary (Appendix~\ref{app:scs-heldout-validation}). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \citep{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple senten
…[truncated 9032 chars]

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


### Tool result

_source line 2413 · 2026-05-21T06:29:21.299036+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format requirements page limit template anonymity"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"}]

I found comprehensive information about ACL Rolling Review 2026 submission format requirements. Here are the key details:

## Page Limits

The page limit is 4 pages for short papers and 8 pages for long papers, excluding the ethical considerations and limitations sections.

## Format Requirements

Submissions that do not conform to the required styles, including paper size, margin width, and font size restri
…[truncated 1016 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 6430
}
```

</details>

---


### Tool call

_source line 2414 · 2026-05-21T06:29:26.871110+00:00_

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

_source line 2415 · 2026-05-21T06:29:27.323393+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}). The pattern is stable across three seeds (max $\Delta = 10.7$\,pp, within 1\,SD; intra-batch variance exceeds inter-seed variance by ${>}$5$\times$; Appendix~\ref{app:variance-decomposition}). Formal trend analysis confirms monotonic RE decline (Jonckheere-Terpstra $J = 109{,}707$, $p < 0.001$). Count curves establish trend direction; magnitude estimation relies on the higher-powered BCS-controlled experiments (\S\ref{sec:bcs_controlled}).
10	
11	\subsection{Pairwise Confusability and Type Confusion}
12	\label{sec:pairwise}
13	
14	We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$) and correlate it with $\text{SCS}(t_i, t_j)$. Table~\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\% CIs.
15	
16	\begin{table}[t]
17	\centering
18	\small
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{llrrrrr}
21	\toprule
22	\textbf{Dataset} & \textbf{Embed.} & \textbf{$n$ pairs} & \textbf{$r$} & \textbf{$r^2$} & \text
…[truncated 10028 chars]

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

_source line 2416 · 2026-05-21T06:29:27.374077+00:00_

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

_source line 2417 · 2026-05-21T06:29:27.825931+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention is to partition the schema so confusable types never co-occur. We test \textbf{Schema-DAG-Guided Decomposition} (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches.
5	
6	\paragraph{NER and ED: merge amplification.}
7	All decomposition modes fall below the single-pass NER baseline (F1\,=\,0.445): SDGD obtains 0.251, random batching 0.320. The core failure is \emph{merge amplification}: presenting text $k$ times collapses precision (0.563$\to$0.210--0.249). MAVEN event detection replicates this (precision 0.287$\to$0.091; Appendix~\ref{sec:appendix_sdgd}).
8	
9	\paragraph{RE: routing failure.}
10	Oracle routing recovers accuracy (0.802 vs.\ 0.504 single-pass; Table~\ref{tab:batch_composition}), but confusability-aware grouping yields only +1.4\,pp over random ($p \approx 0.19$, n.s.). All practical routing strategies fall below the single-pass baseline (Appendix~\ref{sec:appendix_routing}).
11	

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

_source line 2418 · 2026-05-21T06:29:27.826274+00:00_

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

_source line 2419 · 2026-05-21T06:29:28.228141+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-dimensional decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). Approximate separability is confirmed on FewRel and DocRED (\S\ref{sec:multi_channel}); logit-scale evidence remains inconclusive. Both dimensions replicate across four models (8B--70B), two decoding formats, four prompt designs, and two RE datasets.
6	
7	\paragraph{Embedding similarity and format independence.}
8	SCS captures semantic proximity in LLMs' type-resolution space, amplifying from pairwise $R^2 = 1.3\%$ to batch-level 18--25\% via correlated aggregation (Appendix~\ref{app:aggregation-sim}). The BCS--performance relationship holds across all RE settings but not NER; a paired format comparison confirms format independence (Appendix~\ref{app:format-independence}). The task asymmetry reflects error-mode structure: RE errors concentrate in type substitutions \citep{tam-2024-let-me-speak}, whereas NER errors scatter across miss, boundary, and type modes \citep{schall-2025-hidden-cost}. SCS likely proxies deeper conceptual overlap persisting despite label renaming (Appendix~\ref{app:renaming}); we hypothesize high-SCS types intensify softmax competition---testable via logit-space analysis.
9	
10	\paragraph{Practical implications.}
11	For NER, reducing candidate types per prompt is the primary lever; for RE, we suggest flagging type pairs with SCS${}\,>\,0.85$ and monitoring batch-level BCS (typical gap 2--4\,pp in random batches; extreme-BCS contrasts reach 25--31\,pp).
12	
13	\paragraph{Conclusion.}
14	\label{sec:conclusion}
15	Training-free LLM extraction degrades along two separable dimensions---count-associated recall decline and confusability-associated type substitution---replicated on four models (8B--70B); decomposition fails via merge amplification and routing failure.
16	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 2420 · 2026-05-21T06:29:28.228499+00:00_

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

_source line 2421 · 2026-05-21T06:29:28.279107+00:00_

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
11	Yes. The Limitations section (after \S\ref{sec:discussion}) discusses model coverage, effect size and statistical design (including TOST equivalence), task scope, causal mechanism, data contamination, and domain/language scope.
12	
13	\item \textbf{Did you discuss any potential risks of your work?}
14	
15	Yes (Limitations). SCS/BCS may be misused as a standalone deployment criterion. Since they are proxies for confusability and do not capture domain-specific ambiguity or downstream harms, they should be used for diagnostic monitoring rather than automatic schema rejection or high-stakes deployment decisions.
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
33	Yes. Few-NERD \citep{fewnerd-2021}, FewRel \citep{fewrel-2018}, DocRED \citep{docred-2019}, MAVEN \citep{maven-2020}, Qwen3-32B \citep{qwen3-2025}, Meta-Llama-3.1-70B-Instruct and M
…[truncated 4760 chars]

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

_source line 2422 · 2026-05-21T06:29:42.563098+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
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

_source line 2423 · 2026-05-21T06:29:42.613792+00:00_



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

_source line 2424 · 2026-05-21T06:29:45.224630+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TodoWrite",
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
    "query": "select:TodoWrite",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2425 · 2026-05-21T06:29:45.275942+00:00_



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

_source line 2426 · 2026-05-21T06:29:53.960540+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'in_progress', 'activeForm': '进行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 派发外部审稿 + 视觉审查', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿（分配 Reviewer 任务）', 'status': 'pending', 'activeForm': '分配 Round 1 审稿任务'}, {'content': 'Step 2: 交叉分享（Reviewer 互评）', 'status': 'pending', 'activeForm': '进行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '进行收敛判断'}, {'content': 'Step 4: 汇总报告 + Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
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
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'in_progress', 'activeForm': '进行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 派发外部审稿 + 视觉审查', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿（分配 Reviewer 任务）', 'status': 'pending', 'activeForm': '分配 Round 1 审稿任务'}, {'content': 'Step 2: 交叉分享（Reviewer 互评）', 'status': 'pending', 'activeForm': '进行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '进行收敛判断'}, {'content': 'Step 4: 汇总报告 + Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2427 · 2026-05-21T06:29:53.961194+00:00_

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

_source line 2428 · 2026-05-21T06:29:55.617424+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
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
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 2429 · 2026-05-21T06:29:56.973016+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 1355
}
```

</details>

---


### Tool call

_source line 2430 · 2026-05-21T06:29:57.023852+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf 2>/dev/null | grep -i \"pages\" || echo \"pdfinfo not available\"",
  "description": "Check PDF page count"
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
    "command": "pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf 2>/dev/null | grep -i \"pages\" || echo \"pdfinfo not available\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 2431 · 2026-05-21T06:29:57.576349+00:00_

Pages:           27

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 2432 · 2026-05-21T06:29:57.626984+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "decisions.yaml",
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
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2433 · 2026-05-21T06:29:57.677687+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/decisions.yaml\", \"content\": \"_next_id: 69\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 16:10 UTC\\n  summary: 项目立项，MVP 验证方案：Experiment 2 (Confusability Controlled) 为核心验证实验\\n  rationale: 'IDEA_BRIEF 的核心假设是 type confusability 独立于 type count 驱动 LLM IE 质量下降。Experiment\\n    2（固定 count 变 BCS）是最直接的假设检验。Pass 标准: |r|≥0.3 且 p<0.05。ACE05 RE + Few-NERD 双数据集验证。ARR\\n    May 25 DDL（11天），MVP 需 1-2 天完成。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 16:15 UTC\\n  summary: 修正 MVP 统计设计：random samples 从 10 增至 25/档，加入 per-type solo baseline 控制变量，核心指标改为\\n    Δ(solo_F1 - batch_F1)\\n  rationale: Reviewer 指出 n=12 下 |r|=0.3 对应 p≈0.34，无法同时满足 |r|≥0.3 且 p<0.05。增至 25 random\\n    batches/档 → n≈54，|r|≥0.27 即可达 p<0.05。同时加入 solo F1 控制 type 固有难度，避免将\\\"类型本身难抽取\\\"误归因于\\\"confusability\\n    效应\\\"。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 23:11 UTC\\n  summary: MVP 分析方法从 Δ(solo-batch) 切换到 within-count Pearson r(F1, BCS)，pass 标准更新为\\n    |r|≥0.3 at fixed count\\n  rationale: Exp 1 发现 count curve 方向反转（F1 随 count 上升），根因是低 count 时模型过度 hallucinate（pred/gold=8x\\n    at count=1）。solo baseline 处于极端行为模式，Δ 被跨 count 行为差异污染。改为 within-count 对比更干净：同一\\n    count 下比较不同 BCS 的 F1，直接检验 confusability 独立效应。\\n  related_experiments:\\n  - exp_id: exp001_count_baseline\\n    role: evidence\\n    result: count curve reversed, hallucination at low count\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 23:31 UTC\\n  summary: MVP 主指标更新为 within-count r(recall, BCS)，F1 因 over-prediction confound 降为补充指标\\n  rationale: Exp 1 text-match 重评估发现：recall 单调下降（0.72→0.42，符合预期），precision 单调上升（0.11→0.52，over-prediction\\n    减少），F1 受 precision 主导而反转。within-count 分析中 precision confound 在同一 count 下近似恒定，F1\\n    仍可用；但 recall 更干净且直接反映 type confusion。WrongType 错误（text 正确但 type 错标）随 count 从 0\\n    升至 2434，直
…[truncated 1449 chars]

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

_source line 2434 · 2026-05-21T06:30:01.098238+00:00_

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

_source line 2435 · 2026-05-21T06:30:01.959787+00:00_

1	# Review Issues Tracker
2	# Updated: 2026-05-19 (All R22 fixes verified in v12)
3	
4	# ============================================================
5	# R22 CRITICAL — ALL RESOLVED
6	# ============================================================
7	
8	- id: R22-C1
9	  summary: "Title/Abstract scope overclaim: 'Information Extraction' 但 batch-level Dim2 仅 RE 成立"
10	  category: framing
11	  severity: critical
12	  status: resolved
13	  first_raised_round: 21
14	  last_seen_round: 22
15	  mentions:
16	    - {round: 21, reviewers: [R1, R2], note: "R21-W1: NER Dim2 batch-level null, Title IE 过宽"}
17	    - {round: 22, reviewers: [R2], note: "R2 Must-Fix N1。batch-level BCS 仅 RE (FewRel/DocRED) 成立，NER r≈0，MAVEN centrality confound。R1 部分 rebut：pairwise SCS 跨任务成立，batch-level 是聚合局限。交叉后共识：Abstract 需加 task-format qualifier。"}
18	  action_items:
19	    - {round: 22, action: "Abstract 重写：区分 pairwise (跨任务) vs batch-level (RE only)，加 task-dependent qualifier，标注数字来源条件", assigned_to: main_agent, status: done}
20	  resolution: "v12 Abstract 重写完成，区分 pairwise vs batch-level scope，加 task-dependent qualifier + format independence。"
21	  resolution_round: 22
22	
23	- id: R22-C2
24	  summary: "SCS/BCS novelty 不足，与 LLM-PEE partitioning criterion 一致"
25	  category: framing
26	  severity: critical
27	  status: resolved
28	  first_raised_round: 21
29	  last_seen_round: 22
30	  mentions:
31	    - {round: 21, reviewers: [R1, R2], note: "R21-C4: SCS 借自 LLM-PEE，novelty framing 不清晰"}
32	    - {round: 22, reviewers: [R2], note: "R2 Must-Fix N2。SCS=cosine sim, BCS=mean，无技术创新。'controlled framework' 作主贡献论证不充分。R1 rebut：方法论创新在实验范式非指标，22-58% R² 无法靠直觉预测。交叉后分歧保留。"}
33	  action_items:
34	    - {round: 22, action: "Intro+Discussion 强化 non-obvious findings (22-58% R², renaming 反直觉, NER null, few-shot 扩大 gap)", assigned_to: main_agent, status: done}
35	  resolution: "v12 Intro/Discussion 强化 non-obvious findings 作为核心贡献。"
36	  resolution_round: 22
37	
38	- id: R22-C3
39	  summary: "TOST ±3pp margin 循环论证 + logit-sca
…[truncated 11137 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 861
}
```

</details>

---


### Tool call

_source line 2436 · 2026-05-21T06:30:02.111085+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent/config.yaml 2>/dev/null | grep -A 5 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 2437 · 2026-05-21T06:30:02.211983+00:00_

NO_EXTERNAL_REVIEW_CONFIG

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

_source line 2438 · 2026-05-21T06:30:07.691346+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent/config.yaml 2>/dev/null | head -80",
  "description": "Read project config header"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read project config header"
  }
}
```

</details>

---


### Tool result

_source line 2439 · 2026-05-21T06:30:07.742048+00:00_

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

_source line 2440 · 2026-05-21T06:30:13.766930+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -name \"config.*\" -o -name \"*.yaml\" -maxdepth 3 2>/dev/null | head -20",
  "description": "Find config files"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -name \"config.*\" -o -name \"*.yaml\" -maxdepth 3 2>/dev/null | head -20",
    "description": "Find config files"
  }
}
```

</details>

---


### Tool result

_source line 2441 · 2026-05-21T06:30:13.817555+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/distill_tmp/iepile-2024.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/distill_tmp/uniner-2024.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/distill_tmp/familiarity-2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/distill_tmp/gollie-2024.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/distill_tmp/llm4ie-survey-2024.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/distill_tmp/zeroner-2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/distill_tmp/gliner-2024.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/distill_tmp/knowcoder-2024.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/distill_tmp/parse-2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/distill_tmp/cmas-ner-2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/distill_tmp/crossagentie-2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/distill_tmp/gliner2-2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/distill_tmp/guidex-2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/distill_tmp/dlisc-2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/distill_tmp/dee-2024.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/distill_tmp/llm-pee-2025.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/distill_tmp/self-prompting-re-2024.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/distill_tmp/lost-in-middle-2024.yam
…[truncated 215 chars]

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

_source line 2442 · 2026-05-21T06:30:17.734109+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/config.yaml 2>/dev/null | head -100 || find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -maxdepth 2 -name \"config.yaml\" 2>/dev/null",
  "description": "Find main project config"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/config.yaml 2>/dev/null | head -100 || find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -maxdepth 2 -name \"config.yaml\" 2>/dev/null",
    "description": "Find main project config"
  }
}
```

</details>

---


### Tool result

_source line 2443 · 2026-05-21T06:30:17.785592+00:00_

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


### Tool call

_source line 2444 · 2026-05-21T06:30:21.801480+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -maxdepth 1 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null; ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/*.yaml 2>/dev/null; cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config.yaml 2>/dev/null | head -50 || echo \"NO_CONFIG\"",
  "description": "Search for main config"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -maxdepth 1 -name \"*.yaml\" -o -name \"*.yml\" 2>/dev/null; ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/*.yaml 2>/dev/null; cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config.yaml 2>/dev/null | head -50 || echo \"NO_CONFIG\"",
    "description": "Search for main config"
  }
}
```

</details>

---


### Tool result

_source line 2445 · 2026-05-21T06:30:21.902702+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/workspace.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/workspace.yaml

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


### Tool call

_source line 2446 · 2026-05-21T06:30:25.618069+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/workspace.yaml /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ --include=\"*.yaml\" --include=\"*.yml\" 2>/dev/null | head -10 || echo \"NOT_FOUND\"",
  "description": "Search for external review config"
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
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/workspace.yaml /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ --include=\"*.yaml\" --include=\"*.yml\" 2>/dev/null | head -10 || echo \"NOT_FOUND\"",
    "description": "Search for external review config"
  }
}
```

</details>

---


### Tool result

_source line 2447 · 2026-05-21T06:30:25.719812+00:00_

(Bash completed with no output)

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


### Tool call

_source line 2448 · 2026-05-21T06:30:48.786891+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '进行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 派发外部审稿 + 视觉审查', 'status': 'in_progress', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿（分配 Reviewer 任务）', 'status': 'pending', 'activeForm': '分配 Round 1 审稿任务'}, {'content': 'Step 2: 交叉分享（Reviewer 互评）', 'status': 'pending', 'activeForm': '进行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '进行收敛判断'}, {'content': 'Step 4: 汇总报告 + Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
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
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '进行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 派发外部审稿 + 视觉审查', 'status': 'in_progress', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿（分配 Reviewer 任务）', 'status': 'pending', 'activeForm': '分配 Round 1 审稿任务'}, {'content': 'Step 2: 交叉分享（Reviewer 互评）', 'status': 'pending', 'activeForm': '进行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '进行收敛判断'}, {'content': 'Step 4: 汇总报告 + Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2449 · 2026-05-21T06:30:48.787383+00:00_

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

_source line 2450 · 2026-05-21T06:30:50.092433+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "schema-dag-extraction",
  "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "schema-dag-extraction",
    "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
  }
}
```

</details>

---


### Tool result

_source line 2451 · 2026-05-21T06:30:54.218101+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 4125
}
```

</details>

---


### Tool call

_source line 2452 · 2026-05-21T06:31:04.428415+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '进行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿（分配 Reviewer 任务）', 'status': 'in_progress', 'activeForm': '分配 Round 1 审稿任务'}, {'content': 'Step 2: 交叉分享（Reviewer 互评）', 'status': 'pending', 'activeForm': '进行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '进行收敛判断'}, {'content': 'Step 4: 汇总报告 + Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
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
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '进行资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.6-0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查'}, {'content': 'Step 1: Round 1 独立审稿（分配 Reviewer 任务）', 'status': 'in_progress', 'activeForm': '分配 Round 1 审稿任务'}, {'content': 'Step 2: 交叉分享（Reviewer 互评）', 'status': 'pending', 'activeForm': '进行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '进行收敛判断'}, {'content': 'Step 4: 汇总报告 + Issue Tracker + 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2453 · 2026-05-21T06:31:04.428813+00:00_

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

_source line 2454 · 2026-05-21T06:31:30.488430+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（via ACL Rolling Review May 2026 cycle）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，正文 8 页，参考文献不限，Limitations 和 Ethical Considerations 不计入页数（前提是不含过多额外内容）\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind（作者信息和自引不得暴露身份）\n- **附录规则**: 允许附录，参与审稿但不要求审稿人必须阅读\n- **Checklist**: Responsible NLP Research Checklist 必须包含\n\n### 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf`\n\n### 论文概要\n标题：How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n\n研究内容：训练免调 LLM 信息抽取随 schema 复杂度增长而退化，本文将退化因素分解为 type count（Dim1）和 type confusability（Dim2），提出 SCS/BCS 指标量化混淆度，在 NER/RE/ED 四个数据集上进行控制实验，并测试 schema decomposition 策略（SDGD）。\n\n### 你的审查侧重（方法严谨性 + 实验设计）\n\n请重点审查以下方面，给出具体意见（引用 Section/Table/Figure 编号）：\n\n1. **统计方法严谨性**：\n   - TOST 等价检验的 margin 选择是否合理（±3pp / ±2pp）？是否存在循环论证？\n   - Logit-scale 分析 inconclusive 如何影响主要结论？\n   - Bootstrap CI 方法是否适当？单种子+FP8 量化的方差处理是否充分？\n   - 多重比较问题的处理（Rothman 1990 免矫正论证）是否令人信服？\n\n2. **实验控制与因果推断**：\n   - BCS-controlled 实验能否真正隔离 confusability 与 count？有无遗漏的混淆变量？\n   - DocRED range restriction confound 的处理是否充分？\n   - Cross-model 验证是否足以支撑 \"architecture-independent\" 的 claim？\n   - Pair-to-batch aggregation simulation 的独立性假设是否站得住？\n\n3. **Effect size 与实际意义**：\n   - Typical-batch 2-4pp 的 BCS gap 是否具有实际意义？\n   - Pairwise r²=1.3-1.7% 是否过低？论文的 \"amplification\" 叙事是否令人信服？\n   - 负面结果（SDGD 失败、renaming 失败、few-shot 扩大 gap）是否充分分析了根因？\n\n4. **Reproducibility**：\n   - 实验细节是否足够复现？（batch 构造、greedy search for extreme batches、评估协议）\n   - Cross-seed variance decomposition 是否支持单种子设计的可靠性？\n\n请以 **Must-Fix / Should-Fix / Minor** 三级分类你的意见，并给出初步 Overall Assessment 评分（参考 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。"
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
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（via ACL Rolling Review May 2026 cycle）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，正文 8 页，参考文献不限，Limitations 和 Ethical Considerations 不计入页数（前提是不含过多额外内容）\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind（作者信息和自引不得暴露身份）\n- **附录规则**: 允许附录，参与审稿但不要求审稿人必须阅读\n- **Checklist**: Responsible NLP Research Checklist 必须包含\n\n### 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf`\n\n### 论文概要\n标题：How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n\n研究内容：训练免调 LLM 信息抽取随 schema 复杂度增长而退化，本文将退化因素分解为 type count（Dim1）和 type confusability（Dim2），提出 SCS/BCS 指标量化混淆度，在 NER/RE/ED 四个数据集上进行控制实验，并测试 schema decomposition 策略（SDGD）。\n\n### 你的审查侧重（方法严谨性 + 实验设计）\n\n请重点审查以下方面，给出具体意见（引用 Section/Table/Figure 编号）：\n\n1. **统计方法严谨性**：\n   - TOST 等价检验的 margin 选择是否合理（±3pp / ±2pp）？是否存在循环论证？\n   - Logit-scale 分析 inconclusive 如何影响主要结论？\n   - Bootstrap CI 方法是否适当？单种子+FP8 量化的方差处理是否充分？\n   - 多重比较问题的处理（Rothman 1990 免矫正论证）是否令人信服？\n\n2. **实验控制与因果推断**：\n   - BCS-controlled 实验能否真正隔离 confusability 与 count？有无遗漏的混淆变量？\n   - DocRED range restriction confound 的处理是否充分？\n   - Cross-model 验证是否足以支撑 \"architecture-independent\" 的 claim？\n   - Pair-to-batch aggregation simulation 的独立性假设是否站得住？\n\n3. **Effect size 与实际意义**：\n   - Typical-batch 2-4pp 的 BCS gap 是否具有实际意义？\n   - Pairwise r²=1.3-1.7% 是否过低？论文的 \"amplification\" 叙事是否令人信服？\n   - 负面结果（SDGD 失败、renaming 失败、few-shot 扩大 gap）是否充分分析了根因？\n\n4. **Reproducibility**：\n   - 实验细节是否足够复现？（batch 构造、greedy search for extreme batches、评估协议）\n   - Cross-seed variance decomposition 是否支持单种子设计的可靠性？\n\n请以 **Must-Fix / Should-Fix / Minor** 三级分类你的意见，并给出初步 Overall Assessment 评分（参考 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。"
  }
}
```

</details>

---


### Tool result

_source line 2455 · 2026-05-21T06:31:47.675517+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17187
}
```

</details>

---


### Tool call

_source line 2456 · 2026-05-21T06:31:47.876617+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 格式）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（via ACL Rolling Review May 2026 cycle）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，正文 8 页，参考文献不限，Limitations 和 Ethical Considerations 不计入页数（前提是不含过多额外内容）\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind（作者信息和自引不得暴露身份）\n- **附录规则**: 允许附录，参与审稿但不要求审稿人必须阅读\n- **Checklist**: Responsible NLP Research Checklist 必须包含\n\n### 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf`\n\n### 论文概要\n标题：How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n\n研究内容：训练免调 LLM 信息抽取随 schema 复杂度增长而退化，本文将退化因素分解为 type count（Dim1）和 type confusability（Dim2），提出 SCS/BCS 指标量化混淆度，在 NER/RE/ED 四个数据集上进行控制实验，并测试 schema decomposition 策略（SDGD）。\n\n### 你的审查侧重（新颖性 + 完整性 + 格式）\n\n请重点审查以下方面，给出具体意见（引用 Section/Table/Figure 编号）：\n\n1. **新颖性（Novelty）**：\n   - SCS/BCS 的定义是 pairwise cosine similarity of type name embeddings，与 LLM-PEE 的 partitioning criterion 形式一致——论文声称贡献在于 \"controlled experimental framework\" 而非指标本身，这是否构成足够的新颖性？\n   - \"First controlled study isolating count and confusability\" 的 claim 是否成立？有无被遗漏的 prior work？\n   - 负面结果（SDGD/renaming/few-shot 全部失败）的学术价值如何？\n\n2. **Related Work 覆盖**：\n   - 是否遗漏了重要相关工作？特别关注：\n     * Schema complexity in other NLP tasks（dialogue, QA, etc.）\n     * Embedding-based type discrimination（metric learning, zero-shot classification）\n     * Recent concurrent work on LLM IE scaling\n   - 与 LLM-PEE 的区分是否清晰且公正？\n\n3. **写作质量**：\n   - 论文结构是否合理？信息密度是否过高？\n   - Abstract 的 scope claim 是否与实验证据匹配？\n   - 因果语言的使用是否恰当（\"predicts\" vs \"causes\"）？\n   - 术语定义是否清晰一致？\n\n4. **格式合规性（严格检查）**：\n   - **页数**：正文 body（Section 1 到 Discussion/Conclusion 结束）是否 ≤ 8 页？\n   - **匿名性**：是否有任何泄露作者身份的内容（自引、致谢、代码链接、数据链接）？\n   - **Limitations section**：是否存在且内容充分？\n   - **Responsible NLP Research Checklist**：是否完整且诚实填写？\n   - **引用格式**：是否使用 `\\citep`/`\\citet` 且格式一致？\n   - **图表**：标题是否自含、是否有交叉引用、字号是否可读？\n\n5. **Missing References**：\n   - 搜索并列出论文可能遗漏的重要引用（用 web_search 搜索 2025-2026 年相关工作）\n\n请以 **Must-Fix / Should-Fix / Minor** 三级分类你的意见，并给出初步 Overall Assessment 评分（参考 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。"
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
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 格式）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（via ACL Rolling Review May 2026 cycle）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，正文 8 页，参考文献不限，Limitations 和 Ethical Considerations 不计入页数（前提是不含过多额外内容）\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind（作者信息和自引不得暴露身份）\n- **附录规则**: 允许附录，参与审稿但不要求审稿人必须阅读\n- **Checklist**: Responsible NLP Research Checklist 必须包含\n\n### 论文路径\n- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf`\n\n### 论文概要\n标题：How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n\n研究内容：训练免调 LLM 信息抽取随 schema 复杂度增长而退化，本文将退化因素分解为 type count（Dim1）和 type confusability（Dim2），提出 SCS/BCS 指标量化混淆度，在 NER/RE/ED 四个数据集上进行控制实验，并测试 schema decomposition 策略（SDGD）。\n\n### 你的审查侧重（新颖性 + 完整性 + 格式）\n\n请重点审查以下方面，给出具体意见（引用 Section/Table/Figure 编号）：\n\n1. **新颖性（Novelty）**：\n   - SCS/BCS 的定义是 pairwise cosine similarity of type name embeddings，与 LLM-PEE 的 partitioning criterion 形式一致——论文声称贡献在于 \"controlled experimental framework\" 而非指标本身，这是否构成足够的新颖性？\n   - \"First controlled study isolating count and confusability\" 的 claim 是否成立？有无被遗漏的 prior work？\n   - 负面结果（SDGD/renaming/few-shot 全部失败）的学术价值如何？\n\n2. **Related Work 覆盖**：\n   - 是否遗漏了重要相关工作？特别关注：\n     * Schema complexity in other NLP tasks（dialogue, QA, etc.）\n     * Embedding-based type discrimination（metric learning, zero-shot classification）\n     * Recent concurrent work on LLM IE scaling\n   - 与 LLM-PEE 的区分是否清晰且公正？\n\n3. **写作质量**：\n   - 论文结构是否合理？信息密度是否过高？\n   - Abstract 的 scope claim 是否与实验证据匹配？\n   - 因果语言的使用是否恰当（\"predicts\" vs \"causes\"）？\n   - 术语定义是否清晰一致？\n\n4. **格式合规性（严格检查）**：\n   - **页数**：正文 body（Section 1 到 Discussion/Conclusion 结束）是否 ≤ 8 页？\n   - **匿名性**：是否有任何泄露作者身份的内容（自引、致谢、代码链接、数据链接）？\n   - **Limitations section**：是否存在且内容充分？\n   - **Responsible NLP Research Checklist**：是否完整且诚实填写？\n   - **引用格式**：是否使用 `\\citep`/`\\citet` 且格式一致？\n   - **图表**：标题是否自含、是否有交叉引用、字号是否可读？\n\n5. **Missing References**：\n   - 搜索并列出论文可能遗漏的重要引用（用 web_search 搜索 2025-2026 年相关工作）\n\n请以 **Must-Fix / Should-Fix / Minor** 三级分类你的意见，并给出初步 Overall Assessment 评分（参考 EMNLP 2026 ARR 评分标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。"
  }
}
```

</details>

---


### Tool result

_source line 2457 · 2026-05-21T06:31:49.691572+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1814
}
```

</details>

---


### Assistant

_source line 2458 · 2026-05-21T06:31:54.159218+00:00_

Round 1 任务已分配：
- **Reviewer 1**（方法严谨性 + 实验设计）→ 已派发
- **Reviewer 2**（新颖性 + 完整性 + 格式）→ 已派发
- **视觉审查 Agent** → 已派发（并行，不阻塞）
- **外部审稿** → 未配置，跳过

等待两位 Reviewer 返回 Round 1 初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 204

## Round 204

2 recorded events


### User

_source line 2459 · 2026-05-21T06:33:36.936480+00:00_

[Reviewer 1 审稿结果]:
继续阅读最后几页附录。

---

[Reviewer 2 审稿结果]:
开始并行执行：搜索 reviewer guidelines、渲染论文 PDF、验证引用。

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

_source line 2460 · 2026-05-21T06:33:58.182457+00:00_

两位 Reviewer 仍在审稿中，尚未提交完整审稿意见。

- **Reviewer 1**：正在阅读附录最后几页，初审接近完成
- **Reviewer 2**：刚启动并行任务（venue guidelines 搜索、PDF 渲染、引用验证），初审进行中

等待两位 Reviewer 提交完整审稿结果后，进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 205

## Round 205

64 recorded events


### User

_source line 2461 · 2026-05-21T12:16:21.187228+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema-dag-extraction
- 论文路径: projects/schema-dag-extraction/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (via ARR May 2026)
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

_source line 2462 · 2026-05-21T12:16:27.929101+00:00_

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

_source line 2463 · 2026-05-21T12:16:28.030371+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2464 · 2026-05-21T12:16:37.621546+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues,read_project_file",
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
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,get_external_review_status,get_visual_check_status,request_external_review,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2465 · 2026-05-21T12:16:37.673214+00:00_

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

_source line 2466 · 2026-05-21T12:16:42.052178+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2467 · 2026-05-21T12:16:42.102781+00:00_



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

_source line 2468 · 2026-05-21T12:16:46.220249+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
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

_source line 2469 · 2026-05-21T12:16:46.270890+00:00_



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

_source line 2470 · 2026-05-21T12:16:49.643061+00:00_

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

_source line 2471 · 2026-05-21T12:16:49.743984+00:00_

No matching deferred tools found

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

_source line 2472 · 2026-05-21T12:16:55.996700+00:00_

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

_source line 2473 · 2026-05-21T12:16:57.403235+00:00_

{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (68 个)\n\n- **exp012_llama_8b_r2_exp2**: DONE (negative) — \n- **exp012_llama_8b_r2**: DONE (success) — \n- **exp006_interaction_2x2**: DONE (negative) — \n- **exp012_llama_awq**: DONE (killed) — \n- **exp012_llama_8b_r3**: DONE (failed) — \n- **exp012_llama_8b**: DONE (killed) — \n- **exp_fewrel_40rel_r3**: DONE (failed) — \n- **exp_fewrel_40rel_r2**: DONE (failed) — \n- **exp012_llama_fewnerd_r4**: DONE (failed) — \n- **exp012_llama_8b_fewnerd**: DONE (failed) — \n- **exp_fewrel_40rel**: DONE (failed) — \n- **exp012_llama_fewnerd_r3**: DONE (failed) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-19\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- prompt_sensitivity（准备中）\n- prompt_sensitivity_dry4（准备中）\n- prompt_sensitivity_dry3（准备中）\n- prompt_sensitivity_dry2（准备中）\n- prompt_sensitivity_dry（准备中）\n- exp_aggregation_monte_carlo（准备中）\n- exp_scs_name_def_ablation（准备中）\n- exp_fewrel_contamination_check（准备中）\n- exp017_gpt4o_mini_fewrel（准备中）\n- exp_cross_embedding_sensitivity（准备中）\n- …另有 2 项\n\n## 近期结论\n- **exp_gemini_flash_bcs_controlled** (success): BCS-accuracy negative correlation observed on open-weight models (Qwen3-32B, LLaMA) generalizes to proprietary API models. Gemini 2.5 Flash should show significant BCS gap on extreme-BCS batches at count 8 and count 16, confirming Dimension 2 is architecture-family-independent. ← 基于 exp_gemini_flash_cross_model\n- **exp_gemini_flash_cross_model** (success): The two-dimensional degradation pattern (count-related decline + confusability-related type confusion) generalizes beyond open-weight models to proprietary API models. Gemini 2.5 Flash should show: (1) monotonic RE accuracy decline with count, and (2) significant BCS-accuracy correlation on extreme batches. If confirmed, the pattern is architecture-family-independent (open
…[truncated 1331 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool call

_source line 2474 · 2026-05-21T12:16:57.403761+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 2475 · 2026-05-21T12:16:58.358631+00:00_

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
40	\item \textbf{Model coverage.} Primary experiments use a single model (Qwen3-32B); cross-model validation covers the core extreme-BCS setting but does not replicate all secondary analyses (error taxonomy, prompt sensitivity, TOST equivalence tests). Whether these secondary findings generalize beyond Qwen3-32B remains open; see Appendix~\ref{sec:appendix_cross_model_gemini} and Table~\ref{tab:cross_model_bcs} for detailed model-wise results.
41	
42	\item \textbf{Effect size and statistical design.} Pairwise SCS explains a small fraction of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\times$ BCS interaction is bounded on FewRel but nonzero on DocRED, partially confounded by BCS range restriction at higher counts (Appendix~\ref{sec:appendix_factorial}); logit-scale evidence remains inconclusive. DocRED count curves use 5 batches per level due to higher per-batch evaluation cost. BCS-controlled experiments use a single seed with greedy decoding; residual variance is small (Appendix~\ref{app:variance-decomposition}) but precise magnitudes may vary.
43	
44	\item \textbf{Task scope.} Format independence is confirmed
…[truncated 66915 chars]

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

_source line 2476 · 2026-05-21T12:16:58.359106+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
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
    "query": "EMNLP 2026 call for papers submission guidelines ARR",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool call

_source line 2477 · 2026-05-21T12:16:59.364382+00:00_

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

_source line 2478 · 2026-05-21T12:16:59.716952+00:00_

1	# Review Issues Tracker
2	# Updated: 2026-05-19 (All R22 fixes verified in v12)
3	
4	# ============================================================
5	# R22 CRITICAL — ALL RESOLVED
6	# ============================================================
7	
8	- id: R22-C1
9	  summary: "Title/Abstract scope overclaim: 'Information Extraction' 但 batch-level Dim2 仅 RE 成立"
10	  category: framing
11	  severity: critical
12	  status: resolved
13	  first_raised_round: 21
14	  last_seen_round: 22
15	  mentions:
16	    - {round: 21, reviewers: [R1, R2], note: "R21-W1: NER Dim2 batch-level null, Title IE 过宽"}
17	    - {round: 22, reviewers: [R2], note: "R2 Must-Fix N1。batch-level BCS 仅 RE (FewRel/DocRED) 成立，NER r≈0，MAVEN centrality confound。R1 部分 rebut：pairwise SCS 跨任务成立，batch-level 是聚合局限。交叉后共识：Abstract 需加 task-format qualifier。"}
18	  action_items:
19	    - {round: 22, action: "Abstract 重写：区分 pairwise (跨任务) vs batch-level (RE only)，加 task-dependent qualifier，标注数字来源条件", assigned_to: main_agent, status: done}
20	  resolution: "v12 Abstract 重写完成，区分 pairwise vs batch-level scope，加 task-dependent qualifier + format independence。"
21	  resolution_round: 22
22	
23	- id: R22-C2
24	  summary: "SCS/BCS novelty 不足，与 LLM-PEE partitioning criterion 一致"
25	  category: framing
26	  severity: critical
27	  status: resolved
28	  first_raised_round: 21
29	  last_seen_round: 22
30	  mentions:
31	    - {round: 21, reviewers: [R1, R2], note: "R21-C4: SCS 借自 LLM-PEE，novelty framing 不清晰"}
32	    - {round: 22, reviewers: [R2], note: "R2 Must-Fix N2。SCS=cosine sim, BCS=mean，无技术创新。'controlled framework' 作主贡献论证不充分。R1 rebut：方法论创新在实验范式非指标，22-58% R² 无法靠直觉预测。交叉后分歧保留。"}
33	  action_items:
34	    - {round: 22, action: "Intro+Discussion 强化 non-obvious findings (22-58% R², renaming 反直觉, NER null, few-shot 扩大 gap)", assigned_to: main_agent, status: done}
35	  resolution: "v12 Intro/Discussion 强化 non-obvious findings 作为核心贡献。"
36	  resolution_round: 22
37	
38	- id: R22-C3
39	  summary: "TOST ±3pp margin 循环论证 + logit-sca
…[truncated 11137 chars]

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

_source line 2479 · 2026-05-21T12:16:59.717344+00:00_

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

_source line 2480 · 2026-05-21T12:17:05.702460+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026:

## General Submission Information

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational t
…[truncated 1042 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 7343
}
```

</details>

---


### Tool result

_source line 2481 · 2026-05-21T12:17:05.703364+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/memory.md\", \"content\": \"# Memory — schema-dag-extraction\\n\\n## DocRED expanded: interaction reversed, R² increased (2026-05-19)\\n- 原 n=5 per condition: interaction=+5.7pp CI[-1.6, 13.0], R²=0.525 (count16)\\n- 扩展 n=15 per condition (n=55 per count level): interaction=-9.4pp CI[-12.9, -6.0], R²=0.653 (count16), R²=0.614 (count32)\\n- **方向翻转**: 从不确定(+5.7pp, CI 含零)变为确定 sub-additive(-9.4pp, CI 不含零)\\n- BCS effect 从 -25.0pp (count16) 衰减到 -15.7pp (count32)，符合 floor compression\\n- **教训**: 小样本(n=5)的交互估计极不稳定，符号都可以翻转\\n- 论文范围从 \\\"22-53%\\\" 更新为 \\\"22-65%\\\"\\n\\n## MAVEN SDGD: merge amplification 跨任务确认 (2026-05-19)\\n- Single-pass F1=0.207 > SDGD-zero F1=0.123 > random-batch F1=0.111\\n- Precision collapse 0.287→0.091 (-19.6pp), pred_count inflation 3.7×\\n- 与 Few-NERD NER 一致：分解策略在所有 span-based tasks 上因 merge amplification 失败\\n- SDGD-zero 略优于 random (+1.2pp F1)，但均远低于 single-pass\\n\\n## exp_schema_intervention: renaming 不是有效干预手段 (2026-05-17, negative)\\n- Renaming 降低两组 accuracy：high-BCS -8.83pp, low-BCS -2.96pp (both p<0.001)\\n- Interaction 显著 (-5.88pp, p<0.001)：high-BCS 受损更大，但方向是 renaming 损害而非改善\\n- 根因：LLM 对 original type names 有 strong prior，renaming 引入 label unfamiliarity confound\\n- Solo sanity check 11/12 通过，但 multi-type batch 中 compound effect 出现 (r=-0.625)\\n- **教训**：post-hoc renaming 无法分离 SCS 降低效果与 label unfamiliarity，不可用作因果干预\\n- D059 (Greedy auto-renaming) 基于相同逻辑，也已停止\\n\\n## TUM proxy 不是运行中的服务 (2026-05-17)\\n- TUM 是飞书 key 收集机制，不是 API proxy server\\n- localhost:8001 没有进程监听\\n- `tum_` 前缀的 token 不是有效的 Google/OpenAI API key\\n- 本机能直连 Google API（需要真实 Gemini key, 格式 AIza...）\\n- **教训**：API 实验前必须先验证 (a) proxy 是否运行 (b) key 格式是否匹配目标 API\\n\\n## Q3 held-out validation: FewRel val-origin SCS-confusion (2026-05-17, CORRECTED)\\n- 从 80-type confusion matrix 提取 16 val-origin types 的 C(16,2)=120 pairs\\n- 16 val types 与 64 train types
…[truncated 2866 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5986
}
```

</details>

---


### Tool call

_source line 2482 · 2026-05-21T12:17:46.601188+00:00_

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


### Tool call

_source line 2483 · 2026-05-21T12:17:46.653090+00:00_

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


### Tool call

_source line 2484 · 2026-05-21T12:17:46.653557+00:00_

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


### Tool call

_source line 2485 · 2026-05-21T12:17:46.653856+00:00_

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


### Tool call

_source line 2486 · 2026-05-21T12:17:46.654092+00:00_

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


### Tool call

_source line 2487 · 2026-05-21T12:17:46.654307+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission format page limit template anonymity ARR May 2026"
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
    "query": "EMNLP 2026 submission format page limit template anonymity ARR May 2026"
  }
}
```

</details>

---


### Tool result

_source line 2488 · 2026-05-21T12:17:46.654541+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: type count and type confusability. We present what is, to our knowledge, the first controlled study isolating these factors across NER, RE, and event detection on four datasets. We quantify confusability via the Schema Confusability Score (SCS) and its batch-level aggregation, the Batch Confusability Score (BCS). Degradation operates along two dimensions with task-dependent effect structures: count-related recall decline (up to $-$49\,pp on DocRED 96-relation RE) and confusability-related type substitution. In RE, BCS explains 22--58\% of cross-batch accuracy variance (FewRel/DocRED), independent of output format (paired constrained/unconstrained comparison yields virtually identical correlations); NER shows no batch-level BCS signal, as errors scatter across missed entities and boundary failures. Schema decomposition fails due to merge amplification (NER, ED) and routing failure (RE). Both dimensions replicate across four models spanning three architecture families (Qwen, LLaMA, Gemini; 8B--70B), two decoding formats, and five prompt designs.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 53
}
```

</details>

---


### Tool result

_source line 2489 · 2026-05-21T12:17:46.655900+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance.} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \citep{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near-halving or worse. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \citep{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.
9	
10	We ask three questions. \textbf{RQ1}: Does type confusability independently predi
…[truncated 3233 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 2
}
```

</details>

---


### Tool result

_source line 2490 · 2026-05-21T12:17:46.656541+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \citep{instructuie-2023}, code-style schema encoding \citep{knowcoder-2024,codeie-2023}, annotation-guided extraction \citep{gollie-2024,adelie-2024}, schema-driven decoding \citep{slot-2025,oneke-2025}, and constrained JSON decoding \citep{json-schema-bench-2025,willard2023efficient}. For NER, methods include zero-shot decomposition \citep{xie-zeroshot-ner-2023,promptner-2023}, distillation \citep{uniner-2024}, bidirectional encoders \citep{gliner-2024,gliner2-2025}, and fine-grained entity typing \citep{gillick-2014-entity-typing}. For RE, recent work examines zero-shot relation triplet extraction via prompting \citep{relationprompt-2022}, constrained generative extraction \citep{josifoski-2022-genie}, revisits relation extraction in the LLM era \citep{wadhwa-re-llm-2023}, and zero-shot RE via shared embedding spaces \citep{boylan-2025-glirel}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability. \citet{wei-2023-chatie} reformulate zero-shot IE as multi-turn QA with ChatGPT but do not analyze schema-size effects.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \citep{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. LLM-PEE's union merge suffers the same precision collapse (0.56$\to$0.21; \S\ref{sec:sdgd}). In short, LLM-PEE ass
…[truncated 3785 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 2
}
```

</details>

---


### Tool result

_source line 2491 · 2026-05-21T12:17:46.657007+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \citep{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains and is suitable for cross-domain evaluation. We sample 1{,}000 instances uniformly from the test set; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \citep{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). A held-out validation confirms SCS--confusion generalization across the split boundary (Appendix~\ref{app:scs-heldout-validation}). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \citep{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We s
…[truncated 9023 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 3
}
```

</details>

---


### Tool result

_source line 2492 · 2026-05-21T12:17:46.657498+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}). The pattern is stable across three seeds (max $\Delta = 10.7$\,pp, within 1\,SD; intra-batch variance exceeds inter-seed variance by ${>}$5$\times$; Appendix~\ref{app:variance-decomposition}). Formal trend analysis confirms monotonic RE decline (Jonckheere-Terpstra $J = 109{,}707$, $p < 0.001$). Count curves establish trend direction; magnitude estimation relies on the higher-powered BCS-controlled experiments (\S\ref{sec:bcs_controlled}).
10	
11	\subsection{Pairwise Confusability and Type Confusion}
12	\label{sec:pairwise}
13	
14	We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$) and correlate it with $\text{SCS}(t_i, t_j)$. Table~\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\% CIs.
15	
16	\begin{table}[t]
17	\centering
18	\small
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{llrrrrr}
21	\toprule
22	\textbf{Dataset} & \textbf{Embed.} & \textbf{$n$ pairs} & \textbf{$r$} & \textbf{$r^2$} & \text
…[truncated 10028 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 3
}
```

</details>

---


### Tool result

_source line 2493 · 2026-05-21T12:17:53.797481+00:00_

Web search results for query: "EMNLP 2026 submission format page limit template anonymity ARR May 2026"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"EMNLP 2026 on X: \"Here is more precise submission policy. For full details, please check the latest CFP on our website! https://t.co/6dttoXBIT9 https://t.co/ta6IuAjIVm\" / X","url":"https://x.com/emnlpmeeting/status/2047977818928320807"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"GitHub - acl-org/emnlp-2026: Repository for the EMNLP 2026 conference · GitHub","url":"https://github.com/acl-org/emnlp-2026"}]

Based on the search results, here is information about EMNLP 2026 submission format, guidelines, and ARR May 2026:

## Submission Format & Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers.

## Templates

EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences. EMNLP uses the ACL style files available at git
…[truncated 751 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 7143
}
```

</details>

---


### Tool call

_source line 2494 · 2026-05-21T12:18:00.615576+00:00_

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

_source line 2495 · 2026-05-21T12:18:01.519629+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention is to partition the schema so confusable types never co-occur. We test \textbf{Schema-DAG-Guided Decomposition} (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches.
5	
6	\paragraph{NER and ED: merge amplification.}
7	All decomposition modes fall below the single-pass NER baseline (F1\,=\,0.445): SDGD obtains 0.251, random batching 0.320. The core failure is \emph{merge amplification}: presenting text $k$ times collapses precision (0.563$\to$0.210--0.249). MAVEN event detection replicates this (precision 0.287$\to$0.091; Appendix~\ref{sec:appendix_sdgd}).
8	
9	\paragraph{RE: routing failure.}
10	Oracle routing recovers accuracy (0.802 vs.\ 0.504 single-pass; Table~\ref{tab:batch_composition}), but confusability-aware grouping yields only +1.4\,pp over random ($p \approx 0.19$, n.s.). All practical routing strategies fall below the single-pass baseline (Appendix~\ref{sec:appendix_routing}).
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 2496 · 2026-05-21T12:18:01.570289+00:00_

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

_source line 2497 · 2026-05-21T12:18:01.672046+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-dimensional decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). Approximate separability is confirmed on FewRel and DocRED (\S\ref{sec:multi_channel}); logit-scale evidence remains inconclusive. Both dimensions replicate across four models from three architecture families (8B--70B open-weight; Gemini 2.5 Flash via API), two decoding formats, five prompt designs, and two RE datasets.
6	
7	\paragraph{Embedding similarity and format independence.}
8	SCS captures semantic proximity in LLMs' type-resolution space, amplifying from pairwise $R^2 = 1.3\%$ to batch-level 22--58\% via correlated aggregation (Appendix~\ref{app:aggregation-sim}). The BCS--performance relationship holds across all RE settings but not NER; a paired format comparison confirms format independence (Appendix~\ref{app:format-independence}). The task asymmetry reflects error-mode structure: RE errors concentrate in type substitutions \citep{tam-2024-let-me-speak}, whereas NER errors scatter across miss, boundary, and type modes \citep{schall-2025-hidden-cost}. SCS likely proxies deeper conceptual overlap persisting despite label renaming (Appendix~\ref{app:renaming}); we hypothesize high-SCS types intensify softmax competition---testable via logit-space analysis.
9	
10	\paragraph{Practical implications.}
11	For NER, reducing candidate types per prompt is the primary lever; for RE, we suggest flagging type pairs with SCS${}\,>\,0.85$ and monitoring batch-level BCS (typical gap 2--4\,pp in random batches; extreme-BCS contrasts reach 25--31\,pp).
12	
13	\paragraph{Conclusion.}
14	\label{sec:conclusion}
15	Training-free LLM extraction degrades along two separable dimensions---count-associated recall decline and confusability-associated type substitution---replicated on four models from three architecture families (8B-
…[truncated 113 chars]

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

_source line 2498 · 2026-05-21T12:18:01.672513+00:00_

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

_source line 2499 · 2026-05-21T12:18:01.924854+00:00_

{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (68 个)\n\n- **exp012_llama_8b_r2_exp2**: DONE (negative) — \n- **exp012_llama_8b_r2**: DONE (success) — \n- **exp006_interaction_2x2**: DONE (negative) — \n- **exp012_llama_awq**: DONE (killed) — \n- **exp012_llama_8b_r3**: DONE (failed) — \n- **exp012_llama_8b**: DONE (killed) — \n- **exp_fewrel_40rel_r3**: DONE (failed) — \n- **exp_fewrel_40rel_r2**: DONE (failed) — \n- **exp012_llama_fewnerd_r4**: DONE (failed) — \n- **exp012_llama_8b_fewnerd**: DONE (failed) — \n- **exp_fewrel_40rel**: DONE (failed) — \n- **exp012_llama_fewnerd_r3**: DONE (failed) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-19\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- prompt_sensitivity（准备中）\n- prompt_sensitivity_dry4（准备中）\n- prompt_sensitivity_dry3（准备中）\n- prompt_sensitivity_dry2（准备中）\n- prompt_sensitivity_dry（准备中）\n- exp_aggregation_monte_carlo（准备中）\n- exp_scs_name_def_ablation（准备中）\n- exp_fewrel_contamination_check（准备中）\n- exp017_gpt4o_mini_fewrel（准备中）\n- exp_cross_embedding_sensitivity（准备中）\n- …另有 2 项\n\n## 近期结论\n- **exp_gemini_flash_bcs_controlled** (success): BCS-accuracy negative correlation observed on open-weight models (Qwen3-32B, LLaMA) generalizes to proprietary API models. Gemini 2.5 Flash should show significant BCS gap on extreme-BCS batches at count 8 and count 16, confirming Dimension 2 is architecture-family-independent. ← 基于 exp_gemini_flash_cross_model\n- **exp_gemini_flash_cross_model** (success): The two-dimensional degradation pattern (count-related decline + confusability-related type confusion) generalizes beyond open-weight models to proprietary API models. Gemini 2.5 Flash should show: (1) monotonic RE accuracy decline with count, and (2) significant BCS-accuracy correlation on extreme batches. If confirmed, the pattern is architecture-family-independent (open
…[truncated 1331 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 2500 · 2026-05-21T12:18:08.553380+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -name \"*.yaml\" -path \"*/agent/*\" 2>/dev/null | head -5",
  "description": "Find project config yaml files"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -name \"*.yaml\" -path \"*/agent/*\" 2>/dev/null | head -5",
    "description": "Find project config yaml files"
  }
}
```

</details>

---


### Tool result

_source line 2501 · 2026-05-21T12:18:09.005656+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2502 · 2026-05-21T12:18:09.508125+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
  "pages": "1-10"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
    "pages": "1-10"
  }
}
```

</details>

---


### Tool call

_source line 2503 · 2026-05-21T12:18:09.660125+00:00_

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

_source line 2504 · 2026-05-21T12:18:09.712137+00:00_

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
11	Yes. The Limitations section (after \S\ref{sec:discussion}) discusses model coverage, effect size and statistical design (including TOST equivalence), task scope, causal mechanism, data contamination, and domain/language scope.
12	
13	\item \textbf{Did you discuss any potential risks of your work?}
14	
15	Yes (Limitations). SCS/BCS may be misused as a standalone deployment criterion. Since they are proxies for confusability and do not capture domain-specific ambiguity or downstream harms, they should be used for diagnostic monitoring rather than automatic schema rejection or high-stakes deployment decisions.
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
33	Yes. Few-NERD \citep{fewnerd-2021}, FewRel \citep{fewrel-2018}, DocRED \citep{docred-2019}, MAVEN \citep{maven-2020}, Qwen3-32B \citep{qwen3-2025}, Meta-Llama-3.1-70B-Instruct and M
…[truncated 4760 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool result

_source line 2505 · 2026-05-21T12:18:10.215962+00:00_

PDF pages extracted: 10 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf (458.9KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 707
}
```

</details>

---


### Tool call

_source line 2506 · 2026-05-21T12:18:50.609560+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -name \"config*\" -o -name \"project*.yaml\" -o -name \"project*.yml\" -o -name \"settings*\" 2>/dev/null | head -20",
  "description": "Find project config files"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -name \"config*\" -o -name \"project*.yaml\" -o -name \"project*.yml\" -o -name \"settings*\" 2>/dev/null | head -20",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool call

_source line 2507 · 2026-05-21T12:18:50.660416+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
  "pages": "11-20"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
    "pages": "11-20"
  }
}
```

</details>

---


### Tool result

_source line 2508 · 2026-05-21T12:18:50.762221+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/fontTools/misc/configTools.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/fontTools/misc/__pycache__/configTools.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/fontTools/config
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/pip/_internal/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/pip/_internal/commands/__pycache__/configuration.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/pip/_internal/commands/configuration.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/pip/_internal/configuration.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/pydantic/v1/__pycache__/config.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/pydantic/v1/config.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/pydantic/__pycache__/config.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/pydantic/deprecated/__pycache__/config.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/pydantic/deprecated/config.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/pydantic/conf
…[truncated 311 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---


### Tool result

_source line 2509 · 2026-05-21T12:18:51.318240+00:00_

PDF pages extracted: 10 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf (458.9KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 657
}
```

</details>

---


### Tool call

_source line 2510 · 2026-05-21T12:18:59.251678+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/configs/ 2>/dev/null",
  "description": "List project configs directory"
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
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/configs/ 2>/dev/null",
    "description": "List project configs directory"
  }
}
```

</details>

---


### Tool result

_source line 2511 · 2026-05-21T12:18:59.302379+00:00_

few_nerd_types.json
fewrel_relation_types.json

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

_source line 2512 · 2026-05-21T12:19:06.843374+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -maxdepth 3 -name \"*.yaml\" -path \"*/schema-dag*\" ! -path \"*/.venv/*\" ! -path \"*/artifacts/*\" 2>/dev/null",
  "description": "Find YAML configs for the project"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18 -maxdepth 3 -name \"*.yaml\" -path \"*/schema-dag*\" ! -path \"*/.venv/*\" ! -path \"*/artifacts/*\" 2>/dev/null",
    "description": "Find YAML configs for the project"
  }
}
```

</details>

---


### Tool result

_source line 2513 · 2026-05-21T12:19:06.894035+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/schema-dag-extraction.yaml

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

_source line 2514 · 2026-05-21T12:19:11.011937+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/schema-dag-extraction.yaml 2>/dev/null || echo \"NOT FOUND\"",
  "description": "Check external review config"
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
    "command": "grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/schema-dag-extraction.yaml 2>/dev/null || echo \"NOT FOUND\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 2515 · 2026-05-21T12:19:11.120210+00:00_

NOT FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 108
}
```

</details>

---


### Tool call

_source line 2516 · 2026-05-21T12:19:16.141120+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -i \"external\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/schema-dag-extraction.yaml 2>/dev/null || echo \"NOT FOUND\"",
  "description": "Check for external review or paperreview config"
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
    "command": "grep -i \"external\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/config/projects/schema-dag-extraction.yaml 2>/dev/null || echo \"NOT FOUND\"",
    "description": "Check for external review or paperreview config"
  }
}
```

</details>

---


### Tool result

_source line 2517 · 2026-05-21T12:19:16.192275+00:00_

NOT FOUND

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

_source line 2518 · 2026-05-21T12:19:50.056779+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "schema-dag-extraction",
  "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "schema-dag-extraction",
    "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
  }
}
```

</details>

---


### Tool result

_source line 2519 · 2026-05-21T12:20:11.234320+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 21177
}
```

</details>

---


### Tool call

_source line 2520 · 2026-05-21T12:20:11.335473+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性与实验设计**。\n\n## 论文信息\n- **标题**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n- **论文路径**: projects/schema-dag-extraction/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf\n- **目标 venue**: EMNLP 2026 via ARR May 2026\n- **投稿类别**: Long Paper\n- **截止日期**: 2026-05-25\n\n## Venue 要求\n- **页数限制**: 正文 8 页（不含 Limitations、references、appendix）\n- **模板**: ACL 双栏格式（acl.sty [review] 模式）\n- **匿名**: Double-blind（无 anonymity period 要求）\n- **附录**: 允许，但 reviewer 不必阅读\n- **Limitations**: 必须有，不计入页数限制\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**核心关注**：\n1. **统计方法论**: TOST 等价性检验的 margin 选择是否合理？CI 宽度是否支持结论？logit-scale inconclusive 如何影响主张？\n2. **实验设计**: BCS-controlled 实验的 batch 构建是否有 confound？Count curve 和 BCS 的因果解耦是否充分？\n3. **跨模型验证**: 4 模型家族（Qwen3-32B, LLaMA-8B, LLaMA-70B, Gemini Flash）的验证范围是否充分支撑 cross-model claim？各模型验证了哪些 dimension？\n4. **SCS/BCS 指标**: 作为 cosine similarity 的简单指标，其 predictive validity 是否被充分检验？name-only vs name+definition ablation 是否有意义？\n5. **单种子 + greedy decoding**: 是否导致 CI 偏窄？FP8 量化噪声（0.88pp）对结论的影响？\n6. **NER null 结果**: batch-level BCS 对 NER 无效——论证是否充分？relaxed matching 是否排除了度量伪影？\n7. **DocRED 交互**: range-matched robustness check 的 power 是否足够？n=29+55 的样本量能否支撑 \"bounded interaction\" 结论？\n\n**同时注意**：\n- 页数是否合规（正文 ≤ 8 页）\n- 正文中数字与 appendix 中数据的一致性\n- 图表质量和可读性\n\n请按 ARR 审稿标准给出完整审稿意见，包括 Summary、Strengths、Weaknesses（Must-Fix / Should-Fix 分级）、Questions、Missing References、Overall Assessment（含评分和置信度）。"
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
    "text": "你是 Reviewer 1，负责审查 **方法严谨性与实验设计**。\n\n## 论文信息\n- **标题**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n- **论文路径**: projects/schema-dag-extraction/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf\n- **目标 venue**: EMNLP 2026 via ARR May 2026\n- **投稿类别**: Long Paper\n- **截止日期**: 2026-05-25\n\n## Venue 要求\n- **页数限制**: 正文 8 页（不含 Limitations、references、appendix）\n- **模板**: ACL 双栏格式（acl.sty [review] 模式）\n- **匿名**: Double-blind（无 anonymity period 要求）\n- **附录**: 允许，但 reviewer 不必阅读\n- **Limitations**: 必须有，不计入页数限制\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**核心关注**：\n1. **统计方法论**: TOST 等价性检验的 margin 选择是否合理？CI 宽度是否支持结论？logit-scale inconclusive 如何影响主张？\n2. **实验设计**: BCS-controlled 实验的 batch 构建是否有 confound？Count curve 和 BCS 的因果解耦是否充分？\n3. **跨模型验证**: 4 模型家族（Qwen3-32B, LLaMA-8B, LLaMA-70B, Gemini Flash）的验证范围是否充分支撑 cross-model claim？各模型验证了哪些 dimension？\n4. **SCS/BCS 指标**: 作为 cosine similarity 的简单指标，其 predictive validity 是否被充分检验？name-only vs name+definition ablation 是否有意义？\n5. **单种子 + greedy decoding**: 是否导致 CI 偏窄？FP8 量化噪声（0.88pp）对结论的影响？\n6. **NER null 结果**: batch-level BCS 对 NER 无效——论证是否充分？relaxed matching 是否排除了度量伪影？\n7. **DocRED 交互**: range-matched robustness check 的 power 是否足够？n=29+55 的样本量能否支撑 \"bounded interaction\" 结论？\n\n**同时注意**：\n- 页数是否合规（正文 ≤ 8 页）\n- 正文中数字与 appendix 中数据的一致性\n- 图表质量和可读性\n\n请按 ARR 审稿标准给出完整审稿意见，包括 Summary、Strengths、Weaknesses（Must-Fix / Should-Fix 分级）、Questions、Missing References、Overall Assessment（含评分和置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 2521 · 2026-05-21T12:20:28.607485+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17272
}
```

</details>

---


### Tool call

_source line 2522 · 2026-05-21T12:20:28.760065+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查 **新颖性、完整性与写作质量**。\n\n## 论文信息\n- **标题**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n- **论文路径**: projects/schema-dag-extraction/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf\n- **目标 venue**: EMNLP 2026 via ARR May 2026\n- **投稿类别**: Long Paper\n- **截止日期**: 2026-05-25\n\n## Venue 要求\n- **页数限制**: 正文 8 页（不含 Limitations、references、appendix）\n- **模板**: ACL 双栏格式（acl.sty [review] 模式）\n- **匿名**: Double-blind（无 anonymity period 要求）\n- **附录**: 允许，但 reviewer 不必阅读\n- **Limitations**: 必须有，不计入页数限制\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**核心关注**：\n1. **Novelty 评估**: SCS = pairwise cosine similarity, BCS = mean pairwise SCS。这些是已有概念（LLM-PEE 的 partitioning criterion）。论文的贡献是 \"controlled experimental framework\" 而非新指标——这是否构成足够的 novelty？\n2. **贡献定位**: \"to our knowledge, the first controlled study\" 的 claim 是否站得住？有没有遗漏的先行工作也做了类似的 count vs. confusability 解耦？\n3. **Related Work 覆盖**: 是否充分覆盖 LLM IE 最新进展（2025-2026）？zero-shot IE、schema complexity、label confusion 领域有无重要遗漏？\n4. **写作质量**: Abstract 和 Introduction 是否清晰传达主要贡献？Section 间叙事逻辑是否连贯？SDGD 负面结果的处理是否恰当？\n5. **任务不对称性**: BCS 解释 RE 但不解释 NER 的差异——这是 limitation 还是 finding？论文如何定位这一结果？是否有 over/underclaim？\n6. **Practical Impact**: 论文发现 SCS > 0.85 可标记高风险 type pairs，typical gap ~2pp——这是否有足够的实际意义？所有 mitigation 均失败（SDGD、renaming、few-shot）是否削弱了 practical contribution？\n7. **负面结果价值**: SDGD 失败、renaming 失败、few-shot 扩大 gap——这些负面结果的呈现是否令人信服？是否充分解释了失败的结构性原因？\n\n**同时注意**：\n- Limitations 章节覆盖是否充分（EMNLP 规范：简短，~3 点）\n- 引用格式一致性\n- 匿名性（是否有 deanonymization 风险）\n- Figure/Table caption 信息量\n\n请按 ARR 审稿标准给出完整审稿意见，包括 Summary、Strengths、Weaknesses（Must-Fix / Should-Fix 分级）、Questions、Missing References、Overall Assessment（含评分和置信度）。"
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
    "text": "你是 Reviewer 2，负责审查 **新颖性、完整性与写作质量**。\n\n## 论文信息\n- **标题**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n- **论文路径**: projects/schema-dag-extraction/docs/paper/main.tex\n- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf\n- **目标 venue**: EMNLP 2026 via ARR May 2026\n- **投稿类别**: Long Paper\n- **截止日期**: 2026-05-25\n\n## Venue 要求\n- **页数限制**: 正文 8 页（不含 Limitations、references、appendix）\n- **模板**: ACL 双栏格式（acl.sty [review] 模式）\n- **匿名**: Double-blind（无 anonymity period 要求）\n- **附录**: 允许，但 reviewer 不必阅读\n- **Limitations**: 必须有，不计入页数限制\n- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n## 你的审查侧重\n\n**核心关注**：\n1. **Novelty 评估**: SCS = pairwise cosine similarity, BCS = mean pairwise SCS。这些是已有概念（LLM-PEE 的 partitioning criterion）。论文的贡献是 \"controlled experimental framework\" 而非新指标——这是否构成足够的 novelty？\n2. **贡献定位**: \"to our knowledge, the first controlled study\" 的 claim 是否站得住？有没有遗漏的先行工作也做了类似的 count vs. confusability 解耦？\n3. **Related Work 覆盖**: 是否充分覆盖 LLM IE 最新进展（2025-2026）？zero-shot IE、schema complexity、label confusion 领域有无重要遗漏？\n4. **写作质量**: Abstract 和 Introduction 是否清晰传达主要贡献？Section 间叙事逻辑是否连贯？SDGD 负面结果的处理是否恰当？\n5. **任务不对称性**: BCS 解释 RE 但不解释 NER 的差异——这是 limitation 还是 finding？论文如何定位这一结果？是否有 over/underclaim？\n6. **Practical Impact**: 论文发现 SCS > 0.85 可标记高风险 type pairs，typical gap ~2pp——这是否有足够的实际意义？所有 mitigation 均失败（SDGD、renaming、few-shot）是否削弱了 practical contribution？\n7. **负面结果价值**: SDGD 失败、renaming 失败、few-shot 扩大 gap——这些负面结果的呈现是否令人信服？是否充分解释了失败的结构性原因？\n\n**同时注意**：\n- Limitations 章节覆盖是否充分（EMNLP 规范：简短，~3 点）\n- 引用格式一致性\n- 匿名性（是否有 deanonymization 风险）\n- Figure/Table caption 信息量\n\n请按 ARR 审稿标准给出完整审稿意见，包括 Summary、Strengths、Weaknesses（Must-Fix / Should-Fix 分级）、Questions、Missing References、Overall Assessment（含评分和置信度）。"
  }
}
```

</details>

---


### Tool result

_source line 2523 · 2026-05-21T12:20:30.476363+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1716
}
```

</details>

---


### Assistant

_source line 2524 · 2026-05-21T12:20:43.398037+00:00_

**Round 1 已启动**：

| 任务 | 状态 |
|------|------|
| 视觉审查 Agent | ✅ 已派发（fire-and-forget） |
| Reviewer 1（方法严谨性） | ✅ 已分配，独立审稿中 |
| Reviewer 2（新颖性/完整性） | ✅ 已分配，独立审稿中 |
| 外部审稿 | ⏭️ 未配置，跳过 |

等待两名 Reviewer 返回 Round 1 独立审稿意见后，进入交叉分享阶段（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 206

## Round 206

2 recorded events


### User

_source line 2525 · 2026-05-21T12:27:56.079757+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见：方法严谨性与实验设计

**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?
**Venue**: EMNLP 2026 via ARR May 2026 (Long Paper)

---

## 总体评分
**Overall Assessment**: 3.5 — Borderline Conference
**一句话总结**: 实验设计精细、分析全面的实证研究，但 TOST 等价性检验的 margin 选择存在循环论证风险，跨模型验证覆盖不对称，核心 claim 的泛化性需要更谨慎的措辞。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心实验设计（BCS-controlled + count curves）严谨，统计方法多样（bootstrap CI、TOST、factorial regression），但 TOST margin 部分循环、跨模型验证不对称、NER null result 缺乏 power analysis |
| Excitement | 3/5 | 实证分析角度新颖（分离 count vs. confusability），findings 可操作（SCS 指导 batch 设计），但本质是诊断性分析而非方法贡献，主要发现（更多类型→更差性能）虽量化精确但方向上不出人意料 |
| Reproducibility | 4/5 | 实验细节充分（Appendix G 完整 prompt 模板、§3.3 详细超参、Appendix R 方差分解），承诺开源代码和数据，但主实验仅 Qwen3-32B 单模型，复现依赖特定 FP8 量化环境 |
| Overall Assessment | 3.5/5 | Borderline Conference — 修复 must-fix 问题后可达 Conference (4.0) |
| Confidence | 4/5 | 仔细阅读了全部 27 页（含 appendix），熟悉 training-free IE 和统计方法论相关工作 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] TOST 等价性检验的 ±3pp margin 存在循环论证风险

- 具体位置：§4.3 (p.8)、Appendix C (p.16)
- 问题：论文用三个"converging anchors"论证 ±3pp margin 的合理性（Appendix C）：(1) Empirical: 同一实验的 batch SD=1.6pp → 0.5×SD≈3pp；(2) Practical: ±3pp 低于部署阈值；(3) Statistical: 3pp≈Cohen's d=0.5。其中 anchor (1) 直接从被检验数据的 SD 推导 margin，构成循环——若真实 batch 方差更大，同一 margin 会过窄；若更小，又过宽。Anchor (3) 本质是 anchor (1) 的统计学重述（d=effect/SD，SD 仍来自同一数据）。仅 anchor (2) 是外部标准，但"部署阈值"未给出具体引用来源或行业标准。
- 更关键的是：logit-scale TOST 不显著（p>0.20, Appendix C），论文承认但在 abstract 和 §5 的结论中仅强调 probability-scale 等价结果。当 base rate 接近边界时，两个 scale 可以给出矛盾结论（probability 空间的 3pp 在低准确率区域对应更大的 logit 差异）。
- 为什么影响接收：这是支撑 "count 与 confusability 独立可加" 这一核心 claim 的关键统计检验。如果 margin 选择不独立于数据，等价性结论的可信度降低。
- 建议修改方向：(a) 从先前工作或独立 pilot study 导出 margin（如引用 LLM IE 领域已有的 accuracy 波动基线）；(b) 在正文中明确报告 logit-scale TOST 结果及其不一致性，而非仅在 appendix 提及；(c) 做 margin sensitivity analysis，展示结论在 ±2pp 至 ±5pp 范围内的稳健性。

---

**N2** [critical] 跨模型验证覆盖严重不对称，但 claim 未做相应限定

- 具体位置：Abstract ("replicated across four models spanning three architecture families")、§3.3 (p.5)、Appendix S-U (p.24-25)
- 问题：Abstract 和 Introduction 声称"四个模型家族"验证了 "both dimensions"，但实际验证矩阵如下：

| 维度/任务 | Qwen3-32B | LLaMA-8B | LLaMA-70B | Gemini 2.5 Flash |
|----------|-----------|----------|-----------|-----------------|
| FewRel count curve | ✓ | ✓ | ✓ | ✓ |
| FewRel BCS-controlled | ✓ | ✗ | ✓ | ✓ |
| Few-NERD count curve | ✓ | ✓ | ✗ | ✗ |
| NER null (BCS无效) | ✓ | ✗ | ✗ | ✗ |
| DocRED factorial | ✓ | ✗ | ✗ | ✗ |
| MAVEN centrality | ✓ | ✗ | ✗ | ✗ |
| ED task | ✓ | ✗ | ✗ | ✗ |
| Error taxonomy (§4.4) | ✓ | ✗ | ✗ | ✗ |

真正在所有四个模型上验证的只有 FewRel count-degradation curve。NER null result——论文的关键发现之一——仅在 Qwen3-32B 上验证。DocRED 和 MAVEN 的分析完全依赖单一模型。

- 为什么影响接收：论文的 novelty 很大程度建立在 "cross-model generalization" 上。如果 NER null result 是 Qwen3 特有的（例如 Qwen3 的 NER 能力特别强以至于不受 BCS 影响），整个 "task asymmetry" 的 claim 就需要重新评估。
- 建议修改方向：(a) 在 abstract 和 §5 中明确区分 "across all four models" vs. "primarily on Qwen3-32B" 的结论；(b) 至少在一个额外模型上验证 NER null result（即使只做 BCS-controlled 子集）；(c) 在 Limitations 中增加一条关于跨模型覆盖的具体限制，当前的 Limitation #1 过于笼统。

---

**N3** [critical] BCS-controlled batch 构建可能引入超越 confusability 的混杂因素

- 具体位置：§3.3 Experiment 2 (p.4-5)、§4.5 (p.7-8)、Appendix E (p.17)
- 问题：BCS-controlled 实验通过选择 pairwise cosine similarity 极端的类型组合来构建 high/low-BCS batch。但高 BCS batch 中的类型在语义空间中聚集，这些类型可能共享其他影响抽取性能的属性：
  - **预训练频率共变**：语义相近的类型可能在预训练数据中共现频率相似（§4.5 确认 MAVEN 上 BCS 与 log frequency 和 degree centrality 存在正相关）
  - **实体/mention 长度分布**：相似类型可能有相似的 mention 特征
  - **类型定义复杂度**：语义聚集的类型可能有结构性相似的 schema definition

  论文在 Appendix E 中对 MAVEN 做了 partial correlation 控制 centrality（结论：控制后 BCS 效应消失），但 **FewRel 和 DocRED 缺乏等价的混杂因素分析**。在 Appendix Q (p.23) 中仅对 FewRel 做了 train-origin covariate 分析（控制预训练暴露），但未控制 type frequency 或其他 distributional 属性。
- 为什么影响接收：如果 BCS 与 type frequency 在 FewRel 上也共变（但论文未检查），则 BCS-controlled 实验实际隔离的可能不是"confusability"而是"类型熟悉度"，这会改变论文的解释框架。
- 建议修改方向：(a) 对 FewRel 也做 Appendix E 式的 partial correlation 分析（控制 type frequency 和 degree centrality）；(b) 讨论 BCS batch 构建中可能的 distributional confound；(c) 如果 FewRel 上 BCS 效应在控制后仍然显著，这反而会加强论文结论。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 单种子评估 + FP8 量化噪声可能导致 CI 反保守

- 具体位置：§3.3 (p.5)、Appendix R (p.23)
- 问题：所有 batch 均使用 greedy decoding (temperature=0, seed=42) 单次评估。Appendix R 表明 FP8 量化引入 ~0.88pp 的 seed-level 噪声（Table 19, count=80 时 Seed SD=0.88pp）。论文的 bootstrap CI 仅捕获 batch composition 方差，不包含此测量噪声。
  - Factorial 交互项点估计 = 0.47pp (Appendix I)，**小于** FP8 噪声 (0.88pp)
  - 考虑测量噪声后，交互项真值可能在 [-0.41pp, 1.35pp] 范围，虽仍在 ±3pp margin 内，但 CI 的名义覆盖率可能低于 95%
- 建议：在 FewRel 的一个代表性 count level 上用 2-3 个不同 seed 重复评估，量化 FP8 导致的 within-batch 方差，并将其纳入 CI 计算。

**W2** [warning] DocRED range-matched robustness check 的统计检验力不足

- 具体位置：Appendix C (p.16)、Appendix D (p.17)
- 问题：Range-matched 子集限制到 BCS 范围 [0.43, 0.70] 后，count 16 仅剩 29 batches、count 32 约 55 batches。在此样本量下：
  - Appendix D 的 quartile contrast ΔR² 跨越零（论文自承 "lacks statistical power"）
  - TOST p=0.003 看似有力，但 minimum detectable effect size 未报告
  - 若 MDE > 2pp，这个 "bounded interaction" 结论的实际信息量有限
- 建议：报告 range-matched 子集的 MDE（给定 n 和 observed SD），让读者判断 "bounded" 的精度。

**W3** [warning] NER null result 缺乏 power analysis，可能反映 BCS range 不足而非真正的任务差异

- 具体位置：§4.2 (p.6)、Appendix Y (p.26-27)
- 问题：论文主张 "NER shows no batch-level BCS signal"（§4.2），Appendix Y 的 relaxed matching 分析（Table 28: Pearson r 全部在 [-0.042, 0.014] 范围，p>0.10）支持 null。但：
  - Few-NERD 的 BCS range 相对 FewRel 可能更窄（66 fine-grained types 来自 8 coarse categories，BCS range 可能被 hierarchical structure 压缩）
  - 论文未报告 Few-NERD vs. FewRel 的 BCS range 比较
  - 未做 power analysis：当前样本量和 BCS range 下能检测到多大的效应？
  - 如果 BCS range 是 [0.50, 0.70]（窄），那么 null result 可能仅说明 "在这个 range 内检测不到"，而非 "NER 对 confusability 免疫"
- 建议：(a) 报告 Few-NERD 和 FewRel 的 BCS range 分布对比；(b) 做 post-hoc power analysis；(c) 考虑在措辞上区分 "absence of evidence" 和 "evidence of absence"。

**W4** [warning] SCS 作为 lightweight proxy 的 predictive validity 边界讨论不足

- 具体位置：§3.2 (p.4)、Appendix M (p.22)、Table 17
- 问题：SCS 是 name string 的 pairwise cosine similarity，极为简单。论文展示其对 RE 有预测力但对 NER 无效。Appendix M 的 name-only vs. name+definition 消融（Table 17）显示 definition 不提供系统性增益，这可能有两种解释：
  - (a) name embedding 已充分编码类型语义（论文的解释）
  - (b) Qwen3 的 embedding 对 definition 文本不敏感（模型局限）
  论文未区分这两种解释。此外，SCS 不捕获上下文消歧线索（同一 mention 在不同上下文中可能属于不同类型），这对 NER 尤其重要。
- 建议：(a) 在 §3.2 中讨论 SCS 不捕获的因素（上下文消歧、entity mention ambiguity）；(b) 在另一个 embedding 模型上重复 name-only vs. name+definition 消融以区分上述两种解释。

**W5** [warning] SDGD 负面结果呈现不足，难以判断是方法本身的局限还是实现的局限

- 具体位置：§5 (p.8)、Appendix B (p.14)
- 问题：SchemaDAG-Guided Decomposition (SDGD) 是论文提出的解决方案，但 F1=0.445 远低于 single-pass baseline (0.563)。论文归因于 merge amplification 和 routing failure。但：
  - Appendix B 的 SDGD 描述仅两段，算法细节不足
  - 四种 decomposition 模式（single_pass, sdgd_zero, random_batch, per_type）的比较（Table 6, p.15）中，SDGD 没有跑 oracle routing 的 ablation——只有 Table 10 (p.17) 展示了 oracle routing 的上界
  - 未探索 intermediate granularity（如 2-3 个子 schema 而非完全分解）
- 建议：(a) 增加 SDGD 的算法伪代码；(b) 至少做一个 oracle-routing ablation 来区分 routing failure vs. decomposition 本身的问题。

---

## 小问题（不影响接收）

1. **术语歧义 "seed"**：Figure 1 caption 说 "3 seeds × 25 batches"，§3.3 说 "single-seed evaluation with greedy decoding"。虽然从 Appendix R 可推断前者指 batch composition seed、后者指 inference seed，但正文应明确区分两种 seed 的含义。

2. **Table 2 (p.6) bootstrap 方法未指定**：报告了 bootstrap 95% CI 但未说明用 percentile、BCa 还是其他方法。对于偏斜分布（如 Spearman ρ 接近 ±1），BCa 和 percentile CI 可能有显著差异。

3. **§4.5 MAVEN centrality confound 的措辞**：论文发现控制 centrality 后 BCS 效应在 MAVEN 上消失，但用 "centrality confound" 命名。建议改为更中性的 "centrality as a mediator or confound"，因为 centrality 也可能是因果路径的一部分（高 centrality → 高 BCS → 更多混淆）。

4. **Appendix N (p.22) pair-to-batch simulation**：模拟用 ρ=0.35 估计 pair-level SCS 相关，但这个 ρ 的来源（"computed over non-zero confusion pairs"）的样本构成未详细说明。

5. **Figure 2 (p.7)** 图例 "IntaSub" 疑为 "IntraSub" 的拼写错误。

---

## 主要优势

1. **精巧的实验设计**：Count curves + BCS-controlled 两种互补范式有效分离了 schema size 和 confusability 的效应，这是相对于此前工作（Xu et al. 2024a, Chen et al. 2026）的真正方法论进步。

2. **极为充分的 appendix**（17 页）：包含 prompt 模板 (G)、方差分解 (R)、cross-variant sensitivity (H)、format independence (K)、BCS range analysis (J)、relaxed matching (Y) 等，展现了对 robustness 的严肃态度。

3. **诚实的负面结果报告**：NER null result (§4.2)、SDGD 失败 (§5)、MAVEN centrality confound (§4.5) 均未被掩盖，反而成为论文最有信息量的部分之一。

4. **可操作的实践建议**：§5 和 §8 提出的 SCS > 0.85 阈值监控、batch BCS 跟踪等建议直接可用于 LLM IE 系统部署。

5. **SCS/BCS 指标设计简洁有效**：用 cosine similarity 的简单聚合即可解释 22-58% 的 RE 准确率方差（Table 2），且在 Qwen3 和 MiniLM 两种 embedding 下一致（§4.2），具有实用价值。

6. **统计方法多样且互补**：Spearman 相关 + bootstrap CI + TOST 等价性检验 + factorial regression + Monte Carlo simulation (Appendix N)，多种方法交叉验证同一结论。

---

## Questions for Authors

Q1. FewRel 上 BCS 与 type frequency 的相关性是多少？如果 BCS 与 type frequency 在 FewRel 上也正相关（类似 MAVEN），控制 frequency 后 BCS 对 RE accuracy 的解释力还剩多少？

Q2. Few-NERD 的 BCS range（min/max/IQR）与 FewRel 相比如何？如果 Few-NERD 的 BCS range 显著窄于 FewRel，NER null result 是否可能仅反映 range restriction 而非任务差异？

Q3. 在 FP8 量化下，同一 batch 用不同 random seed 重复 3 次，accuracy 的 SD 是多少？这个 within-batch 方差是否会改变 factorial 交互项的 CI？

Q4. SDGD 中如果使用 oracle routing（即已知每个 test instance 属于哪个子 schema），F1 能恢复到什么水平？Table 10 (Appendix F) 的 oracle routing 结果（F1=0.320）仍低于 single-pass（F1=0.445 for SDGD vs. 0.563 for single-pass）——这是否意味着问题不仅在 routing，decomposition 本身也有损失？

Q5. Appendix C 中 logit-scale TOST 不显著——如果只在高准确率区域（如 count ≤ 8）做 TOST，probability 和 logit scale 是否一致？在低准确率区域（count ≥ 32）呢？

---

## Missing References

- Sainz et al., 2024 (GoLLIE) 已引用。考虑补充：
  - **Ma et al., 2024** "Let's Ask GPT" — 系统评估 schema complexity 对 ChatGPT IE 的影响，与本文问题直接相关但 Related Work 中讨论不足
  - **Wadhwa et al., 2023** "Revisiting relation extraction in the era of LLMs" — 虽已引用但主要在 Related Work，其关于 type confusion 的发现与本文 §4.2 高度相关，建议在 §4.2 中做更具体的对比

---

## 格式合规性检查

- **页数**：正文 Sections 1-5 占 pages 1-8，Limitations 从 page 8 底部开始 → **合规**（≤8 页）
- **匿名性**：标题页标注 "Anonymous ACL submission"，正文未发现 de-anonymization → **合规**
- **Limitations**：page 8-9，覆盖 4 个点（model coverage, effect size/statistical design, task scope, causal mechanism）→ **合规**
- **NLP Checklist**：pages 9-11，所有 section 均有回答 → **合规**
- **模板**：ACL 双栏格式，review 模式 → **合规**


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

_source line 2526 · 2026-05-21T12:28:19.149207+00:00_

收到 Reviewer 1 审稿意见。

**R1 核心发现摘要**：
- **评分**: 3.5 (Borderline Conference)
- **Must-Fix (3)**：TOST margin 循环论证风险、跨模型验证覆盖不对称、BCS-controlled batch 可能引入超越 confusability 的混杂因素
- **Should-Fix (5)**：单种子 CI 偏窄、DocRED range-matched power 不足、NER null 缺 power analysis、SCS validity 边界讨论不足、SDGD 呈现不足

等待 Reviewer 2 审稿意见返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 207

## Round 207

2 recorded events


### User

_source line 2527 · 2026-05-21T12:28:21.855877+00:00_

[Reviewer 1 审稿结果]:
审稿完成。总结：

**Overall: 3.5 (Borderline Conference)**，Soundness 3.5，Excitement 3，Reproducibility 4，Confidence 4。

提出 3 个 Must-Fix：
1. TOST ±3pp margin 从同一实验 SD 推导，存在循环论证；logit-scale 不显著但正文未充分讨论
2. 跨模型验证严重不对称——仅 FewRel count curve 在全部 4 个模型上验证，NER null result 等关键发现仅有 Qwen3-32B
3. BCS-controlled batch 构建可能引入 type frequency 等混杂因素，FewRel/DocRED 缺乏 MAVEN 式的 partial correlation 控制

5 个 Should-Fix（FP8 噪声与 CI 保守性、DocRED 小样本 power、NER null 的 power analysis、SCS proxy 边界讨论、SDGD 负面结果呈现不足）和 5 个小问题。

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

_source line 2528 · 2026-05-21T12:28:32.163088+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成审稿后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 208

## Round 208

2 recorded events


### User

_source line 2529 · 2026-05-21T12:40:33.175772+00:00_

[Reviewer 2 审稿结果]:
论文共27页，先读前10页。同时获取 ARR 官方 review form 详情。

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

_source line 2530 · 2026-05-21T12:40:43.545223+00:00_

等待 Reviewer 2 完成审稿。Reviewer 1 已完成（3.5 Borderline Conference），Reviewer 2 正在阅读论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 209

## Round 209

62 recorded events


### User

_source line 2531 · 2026-05-21T17:43:44.227788+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema-dag-extraction
- 论文路径: projects/schema-dag-extraction/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (via ARR May 2026)
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

_source line 2532 · 2026-05-21T17:43:49.621926+00:00_

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

_source line 2533 · 2026-05-21T17:43:49.622835+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2534 · 2026-05-21T17:44:00.154338+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2535 · 2026-05-21T17:44:00.154699+00:00_



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

_source line 2536 · 2026-05-21T17:44:00.606682+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
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

_source line 2537 · 2026-05-21T17:44:00.757857+00:00_



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

_source line 2538 · 2026-05-21T17:44:07.332804+00:00_

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


### Tool call

_source line 2539 · 2026-05-21T17:44:07.586011+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 2540 · 2026-05-21T17:44:08.590431+00:00_

{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (69 个)\n\n- **exp012_llama_8b_r2_exp2**: DONE (negative) — \n- **exp012_llama_8b_r2**: DONE (success) — \n- **exp006_interaction_2x2**: DONE (negative) — \n- **exp012_llama_awq**: DONE (killed) — \n- **exp012_llama_8b_r3**: DONE (failed) — \n- **exp012_llama_8b**: DONE (killed) — \n- **exp_fewrel_40rel_r3**: DONE (failed) — \n- **exp_fewrel_40rel_r2**: DONE (failed) — \n- **exp012_llama_fewnerd_r4**: DONE (failed) — \n- **exp012_llama_8b_fewnerd**: DONE (failed) — \n- **exp_fewrel_40rel**: DONE (failed) — \n- **exp012_llama_fewnerd_r3**: DONE (failed) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- prompt_sensitivity（准备中）\n- prompt_sensitivity_dry4（准备中）\n- prompt_sensitivity_dry3（准备中）\n- prompt_sensitivity_dry2（准备中）\n- prompt_sensitivity_dry（准备中）\n- exp_aggregation_monte_carlo（准备中）\n- exp_scs_name_def_ablation（准备中）\n- exp_fewrel_contamination_check（准备中）\n- exp017_gpt4o_mini_fewrel（准备中）\n- exp_cross_embedding_sensitivity（准备中）\n- …另有 2 项\n\n## 近期结论\n- **exp_llama70b_ner_bcs_null** (success): Batch-level BCS does not correlate with NER F1 for LLaMA-3.1-70B-FP8, consistent with the BCS null observed in Qwen3-32B (r=0.004) and LLaMA-8B (r=-0.12). The confusability metric is not predictive of extraction quality at the batch level. ← 基于 exp012_llama_8b_r2_exp2\n  [LLaMA-70B NER BCS-null analysis](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_llama70b_ner_bcs_null/data/bcs_null_analysis.json)\n- **exp_gemini_flash_bcs_controlled** (success): BCS-accuracy negative correlation observed on open-weight models (Qwen3-32B, LLaMA) generalizes to proprietary API models. Gemini 2.5 Flash should show significant BCS gap on extreme-BCS batches at count 8 and count 16, confirming Dimension 2 is architecture-family-in
…[truncated 1221 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1257
}
```

</details>

---


### Tool result

_source line 2541 · 2026-05-21T17:44:08.590956+00:00_

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
40	\item \textbf{Model coverage.} Primary experiments use a single model (Qwen3-32B); cross-model validation covers the core extreme-BCS setting but does not replicate all secondary analyses (error taxonomy, prompt sensitivity, TOST equivalence tests). Whether these secondary findings generalize beyond Qwen3-32B remains open; see Appendix~\ref{sec:appendix_cross_model_gemini} and Table~\ref{tab:cross_model_bcs} for detailed model-wise results.
41	
42	\item \textbf{Effect size and statistical design.} Pairwise SCS explains a small fraction of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\times$ BCS interaction is bounded on FewRel but nonzero on DocRED, partially confounded by BCS range restriction at higher counts (Appendix~\ref{sec:appendix_factorial}); logit-scale evidence remains inconclusive. DocRED count curves use 5 batches per level due to higher per-batch evaluation cost. BCS-controlled experiments use a single seed with greedy decoding; residual variance is small (Appendix~\ref{app:variance-decomposition}) but precise magnitudes may vary. Greedy-decoding seed SD (0.88\,pp) implies CIs may slightly underc
…[truncated 7776 chars]

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

_source line 2542 · 2026-05-21T17:44:08.591173+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR May 2026 submission deadline author guidelines"
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
    "query": "ACL Rolling Review ARR May 2026 submission deadline author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 2543 · 2026-05-21T17:44:09.594959+00:00_

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


### Tool call

_source line 2544 · 2026-05-21T17:44:09.997014+00:00_

called mcp__agent-ml-research__read_local_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_local_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file_path": "projects/schema-dag-extraction/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_local_file",
  "tool_args": {
    "project": "schema-dag-extraction",
    "file_path": "projects/schema-dag-extraction/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2545 · 2026-05-21T17:44:09.997358+00:00_

&lt;tool_use_error>Error: No such tool available: mcp__agent-ml-research__read_local_file&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_local_file",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 2546 · 2026-05-21T17:44:24.826201+00:00_

Web search results for query: "ACL Rolling Review ARR May 2026 submission deadline author guidelines"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"ACL ARR 2026 May | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMay"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Let me search for more specific information about the May 2026 ARR submission deadline and author guidelines.

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Lingu
…[truncated 3269 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 16235
}
```

</details>

---


### Tool result

_source line 2547 · 2026-05-21T17:44:24.876964+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'schema-dag-extraction'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 15282
}
```

</details>

---


### Tool call

_source line 2548 · 2026-05-21T17:44:32.664708+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/dates",
  "prompt": "Extract the exact submission deadline for ARR May 2026 cycle, and also EMNLP 2026 commitment deadline. List all dates for 2026 cycles."
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
    "url": "https://aclrollingreview.org/dates",
    "prompt": "Extract the exact submission deadline for ARR May 2026 cycle, and also EMNLP 2026 commitment deadline. List all dates for 2026 cycles."
  }
}
```

</details>

---


### Tool call

_source line 2549 · 2026-05-21T17:44:33.970812+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract all important information: submission deadline, page limits, format requirements, anonymity rules, appendix rules, commitment deadline, and any other author guidelines for EMNLP 2026."
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
    "prompt": "Extract all important information: submission deadline, page limits, format requirements, anonymity rules, appendix rules, commitment deadline, and any other author guidelines for EMNLP 2026."
  }
}
```

</details>

---


### Tool call

_source line 2550 · 2026-05-21T17:44:35.879601+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/cfp",
  "prompt": "Extract the full call for papers details: page limits for long and short papers, formatting requirements, anonymity policy, supplementary material rules, citation format, responsible NLP checklist requirements, and any other submission guidelines."
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
    "prompt": "Extract the full call for papers details: page limits for long and short papers, formatting requirements, anonymity policy, supplementary material rules, citation format, responsible NLP checklist requirements, and any other submission guidelines."
  }
}
```

</details>

---


### Tool result

_source line 2551 · 2026-05-21T17:44:36.934689+00:00_

# ARR 2026 Submission and Commitment Deadlines

## May 2026 Cycle Submission Deadline
"May 25, 2026" is the exact submission deadline for the ARR May 2026 cycle.

## EMNLP 2026 Commitment Deadline
Papers can be committed to EMNLP 2026 by "August 2, 2026".

## All 2026 ARR Cycle Dates

| Cycle | Submission | Reviewer Registration | Reviews Due | Author Response | Meta-reviews Release | Cycle End |
|-------|-----------|----------------------|-------------|-----------------|-------------------|-----------|
| March 2026 | March 16 | March 18 | April 20 | April 28–May 4 | May 21 | May 24 |
| May 2026 | May 25 | May 27 | June 29 | July 7–July 13 | July 30 | August 2 |
| August 2026 | August 3 | TBA | TBA | TBA | TBA | October 11 |
| October 2026 | October 12 | TBA | TBA | TBA | TBA | December 20 |

Note: The August and October 2026 cycles show some details marked as "TBA" (to be announced) in the source material.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebFetch",
  "elapsed_ms": 4269
}
```

</details>

---


### Tool call

_source line 2552 · 2026-05-21T17:44:36.985896+00:00_

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

_source line 2553 · 2026-05-21T17:44:37.036720+00:00_

1	# Review Issues Tracker
2	# Updated: 2026-05-19 (All R22 fixes verified in v12)
3	
4	# ============================================================
5	# R22 CRITICAL — ALL RESOLVED
6	# ============================================================
7	
8	- id: R22-C1
9	  summary: "Title/Abstract scope overclaim: 'Information Extraction' 但 batch-level Dim2 仅 RE 成立"
10	  category: framing
11	  severity: critical
12	  status: resolved
13	  first_raised_round: 21
14	  last_seen_round: 22
15	  mentions:
16	    - {round: 21, reviewers: [R1, R2], note: "R21-W1: NER Dim2 batch-level null, Title IE 过宽"}
17	    - {round: 22, reviewers: [R2], note: "R2 Must-Fix N1。batch-level BCS 仅 RE (FewRel/DocRED) 成立，NER r≈0，MAVEN centrality confound。R1 部分 rebut：pairwise SCS 跨任务成立，batch-level 是聚合局限。交叉后共识：Abstract 需加 task-format qualifier。"}
18	  action_items:
19	    - {round: 22, action: "Abstract 重写：区分 pairwise (跨任务) vs batch-level (RE only)，加 task-dependent qualifier，标注数字来源条件", assigned_to: main_agent, status: done}
20	  resolution: "v12 Abstract 重写完成，区分 pairwise vs batch-level scope，加 task-dependent qualifier + format independence。"
21	  resolution_round: 22
22	
23	- id: R22-C2
24	  summary: "SCS/BCS novelty 不足，与 LLM-PEE partitioning criterion 一致"
25	  category: framing
26	  severity: critical
27	  status: resolved
28	  first_raised_round: 21
29	  last_seen_round: 22
30	  mentions:
31	    - {round: 21, reviewers: [R1, R2], note: "R21-C4: SCS 借自 LLM-PEE，novelty framing 不清晰"}
32	    - {round: 22, reviewers: [R2], note: "R2 Must-Fix N2。SCS=cosine sim, BCS=mean，无技术创新。'controlled framework' 作主贡献论证不充分。R1 rebut：方法论创新在实验范式非指标，22-58% R² 无法靠直觉预测。交叉后分歧保留。"}
33	  action_items:
34	    - {round: 22, action: "Intro+Discussion 强化 non-obvious findings (22-58% R², renaming 反直觉, NER null, few-shot 扩大 gap)", assigned_to: main_agent, status: done}
35	  resolution: "v12 Intro/Discussion 强化 non-obvious findings 作为核心贡献。"
36	  resolution_round: 22
37	
38	- id: R22-C3
39	  summary: "TOST ±3pp margin 循环论证 + logit-sca
…[truncated 11137 chars]

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


### Tool result

_source line 2554 · 2026-05-21T17:44:39.847298+00:00_

# EMNLP 2026 Submission Guidelines

## Key Deadlines
- **ARR Submission:** May 25, 2026
- **Reviewer Registration:** May 27, 2026
- **EMNLP Commitment:** August 2, 2026
- **Acceptance Notification:** August 20, 2026
- **Camera-Ready Due:** September 20, 2026
- **Conference Dates:** October 24-29, 2026

*All deadlines are 11:59 PM UTC-12:00*

## Paper Length Requirements
- **Long Papers:** 8 pages (9 pages in camera-ready with reviewer feedback)
- **Short Papers:** 4 pages (5 pages in camera-ready with reviewer feedback)

## Anonymity Rules
The guidelines state: "there is no anonymity period requirement" following ACL and ARR policies. However, the review process itself maintains "double-blind" standards where "Reviewers will not see authors, nor will authors see reviewers."

## Format & Submission Details
Authors must adhere to all ARR submission requirements, including:
- Two-way anonymized review procedures
- ACL Publication Ethics Policy compliance
- Responsible NLP research checklist
- Citation and comparison standards

## Appendix & Supplementary Materials
Optional supplementary materials, appendices, software, and data are permitted per ARR guidelines.

## Author Responsibilities
All authors must register by May 27 and complete mandatory reviewing work (reviews due July 6; meta-reviews by July 29), or declare emergencies through proper channels.

## Commitment Phase Rules
"During the commitment phase, it is not allowed to modify the author list...However, modification of author order is possible."

## Presentation Requirement
All accepted papers require presentation at the conference by a registered author to appear in proceedings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebFetch",
  "elapsed_ms": 5876
}
```

</details>

---


### Tool result

_source line 2555 · 2026-05-21T17:44:43.511662+00:00_

# ACL Rolling Review Call for Papers Summary

## Page Limits

**Long Papers:**
- Up to 8 pages of content
- Unlimited space for limitations section (required) and ethical considerations
- Unlimited reference pages

**Short Papers:**
- Up to 4 pages of content
- Unlimited space for limitations section (required) and ethical considerations
- Unlimited reference pages

Papers exceeding length requirements or lacking a limitations section face desk rejection.

## Formatting Requirements

Submissions must follow the official ACL style template and formatting guidelines. The document specifies that "submissions that do not conform to the required styles, including paper size, margin width, and font size restrictions, will be rejected without review." Authors cannot modify style files or use templates from other conferences. Appendices must follow double-column format with limited exceptions.

## Anonymity Policy

The platform enforces two-way anonymized review. Authors must remove their names, affiliations, and self-references that reveal identity. Rather than "We previously showed," use "Smith previously showed." Supplementary materials and repository links must also be anonymized—cloud services like Dropbox are prohibited due to download tracking capabilities.

## Supplementary Materials

Appendices, software, and data are encouraged but optional. They should not contain material necessary for assessing novelty or claims; such content belongs in the main paper. Reviewers are not obligated to review appendices. Software must be submitted as single compressed archives through anonymized repositories.

## Citation Format for Concurrent Work

For overlapping submissions by the same authors, use this format: "Anonymous (2026). Paper title. Under review."

## Responsible NLP Checklist

Completion is mandatory during submission. Incorrect, incomplete, or misleading responses can result in desk rejection. The checklist content influences review evaluation, and authors should an
…[truncated 751 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebFetch",
  "elapsed_ms": 7632
}
```

</details>

---


### Tool call

_source line 2556 · 2026-05-21T17:45:00.327737+00:00_

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

_source line 2557 · 2026-05-21T17:45:01.081609+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: type count and type confusability. We present what is, to our knowledge, the first controlled study isolating these factors across NER, RE, and event detection on four datasets. We quantify confusability via the Schema Confusability Score (SCS) and its batch-level aggregation, the Batch Confusability Score (BCS). Degradation operates along two dimensions with task-dependent effect structures: count-related recall decline (up to $-$49\,pp on DocRED 96-relation RE) and confusability-related type substitution. In RE, BCS explains 22--58\% of cross-batch accuracy variance (FewRel/DocRED), independent of output format (paired constrained/unconstrained comparison yields virtually identical correlations); NER shows no batch-level BCS signal, as errors scatter across missed entities and boundary failures. Schema decomposition fails due to merge amplification (NER, ED) and routing failure (RE). The RE confusability effect replicates across four models spanning three architecture families (Qwen, LLaMA, Gemini; 8B--70B), two decoding formats, and five prompt designs; the NER batch-level null is confirmed on three models (8B--70B).
3	\end{abstract}
4	

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

_source line 2558 · 2026-05-21T17:45:01.082142+00:00_

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

_source line 2559 · 2026-05-21T17:45:01.684833+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance.} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \citep{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near-halving or worse. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What explains this degradation? Prior decomposition strategies \citep{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
7	
8	This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.
9	
10	We ask three questions. \textbf{RQ1}: Does type confusability independently predi
…[truncated 3279 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 2560 · 2026-05-21T17:45:01.685265+00:00_

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

_source line 2561 · 2026-05-21T17:45:02.187440+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	Training-free LLM IE spans instruction tuning \citep{instructuie-2023}, code-style schema encoding \citep{knowcoder-2024,codeie-2023}, annotation-guided extraction \citep{gollie-2024,adelie-2024}, schema-driven decoding \citep{slot-2025,oneke-2025}, and constrained JSON decoding \citep{json-schema-bench-2025,willard2023efficient}. For NER, methods include zero-shot decomposition \citep{xie-zeroshot-ner-2023,promptner-2023}, distillation \citep{uniner-2024}, bidirectional encoders \citep{gliner-2024,gliner2-2025}, and fine-grained entity typing \citep{gillick-2014-entity-typing}. For RE, recent work examines zero-shot relation triplet extraction via prompting \citep{relationprompt-2022}, constrained generative extraction \citep{josifoski-2022-genie}, revisits relation extraction in the LLM era \citep{wadhwa-re-llm-2023}, and zero-shot RE via shared embedding spaces \citep{boylan-2025-glirel}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales, nor proposes quantitative metrics for inter-type confusability. \citet{wei-2023-chatie} reformulate zero-shot IE as multi-turn QA with ChatGPT but do not analyze schema-size effects.
6	
7	\paragraph{Schema complexity in IE.}
8	The most directly related work is LLM-PEE \citep{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. LLM-PEE's union merge suffers the same precision collapse (0.56$\to$0.21; \S\ref{sec:sdgd}). In short, LLM-PEE ass
…[truncated 3785 chars]

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

_source line 2562 · 2026-05-21T17:45:02.187782+00:00_

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

_source line 2563 · 2026-05-21T17:45:02.489326+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \citep{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains and is suitable for cross-domain evaluation. We sample 1{,}000 instances uniformly from the test set; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \citep{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). A held-out validation confirms SCS--confusion generalization across the split boundary (Appendix~\ref{app:scs-heldout-validation}). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \citep{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We s
…[truncated 9195 chars]

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

_source line 2564 · 2026-05-21T17:45:02.489798+00:00_

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

_source line 2565 · 2026-05-21T17:45:02.590650+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where the elimination of type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}). The pattern is stable across three seeds (max $\Delta = 10.7$\,pp, within 1\,SD; intra-batch variance exceeds inter-seed variance by ${>}$5$\times$; Appendix~\ref{app:variance-decomposition}). Formal trend analysis confirms monotonic RE decline (Jonckheere-Terpstra $J = 109{,}707$, $p < 0.001$). Count curves establish trend direction; magnitude estimation relies on the higher-powered BCS-controlled experiments (\S\ref{sec:bcs_controlled}).
10	
11	\subsection{Pairwise Confusability and Type Confusion}
12	\label{sec:pairwise}
13	
14	We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$) and correlate it with $\text{SCS}(t_i, t_j)$. Table~\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\% CIs.
15	
16	\begin{table}[t]
17	\centering
18	\small
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{llrrrrr}
21	\toprule
22	\textbf{Dataset} & \textbf{Embed.} & \textbf{$n$ pairs} & \textbf{$r$} & \textbf{$r^2$} & \text
…[truncated 10771 chars]

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

_source line 2566 · 2026-05-21T17:45:07.359085+00:00_

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

_source line 2567 · 2026-05-21T17:45:08.362941+00:00_

1	\enlargethispage{3\baselineskip}
2	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
3	\label{sec:sdgd}
4	
5	A natural intervention is to partition the schema so confusable types never co-occur. We test \textbf{Schema-DAG-Guided Decomposition} (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches.
6	
7	\paragraph{NER and ED: merge amplification.}
8	All decomposition modes fall below the single-pass NER baseline (F1\,=\,0.445): SDGD obtains 0.251, random batching 0.320. The core failure is \emph{merge amplification}: presenting text $k$ times collapses precision (0.563$\to$0.210--0.249). MAVEN event detection replicates this (precision 0.287$\to$0.091; Appendix~\ref{sec:appendix_sdgd}).
9	
10	\paragraph{RE: routing failure.}
11	Oracle routing recovers accuracy (0.802 vs.\ 0.504 single-pass; Table~\ref{tab:batch_composition}), but confusability-aware grouping yields only +1.4\,pp over random ($p \approx 0.19$, n.s.). All practical routing strategies fall below the single-pass baseline (Appendix~\ref{sec:appendix_routing}).
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 1003
}
```

</details>

---


### Tool call

_source line 2568 · 2026-05-21T17:45:08.413644+00:00_

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

_source line 2569 · 2026-05-21T17:45:08.567082+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions and mechanisms.}
5	The decomposition applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). RE effects replicate across four models (8B--70B; Gemini Flash), two formats, five prompts, and two RE datasets; the NER null is confirmed on three models spanning two architecture families. Individually weak pairwise signals ($R^2 {=}\, 1.3\%$) compound into operationally significant batch effects ($R^2 {=}\, 22\text{--}58\%$)---a pattern not previously quantified in IE. The NER--RE asymmetry reveals structurally different error modes: RE errors arise from type-label confusion, while NER errors stem from span-boundary decisions independent of label similarity \citep{tam-2024-let-me-speak,schall-2025-hidden-cost}, with implications for task-specific mitigation.
6	
7	\paragraph{Practical implications and conclusion.}
8	\label{sec:conclusion}
9	For NER, reducing candidate types per prompt is the primary lever. For RE, BCS is a pre-hoc diagnostic: high type-pair similarity (SCS${}\,>\,0.85$) flags degradation without runs, and 22--58\% explained variance means BCS anticipates roughly half of cross-schema variation at zero annotation cost. Na\"{i}ve decompose-then-merge fails (\S\ref{sec:sdgd}), but oracle routing recovers substantial accuracy (72.4\% vs.\ 50.4\%), motivating routing-aware decomposition. In sum, extraction degrades along two separable dimensions---count-driven recall decline and confusability-driven type substitution---replicated across four RE models; NER null on three (8B--70B).
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 2570 · 2026-05-21T17:45:08.567559+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "150"
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
    "offset": "150"
  }
}
```

</details>

---


### Tool result

_source line 2571 · 2026-05-21T17:45:08.869611+00:00_

150	Oracle routing (Table~\ref{tab:routing_strategies}) recovers substantial accuracy (72.4\% vs.\ 50.4\% single-pass), confirming the sub-schemas contain correct predictions; the failure lies in routing, not decomposition quality.
151	
152	We compare four modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, the extreme case where each type is extracted in isolation.
153	
154	Single-pass extraction achieves F1\,=\,0.445 (P\,=\,0.563, R\,=\,0.368). SDGD obtains F1\,=\,0.251 (P\,=\,0.210, R\,=\,0.314), a 44\% relative drop. Random batching reaches F1\,=\,0.320 (P\,=\,0.249, R\,=\,0.446), and per-type extraction yields F1\,=\,0.292 (P\,=\,0.194, R\,=\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\ref{tab:sdgd_results}).
155	
156	\begin{table}[h]
157	\centering
158	\small
159	\resizebox{\columnwidth}{!}{%
160	\begin{tabular}{lrccc}
161	\toprule
162	\textbf{Mode} & \textbf{\# Batches} & \textbf{Precision} & \textbf{Recall} & \textbf{F1} \\
163	\midrule
164	single\_pass & 1 & 0.563 & 0.368 & 0.445 \\
165	\midrule
166	sdgd\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\
167	random\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\
168	per\_type & 66 & 0.194 & 0.586 & 0.292 \\
169	\midrule
170	sdgd\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\
171	random\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\
172	\bottomrule
173	\end{tabular}}
174	\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \texttt{min\_batch\_size=8} (reducing 8$\to$4 batches for sdgd\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}
175	\label{tab:sdgd_results}
176	\end{table}
177	
178	Decomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). W
…[truncated 62388 chars]

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

_source line 2572 · 2026-05-21T17:45:14.642250+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "decisions.yaml"
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
    "file": "decisions.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2573 · 2026-05-21T17:45:16.049292+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/decisions.yaml\", \"content\": \"_next_id: 69\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 16:10 UTC\\n  summary: 项目立项，MVP 验证方案：Experiment 2 (Confusability Controlled) 为核心验证实验\\n  rationale: 'IDEA_BRIEF 的核心假设是 type confusability 独立于 type count 驱动 LLM IE 质量下降。Experiment\\n    2（固定 count 变 BCS）是最直接的假设检验。Pass 标准: |r|≥0.3 且 p<0.05。ACE05 RE + Few-NERD 双数据集验证。ARR\\n    May 25 DDL（11天），MVP 需 1-2 天完成。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 16:15 UTC\\n  summary: 修正 MVP 统计设计：random samples 从 10 增至 25/档，加入 per-type solo baseline 控制变量，核心指标改为\\n    Δ(solo_F1 - batch_F1)\\n  rationale: Reviewer 指出 n=12 下 |r|=0.3 对应 p≈0.34，无法同时满足 |r|≥0.3 且 p<0.05。增至 25 random\\n    batches/档 → n≈54，|r|≥0.27 即可达 p<0.05。同时加入 solo F1 控制 type 固有难度，避免将\\\"类型本身难抽取\\\"误归因于\\\"confusability\\n    效应\\\"。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 23:11 UTC\\n  summary: MVP 分析方法从 Δ(solo-batch) 切换到 within-count Pearson r(F1, BCS)，pass 标准更新为\\n    |r|≥0.3 at fixed count\\n  rationale: Exp 1 发现 count curve 方向反转（F1 随 count 上升），根因是低 count 时模型过度 hallucinate（pred/gold=8x\\n    at count=1）。solo baseline 处于极端行为模式，Δ 被跨 count 行为差异污染。改为 within-count 对比更干净：同一\\n    count 下比较不同 BCS 的 F1，直接检验 confusability 独立效应。\\n  related_experiments:\\n  - exp_id: exp001_count_baseline\\n    role: evidence\\n    result: count curve reversed, hallucination at low count\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 23:31 UTC\\n  summary: MVP 主指标更新为 within-count r(recall, BCS)，F1 因 over-prediction confound 降为补充指标\\n  rationale: Exp 1 text-match 重评估发现：recall 单调下降（0.72→0.42，符合预期），precision 单调上升（0.11→0.52，over-prediction\\n    减少），F1 受 precision 主导而反转。within-count 分析中 precision confound 在同一 count 下近似恒定，F1\\n    仍可用；但 recall 更干净且直接反映 type confusion。WrongType 错误（text 正确但 type 错标）随 count 从 0\\n    升至 2434，直
…[truncated 10865 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1407
}
```

</details>

---


### Tool call

_source line 2574 · 2026-05-21T17:45:16.603197+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if paper PDF exists"
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if paper PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 2575 · 2026-05-21T17:45:17.055038+00:00_

-rw-r--r-- 1 ubuntu ubuntu 479097 May 21 17:45 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 2576 · 2026-05-21T17:45:17.207637+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent/config.yaml 2>/dev/null | head -100",
  "description": "Check project config for external review settings"
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
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent/config.yaml 2>/dev/null | head -100",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 2577 · 2026-05-21T17:45:17.258319+00:00_

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

_source line 2578 · 2026-05-21T17:45:41.669049+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null",
  "description": "Find project config file"
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
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 2579 · 2026-05-21T17:45:41.770030+00:00_

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

_source line 2580 · 2026-05-21T17:45:41.770506+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
  "pages": "1-9"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
    "pages": "1-9"
  }
}
```

</details>

---


### Tool result

_source line 2581 · 2026-05-21T17:45:42.426417+00:00_

PDF pages extracted: 9 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf (468.4KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 655
}
```

</details>

---


### Tool call

_source line 2582 · 2026-05-21T17:47:07.203433+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR May 2026 提交）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，正文 8 页，参考文献不限，Limitations 章节必须有但不计入页数\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind\n- **ARR Overall Assessment 评分**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n### 论文路径\n- LaTeX: `projects/schema-dag-extraction/docs/paper/main.tex`（main.tex 通过 `\\input{}` 引用各章节文件：abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf`\n\n### 你的审查侧重：方法严谨性\n\n请重点审查以下方面：\n\n1. **实验设计质量**：\n   - Count curves 和 BCS-controlled 两套实验范式是否互补完整\n   - BCS-controlled 实验中 extreme batch 的构建方式（greedy search）是否引入偏差\n   - Within-pool analysis 是否充分控制了 pool composition confound\n   - DocRED 仅 5 batches/level（count curves）是否 power 不足\n   - MAVEN 仅作为 supplementary 角色是否合理（centrality confound 的处理）\n\n2. **统计方法**：\n   - TOST 等价性检验的 margin 选择（±3pp）是否有循环论证嫌疑（margin 来自 BCS 自身预测力？）\n   - Logit-scale TOST inconclusive 但论文仍以 linear-scale 为主——这是否 cherry-picking\n   - Bootstrap CI 是否适用于这些数据结构（batch 内 types 共享 prompt context，非独立）\n   - Pairwise r² 极低（1.3-1.7%），aggregation 到 batch-level R²=22-58% 的 Monte Carlo simulation 假设是否合理（非独立性讨论是否充分）\n   - Multiple comparisons：论文声称 cross-dataset 比较是独立 replication 不需 correction——是否成立\n   - 偏相关分析（controlling for centrality）：DocRED VIF=50.9 说明 BCS-centrality 高度共线，偏相关可靠吗\n\n3. **跨模型验证**：\n   - 主模型 Qwen3-32B 的全部分析是否在其他模型上充分验证\n   - Gemini count-16 结果依赖单个 leverage point（leave-one-out 后 r 从 -0.80 降到 -0.42）——是否需要更多数据\n   - LLaMA-70B FP8 量化可能引入额外噪声——是否讨论充分\n   - 4 个模型跨 3 个架构家族——但 proprietary (Gemini) 仅验证了部分实验\n\n4. **NER null 的解释**：\n   - NER batch-level BCS null 是 genuine absence 还是 power 不足（BCS range 受限）\n   - Power analysis 报告 minimum detectable |r|=0.132，但 FewRel attenuated r=-0.111——这说明什么\n   - Relaxed matching 实验是否充分排除了 metric artifact\n\n5. **可重复性**：\n   - 单种子 + greedy decoding 的设计是否充分（residual SD=0.88pp 来自 FP8 量化非确定性）\n   - 是否提供了足够的实验细节供复现\n\n### 输出格式\n请按以下结构输出审稿意见：\n\n```\n## Summary（2-3句）\n\n## Strengths（逐条，标 S1/S2/...）\n\n## Weaknesses（逐条，标 W1/W2/...，每条标注 severity: Must-Fix / Should-Fix / Minor）\n\n## Questions（需要作者回答的问题）\n\n## Missing References（如有遗漏的重要相关工作）\n\n## Overall Assessment\n- Score: [1-5, 参照 ARR Overall Assessment]\n- Confidence: [1-5]\n- 简要理由\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "schema-dag-extraction",
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR May 2026 提交）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，正文 8 页，参考文献不限，Limitations 章节必须有但不计入页数\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind\n- **ARR Overall Assessment 评分**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n### 论文路径\n- LaTeX: `projects/schema-dag-extraction/docs/paper/main.tex`（main.tex 通过 `\\input{}` 引用各章节文件：abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf`\n\n### 你的审查侧重：方法严谨性\n\n请重点审查以下方面：\n\n1. **实验设计质量**：\n   - Count curves 和 BCS-controlled 两套实验范式是否互补完整\n   - BCS-controlled 实验中 extreme batch 的构建方式（greedy search）是否引入偏差\n   - Within-pool analysis 是否充分控制了 pool composition confound\n   - DocRED 仅 5 batches/level（count curves）是否 power 不足\n   - MAVEN 仅作为 supplementary 角色是否合理（centrality confound 的处理）\n\n2. **统计方法**：\n   - TOST 等价性检验的 margin 选择（±3pp）是否有循环论证嫌疑（margin 来自 BCS 自身预测力？）\n   - Logit-scale TOST inconclusive 但论文仍以 linear-scale 为主——这是否 cherry-picking\n   - Bootstrap CI 是否适用于这些数据结构（batch 内 types 共享 prompt context，非独立）\n   - Pairwise r² 极低（1.3-1.7%），aggregation 到 batch-level R²=22-58% 的 Monte Carlo simulation 假设是否合理（非独立性讨论是否充分）\n   - Multiple comparisons：论文声称 cross-dataset 比较是独立 replication 不需 correction——是否成立\n   - 偏相关分析（controlling for centrality）：DocRED VIF=50.9 说明 BCS-centrality 高度共线，偏相关可靠吗\n\n3. **跨模型验证**：\n   - 主模型 Qwen3-32B 的全部分析是否在其他模型上充分验证\n   - Gemini count-16 结果依赖单个 leverage point（leave-one-out 后 r 从 -0.80 降到 -0.42）——是否需要更多数据\n   - LLaMA-70B FP8 量化可能引入额外噪声——是否讨论充分\n   - 4 个模型跨 3 个架构家族——但 proprietary (Gemini) 仅验证了部分实验\n\n4. **NER null 的解释**：\n   - NER batch-level BCS null 是 genuine absence 还是 power 不足（BCS range 受限）\n   - Power analysis 报告 minimum detectable |r|=0.132，但 FewRel attenuated r=-0.111——这说明什么\n   - Relaxed matching 实验是否充分排除了 metric artifact\n\n5. **可重复性**：\n   - 单种子 + greedy decoding 的设计是否充分（residual SD=0.88pp 来自 FP8 量化非确定性）\n   - 是否提供了足够的实验细节供复现\n\n### 输出格式\n请按以下结构输出审稿意见：\n\n```\n## Summary（2-3句）\n\n## Strengths（逐条，标 S1/S2/...）\n\n## Weaknesses（逐条，标 W1/W2/...，每条标注 severity: Must-Fix / Should-Fix / Minor）\n\n## Questions（需要作者回答的问题）\n\n## Missing References（如有遗漏的重要相关工作）\n\n## Overall Assessment\n- Score: [1-5, 参照 ARR Overall Assessment]\n- Confidence: [1-5]\n- 简要理由\n```"
  }
}
````

</details>

---


### Tool result

_source line 2583 · 2026-05-21T17:47:32.218282+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 25014
}
```

</details>

---


### Tool call

_source line 2584 · 2026-05-21T17:47:32.420035+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 格式合规）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR May 2026 提交）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，正文 8 页，参考文献不限，Limitations 章节必须有但不计入页数\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind\n- **ARR Overall Assessment 评分**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n- **重要规则**: ARR Responsible NLP Checklist 在 OpenReview submission form 里填写，不是写在论文 PDF 里\n\n### 论文路径\n- LaTeX: `projects/schema-dag-extraction/docs/paper/main.tex`（main.tex 通过 `\\input{}` 引用各章节文件：abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf`\n\n### 你的审查侧重：新颖性 / 完整性 / 格式合规\n\n请重点审查以下方面：\n\n1. **Novelty Framing**：\n   - SCS（pairwise cosine similarity of type name embeddings）与 LLM-PEE 的 partitioning criterion 形式上完全一致——论文如何定位自己的 novelty？是否足够\n   - \"first controlled study\" 的 claim 是否 justified（有无其他 controlled study 被忽略）\n   - 核心贡献是实验范式（controlled experiments）而非方法创新——对 EMNLP 2026 这是否足够\n   - 负面结果（SDGD 失败、renaming 反效果、few-shot 扩大 gap）的 framing 是否有价值\n   - 22-58% R² 是 non-obvious finding 还是预期之内\n\n2. **Related Work 完整性**：\n   - 是否遗漏了重要的 schema complexity / LLM IE 相关工作\n   - 与 label confusion / confusability 在 CV、NLP 其他子领域的工作对比是否充分\n   - Concurrent work 的处理是否得当（Chen et al. 2026, Vandemoortele et al. 2025, etc.）\n   - 是否需要引用更多 document-level RE 的相关工作\n\n3. **Writing Quality**：\n   - Abstract 是否准确反映论文核心发现（注意 task-dependent qualifier）\n   - Introduction 的 RQ 设置与实际实验结果的对应是否清晰\n   - 正文叙事密度——是否有 reader 难以跟进的地方\n   - 因果语言（causal language）的使用是否谨慎（\"predicts\" vs \"causes\"）\n   - 数字和统计结果的呈现是否过密（reader 能否有效处理如此多的数字）\n   - Discussion 是否充分讨论了 implications 和 future directions\n\n4. **Format 合规**（EMNLP 2026 严格要求）：\n   - **页数**：正文（Section 1 到 Discussion and Conclusion）是否 ≤ 8 页。注意检查是否使用了 `\\enlargethispage` 等 formatting hacks\n   - **Limitations 章节**：是否存在、内容是否充实（覆盖 3 个点左右即可）、是否放在正确位置\n   - **匿名性**：是否有 de-anonymization 风险（自引、GitHub 链接、致谢等）\n   - **Checklist**：论文 PDF 中是否包含 Responsible NLP Research Checklist（注意：按规则应在 OpenReview 表单填写，不应在 PDF 中出现）\n   - **模板合规**：字体大小、margin、双栏格式等\n   - **引用格式**：是否一致，是否有格式错误\n\n5. **Limitations 质量**：\n   - 当前 Limitations 是否坦诚地覆盖了论文的主要限制\n   - 是否有被遗漏的重要 limitation\n   - 长度是否适当（不需要写得很长，3 个点左右即可）\n\n### 输出格式\n请按以下结构输出审稿意见：\n\n```\n## Summary（2-3句）\n\n## Strengths（逐条，标 S1/S2/...）\n\n## Weaknesses（逐条，标 W1/W2/...，每条标注 severity: Must-Fix / Should-Fix / Minor）\n\n## Questions（需要作者回答的问题）\n\n## Missing References（如有遗漏的重要相关工作）\n\n## Overall Assessment\n- Score: [1-5, 参照 ARR Overall Assessment]\n- Confidence: [1-5]\n- 简要理由\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "schema-dag-extraction",
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 格式合规）\n\n### Venue 信息\n- **目标会议**: EMNLP 2026（通过 ARR May 2026 提交）\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，正文 8 页，参考文献不限，Limitations 章节必须有但不计入页数\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**: Double-blind\n- **ARR Overall Assessment 评分**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n- **重要规则**: ARR Responsible NLP Checklist 在 OpenReview submission form 里填写，不是写在论文 PDF 里\n\n### 论文路径\n- LaTeX: `projects/schema-dag-extraction/docs/paper/main.tex`（main.tex 通过 `\\input{}` 引用各章节文件：abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, sdgd_negative.tex, discussion.tex）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf`\n\n### 你的审查侧重：新颖性 / 完整性 / 格式合规\n\n请重点审查以下方面：\n\n1. **Novelty Framing**：\n   - SCS（pairwise cosine similarity of type name embeddings）与 LLM-PEE 的 partitioning criterion 形式上完全一致——论文如何定位自己的 novelty？是否足够\n   - \"first controlled study\" 的 claim 是否 justified（有无其他 controlled study 被忽略）\n   - 核心贡献是实验范式（controlled experiments）而非方法创新——对 EMNLP 2026 这是否足够\n   - 负面结果（SDGD 失败、renaming 反效果、few-shot 扩大 gap）的 framing 是否有价值\n   - 22-58% R² 是 non-obvious finding 还是预期之内\n\n2. **Related Work 完整性**：\n   - 是否遗漏了重要的 schema complexity / LLM IE 相关工作\n   - 与 label confusion / confusability 在 CV、NLP 其他子领域的工作对比是否充分\n   - Concurrent work 的处理是否得当（Chen et al. 2026, Vandemoortele et al. 2025, etc.）\n   - 是否需要引用更多 document-level RE 的相关工作\n\n3. **Writing Quality**：\n   - Abstract 是否准确反映论文核心发现（注意 task-dependent qualifier）\n   - Introduction 的 RQ 设置与实际实验结果的对应是否清晰\n   - 正文叙事密度——是否有 reader 难以跟进的地方\n   - 因果语言（causal language）的使用是否谨慎（\"predicts\" vs \"causes\"）\n   - 数字和统计结果的呈现是否过密（reader 能否有效处理如此多的数字）\n   - Discussion 是否充分讨论了 implications 和 future directions\n\n4. **Format 合规**（EMNLP 2026 严格要求）：\n   - **页数**：正文（Section 1 到 Discussion and Conclusion）是否 ≤ 8 页。注意检查是否使用了 `\\enlargethispage` 等 formatting hacks\n   - **Limitations 章节**：是否存在、内容是否充实（覆盖 3 个点左右即可）、是否放在正确位置\n   - **匿名性**：是否有 de-anonymization 风险（自引、GitHub 链接、致谢等）\n   - **Checklist**：论文 PDF 中是否包含 Responsible NLP Research Checklist（注意：按规则应在 OpenReview 表单填写，不应在 PDF 中出现）\n   - **模板合规**：字体大小、margin、双栏格式等\n   - **引用格式**：是否一致，是否有格式错误\n\n5. **Limitations 质量**：\n   - 当前 Limitations 是否坦诚地覆盖了论文的主要限制\n   - 是否有被遗漏的重要 limitation\n   - 长度是否适当（不需要写得很长，3 个点左右即可）\n\n### 输出格式\n请按以下结构输出审稿意见：\n\n```\n## Summary（2-3句）\n\n## Strengths（逐条，标 S1/S2/...）\n\n## Weaknesses（逐条，标 W1/W2/...，每条标注 severity: Must-Fix / Should-Fix / Minor）\n\n## Questions（需要作者回答的问题）\n\n## Missing References（如有遗漏的重要相关工作）\n\n## Overall Assessment\n- Score: [1-5, 参照 ARR Overall Assessment]\n- Confidence: [1-5]\n- 简要理由\n```"
  }
}
````

</details>

---


### Tool result

_source line 2585 · 2026-05-21T17:47:34.094554+00:00_

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


### Tool call

_source line 2586 · 2026-05-21T17:47:34.094985+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "schema-dag-extraction",
  "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "schema-dag-extraction",
    "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
  }
}
```

</details>

---


### Tool call

_source line 2587 · 2026-05-21T17:47:35.257369+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "schema-dag-extraction",
  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
  "venue": "EMNLP 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "schema-dag-extraction",
    "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
    "venue": "EMNLP 2026"
  }
}
```

</details>

---


### Tool call

_source line 2588 · 2026-05-21T17:47:35.257785+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

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
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 2589 · 2026-05-21T17:47:35.924292+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 1829
}
```

</details>

---


### Tool result

_source line 2590 · 2026-05-21T17:47:36.626463+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 1369
}
```

</details>

---


### Tool result

_source line 2591 · 2026-05-21T17:47:36.677032+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-21T17:47:36.554989+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_51326259fe46fbae9da26b81cf03f1f8\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1419
}
```

</details>

---


### Assistant

_source line 2592 · 2026-05-21T17:47:57.989049+00:00_

**审稿圆桌已启动，当前状态：**

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性） | ✅ 已派发，审稿中 |
| Reviewer 2（新颖性/完整性/格式） | ✅ 已派发，审稿中 |
| 视觉审查 Agent | ✅ 已启动，并行运行 |
| 外部审稿（Stanford Agentic Reviewer） | ✅ 请求已发送，等待用户提交 |

**Venue 确认：**
- ARR May 2026 submission deadline: **2026-05-25**（距今 4 天）✓
- Long paper 8 页正文 + 无限参考文献 + Limitations 不计页数
- Double-blind, ACL template

等待两位 Reviewer 完成独立初审后，进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 210

## Round 210

2 recorded events


### User

_source line 2593 · 2026-05-21T17:52:23.489261+00:00_

[Reviewer 1 审稿意见]:
## Round 1 审稿意见 — Reviewer 1（方法严谨性）

### Paper Summary（2-3句）

本文研究 schema 复杂度如何影响 training-free LLM 信息抽取性能。提出 Schema Confusability Score (SCS/BCS) 量化类型间嵌入相似度，通过 count curves 和 BCS-controlled 两套互补实验范式，在 4 个数据集（Few-NERD, FewRel, DocRED, MAVEN）和 4 个模型上进行系统分析。核心发现是性能退化沿两个维度展开：count-driven recall decline 和 confusability-driven type substitution，且 BCS 可解释 22–58% 的 batch-level RE 准确率方差。

---

### Strengths

**S1. 研究问题重要且新颖。** 这是首个系统隔离 type count 与 type confusability 对 zero-shot LLM IE 性能影响的控制研究。现有工作（LLM-PEE, CrossAgentIE 等）观察到 schema 变大时性能下降，但未分离出具体因素。本文的 confusability-aware 视角填补了一个重要的认知空白，对 IE schema 设计有直接实践指导意义。

**S2. 两套实验范式互补且设计巧妙。** Count curves 控制 count 变化观察退化趋势，BCS-controlled 实验固定 count 变化 BCS 观察 confusability 效应——这种交叉设计比单一 correlational study 更有说服力。特别是 BCS-controlled 的 extreme batch 构建（greedy search on SCS graph）是一个有创意的实验手段（§3.3, Appendix A）。

**S3. 分析极为详尽，敏感性检验充分。** 28 页含 18 个附录，涵盖 TOST 等价性检验（Appendix C）、Monte Carlo simulation（Appendix N）、prompt sensitivity（Appendix H）、within-pool analysis（Appendix D）、label renaming intervention（Appendix X）、relaxed matching（Appendix Y）等。这种分析深度在 empirical NLP 论文中少见。

**S4. 诚实的 null result 报告。** NER batch-level BCS null（§4.2, §5）和 MAVEN centrality confound（§4.5, Appendix E）均未被掩饰，而是做了详细的 power analysis 和 confound analysis。这种学术诚实值得肯定。

**S5. SCS/BCS 指标有清晰的操作化定义和独立于 type composition 的验证。** Appendix O 的 joint model 分析（BCS unique R²=0.259 vs composition unique R²=0.299, VIF=1.06）有力地支持了 BCS 确实捕获了 confusability-specific signal。

**S6. Schema Decomposition 的负面结果（§5）有建设性意义。** SDGD 方法的系统失败分析（merge amplification + routing failure）不仅报告了 negative result，还提供了机制解释，对后续 schema decomposition 研究有参考价值。

---

### Weaknesses

**W1 [Must-Fix] Logit-scale TOST inconclusive 但论文以 linear-scale 为主要结论——存在 cherry-picking 嫌疑。**
- 具体位置：Appendix C（p.16），§4.1
- 问题：论文在 Appendix C 坦承 logit-scale TOST 在 count×BCS interaction 上 inconclusive（p=0.25），但将 linear-scale TOST 作为 primary analysis（p=0.047 at ±2pp, p=0.063 at ±3.3pp）。对于 bounded accuracy data（0–1），logit-scale 是统计学上更合适的尺度（variance stabilization, homoscedasticity）。论文将 logit 结果降格为 "sensitivity check" 而将 linear 结果作为主要发现，需要更充分的方法论辩护。
- 为什么影响接收：这直接关系到核心 claim 之一（count×BCS interaction bounded）的统计支撑。如果 logit-scale 下 interaction 不可排除实际意义，则 "BCS effect 不随 count 放大" 的结论被削弱。
- 建议修改方向：(a) 在正文中直接报告 logit-scale 结果并讨论两种尺度的差异，而非仅在附录中提及；(b) 提供明确的统计理由说明为何 linear-scale 是合理的 primary analysis（例如，如果 accuracy 远离 0/1 边界，logit 变换的优势较小）；(c) 或者将结论弱化为 "linear-scale 下 equivalent，logit-scale 下 inconclusive"。

**W2 [Must-Fix] DocRED 偏相关分析在 VIF=50.9 下不可靠。**
- 具体位置：Appendix E, Table 11
- 问题：DocRED 的 BCS-centrality collinearity 达到 VIF=50.9（r=0.99），标准误膨胀约 7.1 倍。在此条件下，偏相关估计极不稳定——微小的数据扰动就能大幅改变偏相关系数。论文称 "BCS retains predictive value but does not uniquely identify the causal channel"，但 VIF=50.9 下甚至偏相关系数本身的 point estimate 都不可靠。
- 为什么影响接收：这影响 BCS 在 document-level RE 上的可解释性 claim。如果 BCS 和 centrality 在 DocRED 上完全混淆，就无法声称 BCS 在此数据集上有独立预测力。
- 建议修改方向：(a) 对 DocRED 偏相关的结论大幅弱化，直接承认 BCS 和 centrality 在 DocRED 上 inseparable；(b) 补充 ridge regression 或其他 regularization 方法来处理多重共线性；(c) 或者将 DocRED centrality 分析的 claim 限缩为 "descriptive, not inferential"。

**W3 [Must-Fix] Gemini leverage point 削弱跨架构泛化声明。**
- 具体位置：Appendix U（p.25-26），Table 23-24
- 问题：Gemini 2.5 Flash 的 BCS-controlled 结果（count 16）依赖单个极端 batch（BCS=0.97, accuracy 59.9%）。Leave-one-out 后相关系数可能显著下降（论文提到 count 8 gap 比 Qwen3-32B 小）。作为唯一的 proprietary model，Gemini 仅验证了部分实验（FewRel count curves + 部分 BCS-controlled），且存在 API-based 访问的不可控因素。
- 为什么影响接收：论文声称 "跨三个架构家族验证"（§1, Contribution 2），但 proprietary model 的验证最薄弱。单个 leverage point 驱动的相关性不足以支撑 "跨架构 robust" 的结论。
- 建议修改方向：(a) 正文中明确报告 Gemini leave-one-out sensitivity，不仅在附录；(b) 弱化跨架构泛化的措辞，明确区分 "open-weight models 一致复现" 与 "proprietary model 部分支持"；(c) 如果可行，在 Gemini 上增加更多 count levels 的 BCS-controlled batches 以消除 leverage 依赖。

**W4 [Should-Fix] TOST 等价性 margin（±3pp）的部分循环论证。**
- 具体位置：Appendix C（p.16）
- 问题：论文提出三个 converging arguments 支持 ±3pp margin：(1) IQR-predicted Δ=2.2pp from BCS effect itself, (2) 3.43pp = 100% amplification, (3) Cohen's d = 0.35 × within-cell SD = 4.6pp → ±2.3pp。其中 argument (1) 直接引用了 BCS 效应自身的 effect size 来确定 margin——这构成 "用被检验量的 effect size 确定检验 margin" 的逻辑循环。
- 建议：删除 argument (1) 或明确标注其循环性质；仅依赖 (2)(3) 两个外部标准也足以支持 ±3pp margin。

**W5 [Should-Fix] Bootstrap CI 在 non-independence 结构下的有效性讨论不足。**
- 具体位置：§3.5, Appendix N
- 问题：同一 batch 内的 types 共享 prompt context（in-context 示例、JSON schema），bootstrap resample 的独立性假设在 batch 内部被违反。论文在 Appendix N 讨论了 pair-to-batch aggregation 的 ecological inference 问题（引用 Robinson, 1950），但未正式讨论 bootstrap percentile CI 在 batch-level 相关残差结构下的 coverage property。如果 batch-level residuals 存在 model/prompt-induced 的 across-batch correlation，bootstrap CI 可能 undercover。
- 建议：(a) 讨论 bootstrap CI 的 coverage guarantee 在非独立数据下的 known limitations；(b) 补充 cluster-robust standard errors 或 block bootstrap 作为 robustness check。

**W6 [Should-Fix] Pair-level r²=1.3-1.7% 到 batch-level R²=22-58% 的放大效应需要更突出的 caveats。**
- 具体位置：§4.2, §4.3, Appendix N
- 问题：从 pairwise r²≈1.5% 到 batch R²≈22% 的 ~15× 放大本质上是 ecological correlation（Simpson's paradox 的反面）。Appendix N 的 Monte Carlo simulation 提供了分析解释（EF≈3.35），但这一放大的前提是 batch-level aggregation 的因果合法性——即 batch mean BCS 确实是 causal driver 而非 collider。论文未充分讨论这一因果识别问题。
- 建议：在正文讨论 R²=22-58% 时加入显眼的 caveat：batch-level R² 不等同于 pair-level explanatory power，ecological correlation 需要额外的因果假设。

**W7 [Should-Fix] NER null 的解释存在内部张力。**
- 具体位置：§4.2, §5, Appendix E.2
- 问题：论文在 §5 将 NER 描述为 "structural barrier"（"schema decomposition fails... NER errors stem from span-boundary decisions independent of label similarity"），但在 Appendix E.2 的 power analysis 得出 "absence of evidence rather than evidence of absence"（80% power 需要 |r|≥0.132，而 attenuated r=−0.111 在此阈值之下）。这两个叙述存在张力：如果是 power 不足，就不能同时声称是 "genuine structural absence"。
- 建议：在正文中统一叙述——要么是 "power 受限下的 inconclusive"（需弱化 §5 和 §6 中 NER 作为 fundamental boundary 的措辞），要么提供额外证据支持 structural absence（如更大样本量的 NER 实验）。当前 "NER 是根本不同的" 与 "power 不足" 并存，读者会困惑。

**W8 [Should-Fix] DocRED count curves 仅 5 batches/level，统计效力不足。**
- 具体位置：Table 1, §3.3
- 问题：DocRED 每个 count level 仅 5 batches（vs Few-NERD 25, FewRel 8）。5×5=25 个数据点的回归对 noise 极为敏感。论文报告 DocRED 的 count-curve decline（−47pp per 34pp BCS decline），但这一估计的置信区间必然很宽。
- 建议：报告 DocRED count curve regression 的完整 confidence intervals；明确讨论 n=25 下的 effect size uncertainty。

**W9 [Should-Fix] 跨模型验证的不对称性。**
- 具体位置：§3.5, Appendix T-U, Table 3-5
- 问题：主模型 Qwen3-32B 有完整的 4 数据集 × 2 实验范式分析。但：(a) LLaMA-3.1-70B-Instruct FP8 仅验证了 FewRel count curves + BCS-controlled 和 Few-NERD NER；(b) Gemini 仅验证了 FewRel 部分实验（且有 leverage point 问题，见 W3）；(c) DocRED 和 MAVEN 的全部分析仅在 Qwen3-32B 上进行。这意味着论文最有趣的发现之一——document-level RE 的高 R²=58%——缺乏跨模型验证。
- 建议：(a) 明确标注哪些 findings 有跨模型支持、哪些仅基于单一模型；(b) 在 Limitations 中讨论 DocRED R²=58% 的单模型依赖性。

**W10 [Minor] Multiple comparisons 不做 correction 的理由可以更充分。**
- 具体位置：§4.2, §4.3
- 论文声称 cross-dataset 比较是 independent replication 不需 Bonferroni correction。但 Few-NERD 和 FewRel 共享 Wikidata 知识库来源，annotation guidelines 有相似性。如果效应来自共享的 schema 设计传统而非 general mechanism，"独立复现" 的假设就被削弱。
- 建议：简要讨论 datasets 的独立性程度。

**W11 [Minor] 单种子 + greedy decoding 的可复现性。**
- 具体位置：§3.5, Limitations §6
- Residual SD=0.88pp（count 80, FP8）说明量化非确定性引入了不可忽略的噪声。论文在 Limitations 中承认但未量化其对核心结论的影响（如 BCS-F1 correlation 的 bootstrap interval 是否 cover zero 如果加入 seed variation）。
- 建议：报告 2-3 个不同 seed 下关键 metric 的 variability，或至少讨论 0.88pp residual 相对于 BCS effect size（~2-5pp）的比例。

---

### Questions（需要作者回答）

**Q1.** Logit-scale TOST 在 ±3.5pp logit margin 下 interaction inconclusive（p=0.25）。作者能否解释为何 linear-scale 比 logit-scale 更适合作为 primary analysis？是否考虑过其他 variance-stabilizing transformations（如 arcsine）？

**Q2.** DocRED VIF=50.9 下的偏相关（Table 11）是否在 bootstrapped/permutation 框架下稳定？作者是否尝试过 ridge 或 elastic net 来处理这一共线性？

**Q3.** Gemini count-16 BCS-controlled 的 leave-one-out 后，Pearson r 和 p-value 的具体数值是什么？如果删除该 leverage point 后效应消失，作者如何维持 "跨架构 robust" 的声明？

**Q4.** 论文在 §5 和 §6 中将 NER 描述为 fundamental structural barrier，但 Appendix E.2 的 power analysis 表明 power 不足（65% at attenuated effect size）。作者倾向于哪种解释？是否有计划在更大样本量下验证 NER null？

**Q5.** Batch-level bootstrap CI（B=1,000）是否考虑了 batch-level residuals 的 potential clustering（来自共享 model + prompt template）？是否尝试过 cluster-robust SE 或 block bootstrap？

**Q6.** Pair-level r²=1.5% 而 batch-level R²=22%——作者是否认为 batch-level 的因果解释是合法的，还是认为这仅仅是一个有用的 descriptive pattern？如果是后者，§6 中 "confusability-aware schema design" 的实践建议是否过度推断？

**Q7.** Multiple comparisons：Few-NERD 和 FewRel 都源自 Wikidata，MAVEN 源自 FrameNet，DocRED 源自 Wikipedia——作者是否考虑过这些共享来源可能引入的 pseudo-replication？

---

### Missing References

1. **Robinson, W.S. (1950)** — 论文在 Appendix N 引用了 ecological correlation 问题，但正文讨论 batch-level R² 时未提及此经典警示。建议在正文中引用。
2. 无其他明显遗漏——Related Work（§2）覆盖了主要 zero-shot IE、schema complexity、LLM-PEE 等方向的核心工作。

---

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 实验设计有创意且大部分分析严谨，但 logit-scale TOST inconclusive（W1）、DocRED VIF=50.9（W2）、Gemini leverage point（W3）三个统计问题削弱了部分核心 claim 的 robustness。NER null 的叙述张力（W7）也需要统一。 |
| **Excitement** | 3.5/5 | 研究问题新颖且实用（schema complexity → IE performance），confusability 视角有潜力影响 IE schema 设计实践。但当前的 causal claim 力度受限于 ecological correlation 问题，实践指导（SDGD）以负面结果告终。 |
| **Reproducibility** | 4/5 | 实验细节充分（prompt templates in Appendix G, 模型版本和推理参数在 §3.5），承诺 release code/data。单种子 + greedy decoding 是一个小遗憾。 |
| **Confidence** | 4/5 | 我仔细检查了统计方法（TOST、bootstrap CI、偏相关、Monte Carlo simulation）和实验设计。对 ecological correlation 和 equivalence testing 有专业背景。 |

---

### Overall Assessment

- **Score: 3.5**（Borderline Conference）
- **Confidence: 4/5**

**简要理由：** 本文提出了一个重要且新颖的研究问题，实验设计有创造性（count curves + BCS-controlled 互补范式），分析深度在 empirical NLP 论文中出色（28 页，18 个附录）。主要优势在于系统地隔离了 type count 和 type confusability 两个退化维度，并在多数据集上展示了 BCS 的预测力。

然而，方法严谨性上有三个 Must-Fix 问题需要解决：(1) logit-scale TOST inconclusive 削弱了 count×BCS interaction bounded 的核心结论，当前以 linear-scale 为主的做法需要更强的方法论辩护；(2) DocRED VIF=50.9 下的偏相关不可靠，相关 claim 需要大幅弱化；(3) Gemini leverage point 削弱了跨架构泛化声明。此外，NER null 的双重叙述（structural absence vs power limitation）需要统一，pair-to-batch R² 放大的 ecological correlation caveat 需要更突出。

如果这三个 Must-Fix 问题得到妥善处理（主要是弱化过度声明、补充合理的 caveats），论文可以达到 Conference 水平。当前状态下，部分核心 claim 的统计基础不够稳固，建议 borderline accept 至 Findings。

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

_source line 2594 · 2026-05-21T17:52:30.719061+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 211

## Round 211

2 recorded events


### User

_source line 2595 · 2026-05-21T17:52:33.288053+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿概要：**
- **Overall: 3.5**（Borderline Conference），Confidence 4/5
- **3 个 Must-Fix 问题**：(1) logit-scale TOST inconclusive 但论文以 linear-scale 为主要结论；(2) DocRED 偏相关 VIF=50.9 下不可靠；(3) Gemini BCS-controlled 依赖单个 leverage point
- **6 个 Should-Fix 问题**：TOST margin 部分循环论证、Bootstrap CI 非独立性讨论不足、pair→batch R² 放大的 ecological correlation caveat、NER null 叙述张力、DocRED count curves 仅 5 batches/level、跨模型验证不对称
- **2 个 Minor**：multiple comparisons 理由可更充分、单种子+greedy decoding
- **核心判断**：研究问题新颖、实验设计有创意、分析深度优秀，但部分核心 claim 的统计基础存在裂缝，需要修订后可达 Conference 水平

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

_source line 2596 · 2026-05-21T17:52:39.960609+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 212

## Round 212

6 recorded events


### User

_source line 2597 · 2026-05-21T17:57:25.360573+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见（新颖性 / 完整性 / 格式合规）

### 论文信息
- **Title**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?
- **Venue**: EMNLP 2026 via ARR May 2026
- **审查依据**: ACL ARR Review Form（Soundness / Excitement / Reproducibility / Overall Assessment，均 1-5 with 0.5 increments）

---

## Summary（2-3句）

本文研究 training-free LLM IE 中 schema 复杂度对性能的影响，通过 Schema Confusability Score (SCS) 和 Batch Confusability Score (BCS) 在控制变量实验中将 type count 与 type confusability 解耦。实验覆盖 4 个数据集（Few-NERD, FewRel, DocRED, MAVEN）和 3 个 IE 任务（NER, RE, ED），发现降解沿两个维度运作（count→recall 下降，confusability→type 混淆），BCS 可解释 RE 中 22-58% 的 cross-batch 准确率方差，同时报告了 schema decomposition (SDGD) 失败的重要负面结果。

---

## Strengths

**S1**: **控制变量实验设计是核心贡献，且质量很高。** 通过构造 BCS-controlled batches（固定 type count、变化 confusability），论文干净地隔离了两个因素。这比先前工作（LLM-PEE, PARSE 等）的相关性分析严格得多。Quasi-experimental manipulation（Section 3.3, Experiment 2）加上 bootstrap CIs 和 permutation tests 确保了统计可靠性。

**S2**: **经验覆盖面广且深。** 4 个数据集 × 3 个 IE 任务 × 2 个 embedding 模型（Qwen3, MiniLM）× 3 个 LLM 架构的 cross-model validation（Appendices T, U），加上大量 robustness checks：prompt sensitivity（Appendix H）、format independence（Appendix K）、aggregation sensitivity（Appendix I）、BCS aggregation ablation（Appendix I, Table 14）。Appendix 的实验量远超主文，体现了实验的扎实程度。

**S3**: **负面结果诚实且有价值。** Section 5 的 SDGD 失败分析（merge amplification 和 routing failure）和 Appendix X 的 label renaming 负面结果（Table 29: renaming 降低 SCS 但反而损害准确率）为社区节省了大量试错成本。SDGD oracle routing（Table 8）恢复了大部分准确率，精准定位了 decompose-then-merge 范式的瓶颈。

**S4**: **两维降解分解概念清晰。** Dimension 1（count→recall decline）和 Dimension 2（confusability→type confusion）在 Figure 2 的 error taxonomy 分析中得到了直接的经验支撑——IntraSub 与 BCS 单调共变，而 NER missed rates 保持相对稳定。这为理解 LLM IE 降解提供了可操作的分析框架。

**S5**: **Limitations 部分坦诚全面。** 覆盖了 model coverage、effect size and statistical design、task scope、causal mechanism、data contamination、domain/language scope、multiple comparisons 共 7 个点，远超通常水平。

---

## Weaknesses

**W1** [Should-Fix] **SCS 相对于 LLM-PEE 的新颖性定位不够清晰**
- **具体位置**: Section 2 (Related Work, paragraph on SCS novelty) 和 Section 3.2 (SCS 定义)
- **问题**: LLM-PEE (Liu et al., 2025) 的 partitioning criterion 与 SCS 在形式上完全一致——都是基于 type name embeddings 的 pairwise cosine similarity。论文在 Section 2 承认了这一点（"our work uses the same metric for scientific analysis"），但这个区分在当前的 framing 中不够突出。读者很容易得出"SCS = LLM-PEE's criterion rebranded"的印象。
- **为什么影响评分**: 对于 novelty-sensitive 的 reviewer，metric 层面的重叠会削弱整体贡献评估。论文的真正新颖性在于 *experimental paradigm*（controlled batches, quasi-experimental manipulation, two-dimensional decomposition），而非 metric 本身。
- **建议**: 在 Section 2 或 Section 3.2 增加一段明确的 novelty statement，强调贡献不在于 SCS metric 本身（which parallels LLM-PEE），而在于：(1) 将其作为 analytical tool 嵌入控制变量框架；(2) batch-level aggregation (BCS) 的设计以及 BCS-controlled 实验范式。可以用一句话点明："While the pairwise SCS computation mirrors LLM-PEE's partitioning criterion, our contribution is the controlled experimental framework that uses BCS to isolate confusability's causal role."

**W2** [Should-Fix] **R² 的 task-dependent 弱信号在 abstract/intro 中表述不均衡**
- **具体位置**: Abstract（第1页）, Section 4.3, Table 5（第6页）
- **问题**: Abstract 突出了 "BCS explains 22–58% of cross-batch RE accuracy variance"，但对 NER 上 batch-level BCS-F1 相关性为 null 的结果（Table 5: Few-NERD Qwen3-32B r = 0.001, p = 0.94）缺乏同等prominence 的呈现。这造成了 framing asymmetry——读者从 abstract 获得的印象是"confusability is a strong predictor"，但实际上这只在 RE 上成立，NER 上 BCS 的解释力接近零。
- **为什么影响评分**: 这不是数据问题而是 framing 问题。如果 reviewer 认为 abstract 过度 claim，可能降低 soundness 评分。
- **建议**: Abstract 中在提到 22-58% R² 后立即加入 qualifier，如"while the NER batch-level signal is attenuated by task-specific factors (§4.3)"。Introduction 的 RQ1 回答部分也应同步调整。

**W3** [Should-Fix] **主实验依赖单一模型，跨模型验证深度不均**
- **具体位置**: Section 3.5 (Model and Inference), Appendices T, U
- **问题**: 所有 core experiments（count curves, BCS-controlled, error taxonomy, centrality analysis, SDGD）均使用 Qwen3-32B。Cross-model validation（Llama-3.1-70B Appendix T; Gemini 2.5 Flash Appendix U）仅复制了 count curves 和 BCS-controlled 两个实验，未涵盖 error taxonomy decomposition、centrality confound analysis、SDGD experiments。论文声称 findings "replicate across three architectures"（Section 6），但复制深度不对等。
- **为什么影响评分**: Reviewer 可能质疑 two-dimensional decomposition 和 SDGD failure 是否 model-specific。
- **建议**: (1) 至少在 Appendix T/U 中补充 Llama-3.1-70B 或 Gemini 上的 error taxonomy decomposition（IntraSub vs BCS 的单调性是否保持）；(2) 如果资源不允许，在 Limitations 中明确说明跨模型验证仅覆盖了 count curves 和 BCS-controlled 两个维度。

**W4** [Should-Fix] **Sections 5-6 过度压缩，叙事密度过高**
- **具体位置**: Page 8（Section 4.4 尾部 + Section 5 全文 + Section 6 全文）
- **问题**: 第 8 页承载了三个完整的分析板块：centrality confound 结论、SDGD 全部分析（failure modes, merge amplification, RE routing failure, 4 种 decomposition modes 的对比）、以及整个 Discussion and Conclusion。这导致 SDGD 的 failure analysis 感觉 post-hoc（只展示了"that it fails"而非充分解释"why"），Discussion 中的 practical implications 仅用一段话覆盖，且完全没有展开 future directions。
- **为什么影响评分**: Reviewer 可能认为 SDGD section 和 discussion 的分析深度不够，影响 excitement 评分。
- **建议**: 考虑将 Section 4.4（centrality confound）移入 appendix，为 Sections 5-6 腾出 ~0.5 页空间。Discussion 至少应包含：(1) 何时应/不应使用 schema decomposition 的 practical guidelines；(2) confusability-aware schema design 的具体建议；(3) 明确的 future work directions（如 learned decomposition, task-adaptive routing）。

**W5** [Minor] **数字/统计呈现密度过高，部分 reader 可能跟不上**
- **具体位置**: Sections 4.1-4.3（pages 6-7）
- **问题**: 例如 page 7 "Practical magnitude" 段落在约 8 行文字内包含 10+ 个统计值（r², p, IQR, bootstrap averages, Monte Carlo percentiles）。类似的高密度也出现在 page 6 的 Section 4.2（Pairwise Confusability and Type Confusion）。对于非统计学背景的 NLP reviewer，这些数字流可能导致 cognitive overload。
- **建议**: 将 per-dataset 的详细统计值移入 appendix table，正文只保留 headline numbers 和方向性结论。

**W6** [Minor] **Responsible NLP Research Checklist 出现在论文 PDF 中（pages 9-10）**
- **具体位置**: Pages 9-10, "Responsible NLP Research Checklist" section
- **问题**: 根据 EMNLP 2026/ARR 当前政策，Responsible NLP Checklist 应在 OpenReview submission form 中填写，而非包含在论文 PDF 中。论文中包含了完整的 checklist（Section A-E, pages 9-10），占用约 2 页空间。虽然 EMNLP 2025 曾宣布 accepted papers 将在发表时附带 checklist appendix，但 *submission* 阶段的 checklist 应在 form 中。
- **建议**: 从 PDF 中移除 checklist section，在 OpenReview form 中填写。这不会影响 page count（已在主文之外），但消除了潜在的格式合规风险。

**W7** [Minor] **2 个 orphan bibliography entries**
- **具体位置**: references.bib
- **问题**: `park-2024-grammar-aligned`（Grammar-Aligned Decoding）和 `zhou-2024-grasping`（Grasping the Essentials）在 .bib 中存在但未被论文正文引用。
- **建议**: 删除或引用。

---

## Questions

**Q1**: Pairwise SCS 相关性很弱（r ≈ 0.17, Table 2），但 batch-level R² 明显更高（22-58% on RE）。这种从 pair-level 到 batch-level 的 amplification 是单纯的 aggregation smoothing（noise averaging），还是存在 compositional effect（多个 confusable pairs 交互放大 confusion）？Appendix N 的 pair-to-batch simulation 似乎暗示前者，但能否排除后者？

**Q2**: Section 4.4 发现 MAVEN 上 BCS-F1 正相关完全归因于 centrality confound（Appendix E, Table 10-11）。这是否意味着 SCS/BCS 在 homogeneous schemas（单一 ontology，type 间语义距离较均匀）上不适用？如果是，这对论文的 generalizability 有何影响？

**Q3**: SDGD 失败（Section 5）的核心原因是 merge amplification。是否考虑过避免 merge 步骤的替代方案——如 hierarchical extraction（先粗分类再细分类）或 retrieval-augmented type selection？

**Q4**: Table 29（Appendix X）显示 renaming labels 降低 SCS 后反而损害准确率。这是因为 renamed labels 丢失了语义信息（模型依赖 label name 的 pre-training knowledge），还是因为 renaming 引入了 unfamiliar paraphrases 扰乱了模型的 type semantics？这个发现对 "confusability-aware schema design" 的 practical implication 至关重要。

**Q5**: 论文使用 Qwen3 和 MiniLM 两种 embeddings 计算 SCS，均 "directionally consistent"。对于 practitioners，应该用哪个？是否推荐使用 extraction model 自身的 embeddings（如 Qwen3）以更好地捕获 model-specific confusion patterns？

---

## Missing References

未发现 critical-level 的遗漏。以下为 potentially relevant 的补充建议：

1. **Hierarchical entity typing**: Ren et al. (2016) "AFET: Automatic Fine-Grained Entity Typing by Hierarchical Partial-Label Embedding"、Choi et al. (2018) "Ultra-Fine Entity Typing"——这些工作直接研究 type granularity/hierarchy 如何影响 typing 性能，与本文的 confusability 主题高度相关，但当前 Related Work 未涉及。
2. **In-context learning analysis**: Min et al. (2022) "Rethinking the Role of Demonstrations in In-Context Learning"——可为 few-shot prompting 下 confusability 的影响提供理论支撑。

这两类工作不影响论文的核心 claim，但可以增强 Related Work 的理论联系。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 控制变量设计严谨（BCS-controlled batches, bootstrap CIs, permutation tests），但 R² 在 NER 上接近 null（Table 5），单一主模型限制了 generalizability claims |
| **Excitement** | 3/5 | 研究问题重要且 understudied，two-dimensional decomposition 和 SDGD 负面结果有价值，但 SCS 与 LLM-PEE criterion 的形式重叠削弱了 perceived novelty，实际 impact 有限（decomposition 和 renaming 均失败） |
| **Reproducibility** | 4/5 | 实验细节详尽（模型版本、GPU 型号、vLLM 版本、prompt templates in Appendix G、evaluation metrics 定义清晰），承诺 release code and data upon acceptance |
| **Overall Assessment** | 3.5/5 | Borderline Conference |
| **Confidence** | 4/5 | 仔细阅读了全文（28页），熟悉 LLM IE 和 schema complexity 领域 |

---

## Overall Assessment

- **Score**: 3.5（Borderline Conference）
- **Confidence**: 4
- **简要理由**: 本文是一篇 well-executed 的经验分析论文，核心贡献在于控制变量实验范式（isolating count from confusability）而非方法创新。Strengths 包括：严格的实验设计、广泛的 empirical coverage（4 datasets × 3 tasks × 3 models）、诚实且有价值的负面结果（SDGD, renaming）、清晰的 two-dimensional degradation framework。Weaknesses 包括：SCS 与 LLM-PEE criterion 的形式重叠未充分区分、R² 在 NER 上接近 null 但 framing 中未充分 qualify、主实验依赖单一模型、Sections 5-6 过度压缩。论文是 Findings track 的 strong candidate，若能 (1) 更清晰地定位 novelty（experimental paradigm, not metric）并 (2) 在 abstract/intro 中平衡呈现 task-dependent 的弱信号，则有望达到 main conference 水准。

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

_source line 2598 · 2026-05-21T17:59:50.752352+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每一条 Weakness 和 Question，请标注：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别注意你与 Reviewer 1 在以下方面的潜在分歧或共识：\n1. Logit-scale TOST 作为 primary vs secondary analysis（R1-W1）\n2. DocRED VIF=50.9 的偏相关可靠性（R1-W2）\n3. Gemini leverage point 对跨架构声明的影响（R1-W3）\n4. NER null 的解释框架（R1-W7 vs 你对 task-dependent framing 的看法）\n5. Pair-to-batch R² 放大的因果合法性（R1-W6）\n\n---\n\n以下是 Reviewer 1 的完整审稿意见原文：\n\n### Strengths\n\n**S1. 研究问题重要且新颖。** 这是首个系统隔离 type count 与 type confusability 对 zero-shot LLM IE 性能影响的控制研究。现有工作（LLM-PEE, CrossAgentIE 等）观察到 schema 变大时性能下降，但未分离出具体因素。本文的 confusability-aware 视角填补了一个重要的认知空白，对 IE schema 设计有直接实践指导意义。\n\n**S2. 两套实验范式互补且设计巧妙。** Count curves 控制 count 变化观察退化趋势，BCS-controlled 实验固定 count 变化 BCS 观察 confusability 效应——这种交叉设计比单一 correlational study 更有说服力。特别是 BCS-controlled 的 extreme batch 构建（greedy search on SCS graph）是一个有创意的实验手段（§3.3, Appendix A）。\n\n**S3. 分析极为详尽，敏感性检验充分。** 28 页含 18 个附录，涵盖 TOST 等价性检验（Appendix C）、Monte Carlo simulation（Appendix N）、prompt sensitivity（Appendix H）、within-pool analysis（Appendix D）、label renaming intervention（Appendix X）、relaxed matching（Appendix Y）等。这种分析深度在 empirical NLP 论文中少见。\n\n**S4. 诚实的 null result 报告。** NER batch-level BCS null（§4.2, §5）和 MAVEN centrality confound（§4.5, Appendix E）均未被掩饰，而是做了详细的 power analysis 和 confound analysis。这种学术诚实值得肯定。\n\n**S5. SCS/BCS 指标有清晰的操作化定义和独立于 type composition 的验证。** Appendix O 的 joint model 分析（BCS unique R²=0.259 vs composition unique R²=0.299, VIF=1.06）有力地支持了 BCS 确实捕获了 confusability-specific signal。\n\n**S6. Schema Decomposition 的负面结果（§5）有建设性意义。** SDGD 方法的系统失败分析（merge amplification + routing failure）不仅报告了 negative result，还提供了机制解释，对后续 schema decomposition 研究有参考价值。\n\n### Weaknesses\n\n**W1 [Must-Fix] Logit-scale TOST inconclusive 但论文以 linear-scale 为主要结论——存在 cherry-picking 嫌疑。**\n- 具体位置：Appendix C（p.16），§4.1\n- 问题：论文在 Appendix C 坦承 logit-scale TOST 在 count×BCS interaction 上 inconclusive（p=0.25），但将 linear-scale TOST 作为 primary analysis（p=0.047 at ±2pp, p=0.063 at ±3.3pp）。对于 bounded accuracy data（0–1），logit-scale 是统计学上更合适的尺度（variance stabilization, homoscedasticity）。论文将 logit 结果降格为 \"sensitivity check\" 而将 linear 结果作为主要发现，需要更充分的方法论辩护。\n- 为什么影响接收：这直接关系到核心 claim 之一（count×BCS interaction bounded）的统计支撑。如果 logit-scale 下 interaction 不可排除实际意义，则 \"BCS effect 不随 count 放大\" 的结论被削弱。\n- 建议修改方向：(a) 在正文中直接报告 logit-scale 结果并讨论两种尺度的差异，而非仅在附录中提及；(b) 提供明确的统计理由说明为何 linear-scale 是合理的 primary analysis（例如，如果 accuracy 远离 0/1 边界，logit 变换的优势较小）；(c) 或者将结论弱化为 \"linear-scale 下 equivalent，logit-scale 下 inconclusive\"。\n\n**W2 [Must-Fix] DocRED 偏相关分析在 VIF=50.9 下不可靠。**\n- 具体位置：Appendix E, Table 11\n- 问题：DocRED 的 BCS-centrality collinearity 达到 VIF=50.9（r=0.99），标准误膨胀约 7.1 倍。在此条件下，偏相关估计极不稳定——微小的数据扰动就能大幅改变偏相关系数。论文称 \"BCS retains predictive value but does not uniquely identify the causal channel\"，但 VIF=50.9 下甚至偏相关系数本身的 point estimate 都不可靠。\n- 为什么影响接收：这影响 BCS 在 document-level RE 上的可解释性 claim。如果 BCS 和 centrality 在 DocRED 上完全混淆，就无法声称 BCS 在此数据集上有独立预测力。\n- 建议修改方向：(a) 对 DocRED 偏相关的结论大幅弱化，直接承认 BCS 和 centrality 在 DocRED 上 inseparable；(b) 补充 ridge regression 或其他 regularization 方法来处理多重共线性；(c) 或者将 DocRED centrality 分析的 claim 限缩为 \"descriptive, not inferential\"。\n\n**W3 [Must-Fix] Gemini leverage point 削弱跨架构泛化声明。**\n- 具体位置：Appendix U（p.25-26），Table 23-24\n- 问题：Gemini 2.5 Flash 的 BCS-controlled 结果（count 16）依赖单个极端 batch（BCS=0.97, accuracy 59.9%）。Leave-one-out 后相关系数可能显著下降（论文提到 count 8 gap 比 Qwen3-32B 小）。作为唯一的 proprietary model，Gemini 仅验证了部分实验（FewRel count curves + 部分 BCS-controlled），且存在 API-based 访问的不可控因素。\n- 为什么影响接收：论文声称 \"跨三个架构家族验证\"（§1, Contribution 2），但 proprietary model 的验证最薄弱。单个 leverage point 驱动的相关性不足以支撑 \"跨架构 robust\" 的结论。\n- 建议修改方向：(a) 正文中明确报告 Gemini leave-one-out sensitivity，不仅在附录；(b) 弱化跨架构泛化的措辞，明确区分 \"open-weight models 一致复现\" 与 \"proprietary model 部分支持\"；(c) 如果可行，在 Gemini 上增加更多 count levels 的 BCS-controlled batches 以消除 leverage 依赖。\n\n**W4 [Should-Fix] TOST 等价性 margin（±3pp）的部分循环论证。**\n- 具体位置：Appendix C（p.16）\n- 问题：论文提出三个 converging arguments 支持 ±3pp margin：(1) IQR-predicted Δ=2.2pp from BCS effect itself, (2) 3.43pp = 100% amplification, (3) Cohen's d = 0.35 × within-cell SD = 4.6pp → ±2.3pp。其中 argument (1) 直接引用了 BCS 效应自身的 effect size 来确定 margin——这构成 \"用被检验量的 effect size 确定检验 margin\" 的逻辑循环。\n- 建议：删除 argument (1) 或明确标注其循环性质；仅依赖 (2)(3) 两个外部标准也足以支持 ±3pp margin。\n\n**W5 [Should-Fix] Bootstrap CI 在 non-independence 结构下的有效性讨论不足。**\n- 具体位置：§3.5, Appendix N\n- 问题：同一 batch 内的 types 共享 prompt context（in-context 示例、JSON schema），bootstrap resample 的独立性假设在 batch 内部被违反。论文在 Appendix N 讨论了 pair-to-batch aggregation 的 ecological inference 问题（引用 Robinson, 1950），但未正式讨论 bootstrap percentile CI 在 batch-level 相关残差结构下的 coverage property。如果 batch-level residuals 存在 model/prompt-induced 的 across-batch correlation，bootstrap CI 可能 undercover。\n- 建议：(a) 讨论 bootstrap CI 的 coverage guarantee 在非独立数据下的 known limitations；(b) 补充 cluster-robust standard errors 或 block bootstrap 作为 robustness check。\n\n**W6 [Should-Fix] Pair-level r²=1.3-1.7% 到 batch-level R²=22-58% 的放大效应需要更突出的 caveats。**\n- 具体位置：§4.2, §4.3, Appendix N\n- 问题：从 pairwise r²≈1.5% 到 batch R²≈22% 的 ~15× 放大本质上是 ecological correlation（Simpson's paradox 的反面）。Appendix N 的 Monte Carlo simulation 提供了分析解释（EF≈3.35），但这一放大的前提是 batch-level aggregation 的因果合法性——即 batch mean BCS 确实是 causal driver 而非 collider。论文未充分讨论这一因果识别问题。\n- 建议：在正文讨论 R²=22-58% 时加入显眼的 caveat：batch-level R² 不等同于 pair-level explanatory power，ecological correlation 需要额外的因果假设。\n\n**W7 [Should-Fix] NER null 的解释存在内部张力。**\n- 具体位置：§4.2, §5, Appendix E.2\n- 问题：论文在 §5 将 NER 描述为 \"structural barrier\"（\"schema decomposition fails... NER errors stem from span-boundary decisions independent of label similarity\"），但在 Appendix E.2 的 power analysis 得出 \"absence of evidence rather than evidence of absence\"（80% power 需要 |r|≥0.132，而 attenuated r=−0.111 在此阈值之下）。这两个叙述存在张力：如果是 power 不足，就不能同时声称是 \"genuine structural absence\"。\n- 建议：在正文中统一叙述——要么是 \"power 受限下的 inconclusive\"（需弱化 §5 和 §6 中 NER 作为 fundamental boundary 的措辞），要么提供额外证据支持 structural absence（如更大样本量的 NER 实验）。当前 \"NER 是根本不同的\" 与 \"power 不足\" 并存，读者会困惑。\n\n**W8 [Should-Fix] DocRED count curves 仅 5 batches/level，统计效力不足。**\n- 具体位置：Table 1, §3.3\n- 问题：DocRED 每个 count level 仅 5 batches（vs Few-NERD 25, FewRel 8）。5×5=25 个数据点的回归对 noise 极为敏感。论文报告 DocRED 的 count-curve decline（−47pp per 34pp BCS decline），但这一估计的置信区间必然很宽。\n- 建议：报告 DocRED count curve regression 的完整 confidence intervals；明确讨论 n=25 下的 effect size uncertainty。\n\n**W9 [Should-Fix] 跨模型验证的不对称性。**\n- 具体位置：§3.5, Appendix T-U, Table 3-5\n- 问题：主模型 Qwen3-32B 有完整的 4 数据集 × 2 实验范式分析。但：(a) LLaMA-3.1-70B-Instruct FP8 仅验证了 FewRel count curves + BCS-controlled 和 Few-NERD NER；(b) Gemini 仅验证了 FewRel 部分实验（且有 leverage point 问题，见 W3）；(c) DocRED 和 MAVEN 的全部分析仅在 Qwen3-32B 上进行。这意味着论文最有趣的发现之一——document-level RE 的高 R²=58%——缺乏跨模型验证。\n- 建议：(a) 明确标注哪些 findings 有跨模型支持、哪些仅基于单一模型；(b) 在 Limitations 中讨论 DocRED R²=58% 的单模型依赖性。\n\n**W10 [Minor] Multiple comparisons 不做 correction 的理由可以更充分。**\n- 具体位置：§4.2, §4.3\n- 论文声称 cross-dataset 比较是 independent replication 不需 Bonferroni correction。但 Few-NERD 和 FewRel 共享 Wikidata 知识库来源，annotation guidelines 有相似性。如果效应来自共享的 schema 设计传统而非 general mechanism，\"独立复现\" 的假设就被削弱。\n- 建议：简要讨论 datasets 的独立性程度。\n\n**W11 [Minor] 单种子 + greedy decoding 的可复现性。**\n- 具体位置：§3.5, Limitations §6\n- Residual SD=0.88pp（count 80, FP8）说明量化非确定性引入了不可忽略的噪声。论文在 Limitations 中承认但未量化其对核心结论的影响（如 BCS-F1 correlation 的 bootstrap interval 是否 cover zero 如果加入 seed variation）。\n- 建议：报告 2-3 个不同 seed 下关键 metric 的 variability，或至少讨论 0.88pp residual 相对于 BCS effect size（~2-5pp）的比例。\n\n### Questions\n\n**Q1.** Logit-scale TOST 在 ±3.5pp logit margin 下 interaction inconclusive（p=0.25）。作者能否解释为何 linear-scale 比 logit-scale 更适合作为 primary analysis？是否考虑过其他 variance-stabilizing transformations（如 arcsine）？\n\n**Q2.** DocRED VIF=50.9 下的偏相关（Table 11）是否在 bootstrapped/permutation 框架下稳定？作者是否尝试过 ridge 或 elastic net 来处理这一共线性？\n\n**Q3.** Gemini count-16 BCS-controlled 的 leave-one-out 后，Pearson r 和 p-value 的具体数值是什么？如果删除该 leverage point 后效应消失，作者如何维持 \"跨架构 robust\" 的声明？\n\n**Q4.** 论文在 §5 和 §6 中将 NER 描述为 fundamental structural barrier，但 Appendix E.2 的 power analysis 表明 power 不足（65% at attenuated effect size）。作者倾向于哪种解释？是否有计划在更大样本量下验证 NER null？\n\n**Q5.** Batch-level bootstrap CI（B=1,000）是否考虑了 batch-level residuals 的 potential clustering（来自共享 model + prompt template）？是否尝试过 cluster-robust SE 或 block bootstrap？\n\n**Q6.** Pair-level r²=1.5% 而 batch-level R²=22%——作者是否认为 batch-level 的因果解释是合法的，还是认为这仅仅是一个有用的 descriptive pattern？如果是后者，§6 中 \"confusability-aware schema design\" 的实践建议是否过度推断？\n\n**Q7.** Multiple comparisons：Few-NERD 和 FewRel 都源自 Wikidata，MAVEN 源自 FrameNet，DocRED 源自 Wikipedia——作者是否考虑过这些共享来源可能引入的 pseudo-replication？\n\n### Missing References\n\n1. **Robinson, W.S. (1950)** — 论文在 Appendix N 引用了 ecological correlation 问题，但正文讨论 batch-level R² 时未提及此经典警示。建议在正文中引用。\n\n### Overall Assessment\n- Score: 3.5（Borderline Conference）\n- Confidence: 4/5\n- 简要理由：研究问题新颖、实验设计有创意、分析深度优秀，但部分核心 claim 的统计基础存在裂缝，需要修订后可达 Conference 水平。"
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
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每一条 Weakness 和 Question，请标注：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别注意你与 Reviewer 1 在以下方面的潜在分歧或共识：\n1. Logit-scale TOST 作为 primary vs secondary analysis（R1-W1）\n2. DocRED VIF=50.9 的偏相关可靠性（R1-W2）\n3. Gemini leverage point 对跨架构声明的影响（R1-W3）\n4. NER null 的解释框架（R1-W7 vs 你对 task-dependent framing 的看法）\n5. Pair-to-batch R² 放大的因果合法性（R1-W6）\n\n---\n\n以下是 Reviewer 1 的完整审稿意见原文：\n\n### Strengths\n\n**S1. 研究问题重要且新颖。** 这是首个系统隔离 type count 与 type confusability 对 zero-shot LLM IE 性能影响的控制研究。现有工作（LLM-PEE, CrossAgentIE 等）观察到 schema 变大时性能下降，但未分离出具体因素。本文的 confusability-aware 视角填补了一个重要的认知空白，对 IE schema 设计有直接实践指导意义。\n\n**S2. 两套实验范式互补且设计巧妙。** Count curves 控制 count 变化观察退化趋势，BCS-controlled 实验固定 count 变化 BCS 观察 confusability 效应——这种交叉设计比单一 correlational study 更有说服力。特别是 BCS-controlled 的 extreme batch 构建（greedy search on SCS graph）是一个有创意的实验手段（§3.3, Appendix A）。\n\n**S3. 分析极为详尽，敏感性检验充分。** 28 页含 18 个附录，涵盖 TOST 等价性检验（Appendix C）、Monte Carlo simulation（Appendix N）、prompt sensitivity（Appendix H）、within-pool analysis（Appendix D）、label renaming intervention（Appendix X）、relaxed matching（Appendix Y）等。这种分析深度在 empirical NLP 论文中少见。\n\n**S4. 诚实的 null result 报告。** NER batch-level BCS null（§4.2, §5）和 MAVEN centrality confound（§4.5, Appendix E）均未被掩饰，而是做了详细的 power analysis 和 confound analysis。这种学术诚实值得肯定。\n\n**S5. SCS/BCS 指标有清晰的操作化定义和独立于 type composition 的验证。** Appendix O 的 joint model 分析（BCS unique R²=0.259 vs composition unique R²=0.299, VIF=1.06）有力地支持了 BCS 确实捕获了 confusability-specific signal。\n\n**S6. Schema Decomposition 的负面结果（§5）有建设性意义。** SDGD 方法的系统失败分析（merge amplification + routing failure）不仅报告了 negative result，还提供了机制解释，对后续 schema decomposition 研究有参考价值。\n\n### Weaknesses\n\n**W1 [Must-Fix] Logit-scale TOST inconclusive 但论文以 linear-scale 为主要结论——存在 cherry-picking 嫌疑。**\n- 具体位置：Appendix C（p.16），§4.1\n- 问题：论文在 Appendix C 坦承 logit-scale TOST 在 count×BCS interaction 上 inconclusive（p=0.25），但将 linear-scale TOST 作为 primary analysis（p=0.047 at ±2pp, p=0.063 at ±3.3pp）。对于 bounded accuracy data（0–1），logit-scale 是统计学上更合适的尺度（variance stabilization, homoscedasticity）。论文将 logit 结果降格为 \"sensitivity check\" 而将 linear 结果作为主要发现，需要更充分的方法论辩护。\n- 为什么影响接收：这直接关系到核心 claim 之一（count×BCS interaction bounded）的统计支撑。如果 logit-scale 下 interaction 不可排除实际意义，则 \"BCS effect 不随 count 放大\" 的结论被削弱。\n- 建议修改方向：(a) 在正文中直接报告 logit-scale 结果并讨论两种尺度的差异，而非仅在附录中提及；(b) 提供明确的统计理由说明为何 linear-scale 是合理的 primary analysis（例如，如果 accuracy 远离 0/1 边界，logit 变换的优势较小）；(c) 或者将结论弱化为 \"linear-scale 下 equivalent，logit-scale 下 inconclusive\"。\n\n**W2 [Must-Fix] DocRED 偏相关分析在 VIF=50.9 下不可靠。**\n- 具体位置：Appendix E, Table 11\n- 问题：DocRED 的 BCS-centrality collinearity 达到 VIF=50.9（r=0.99），标准误膨胀约 7.1 倍。在此条件下，偏相关估计极不稳定——微小的数据扰动就能大幅改变偏相关系数。论文称 \"BCS retains predictive value but does not uniquely identify the causal channel\"，但 VIF=50.9 下甚至偏相关系数本身的 point estimate 都不可靠。\n- 为什么影响接收：这影响 BCS 在 document-level RE 上的可解释性 claim。如果 BCS 和 centrality 在 DocRED 上完全混淆，就无法声称 BCS 在此数据集上有独立预测力。\n- 建议修改方向：(a) 对 DocRED 偏相关的结论大幅弱化，直接承认 BCS 和 centrality 在 DocRED 上 inseparable；(b) 补充 ridge regression 或其他 regularization 方法来处理多重共线性；(c) 或者将 DocRED centrality 分析的 claim 限缩为 \"descriptive, not inferential\"。\n\n**W3 [Must-Fix] Gemini leverage point 削弱跨架构泛化声明。**\n- 具体位置：Appendix U（p.25-26），Table 23-24\n- 问题：Gemini 2.5 Flash 的 BCS-controlled 结果（count 16）依赖单个极端 batch（BCS=0.97, accuracy 59.9%）。Leave-one-out 后相关系数可能显著下降（论文提到 count 8 gap 比 Qwen3-32B 小）。作为唯一的 proprietary model，Gemini 仅验证了部分实验（FewRel count curves + 部分 BCS-controlled），且存在 API-based 访问的不可控因素。\n- 为什么影响接收：论文声称 \"跨三个架构家族验证\"（§1, Contribution 2），但 proprietary model 的验证最薄弱。单个 leverage point 驱动的相关性不足以支撑 \"跨架构 robust\" 的结论。\n- 建议修改方向：(a) 正文中明确报告 Gemini leave-one-out sensitivity，不仅在附录；(b) 弱化跨架构泛化的措辞，明确区分 \"open-weight models 一致复现\" 与 \"proprietary model 部分支持\"；(c) 如果可行，在 Gemini 上增加更多 count levels 的 BCS-controlled batches 以消除 leverage 依赖。\n\n**W4 [Should-Fix] TOST 等价性 margin（±3pp）的部分循环论证。**\n- 具体位置：Appendix C（p.16）\n- 问题：论文提出三个 converging arguments 支持 ±3pp margin：(1) IQR-predicted Δ=2.2pp from BCS effect itself, (2) 3.43pp = 100% amplification, (3) Cohen's d = 0.35 × within-cell SD = 4.6pp → ±2.3pp。其中 argument (1) 直接引用了 BCS 效应自身的 effect size 来确定 margin——这构成 \"用被检验量的 effect size 确定检验 margin\" 的逻辑循环。\n- 建议：删除 argument (1) 或明确标注其循环性质；仅依赖 (2)(3) 两个外部标准也足以支持 ±3pp margin。\n\n**W5 [Should-Fix] Bootstrap CI 在 non-independence 结构下的有效性讨论不足。**\n- 具体位置：§3.5, Appendix N\n- 问题：同一 batch 内的 types 共享 prompt context（in-context 示例、JSON schema），bootstrap resample 的独立性假设在 batch 内部被违反。论文在 Appendix N 讨论了 pair-to-batch aggregation 的 ecological inference 问题（引用 Robinson, 1950），但未正式讨论 bootstrap percentile CI 在 batch-level 相关残差结构下的 coverage property。如果 batch-level residuals 存在 model/prompt-induced 的 across-batch correlation，bootstrap CI 可能 undercover。\n- 建议：(a) 讨论 bootstrap CI 的 coverage guarantee 在非独立数据下的 known limitations；(b) 补充 cluster-robust standard errors 或 block bootstrap 作为 robustness check。\n\n**W6 [Should-Fix] Pair-level r²=1.3-1.7% 到 batch-level R²=22-58% 的放大效应需要更突出的 caveats。**\n- 具体位置：§4.2, §4.3, Appendix N\n- 问题：从 pairwise r²≈1.5% 到 batch R²≈22% 的 ~15× 放大本质上是 ecological correlation（Simpson's paradox 的反面）。Appendix N 的 Monte Carlo simulation 提供了分析解释（EF≈3.35），但这一放大的前提是 batch-level aggregation 的因果合法性——即 batch mean BCS 确实是 causal driver 而非 collider。论文未充分讨论这一因果识别问题。\n- 建议：在正文讨论 R²=22-58% 时加入显眼的 caveat：batch-level R² 不等同于 pair-level explanatory power，ecological correlation 需要额外的因果假设。\n\n**W7 [Should-Fix] NER null 的解释存在内部张力。**\n- 具体位置：§4.2, §5, Appendix E.2\n- 问题：论文在 §5 将 NER 描述为 \"structural barrier\"（\"schema decomposition fails... NER errors stem from span-boundary decisions independent of label similarity\"），但在 Appendix E.2 的 power analysis 得出 \"absence of evidence rather than evidence of absence\"（80% power 需要 |r|≥0.132，而 attenuated r=−0.111 在此阈值之下）。这两个叙述存在张力：如果是 power 不足，就不能同时声称是 \"genuine structural absence\"。\n- 建议：在正文中统一叙述——要么是 \"power 受限下的 inconclusive\"（需弱化 §5 和 §6 中 NER 作为 fundamental boundary 的措辞），要么提供额外证据支持 structural absence（如更大样本量的 NER 实验）。当前 \"NER 是根本不同的\" 与 \"power 不足\" 并存，读者会困惑。\n\n**W8 [Should-Fix] DocRED count curves 仅 5 batches/level，统计效力不足。**\n- 具体位置：Table 1, §3.3\n- 问题：DocRED 每个 count level 仅 5 batches（vs Few-NERD 25, FewRel 8）。5×5=25 个数据点的回归对 noise 极为敏感。论文报告 DocRED 的 count-curve decline（−47pp per 34pp BCS decline），但这一估计的置信区间必然很宽。\n- 建议：报告 DocRED count curve regression 的完整 confidence intervals；明确讨论 n=25 下的 effect size uncertainty。\n\n**W9 [Should-Fix] 跨模型验证的不对称性。**\n- 具体位置：§3.5, Appendix T-U, Table 3-5\n- 问题：主模型 Qwen3-32B 有完整的 4 数据集 × 2 实验范式分析。但：(a) LLaMA-3.1-70B-Instruct FP8 仅验证了 FewRel count curves + BCS-controlled 和 Few-NERD NER；(b) Gemini 仅验证了 FewRel 部分实验（且有 leverage point 问题，见 W3）；(c) DocRED 和 MAVEN 的全部分析仅在 Qwen3-32B 上进行。这意味着论文最有趣的发现之一——document-level RE 的高 R²=58%——缺乏跨模型验证。\n- 建议：(a) 明确标注哪些 findings 有跨模型支持、哪些仅基于单一模型；(b) 在 Limitations 中讨论 DocRED R²=58% 的单模型依赖性。\n\n**W10 [Minor] Multiple comparisons 不做 correction 的理由可以更充分。**\n- 具体位置：§4.2, §4.3\n- 论文声称 cross-dataset 比较是 independent replication 不需 Bonferroni correction。但 Few-NERD 和 FewRel 共享 Wikidata 知识库来源，annotation guidelines 有相似性。如果效应来自共享的 schema 设计传统而非 general mechanism，\"独立复现\" 的假设就被削弱。\n- 建议：简要讨论 datasets 的独立性程度。\n\n**W11 [Minor] 单种子 + greedy decoding 的可复现性。**\n- 具体位置：§3.5, Limitations §6\n- Residual SD=0.88pp（count 80, FP8）说明量化非确定性引入了不可忽略的噪声。论文在 Limitations 中承认但未量化其对核心结论的影响（如 BCS-F1 correlation 的 bootstrap interval 是否 cover zero 如果加入 seed variation）。\n- 建议：报告 2-3 个不同 seed 下关键 metric 的 variability，或至少讨论 0.88pp residual 相对于 BCS effect size（~2-5pp）的比例。\n\n### Questions\n\n**Q1.** Logit-scale TOST 在 ±3.5pp logit margin 下 interaction inconclusive（p=0.25）。作者能否解释为何 linear-scale 比 logit-scale 更适合作为 primary analysis？是否考虑过其他 variance-stabilizing transformations（如 arcsine）？\n\n**Q2.** DocRED VIF=50.9 下的偏相关（Table 11）是否在 bootstrapped/permutation 框架下稳定？作者是否尝试过 ridge 或 elastic net 来处理这一共线性？\n\n**Q3.** Gemini count-16 BCS-controlled 的 leave-one-out 后，Pearson r 和 p-value 的具体数值是什么？如果删除该 leverage point 后效应消失，作者如何维持 \"跨架构 robust\" 的声明？\n\n**Q4.** 论文在 §5 和 §6 中将 NER 描述为 fundamental structural barrier，但 Appendix E.2 的 power analysis 表明 power 不足（65% at attenuated effect size）。作者倾向于哪种解释？是否有计划在更大样本量下验证 NER null？\n\n**Q5.** Batch-level bootstrap CI（B=1,000）是否考虑了 batch-level residuals 的 potential clustering（来自共享 model + prompt template）？是否尝试过 cluster-robust SE 或 block bootstrap？\n\n**Q6.** Pair-level r²=1.5% 而 batch-level R²=22%——作者是否认为 batch-level 的因果解释是合法的，还是认为这仅仅是一个有用的 descriptive pattern？如果是后者，§6 中 \"confusability-aware schema design\" 的实践建议是否过度推断？\n\n**Q7.** Multiple comparisons：Few-NERD 和 FewRel 都源自 Wikidata，MAVEN 源自 FrameNet，DocRED 源自 Wikipedia——作者是否考虑过这些共享来源可能引入的 pseudo-replication？\n\n### Missing References\n\n1. **Robinson, W.S. (1950)** — 论文在 Appendix N 引用了 ecological correlation 问题，但正文讨论 batch-level R² 时未提及此经典警示。建议在正文中引用。\n\n### Overall Assessment\n- Score: 3.5（Borderline Conference）\n- Confidence: 4/5\n- 简要理由：研究问题新颖、实验设计有创意、分析深度优秀，但部分核心 claim 的统计基础存在裂缝，需要修订后可达 Conference 水平。"
  }
}
```

</details>

---


### Tool result

_source line 2599 · 2026-05-21T18:00:51.046736+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 60294
}
```

</details>

---


### Tool call

_source line 2600 · 2026-05-21T18:00:51.398624+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每一条 Weakness 和 Question，请标注：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别注意你与 Reviewer 2 在以下方面的潜在分歧或共识：\n1. SCS vs LLM-PEE 的 novelty 定位（R2-W1）——你是否认为实验范式足以构成 novelty\n2. Abstract/Intro 中 task-dependent 弱信号的 framing（R2-W2）——你的 W7（NER null 叙述张力）是否与此相关\n3. 跨模型验证深度（R2-W3 vs 你的 W9）——两者的严重性判断是否一致\n4. Sections 5-6 的压缩问题（R2-W4）——你是否同意 centrality confound 可移入 appendix\n5. Responsible NLP Checklist 在 PDF 中的格式合规问题（R2-W6）\n\n---\n\n以下是 Reviewer 2 的完整审稿意见原文：\n\n### Strengths\n\n**S1**: **控制变量实验设计是核心贡献，且质量很高。** 通过构造 BCS-controlled batches（固定 type count、变化 confusability），论文干净地隔离了两个因素。这比先前工作（LLM-PEE, PARSE 等）的相关性分析严格得多。Quasi-experimental manipulation（Section 3.3, Experiment 2）加上 bootstrap CIs 和 permutation tests 确保了统计可靠性。\n\n**S2**: **经验覆盖面广且深。** 4 个数据集 × 3 个 IE 任务 × 2 个 embedding 模型（Qwen3, MiniLM）× 3 个 LLM 架构的 cross-model validation（Appendices T, U），加上大量 robustness checks：prompt sensitivity（Appendix H）、format independence（Appendix K）、aggregation sensitivity（Appendix I）、BCS aggregation ablation（Appendix I, Table 14）。Appendix 的实验量远超主文，体现了实验的扎实程度。\n\n**S3**: **负面结果诚实且有价值。** Section 5 的 SDGD 失败分析（merge amplification 和 routing failure）和 Appendix X 的 label renaming 负面结果（Table 29: renaming 降低 SCS 但反而损害准确率）为社区节省了大量试错成本。SDGD oracle routing（Table 8）恢复了大部分准确率，精准定位了 decompose-then-merge 范式的瓶颈。\n\n**S4**: **两维降解分解概念清晰。** Dimension 1（count→recall decline）和 Dimension 2（confusability→type confusion）在 Figure 2 的 error taxonomy 分析中得到了直接的经验支撑——IntraSub 与 BCS 单调共变，而 NER missed rates 保持相对稳定。这为理解 LLM IE 降解提供了可操作的分析框架。\n\n**S5**: **Limitations 部分坦诚全面。** 覆盖了 model coverage、effect size and statistical design、task scope、causal mechanism、data contamination、domain/language scope、multiple comparisons 共 7 个点，远超通常水平。\n\n### Weaknesses\n\n**W1 [Should-Fix] SCS 相对于 LLM-PEE 的新颖性定位不够清晰**\n- 具体位置：Section 2 (Related Work, paragraph on SCS novelty) 和 Section 3.2 (SCS 定义)\n- 问题：LLM-PEE (Liu et al., 2025) 的 partitioning criterion 与 SCS 在形式上完全一致——都是基于 type name embeddings 的 pairwise cosine similarity。论文在 Section 2 承认了这一点（\"our work uses the same metric for scientific analysis\"），但这个区分在当前的 framing 中不够突出。读者很容易得出\"SCS = LLM-PEE's criterion rebranded\"的印象。\n- 建议：在 Section 2 或 Section 3.2 增加一段明确的 novelty statement，强调贡献不在于 SCS metric 本身，而在于控制变量实验框架。\n\n**W2 [Should-Fix] R² 的 task-dependent 弱信号在 abstract/intro 中表述不均衡**\n- 具体位置：Abstract（第1页）, Section 4.3, Table 5（第6页）\n- 问题：Abstract 突出了 \"BCS explains 22–58% of cross-batch RE accuracy variance\"，但对 NER 上 batch-level BCS-F1 相关性为 null 的结果缺乏同等 prominence 的呈现。\n- 建议：Abstract 中在提到 22-58% R² 后立即加入 qualifier。\n\n**W3 [Should-Fix] 主实验依赖单一模型，跨模型验证深度不均**\n- 具体位置：Section 3.5, Appendices T, U\n- 问题：所有 core experiments 均使用 Qwen3-32B。Cross-model validation 仅复制了 count curves 和 BCS-controlled 两个实验，未涵盖 error taxonomy decomposition、centrality confound analysis、SDGD experiments。\n- 建议：至少补充 error taxonomy decomposition 的跨模型验证，或在 Limitations 中明确说明。\n\n**W4 [Should-Fix] Sections 5-6 过度压缩，叙事密度过高**\n- 具体位置：Page 8\n- 问题：第 8 页承载了三个完整的分析板块：centrality confound 结论、SDGD 全部分析、以及整个 Discussion and Conclusion。SDGD 的 failure analysis 感觉 post-hoc，Discussion 中的 practical implications 仅用一段话覆盖。\n- 建议：考虑将 Section 4.5（centrality confound）移入 appendix，为 Sections 5-6 腾出空间。\n\n**W5 [Minor] 数字/统计呈现密度过高**\n- 具体位置：Sections 4.1-4.3（pages 6-7）\n- 建议：将 per-dataset 的详细统计值移入 appendix table，正文只保留 headline numbers。\n\n**W6 [Minor] Responsible NLP Research Checklist 出现在论文 PDF 中**\n- 具体位置：Pages 9-10\n- 问题：按 EMNLP 2026/ARR 政策，Checklist 应在 OpenReview form 中填写，不应在 PDF 中。\n- 建议：从 PDF 中移除。\n\n**W7 [Minor] 2 个 orphan bibliography entries**\n- references.bib 中 `park-2024-grammar-aligned` 和 `zhou-2024-grasping` 未被引用。\n\n### Questions\n\n**Q1**: Pairwise SCS 相关性很弱（r ≈ 0.17），但 batch-level R² 明显更高（22-58%）。这种 amplification 是单纯的 aggregation smoothing 还是存在 compositional effect？\n\n**Q2**: MAVEN 上 BCS-F1 正相关完全归因于 centrality confound。这是否意味着 SCS/BCS 在 homogeneous schemas 上不适用？\n\n**Q3**: SDGD 失败的核心是 merge amplification。是否考虑过避免 merge 的替代方案——如 hierarchical extraction 或 retrieval-augmented type selection？\n\n**Q4**: Table 29 显示 renaming labels 降低 SCS 后反而损害准确率。这是因为 renamed labels 丢失了语义信息，还是因为 unfamiliar paraphrases 扰乱了模型的 type semantics？\n\n**Q5**: 论文使用 Qwen3 和 MiniLM 两种 embeddings。对于 practitioners，应该用哪个？\n\n### Missing References\n1. Ren et al. (2016) \"AFET\"、Choi et al. (2018) \"Ultra-Fine Entity Typing\" — 与 type granularity/hierarchy 相关\n2. Min et al. (2022) \"Rethinking Demonstrations in ICL\" — 可为 few-shot confusability 提供理论支撑\n\n### Overall Assessment\n- Score: 3.5（Borderline Conference）\n- Confidence: 4\n- 简要理由：well-executed 经验分析论文，核心贡献在于控制变量实验范式。SCS 与 LLM-PEE 形式重叠未充分区分，NER null 的 framing 需平衡，Sections 5-6 过度压缩。Findings track strong candidate，若改善 novelty 定位和 task-dependent framing 则有望 main conference。"
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
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每一条 Weakness 和 Question，请标注：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别注意你与 Reviewer 2 在以下方面的潜在分歧或共识：\n1. SCS vs LLM-PEE 的 novelty 定位（R2-W1）——你是否认为实验范式足以构成 novelty\n2. Abstract/Intro 中 task-dependent 弱信号的 framing（R2-W2）——你的 W7（NER null 叙述张力）是否与此相关\n3. 跨模型验证深度（R2-W3 vs 你的 W9）——两者的严重性判断是否一致\n4. Sections 5-6 的压缩问题（R2-W4）——你是否同意 centrality confound 可移入 appendix\n5. Responsible NLP Checklist 在 PDF 中的格式合规问题（R2-W6）\n\n---\n\n以下是 Reviewer 2 的完整审稿意见原文：\n\n### Strengths\n\n**S1**: **控制变量实验设计是核心贡献，且质量很高。** 通过构造 BCS-controlled batches（固定 type count、变化 confusability），论文干净地隔离了两个因素。这比先前工作（LLM-PEE, PARSE 等）的相关性分析严格得多。Quasi-experimental manipulation（Section 3.3, Experiment 2）加上 bootstrap CIs 和 permutation tests 确保了统计可靠性。\n\n**S2**: **经验覆盖面广且深。** 4 个数据集 × 3 个 IE 任务 × 2 个 embedding 模型（Qwen3, MiniLM）× 3 个 LLM 架构的 cross-model validation（Appendices T, U），加上大量 robustness checks：prompt sensitivity（Appendix H）、format independence（Appendix K）、aggregation sensitivity（Appendix I）、BCS aggregation ablation（Appendix I, Table 14）。Appendix 的实验量远超主文，体现了实验的扎实程度。\n\n**S3**: **负面结果诚实且有价值。** Section 5 的 SDGD 失败分析（merge amplification 和 routing failure）和 Appendix X 的 label renaming 负面结果（Table 29: renaming 降低 SCS 但反而损害准确率）为社区节省了大量试错成本。SDGD oracle routing（Table 8）恢复了大部分准确率，精准定位了 decompose-then-merge 范式的瓶颈。\n\n**S4**: **两维降解分解概念清晰。** Dimension 1（count→recall decline）和 Dimension 2（confusability→type confusion）在 Figure 2 的 error taxonomy 分析中得到了直接的经验支撑——IntraSub 与 BCS 单调共变，而 NER missed rates 保持相对稳定。这为理解 LLM IE 降解提供了可操作的分析框架。\n\n**S5**: **Limitations 部分坦诚全面。** 覆盖了 model coverage、effect size and statistical design、task scope、causal mechanism、data contamination、domain/language scope、multiple comparisons 共 7 个点，远超通常水平。\n\n### Weaknesses\n\n**W1 [Should-Fix] SCS 相对于 LLM-PEE 的新颖性定位不够清晰**\n- 具体位置：Section 2 (Related Work, paragraph on SCS novelty) 和 Section 3.2 (SCS 定义)\n- 问题：LLM-PEE (Liu et al., 2025) 的 partitioning criterion 与 SCS 在形式上完全一致——都是基于 type name embeddings 的 pairwise cosine similarity。论文在 Section 2 承认了这一点（\"our work uses the same metric for scientific analysis\"），但这个区分在当前的 framing 中不够突出。读者很容易得出\"SCS = LLM-PEE's criterion rebranded\"的印象。\n- 建议：在 Section 2 或 Section 3.2 增加一段明确的 novelty statement，强调贡献不在于 SCS metric 本身，而在于控制变量实验框架。\n\n**W2 [Should-Fix] R² 的 task-dependent 弱信号在 abstract/intro 中表述不均衡**\n- 具体位置：Abstract（第1页）, Section 4.3, Table 5（第6页）\n- 问题：Abstract 突出了 \"BCS explains 22–58% of cross-batch RE accuracy variance\"，但对 NER 上 batch-level BCS-F1 相关性为 null 的结果缺乏同等 prominence 的呈现。\n- 建议：Abstract 中在提到 22-58% R² 后立即加入 qualifier。\n\n**W3 [Should-Fix] 主实验依赖单一模型，跨模型验证深度不均**\n- 具体位置：Section 3.5, Appendices T, U\n- 问题：所有 core experiments 均使用 Qwen3-32B。Cross-model validation 仅复制了 count curves 和 BCS-controlled 两个实验，未涵盖 error taxonomy decomposition、centrality confound analysis、SDGD experiments。\n- 建议：至少补充 error taxonomy decomposition 的跨模型验证，或在 Limitations 中明确说明。\n\n**W4 [Should-Fix] Sections 5-6 过度压缩，叙事密度过高**\n- 具体位置：Page 8\n- 问题：第 8 页承载了三个完整的分析板块：centrality confound 结论、SDGD 全部分析、以及整个 Discussion and Conclusion。SDGD 的 failure analysis 感觉 post-hoc，Discussion 中的 practical implications 仅用一段话覆盖。\n- 建议：考虑将 Section 4.5（centrality confound）移入 appendix，为 Sections 5-6 腾出空间。\n\n**W5 [Minor] 数字/统计呈现密度过高**\n- 具体位置：Sections 4.1-4.3（pages 6-7）\n- 建议：将 per-dataset 的详细统计值移入 appendix table，正文只保留 headline numbers。\n\n**W6 [Minor] Responsible NLP Research Checklist 出现在论文 PDF 中**\n- 具体位置：Pages 9-10\n- 问题：按 EMNLP 2026/ARR 政策，Checklist 应在 OpenReview form 中填写，不应在 PDF 中。\n- 建议：从 PDF 中移除。\n\n**W7 [Minor] 2 个 orphan bibliography entries**\n- references.bib 中 `park-2024-grammar-aligned` 和 `zhou-2024-grasping` 未被引用。\n\n### Questions\n\n**Q1**: Pairwise SCS 相关性很弱（r ≈ 0.17），但 batch-level R² 明显更高（22-58%）。这种 amplification 是单纯的 aggregation smoothing 还是存在 compositional effect？\n\n**Q2**: MAVEN 上 BCS-F1 正相关完全归因于 centrality confound。这是否意味着 SCS/BCS 在 homogeneous schemas 上不适用？\n\n**Q3**: SDGD 失败的核心是 merge amplification。是否考虑过避免 merge 的替代方案——如 hierarchical extraction 或 retrieval-augmented type selection？\n\n**Q4**: Table 29 显示 renaming labels 降低 SCS 后反而损害准确率。这是因为 renamed labels 丢失了语义信息，还是因为 unfamiliar paraphrases 扰乱了模型的 type semantics？\n\n**Q5**: 论文使用 Qwen3 和 MiniLM 两种 embeddings。对于 practitioners，应该用哪个？\n\n### Missing References\n1. Ren et al. (2016) \"AFET\"、Choi et al. (2018) \"Ultra-Fine Entity Typing\" — 与 type granularity/hierarchy 相关\n2. Min et al. (2022) \"Rethinking Demonstrations in ICL\" — 可为 few-shot confusability 提供理论支撑\n\n### Overall Assessment\n- Score: 3.5（Borderline Conference）\n- Confidence: 4\n- 简要理由：well-executed 经验分析论文，核心贡献在于控制变量实验范式。SCS 与 LLM-PEE 形式重叠未充分区分，NER null 的 framing 需平衡，Sections 5-6 过度压缩。Findings track strong candidate，若改善 novelty 定位和 task-dependent framing 则有望 main conference。"
  }
}
```

</details>

---


### Tool result

_source line 2601 · 2026-05-21T18:00:52.805763+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1407
}
```

</details>

---


### Assistant

_source line 2602 · 2026-05-21T18:00:58.647178+00:00_

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


## Round 213

## Round 213

2 recorded events


### User

_source line 2603 · 2026-05-21T18:01:01.255966+00:00_

[Reviewer 2 审稿结果]:
Round 1 审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.5（Borderline Conference），Confidence 4/5。

核心判断：
- **最大亮点**：控制变量实验设计（BCS-controlled batches）质量高，是 empirical analysis 论文的典范；SDGD 负面结果对社区有实际价值
- **最大风险**：SCS 与 LLM-PEE 的 metric 重叠削弱 perceived novelty；NER 上 BCS 信号为 null 但 abstract 未充分 qualify；Sections 5-6 压缩过度
- **建议路径**：强化 novelty framing（contribution = experimental paradigm, not metric）+ 平衡呈现 task-dependent 弱信号 → 可望达到 main conference 水准

提交了 5 个 Should-Fix 问题（W1-W4 影响评分）和 3 个 Minor 问题（W5-W7 不影响接收），以及 5 个需要作者回答的技术问题。

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

_source line 2604 · 2026-05-21T18:01:07.537584+00:00_

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


## Round 214

## Round 214

2 recorded events


### User

_source line 2605 · 2026-05-21T18:02:24.706671+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 对 Reviewer 1 审稿意见的逐条分析

---

### 对 Strengths 的回应

R1 的 S1-S6 与我的评估高度一致。特别认同 S2（交叉实验设计）、S3（分析深度）和 S4（诚实的 null result 报告）。补充一点：R1 的 S5 提到 Appendix O 的 joint model 分析（BCS unique R²=0.259, VIF=1.06）是我审稿中未充分关注的，这确实是支持 BCS 捕获 confusability-specific signal 的有力证据。

---

### 对 Weaknesses 的逐条回应

**[AGREE] R1-W1: Logit-scale TOST 作为 primary vs secondary analysis**
R1 的统计论证是正确的：对于 bounded [0,1] accuracy data，logit-scale 通常是更合适的 variance-stabilizing transformation。不过我对 severity 的判断略低于 R1（Should-Fix 而非 Must-Fix），理由如下：
- FewRel accuracy 在本文实验中大致分布在 0.37–0.86 区间（Figure 1, Table 4），距离 0/1 边界尚有距离。在此区间内 logit 与 linear 的差异相对有限（logit 变换的主要优势在 accuracy 接近 0 或 1 时发挥作用）。
- 论文确实报告了两种 scale 的结果（Appendix C），且 linear-scale 下 ±2pp margin 的 p=0.047 刚过 0.05 threshold，本身就不是强有力的 rejection。
- 但 R1 关于 "cherry-picking 嫌疑" 的 framing concern 是对的——将 inconclusive logit 结果降格为 sensitivity check 而不充分论证 scale 选择，确实削弱可信度。
- **我的建议**：正文中应同时报告两种 scale 结果，将结论调整为 "linear-scale 下 interaction bounded, logit-scale 下 inconclusive"，让读者自行判断。这比 R1 的 Must-Fix 更可行，但必须做。

**[AGREE] R1-W2: DocRED VIF=50.9 下偏相关不可靠**
完全同意。VIF=50.9 意味着标准误膨胀 ~7.1×，偏相关 point estimate 极不稳定。我在自己的审稿中未单独 flag 这一点（我关注的是更宏观的 task-dependent framing 问题），但 R1 精准地指出了 DocRED 偏相关分析的具体统计缺陷。
- 需要注意的是，论文自身在 Appendix E（page 17）已有所收敛："BCS retains predictive value but does not uniquely identify the causal channel"。但这句措辞仍然过度——在 VIF=50.9 下，甚至不能可靠地说 "retains predictive value"。
- **补充论据**：论文的 BCS 核心 claim 并不完全依赖 DocRED 偏相关——FewRel BCS-controlled 实验（Table 4, Table 15）是更干净的证据。因此我认为 W2 是 Should-Fix（弱化 DocRED 偏相关 claim）而非 Must-Fix（不影响全文核心结论），但 R1 的 ridge regression 建议很有建设性。
- **severity 分歧**：R1 标 Must-Fix，我倾向 Should-Fix。理由：DocRED 偏相关是 Appendix E 中的补充分析，非主文核心 claim。弱化措辞即可解决，无需重新实验。

**[REBUT] R1-W3: Gemini leverage point 削弱跨架构声明 — 严重性被高估**
R1 的技术观察（单个 leverage point 驱动相关性）是正确的，但 Must-Fix 的 severity 判断我认为过高。
- **证据 1**：论文的跨架构 claim 并非主要依赖 Gemini。核心跨模型验证是 Llama-3.1-70B（Appendix T），Table 22 显示 RE count-curve slopes 在 Llama-70B 和 Qwen3-32B 之间高度一致（decline −30.7pp vs −30.1pp），BCS-controlled 效应也复现（Table 3: Llama-3.1-8B decline −47pp, Qwen3-32B −34pp）。即使完全删除 Gemini 验证，"两个开放权重架构一致复现" 仍然成立。
- **证据 2**：论文在 Appendix U（page 25-26, Table 23）已报告 Gemini count curves 与 Qwen3-32B directionally consistent，且 count-curve replication 不受 leverage point 问题影响（多 count levels, 非 single-batch 依赖）。
- **我的建议**：同意 R1 的措辞建议（区分 "open-weight models 一致复现" vs "proprietary model 部分支持"），但应降为 Should-Fix。论文不需要在 Gemini 上做更多实验来支撑核心结论。

**[AGREE] R1-W4: TOST margin 的部分循环论证**
同意。用 BCS effect size（IQR-predicted Δ=2.2pp）来确定 TOST equivalence margin 确实构成循环：你用被检验量本身的估计来设定 "多大算 equivalent"。R1 的建议合理——删除 argument (1)，仅依赖 (2)(3) 两个外部标准。这是一个 clean 的方法论修复。

**[REBUT] R1-W5: Bootstrap CI non-independence 问题 — 需要区分分析层级**
R1 的 concern 有道理，但我认为论文的 bootstrap 设计在关键层级上是正确的：
- 论文的 batch-level 分析（§4.3, BCS-controlled experiments）以 **batch 为分析单位**（每个 batch 是一个独立的实验 trial：独立采样 type set → 独立生成 prompt → 独立 inference）。Bootstrap resampling 是在 batch 层级进行的（B=1,000 at batch level, §3.5），不是在 within-batch type 层级。
- R1 担心的 within-batch non-independence（types 共享 prompt context）被 batch-level aggregation 设计所吸收——每个 batch 的 accuracy 已经是 within-batch 的聚合量，bootstrap CI 不需要 within-batch independence。
- **但 R1 有一个 valid sub-point**：across-batch 的 potential non-independence（来自 shared model + prompt template）确实未被讨论。如果不同 batches 共享系统性偏差（如模型对特定 prompt structure 的 sensitivity），batch-level bootstrap CI 可能 undercover。
- **我的建议**：Should-Fix，但重点应放在讨论 across-batch residual correlation 而非 within-batch non-independence。论文可以补充一句说明 batches 使用相同 prompt template 但 type composition 独立采样，bootstrap CI 的 coverage 主要受 across-batch correlation 影响。

**[AGREE] R1-W6: Pair-to-batch R² 放大需要更显著的 caveats**
同意。这与我的 Q1 提出的问题高度一致——我也注意到了 pairwise r²≈1.5% 到 batch R²≈22% 的 ~15× 放大。R1 正确指出这是 ecological correlation 问题。
- 论文在 Appendix N 的 Monte Carlo simulation 提供了分析性解释（EF≈3.35），但这个分析仅在 appendix，正文未充分警示读者。
- **关键问题**：batch-level R² 的因果解释是否合法取决于 batch mean BCS 是否是 causal intermediate（confusable types → higher BCS → more confusion → lower accuracy）还是 collider。论文隐含假设前者但未论证。
- **与我审稿的关联**：这强化了我的 W2（R² framing 不均衡）和 Q1——不仅 task-dependent 信号需要 qualify，R² 本身的因果含义也需要 caveat。
- **建议**：正文 §4.3 讨论 R²=22-58% 时加入 1-2 句显式 caveat，引用 Robinson (1950)——论文已在 Appendix N 引用此文，移到正文即可。

**[AGREE] R1-W7: NER null 解释的内部张力**
这是 R1 最 insightful 的观察之一，与我的 W2（task-dependent framing 不均衡）互补。
- R1 精准地指出了 §5/§6 的 "structural barrier" 叙述与 Appendix E.2 的 "power insufficient" 叙述之间的矛盾。两者不能同时成立：
  - 如果 NER batch-level BCS null 是因为 power 不足（65% at attenuated effect size, Appendix E.2），则不能声称 NER 是 "fundamental structural barrier"。
  - 如果 NER 确实存在 structural difference（span-boundary decisions independent of label similarity），则 power analysis 是 moot。
- 论文需要选择一个主叙述并保持一致。我的建议：鉴于 power analysis 显示 80% power 需要 |r|≥0.132 而观测 r=−0.111 就在阈值附近（Appendix E.2），正文应采取 "inconclusive, likely attenuated" 而非 "fundamental barrier" 的措辞。

**[AGREE] R1-W8: DocRED 5 batches/level 统计效力不足**
同意。n=5 per level 确实偏低。不过需要注意论文的解释：DocRED 是 document-level RE，每个 batch 的评估成本远高于 sentence-level（8,042 sentences per batch, Table 1 footnote），batch 数量限制有实际原因。建议论文 (a) 报告 DocRED count curve 的 complete CIs，(b) 在正文或 caption 中说明为何 batch 数少于其他数据集。

**[AGREE] R1-W9: 跨模型验证的不对称性**
完全同意。这与我自己的 W3 一致。R1 更细致地分解了每个模型覆盖了哪些实验维度——特别是指出 DocRED R²=58%（论文最高 effect size）完全缺乏跨模型验证，这一点很重要。

**[AGREE] R1-W10: Multiple comparisons 和 dataset independence**
部分同意。Few-NERD 和 FewRel 确实共享 Wikidata 来源，可能存在 pseudo-replication。但两者的 annotation guidelines、task types（NER vs RE）和 schema structures 差异显著。我认为 "independent replication" 的 claim 不完美但 broadly defensible。简要讨论 dataset independence 的程度是合理的，但不构成重大问题。

**[AGREE] R1-W11: 单种子 + greedy decoding 的可复现性**
同意。Residual SD=0.88pp（§3.5）相对于 BCS effect size ~2-5pp 是 non-trivial 的（约 18-44%）。至少报告 2-3 个 seed 下 key metrics 的 variability 是合理的要求。

---

### 对 Questions 的回应

**R1-Q1 (Logit vs linear scale)**: 与 W1 一致，我同意这需要回答。作者应论证 linear-scale 的 appropriateness（如 accuracy 远离边界）或承认 logit-scale 结果更保守。

**R1-Q2 (DocRED VIF=50.9 下 bootstrap stability)**: 这是一个很好的诊断建议。如果 bootstrap/permutation 下偏相关系数 highly variable，则进一步证实 VIF=50.9 下的不可靠性。

**R1-Q3 (Gemini leave-one-out)**: 合理的诊断请求，但如上文 W3 回应所述，即使 Gemini leave-one-out 后效应消失，论文的跨架构 claim 仍有 Llama-70B 支撑。作者应报告 leave-one-out 数值并调整措辞。

**R1-Q4 (NER null interpretation)**: 与 W7 一致，这是论文需要统一叙述的关键问题。

**R1-Q5 (Cluster-robust SE)**: 如上文 W5 回应所述，across-batch correlation 是更相关的 concern。建议作者检验 batch-level residuals 是否存在系统性 pattern。

**R1-Q6 (Batch-level causal interpretation)**: 这是最深刻的问题。我倾向认为 batch-level R² 是 useful descriptive pattern 而非 fully causal——论文的实践建议（confusability-aware schema design）需要更谨慎的措辞。但 BCS-controlled 实验（固定 count, 变化 BCS）确实提供了 quasi-experimental 的因果证据：在 count 控制的条件下，high-BCS batches consistently 低于 low-BCS batches（Table 4, Table 15），这不是纯 descriptive correlation。

**R1-Q7 (Pseudo-replication from shared sources)**: 同 W10，合理但非 critical。

---

### 对 Missing References 的回应

**[AGREE]** R1 建议在正文中引用 Robinson (1950) — 这完全正确。论文已在 Appendix N 引用此文，但正文讨论 batch-level R² 时应同步引用以警示读者。

---

### 汇总：R2 与 R1 的共识与分歧

| R1 编号 | R1 Severity | R2 判断 | R2 Severity | 理由 |
|---------|------------|---------|------------|------|
| W1 | Must-Fix | AGREE | Should-Fix | 统计论点正确，但 accuracy 不在极端区间，linear-scale 非完全不当。调整 framing 即可。 |
| W2 | Must-Fix | AGREE | Should-Fix | VIF=50.9 确实致命，但 DocRED 偏相关是补充分析非核心 claim。弱化措辞即可。 |
| W3 | Must-Fix | REBUT | Should-Fix | Gemini 是补充验证，核心跨模型证据在 Llama-70B。调整措辞而非增加实验。 |
| W4 | Should-Fix | AGREE | Should-Fix | 循环论证明确，修复简单（删除 argument 1）。 |
| W5 | Should-Fix | Partial REBUT | Minor→Should-Fix | Batch-level bootstrap 的 independence 假设在分析层级上基本成立，across-batch correlation 才是真正的 concern。 |
| W6 | Should-Fix | AGREE | Should-Fix | 正文需要显式 ecological correlation caveat + 引用 Robinson (1950)。 |
| W7 | Should-Fix | AGREE | Should-Fix | 与我的 W2 互补。NER null 叙述必须统一。 |
| W8 | Should-Fix | AGREE | Should-Fix | 报告 CIs + 说明 batch 数限制原因即可。 |
| W9 | Should-Fix | AGREE | Should-Fix | 与我的 W3 一致。标注哪些 findings 有跨模型支持。 |
| W10 | Minor | AGREE | Minor | 简要讨论 dataset independence。 |
| W11 | Minor | AGREE | Minor | 报告 seed variability 或讨论相对 effect size。 |

### 总体评价

R1 的审稿质量很高，尤其在统计方法论层面（logit-scale TOST, VIF, ecological correlation, bootstrap coverage）比我的审稿更深入。主要分歧在于 severity：R1 将 W1-W3 标为 Must-Fix，我认为其中 W1-W2 是 Should-Fix（调整 framing/措辞即可），W3 应降为 Should-Fix（Gemini 非核心证据）。

综合两份审稿，论文的核心 strengths 得到一致认可（控制变量设计、分析深度、诚实的负面结果），核心 weaknesses 也有共识（SCS novelty 定位、NER null framing、跨模型验证不对称）。R1 补充了我未涉及的统计层面问题（TOST scale, VIF, bootstrap coverage），我补充了 R1 未涉及的 writing/framing 层面问题（数字密度、Sections 5-6 压缩、checklist in PDF）。

**我维持 Overall Assessment 3.5（Borderline Conference）不变。** R1 的统计问题是 legitimate concerns，但均可通过 framing 调整、措辞弱化和补充讨论来解决，不需要重新实验。修订后论文应能达到 Conference 水平。

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

_source line 2606 · 2026-05-21T18:02:30.523443+00:00_

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


## Round 215

## Round 215

2 recorded events


### User

_source line 2607 · 2026-05-21T18:02:35.143608+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

汇总：我对 R1 的 11 条 Weaknesses 中 9 条表示 AGREE（其中 3 条我认为 severity 应降低），1 条 Partial REBUT（W5 bootstrap independence——batch-level 分析的独立性假设基本成立），1 条 REBUT（W3 Gemini leverage point——核心跨模型证据在 Llama-70B，Gemini 仅为补充验证）。

与 R1 的核心分歧在 severity 而非 direction：R1 的 3 条 Must-Fix（logit TOST、DocRED VIF、Gemini leverage）我均认为可通过 framing 调整解决（Should-Fix），不需要重新实验。两份审稿在论文 strengths 和 weaknesses 的方向性判断上高度一致。

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

_source line 2608 · 2026-05-21T18:02:41.222542+00:00_

Reviewer 2 的交叉回应已收到。等待 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 216

## Round 216

10 recorded events


### User

_source line 2609 · 2026-05-21T18:03:35.243993+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

### Weaknesses 逐条回应

**[AGREE] R2-W1: SCS 相对于 LLM-PEE 的新颖性定位不够清晰**

同意这是一个 framing 问题。Section 2 确实承认了 "our work uses the same metric for scientific analysis"，但这句话淹没在相关工作段落中，未上升为显眼的 novelty statement。读者很可能快速浏览后得出 "SCS = LLM-PEE criterion rebranded" 的印象。

但我认为 R2 对 severity 的判断是恰当的（Should-Fix 而非 Must-Fix）。原因：本文的实际贡献——controlled experimental framework（count curves + BCS-controlled batches）——是实质性的方法论贡献，远超 LLM-PEE 的 post-hoc correlational analysis。LLM-PEE 仅用 similarity 做 partitioning 工具，从未系统研究 confusability 如何 predict performance degradation。这个区分在 Section 3.3（Experiment 2 设计）和 Appendix A（SDGD graph coloring）中隐含体现，但需要一个 explicit framing paragraph 来点明。

**建议**：在 Section 3.2 SCS 定义后加一段，明确说 "SCS 的形式与 LLM-PEE 的 partitioning criterion 相同；本文的贡献不在于 metric 而在于将其作为 controlled variable 嵌入 quasi-experimental framework"。

---

**[AGREE] R2-W2: R² 的 task-dependent 弱信号在 abstract/intro 中表述不均衡**

同意，且这与我的 W7（NER null 叙述张力）高度相关。

Abstract 中 "BCS explains 22–58% of cross-batch RE accuracy variance" 是论文最显眼的数字 claim，但 NER batch-level BCS null（Table 5）仅在 abstract 末尾以 "the NER batch-level null is confirmed on three models" 一句带过，远不及 22–58% 的 prominence。这产生了两层不平衡：

1. **任务间不平衡**：RE 的正面结果被突出，NER 的 null 被弱化——这在 abstract 的信息密度下容易误导读者认为 BCS 是 universal predictor。
2. **与我的 W7 的交叉**：论文在 §5/§6 将 NER 作为 "structural barrier" 叙述，但 Appendix E.2 的 power analysis 说 power 仅 65%。如果 abstract 对 NER null 给予更 prominent 的呈现，就需要同步澄清这究竟是 "confirmed absence" 还是 "inconclusive due to insufficient power"——这正是我在 W7 中要求统一的叙述。

**建议**：Abstract 中 "BCS explains 22–58%..." 之后立刻加入 "while NER shows no batch-level BCS signal across three models, potentially reflecting both task structure differences and restricted BCS range"。

---

**[AGREE] R2-W3: 主实验依赖单一模型，跨模型验证深度不均**

同意，且与我的 W9 一致。但我对 severity 的判断略高于 R2。

R2 关注的是验证 breadth（error taxonomy decomposition 等未跨模型验证），我的 W9 关注的是最有价值发现的 single-model dependency（DocRED R²=58% 仅基于 Qwen3-32B）。这两个角度互补：

- **R2 视角**：error taxonomy（Figure 2 的 IntraSub/Missed 分解）是 Dimension 1 vs Dimension 2 叙述的直接支撑。如果仅在 Qwen3-32B 上验证，就无法确认 IntraSub 与 BCS 单调共变是 general pattern 还是 model-specific artifact。
- **我的视角**：DocRED R²=58% 是论文中最强的定量 claim，但无跨模型支持。如果 LLaMA-70B 在 DocRED 上只有 R²=15%，整个 "22–58% variance explained" 的 headline 就需要重写。

两者叠加，这个问题的 severity 可能应为 borderline Must-Fix。至少需要在 Limitations 中明确标注哪些 findings 仅基于 Qwen3-32B，哪些有跨模型支持。

---

**[REBUT] R2-W4: Sections 5-6 过度压缩——同意问题存在，但不同意将 Section 4.5 移入 appendix**

同意 page 8 叙事密度过高的诊断。Section 4.5（MAVEN centrality confound）+ Section 5（SDGD）+ Section 6（Discussion & Conclusion）挤在同一页确实影响可读性。

但我反对将 Section 4.5 整体移入 appendix。理由：

1. **MAVEN centrality confound 是理解 BCS 适用边界的关键信息。** Table 10（偏相关结果）直接回答了 "BCS 在什么条件下不 work" 这一读者核心问题。仅在 appendix 呈现会导致读者对 BCS 的适用范围产生过度乐观的印象。
2. **Section 4.5 实际上是 Section 4 实验 narrative 的必要收尾。** Sections 4.1–4.3 建立了 BCS 在 RE/NER/ED 上的效应，4.4 分析了 multi-dimensional degradation mechanism，4.5 提供了 boundary condition（MAVEN）。去掉 4.5 会让 Section 4 的叙述在 "BCS works" 上戛然而止，缺少 "when BCS doesn't work" 的平衡。

**替代建议**：压缩 Section 4.5 为 1-2 段（目前约 3 段），仅保留 headline finding（centrality confound + partial correlation 后 BCS 信号消失）。详细的 per-embedding 分析（Qwen3 vs MiniLM 差异）移入 Appendix E。这样可释放约 0.3 页给 Sections 5-6 展开。

---

**[AGREE] R2-W5: 数字/统计呈现密度过高**

同意这是一个 presentation issue。Sections 4.1–4.3 每段都密集嵌入了 r-values、p-values、CI bounds、R² 值，阅读体验像在读 supplementary materials 而非主文。

但我认为这属于 Minor 而非 Should-Fix。论文的目标读者是关注实验设计的 NLP 研究者，他们可能需要这些数字来判断结论的可靠性。问题在于排版组织而非信息量本身。

---

**[AGREE] R2-W6: Responsible NLP Research Checklist 出现在论文 PDF 中**

同意。按 EMNLP 2026/ARR 政策，Checklist 应在 OpenReview submission form 中由作者手动填写，不应出现在论文 PDF 中。论文 pages 9-10 包含了完整的 Checklist（Section A/B/C/D/E），这违反了格式要求。

这在技术上属于 format violation，可能在 desk rejection checklist 中被标记。虽然不影响学术内容评判，但必须修复。

---

**[AGREE] R2-W7: 2 个 orphan bibliography entries**

如果 `park-2024-grammar-aligned` 和 `zhou-2024-grasping` 确实未被 cite，这是容易修复的清理工作。

---

### Questions 交叉评论

**R2-Q1（pair-level r≈0.17 → batch R²=22-58%: aggregation smoothing vs compositional?）**

这与我的 W6（ecological correlation caveat）直接相关。根据 Appendix N 的 Monte Carlo simulation，amplification 主要来自 aggregation smoothing（averaging 消除了 pair-level noise），而非 compositional interaction（batch composition 产生 emergent effect）。Appendix N 的分析公式 SNR × EF/(SNR × EF + 1) 是纯 aggregation model，不包含 compositional terms，且 simulated R²=0.218 与 observed R²=0.218 吻合。

这意味着 batch-level R²=22% 是 pair-level 弱信号在聚合后的 "表观放大"，而非 batch composition 本身产生了额外的 confusability effect。这进一步支持了我在 W6 中提出的 caveat：**论文应更明确地说明 batch-level R² 是 aggregation artifact 而非 batch-level causal mechanism。** 当前正文（§4.3）在报告 R²=22-58% 时未区分这两种解释。

**R2-Q2（MAVEN centrality confound → SCS 在 homogeneous schemas 上不适用？）**

合理的问题。Appendix E / Table 10 的偏相关分析显示，MAVEN 的 BCS-F1 正相关在控制 centrality 后消失（对于 Qwen3 embedding），确实表明 SCS/BCS 在单一 ontology、高 centrality-confusability 共线的 schemas 上丧失了独立预测力。这不是 SCS 的"缺陷"——它准确地反映了当 confusability 被 centrality 解释时，没有额外的 confusability-specific signal。但这确实限定了 SCS 的 practical applicability：对于 FrameNet-style hierarchical ontologies（type 间的层级关系 dominate embedding similarity），SCS 不如对 flat schemas（如 Wikidata-derived Few-NERD/FewRel）有效。这应该在正文讨论中更明确。

**R2-Q3（SDGD 替代方案——hierarchical extraction / retrieval-augmented type selection？）**

论文 §6 简短提到了 "confusability-aware schema design" 作为 practical implication，但未深入讨论 merge-free 替代方案。R2 的建议（hierarchical extraction、retrieval-augmented type selection）是合理的后续方向。我注意到 Section 5 的 SDGD oracle routing（Table 8）恢复了 72.4% vs 50.4% 的准确率，说明 routing 而非 decomposition 本身是瓶颈。这暗示 retrieval-augmented type selection（先 retrieve 相关 sub-schema 再 extract）可能是更有前途的方向。但这属于 future work 讨论范畴，不构成当前论文的 weakness。

**R2-Q4（Table 29 label renaming 为何损害准确率？）**

Appendix X 的解释很清楚：renaming 降低了 SCS（embedding similarity），但 renamed labels（unfamiliar paraphrases）破坏了模型对 type semantics 的理解。Table 29 显示 11/12 renamed pairs 被正确分类（说明模型仍能识别），但整体准确率下降。这说明 BCS 的 confusability effect 与 label familiarity effect 存在 trade-off——降低 confusability 如果以牺牲 label 语义清晰度为代价，净效果可能为负。这进一步削弱了 "通过 label engineering 降低 BCS 来改善性能" 的实践建议。

**R2-Q5（Qwen3 vs MiniLM — practitioners 应该用哪个？）**

论文在 Appendix I（Table 14: BCS aggregation sensitivity）和 Appendix M（SCS embedding ablation）中报告了两个 embedding 的对比。Qwen3 和 MiniLM 在 SCS-confusion correlation（Table 2）和 BCS-F1 方向上一致，但 Qwen3 的 Spearman correlations 通常更强。对 practitioners 的实际建议应该是：两者方向一致，MiniLM 更易部署（384-dim vs 高维），Qwen3 在语义细粒度上可能更好。但这一建议在论文中缺失。

---

### 与我的审稿意见的交叉对照

| 维度 | R2 视角 | R1（我）视角 | 一致性 |
|------|--------|-----------|---------|
| SCS novelty (R2-W1) | Framing 不清 | 未单独提出，但 agree | 共识：Should-Fix framing issue |
| NER null framing (R2-W2) | Abstract 不平衡 | W7: 叙述张力（structural vs power-limited） | **互补**：R2 关注 prominence，我关注 logical consistency。两者指向同一 revision 需求 |
| Cross-model (R2-W3 / R1-W9) | Error taxonomy 未跨模型 | DocRED R²=58% 单模型 + Gemini leverage | **互补**：R2 关注 breadth，我关注 depth。叠加后 severity 应为 borderline Must-Fix |
| Sections 5-6 压缩 (R2-W4) | 移 4.5 到 appendix | 反对移除 4.5，建议压缩 | **分歧**：我认为 boundary condition 信息应留在正文 |
| Checklist 格式 (R2-W6) | 应从 PDF 移除 | 同意 | 共识：必须修复 |

---

### 总体评价

Reviewer 2 的审稿准确地识别了 framing 和 presentation 层面的问题（W1, W2, W4, W5），这些与我关注的方法严谨性问题（W1-W3: TOST/VIF/leverage point）互补而非重叠。两份审稿的核心共识是：

1. **控制变量实验框架是真正的贡献**（R2-S1 / R1-S2），但需要更清晰地与 SCS metric 的 non-novelty 区分开来（R2-W1）。
2. **NER null 的处理需要改进**：R2 要求 prominence 平衡，我要求叙述一致性，两者可在同一修改中解决。
3. **跨模型验证是共同关注**（R2-W3 / R1-W9 / R1-W3），两个角度叠加后这可能是仅次于统计方法问题的第二大 concern。

两份审稿均给出 **3.5（Borderline Conference）**，confidence 均为 4。我认为这反映了论文的真实水平：研究问题重要、实验框架有创意、分析深度出色，但部分核心 claim 的统计基础和跨模型支持需要加强。如果 Must-Fix 问题（我的 W1-W3 + R2-W1/W2 的 framing 修复）能在 revision 中解决，论文有望达到 Conference 水平。

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


### Tool call

_source line 2610 · 2026-05-21T18:04:08.580112+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

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
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 2611 · 2026-05-21T18:04:08.630973+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T17:47:35.357132+00:00\", \"completed_at\": \"2026-05-21T17:51:01.477504+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 1-3\", \"message\": \"前 3 页为连续纯文本（Title/Abstract/Intro/Related Work/Experimental Setup），无任何 display item。第一个视觉锚点（Table 1）直到第 4 页才出现。审稿人在前 2 分钟仅看到密集文本墙，无法快速建立对核心发现的视觉认知。建议在第 1-2 页加入一个 motivating figure（例如 Figure 1 的简化版——展示 schema 复杂度与性能下降的核心 pattern），显著提升第一印象\"}, {\"severity\": \"warning\", \"dimension\": \"pages 1-8\", \"message\": \"主文 8 页仅 4 个 display items（2 figures + 2 tables），对于一篇重实证的控制实验论文偏少（同类论文通常 5-8 个）。大量定量结果（相关系数、p 值、效应量、置信区间）仅以文字陈述，未有图表辅助。附录有 28 个 tables 但主文审稿人不一定会看。建议从附录提升 1-2 个关键表格（如 Table 7 decomposition 对比、或 Table 8 routing 策略对比）到主文，或为核心发现增加汇总可视化\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"主文最后一页（Section 5 Schema Decomposition + Section 6 Discussion and Conclusion）为纯文本页，无任何 display item。与开头的文本墙形成首尾呼应的\\\"文字夹击\\\"感。Section 5 的 decomposition 结果（SDGD 方法的 oracle 恢复率 72.4%、routing failure 分析）适合配一个小型汇总表或示意图\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Table 1（Dataset statistics）使用 booktabs 风格，排版整洁，数字对齐良好。但缺少最优值加粗——此表为统计描述表，不适用加粗，合理\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 1 为全宽双面板图（figure*），左侧 count-degradation 曲线 + 右侧 BCS-controlled 柱状图。颜色方案使用蓝/橙，色盲友好。Caption 自包含，解释了误差棒含义和关键发现。但左面板 legend 文字偏小（约 7pt），打印后可能难以辨认\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 1 右面板柱状图中 \\\"Low BCS\\\" / \\\"High BCS\\\" 标签配箭头的设计有效传达了关键对比，是好的设计选择\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2 全宽双面板（Few-NERD NER + FewRel RE 的 error taxonomy decomposition）。使用蓝/橙/绿/灰多色方案，颜色区分度可接受。Legend 条目较小。Caption 自包含且包含关键数值（ρ = 0.84–1.1）。x 轴 BCS bin 标签清晰可读\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 2（Pairwise SCS-correlation）booktabs 风格，格式规范。数值精度统一（3 位小数）。置信区间标注清晰\"}, {\
…[truncated 943 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2612 · 2026-05-21T18:04:08.631402+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

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
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 2613 · 2026-05-21T18:04:08.782376+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"skipped\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-21T17:47:36.554989+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_51326259fe46fbae9da26b81cf03f1f8\", \"skipped_at\": \"2026-05-21T17:51:22.915921+00:00\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 2614 · 2026-05-21T18:06:25.646245+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "schema-dag-extraction",
  "issues_yaml": "# Review Issues Tracker\n# Updated: 2026-05-21 (Round 23 — Fresh review)\n\n# ============================================================\n# R23 HIGH-PRIORITY (Consensus from R1+R2)\n# ============================================================\n\n- id: R23-C1\n  summary: \"Logit-scale TOST inconclusive 但论文以 linear-scale 为主要结论\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R1 Must-Fix W1, R2 AGREE 但降为 Should-Fix。Logit-scale p=0.209 inconclusive, linear-scale p=0.003。R2 论据：accuracy 在 0.37-0.86 区间，logit 优势有限。共识：至少正文需同时报告两种 scale 结果。\"}\n  action_items:\n    - {round: 23, action: \"正文同时报告 linear 和 logit-scale TOST 结果，结论调整为 'linear-scale bounded, logit-scale inconclusive'\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-C2\n  summary: \"DocRED 偏相关 VIF=50.9 下不可靠，BCS-centrality inseparable\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R1 Must-Fix W2, R2 AGREE 但降为 Should-Fix（非核心 claim，弱化措辞即可）。VIF=50.9 标准误膨胀 ~7.1x。论文已有 'does not uniquely identify causal channel' 但措辞仍偏强。\"}\n  action_items:\n    - {round: 23, action: \"大幅弱化 DocRED 偏相关结论：承认 BCS 和 centrality 在 DocRED 上 inseparable，偏相关仅作 descriptive reference\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-C3\n  summary: \"NER null 叙述张力 + Abstract 中 task-dependent 信号呈现不均衡\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R1-W7 + R2-W2 互补共识。§5/§6 的 'structural barrier' 叙述与 Appendix E.2 的 power analysis (65%) 矛盾。Abstract 突出 22-58% R² 但 NER null 仅一句带过。双方 AGREE 必须统一叙述。\"}\n  action_items:\n    - {round: 23, action: \"统一 NER null 叙述为 'inconclusive, likely attenuated by BCS range restriction'，弱化 §5/§6 中 structural barrier 措辞\", assigned_to: \"\", status: open}\n    - {round: 23, action: \"Abstract 在 22-58% R² 后加 NER null qualifier，给予同等 prominence\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-C4\n  summary: \"跨模型验证不对称：DocRED R²=58% 缺乏跨模型支持，error taxonomy 未跨模型验证\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R1-W9 + R2-W3 互补共识。R1 指出 DocRED R²=58% 仅 Qwen3-32B，R2 指出 error taxonomy (IntraSub 单调性) 未跨模型。R1 交叉后升至 borderline Must-Fix。\"}\n  action_items:\n    - {round: 23, action: \"明确标注哪些 findings 有跨模型支持、哪些仅基于 Qwen3-32B；Limitations 中讨论 DocRED R²=58% 的单模型依赖\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R23 WARNING (Consensus Should-Fix)\n# ============================================================\n\n- id: R23-W1\n  summary: \"SCS vs LLM-PEE novelty framing 不清晰\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R2-W1, R1 交叉 AGREE。SCS = LLM-PEE partitioning criterion 形式一致，novelty 在 experimental paradigm 而非 metric，但 framing 不够突出。\"}\n  action_items:\n    - {round: 23, action: \"Section 2 或 3.2 加 explicit novelty statement：贡献是 controlled experimental framework，非 SCS metric 本身\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-W2\n  summary: \"TOST margin ±3pp 的 argument (1) 存在循环论证\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R1-W4, R2 AGREE。IQR-predicted Δ=2.2pp 来自 BCS 效应自身——用被检验量确定检验 margin。\"}\n  action_items:\n    - {round: 23, action: \"删除 TOST margin 的 argument (1)（BCS effect size anchor），仅保留 (2) amplification threshold 和 (3) Cohen's d 两个外部标准\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-W3\n  summary: \"Batch-level R²=22-58% 的 ecological correlation caveat 不足\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R1-W6, R2 AGREE。Pairwise r²≈1.5% 到 batch R²≈22% 是 aggregation smoothing 非 compositional effect（Appendix N simulation 证实）。正文需 explicit caveat + 引用 Robinson (1950)。\"}\n  action_items:\n    - {round: 23, action: \"§4.3 讨论 R²=22-58% 时加 ecological correlation caveat，引用 Robinson (1950)（已在 Appendix N 引用，移到正文）\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-W4\n  summary: \"Gemini count-16 BCS-controlled 依赖单个 leverage point\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R1-W3 Must-Fix, R2 REBUT 降为 Should-Fix。R2 论据：核心跨模型证据在 Llama-70B，Gemini 仅补充验证。共识：弱化措辞，区分 open-weight 一致复现 vs proprietary 部分支持。分歧保留。\"}\n  action_items:\n    - {round: 23, action: \"正文报告 Gemini leave-one-out sensitivity；弱化跨架构措辞，区分 open-weight vs proprietary 验证深度\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-W5\n  summary: \"Sections 5-6 过度压缩，SDGD 分析和 Discussion 展开不足\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R2-W4, R1 同意问题存在但反对将 §4.5 移入 appendix（boundary condition 应留正文）。R1 建议压缩 §4.5 为 1-2 段释放空间。\"}\n  action_items:\n    - {round: 23, action: \"压缩 §4.5 为 1-2 段（保留 headline finding，per-embedding 细节移入 Appendix），释放约 0.3 页给 §5-§6 展开 practical guidelines 和 future directions\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-W6\n  summary: \"DocRED count curves 仅 5 batches/level，缺 confidence intervals\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R1-W8, R2 AGREE。n=5 per level 偏低，CI 必然很宽。论文已在脚注说明高评估成本原因。\"}\n  action_items:\n    - {round: 23, action: \"报告 DocRED count curve 的完整 CIs；正文或 caption 中说明 batch 数限制原因\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-W7\n  summary: \"Bootstrap CI 的 across-batch correlation 讨论不足\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R1-W5, R2 Partial REBUT。R2 指出 batch-level 分析单位的独立性基本成立（每个 batch 独立采样），但 across-batch 的 shared model/prompt template 可能引入系统性偏差。\"}\n  action_items:\n    - {round: 23, action: \"补充讨论：batches 共享 prompt template 但 type composition 独立采样，bootstrap CI coverage 主要受 across-batch correlation 影响\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R23 INFO / FORMAT\n# ============================================================\n\n- id: R23-F1\n  summary: \"Responsible NLP Checklist 出现在 PDF 中——格式违规\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R2-W6, R1 AGREE。EMNLP 2026/ARR 要求 checklist 在 OpenReview form 填写，不在 PDF 中。占 pages 9-10。\"}\n  action_items:\n    - {round: 23, action: \"从 PDF 移除 checklist section，在 OpenReview form 中填写\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-F2\n  summary: \"正文数字/统计呈现密度过高\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R2-W5, R1 AGREE Minor。§4.1-4.3 每段 10+ 统计值，cognitive overload。\"}\n  action_items:\n    - {round: 23, action: \"将 per-dataset 详细统计值移入 appendix table，正文保留 headline numbers 和方向性结论\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-F3\n  summary: \"Multiple comparisons 不做 correction 的理由不充分\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R1-W10, R2 AGREE Minor。datasets 共享 Wikidata 来源，'independent replication' 假设可讨论。\"}\n  action_items:\n    - {round: 23, action: \"简要讨论 dataset independence 程度\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-F4\n  summary: \"单种子 + greedy decoding 可复现性\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R1-W11, R2 AGREE。Residual SD=0.88pp 约占 BCS effect size 的 18-44%。\"}\n  action_items:\n    - {round: 23, action: \"报告 2-3 个 seed 下 key metrics variability，或讨论 0.88pp residual 相对于 effect size 的比例\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-F5\n  summary: \"2 个 orphan bibliography entries\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R2-W7, R1 AGREE。park-2024-grammar-aligned 和 zhou-2024-grasping 未被引用。\"}\n  action_items:\n    - {round: 23, action: \"删除或引用这两个 bib entries\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R23 MISSING REFERENCES\n# ============================================================\n\n- id: R23-MR1\n  summary: \"Robinson (1950) ecological correlation 应在正文引用\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R1 Missing Ref, R2 AGREE。已在 Appendix N 引用，需移到正文 §4.3。\"}\n  action_items:\n    - {round: 23, action: \"正文 §4.3 引用 Robinson (1950)\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-MR2\n  summary: \"Ren et al. (2016) AFET / Choi et al. (2018) Ultra-Fine Entity Typing\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R2], note: \"Hierarchical entity typing 相关，与 type granularity/confusability 主题相关但非 critical。\"}\n  action_items:\n    - {round: 23, action: \"考虑补充引用（非必须）\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-MR3\n  summary: \"Min et al. (2022) Rethinking Demonstrations in ICL\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R2], note: \"可为 few-shot prompting 下 confusability 影响提供理论支撑。非 critical。\"}\n  action_items:\n    - {round: 23, action: \"考虑补充引用（非必须）\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R22 以前 RESOLVED（精简保留）\n# ============================================================\n\n- id: R22-C1\n  summary: \"Title/Abstract scope overclaim: 'Information Extraction' 但 batch-level Dim2 仅 RE 成立\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 22\n  resolution: \"v12 Abstract 重写完成，区分 pairwise vs batch-level scope，加 task-dependent qualifier + format independence。\"\n  resolution_round: 22\n\n- id: R22-C2\n  summary: \"SCS/BCS novelty 不足，与 LLM-PEE partitioning criterion 一致\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 22\n  resolution: \"v12 Intro/Discussion 强化 non-obvious findings 作为核心贡献。\"\n  resolution_round: 22\n\n- id: R22-C3\n  summary: \"TOST ±3pp margin 循环论证 + logit-scale inconclusive\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 22\n  resolution: \"v12 TOST margin 重构为 practical significance + Cohen's d 双锚，删除循环论证。\"\n  resolution_round: 22\n\n- id: R22-C4\n  summary: \"页数违规：Section 7 (Conclusion) 起始于第9页，超 EMNLP 8页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"v12 Conclusion 并入 Discussion，正文 body ≤ 8 页，0 critical warnings。\"\n  resolution_round: 22\n\n- id: R22-W1\n  summary: \"无有效 mitigation：SDGD/renaming/few-shot 全部失败\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 22\n  resolution: \"v12 Discussion 深化 SDGD 失败原因分析。\"\n  resolution_round: 22\n\n- id: R22-W2\n  summary: \"单种子+FP8 噪声→CI 未含模型级方差\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"v12 报告 corrected bootstrap CI [2.98, 20.08]pp，写入 Limitations + Appendix。\"\n  resolution_round: 22\n\n- id: R22-W3\n  summary: \"Dim2 cross-model 验证不足，Abstract claim 过宽\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 22\n  resolution: \"v12 Dim2 跨模型验证升级至 4 个模型家族。\"\n  resolution_round: 22\n\n- id: R22-W4\n  summary: \"Unconstrained decoding ablation 结论过强 (n=25)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"v12 paired experiment 证明 format-independent。\"\n  resolution_round: 22\n\n- id: R22-W5\n  summary: \"DocRED range-matching power 不足\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"v12 报告 DocRED power analysis (n=84, MDE=10.54pp)。\"\n  resolution_round: 22\n\n- id: R22-W6\n  summary: \"Pair-to-batch R² 放大 simulation 独立性假设有问题\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"v12 Appendix 加非独立性讨论 + Robinson (1950) 引用。\"\n  resolution_round: 22\n\n- id: R22-W7\n  summary: \"Type definitions 分析 (Table 15) 应提升至正文\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"v12 §6 practical implications 加 definitions 无效发现。\"\n  resolution_round: 22\n"
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
    "issues_yaml": "# Review Issues Tracker\n# Updated: 2026-05-21 (Round 23 — Fresh review)\n\n# ============================================================\n# R23 HIGH-PRIORITY (Consensus from R1+R2)\n# ============================================================\n\n- id: R23-C1\n  summary: \"Logit-scale TOST inconclusive 但论文以 linear-scale 为主要结论\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R1 Must-Fix W1, R2 AGREE 但降为 Should-Fix。Logit-scale p=0.209 inconclusive, linear-scale p=0.003。R2 论据：accuracy 在 0.37-0.86 区间，logit 优势有限。共识：至少正文需同时报告两种 scale 结果。\"}\n  action_items:\n    - {round: 23, action: \"正文同时报告 linear 和 logit-scale TOST 结果，结论调整为 'linear-scale bounded, logit-scale inconclusive'\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-C2\n  summary: \"DocRED 偏相关 VIF=50.9 下不可靠，BCS-centrality inseparable\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R1 Must-Fix W2, R2 AGREE 但降为 Should-Fix（非核心 claim，弱化措辞即可）。VIF=50.9 标准误膨胀 ~7.1x。论文已有 'does not uniquely identify causal channel' 但措辞仍偏强。\"}\n  action_items:\n    - {round: 23, action: \"大幅弱化 DocRED 偏相关结论：承认 BCS 和 centrality 在 DocRED 上 inseparable，偏相关仅作 descriptive reference\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-C3\n  summary: \"NER null 叙述张力 + Abstract 中 task-dependent 信号呈现不均衡\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R1-W7 + R2-W2 互补共识。§5/§6 的 'structural barrier' 叙述与 Appendix E.2 的 power analysis (65%) 矛盾。Abstract 突出 22-58% R² 但 NER null 仅一句带过。双方 AGREE 必须统一叙述。\"}\n  action_items:\n    - {round: 23, action: \"统一 NER null 叙述为 'inconclusive, likely attenuated by BCS range restriction'，弱化 §5/§6 中 structural barrier 措辞\", assigned_to: \"\", status: open}\n    - {round: 23, action: \"Abstract 在 22-58% R² 后加 NER null qualifier，给予同等 prominence\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-C4\n  summary: \"跨模型验证不对称：DocRED R²=58% 缺乏跨模型支持，error taxonomy 未跨模型验证\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R1-W9 + R2-W3 互补共识。R1 指出 DocRED R²=58% 仅 Qwen3-32B，R2 指出 error taxonomy (IntraSub 单调性) 未跨模型。R1 交叉后升至 borderline Must-Fix。\"}\n  action_items:\n    - {round: 23, action: \"明确标注哪些 findings 有跨模型支持、哪些仅基于 Qwen3-32B；Limitations 中讨论 DocRED R²=58% 的单模型依赖\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R23 WARNING (Consensus Should-Fix)\n# ============================================================\n\n- id: R23-W1\n  summary: \"SCS vs LLM-PEE novelty framing 不清晰\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R2-W1, R1 交叉 AGREE。SCS = LLM-PEE partitioning criterion 形式一致，novelty 在 experimental paradigm 而非 metric，但 framing 不够突出。\"}\n  action_items:\n    - {round: 23, action: \"Section 2 或 3.2 加 explicit novelty statement：贡献是 controlled experimental framework，非 SCS metric 本身\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-W2\n  summary: \"TOST margin ±3pp 的 argument (1) 存在循环论证\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R1-W4, R2 AGREE。IQR-predicted Δ=2.2pp 来自 BCS 效应自身——用被检验量确定检验 margin。\"}\n  action_items:\n    - {round: 23, action: \"删除 TOST margin 的 argument (1)（BCS effect size anchor），仅保留 (2) amplification threshold 和 (3) Cohen's d 两个外部标准\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-W3\n  summary: \"Batch-level R²=22-58% 的 ecological correlation caveat 不足\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R1-W6, R2 AGREE。Pairwise r²≈1.5% 到 batch R²≈22% 是 aggregation smoothing 非 compositional effect（Appendix N simulation 证实）。正文需 explicit caveat + 引用 Robinson (1950)。\"}\n  action_items:\n    - {round: 23, action: \"§4.3 讨论 R²=22-58% 时加 ecological correlation caveat，引用 Robinson (1950)（已在 Appendix N 引用，移到正文）\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-W4\n  summary: \"Gemini count-16 BCS-controlled 依赖单个 leverage point\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R1-W3 Must-Fix, R2 REBUT 降为 Should-Fix。R2 论据：核心跨模型证据在 Llama-70B，Gemini 仅补充验证。共识：弱化措辞，区分 open-weight 一致复现 vs proprietary 部分支持。分歧保留。\"}\n  action_items:\n    - {round: 23, action: \"正文报告 Gemini leave-one-out sensitivity；弱化跨架构措辞，区分 open-weight vs proprietary 验证深度\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-W5\n  summary: \"Sections 5-6 过度压缩，SDGD 分析和 Discussion 展开不足\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R2-W4, R1 同意问题存在但反对将 §4.5 移入 appendix（boundary condition 应留正文）。R1 建议压缩 §4.5 为 1-2 段释放空间。\"}\n  action_items:\n    - {round: 23, action: \"压缩 §4.5 为 1-2 段（保留 headline finding，per-embedding 细节移入 Appendix），释放约 0.3 页给 §5-§6 展开 practical guidelines 和 future directions\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-W6\n  summary: \"DocRED count curves 仅 5 batches/level，缺 confidence intervals\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R1-W8, R2 AGREE。n=5 per level 偏低，CI 必然很宽。论文已在脚注说明高评估成本原因。\"}\n  action_items:\n    - {round: 23, action: \"报告 DocRED count curve 的完整 CIs；正文或 caption 中说明 batch 数限制原因\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-W7\n  summary: \"Bootstrap CI 的 across-batch correlation 讨论不足\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R1-W5, R2 Partial REBUT。R2 指出 batch-level 分析单位的独立性基本成立（每个 batch 独立采样），但 across-batch 的 shared model/prompt template 可能引入系统性偏差。\"}\n  action_items:\n    - {round: 23, action: \"补充讨论：batches 共享 prompt template 但 type composition 独立采样，bootstrap CI coverage 主要受 across-batch correlation 影响\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R23 INFO / FORMAT\n# ============================================================\n\n- id: R23-F1\n  summary: \"Responsible NLP Checklist 出现在 PDF 中——格式违规\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R2-W6, R1 AGREE。EMNLP 2026/ARR 要求 checklist 在 OpenReview form 填写，不在 PDF 中。占 pages 9-10。\"}\n  action_items:\n    - {round: 23, action: \"从 PDF 移除 checklist section，在 OpenReview form 中填写\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-F2\n  summary: \"正文数字/统计呈现密度过高\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R2-W5, R1 AGREE Minor。§4.1-4.3 每段 10+ 统计值，cognitive overload。\"}\n  action_items:\n    - {round: 23, action: \"将 per-dataset 详细统计值移入 appendix table，正文保留 headline numbers 和方向性结论\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-F3\n  summary: \"Multiple comparisons 不做 correction 的理由不充分\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R1-W10, R2 AGREE Minor。datasets 共享 Wikidata 来源，'independent replication' 假设可讨论。\"}\n  action_items:\n    - {round: 23, action: \"简要讨论 dataset independence 程度\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-F4\n  summary: \"单种子 + greedy decoding 可复现性\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R1-W11, R2 AGREE。Residual SD=0.88pp 约占 BCS effect size 的 18-44%。\"}\n  action_items:\n    - {round: 23, action: \"报告 2-3 个 seed 下 key metrics variability，或讨论 0.88pp residual 相对于 effect size 的比例\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-F5\n  summary: \"2 个 orphan bibliography entries\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R2-W7, R1 AGREE。park-2024-grammar-aligned 和 zhou-2024-grasping 未被引用。\"}\n  action_items:\n    - {round: 23, action: \"删除或引用这两个 bib entries\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R23 MISSING REFERENCES\n# ============================================================\n\n- id: R23-MR1\n  summary: \"Robinson (1950) ecological correlation 应在正文引用\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R1 Missing Ref, R2 AGREE。已在 Appendix N 引用，需移到正文 §4.3。\"}\n  action_items:\n    - {round: 23, action: \"正文 §4.3 引用 Robinson (1950)\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-MR2\n  summary: \"Ren et al. (2016) AFET / Choi et al. (2018) Ultra-Fine Entity Typing\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R2], note: \"Hierarchical entity typing 相关，与 type granularity/confusability 主题相关但非 critical。\"}\n  action_items:\n    - {round: 23, action: \"考虑补充引用（非必须）\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-MR3\n  summary: \"Min et al. (2022) Rethinking Demonstrations in ICL\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 23\n  mentions:\n    - {round: 23, reviewers: [R2], note: \"可为 few-shot prompting 下 confusability 影响提供理论支撑。非 critical。\"}\n  action_items:\n    - {round: 23, action: \"考虑补充引用（非必须）\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R22 以前 RESOLVED（精简保留）\n# ============================================================\n\n- id: R22-C1\n  summary: \"Title/Abstract scope overclaim: 'Information Extraction' 但 batch-level Dim2 仅 RE 成立\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 22\n  resolution: \"v12 Abstract 重写完成，区分 pairwise vs batch-level scope，加 task-dependent qualifier + format independence。\"\n  resolution_round: 22\n\n- id: R22-C2\n  summary: \"SCS/BCS novelty 不足，与 LLM-PEE partitioning criterion 一致\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 22\n  resolution: \"v12 Intro/Discussion 强化 non-obvious findings 作为核心贡献。\"\n  resolution_round: 22\n\n- id: R22-C3\n  summary: \"TOST ±3pp margin 循环论证 + logit-scale inconclusive\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 22\n  resolution: \"v12 TOST margin 重构为 practical significance + Cohen's d 双锚，删除循环论证。\"\n  resolution_round: 22\n\n- id: R22-C4\n  summary: \"页数违规：Section 7 (Conclusion) 起始于第9页，超 EMNLP 8页限制\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"v12 Conclusion 并入 Discussion，正文 body ≤ 8 页，0 critical warnings。\"\n  resolution_round: 22\n\n- id: R22-W1\n  summary: \"无有效 mitigation：SDGD/renaming/few-shot 全部失败\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 22\n  resolution: \"v12 Discussion 深化 SDGD 失败原因分析。\"\n  resolution_round: 22\n\n- id: R22-W2\n  summary: \"单种子+FP8 噪声→CI 未含模型级方差\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"v12 报告 corrected bootstrap CI [2.98, 20.08]pp，写入 Limitations + Appendix。\"\n  resolution_round: 22\n\n- id: R22-W3\n  summary: \"Dim2 cross-model 验证不足，Abstract claim 过宽\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 22\n  resolution: \"v12 Dim2 跨模型验证升级至 4 个模型家族。\"\n  resolution_round: 22\n\n- id: R22-W4\n  summary: \"Unconstrained decoding ablation 结论过强 (n=25)\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"v12 paired experiment 证明 format-independent。\"\n  resolution_round: 22\n\n- id: R22-W5\n  summary: \"DocRED range-matching power 不足\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"v12 报告 DocRED power analysis (n=84, MDE=10.54pp)。\"\n  resolution_round: 22\n\n- id: R22-W6\n  summary: \"Pair-to-batch R² 放大 simulation 独立性假设有问题\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"v12 Appendix 加非独立性讨论 + Robinson (1950) 引用。\"\n  resolution_round: 22\n\n- id: R22-W7\n  summary: \"Type definitions 分析 (Table 15) 应提升至正文\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"v12 §6 practical implications 加 definitions 无效发现。\"\n  resolution_round: 22\n"
  }
}
```

</details>

---


### Tool result

_source line 2615 · 2026-05-21T18:06:25.748166+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml\", \"bytes\": 13847}, \"error\": \"\"}"}

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

_source line 2616 · 2026-05-21T18:09:17.257249+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "schema-dag-extraction",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5",
  "report": "# 审稿报告 — Round 23 (Fresh Review)\n\n**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n**Venue**: EMNLP 2026 via ARR May 2026 (Deadline: 2026-05-25)\n**类型**: Long Paper (8 pages)\n**审稿人**: Reviewer 1（方法严谨性）+ Reviewer 2（新颖性/完整性/格式合规）\n**审稿模式**: 圆桌 1 轮 + 交叉分享\n\n---\n\n## Summary\n\n本文研究 training-free LLM IE 中 schema 复杂度对性能的影响，提出 Schema Confusability Score (SCS) 及其 batch-level 聚合 Batch Confusability Score (BCS)，通过 count curves 和 BCS-controlled 两套互补实验范式，在 4 个数据集（Few-NERD/FewRel/DocRED/MAVEN）、3 个 IE 任务（NER/RE/ED）和 4 个模型（Qwen3-32B/LLaMA-8B/LLaMA-70B/Gemini 2.5 Flash）上系统分析。核心发现：性能退化沿两个维度展开——count-driven recall decline 和 confusability-driven type substitution；BCS 在 RE 上解释 22-58% 的 cross-batch 方差但在 NER 上信号为 null；schema decomposition (SDGD) 因 merge amplification 和 routing failure 而失败。\n\n---\n\n## Strengths\n\n**S1. 研究问题重要且 understudied。** 首个系统隔离 type count 与 type confusability 的控制研究。现有工作（LLM-PEE, CrossAgentIE 等）观察到 schema 变大时性能下降，但未分离出具体因素。confusability-aware 视角填补了重要的认知空白。[R1-S1, R2-S1 共识]\n\n**S2. 控制变量实验设计质量高。** Count curves + BCS-controlled 两套范式交叉设计，BCS-controlled 的 extreme batch 构建（greedy search on SCS graph）是有创意的 quasi-experimental manipulation，远超 LLM-PEE 的 post-hoc correlational analysis。[R1-S2, R2-S1 共识]\n\n**S3. 分析深度在 empirical NLP 论文中罕见。** 28 页含 18 个附录，涵盖 TOST 等价性检验、Monte Carlo simulation、prompt sensitivity（5 种 prompt variant）、format independence（paired constrained/unconstrained）、within-pool analysis、label renaming intervention、relaxed matching 等。[R1-S3, R2-S2 共识]\n\n**S4. 诚实的 null result 和负面结果报告。** NER batch-level BCS null、MAVEN centrality confound、SDGD 全面失败、label renaming 反效果——均未掩饰，配有详细的 power analysis 和机制分析。SDGD oracle routing (72.4% vs 50.4%) 精准定位了 decompose-then-merge 的瓶颈在 routing 而非 decomposition。[R1-S4/S6, R2-S3 共识]\n\n**S5. BCS 的独立预测力有干净验证。** Appendix O joint model 分析（BCS unique R²=0.259 vs composition unique R²=0.299, VIF=1.06）有力支持 BCS 捕获 confusability-specific signal 而非 type difficulty proxy。[R1-S5]\n\n**S6. Limitations 部分坦诚全面。** 覆盖 model coverage、effect size、task scope、causal mechanism、data contamination、domain/language scope、multiple comparisons 共 7 个点。[R2-S5]\n\n---\n\n## Weaknesses\n\n### 高优先级（两位 Reviewer 共识，需优先处理）\n\n**W1 [R1 Must-Fix / R2 Should-Fix] Logit-scale TOST inconclusive 但论文以 linear-scale 为主要结论。**\nAppendix C 坦承 logit-scale TOST 在 count×BCS interaction 上 inconclusive（p=0.209），但将 linear-scale 作为 primary analysis（p=0.003 at ±3pp）。对于 bounded [0,1] accuracy data，logit-scale 通常更合适。R2 指出 accuracy 在 0.37-0.86 区间内 logit 优势有限，但双方一致认为正文需同时报告两种 scale 结果，结论至少调整为\"linear-scale bounded, logit-scale inconclusive\"。\n→ **Action**: 正文报告 logit-scale 结果，调整 interaction bounded 的 claim 强度。\n\n**W2 [R1 Must-Fix / R2 Should-Fix] DocRED 偏相关 VIF=50.9 下不可靠。**\nDocRED BCS-centrality collinearity 达 VIF=50.9（r=0.99），标准误膨胀 ~7.1×，偏相关 point estimate 极不稳定。论文称\"BCS retains predictive value but does not uniquely identify the causal channel\"——在 VIF=50.9 下，甚至这一措辞都过强。R2 指出 FewRel BCS-controlled（VIF=1.18）是更干净的核心证据，DocRED 偏相关仅为补充。\n→ **Action**: 大幅弱化 DocRED 偏相关结论，承认 BCS 和 centrality 在 DocRED 上 inseparable。\n\n**W3 [R1-W7 + R2-W2 共识] NER null 叙述张力 + Abstract task-dependent 信号不均衡。**\n两层问题交织：(1) §5/§6 将 NER 描述为\"structural barrier\"，但 Appendix E.2 power analysis 显示 power 仅 65%——两者不能同时成立；(2) Abstract 突出 22-58% R² 但 NER null 仅一句带过，造成 framing 不平衡。R1 从 logical consistency 角度、R2 从 framing prominence 角度指出同一问题。\n→ **Action**: 统一 NER null 叙述为\"inconclusive, likely attenuated\"；Abstract 给 NER null 同等 prominence。\n\n**W4 [R1-W9 + R2-W3 共识，交叉后升至 borderline Must-Fix] 跨模型验证不对称。**\n所有 core experiments 仅在 Qwen3-32B 上完成。跨模型验证（LLaMA-70B/8B, Gemini）仅覆盖 count curves + BCS-controlled，未涵盖 error taxonomy decomposition、centrality confound analysis、SDGD。最关键的是：DocRED R²=58%（论文最强定量 claim）完全缺乏跨模型支持。R1 指出如果 LLaMA-70B 在 DocRED 上只有 R²=15%，headline claim 需重写。\n→ **Action**: 明确标注各 finding 的跨模型支持状况；Limitations 讨论 DocRED R²=58% 的单模型依赖。\n\n### Should-Fix（两位 Reviewer 共识或单方提出且对方认可）\n\n**W5 [R2-W1, R1 AGREE] SCS vs LLM-PEE novelty framing 不清晰。**\nSCS 与 LLM-PEE partitioning criterion 形式完全一致（pairwise cosine similarity of type name embeddings）。论文在 Section 2 承认但未上升为显眼的 novelty statement。读者容易得出\"SCS = LLM-PEE rebranded\"的印象。实际贡献是 controlled experimental framework，需明确点明。\n→ **Action**: Section 2 或 3.2 加 explicit novelty statement。\n\n**W6 [R1-W4, R2 AGREE] TOST margin ±3pp 的 argument (1) 循环论证。**\n三个 converging arguments 中 argument (1)（IQR-predicted Δ=2.2pp from BCS effect itself）直接引用被检验量的 effect size 确定 margin。\n→ **Action**: 删除 argument (1)，仅保留 (2)(3) 两个外部标准。\n\n**W7 [R1-W6, R2 AGREE] Batch-level R²=22-58% 缺少 ecological correlation caveat。**\nPairwise r²≈1.5% 到 batch R²≈22% 的 ~15× 放大本质是 ecological correlation。Appendix N Monte Carlo simulation 证实是 aggregation smoothing（EF≈3.35）而非 compositional effect。正文需显式 caveat + 引用 Robinson (1950)。\n→ **Action**: §4.3 加 ecological correlation caveat，将 Robinson (1950) 引用从 Appendix 移到正文。\n\n**W8 [R2-W4, R1 部分同意] Sections 5-6 过度压缩。**\nPage 8 承载 centrality confound + SDGD 全部分析 + Discussion and Conclusion，叙事密度过高。R2 建议移 §4.5 到 appendix，R1 反对（boundary condition 应留正文），建议压缩 §4.5 为 1-2 段。\n→ **Action**: 压缩 §4.5（per-embedding 细节移入 Appendix），释放空间给 §5-§6 展开 practical guidelines 和 future directions。\n\n**W9 [R1-W3, R2 REBUT 降级] Gemini count-16 BCS-controlled 依赖单个 leverage point。**\nLeave-one-out 后相关从 r=-0.80 降至 r=-0.42。R1 标 Must-Fix，R2 rebut 降为 Should-Fix——核心跨模型证据在 LLaMA-70B（decline −30.7pp vs Qwen3 −30.1pp），Gemini 仅补充验证。**此为两位 Reviewer 的主要 severity 分歧。**\n→ **Action**: 正文报告 leave-one-out sensitivity；区分\"open-weight 一致复现\"vs\"proprietary 部分支持\"。\n\n**W10 [R1-W8, R2 AGREE] DocRED count curves 仅 5 batches/level。**\nn=5 per level 偏低（vs Few-NERD 25, FewRel 25），CI 必然很宽。论文已在脚注说明高评估成本原因。\n→ **Action**: 报告完整 CIs，正文说明 batch 数限制原因。\n\n**W11 [R1-W5, R2 Partial REBUT] Bootstrap CI 非独立性讨论不足。**\nR2 指出 batch-level 分析单位的独立性基本成立（每个 batch 独立采样 type set），但 across-batch 的 shared model/prompt template 可能引入系统性偏差。\n→ **Action**: 补充讨论 across-batch correlation 对 bootstrap CI coverage 的潜在影响。\n\n### Minor\n\n**W12 [R2-W6, R1 AGREE] Responsible NLP Checklist 出现在 PDF 中（格式违规）。**\n按 EMNLP 2026/ARR 政策，Checklist 应在 OpenReview form 中填写，不在 PDF 中。Pages 9-10 包含完整 Checklist。可能在 desk rejection checklist 中被标记。\n→ **Action**: 从 PDF 移除，在 OpenReview form 中填写。\n\n**W13 [R2-W5, R1 AGREE] 正文数字/统计呈现密度过高。**\n§4.1-4.3 每段嵌入 10+ 统计值，cognitive overload。\n→ **Action**: per-dataset 详细统计值移入 appendix table，正文保留 headline numbers。\n\n**W14 [R1-W10, R2 AGREE] Multiple comparisons 不做 correction 的理由不充分。**\nFew-NERD 和 FewRel 共享 Wikidata 来源，\"independent replication\"假设可讨论。\n→ **Action**: 简要讨论 dataset independence 程度。\n\n**W15 [R1-W11, R2 AGREE] 单种子 + greedy decoding 可复现性。**\nResidual SD=0.88pp 约占 BCS effect size 的 18-44%。\n→ **Action**: 报告 seed variability 或讨论 residual 相对于 effect size 的比例。\n\n**W16 [R2-W7, R1 AGREE] 2 个 orphan bibliography entries。**\n`park-2024-grammar-aligned` 和 `zhou-2024-grasping` 未被引用。\n→ **Action**: 删除或引用。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键判断上达成一致：\n\n1. **控制变量实验框架是本文真正的贡献**，远超 SCS metric 本身的新颖性。论文需要更清晰地区分这两层。\n2. **NER batch-level BCS null 的处理需要改进**：叙述一致性（R1）+ framing prominence（R2）两个角度指向同一修改需求。\n3. **跨模型验证是核心薄弱点**：R1 关注 DocRED R²=58% 的单模型依赖，R2 关注 error taxonomy 未跨模型验证——叠加后为仅次于统计方法问题的第二大 concern。\n4. **SDGD 负面结果有独立价值**，对 decompose-then-merge 范式的失败分析（merge amplification + routing failure）值得发表。\n5. **分析深度出色**：28 页 18 附录，是 empirical NLP 论文的高水准。\n6. **整体评分 3.5 Borderline Conference**：两人独立给出相同分数。\n\n## Reviewer Divergence [REBUT]\n\n主要分歧在 **severity 而非 direction**：\n\n| 问题 | R1 判断 | R2 判断 | 分歧本质 |\n|------|---------|---------|----------|\n| Logit TOST (W1) | Must-Fix | Should-Fix | R2: accuracy 不在极端区间，linear 非完全不当 |\n| DocRED VIF (W2) | Must-Fix | Should-Fix | R2: 非核心 claim，弱化措辞即可 |\n| Gemini leverage (W9) | Must-Fix | Should-Fix | R2: 核心跨模型证据在 LLaMA-70B，Gemini 仅补充 |\n| §4.5 处理 (W8) | 留正文压缩 | 移入 appendix | R1: boundary condition 信息应留正文 |\n\n无方向性对立矛盾。所有分歧均可通过 framing 调整和措辞弱化解决，不需要重新实验。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1 [R1/R2 共同关注]** Logit-scale TOST inconclusive (p=0.209) 与 linear-scale TOST (p=0.003) 的分歧——作者选择 linear-scale 作为 primary analysis 的统计理由是什么？\n\n**Q2 [R1]** DocRED VIF=50.9 下的偏相关（Table 11）是否在 bootstrapped/permutation 框架下稳定？是否尝试过 ridge regression？\n\n**Q3 [R1]** Gemini count-16 BCS-controlled 的 leave-one-out 后，具体 Pearson r 和 p-value 数值？\n\n**Q4 [R1/R2 共同关注]** NER batch-level BCS null：作者倾向于\"structural absence\"还是\"power insufficient\"的解释？两者在论文中的不一致如何解决？\n\n**Q5 [R2]** Pair-to-batch R² 放大（1.5% → 22%）是 aggregation smoothing 还是存在 compositional interaction？Appendix N simulation 支持前者，但论文在 §6 的 practical implications 更像假设后者。\n\n**Q6 [R2]** SCS/BCS 在 homogeneous schemas（如 MAVEN/FrameNet）上不适用——这对 generalizability 有何影响？实践中如何判断一个 schema 是否适合用 BCS 做诊断？\n\n**Q7 [R2]** Label renaming 降低 SCS 后反而损害准确率（Table 29）——这是否意味着\"confusability-aware schema design\"的实践建议本质上不可行？\n\n---\n\n## Missing References\n\n1. **Robinson, W.S. (1950)** \"Ecological Correlations and the Behavior of Individuals\" — 已在 Appendix N 引用，需移到正文 §4.3 作为 batch-level R² 的 ecological correlation 警示。[R1 提出, R2 AGREE]\n2. **Ren et al. (2016)** \"AFET\" / **Choi et al. (2018)** \"Ultra-Fine Entity Typing\" — Hierarchical entity typing 工作，与 type granularity/confusability 主题相关。[R2 建议, 非 critical]\n3. **Min et al. (2022)** \"Rethinking the Role of Demonstrations in In-Context Learning\" — 可为 few-shot confusability 影响提供理论支撑。[R2 建议, 非 critical]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：已跳过。** 外部审稿请求已发送（2026-05-21T17:47 UTC），但用户选择跳过（2026-05-21T17:51 UTC）。本轮无外部审稿结果。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成。** 3 warnings, 0 critical, 11 info。\n\n**主要发现：**\n\n1. **[Warning] 前 3 页无任何 display item。** Pages 1-3 为连续纯文本（Title/Abstract/Intro/Related Work/Experimental Setup），第一个视觉锚点（Table 1）到第 4 页才出现。审稿人在前 2 分钟仅看到密集文本墙。建议在 page 1-2 加入 motivating figure（如 Figure 1 的简化版）。\n\n2. **[Warning] 主文 8 页仅 4 个 display items（2 figures + 2 tables）。** 对于重实证的控制实验论文偏少（同类论文通常 5-8 个）。大量定量结果仅以文字陈述。建议从附录提升 1-2 个关键表格到主文。\n\n3. **[Warning] Page 8（最后一页正文）为纯文本。** Section 5 + Section 6 无任何 display item，与开头形成\"文字夹击\"。SDGD decomposition 结果适合配一个小型汇总表。\n\n**正面评价：** Figure 1/2 色盲友好（蓝/橙方案），caption 自包含，Table 排版使用 booktabs 规范。References 无 [?] 未解析引用。Limitations 篇幅适当。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5（Borderline Conference）**\n**Confidence: 4/5**\n\n### 评分理由\n\n**研究问题（+）**：重要且 understudied。首个系统隔离 count vs confusability 的控制研究，对 IE schema 设计有直接实践意义。\n\n**实验设计（+）**：控制变量框架（count curves + BCS-controlled batches）质量高，quasi-experimental manipulation 远超先前 correlational work。分析深度（28 页 18 附录）在 empirical NLP 论文中出色。\n\n**负面结果价值（+）**：SDGD 失败的机制分析、label renaming 反效果、few-shot 扩大 gap——这些 non-obvious negative findings 有独立发表价值。\n\n**统计基础裂缝（−）**：logit-scale TOST inconclusive 削弱 interaction bounded claim；DocRED VIF=50.9 使偏相关不可靠；batch-level R² 缺少 ecological correlation caveat。这些问题均可通过 framing 调整解决，但当前状态下部分核心 claim 的统计支撑不够稳固。\n\n**跨模型验证不足（−）**：DocRED R²=58%（最强定量 claim）和 error taxonomy 仅基于 Qwen3-32B。Gemini 验证有 leverage point 问题。\n\n**Novelty 定位（−）**：SCS 与 LLM-PEE 形式重叠，实验范式的 novelty 需要更清晰的 framing。\n\n**NER null 处理（−）**：structural barrier vs power insufficient 的双重叙述需要统一。\n\n### 修订路径\n\n所有高优先级问题均可通过 **framing 调整、措辞弱化和补充讨论** 解决，不需要重新实验。具体修订：\n1. 正文同时报告 linear 和 logit-scale TOST 结果\n2. 弱化 DocRED 偏相关 claim\n3. 统一 NER null 叙述，Abstract 给予同等 prominence\n4. 标注各 finding 的跨模型支持状况\n5. 加 SCS novelty statement 和 ecological correlation caveat\n6. 从 PDF 移除 Responsible NLP Checklist\n7. 压缩 §4.5，扩展 §5-§6\n\n修订后论文有望达到 **4.0（Conference）** 水平。当前状态适合 **Findings track**（3.0-3.5）。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 22-58% R² claim 需加 NER null qualifier（W3）\n- \"task-dependent effect structures\" 的表述是好的，但需要更突出\n\n### Section 1 (Introduction)\n- RQ1-RQ3 设置清晰，但 RQ1 的回答（§4.3）是 task-dependent 的——RE yes, NER inconclusive——这一 nuance 在 Introduction 的 findings 概述中不够明确\n- Contribution list 需要更突出 experimental paradigm 而非 metric\n\n### Section 2 (Related Work)\n- LLM-PEE 的区分当前是在 \"our work differs in three ways\" 中处理的，需要在 SCS novelty paragraph 中更直接地承认形式重叠并点明真正的 novelty\n\n### Section 3 (Experimental Setup)\n- SCS/BCS 定义清晰，操作化良好\n- 数据集选择合理，但 DocRED 5 batches/level 的限制需要在正文中说明（W10）\n- 单种子 + greedy decoding 的设计合理但需要在 Limitations 中更定量地讨论 residual variance\n\n### Section 4 (Results)\n- §4.1-4.3 统计值密度过高，考虑将 per-dataset 细节移入 appendix table\n- §4.3 R²=22-58% 需加 ecological correlation caveat + Robinson (1950)\n- §4.4 NER-RE asymmetry 分析是论文亮点之一\n- §4.5 centrality confound 留在正文但应压缩\n\n### Section 5 (SDGD)\n- 负面结果有价值但分析过度压缩\n- Oracle routing 恢复 72.4% 的发现很有启示性，值得更多讨论空间\n\n### Section 6 (Discussion and Conclusion)\n- 过短，practical implications 仅一段\n- 缺少 future directions（hierarchical extraction, routing-aware decomposition, task-adaptive BCS thresholds）\n- Confusability-aware schema design 的建议需要更谨慎（W7 ecological correlation + Q7 renaming 反效果）\n\n### Limitations\n- 覆盖面充分（7 个点）\n- 需补充：DocRED R²=58% 单模型依赖、跨模型验证的不对称性\n\n### Format\n- 正文 ≤ 8 页 ✓\n- ACL template with [review] option ✓\n- Anonymous ✓\n- Limitations section present ✓\n- **Checklist 在 PDF 中需移除** ✗\n- **`\\enlargethispage{3\\baselineskip}` 在 sdgd_negative.tex 中**——formatting hack，审稿人可能注意到"
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
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5",
    "report": "# 审稿报告 — Round 23 (Fresh Review)\n\n**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n**Venue**: EMNLP 2026 via ARR May 2026 (Deadline: 2026-05-25)\n**类型**: Long Paper (8 pages)\n**审稿人**: Reviewer 1（方法严谨性）+ Reviewer 2（新颖性/完整性/格式合规）\n**审稿模式**: 圆桌 1 轮 + 交叉分享\n\n---\n\n## Summary\n\n本文研究 training-free LLM IE 中 schema 复杂度对性能的影响，提出 Schema Confusability Score (SCS) 及其 batch-level 聚合 Batch Confusability Score (BCS)，通过 count curves 和 BCS-controlled 两套互补实验范式，在 4 个数据集（Few-NERD/FewRel/DocRED/MAVEN）、3 个 IE 任务（NER/RE/ED）和 4 个模型（Qwen3-32B/LLaMA-8B/LLaMA-70B/Gemini 2.5 Flash）上系统分析。核心发现：性能退化沿两个维度展开——count-driven recall decline 和 confusability-driven type substitution；BCS 在 RE 上解释 22-58% 的 cross-batch 方差但在 NER 上信号为 null；schema decomposition (SDGD) 因 merge amplification 和 routing failure 而失败。\n\n---\n\n## Strengths\n\n**S1. 研究问题重要且 understudied。** 首个系统隔离 type count 与 type confusability 的控制研究。现有工作（LLM-PEE, CrossAgentIE 等）观察到 schema 变大时性能下降，但未分离出具体因素。confusability-aware 视角填补了重要的认知空白。[R1-S1, R2-S1 共识]\n\n**S2. 控制变量实验设计质量高。** Count curves + BCS-controlled 两套范式交叉设计，BCS-controlled 的 extreme batch 构建（greedy search on SCS graph）是有创意的 quasi-experimental manipulation，远超 LLM-PEE 的 post-hoc correlational analysis。[R1-S2, R2-S1 共识]\n\n**S3. 分析深度在 empirical NLP 论文中罕见。** 28 页含 18 个附录，涵盖 TOST 等价性检验、Monte Carlo simulation、prompt sensitivity（5 种 prompt variant）、format independence（paired constrained/unconstrained）、within-pool analysis、label renaming intervention、relaxed matching 等。[R1-S3, R2-S2 共识]\n\n**S4. 诚实的 null result 和负面结果报告。** NER batch-level BCS null、MAVEN centrality confound、SDGD 全面失败、label renaming 反效果——均未掩饰，配有详细的 power analysis 和机制分析。SDGD oracle routing (72.4% vs 50.4%) 精准定位了 decompose-then-merge 的瓶颈在 routing 而非 decomposition。[R1-S4/S6, R2-S3 共识]\n\n**S5. BCS 的独立预测力有干净验证。** Appendix O joint model 分析（BCS unique R²=0.259 vs composition unique R²=0.299, VIF=1.06）有力支持 BCS 捕获 confusability-specific signal 而非 type difficulty proxy。[R1-S5]\n\n**S6. Limitations 部分坦诚全面。** 覆盖 model coverage、effect size、task scope、causal mechanism、data contamination、domain/language scope、multiple comparisons 共 7 个点。[R2-S5]\n\n---\n\n## Weaknesses\n\n### 高优先级（两位 Reviewer 共识，需优先处理）\n\n**W1 [R1 Must-Fix / R2 Should-Fix] Logit-scale TOST inconclusive 但论文以 linear-scale 为主要结论。**\nAppendix C 坦承 logit-scale TOST 在 count×BCS interaction 上 inconclusive（p=0.209），但将 linear-scale 作为 primary analysis（p=0.003 at ±3pp）。对于 bounded [0,1] accuracy data，logit-scale 通常更合适。R2 指出 accuracy 在 0.37-0.86 区间内 logit 优势有限，但双方一致认为正文需同时报告两种 scale 结果，结论至少调整为\"linear-scale bounded, logit-scale inconclusive\"。\n→ **Action**: 正文报告 logit-scale 结果，调整 interaction bounded 的 claim 强度。\n\n**W2 [R1 Must-Fix / R2 Should-Fix] DocRED 偏相关 VIF=50.9 下不可靠。**\nDocRED BCS-centrality collinearity 达 VIF=50.9（r=0.99），标准误膨胀 ~7.1×，偏相关 point estimate 极不稳定。论文称\"BCS retains predictive value but does not uniquely identify the causal channel\"——在 VIF=50.9 下，甚至这一措辞都过强。R2 指出 FewRel BCS-controlled（VIF=1.18）是更干净的核心证据，DocRED 偏相关仅为补充。\n→ **Action**: 大幅弱化 DocRED 偏相关结论，承认 BCS 和 centrality 在 DocRED 上 inseparable。\n\n**W3 [R1-W7 + R2-W2 共识] NER null 叙述张力 + Abstract task-dependent 信号不均衡。**\n两层问题交织：(1) §5/§6 将 NER 描述为\"structural barrier\"，但 Appendix E.2 power analysis 显示 power 仅 65%——两者不能同时成立；(2) Abstract 突出 22-58% R² 但 NER null 仅一句带过，造成 framing 不平衡。R1 从 logical consistency 角度、R2 从 framing prominence 角度指出同一问题。\n→ **Action**: 统一 NER null 叙述为\"inconclusive, likely attenuated\"；Abstract 给 NER null 同等 prominence。\n\n**W4 [R1-W9 + R2-W3 共识，交叉后升至 borderline Must-Fix] 跨模型验证不对称。**\n所有 core experiments 仅在 Qwen3-32B 上完成。跨模型验证（LLaMA-70B/8B, Gemini）仅覆盖 count curves + BCS-controlled，未涵盖 error taxonomy decomposition、centrality confound analysis、SDGD。最关键的是：DocRED R²=58%（论文最强定量 claim）完全缺乏跨模型支持。R1 指出如果 LLaMA-70B 在 DocRED 上只有 R²=15%，headline claim 需重写。\n→ **Action**: 明确标注各 finding 的跨模型支持状况；Limitations 讨论 DocRED R²=58% 的单模型依赖。\n\n### Should-Fix（两位 Reviewer 共识或单方提出且对方认可）\n\n**W5 [R2-W1, R1 AGREE] SCS vs LLM-PEE novelty framing 不清晰。**\nSCS 与 LLM-PEE partitioning criterion 形式完全一致（pairwise cosine similarity of type name embeddings）。论文在 Section 2 承认但未上升为显眼的 novelty statement。读者容易得出\"SCS = LLM-PEE rebranded\"的印象。实际贡献是 controlled experimental framework，需明确点明。\n→ **Action**: Section 2 或 3.2 加 explicit novelty statement。\n\n**W6 [R1-W4, R2 AGREE] TOST margin ±3pp 的 argument (1) 循环论证。**\n三个 converging arguments 中 argument (1)（IQR-predicted Δ=2.2pp from BCS effect itself）直接引用被检验量的 effect size 确定 margin。\n→ **Action**: 删除 argument (1)，仅保留 (2)(3) 两个外部标准。\n\n**W7 [R1-W6, R2 AGREE] Batch-level R²=22-58% 缺少 ecological correlation caveat。**\nPairwise r²≈1.5% 到 batch R²≈22% 的 ~15× 放大本质是 ecological correlation。Appendix N Monte Carlo simulation 证实是 aggregation smoothing（EF≈3.35）而非 compositional effect。正文需显式 caveat + 引用 Robinson (1950)。\n→ **Action**: §4.3 加 ecological correlation caveat，将 Robinson (1950) 引用从 Appendix 移到正文。\n\n**W8 [R2-W4, R1 部分同意] Sections 5-6 过度压缩。**\nPage 8 承载 centrality confound + SDGD 全部分析 + Discussion and Conclusion，叙事密度过高。R2 建议移 §4.5 到 appendix，R1 反对（boundary condition 应留正文），建议压缩 §4.5 为 1-2 段。\n→ **Action**: 压缩 §4.5（per-embedding 细节移入 Appendix），释放空间给 §5-§6 展开 practical guidelines 和 future directions。\n\n**W9 [R1-W3, R2 REBUT 降级] Gemini count-16 BCS-controlled 依赖单个 leverage point。**\nLeave-one-out 后相关从 r=-0.80 降至 r=-0.42。R1 标 Must-Fix，R2 rebut 降为 Should-Fix——核心跨模型证据在 LLaMA-70B（decline −30.7pp vs Qwen3 −30.1pp），Gemini 仅补充验证。**此为两位 Reviewer 的主要 severity 分歧。**\n→ **Action**: 正文报告 leave-one-out sensitivity；区分\"open-weight 一致复现\"vs\"proprietary 部分支持\"。\n\n**W10 [R1-W8, R2 AGREE] DocRED count curves 仅 5 batches/level。**\nn=5 per level 偏低（vs Few-NERD 25, FewRel 25），CI 必然很宽。论文已在脚注说明高评估成本原因。\n→ **Action**: 报告完整 CIs，正文说明 batch 数限制原因。\n\n**W11 [R1-W5, R2 Partial REBUT] Bootstrap CI 非独立性讨论不足。**\nR2 指出 batch-level 分析单位的独立性基本成立（每个 batch 独立采样 type set），但 across-batch 的 shared model/prompt template 可能引入系统性偏差。\n→ **Action**: 补充讨论 across-batch correlation 对 bootstrap CI coverage 的潜在影响。\n\n### Minor\n\n**W12 [R2-W6, R1 AGREE] Responsible NLP Checklist 出现在 PDF 中（格式违规）。**\n按 EMNLP 2026/ARR 政策，Checklist 应在 OpenReview form 中填写，不在 PDF 中。Pages 9-10 包含完整 Checklist。可能在 desk rejection checklist 中被标记。\n→ **Action**: 从 PDF 移除，在 OpenReview form 中填写。\n\n**W13 [R2-W5, R1 AGREE] 正文数字/统计呈现密度过高。**\n§4.1-4.3 每段嵌入 10+ 统计值，cognitive overload。\n→ **Action**: per-dataset 详细统计值移入 appendix table，正文保留 headline numbers。\n\n**W14 [R1-W10, R2 AGREE] Multiple comparisons 不做 correction 的理由不充分。**\nFew-NERD 和 FewRel 共享 Wikidata 来源，\"independent replication\"假设可讨论。\n→ **Action**: 简要讨论 dataset independence 程度。\n\n**W15 [R1-W11, R2 AGREE] 单种子 + greedy decoding 可复现性。**\nResidual SD=0.88pp 约占 BCS effect size 的 18-44%。\n→ **Action**: 报告 seed variability 或讨论 residual 相对于 effect size 的比例。\n\n**W16 [R2-W7, R1 AGREE] 2 个 orphan bibliography entries。**\n`park-2024-grammar-aligned` 和 `zhou-2024-grasping` 未被引用。\n→ **Action**: 删除或引用。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键判断上达成一致：\n\n1. **控制变量实验框架是本文真正的贡献**，远超 SCS metric 本身的新颖性。论文需要更清晰地区分这两层。\n2. **NER batch-level BCS null 的处理需要改进**：叙述一致性（R1）+ framing prominence（R2）两个角度指向同一修改需求。\n3. **跨模型验证是核心薄弱点**：R1 关注 DocRED R²=58% 的单模型依赖，R2 关注 error taxonomy 未跨模型验证——叠加后为仅次于统计方法问题的第二大 concern。\n4. **SDGD 负面结果有独立价值**，对 decompose-then-merge 范式的失败分析（merge amplification + routing failure）值得发表。\n5. **分析深度出色**：28 页 18 附录，是 empirical NLP 论文的高水准。\n6. **整体评分 3.5 Borderline Conference**：两人独立给出相同分数。\n\n## Reviewer Divergence [REBUT]\n\n主要分歧在 **severity 而非 direction**：\n\n| 问题 | R1 判断 | R2 判断 | 分歧本质 |\n|------|---------|---------|----------|\n| Logit TOST (W1) | Must-Fix | Should-Fix | R2: accuracy 不在极端区间，linear 非完全不当 |\n| DocRED VIF (W2) | Must-Fix | Should-Fix | R2: 非核心 claim，弱化措辞即可 |\n| Gemini leverage (W9) | Must-Fix | Should-Fix | R2: 核心跨模型证据在 LLaMA-70B，Gemini 仅补充 |\n| §4.5 处理 (W8) | 留正文压缩 | 移入 appendix | R1: boundary condition 信息应留正文 |\n\n无方向性对立矛盾。所有分歧均可通过 framing 调整和措辞弱化解决，不需要重新实验。\n\n---\n\n## Questions（需要作者澄清）\n\n**Q1 [R1/R2 共同关注]** Logit-scale TOST inconclusive (p=0.209) 与 linear-scale TOST (p=0.003) 的分歧——作者选择 linear-scale 作为 primary analysis 的统计理由是什么？\n\n**Q2 [R1]** DocRED VIF=50.9 下的偏相关（Table 11）是否在 bootstrapped/permutation 框架下稳定？是否尝试过 ridge regression？\n\n**Q3 [R1]** Gemini count-16 BCS-controlled 的 leave-one-out 后，具体 Pearson r 和 p-value 数值？\n\n**Q4 [R1/R2 共同关注]** NER batch-level BCS null：作者倾向于\"structural absence\"还是\"power insufficient\"的解释？两者在论文中的不一致如何解决？\n\n**Q5 [R2]** Pair-to-batch R² 放大（1.5% → 22%）是 aggregation smoothing 还是存在 compositional interaction？Appendix N simulation 支持前者，但论文在 §6 的 practical implications 更像假设后者。\n\n**Q6 [R2]** SCS/BCS 在 homogeneous schemas（如 MAVEN/FrameNet）上不适用——这对 generalizability 有何影响？实践中如何判断一个 schema 是否适合用 BCS 做诊断？\n\n**Q7 [R2]** Label renaming 降低 SCS 后反而损害准确率（Table 29）——这是否意味着\"confusability-aware schema design\"的实践建议本质上不可行？\n\n---\n\n## Missing References\n\n1. **Robinson, W.S. (1950)** \"Ecological Correlations and the Behavior of Individuals\" — 已在 Appendix N 引用，需移到正文 §4.3 作为 batch-level R² 的 ecological correlation 警示。[R1 提出, R2 AGREE]\n2. **Ren et al. (2016)** \"AFET\" / **Choi et al. (2018)** \"Ultra-Fine Entity Typing\" — Hierarchical entity typing 工作，与 type granularity/confusability 主题相关。[R2 建议, 非 critical]\n3. **Min et al. (2022)** \"Rethinking the Role of Demonstrations in In-Context Learning\" — 可为 few-shot confusability 影响提供理论支撑。[R2 建议, 非 critical]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态：已跳过。** 外部审稿请求已发送（2026-05-21T17:47 UTC），但用户选择跳过（2026-05-21T17:51 UTC）。本轮无外部审稿结果。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成。** 3 warnings, 0 critical, 11 info。\n\n**主要发现：**\n\n1. **[Warning] 前 3 页无任何 display item。** Pages 1-3 为连续纯文本（Title/Abstract/Intro/Related Work/Experimental Setup），第一个视觉锚点（Table 1）到第 4 页才出现。审稿人在前 2 分钟仅看到密集文本墙。建议在 page 1-2 加入 motivating figure（如 Figure 1 的简化版）。\n\n2. **[Warning] 主文 8 页仅 4 个 display items（2 figures + 2 tables）。** 对于重实证的控制实验论文偏少（同类论文通常 5-8 个）。大量定量结果仅以文字陈述。建议从附录提升 1-2 个关键表格到主文。\n\n3. **[Warning] Page 8（最后一页正文）为纯文本。** Section 5 + Section 6 无任何 display item，与开头形成\"文字夹击\"。SDGD decomposition 结果适合配一个小型汇总表。\n\n**正面评价：** Figure 1/2 色盲友好（蓝/橙方案），caption 自包含，Table 排版使用 booktabs 规范。References 无 [?] 未解析引用。Limitations 篇幅适当。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5（Borderline Conference）**\n**Confidence: 4/5**\n\n### 评分理由\n\n**研究问题（+）**：重要且 understudied。首个系统隔离 count vs confusability 的控制研究，对 IE schema 设计有直接实践意义。\n\n**实验设计（+）**：控制变量框架（count curves + BCS-controlled batches）质量高，quasi-experimental manipulation 远超先前 correlational work。分析深度（28 页 18 附录）在 empirical NLP 论文中出色。\n\n**负面结果价值（+）**：SDGD 失败的机制分析、label renaming 反效果、few-shot 扩大 gap——这些 non-obvious negative findings 有独立发表价值。\n\n**统计基础裂缝（−）**：logit-scale TOST inconclusive 削弱 interaction bounded claim；DocRED VIF=50.9 使偏相关不可靠；batch-level R² 缺少 ecological correlation caveat。这些问题均可通过 framing 调整解决，但当前状态下部分核心 claim 的统计支撑不够稳固。\n\n**跨模型验证不足（−）**：DocRED R²=58%（最强定量 claim）和 error taxonomy 仅基于 Qwen3-32B。Gemini 验证有 leverage point 问题。\n\n**Novelty 定位（−）**：SCS 与 LLM-PEE 形式重叠，实验范式的 novelty 需要更清晰的 framing。\n\n**NER null 处理（−）**：structural barrier vs power insufficient 的双重叙述需要统一。\n\n### 修订路径\n\n所有高优先级问题均可通过 **framing 调整、措辞弱化和补充讨论** 解决，不需要重新实验。具体修订：\n1. 正文同时报告 linear 和 logit-scale TOST 结果\n2. 弱化 DocRED 偏相关 claim\n3. 统一 NER null 叙述，Abstract 给予同等 prominence\n4. 标注各 finding 的跨模型支持状况\n5. 加 SCS novelty statement 和 ecological correlation caveat\n6. 从 PDF 移除 Responsible NLP Checklist\n7. 压缩 §4.5，扩展 §5-§6\n\n修订后论文有望达到 **4.0（Conference）** 水平。当前状态适合 **Findings track**（3.0-3.5）。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 22-58% R² claim 需加 NER null qualifier（W3）\n- \"task-dependent effect structures\" 的表述是好的，但需要更突出\n\n### Section 1 (Introduction)\n- RQ1-RQ3 设置清晰，但 RQ1 的回答（§4.3）是 task-dependent 的——RE yes, NER inconclusive——这一 nuance 在 Introduction 的 findings 概述中不够明确\n- Contribution list 需要更突出 experimental paradigm 而非 metric\n\n### Section 2 (Related Work)\n- LLM-PEE 的区分当前是在 \"our work differs in three ways\" 中处理的，需要在 SCS novelty paragraph 中更直接地承认形式重叠并点明真正的 novelty\n\n### Section 3 (Experimental Setup)\n- SCS/BCS 定义清晰，操作化良好\n- 数据集选择合理，但 DocRED 5 batches/level 的限制需要在正文中说明（W10）\n- 单种子 + greedy decoding 的设计合理但需要在 Limitations 中更定量地讨论 residual variance\n\n### Section 4 (Results)\n- §4.1-4.3 统计值密度过高，考虑将 per-dataset 细节移入 appendix table\n- §4.3 R²=22-58% 需加 ecological correlation caveat + Robinson (1950)\n- §4.4 NER-RE asymmetry 分析是论文亮点之一\n- §4.5 centrality confound 留在正文但应压缩\n\n### Section 5 (SDGD)\n- 负面结果有价值但分析过度压缩\n- Oracle routing 恢复 72.4% 的发现很有启示性，值得更多讨论空间\n\n### Section 6 (Discussion and Conclusion)\n- 过短，practical implications 仅一段\n- 缺少 future directions（hierarchical extraction, routing-aware decomposition, task-adaptive BCS thresholds）\n- Confusability-aware schema design 的建议需要更谨慎（W7 ecological correlation + Q7 renaming 反效果）\n\n### Limitations\n- 覆盖面充分（7 个点）\n- 需补充：DocRED R²=58% 单模型依赖、跨模型验证的不对称性\n\n### Format\n- 正文 ≤ 8 页 ✓\n- ACL template with [review] option ✓\n- Anonymous ✓\n- Limitations section present ✓\n- **Checklist 在 PDF 中需移除** ✗\n- **`\\enlargethispage{3\\baselineskip}` 在 sdgd_negative.tex 中**——formatting hack，审稿人可能注意到"
  }
}
```

</details>

---


### Tool result

_source line 2617 · 2026-05-21T18:09:21.527532+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_51326259fe46fbae9da26b81cf03f1f8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4270
}
```

</details>

---


### Assistant

_source line 2618 · 2026-05-21T18:09:34.591997+00:00_

审稿报告已投递至 Research Director。

**本轮审稿总结：**

- **Overall: 3.5（Borderline Conference）**，两位 Reviewer 独立评分一致，交叉后维持不变
- **4 条高优先级问题**：logit-scale TOST inconclusive、DocRED VIF=50.9 偏相关不可靠、NER null 叙述张力 + Abstract 不均衡、跨模型验证不对称（DocRED R²=58% 单模型）
- **7 条 Should-Fix**：SCS novelty framing、TOST margin 循环论证、ecological correlation caveat、Gemini leverage point、Sections 5-6 压缩、DocRED 5 batches CIs、bootstrap CI 讨论
- **5 条 Minor**：Checklist 格式违规、数字密度、multiple comparisons、单种子可复现性、orphan bib entries
- **核心判断**：所有问题均可通过 framing 调整和措辞弱化解决，不需要重新实验。修订后有望达到 4.0 Conference 水平，当前适合 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 217

## Round 217

2 recorded events


### User

_source line 2619 · 2026-05-21T18:09:37.160136+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **6 条 AGREE**（W1/W2/W3/W5/W6/W7），**1 条 REBUT**（W4——同意压缩问题但反对将 centrality confound 移出正文）
- 与 R2 的核心共识：实验框架是真正贡献但 SCS novelty framing 需改进；NER null 处理需改善（R2 关注 prominence，我关注 logical consistency）；跨模型验证不足（两视角互补，叠加后 severity 提升）
- 主要分歧：Section 4.5 的处理方式——我认为 boundary condition 信息应留正文但可压缩

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

_source line 2620 · 2026-05-21T18:09:52.973509+00:00_

审稿报告已投递至 Research Director。

**本轮审稿汇总：**

- **Overall Score: 3.5**（Borderline Conference）
- **2 位 Reviewer 独立评分一致**，交叉分享后维持不变
- **4 条高优先级问题**：logit-scale TOST 需正文报告、DocRED VIF=50.9 偏相关需弱化、NER null 叙述需统一 + Abstract 平衡呈现、跨模型验证不对称需标注
- **7 条 Should-Fix**：SCS novelty framing、TOST margin 循环论证、ecological correlation caveat、Gemini leverage point、§5-6 压缩、DocRED CIs、bootstrap 非独立性讨论
- **5 条 Minor**：Checklist 格式违规（需移除）、数字密度、multiple comparisons、单种子、orphan bib
- **修订路径**：所有问题均可通过 framing 调整和措辞弱化解决，不需要重新实验。修订后有望达到 4.0 Conference 水平

Issue Tracker 已同步更新（`review_issues.yaml`）：R23 新增 17 条 issues（4 critical + 7 warning + 6 info）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 218

## Round 218

60 recorded events


### User

_source line 2621 · 2026-05-21T18:46:22.640442+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema-dag-extraction
- 论文路径: projects/schema-dag-extraction/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR May 2026)
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

_source line 2622 · 2026-05-21T18:46:28.169049+00:00_

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

_source line 2623 · 2026-05-21T18:46:28.221125+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 2624 · 2026-05-21T18:46:33.352790+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2625 · 2026-05-21T18:46:33.353306+00:00_



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

_source line 2626 · 2026-05-21T18:46:36.113517+00:00_

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

_source line 2627 · 2026-05-21T18:46:36.415038+00:00_

{"result":"# 项目 schema-dag-extraction 概况\n\n## 实验状态 (69 个)\n\n- **exp012_llama_8b_r2_exp2**: DONE (negative) — \n- **exp012_llama_8b_r2**: DONE (success) — \n- **exp006_interaction_2x2**: DONE (negative) — \n- **exp012_llama_awq**: DONE (killed) — \n- **exp012_llama_8b_r3**: DONE (failed) — \n- **exp012_llama_8b**: DONE (killed) — \n- **exp_fewrel_40rel_r3**: DONE (failed) — \n- **exp_fewrel_40rel_r2**: DONE (failed) — \n- **exp012_llama_fewnerd_r4**: DONE (failed) — \n- **exp012_llama_8b_fewnerd**: DONE (failed) — \n- **exp_fewrel_40rel**: DONE (failed) — \n- **exp012_llama_fewnerd_r3**: DONE (failed) — \n- **exp012_llama_fewnerd_r2**: DONE (failed) — \n- **exp012_llama_fewnerd**: DONE (failed) — \n- **exp008_sdgd_zero_fewnerd**: DONE (failed) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- prompt_sensitivity（准备中）\n- prompt_sensitivity_dry4（准备中）\n- prompt_sensitivity_dry3（准备中）\n- prompt_sensitivity_dry2（准备中）\n- prompt_sensitivity_dry（准备中）\n- exp_aggregation_monte_carlo（准备中）\n- exp_scs_name_def_ablation（准备中）\n- exp_fewrel_contamination_check（准备中）\n- exp017_gpt4o_mini_fewrel（准备中）\n- exp_cross_embedding_sensitivity（准备中）\n- …另有 2 项\n\n## 近期结论\n- **exp_llama70b_ner_bcs_null** (success): Batch-level BCS does not correlate with NER F1 for LLaMA-3.1-70B-FP8, consistent with the BCS null observed in Qwen3-32B (r=0.004) and LLaMA-8B (r=-0.12). The confusability metric is not predictive of extraction quality at the batch level. ← 基于 exp012_llama_8b_r2_exp2\n  [LLaMA-70B NER BCS-null analysis](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_llama70b_ner_bcs_null/data/bcs_null_analysis.json)\n- **exp_gemini_flash_bcs_controlled** (success): BCS-accuracy negative correlation observed on open-weight models (Qwen3-32B, LLaMA) generalizes to proprietary API models. Gemini 2.5 Flash should show significant BCS gap on extreme-BCS batches at count 8 and count 16, confirming Dimension 2 is architecture-family-in
…[truncated 1221 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2628 · 2026-05-21T18:46:36.415408+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "report.md"
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
    "file": "report.md"
  }
}
```

</details>

---


### Tool result

_source line 2629 · 2026-05-21T18:46:36.616433+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/report.md\", \"content\": \"# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- prompt_sensitivity（准备中）\\n- prompt_sensitivity_dry4（准备中）\\n- prompt_sensitivity_dry3（准备中）\\n- prompt_sensitivity_dry2（准备中）\\n- prompt_sensitivity_dry（准备中）\\n- exp_aggregation_monte_carlo（准备中）\\n- exp_scs_name_def_ablation（准备中）\\n- exp_fewrel_contamination_check（准备中）\\n- exp017_gpt4o_mini_fewrel（准备中）\\n- exp_cross_embedding_sensitivity（准备中）\\n- …另有 2 项\\n\\n## 近期结论\\n- **exp_llama70b_ner_bcs_null** (success): Batch-level BCS does not correlate with NER F1 for LLaMA-3.1-70B-FP8, consistent with the BCS null observed in Qwen3-32B (r=0.004) and LLaMA-8B (r=-0.12). The confusability metric is not predictive of extraction quality at the batch level. ← 基于 exp012_llama_8b_r2_exp2\\n  [LLaMA-70B NER BCS-null analysis](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_llama70b_ner_bcs_null/data/bcs_null_analysis.json)\\n- **exp_gemini_flash_bcs_controlled** (success): BCS-accuracy negative correlation observed on open-weight models (Qwen3-32B, LLaMA) generalizes to proprietary API models. Gemini 2.5 Flash should show significant BCS gap on extreme-BCS batches at count 8 and count 16, confirming Dimension 2 is architecture-family-independent. ← 基于 exp_gemini_flash_cross_model\\n- **exp_gemini_flash_cross_model** (success): The two-dimensional degradation pattern (count-related decline + confusability-related type confusion) generalizes beyond open-weight models to proprietary API models. Gemini 2.5 Flash should show: (1) monotonic RE accuracy decline with count, and (2) significant BCS-accuracy correlation on extreme batches. If confirmed, the pattern is architecture-family-independent (open-weight Qwen/LLaMA + proprietary Gemini).\\n\\n## 趋势\\n成功 34 / 负向 9 / 失败 10 / 共 57\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.
…[truncated 750 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 2630 · 2026-05-21T18:46:43.292473+00:00_

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

_source line 2631 · 2026-05-21T18:46:43.794958+00:00_

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
40	\item \textbf{Model coverage.} Primary experiments use a single model (Qwen3-32B); cross-model validation covers Dimensions~1--2 (count curves, BCS-controlled extremes) but does not replicate secondary analyses (error taxonomy, prompt sensitivity, TOST equivalence). In particular, DocRED $R^2 = 0.58$ and the error taxonomy decomposition are single-model results; whether these generalize remains open. See Appendix~\ref{sec:appendix_cross_model_gemini} and Table~\ref{tab:cross_model_bcs} for detailed model-wise results.
41	
42	\item \textbf{Effect size and statistical design.} Pairwise SCS explains a small fraction of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\times$ BCS interaction is bounded on FewRel but nonzero on DocRED, partially confounded by BCS range restriction at higher counts (Appendix~\ref{sec:appendix_factorial}); logit-scale evidence remains inconclusive. DocRED count curves use 5 batches per level due to higher per-batch evaluation cost. BCS-controlled experiments use a single seed with greedy decoding; residual variance is small (Appendix~\ref{app:variance-decomposition}) but precise magnitud
…[truncated 5069 chars]

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

_source line 2632 · 2026-05-21T18:46:43.795439+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
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

_source line 2633 · 2026-05-21T18:46:43.795749+00:00_



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

_source line 2634 · 2026-05-21T18:46:43.996678+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
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

_source line 2635 · 2026-05-21T18:46:44.047435+00:00_



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

_source line 2636 · 2026-05-21T18:46:49.217058+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines page limit"
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
    "query": "EMNLP 2026 call for papers ARR submission guidelines page limit"
  }
}
```

</details>

---


### Tool call

_source line 2637 · 2026-05-21T18:46:49.669214+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 author guidelines submission format requirements"
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
    "query": "ACL Rolling Review 2026 author guidelines submission format requirements"
  }
}
```

</details>

---


### Tool call

_source line 2638 · 2026-05-21T18:46:50.071085+00:00_

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
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
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

_source line 2639 · 2026-05-21T18:46:50.121674+00:00_



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


### Tool result

_source line 2640 · 2026-05-21T18:46:54.538981+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"}]

Based on the search results, here's information about EMNLP 2026's call for papers, ARR submission guidelines, and page limits:

## Page Limits

EMNLP 2026 uses a two-column format with an 8-page limit for long papers and a 4-page limit for short papers. A mandatory Limitations section is required, placed after the conclusion.

## ARR Submission Guidelines

Authors submitting to the ARR 2026 May cycle aligned with EMNLP must explicitly declare which conference they intend to commit to at submission time, and this choice is binding for EMNLP 2026—submissions that do not sele
…[truncated 502 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 5321
}
```

</details>

---


### Tool result

_source line 2641 · 2026-05-21T18:46:57.299759+00:00_

Web search results for query: "ACL Rolling Review 2026 author guidelines submission format requirements"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Here are the key submission format requirements and author guidelines for ACL Rolling Review 2026:

## Submission Format Requirements

Paper submissions must use the official ACL style template, and submissions based on the Word template will be desk-rejected starting from March 2026. There is an official Overleaf template with a [review] setting that must be on for the submission.

## Anonymity Require
…[truncated 1112 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "WebSearch",
  "elapsed_ms": 7630
}
```

</details>

---


### Tool call

_source line 2642 · 2026-05-21T18:47:02.482491+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "schema-dag-extraction",
  "file": "config.yaml",
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
    "file": "config.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 2643 · 2026-05-21T18:47:02.633661+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'config.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2644 · 2026-05-21T18:47:02.634125+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TodoWrite",
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
    "query": "select:TodoWrite",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2645 · 2026-05-21T18:47:02.634355+00:00_



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

_source line 2646 · 2026-05-21T18:47:11.471335+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'in_progress', 'activeForm': '检查论文资料完整性和 Venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 人数和侧重'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
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
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'in_progress', 'activeForm': '检查论文资料完整性和 Venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 人数和侧重'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'pending', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2647 · 2026-05-21T18:47:11.471798+00:00_

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

_source line 2648 · 2026-05-21T18:47:12.798859+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/schema-dag-extraction/**/config.yaml",
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
    "pattern": "**/schema-dag-extraction/**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
  }
}
```

</details>

---


### Tool result

_source line 2649 · 2026-05-21T18:47:13.100346+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2650 · 2026-05-21T18:47:13.100818+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/schema-dag-extraction/artifacts/review_issues.yaml",
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
    "pattern": "**/schema-dag-extraction/artifacts/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
  }
}
```

</details>

---


### Tool result

_source line 2651 · 2026-05-21T18:47:13.201785+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2652 · 2026-05-21T18:47:16.967215+00:00_

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

_source line 2653 · 2026-05-21T18:47:17.118422+00:00_

1	
2	# Review Issues Tracker
3	# Updated: 2026-05-21 (Round 23 — Action Matrix dispatched to Agent)
4	
5	# ============================================================
6	# R23 HIGH-PRIORITY (Consensus from R1+R2)
7	# ============================================================
8	
9	- id: R23-C1
10	  summary: "Logit-scale TOST inconclusive 但论文以 linear-scale 为主要结论"
11	  category: method
12	  severity: critical
13	  status: in_progress
14	  first_raised_round: 23
15	  last_seen_round: 23
16	  mentions:
17	    - {round: 23, reviewers: [R1, R2], note: "R1 Must-Fix W1, R2 AGREE 但降为 Should-Fix。Logit-scale p=0.209 inconclusive, linear-scale p=0.003。"}
18	  action_items:
19	    - {round: 23, action: "正文提升 logit-scale 结果到正文级别，结论改为 linear bounded + logit inconclusive，引用 regression logit p=0.050", assigned_to: "Agent", status: in_progress}
20	  resolution: ""
21	  resolution_round: null
22	
23	- id: R23-C2
24	  summary: "DocRED 偏相关 VIF=50.9 下不可靠，BCS-centrality inseparable"
25	  category: method
26	  severity: critical
27	  status: in_progress
28	  first_raised_round: 23
29	  last_seen_round: 23
30	  mentions:
31	    - {round: 23, reviewers: [R1, R2], note: "R1 Must-Fix W2, R2 AGREE 但降为 Should-Fix。VIF=50.9 标准误膨胀 ~7.1x。"}
32	  action_items:
33	    - {round: 23, action: "重写 DocRED 偏相关段：reported for completeness, clean evidence from FewRel (VIF=1.18)", assigned_to: "Agent", status: in_progress}
34	  resolution: ""
35	  resolution_round: null
36	
37	- id: R23-C3
38	  summary: "NER null 叙述张力 + Abstract 中 task-dependent 信号呈现不均衡"
39	  category: framing
40	  severity: critical
41	  status: in_progress
42	  first_raised_round: 23
43	  last_seen_round: 23
44	  mentions:
45	    - {round: 23, reviewers: [R1, R2], note: "R1-W7 + R2-W2 互补共识。§5/§6 的 structural barrier 与 power analysis 65% 矛盾。"}
46	  action_items:
47	    - {round: 23, action: "双层解释：primary=error-mode 结构(miss/boundary/type 分散), secondary=BCS range restriction。保留机制解释不丢弃", assigned_to: "Agent", status: in_progress}
48	    - {round
…[truncated 11969 chars]

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

_source line 2654 · 2026-05-21T18:47:17.169062+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/schema-dag-extraction/agent/config.yaml",
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
    "pattern": "**/schema-dag-extraction/agent/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
  }
}
```

</details>

---


### Tool result

_source line 2655 · 2026-05-21T18:47:17.169389+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2656 · 2026-05-21T18:47:33.840662+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if paper PDF exists"
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
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if paper PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 2657 · 2026-05-21T18:47:34.394555+00:00_

-rw-r--r-- 1 ubuntu ubuntu 469104 May 21 18:42 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "Bash",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 2658 · 2026-05-21T18:47:34.846628+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/schema-dag-extraction/**/project.yaml",
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
    "pattern": "**/schema-dag-extraction/**/project.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18"
  }
}
```

</details>

---


### Tool result

_source line 2659 · 2026-05-21T18:47:35.048439+00:00_

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

_source line 2660 · 2026-05-21T18:47:35.099032+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "description": "Count lines in main.tex"
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
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "description": "Count lines in main.tex"
  }
}
```

</details>

---


### Tool result

_source line 2661 · 2026-05-21T18:47:35.149681+00:00_

887 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex

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

_source line 2662 · 2026-05-21T18:47:38.914322+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/schema-dag-extraction/**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent"
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
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent"
  }
}
```

</details>

---


### Tool result

_source line 2663 · 2026-05-21T18:47:39.466806+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/sessions/review_director_338aa0a5.&lt;/tool_use_error>

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

_source line 2664 · 2026-05-21T18:47:39.617820+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
  "pages": "1-9"
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
    "pages": "1-9"
  }
}
```

</details>

---


### Tool result

_source line 2665 · 2026-05-21T18:47:40.221550+00:00_

PDF pages extracted: 9 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf (458.1KB)

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

_source line 2666 · 2026-05-21T18:48:23.644736+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf 2>/dev/null || echo \"pdfinfo not available\"",
  "description": "Get PDF page count and metadata"
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
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || pdfinfo /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf 2>/dev/null || echo \"pdfinfo not available\"",
    "description": "Get PDF page count and metadata"
  }
}
```

</details>

---


### Tool result

_source line 2667 · 2026-05-21T18:48:23.796123+00:00_

Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Thu May 21 18:42:24 2026 UTC
ModDate:         Thu May 21 18:42:24 2026 UTC
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
File size:       469104 bytes
Optimized:       no
PDF version:     1.7

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

_source line 2668 · 2026-05-21T18:48:46.389209+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性和 Venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 人数和侧重'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'in_progress', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
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
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性和 Venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 人数和侧重'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'in_progress', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'pending', 'activeForm': '分配 Reviewer 独立审稿'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2669 · 2026-05-21T18:48:46.389792+00:00_

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

_source line 2670 · 2026-05-21T18:49:01.154744+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "schema-dag-extraction",
  "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "schema-dag-extraction",
    "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
  }
}
```

</details>

---


### Tool call

_source line 2671 · 2026-05-21T18:49:03.115363+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "schema-dag-extraction",
  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
  "venue": "EMNLP 2026",
  "note": "ARR May 2026 cycle, deadline May 25. Long paper (8-page main text). Double-blind."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "schema-dag-extraction",
    "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf",
    "venue": "EMNLP 2026",
    "note": "ARR May 2026 cycle, deadline May 25. Long paper (8-page main text). Double-blind."
  }
}
```

</details>

---


### Tool result

_source line 2672 · 2026-05-21T18:49:27.542476+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 26387
}
```

</details>

---


### Tool result

_source line 2673 · 2026-05-21T18:49:27.542812+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 24427
}
```

</details>

---


### Tool call

_source line 2674 · 2026-05-21T18:49:27.693655+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "## Round 1 审稿任务 — Reviewer 1: 方法严谨性\n\n### Venue 信息\n- **目标**: EMNLP 2026 (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL template with [review], double-blind, 8 页正文限制（unlimited references）\n- **Limitations**: 必须有，不计入页数限制\n- **Checklist**: 在 OpenReview form 填写，不放 PDF\n- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n### 论文路径\n- TeX: `projects/schema-dag-extraction/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf`\n- 共 26 页（8 页正文 + Limitations + References + ~14 页 Appendix）\n\n### 论文概要\nTitle: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n研究 schema 复杂度（type count + inter-type confusability）如何预测 training-free LLM IE 的性能退化。提出 SCS（Schema Confusability Score）和 BCS（Batch Confusability Score），在 4 个数据集（Few-NERD/FewRel/DocRED/MAVEN）上进行 count curves + BCS-controlled 实验。主要发现：BCS 解释 22-58% 的跨 batch RE 准确率方差；NER batch-level BCS 信号为 null；schema 分解（SDGD）因 merge amplification 失败。跨模型验证覆盖 4 个模型家族（Qwen3-32B, LLaMA-8B, LLaMA-70B, Gemini 2.5 Flash）。\n\n### 你的审查侧重\n\n**方法严谨性**——重点审查以下方面：\n\n1. **统计分析有效性**：\n   - SCS/BCS 指标定义的合理性和局限性\n   - Pairwise r² ≈ 1.3-1.7% 到 batch-level R² = 22-58% 的放大机制是否有充分的 ecological correlation caveat\n   - TOST 等价检验（linear-scale p=0.003 vs logit-scale p=0.209）的处理是否充分、结论是否过强\n   - 偏相关分析中 DocRED VIF=50.9 的处理是否妥当\n   - Bootstrap CI 在 across-batch correlation 下的有效性\n\n2. **实验设计**：\n   - Count curves 实验：FewRel 25 batches/level vs DocRED 5 batches/level 的统计效力差异\n   - BCS-controlled extreme batch 构建方法的 validity（greedy search on SCS matrix）\n   - 单种子 + greedy decoding 的可复现性（residual SD = 0.88pp）\n   - Gemini count-16 BCS-controlled 是否依赖单个 leverage point（leave-one-out sensitivity）\n\n3. **跨模型验证的完整性**：\n   - 哪些 claims 有跨模型支持，哪些仍是单模型（Qwen3-32B）结果\n   - DocRED R² = 58% 是否只在 Qwen3-32B 上验证\n   - Error taxonomy 跨模型验证的覆盖范围\n\n4. **因果推断强度**：\n   - 论文声称 \"controlled study isolating confusability from count\"——实际控制水平如何\n   - BCS-controlled 实验是否充分排除了混杂变量（type frequency, centrality）\n   - 2×2 factorial interaction 的 effect size 和 statistical power\n\n5. **格式合规**：\n   - 正文是否在 8 页以内\n   - Limitations section 是否仅包含 limitations（不含新实验、新图表）\n\n请输出结构化审稿报告：Summary → Strengths → Weaknesses (按 Must-Fix / Should-Fix / Minor 分级) → Questions → Missing References → Overall Assessment（含评分和置信度）。\n\n**要求严格客观，像顶会最严格的审稿人一样评估。**"
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
    "text": "## Round 1 审稿任务 — Reviewer 1: 方法严谨性\n\n### Venue 信息\n- **目标**: EMNLP 2026 (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL template with [review], double-blind, 8 页正文限制（unlimited references）\n- **Limitations**: 必须有，不计入页数限制\n- **Checklist**: 在 OpenReview form 填写，不放 PDF\n- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n### 论文路径\n- TeX: `projects/schema-dag-extraction/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf`\n- 共 26 页（8 页正文 + Limitations + References + ~14 页 Appendix）\n\n### 论文概要\nTitle: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n研究 schema 复杂度（type count + inter-type confusability）如何预测 training-free LLM IE 的性能退化。提出 SCS（Schema Confusability Score）和 BCS（Batch Confusability Score），在 4 个数据集（Few-NERD/FewRel/DocRED/MAVEN）上进行 count curves + BCS-controlled 实验。主要发现：BCS 解释 22-58% 的跨 batch RE 准确率方差；NER batch-level BCS 信号为 null；schema 分解（SDGD）因 merge amplification 失败。跨模型验证覆盖 4 个模型家族（Qwen3-32B, LLaMA-8B, LLaMA-70B, Gemini 2.5 Flash）。\n\n### 你的审查侧重\n\n**方法严谨性**——重点审查以下方面：\n\n1. **统计分析有效性**：\n   - SCS/BCS 指标定义的合理性和局限性\n   - Pairwise r² ≈ 1.3-1.7% 到 batch-level R² = 22-58% 的放大机制是否有充分的 ecological correlation caveat\n   - TOST 等价检验（linear-scale p=0.003 vs logit-scale p=0.209）的处理是否充分、结论是否过强\n   - 偏相关分析中 DocRED VIF=50.9 的处理是否妥当\n   - Bootstrap CI 在 across-batch correlation 下的有效性\n\n2. **实验设计**：\n   - Count curves 实验：FewRel 25 batches/level vs DocRED 5 batches/level 的统计效力差异\n   - BCS-controlled extreme batch 构建方法的 validity（greedy search on SCS matrix）\n   - 单种子 + greedy decoding 的可复现性（residual SD = 0.88pp）\n   - Gemini count-16 BCS-controlled 是否依赖单个 leverage point（leave-one-out sensitivity）\n\n3. **跨模型验证的完整性**：\n   - 哪些 claims 有跨模型支持，哪些仍是单模型（Qwen3-32B）结果\n   - DocRED R² = 58% 是否只在 Qwen3-32B 上验证\n   - Error taxonomy 跨模型验证的覆盖范围\n\n4. **因果推断强度**：\n   - 论文声称 \"controlled study isolating confusability from count\"——实际控制水平如何\n   - BCS-controlled 实验是否充分排除了混杂变量（type frequency, centrality）\n   - 2×2 factorial interaction 的 effect size 和 statistical power\n\n5. **格式合规**：\n   - 正文是否在 8 页以内\n   - Limitations section 是否仅包含 limitations（不含新实验、新图表）\n\n请输出结构化审稿报告：Summary → Strengths → Weaknesses (按 Must-Fix / Should-Fix / Minor 分级) → Questions → Missing References → Overall Assessment（含评分和置信度）。\n\n**要求严格客观，像顶会最严格的审稿人一样评估。**"
  }
}
```

</details>

---


### Tool result

_source line 2675 · 2026-05-21T18:49:47.060207+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19366
}
```

</details>

---


### Tool call

_source line 2676 · 2026-05-21T18:49:47.261264+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "## Round 1 审稿任务 — Reviewer 2: 新颖性与完整性\n\n### Venue 信息\n- **目标**: EMNLP 2026 (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL template with [review], double-blind, 8 页正文限制（unlimited references）\n- **Limitations**: 必须有，不计入页数限制\n- **Checklist**: 在 OpenReview form 填写，不放 PDF\n- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n### 论文路径\n- TeX: `projects/schema-dag-extraction/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf`\n- 共 26 页（8 页正文 + Limitations + References + ~14 页 Appendix）\n\n### 论文概要\nTitle: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n研究 schema 复杂度（type count + inter-type confusability）如何预测 training-free LLM IE 的性能退化。提出 SCS（Schema Confusability Score）和 BCS（Batch Confusability Score），在 4 个数据集（Few-NERD/FewRel/DocRED/MAVEN）上进行 count curves + BCS-controlled 实验。主要发现：BCS 解释 22-58% 的跨 batch RE 准确率方差；NER batch-level BCS 信号为 null；schema 分解（SDGD）因 merge amplification 失败。跨模型验证覆盖 4 个模型家族。\n\n### 你的审查侧重\n\n**新颖性与完整性**——重点审查以下方面：\n\n1. **贡献定位与 Novelty**：\n   - SCS 继承自 LLM-PEE 的 embedding-similarity criterion——本文的独立贡献是什么？实验方法论 vs 指标本身的创新如何定位？\n   - \"first controlled study isolating confusability from count\" 这一 claim 是否成立？\n   - 与 LLM-PEE (Liu et al., 2025) 的差异化是否足够清晰？\n   - 三个 contributions 的实际新颖程度评估\n\n2. **相关工作覆盖**：\n   - Training-free LLM IE 领域的重要文献是否遗漏\n   - Schema complexity in IE 的相关工作是否充分\n   - Type confusion / label confusion 在 fine-grained classification 领域的经典文献是否覆盖\n   - 是否有遗漏的重要 missing references\n\n3. **NER Null 叙述逻辑**：\n   - BCS 在 RE 上有效但在 NER 上为 null——这个 task asymmetry 的解释是否令人信服\n   - \"structural barrier\"（error modes 分散 across miss/boundary/type）vs power analysis（65% power）的叙述是否存在张力\n   - Abstract 和 Introduction 中对 NER null 的呈现是否均衡、是否存在 cherry-picking 嫌疑\n\n4. **写作质量**：\n   - 论文的整体叙述流畅度和逻辑链\n   - 数字/统计密度是否影响可读性\n   - Sections 5-6（Schema Decomposition + Discussion）的信息密度和展开程度\n   - Abstract 的信息量是否过载\n\n5. **格式合规性**：\n   - ACL template 使用是否正确（[review] option）\n   - 正文页数是否 ≤ 8 页\n   - Limitations section 内容是否合规（仅 limitations，不含新实验/图表/分析）\n   - 匿名化是否彻底（检查 footnotes, acknowledgments, repository links）\n   - References 格式一致性\n   - Appendix 引用方式是否规范\n\n6. **论文完整性**：\n   - 实验覆盖是否支撑所有 claims\n   - 是否有未回答的关键问题\n   - 负面结果（NER null, SDGD failure）的呈现是否诚实且充分\n\n请输出结构化审稿报告：Summary → Strengths → Weaknesses (按 Must-Fix / Should-Fix / Minor 分级) → Questions → Missing References → Overall Assessment（含评分和置信度）。\n\n**要求严格客观，像顶会最严格的审稿人一样评估。**"
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
    "text": "## Round 1 审稿任务 — Reviewer 2: 新颖性与完整性\n\n### Venue 信息\n- **目标**: EMNLP 2026 (ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL template with [review], double-blind, 8 页正文限制（unlimited references）\n- **Limitations**: 必须有，不计入页数限制\n- **Checklist**: 在 OpenReview form 填写，不放 PDF\n- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit\n\n### 论文路径\n- TeX: `projects/schema-dag-extraction/docs/paper/main.tex`\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf`\n- 共 26 页（8 页正文 + Limitations + References + ~14 页 Appendix）\n\n### 论文概要\nTitle: \"How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\"\n研究 schema 复杂度（type count + inter-type confusability）如何预测 training-free LLM IE 的性能退化。提出 SCS（Schema Confusability Score）和 BCS（Batch Confusability Score），在 4 个数据集（Few-NERD/FewRel/DocRED/MAVEN）上进行 count curves + BCS-controlled 实验。主要发现：BCS 解释 22-58% 的跨 batch RE 准确率方差；NER batch-level BCS 信号为 null；schema 分解（SDGD）因 merge amplification 失败。跨模型验证覆盖 4 个模型家族。\n\n### 你的审查侧重\n\n**新颖性与完整性**——重点审查以下方面：\n\n1. **贡献定位与 Novelty**：\n   - SCS 继承自 LLM-PEE 的 embedding-similarity criterion——本文的独立贡献是什么？实验方法论 vs 指标本身的创新如何定位？\n   - \"first controlled study isolating confusability from count\" 这一 claim 是否成立？\n   - 与 LLM-PEE (Liu et al., 2025) 的差异化是否足够清晰？\n   - 三个 contributions 的实际新颖程度评估\n\n2. **相关工作覆盖**：\n   - Training-free LLM IE 领域的重要文献是否遗漏\n   - Schema complexity in IE 的相关工作是否充分\n   - Type confusion / label confusion 在 fine-grained classification 领域的经典文献是否覆盖\n   - 是否有遗漏的重要 missing references\n\n3. **NER Null 叙述逻辑**：\n   - BCS 在 RE 上有效但在 NER 上为 null——这个 task asymmetry 的解释是否令人信服\n   - \"structural barrier\"（error modes 分散 across miss/boundary/type）vs power analysis（65% power）的叙述是否存在张力\n   - Abstract 和 Introduction 中对 NER null 的呈现是否均衡、是否存在 cherry-picking 嫌疑\n\n4. **写作质量**：\n   - 论文的整体叙述流畅度和逻辑链\n   - 数字/统计密度是否影响可读性\n   - Sections 5-6（Schema Decomposition + Discussion）的信息密度和展开程度\n   - Abstract 的信息量是否过载\n\n5. **格式合规性**：\n   - ACL template 使用是否正确（[review] option）\n   - 正文页数是否 ≤ 8 页\n   - Limitations section 内容是否合规（仅 limitations，不含新实验/图表/分析）\n   - 匿名化是否彻底（检查 footnotes, acknowledgments, repository links）\n   - References 格式一致性\n   - Appendix 引用方式是否规范\n\n6. **论文完整性**：\n   - 实验覆盖是否支撑所有 claims\n   - 是否有未回答的关键问题\n   - 负面结果（NER null, SDGD failure）的呈现是否诚实且充分\n\n请输出结构化审稿报告：Summary → Strengths → Weaknesses (按 Must-Fix / Should-Fix / Minor 分级) → Questions → Missing References → Overall Assessment（含评分和置信度）。\n\n**要求严格客观，像顶会最严格的审稿人一样评估。**"
  }
}
```

</details>

---


### Tool result

_source line 2677 · 2026-05-21T18:49:48.676736+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1415
}
```

</details>

---


### Tool call

_source line 2678 · 2026-05-21T18:49:57.527346+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性和 Venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 人数和侧重'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 和 Reviewer 2 独立审稿结果'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
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
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性和 Venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 人数和侧重'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 和 Reviewer 2 独立审稿结果'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2679 · 2026-05-21T18:49:57.527890+00:00_

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

_source line 2680 · 2026-05-21T18:50:02.948560+00:00_

全部派发完成：

| 任务 | 状态 |
|------|------|
| 视觉审查 Agent | ✅ 已启动（fire-and-forget） |
| 外部审稿（Stanford Agentic Reviewer） | ✅ 请求已发送，8h 后自动提醒 |
| Reviewer 1（方法严谨性） | ✅ 已分配 |
| Reviewer 2（新颖性与完整性） | ✅ 已分配 |

等待两位 Reviewer 的独立审稿结果返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 219

## Round 219

2 recorded events


### User

_source line 2681 · 2026-05-21T18:57:46.373179+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿报告完成

### 总体评分
**Overall: 3.0 (Findings)**
**Confidence: 4/5**

### 维度打分
| 维度 | 分数 |
|------|------|
| Soundness | 3.5/5 |
| Excitement | 2.5/5 |
| Reproducibility | 4/5 |

### Must-Fix (2 items)
**N1** SCS/BCS 指标新颖性不足，贡献定位模糊 — SCS 本质是标准 embedding cosine similarity，继承自 LLM-PEE。论文真正的贡献在于实验方法论（BCS-controlled batch design），但 Abstract 和 Contributions 的措辞将 SCS 包装为独立贡献。需明确区分 methodology contribution vs. metric contribution。

**N2** NER null 叙述内部张力 — 论文同时给出 "structural barrier"（NER 错误分散于 miss/boundary/type，BCS 根本无法预测）和 "insufficient power"（65% power，absence of evidence）两种不兼容解释。Abstract "confirmed on three models" 的措辞暗示确定性结论，但 Appendix E.2 承认统计功效不足。需在正文中明确承认张力并统一叙述。

### Should-Fix (5 items)
- W1: Abstract 信息过载（数字过多）
- W2: Section 5-6 过于压缩（Schema Decomposition 是三大贡献之一却只有半 column）
- W3: 生态谬误影响讨论不足（batch-level R² 对 individual type-pair prediction 的实用性有限）
- W4: 跨模型验证深度不均（DocRED R²=0.58 仅 single-model）
- W5: MAVEN centrality confound 使 BCS 预测力实际仅在 RE 两个数据集上验证

### 主要优势
1. BCS-controlled batch 实验设计巧妙，统计分析严谨（TOST, bootstrap CIs, power analysis）
2. 诚实报告负面结果（NER null, SDGD failure, MAVEN confound）
3. 14 页 Appendix 含大量 robustness checks
4. 跨 4 个模型家族验证方向一致性
5. 研究问题具有直接实际应用价值

### 引用检查
- 72 bib entries, 70 cited, 2 orphan (schall-2025-hidden-cost, tam-2024-let-me-speak)
- 0 missing citations
- 59/72 online verified, 4 not found in OpenAlex (likely recent preprints), 9 minor mismatches (mostly LaTeX encoding)
- 无虚假引用

### 格式合规
- ✅ ACL template [review] option
- ✅ 正文 8 页（Sections 1-6）
- ✅ Limitations 合规（仅 limitations，无新实验/图表）
- ✅ 匿名化完整（\author{Anonymous}，无 repo links/acknowledgments）
- ✅ Checklist 注释说明在 OpenReview form 中填写

完整审稿报告已在对话中输出。

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

_source line 2682 · 2026-05-21T18:57:54.659596+00:00_

Reviewer 2 审稿意见已收到。评分 3.0 (Findings)，2 个 Must-Fix + 5 个 Should-Fix。等待 Reviewer 1 完成后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 220

## Round 220

2 recorded events


### User

_source line 2683 · 2026-05-21T18:58:01.831410+00:00_

[Reviewer 2 审稿结果]:
审稿报告已完成并提交给 Review Director。

核心判断：**Overall 3.0 (Findings)**。两个 Must-Fix：(1) SCS/BCS 贡献定位需与 LLM-PEE 明确区分，重新框架为实验方法论贡献而非指标贡献；(2) NER null 的 "structural barrier" 与 "insufficient power" 两种解释存在逻辑张力，需统一叙述。五个 Should-Fix 涉及 Abstract 过载、Section 5-6 压缩、ecological fallacy 讨论不足、跨模型验证深度不均、MAVEN confound 限制泛化性。格式合规，引用无虚假，匿名化完整。

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

_source line 2684 · 2026-05-21T18:58:14.615159+00:00_

Reviewer 2 审稿已收到。核心判断 3.0 (Findings)，2 个 Must-Fix + 5 个 Should-Fix。

等待 Reviewer 1 完成独立审稿后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 221

## Round 221

8 recorded events


### User

_source line 2685 · 2026-05-21T18:58:51.110366+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 — 方法严谨性审查报告

### Paper Summary

本文研究 schema 复杂度如何预测 training-free LLM 信息抽取的性能退化。作者提出两个指标：Schema Confusability Score (SCS，类型名嵌入的余弦相似度) 和 Batch Confusability Score (BCS，batch 内 SCS 均值)，在 4 个数据集 (Few-NERD/FewRel/DocRED/MAVEN) 上通过 count curves 和 BCS-controlled 实验验证。主要发现：(1) BCS 解释 22–58% 的跨 batch RE 准确率方差；(2) NER batch-level BCS 信号为 null；(3) schema 分解 (SDGD) 因 merge amplification 失败。跨模型验证覆盖 Qwen3-32B、LLaMA-8B、LLaMA-70B 和 Gemini 2.5 Flash。

---

## 总体评分

**Overall**: 3.5 / 5 — Borderline Conference
**Confidence**: 4 / 5
**一句话总结**: 研究问题重要且实验设计精细，FewRel 上的 BCS 预测效应 (R²=22%) 可信，但 DocRED R²=58% 受 centrality 严重混淆 (VIF=50.9)，跨模型验证的 Gemini 结果依赖单一 leverage point，多项核心分析仅限 Qwen3-32B，削弱了论文声称的普适性。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5 / 5 | FewRel 方法学扎实 (VIF=1.16, N=25/level)，但 DocRED 核心结论受 centrality confound 和小样本影响；TOST 量表敏感性未妥善解决；ecological correlation caveat 不够突出 |
| **Excitement** | 3.5 / 5 | 首个隔离 confusability vs. count 的控制研究，BCS 作为诊断工具有实用价值，负面结果 (NER null, SDGD 失败) 诚实且有启发性，但 pair-level 效应量极小 (r²≈1–5%)，batch-level 的高 R² 是 ecological aggregation 的数学必然 |
| **Reproducibility** | 4 / 5 | 单种子 + greedy decoding 便于复现，prompt 模板完整附于 Appendix G，承诺开源代码和数据，但 FP8 quantization 引入 non-determinism (residual SD=0.88pp) |

---

## 主要优势

1. **研究问题的新颖性与重要性**：首个在 training-free LLM IE 中系统隔离 type confusability 与 type count 效应的控制研究，填补了现有工作仅讨论 schema 规模但忽略 inter-type confusability 的空白（Section 1, RQ1–RQ3）。

2. **实验设计的精细程度**：Count curves + BCS-controlled extreme batches 的双重设计互相补充——前者建立 baseline degradation trend，后者在固定 count 下隔离 confusability 效应（Section 3.3）。FewRel 的 balanced design (700 instances/type) 有效控制了 type frequency 混淆。

3. **统计方法学的透明度**：罕见地报告了 VIF (Table 11)、ecological correlation caveat (Section 4.2 cite Robinson 1950)、TOST 等价检验的量表敏感性 (Appendix C)、功效分析 (Appendix E.2)。这种自我批判的风格在 NLP 论文中少见且值得肯定。

4. **诚实的负面结果**：NER batch-level BCS 为 null (Table 5, 3 个模型确认)、SDGD decomposition 因 merge amplification 失败 (Section 5, Table 7)——这些负面结果本身就是重要贡献，防止社区在无效方向上投入资源。

5. **Appendix 的深度**：14 页附录覆盖 factorial analysis (C)、centrality confound control (E)、power analysis (E.2)、batch aggregation simulation (N)、split-origin analysis (O)、prompt sensitivity (H)、variance decomposition (R) 等，展现了严谨的 robustness checking。

6. **跨模型验证的方向性一致**：Count-related decline 在 4 个模型家族上均呈单调下降 (Table 22, 23)，BCS 效应方向在 FewRel 上跨 5 个模型一致 (Table 24)。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] DocRED R²=58% 受 centrality 严重混淆，不应作为核心 claim

- **具体位置**：Abstract ("22–58%"), Section 4.3 ("DocRED R²=0.614"), Table 11 (Appendix E.1)
- **问题**：Table 11 显示 DocRED 上 BCS 与 degree centrality 的 VIF=50.9，两变量相关系数 r=0.99。在如此极端的共线性下，偏相关分析虽然 BCS partial correlation 显著 (p<0.001)，但这仅说明 BCS 包含 predictive information——**无法归因于 confusability 而非 centrality**。作者自己也承认 "the near-perfect BCS-centrality correlation makes it impossible to fully separate the two predictors"（Appendix E.1），但 Abstract 和 Section 4.3 仍然突出报道 "22–58%"，读者自然将上界 58% 视为 confusability 的解释力，这是误导性的。
- **为什么影响接收**：这是论文最引人注目的定量声明。如果 58% 的方差实际上主要由 centrality（高频/核心类型本身更难区分）驱动，那么 confusability metric 的价值将大打折扣。FewRel R²=22% (VIF=1.16) 是唯一可靠的效应量估计，但 22% 远不如 58% 抢眼。
- **建议修改方向**：(a) Abstract 和正文中将 DocRED R² 标注为 "confounded by centrality"，改为报告 FewRel R²=22% 作为主要 claim；(b) 对 DocRED 做 centrality-residualized BCS 回归，报告去除 centrality 后的残差 R²；(c) 或将 DocRED R² 从正文移至 Appendix 讨论。

**N2** [critical] Gemini 跨模型验证受单一 leverage point 驱动

- **具体位置**：Section 4.3 ("Cross-model validation"), Appendix C (leave-one-out analysis)
- **问题**：Appendix C 披露，Gemini 2.5 Flash count-16 的 BCS-accuracy 相关受到一个 high-BCS outlier 驱动 (BCS=0.197, accuracy 59.9%)。Leave-one-out 删除该点后，Pearson r 从 −0.480 降至 −0.18 (p=0.64)，Spearman ρ 从 −0.480 降至 −0.18 (p=0.64)，**相关完全不显著**。然而，Section 4.3 正文声称 Gemini 的结果 "replicates on a proprietary architecture with unknown training details"，未提及此 leverage point 问题。
- **为什么影响接收**：论文声称 "4 model families" 跨模型验证是关键 selling point。如果 Gemini（唯一的 proprietary model）的验证依赖单个异常点，则跨模型验证实际上是 3 个开源模型家族（Qwen + 2 个 LLaMA sizes），且都是 decoder-only architectures。这显著削弱了普适性声明。
- **建议修改方向**：(a) Section 4.3 必须在正文中披露 Gemini leverage point 问题；(b) 将 Gemini 描述为 "directionally consistent but statistically fragile"；(c) 考虑增加更多 Gemini batches 以提高统计稳定性。

**N3** [critical] Ecological correlation caveat 需要更显著的 framing

- **具体位置**：Abstract ("BCS explains 22–58%"), Section 4.2, Section 4.3, Appendix N
- **问题**：Pair-level r² ≈ 1.3–5.2% (Table 2)，但 batch-level R² = 22–58%。这个 ~10–40× 的放大是 ecological aggregation 的数学必然（Appendix N 的 simulation 证实了这一点），而非 confusability 有强大的个体预测力。然而，论文的核心叙事围绕 batch-level R² 展开，只在 Section 4.2 用一句话提及 Robinson (1950) ecological correlation。Abstract 和 Conclusion 均使用 "BCS explains 22–58% of cross-batch RE accuracy variance" 而未注明 ecological 属性。
- **为什么影响接收**：不了解 ecological correlation 的读者（NLP 社区中可能占多数）会将 R²=22–58% 误读为 BCS 对个体预测有强解释力。实际上，任何 batch-level 聚合的弱信号都会产生类似放大。这不是作者的错误，但需要更显著的 caveat 以避免过度解读。
- **建议修改方向**：(a) Abstract 加注 "at the ecological (batch-aggregate) level"；(b) Section 4.3 添加一段专门讨论 ecological amplification 的含义和局限；(c) 正文引用 Appendix N simulation 结果，说明 pair-level r²=1.3% 如何通过 ~28 pairs 的聚合产生 batch-level R²=22%。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] DocRED 每 count level 仅 5 batches，R² 估计存在小样本膨胀

- **具体位置**：Section 3.3 (Table 1 footnote), Appendix J
- **问题**：FewRel 使用 25 batches/count level，DocRED 仅 5 batches/count level。N=5 时 R² 估计即使经过 adjusted R² 校正仍然存在显著正偏。Appendix J 报告 95% CI [0.47, 0.75]，区间虽宽但点估计 (R²=0.614) 仍然主导叙事。更重要的是，N=5 + VIF=50.9 的组合意味着 DocRED 的偏相关分析几乎没有统计效力来分离 BCS 与 centrality。
- **建议**：明确报告 DocRED 的有效样本量和相应的 R² 估计精度限制；考虑增加 DocRED batches 或降低对 DocRED R² 的强调。

**W2** [warning] TOST 量表敏感性（linear p=0.003 vs logit p=0.209）处理不充分

- **具体位置**：Appendix C, Section 4.3 (factorial interaction)
- **问题**：Linear-scale TOST 确认等价 (p=0.003)，但 logit-scale TOST 不能确认 (p=0.209)。作者选择 linear-scale 作为 "primary test" 而未提供充分理由。对于 bounded [0,1] 的准确率数据，logit transformation 通常更合适，因为它避免了边界效应对等价检验的影响。如果 logit-scale 结论成立，则 2×2 factorial 的 interaction 可能并非 negligible，这动摇了 "count 和 confusability 效应独立" 的声明。
- **建议**：(a) 提供选择 linear-scale 的统计理由（或引用方法学文献支持）；(b) 将 logit-scale 结果提升至正文而非仅在 appendix 注脚；(c) 如果无法解决量表选择问题，将 factorial interaction 的结论从 "negligible" 改为 "inconclusive depending on scale choice"。

**W3** [warning] 多项核心分析缺乏跨模型验证

- **具体位置**：Section 4.3 ("DocRED R², TOST remain single-model"), Section 4.4, Section 5
- **问题**：以下关键分析仅在 Qwen3-32B 上完成：
  - DocRED R²=58%（最高效应量）
  - Error taxonomy (IntraSub/ExtraSub/Missed/WrongType) 的 BCS scaling
  - SDGD decomposition failure
  - TOST factorial interaction
  跨模型验证仅覆盖 count decline direction + FewRel BCS effect direction (Table 22, 24)，但量化效应量和深层分析均为单模型。这限制了结论的 generalizability，因为不同模型可能有不同的 confusability sensitivity profile。
- **建议**：至少对 LLaMA-70B 复现 DocRED BCS-controlled 实验和 error taxonomy 分析，以验证这些不仅是 Qwen3-32B 的特性。

**W4** [warning] BCS-controlled batch 的 greedy 构建可能引入系统性混淆

- **具体位置**：Section 3.3 (Experiment 2), page 5 left column
- **问题**：High-BCS batch 通过 greedy 搜索选择 SCS 最高的类型对，这些类型通常来自同一语义域（如 Table 26-27 所示，high-BCS pairs 大量来自 person-politician、location-GPE 等同域类型）。这意味着 high-BCS batches 不仅 confusability 高，而且**语义域覆盖更窄**。窄域 batch 可能因为实例分布的 domain-specific 特征（而非 embedding-level confusion）而更难——例如，政治领域的关系类型可能天然有更多歧义实例。论文未讨论这一系统性混淆。
- **建议**：(a) 分析 extreme batches 的语义域覆盖度差异；(b) 增加 domain-controlled 实验（在同一语义域内构建 high/low BCS batches）；(c) 至少在 Discussion 中讨论此 confound 的可能影响。

**W5** [warning] 单种子设计下 FP8 quantization 的 non-determinism

- **具体位置**：Section 3.5, Limitations point 2, Appendix R
- **问题**：虽然 greedy decoding 使输出对同一输入确定，但 FP8 quantization 引入 floating-point non-determinism。Appendix R 报告 residual SD=0.88pp，占观测 BCS effect size 的 18–44%。这意味着在 DocRED (N=5 batches/level) 这样的小样本设置下，单次运行的结果可能有不可忽略的随机波动。
- **建议**：至少对 key results（尤其是 DocRED 和 MAVEN 的小样本实验）运行 3 个 seeds 并报告 cross-seed variance。

---

## 小问题（不影响接收）

1. **孤儿引用**：bib 中有 2 条未被引用的条目 (schall-2025-hidden-cost, tam-2024-let-me-speak)，应清理。
2. **术语**："Training-free" 非标准术语（论文 footnote 1 承认与 "zero-shot" 可互换使用），建议统一使用 "zero-shot" 或在首次使用时更清晰地定义 "training-free" 的范围。
3. **Table 2** MAVEN 的 bootstrap CI (0.081, 0.185) 跨度较大，弱化了 MAVEN pairwise correlation 的信号强度。
4. **Figure 1(b)** BCS-controlled 实验的 error bars 在视觉上不太清晰，建议加大 error bar 的对比度。

---

## Questions for Authors

1. **DocRED centrality confound**：是否可以计算 centrality-residualized BCS（先对 centrality 做回归，取 BCS 残差），然后报告残差 BCS 与 accuracy 的 R²？这能更清楚地隔离 confusability 的独立贡献。

2. **Gemini leverage point**：能否增加 Gemini count-16 的 BCS-controlled batches 数量（如从 25 增至 50），以检验 leverage point 是否是采样偏差？

3. **TOST 量表选择**：是否有统计方法学文献支持在 accuracy ∈ [0,1] 数据上使用 linear-scale TOST 而非 logit-scale？

4. **NER null 的机制解释**：Section 4.5 分析了 MAVEN per-type 的 centrality confound，但未系统解释为什么 confusability 影响 RE 而不影响 NER。是否可能因为 NER 是 span-level 任务（局部特征更重要）而 RE 是 sentence/document-level 任务（全局 schema 推理更重要）？

5. **High-BCS batch 的语义域偏差**：Tables 26-27 显示 high-BCS 的 confused pairs 集中在少数语义域。是否测试过在同一域内构建 BCS-controlled batches 来排除 domain bias？

---

## Missing References

未发现严重遗漏。Related work 覆盖了 schema complexity in dialogue (Rastogi et al., 2020; Lee et al., 2022)、label confusion in CV (Dubey et al., 2018; Collier et al., 2021)、schema decomposition in IE (LLM-PEE, PARSE, DEE) 等关键方向。

可选补充：
- Aly et al. (2019) "Hierarchical Multi-Task Learning for Fine-Grained Entity Typing" —— 讨论了 hierarchical label set 中 type confusion 对 fine-grained entity typing 的影响
- Onoe & Durrett (2020) "Fine-Grained Entity Typing for Domain Independent Entity Linking" —— 研究了 entity type embedding space 的结构对 disambiguation 的影响

---

## Overall Assessment 详述

**接收理由**：
- 研究问题重要且定义清晰（RQ1–RQ3）
- FewRel 上的 BCS 预测效应 (R²=22%, VIF=1.16) 在低混淆条件下是可信的
- 实验设计精细，统计方法透明度高
- 负面结果 (NER null, SDGD failure) 是有价值的社区贡献
- BCS 作为 pre-hoc diagnostic 有明确的实用价值

**拒稿顾虑**：
- 最引人注目的定量 claim (R²=58%) 本质上不可解释（centrality vs. confusability）
- 跨模型验证在 Gemini 上由单一 leverage point 支撑
- 核心分析（error taxonomy, SDGD, DocRED R²）均为 Qwen3-32B 单模型
- Ecological correlation 的 framing 可能导致读者过度解读效应量
- TOST 量表敏感性使 factorial independence 结论悬而未决

**综合判断**：论文在 FewRel 上提供了可信的 confusability 效应证据 (R²=22%)，但主要 selling points (DocRED 58%, 4-model validation, clean factorial) 均存在方法学弱点。如果作者在 revision 中 (a) 重新 frame DocRED 结果以反映 centrality confound，(b) 在正文中披露 Gemini leverage point，(c) 加强 ecological correlation caveat，这篇论文可以达到 Conference 水准。目前的 framing 下，Soundness 和 Excitement 均处于 Conference/Findings 边界，给予 **3.5 = Borderline Conference**。


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


### Tool call

_source line 2686 · 2026-05-21T18:59:14.506950+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性和 Venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 人数和侧重'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'Reviewer 1 和 Reviewer 2 独立审稿完成'}, {'content': 'Step 2: 交叉分享', 'status': 'in_progress', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
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
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性和 Venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 人数和侧重'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'Reviewer 1 和 Reviewer 2 独立审稿完成'}, {'content': 'Step 2: 交叉分享', 'status': 'in_progress', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿意见是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2687 · 2026-05-21T18:59:14.557724+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2688 · 2026-05-21T18:59:35.889732+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每一条使用：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n### 总体评分\n**Overall: 3.0 (Findings)**, Confidence: 4/5\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 2.5/5 |\n| Reproducibility | 4/5 |\n\n### Must-Fix (2 items)\n\n**N1** SCS/BCS 指标新颖性不足，贡献定位模糊 — SCS 本质是标准 embedding cosine similarity，继承自 LLM-PEE。论文真正的贡献在于实验方法论（BCS-controlled batch design），但 Abstract 和 Contributions 的措辞将 SCS 包装为独立贡献。需明确区分 methodology contribution vs. metric contribution。\n\n**N2** NER null 叙述内部张力 — 论文同时给出 \"structural barrier\"（NER 错误分散于 miss/boundary/type，BCS 根本无法预测）和 \"insufficient power\"（65% power，absence of evidence）两种不兼容解释。Abstract \"confirmed on three models\" 的措辞暗示确定性结论，但 Appendix E.2 承认统计功效不足。需在正文中明确承认张力并统一叙述。\n\n### Should-Fix (5 items)\n\n**W1**: Abstract 信息过载（数字过多）\n\n**W2**: Section 5-6 过于压缩（Schema Decomposition 是三大贡献之一却只有半 column）\n\n**W3**: 生态谬误影响讨论不足（batch-level R² 对 individual type-pair prediction 的实用性有限）\n\n**W4**: 跨模型验证深度不均（DocRED R²=0.58 仅 single-model）\n\n**W5**: MAVEN centrality confound 使 BCS 预测力实际仅在 RE 两个数据集上验证\n\n### 主要优势\n1. BCS-controlled batch 实验设计巧妙，统计分析严谨\n2. 诚实报告负面结果（NER null, SDGD failure, MAVEN confound）\n3. 14 页 Appendix 含大量 robustness checks\n4. 跨 4 个模型家族验证方向一致性\n5. 研究问题具有直接实际应用价值\n\n### 引用检查\n- 72 bib entries, 70 cited, 2 orphan\n- 无虚假引用\n\n### 格式合规\n- ✅ 全部通过（ACL template, 8 页正文, Limitations 合规, 匿名化完整, Checklist 注释）\n\n---\n\n请对 R2 的每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT] 回应。"
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
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每一条使用：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n以下是 Reviewer 2 的完整审稿原文：\n\n### 总体评分\n**Overall: 3.0 (Findings)**, Confidence: 4/5\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 2.5/5 |\n| Reproducibility | 4/5 |\n\n### Must-Fix (2 items)\n\n**N1** SCS/BCS 指标新颖性不足，贡献定位模糊 — SCS 本质是标准 embedding cosine similarity，继承自 LLM-PEE。论文真正的贡献在于实验方法论（BCS-controlled batch design），但 Abstract 和 Contributions 的措辞将 SCS 包装为独立贡献。需明确区分 methodology contribution vs. metric contribution。\n\n**N2** NER null 叙述内部张力 — 论文同时给出 \"structural barrier\"（NER 错误分散于 miss/boundary/type，BCS 根本无法预测）和 \"insufficient power\"（65% power，absence of evidence）两种不兼容解释。Abstract \"confirmed on three models\" 的措辞暗示确定性结论，但 Appendix E.2 承认统计功效不足。需在正文中明确承认张力并统一叙述。\n\n### Should-Fix (5 items)\n\n**W1**: Abstract 信息过载（数字过多）\n\n**W2**: Section 5-6 过于压缩（Schema Decomposition 是三大贡献之一却只有半 column）\n\n**W3**: 生态谬误影响讨论不足（batch-level R² 对 individual type-pair prediction 的实用性有限）\n\n**W4**: 跨模型验证深度不均（DocRED R²=0.58 仅 single-model）\n\n**W5**: MAVEN centrality confound 使 BCS 预测力实际仅在 RE 两个数据集上验证\n\n### 主要优势\n1. BCS-controlled batch 实验设计巧妙，统计分析严谨\n2. 诚实报告负面结果（NER null, SDGD failure, MAVEN confound）\n3. 14 页 Appendix 含大量 robustness checks\n4. 跨 4 个模型家族验证方向一致性\n5. 研究问题具有直接实际应用价值\n\n### 引用检查\n- 72 bib entries, 70 cited, 2 orphan\n- 无虚假引用\n\n### 格式合规\n- ✅ 全部通过（ACL template, 8 页正文, Limitations 合规, 匿名化完整, Checklist 注释）\n\n---\n\n请对 R2 的每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 2689 · 2026-05-21T18:59:57.084835+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21195
}
```

</details>

---


### Tool call

_source line 2690 · 2026-05-21T18:59:57.236088+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "schema-dag-extraction",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每一条使用：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### 总体评分\n**Overall: 3.5 (Borderline Conference)**, Confidence: 4/5\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 3.5/5 |\n| Reproducibility | 4/5 |\n\n### Must-Fix (3 items)\n\n**N1** [critical] DocRED R²=58% 受 centrality 严重混淆，不应作为核心 claim\n- Table 11 显示 DocRED 上 BCS 与 degree centrality 的 VIF=50.9，两变量相关系数 r=0.99\n- Abstract 和 Section 4.3 仍然突出报道 \"22–58%\"，读者自然将上界 58% 视为 confusability 的解释力，这是误导性的\n- FewRel R²=22% (VIF=1.16) 是唯一可靠的效应量估计\n- 建议：Abstract 标注 DocRED R² 为 \"confounded by centrality\"，以 FewRel R²=22% 为主要 claim\n\n**N2** [critical] Gemini 跨模型验证受单一 leverage point 驱动\n- Gemini count-16 leave-one-out 删除 high-BCS outlier 后，r 从 −0.480 降至 −0.18 (p=0.64)，相关完全不显著\n- Section 4.3 正文未提及此 leverage point 问题\n- 论文声称 \"4 model families\" 跨模型验证是关键 selling point，但 Gemini 验证实际上 statistically fragile\n- 建议：正文披露 leverage point，将 Gemini 描述为 \"directionally consistent but statistically fragile\"\n\n**N3** [critical] Ecological correlation caveat 需要更显著的 framing\n- Pair-level r² ≈ 1.3–5.2% 但 batch-level R² = 22–58%，~10–40× 放大是 ecological aggregation 的数学必然\n- Abstract 和 Conclusion 使用 \"BCS explains 22–58%\" 而未注明 ecological 属性\n- 不了解 ecological correlation 的 NLP 读者会误读效应量\n- 建议：Abstract 加注 \"at the ecological (batch-aggregate) level\"，Section 4.3 添加专门讨论段\n\n### Should-Fix (5 items)\n\n**W1**: DocRED 每 count level 仅 5 batches，R² 估计存在小样本膨胀\n\n**W2**: TOST 量表敏感性（linear p=0.003 vs logit p=0.209）处理不充分。对 bounded [0,1] 数据，logit transformation 通常更合适。\n\n**W3**: 多项核心分析缺乏跨模型验证（DocRED R²=58%, Error taxonomy, SDGD, TOST factorial 均仅 Qwen3-32B）\n\n**W4**: BCS-controlled batch 的 greedy 构建可能引入系统性混淆——high-BCS batches 语义域覆盖更窄，可能因 domain-specific 特征而更难\n\n**W5**: 单种子设计下 FP8 quantization 的 non-determinism（residual SD=0.88pp，占 BCS effect size 18–44%）\n\n### 小问题\n1. 2 条孤儿 bib entries\n2. \"Training-free\" vs \"zero-shot\" 术语统一\n3. Table 2 MAVEN bootstrap CI 跨度大\n4. Figure 1(b) error bars 对比度不足\n\n### Questions for Authors\n1. 能否计算 centrality-residualized BCS 的残差 R²？\n2. 能否增加 Gemini batches 检验 leverage point？\n3. 是否有文献支持 linear-scale TOST？\n4. NER null 是否因为 span-level vs sentence-level 任务差异？\n5. 是否测试过同域内 BCS-controlled batches？\n\n### Missing References\n无严重遗漏。可选补充 Aly et al. (2019), Onoe & Durrett (2020)。\n\n---\n\n请对 R1 的每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT] 回应。"
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
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每一条使用：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n以下是 Reviewer 1 的完整审稿原文：\n\n### 总体评分\n**Overall: 3.5 (Borderline Conference)**, Confidence: 4/5\n\n| 维度 | 分数 |\n|------|------|\n| Soundness | 3.5/5 |\n| Excitement | 3.5/5 |\n| Reproducibility | 4/5 |\n\n### Must-Fix (3 items)\n\n**N1** [critical] DocRED R²=58% 受 centrality 严重混淆，不应作为核心 claim\n- Table 11 显示 DocRED 上 BCS 与 degree centrality 的 VIF=50.9，两变量相关系数 r=0.99\n- Abstract 和 Section 4.3 仍然突出报道 \"22–58%\"，读者自然将上界 58% 视为 confusability 的解释力，这是误导性的\n- FewRel R²=22% (VIF=1.16) 是唯一可靠的效应量估计\n- 建议：Abstract 标注 DocRED R² 为 \"confounded by centrality\"，以 FewRel R²=22% 为主要 claim\n\n**N2** [critical] Gemini 跨模型验证受单一 leverage point 驱动\n- Gemini count-16 leave-one-out 删除 high-BCS outlier 后，r 从 −0.480 降至 −0.18 (p=0.64)，相关完全不显著\n- Section 4.3 正文未提及此 leverage point 问题\n- 论文声称 \"4 model families\" 跨模型验证是关键 selling point，但 Gemini 验证实际上 statistically fragile\n- 建议：正文披露 leverage point，将 Gemini 描述为 \"directionally consistent but statistically fragile\"\n\n**N3** [critical] Ecological correlation caveat 需要更显著的 framing\n- Pair-level r² ≈ 1.3–5.2% 但 batch-level R² = 22–58%，~10–40× 放大是 ecological aggregation 的数学必然\n- Abstract 和 Conclusion 使用 \"BCS explains 22–58%\" 而未注明 ecological 属性\n- 不了解 ecological correlation 的 NLP 读者会误读效应量\n- 建议：Abstract 加注 \"at the ecological (batch-aggregate) level\"，Section 4.3 添加专门讨论段\n\n### Should-Fix (5 items)\n\n**W1**: DocRED 每 count level 仅 5 batches，R² 估计存在小样本膨胀\n\n**W2**: TOST 量表敏感性（linear p=0.003 vs logit p=0.209）处理不充分。对 bounded [0,1] 数据，logit transformation 通常更合适。\n\n**W3**: 多项核心分析缺乏跨模型验证（DocRED R²=58%, Error taxonomy, SDGD, TOST factorial 均仅 Qwen3-32B）\n\n**W4**: BCS-controlled batch 的 greedy 构建可能引入系统性混淆——high-BCS batches 语义域覆盖更窄，可能因 domain-specific 特征而更难\n\n**W5**: 单种子设计下 FP8 quantization 的 non-determinism（residual SD=0.88pp，占 BCS effect size 18–44%）\n\n### 小问题\n1. 2 条孤儿 bib entries\n2. \"Training-free\" vs \"zero-shot\" 术语统一\n3. Table 2 MAVEN bootstrap CI 跨度大\n4. Figure 1(b) error bars 对比度不足\n\n### Questions for Authors\n1. 能否计算 centrality-residualized BCS 的残差 R²？\n2. 能否增加 Gemini batches 检验 leverage point？\n3. 是否有文献支持 linear-scale TOST？\n4. NER null 是否因为 span-level vs sentence-level 任务差异？\n5. 是否测试过同域内 BCS-controlled batches？\n\n### Missing References\n无严重遗漏。可选补充 Aly et al. (2019), Onoe & Durrett (2020)。\n\n---\n\n请对 R1 的每个 Must-Fix 和 Should-Fix 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 2691 · 2026-05-21T18:59:58.650020+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1413
}
```

</details>

---


### Assistant

_source line 2692 · 2026-05-21T19:00:02.928781+00:00_

交叉分享已派发。两位 Reviewer 正在互审对方意见，等待 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 222

## Round 222

2 recorded events


### User

_source line 2693 · 2026-05-21T19:00:05.843567+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**审稿结论**：3.5/5 (Borderline Conference)。

识别了 3 个 Must-Fix 问题：
1. DocRED R²=58% 受 centrality 严重混淆 (VIF=50.9)，不应作为核心 claim
2. Gemini 跨模型验证受单一 leverage point 驱动（leave-one-out 后 p=0.64）
3. Ecological correlation caveat 不够显著，读者可能将 batch-level R²=22-58% 误读为个体级强效应

5 个 Should-Fix：TOST 量表敏感性、DocRED 小样本膨胀、多项核心分析缺乏跨模型验证、BCS-controlled batch 的语义域系统偏差、单种子 FP8 non-determinism。

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

_source line 2694 · 2026-05-21T19:00:14.723319+00:00_

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


## Round 223

## Round 223

2 recorded events


### User

_source line 2695 · 2026-05-21T19:01:20.893789+00:00_

[Reviewer 1 审稿结果]:
逐条回应 Reviewer 2 的审稿意见。

---

## 交叉回应：Reviewer 1 → Reviewer 2

### Must-Fix

**[AGREE] R2-N1: SCS/BCS 指标新颖性定位**

同意 R2 的核心判断。SCS 本质是 `cos(embed(name_i), embed(name_j))`（Section 3.2），这是标准的 embedding cosine similarity，没有方法论上的新意。LLM-PEE (2025) 已经使用 pairwise SCS 做 schema partitioning，本文的 SCS 定义与之几乎相同。BCS 只是 SCS 的算术平均。

论文的真正贡献在于 **实验设计**（BCS-controlled extreme batch 构建 + count curves 的双重验证框架）和 **empirical findings**（RE vs NER asymmetry, merge amplification failure），而非 metric 本身。但 Abstract 的行文 "We quantify confusability via the Schema Confusability Score (SCS) and its batch-level aggregation, the Batch Confusability Score (BCS)" 以及 Contributions 第 2 条 "we document a task asymmetry: BCS explains 22–58% of RE accuracy variance"，都将 SCS/BCS 作为核心话语单元，客观上制造了 metric novelty 的印象。

补充一点 R2 未提及的：Appendix M (Table 19) 显示 name-only SCS 与 name+definition SCS 的预测力无差异 ("definitions provide no systematic benefit")。这进一步说明 SCS 只是捕获了 **表面名称重叠**，而非深层概念混淆。如果一个 metric 对其理论构念（type confusability）的操作化如此粗糙，将其作为独立贡献是值得质疑的。

**[AGREE] R2-N2: NER null 叙述内部张力**

完全同意。这是论文叙述逻辑中一个真实的矛盾：

1. **"结构性障碍" 解释**（Section 4.4, Section 6）：NER 错误分散于 IntraSub（56–93%）、Missed（10–43%）和 boundary errors，BCS 仅与 IntraSub 相关，因此 batch-level 信号被稀释——这意味着 **NER null 是 genuine**，confusability 不是 NER 的主要退化因素。

2. **"统计功效不足" 解释**（Appendix E.2）：Few-NERD 的 BCS 标准差仅 0.027（FewRel 的 19%），受限的 BCS range 导致 65% power (α=.05)，最小可检测 |r| = 0.132——这意味着 **NER null 可能是 false negative**，效应可能存在但检测不到。

两种解释不可能同时成立：如果 NER 的退化确实由 confusability 以外的因素主导（解释 1），那么 power 不足（解释 2）就不是问题，因为没有效应可以检测；反之，如果 power 是问题，那么 "structural barrier" 的结论就太强了。

Abstract 说 "NER batch-level confusability signal remains nonexistent, suggesting task-dependent effect structures" —— "suggesting" 虽然比 "confirmed" 弱，但 "nonexistent" 一词仍然传达了确定性。正文应明确采取其中一种立场，或将两种作为 competing hypotheses 呈现并讨论如何在未来工作中区分。

---

### Should-Fix

**[AGREE] R2-W1: Abstract 信息过载**

部分同意。Abstract 中包含 "r² ≈ 1.3–1.7%"、"22–58%"、"up to ~49pp"、"96-relation"、"22–44 types"、"−0.27"、"0.72" 等大量数字，信息密度过高。对于不熟悉该领域的读者，这些数字难以在第一次阅读中形成连贯理解。但我认为这更多是 **写作风格问题** 而非方法学问题，不应上升到 Must-Fix 级别。R2 也只将其列为 Should-Fix，分级合理。

**[AGREE] R2-W2: Section 5-6 过度压缩**

同意。Section 5（Schema Decomposition: Failure, Diagnosis, and Mitigation）是三大贡献之一，但正文仅约半个 column（page 8 上半部分），涵盖了 NER merge amplification、RE routing failure、和 boundary conditions 三个子主题。虽然详细数据在 Appendix B (Tables 7, 8, 12) 中，但正文的 narrative 过于急促——读者需要在半 column 内理解 SDGD 为什么失败、失败的两种不同机制（NER vs RE）、以及 boundary conditions，这对信息吸收构成压力。

建议将 Section 5 扩展到至少一个完整 column，可以通过压缩 Section 2 Related Work（当前约 1.3 页，部分内容与 Introduction 重复）来腾出空间。

**[AGREE] R2-W3: 生态谬误影响讨论不足**

完全同意，且这与我的 N3 高度一致。Batch-level R² = 22–58% 对个体 type-pair prediction 的实用性确实有限。论文的实际应用场景（Section 6: "BCS enables pre-hoc diagnostics"）是 batch-level 的，所以 ecological aggregation 并不削弱其实用价值，但论文需要更清楚地将 R² 的解读限定在 batch-level 诊断用途，而非暗示 confusability 对单个抽取实例有强预测力。

**[AGREE] R2-W4: 跨模型验证深度不均（DocRED R²=0.58 单模型）**

完全同意，与我的 W3 一致。补充证据：Table 24 的跨模型 BCS-controlled 结果仅限 FewRel RE，而 DocRED（论文最高 R² 的数据集）和 MAVEN 均未做跨模型 BCS-controlled 验证。Section 4.3 自己承认 "DocRED R², TOST remain single-model"，但这一关键限制在 Conclusion 中被 "replicated across four models spanning three architecture families" 的措辞掩盖了。

**[REBUT] R2-W5: BCS 预测力实际仅在 RE 两个数据集验证**

R2 的结论方向正确，但分级低估了问题严重性。R2 将此列为 Should-Fix，但实际上这个问题比 R2 描述的更严重：

- **FewRel**：BCS 效应可信（R²=22%, VIF=1.16）——这是唯一 clean 的验证
- **DocRED**：VIF=50.9，BCS 与 centrality 近乎完全共线性（r=0.99），**无法归因于 confusability**（我的 N1）
- **Few-NERD**：Null result
- **MAVEN**：Section 4.5 和 Appendix E 显示 centrality confound 使 BCS 信号消失（控制 centrality 后 correlation weakens to non-significance）

因此，BCS 作为 confusability 的独立预测指标，**严格来说仅在 FewRel 1 个数据集上获得 clean 验证**，而非 R2 所说的 "2 个 RE 数据集"。DocRED 的 R²=58% 可能大部分来自 centrality 而非 confusability。这应该是 Must-Fix 级别的问题，因为它直接影响论文核心 claim ("BCS explains 22–58% of variance") 的可信度。FewRel 单数据集的 R²=22% 是实际可信的效应量上界。

---

### 对 R2 总体评分的看法

R2 给出 Overall 3.0 (Findings)，我给出 3.5 (Borderline Conference)。差异主要来自 Excitement 维度：R2 给 2.5，我给 3.5。

我认为 R2 在 Excitement 上偏低。虽然 SCS/BCS metric 本身缺乏新意（同意 R2-N1），但论文的 **实验方法论贡献**（BCS-controlled batch design 作为隔离混淆变量的范式）和 **负面结果**（NER null、SDGD failure、merge amplification）对社区有明确的实用和启发价值。这些发现不需要复杂的新 metric 来支撑——简单 metric + 精细实验设计 本身就是一种贡献模式。Excitement 2.5 意味着 "potentially interesting to some community members"，但考虑到 training-free LLM IE 的快速增长和 schema complexity 问题的普遍性，我认为 3.0–3.5 更合适。

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

_source line 2696 · 2026-05-21T19:01:27.614128+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 224

## Round 224

14 recorded events


### User

_source line 2697 · 2026-05-21T19:02:04.155514+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 交叉回应 R1 完成

### 回应总结

**R1 Must-Fix (3 items):**
- N1 DocRED R²=58% centrality confound → **[AGREE]** Table 11 VIF=50.9 使该 R² 不可信，可靠估计仅 FewRel R²=22%
- N2 Gemini leverage point → **[AGREE]** BCS dimension 验证 fragile，但 count dimension 方向一致性不受影响
- N3 Ecological correlation caveat → **[AGREE]** 与我 W3 独立指出的问题重合，pair-level r²≈1.3-5.2% 到 batch R²=22% 是 ecological aggregation

**R1 Should-Fix (5 items):**
- W1 DocRED 5-batch R² 膨胀 → **[AGREE]**
- W2 TOST logit vs linear → **[REBUT]** accuracy 范围 0.70-0.92 远离边界，linear 可辩护；核心 claim 不依赖 TOST
- W3 缺乏跨模型验证 → **[AGREE]** 与我 W4 重合
- W4 Greedy batch 构建 confound → **[AGREE]** 真实 confound，论文有部分 mitigations 但不完全
- W5 单种子 FP8 non-determinism → **[AGREE]** 18-44% of effect size 是非平凡的

### 关键共识
两位 Reviewer 独立达成一致：论文方法论和统计设计属上乘，但 **claims scope 超出证据可靠支撑**。可靠结论应收紧至 "FewRel R²≈22%, ecological level, open-weight models"。

### 评分维持
Overall 3.0 (Findings)，R1 的分析（特别是 DocRED centrality）强化了我对 novelty/excitement 的保留意见。

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

_source line 2698 · 2026-05-21T19:02:39.601118+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性和 Venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 人数和侧重'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'Reviewer 1 和 Reviewer 2 独立审稿完成'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享完成'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '关键问题已达成共识，满足收敛标准'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'in_progress', 'activeForm': '汇总审稿报告并投递'}]"
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
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性和 Venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 人数和侧重'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'Reviewer 1 和 Reviewer 2 独立审稿完成'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享完成'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '关键问题已达成共识，满足收敛标准'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'in_progress', 'activeForm': '汇总审稿报告并投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2699 · 2026-05-21T19:02:39.651919+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2700 · 2026-05-21T19:02:39.652338+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

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
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 2701 · 2026-05-21T19:02:39.704015+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-21T18:49:05.553692+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_51326259fe46fbae9da26b81cf03f1f8\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2702 · 2026-05-21T19:02:39.704505+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

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
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "schema-dag-extraction"
  }
}
```

</details>

---


### Tool result

_source line 2703 · 2026-05-21T19:02:39.855510+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-21T18:49:04.688007+00:00\", \"completed_at\": \"2026-05-21T18:52:37.942833+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-3\", \"message\": \"连续 3 页纯文本（Title/Abstract/Intro/Related Work），无任何 display item。审稿人需翻过 3 页才看到第一个视觉锚点（Table 1, p4）。建议在 p1 或 p2 加入一个概览图（如 SCS 概念示意 / 核心发现预览图），帮助审稿人在前 2 分钟内锚定论文贡献\"}, {\"severity\": \"warning\", \"dimension\": \"page 1-8\", \"message\": \"正文 8 页仅 4 个 display items（Table 1-2, Figure 1-2），对于实证为主的论文偏少（通常 5-8 个）。核心定量结果（count-degradation 斜率、BCS 效应量、跨模型验证）分散在正文文字中，缺少一张汇总 main results 表。审稿人需逐段读文字才能拼凑全貌\"}, {\"severity\": \"warning\", \"dimension\": \"page 8-9\", \"message\": \"连续 2 页纯文本（Section 5 Schema Decomposition + Section 6 Discussion + Limitations），无 display item 穿插。Section 5 的 decomposition failure 分析适合用一张小表或示意图辅助\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Table 1（Dataset statistics）使用 booktabs 风格，排版整洁。但作为论文第一个 display item，它是描述性统计表而非核心结果——锚定效应弱于一个传达核心 message 的 figure\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 1 全宽双面板，蓝/橙配色方案色盲友好。左面板 degradation curves 清晰，右面板 bar chart 标注了具体数值（+13.3pp 等）。Caption 多行，信息自包含。字号可读但偏小，建议 axis label 再放大 ~10%\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 1 左面板：FewRel RE 的两条线（all-types / BCS-ctrl）在高 count 端几乎重合，视觉区分度低。可考虑用不同 line style（dash vs solid）加强区分\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Table 2 紧凑清晰，correlation 值排列整齐。Booktabs 风格。无问题\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2 全宽双面板，配色与 Figure 1 一致（颜色语义连贯）。Error share (%) 的 y 轴从 0 开始，合理。IntraSub/ExtraSub 类别清晰。Caption 详细自包含\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 2 panel (a) Few-NERD NER 图中 legend 放在图内右侧，与数据线有轻微重叠。可考虑移至图外或调整位置\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": \"Limitations 段 4 个点，篇幅约 2/3 页。按 EMNLP 规范覆盖面
…[truncated 975 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2704 · 2026-05-21T19:06:12.276185+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "schema-dag-extraction",
  "issues_yaml": "# Review Issues Tracker\n# Updated: 2026-05-21 (Round 24 — Fresh review, report synthesis)\n\n# ============================================================\n# R24 MUST-FIX (Consensus from R1+R2, 5 items)\n# ============================================================\n\n- id: R24-C1\n  summary: \"DocRED R²=58% 受 centrality 严重混淆 (VIF=50.9)，不应作为核心 claim\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-C2: VIF=50.9 标准误膨胀 ~7.1x\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R1-N1 Must-Fix, R2 AGREE。BCS-centrality r=0.99, 偏相关无法归因 confusability vs centrality。FewRel R²=22% (VIF=1.16) 是唯一 clean estimate。Abstract '22-58%' 误导。\"}\n  action_items:\n    - {round: 23, action: \"重写 DocRED 偏相关段\", assigned_to: \"Agent\", status: in_progress}\n    - {round: 24, action: \"Abstract/正文将 DocRED R² 标注为 confounded by centrality，以 FewRel R²=22% 为主要 claim；或做 centrality-residualized BCS 回归\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-C2\n  summary: \"Gemini 跨模型验证受单一 leverage point 驱动 (leave-one-out 后 p=0.64)\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-W4: 分歧保留，R2 降为 Should-Fix\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R1-N2 Must-Fix, R2 AGREE（BCS dimension fragile, count dimension OK）。Leave-one-out 删除 BCS=0.197 outlier 后 r 从 -0.480 降至 -0.18。正文未披露。升级为 Must-Fix 共识。\"}\n  action_items:\n    - {round: 23, action: \"报告 leave-one-out sensitivity\", assigned_to: \"Agent\", status: in_progress}\n    - {round: 24, action: \"正文 §4.3 披露 Gemini leverage point，描述为 directionally consistent but statistically fragile；考虑增加 Gemini batches\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-C3\n  summary: \"Ecological correlation caveat 不够显著，batch-level R² 可能被读者误读为个体级强效应\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-W3: pair-to-batch 15× 放大是 aggregation smoothing\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R1-N3 Must-Fix, R2 AGREE（与 R2-W3 独立重合）。Pair r²≈1.3-5.2% → batch R²=22-58% 是 ecological aggregation 数学必然。Abstract/Conclusion 未注明 ecological 属性。升级为 Must-Fix 共识。\"}\n  action_items:\n    - {round: 23, action: \"§4.3 加 ecological correlation caveat + Robinson (1950) 正文引用\", assigned_to: \"Agent\", status: in_progress}\n    - {round: 24, action: \"Abstract 加注 at the ecological (batch-aggregate) level；§4.3 添加专门讨论段，引用 Appendix N simulation\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-C4\n  summary: \"SCS/BCS 指标新颖性不足，贡献定位模糊——需明确区分 methodology vs metric contribution\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-W1: SCS = LLM-PEE criterion 形式一致\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R2-N1 Must-Fix, R1 AGREE。SCS 是标准 embedding cosine similarity，继承自 LLM-PEE。Name-only vs name+def 无差异 (Appendix M) 进一步说明 SCS 操作化粗糙。真正贡献在实验方法论 (BCS-controlled batch design)，但 Abstract/Contributions 包装为 metric 贡献。升级为 Must-Fix 共识。\"}\n  action_items:\n    - {round: 23, action: \"§2 Related Work 加 explicit novelty positioning\", assigned_to: \"Agent\", status: in_progress}\n    - {round: 24, action: \"重写 Contributions 区分 methodology contribution (BCS-controlled batch design) vs metric (SCS inherits LLM-PEE)；Abstract 措辞降低 SCS 独立贡献暗示\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-C5\n  summary: \"NER null 叙述内部张力——structural barrier 与 insufficient power 两种解释不兼容\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-C3: §5/§6 的 structural barrier 与 power=65% 矛盾\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R2-N2 Must-Fix, R1 AGREE。structural barrier (IntraSub 56-93%, errors scatter) 暗示 genuine null，但 power=65% 暗示 possible false negative。Abstract 'confirmed on three models' 措辞传达确定性。两种解释不可同时成立。\"}\n  action_items:\n    - {round: 23, action: \"双层解释 + Abstract 加 NER null qualifier\", assigned_to: \"Agent\", status: in_progress}\n    - {round: 24, action: \"明确采取一种立场或将两种作为 competing hypotheses 呈现；Abstract 避免暗示确定性结论\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R24 SHOULD-FIX (Consensus, 7 items)\n# ============================================================\n\n- id: R24-W1\n  summary: \"DocRED 每 count level 仅 5 batches，R² 估计存在小样本正偏\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-W6: n=5 per level 偏低\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R1-W1, R2 AGREE。N=5 + VIF=50.9 组合使 DocRED 偏相关分析几乎无统计效力。\"}\n  action_items:\n    - {round: 24, action: \"明确报告 DocRED 有效样本量和 R² 估计精度限制\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-W2\n  summary: \"多项核心分析缺乏跨模型验证 (DocRED R², error taxonomy, SDGD, TOST 均仅 Qwen3-32B)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-C4: DocRED R²=58% 缺乏跨模型支持\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R1-W3 + R2-W4 独立重合。Conclusion 中 'replicated across four models' 掩盖了仅 count direction + FewRel BCS direction 被跨模型验证的事实。\"}\n  action_items:\n    - {round: 24, action: \"Conclusion 措辞精确化跨模型验证范围；至少对 LLaMA-70B 复现 DocRED BCS-controlled\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-W3\n  summary: \"BCS-controlled batch 的 greedy 构建引入语义域系统偏差\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - {round: 24, reviewers: [R1, R2], note: \"R1-W4 新发现, R2 AGREE。High-BCS batches 语义域覆盖更窄（Tables 26-27），可能因 domain-specific 特征而更难，非纯 embedding confusion。论文未讨论。\"}\n  action_items:\n    - {round: 24, action: \"分析 extreme batches 语义域覆盖度差异；Discussion 讨论此 confound；考虑同域内 BCS-controlled 实验\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-W4\n  summary: \"单种子 + FP8 quantization non-determinism (residual SD=0.88pp, 占 BCS effect 18-44%)\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-F4: Residual SD=0.88pp\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R1-W5, R2 AGREE。DocRED (N=5) 下单次运行有不可忽略随机波动。\"}\n  action_items:\n    - {round: 24, action: \"至少对 key results (DocRED, MAVEN) 运行 3 seeds 并报告 cross-seed variance\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-W5\n  summary: \"Abstract 信息过载，数字密度过高影响首次阅读理解\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-F2: §4.1-4.3 每段 10+ 统计值\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R2-W1, R1 AGREE (写作风格问题，非方法学问题)。\"}\n  action_items:\n    - {round: 24, action: \"Abstract 精简数字，保留 headline numbers\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-W6\n  summary: \"Sections 5-6 过度压缩 (Schema Decomposition 仅半 column)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-W5: §4.5 留正文但压缩\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R2-W2, R1 AGREE。三大贡献之一却只有半 column。建议压缩 §2 Related Work 腾出空间。\"}\n  action_items:\n    - {round: 24, action: \"Section 5 扩展到至少一个完整 column\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-W7\n  summary: \"BCS clean validation 实际仅限 FewRel 1 个数据集 (DocRED confounded, MAVEN confounded, NER null)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - {round: 24, reviewers: [R1, R2], note: \"R1 交叉回应升级 R2-W5。FewRel R²=22% (VIF=1.16) 是唯一 clean verification。DocRED VIF=50.9, MAVEN centrality confound, NER null。R2 原评估为 2 个 RE 数据集，R1 认为实际仅 1 个。分歧保留。\"}\n  action_items:\n    - {round: 24, action: \"明确论文可靠结论范围：FewRel R²≈22%, ecological level, open-weight models\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R24 DIVERGENCE (1 item)\n# ============================================================\n\n- id: R24-D1\n  summary: \"TOST 量表敏感性 (linear p=0.003 vs logit p=0.209)\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-C1: Logit-scale inconclusive\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R1-W2 Should-Fix vs R2 REBUT (accuracy 0.70-0.92 远离边界, linear defensible; 核心 claim 不依赖 TOST)。分歧保留。相比 R23 从 critical 降级为 divergent warning。\"}\n  action_items:\n    - {round: 24, action: \"提供选择 linear-scale 的统计理由；或将 factorial interaction 结论改为 inconclusive depending on scale\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R24 INFO / MINOR (3 items)\n# ============================================================\n\n- id: R24-F1\n  summary: \"2 条 orphan bibliography entries (schall-2025, tam-2024)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-F5\"}\n    - {round: 24, reviewers: [R1, R2], note: \"仍存在，两位 Reviewer 均发现。\"}\n  action_items:\n    - {round: 24, action: \"删除 2 条 orphan bib entries\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-F2\n  summary: \"Training-free vs zero-shot 术语不统一\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - {round: 24, reviewers: [R1], note: \"R1 minor。Footnote 1 承认可互换使用，但 training-free 非标准术语。\"}\n  action_items:\n    - {round: 24, action: \"统一使用 zero-shot 或在首次使用时明确定义 training-free\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-F3\n  summary: \"可选补充引用: Aly et al. (2019), Onoe & Durrett (2020)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - {round: 24, reviewers: [R1], note: \"非 critical，考虑补充。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R23 POSSIBLY RESOLVED (本轮未提及)\n# ============================================================\n\n- id: R23-W2\n  summary: \"TOST margin ±3pp 的 argument (1) 存在循环论证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"IQR-predicted Δ=2.2pp 循环\"}\n    - {round: 24, reviewers: [], note: \"本轮未被任何 Reviewer 提及。当前正文使用 (i) dimensional separability + (ii) Cohen's d 论证，循环论证可能已修复。待 Research Director 确认。\"}\n  action_items:\n    - {round: 23, action: \"删除 argument (1)，argument (2) 改纯概念论证\", assigned_to: \"Agent\", status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-W7\n  summary: \"Bootstrap CI 的 across-batch correlation 讨论不足\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"across-batch shared model/prompt 可能引入偏差\"}\n    - {round: 24, reviewers: [], note: \"本轮未被任何 Reviewer 提及。Limitations 已添加 Across-batch correlation 段落。待 Research Director 确认。\"}\n  action_items:\n    - {round: 23, action: \"Limitations 补充讨论\", assigned_to: \"Agent\", status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-F1\n  summary: \"Responsible NLP Checklist 出现在 PDF 中——格式违规\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"占 pages 9-10\"}\n    - {round: 24, reviewers: [], note: \"已修复。main.tex 中 \\\\input{checklist} 已注释，附注 EMNLP 2026 要求在 OpenReview form 中填写。\"}\n  action_items: []\n  resolution: \"Checklist section 已从 PDF 移除\"\n  resolution_round: 24\n\n- id: R23-F3\n  summary: \"Multiple comparisons 不做 correction 的理由不充分\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"datasets 共享 knowledge base\"}\n    - {round: 24, reviewers: [], note: \"本轮未被任何 Reviewer 提及。Limitations 已添加 Multiple comparisons 段落，讨论 dataset independence (Wikipedia/Wikidata 重叠)、converging evidence framing、p<0.001 threshold。待 Research Director 确认。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-MR1\n  summary: \"Robinson (1950) ecological correlation 应在正文引用\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"已在 Appendix N 引用，需移到正文 §4.3\"}\n    - {round: 24, reviewers: [], note: \"已修复。Section 4.2 正文引用 Robinson (1950)。\"}\n  action_items: []\n  resolution: \"Robinson (1950) 已在正文 §4.2 引用\"\n  resolution_round: 24\n\n# ============================================================\n# R22 以前 RESOLVED（精简保留）\n# ============================================================\n\n- id: R22-C1\n  summary: \"Title/Abstract scope overclaim\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 22\n  resolution: \"v12 Abstract 重写完成。\"\n  resolution_round: 22\n\n- id: R22-C2\n  summary: \"SCS/BCS novelty 不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 22\n  resolution: \"v12 Intro/Discussion 强化 non-obvious findings。\"\n  resolution_round: 22\n\n- id: R22-C3\n  summary: \"TOST ±3pp margin 循环论证 + logit-scale inconclusive\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 22\n  resolution: \"v12 TOST margin 重构。\"\n  resolution_round: 22\n\n- id: R22-C4\n  summary: \"页数违规\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"v12 Conclusion 并入 Discussion。\"\n  resolution_round: 22\n\n- id: R22-W1\n  summary: \"无有效 mitigation\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 22\n  resolution: \"v12 SDGD 失败分析深化。\"\n  resolution_round: 22\n\n- id: R22-W2\n  summary: \"单种子+FP8 噪声→CI 未含模型级方差\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"v12 corrected bootstrap CI。\"\n  resolution_round: 22\n\n- id: R22-W3\n  summary: \"Dim2 cross-model 验证不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 22\n  resolution: \"v12 升级至 4 模型家族。\"\n  resolution_round: 22\n\n- id: R22-W4\n  summary: \"Unconstrained decoding ablation 结论过强\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"v12 paired experiment。\"\n  resolution_round: 22\n\n- id: R22-W5\n  summary: \"DocRED range-matching power 不足\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"v12 DocRED power analysis。\"\n  resolution_round: 22\n\n- id: R22-W6\n  summary: \"Pair-to-batch R² 放大 simulation 独立性假设\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"v12 Appendix 加非独立性讨论。\"\n  resolution_round: 22\n\n- id: R22-W7\n  summary: \"Type definitions 分析应提升至正文\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"v12 §6 加 definitions 发现。\"\n  resolution_round: 22"
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
    "issues_yaml": "# Review Issues Tracker\n# Updated: 2026-05-21 (Round 24 — Fresh review, report synthesis)\n\n# ============================================================\n# R24 MUST-FIX (Consensus from R1+R2, 5 items)\n# ============================================================\n\n- id: R24-C1\n  summary: \"DocRED R²=58% 受 centrality 严重混淆 (VIF=50.9)，不应作为核心 claim\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-C2: VIF=50.9 标准误膨胀 ~7.1x\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R1-N1 Must-Fix, R2 AGREE。BCS-centrality r=0.99, 偏相关无法归因 confusability vs centrality。FewRel R²=22% (VIF=1.16) 是唯一 clean estimate。Abstract '22-58%' 误导。\"}\n  action_items:\n    - {round: 23, action: \"重写 DocRED 偏相关段\", assigned_to: \"Agent\", status: in_progress}\n    - {round: 24, action: \"Abstract/正文将 DocRED R² 标注为 confounded by centrality，以 FewRel R²=22% 为主要 claim；或做 centrality-residualized BCS 回归\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-C2\n  summary: \"Gemini 跨模型验证受单一 leverage point 驱动 (leave-one-out 后 p=0.64)\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-W4: 分歧保留，R2 降为 Should-Fix\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R1-N2 Must-Fix, R2 AGREE（BCS dimension fragile, count dimension OK）。Leave-one-out 删除 BCS=0.197 outlier 后 r 从 -0.480 降至 -0.18。正文未披露。升级为 Must-Fix 共识。\"}\n  action_items:\n    - {round: 23, action: \"报告 leave-one-out sensitivity\", assigned_to: \"Agent\", status: in_progress}\n    - {round: 24, action: \"正文 §4.3 披露 Gemini leverage point，描述为 directionally consistent but statistically fragile；考虑增加 Gemini batches\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-C3\n  summary: \"Ecological correlation caveat 不够显著，batch-level R² 可能被读者误读为个体级强效应\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-W3: pair-to-batch 15× 放大是 aggregation smoothing\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R1-N3 Must-Fix, R2 AGREE（与 R2-W3 独立重合）。Pair r²≈1.3-5.2% → batch R²=22-58% 是 ecological aggregation 数学必然。Abstract/Conclusion 未注明 ecological 属性。升级为 Must-Fix 共识。\"}\n  action_items:\n    - {round: 23, action: \"§4.3 加 ecological correlation caveat + Robinson (1950) 正文引用\", assigned_to: \"Agent\", status: in_progress}\n    - {round: 24, action: \"Abstract 加注 at the ecological (batch-aggregate) level；§4.3 添加专门讨论段，引用 Appendix N simulation\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-C4\n  summary: \"SCS/BCS 指标新颖性不足，贡献定位模糊——需明确区分 methodology vs metric contribution\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-W1: SCS = LLM-PEE criterion 形式一致\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R2-N1 Must-Fix, R1 AGREE。SCS 是标准 embedding cosine similarity，继承自 LLM-PEE。Name-only vs name+def 无差异 (Appendix M) 进一步说明 SCS 操作化粗糙。真正贡献在实验方法论 (BCS-controlled batch design)，但 Abstract/Contributions 包装为 metric 贡献。升级为 Must-Fix 共识。\"}\n  action_items:\n    - {round: 23, action: \"§2 Related Work 加 explicit novelty positioning\", assigned_to: \"Agent\", status: in_progress}\n    - {round: 24, action: \"重写 Contributions 区分 methodology contribution (BCS-controlled batch design) vs metric (SCS inherits LLM-PEE)；Abstract 措辞降低 SCS 独立贡献暗示\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-C5\n  summary: \"NER null 叙述内部张力——structural barrier 与 insufficient power 两种解释不兼容\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-C3: §5/§6 的 structural barrier 与 power=65% 矛盾\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R2-N2 Must-Fix, R1 AGREE。structural barrier (IntraSub 56-93%, errors scatter) 暗示 genuine null，但 power=65% 暗示 possible false negative。Abstract 'confirmed on three models' 措辞传达确定性。两种解释不可同时成立。\"}\n  action_items:\n    - {round: 23, action: \"双层解释 + Abstract 加 NER null qualifier\", assigned_to: \"Agent\", status: in_progress}\n    - {round: 24, action: \"明确采取一种立场或将两种作为 competing hypotheses 呈现；Abstract 避免暗示确定性结论\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R24 SHOULD-FIX (Consensus, 7 items)\n# ============================================================\n\n- id: R24-W1\n  summary: \"DocRED 每 count level 仅 5 batches，R² 估计存在小样本正偏\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-W6: n=5 per level 偏低\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R1-W1, R2 AGREE。N=5 + VIF=50.9 组合使 DocRED 偏相关分析几乎无统计效力。\"}\n  action_items:\n    - {round: 24, action: \"明确报告 DocRED 有效样本量和 R² 估计精度限制\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-W2\n  summary: \"多项核心分析缺乏跨模型验证 (DocRED R², error taxonomy, SDGD, TOST 均仅 Qwen3-32B)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-C4: DocRED R²=58% 缺乏跨模型支持\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R1-W3 + R2-W4 独立重合。Conclusion 中 'replicated across four models' 掩盖了仅 count direction + FewRel BCS direction 被跨模型验证的事实。\"}\n  action_items:\n    - {round: 24, action: \"Conclusion 措辞精确化跨模型验证范围；至少对 LLaMA-70B 复现 DocRED BCS-controlled\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-W3\n  summary: \"BCS-controlled batch 的 greedy 构建引入语义域系统偏差\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - {round: 24, reviewers: [R1, R2], note: \"R1-W4 新发现, R2 AGREE。High-BCS batches 语义域覆盖更窄（Tables 26-27），可能因 domain-specific 特征而更难，非纯 embedding confusion。论文未讨论。\"}\n  action_items:\n    - {round: 24, action: \"分析 extreme batches 语义域覆盖度差异；Discussion 讨论此 confound；考虑同域内 BCS-controlled 实验\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-W4\n  summary: \"单种子 + FP8 quantization non-determinism (residual SD=0.88pp, 占 BCS effect 18-44%)\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-F4: Residual SD=0.88pp\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R1-W5, R2 AGREE。DocRED (N=5) 下单次运行有不可忽略随机波动。\"}\n  action_items:\n    - {round: 24, action: \"至少对 key results (DocRED, MAVEN) 运行 3 seeds 并报告 cross-seed variance\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-W5\n  summary: \"Abstract 信息过载，数字密度过高影响首次阅读理解\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-F2: §4.1-4.3 每段 10+ 统计值\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R2-W1, R1 AGREE (写作风格问题，非方法学问题)。\"}\n  action_items:\n    - {round: 24, action: \"Abstract 精简数字，保留 headline numbers\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-W6\n  summary: \"Sections 5-6 过度压缩 (Schema Decomposition 仅半 column)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-W5: §4.5 留正文但压缩\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R2-W2, R1 AGREE。三大贡献之一却只有半 column。建议压缩 §2 Related Work 腾出空间。\"}\n  action_items:\n    - {round: 24, action: \"Section 5 扩展到至少一个完整 column\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-W7\n  summary: \"BCS clean validation 实际仅限 FewRel 1 个数据集 (DocRED confounded, MAVEN confounded, NER null)\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - {round: 24, reviewers: [R1, R2], note: \"R1 交叉回应升级 R2-W5。FewRel R²=22% (VIF=1.16) 是唯一 clean verification。DocRED VIF=50.9, MAVEN centrality confound, NER null。R2 原评估为 2 个 RE 数据集，R1 认为实际仅 1 个。分歧保留。\"}\n  action_items:\n    - {round: 24, action: \"明确论文可靠结论范围：FewRel R²≈22%, ecological level, open-weight models\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R24 DIVERGENCE (1 item)\n# ============================================================\n\n- id: R24-D1\n  summary: \"TOST 量表敏感性 (linear p=0.003 vs logit p=0.209)\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-C1: Logit-scale inconclusive\"}\n    - {round: 24, reviewers: [R1, R2], note: \"R1-W2 Should-Fix vs R2 REBUT (accuracy 0.70-0.92 远离边界, linear defensible; 核心 claim 不依赖 TOST)。分歧保留。相比 R23 从 critical 降级为 divergent warning。\"}\n  action_items:\n    - {round: 24, action: \"提供选择 linear-scale 的统计理由；或将 factorial interaction 结论改为 inconclusive depending on scale\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R24 INFO / MINOR (3 items)\n# ============================================================\n\n- id: R24-F1\n  summary: \"2 条 orphan bibliography entries (schall-2025, tam-2024)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"R23-F5\"}\n    - {round: 24, reviewers: [R1, R2], note: \"仍存在，两位 Reviewer 均发现。\"}\n  action_items:\n    - {round: 24, action: \"删除 2 条 orphan bib entries\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-F2\n  summary: \"Training-free vs zero-shot 术语不统一\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - {round: 24, reviewers: [R1], note: \"R1 minor。Footnote 1 承认可互换使用，但 training-free 非标准术语。\"}\n  action_items:\n    - {round: 24, action: \"统一使用 zero-shot 或在首次使用时明确定义 training-free\", assigned_to: \"\", status: open}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R24-F3\n  summary: \"可选补充引用: Aly et al. (2019), Onoe & Durrett (2020)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 24\n  last_seen_round: 24\n  mentions:\n    - {round: 24, reviewers: [R1], note: \"非 critical，考虑补充。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n# ============================================================\n# R23 POSSIBLY RESOLVED (本轮未提及)\n# ============================================================\n\n- id: R23-W2\n  summary: \"TOST margin ±3pp 的 argument (1) 存在循环论证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"IQR-predicted Δ=2.2pp 循环\"}\n    - {round: 24, reviewers: [], note: \"本轮未被任何 Reviewer 提及。当前正文使用 (i) dimensional separability + (ii) Cohen's d 论证，循环论证可能已修复。待 Research Director 确认。\"}\n  action_items:\n    - {round: 23, action: \"删除 argument (1)，argument (2) 改纯概念论证\", assigned_to: \"Agent\", status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-W7\n  summary: \"Bootstrap CI 的 across-batch correlation 讨论不足\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"across-batch shared model/prompt 可能引入偏差\"}\n    - {round: 24, reviewers: [], note: \"本轮未被任何 Reviewer 提及。Limitations 已添加 Across-batch correlation 段落。待 Research Director 确认。\"}\n  action_items:\n    - {round: 23, action: \"Limitations 补充讨论\", assigned_to: \"Agent\", status: in_progress}\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-F1\n  summary: \"Responsible NLP Checklist 出现在 PDF 中——格式违规\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"占 pages 9-10\"}\n    - {round: 24, reviewers: [], note: \"已修复。main.tex 中 \\\\input{checklist} 已注释，附注 EMNLP 2026 要求在 OpenReview form 中填写。\"}\n  action_items: []\n  resolution: \"Checklist section 已从 PDF 移除\"\n  resolution_round: 24\n\n- id: R23-F3\n  summary: \"Multiple comparisons 不做 correction 的理由不充分\"\n  category: method\n  severity: info\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"datasets 共享 knowledge base\"}\n    - {round: 24, reviewers: [], note: \"本轮未被任何 Reviewer 提及。Limitations 已添加 Multiple comparisons 段落，讨论 dataset independence (Wikipedia/Wikidata 重叠)、converging evidence framing、p<0.001 threshold。待 Research Director 确认。\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: R23-MR1\n  summary: \"Robinson (1950) ecological correlation 应在正文引用\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 24\n  mentions:\n    - {round: 23, reviewers: [R1, R2], note: \"已在 Appendix N 引用，需移到正文 §4.3\"}\n    - {round: 24, reviewers: [], note: \"已修复。Section 4.2 正文引用 Robinson (1950)。\"}\n  action_items: []\n  resolution: \"Robinson (1950) 已在正文 §4.2 引用\"\n  resolution_round: 24\n\n# ============================================================\n# R22 以前 RESOLVED（精简保留）\n# ============================================================\n\n- id: R22-C1\n  summary: \"Title/Abstract scope overclaim\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 22\n  resolution: \"v12 Abstract 重写完成。\"\n  resolution_round: 22\n\n- id: R22-C2\n  summary: \"SCS/BCS novelty 不足\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 22\n  resolution: \"v12 Intro/Discussion 强化 non-obvious findings。\"\n  resolution_round: 22\n\n- id: R22-C3\n  summary: \"TOST ±3pp margin 循环论证 + logit-scale inconclusive\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 22\n  resolution: \"v12 TOST margin 重构。\"\n  resolution_round: 22\n\n- id: R22-C4\n  summary: \"页数违规\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"v12 Conclusion 并入 Discussion。\"\n  resolution_round: 22\n\n- id: R22-W1\n  summary: \"无有效 mitigation\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 22\n  resolution: \"v12 SDGD 失败分析深化。\"\n  resolution_round: 22\n\n- id: R22-W2\n  summary: \"单种子+FP8 噪声→CI 未含模型级方差\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"v12 corrected bootstrap CI。\"\n  resolution_round: 22\n\n- id: R22-W3\n  summary: \"Dim2 cross-model 验证不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 22\n  resolution: \"v12 升级至 4 模型家族。\"\n  resolution_round: 22\n\n- id: R22-W4\n  summary: \"Unconstrained decoding ablation 结论过强\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"v12 paired experiment。\"\n  resolution_round: 22\n\n- id: R22-W5\n  summary: \"DocRED range-matching power 不足\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"v12 DocRED power analysis。\"\n  resolution_round: 22\n\n- id: R22-W6\n  summary: \"Pair-to-batch R² 放大 simulation 独立性假设\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"v12 Appendix 加非独立性讨论。\"\n  resolution_round: 22\n\n- id: R22-W7\n  summary: \"Type definitions 分析应提升至正文\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"v12 §6 加 definitions 发现。\"\n  resolution_round: 22"
  }
}
```

</details>

---


### Tool result

_source line 2705 · 2026-05-21T19:06:12.378021+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/review_issues.yaml\", \"bytes\": 15999}, \"error\": \"\"}"}

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

_source line 2706 · 2026-05-21T19:08:52.377112+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "schema-dag-extraction",
  "report": "# 审稿报告 — Round 24 (Fresh Review)\n\n**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n**Venue**: EMNLP 2026 (ARR May 2026 cycle), Long Paper\n**Reviewers**: R1 (方法严谨性, 3.5 Borderline Conference), R2 (新颖性与完整性, 3.0 Findings)\n**审稿模式**: Fresh (无上轮记忆)\n\n---\n\n## Summary\n\n本文研究 schema 复杂度（type count + inter-type confusability）如何预测 training-free LLM 信息抽取的性能退化。作者提出 Schema Confusability Score (SCS) 及其 batch 聚合 Batch Confusability Score (BCS)，通过 count curves 和 BCS-controlled extreme batch 实验，在 4 个数据集（Few-NERD/FewRel/DocRED/MAVEN）上验证了两个退化维度：count-related recall decline 和 confusability-related type substitution。核心发现：BCS 解释 22–58% 的跨 batch RE 准确率方差（但 58% 受 centrality 严重混淆），NER batch-level BCS 信号为 null，schema 分解（SDGD）因 merge amplification 失败。跨模型验证覆盖 4 个模型家族（Qwen3-32B, LLaMA-8B/70B, Gemini 2.5 Flash）。\n\n---\n\n## Strengths\n\n1. **研究问题重要且定义清晰**：首个在 training-free LLM IE 中系统隔离 type confusability 与 type count 效应的控制研究，填补了现有工作仅讨论 schema 规模但忽略 inter-type confusability 的空白。[R1, R2 共识]\n\n2. **实验设计精细**：Count curves + BCS-controlled extreme batches 的双重设计互相补充。FewRel 的 balanced design (700 instances/type) 有效控制了 type frequency 混淆。[R1, R2 共识]\n\n3. **统计方法学透明度罕见**：报告了 VIF、ecological correlation caveat (Robinson 1950)、TOST 等价检验、功效分析、variance decomposition。这种自我批判风格在 NLP 论文中少见。[R1]\n\n4. **诚实报告负面结果**：NER batch-level BCS null（3 个模型确认）、SDGD decomposition failure（merge amplification）——这些负面结果本身是有价值的社区贡献。[R1, R2 共识]\n\n5. **14 页深度 Appendix**：覆盖 factorial analysis、centrality confound control、power analysis、batch aggregation simulation、split-origin analysis、prompt sensitivity、variance decomposition 等，展现严谨的 robustness checking。[R1, R2 共识]\n\n6. **跨模型验证方向一致**：Count decline 在 4 个模型家族上均呈单调下降，BCS 效应方向在 FewRel 上跨 5 个模型一致。[R1]\n\n7. **格式完全合规**：ACL template [review]、8 页正文、Limitations 合规、匿名化完整、Checklist 正确放在 OpenReview form。[R2]\n\n8. **引用无虚假**：72 条 bib entries，59/72 在线验证通过，无 fabricated citations。[R2]\n\n---\n\n## Weaknesses\n\n### Must-Fix (5 items, 全部为 R1+R2 共识)\n\n**C1. DocRED R²=58% 受 centrality 严重混淆，不应作为核心 claim** [R1-N1, R2 AGREE]\n\nTable 11 显示 DocRED 上 BCS 与 degree centrality 的 VIF=50.9，两变量 r=0.99。偏相关虽然显著，但无法归因于 confusability 而非 centrality。Abstract 和 Section 4.3 突出报道 \"22–58%\"，读者自然将 58% 视为 confusability 解释力——这是误导性的。FewRel R²=22% (VIF=1.16) 是唯一可靠的效应量估计。\n\n→ **要求**：Abstract/正文将 DocRED R² 标注为 confounded by centrality，以 FewRel R²=22% 为主要 claim；或做 centrality-residualized BCS 回归报告残差 R²。\n\n**C2. Gemini 跨模型验证受单一 leverage point 驱动** [R1-N2, R2 AGREE]\n\nGemini count-16 的 BCS-accuracy 相关受一个 high-BCS outlier 驱动。Leave-one-out 删除该点后，r 从 −0.480 降至 −0.18 (p=0.64)，相关完全不显著。但 Section 4.3 正文声称 Gemini 结果 \"replicates on a proprietary architecture\"，未披露此 leverage point。论文的 \"4 model families\" 跨模型验证是关键 selling point，Gemini 验证的 fragility 显著削弱普适性声明。R2 补充：count dimension 方向一致性不受影响，仅 BCS dimension 受影响。\n\n→ **要求**：正文 §4.3 披露 Gemini leverage point，描述为 \"directionally consistent but statistically fragile\"。\n\n**C3. Ecological correlation caveat 需要更显著的 framing** [R1-N3, R2-W3 独立重合]\n\nPair-level r² ≈ 1.3–5.2% 但 batch-level R² = 22–58%，~10–40× 放大是 ecological aggregation 的数学必然（Appendix N simulation 已证实）。然而 Abstract 和 Conclusion 使用 \"BCS explains 22–58%\" 而未注明 ecological 属性。NLP 社区多数读者不了解 ecological correlation，会将 R² 误读为个体级强效应。\n\n→ **要求**：Abstract 加注 \"at the ecological (batch-aggregate) level\"；Section 4.3 添加专门讨论段，引用 Appendix N simulation 说明 pair-level 如何通过聚合产生 batch-level R²。\n\n**C4. SCS/BCS 指标新颖性不足，贡献定位模糊** [R2-N1, R1 AGREE]\n\nSCS 本质是 `cos(embed(name_i), embed(name_j))`，是标准 embedding cosine similarity，继承自 LLM-PEE (Liu et al., 2025)。Appendix M 显示 name-only 与 name+definition SCS 无差异，进一步说明 SCS 仅捕获表面名称重叠而非深层概念混淆。论文真正贡献在实验方法论（BCS-controlled batch design），但 Abstract 和 Contributions 的措辞将 SCS 包装为独立贡献。\n\n→ **要求**：重写 Contributions 明确区分 methodology contribution (BCS-controlled experimental framework) vs. metric (SCS inherits LLM-PEE)；Abstract 降低 SCS 独立贡献暗示。\n\n**C5. NER null 叙述内部张力** [R2-N2, R1 AGREE]\n\n论文同时给出两种不兼容解释：(1) \"structural barrier\" — NER 错误分散于 miss/boundary/type (IntraSub 56–93%)，BCS 根本无法预测，暗示 genuine null；(2) \"insufficient power\" — BCS SD=0.027，65% power，暗示 possible false negative。两种解释不可同时成立。Abstract \"NER batch-level confusability signal remains nonexistent\" 中 \"nonexistent\" 传达确定性，但 Appendix E.2 承认功效不足。\n\n→ **要求**：明确采取一种立场，或将两种作为 competing hypotheses 呈现并讨论如何区分；Abstract 避免暗示确定性结论。\n\n### Should-Fix (7 items)\n\n**W1. DocRED 每 count level 仅 5 batches，R² 估计存在小样本正偏** [R1-W1, R2 AGREE]\nN=5 + VIF=50.9 组合使 DocRED 偏相关分析几乎无统计效力。建议增加 batches 或降低 DocRED R² 强调。\n\n**W2. 多项核心分析缺乏跨模型验证** [R1-W3, R2-W4 独立重合]\nDocRED R²=58%、error taxonomy、SDGD failure、TOST factorial 均仅 Qwen3-32B。Conclusion 中 \"replicated across four models\" 掩盖了实际验证范围。至少对 LLaMA-70B 复现 DocRED BCS-controlled。\n\n**W3. BCS-controlled batch 的 greedy 构建引入语义域系统偏差** [R1-W4, R2 AGREE]\nHigh-BCS batches 类型来自同一语义域（Tables 26-27），语义域覆盖更窄。窄域 batch 可能因 domain-specific 特征而更难，非纯 embedding confusion。论文未讨论。建议分析语义域覆盖差异或增加域内 BCS-controlled 实验。\n\n**W4. 单种子 + FP8 non-determinism** [R1-W5, R2 AGREE]\nResidual SD=0.88pp 占 BCS effect size 18–44%。DocRED (N=5) 下单次运行有不可忽略随机波动。建议对 key results 运行 3 seeds。\n\n**W5. Abstract 信息过载** [R2-W1, R1 AGREE]\nAbstract 数字密度过高（r², R², pp decline 等），影响首次阅读理解。建议精简保留 headline numbers。\n\n**W6. Sections 5-6 过度压缩** [R2-W2, R1 AGREE]\nSchema Decomposition (Section 5) 是三大贡献之一却仅半 column。建议压缩 §2 Related Work（当前约 1.3 页，部分与 Intro 重复）腾出空间扩展。\n\n**W7. BCS clean validation 实际仅限 FewRel 1 个数据集** [R1 交叉升级 R2-W5，分歧保留]\nFewRel R²=22% (VIF=1.16) 是唯一 clean verification。DocRED: VIF=50.9；MAVEN: centrality confound；NER: null。R2 原评估 2 个 RE 数据集，R1 认为仅 1 个。可靠结论应收紧至 \"FewRel R²≈22%, ecological level, open-weight models\"。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键问题上完全一致：\n\n1. **DocRED R²=58% 不可信**：VIF=50.9 使 BCS vs centrality 不可分离，论文最引人注目的定量 claim 需要大幅降调 [C1]\n2. **Gemini 验证 fragile**：BCS dimension 依赖单一 leverage point，\"4 model families\" 验证实际在 BCS dimension 上只有 3 个开源家族可靠 [C2]\n3. **Ecological amplification 需显著 caveat**：pair-level r²≈1-5% → batch R²=22% 是聚合的数学必然，非 confusability 的强预测力 [C3]\n4. **SCS 非独立贡献**：继承自 LLM-PEE，论文真正贡献在实验方法论 [C4]\n5. **NER null 叙述自相矛盾**：structural barrier vs insufficient power 不兼容 [C5]\n6. **跨模型验证深度不均**：核心量化分析均为 Qwen3-32B 单模型 [W2]\n7. **实验设计精细**：BCS-controlled batch design 是有价值的方法论贡献 [Strength]\n8. **负面结果有价值**：NER null + SDGD failure 对社区有启发性 [Strength]\n9. **格式完全合规**：无违规 [Strength]\n\n## Reviewer Divergence [REBUT]\n\n1. **TOST 量表敏感性** — R1 认为 Should-Fix（logit-scale 对 bounded data 更合适），R2 认为 accuracy 0.70-0.92 远离边界，linear defensible，且核心 claim 不依赖 TOST。**Director 判断**：保留分歧，列为 divergent warning (R24-D1)。\n\n2. **BCS 可靠验证数据集数量** — R1 认为仅 FewRel 1 个 clean（DocRED confounded），R2 认为 RE 2 个数据集。**Director 判断**：R1 论证更有力（VIF=50.9 确实使 DocRED 不可信），但 DocRED 的方向一致性仍有参考价值，不宜完全否定。\n\n3. **Excitement 维度** — R1 给 3.5（实验方法论 + 负面结果有社区价值），R2 给 2.5（SCS metric 缺乏新意限制 excitement）。**Director 判断**：R1 观点更合理——简单 metric + 精细实验设计 本身是有效贡献模式。Excitement 综合 3.0。\n\n---\n\n## Questions\n\n1. **DocRED centrality-residualized BCS**：能否先对 centrality 回归取 BCS 残差，再报告残差 R²？这能更清楚隔离 confusability 独立贡献。[R1]\n2. **Gemini batches 扩展**：能否增加 Gemini count-16 BCS-controlled batches（25→50），检验 leverage point 是否采样偏差？[R1]\n3. **TOST 量表选择文献**：是否有方法学文献支持 accuracy ∈ [0,1] 上使用 linear-scale TOST？[R1]\n4. **NER null 机制**：NER 是 span-level 任务（局部特征更重要），RE 是 sentence/document-level 任务（全局 schema 推理更重要）——这是否是 task asymmetry 的根本原因？[R1]\n5. **域内 BCS-controlled**：是否测试过同一语义域内构建 high/low BCS batches 以排除 domain bias？[R1]\n\n---\n\n## Missing References\n\n两位 Reviewer 均未发现严重遗漏。Related work 覆盖充分。\n\n可选补充：\n- Aly et al. (2019) \"Hierarchical Multi-Task Learning for Fine-Grained Entity Typing\"\n- Onoe & Durrett (2020) \"Fine-Grained Entity Typing for Domain Independent Entity Linking\"\n- R23 遗留可选：Ren et al. (2016) AFET, Choi et al. (2018) Ultra-Fine Entity Typing, Min et al. (2022) Rethinking Demonstrations\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**：pending（已请求，尚未返回）。请求时间：2026-05-21T18:49:05Z，将在 8 小时后自动提醒用户。\n\n内部审稿不等待外部结果。如外部审稿返回后发现与内部审稿的重大差异，Research Director 可酌情追加评估。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：done（2026-05-21T18:49:04 → 18:52:37，耗时约 3.5 分钟）\n\n### Warnings (3)\n\n1. **Pages 1-3 连续纯文本**：Title/Abstract/Intro/Related Work 共 3 页无任何 display item。审稿人需翻过 3 页才看到第一个视觉锚点（Table 1, p4）。建议在 p1 或 p2 加入概览图（如 SCS 概念示意 / 核心发现预览图）。\n\n2. **正文 display items 偏少**：8 页正文仅 4 个 display items（Table 1-2, Figure 1-2），对实证论文偏少（通常 5-8 个）。核心定量结果分散在文字中，缺少汇总 main results 表。\n\n3. **Pages 8-9 连续纯文本**：Section 5 + Section 6 + Limitations 连续 2 页无 display item。Section 5 的 decomposition failure 适合用一张小表或示意图辅助。\n\n### Info (13) — 摘要\n- Table 1-2, Figure 1-2 排版整洁，booktabs 风格，配色色盲友好\n- Figure 1 左面板两条线在高 count 端区分度低\n- Figure 2 panel (a) legend 与数据线有轻微重叠\n- Appendix 14 页含 27 张表但 0 张 figure\n- Prompt templates 排版清晰\n- SCS 公式渲染正确\n- 匿名标记正确\n\n---\n\n## Overall Assessment\n\n**综合评分：3.0 (Findings)**\n**置信度：4/5**\n\n### 评分理由\n\n**可接收为 Findings 的理由：**\n- 研究问题重要且实验设计精细（BCS-controlled batch design 是有价值的方法论范式）\n- FewRel 上 BCS R²=22%（ecological level, VIF=1.16）是可信的效应量\n- 负面结果（NER null, SDGD failure）对社区有明确的警示价值\n- 14 页 Appendix 展现了罕见的统计透明度\n- 格式完全合规，引用无虚假\n\n**不足以进入 Conference (4.0) 的理由：**\n- **核心定量 claim 过度宣称**：最引人注目的 R²=58% 本质上不可解释（centrality vs. confusability）；跨模型验证在 Gemini 上由单一 leverage point 支撑\n- **SCS/BCS 指标新颖性有限**：继承自 LLM-PEE 的标准 embedding cosine similarity，Appendix M 证实 definitions 无额外贡献\n- **可靠结论范围窄于呈现**：严格而言仅 FewRel 1 个数据集提供 clean BCS validation，且为 ecological level R²=22%\n- **NER null 叙述自相矛盾**：structural barrier vs insufficient power 两种解释不兼容\n- **核心分析缺乏跨模型验证**：DocRED R², error taxonomy, SDGD, TOST factorial 均为 Qwen3-32B 单模型\n\n### 达到 Conference (3.5-4.0) 的路径\n\n如果作者在 revision 中：\n1. 将 DocRED R² 标注为 confounded，以 FewRel R²=22% 为主要 claim\n2. 正文披露 Gemini leverage point\n3. 加强 ecological correlation caveat（Abstract + 正文专门讨论段）\n4. 重新 frame SCS 贡献为 methodology vs metric\n5. 统一 NER null 叙述\n6. 至少对 LLaMA-70B 复现一项核心分析\n\n则有望达到 3.5 (Borderline Conference)。进一步达到 4.0 需要新增实验数据（centrality-residualized R², 更多 Gemini batches, 域内 BCS-controlled）。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- RQ1-RQ3 定义清晰，但 \"first controlled study\" claim 需要更精确的 scoping（LLM-PEE 已做 schema partitioning，本文的控制研究是 analytical 而非 engineering）\n- Contributions 第 1 条将 SCS/BCS 与实验方法混为一谈，建议拆分\n\n### Section 2 (Related Work)\n- 覆盖充分，约 1.3 页\n- \"SCS novelty\" 段 (lines 220-233) 已尝试区分与 LLM-PEE，但措辞仍模糊——\"our contribution is the controlled experimental methodology\" 应提升到更显著位置\n- 可适当压缩以为 Section 5 腾空间\n\n### Section 3 (Experimental Setup)\n- BCS-controlled batch 的 greedy 构建方法（Section 3.3）未讨论语义域偏差\n- Table 1 数据集统计清晰\n- SCS 定义（Section 3.2）技术上正确但应更明确承认与 LLM-PEE 的关系\n\n### Section 4 (Results)\n- §4.1 Count curves：方向性发现稳健，跨模型一致\n- §4.2 Pairwise SCS：效应量极小 (r²≈1-5%)，已适当报告\n- §4.3 BCS-Controlled：核心结果章节。DocRED R²=58% 的 centrality confound 讨论不足（仅在 footnote 4 中一笔带过）；ecological amplification caveat 不够显著；Gemini leverage point 未在正文披露\n- §4.4 Multi-Dimensional Degradation：error taxonomy 分析有洞察力（IntraSub vs ExtraSub 分布差异），但仅 Qwen3-32B\n- §4.5 Centrality Confound：诚实的分析，MAVEN 的 centrality 问题处理得当\n\n### Section 5 (Schema Decomposition)\n- 三大贡献之一，空间严重不足（半 column）\n- NER merge amplification 和 RE routing failure 的双重失败机制是有价值的发现\n- 建议用 Table 或 Figure 辅助叙述\n\n### Section 6 (Discussion and Conclusion)\n- \"BCS enables pre-hoc diagnostics\" 是合理的实用价值定位\n- \"replicated across four models\" 措辞过强，应精确化为 \"count direction replicated on four models; BCS effect replicated on three open-weight families\"\n\n### Limitations\n- 6 点覆盖全面（model coverage, effect size, task scope, causal mechanism, contamination, domain scope）\n- Across-batch correlation 和 Multiple comparisons 两段补充得当\n- NER null 的 power=65% 应在此更明确讨论其与正文 structural barrier 解释的张力\n\n### Appendix\n- 14 页 27 表，robustness 极其充分\n- Appendix N (ecological simulation) 是关键证据，应在正文更显著地引用\n- Appendix R (variance decomposition) 量化了 FP8 non-determinism，有价值但未在正文充分讨论影响",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
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
    "report": "# 审稿报告 — Round 24 (Fresh Review)\n\n**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?\n**Venue**: EMNLP 2026 (ARR May 2026 cycle), Long Paper\n**Reviewers**: R1 (方法严谨性, 3.5 Borderline Conference), R2 (新颖性与完整性, 3.0 Findings)\n**审稿模式**: Fresh (无上轮记忆)\n\n---\n\n## Summary\n\n本文研究 schema 复杂度（type count + inter-type confusability）如何预测 training-free LLM 信息抽取的性能退化。作者提出 Schema Confusability Score (SCS) 及其 batch 聚合 Batch Confusability Score (BCS)，通过 count curves 和 BCS-controlled extreme batch 实验，在 4 个数据集（Few-NERD/FewRel/DocRED/MAVEN）上验证了两个退化维度：count-related recall decline 和 confusability-related type substitution。核心发现：BCS 解释 22–58% 的跨 batch RE 准确率方差（但 58% 受 centrality 严重混淆），NER batch-level BCS 信号为 null，schema 分解（SDGD）因 merge amplification 失败。跨模型验证覆盖 4 个模型家族（Qwen3-32B, LLaMA-8B/70B, Gemini 2.5 Flash）。\n\n---\n\n## Strengths\n\n1. **研究问题重要且定义清晰**：首个在 training-free LLM IE 中系统隔离 type confusability 与 type count 效应的控制研究，填补了现有工作仅讨论 schema 规模但忽略 inter-type confusability 的空白。[R1, R2 共识]\n\n2. **实验设计精细**：Count curves + BCS-controlled extreme batches 的双重设计互相补充。FewRel 的 balanced design (700 instances/type) 有效控制了 type frequency 混淆。[R1, R2 共识]\n\n3. **统计方法学透明度罕见**：报告了 VIF、ecological correlation caveat (Robinson 1950)、TOST 等价检验、功效分析、variance decomposition。这种自我批判风格在 NLP 论文中少见。[R1]\n\n4. **诚实报告负面结果**：NER batch-level BCS null（3 个模型确认）、SDGD decomposition failure（merge amplification）——这些负面结果本身是有价值的社区贡献。[R1, R2 共识]\n\n5. **14 页深度 Appendix**：覆盖 factorial analysis、centrality confound control、power analysis、batch aggregation simulation、split-origin analysis、prompt sensitivity、variance decomposition 等，展现严谨的 robustness checking。[R1, R2 共识]\n\n6. **跨模型验证方向一致**：Count decline 在 4 个模型家族上均呈单调下降，BCS 效应方向在 FewRel 上跨 5 个模型一致。[R1]\n\n7. **格式完全合规**：ACL template [review]、8 页正文、Limitations 合规、匿名化完整、Checklist 正确放在 OpenReview form。[R2]\n\n8. **引用无虚假**：72 条 bib entries，59/72 在线验证通过，无 fabricated citations。[R2]\n\n---\n\n## Weaknesses\n\n### Must-Fix (5 items, 全部为 R1+R2 共识)\n\n**C1. DocRED R²=58% 受 centrality 严重混淆，不应作为核心 claim** [R1-N1, R2 AGREE]\n\nTable 11 显示 DocRED 上 BCS 与 degree centrality 的 VIF=50.9，两变量 r=0.99。偏相关虽然显著，但无法归因于 confusability 而非 centrality。Abstract 和 Section 4.3 突出报道 \"22–58%\"，读者自然将 58% 视为 confusability 解释力——这是误导性的。FewRel R²=22% (VIF=1.16) 是唯一可靠的效应量估计。\n\n→ **要求**：Abstract/正文将 DocRED R² 标注为 confounded by centrality，以 FewRel R²=22% 为主要 claim；或做 centrality-residualized BCS 回归报告残差 R²。\n\n**C2. Gemini 跨模型验证受单一 leverage point 驱动** [R1-N2, R2 AGREE]\n\nGemini count-16 的 BCS-accuracy 相关受一个 high-BCS outlier 驱动。Leave-one-out 删除该点后，r 从 −0.480 降至 −0.18 (p=0.64)，相关完全不显著。但 Section 4.3 正文声称 Gemini 结果 \"replicates on a proprietary architecture\"，未披露此 leverage point。论文的 \"4 model families\" 跨模型验证是关键 selling point，Gemini 验证的 fragility 显著削弱普适性声明。R2 补充：count dimension 方向一致性不受影响，仅 BCS dimension 受影响。\n\n→ **要求**：正文 §4.3 披露 Gemini leverage point，描述为 \"directionally consistent but statistically fragile\"。\n\n**C3. Ecological correlation caveat 需要更显著的 framing** [R1-N3, R2-W3 独立重合]\n\nPair-level r² ≈ 1.3–5.2% 但 batch-level R² = 22–58%，~10–40× 放大是 ecological aggregation 的数学必然（Appendix N simulation 已证实）。然而 Abstract 和 Conclusion 使用 \"BCS explains 22–58%\" 而未注明 ecological 属性。NLP 社区多数读者不了解 ecological correlation，会将 R² 误读为个体级强效应。\n\n→ **要求**：Abstract 加注 \"at the ecological (batch-aggregate) level\"；Section 4.3 添加专门讨论段，引用 Appendix N simulation 说明 pair-level 如何通过聚合产生 batch-level R²。\n\n**C4. SCS/BCS 指标新颖性不足，贡献定位模糊** [R2-N1, R1 AGREE]\n\nSCS 本质是 `cos(embed(name_i), embed(name_j))`，是标准 embedding cosine similarity，继承自 LLM-PEE (Liu et al., 2025)。Appendix M 显示 name-only 与 name+definition SCS 无差异，进一步说明 SCS 仅捕获表面名称重叠而非深层概念混淆。论文真正贡献在实验方法论（BCS-controlled batch design），但 Abstract 和 Contributions 的措辞将 SCS 包装为独立贡献。\n\n→ **要求**：重写 Contributions 明确区分 methodology contribution (BCS-controlled experimental framework) vs. metric (SCS inherits LLM-PEE)；Abstract 降低 SCS 独立贡献暗示。\n\n**C5. NER null 叙述内部张力** [R2-N2, R1 AGREE]\n\n论文同时给出两种不兼容解释：(1) \"structural barrier\" — NER 错误分散于 miss/boundary/type (IntraSub 56–93%)，BCS 根本无法预测，暗示 genuine null；(2) \"insufficient power\" — BCS SD=0.027，65% power，暗示 possible false negative。两种解释不可同时成立。Abstract \"NER batch-level confusability signal remains nonexistent\" 中 \"nonexistent\" 传达确定性，但 Appendix E.2 承认功效不足。\n\n→ **要求**：明确采取一种立场，或将两种作为 competing hypotheses 呈现并讨论如何区分；Abstract 避免暗示确定性结论。\n\n### Should-Fix (7 items)\n\n**W1. DocRED 每 count level 仅 5 batches，R² 估计存在小样本正偏** [R1-W1, R2 AGREE]\nN=5 + VIF=50.9 组合使 DocRED 偏相关分析几乎无统计效力。建议增加 batches 或降低 DocRED R² 强调。\n\n**W2. 多项核心分析缺乏跨模型验证** [R1-W3, R2-W4 独立重合]\nDocRED R²=58%、error taxonomy、SDGD failure、TOST factorial 均仅 Qwen3-32B。Conclusion 中 \"replicated across four models\" 掩盖了实际验证范围。至少对 LLaMA-70B 复现 DocRED BCS-controlled。\n\n**W3. BCS-controlled batch 的 greedy 构建引入语义域系统偏差** [R1-W4, R2 AGREE]\nHigh-BCS batches 类型来自同一语义域（Tables 26-27），语义域覆盖更窄。窄域 batch 可能因 domain-specific 特征而更难，非纯 embedding confusion。论文未讨论。建议分析语义域覆盖差异或增加域内 BCS-controlled 实验。\n\n**W4. 单种子 + FP8 non-determinism** [R1-W5, R2 AGREE]\nResidual SD=0.88pp 占 BCS effect size 18–44%。DocRED (N=5) 下单次运行有不可忽略随机波动。建议对 key results 运行 3 seeds。\n\n**W5. Abstract 信息过载** [R2-W1, R1 AGREE]\nAbstract 数字密度过高（r², R², pp decline 等），影响首次阅读理解。建议精简保留 headline numbers。\n\n**W6. Sections 5-6 过度压缩** [R2-W2, R1 AGREE]\nSchema Decomposition (Section 5) 是三大贡献之一却仅半 column。建议压缩 §2 Related Work（当前约 1.3 页，部分与 Intro 重复）腾出空间扩展。\n\n**W7. BCS clean validation 实际仅限 FewRel 1 个数据集** [R1 交叉升级 R2-W5，分歧保留]\nFewRel R²=22% (VIF=1.16) 是唯一 clean verification。DocRED: VIF=50.9；MAVEN: centrality confound；NER: null。R2 原评估 2 个 RE 数据集，R1 认为仅 1 个。可靠结论应收紧至 \"FewRel R²≈22%, ecological level, open-weight models\"。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n两位 Reviewer 在以下关键问题上完全一致：\n\n1. **DocRED R²=58% 不可信**：VIF=50.9 使 BCS vs centrality 不可分离，论文最引人注目的定量 claim 需要大幅降调 [C1]\n2. **Gemini 验证 fragile**：BCS dimension 依赖单一 leverage point，\"4 model families\" 验证实际在 BCS dimension 上只有 3 个开源家族可靠 [C2]\n3. **Ecological amplification 需显著 caveat**：pair-level r²≈1-5% → batch R²=22% 是聚合的数学必然，非 confusability 的强预测力 [C3]\n4. **SCS 非独立贡献**：继承自 LLM-PEE，论文真正贡献在实验方法论 [C4]\n5. **NER null 叙述自相矛盾**：structural barrier vs insufficient power 不兼容 [C5]\n6. **跨模型验证深度不均**：核心量化分析均为 Qwen3-32B 单模型 [W2]\n7. **实验设计精细**：BCS-controlled batch design 是有价值的方法论贡献 [Strength]\n8. **负面结果有价值**：NER null + SDGD failure 对社区有启发性 [Strength]\n9. **格式完全合规**：无违规 [Strength]\n\n## Reviewer Divergence [REBUT]\n\n1. **TOST 量表敏感性** — R1 认为 Should-Fix（logit-scale 对 bounded data 更合适），R2 认为 accuracy 0.70-0.92 远离边界，linear defensible，且核心 claim 不依赖 TOST。**Director 判断**：保留分歧，列为 divergent warning (R24-D1)。\n\n2. **BCS 可靠验证数据集数量** — R1 认为仅 FewRel 1 个 clean（DocRED confounded），R2 认为 RE 2 个数据集。**Director 判断**：R1 论证更有力（VIF=50.9 确实使 DocRED 不可信），但 DocRED 的方向一致性仍有参考价值，不宜完全否定。\n\n3. **Excitement 维度** — R1 给 3.5（实验方法论 + 负面结果有社区价值），R2 给 2.5（SCS metric 缺乏新意限制 excitement）。**Director 判断**：R1 观点更合理——简单 metric + 精细实验设计 本身是有效贡献模式。Excitement 综合 3.0。\n\n---\n\n## Questions\n\n1. **DocRED centrality-residualized BCS**：能否先对 centrality 回归取 BCS 残差，再报告残差 R²？这能更清楚隔离 confusability 独立贡献。[R1]\n2. **Gemini batches 扩展**：能否增加 Gemini count-16 BCS-controlled batches（25→50），检验 leverage point 是否采样偏差？[R1]\n3. **TOST 量表选择文献**：是否有方法学文献支持 accuracy ∈ [0,1] 上使用 linear-scale TOST？[R1]\n4. **NER null 机制**：NER 是 span-level 任务（局部特征更重要），RE 是 sentence/document-level 任务（全局 schema 推理更重要）——这是否是 task asymmetry 的根本原因？[R1]\n5. **域内 BCS-controlled**：是否测试过同一语义域内构建 high/low BCS batches 以排除 domain bias？[R1]\n\n---\n\n## Missing References\n\n两位 Reviewer 均未发现严重遗漏。Related work 覆盖充分。\n\n可选补充：\n- Aly et al. (2019) \"Hierarchical Multi-Task Learning for Fine-Grained Entity Typing\"\n- Onoe & Durrett (2020) \"Fine-Grained Entity Typing for Domain Independent Entity Linking\"\n- R23 遗留可选：Ren et al. (2016) AFET, Choi et al. (2018) Ultra-Fine Entity Typing, Min et al. (2022) Rethinking Demonstrations\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**：pending（已请求，尚未返回）。请求时间：2026-05-21T18:49:05Z，将在 8 小时后自动提醒用户。\n\n内部审稿不等待外部结果。如外部审稿返回后发现与内部审稿的重大差异，Research Director 可酌情追加评估。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：done（2026-05-21T18:49:04 → 18:52:37，耗时约 3.5 分钟）\n\n### Warnings (3)\n\n1. **Pages 1-3 连续纯文本**：Title/Abstract/Intro/Related Work 共 3 页无任何 display item。审稿人需翻过 3 页才看到第一个视觉锚点（Table 1, p4）。建议在 p1 或 p2 加入概览图（如 SCS 概念示意 / 核心发现预览图）。\n\n2. **正文 display items 偏少**：8 页正文仅 4 个 display items（Table 1-2, Figure 1-2），对实证论文偏少（通常 5-8 个）。核心定量结果分散在文字中，缺少汇总 main results 表。\n\n3. **Pages 8-9 连续纯文本**：Section 5 + Section 6 + Limitations 连续 2 页无 display item。Section 5 的 decomposition failure 适合用一张小表或示意图辅助。\n\n### Info (13) — 摘要\n- Table 1-2, Figure 1-2 排版整洁，booktabs 风格，配色色盲友好\n- Figure 1 左面板两条线在高 count 端区分度低\n- Figure 2 panel (a) legend 与数据线有轻微重叠\n- Appendix 14 页含 27 张表但 0 张 figure\n- Prompt templates 排版清晰\n- SCS 公式渲染正确\n- 匿名标记正确\n\n---\n\n## Overall Assessment\n\n**综合评分：3.0 (Findings)**\n**置信度：4/5**\n\n### 评分理由\n\n**可接收为 Findings 的理由：**\n- 研究问题重要且实验设计精细（BCS-controlled batch design 是有价值的方法论范式）\n- FewRel 上 BCS R²=22%（ecological level, VIF=1.16）是可信的效应量\n- 负面结果（NER null, SDGD failure）对社区有明确的警示价值\n- 14 页 Appendix 展现了罕见的统计透明度\n- 格式完全合规，引用无虚假\n\n**不足以进入 Conference (4.0) 的理由：**\n- **核心定量 claim 过度宣称**：最引人注目的 R²=58% 本质上不可解释（centrality vs. confusability）；跨模型验证在 Gemini 上由单一 leverage point 支撑\n- **SCS/BCS 指标新颖性有限**：继承自 LLM-PEE 的标准 embedding cosine similarity，Appendix M 证实 definitions 无额外贡献\n- **可靠结论范围窄于呈现**：严格而言仅 FewRel 1 个数据集提供 clean BCS validation，且为 ecological level R²=22%\n- **NER null 叙述自相矛盾**：structural barrier vs insufficient power 两种解释不兼容\n- **核心分析缺乏跨模型验证**：DocRED R², error taxonomy, SDGD, TOST factorial 均为 Qwen3-32B 单模型\n\n### 达到 Conference (3.5-4.0) 的路径\n\n如果作者在 revision 中：\n1. 将 DocRED R² 标注为 confounded，以 FewRel R²=22% 为主要 claim\n2. 正文披露 Gemini leverage point\n3. 加强 ecological correlation caveat（Abstract + 正文专门讨论段）\n4. 重新 frame SCS 贡献为 methodology vs metric\n5. 统一 NER null 叙述\n6. 至少对 LLaMA-70B 复现一项核心分析\n\n则有望达到 3.5 (Borderline Conference)。进一步达到 4.0 需要新增实验数据（centrality-residualized R², 更多 Gemini batches, 域内 BCS-controlled）。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- RQ1-RQ3 定义清晰，但 \"first controlled study\" claim 需要更精确的 scoping（LLM-PEE 已做 schema partitioning，本文的控制研究是 analytical 而非 engineering）\n- Contributions 第 1 条将 SCS/BCS 与实验方法混为一谈，建议拆分\n\n### Section 2 (Related Work)\n- 覆盖充分，约 1.3 页\n- \"SCS novelty\" 段 (lines 220-233) 已尝试区分与 LLM-PEE，但措辞仍模糊——\"our contribution is the controlled experimental methodology\" 应提升到更显著位置\n- 可适当压缩以为 Section 5 腾空间\n\n### Section 3 (Experimental Setup)\n- BCS-controlled batch 的 greedy 构建方法（Section 3.3）未讨论语义域偏差\n- Table 1 数据集统计清晰\n- SCS 定义（Section 3.2）技术上正确但应更明确承认与 LLM-PEE 的关系\n\n### Section 4 (Results)\n- §4.1 Count curves：方向性发现稳健，跨模型一致\n- §4.2 Pairwise SCS：效应量极小 (r²≈1-5%)，已适当报告\n- §4.3 BCS-Controlled：核心结果章节。DocRED R²=58% 的 centrality confound 讨论不足（仅在 footnote 4 中一笔带过）；ecological amplification caveat 不够显著；Gemini leverage point 未在正文披露\n- §4.4 Multi-Dimensional Degradation：error taxonomy 分析有洞察力（IntraSub vs ExtraSub 分布差异），但仅 Qwen3-32B\n- §4.5 Centrality Confound：诚实的分析，MAVEN 的 centrality 问题处理得当\n\n### Section 5 (Schema Decomposition)\n- 三大贡献之一，空间严重不足（半 column）\n- NER merge amplification 和 RE routing failure 的双重失败机制是有价值的发现\n- 建议用 Table 或 Figure 辅助叙述\n\n### Section 6 (Discussion and Conclusion)\n- \"BCS enables pre-hoc diagnostics\" 是合理的实用价值定位\n- \"replicated across four models\" 措辞过强，应精确化为 \"count direction replicated on four models; BCS effect replicated on three open-weight families\"\n\n### Limitations\n- 6 点覆盖全面（model coverage, effect size, task scope, causal mechanism, contamination, domain scope）\n- Across-batch correlation 和 Multiple comparisons 两段补充得当\n- NER null 的 power=65% 应在此更明确讨论其与正文 structural barrier 解释的张力\n\n### Appendix\n- 14 页 27 表，robustness 极其充分\n- Appendix N (ecological simulation) 是关键证据，应在正文更显著地引用\n- Appendix R (variance decomposition) 量化了 FP8 non-determinism，有价值但未在正文充分讨论影响",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_ac7ab7270b6b5caecee04f89b11aab3e"
  }
}
```

</details>

---


### Tool result

_source line 2707 · 2026-05-21T19:08:56.497076+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_51326259fe46fbae9da26b81cf03f1f8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4119
}
```

</details>

---


### Tool call

_source line 2708 · 2026-05-21T19:09:11.075122+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性和 Venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 人数和侧重'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'Reviewer 1 和 Reviewer 2 独立审稿完成'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享完成'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '关键问题已达成共识'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'completed', 'activeForm': '审稿报告已投递'}]"
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
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性和 Venue 要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 人数和侧重'}, {'content': 'Step 0.6/0.7: 派发外部审稿 + 视觉审查', 'status': 'completed', 'activeForm': '派发外部审稿和视觉审查'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': 'Reviewer 1 和 Reviewer 2 独立审稿完成'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '交叉分享完成'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '关键问题已达成共识'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'completed', 'activeForm': '审稿报告已投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 2709 · 2026-05-21T19:09:11.125954+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 2710 · 2026-05-21T19:09:24.050128+00:00_

---

**Round 24 审稿圆桌会议完成。**

审稿报告已投递给 Research Director。

**结论：3.0 (Findings)**，置信度 4/5。

**核心发现汇总：**

| 类别 | 数量 | 关键问题 |
|------|------|----------|
| Must-Fix (共识) | 5 | DocRED R² confounded; Gemini leverage point; ecological caveat; SCS novelty; NER null tension |
| Should-Fix (共识) | 7 | DocRED 小样本; 跨模型验证不足; greedy batch 域偏差; 单种子; Abstract 过载; §5-6 压缩; clean validation 仅 FewRel |
| Divergence | 1 | TOST 量表敏感性 |
| Minor | 3 | orphan bib; 术语统一; 可选引用 |

**可靠结论范围（两位 Reviewer 共识）**：FewRel BCS R²≈22%，ecological (batch-aggregate) level，open-weight models。论文当前 framing 超出此范围。

**外部审稿**：pending（未返回，不阻塞报告）。**视觉审查**：done，3 个 warning（前 3 页无 display item、display items 偏少、§5-6 无视觉辅助）。

Issue Tracker 已同步更新至 `review_issues.yaml`（R24 新增 16 条，R23 resolved 3 条，possibly resolved 4 条）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 225

## Round 225

2 recorded events


### User

_source line 2711 · 2026-05-21T19:09:26.632419+00:00_

[Reviewer 2 审稿结果]:
交叉回应已完成并提交给 Director。

核心结论：R1 的三个 Must-Fix 全部同意，Should-Fix 中仅对 W2（TOST scale 选择）部分反驳。两位 Reviewer 的独立分析在关键问题上高度一致——DocRED R² 不可信、ecological caveat 缺失、跨模型验证不足。评分维持 3.0 (Findings)。

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

_source line 2712 · 2026-05-21T19:09:39.700205+00:00_

审稿圆桌会议已完成。

**Round 24 审稿报告已投递至 Research Director。**

**结果摘要：**
- **综合评分**：3.0 (Findings)，置信度 4/5
- **5 个 Must-Fix**（全部为 R1+R2 共识）：DocRED R²=58% centrality confound、Gemini leverage point、ecological correlation caveat、SCS 贡献定位、NER null 叙述张力
- **7 个 Should-Fix**：DocRED 小样本、跨模型验证缺口、greedy batch 语义域偏差、单种子 FP8、Abstract 过载、Section 5-6 压缩、BCS clean validation 仅 FewRel
- **1 个分歧**：TOST 量表敏感性（R1 Should-Fix vs R2 REBUT）
- **外部审稿**：pending（未返回，不阻塞）
- **视觉审查**：done（3 warnings — 前 3 页无 display item、正文图表偏少、后 2 页纯文本）
- **Issue Tracker**：已更新至 R24，R23-F1（Checklist）和 R23-MR1（Robinson 引用）确认已修复

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_ac7ab7270b6b5caecee04f89b11aab3e:director"
}
```

</details>

---


## Round 226

## Round 226

74 recorded events


### User

_source line 2713 · 2026-05-21T21:05:23.713875+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: schema-dag-extraction
- 论文路径: projects/schema-dag-extraction/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR May 2026)
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

_source line 2714 · 2026-05-21T21:05:31.854456+00:00_

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
