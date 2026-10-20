# Research conversation: [Round 4 审稿请求]: ## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见 以下是 Reviewer 2 的完整审稿报告。请对每个 Must-Fix 和 Should-Fix 逐条回应： - **[AGREE]** 同 — Part 3 of 3

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../research-conversation-round-4-reviewer-2-reviewer-2-must-fix-should-fix-agree.md) · [Structured JSON](../../../sessions/39/3960f2477a3c45f1bc53.json)

## Round 1

### Assistant

_source line 76 · 2026-05-15T06:55:51.921Z_

已读完全部 10 页论文。现在逐条回应 R2 的意见。

---

## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

### Must-Fix

**[REBUT] R2-N1: Correlation-selection gap 的"意外性"论证不足**

R2 认为"4/5 信号是 instance-level，selection 失败可从设计原理推出"，因此 gap 缺少意外性。我不完全同意，理由如下：

1. **MBR 类比的非平凡性**。论文 Section 4.3（p7）明确建立了 MBR decoding 连接——指出五种选择策略本质上是 MBR risk minimization 的实例化。MBR 在机器翻译中是成功的范式（Eikema and Aziz, 2022; Freitag et al., 2022），所以并非显然可以预测 structural MBR 在 IE 中会全面失败。论文已指出这一点但确实可以更突出地论证 MT vs IE 的差异。

2. **Logprob 是 per-sample 信号但仍失败**。R2 自己也注意到 logprob 是唯一的 per-sample 信号，论文 Section 4.3 报告了"75% of comparisons are effectively ties"（p7），这一定量发现恰恰不是从设计原理可推出的——它是经验性的发现，说明 constrained decoding 下 logprob 的鉴别力坍塌。

3. **不过 R2 的改进建议是合理的**。论文 Discussion 的 "Why the gap exists" 段落（p7-8）确实偏向事后解释而非正面论证"why not obvious a priori"。增加 MBR-in-MT 成功 vs MBR-in-IE 失败的对比讨论，以及 logprob ties 的更深入分析（如 ties 在不同 task difficulty 下的分布），会实质性地加强论证。

**结论：核心观察有价值，但 R2 关于加强"非显然性"论证的建议可行且有益。不应作为 reject 理由，但应修改。**

---

**[AGREE] R2-N2: RE 结论基于单一数据集，泛化性不明**

同意这是一个实质性弱点。具体证据：

1. Table 1（p6）RE 列仅有 SciERC 一个数据集，而 NER 有三个（SciERC、CoNLL-2003、WNUT-17），覆盖了从 easy 到 hard 的 difficulty 梯度。RE 缺少对应的 difficulty 对照。

2. 论文 Limitations（p9）自己承认"40% of instances receive zero F1, compressing the discriminable range"——这意味着 SciERC RE 不仅是单数据集问题，还是一个存在严重 floor effect 的数据集，信号鉴别力在这种条件下天然受限。

3. Abstract（p1）和 Contributions（p2）均将 RE 与 NER 并列（"quality estimation for NER and RE"），但实际支撑力度不对等。Figure 3（p8）右图的 RE 结果中，所有信号的 ρ 上界仅约 0.38，远低于 NER 侧。

4. **但我补充一个缓解因素**：论文 Section 4.4（p7）的 3-seed robustness 验证覆盖了 RE，且 Figure 2 的 conditional set 分析也包含 RE，说明方法论上的严谨性适用于 RE。问题不是方法不对，而是数据支撑不足。

**建议：同意 R2 的方案——增加至少一个 RE 数据集，或在 Contributions 中明确将 RE 降级为 "preliminary findings on RE"。**

---

### Should-Fix

**[AGREE] R2-W1: Abstract 过于密集**

同意。p1 Abstract 第 3-4 行（"We systematically compare five confidence signals from three families—structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' κ), and model-internal (log-probability)—across NER (three datasets of varying difficulty) and RE (SciERC) with two model families (Qwen3-8B, LLaMA-3.1-8B)."）是一个包含 3 层嵌套括号和多重并列的超长句子。对于 Findings paper 的 abstract 来说，这种信息密度确实超出必要——可以先说信号家族，再说数据集，分两句叙述。

---

**[AGREE] R2-W2: "confidence signal" vs "consistency signal" 术语不一致**

部分同意。论文标题和 Section 3.2 用 "Confidence Signals" 作为五种信号的总称，但 Section 1 Introduction（p2）的 central finding 写的是 "consistency-based signals are effective quality estimators"，这里准确地限定了是 consistency-based 子集。问题出在正文某些过渡段落中，"consistency signals" 和 "confidence signals" 的边界模糊，尤其是 logprob 不属于 consistency 类但有时被笼统带入。

**建议：在 Section 3.2 开头增加一个明确的 taxonomy 定义（如 "We use *confidence signal* as the umbrella term covering..."），不需要大改。**

---

**[REBUT] R2-W3: Nedellec (2026) 引用键名 misleading**

不同意这是一个应修改的问题。R2 自己的描述存在内在矛盾："BibTeX 键名 `nedellec2026consistency` 但第一作者是 Yao"与"正文多处说 'Nedellec (2026)' 但 \citet 输出 'Yao et al. (2026)'"——如果 `\citet` 的输出是正确的 "Yao et al. (2026)"，那么读者看到的引用就是正确的。BibTeX 键名是内部实现细节，不影响论文的可读性或学术正确性。

我在通读论文时（p2-3 Related Work，p3 Method 引用处），所有对该文献的引用均显示为 "Yao et al. (2026)"，未发现正文中出现硬编码的 "Nedellec (2026)"。如果 R2 能指出具体哪一行正文文本显示为 "Nedellec"，我会重新考虑。

**结论：BibTeX 键名不属于审稿范围，除非它导致了可见的引用错误，而我未观察到这一点。建议降级为"小问题"或移除。**

---

**[AGREE] R2-W4: Soft Jaccard 对 Nedellec 改进幅度有限**

同意。Table 1（p6）的数据确认了 R2 的观察：

- SciERC NER: SJ ρ=0.381 vs EM ρ=（约 0.316 从 heatmap），差距存在但幅度有限
- CoNLL: EM 反超 SJ（Table 1 CoNLL 列，EM 的 ρ 更高）
- 论文 p5 脚注提到 "Pairwise bootstrap CIs confirm the SJ advantage over logprob (Δρ=+0.155, CI excludes zero) but not over EM (Δρ=+0.065, marginal under Bonferroni correction; Table 7, Appendix E)"

这直接支持 R2 的论点：SJ 相对 EM 的优势在统计上是 marginal 的。论文当前的 "structural advantage" 叙事应调整为强调 **difficulty-dependent complementarity**——即 SJ 在 hard tasks（SciERC）上占优但 EM 在 easy tasks（CoNLL）上更好。论文的数据实际上支持这个更细致的叙事（Section 4.2 讨论了 difficulty-dependent rankings），只是当前措辞过度倾向 structural signals。

---

**[REBUT] R2-W5: 缺少 constrained decoding 对 diversity 影响的实验对照**

不同意这应列为 Should-Fix。理由：

1. **方法论必要性**。对 structured IE（NER/RE）来说，constrained decoding 是获得可解析输出的必要条件。Free-form generation 产出的非结构化文本需要额外的后处理/解析步骤，引入了新的混淆变量，使对照实验的可比性存疑。

2. **论文已诚实处理**。Limitations（p9-10）明确指出："Constrained decoding (Outlines/vLLM) enforces schema compliance, potentially compressing per-sample diversity and contributing to the correlation-selection gap beyond what free-form generation would exhibit. Finally, log-probability was excluded from the temperature comparison (T=0.7 vs T=1.0) due to missing T=0.7 logprob data, leaving its temperature sensitivity uncharacterized."

3. **工作量与贡献不成比例**。增加 free-form baseline 实质上是要求作者同时解决输出解析的鲁棒性问题，这超出了 Findings paper 的合理范围。

**建议：保持当前 Limitations 中的讨论即可，可以额外加一句定量描述 constrained decoding 下的 diversity 统计（如 unique output ratio），但不需要 free-form baseline 实验。**

---

**[AGREE] R2-W6: 缺少若干相关工作**

部分同意。三篇文献的相关度我逐一评估：

1. **Xiong et al. (2024) "Can LLMs Express Their Uncertainty?" ICLR 2024** — **高度相关，应引用**。该文直接研究 LLM 的 uncertainty 表达能力，包括 verbalized confidence，与本文的 confidence signal 主题直接对话。论文 Related Work（p3）讨论了 uncertainty estimation and calibration，但未引用这篇 ICLR 2024 的关键工作。

2. **Ye et al. (2025) ICLR 2025** — 中度相关，nice-to-cite。与 Xiong et al. 主题接近但更偏 evaluation 角度。

3. **Generative IE survey (COLING 2025)** — 中度相关。论文已引用了多篇 generative IE 工作（p3），但一篇系统性 survey 的缺失确实是遗漏。

**结论：至少 Xiong et al. (2024) 应该被引用并在 Related Work 中讨论。**

---

### 对 R2 整体评价的意见

R2 给出 Overall 3.5/5，Soundness 4/5，Excitement 2.5/5。

我认为 **Soundness 4/5 是准确的**——方法论严谨性（bootstrap CI, TOST, 3-seed）确实出色。

对于 **Excitement 2.5/5**，我理解 R2 的逻辑（核心 gap 部分可从信号设计推出），但我认为这稍微低估了以下贡献：(a) 系统性 benchmark 本身的实用价值；(b) MBR 连接的理论优雅性；(c) difficulty-dependent signal ranking 的实际指导意义。对 Findings track 来说，3/5 的 Excitement 更合理。

**总体来说，R2 的审稿质量高，大部分技术判断准确。N2（RE 单数据集）和 W4（SJ 优势弱化）是最有价值的意见。N1 的"非显然性"批评有一定道理但过度了。W3（BibTeX 键名）和 W5（free-form baseline）可以降级处理。**

---

现在把这个交叉回应提交给 Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abee393c-fc64-402a-acdb-e6dacfb2391a",
  "isSidechain": false,
  "requestId": "req_011Cb3uyD1BQ9FPXorGpY4AT",
  "type": "assistant",
  "uuid": "c4b235a3-3f1c-4c80-9e9a-77e6d2dc8229",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8d164322-042b-459c-b3de-6ad10c70dae0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hu8a4mnJcs1Twt8eVphQQo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1870,
      "cache_read_input_tokens": 34354,
      "output_tokens": 7674,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1870,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7674,
          "cache_read_input_tokens": 34354,
          "cache_creation_input_tokens": 1870,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1870
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


### Tool call

_source line 77 · 2026-05-15T06:56:10.471Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01TvHSfqTFfYb3utv5Uu8ed7`</summary>

```json
{
  "text": "## Reviewer 1 → 交叉回应 Reviewer 2 审稿意见\n\n---\n\n### Must-Fix\n\n**[REBUT] R2-N1: Correlation-selection gap 的\"意外性\"论证不足**\n\nR2 认为\"4/5 信号是 instance-level，selection 失败可从设计原理推出\"。我部分反驳：\n\n1. **MBR 类比非平凡**。论文 Section 4.3（p7）建立了 MBR decoding 连接。MBR 在 MT 中成功（Eikema and Aziz, 2022），并非显然可预测 structural MBR 在 IE 中全面失败。\n2. **Logprob 是 per-sample 信号但仍失败**。75% comparisons are ties（Section 4.3, p7）是经验发现，非设计可推。\n3. **但 R2 改进建议合理**。\"Why the gap exists\"（p7-8）偏事后解释，增加 MT-vs-IE 的 MBR 对比讨论会加强论证。\n\n**结论：核心观察有价值，\"非显然性\"论证可加强，但不应作为 reject 理由。**\n\n---\n\n**[AGREE] R2-N2: RE 结论基于单一数据集**\n\n同意这是实质性弱点：\n- Table 1 RE 仅有 SciERC，NER 有三个 difficulty 梯度数据集\n- 40% zero-F1 floor effect 严重限制信号鉴别力\n- Contributions 中 RE 与 NER 并列但支撑力度不对等\n- 缓解因素：3-seed 验证和 conditional set 分析覆盖了 RE，方法论严谨性无问题\n\n**建议：增加 RE 数据集或将 RE 降级为 \"preliminary findings\"。**\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: Abstract 过于密集**\n同意。第 3-4 行含 3 层嵌套括号的超长句子可拆分为 2-3 句。\n\n**[AGREE] R2-W2: terminology 不一致**\n部分同意。\"confidence signal\"（总称）vs \"consistency signal\"（子集）边界在某些段落模糊。建议 Section 3.2 开头增加明确 taxonomy。\n\n**[REBUT] R2-W3: Nedellec (2026) BibTeX 键名**\n不同意。R2 称\"正文说 Nedellec (2026) 但 \\citet 输出 Yao et al. (2026)\"——如果 \\citet 输出正确，读者看到的就是正确引用。我通读全文（p2-3）未发现硬编码的 \"Nedellec\"。BibTeX 键名是内部实现细节，不属于审稿范围。建议降级或移除。\n\n**[AGREE] R2-W4: Soft Jaccard 改进幅度有限**\n同意。SJ vs EM Δρ=+0.065 在 Bonferroni 下 marginal（论文 p5 脚注确认）；CoNLL 上 EM 反超。应调整叙事为 difficulty-dependent complementarity 而非 structural dominance。\n\n**[REBUT] R2-W5: 缺少 free-form generation baseline**\n不同意列为 Should-Fix。Constrained decoding 对 structured IE 是方法论必要条件，free-form 引入新混淆变量。论文 Limitations 已诚实讨论。可加 diversity 统计，但不需 free-form 实验。\n\n**[AGREE] R2-W6: 缺少相关工作**\n部分同意。Xiong et al. (2024) ICLR \"Can LLMs Express Their Uncertainty?\" 高度相关，应引用。其余两篇 nice-to-cite。\n\n---\n\n### 对 R2 整体评价的意见\n\n- Soundness 4/5：准确\n- Excitement 2.5/5：稍低估，Findings track 3/5 更合理（系统性 benchmark 实用价值 + MBR 连接 + difficulty-dependent guidance）\n- R2 审稿质量高。最有价值意见：N2（RE 单数据集）和 W4（SJ 优势弱化）。N1 过度批评，W3 和 W5 可降级。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4b235a3-3f1c-4c80-9e9a-77e6d2dc8229",
  "isSidechain": false,
  "requestId": "req_011Cb3uyD1BQ9FPXorGpY4AT",
  "type": "assistant",
  "uuid": "db1afc91-2a5e-43f0-ab29-0da7989942ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8d164322-042b-459c-b3de-6ad10c70dae0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hu8a4mnJcs1Twt8eVphQQo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1870,
      "cache_read_input_tokens": 34354,
      "output_tokens": 7674,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1870,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7674,
          "cache_read_input_tokens": 34354,
          "cache_creation_input_tokens": 1870,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1870
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

_source line 78_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 4 审稿请求]: ## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见  以下是 Reviewer 2 的完整审稿报告。请对每个 Must-Fix 和 Should-Fix 逐条回应： - **[AGREE]** 同意并说明理由 - **[REBUT]** 反驳并提供证据（引用论文具体 Section/Table/Figure）  ---  ## Reviewer 2 —…",
  "leafUuid": "db1afc91-2a5e-43f0-ab29-0da7989942ae",
  "sessionId": "8d164322-042b-459c-b3de-6ad10c70dae0"
}
```

---


### Runtime record

_source line 79_

```json
{
  "type": "ai-title",
  "aiTitle": "Respond to Round 4 reviewer feedback on quality signals",
  "sessionId": "8d164322-042b-459c-b3de-6ad10c70dae0"
}
```

---


### Tool result

_source line 80 · 2026-05-15T06:56:14.488Z_

<details><summary>↩ Tool result · `toolu_01TvHSfqTFfYb3utv5Uu8ed7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db1afc91-2a5e-43f0-ab29-0da7989942ae",
  "isSidechain": false,
  "promptId": "e2f32aea-1f32-42ec-86fc-7afab0cd3a9b",
  "type": "user",
  "uuid": "bb2d06ee-85fe-406e-bdfe-f95bab3ab846",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_3897c2857f11615119e277e820eae311:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "db1afc91-2a5e-43f0-ab29-0da7989942ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_1_68ddc296",
  "sessionId": "8d164322-042b-459c-b3de-6ad10c70dae0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
