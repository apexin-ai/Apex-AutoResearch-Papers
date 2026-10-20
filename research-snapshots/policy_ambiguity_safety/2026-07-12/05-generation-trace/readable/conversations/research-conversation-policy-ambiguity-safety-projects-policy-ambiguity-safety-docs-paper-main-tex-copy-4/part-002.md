# Research conversation: 系统通知：审稿审批已通过。请开始审稿。 [论文提交] - 项目: policy_ambiguity_safety - 论文路径: projects/policy_ambiguity_safety/docs/paper/main.tex -  — Part 2 of 2

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-policy-ambiguity-safety-projects-policy-ambiguity-safety-docs-paper-main-tex-copy-4.md) · [Structured JSON](../../../sessions/99/9944903d347906e44b5d.json)

## Round 14

### Tool call

_source line 185 · 2026-05-23T20:01:45.352Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director · `toolu_01AEpbqdDLKqczDmhSQY4g59`</summary>

```json
{
  "project": "policy_ambiguity_safety",
  "force_resubmit": "true",
  "report": "# Round 28 审稿报告（最终版）\n\n**论文**: Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety\n**Venue**: EMNLP 2026 (ARR May cycle)\n**审稿日期**: 2026-05-23\n**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性/完整性）\n**流程**: Round 1 独立初审 → 交叉分享 → R1 结构化 9 维度审稿 → 第二轮交叉分享 → 收敛\n\n---\n\n## Summary\n\n本文通过匹配对因果设计研究策略文本歧义对 LLM agent 安全违规的影响。在 τ²-bench 上使用 300 个 clause pairs（六类型分类法）×5 个模型（2,997 episodes），发现歧义条款使违规率增加 34.0pp（排除 incompleteness 后 31.0pp）。论文进一步发现 type–mechanism dissociation（V=0.45 LLM-coded）、disambiguation neglect（4.6% 意识率）和 systematic nocuity（41.3% 收敛违规，77% 偏向宽容解释）。SOPBench 跨基准复制确认方向一致（+12.7pp）。\n\n---\n\n## Strengths\n\n1. **C1 因果证据链完整**：matched-pair 设计正确隔离歧义作为 IV；perturbation control（Δ=-0.67pp, CI 含零）、within-family ICC=0.919、SOPBench 跨基准复制、7 模型跨 6 provider 均为正效应——因果推断在 agent safety 领域属方法论质变。[两轮审稿一致共识]\n\n2. **统计方法规范**：McNemar 配对检验、TOST 7-margin 敏感性分析、Holm-Bonferroni 校正、bootstrap cluster analysis (B=10,000)。C3 未通过校正后正确标记为 inconclusive，C4 标记为 exploratory——显示严格统计纪律。[R1 两轮均重点肯定]\n\n3. **Cross-judge validation 全面**：三独立 judge Fleiss' κ=0.717，无 same-family leniency（Claude judge 对 Claude agent 更严格而非更宽松）。Human validation (inter-annotator κ=0.798, human-LLM κ=0.733) 确认违规检测可靠性。[共识]\n\n4. **Disambiguation neglect (4.6%) 量化**：将 ambiguity collapse (Liu et al. 2023) 从表示层面扩展到行为层面。Qwen3/DeepSeek 零意识 vs GPT-4.1/Claude 10-11% 的模型分化有独立研究价值。[共识]\n\n5. **Claims 标定诚实**：C1/C2 supported, C3 inconclusive, C4 exploratory, incompleteness 效应标为 upper bound。15 页高质量附录覆盖几乎所有可预期疑问。[共识]\n\n6. **格式合规**：Abstract ~160 词（<200 限制），double-blind 匿名完整。[共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（3 项，两轮稳定）\n\n**MF1** Type–mechanism dissociation \"establishes\" 与 [Exploratory] 标签矛盾\n\nAbstract \"establishes the taxonomy as a diagnostic instrument\" vs §6 标题 [Exploratory] vs Introduction contribution (3) \"exploratory\"——同一论文中对同一发现定位摇摆。Failure mechanism 编码 human κ=0.15（collapsed 后 0.34-0.52），远低于 LLM coder κ=0.52。Abstract 仅报告 collapsed κ=0.34-0.52，省略原始 κ=0.15。\n\nR1 第二轮进一步分析：论文声称 ICC pattern、failure modes、violation rates 构成 \"convergent evidence\"，但三个 evidence streams 共享实验平台和 LLM measurement tools，独立性打折扣——evidence 是 partially convergent 而非 fully convergent。\n\n**修改要求**：(a) \"establishes\" → \"suggests\"/\"provides exploratory evidence for\"；(b) Abstract 加入 κ=0.15；(c) 讨论 LLM coder 一致性高于人间的可能解释；(d) 降低 convergent evidence 的措辞。\n\n**R1 明确表示：满足此条件是从 3.5 升至 4.0 的前提之一。**\n\n---\n\n**MF2** Clause pair 构建方法描述自相矛盾\n\n§4.2 \"template-based pipeline\" vs Appendix T \"hand-crafted, no automated over-generation\"。两位 Reviewer 共识 [AGREE]。R2 分析：最可能是 §4.2 表述不准确，实际是人工按模板规范手工编写。\n\n**修改要求**：§4.2 改为 \"hand-crafted following structured type-level specifications\"。\n\n---\n\n**MF3** 信息添加混淆未在全部高 Δtoken 类型上充分标注\n\nAuth-scope（Δtoken=36.1, 所有类型中最大）与 incompleteness（34.6）同样存在信息添加混淆，但仅 incompleteness 有 † 标注和专项 confound analysis（Appendix F）。R2 补充关键观察：两个效应最大的类型同时也是信息添加最大的类型，而 confound-minimized coreferential 仅 +18.7pp——headline +34.0pp 可能显著高估纯歧义效应。\n\nR1 第二轮进一步指出：perturbation control（同义词替换、clause 重排）保持信息量不变，不覆盖信息添加混淆。缺少理想控制条件（添加等量无关信息或 partial disambiguation）。\n\n**修改要求**：(a) Table 2 对 Δtoken>25 words 的类型均加注信息添加警告；(b) §5.1/Discussion 明确区分 ambiguity-only 效应 (coreferential 18.7pp) 与 mixed effects。\n\n**R1 明确表示：满足此条件是从 3.5 升至 4.0 的前提之一。**\n\n---\n\n### Should-Fix（7 项）\n\n**SF1** Discussion + Conclusion 合计约 150 词，讨论严重不足。缺失：disambiguation neglect 与 sycophancy 关系、systematic nocuity 对 evaluation 范式启示、开发者实操建议、RE 工具链借鉴。R2 列为 MF，R1 降为 SF（8 页限制下的合理 trade-off）。最终定级 SF，但强烈建议扩展至 ~300 词。\n\n**SF2** Berry \"nocuous\" 术语反转过度修辞。\"Inverting Berry\" → \"Berry's criterion breaks down for LLM agents\"。41.3% convergent violations 未按模型家族分析——如果主要在同族模型间收敛，可被 training-data similarity trivially 解释。需补充 cross-family convergence 分析。\n\n**SF3** Cramér's V 跨维度比较方法论缺陷。V=0.45 (6×5) vs V=0.14 (6×2) 归一化因子不同，不可直接比较。建议用 NMI 作主论据。R2 修正 R1 的事实错误：实际为 6×5 而非 6×3，但核心关切成立。\n\n**SF4** Temperature=0 唯一条件。无 temp>0 pilot data。R2 第二轮补充：temp=0 下 convergent nocuity 解读需更谨慎——每个 model-clause pair 仅一个确定性输出，temp>0 下 convergence pattern 可能完全不同。**R1 明确表示：1 model × 2 temp × 50 pairs 的 pilot 是升至 4.0 的前提之一。**\n\n**SF5** 合成刺激生态效度。SOPBench +12.7pp 仅为 τ²-bench 37%，论文三个 post-hoc 解释之外还有一个可信解释：更接近真实 SOP 的歧义效应自然更小。R2 REBUT \"96% agreement = 任务过简\"——高分类一致性是实验设计优点（标注者带 taxonomy 定义做分类 vs LLM 无标签执行任务，认知任务不同）。R1 在第二轮未反驳此 REBUT → 该分歧部分消解。\n\n**SF6** `\\enlargethispage{26\\baselineskip}` ≈ 4.3 inches 页面扩展，几乎肯定超出 ACL bottom margin 要求。\n\n**SF7** Judge prompt template 未完整披露。论文未提供 evaluation judge 的完整 prompt（分类 none/minor/moderate/critical 的指令）。Appendix AB 提及 \"the same rubric and prompt template\" 但未附全文。对可复现性至关重要。[R1 第二轮结构化审稿新发现]\n\n---\n\n### Minor（6 项）\n\n- **M1**: §5.1 McNemar OR=15.1 基于 discordant pairs (n=580)，应在首次报告时重申。\n- **M2**: Conclusion \">89% disambiguation neglect\" 来源不明确。建议改用 overall 95.4% 或标注 \"range: 89–100%\"。\n- **M3**: Prevalence audit κ=0.295 很低但报告 87%——R2 补充：低 κ + 高 prevalence 可能反映标注者各自的宽松倾向（base-rate 效应）。\n- **M4**: SOPBench +12.7pp 是 unweighted mean，应标注。\n- **M5**: τ²-bench policy injection 技术细节不足（如何定位原始 clause、context preservation、boundary effects）。[R1 第二轮新发现]\n- **M6**: Human annotator 资质和培训细节不足——§4.2 和 Appendix AF 的标注者是否为同一人？是否有 mechanism 分类培训？如果 human κ=0.15 部分反映培训不足而非分类体系问题，应澄清。[R1 第二轮新发现]\n\n---\n\n## Reviewer Consensus（跨两轮稳定）\n\n两位 Reviewer 在以下问题上跨两轮保持共识 [AGREE]：\n- Type-mechanism dissociation \"establishes\" 过度表述 (MF1)\n- Clause pair 构建描述矛盾 (MF2)\n- 信息添加混淆范围需扩展 (MF3)\n- Discussion/Conclusion 过短 (SF1)\n- Berry 术语反转需更深入论证 (SF2)\n- V 跨维度比较缺陷 (SF3)\n- Temperature=0 泛化局限 (SF4)\n- SOPBench 效应差异需更多讨论 (SF5)\n- C1 因果设计是论文最强贡献\n- Disambiguation neglect 4.6% 是有价值的发现\n- Claims 标定诚实是高质量实证论文标志\n\n## Reviewer Divergence\n\n- **Excitement 评分**：R1 给 3.5/5（\"core finding 'ambiguity hurts' 不 surprising，excitement 来自操作化而非理论突破\"），R2 可能给 4/5（更看重概念贡献 convergent nocuity 和方法论质变）。\n- **96% agreement 解释**：R1 认为暗示任务过简，R2 REBUT 认为是实验设计优点。R1 第二轮未反驳 → 分歧部分消解。\n- **\"Ambiguity\" 广义定义**：R2 认为影响 headline result，R1 REBUT 认为 §3 处理充分。→ 不列为修改要求。\n- **Overall 评分**：R1 稳定在 3.5（两轮一致），R2 从 3.5 可能上调至 4.0。\n\n---\n\n## Questions\n\n1. §4.2 \"template-based pipeline\" 和 Appendix T \"hand-crafted\" 的矛盾如何解释？\n2. 41.3% convergent violations 中，同族模型间收敛 vs 跨厂商收敛的比例？\n3. Auth-scope 是否可提供类似 incompleteness 的专项 confound analysis？\n4. 是否有任何 temperature>0 pilot data 或计划？\n5. Human mechanism coding 标注者是否接受了系统培训？\n6. \"Diagnostic instrument\" 的预期端到端 workflow 是什么？\n7. Evaluation judge prompt template 能否完整披露？\n8. τ²-bench policy injection 的技术实现细节？\n\n---\n\n## Missing References\n\n无重大遗漏。可选补充：\n- D'Amour et al. (2022) \"Underspecification Presents Challenges for Credibility in Modern Machine Learning\" [两位 Reviewer 共识]\n- Constitutional AI / RLHF 文献，解释不同 safety training 导致不同 ambiguity vulnerability profiles [R1 第二轮建议]\n\n---\n\n## External Review\n\n**外部审稿**：未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n已完成（0 critical, 1 warning, 6 info）：\n- **[warning]** Pages 1-2 连续纯文本无 display item，Figure 1 直到 page 3 才出现\n- **[info]** Page 5 整页 Method 纯文本；Page 6 Figure 2 灰度区分度不足；Page 8 热力图字号偏小；Pages 13/18 Appendix 表格密集；Page 23 约 60% 填充\n\n---\n\n## Overall Assessment\n\n| 维度 | R1 | R2 | 综合 |\n|------|-----|-----|------|\n| Soundness | 3.5 | 4 | **3.5** |\n| Excitement | 3.5 | 3-4 | **3.5** |\n| Reproducibility | 3.5 | 4 | **3.5** |\n| Overall | 3.5 | 3.5-4.0 | **3.5** |\n| Confidence | 4 | 4 | **4** |\n\n**Overall Assessment: 3.5 / 5（Borderline Conference）**\n\n**评分理由**：C1（歧义→违规 +34pp 因果效应）实验设计扎实、控制链完整，是对该领域的方法论质变——这是论文最强且无争议的贡献。Disambiguation neglect (4.6%) 和 systematic nocuity (77% permissive) 是有价值的实证发现。但论文的核心概念重构——type–mechanism dissociation 作为 \"diagnostic instrument\"——依赖 human κ=0.15 的 failure mechanism 编码，evidence 不足以支撑 \"establishes\" 级别的 claim。三个 Must-Fix（措辞过度、构建描述矛盾、信息添加混淆标注不完整）和七个 Should-Fix 叠加，使论文停留在 Borderline Conference。\n\n**升级路径（R1 明确条件）**：\n1. \"establishes\" → \"suggests\"（文字修改，camera-ready 可完成）\n2. auth-scope 和 incompleteness 同时标注信息添加混淆，区分 confound-free 效应和 mixed 效应（文字修改，camera-ready 可完成）\n3. 至少 1 model × 2 temperature × 50 pairs 的 pilot（需额外实验）\n\n满足 (1)(2) 即可显著提升论文可信度；(3) 是 ideal 但非必需。\n\n**EMNLP 2026 标准映射**：3.5 = Borderline Conference。如果 MF1-MF3 得到充分解决，论文有潜力达到 4.0（Conference / Main）。AC 可据 R1（偏方法严谨性，稳定 3.5）和 R2（偏概念贡献，3.5-4.0）的不同视角做最终判断。",
  "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
  "cross_response_reviewer_ids": "[\"1\", \"2\"]",
  "overall_score": "3.5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d838dcf-660f-4446-8693-6f48e27c7e30",
  "isSidechain": false,
  "requestId": "req_011CbL6PqL7VS1JLKSzzHszY",
  "type": "assistant",
  "uuid": "aa7bf26d-d8cc-4828-b432-c39b4fe7329e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/review_director_0e80b40a",
  "sessionId": "a12edc2b-318d-49ec-adb5-ee9cfa431360",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FuDddUPoMKYA5GAC8MvLpb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5378,
      "cache_read_input_tokens": 147669,
      "output_tokens": 5125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5378,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5125,
          "cache_read_input_tokens": 147669,
          "cache_creation_input_tokens": 5378,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5378
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Runtime record

_source line 186_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Reviewer 1 审稿意见]: ## Reviewer 1 对 R2 Cross-Share 的回应  ### 说明  注意到此处 R2 的评分（Excitement 4/5, Overall 4.0）与 Round 1 中 R2 的评分（Excitement 3/5, Overall 3.5）**不一致**。可能存在两种情况：(1) Director 在 cross-share 中引用了不…",
  "leafUuid": "aa7bf26d-d8cc-4828-b432-c39b4fe7329e",
  "sessionId": "a12edc2b-318d-49ec-adb5-ee9cfa431360"
}
```

---


### Runtime record

_source line 187_

```json
{
  "type": "ai-title",
  "aiTitle": "Review policy ambiguity safety paper",
  "sessionId": "a12edc2b-318d-49ec-adb5-ee9cfa431360"
}
```

---


### Tool result

_source line 188 · 2026-05-23T20:01:50.798Z_

<details><summary>↩ Tool result · `toolu_01AEpbqdDLKqczDmhSQY4g59`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_10fa2e89afc5e9b8a13613245e008dd9:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa7bf26d-d8cc-4828-b432-c39b4fe7329e",
  "isSidechain": false,
  "promptId": "6d438992-8da4-4709-9761-9fb5e5c6d83d",
  "type": "user",
  "uuid": "de8fb4ca-ca7f-4d50-bf0a-888d4ce4c6e7",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"research_director_key\\\": \\\"feishu:group:oc_10fa2e89afc5e9b8a13613245e008dd9:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_10fa2e89afc5e9b8a13613245e008dd9:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "aa7bf26d-d8cc-4828-b432-c39b4fe7329e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/review_director_0e80b40a",
  "sessionId": "a12edc2b-318d-49ec-adb5-ee9cfa431360",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 189 · 2026-05-23T20:01:50.804Z_

```json
{
  "parentUuid": "de8fb4ca-ca7f-4d50-bf0a-888d4ce4c6e7",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "1d9590c3-9a53-46ac-9117-92134488a482",
  "timestamp": "2026-05-23T20:01:50.804Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/review_director_0e80b40a",
  "sessionId": "a12edc2b-318d-49ec-adb5-ee9cfa431360",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---


### Runtime record

_source line 190_

```json
{
  "type": "ai-title",
  "aiTitle": "Review policy ambiguity safety paper",
  "sessionId": "a12edc2b-318d-49ec-adb5-ee9cfa431360"
}
```

---


### Runtime record

_source line 191 · 2026-05-23T20:02:05.823Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-23T20:02:05.823Z",
  "sessionId": "a12edc2b-318d-49ec-adb5-ee9cfa431360",
  "content": "[SYSTEM] Research Reviewer 刚完成 context rotation (Loop 5)，已读取 handoff 并就绪。如有待办任务请立即分配。\n\n---\n\n[Reviewer 1 审稿结果]:\n审稿意见已提交。\n\n总结：经过审慎考虑 R2 的 cross-share 意见后，我维持 Overall 3.5 (Borderline Conference) 不变。同意 R2 对研究新颖性和概念贡献的肯定，但从方法严谨性角度，三个核心问题（信息添加混淆未全面控制、mechanism analysis circularity、temperature=0 唯一条件）阻止升至 4.0。与 R2 的 0.5 分分歧主要来自不同的评价权重：R2 偏重概念新颖性，我偏重方法完备性。\n\n---\n\n[Reviewer 2 审稿意见]:\n## Reviewer 2 补充审查报告：新颖性 + Related Work + 概念框架 + 写作 + 影响力\n\n**说明**：此报告基于我对论文全部 23 页 PDF 和关键 LaTeX 源文件的精读，按 Director 指定的 6 个评估维度展开。分数与我此前提交的 Round 1 审稿一致（Overall 3.5）。\n\n**标题核对**：Director 任务描述中的标题 \"Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families\" 与我实际审阅的论文标题 \"Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety\" 不一致。以下审查基于实际论文内容。Director 描述中的部分术语（\"Differential Nocuity\"、\"Ambiguity Blindness\"、\"27% all-model convergence\"）也与论文实际使用的术语和数据有差异——论文使用 \"systematic nocuity\"、\"disambiguation neglect\"、13.0% unanimous / 41.3% majority-convergent。\n\n---\n\n## 1. 新颖性评估\n\n### 1.1 研究问题新颖性\n\n**\"Has anyone causally measured ambiguity→safety violations before?\"**\n\n据我所知，**没有**。DRIP-R (Vijayvarrgiya et al., 2026b) 是最接近的并发工作，但使用相关性设计（400 scenarios, 5 RE ambiguity types, 测量 decision quality 而非 safety violations）。论文在 Related Work §2 (related_work.tex L14) 中明确对比了差异：\"DRIP-R's correlational design leaves open whether ambiguity *causes* violations or merely co-occurs with harder scenarios; our matched-pair controls (Δ_perturb = −0.67 pp) isolate the causal contribution.\"\n\n**评估**：matched-pair causal design 是对该领域的**方法论质变**（从相关性到因果性）。Perturbation control (+perturbation 效应含零 CI)、ICC replicability (0.919)、SOPBench 跨基准复现构成了完整的因果推断控制链。这是论文最扎实的新颖性来源。\n\n### 1.2 \"Systematic Nocuity\" / \"Convergent Nocuity\" 是否为真正的概念推进？\n\n论文在 Introduction (introduction.tex L6) 中定义 convergent nocuity：\"Unlike human teams, where convergence reflects shared domain knowledge, agent convergence reflects shared training biases operating on identical inputs.\" 并在 Section 6.3 (analysis.tex L33-35) 报告：41.3% 的歧义 clause 触发 majority-convergent violations (≥3/5 models agree), 13.0% unanimous, 77.0% permissive bias。\n\n**评估**：这不是简单地\"应用一个现有框架\"，而是指出了 Berry & Kamsties (2004) 框架在 LLM 语境下的一个**根本性假设失败**——B&K 假设 convergence = innocuous（因为来自共享领域知识），但 LLM 的 convergence 来自 shared training biases，是一种完全不同的机制。这是一个**genuine conceptual insight**。\n\n**但有两个重要限制**（与我此前审稿的 W1 一致）：\n1. **概念包装过度**：论文称此为 \"inverting Berry's framework\"（Introduction L6），但更准确的表述是 \"Berry's framework breaks down for LLMs\"。Berry 的框架从未声称适用于 AI agents；论文发现的是框架的**适用边界**，而非框架本身的\"反转\"。\n2. **训练数据混淆**：41.3% 的跨模型收敛可能部分源于 shared pre-training data（WebText, CommonCrawl），而非歧义文本的内在结构特征。论文未按模型家族分解收敛模式（OpenAI 内部 vs. 跨厂商）。如果收敛主要发生在同族模型间，systematic nocuity 的普遍性结论需下调。\n\n### 1.3 \"Disambiguation Neglect\" (<5% awareness) 是否意外？\n\n论文报告 4.6% 歧义意识率（Section 6.2, analysis.tex L28-30）。\n\n**评估**：介于 \"novel\" 和 \"expected\" 之间。\n- **Expected 的方面**：Liu et al. (2023) 已证明 LLMs 在表示层面进行 ambiguity collapse（将多种解释压缩为单一表示）。从 representation collapse 推导到 behavioral neglect 并非大跳跃。\n- **Novel 的方面**：(a) 量化程度前所未有（4.6% vs. 此前仅有定性观察）；(b) 从表示层扩展到**行为层**——agents 不仅在内部 collapse 解释，还在行为上从不 flag 歧义、直接产生不可逆安全违规，这是一个有实践意义的新发现；(c) 跨 5 个模型的一致性增强了发现的稳健性。\n- **关键缺陷**：在 temperature=0 下，每个 model-clause pair 仅有一个确定性输出，agent 没有\"机会\"在不同 runs 中展现不同程度的意识。4.6% 可能低估了 stochastic sampling 下的意识率。\n\n### 1.4 Type–Mechanism Dissociation\n\nV = 0.45 (LLM-coded, 6×5 table, 95% CI [0.41, 0.50])，human κ = 0.15 (raw), 0.34–0.52 (collapsed)。\n\n**评估**：**概念有趣但证据不够稳固**。如我此前 N1 所述，human κ = 0.15 意味着人类标注者几乎无法可靠区分 failure mechanisms。V = 0.45 的 LLM 编码一致性可能反映 LLM coder 的 shared bias 而非真正的 type→mechanism 映射。论文正确标记 Section 6 为 \"[Exploratory]\"，但 Abstract/Introduction 的 \"establishes\" 表述过强。\n\n---\n\n## 2. Related Work 覆盖评估\n\n### Requirements Engineering\n\n| 引用 | 状态 | 评估 |\n|------|------|------|\n| Berry & Kamsties (2004) | ✓ 核心引用 | 充分讨论，nocuous/innocuous 框架是论文理论基础 |\n| Chantree et al. (2006) | ✓ 已引用 | related_work.tex L5: \"from heuristic methods (Chantree et al., 2006; Willis et al., 2008)\" |\n| Ferrari et al. (2018, 2019) | ✓ 已引用 | 两篇均引用 |\n| Willis et al. (2008) | ✓ 已引用 | 与 Chantree 一起引用 |\n| Ezzini et al. (2022) | ✓ 已引用 | 两篇 Ezzini 均引用（TAPHSIR + anaphoric） |\n| Massey et al. (2014) | ✓ 已引用 | taxonomy.tex 中引用，6 种 RE 歧义类型 |\n\n**评估**：RE 覆盖**充分**，核心文献无遗漏。\n\n### Agent Safety\n\n| 引用 | 状态 | 评估 |\n|------|------|------|\n| ToolEmu (Ruan et al. 2024) | ✓ 已引用 | related_work.tex L11 |\n| InjecAgent (Zhan et al. 2024) | ✓ 已引用 | related_work.tex L11 |\n| R-Judge | ✓ 已引用 | related_work.tex L11 |\n| τ²-bench (Barres et al. 2025) | ✓ 核心引用 | 实验平台 |\n| AgentPex (Sharma et al. 2026) | ✓ 已引用 | related_work.tex L14 |\n| DRIP-R (Vijayvarrgiya et al. 2026) | ✓ 详细对比 | 最主要的并发工作，Appendix L 有分类映射 |\n\n**评估**：Agent safety 覆盖**充分且详细**。论文还引用了多个 Director 未列出的相关工作（PolicyBank, SOPBench, MANTRA, SafeAgentBench 等）。\n\n### Prompt Sensitivity\n\n| 引用 | 状态 | 评估 |\n|------|------|------|\n| Sclar et al. (2024) | ✗ 未引用 | 关于 prompt design 敏感性的定量研究 |\n| Lu et al. (2022) | ✗ 未引用 | prompt ordering effects |\n| Zhou et al. (2022) | ✗ 未引用 | automatic prompt engineering |\n\n**评估**：prompt sensitivity 文献**未被引用**，但这是否为重大遗漏取决于 scope 判断。论文关注的是**policy specification 中的歧义**（一种语义层面的变异），而非**prompt phrasing 的表面敏感性**（格式、排序等）。Sclar et al. 的工作讨论的是 spurious features（标点、大小写、formatting），与 policy ambiguity（语义多义性）在概念层面有区别。但论文的 perturbation control (§4.5: synonym substitution, clause reordering → Δ = −0.67 pp) 本质上在测试一种弱形式的 prompt sensitivity，与 Sclar et al. 有交集。\n\n**建议**：在 Related Work 中加 1-2 句连接 prompt sensitivity 文献，说明本文的 perturbation control 与该领域的关系。不属于 must-cite 但会加强论文的 positioning。\n\n### NLP Ambiguity\n\n| 引用 | 状态 | 评估 |\n|------|------|------|\n| Poesio & Artstein (2005) | ✓ 已引用 | taxonomy.tex 中引用 |\n| Bender (e.g., Bender & Koller 2020) | ✗ 未引用 | \"Climbing towards NLU\" |\n| Wasow et al. (2005) | ✓ 已引用 | taxonomy.tex 中引用 |\n| Liu et al. (2023) | ✓ 已引用 | ambiguity collapse |\n| Gur-Arieh et al. (2026) | ✓ 已引用 | ambiguity collapse taxonomy |\n\n**评估**：NLP ambiguity 覆盖**充分**。Bender & Koller (2020) 关于 language understanding 的讨论与本文 scope 交叉有限，不属于必要引用。论文引用了更直接相关的 psycholinguistics 文献（Ferreira 2002, Frazier & Rayner 1982, Hu et al. 2023）。\n\n### 总体 Related Work 评估\n\n**覆盖度评分：4/5 (Strong)**。所有核心 RE、agent safety、psycholinguistics 引用均已覆盖。唯一可改进的是加入 prompt sensitivity 文献作为对比 positioning，但这属于 \"nice-to-have\" 而非必要。\n\n---\n\n## 3. 概念框架质量\n\n### 3.1 Two-layer taxonomy\n\n论文将 6 种歧义类型组织为两层——specification layer（incompleteness, conditional precedence, coreferential）和 linguistic layer（lexical, scopal, authorization scope）。来源：Li et al. (2024) 的 11-type NLP taxonomy + Massey et al. (2014) 的 6-type RE taxonomy。\n\n**评估**：\n- **Well-motivated**：Section 3 (taxonomy.tex) 明确说明了选择标准——(1) theoretical attestation in prior RE literature, (2) minimal-pair constructability, (3) mutual exclusivity for unambiguous PV assignment。\n- **但两层结构在分析中作用有限**：C3（layer grouping effect）未通过 Holm-Bonferroni 校正（experiments.tex L55: p = 0.017, threshold 0.0125）。论文诚实地报告了这一结果，但这意味着 two-layer 组织是一个**描述性分类而非有分析力的 structural distinction**。\n- **Authorization scope 的归属可疑**：auth-scope 被归入 linguistic layer，但其本质更接近 specification-layer 问题（permissions 和 boundaries 属于 policy specification 而非语言结构）。Table 13 显示 auth-scope 的 Δtoken (+36.1) 远高于其他 linguistic-layer 类型（lexical +25.7, scopal +17.8），行为模式也更接近 specification-layer。这一分类选择可能人为地弱化了 layer-level 效应（C3）。\n\n### 3.2 \"Disambiguation channel\" 解释\n\nIntroduction (L6): \"LLM agents lack these disambiguation channels. They cannot consult colleagues, rarely escalate to users, and must resolve ambiguity in real time from the text alone.\"\n\n**评估**：\n- **直觉合理但未被直接测试**。论文的实验设计不操纵 disambiguation channels（没有 \"with channel\" vs. \"without channel\" 条件）。\n- **但有间接支撑**：Appendix B 的 mitigation experiment 测试了一种简单的 disambiguation instruction，结果显示 type-dependent effectiveness（auth-scope −18.0pp, lexical −8.9pp, incompleteness −3.4pp n.s.）。这间接说明 disambiguation 能力因类型而异——specification-layer 缺失信息无法从 prompt alone 恢复。\n- **Vijayvargiya et al. (2026) 的 74% recovery** (related_work.tex L8) 提供了正向证据：当 disambiguation channel 可用时（interactive clarification），underspecification 的影响大幅减少。\n- **总体判断**：post-hoc 但 testable，有间接证据支撑。不是 circular reasoning，但也不是直接验证。\n\n### 3.3 ICC pattern → failure modes → disambiguation channels 的证据链\n\n- ICC pattern：clause identity 解释 22.4% variance, type 仅 0.4%（Appendix AC, Figure 2）\n- Failure modes：V = 0.45 type→mechanism（Section 6, LLM-coded）\n- Disambiguation channels：概念性解释，未直接测试\n\n**评估**：三者之间是**convergent evidence 而非 circular reasoning**。\n- ICC 分析不依赖 failure mode coding（纯数值方差分解）\n- Failure mode coding 不依赖 ICC（独立的分类任务）\n- Disambiguation channel 是 interpretive framework，不进入任何定量分析\n\n每个分析层面使用独立的数据和方法，然后在 Discussion 中整合解释。这是合理的科学推理结构。但 Discussion (discussion.tex) 仅用约 80 词整合这些证据，远不足以让读者看到 convergent evidence 的力度。\n\n---\n\n## 4. 写作质量\n\n### 4.1 Abstract\n\n- **字数**：约 160 词（LaTeX 源文件 abstract.tex），**符合 ≤200 词要求**。\n- **贡献清晰度**：三个核心数字（+34.0/+31.0 pp, V = 0.45, 4.6% awareness）均出现在 Abstract 中。\n- **问题**：(a) 仅报告 collapsed κ = 0.34–0.52，未报告 raw κ = 0.15，可能误导读者对 human agreement 的判断；(b) \"establishes the taxonomy as a diagnostic instrument\" 用词过强（与 Section 6 的 [Exploratory] 标签矛盾）。\n\n### 4.2 Introduction\n\n- **Opening vignette**（Introduction L4）：scopal ambiguity 导致 $200 损失的客服案例，**有效**——具体、可感、直接说明实际危害。\n- **Gap statement**（Introduction L8）：\"no existing study provides a causal, type-granularity mapping from ambiguity to safety violations\"——**清晰且准确**。我核查了相关工作，未找到反例。\n- **叙事弧**：problem（§1 L4-6）→ gap（§1 L8）→ method（§1 L17）→ findings（§1 L19-21）→ contributions（§1 L21），结构**清晰完整**。\n- **Berry 框架引入**（Introduction L6）：2 段话阐述 convergent nocuity 的概念，篇幅恰当。但 \"inverting Berry's framework\" 的表述偏激进（见 1.2 节评估）。\n\n### 4.3 Claim 标定\n\n- C1/C2: \"supported\" — 合理（统计证据充分）\n- C3 (layer effect): 报告 \"did not survive Holm-Bonferroni\" (experiments.tex L55) — **非常诚实**\n- Section 6: 标记为 \"[Exploratory]\" — 正确\n- **但**：Abstract/Introduction 中 \"establishes\" 与 [Exploratory] 矛盾。应统一为 \"suggests\" 或 \"provides exploratory evidence for\"。\n\n### 4.4 Limitations\n\n- **覆盖内容**（limitations.tex L4）：\n  - ✓ 合成数据 → upper bound（SOPBench +12.7pp as lower bound）\n  - ✓ Temperature=0 → modal interpretation only\n  - ✓ LLM annotator κ = 0.52 / human κ = 0.15\n  - ✓ 两个 customer-service domains\n  - ✓ 无 temp > 0 pilot data\n- **遗漏**：未讨论 auth-scope 的信息添加混淆（Table 2 脚注 ‡ 有标注但 Limitations 未提及）；未讨论 training data overlap 对 convergent nocuity 的影响。\n- **总体评估**：覆盖度 **adequate** 但不完整。关键限制已列出，语气诚实。\n\n### 4.5 Discussion + Conclusion\n\n**这是论文写作质量的最大短板**（与我此前 N2 一致）。\n- Discussion (discussion.tex): 1 段，约 80 词\n- Conclusion (conclusion.tex): 1 段，约 70 词\n- 合计约 150 词，占主文本不到 0.2 页\n\n对比之下，Method + Results + Error Analysis 占约 5 页。这种严重不平衡意味着论文在 \"what we found\" 上非常充分，但在 \"why it matters\" 上严重不足。\n\n---\n\n## 5. Excitement 与 Impact\n\n### 5.1 对实践者的影响\n\n**Moderate**。论文的核心实践启示是：(a) policy documents 应在 clause level 审计歧义而非 type level 评估风险；(b) prompt-level disambiguation 对 specification-layer 歧义（尤其 incompleteness）无效。\n\n但 \"how to fix\" 严重欠发展。Appendix B 的 mitigation experiment 是一个好的起点（type-specific prompts 比 generic prompts 有效），但 Discussion 未讨论实际部署建议。一位 practitioner 读完论文后知道 \"歧义有害\" 但不知道具体该怎么做。\n\n### 5.2 对后续研究的启发\n\n**Good**。论文打开了多条研究方向：\n- 非 customer-service domains（医疗、法律、金融）的歧义效应\n- Temperature > 0 下的 convergence patterns\n- Disambiguation channel 的系统性比较（clarification-seeking, multi-agent verification, structured uncertainty estimation）\n- Human mechanism annotations at scale\n- Incompleteness 的 specification-layer detection 工具\n\n但论文本身几乎未讨论这些方向（Conclusion 仅用 1 句提及 future work），削弱了 inspiration 效果。\n\n### 5.3 Venue 适配性\n\n**EMNLP 合适**。论文的核心贡献在 NLP/language 层面——taxonomy 基于语言学和 RE 分析，findings 关于 language ambiguity 如何影响 agent behavior。虽然 safety 领域也相关，但 agent safety venues（如 SafeAI workshop、AAAI Safety track）的读者群较小。SE conferences（ICSE, FSE）也可以考虑，但论文的 NLP framing 更适合 *CL 社区。\n\n---\n\n## 6. 格式合规\n\n| 检查项 | 状态 | 说明 |\n|--------|------|------|\n| 正文 ≤8 页 | ✓ | Pages 1-8（Conclusion 在 page 8 底部） |\n| 匿名 | ✓ | \"Anonymous ACL submission\"，匿名 GitHub URL |\n| Limitations | ✓ | Page 9，独立 section |\n| ACL 模板 | ✓ | `\\usepackage[review]{acl}`，main.tex L2 |\n| Abstract ≤200 词 | ✓ | ~160 词 |\n| 引用格式 | ✓ | natbib/ACL style，一致 |\n\n**潜在问题**：analysis.tex L37 使用 `\\enlargethispage{26\\baselineskip}`（约 4.3 英寸扩展），page 8 底部 margin 可能被大幅侵占。建议检查 ACL 模板的 margin 要求。\n\n---\n\n## 最终评分\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| **Overall Assessment** | **3.5** (Borderline Conference) | 方法论贡献扎实（causal design），实验执行充分；但 Discussion 过于简短，type–mechanism dissociation 证据不够稳固，概念包装（Berry inversion）略有过度 |\n| Soundness | 4/5 (Strong) | 控制链完整，统计方法规范，透明讨论限制 |\n| Excitement | 3/5 (Interesting) | 因果设计有方法论价值，disambiguation neglect 是好的实证发现；但 scope 窄（2 domains, temp=0），impact 部分严重欠发展 |\n| Confidence | 4/5 | 逐节精读全部 23 页含附录，核查了关键引用和数据 |\n\n**如何提升至 4.0 (Conference)**：\n1. 扩展 Discussion 至至少半页，分段讨论三项贡献的 theoretical implications 和 practical recommendations\n2. 在 Abstract/Introduction 中将 \"establishes\" 改为 \"suggests\"，与 [Exploratory] 标签统一\n3. 对 auth-scope 补充 incompleteness 同级别的 confound analysis\n4. 按模型家族分解 convergent nocuity，区分 training-data-driven vs. ambiguity-structure-driven convergence\n\n---\n\n[Reviewer 2 审稿结果]:\n已提交。报告覆盖了 Director 要求的全部 6 个评估维度：\n\n1. **新颖性**：causal design 是真正的方法论质变；disambiguation neglect 有实证新颖性；convergent nocuity 概念有趣但包装略过度；type–mechanism dissociation 证据不够稳固\n2. **Related Work**：RE、agent safety、psycholinguistics 覆盖充分（全部核心引用已确认）；prompt sensitivity 文献（Sclar et al.）未引用但属 nice-to-have\n3. **概念框架**：taxonomy well-motivated 但 two-layer 区分缺乏分析力（C3 未通过校正）；disambiguation channel 解释 post-hoc 但 testable；证据链为 convergent 而非 circular\n4. **写作**：Abstract/Introduction 质量高，但 Discussion+Conclusion 合计仅 150 词，严重不足\n5. **Excitement**：3/5，scope 窄且 impact 部分欠发展\n6. **格式**：全部合规，`\\enlargethispage` hack 值得注意\n\nOverall 维持 3.5 (Borderline Conference)。\n\n---\n\n[Reviewer 2 审稿意见]:\n## Reviewer 2 对 R1 Key Findings 的回应\n\n收到 R1 的方法论发现。逐条评估其对新颖性和整体评分的影响。\n\n---\n\n### 对 R1 方法论优势的回应\n\n**[AGREE] R1-S1: Perturbation control 的创新性**\n\n同意。perturbation control (§4.5, method.tex L28) 是论文因果推断链中的关键环节。Δ = −0.67pp (CI [−8.0, 6.67]) 排除了\"表面文本变化即可导致违规率变化\"的替代解释。R1 将其定位为 \"first explicit perturbation control in agent safety literature\" 我无法独立核实（需要更广泛的文献调查），但在我审阅的相关工作中确实未见类似设计。\n\n这一控制也与 prompt sensitivity 文献（Sclar et al. 2024）形成了有意义的对比——synonym substitution + clause reordering 本质上在测试弱形式的 prompt sensitivity，结果 (Δ ≈ 0) 说明本文测量的不是 surface prompt sensitivity 而是 semantic ambiguity effect。我在补充审查报告中建议在 Related Work 中加 1-2 句连接 Sclar et al.，R1 的这一观察强化了此建议。\n\n**[AGREE] R1-S2: Cross-family judging 设计**\n\n同意。Claude 由 GPT-5.4 评判、GPT-5.4 由 GPT-4.1 评判避免了 self-evaluation bias。Human calibration κ = 0.807 (method.tex L24) 接近 inter-annotator levels，验证了 pipeline 可靠性。\n\n**[AGREE] R1-S3: ICC test-retest + layer-aligned pattern**\n\n同意这是重要的 convergent evidence。ICC = 0.919 证明 test-retest 稳定性；linguistic layer (0.976-0.989) vs. specification layer (0.807-0.857) 的差异为 disambiguation channel framework 提供了独立于 failure mode coding 的结构性证据。这一点我在此前审稿中未单独提出——R1 的观察为 Section 6 的 exploratory findings 增加了一条独立的支撑线索，值得 authors 在 Discussion 中更明确地整合。\n\n**[AGREE] R1-S4: TOST 等价检验的分析选择**\n\n同意。TOST with 7-margin sensitivity (Appendix A) 避免了对单一 SESOI 的依赖。我在 Round 1 审稿 Strengths 中已列此项。\n\n---\n\n### 对 R1 方法论关切的回应及其对新颖性/excitement 的影响\n\n**[REBUT] R1-Concern-1: C2 pairwise comparisons 缺乏多重比较校正**\n\n部分不同意。论文在 method.tex L34 中明确说明：\"We apply Holm-Bonferroni correction within three pre-registered test families (Appendix K)\"。Appendix K (appendix.tex) 报告了 Holm-Bonferroni 校正结果。C2 的 omnibus χ² 已通过校正，post-hoc pairwise 分析使用 TOST 等价检验（Appendix A）而非显著性检验——TOST 框架下的多重比较逻辑与传统 pairwise significance testing 不同（TOST 是判断等价而非差异，Type I error 的含义不同）。\n\n不过 R1 的关切有一定道理：论文确实在 §5.2 中对 6 types 的 pairwise ordering 做了讨论性比较，虽然使用了 TOST equivalence framework 而非 significance testing，但读者可能混淆两种框架。建议在 §5.2 中增加一句明确说明 pairwise 比较使用 TOST（等价性判断）而非 significance testing，以消除方法论歧义。\n\n**对新颖性影响**：**无**。C2 的核心 claim 是 \"types form a partial ordering with robust extremes\"——这基于 bootstrap clustering (Appendix I) 和 TOST sensitivity analysis (Appendix A) 两条独立证据链，不受 pairwise significance correction 的影响。\n\n---\n\n**[AGREE] R1-Concern-2: Per-cell N=50 对 C4 interaction 的统计功效**\n\n同意。C4 (model×type interaction) 的每个 cell 仅 N=50。auth-scope 的 52pp range 足够大，但 cond-prec 的 6pp range 在 N=50 下几乎无法可靠检测。论文在 §5.2 和 experiments.tex L53-54 中将 C4 定位为 exploratory 是正确的。\n\n**对新颖性影响**：**有限**。C4 不是论文的核心贡献。论文将其标为 exploratory 是恰当的 hedging。\n\n---\n\n**[REBUT] R1-Concern-3: Reproducibility gaps (temperature/prompts/API versions)**\n\n不同意此为重大 gap。论文在 method.tex L16 明确报告：\n- Temperature = 0 ✓\n- top_p = 1 ✓  \n- max_tokens = 4096 ✓\n- API call date: May 20, 2026 ✓\n\nR1 说 \"No temperature settings reported\" 与原文不符。prompt templates 未在正文中展示，但 Appendix B (appendix.tex L31) 展示了 mitigation prompt template，Appendix T 描述了 clause pair 构建细节，且论文承诺数据开源。API 版本通过日期间接指定（\"were made on May 20, 2026\"）。\n\n**对新颖性影响**：**无**。Reproducibility 是 quality 问题而非 novelty 问题。\n\n---\n\n**[AGREE] R1-Concern-4: 生态效度的局限性**\n\n同意生态效度 \"adequate but not definitive\"。SOPBench 效应缩小至 37% (+12.7pp vs +34.0pp) 是最有力的生态效度信号。我在补充审查中已将此列入 Excitement 评估——合成 clause pairs 的效应量可能显著高估真实部署场景的风险。\n\n**对新颖性影响**：**间接影响**。不影响因果设计的方法论新颖性，但影响 practical significance 的判断。如果真实效应更接近 +12.7pp 而非 +34.0pp，论文的实践影响力需下调。\n\n---\n\n**[AGREE with nuance] R1-Concern-5: SOPBench replication 的局限**\n\n同意 N=100 和 4/6 types 是局限。但需补充上下文：\n- SOPBench 本身是一个已有的独立 benchmark (Li et al., 2025)，不是 authors 自建的；其 policy 结构与 τ²-bench 根本不同\n- 4/6 types 是因为 SOPBench 的 SOP 格式不支持 coreferential 和（可能）某些其他类型\n- 效应方向一致 (all positive) 且 3/5 models 显著，作为 directional replication 已有价值\n\n**对新颖性影响**：**无**。SOPBench replication 是 robustness check 而非 novelty claim。\n\n---\n\n**[AGREE] R1-Concern-6: Human annotation 局限**\n\n完全同意，与我的 N1 高度重叠。2 annotators × 100 traces × κ = 0.52 (failure mode) / κ = 0.15 (raw) 是整篇论文证据链中最薄弱的环节。这直接影响 contribution (3) type–mechanism dissociation 的可信度。\n\n**对新颖性影响**：**显著**。这是 R1 的方法论关切中对新颖性影响最大的一条。如果 failure mechanism coding 不可靠，type–mechanism dissociation 这一\"概念新颖性\"就缺乏稳固的实证基础。论文的 [Exploratory] 标签是正确的 hedge，但 Abstract/Introduction 的表述与之不一致。\n\n---\n\n### 综合评估：R1 的方法论关切是否影响新颖性判断和整体评分？\n\n**新颖性判断不变**：\n- Contribution (1) (causal effect): R1 的方法论优势发现（perturbation control、ICC、cross-family judging）实际上**加强了**这一贡献的可信度。方法论创新性充分。\n- Contribution (2) (disambiguation neglect + systematic nocuity): 不受 R1 关切的实质影响。4.6% awareness 和 41.3% convergence 基于主实验数据，不依赖 failure mode coding。\n- Contribution (3) (type–mechanism dissociation): R1-Concern-6 (human annotation) 与我的 N1 独立 converge，**确认**这是论文最弱的概念贡献。\n\n**整体评分不变：3.5 (Borderline Conference)**。\n\nR1 的方法论审查整体上是 favorable 的（4 个 strengths vs. 6 个 concerns，其中 concern-3 我不同意）。R1 给出 3.5-4.0 的区间与我的 3.5 一致。\n\n两位 Reviewer 的**核心共识**是：\n1. Contribution (1) 方法论扎实，是论文的主要价值来源\n2. Contribution (3) 证据不够稳固，需要 downgrade 表述\n3. Discussion 过于简短（R1 未直接提出但 R1 的 \"how to fix\" 关切间接指向同一问题）\n4. 生态效度 adequate 但 SOPBench 效应缩小需更多讨论\n\n**升至 4.0 的条件**不变（见我此前补充审查末尾的 4 点建议）。\n\n---\n\n### R1 分数对比\n\n| 维度 | R1 | R2 | 差异 |\n|------|-----|-----|------|\n| Soundness | 4/5 | 4/5 | 一致 |\n| Reproducibility | 3.5/5 | 4/5 | R1 较严（我认为 R1-Concern-3 关于 temperature/prompts 的批评与原文不符） |\n| Overall | 3.5-4.0 | 3.5 | 基本一致 |\n| Excitement | 3.5/5 | 3/5 | R1 略高；我认为 Discussion 的严重不足和 impact 部分的欠发展拉低了 excitement |\n\n---\n\n[Reviewer 2 审稿结果]:\n审稿意见已提交。\n\n三轮审稿（Round 1 初审、R1 交叉回应、补充深度审查、R1 Key Findings 回应）均已完成。核心结论：\n\n- **Overall: 3.5 (Borderline Conference)**\n- Contribution (1) causal design 是最扎实的贡献（两位 Reviewer 一致认可）\n- Contribution (3) type–mechanism dissociation 证据最弱（两位 Reviewer 独立 converge）\n- Discussion 过于简短是最可修复的提分点"
}
```

---


### Runtime record

_source line 192 · 2026-05-23T20:02:05.824Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-23T20:02:05.824Z",
  "sessionId": "a12edc2b-318d-49ec-adb5-ee9cfa431360"
}
```

---


## Round 15

## Round 15

2 recorded events


### User

_source line 193 · 2026-05-23T20:02:05.805Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d9590c3-9a53-46ac-9117-92134488a482",
  "isSidechain": false,
  "promptId": "fa3d9c11-e599-4e0b-8a6a-865ce5431404",
  "type": "user",
  "isMeta": true,
  "uuid": "77b8d3cc-c850-4bf6-9ba4-dc96b7dce85f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/review_director_0e80b40a",
  "sessionId": "a12edc2b-318d-49ec-adb5-ee9cfa431360",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Assistant

_source line 194 · 2026-05-23T20:02:05.806Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77b8d3cc-c850-4bf6-9ba4-dc96b7dce85f",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "9bd2ff8f-830a-4783-8676-23dd7326592a",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/review_director_0e80b40a",
  "sessionId": "a12edc2b-318d-49ec-adb5-ee9cfa431360",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "id": "089fa6a5-bc4c-4553-b8a2-6093ea56f2b1",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---


## Round 16

## Round 16

3 recorded events


### User

_source line 195 · 2026-05-23T20:02:06.055Z_

[SYSTEM] Research Reviewer 刚完成 context rotation (Loop 5)，已读取 handoff 并就绪。如有待办任务请立即分配。

---

[Reviewer 1 审稿结果]:
审稿意见已提交。

总结：经过审慎考虑 R2 的 cross-share 意见后，我维持 Overall 3.5 (Borderline Conference) 不变。同意 R2 对研究新颖性和概念贡献的肯定，但从方法严谨性角度，三个核心问题（信息添加混淆未全面控制、mechanism analysis circularity、temperature=0 唯一条件）阻止升至 4.0。与 R2 的 0.5 分分歧主要来自不同的评价权重：R2 偏重概念新颖性，我偏重方法完备性。

---

[Reviewer 2 审稿意见]:
## Reviewer 2 补充审查报告：新颖性 + Related Work + 概念框架 + 写作 + 影响力

**说明**：此报告基于我对论文全部 23 页 PDF 和关键 LaTeX 源文件的精读，按 Director 指定的 6 个评估维度展开。分数与我此前提交的 Round 1 审稿一致（Overall 3.5）。

**标题核对**：Director 任务描述中的标题 "Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families" 与我实际审阅的论文标题 "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety" 不一致。以下审查基于实际论文内容。Director 描述中的部分术语（"Differential Nocuity"、"Ambiguity Blindness"、"27% all-model convergence"）也与论文实际使用的术语和数据有差异——论文使用 "systematic nocuity"、"disambiguation neglect"、13.0% unanimous / 41.3% majority-convergent。

---

## 1. 新颖性评估

### 1.1 研究问题新颖性

**"Has anyone causally measured ambiguity→safety violations before?"**

据我所知，**没有**。DRIP-R (Vijayvarrgiya et al., 2026b) 是最接近的并发工作，但使用相关性设计（400 scenarios, 5 RE ambiguity types, 测量 decision quality 而非 safety violations）。论文在 Related Work §2 (related_work.tex L14) 中明确对比了差异："DRIP-R's correlational design leaves open whether ambiguity *causes* violations or merely co-occurs with harder scenarios; our matched-pair controls (Δ_perturb = −0.67 pp) isolate the causal contribution."

**评估**：matched-pair causal design 是对该领域的**方法论质变**（从相关性到因果性）。Perturbation control (+perturbation 效应含零 CI)、ICC replicability (0.919)、SOPBench 跨基准复现构成了完整的因果推断控制链。这是论文最扎实的新颖性来源。

### 1.2 "Systematic Nocuity" / "Convergent Nocuity" 是否为真正的概念推进？

论文在 Introduction (introduction.tex L6) 中定义 convergent nocuity："Unlike human teams, where convergence reflects shared domain knowledge, agent convergence reflects shared training biases operating on identical inputs." 并在 Section 6.3 (analysis.tex L33-35) 报告：41.3% 的歧义 clause 触发 majority-convergent violations (≥3/5 models agree), 13.0% unanimous, 77.0% permissive bias。

**评估**：这不是简单地"应用一个现有框架"，而是指出了 Berry & Kamsties (2004) 框架在 LLM 语境下的一个**根本性假设失败**——B&K 假设 convergence = innocuous（因为来自共享领域知识），但 LLM 的 convergence 来自 shared training biases，是一种完全不同的机制。这是一个**genuine conceptual insight**。

**但有两个重要限制**（与我此前审稿的 W1 一致）：
1. **概念包装过度**：论文称此为 "inverting Berry's framework"（Introduction L6），但更准确的表述是 "Berry's framework breaks down for LLMs"。Berry 的框架从未声称适用于 AI agents；论文发现的是框架的**适用边界**，而非框架本身的"反转"。
2. **训练数据混淆**：41.3% 的跨模型收敛可能部分源于 shared pre-training data（WebText, CommonCrawl），而非歧义文本的内在结构特征。论文未按模型家族分解收敛模式（OpenAI 内部 vs. 跨厂商）。如果收敛主要发生在同族模型间，systematic nocuity 的普遍性结论需下调。

### 1.3 "Disambiguation Neglect" (<5% awareness) 是否意外？

论文报告 4.6% 歧义意识率（Section 6.2, analysis.tex L28-30）。

**评估**：介于 "novel" 和 "expected" 之间。
- **Expected 的方面**：Liu et al. (2023) 已证明 LLMs 在表示层面进行 ambiguity collapse（将多种解释压缩为单一表示）。从 representation collapse 推导到 behavioral neglect 并非大跳跃。
- **Novel 的方面**：(a) 量化程度前所未有（4.6% vs. 此前仅有定性观察）；(b) 从表示层扩展到**行为层**——agents 不仅在内部 collapse 解释，还在行为上从不 flag 歧义、直接产生不可逆安全违规，这是一个有实践意义的新发现；(c) 跨 5 个模型的一致性增强了发现的稳健性。
- **关键缺陷**：在 temperature=0 下，每个 model-clause pair 仅有一个确定性输出，agent 没有"机会"在不同 runs 中展现不同程度的意识。4.6% 可能低估了 stochastic sampling 下的意识率。

### 1.4 Type–Mechanism Dissociation

V = 0.45 (LLM-coded, 6×5 table, 95% CI [0.41, 0.50])，human κ = 0.15 (raw), 0.34–0.52 (collapsed)。

**评估**：**概念有趣但证据不够稳固**。如我此前 N1 所述，human κ = 0.15 意味着人类标注者几乎无法可靠区分 failure mechanisms。V = 0.45 的 LLM 编码一致性可能反映 LLM coder 的 shared bias 而非真正的 type→mechanism 映射。论文正确标记 Section 6 为 "[Exploratory]"，但 Abstract/Introduction 的 "establishes" 表述过强。

---

## 2. Related Work 覆盖评估

### Requirements Engineering

| 引用 | 状态 | 评估 |
|------|------|------|
| Berry & Kamsties (2004) | ✓ 核心引用 | 充分讨论，nocuous/innocuous 框架是论文理论基础 |
| Chantree et al. (2006) | ✓ 已引用 | related_work.tex L5: "from heuristic methods (Chantree et al., 2006; Willis et al., 2008)" |
| Ferrari et al. (2018, 2019) | ✓ 已引用 | 两篇均引用 |
| Willis et al. (2008) | ✓ 已引用 | 与 Chantree 一起引用 |
| Ezzini et al. (2022) | ✓ 已引用 | 两篇 Ezzini 均引用（TAPHSIR + anaphoric） |
| Massey et al. (2014) | ✓ 已引用 | taxonomy.tex 中引用，6 种 RE 歧义类型 |

**评估**：RE 覆盖**充分**，核心文献无遗漏。

### Agent Safety

| 引用 | 状态 | 评估 |
|------|------|------|
| ToolEmu (Ruan et al. 2024) | ✓ 已引用 | related_work.tex L11 |
| InjecAgent (Zhan et al. 2024) | ✓ 已引用 | related_work.tex L11 |
| R-Judge | ✓ 已引用 | related_work.tex L11 |
| τ²-bench (Barres et al. 2025) | ✓ 核心引用 | 实验平台 |
| AgentPex (Sharma et al. 2026) | ✓ 已引用 | related_work.tex L14 |
| DRIP-R (Vijayvarrgiya et al. 2026) | ✓ 详细对比 | 最主要的并发工作，Appendix L 有分类映射 |

**评估**：Agent safety 覆盖**充分且详细**。论文还引用了多个 Director 未列出的相关工作（PolicyBank, SOPBench, MANTRA, SafeAgentBench 等）。

### Prompt Sensitivity

| 引用 | 状态 | 评估 |
|------|------|------|
| Sclar et al. (2024) | ✗ 未引用 | 关于 prompt design 敏感性的定量研究 |
| Lu et al. (2022) | ✗ 未引用 | prompt ordering effects |
| Zhou et al. (2022) | ✗ 未引用 | automatic prompt engineering |

**评估**：prompt sensitivity 文献**未被引用**，但这是否为重大遗漏取决于 scope 判断。论文关注的是**policy specification 中的歧义**（一种语义层面的变异），而非**prompt phrasing 的表面敏感性**（格式、排序等）。Sclar et al. 的工作讨论的是 spurious features（标点、大小写、formatting），与 policy ambiguity（语义多义性）在概念层面有区别。但论文的 perturbation control (§4.5: synonym substitution, clause reordering → Δ = −0.67 pp) 本质上在测试一种弱形式的 prompt sensitivity，与 Sclar et al. 有交集。

**建议**：在 Related Work 中加 1-2 句连接 prompt sensitivity 文献，说明本文的 perturbation control 与该领域的关系。不属于 must-cite 但会加强论文的 positioning。

### NLP Ambiguity

| 引用 | 状态 | 评估 |
|------|------|------|
| Poesio & Artstein (2005) | ✓ 已引用 | taxonomy.tex 中引用 |
| Bender (e.g., Bender & Koller 2020) | ✗ 未引用 | "Climbing towards NLU" |
| Wasow et al. (2005) | ✓ 已引用 | taxonomy.tex 中引用 |
| Liu et al. (2023) | ✓ 已引用 | ambiguity collapse |
| Gur-Arieh et al. (2026) | ✓ 已引用 | ambiguity collapse taxonomy |

**评估**：NLP ambiguity 覆盖**充分**。Bender & Koller (2020) 关于 language understanding 的讨论与本文 scope 交叉有限，不属于必要引用。论文引用了更直接相关的 psycholinguistics 文献（Ferreira 2002, Frazier & Rayner 1982, Hu et al. 2023）。

### 总体 Related Work 评估

**覆盖度评分：4/5 (Strong)**。所有核心 RE、agent safety、psycholinguistics 引用均已覆盖。唯一可改进的是加入 prompt sensitivity 文献作为对比 positioning，但这属于 "nice-to-have" 而非必要。

---

## 3. 概念框架质量

### 3.1 Two-layer taxonomy

论文将 6 种歧义类型组织为两层——specification layer（incompleteness, conditional precedence, coreferential）和 linguistic layer（lexical, scopal, authorization scope）。来源：Li et al. (2024) 的 11-type NLP taxonomy + Massey et al. (2014) 的 6-type RE taxonomy。

**评估**：
- **Well-motivated**：Section 3 (taxonomy.tex) 明确说明了选择标准——(1) theoretical attestation in prior RE literature, (2) minimal-pair constructability, (3) mutual exclusivity for unambiguous PV assignment。
- **但两层结构在分析中作用有限**：C3（layer grouping effect）未通过 Holm-Bonferroni 校正（experiments.tex L55: p = 0.017, threshold 0.0125）。论文诚实地报告了这一结果，但这意味着 two-layer 组织是一个**描述性分类而非有分析力的 structural distinction**。
- **Authorization scope 的归属可疑**：auth-scope 被归入 linguistic layer，但其本质更接近 specification-layer 问题（permissions 和 boundaries 属于 policy specification 而非语言结构）。Table 13 显示 auth-scope 的 Δtoken (+36.1) 远高于其他 linguistic-layer 类型（lexical +25.7, scopal +17.8），行为模式也更接近 specification-layer。这一分类选择可能人为地弱化了 layer-level 效应（C3）。

### 3.2 "Disambiguation channel" 解释

Introduction (L6): "LLM agents lack these disambiguation channels. They cannot consult colleagues, rarely escalate to users, and must resolve ambiguity in real time from the text alone."

**评估**：
- **直觉合理但未被直接测试**。论文的实验设计不操纵 disambiguation channels（没有 "with channel" vs. "without channel" 条件）。
- **但有间接支撑**：Appendix B 的 mitigation experiment 测试了一种简单的 disambiguation instruction，结果显示 type-dependent effectiveness（auth-scope −18.0pp, lexical −8.9pp, incompleteness −3.4pp n.s.）。这间接说明 disambiguation 能力因类型而异——specification-layer 缺失信息无法从 prompt alone 恢复。
- **Vijayvargiya et al. (2026) 的 74% recovery** (related_work.tex L8) 提供了正向证据：当 disambiguation channel 可用时（interactive clarification），underspecification 的影响大幅减少。
- **总体判断**：post-hoc 但 testable，有间接证据支撑。不是 circular reasoning，但也不是直接验证。

### 3.3 ICC pattern → failure modes → disambiguation channels 的证据链

- ICC pattern：clause identity 解释 22.4% variance, type 仅 0.4%（Appendix AC, Figure 2）
- Failure modes：V = 0.45 type→mechanism（Section 6, LLM-coded）
- Disambiguation channels：概念性解释，未直接测试

**评估**：三者之间是**convergent evidence 而非 circular reasoning**。
- ICC 分析不依赖 failure mode coding（纯数值方差分解）
- Failure mode coding 不依赖 ICC（独立的分类任务）
- Disambiguation channel 是 interpretive framework，不进入任何定量分析

每个分析层面使用独立的数据和方法，然后在 Discussion 中整合解释。这是合理的科学推理结构。但 Discussion (discussion.tex) 仅用约 80 词整合这些证据，远不足以让读者看到 convergent evidence 的力度。

---

## 4. 写作质量

### 4.1 Abstract

- **字数**：约 160 词（LaTeX 源文件 abstract.tex），**符合 ≤200 词要求**。
- **贡献清晰度**：三个核心数字（+34.0/+31.0 pp, V = 0.45, 4.6% awareness）均出现在 Abstract 中。
- **问题**：(a) 仅报告 collapsed κ = 0.34–0.52，未报告 raw κ = 0.15，可能误导读者对 human agreement 的判断；(b) "establishes the taxonomy as a diagnostic instrument" 用词过强（与 Section 6 的 [Exploratory] 标签矛盾）。

### 4.2 Introduction

- **Opening vignette**（Introduction L4）：scopal ambiguity 导致 $200 损失的客服案例，**有效**——具体、可感、直接说明实际危害。
- **Gap statement**（Introduction L8）："no existing study provides a causal, type-granularity mapping from ambiguity to safety violations"——**清晰且准确**。我核查了相关工作，未找到反例。
- **叙事弧**：problem（§1 L4-6）→ gap（§1 L8）→ method（§1 L17）→ findings（§1 L19-21）→ contributions（§1 L21），结构**清晰完整**。
- **Berry 框架引入**（Introduction L6）：2 段话阐述 convergent nocuity 的概念，篇幅恰当。但 "inverting Berry's framework" 的表述偏激进（见 1.2 节评估）。

### 4.3 Claim 标定

- C1/C2: "supported" — 合理（统计证据充分）
- C3 (layer effect): 报告 "did not survive Holm-Bonferroni" (experiments.tex L55) — **非常诚实**
- Section 6: 标记为 "[Exploratory]" — 正确
- **但**：Abstract/Introduction 中 "establishes" 与 [Exploratory] 矛盾。应统一为 "suggests" 或 "provides exploratory evidence for"。

### 4.4 Limitations

- **覆盖内容**（limitations.tex L4）：
  - ✓ 合成数据 → upper bound（SOPBench +12.7pp as lower bound）
  - ✓ Temperature=0 → modal interpretation only
  - ✓ LLM annotator κ = 0.52 / human κ = 0.15
  - ✓ 两个 customer-service domains
  - ✓ 无 temp > 0 pilot data
- **遗漏**：未讨论 auth-scope 的信息添加混淆（Table 2 脚注 ‡ 有标注但 Limitations 未提及）；未讨论 training data overlap 对 convergent nocuity 的影响。
- **总体评估**：覆盖度 **adequate** 但不完整。关键限制已列出，语气诚实。

### 4.5 Discussion + Conclusion

**这是论文写作质量的最大短板**（与我此前 N2 一致）。
- Discussion (discussion.tex): 1 段，约 80 词
- Conclusion (conclusion.tex): 1 段，约 70 词
- 合计约 150 词，占主文本不到 0.2 页

对比之下，Method + Results + Error Analysis 占约 5 页。这种严重不平衡意味着论文在 "what we found" 上非常充分，但在 "why it matters" 上严重不足。

---

## 5. Excitement 与 Impact

### 5.1 对实践者的影响

**Moderate**。论文的核心实践启示是：(a) policy documents 应在 clause level 审计歧义而非 type level 评估风险；(b) prompt-level disambiguation 对 specification-layer 歧义（尤其 incompleteness）无效。

但 "how to fix" 严重欠发展。Appendix B 的 mitigation experiment 是一个好的起点（type-specific prompts 比 generic prompts 有效），但 Discussion 未讨论实际部署建议。一位 practitioner 读完论文后知道 "歧义有害" 但不知道具体该怎么做。

### 5.2 对后续研究的启发

**Good**。论文打开了多条研究方向：
- 非 customer-service domains（医疗、法律、金融）的歧义效应
- Temperature > 0 下的 convergence patterns
- Disambiguation channel 的系统性比较（clarification-seeking, multi-agent verification, structured uncertainty estimation）
- Human mechanism annotations at scale
- Incompleteness 的 specification-layer detection 工具

但论文本身几乎未讨论这些方向（Conclusion 仅用 1 句提及 future work），削弱了 inspiration 效果。

### 5.3 Venue 适配性

**EMNLP 合适**。论文的核心贡献在 NLP/language 层面——taxonomy 基于语言学和 RE 分析，findings 关于 language ambiguity 如何影响 agent behavior。虽然 safety 领域也相关，但 agent safety venues（如 SafeAI workshop、AAAI Safety track）的读者群较小。SE conferences（ICSE, FSE）也可以考虑，但论文的 NLP framing 更适合 *CL 社区。

---

## 6. 格式合规

| 检查项 | 状态 | 说明 |
|--------|------|------|
| 正文 ≤8 页 | ✓ | Pages 1-8（Conclusion 在 page 8 底部） |
| 匿名 | ✓ | "Anonymous ACL submission"，匿名 GitHub URL |
| Limitations | ✓ | Page 9，独立 section |
| ACL 模板 | ✓ | `\usepackage[review]{acl}`，main.tex L2 |
| Abstract ≤200 词 | ✓ | ~160 词 |
| 引用格式 | ✓ | natbib/ACL style，一致 |

**潜在问题**：analysis.tex L37 使用 `\enlargethispage{26\baselineskip}`（约 4.3 英寸扩展），page 8 底部 margin 可能被大幅侵占。建议检查 ACL 模板的 margin 要求。

---

## 最终评分

| 维度 | 分数 | 理由 |
|------|------|------|
| **Overall Assessment** | **3.5** (Borderline Conference) | 方法论贡献扎实（causal design），实验执行充分；但 Discussion 过于简短，type–mechanism dissociation 证据不够稳固，概念包装（Berry inversion）略有过度 |
| Soundness | 4/5 (Strong) | 控制链完整，统计方法规范，透明讨论限制 |
| Excitement | 3/5 (Interesting) | 因果设计有方法论价值，disambiguation neglect 是好的实证发现；但 scope 窄（2 domains, temp=0），impact 部分严重欠发展 |
| Confidence | 4/5 | 逐节精读全部 23 页含附录，核查了关键引用和数据 |

**如何提升至 4.0 (Conference)**：
1. 扩展 Discussion 至至少半页，分段讨论三项贡献的 theoretical implications 和 practical recommendations
2. 在 Abstract/Introduction 中将 "establishes" 改为 "suggests"，与 [Exploratory] 标签统一
3. 对 auth-scope 补充 incompleteness 同级别的 confound analysis
4. 按模型家族分解 convergent nocuity，区分 training-data-driven vs. ambiguity-structure-driven convergence

---

[Reviewer 2 审稿结果]:
已提交。报告覆盖了 Director 要求的全部 6 个评估维度：

1. **新颖性**：causal design 是真正的方法论质变；disambiguation neglect 有实证新颖性；convergent nocuity 概念有趣但包装略过度；type–mechanism dissociation 证据不够稳固
2. **Related Work**：RE、agent safety、psycholinguistics 覆盖充分（全部核心引用已确认）；prompt sensitivity 文献（Sclar et al.）未引用但属 nice-to-have
3. **概念框架**：taxonomy well-motivated 但 two-layer 区分缺乏分析力（C3 未通过校正）；disambiguation channel 解释 post-hoc 但 testable；证据链为 convergent 而非 circular
4. **写作**：Abstract/Introduction 质量高，但 Discussion+Conclusion 合计仅 150 词，严重不足
5. **Excitement**：3/5，scope 窄且 impact 部分欠发展
6. **格式**：全部合规，`\enlargethispage` hack 值得注意

Overall 维持 3.5 (Borderline Conference)。

---

[Reviewer 2 审稿意见]:
## Reviewer 2 对 R1 Key Findings 的回应

收到 R1 的方法论发现。逐条评估其对新颖性和整体评分的影响。

---

### 对 R1 方法论优势的回应

**[AGREE] R1-S1: Perturbation control 的创新性**

同意。perturbation control (§4.5, method.tex L28) 是论文因果推断链中的关键环节。Δ = −0.67pp (CI [−8.0, 6.67]) 排除了"表面文本变化即可导致违规率变化"的替代解释。R1 将其定位为 "first explicit perturbation control in agent safety literature" 我无法独立核实（需要更广泛的文献调查），但在我审阅的相关工作中确实未见类似设计。

这一控制也与 prompt sensitivity 文献（Sclar et al. 2024）形成了有意义的对比——synonym substitution + clause reordering 本质上在测试弱形式的 prompt sensitivity，结果 (Δ ≈ 0) 说明本文测量的不是 surface prompt sensitivity 而是 semantic ambiguity effect。我在补充审查报告中建议在 Related Work 中加 1-2 句连接 Sclar et al.，R1 的这一观察强化了此建议。

**[AGREE] R1-S2: Cross-family judging 设计**

同意。Claude 由 GPT-5.4 评判、GPT-5.4 由 GPT-4.1 评判避免了 self-evaluation bias。Human calibration κ = 0.807 (method.tex L24) 接近 inter-annotator levels，验证了 pipeline 可靠性。

**[AGREE] R1-S3: ICC test-retest + layer-aligned pattern**

同意这是重要的 convergent evidence。ICC = 0.919 证明 test-retest 稳定性；linguistic layer (0.976-0.989) vs. specification layer (0.807-0.857) 的差异为 disambiguation channel framework 提供了独立于 failure mode coding 的结构性证据。这一点我在此前审稿中未单独提出——R1 的观察为 Section 6 的 exploratory findings 增加了一条独立的支撑线索，值得 authors 在 Discussion 中更明确地整合。

**[AGREE] R1-S4: TOST 等价检验的分析选择**

同意。TOST with 7-margin sensitivity (Appendix A) 避免了对单一 SESOI 的依赖。我在 Round 1 审稿 Strengths 中已列此项。

---

### 对 R1 方法论关切的回应及其对新颖性/excitement 的影响

**[REBUT] R1-Concern-1: C2 pairwise comparisons 缺乏多重比较校正**

部分不同意。论文在 method.tex L34 中明确说明："We apply Holm-Bonferroni correction within three pre-registered test families (Appendix K)"。Appendix K (appendix.tex) 报告了 Holm-Bonferroni 校正结果。C2 的 omnibus χ² 已通过校正，post-hoc pairwise 分析使用 TOST 等价检验（Appendix A）而非显著性检验——TOST 框架下的多重比较逻辑与传统 pairwise significance testing 不同（TOST 是判断等价而非差异，Type I error 的含义不同）。

不过 R1 的关切有一定道理：论文确实在 §5.2 中对 6 types 的 pairwise ordering 做了讨论性比较，虽然使用了 TOST equivalence framework 而非 significance testing，但读者可能混淆两种框架。建议在 §5.2 中增加一句明确说明 pairwise 比较使用 TOST（等价性判断）而非 significance testing，以消除方法论歧义。

**对新颖性影响**：**无**。C2 的核心 claim 是 "types form a partial ordering with robust extremes"——这基于 bootstrap clustering (Appendix I) 和 TOST sensitivity analysis (Appendix A) 两条独立证据链，不受 pairwise significance correction 的影响。

---

**[AGREE] R1-Concern-2: Per-cell N=50 对 C4 interaction 的统计功效**

同意。C4 (model×type interaction) 的每个 cell 仅 N=50。auth-scope 的 52pp range 足够大，但 cond-prec 的 6pp range 在 N=50 下几乎无法可靠检测。论文在 §5.2 和 experiments.tex L53-54 中将 C4 定位为 exploratory 是正确的。

**对新颖性影响**：**有限**。C4 不是论文的核心贡献。论文将其标为 exploratory 是恰当的 hedging。

---

**[REBUT] R1-Concern-3: Reproducibility gaps (temperature/prompts/API versions)**

不同意此为重大 gap。论文在 method.tex L16 明确报告：
- Temperature = 0 ✓
- top_p = 1 ✓  
- max_tokens = 4096 ✓
- API call date: May 20, 2026 ✓

R1 说 "No temperature settings reported" 与原文不符。prompt templates 未在正文中展示，但 Appendix B (appendix.tex L31) 展示了 mitigation prompt template，Appendix T 描述了 clause pair 构建细节，且论文承诺数据开源。API 版本通过日期间接指定（"were made on May 20, 2026"）。

**对新颖性影响**：**无**。Reproducibility 是 quality 问题而非 novelty 问题。

---

**[AGREE] R1-Concern-4: 生态效度的局限性**

同意生态效度 "adequate but not definitive"。SOPBench 效应缩小至 37% (+12.7pp vs +34.0pp) 是最有力的生态效度信号。我在补充审查中已将此列入 Excitement 评估——合成 clause pairs 的效应量可能显著高估真实部署场景的风险。

**对新颖性影响**：**间接影响**。不影响因果设计的方法论新颖性，但影响 practical significance 的判断。如果真实效应更接近 +12.7pp 而非 +34.0pp，论文的实践影响力需下调。

---

**[AGREE with nuance] R1-Concern-5: SOPBench replication 的局限**

同意 N=100 和 4/6 types 是局限。但需补充上下文：
- SOPBench 本身是一个已有的独立 benchmark (Li et al., 2025)，不是 authors 自建的；其 policy 结构与 τ²-bench 根本不同
- 4/6 types 是因为 SOPBench 的 SOP 格式不支持 coreferential 和（可能）某些其他类型
- 效应方向一致 (all positive) 且 3/5 models 显著，作为 directional replication 已有价值

**对新颖性影响**：**无**。SOPBench replication 是 robustness check 而非 novelty claim。

---

**[AGREE] R1-Concern-6: Human annotation 局限**

完全同意，与我的 N1 高度重叠。2 annotators × 100 traces × κ = 0.52 (failure mode) / κ = 0.15 (raw) 是整篇论文证据链中最薄弱的环节。这直接影响 contribution (3) type–mechanism dissociation 的可信度。

**对新颖性影响**：**显著**。这是 R1 的方法论关切中对新颖性影响最大的一条。如果 failure mechanism coding 不可靠，type–mechanism dissociation 这一"概念新颖性"就缺乏稳固的实证基础。论文的 [Exploratory] 标签是正确的 hedge，但 Abstract/Introduction 的表述与之不一致。

---

### 综合评估：R1 的方法论关切是否影响新颖性判断和整体评分？

**新颖性判断不变**：
- Contribution (1) (causal effect): R1 的方法论优势发现（perturbation control、ICC、cross-family judging）实际上**加强了**这一贡献的可信度。方法论创新性充分。
- Contribution (2) (disambiguation neglect + systematic nocuity): 不受 R1 关切的实质影响。4.6% awareness 和 41.3% convergence 基于主实验数据，不依赖 failure mode coding。
- Contribution (3) (type–mechanism dissociation): R1-Concern-6 (human annotation) 与我的 N1 独立 converge，**确认**这是论文最弱的概念贡献。

**整体评分不变：3.5 (Borderline Conference)**。

R1 的方法论审查整体上是 favorable 的（4 个 strengths vs. 6 个 concerns，其中 concern-3 我不同意）。R1 给出 3.5-4.0 的区间与我的 3.5 一致。

两位 Reviewer 的**核心共识**是：
1. Contribution (1) 方法论扎实，是论文的主要价值来源
2. Contribution (3) 证据不够稳固，需要 downgrade 表述
3. Discussion 过于简短（R1 未直接提出但 R1 的 "how to fix" 关切间接指向同一问题）
4. 生态效度 adequate 但 SOPBench 效应缩小需更多讨论

**升至 4.0 的条件**不变（见我此前补充审查末尾的 4 点建议）。

---

### R1 分数对比

| 维度 | R1 | R2 | 差异 |
|------|-----|-----|------|
| Soundness | 4/5 | 4/5 | 一致 |
| Reproducibility | 3.5/5 | 4/5 | R1 较严（我认为 R1-Concern-3 关于 temperature/prompts 的批评与原文不符） |
| Overall | 3.5-4.0 | 3.5 | 基本一致 |
| Excitement | 3.5/5 | 3/5 | R1 略高；我认为 Discussion 的严重不足和 impact 部分的欠发展拉低了 excitement |

---

[Reviewer 2 审稿结果]:
审稿意见已提交。

三轮审稿（Round 1 初审、R1 交叉回应、补充深度审查、R1 Key Findings 回应）均已完成。核心结论：

- **Overall: 3.5 (Borderline Conference)**
- Contribution (1) causal design 是最扎实的贡献（两位 Reviewer 一致认可）
- Contribution (3) type–mechanism dissociation 证据最弱（两位 Reviewer 独立 converge）
- Discussion 过于简短是最可修复的提分点

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9bd2ff8f-830a-4783-8676-23dd7326592a",
  "isSidechain": false,
  "promptId": "fa3d9c11-e599-4e0b-8a6a-865ce5431404",
  "type": "user",
  "uuid": "9a01fdfa-42ec-45f0-9049-b78de5b7de6c",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/sessions/review_director_0e80b40a",
  "sessionId": "a12edc2b-318d-49ec-adb5-ee9cfa431360",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 196_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[SYSTEM] Research Reviewer 刚完成 context rotation (Loop 5)，已读取 handoff 并就绪。如有待办任务请立即分配。  ---  [Reviewer 1 审稿结果]: 审稿意见已提交。  总结：经过审慎考虑 R2 的 cross-share 意见后，我维持 Overall 3.5 (Borderline Conference) 不变。同意 R2…",
  "leafUuid": "9a01fdfa-42ec-45f0-9049-b78de5b7de6c",
  "sessionId": "a12edc2b-318d-49ec-adb5-ee9cfa431360"
}
```

---


### Runtime record

_source line 197_

```json
{
  "type": "ai-title",
  "aiTitle": "Review policy ambiguity safety paper",
  "sessionId": "a12edc2b-318d-49ec-adb5-ee9cfa431360"
}
```

---
