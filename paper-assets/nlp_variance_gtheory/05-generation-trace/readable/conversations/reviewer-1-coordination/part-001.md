# Reviewer 1 coordination — Part 1 of 2

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Conversation logs

[Transcript overview](../reviewer-1-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/43/43d7fe325dc90230775f.json)

## Round 1

## Round 1

48 recorded events


### User

_source line 1 · 2026-05-21T08:35:52.893317+00:00_

[Round 1 审稿请求]:
[Dream 审稿任务 — Reviewer 1：方法 + 实验]

PDF 路径：/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/review_input_db82206b.pdf

实验设计参考（含完整 imagined experiments）：/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/review_context.yaml

## 评分标准
无法确认目标 venue，使用 **ACL ARR 1–5 分制**（含 0.5 刻度）：
- 5: Award quality (top 2-5%)
- 4.5: Strong accept
- 4: Accept
- 3.5: Leaning accept
- 3: Borderline
- 2.5: Leaning reject
- 2: Reject
- 1.5: Strong reject
- 1: Trivial/wrong

## 你的审查侧重
- **方法描述**：G-theory 模型设定是否完整、claim 是否被实验数据支撑、关键设计选择（Henderson I vs REML、balanced design、binary scoring）是否充分论证
- **实验设计**：是否覆盖关键 ablation / 跨 benchmark / 跨 scale / 跨 hardware 维度；参考 review_context.yaml 中的 imagined_experiments 列表判断覆盖度
- **数据呈现**：表格/图是否能让审稿人复现结论、bootstrap CI / robustness checks 是否充分
- **统计方法**：variance decomposition 的估计方法是否合理、D-study projections 的外推是否 justified、binary data 上应用 G-theory 的 validity

请基于论文内容独立评判，不要假设论文结果的质量高低。

## Dream 审稿边界
这是 Dream 模拟论文。实验数据是想象的。
- **不需要评审**：Reproducibility checklist、代码/数据可用性、数值精确性、伦理/IRB
- **需要评审但标注为 "presentation 层面"**：Reference 真实性、论文完整度、引用数量
- **必须评审（idea 层面）**：实验设计是否足以支撑 claims（假设数据为真）、叙事逻辑自洽性、Claim generality vs 实验范围

每条 weakness 必须标注属于 **idea 层面** 还是 **presentation 层面**。

## 评分校准规则
- 3+ Major issues → 不高于 Borderline (3.0)
- 2 Major issues → 不高于 Leaning Accept (3.5)
- 1 Major issue → 不高于 Accept (4.0)
- 0 Major issues → 可给 Strong Accept (4.5) 或 Award (5.0)
Major issue 需有 explicit justification。

**不要评判**：新颖性 / 相关工作（那是 Reviewer 2 的范围）、格式 / 排版。

请通过 `review_reviewer_post_to_director(text, reviewer_id="1", project="nlp_variance_gtheory", dream_id="20260521T075006")` 汇报。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-21T08:36:03.686650+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-21T08:36:03.686984+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-21T08:36:03.995690+00:00_

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
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
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

_source line 5 · 2026-05-21T08:36:04.047173+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-21T08:36:09.533907+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/review_input_db82206b.pdf",
  "project": "nlp_variance_gtheory",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/review_input_db82206b.pdf",
    "project": "nlp_variance_gtheory",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-21T08:36:10.487646+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 373.3}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 429.5}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 307.1}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 298.0}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 335.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 304.9}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 337.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 305.5}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-
…[truncated 684 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-21T08:36:10.638585+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/review_context.yaml"
  }
}
```

</details>

---


### Tool call

_source line 9 · 2026-05-21T08:36:10.741054+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring rubric"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring rubric"
  }
}
```

</details>

---


### Tool result

_source line 10 · 2026-05-21T08:36:10.944594+00:00_

1	narrative_guidance: 'Original framing完全成立。Cross-benchmark gradient是primary novel finding——
2	  item_id从MMLU 42.1%单调递减至GSM8K 22.4%（Δ=19.7pp），model×item从33.6% 单调递增至46.5%。知识检索→多步推理的variance
3	  structure发生质变，item dominance 系统性减弱而model×item上升，直接解释了文献中关于"item重要还是prompt重要"的 矛盾结论——答案是benchmark-conditional。所有robustness分析hold：item
4	  resampling CV=3.2%，leave-one-model-out G_item spread=0.023，BF16≈FP16（Δ<0.001%），
5	  hardware×methodology<0.18%（binary）跨GPU confirmed。D-study在4个benchmark 上out-of-sample验证Δ≤0.007。IRT/G-theory
6	  ratio 3.5–4.4×在所有benchmark成立， 因为G-theory显式建模prompt×item、seed×item等IRT忽略的维度。Separability在binary
7	  scoring下跨benchmark、跨GPU均<0.5%。5个figure全部有实质数据。Hook直接用： "no universal reproducibility
8	  recipe"。AAAI 2027 strong accept范围（7–8/10）， 三个claim均有充分empirical support，无需削弱任何主张。
9	
10	  '
11	imagined_experiments:
12	- name: MMLU Full-Scale 4-Model G-Study
13	  plan_id: exp-001
14	  description: '4 models (Llama-3.1-8B, Gemma-2-9B, Mistral-7B, Qwen3-8B) × 3 precisions
15	    (FP32/BF16/FP16; Gemma BF16+FP32 only) × 6 prompts × 6 seeds × 3 temperatures
16	    × 4 orderings × 200 stratified MMLU items。V0 enforce_eager统一engine消除 FP32 confound。Henderson
17	    I + REML-EM(500 iter)双估计。Cross-model分析将 model作为crossed random facet。
18	
19	    '
20	  expected_results:
21	    total_records: 930400
22	    records_per_model:
23	      Llama: 239200
24	      Gemma: 172800
25	      Mistral: 259200
26	      Qwen: 259200
27	    overall_accuracy_bf16:
28	      Llama: 0.711
29	      Gemma: 0.732
30	      Mistral: 0.638
31	      Qwen: 0.726
32	    single_model_variance_pct:
33	      item_id: 61.1
34	      temperature: 4.1
35	      prompt_template: 3.2
36	      seed: 0.7
37	      ordering: 0.3
38	      precision: 0.4
39	      prompt_x_item: 4.6
40	      seed_x_item: 4.7
41	      temperature_x_item: 2.8
42	      precision_x_item: 1.3
43	      precision_x_temperature: 0.06
44	      other_2way: 0.9
45	      residual: 15.8
46	    single_model_G_200items: 0.611
47	    cross_model_variance
…[truncated 51170 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 306
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-21T08:36:17.181407+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring rubric"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Development and Validation of a Scoring Rubric for Editorial Evaluation of Peer-review Quality: A Pilot Study","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11000557/"}]

Based on the search results, I found information about the ACL Rolling Review (ARR) reviewer guidelines for 2025-2026:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Key Guidelines and Policies

All reviewers must familiarize themselves with the latest version of the ARR reviewer guidelines and perform the reviews on time and in line with ARR requirements.

## Review Quality Standards

Starting in May 2025, ARR adopts a new policy on 'highly irresponsible' (meta-)reviewers, with the program chairs
…[truncated 640 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6440
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-21T08:36:24.697617+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-21T08:36:25.204852+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 507
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-21T08:36:25.269569+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 15 · 2026-05-21T08:36:25.726621+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 16 · 2026-05-21T08:36:29.239167+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3969
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-21T08:36:29.240430+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3513
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-21T08:36:29.392166+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 19 · 2026-05-21T08:36:29.595537+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-21T08:36:29.595929+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 21 · 2026-05-21T08:36:29.596123+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-21T08:36:29.596294+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-21T08:36:30.307053+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 914
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-21T08:36:30.310349+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 25 · 2026-05-21T08:36:30.713187+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 26 · 2026-05-21T08:36:31.975835+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2380
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-21T08:36:31.977349+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2381
}
```

</details>

---


### Tool result

_source line 28 · 2026-05-21T08:36:31.978550+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2382
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-21T08:36:31.979559+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2383
}
```

</details>

---


### Tool result

_source line 30 · 2026-05-21T08:36:31.980591+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1670
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-21T08:36:31.981542+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1268
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-21T08:36:32.082049+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form criteria, scoring rubric, and scoring scales (especially soundness, excitement, overall recommendation scales with their numeric values and descriptions). List all dimensions reviewers must score."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form criteria, scoring rubric, and scoring scales (especially soundness, excitement, overall recommendation scales with their numeric values and descriptions). List all dimensions reviewers must score."
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-21T08:36:39.877153+00:00_

# ARR Review Form Scoring Criteria

Based on the provided guidelines, ARR reviewers evaluate papers using **three primary scores** (as of February 2025):

## Scoring Dimensions

### 1. **Soundness**
The guidelines specify that "soundness scores must be justified by the text of the review." Low soundness ratings require explicit justification for any identified technical flaws or methodological issues. This score assesses whether the work is technically correct and appropriately scoped.

### 2. **Excitement**
Described as reflecting "personal taste" and "subjective" preferences, this dimension is "orthogonal to the assessment of the soundness of the paper." A reviewer may find work sound but unexciting personally, or exciting despite minor soundness concerns.

### 3. **Overall Recommendation**
A "composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact." This represents an explicit recommendation regarding paper acceptance suitability, applicable when the work is committed to an ACL venue.

## Important Note on Numeric Scales

**The document does not explicitly specify numeric values or point scales** for any of these three dimensions. While the guidelines discuss these three scoring categories comprehensively, the actual numeric rating scale details (e.g., 1-5, 1-10) are referenced as being available in a separate resource: "a post describing the ARR review form in detail."

The guidelines emphasize that all three scores must align with review content and justify recommendations appropriately.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7795
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-21T08:36:44.861736+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/review_input_db82206b.pdf",
  "project": "nlp_variance_gtheory",
  "pages": "11-15",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/review_input_db82206b.pdf",
    "project": "nlp_variance_gtheory",
    "pages": "11-15",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-21T08:36:45.620086+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 309.5}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 339.3}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 177.6}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 172.2}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 66.9}], \"total_pages\": 15, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 758
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-21T08:36:48.835575+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-21T08:36:49.589923+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-21T08:36:49.641534+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 39 · 2026-05-21T08:36:50.144903+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 40 · 2026-05-21T08:36:50.552532+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 910
}
```

</details>

---


### Tool call

_source line 41 · 2026-05-21T08:36:50.552959+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 42 · 2026-05-21T08:36:51.306745+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1161
}
```

</details>

---


### Tool call

_source line 43 · 2026-05-21T08:36:51.307176+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/best/_pdf_images/paper_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 44 · 2026-05-21T08:36:51.361610+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 54
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-21T08:36:51.515873+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 962
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-21T08:40:36.624590+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## 总体评分\n**Overall**: 3.5/5 (Leaning Accept)\n**一句话总结**: 实验设计扎实、robustness analysis全面，但 binary data 上直接使用 ANOVA-based G-theory 缺乏充分理论辩护，且仅 4 个模型作为 random facet 使 model×item 估计不稳定——这两个方法论问题动摇了 primary findings 的根基。\n\n## 官方维度打分（ACL ARR 1–5 scale）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 两个方法论缺陷（binary G-theory validity、model facet sample size）影响核心 variance decomposition 的可信度，但 6 项 robustness analyses 和 cross-validation 提供了部分补偿 |\n| Overall | 3.5/5 | 实验覆盖度优秀（5 benchmarks、2 GPU architectures、14B scale extension、fine-tuning preliminary），claim-evidence alignment 总体较好，但 2 个 Major issues 限制了评分上限 |\n\n（注：新颖性/相关工作不在本 Reviewer 审查范围内）\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical / idea 层面] Binary data 上应用 ANOVA-based G-theory 的理论辩护不足\n\n- 具体位置：Section 3 (Eq. 1-2)、Section 5.7 (Binary data validation)、References (Jung et al. 2017)\n- 问题：论文将 Henderson Method I（ANOVA-type 估计）直接应用于 0/1 binary responses。G-theory 的线性模型假设近似正态分布，binary data 系统性违反此假设。论文在 Section 5.7 通过 null simulation 证明 observed item_id 是 null 的 737×，且 Bernoulli p(1-p) correlation 为 moderate (r=0.42)——这证明了 signal 的存在，但**没有证明 ANOVA-based 方差分量估计在 binary data 上是无偏的**。\n- 关键矛盾：论文在 References 中引用了 Jung et al. (2017) 的 logistic-link generalized G-theory model——这恰恰是为 binary data 设计的正确方法。论文引用了但未使用，也**未解释为何不使用**。Shavelson et al. (1989) \"Generalizability of binary items\" 同样被引用，但论文未讨论该文献对 binary data G-theory 的具体建议。\n- 为什么影响接收：全部 variance decomposition 百分比（item_id 42.1%、model×item 33.6% 等）、cross-benchmark gradient、D-study budget 均建立在 ANOVA-based 估计之上。如果 binary data 导致估计有偏，则所有定量结论需要修正。特别是，Bernoulli variance ceiling p(1-p) 对不同 accuracy 水平的 benchmarks 有不同影响——MMLU (acc≈0.67) 和 GSM8K (acc≈0.485) 的 Bernoulli constraint 不同，可能混淆 cross-benchmark gradient 的解读。\n- 建议修改方向：(a) 作为 sensitivity check 运行 logistic-link G-theory model（Jung et al. 2017），比较方差分量估计与 ANOVA-based 结果的差异；或 (b) 提供严格的理论论证说明 balanced design 下 Henderson I 对 binary data 的 bias 是 bounded 的，引用 Shavelson et al. (1989) 的具体结论；(c) 讨论不同 benchmarks 的 accuracy distribution 如何影响 Bernoulli-adjusted variance decomposition——GSM8K accuracy 最接近 0.5（Bernoulli variance 最大），但 item_id% 反而最低，这实际上**有利于**论文的 gradient claim，应明确讨论。\n\n**N2** [critical / idea 层面] 仅 4 个模型作为 crossed random facet——model×item 估计不稳定\n\n- 具体位置：Section 4.1 (Models)、Table 1 (cross-model decomposition)、Table 4 (Leave-one-model-out)、Section 6.5 (Limitations)\n- 问题：论文将 model 视为 crossed random facet，但仅有 4 个 7-9B 模型（Llama-3.1-8B、Gemma-2-9B、Mistral-7B、Qwen3-8B），来自 4 个不同 architecture families。这不是从 population 中的 random sample，而是 purposive selection。Random effects 要求样本代表 population——4 个精心选择的模型不满足此条件。\n- 后果的严重性：model×item 是论文 primary finding（cross-benchmark gradient）的核心——从 MMLU 33.6% 到 MATH 50.8%。Bootstrap CI（Table 12）显示 MMLU model×item 为 [28.4, 37.9]，宽度 9.5pp；GSM8K 为 [39.8, 53.7]，宽度 13.9pp。虽然两个 CI 不重叠（gradient 方向 robust），但绝对值的不确定性很大。Leave-one-model-out spread 为 0.023（Section 5.2），论文声称\"稳定\"，但 4 选 3 的 jackknife 本身统计 power 极低。\n- 14B extension（Section 5.8）只有 2 个模型，进一步弱化了 random facet 假设。Table 13 显示 7-9B 与 14B 的 delta 在 bootstrap CI 内，但 2 个模型的 CI 必然极宽。\n- 为什么影响接收：如果增加到 8-10 个模型，model×item 的估计值可能发生非平凡变化，特别是如果新模型来自相似 architecture families（如多个 Llama variants），model×item 可能显著下降——gradient 的 slope 和 monotonicity 都可能改变。\n- 建议修改方向：(a) 明确承认 model 是 \"fixed\" 或 \"quasi-random\" facet，调整 G-coefficient 公式和 D-study interpretation；(b) 在 Section 5.7 的 fixed vs random sensitivity analysis（Table 11）中加入 model-as-fixed 的完整分析，展示固定 model 后 variance decomposition 的变化；(c) 讨论 purposive vs random sampling 对 generalizability 的影响——current models 覆盖了 4 个 architecture families，但如果 population 定义为 \"all 7-9B open-weight LLMs\"，4 个样本的代表性有限。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning / idea 层面] D-study 从 200 items 外推至 414-1320 items 缺乏 progressive validation\n\n- 具体位置：Section 5.6 (D-Study Reproducibility Budgets)、Table 9\n- 问题：D-study 公式假设方差分量在不同 item count 下保持稳定。论文从 200 items 外推至 G≥0.80 所需的 414-648 items 和 G≥0.90 所需的 820-1320 items——最高外推到观测值的 6.6 倍。Item resampling stability（Section 5.2, Table 5）仅验证了不同 200-item 样本之间的稳定性（CV=3.2%），**未验证 200→400→800 items 时方差分量是否保持稳定**。\n- 建议：如果计算资源允许，在至少一个 benchmark 上运行 100/200/400 items 的 progressive validation；或者明确声明 D-study projections 是 model-based extrapolation 而非 empirically validated，并讨论可能的 bias 方向。\n\n**W2** [warning / idea 层面] Cross-benchmark \"reasoning complexity\" 排序是 post-hoc 的\n\n- 具体位置：Section 5.3、Figure 1 description\n- 问题：5 个 benchmarks 按 MMLU→HellaSwag→ARC→GSM8K→MATH 排列以展示 monotonic gradient。\"Reasoning complexity\" 作为排序依据没有独立的操作性定义——它是观察到 gradient 后用来解释排序的 narrative。HellaSwag 是\"commonsense completion\"而非典型\"reasoning\"，ARC-Challenge 是 science QA 而非纯 reasoning。\n- 5 个点的 monotonicity 有多 informative？item_id 和 model×item 在百分比约束下（总和接近但不等于 100%）存在机械的负相关——如果 item_id 下降，剩余 variance 增加，model×item 作为最大的非 item 分量自然上升。Perfect inverse monotonicity 部分源于此机械关系。\n- 建议：(a) 提供 reasoning complexity 的独立操作定义（如 average solution steps、required inference hops），而非 post-hoc label；(b) 报告 permutation test：在 5! = 120 种排列中，有多少种同时使 item_id 和 model×item monotonic；(c) 讨论 item_id 与 model×item 的机械负相关对 gradient 解读的影响。\n\n**W3** [warning / idea 层面] Balanced design 假设与实际设计的不一致\n\n- 具体位置：Section 3 (\"Henderson Method I for primary estimation (balanced designs)\")、Section 4.3\n- 问题：论文声称使用 Henderson Method I 因为 \"balanced design unbiased\"。但实际设计存在多处不平衡：(a) Gemma 仅支持 BF16+FP32，无 FP16——MMLU 主实验中的 precision facet 不 balanced；(b) MMLU 用 3 precisions × 3 temperatures，其他 4 个 benchmarks 用 2×2——cross-benchmark 比较中 design 不同；(c) 14B 实验仅 2 个模型 on MMLU。\n- 论文在 Section 5.4 提到 \"re-analyzing MMLU with the reduced 2×2 design\" 确认 delta<1pp，在 Section 5.1 提到 \"cross-model analysis uses balanced bf16 subset\"。但这些关键的 analysis subset 选择分散在不同 section，读者难以追踪哪些数字来自哪个 subset。\n- 建议：在 Section 4 或 Appendix 中提供一张 design matrix 表，明确标注每个 benchmark × model × precision 的数据状态（balanced subset vs full data），以及每个 table 使用的 subset。\n\n**W4** [warning / presentation 层面] \"Ordering\" facet 在开放式 benchmarks 上的定义不明\n\n- 具体位置：Section 4 (Experimental Design)\n- 问题：Section 4 提到 \"4 orderings\" 作为 facet，但未定义 ordering 对不同 benchmark 类型的含义。对 MMLU/ARC（多选题），ordering 可能是选项顺序（A/B/C/D 的排列，4! = 24 中选 4）。对 GSM8K/MATH（开放式数学题），\"ordering\" 的操作定义不清——可能是 few-shot examples 的排列顺序？\n- 建议：在 Section 4 中明确定义每个 benchmark 上 ordering facet 的具体操作。\n\n**W5** [warning / idea 层面] Temperature=0.0 下 seed 效应的理论预期为零，但 seed 仍被作为 facet\n\n- 具体位置：Section 4.3-4.4\n- 问题：T=0.0 时 greedy decoding 应完全确定性——同一 prompt+item 在不同 seed 下应产生相同输出。但论文的 variance decomposition 将所有 temperature levels 的数据 pooled 在一起估计 seed 主效应。如果 T=0 下 seed 确实无效应，则 pooling 会 dilute seed variance 估计（MMLU cross-model seed = 0.5%），并可能影响 temperature×seed interaction 的估计。\n- 建议：(a) 报告 T=0 条件下 seed 的 within-condition variance（应≈0）；(b) 讨论 pooling across temperature levels 对 seed variance 估计的影响；或 (c) 在 temperature-stratified analysis（Figure 5 描述中提到的 heatmap）中分离展示。\n\n---\n\n## 小问题（不影响接收）\n\n- [presentation] Table 1 的 \"residual+other\" 从 single-model 21.2% 降至 cross-model 11.5%（Δ=-9.7pp），但论文未在正文中解释这 9.7pp 的去向。Section 5.7 提到 \"3-way interactions account for ~6%\"，应在 Table 1 讨论时交叉引用。\n- [presentation] Section 5.5 (IRT vs G-theory) 中 \"At IRT's recommended 116 items for MMLU, the G-theory G is only 0.529\" 是一个很有力的论点，但放在 Section 5.5 较后的位置，建议提前到 Section 5.3 或 abstract 中强调。\n- [presentation] Table 6 使用 reduced design (2×2) 的数据，但这一点直到 Section 5.4 才说明（\"Re-analyzing MMLU with the reduced 2×2 design\"）。建议在 Table 6 caption 中直接注明。\n- [presentation] 论文 Section 6.5 Limitations 中 \"Standard G-theory assumes continuous responses\" 一句过于轻描淡写——这是一个核心方法论假设，不应仅用一句 limitation 带过（参见 N1）。\n\n---\n\n## 主要优势\n\n- **实验规模和覆盖度优秀**：5 benchmarks × 6 models × 2 GPU architectures × multiple precisions/prompts/seeds/temperatures/orderings，总计 ~4.25M records（Section 4.5）。这是目前 LLM evaluation variance 文献中最全面的 crossed factorial design。\n- **Robustness analysis 体系完整**：6 项独立验证（bootstrap CI、jackknife、item resampling、REML cross-check、fixed vs random sensitivity、binary null simulation），形成了系统性的 methodological defense。\n- **Cross-benchmark gradient 是一个有实质性见解的 finding**：即使考虑 N2 的模型数量限制，\"variance structure is benchmark-conditional\" 这一定性结论在所有 robustness checks 中都 hold——item_id dominance 在 knowledge retrieval tasks 上始终最高，model×item 在 reasoning tasks 上始终最高。这直接解释了文献中关于\"item重要还是prompt重要\"的矛盾结论。\n- **D-study budget calculator 有高实用价值**：Table 9 给出的 benchmark-specific reproducibility budgets（e.g., MMLU: 414 items × 3 prompts × 3 seeds for G≥0.80）是 practitioner 可以直接使用的 actionable guidelines。\n- **IRT vs G-theory 对比量化了忽略 multi-facet reliability 的隐性代价**：3.6-4.6× 的 item requirement ratio 和 \"at IRT's 116 items, G-theory G = 0.529\" 是有说服力的论据。\n- **Separability finding（Section 5.4）为孤立因子研究的组合提供了 empirical 支持**：hardware×methodology < 0.18%（binary）意味着独立研究 hardware 和 methodology 的文献结论可以合法组合。",
  "reviewer_id": "1",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## 总体评分\n**Overall**: 3.5/5 (Leaning Accept)\n**一句话总结**: 实验设计扎实、robustness analysis全面，但 binary data 上直接使用 ANOVA-based G-theory 缺乏充分理论辩护，且仅 4 个模型作为 random facet 使 model×item 估计不稳定——这两个方法论问题动摇了 primary findings 的根基。\n\n## 官方维度打分（ACL ARR 1–5 scale）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 两个方法论缺陷（binary G-theory validity、model facet sample size）影响核心 variance decomposition 的可信度，但 6 项 robustness analyses 和 cross-validation 提供了部分补偿 |\n| Overall | 3.5/5 | 实验覆盖度优秀（5 benchmarks、2 GPU architectures、14B scale extension、fine-tuning preliminary），claim-evidence alignment 总体较好，但 2 个 Major issues 限制了评分上限 |\n\n（注：新颖性/相关工作不在本 Reviewer 审查范围内）\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical / idea 层面] Binary data 上应用 ANOVA-based G-theory 的理论辩护不足\n\n- 具体位置：Section 3 (Eq. 1-2)、Section 5.7 (Binary data validation)、References (Jung et al. 2017)\n- 问题：论文将 Henderson Method I（ANOVA-type 估计）直接应用于 0/1 binary responses。G-theory 的线性模型假设近似正态分布，binary data 系统性违反此假设。论文在 Section 5.7 通过 null simulation 证明 observed item_id 是 null 的 737×，且 Bernoulli p(1-p) correlation 为 moderate (r=0.42)——这证明了 signal 的存在，但**没有证明 ANOVA-based 方差分量估计在 binary data 上是无偏的**。\n- 关键矛盾：论文在 References 中引用了 Jung et al. (2017) 的 logistic-link generalized G-theory model——这恰恰是为 binary data 设计的正确方法。论文引用了但未使用，也**未解释为何不使用**。Shavelson et al. (1989) \"Generalizability of binary items\" 同样被引用，但论文未讨论该文献对 binary data G-theory 的具体建议。\n- 为什么影响接收：全部 variance decomposition 百分比（item_id 42.1%、model×item 33.6% 等）、cross-benchmark gradient、D-study budget 均建立在 ANOVA-based 估计之上。如果 binary data 导致估计有偏，则所有定量结论需要修正。特别是，Bernoulli variance ceiling p(1-p) 对不同 accuracy 水平的 benchmarks 有不同影响——MMLU (acc≈0.67) 和 GSM8K (acc≈0.485) 的 Bernoulli constraint 不同，可能混淆 cross-benchmark gradient 的解读。\n- 建议修改方向：(a) 作为 sensitivity check 运行 logistic-link G-theory model（Jung et al. 2017），比较方差分量估计与 ANOVA-based 结果的差异；或 (b) 提供严格的理论论证说明 balanced design 下 Henderson I 对 binary data 的 bias 是 bounded 的，引用 Shavelson et al. (1989) 的具体结论；(c) 讨论不同 benchmarks 的 accuracy distribution 如何影响 Bernoulli-adjusted variance decomposition——GSM8K accuracy 最接近 0.5（Bernoulli variance 最大），但 item_id% 反而最低，这实际上**有利于**论文的 gradient claim，应明确讨论。\n\n**N2** [critical / idea 层面] 仅 4 个模型作为 crossed random facet——model×item 估计不稳定\n\n- 具体位置：Section 4.1 (Models)、Table 1 (cross-model decomposition)、Table 4 (Leave-one-model-out)、Section 6.5 (Limitations)\n- 问题：论文将 model 视为 crossed random facet，但仅有 4 个 7-9B 模型（Llama-3.1-8B、Gemma-2-9B、Mistral-7B、Qwen3-8B），来自 4 个不同 architecture families。这不是从 population 中的 random sample，而是 purposive selection。Random effects 要求样本代表 population——4 个精心选择的模型不满足此条件。\n- 后果的严重性：model×item 是论文 primary finding（cross-benchmark gradient）的核心——从 MMLU 33.6% 到 MATH 50.8%。Bootstrap CI（Table 12）显示 MMLU model×item 为 [28.4, 37.9]，宽度 9.5pp；GSM8K 为 [39.8, 53.7]，宽度 13.9pp。虽然两个 CI 不重叠（gradient 方向 robust），但绝对值的不确定性很大。Leave-one-model-out spread 为 0.023（Section 5.2），论文声称\"稳定\"，但 4 选 3 的 jackknife 本身统计 power 极低。\n- 14B extension（Section 5.8）只有 2 个模型，进一步弱化了 random facet 假设。Table 13 显示 7-9B 与 14B 的 delta 在 bootstrap CI 内，但 2 个模型的 CI 必然极宽。\n- 为什么影响接收：如果增加到 8-10 个模型，model×item 的估计值可能发生非平凡变化，特别是如果新模型来自相似 architecture families（如多个 Llama variants），model×item 可能显著下降——gradient 的 slope 和 monotonicity 都可能改变。\n- 建议修改方向：(a) 明确承认 model 是 \"fixed\" 或 \"quasi-random\" facet，调整 G-coefficient 公式和 D-study interpretation；(b) 在 Section 5.7 的 fixed vs random sensitivity analysis（Table 11）中加入 model-as-fixed 的完整分析，展示固定 model 后 variance decomposition 的变化；(c) 讨论 purposive vs random sampling 对 generalizability 的影响——current models 覆盖了 4 个 architecture families，但如果 population 定义为 \"all 7-9B open-weight LLMs\"，4 个样本的代表性有限。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning / idea 层面] D-study 从 200 items 外推至 414-1320 items 缺乏 progressive validation\n\n- 具体位置：Section 5.6 (D-Study Reproducibility Budgets)、Table 9\n- 问题：D-study 公式假设方差分量在不同 item count 下保持稳定。论文从 200 items 外推至 G≥0.80 所需的 414-648 items 和 G≥0.90 所需的 820-1320 items——最高外推到观测值的 6.6 倍。Item resampling stability（Section 5.2, Table 5）仅验证了不同 200-item 样本之间的稳定性（CV=3.2%），**未验证 200→400→800 items 时方差分量是否保持稳定**。\n- 建议：如果计算资源允许，在至少一个 benchmark 上运行 100/200/400 items 的 progressive validation；或者明确声明 D-study projections 是 model-based extrapolation 而非 empirically validated，并讨论可能的 bias 方向。\n\n**W2** [warning / idea 层面] Cross-benchmark \"reasoning complexity\" 排序是 post-hoc 的\n\n- 具体位置：Section 5.3、Figure 1 description\n- 问题：5 个 benchmarks 按 MMLU→HellaSwag→ARC→GSM8K→MATH 排列以展示 monotonic gradient。\"Reasoning complexity\" 作为排序依据没有独立的操作性定义——它是观察到 gradient 后用来解释排序的 narrative。HellaSwag 是\"commonsense completion\"而非典型\"reasoning\"，ARC-Challenge 是 science QA 而非纯 reasoning。\n- 5 个点的 monotonicity 有多 informative？item_id 和 model×item 在百分比约束下（总和接近但不等于 100%）存在机械的负相关——如果 item_id 下降，剩余 variance 增加，model×item 作为最大的非 item 分量自然上升。Perfect inverse monotonicity 部分源于此机械关系。\n- 建议：(a) 提供 reasoning complexity 的独立操作定义（如 average solution steps、required inference hops），而非 post-hoc label；(b) 报告 permutation test：在 5! = 120 种排列中，有多少种同时使 item_id 和 model×item monotonic；(c) 讨论 item_id 与 model×item 的机械负相关对 gradient 解读的影响。\n\n**W3** [warning / idea 层面] Balanced design 假设与实际设计的不一致\n\n- 具体位置：Section 3 (\"Henderson Method I for primary estimation (balanced designs)\")、Section 4.3\n- 问题：论文声称使用 Henderson Method I 因为 \"balanced design unbiased\"。但实际设计存在多处不平衡：(a) Gemma 仅支持 BF16+FP32，无 FP16——MMLU 主实验中的 precision facet 不 balanced；(b) MMLU 用 3 precisions × 3 temperatures，其他 4 个 benchmarks 用 2×2——cross-benchmark 比较中 design 不同；(c) 14B 实验仅 2 个模型 on MMLU。\n- 论文在 Section 5.4 提到 \"re-analyzing MMLU with the reduced 2×2 design\" 确认 delta<1pp，在 Section 5.1 提到 \"cross-model analysis uses balanced bf16 subset\"。但这些关键的 analysis subset 选择分散在不同 section，读者难以追踪哪些数字来自哪个 subset。\n- 建议：在 Section 4 或 Appendix 中提供一张 design matrix 表，明确标注每个 benchmark × model × precision 的数据状态（balanced subset vs full data），以及每个 table 使用的 subset。\n\n**W4** [warning / presentation 层面] \"Ordering\" facet 在开放式 benchmarks 上的定义不明\n\n- 具体位置：Section 4 (Experimental Design)\n- 问题：Section 4 提到 \"4 orderings\" 作为 facet，但未定义 ordering 对不同 benchmark 类型的含义。对 MMLU/ARC（多选题），ordering 可能是选项顺序（A/B/C/D 的排列，4! = 24 中选 4）。对 GSM8K/MATH（开放式数学题），\"ordering\" 的操作定义不清——可能是 few-shot examples 的排列顺序？\n- 建议：在 Section 4 中明确定义每个 benchmark 上 ordering facet 的具体操作。\n\n**W5** [warning / idea 层面] Temperature=0.0 下 seed 效应的理论预期为零，但 seed 仍被作为 facet\n\n- 具体位置：Section 4.3-4.4\n- 问题：T=0.0 时 greedy decoding 应完全确定性——同一 prompt+item 在不同 seed 下应产生相同输出。但论文的 variance decomposition 将所有 temperature levels 的数据 pooled 在一起估计 seed 主效应。如果 T=0 下 seed 确实无效应，则 pooling 会 dilute seed variance 估计（MMLU cross-model seed = 0.5%），并可能影响 temperature×seed interaction 的估计。\n- 建议：(a) 报告 T=0 条件下 seed 的 within-condition variance（应≈0）；(b) 讨论 pooling across temperature levels 对 seed variance 估计的影响；或 (c) 在 temperature-stratified analysis（Figure 5 描述中提到的 heatmap）中分离展示。\n\n---\n\n## 小问题（不影响接收）\n\n- [presentation] Table 1 的 \"residual+other\" 从 single-model 21.2% 降至 cross-model 11.5%（Δ=-9.7pp），但论文未在正文中解释这 9.7pp 的去向。Section 5.7 提到 \"3-way interactions account for ~6%\"，应在 Table 1 讨论时交叉引用。\n- [presentation] Section 5.5 (IRT vs G-theory) 中 \"At IRT's recommended 116 items for MMLU, the G-theory G is only 0.529\" 是一个很有力的论点，但放在 Section 5.5 较后的位置，建议提前到 Section 5.3 或 abstract 中强调。\n- [presentation] Table 6 使用 reduced design (2×2) 的数据，但这一点直到 Section 5.4 才说明（\"Re-analyzing MMLU with the reduced 2×2 design\"）。建议在 Table 6 caption 中直接注明。\n- [presentation] 论文 Section 6.5 Limitations 中 \"Standard G-theory assumes continuous responses\" 一句过于轻描淡写——这是一个核心方法论假设，不应仅用一句 limitation 带过（参见 N1）。\n\n---\n\n## 主要优势\n\n- **实验规模和覆盖度优秀**：5 benchmarks × 6 models × 2 GPU architectures × multiple precisions/prompts/seeds/temperatures/orderings，总计 ~4.25M records（Section 4.5）。这是目前 LLM evaluation variance 文献中最全面的 crossed factorial design。\n- **Robustness analysis 体系完整**：6 项独立验证（bootstrap CI、jackknife、item resampling、REML cross-check、fixed vs random sensitivity、binary null simulation），形成了系统性的 methodological defense。\n- **Cross-benchmark gradient 是一个有实质性见解的 finding**：即使考虑 N2 的模型数量限制，\"variance structure is benchmark-conditional\" 这一定性结论在所有 robustness checks 中都 hold——item_id dominance 在 knowledge retrieval tasks 上始终最高，model×item 在 reasoning tasks 上始终最高。这直接解释了文献中关于\"item重要还是prompt重要\"的矛盾结论。\n- **D-study budget calculator 有高实用价值**：Table 9 给出的 benchmark-specific reproducibility budgets（e.g., MMLU: 414 items × 3 prompts × 3 seeds for G≥0.80）是 practitioner 可以直接使用的 actionable guidelines。\n- **IRT vs G-theory 对比量化了忽略 multi-facet reliability 的隐性代价**：3.6-4.6× 的 item requirement ratio 和 \"at IRT's 116 items, G-theory G = 0.529\" 是有说服力的论据。\n- **Separability finding（Section 5.4）为孤立因子研究的组合提供了 empirical 支持**：hardware×methodology < 0.18%（binary）意味着独立研究 hardware 和 methodology 的文献结论可以合法组合。",
    "reviewer_id": "1",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-21T08:40:40.591266+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3966
}
```

</details>

---


### Assistant

_source line 48 · 2026-05-21T08:40:48.602422+00:00_

审稿意见已提交给 Review Director。

总结：给出 **3.5/5 (Leaning Accept)**。识别出 2 个 Must-Fix 问题：(1) binary data 上使用 ANOVA-based G-theory 缺乏理论辩护——论文引用了 logistic-link G-theory (Jung et al. 2017) 却未使用也未解释原因；(2) 仅 4 个模型作为 crossed random facet，model×item 估计不稳定，cross-benchmark gradient 的定量结论对模型选择敏感。另有 5 个 Should-Fix 问题涉及 D-study 外推验证、benchmark 排序的 post-hoc 性质、balanced design 不一致、ordering facet 定义不清、T=0 下 seed 效应。优势方面肯定了实验规模（~4.25M records）、robustness analysis 体系、和 practitioner-facing D-study budget calculator 的实用价值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1"
}
```

</details>

---


## Round 2

## Round 2

4 recorded events


### User

_source line 49 · 2026-05-21T08:42:22.689036+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 2 的 Round 1 审稿意见

请逐条阅读 Reviewer 2 的审稿意见，对每个 Must-Fix 和 Should-Fix 问题用 `[AGREE]` 或 `[REBUT]` 回应，并附简要理由。如果你有补充观点或与你的发现相关联的地方，也请指出。

---

以下是 Reviewer 2 的完整审稿意见：

**Overall**: 3.5/5 (Leaning Accept)

### Must-Fix 问题

**N1** [critical, idea 层面] Cross-benchmark gradient 的 generality claim 显著超出 5 个 benchmarks 的实验基础

- 5 个 benchmarks 全部落在 "factual knowledge retrieval → multi-step mathematical reasoning" 一条轴上，完全没覆盖 code generation、translation、summarization、instruction following、open-ended generation 等 task types。
- Benchmark ordering 的 "reasoning complexity" 排序缺乏独立验证，HellaSwag 和 ARC-Challenge 的相对排序可质疑。
- n=5 的 monotonicity 统计功效极低，Spearman ρ=1.0 在 n=5 时 p≈0.017（单侧），且 ranking 本身非独立于数据。
- Title "Across Benchmarks" 和 "no universal reproducibility recipe" 暗示了跨所有 benchmark 类型的普遍性，但实验仅支持一个 task dimension。

### Should-Fix 问题

**W1** IRT vs. G-theory 对比方向上是数学必然，新颖性主要在经验量化。建议将 C3 从 primary contribution 降级或明确表述为 "first empirical quantification"。

**W2** "No universal reproducibility recipe" 叙事被实际推荐削弱——跨 benchmark 变化主要体现在 item count（414 vs 648，仅 1.6× 差异），其他 facet 推荐几乎一致。实际发现更接近 "item budget is benchmark-conditional, but methodological recipe is largely stable"。

**W3** 与 Mesting (2026) 的差异化偏弱——三个 extension（infrastructure crossing, multi-benchmark, model as crossed facet）均属 G-theory 的 straightforward 应用，方法论层面是增量的。

**W4** Related Work 缺少：(a) 教育测量中的 cross-test G-study 比较文献；(b) benchmark contamination/saturation 对 item_id variance 解释的影响；(c) GLMM 在 NLP evaluation 中的应用。

**W5** Fine-tuning G-study（RoBERTa）超出论文核心 scope（LLM inference evaluation），分散叙事焦点。

### 小问题
- Section 3 缺少 balanced vs unbalanced design 对 Henderson I 影响的讨论
- Table 6 "trend" 列略 informal，可用 Spearman ρ + p-value 替代
- Limitations 未讨论 task type coverage 限制
- References 格式不一致

### 主要优势
- Cross-benchmark variance gradient 有真实 empirical value
- Practitioner toolkit 实用性强
- Robustness 分析体系完整
- Metric qualification 是重要方法论贡献
- 叙事结构清晰

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-21T08:43:27.434979+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 Round 1 意见的交叉回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1: Cross-benchmark gradient 的 generality claim 超出 5 个 benchmarks 的实验基础**\n\n同意这是一个实质性问题。我在自己的 W2 中也指出了 \"reasoning complexity\" 排序是 post-hoc 的，但 R2 的论述更尖锐且补充了关键统计论据：\n\n1. **n=5 时 Spearman ρ=1.0 的 p≈0.017**——R2 正确指出这在统计上并不 overwhelming，尤其考虑到 ranking 本身 non-independent（derived from same data）。\n2. **Task type coverage 确实是 blind spot**——5 个 benchmarks 全部是 closed-form QA（multiple-choice 或 short-answer math），完全没有 generation-heavy tasks（summarization、translation、instruction following）。论文的 \"no universal recipe\" claim 在逻辑上需要覆盖更多 task types 才能成立。\n3. **Title 和 framing 的 overclaim**——\"Across Benchmarks\" 在字面上暗示 general coverage，但实际只覆盖了 knowledge-to-reasoning 这一条轴。\n\n补充我的发现：我在 W2 中指出了 item_id 与 model×item 之间存在机械负相关（两者是 variance decomposition 中最大的两个分量，总和受约束），这进一步削弱了\"perfect inverse monotonicity\"作为 empirical finding 的 informativeness。R2 的 task type coverage 论点和我的 mechanical correlation 论点共同构成对 gradient claim 的 convergent critique。\n\n**建议**：将 claim 限定为 \"across closed-form QA benchmarks spanning knowledge retrieval to mathematical reasoning\"，并在 Limitations 中明确讨论 generation tasks 的缺失。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: IRT vs G-theory 对比方向上是数学必然**\n\n同意方向性结论（G-theory 需要更多 items）是 trivially true——G-theory 模型化了更多 variance sources，必然需要更多 items 来 stabilize 这些额外分量。论文的 empirical contribution 在于量化了 ratio（3.6-4.6×），但 \"G-theory requires 3.6-4.6× more items\" 不应被框架为一个 surprising finding。\n\n补充：我在审稿中将 IRT 对比列为\"主要优势\"之一，现在认为应重新定位——它的价值是 **practitioner-facing quantification**（\"如果你按 IRT 建议用 116 items，actual reliability 只有 0.529\"），而非 theoretical insight。建议作者将 C3 表述为 \"first empirical quantification of the multi-facet reliability gap\"。\n\n**[REBUT] R2-W2: \"No universal recipe\" 叙事被 actual recommendations 削弱**\n\n部分不同意。R2 的论据是跨 benchmark 的推荐差异主要体现在 item count（414 vs 648，1.6×），其他 facet 推荐\"几乎一致\"（prompts 3-4, seeds 3-5）。但：\n\n1. **Item count 差异本身就是实质性的**——从 MMLU 414 items 到 MATH 648 items 是 56% 的增加，对 compute budget 有直接影响。Table 9 显示 G≥0.90 时差距更大（MMLU 820 vs GSM8K 1180，44% increase）。\n2. **Facet 推荐的\"一致性\"恰恰是一个 finding**——即 methodological facets（prompts, seeds）的 optimal budget 相对 stable，而 item budget 是 benchmark-conditional。这**不等于**\"universal recipe exists\"——它等于\"recipe 的 methodology 部分 portable，item 部分不 portable\"。\n3. 但 R2 有一个合理内核：**\"no universal recipe\" 的措辞确实 overclaim**。更准确的表述是 \"item budget is benchmark-conditional; methodological protocol is largely transferable\"。这与论文当前的 dramatic framing (\"no universal reproducibility recipe\") 有落差。\n\n**结论**：叙事需要 recalibrate，但不应完全反转为 \"recipe is largely stable\"。实际 finding 介于两个极端之间。\n\n**[AGREE] R2-W3: 与 Mesting (2026) 的差异化偏弱**\n\n新颖性/相关工作不在我的审查范围内，无法独立评判。但从方法论角度，R2 的观察与我的审稿一致——论文的 contribution 更多是 empirical scale-up（更多 benchmarks、更多 models、加入 infrastructure）而非 methodological innovation。G-theory 框架本身是直接复用的。\n\n**[AGREE] R2-W4: Related Work 缺失**\n\n同意缺少以下文献会影响方法论讨论：\n- **(a) 教育测量中 cross-test G-study 文献**——这直接关联论文的 cross-benchmark comparison，如果教育测量领域已有类似的 cross-test variance gradient 发现，论文应讨论。\n- **(c) GLMM 在 NLP evaluation 中的应用**——这与我的 N1（binary data G-theory）直接相关。GLMM 是 binary data 上的正确方法，如果 NLP 领域已有 GLMM 应用，论文更应对比。\n- (b) benchmark contamination 对 item_id 的影响——这是一个有趣的 confound，如果某些模型在训练中见过 benchmark items，item_id variance 的解读会改变。\n\n**[AGREE] R2-W5: Fine-tuning G-study 超出核心 scope**\n\n同意。论文标题是 \"LLM Evaluation\"，Section 6.2 的 RoBERTa fine-tuning 是 encoder-only model 的 training variance，与 LLM inference evaluation 是完全不同的 evaluation paradigm。论文自己也承认 \"decoder fine-tuning may differ due to autoregressive generation during evaluation\"（Section 6.2）。\n\n建议：要么删除 Section 6.2，要么将其明确标注为 \"out-of-scope preliminary observation\" 并压缩到 1-2 句。当前占据了约半页 Discussion 空间，对核心 claims 没有贡献。\n\n---\n\n### 小问题\n\n- **\"Section 3 缺少 balanced vs unbalanced design 对 Henderson I 影响的讨论\"**——[AGREE]，与我的 W3 完全一致。\n- **\"Table 6 trend 列略 informal\"**——[AGREE]，\"↓ monotonic\" 等标注应替换为 Spearman ρ + p-value。\n- **\"Limitations 未讨论 task type coverage\"**——[AGREE]，这是 N1 的 downstream consequence。\n- **\"References 格式不一致\"**——[AGREE]，presentation 层面问题。\n\n---\n\n### 综合评估\n\nR2 和我的审稿意见在多个维度上 convergent：\n- **Overclaim risk**：R2-N1（benchmark coverage）+ R1-W2（post-hoc ordering）→ gradient claim 需要 scope down\n- **Binary data validity**：R1-N1 + R2-W4(c)（缺少 GLMM 讨论）→ 需要更严格的 binary data 理论辩护\n- **Design transparency**：R1-W3 + R2 小问题（balanced design 讨论）→ 需要 design matrix 表\n\n**我维持 Overall 3.5/5**。R2 的 N1 加强了我对 overclaim 的担忧，但论文的 empirical contribution 仍然 substantial——即使 gradient 的 generality 受限，\"variance structure is benchmark-conditional\" 这一定性结论在 5 个 benchmarks 上 consistently hold，对 practitioner 有直接价值。",
  "reviewer_id": "1",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 Round 1 意见的交叉回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1: Cross-benchmark gradient 的 generality claim 超出 5 个 benchmarks 的实验基础**\n\n同意这是一个实质性问题。我在自己的 W2 中也指出了 \"reasoning complexity\" 排序是 post-hoc 的，但 R2 的论述更尖锐且补充了关键统计论据：\n\n1. **n=5 时 Spearman ρ=1.0 的 p≈0.017**——R2 正确指出这在统计上并不 overwhelming，尤其考虑到 ranking 本身 non-independent（derived from same data）。\n2. **Task type coverage 确实是 blind spot**——5 个 benchmarks 全部是 closed-form QA（multiple-choice 或 short-answer math），完全没有 generation-heavy tasks（summarization、translation、instruction following）。论文的 \"no universal recipe\" claim 在逻辑上需要覆盖更多 task types 才能成立。\n3. **Title 和 framing 的 overclaim**——\"Across Benchmarks\" 在字面上暗示 general coverage，但实际只覆盖了 knowledge-to-reasoning 这一条轴。\n\n补充我的发现：我在 W2 中指出了 item_id 与 model×item 之间存在机械负相关（两者是 variance decomposition 中最大的两个分量，总和受约束），这进一步削弱了\"perfect inverse monotonicity\"作为 empirical finding 的 informativeness。R2 的 task type coverage 论点和我的 mechanical correlation 论点共同构成对 gradient claim 的 convergent critique。\n\n**建议**：将 claim 限定为 \"across closed-form QA benchmarks spanning knowledge retrieval to mathematical reasoning\"，并在 Limitations 中明确讨论 generation tasks 的缺失。\n\n---\n\n### Should-Fix\n\n**[AGREE] R2-W1: IRT vs G-theory 对比方向上是数学必然**\n\n同意方向性结论（G-theory 需要更多 items）是 trivially true——G-theory 模型化了更多 variance sources，必然需要更多 items 来 stabilize 这些额外分量。论文的 empirical contribution 在于量化了 ratio（3.6-4.6×），但 \"G-theory requires 3.6-4.6× more items\" 不应被框架为一个 surprising finding。\n\n补充：我在审稿中将 IRT 对比列为\"主要优势\"之一，现在认为应重新定位——它的价值是 **practitioner-facing quantification**（\"如果你按 IRT 建议用 116 items，actual reliability 只有 0.529\"），而非 theoretical insight。建议作者将 C3 表述为 \"first empirical quantification of the multi-facet reliability gap\"。\n\n**[REBUT] R2-W2: \"No universal recipe\" 叙事被 actual recommendations 削弱**\n\n部分不同意。R2 的论据是跨 benchmark 的推荐差异主要体现在 item count（414 vs 648，1.6×），其他 facet 推荐\"几乎一致\"（prompts 3-4, seeds 3-5）。但：\n\n1. **Item count 差异本身就是实质性的**——从 MMLU 414 items 到 MATH 648 items 是 56% 的增加，对 compute budget 有直接影响。Table 9 显示 G≥0.90 时差距更大（MMLU 820 vs GSM8K 1180，44% increase）。\n2. **Facet 推荐的\"一致性\"恰恰是一个 finding**——即 methodological facets（prompts, seeds）的 optimal budget 相对 stable，而 item budget 是 benchmark-conditional。这**不等于**\"universal recipe exists\"——它等于\"recipe 的 methodology 部分 portable，item 部分不 portable\"。\n3. 但 R2 有一个合理内核：**\"no universal recipe\" 的措辞确实 overclaim**。更准确的表述是 \"item budget is benchmark-conditional; methodological protocol is largely transferable\"。这与论文当前的 dramatic framing (\"no universal reproducibility recipe\") 有落差。\n\n**结论**：叙事需要 recalibrate，但不应完全反转为 \"recipe is largely stable\"。实际 finding 介于两个极端之间。\n\n**[AGREE] R2-W3: 与 Mesting (2026) 的差异化偏弱**\n\n新颖性/相关工作不在我的审查范围内，无法独立评判。但从方法论角度，R2 的观察与我的审稿一致——论文的 contribution 更多是 empirical scale-up（更多 benchmarks、更多 models、加入 infrastructure）而非 methodological innovation。G-theory 框架本身是直接复用的。\n\n**[AGREE] R2-W4: Related Work 缺失**\n\n同意缺少以下文献会影响方法论讨论：\n- **(a) 教育测量中 cross-test G-study 文献**——这直接关联论文的 cross-benchmark comparison，如果教育测量领域已有类似的 cross-test variance gradient 发现，论文应讨论。\n- **(c) GLMM 在 NLP evaluation 中的应用**——这与我的 N1（binary data G-theory）直接相关。GLMM 是 binary data 上的正确方法，如果 NLP 领域已有 GLMM 应用，论文更应对比。\n- (b) benchmark contamination 对 item_id 的影响——这是一个有趣的 confound，如果某些模型在训练中见过 benchmark items，item_id variance 的解读会改变。\n\n**[AGREE] R2-W5: Fine-tuning G-study 超出核心 scope**\n\n同意。论文标题是 \"LLM Evaluation\"，Section 6.2 的 RoBERTa fine-tuning 是 encoder-only model 的 training variance，与 LLM inference evaluation 是完全不同的 evaluation paradigm。论文自己也承认 \"decoder fine-tuning may differ due to autoregressive generation during evaluation\"（Section 6.2）。\n\n建议：要么删除 Section 6.2，要么将其明确标注为 \"out-of-scope preliminary observation\" 并压缩到 1-2 句。当前占据了约半页 Discussion 空间，对核心 claims 没有贡献。\n\n---\n\n### 小问题\n\n- **\"Section 3 缺少 balanced vs unbalanced design 对 Henderson I 影响的讨论\"**——[AGREE]，与我的 W3 完全一致。\n- **\"Table 6 trend 列略 informal\"**——[AGREE]，\"↓ monotonic\" 等标注应替换为 Spearman ρ + p-value。\n- **\"Limitations 未讨论 task type coverage\"**——[AGREE]，这是 N1 的 downstream consequence。\n- **\"References 格式不一致\"**——[AGREE]，presentation 层面问题。\n\n---\n\n### 综合评估\n\nR2 和我的审稿意见在多个维度上 convergent：\n- **Overclaim risk**：R2-N1（benchmark coverage）+ R1-W2（post-hoc ordering）→ gradient claim 需要 scope down\n- **Binary data validity**：R1-N1 + R2-W4(c)（缺少 GLMM 讨论）→ 需要更严格的 binary data 理论辩护\n- **Design transparency**：R1-W3 + R2 小问题（balanced design 讨论）→ 需要 design matrix 表\n\n**我维持 Overall 3.5/5**。R2 的 N1 加强了我对 overclaim 的担忧，但论文的 empirical contribution 仍然 substantial——即使 gradient 的 generality 受限，\"variance structure is benchmark-conditional\" 这一定性结论在 5 个 benchmarks 上 consistently hold，对 practitioner 有直接价值。",
    "reviewer_id": "1",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-21T08:43:34.679688+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 7244
}
```

</details>

---


### Assistant

_source line 52 · 2026-05-21T08:43:40.699580+00:00_

交叉回应已提交。对 R2 的 5 条 Must-Fix/Should-Fix 意见：3 条 AGREE（N1 benchmark coverage overclaim、W1 IRT 对比数学必然性、W5 fine-tuning scope creep），1 条 REBUT（W2 "no universal recipe" 叙事——item budget 差异本身是实质性的），1 条 AGREE-with-scope-note（W3 差异化偏弱，但新颖性不在我审查范围内）。R2 的 W4 中 GLMM 文献缺失与我的 N1（binary data G-theory validity）形成 convergent critique。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1"
}
```

</details>

---


## Round 3

## Round 3

64 recorded events


### User

_source line 53 · 2026-05-22T02:57:45.437961+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性 + 实验设计 + 统计分析**。

## Venue 信息
- **目标会议**: AAAI 2027 Main Technical Track
- **截止日期**: 2026-07-28
- **格式**: 7 页正文 + 无限参考文献，双栏 US Letter，双盲审稿
- **模板**: aaai2026 样式包（AAAI 2027 模板尚未发布）

## 论文路径
- LaTeX 源码: `projects/nlp_variance_gtheory/docs/paper/main.tex`（各章节为独立 .tex 文件）
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/submitted.pdf`

## 审查侧重

请重点审查以下方面：

1. **G-theory 方法论**：Henderson Method I 用于二值数据是否合理？论文提供的四项 robustness check（simulation, GLMM, accuracy-range stability, estimator guarantee）是否充分论证了 binary data 上 G-theory 的有效性？是否存在遗漏的假设或限制？

2. **实验设计**：
   - 7-facet crossed design 的合理性——facet 选择是否全面？是否遗漏了关键变异来源（如 GPU 型号、batch size、decoding strategy）？
   - 200 items × 8 models × 5 benchmarks 的样本量是否足够支撑方差分解的精度？
   - "quasi-random" model facet 处理是否合理？8 个 7-9B 模型是否足以代表更广泛的模型群体？
   - exp-002 降低 crossing（BF16 only, 2 temps）是否引入了 confounding？

3. **统计分析**：
   - Bootstrap CI（1000 resamples）是否充分？resampling 单元是什么（item-level? observation-level?）？
   - Permutation test（p=0.10, n=5 benchmarks）的统计效力——5 个 benchmark 是否足以支撑 format-conditional 的核心 claim？
   - D-study projection 的外推有效性——从 200 items 外推到 55 items 或 552 items 是否可靠？
   - Cohen's d=1.73 在 n=5 时的可信度

4. **Claims 与 evidence 的匹配**：
   - "10.0× fewer items" claim 是否 over-stated？这个比率的 CI 是多少？
   - "item dominance" 在 free-form 上不成立——这是否削弱了论文的核心叙事？
   - IRT comparison（G=0.457）是否公平？IRT 的目标函数与 G-theory 不同

5. **Robustness**：
   - 6 项 robustness check 是否覆盖了主要威胁？
   - Leave-one-model-out 检查是否充分验证了 model-as-facet 假设？
   - Item resampling（3 samples）的覆盖面是否足够？

请提交完整审稿意见，包含 Summary、Strengths、Weaknesses、Questions、Overall Assessment（含评分）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-22T02:58:02.765777+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-22T02:58:03.578039+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 812
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-22T02:58:03.578516+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 57 · 2026-05-22T02:58:03.629052+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-22T02:58:08.106698+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AAAI 2027 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AAAI 2027 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 59 · 2026-05-22T02:58:09.009773+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AAAI 2026 2027 review form scoring dimensions technical track"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AAAI 2026 2027 review form scoring dimensions technical track"
  }
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-22T02:58:10.715613+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/submitted.pdf",
  "project": "nlp_variance_gtheory",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/submitted.pdf",
    "project": "nlp_variance_gtheory",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-22T02:58:17.859048+00:00_

Web search results for query: "AAAI 2027 reviewer guidelines review form criteria"

Links: [{"title":"Reviewer Guidelines | Archives of Asthma, Allergy and Immunology","url":"https://www.allergyimmunoljournal.com/index.php/aaai/reviewer-guidelines"},{"title":"AAAI Publication Policies & Guidelines - AAAI","url":"https://aaai.org/aaai-publications/aaai-publication-policies-guidelines/"},{"title":"Instructions for AAAI-26 Reviewers - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/instructions-for-aaai-26-reviewers/"},{"title":"Guidelines for reviewing manuscripts submitted to Animal Bioscience","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7876709/"},{"title":"Reviewing the review: a qualitative assessment of the peer review process in surgical journals","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5964882/"}]

The search results show information about AAAI publication policies and reviewer guidelines, but the results don't contain specific information about AAAI 2027 reviewer guidelines or a review form with specific criteria. 

From the search results, I found that AAAI publication policies and guidelines provide instructions and forms for authors, and author kits for specific conferences can be downloaded. I also found a reference to instructions for AAAI-26 reviewers, but the detailed content wasn't available in the search results.

The search results primarily returned general peer review guidelines from medical journals and information about AAAI's publication ethics policies, rather than the specific AAAI 2027 conference reviewer form and criteria you're looking for. To get the actual AAAI 2027 reviewer guidelines and review form, you would likely need to:

1. Visit the official AAAI 2027 conference website directly
2. Check the AAAI conferences page at aaai.org for the specific conference
3. Contact the AAAI conference organizers directly

Would you like me to search for more specific information about accessing AAAI 2027 reviewer materials
…[truncated 104 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9752
}
```

</details>

---


### Tool result

_source line 62 · 2026-05-22T02:58:28.647956+00:00_

Web search results for query: "AAAI 2026 2027 review form scoring dimensions technical track"

Links: [{"title":"Main Technical Track: Call for Papers - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/main-technical-track-call/"},{"title":"AAAI-27 Main Technical Track - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/"},{"title":"Ethical and Social Considerations of Applying Artificial Intelligence in Healthcare; a Two-Pronged Scoping Review","url":"https://www.medrxiv.org/content/10.1101/2025.02.10.25321994.full.pdf"},{"title":"Are numerical scores important for grant assessment? A cross-sectional study","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11362741/"},{"title":"AAAI-26 Main Technical Track - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/main-technical-track/"},{"title":"Large language models for abstract screening in systematic- and scoping reviews: A diagnostic test accuracy study","url":"https://www.medrxiv.org/content/10.1101/2024.10.01.24314702.full.pdf"},{"title":"Instructions for AAAI-26 Reviewers - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/instructions-for-aaai-26-reviewers/"},{"title":"Phase 3 Randomized, Double-Blind, Placebo-Controlled Study to Evaluate Sialic Acid in Patients With Glucosamine (UDP-N-acetyl)-2-epimerase Myopathy (GNEM) or Hereditary Inclusion Body Myopathy (HIBM)","url":"https://cdn.clinicaltrials.gov/large-docs/21/NCT02377921/SAP_001.pdf"}]

Based on the search results, I found information about AAAI-26 and AAAI-27 submission evaluation criteria:

## AAAI-26 Main Technical Track Evaluation Criteria

All submissions will be evaluated and scored for the significance and novelty of the contributions (research problems or questions addressed, methods, experiments, analyses), theoretical and/or empirical soundness of the claims, their relevance to the AAAI community, and clarity of exposition.

Additional considerations include adherence to responsible research practice
…[truncated 957 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 19638
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-22T02:58:28.748799+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"页码超出范围 (共 9 页): 1-10\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 18033
}
```

</details>

---


### Tool call

_source line 64 · 2026-05-22T02:58:42.751592+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/submitted.pdf",
  "project": "nlp_variance_gtheory",
  "pages": "1-9",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/submitted.pdf",
    "project": "nlp_variance_gtheory",
    "pages": "1-9",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-22T02:58:44.667618+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p1.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 428.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p2.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 537.3}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p3.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 484.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p4.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 475.6}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p5.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 497.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p6.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 445.3}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p7.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 475.1}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p8.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 555.4}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p9.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 93.6}], \"total_pa
…[truncated 218 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1916
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-22T02:58:44.668117+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aaai.org/conference/aaai/aaai-26/instructions-for-aaai-26-reviewers/",
  "prompt": "Extract the complete review form dimensions, scoring scales, and evaluation criteria. List all scoring dimensions with their scale ranges and descriptions. Include any guidance on what constitutes each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aaai.org/conference/aaai/aaai-26/instructions-for-aaai-26-reviewers/",
    "prompt": "Extract the complete review form dimensions, scoring scales, and evaluation criteria. List all scoring dimensions with their scale ranges and descriptions. Include any guidance on what constitutes each score level."
  }
}
```

</details>

---


### Tool call

_source line 67 · 2026-05-22T02:58:47.784588+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/",
  "prompt": "Extract the complete evaluation criteria, review dimensions, submission requirements (page limits, formatting), and any specific review form details for AAAI-27 Main Technical Track."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/",
    "prompt": "Extract the complete evaluation criteria, review dimensions, submission requirements (page limits, formatting), and any specific review form details for AAAI-27 Main Technical Track."
  }
}
```

</details>

---


### Tool result

_source line 68 · 2026-05-22T02:58:49.691006+00:00_

# AAAI-26 Review Form Dimensions and Scoring

Based on the provided content, **the document does not contain a complete review form with specific scoring scales or dimensions.**

The "Instructions for AAAI-26 Reviewers" page provides guidance on **how to write helpful reviews** but does not include:

- Numbered or named scoring dimensions
- Specific numerical rating scales (e.g., 1-5, 1-10)
- Defined score level descriptions
- Official evaluation rubrics

## What Is Provided Instead

The instructions offer **qualitative evaluation guidance** organized around these topics:

1. **Paper Clarity**: Problem articulation, state-of-the-art limitations, and claim support
2. **Technical Approach**: Soundness, clarity, reproducibility, and limitation acknowledgment
3. **Related Work**: Contextual positioning
4. **Empirical Evaluation**: Baselines, metrics, benchmarks, error analysis
5. **Improvement Suggestions**: Research and presentation enhancement

The document emphasizes that reviewers should adopt a constructive mindset: "Instead of 'What is wrong with this paper?', ask yourself 'How could this paper be better?'"

## Note

The actual scoring form likely exists in the submission system (Open Review) but is not included in this webpage content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5022
}
```

</details>

---


### Tool result

_source line 69 · 2026-05-22T02:58:51.798123+00:00_

# AAAI-27 Main Technical Track: Evaluation Criteria & Requirements

Based on the provided content, I cannot extract the complete evaluation criteria, review dimensions, submission requirements, or specific review form details you've requested.

## What the Page Contains

The webpage displays the **Main Conference Timetable for Authors**, including key deadlines:

- Abstract submission: "July 21, 2026"
- Full paper deadline: "July 28, 2026"
- Supplementary materials: "July 31, 2026"
- Final notification: "November 30, 2026"

## What is Missing

The page explicitly states that the "Call for Papers" section shows: **"Coming Soon"**

This indicates the detailed submission guidelines, page limits, formatting requirements, evaluation criteria, and review form specifics have not yet been published. These details typically appear once the full call for papers is released closer to the submission period.

**Recommendation:** Check back on the AAAI-27 Call for Papers page or contact AAAI directly once the comprehensive guidelines become available.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 4013
}
```

</details>

---


### Tool call

_source line 70 · 2026-05-22T02:58:59.467737+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AAAI 2026 OpenReview review form dimensions scoring scale overall recommendation soundness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AAAI 2026 OpenReview review form dimensions scoring scale overall recommendation soundness"
  }
}
```

</details>

---


### Tool call

_source line 71 · 2026-05-22T02:58:59.919684+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 72 · 2026-05-22T02:59:00.925435+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 73 · 2026-05-22T02:59:00.925765+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 74 · 2026-05-22T02:59:01.376980+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 75 · 2026-05-22T02:59:01.377310+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 76 · 2026-05-22T02:59:01.878627+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 77 · 2026-05-22T02:59:01.878953+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 78 · 2026-05-22T02:59:01.879119+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 79 · 2026-05-22T02:59:02.380657+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 80 · 2026-05-22T02:59:02.432545+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 81 · 2026-05-22T02:59:33.055873+00:00_

Web search results for query: "AAAI 2026 OpenReview review form dimensions scoring scale overall recommendation soundness"

Links: [{"title":"AAAI 2026 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/aaai-statistics/aaai-2026-statistics/"},{"title":"AAAI 2026 | OpenReview","url":"https://openreview.net/group?id=AAAI.org%2F2026"},{"title":"AAAI 2026 AI Alignment Track | OpenReview","url":"https://openreview.net/group?id=AAAI.org%2F2026%2FAI_Alignment_Track"},{"title":"AAAI 2026 Conference | OpenReview","url":"https://openreview.net/group?id=AAAI.org%2F2026%2FConference"},{"title":"AAAI 2026 Demonstration Program | OpenReview","url":"https://openreview.net/group?id=AAAI.org/2026/Demonstration_Program"},{"title":"AAAI | OpenReview","url":"https://openreview.net/group?id=AAAI.org"},{"title":"IntelliAsk: Learning to Ask High-Quality Research Questions via RLVR","url":"https://arxiv.org/pdf/2602.15849"},{"title":"Are numerical scores important for grant assessment? A cross-sectional study","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11362741/"},{"title":"The effect of the scale of grant scoring on ranking accuracy","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9938341/"},{"title":"AAAI-26 Review Process Update: Scale, Integrity Measures, and Pathways to Sustainability - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/review-process-update/"}]

Let me search more specifically for the AAAI 2026 review form details:

Links: [{"title":"Reviewer Guidelines","url":"https://virtual.aistats.org/Conferences/2026/ReviewerGuidelines"},{"title":"Reviewer Instructions","url":"https://docs.google.com/document/u/0/d/1tqQGwtNUlALPSTqoTo5uTFx8vKuqpILNTne9jeBCOVI/mobilebasic"},{"title":"Submission Instructions (Main Technical Track) | AAMAS","url":"https://cyprusconferences.org/aamas2026/submission-instructions/"},{"title":"AAAI-26 Review Process - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/review-process/"},{"title":"Instructions for A
…[truncated 6494 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 33588
}
```

</details>

---


### Tool call

_source line 82 · 2026-05-22T02:59:41.547556+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/",
  "description": "List PDF image files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/",
    "description": "List PDF image files"
  }
}
```

</details>

---


### Tool result

_source line 83 · 2026-05-22T02:59:41.698520+00:00_

submitted_p1.png
submitted_p2.png
submitted_p3.png
submitted_p4.png
submitted_p5.png
submitted_p6.png
submitted_p7.png
submitted_p8.png
submitted_p9.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 84 · 2026-05-22T02:59:46.015749+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 85 · 2026-05-22T02:59:46.519922+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 86 · 2026-05-22T02:59:47.476025+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1460
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-22T02:59:47.477470+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 88 · 2026-05-22T02:59:47.477786+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 89 · 2026-05-22T02:59:47.929425+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 90 · 2026-05-22T02:59:48.231550+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 91 · 2026-05-22T02:59:48.231986+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 92 · 2026-05-22T02:59:48.786929+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-22T02:59:49.189135+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 94 · 2026-05-22T03:00:03.775665+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 95 · 2026-05-22T03:00:04.030737+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-22T03:00:04.435103+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-22T03:00:05.443991+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1668
}
```

</details>

---


### Tool result

_source line 98 · 2026-05-22T03:00:05.445224+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1414
}
```

</details>

---


### Tool call

_source line 99 · 2026-05-22T03:00:05.449704+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 100 · 2026-05-22T03:00:05.902020+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1466
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-22T03:00:05.903414+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-22T03:00:07.106595+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aaai.org/conference/aaai/aaai-26/review-process/",
  "prompt": "Extract the complete review form dimensions and scoring scales used for AAAI-26 reviews. List all rating dimensions (e.g., overall recommendation, soundness, novelty, clarity, significance, confidence) with their scale ranges and what each score level means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aaai.org/conference/aaai/aaai-26/review-process/",
    "prompt": "Extract the complete review form dimensions and scoring scales used for AAAI-26 reviews. List all rating dimensions (e.g., overall recommendation, soundness, novelty, clarity, significance, confidence) with their scale ranges and what each score level means."
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-22T03:00:11.469603+00:00_

# AAAI-26 Review Form Dimensions and Scoring Scales

Based on the provided webpage content, **I cannot extract the complete review form dimensions and scoring scales** for AAAI-26 reviews.

## What's Available

The webpage describes the **two-phase review process structure**:
- Phase 1: Three reviewers per paper
- Phase 2: Additional reviewers who don't see Phase 1 reviews initially
- Author feedback window: October 7-13, 2025
- Final decisions: November 8, 2025

However, the actual **review rating dimensions, scale ranges, and score definitions are not included** in this webpage content.

## Where to Find This Information

The page references several related documents that likely contain this information:
- "Instructions for AAAI-26 Reviewers" (linked as a Google Doc)
- "Ethical Guidelines for AAAI-26 Reviewers"
- "FAQ for the AI-Assisted Peer-Review Process Pilot Program"

To obtain the complete review form specifications, you would need to access these supplementary documents directly, which are not reproduced in the webpage excerpt provided.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 4363
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-22T03:00:19.299698+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AAAI conference review form \"overall assessment\" score 1-10 soundness novelty significance clarity site:openreview.net OR site:aaai.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AAAI conference review form \"overall assessment\" score 1-10 soundness novelty significance clarity site:openreview.net OR site:aaai.org"
  }
}
```

</details>

---


### Tool call

_source line 105 · 2026-05-22T03:00:20.054059+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AAAI 2025 2026 review form rating scale \"strong reject\" \"weak accept\" \"strong accept\" reviewer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AAAI 2025 2026 review form rating scale \"strong reject\" \"weak accept\" \"strong accept\" reviewer"
  }
}
```

</details>

---


### Tool result

_source line 106 · 2026-05-22T03:00:27.384609+00:00_

Web search results for query: "AAAI conference review form "overall assessment" score 1-10 soundness novelty significance clarity site:openreview.net OR site:aaai.org"

Links: [{"title":"Main Technical Track: Call for Papers - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/main-technical-track-call/"},{"title":"Reviewer Guidelines","url":"https://virtual.aistats.org/Conferences/2026/ReviewerGuidelines"},{"title":"Reviewer Guidelines| Artificial Intelligence and Statistics Conference","url":"https://aistats.org/aistats2025//reviewer_guidelines.html"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"AAAI 2026 Conference | OpenReview","url":"https://openreview.net/group?id=AAAI.org%2F2026%2FConference"},{"title":"AAAI 2025 Conference | OpenReview","url":"https://openreview.net/group?id=AAAI.org%2F2025%2FConference"},{"title":"OpenReviewer: A Specialized Large Language Model for Generating Critical   Scientific Paper Reviews","url":"https://arxiv.org/pdf/2412.11948"},{"title":"AAAI-26 Review Process - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/review-process/"},{"title":"What Drives Paper Acceptance? A Process-Centric Analysis of Modern Peer Review","url":"https://arxiv.org/pdf/2509.25701"}]

I found some relevant information about AAAI's review evaluation criteria. Based on the search results:

All submissions to AAAI are evaluated and scored for the significance and novelty of the contributions, theoretical and/or empirical soundness of the claims, their relevance to the AAAI community, and clarity of exposition.

However, the search results did not return the specific AAAI review form with the 1-10 scoring scale you're looking for. The OpenReview pages for AAAI 2026 and 2025 conferences (results 5 and 6) appear to exist but only show landing pages without detailed content.

The results did show that other conferences like AISTATS use fine-grained evaluation based on three key aspects: Soundness, Significance, and Nove
…[truncated 501 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 8084
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-22T03:00:55.254059+00:00_

Web search results for query: "AAAI 2025 2026 review form rating scale "strong reject" "weak accept" "strong accept" reviewer"

Links: [{"title":"AAAI-26 Review Process Update: Scale, Integrity Measures, and Pathways to Sustainability - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/review-process-update/"},{"title":"ReviewerToo: Should AI Join The Program Committee? A Look At The Future of Peer Review","url":"https://arxiv.org/html/2510.08867v1"},{"title":"AAAI 2025 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/aaai-statistics/aaai-2025-statistics/"},{"title":"Overview of the AI Review System","url":"https://aaai.org/wp-content/uploads/2025/08/FAQ-for-the-AI-Assisted-Peer-Review-Process-Pilot-Program.pdf"},{"title":"Thank you to our 2025 reviewers","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12905618/"},{"title":"Instructions for AAAI-26 Reviewers - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/instructions-for-aaai-26-reviewers/"},{"title":"Thank you to our 2025 reviewers","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12853355/"},{"title":"Are reviewers suggested by authors as good as those chosen by editors? Results of a rater-blinded, retrospective study","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1482713/"},{"title":"Thank you to our 2025 reviewers","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12921489/"},{"title":"Thanks to reviewers list 2025","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12795292/"}]

The search results provide some information about AAAI-26's review process but don't include specific details about the rating scale with terms like "strong reject," "weak accept," and "strong accept." Let me search more specifically for the AAAI review rating scale details.

Links: [{"title":"Reviewer Guidelines","url":"https://neurips.cc/Conferences/2022/ReviewerGuidelines"},{"title":"Uncertainty in Artificial Intelligence","url":"https://www.auai.org/uai2022/reviewing_instructions"},
…[truncated 5132 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 35199
}
```

</details>

---


### Tool call

_source line 108 · 2026-05-22T03:01:03.742280+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2604.13940v1",
  "prompt": "Extract the AAAI review form dimensions and scoring scales. Look for information about: overall recommendation scale (1-10), soundness, novelty, significance, clarity, confidence, and what each score level means. List all rating dimensions used in AAAI peer review."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2604.13940v1",
    "prompt": "Extract the AAAI review form dimensions and scoring scales. Look for information about: overall recommendation scale (1-10), soundness, novelty, significance, clarity, confidence, and what each score level means. List all rating dimensions used in AAAI peer review."
  }
}
```

</details>

---


### Tool call

_source line 109 · 2026-05-22T03:01:04.997712+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://papercopilot.com/statistics/aaai-statistics/aaai-2026-statistics/",
  "prompt": "Extract the review rating scale used at AAAI 2026. Look for information about the scoring dimensions, overall rating scale (e.g., 1-10), and what each score level means (accept, reject, etc.)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://papercopilot.com/statistics/aaai-statistics/aaai-2026-statistics/",
    "prompt": "Extract the review rating scale used at AAAI 2026. Look for information about the scoring dimensions, overall rating scale (e.g., 1-10), and what each score level means (accept, reject, etc.)."
  }
}
```

</details>

---


### Tool result

_source line 110 · 2026-05-22T03:01:09.377374+00:00_

# AAAI Review Form Analysis

Based on the provided document, **the AAAI-26 AI Review Pilot does not describe a traditional numerical scoring scale** for peer reviews.

## Key Findings

The document explicitly states that the AI review system was designed to **exclude scores entirely**:

> "The AI review system did not include any scores or recommendations, and no human reviewers were replaced in the process."

## What the System Evaluated Instead

Rather than using numerical ratings, the AI reviews assessed papers across five **qualitative dimensions**:

1. **Story** - Problem formulation and contribution clarity
2. **Presentation** - Writing clarity and organization
3. **Evaluations** - Experimental methodology sufficiency
4. **Correctness** - Mathematical and algorithmic accuracy
5. **Significance** - Novelty and positioning relative to prior work

## Survey Assessment Scale

The community feedback survey used a **five-point Likert scale** (not for paper ratings, but for evaluating review quality):
- -2: Strongly disagree
- -1: Disagree
- 0: Neutral
- 1: Agree
- 2: Strongly agree

The document does not reveal the specific numerical scoring dimensions (1-10 scales, confidence levels, etc.) that standard AAAI reviews might use, as it focuses on this experimental AI-assisted system rather than traditional review forms.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5635
}
```

</details>

---


### Tool result

_source line 111 · 2026-05-22T03:01:10.288617+00:00_

# AAAI 2026 Review Rating Scale

Based on the webpage content provided, **specific information about the review rating scale for AAAI 2026 is not detailed**.

The page only shows that community form data was collected with "92 responses · 86 valid · 1 rebuttal," and displays aggregate statistics indicating "min:6.30 max:6.30 avg:6.30 std:0.00" for ratings. However, this appears to represent summary statistics rather than an explanation of the actual rating scale.

The interface mentions options for viewing "[Collected] Rating" and "[OpenReview] Rating" metrics, suggesting reviewers submitted scores, but the document does not explain:
- The numerical range of the rating scale
- What each score level signifies
- Acceptance thresholds
- Scoring criteria or dimensions

To find the actual AAAI 2026 review guidelines and rating scale definitions, you would need to consult the official AAAI 2026 call for papers or reviewer instructions, which are not included in this webpage excerpt.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 5290
}
```

</details>

---


### Tool call

_source line 112 · 2026-05-22T03:01:22.212559+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://forum.cspaper.org/topic/154/aaai-2026-first-round-results-high-scores-rejected-ai-reviews-useful",
  "prompt": "Extract the AAAI 2026 review form rating scale. Look for the overall recommendation scale (what numbers mean what, e.g., 1=reject, 10=accept), and any other review dimensions like soundness, novelty, significance, clarity, confidence."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://forum.cspaper.org/topic/154/aaai-2026-first-round-results-high-scores-rejected-ai-reviews-useful",
    "prompt": "Extract the AAAI 2026 review form rating scale. Look for the overall recommendation scale (what numbers mean what, e.g., 1=reject, 10=accept), and any other review dimensions like soundness, novelty, significance, clarity, confidence."
  }
}
```

</details>

---


### Tool result

_source line 113 · 2026-05-22T03:01:22.413368+00:00_

REDIRECT DETECTED: The URL redirects to a different host.

Original URL: https://forum.cspaper.org/topic/154/aaai-2026-first-round-results-high-scores-rejected-ai-reviews-useful
Redirect URL: https://cspaper.org/articles
Status: 301 Moved Permanently

To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
- url: "https://cspaper.org/articles"
- prompt: "Extract the AAAI 2026 review form rating scale. Look for the overall recommendation scale (what numbers mean what, e.g., 1=reject, 10=accept), and any other review dimensions like soundness, novelty, significance, clarity, confidence."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 200
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-22T03:07:16.722576+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 审稿意见：Format-Conditional Variance Structure in LLM Evaluation: A Generalizability Theory Approach\n\n**目标会议**: AAAI 2027 Main Technical Track\n**审查侧重**: 方法严谨性 + 实验设计 + 统计分析\n\n---\n\n## 总体评分\n\n**Overall**: 6/10 (Weak Accept — marginally above acceptance threshold)\n\n**一句话总结**: 论文将 G-theory 引入 LLM 评测方差分解，核心发现（format-conditional variance structure）有实际价值且描述性证据充分，但其核心 claim 的形式化统计检验（permutation test, n=5）从根本上不具备充分的统计效力，model facet 的 quasi-random 处理也限制了结论的可推广性。\n\n---\n\n## 官方维度打分\n\n（基于 AAAI-26 CFP 公开评估标准 + AI Review Pilot 定性维度，AAAI 2027 review form 尚未发布）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | Henderson Method I 对 binary data 的 robustness 有四项验证但缺少标准心理测量方法（tetrachoric correlation）对比；permutation test 先天不足（n=5）；部分 claims 缺少 CI |\n| Novelty/Originality | 4/5 | 首次将多 benchmark、多 facet 全交叉 G-theory 设计应用于 LLM 评测，format-conditional 发现新颖；但 G-theory 本身非新方法 |\n| Significance | 3.5/5 | D-study budget 工具有明确实践价值；但 model facet 仅覆盖 7-9B，不能直接指导 API 模型或大规模模型评测 |\n| Clarity | 4/5 | 论文结构清晰，Figure 1-3 直观有效；但 bootstrap resampling unit 未明确说明，部分关键方法细节不足 |\n| Reproducibility | 3/5 | 实验规模大（2.3M records），facet 设计详细；但未提供代码/数据，resampling 细节缺失，FP32 实现 bug（fence.sage mode）的发现表明环境依赖性较强 |\n| Relevance to AAAI | 4/5 | AI 评测方法论是 AAAI 社区关注的问题，实验设计和统计方法有 broad interest |\n| Confidence | 4/5 | 我熟悉 G-theory、心理测量方法和 LLM evaluation 领域 |\n\n---\n\n## Summary\n\n本文将心理测量学中的 Generalizability Theory (G-theory) 应用于 LLM 评测的方差分解。通过 7-facet 全交叉设计（item, model, precision, prompt, temperature, seed, ordering），在 MMLU 上进行了 exp-001 全交叉实验（460,800 records），并通过 exp-002 将方差分解扩展到 5 个 benchmark（2,304,000 records）。核心发现是方差结构具有 format-conditional 特性：multiple-choice benchmark 中 item selection 贡献 34-38% 方差，而 free-form benchmark 中无单一主导来源（各因素贡献 5-24%）。论文还提供了 D-study budget 工具，证明 multi-facet 设计比 single-condition 设计可减少约 10× 的 items 需求。\n\n---\n\n## 主要优势\n\n**S1. 问题定义精准，研究设计系统性强。** 现有 LLM 评测方差研究多为 single-benchmark、single-facet，无法分离交互效应。本文的 7-facet 全交叉设计是该领域迄今最全面的方差分解尝试，实验规模（2.3M records across 5 benchmarks）也体现了充分的工程投入。\n\n**S2. Format-conditional 发现有实际价值。** Table 3 中 MC vs. FF benchmark 的方差结构差异非常显著（item 方差份额：37-54% vs. 2.9-6.4%），这一发现直接启示了不同 benchmark 类型应采用不同的评测优化策略。即使形式化检验力不足，描述性证据本身已足够引人注目。\n\n**S3. D-study budget 工具有明确的实践意义。** Figure 3 的 projection curves 和 55 items vs. 552 items 的对比，为 benchmark 设计者提供了可操作的指导。将 G-theory 从描述性分析推进到设计决策工具，是本文超越纯方法论贡献的亮点。\n\n**S4. Robustness 分析覆盖较广。** 6 项 robustness check（REML 对比、Bootstrap vs. jackknife CI、facet specification、LOMO、null calibration、item resampling）覆盖了主要的方法论关切，尤其是 LOMO 分析（G_item 0.877-0.889）有效地展示了 model composition 的稳定性。\n\n**S5. Precision separability 的实用发现。** BF16 和 FP16 在 binary scoring 下可互换（方差贡献 <0.01%）是有实用价值的结论，能帮助实践者简化评测配置。FP32 fence.sage mode 的发现也是有价值的社区知识。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Permutation test 先天不足：p=0.10 是该设计下可达到的最小 p 值\n\n- 具体位置：Section \"Format-Conditional Variance Structure\"（Page 6，Table 3 下方）\n- 问题：论文用 permutation test 检验 MC vs. FF benchmark 的方差结构差异，报告 p=0.10, n=5。然而，将 5 个 benchmark 分为 3 MC + 2 FF 的所有可能划分只有 C(5,2)=10 种。因此 **p=0.10 = 1/10 是理论上可达到的最小 p 值**，即使完美分离也无法拒绝 H₀ at α=0.05。论文报告 p=0.10 但未说明这一根本限制，读者可能误解为\"接近显著\"而非\"这是检验框架本身能给出的最强证据\"。\n- 为什么影响接收：\"Format-conditional variance structure\" 是论文标题中的核心 claim。如果支持该 claim 的唯一形式化检验在设计上就无法提供强证据，则该 claim 的证据基础不足。\n- 建议修改方向：(a) 在正文中明确说明 p=0.10 是 minimum achievable p-value，解释其含义；(b) 补充额外的 benchmarks 以增强检验力，或 (c) 放弃 permutation test，转而依赖描述性证据（Table 3 的效应量）和理论论证，而非 p-value；(d) 考虑 bootstrap-based test 或 Bayesian 分析作为替代。\n\n**N2** [critical] Model facet 的 quasi-random 处理严重限制了 claims 的可推广性\n\n- 具体位置：Section \"Experimental Design: MMLU\" → \"Models\" 和 Section \"Model-as-Facet Justification\"（Page 3-4）\n- 问题：G-theory 的 random facet 假设要求 facet levels 是从某个定义良好的 universe 中随机抽取的。论文选择了 8 个 7-9B 参数的 instruction-tuned 模型，并称之为\"quasi-random facet\"。但这些模型：(1) 参数量范围极窄（7-9B），不能代表 1B-405B 的全谱系；(2) 全部为 instruction-tuned，排除了 base models；(3) 全部为开源模型，排除了 API models（GPT-4o, Claude, Gemini）。LOMO 检查（G_item 0.877-0.889）仅验证了这 8 个模型内部的稳定性，但无法回答\"如果加入 70B 或 405B 模型，item difficulty profile 是否改变\"这个关键问题。\n- 为什么影响接收：论文的 title 和 abstract 使用了泛化表述\"LLM Evaluation\"而非\"7-9B Open-Weight Model Evaluation\"。如果方差结构随模型规模变化（例如，大模型可能使 item 方差缩小、model×item 交互变化），则核心结论的适用范围需大幅限缩。\n- 建议修改方向：(a) 在 title/abstract 中明确限定适用范围为 7-9B open-weight models；(b) 增加至少 2-3 个不同规模的模型（如 1-3B, 13B, 70B）验证方差结构的 scale-invariance；(c) 如不增加实验，至少在 Discussion 中提供 model scale 可能影响方差结构的理论分析。\n\n**N3** [critical] \"10.0× fewer items\" claim 缺少置信区间\n\n- 具体位置：Section \"Design-Dependent Reproducibility Budgets\"（Page 6-7）及 Conclusion\n- 问题：论文的核心实践 claim \"multi-facet designs require 10.0× fewer items\" 是一个点估计（55 items vs. 552 items），但未报告该比率的任何不确定性度量。论文提到 \"this ratio remains stable across subset sizes from 50 to 200 items (CV = 1.9%)\"，但这是跨 item pool size 的稳定性，不是估计误差的 CI。如果方差分量估计本身有不确定性（显然有），则 D-study 投射出的 item 数量也有不确定性。55 items 的 CI 可能是 [30, 90] 或 [45, 70]——这对实践指导有本质差异。\n- 为什么影响接收：这是论文的核心实用贡献之一。无 CI 的点估计在统计严谨性上不够。\n- 建议修改方向：通过 bootstrap（对 variance components 进行 bootstrap）或 parametric 方法计算 D-study projection 的 CI，并报告 10× ratio 的 CI。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] IRT 对比不公平——优化目标不同\n\n- 具体位置：Section \"IRT and Efficient Benchmarking\"（Page 6）及 Table 4\n- 问题：论文将 IRT-selected 116 items（G=0.457）与 G-theory multi-facet 设计（55 items, G≥0.80）对比，得出 G-theory \"更高效\"的结论。但 IRT 的目标函数是最大化 item information/discrimination（优化 θ 估计精度），而 G-theory 优化的是跨 facet 条件的 generalizability。两者是不同的优化目标。在 IRT 的框架内，这 116 个 items 可能已经是最优的；用 G-theory 的标准评估 IRT 的 item 选择，相当于用田径标准评价游泳成绩。\n- 建议：(a) 明确说明 IRT 和 G-theory 优化不同目标，对比是 illustrative 而非 definitive；(b) 补充一个公平对比：用相同的 116 items，分别报告在 IRT framework 和 G-theory framework 下的 reliability/information。\n\n**W2** [warning] Bootstrap resampling unit 未说明\n\n- 具体位置：Section \"Evaluation Protocol\"（Page 4）\n- 问题：论文报告 \"1,000 bootstrap resamples\" 但未说明 resampling unit 是 item-level、observation-level 还是 block-level。对于方差分量估计，resampling unit 的选择直接影响 CI 的有效性：item-level resampling 保留了 item-level 相关结构，而 observation-level resampling 可能低估 CI 宽度。\n- 建议：在 Method 中明确说明 resampling strategy（推荐 item-level block bootstrap）。\n\n**W3** [warning] Cohen's d=1.73 在 n₁=3, n₂=2 时置信区间极宽\n\n- 具体位置：Section \"Format-Conditional Variance Structure\"（Page 6）\n- 问题：论文报告 Cohen's d=1.73 作为 MC vs. FF 方差结构差异的效应量。但在 n₁=3（MC benchmarks）, n₂=2（FF benchmarks）下，d 的 sampling distribution 极为分散。粗略估计 95% CI 约为 [-0.5, 4.0]，这意味着该效应量的估计精度非常低。同样，论文报告的 CI [11.44, 21.02] 看起来像是均值差的 CI 而非 d 的 CI——如果是 d 的 CI，这也不正确（d 的 CI 应基于 noncentral t distribution）。\n- 建议：(a) 提供 d 的正确 CI（基于 noncentral t）；(b) 明确说明小样本下效应量估计的局限；(c) 考虑不报告 d，而是直接报告描述性的差异幅度。\n\n**W4** [warning] Exp-002 降低 crossing 可能引入 confounding\n\n- 具体位置：Section \"Cross-Benchmark Extension\"（Page 4）\n- 问题：Exp-002 为扩展到 5 个 benchmark，将设计从 3 precisions × 3 temperatures 简化为 BF16 only × 2 temperatures。这意味着 cross-benchmark 比较中，precision 和 temperature 的主效应及交互效应被吸收进了残差项。如果 precision 和 temperature 的交互效应在 MC 和 FF benchmark 上有不同模式（虽然 exp-001 在 MMLU 上显示其贡献小），则 exp-002 的 format-conditional 差异可能部分被这些被混淆的效应放大或掩盖。\n- 建议：在正文中讨论这一 confounding 的可能性，并提供 exp-001 中 BF16-only subset 与 full design 的方差分解对比，以证明简化不影响结论。\n\n**W5** [warning] Binary data 处理缺少与标准心理测量方法的对比\n\n- 具体位置：Section \"Binary Data Assumptions\"（Page 4）\n- 问题：心理测量领域处理 binary/ordinal 数据的标准方法是使用 tetrachoric/polychoric correlation（如 Muthén 1984; Holgado-Tello et al. 2010），而非直接在 0/1 数据上应用为连续数据设计的 ANOVA-based 估计。论文提供了 4 项 robustness check，但没有与 tetrachoric-based G-theory（如 Schroeders & Wilhelm 2011）或 GLMM-based variance decomposition（论文提到 GLMM 作为\"complement\"但未作为 primary analysis）进行系统对比。熟悉心理测量的 reviewer 会期望看到这一对比。\n- 建议：补充 tetrachoric-based decomposition 的结果作为 robustness check，或在 Discussion 中说明不使用该方法的理由。\n\n**W6** [warning] Item resampling 仅 3 个样本覆盖不足\n\n- 具体位置：Section \"Robustness Checks\"（Page 7）\n- 问题：论文从 full MMLU pool 中抽取了 3 个独立 200-item 样本验证方差结构稳定性。3 个样本远不足以刻画 variance components 的 sampling distribution。以 3 个观测估计一个分布的位置和离散度，置信水平极低。\n- 建议：增加到至少 30-50 个 bootstrap item sets，报告 variance components 的分布（中位数、IQR、95% range），以充分量化 item sampling variability。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Accuracy-range stability（Section \"Binary Data Assumptions\"）仅在 mean accuracy 0.6-0.72 范围内验证。对于 accuracy ≈ 0.3（如某些模型在 MATH 上的表现）或 accuracy ≈ 0.9 的情况，binary data 的 floor/ceiling effect 可能更显著。建议说明这一限制。\n\n- **M2**: MATH benchmark 中的 `highest_intermediate_math` subject 显示 item variance 仅 10.4%（接近 free-form pattern），但论文将 MATH 整体归为 free-form。这表明 format-conditional 差异可能更准确地描述为 item format（选择题 vs. 开放式）而非 benchmark category 的差异。建议讨论这一 nuance。\n\n- **M3**: 论文提到 \"quasi-random model facet\" 的 ratio 为 \"(3:6)\"（Page 3），但未解释这个比率的含义。推测是指某种固定/随机比例，但表述不清。\n\n- **M4**: Figure 2 中 HellaSwag 的 bar 看起来与其他 MC benchmark 的 pattern 接近但 item variance 份额（54.3%）异常高，而 Table 3 中 model×item 交互也不同（14.6% vs. MMLU 的 36.0%）。建议在正文中讨论 HellaSwag 的异质性——这可能进一步弱化 \"MC benchmarks share a common variance structure\" 的叙事。\n\n- **M5**: 格式检查——论文使用 AAAI 双栏格式，正文约 7 页（含 Limitations），References 占 1+ 页，Appendix 约半页。符合 AAAI 2027 的 7 页正文限制（假设 Limitations 不计入正文页数上限，需确认 AAAI 2027 的具体政策）。\n\n---\n\n## Questions for Authors\n\n**Q1**: 如果将 model facet 从 8 个 7-9B 模型扩展到包含 70B 模型，你预期方差结构会如何变化？具体地，model 主效应和 model×item 交互是否会增大（因为大模型可能 \"solve\" 更多 items）？\n\n**Q2**: Bootstrap CI 的 resampling unit 是什么？如果是 item-level，请确认；如果不是，请解释选择。\n\n**Q3**: 论文报告 Cohen's d 的 CI 为 [11.44, 21.02]——这看起来像是 mean difference 的 CI 而非 d 的 CI。能否澄清？\n\n**Q4**: 对于 D-study projection 中 \"55 items for G ≥ 0.80\"，如果 variance components 的估计有 ±10% 的不确定性，所需 items 数量的范围是多少？\n\n**Q5**: 论文在 cross-benchmark extension (exp-002) 中仅使用 BF16 和 2 个温度。是否有在 exp-001 的 BF16-only subset 上复现 full-design 方差分解结果的验证？\n\n---\n\n## 元信息\n\n- **Reviewer 角色**: 方法严谨性 + 实验设计 + 统计分析\n- **审稿模式**: fresh（首次审稿）\n- **Review form 来源**: AAAI 2027 review form 尚未发布。评分维度基于 AAAI-26 CFP 公开的评估标准（significance/novelty, soundness, relevance, clarity, reproducibility）和 AAAI-26 AI Review Pilot 论文（arXiv:2604.13940）描述的定性维度（Story, Presentation, Evaluations, Correctness, Significance）。\n",
  "reviewer_id": "1",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 审稿意见：Format-Conditional Variance Structure in LLM Evaluation: A Generalizability Theory Approach\n\n**目标会议**: AAAI 2027 Main Technical Track\n**审查侧重**: 方法严谨性 + 实验设计 + 统计分析\n\n---\n\n## 总体评分\n\n**Overall**: 6/10 (Weak Accept — marginally above acceptance threshold)\n\n**一句话总结**: 论文将 G-theory 引入 LLM 评测方差分解，核心发现（format-conditional variance structure）有实际价值且描述性证据充分，但其核心 claim 的形式化统计检验（permutation test, n=5）从根本上不具备充分的统计效力，model facet 的 quasi-random 处理也限制了结论的可推广性。\n\n---\n\n## 官方维度打分\n\n（基于 AAAI-26 CFP 公开评估标准 + AI Review Pilot 定性维度，AAAI 2027 review form 尚未发布）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | Henderson Method I 对 binary data 的 robustness 有四项验证但缺少标准心理测量方法（tetrachoric correlation）对比；permutation test 先天不足（n=5）；部分 claims 缺少 CI |\n| Novelty/Originality | 4/5 | 首次将多 benchmark、多 facet 全交叉 G-theory 设计应用于 LLM 评测，format-conditional 发现新颖；但 G-theory 本身非新方法 |\n| Significance | 3.5/5 | D-study budget 工具有明确实践价值；但 model facet 仅覆盖 7-9B，不能直接指导 API 模型或大规模模型评测 |\n| Clarity | 4/5 | 论文结构清晰，Figure 1-3 直观有效；但 bootstrap resampling unit 未明确说明，部分关键方法细节不足 |\n| Reproducibility | 3/5 | 实验规模大（2.3M records），facet 设计详细；但未提供代码/数据，resampling 细节缺失，FP32 实现 bug（fence.sage mode）的发现表明环境依赖性较强 |\n| Relevance to AAAI | 4/5 | AI 评测方法论是 AAAI 社区关注的问题，实验设计和统计方法有 broad interest |\n| Confidence | 4/5 | 我熟悉 G-theory、心理测量方法和 LLM evaluation 领域 |\n\n---\n\n## Summary\n\n本文将心理测量学中的 Generalizability Theory (G-theory) 应用于 LLM 评测的方差分解。通过 7-facet 全交叉设计（item, model, precision, prompt, temperature, seed, ordering），在 MMLU 上进行了 exp-001 全交叉实验（460,800 records），并通过 exp-002 将方差分解扩展到 5 个 benchmark（2,304,000 records）。核心发现是方差结构具有 format-conditional 特性：multiple-choice benchmark 中 item selection 贡献 34-38% 方差，而 free-form benchmark 中无单一主导来源（各因素贡献 5-24%）。论文还提供了 D-study budget 工具，证明 multi-facet 设计比 single-condition 设计可减少约 10× 的 items 需求。\n\n---\n\n## 主要优势\n\n**S1. 问题定义精准，研究设计系统性强。** 现有 LLM 评测方差研究多为 single-benchmark、single-facet，无法分离交互效应。本文的 7-facet 全交叉设计是该领域迄今最全面的方差分解尝试，实验规模（2.3M records across 5 benchmarks）也体现了充分的工程投入。\n\n**S2. Format-conditional 发现有实际价值。** Table 3 中 MC vs. FF benchmark 的方差结构差异非常显著（item 方差份额：37-54% vs. 2.9-6.4%），这一发现直接启示了不同 benchmark 类型应采用不同的评测优化策略。即使形式化检验力不足，描述性证据本身已足够引人注目。\n\n**S3. D-study budget 工具有明确的实践意义。** Figure 3 的 projection curves 和 55 items vs. 552 items 的对比，为 benchmark 设计者提供了可操作的指导。将 G-theory 从描述性分析推进到设计决策工具，是本文超越纯方法论贡献的亮点。\n\n**S4. Robustness 分析覆盖较广。** 6 项 robustness check（REML 对比、Bootstrap vs. jackknife CI、facet specification、LOMO、null calibration、item resampling）覆盖了主要的方法论关切，尤其是 LOMO 分析（G_item 0.877-0.889）有效地展示了 model composition 的稳定性。\n\n**S5. Precision separability 的实用发现。** BF16 和 FP16 在 binary scoring 下可互换（方差贡献 <0.01%）是有实用价值的结论，能帮助实践者简化评测配置。FP32 fence.sage mode 的发现也是有价值的社区知识。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Permutation test 先天不足：p=0.10 是该设计下可达到的最小 p 值\n\n- 具体位置：Section \"Format-Conditional Variance Structure\"（Page 6，Table 3 下方）\n- 问题：论文用 permutation test 检验 MC vs. FF benchmark 的方差结构差异，报告 p=0.10, n=5。然而，将 5 个 benchmark 分为 3 MC + 2 FF 的所有可能划分只有 C(5,2)=10 种。因此 **p=0.10 = 1/10 是理论上可达到的最小 p 值**，即使完美分离也无法拒绝 H₀ at α=0.05。论文报告 p=0.10 但未说明这一根本限制，读者可能误解为\"接近显著\"而非\"这是检验框架本身能给出的最强证据\"。\n- 为什么影响接收：\"Format-conditional variance structure\" 是论文标题中的核心 claim。如果支持该 claim 的唯一形式化检验在设计上就无法提供强证据，则该 claim 的证据基础不足。\n- 建议修改方向：(a) 在正文中明确说明 p=0.10 是 minimum achievable p-value，解释其含义；(b) 补充额外的 benchmarks 以增强检验力，或 (c) 放弃 permutation test，转而依赖描述性证据（Table 3 的效应量）和理论论证，而非 p-value；(d) 考虑 bootstrap-based test 或 Bayesian 分析作为替代。\n\n**N2** [critical] Model facet 的 quasi-random 处理严重限制了 claims 的可推广性\n\n- 具体位置：Section \"Experimental Design: MMLU\" → \"Models\" 和 Section \"Model-as-Facet Justification\"（Page 3-4）\n- 问题：G-theory 的 random facet 假设要求 facet levels 是从某个定义良好的 universe 中随机抽取的。论文选择了 8 个 7-9B 参数的 instruction-tuned 模型，并称之为\"quasi-random facet\"。但这些模型：(1) 参数量范围极窄（7-9B），不能代表 1B-405B 的全谱系；(2) 全部为 instruction-tuned，排除了 base models；(3) 全部为开源模型，排除了 API models（GPT-4o, Claude, Gemini）。LOMO 检查（G_item 0.877-0.889）仅验证了这 8 个模型内部的稳定性，但无法回答\"如果加入 70B 或 405B 模型，item difficulty profile 是否改变\"这个关键问题。\n- 为什么影响接收：论文的 title 和 abstract 使用了泛化表述\"LLM Evaluation\"而非\"7-9B Open-Weight Model Evaluation\"。如果方差结构随模型规模变化（例如，大模型可能使 item 方差缩小、model×item 交互变化），则核心结论的适用范围需大幅限缩。\n- 建议修改方向：(a) 在 title/abstract 中明确限定适用范围为 7-9B open-weight models；(b) 增加至少 2-3 个不同规模的模型（如 1-3B, 13B, 70B）验证方差结构的 scale-invariance；(c) 如不增加实验，至少在 Discussion 中提供 model scale 可能影响方差结构的理论分析。\n\n**N3** [critical] \"10.0× fewer items\" claim 缺少置信区间\n\n- 具体位置：Section \"Design-Dependent Reproducibility Budgets\"（Page 6-7）及 Conclusion\n- 问题：论文的核心实践 claim \"multi-facet designs require 10.0× fewer items\" 是一个点估计（55 items vs. 552 items），但未报告该比率的任何不确定性度量。论文提到 \"this ratio remains stable across subset sizes from 50 to 200 items (CV = 1.9%)\"，但这是跨 item pool size 的稳定性，不是估计误差的 CI。如果方差分量估计本身有不确定性（显然有），则 D-study 投射出的 item 数量也有不确定性。55 items 的 CI 可能是 [30, 90] 或 [45, 70]——这对实践指导有本质差异。\n- 为什么影响接收：这是论文的核心实用贡献之一。无 CI 的点估计在统计严谨性上不够。\n- 建议修改方向：通过 bootstrap（对 variance components 进行 bootstrap）或 parametric 方法计算 D-study projection 的 CI，并报告 10× ratio 的 CI。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] IRT 对比不公平——优化目标不同\n\n- 具体位置：Section \"IRT and Efficient Benchmarking\"（Page 6）及 Table 4\n- 问题：论文将 IRT-selected 116 items（G=0.457）与 G-theory multi-facet 设计（55 items, G≥0.80）对比，得出 G-theory \"更高效\"的结论。但 IRT 的目标函数是最大化 item information/discrimination（优化 θ 估计精度），而 G-theory 优化的是跨 facet 条件的 generalizability。两者是不同的优化目标。在 IRT 的框架内，这 116 个 items 可能已经是最优的；用 G-theory 的标准评估 IRT 的 item 选择，相当于用田径标准评价游泳成绩。\n- 建议：(a) 明确说明 IRT 和 G-theory 优化不同目标，对比是 illustrative 而非 definitive；(b) 补充一个公平对比：用相同的 116 items，分别报告在 IRT framework 和 G-theory framework 下的 reliability/information。\n\n**W2** [warning] Bootstrap resampling unit 未说明\n\n- 具体位置：Section \"Evaluation Protocol\"（Page 4）\n- 问题：论文报告 \"1,000 bootstrap resamples\" 但未说明 resampling unit 是 item-level、observation-level 还是 block-level。对于方差分量估计，resampling unit 的选择直接影响 CI 的有效性：item-level resampling 保留了 item-level 相关结构，而 observation-level resampling 可能低估 CI 宽度。\n- 建议：在 Method 中明确说明 resampling strategy（推荐 item-level block bootstrap）。\n\n**W3** [warning] Cohen's d=1.73 在 n₁=3, n₂=2 时置信区间极宽\n\n- 具体位置：Section \"Format-Conditional Variance Structure\"（Page 6）\n- 问题：论文报告 Cohen's d=1.73 作为 MC vs. FF 方差结构差异的效应量。但在 n₁=3（MC benchmarks）, n₂=2（FF benchmarks）下，d 的 sampling distribution 极为分散。粗略估计 95% CI 约为 [-0.5, 4.0]，这意味着该效应量的估计精度非常低。同样，论文报告的 CI [11.44, 21.02] 看起来像是均值差的 CI 而非 d 的 CI——如果是 d 的 CI，这也不正确（d 的 CI 应基于 noncentral t distribution）。\n- 建议：(a) 提供 d 的正确 CI（基于 noncentral t）；(b) 明确说明小样本下效应量估计的局限；(c) 考虑不报告 d，而是直接报告描述性的差异幅度。\n\n**W4** [warning] Exp-002 降低 crossing 可能引入 confounding\n\n- 具体位置：Section \"Cross-Benchmark Extension\"（Page 4）\n- 问题：Exp-002 为扩展到 5 个 benchmark，将设计从 3 precisions × 3 temperatures 简化为 BF16 only × 2 temperatures。这意味着 cross-benchmark 比较中，precision 和 temperature 的主效应及交互效应被吸收进了残差项。如果 precision 和 temperature 的交互效应在 MC 和 FF benchmark 上有不同模式（虽然 exp-001 在 MMLU 上显示其贡献小），则 exp-002 的 format-conditional 差异可能部分被这些被混淆的效应放大或掩盖。\n- 建议：在正文中讨论这一 confounding 的可能性，并提供 exp-001 中 BF16-only subset 与 full design 的方差分解对比，以证明简化不影响结论。\n\n**W5** [warning] Binary data 处理缺少与标准心理测量方法的对比\n\n- 具体位置：Section \"Binary Data Assumptions\"（Page 4）\n- 问题：心理测量领域处理 binary/ordinal 数据的标准方法是使用 tetrachoric/polychoric correlation（如 Muthén 1984; Holgado-Tello et al. 2010），而非直接在 0/1 数据上应用为连续数据设计的 ANOVA-based 估计。论文提供了 4 项 robustness check，但没有与 tetrachoric-based G-theory（如 Schroeders & Wilhelm 2011）或 GLMM-based variance decomposition（论文提到 GLMM 作为\"complement\"但未作为 primary analysis）进行系统对比。熟悉心理测量的 reviewer 会期望看到这一对比。\n- 建议：补充 tetrachoric-based decomposition 的结果作为 robustness check，或在 Discussion 中说明不使用该方法的理由。\n\n**W6** [warning] Item resampling 仅 3 个样本覆盖不足\n\n- 具体位置：Section \"Robustness Checks\"（Page 7）\n- 问题：论文从 full MMLU pool 中抽取了 3 个独立 200-item 样本验证方差结构稳定性。3 个样本远不足以刻画 variance components 的 sampling distribution。以 3 个观测估计一个分布的位置和离散度，置信水平极低。\n- 建议：增加到至少 30-50 个 bootstrap item sets，报告 variance components 的分布（中位数、IQR、95% range），以充分量化 item sampling variability。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Accuracy-range stability（Section \"Binary Data Assumptions\"）仅在 mean accuracy 0.6-0.72 范围内验证。对于 accuracy ≈ 0.3（如某些模型在 MATH 上的表现）或 accuracy ≈ 0.9 的情况，binary data 的 floor/ceiling effect 可能更显著。建议说明这一限制。\n\n- **M2**: MATH benchmark 中的 `highest_intermediate_math` subject 显示 item variance 仅 10.4%（接近 free-form pattern），但论文将 MATH 整体归为 free-form。这表明 format-conditional 差异可能更准确地描述为 item format（选择题 vs. 开放式）而非 benchmark category 的差异。建议讨论这一 nuance。\n\n- **M3**: 论文提到 \"quasi-random model facet\" 的 ratio 为 \"(3:6)\"（Page 3），但未解释这个比率的含义。推测是指某种固定/随机比例，但表述不清。\n\n- **M4**: Figure 2 中 HellaSwag 的 bar 看起来与其他 MC benchmark 的 pattern 接近但 item variance 份额（54.3%）异常高，而 Table 3 中 model×item 交互也不同（14.6% vs. MMLU 的 36.0%）。建议在正文中讨论 HellaSwag 的异质性——这可能进一步弱化 \"MC benchmarks share a common variance structure\" 的叙事。\n\n- **M5**: 格式检查——论文使用 AAAI 双栏格式，正文约 7 页（含 Limitations），References 占 1+ 页，Appendix 约半页。符合 AAAI 2027 的 7 页正文限制（假设 Limitations 不计入正文页数上限，需确认 AAAI 2027 的具体政策）。\n\n---\n\n## Questions for Authors\n\n**Q1**: 如果将 model facet 从 8 个 7-9B 模型扩展到包含 70B 模型，你预期方差结构会如何变化？具体地，model 主效应和 model×item 交互是否会增大（因为大模型可能 \"solve\" 更多 items）？\n\n**Q2**: Bootstrap CI 的 resampling unit 是什么？如果是 item-level，请确认；如果不是，请解释选择。\n\n**Q3**: 论文报告 Cohen's d 的 CI 为 [11.44, 21.02]——这看起来像是 mean difference 的 CI 而非 d 的 CI。能否澄清？\n\n**Q4**: 对于 D-study projection 中 \"55 items for G ≥ 0.80\"，如果 variance components 的估计有 ±10% 的不确定性，所需 items 数量的范围是多少？\n\n**Q5**: 论文在 cross-benchmark extension (exp-002) 中仅使用 BF16 和 2 个温度。是否有在 exp-001 的 BF16-only subset 上复现 full-design 方差分解结果的验证？\n\n---\n\n## 元信息\n\n- **Reviewer 角色**: 方法严谨性 + 实验设计 + 统计分析\n- **审稿模式**: fresh（首次审稿）\n- **Review form 来源**: AAAI 2027 review form 尚未发布。评分维度基于 AAAI-26 CFP 公开的评估标准（significance/novelty, soundness, relevance, clarity, reproducibility）和 AAAI-26 AI Review Pilot 论文（arXiv:2604.13940）描述的定性维度（Story, Presentation, Evaluations, Correctness, Significance）。\n",
    "reviewer_id": "1",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 115 · 2026-05-22T03:07:20.988694+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4266
}
```

</details>

---


### Assistant

_source line 116 · 2026-05-22T03:07:39.835545+00:00_

审稿意见已提交给 Review Director。

**审稿要点总结：**

- **总体评分**：6/10 (Weak Accept)
- **3 个 Must-Fix 问题**：
  1. Permutation test (n=5) 的 p=0.10 是理论最小值——该检验从设计上就无法为 format-conditional claim 提供强证据
  2. Model facet 仅覆盖 8 个 7-9B 模型，quasi-random 假设严重限制结论的可推广性
  3. "10× fewer items" 核心 claim 缺少置信区间
- **6 个 Should-Fix 问题**：IRT 对比不公平、bootstrap resampling unit 未说明、Cohen's d 在极小样本下 CI 极宽、exp-002 reduced crossing 的 confounding、缺少 tetrachoric-based 方法对比、item resampling 仅 3 个样本
- **5 个小问题**：accuracy-range 验证范围窄、MATH 内部异质性、notation 不清、HellaSwag 异质性、格式合规

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1"
}
```

</details>

---


## Round 4

## Round 4

16 recorded events


### User

_source line 117 · 2026-05-22T03:09:16.146381+00:00_

[Round 1 审稿请求]:
【交叉分享 — Round 1】

以下是 Reviewer 2 和 Reviewer 3 的完整审稿意见。请逐条回应每个 Must-Fix 和 Should-Fix 问题：
- **[AGREE]** 同意并简要说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

特别关注：你作为方法/统计专家，对 R2 的 novelty 质疑和 R3 的可复现性问题有何看法？

---

## Reviewer 2 审稿意见（5/10 Borderline Reject）

### Must-Fix:
**N1** [critical] "Hidden second-largest source" 的 novelty claim 不成立 — model×item interaction 在 IRT 文献中已被广泛讨论（Pezeshkpour & Hruschka 2024, Zhou et al. AAAI 2026 Oral, Maia Polo et al. 2024, Madaan et al. 2024）。将已知 interaction 称为 "hidden" 缺乏文献支撑。

**N2** [critical] MC/FF 二分法被 HellaSwag anomaly 严重削弱 — HellaSwag 的 model×item=36.0% 超过 item=34.3%，与其他 MC benchmarks 差异显著。3 个 MC 中 1 个反例（33%）对核心框架是致命的。HellaSwag 是 completion-style MC，与 knowledge-style MC 在 item construction 上根本不同。

**N3** [critical] 遗漏直接竞争文献 Madaan et al. (2024, arXiv:2406.10229) "Quantifying Variance in Evaluation Benchmarks" — 覆盖 13 个 benchmarks 和 280+ models，与本文高度重叠。

### Should-Fix:
**W1** Messing (2026) 的可验证性——多平台搜索无法找到该文献，如不存在则 positioning narrative 需完全重构。
**W2** Contribution 2 (Precision Separability) 本质是 negative finding / sanity check，不够 substantial 作为独立贡献。
**W3** D-study calculator 缺乏用户场景验证，无 case study 或与 IRT 的 head-to-head 对比。
**W4** AAAI venue 适配度弱——方法论和引用来源指向 ACL/EMNLP，缺少算法创新。
**W5** 遗漏更多相关工作：Hua et al. (EMNLP 2025)、Variance-Aware LLM Annotation (2026)、LLM Psychometrics systematic review (2025) 等。
**W6** 四项贡献排列和 weight 分配不恰当。

---

## Reviewer 3 审稿意见（5/10 Below Threshold）

### Must-Fix:
**N1** [critical] 缺少 AAAI 强制要求的 Reproducibility Checklist。
**N2** [critical] 8个模型名称和版本未列出——仅提及 Llama 3.1-8B-Instruct，其余 7 个未知。
**N3** [critical] 6个 Prompt Template 内容未公开。

### Should-Fix:
**W1** Appendix Robustness Analyses 过于单薄——5 项各仅一句话，无方法描述、无统计细节。
**W2** G-theory 术语对 AAAI 读者可访问性不足（facet, universe of admissible observations, Henderson Method I 等）。
**W3** 200 items 的 10 个 subject 选择标准不完整。
**W4** Results 数字密度过高。
**W5** Introduction 与 Related Work 内容重叠。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 118 · 2026-05-22T03:10:42.263283+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 119 · 2026-05-22T03:10:42.315064+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 120 · 2026-05-22T03:10:42.716752+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 121 · 2026-05-22T03:10:42.817340+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 122 · 2026-05-22T03:10:58.990622+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/submitted.pdf",
  "project": "nlp_variance_gtheory",
  "pages": "2,3,6,7,8",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/submitted.pdf",
    "project": "nlp_variance_gtheory",
    "pages": "2,3,6,7,8",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 123 · 2026-05-22T03:10:59.642766+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p2.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 537.3}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p3.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 484.6}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p6.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 445.3}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p7.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 475.1}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p8.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 555.4}], \"total_pages\": 9, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-22T03:11:27.969984+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-22T03:11:28.875363+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-22T03:11:28.875865+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 127 · 2026-05-22T03:11:29.079054+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_1/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 128 · 2026-05-22T03:11:29.886642+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1010
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-22T03:11:30.088107+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1009
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-22T03:14:53.370681+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 交叉回应：R2 & R3 审稿意见\n\n---\n\n## 对 Reviewer 2 的逐条回应\n\n### Must-Fix\n\n**[AGREE] R2-N1: \"Hidden second-largest source\" 的 novelty claim 过度**\n\n同意 R2 的核心判断。Model×item interaction 在 IRT 文献中已有充分讨论（Pezeshkpour & Hruschka 2024 讨论了 answer ordering 带来的 item-model differential；Zhou et al. AAAI 2026 Oral 在 IRT 框架下分析了 item difficulty × model 交互）。将这一已知现象称为 \"hidden\" 缺乏支撑。\n\n不过，我要补充一个 nuance：本文的贡献不在于 *发现* model×item interaction，而在于将其置于一个 7-facet 同时分解的框架中 *量化* 其相对占比（高达 36%）。IRT 文献中这种交互通常在 unidimensional 或 bifactor model 中处理，不涉及与 prompt、temperature、precision 等方法论 facets 的同时分解。作者应将 claim 从 \"hidden\" 改为 \"previously unquantified in a multi-facet variance decomposition context\"，并在 Related Work 中明确 acknowledge IRT 文献已识别此 interaction。\n\n**[AGREE] R2-N2: MC/FF 二分法被 HellaSwag anomaly 严重削弱——问题比 R2 指出的更严重**\n\n强烈同意，且作为方法/统计审稿人，我要指出这个问题比 R2 所述的更严重。\n\n根据 Section \"Format-Conditional Variance Structure\"（Page 6）的原文数据，三个 MC benchmarks 的实际情况是：\n\n| Benchmark | item (%) | mod×item (%) | item 是否主导？ |\n|-----------|----------|--------------|----------------|\n| MMLU | 37.0 | 30.7 | 是（差 6.3pp） |\n| ARC-Challenge | 33.7 | 33.7 | **否（完全持平）** |\n| HellaSwag | 34.3 | 36.0 | **否（逆转）** |\n\n论文 Page 6 原文写道：\"For MMLU and ARC-Challenge: item difficulty dominates (37.0% and 33.7%), with model×item second (30.7% and 33.7%)\"——但 ARC 的 item 和 mod×item 均为 33.7%，是 **持平** 而非 \"dominates\"。论文将此描述为 \"item difficulty dominates\" 是不准确的。\n\n因此，\"item selection is the primary reliability lever\" 这一核心叙事在 MC benchmarks 中实际仅对 MMLU 明确成立（1/3）。R2 说 33% 反例（HellaSwag）对框架是致命的——实际上是 66%（ARC 持平 + HellaSwag 逆转）。\n\n**但我也要指出 R2 可能忽略的一个维度**：所有三个 MC benchmarks 的 item + mod×item 合计均 >65%（MMLU: 67.7%, ARC: 67.4%, HellaSwag: 70.3%），而 FF benchmarks 的对应值远低。因此 format-conditional 结论可以 reframe 为 \"item-related variance（含 item 主效应和 model×item 交互）在 MC 中主导，在 FF 中分散\"，而非 \"item selection dominates in MC\"。这需要重构叙事但不毁灭核心贡献。\n\n**[AGREE] R2-N3: 遗漏 Madaan et al. (2024) 是重要缺失**\n\n同意。Madaan et al. (2024, arXiv:2406.10229) \"Quantifying Variance in Evaluation Benchmarks\" 覆盖 13 benchmarks 和 280+ models，与本文在问题定义（evaluation variance decomposition）和部分方法（ANOVA-based decomposition）上高度重叠。未引用直接竞争文献是重大遗漏。\n\n作者需要：(a) 引用并讨论与 Madaan et al. 的区别（G-theory vs. 他们的方法、facet 数量、format-conditional 发现等）；(b) 如果 Madaan et al. 已得出部分相同结论，需调整 novelty claim。\n\n### Should-Fix\n\n**[AGREE] R2-W1: Messing (2026) 可验证性存疑**\n\n这是一个严肃的问题。论文 Page 2 Related Work 和 Page 3 Method 中多次引用 \"Messing (2026)\" 作为 G-theory 在 LLM 评测中的先驱工作，且 Introduction 中用它来定位本文的递增贡献（\"Rather than only attributing variance post hoc, a D-study enables...\"）。如果该文献不可验证，则：(a) 本文的 positioning narrative（\"extending Messing's single-benchmark G-theory to cross-benchmark\"）需完全重构；(b) 可能将本文从 \"incremental extension\" 提升为 \"first application\"，但同时也意味着遗漏了 novelty claim。无论哪种情况，都需要 clarification。\n\n我无法独立验证此引用——在我的审查中未搜索过该文献。R2 报告在多平台搜索未果。**建议 Director 要求作者提供该文献的完整引用信息和访问链接。**\n\n**[REBUT] R2-W2: Precision Separability 作为独立贡献有争议，但并非无价值**\n\nR2 认为这本质上是 negative finding / sanity check。我部分同意其 weight 不足以作为四个列出贡献之一，但反驳其\"无价值\"的判断：\n- 论文 Page 6 指出 BF16/FP16 在 binary scoring 下方差贡献 <0.01%，而 FP32 异常来自 vLLM fence.sage mode 实现 bug。这是有社区价值的实用发现。\n- 然而，它确实更适合放在 Findings 中而非 Contributions 中。建议作者将贡献列表从 4 个缩减到 3 个，将 precision separability 移入实验结果部分。\n\n**[REBUT] R2-W3: D-study calculator 缺乏 case study，但 Figure 3 + Table 4 已提供基本验证**\n\nR2 要求用户场景验证和 IRT head-to-head 对比。Table 4（Page 6）已提供了 multi-facet vs. single-condition vs. IRT 三种设计的 item 需求对比（55 vs. 552 vs. 116 items），且 Figure 3 给出了 projection curves。这不是一个空洞的工具声明。\n\n不过，我在 R1 审稿意见中已指出（R1-W1）IRT 对比不公平——优化目标不同。D-study calculator 的 added value 需要在 *相同优化目标* 下与 IRT 对比才有说服力。所以 R2 的关切方向是对的，但 \"缺乏 case study\" 的表述过于严格。\n\n**[REBUT] R2-W4: AAAI venue 适配度不弱**\n\nR2 认为方法论和引用偏向 ACL/EMNLP，但：\n- Zhou et al. (2026) 用 IRT 分析 LLM benchmark 是 **AAAI 2026 Oral**，这直接证明 AAAI 接受 evaluation methodology 工作。\n- AAAI 评估标准明确包含 \"significance and novelty of contributions... relevance to the AAAI community\"。LLM 评测方法论对 AAAI 社区有 broad relevance。\n- 心理测量方法（G-theory, IRT）引入 AI 评测属于 cross-disciplinary contribution，不应因为方法来源是心理测量就认为不适合 AAAI。\n\n**[AGREE] R2-W5: 遗漏多篇相关工作**\n\n同意需要补充。不过，我无法独立验证 R2 列出的每篇文献（如 \"Variance-Aware LLM Annotation (2026)\", \"LLM Psychometrics systematic review (2025)\"）的具体存在性和相关性。建议 Director 要求作者 verify 这些文献并酌情引用。\n\n**[AGREE] R2-W6: 贡献排列和 weight 分配不当**\n\n同意，与 R2-W2 相关。Precision separability 不应与 format-conditional variance structure 并列为同等 weight 的贡献。\n\n---\n\n## 对 Reviewer 3 的逐条回应\n\n### Must-Fix\n\n**[AGREE] R3-N1: 缺少 Reproducibility Checklist**\n\n同意这是格式合规问题。AAAI 2026 要求 Reproducibility Checklist（在 supplementary materials 中提交），AAAI 2027 大概率会延续该要求。论文当前未包含任何 reproducibility checklist 或 ethics statement。这是一个简单但必要的修复。\n\n**[AGREE] R3-N2: 8 个模型名称和版本未列出——这是致命的可复现性缺陷**\n\n强烈同意。论文 Page 3 仅提及 \"eight open-weight 7-9B parameter instruction-tuned models spanning eight architecture families, treated as a quasi-random facet (3:6)\"，在 Page 4 single-model baseline 中提到 \"Llama-3.1-8B-Instruct\"。其余 7 个模型完全未披露。\n\n从方法论角度补充：model facet 是本文 variance decomposition 的核心。如果模型选择有偏（例如偏向某个架构族、或包含了性能异常接近的模型对），则方差分量估计会受影响。不列出模型名称，reviewer 和读者无法评估 model sampling 的质量——这直接影响了我在 R1-N2 中提出的 model facet quasi-random 处理的评估。\n\n**这是我认为最严重的可复现性问题。**\n\n**[AGREE] R3-N3: 6 个 Prompt Template 内容未公开**\n\n同意。论文 Page 3 提到 \"6 prompts\" 作为 prompt facet 的 levels，但未提供任何 prompt 内容。prompt 是被分解的 facet 之一，其具体内容直接影响 prompt main effect 和 prompt×item interaction 的估计。不公开 prompt 内容等于不公开实验的核心输入变量。\n\n### Should-Fix\n\n**[AGREE] R3-W1: Appendix Robustness Analyses 过于单薄**\n\n强烈同意。Page 9 Appendix 的 5 项 robustness 分析每项仅 1-2 句话（例如 \"REML and Henderson Method I differ by <0.5 percentage points on all components\"），无方法描述、无统计细节、无置信区间。\n\n从统计角度看，这些 robustness check 是本文应对二值数据批评（如我在 R1-W5 提出的 tetrachoric 对比缺失）和模型选择批评的关键防线。将它们压缩到不可评估的程度反而削弱了论文的防御力。建议将关键 check（至少 LOMO、estimator robustness、null calibration）扩展为包含方法、结果表格和 CI 的完整段落。\n\n**[AGREE] R3-W2: G-theory 术语可访问性不足**\n\n同意。G-theory 在 AAAI 社区的普及度远低于 ACL/EMNLP 的 psychometrics-aware 读者群。论文应在 Method Section 开头用 1-2 段 tutorial-style 介绍（类似 Shavelson & Webb 1991 的经典描述），帮助 AAAI 读者建立 facet、universe of admissible observations、G coefficient 等概念的直觉。\n\n**[AGREE] R3-W3: 200 items 的 10 个 subject 选择标准不完整**\n\n同意。Page 3 说 \"200 MMLU questions stratified across 10 subjects, 20 per subject\" 但未解释为什么选这 10 个 subjects（MMLU 有 57 个 subjects）。选择标准会影响 item 方差的估计——如果选了难度差异大的 subjects，item 方差会被人为放大。\n\n**[REBUT] R3-W4: Results 数字密度虽高但可接受**\n\nR3 认为数字密度过高影响可读性。我认为 quantitative results 需要 quantitative reporting——方差分解论文的核心 value 就在精确数字上。Table 2 和 Table 3 的结构化展示已经比纯文本数字更易消化。Figure 2 的 stacked bar chart 也提供了 visual summary。\n\n不过，可以考虑在正文中减少重复 Table 中已有的数字，用 qualitative summary + \"see Table X\" 替代。\n\n**[AGREE] R3-W5: Introduction 与 Related Work 内容重叠**\n\n同意但优先级低。这是 presentation polish 问题。\n\n---\n\n## 作为方法/统计专家的综合评价\n\n### 对 R2 novelty 质疑的看法\n\nR2 的 novelty 质疑在三个层面有效：\n\n1. **\"Hidden\" framing 不成立**（R2-N1）：model×item interaction 是已知现象，需重新措辞为 \"quantified in multi-facet context for the first time\"。\n\n2. **MC/FF 二分法比 R2 所述更脆弱**（R2-N2）：结合我的数据核查，3 个 MC benchmarks 中只有 MMLU 呈现 clear item dominance（37.0% vs 30.7%），ARC 是 tied（33.7% vs 33.7%），HellaSwag 是 reversed（34.3% vs 36.0%）。论文需要 reframe 叙事——从 \"item dominates in MC\" 到 \"item-related variance (item + model×item) concentrates differently across formats\"。\n\n3. **遗漏 Madaan et al.**（R2-N3）：如果 Madaan et al. 已用 280+ models 和 13 benchmarks 做了类似分析，本文的 incremental contribution 需要更精确地界定。\n\n但我认为 R2 的整体评分（5/10 Borderline Reject）过于严厉。本文的贡献不仅在于 \"发现\"——multi-facet G-theory 的 *框架本身*（7-facet crossed design + D-study budget）是新的，format-conditional 的 *描述性证据*（即使形式化检验不足）是有价值的。\n\n### 对 R3 可复现性问题的看法\n\nR3 的三个 Must-Fix（reproducibility checklist、model names、prompt templates）全部是 **致命且易修复的问题**。从方法论角度：\n\n- **R3-N2（模型未列出）是三者中最严重的**：model 是 G-theory decomposition 的核心 facet。不公开模型列表，读者无法判断 model sampling 是否合理——而 model facet 的代表性直接影响所有 variance component 估计（尤其是 model main effect 和 model×item interaction）。这不仅是可复现性问题，更是 *方法论 soundness* 问题——因为它使得 R1-N2（model facet quasi-random 处理）和 R2-N2（HellaSwag anomaly）的评估都无法充分进行。\n\n- R3-N3（prompt 未公开）同理：prompt 是一个 facet，其内容影响 prompt×item interaction 的估计。\n\n这些问题都可以在修改中轻松解决（列出模型名称、附上 prompt template），因此不应导致直接 reject，但必须在 camera-ready 之前解决。\n\n### 汇总建议\n\n考虑 R2 和 R3 的意见后，我维持 **6/10 (Weak Accept)** 的评分，但增加以下条件：\n- 上述 Must-Fix 问题（R2-N1/N2/N3 + R3-N1/N2/N3 + 我的 R1-N1/N2/N3）必须全部解决\n- 如果 Messing (2026)（R2-W1）被证实不存在，需要重新评估 novelty positioning\n- 如果 Madaan et al. 的工作已覆盖了本文的主要贡献，可能需要下调评分\n\n核心判断不变：**论文有真正的方法论贡献（multi-facet G-theory framework + D-study budget），但统计证据、novelty framing 和可复现性均需显著改进。**\n",
  "reviewer_id": "1",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 交叉回应：R2 & R3 审稿意见\n\n---\n\n## 对 Reviewer 2 的逐条回应\n\n### Must-Fix\n\n**[AGREE] R2-N1: \"Hidden second-largest source\" 的 novelty claim 过度**\n\n同意 R2 的核心判断。Model×item interaction 在 IRT 文献中已有充分讨论（Pezeshkpour & Hruschka 2024 讨论了 answer ordering 带来的 item-model differential；Zhou et al. AAAI 2026 Oral 在 IRT 框架下分析了 item difficulty × model 交互）。将这一已知现象称为 \"hidden\" 缺乏支撑。\n\n不过，我要补充一个 nuance：本文的贡献不在于 *发现* model×item interaction，而在于将其置于一个 7-facet 同时分解的框架中 *量化* 其相对占比（高达 36%）。IRT 文献中这种交互通常在 unidimensional 或 bifactor model 中处理，不涉及与 prompt、temperature、precision 等方法论 facets 的同时分解。作者应将 claim 从 \"hidden\" 改为 \"previously unquantified in a multi-facet variance decomposition context\"，并在 Related Work 中明确 acknowledge IRT 文献已识别此 interaction。\n\n**[AGREE] R2-N2: MC/FF 二分法被 HellaSwag anomaly 严重削弱——问题比 R2 指出的更严重**\n\n强烈同意，且作为方法/统计审稿人，我要指出这个问题比 R2 所述的更严重。\n\n根据 Section \"Format-Conditional Variance Structure\"（Page 6）的原文数据，三个 MC benchmarks 的实际情况是：\n\n| Benchmark | item (%) | mod×item (%) | item 是否主导？ |\n|-----------|----------|--------------|----------------|\n| MMLU | 37.0 | 30.7 | 是（差 6.3pp） |\n| ARC-Challenge | 33.7 | 33.7 | **否（完全持平）** |\n| HellaSwag | 34.3 | 36.0 | **否（逆转）** |\n\n论文 Page 6 原文写道：\"For MMLU and ARC-Challenge: item difficulty dominates (37.0% and 33.7%), with model×item second (30.7% and 33.7%)\"——但 ARC 的 item 和 mod×item 均为 33.7%，是 **持平** 而非 \"dominates\"。论文将此描述为 \"item difficulty dominates\" 是不准确的。\n\n因此，\"item selection is the primary reliability lever\" 这一核心叙事在 MC benchmarks 中实际仅对 MMLU 明确成立（1/3）。R2 说 33% 反例（HellaSwag）对框架是致命的——实际上是 66%（ARC 持平 + HellaSwag 逆转）。\n\n**但我也要指出 R2 可能忽略的一个维度**：所有三个 MC benchmarks 的 item + mod×item 合计均 >65%（MMLU: 67.7%, ARC: 67.4%, HellaSwag: 70.3%），而 FF benchmarks 的对应值远低。因此 format-conditional 结论可以 reframe 为 \"item-related variance（含 item 主效应和 model×item 交互）在 MC 中主导，在 FF 中分散\"，而非 \"item selection dominates in MC\"。这需要重构叙事但不毁灭核心贡献。\n\n**[AGREE] R2-N3: 遗漏 Madaan et al. (2024) 是重要缺失**\n\n同意。Madaan et al. (2024, arXiv:2406.10229) \"Quantifying Variance in Evaluation Benchmarks\" 覆盖 13 benchmarks 和 280+ models，与本文在问题定义（evaluation variance decomposition）和部分方法（ANOVA-based decomposition）上高度重叠。未引用直接竞争文献是重大遗漏。\n\n作者需要：(a) 引用并讨论与 Madaan et al. 的区别（G-theory vs. 他们的方法、facet 数量、format-conditional 发现等）；(b) 如果 Madaan et al. 已得出部分相同结论，需调整 novelty claim。\n\n### Should-Fix\n\n**[AGREE] R2-W1: Messing (2026) 可验证性存疑**\n\n这是一个严肃的问题。论文 Page 2 Related Work 和 Page 3 Method 中多次引用 \"Messing (2026)\" 作为 G-theory 在 LLM 评测中的先驱工作，且 Introduction 中用它来定位本文的递增贡献（\"Rather than only attributing variance post hoc, a D-study enables...\"）。如果该文献不可验证，则：(a) 本文的 positioning narrative（\"extending Messing's single-benchmark G-theory to cross-benchmark\"）需完全重构；(b) 可能将本文从 \"incremental extension\" 提升为 \"first application\"，但同时也意味着遗漏了 novelty claim。无论哪种情况，都需要 clarification。\n\n我无法独立验证此引用——在我的审查中未搜索过该文献。R2 报告在多平台搜索未果。**建议 Director 要求作者提供该文献的完整引用信息和访问链接。**\n\n**[REBUT] R2-W2: Precision Separability 作为独立贡献有争议，但并非无价值**\n\nR2 认为这本质上是 negative finding / sanity check。我部分同意其 weight 不足以作为四个列出贡献之一，但反驳其\"无价值\"的判断：\n- 论文 Page 6 指出 BF16/FP16 在 binary scoring 下方差贡献 <0.01%，而 FP32 异常来自 vLLM fence.sage mode 实现 bug。这是有社区价值的实用发现。\n- 然而，它确实更适合放在 Findings 中而非 Contributions 中。建议作者将贡献列表从 4 个缩减到 3 个，将 precision separability 移入实验结果部分。\n\n**[REBUT] R2-W3: D-study calculator 缺乏 case study，但 Figure 3 + Table 4 已提供基本验证**\n\nR2 要求用户场景验证和 IRT head-to-head 对比。Table 4（Page 6）已提供了 multi-facet vs. single-condition vs. IRT 三种设计的 item 需求对比（55 vs. 552 vs. 116 items），且 Figure 3 给出了 projection curves。这不是一个空洞的工具声明。\n\n不过，我在 R1 审稿意见中已指出（R1-W1）IRT 对比不公平——优化目标不同。D-study calculator 的 added value 需要在 *相同优化目标* 下与 IRT 对比才有说服力。所以 R2 的关切方向是对的，但 \"缺乏 case study\" 的表述过于严格。\n\n**[REBUT] R2-W4: AAAI venue 适配度不弱**\n\nR2 认为方法论和引用偏向 ACL/EMNLP，但：\n- Zhou et al. (2026) 用 IRT 分析 LLM benchmark 是 **AAAI 2026 Oral**，这直接证明 AAAI 接受 evaluation methodology 工作。\n- AAAI 评估标准明确包含 \"significance and novelty of contributions... relevance to the AAAI community\"。LLM 评测方法论对 AAAI 社区有 broad relevance。\n- 心理测量方法（G-theory, IRT）引入 AI 评测属于 cross-disciplinary contribution，不应因为方法来源是心理测量就认为不适合 AAAI。\n\n**[AGREE] R2-W5: 遗漏多篇相关工作**\n\n同意需要补充。不过，我无法独立验证 R2 列出的每篇文献（如 \"Variance-Aware LLM Annotation (2026)\", \"LLM Psychometrics systematic review (2025)\"）的具体存在性和相关性。建议 Director 要求作者 verify 这些文献并酌情引用。\n\n**[AGREE] R2-W6: 贡献排列和 weight 分配不当**\n\n同意，与 R2-W2 相关。Precision separability 不应与 format-conditional variance structure 并列为同等 weight 的贡献。\n\n---\n\n## 对 Reviewer 3 的逐条回应\n\n### Must-Fix\n\n**[AGREE] R3-N1: 缺少 Reproducibility Checklist**\n\n同意这是格式合规问题。AAAI 2026 要求 Reproducibility Checklist（在 supplementary materials 中提交），AAAI 2027 大概率会延续该要求。论文当前未包含任何 reproducibility checklist 或 ethics statement。这是一个简单但必要的修复。\n\n**[AGREE] R3-N2: 8 个模型名称和版本未列出——这是致命的可复现性缺陷**\n\n强烈同意。论文 Page 3 仅提及 \"eight open-weight 7-9B parameter instruction-tuned models spanning eight architecture families, treated as a quasi-random facet (3:6)\"，在 Page 4 single-model baseline 中提到 \"Llama-3.1-8B-Instruct\"。其余 7 个模型完全未披露。\n\n从方法论角度补充：model facet 是本文 variance decomposition 的核心。如果模型选择有偏（例如偏向某个架构族、或包含了性能异常接近的模型对），则方差分量估计会受影响。不列出模型名称，reviewer 和读者无法评估 model sampling 的质量——这直接影响了我在 R1-N2 中提出的 model facet quasi-random 处理的评估。\n\n**这是我认为最严重的可复现性问题。**\n\n**[AGREE] R3-N3: 6 个 Prompt Template 内容未公开**\n\n同意。论文 Page 3 提到 \"6 prompts\" 作为 prompt facet 的 levels，但未提供任何 prompt 内容。prompt 是被分解的 facet 之一，其具体内容直接影响 prompt main effect 和 prompt×item interaction 的估计。不公开 prompt 内容等于不公开实验的核心输入变量。\n\n### Should-Fix\n\n**[AGREE] R3-W1: Appendix Robustness Analyses 过于单薄**\n\n强烈同意。Page 9 Appendix 的 5 项 robustness 分析每项仅 1-2 句话（例如 \"REML and Henderson Method I differ by <0.5 percentage points on all components\"），无方法描述、无统计细节、无置信区间。\n\n从统计角度看，这些 robustness check 是本文应对二值数据批评（如我在 R1-W5 提出的 tetrachoric 对比缺失）和模型选择批评的关键防线。将它们压缩到不可评估的程度反而削弱了论文的防御力。建议将关键 check（至少 LOMO、estimator robustness、null calibration）扩展为包含方法、结果表格和 CI 的完整段落。\n\n**[AGREE] R3-W2: G-theory 术语可访问性不足**\n\n同意。G-theory 在 AAAI 社区的普及度远低于 ACL/EMNLP 的 psychometrics-aware 读者群。论文应在 Method Section 开头用 1-2 段 tutorial-style 介绍（类似 Shavelson & Webb 1991 的经典描述），帮助 AAAI 读者建立 facet、universe of admissible observations、G coefficient 等概念的直觉。\n\n**[AGREE] R3-W3: 200 items 的 10 个 subject 选择标准不完整**\n\n同意。Page 3 说 \"200 MMLU questions stratified across 10 subjects, 20 per subject\" 但未解释为什么选这 10 个 subjects（MMLU 有 57 个 subjects）。选择标准会影响 item 方差的估计——如果选了难度差异大的 subjects，item 方差会被人为放大。\n\n**[REBUT] R3-W4: Results 数字密度虽高但可接受**\n\nR3 认为数字密度过高影响可读性。我认为 quantitative results 需要 quantitative reporting——方差分解论文的核心 value 就在精确数字上。Table 2 和 Table 3 的结构化展示已经比纯文本数字更易消化。Figure 2 的 stacked bar chart 也提供了 visual summary。\n\n不过，可以考虑在正文中减少重复 Table 中已有的数字，用 qualitative summary + \"see Table X\" 替代。\n\n**[AGREE] R3-W5: Introduction 与 Related Work 内容重叠**\n\n同意但优先级低。这是 presentation polish 问题。\n\n---\n\n## 作为方法/统计专家的综合评价\n\n### 对 R2 novelty 质疑的看法\n\nR2 的 novelty 质疑在三个层面有效：\n\n1. **\"Hidden\" framing 不成立**（R2-N1）：model×item interaction 是已知现象，需重新措辞为 \"quantified in multi-facet context for the first time\"。\n\n2. **MC/FF 二分法比 R2 所述更脆弱**（R2-N2）：结合我的数据核查，3 个 MC benchmarks 中只有 MMLU 呈现 clear item dominance（37.0% vs 30.7%），ARC 是 tied（33.7% vs 33.7%），HellaSwag 是 reversed（34.3% vs 36.0%）。论文需要 reframe 叙事——从 \"item dominates in MC\" 到 \"item-related variance (item + model×item) concentrates differently across formats\"。\n\n3. **遗漏 Madaan et al.**（R2-N3）：如果 Madaan et al. 已用 280+ models 和 13 benchmarks 做了类似分析，本文的 incremental contribution 需要更精确地界定。\n\n但我认为 R2 的整体评分（5/10 Borderline Reject）过于严厉。本文的贡献不仅在于 \"发现\"——multi-facet G-theory 的 *框架本身*（7-facet crossed design + D-study budget）是新的，format-conditional 的 *描述性证据*（即使形式化检验不足）是有价值的。\n\n### 对 R3 可复现性问题的看法\n\nR3 的三个 Must-Fix（reproducibility checklist、model names、prompt templates）全部是 **致命且易修复的问题**。从方法论角度：\n\n- **R3-N2（模型未列出）是三者中最严重的**：model 是 G-theory decomposition 的核心 facet。不公开模型列表，读者无法判断 model sampling 是否合理——而 model facet 的代表性直接影响所有 variance component 估计（尤其是 model main effect 和 model×item interaction）。这不仅是可复现性问题，更是 *方法论 soundness* 问题——因为它使得 R1-N2（model facet quasi-random 处理）和 R2-N2（HellaSwag anomaly）的评估都无法充分进行。\n\n- R3-N3（prompt 未公开）同理：prompt 是一个 facet，其内容影响 prompt×item interaction 的估计。\n\n这些问题都可以在修改中轻松解决（列出模型名称、附上 prompt template），因此不应导致直接 reject，但必须在 camera-ready 之前解决。\n\n### 汇总建议\n\n考虑 R2 和 R3 的意见后，我维持 **6/10 (Weak Accept)** 的评分，但增加以下条件：\n- 上述 Must-Fix 问题（R2-N1/N2/N3 + R3-N1/N2/N3 + 我的 R1-N1/N2/N3）必须全部解决\n- 如果 Messing (2026)（R2-W1）被证实不存在，需要重新评估 novelty positioning\n- 如果 Madaan et al. 的工作已覆盖了本文的主要贡献，可能需要下调评分\n\n核心判断不变：**论文有真正的方法论贡献（multi-facet G-theory framework + D-study budget），但统计证据、novelty framing 和可复现性均需显著改进。**\n",
    "reviewer_id": "1",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-22T03:14:57.234976+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3864
}
```

</details>

---


### Assistant

_source line 132 · 2026-05-22T03:15:09.393437+00:00_

交叉回应已提交给 Director。

要点总结：
- **R2 的 6 个问题中 AGREE 5 个**，仅 REBUT 了 venue 适配度（W4）和 D-study 验证（W3 部分反驳）
- **R3 的 8 个问题中 AGREE 7 个**，仅 REBUT 了数字密度过高（W4）
- 关键补充发现：R2-N2（HellaSwag anomaly）比 R2 自己指出的更严重——根据论文 Page 6 原文数据，ARC 的 item 和 mod×item 实际上完全持平（均为 33.7%），因此 3 个 MC benchmark 中仅 MMLU 呈现 clear item dominance
- R3-N2（模型未列出）不仅是可复现性问题，更是方法论 soundness 问题——无法评估 model facet 代表性
- 维持 6/10 评分，但附条件

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1"
}
```

</details>

---


## Round 5

## Round 5

64 recorded events


### User

_source line 133 · 2026-05-22T08:00:48.805153+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责审查方法严谨性和实验设计。

## 论文信息
- 标题: Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Analysis
- 目标 Venue: EMNLP 2026（通过 ARR 提交）
- ARR 提交截止: 2026-05-25
- 页数限制: 长文正文 8 页，参考文献不限，Limitations/Ethics 不计入
- 模板要求: ACL 模板（**当前论文使用 AAAI 2026 模板，格式不符**）
- 匿名审稿: Double-blind
- 论文文件: /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex
- PDF: /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/submitted.pdf

## 你的审查侧重

### 1. G-theory 方法论正确性
- Henderson Method I 用于二值数据的理论合理性
- 方差分量估计的无偏性论证是否充分
- G 系数和 D-study 投影的数学推导是否正确
- "item-related variance" 定义（item + model×item）的合理性——将 DIF 归入 item-related 是否有争议
- 交叉设计（crossed design）是否完整，是否存在混淆

### 2. 统计有效性
- 二值数据假设的四项验证（simulation, GLMM, accuracy-range stability, estimator guarantee）是否充分
- Bootstrap CI 的方法选择和实现（item-level resampling）是否正确
- 排列检验（p=0.10, n=5）的统计效力——样本量是否足够支持 "format-associated" 的结论
- Cohen's d=1.73 的解读是否合理
- 准随机 facet（quasi-random model facet）假设的验证是否令人信服

### 3. 实验设计合理性
- 200 items stratified sampling 的代表性
- 8 个 7-9B 模型作为 quasi-random facet 的合理性
- exp-002 精简交叉（reduced crossing）是否引入了系统偏差
- Scale validation（3B-9B）的局限性：是否足够支持 "scale-robust" 结论
- 与 IRT baseline 的比较是否公平

### 4. 结果可复现性
- 实验细节是否足够复现
- vLLM 0.9.2 + enforce_eager 的设置是否影响结论的普适性
- 是否提供了代码和数据

### 5. 格式规范
- 确认模板使用错误（AAAI vs ACL）
- 匿名性检查
- 参考文献格式

请按照 ARR 审稿标准进行严格评审，输出结构化审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Minor Issues → Overall Assessment。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 134 · 2026-05-22T08:00:57.031679+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-22T08:00:57.886092+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 136 · 2026-05-22T08:00:57.936694+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 137 · 2026-05-22T08:00:58.087582+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-22T08:01:02.153270+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 139 · 2026-05-22T08:01:03.060563+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/submitted.pdf",
  "project": "nlp_variance_gtheory",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/submitted.pdf",
    "project": "nlp_variance_gtheory",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-22T08:01:03.512570+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 141 · 2026-05-22T08:01:11.312715+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines and review form criteria:

## Reviewer Guidelines

Reviewers are asked to follow a workflow: (1) read the paper and get the first impression, (2) search for related w
…[truncated 1291 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9159
}
```

</details>

---


### Tool result

_source line 142 · 2026-05-22T08:01:12.465812+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p1.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 444.1}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p2.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 576.2}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p3.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 507.8}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p4.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 474.5}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p5.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 498.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p6.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 472.1}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p7.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 461.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p8.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 468.9}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p9.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 552.7}, {\"page\":
…[truncated 438 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 9405
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-22T08:01:12.466273+00:00_

1	\def\aaaianonymous{true}
2	\documentclass[letterpaper]{article}
3	\ifdefined\aaaianonymous
4	    \usepackage[submission]{aaai2026}
5	\else
6	    \usepackage{aaai2026}
7	\fi
8	\usepackage{times}
9	\usepackage{helvet}
10	\usepackage{courier}
11	\usepackage[hyphens]{url}
12	\usepackage{graphicx}
13	\urlstyle{rm}
14	\def\UrlFont{\rm}
15	\usepackage{natbib}
16	\usepackage{caption}
17	\frenchspacing
18	\setlength{\pdfpagewidth}{8.5in}
19	\setlength{\pdfpageheight}{11in}
20	\usepackage{amsmath,amssymb}
21	\usepackage{booktabs}
22	\usepackage{multirow}
23	\usepackage{xcolor}
24	\graphicspath{{../../figures/paper/}}
25	
26	\pdfinfo{
27	/TemplateVersion (2026.1)
28	}
29	
30	\setcounter{secnumdepth}{0}
31	
32	\ifdefined\aaaianonymous
33	    \title{Reproducibility Budgets for Open-Weight LLM Evaluation:\\A Generalizability Theory Analysis}
34	    \author{Anonymous Submission}
35	    \affiliations{}
36	\else
37	    \title{Reproducibility Budgets for Open-Weight LLM Evaluation:\\A Generalizability Theory Analysis}
38	    \author{Anonymous}
39	    \affiliations{}
40	\fi
41	
42	\begin{document}
43	\maketitle
44	
45	\begin{abstract}
46	\input{abstract}
47	\end{abstract}
48	
49	% === INTRODUCTION ===
50	\input{introduction}
51	
52	% === RELATED WORK ===
53	\input{related_work}
54	
55	% === METHOD ===
56	\input{method}
57	
58	% === EXPERIMENTS ===
59	\input{experiments}
60	
61	% === CONCLUSION ===
62	\input{conclusion}
63	
64	% === LIMITATIONS ===
65	\input{limitations}
66	
67	\bibliography{references}
68	
69	% === APPENDIX ===
70	\input{appendix}
71	
72	\end{document}
73	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 8953
}
```

</details>

---


### Tool call

_source line 144 · 2026-05-22T08:01:19.540975+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their descriptions, and the full rating scales. I need every field a reviewer fills out."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their descriptions, and the full rating scales. I need every field a reviewer fills out."
  }
}
```

</details>

---


### Tool call

_source line 145 · 2026-05-22T08:01:21.104789+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract all reviewer guidelines, including what reviewers should evaluate, how to assess soundness, novelty, clarity, significance, and any specific instructions about scoring."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract all reviewer guidelines, including what reviewers should evaluate, how to assess soundness, novelty, clarity, significance, and any specific instructions about scoring."
  }
}
```

</details>

---


### Tool call

_source line 146 · 2026-05-22T08:01:21.407147+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 147 · 2026-05-22T08:01:21.908637+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 148 · 2026-05-22T08:01:22.360694+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 149 · 2026-05-22T08:01:22.461670+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 150 · 2026-05-22T08:01:23.466185+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1557
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-22T08:01:23.466969+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-22T08:01:23.517428+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 153 · 2026-05-22T08:01:23.568553+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 154 · 2026-05-22T08:01:24.678141+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1109
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-22T08:01:24.678907+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1161
}
```

</details>

---


### Tool result

_source line 156 · 2026-05-22T08:01:28.038644+00:00_

# ACL Rolling Review Form - Complete Structure

## Core Review Sections

**Paper Summary**
"Describe what this paper is about" to help editors understand the topic and identify misunderstandings.

**Summary of Strengths**
Identify reasons for publication, including "novel and useful methodology, insightful empirical results or theoretical analysis, clear organization."

**Summary of Weaknesses**
Numbered concerns addressing "correctness of the results or argumentation, limited perceived impact" and clarity issues.

**Comments/Suggestions/Typos**
Space for improvement recommendations beyond main concerns.

## Scoring Dimensions

**Reviewer Confidence** (1-5 scale)
- 5: Positive evaluation; careful reading with related work familiarity
- 4: Quite sure; important points checked carefully
- 3: Pretty sure; general area knowledge but incomplete detail verification
- 2: Defensible but likely missed details or novelty assessment
- 1: Outside expertise or incomprehensible paper

**Soundness** (1-5 with half-point increments)
Evaluates technical rigor, experimental validity, and claim support. Range: "Excellent: one of most thorough" (5) to "Major Issues: not sufficiently thorough" (1).

**Excitement** (1-5 with half-point increments)
Subjective assessment of innovation, impact potential, and community relevance, from "Highly Exciting" (5) to "Not Exciting" (1).

**Overall Assessment** (1-5 with half-point increments)
Publication recommendation: Award consideration (5), Conference acceptance (4), Findings acceptance (3), Resubmit next cycle (2), or Reject (1).

## Additional Evaluation Areas

**Best Paper Justification**
Required for Award or Borderline Award ratings.

**Limitations and Societal Impact**
Assessment of author discussion regarding exclusion, bias, fairness, and dual-use concerns.

**Ethical Concerns**
Review against ACL ethics code and submitted checklist.

**Needs Ethics Review**
Recommendation for specialized ethics committee consideration.

**Reproducibilit
…[truncated 424 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8497
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-22T08:01:28.339961+00:00_

# ARR Reviewer Guidelines: Comprehensive Summary

## Core Evaluation Framework

Reviewers assess papers using three primary scores:

1. **Soundness**: Technical validity and correctness. "The soundness scores must be justified by the text of the review." Low scores require explicit justification in your written comments.

2. **Excitement**: Personal interest level, kept separate from soundness. Reflects subjective preferences rather than paper quality.

3. **Overall Recommendation**: Composite assessment combining soundness, excitement, novelty, and potential impact for conference acceptance.

## Key Assessment Areas

### Clarity & Specificity
Reviews must be concrete: instead of "X is not clear," explain "Y and Z are missing from X's description." Vague criticism without supporting evidence is inadequate.

### Soundness Validation
Papers should demonstrate "sufficient evidence for the claim that the authors are making." Avoid requiring extra experiments beyond what claims necessitate.

### Common Pitfalls to Avoid
The guidelines identify 17 problematic review patterns (H1-H17), including:
- Dismissing surprising results due to hindsight bias
- Requiring SOTA performance when not claimed
- Rejecting negative results or novel approaches
- Penalizing simplicity in solutions

### NLP-Specific Issues (M, T, R, G codes)
Watch for methodology problems (reproducibility, data quality), artifact sourcing concerns, experimental result issues (statistical significance, scope appropriateness), and general issues (unclear contributions, missing related work).

## Professional Standards

Reviews must maintain "professional and neutral" tone. Write "the review you would like to get yourself" rather than sarcastic or dismissive commentary.

## Engagement Requirements

Reviewers must acknowledge author responses during discussion periods and update assessments when concerns are adequately addressed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7235
}
```

</details>

---


### Tool call

_source line 158 · 2026-05-22T08:01:32.303010+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 159 · 2026-05-22T08:01:32.756507+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 160 · 2026-05-22T08:01:33.713418+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1410
}
```

</details>

---


### Tool result

_source line 161 · 2026-05-22T08:01:33.714796+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool call

_source line 162 · 2026-05-22T08:01:33.715069+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-22T08:01:34.267343+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 164 · 2026-05-22T08:01:34.267809+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 165 · 2026-05-22T08:01:35.125342+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 166 · 2026-05-22T08:01:35.125767+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-22T08:01:36.003964+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 878
}
```

</details>

---


### Tool call

_source line 168 · 2026-05-22T08:01:36.105019+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/submitted.pdf",
  "project": "nlp_variance_gtheory",
  "pages": "11",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/submitted.pdf",
    "project": "nlp_variance_gtheory",
    "pages": "11",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-22T08:01:36.256850+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p11.png\", \"width\": 1275, \"height\": 1650, \"size_kb\": 262.9}], \"total_pages\": 11, \"rendered_pages\": 1, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 170 · 2026-05-22T08:01:42.031021+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_2/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 171 · 2026-05-22T08:01:42.483771+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 172 · 2026-05-22T08:01:42.785140+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-22T08:01:42.835846+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 174 · 2026-05-22T08:01:47.558989+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-22T08:01:48.015594+00:00_

1	Large Language Model (LLM) evaluation results vary across reproductions, but variance sources interact, and their relative importance shifts with the benchmark format. No unified factorial framework exists to decompose these sources simultaneously across benchmarks. We apply Generalizability theory (G-theory) in a crossed design with seven facets across eight open-weight 7--9B parameter models and five benchmarks, totaling 2.3 million evaluation records. Our results suggest a format-associated variance pattern: on multiple-choice benchmarks, item-related variance---item difficulty plus model$\times$item differential item functioning (DIF)---concentrates at 68--72\%, while on free-form benchmarks it disperses to 31--41\%, with no overlap across all five benchmarks. Model$\times$item interaction (up to 36\%) is the second-largest component in cross-model analysis, consistent with prior findings on differential item functioning. Under binary scoring, BF16 and FP16 numerical precisions are functionally interchangeable ($<$0.1\% interaction). Multi-facet designs require 10$\times$ fewer items than single-condition designs to reach a generalizability coefficient of 0.80 (55 versus 552 items), and cross-model projections confirm the ratio exceeds 10$\times$ across all benchmarks, with free-form benchmarks showing nearly double the efficiency gain of multiple-choice benchmarks. Within-family scale validation (3B--9B) confirms item dominance is scale-robust. We release an open-source G-theory pipeline and D-study budget calculator for evaluation design optimization.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 456
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-22T08:01:48.016045+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-22T08:01:48.468423+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Generalizability Theory}
5	\label{sec:gtheory}
6	
7	Generalizability theory (G-theory) treats each measurement as one observation from a universe of admissible conditions defined by the crossed facets of an evaluation design \cite{shavelson1991generalizability, brennan2001generalizability}. The \emph{object of measurement} is the entity whose consistency is of interest. In our setting, test items ($p$) serve as the object of measurement, and the goal is to determine how reliably item-level scores generalize across the methodological conditions under which they are collected.
8	
9	A \emph{G-study} decomposes total observed variance into components $\sigma^2_x$ for each facet $x$ and their interactions. Each component quantifies how much variability that source contributes to the overall measurement. Large interaction components (e.g., $\sigma^2_{pM}$ for item-by-model) indicate that facets do not affect items uniformly but instead create differential difficulty profiles. We estimate variance components via Henderson Method~I, an unbiased ANOVA-based estimator for balanced designs \cite[Ch.~3]{brennan2001generalizability}, with 1,000-resample bootstrap confidence intervals (item-level resampling with replacement, preserving the fully-crossed structure across all other facets) \cite{li2023bootstrap}.
10	
11	A \emph{D-study} projects the generalizability coefficient under hypothetical designs with different numbers of conditions per facet:
12	\begin{equation}
13	G_\text{item} = \frac{\sigma^2_p}{\sigma^2_p + \sigma^2_\text{rel}}
14	\label{eq:gcoeff}
15	\end{equation}
16	where $\sigma^2_\text{rel}$ aggregates all item-by-facet interaction variances, each divided by the number of conditions for the corresponding facets \cite[Ch.~4]{brennan2001generalizability}. This prospective capability distinguishes G-theory from classical ANOVA: rather than only attributing variance post hoc, a D-study enables optimization of ev
…[truncated 11111 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 178 · 2026-05-22T08:01:48.519041+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 179 · 2026-05-22T08:01:49.423000+00:00_

1	\section{Experiments}
2	
3	We apply the G-theory framework from Section~3 to a fully crossed evaluation design spanning multiple models, benchmarks, and methodological facets. All experiments use open-weight 7--9B parameter models evaluated with vLLM~0.9.2 on NVIDIA RTX PRO 6000 GPUs (96GB). Binary correctness (1/0) serves as the primary outcome measure throughout; generation-based scoring avoids the log-likelihood artifacts identified by \citet{hua2025flaw}.
4	
5	\subsection{Single-Model Baseline}
6	
7	We first establish the variance structure within a single model (Llama-3.1-8B-Instruct) on MMLU to isolate methodological facet contributions before introducing cross-model variation.
8	
9	\paragraph{Design.} The G-study crosses six facets: 200 items $\times$ 3 numerical precisions (BF16, FP16, FP32) $\times$ 6 prompt templates $\times$ 6 random seeds $\times$ 3 temperature levels (0.0, 0.3, 0.7) $\times$ 4 answer orderings, yielding 259,200 binary observations. Variance components are estimated via Henderson Method~I with bootstrap confidence intervals (1,000 resamples).
10	
11	\paragraph{Results.} Under binary scoring, item difficulty (\texttt{item\_id}) accounts for 58.4\% of total variance, with the residual term contributing 23.1\%. All main facet effects are negligible ($<$1\% each): precision 0.9\%, prompt template, temperature, seed, and ordering each $<$0.5\%. The interesting structure appears in item-conditional interactions: prompt$\times$item is the largest at 5.5\%, followed by seed$\times$item (4.7\%), precision$\times$item (3.3\%), temperature$\times$item (2.9\%), and ordering$\times$item (0.8\%). This pattern indicates that methodological choices do not shift performance uniformly across items; instead, specific items are differentially sensitive to specific facets---prompt template variation produces the largest item-conditional effect.
12	
13	The resulting generalizability coefficient is $G_\text{item} = 0.936$, indicating that 200 items under mul
…[truncated 14724 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 180 · 2026-05-22T08:01:49.473570+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-22T08:01:49.574442+00:00_

1	\appendix
2	\section{Additional Robustness Analyses}
3	\label{app:robustness}
4	
5	We report six robustness analyses that verify the stability of the variance decomposition under alternative analytical choices.
6	
7	\paragraph{Estimator robustness.} We compare Henderson Method~I with restricted maximum likelihood (REML-EM, 500 iterations, practical convergence $\Delta < 0.003$ percentage points). All variance components differ by $<$0.5 percentage points between estimators. The largest discrepancy occurs on the residual component (0.47pp); all substantive components (item, model$\times$item, model) differ by $<$0.3pp. Henderson Method~I is preferred for our balanced designs because it produces unbiased estimates without distributional assumptions \cite[Ch.~12]{brennan2001generalizability}.
8	
9	\paragraph{CI method comparison.} Bootstrap (1,000 item-level resamples with replacement) and delete-1 jackknife confidence intervals agree closely: width ratios range from 0.96 to 1.04 across all variance components. The agreement indicates that the dependence structure introduced by item-level bootstrap resampling (which creates $\sim$127 unique items per 200-item resample) does not materially distort interval estimates.
10	
11	\paragraph{Facet specification sensitivity.} Treating temperature and ordering as fixed (rather than random) facets changes $G_\text{item}$ by only 0.37 percentage points (all-random: 0.820 vs.\ fixed temperature+ordering: 0.824). The small difference reflects the negligible temperature$\times$item (0.65\%) and ordering$\times$item (0.54\%) variance shares. The random-facet assumption is therefore robust to facet classification.
12	
13	\paragraph{Leave-one-model-out (LOMO).} All eight seven-model subsets preserve the item + model$\times$item dominance pattern: item\_id ranges from 36\% to 41\%, and $G_\text{item}$ ranges from 0.877 to 0.889. No single model disproportionately drives the observed variance structure. The consistency of component rank
…[truncated 7459 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-22T08:01:49.574781+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-22T08:01:49.675333+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Our findings are bounded by three scope constraints. First, the primary cross-model analysis covers eight open-weight 7--9B parameter instruction-tuned models; within-family scale validation extends to 3B--9B (Qwen2.5), but results do not generalize to API-based models (where infrastructure is opaque), base (non-instruction-tuned) models, models above 9B parameters, or domain-adapted fine-tuned variants. Extending this validation to larger scales (e.g., 70B+) remains for future work; larger models with higher accuracy could exhibit compressed item variance due to ceiling effects. Second, all experiments run on single-GPU inference (NVIDIA RTX PRO 6000); multi-GPU tensor parallelism introduces additional numerical non-associativity that our design does not capture. Third, the benchmark sample covers three multiple-choice and two free-form tasks; other evaluation formats such as code generation, long-form text production, and multi-turn dialogue may exhibit different variance structures.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-22T08:01:54.546484+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-22T08:01:55.099076+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	On multiple-choice benchmarks, item selection drives 34--38\% of evaluation variance while prompt wording is negligible ($<$3\%). On the free-form reasoning task GSM8K, the structure shifts: model$\times$prompt interaction alone accounts for approximately 9\%, while item selection drops to 17\%. These numbers, drawn from our factorial analysis of 2.3 million evaluation records across five benchmarks, reveal that the variance structure of LLM evaluation is not a fixed property of the pipeline but shifts qualitatively with the response format. Current evaluation practice treats variance sources as independent nuisance factors and controls them one at a time: one study perturbs prompts, another varies precision, a third changes item subsets. This piecemeal approach cannot capture interactions between sources, nor can it predict how the relative importance of each source changes across evaluation settings. Leaderboard rankings built on single-condition evaluations are therefore sensitive to methodological choices that remain unreported and uncontrolled \citep{rodriguez2021leaderboards, dehghani2021benchmark}. No unified factorial framework exists to decompose these sources simultaneously, quantify their interactions, and compare the resulting variance structure across benchmarks.
5	
6	Existing studies have examined individual variance sources in isolation, each implicitly assuming separability. \citet{sclar2024formatting} documented up to 76\% accuracy swings from prompt formatting perturbations but held hardware and item selection fixed. BrittleBench \citep{brittlebench2026} found 50\% variance from prompt perturbation under the same constraint. \citet{yuan2025layercast} showed that numerical precision and GPU type cause up to 9\% accuracy variation but provided no factorial attribution to specific sources or their interactions. \citet{messing2026hidden} applied Generalizability theory (G-theory) to LLM evaluatio
…[truncated 5027 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-22T08:01:55.099441+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 187 · 2026-05-22T08:01:55.551771+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Variance Decomposition in ML/NLP Evaluation.}
5	Factorial decomposition of evaluation variance has roots in the ML reproducibility literature. \citet{bouthillier2021accounting} introduced an ANOVA-based template that decomposes benchmark variance across implementation details, hyperparameters, and data splits, establishing that design choices account for a substantial share of reproducibility failures. Several subsequent studies applied similar decomposition logic to specific facets of model evaluation \citep{dodge2020finetuning, henderson2018deep, magnusson2023reproducibility}. \citet{messing2026hidden} brought Generalizability theory into LLM evaluation, decomposing variance across five methodology facets on a single benchmark; judge identity dominated at 43.8\%, with prompt$\times$judge interaction at 12.4\%. However, this study used a single benchmark, included no infrastructure facets such as numerical precision, and fixed the judge as an LLM evaluator rather than isolating other sources. \citet{madaan2024quantifying} proposed per-factor variance metrics for LLM evaluation benchmarks but did not cross factors simultaneously. Recently, G-theory has been applied to LLM-based writing assessment \citep{wei2025gtheory} and annotation reliability \citep{varannot2025gtheory}, but these studies address scoring consistency rather than benchmark evaluation variance. \citet{kunievsky2025intent} proposed an alternative decomposition that separates intent uncertainty, articulation variance, and model uncertainty, but this framework does not cross infrastructure and methodology facets in a factorial design. Our work extends these approaches by crossing seven facets across five benchmarks, enabling direct comparison of variance structures across evaluation formats.
6	
7	\paragraph{Infrastructure and Prompt Variance.}
8	A parallel line of work has examined individual variance sources in isolation. On the infrastruc
…[truncated 4550 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-22T08:01:55.552232+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-22T08:01:55.602732+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	This study suggests that the variance structure of LLM evaluation is format-associated. Across three multiple-choice benchmarks, item-related variance---item difficulty plus model$\times$item differential item functioning (DIF)---concentrates at 68--72\%, while on free-form benchmarks (GSM8K, MATH) it disperses to 31--41\%, with no overlap across all five benchmarks. Model$\times$item interaction (up to 36\%) is the second-largest source in cross-model analysis, consistent with DIF patterns identified in IRT research: models differ in which items they find difficult, not in overall ability. Our cross-benchmark D-study framework extends the single-benchmark G-theory approach of \citet{messing2026hidden} to format-associated comparison and actionable design budgets.
5	
6	The format-associated pattern implies distinct optimization strategies. For multiple-choice benchmarks, item pool composition is the primary reliability lever; varying prompts or seeds contributes negligible variance. For free-form benchmarks, model identity and model$\times$prompt interaction matter as much as item selection, and evaluation protocols should systematically vary both. Multi-facet designs are 10$\times$ more efficient than single-condition designs (55 versus 552 items for $G \geq 0.80$). Cross-model projections show that the efficiency gain is itself format-associated: FF benchmarks exhibit $\sim$21$\times$ ratios versus $\sim$12$\times$ for MC, indicating that single-condition evaluation of reasoning tasks incurs nearly double the reliability penalty. BF16 and FP16 are interchangeable under binary scoring on single-GPU inference, which eliminates precision as a required control variable. The released D-study calculator enables practitioners to determine the number of items, models, and conditions needed for a target reliability before data collection.
7	
8	Two extensions are planned. Multi-GPU tensor parallelism will test whether pre
…[truncated 211 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 190 · 2026-05-22T08:02:01.675821+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-22T08:02:01.776662+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-22T08:02:04.336302+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 193 · 2026-05-22T08:02:04.387275+00:00_

1	% references.bib — auto-generated from literature_map.yaml (29 cited papers)
2	% Last synced: 2026-05-21
3	
4	% ====== G-Theory & Evaluation Variance ======
5	
6	@article{messing2026hidden,
7	  title={Hidden Measurement Error in {LLM} Pipelines Distorts Annotation, Evaluation, and Benchmarking},
8	  author={Messing, Solomon},
9	  year={2026},
10	  journal={arXiv preprint arXiv:2604.11581},
11	  url={https://arxiv.org/abs/2604.11581}
12	}
13	
14	@article{wei2025gtheory,
15	  title={Exploring {LLM} Autoscoring Reliability Using Generalizability Theory},
16	  author={Wei, Jiangang and others},
17	  year={2025},
18	  journal={arXiv preprint arXiv:2507.19980},
19	  url={https://arxiv.org/abs/2507.19980}
20	}
21	
22	@article{madaan2024quantifying,
23	  title={Quantifying Variance in Evaluation Benchmarks},
24	  author={Madaan, Lovish and Bhatia, Samarth and Tulio Ribeiro, Marco and Roth, Dan},
25	  year={2024},
26	  journal={arXiv preprint arXiv:2406.10229},
27	  url={https://arxiv.org/abs/2406.10229}
28	}
29	
30	@inproceedings{bouthillier2021accounting,
31	  title={Accounting for Variance in Machine Learning Benchmarks},
32	  author={Bouthillier, Xavier and Delaunay, Pierre and Bronzi, Mirko and Trofimov, Assya and Nichyporuk, Brennan and Szeto, Justin and Sepahvand, Nazanin Mohammadi and Raff, Edward and Madan, Kshitij and Voleti, Vikram and Kahou, Samira Ebrahimi and Michalski, Vincent and Arbel, Tal and Pal, Chris and Varoquaux, Ga{\"e}l and Vincent, Pascal},
33	  booktitle={Proceedings of Machine Learning and Systems (MLSys)},
34	  year={2021},
35	  url={https://arxiv.org/abs/2103.03098}
36	}
37	
38	@book{shavelson1991generalizability,
39	  title={Generalizability Theory: A Primer},
40	  author={Shavelson, Richard J. and Webb, Noreen M.},
41	  year={1991},
42	  publisher={SAGE Publications},
43	  isbn={978-0-8039-3744-4}
44	}
45	
46	@book{brennan2001generalizability,
47	  title={Generalizability Theory},
48	  author={Brennan, Robert L.},
49	  year={2001},
50	  publ
…[truncated 11900 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-22T08:07:12.641667+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见：Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Analysis\n\n### 总体评分\n**Overall**: 3.5 — Borderline Conference\n**一句话总结**: 方法论扎实、实验规模可观的 G-theory 跨基准方差分析研究，但核心 \"format-associated\" claim 的统计检验力不足（permutation test 的 p=0.10 本身就是理论最小值），且 \"item-related variance\" 的打包定义夸大了 item 因素的主导地位，加之使用了错误的会议模板。\n\n### 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | Henderson Method I 的使用基本合理，但 permutation test 统计效力不足、item-related variance 的 bundling 有争议、D-study 缺少总评估成本分析 |\n| Excitement | 3.5/5 | 首次对 LLM 评估做跨基准多 facet G-theory 分析，format-associated pattern 有新意，D-study 工具有实用价值；但 n=5 基准的泛化性有限 |\n| Reproducibility | 4/5 | 实验设置详尽（模型列表、prompt 模板、超参数均已提供），承诺开源工具；但代码仓库尚未可用，原始数据未公开 |\n| Reviewer Confidence | 4/5 | 熟悉 G-theory 和 LLM 评估方法论，仔细检查了核心技术细节 |\n\n---\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 使用 AAAI 2026 模板而非 ACL 模板——desk-reject 风险\n- 具体位置：main.tex 第1-7行，\\usepackage[submission]{aaai2026}\n- 问题：论文目标投稿 EMNLP 2026（通过 ARR），必须使用 ACL 模板。当前使用 AAAI 2026 模板，字体、margin、标题格式均不合规。AAAI 模板的排版密度与 ACL 不同，转换后页数可能超限。\n- 为什么影响接收：ARR 系统对模板有硬性检查，使用错误模板可能在 desk review 阶段直接退回。\n- 建议修改方向：改用 acl2023.sty（或 ARR 当前指定的 ACL 模板），重新编译并验证正文在 8 页以内。\n\n**N2** [critical] \"Format-associated\" 核心 claim 的统计检验力根本不足\n- 具体位置：Section 4.3，permutation test 报告 p=0.10\n- 问题：论文用 3 个 MC 基准 vs 2 个 FF 基准做排列检验，C(5,3)=10 种排列，p=0.10 已经是理论最小 p 值——即使格式效应无穷大，也不可能得到 p<0.10。论文虽提到 \"the theoretical minimum for this sample size\"，但这一根本限制在正文中仅以半句话带过，读者很容易忽略其含义：在当前设计下，format-associated 假说在任何常规显著性水平（p<0.05）下原则上不可检验。\n- 补充问题：Cohen's d=1.73 在 n=5 下的置信区间极宽（估计约 [-0.5, 4.0]），论文未报告 d 的 CI。95% CI [11.44, 21.02] 的构造方法也未说明。\n- 为什么影响接收：这是论文的核心贡献（Contribution 1），统计支撑不足直接影响 soundness。\n- 建议修改方向：(1) 在正文和 abstract 中更显著地对冲此限制；(2) 报告 Cohen's d 的 bootstrap CI；(3) 考虑增加更多基准以增加统计效力；(4) 或将 claim 降级为 \"suggestive pattern that warrants replication with more benchmarks\"。\n\n**N3** [critical] \"Item-related variance\" 的打包定义（σ²_p + σ²_pM）夸大了 item 因素的主导地位\n- 具体位置：Section 3.1（定义），Abstract 和 Introduction（\"68–72%\" 核心数字）\n- 问题：论文将 item main effect（σ²_p）与 model×item 交互（σ²_pM）合并为 \"item-related variance\"，理由是 DIF \"operationally an item-level property\"。但 DIF 本质上是交互效应——它等价地刻画了 model-specific 的 item difficulty profiles。若将 σ²_pM 归入 \"model-related variance\"（σ²_M + σ²_pM），则 MMLU 上 model-related = 33.0%，与 \"item-only\" 的 37.9% 相近。68–72% 的 headline number 严重依赖于这一打包选择。\n- 在 ML 实践中，控制 DIF 需要同时控制 item selection 和 model selection——仅控制 item 无法消除 σ²_pM。\n- 为什么影响接收：这一定义选择驱动了论文的核心叙事（\"item-related variance dominates\"），若读者接受另一种同样合理的分解方式，结论将显著不同。\n- 建议修改方向：(1) 在 Section 3.1 中明确讨论打包 vs 不打包两种视角；(2) 在 Table 3 中同时报告 item-only、model-only、interaction 三列；(3) 调整 abstract/conclusion 措辞。\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 准随机模型 facet 假设的外部效度不足\n- 具体位置：Section 3.6, Appendix (LOMO)\n- 问题：8 个模型均为 7-9B instruction-tuned open-weight 模型，来自相近训练范式。LOMO 只证明内部一致性，未验证外部代表性。\n- 建议：讨论代表性局限，明确结论仅适用于当代 7-9B instruction-tuned 模型。\n\n**W2** [warning] Scale validation 不足以支撑 \"scale-robust\" 结论\n- 具体位置：Section 4.6\n- 问题：仅在 Qwen2.5 一个家族的 3B 和 7B 两个尺度上验证，证据过于薄弱。\n- 建议：将标题改为 \"Preliminary Scale Check\" 并限定措辞。\n\n**W3** [warning] 二值数据模拟的 ρ=0.732 意味着 27% 的方差分量排序被扰乱\n- 具体位置：Section 3.4\n- 问题：论文对这一数字的呈现偏乐观。GLMM（ρ=1.0）只检查分组排序，accuracy-range stability 只检查 item_id。\n- 建议：明确报告 ρ=0.732 的实际含义，补充 GLMM 在 individual component 水平的 ρ。\n\n**W4** [warning] D-study \"10× fewer items\" 缺少总评估成本对比\n- 具体位置：Section 4.5, Table 4\n- 问题：multi-facet 55 items × 1,296 conditions = 71,280 次推理 vs single-condition 552 × 1 = 552 次。总计算成本高出约 129 倍。\"10× fewer items\" 技术正确但实践上易误导。\n- 建议：增加 total inference cost 对比表，讨论固定预算下的 reliability 权衡。\n\n**W5** [warning] MATH 残差方差 43.9% 未讨论\n- 具体位置：Table 3（MATH 列）\n- 问题：近一半方差未被解释，可能来源包括高阶交互、CoT 的固有随机性等。\n- 建议：在 Discussion 或 Limitations 中讨论残差的可能构成。\n\n**W6** [warning] IRT baseline 对比不公平\n- 具体位置：Table 4\n- 问题：同时改变了 item 数量和 evaluation protocol，无法归因。\n- 建议：补充 IRT items under multi-facet 的 G 值以实现公平对比。\n\n---\n\n### 小问题\n- P1: bib 中多处 \"and others\" 应扩展完整作者列表\n- P2: varannot2025gtheory 作者为 Anonymous，应更新\n- P3: exp-002 中 ordering 在非 MMLU 基准上 structurally inert，实际为 5-facet 设计，应明确说明\n- P4: Abstract 中 \"seven facets\" 描述对 exp-002 不够精确\n- P5: Conclusion 中 future work 可移入 Limitations 节省空间\n\n---\n\n### 主要优势\n- S1: 首次跨基准、多 facet 的 G-theory 完整分析，实验规模领先（2.3M records）\n- S2: Generation-based scoring 避免了 log-likelihood 偏差，设计选择有文献支撑\n- S3: 稳健性分析全面（6 项检查），方法论态度认真\n- S4: 二值数据假设的四重验证在同类文献中属较完善\n- S5: D-study budget calculator 有直接实用价值\n- S6: Precision separability 确认性结果对实践有清晰指导",
  "reviewer_id": "1",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见：Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Analysis\n\n### 总体评分\n**Overall**: 3.5 — Borderline Conference\n**一句话总结**: 方法论扎实、实验规模可观的 G-theory 跨基准方差分析研究，但核心 \"format-associated\" claim 的统计检验力不足（permutation test 的 p=0.10 本身就是理论最小值），且 \"item-related variance\" 的打包定义夸大了 item 因素的主导地位，加之使用了错误的会议模板。\n\n### 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | Henderson Method I 的使用基本合理，但 permutation test 统计效力不足、item-related variance 的 bundling 有争议、D-study 缺少总评估成本分析 |\n| Excitement | 3.5/5 | 首次对 LLM 评估做跨基准多 facet G-theory 分析，format-associated pattern 有新意，D-study 工具有实用价值；但 n=5 基准的泛化性有限 |\n| Reproducibility | 4/5 | 实验设置详尽（模型列表、prompt 模板、超参数均已提供），承诺开源工具；但代码仓库尚未可用，原始数据未公开 |\n| Reviewer Confidence | 4/5 | 熟悉 G-theory 和 LLM 评估方法论，仔细检查了核心技术细节 |\n\n---\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 使用 AAAI 2026 模板而非 ACL 模板——desk-reject 风险\n- 具体位置：main.tex 第1-7行，\\usepackage[submission]{aaai2026}\n- 问题：论文目标投稿 EMNLP 2026（通过 ARR），必须使用 ACL 模板。当前使用 AAAI 2026 模板，字体、margin、标题格式均不合规。AAAI 模板的排版密度与 ACL 不同，转换后页数可能超限。\n- 为什么影响接收：ARR 系统对模板有硬性检查，使用错误模板可能在 desk review 阶段直接退回。\n- 建议修改方向：改用 acl2023.sty（或 ARR 当前指定的 ACL 模板），重新编译并验证正文在 8 页以内。\n\n**N2** [critical] \"Format-associated\" 核心 claim 的统计检验力根本不足\n- 具体位置：Section 4.3，permutation test 报告 p=0.10\n- 问题：论文用 3 个 MC 基准 vs 2 个 FF 基准做排列检验，C(5,3)=10 种排列，p=0.10 已经是理论最小 p 值——即使格式效应无穷大，也不可能得到 p<0.10。论文虽提到 \"the theoretical minimum for this sample size\"，但这一根本限制在正文中仅以半句话带过，读者很容易忽略其含义：在当前设计下，format-associated 假说在任何常规显著性水平（p<0.05）下原则上不可检验。\n- 补充问题：Cohen's d=1.73 在 n=5 下的置信区间极宽（估计约 [-0.5, 4.0]），论文未报告 d 的 CI。95% CI [11.44, 21.02] 的构造方法也未说明。\n- 为什么影响接收：这是论文的核心贡献（Contribution 1），统计支撑不足直接影响 soundness。\n- 建议修改方向：(1) 在正文和 abstract 中更显著地对冲此限制；(2) 报告 Cohen's d 的 bootstrap CI；(3) 考虑增加更多基准以增加统计效力；(4) 或将 claim 降级为 \"suggestive pattern that warrants replication with more benchmarks\"。\n\n**N3** [critical] \"Item-related variance\" 的打包定义（σ²_p + σ²_pM）夸大了 item 因素的主导地位\n- 具体位置：Section 3.1（定义），Abstract 和 Introduction（\"68–72%\" 核心数字）\n- 问题：论文将 item main effect（σ²_p）与 model×item 交互（σ²_pM）合并为 \"item-related variance\"，理由是 DIF \"operationally an item-level property\"。但 DIF 本质上是交互效应——它等价地刻画了 model-specific 的 item difficulty profiles。若将 σ²_pM 归入 \"model-related variance\"（σ²_M + σ²_pM），则 MMLU 上 model-related = 33.0%，与 \"item-only\" 的 37.9% 相近。68–72% 的 headline number 严重依赖于这一打包选择。\n- 在 ML 实践中，控制 DIF 需要同时控制 item selection 和 model selection——仅控制 item 无法消除 σ²_pM。\n- 为什么影响接收：这一定义选择驱动了论文的核心叙事（\"item-related variance dominates\"），若读者接受另一种同样合理的分解方式，结论将显著不同。\n- 建议修改方向：(1) 在 Section 3.1 中明确讨论打包 vs 不打包两种视角；(2) 在 Table 3 中同时报告 item-only、model-only、interaction 三列；(3) 调整 abstract/conclusion 措辞。\n\n---\n\n### Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 准随机模型 facet 假设的外部效度不足\n- 具体位置：Section 3.6, Appendix (LOMO)\n- 问题：8 个模型均为 7-9B instruction-tuned open-weight 模型，来自相近训练范式。LOMO 只证明内部一致性，未验证外部代表性。\n- 建议：讨论代表性局限，明确结论仅适用于当代 7-9B instruction-tuned 模型。\n\n**W2** [warning] Scale validation 不足以支撑 \"scale-robust\" 结论\n- 具体位置：Section 4.6\n- 问题：仅在 Qwen2.5 一个家族的 3B 和 7B 两个尺度上验证，证据过于薄弱。\n- 建议：将标题改为 \"Preliminary Scale Check\" 并限定措辞。\n\n**W3** [warning] 二值数据模拟的 ρ=0.732 意味着 27% 的方差分量排序被扰乱\n- 具体位置：Section 3.4\n- 问题：论文对这一数字的呈现偏乐观。GLMM（ρ=1.0）只检查分组排序，accuracy-range stability 只检查 item_id。\n- 建议：明确报告 ρ=0.732 的实际含义，补充 GLMM 在 individual component 水平的 ρ。\n\n**W4** [warning] D-study \"10× fewer items\" 缺少总评估成本对比\n- 具体位置：Section 4.5, Table 4\n- 问题：multi-facet 55 items × 1,296 conditions = 71,280 次推理 vs single-condition 552 × 1 = 552 次。总计算成本高出约 129 倍。\"10× fewer items\" 技术正确但实践上易误导。\n- 建议：增加 total inference cost 对比表，讨论固定预算下的 reliability 权衡。\n\n**W5** [warning] MATH 残差方差 43.9% 未讨论\n- 具体位置：Table 3（MATH 列）\n- 问题：近一半方差未被解释，可能来源包括高阶交互、CoT 的固有随机性等。\n- 建议：在 Discussion 或 Limitations 中讨论残差的可能构成。\n\n**W6** [warning] IRT baseline 对比不公平\n- 具体位置：Table 4\n- 问题：同时改变了 item 数量和 evaluation protocol，无法归因。\n- 建议：补充 IRT items under multi-facet 的 G 值以实现公平对比。\n\n---\n\n### 小问题\n- P1: bib 中多处 \"and others\" 应扩展完整作者列表\n- P2: varannot2025gtheory 作者为 Anonymous，应更新\n- P3: exp-002 中 ordering 在非 MMLU 基准上 structurally inert，实际为 5-facet 设计，应明确说明\n- P4: Abstract 中 \"seven facets\" 描述对 exp-002 不够精确\n- P5: Conclusion 中 future work 可移入 Limitations 节省空间\n\n---\n\n### 主要优势\n- S1: 首次跨基准、多 facet 的 G-theory 完整分析，实验规模领先（2.3M records）\n- S2: Generation-based scoring 避免了 log-likelihood 偏差，设计选择有文献支撑\n- S3: 稳健性分析全面（6 项检查），方法论态度认真\n- S4: 二值数据假设的四重验证在同类文献中属较完善\n- S5: D-study budget calculator 有直接实用价值\n- S6: Precision separability 确认性结果对实践有清晰指导",
    "reviewer_id": "1",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 195 · 2026-05-22T08:07:16.454666+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3812
}
```

</details>

---


### Assistant

_source line 196 · 2026-05-22T08:07:24.186057+00:00_

审稿意见已提交给 Review Director。

总结：给出 **Overall 3.5（Borderline Conference）**。三个 critical 问题：(1) AAAI 模板需换 ACL 模板；(2) format-associated claim 的 permutation test p=0.10 是理论最小值，统计效力根本不足；(3) "item-related variance" 将 model×item DIF 打包进 item，使 68-72% 的 headline number 依赖于可争议的定义选择。六个 warning 涵盖 quasi-random model 外部效度、scale validation 不足、D-study 总成本缺失、IRT 对比不公平等。优势方面，实验规模（2.3M records）、稳健性分析的系统性、以及 D-study 工具的实用价值均值得肯定。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1"
}
```

</details>

---


## Round 6

## Round 6

4 recorded events


### User

_source line 197 · 2026-05-22T08:08:31.840228+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每一条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 审稿意见（Round 1 — 新颖性与论文完整性）

### 总体评分
**Overall**: 3.5 — Borderline Conference

### 官方维度打分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计和 robustness checks 充分，但核心 claim 的统计检验力不足（p=0.10），residual variance 大且未充分讨论 |
| Excitement | 3.0/5 | G-theory 应用于多 benchmark LLM 评估有价值，但 Messing (2026) 已有先例；主要贡献为增量扩展；10× 效率增益和 precision separability 可预期 |
| Reproducibility | 4.0/5 | 设计矩阵完整，声明发布 toolkit，但无代码/数据可用性 URL |
| Reviewer Confidence | 4/5 | 熟悉 G-theory、LLM 评估方差分解、IRT 文献 |

### Must-Fix 问题

**N1** [critical] AAAI 2026 模板 → 应为 ACL 模板
- 位置：main.tex L1-7, `\usepackage[submission]{aaai2026}`
- EMNLP 2026 通过 ARR 提交，必须使用 ACL 模板。当前字体、布局、section numbering 全部不符。Desk reject 级别。

**N2** [critical] "Format-associated variance pattern" 统计支撑不足
- 位置：Section 4.3, experiments.tex L80
- MC vs FF 分组差异 permutation test p=0.10（n=5 的理论最小值），不满足常规显著性水平。Cohen's d=1.73 但仅基于 5 个数据点。该 claim 贯穿 abstract、introduction、全部 contributions、conclusion——是论文核心发现，但统计基础薄弱。
- 建议：增加 2-3 个 benchmark 提高检验力，或将 "format-associated" 从 claim 降级为描述性 "observed pattern"。

**N3** [critical] 多项重要相关工作遗漏
- 位置：Section 2
- 遗漏：(1) ATLAS (2025, ICLR 2026 submission)——自适应测试框架，30-78 items 达到 full-benchmark 精度，直接与 D-study budget claim 竞争；(2) MetaBench (Kipnis et al., ICLR 2025)——6 个 benchmark 压缩至 <3% items，含 ARC/GSM8K/HellaSwag/MMLU；(3) Waldis et al. (2024) "Examining the robustness of LLM evaluation to distributional assumptions of benchmarks"。
- 不讨论 ATLAS 和 MetaBench 让 contribution 定位不完整——本文 multi-facet design 55 items vs ATLAS 30-78 items，优化维度不同（cross-facet reliability vs ability estimation），应阐明。

### Should-Fix 问题

**W1** [warning] Ordering facet 在 4/5 benchmark 上结构性为零
- 声称 "seven facets across five benchmarks"，但 ordering 仅在 MMLU 上有操作定义，其余 4 个 benchmark σ²=0 by construction。Abstract/Introduction 应限定。

**W2** [warning] Residual variance 过大未讨论
- MATH 43.9%, GSM8K 39.9% residual 是最大单一来源。论文未讨论可能来源（decoding path dependency, CoT 随机性, parsing variance）。

**W3** [warning] 10× 效率增益新颖性有限
- Multi-facet 需要更少 items 是 G-theory D-study 的数学性质，非 LLM 特有发现。作为独立 Contribution 2 可能 oversell。

**W4** [warning] Model-as-facet 外部效度受限
- 8 个 7-9B instruction-tuned 模型是 purposive selection，LOMO 和 D-study CV 仅证明 internal consistency。Abstract/conclusion 的 "open-weight LLM evaluation" 暗示更广适用范围。

**W5** [warning] 代码/数据可用性声明缺失
- Contribution 4 提到 release toolkit 但无 URL/匿名链接。

### 小问题
- Table 3 同一列在 MC/FF 上报告不同 variance component（prompt×item vs prompt main），易混淆
- references.bib 中 `varannot2025gtheory` author 为 `{Anonymous}`——可能的 self-citation 问题
- 部分 bib 条目缺 volume/pages
- Conclusion "Two extensions are planned" 暗示工作未完成
- 6 个 prompt templates 的选择无 saturation analysis 证明

### 主要优势
- 2.3M records、7 facets 的 fully crossed design 是该领域最大规模 factorial 实验
- Binary data 处理用 4 种互补方法论证，严格超出同类工作
- D-study budget calculator 有实用价值
- 与 Messing (2026) 的差异化定位清晰（fixing judge, multi-benchmark）
- 6 项 robustness checks 全面

---

请逐条回应上述意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-22T08:10:26.816221+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 交叉回应：对 Reviewer 2 审稿意见的逐条回应\n\n### Must-Fix\n\n**[AGREE] R2-N1: AAAI 模板** — 与 R1-N1 一致，desk-reject 级别，无争议。\n\n**[AGREE] R2-N2: Format-associated 统计支撑不足** — 与 R1-N2 一致，两位 reviewer 独立指出同一核心问题。p=0.10 是理论最小值，该 claim 在常规显著性水平下原则上不可检验。\n\n**[REBUT] R2-N3: 相关工作遗漏（ATLAS/MetaBench/Waldis）** — 应补充引用，但不构成 critical 级别。理由：论文已在 Section 2 引用了同类 benchmark compression 工作（tinyBenchmarks, Perlitz, Zhou 2026），并在 Section 4.5 明确阐述 \"IRT selects informative items, while G-theory determines the conditions needed for a target reliability\" 的正交定位。ATLAS/MetaBench 属同一类方法，论文的定位框架同样适用。但 MetaBench 覆盖本文 4/5 benchmarks，直接对比会强化差异化。**建议降级为 Should-Fix**：补充引用并增加 1-2 句定位说明即可。\n\n### Should-Fix\n\n**[AGREE] R2-W1: Ordering facet 结构性为零** — 与 R1-P3 一致（我原列为 minor），R2 升级合理。Abstract/Intro 的 \"seven facets across five benchmarks\" 确实误导。\n\n**[AGREE] R2-W2: Residual variance 过大** — 与 R1-W5 一致。MATH 43.9% residual 是最大单一来源，需讨论（CoT 路径随机性、parsing variance 等）。\n\n**[REBUT] R2-W3: 10× 效率增益新颖性** — 部分不同意。方向可预期但幅度（10×）和 format-dependence（MC 12× vs FF 21×, Table 5）是 LLM 特有的经验发现。但同意论文缺少 total evaluation cost 分析（55×1,296=71,280 vs 552×1=552 次推理），\"10× fewer items\" 实践含义被高估。建议 Contribution 2 措辞从 \"10× fewer items\" 转向 \"format-dependent efficiency gap\"。\n\n**[AGREE] R2-W4: Model-as-facet 外部效度** — 与 R1-W1 一致。\n\n**[AGREE] R2-W5: 代码/数据可用性** — 同意。\n\n### Minor\n\n**[AGREE]** R2-Minor-1 到 Minor-4 均同意（与 R1 意见重合）。\n\n**[REBUT] R2-Minor-5: Prompt saturation analysis** — 合理关切但有缓解：prompt×item 仅 2.5%（MMLU），bootstrap CI 窄度间接表明稳定，facet specification sensitivity 显示低敏感度。严格 saturation 曲线确实缺失，但列为 minor improvement 即可。\n\n### 关于 Excitement 评分\n\nR2 给 3.0/5，我给 3.5/5。R2 的 \"Messing 2026 已有先例\" 判断过于简化——Messing 研究 LLM-as-judge（judge identity 43.8%）、单基准、无 infrastructure facets，与本文的 generation-based scoring、5 基准、7 facets 有本质区别。Format-associated pattern 即使降级为描述性发现也有概念新颖性。建议 Excitement 上调至 3.0-3.5 区间。\n\n### 两位 Reviewer 的共识问题（建议 Director 重点关注）\n1. **模板错误**（R1-N1 = R2-N1）：必须修复\n2. **p=0.10 统计效力**（R1-N2 = R2-N2）：核心 claim 最大弱点\n3. **Model-as-facet 外部效度**（R1-W1 = R2-W4）：结论适用范围需限定\n4. **Residual variance 未讨论**（R1-W5 = R2-W2）：MATH/GSM8K 近半方差未解释\n\n### 分歧点\n1. **R2-N3 相关工作遗漏**：R2 列 critical，R1 建议降为 Should-Fix\n2. **R2-W3 10× 新颖性**：R2 认为可预期，R1 认为 format-dependent ratio 有经验价值\n3. **Excitement**：R2 给 3.0，R1 给 3.5",
  "reviewer_id": "1",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 交叉回应：对 Reviewer 2 审稿意见的逐条回应\n\n### Must-Fix\n\n**[AGREE] R2-N1: AAAI 模板** — 与 R1-N1 一致，desk-reject 级别，无争议。\n\n**[AGREE] R2-N2: Format-associated 统计支撑不足** — 与 R1-N2 一致，两位 reviewer 独立指出同一核心问题。p=0.10 是理论最小值，该 claim 在常规显著性水平下原则上不可检验。\n\n**[REBUT] R2-N3: 相关工作遗漏（ATLAS/MetaBench/Waldis）** — 应补充引用，但不构成 critical 级别。理由：论文已在 Section 2 引用了同类 benchmark compression 工作（tinyBenchmarks, Perlitz, Zhou 2026），并在 Section 4.5 明确阐述 \"IRT selects informative items, while G-theory determines the conditions needed for a target reliability\" 的正交定位。ATLAS/MetaBench 属同一类方法，论文的定位框架同样适用。但 MetaBench 覆盖本文 4/5 benchmarks，直接对比会强化差异化。**建议降级为 Should-Fix**：补充引用并增加 1-2 句定位说明即可。\n\n### Should-Fix\n\n**[AGREE] R2-W1: Ordering facet 结构性为零** — 与 R1-P3 一致（我原列为 minor），R2 升级合理。Abstract/Intro 的 \"seven facets across five benchmarks\" 确实误导。\n\n**[AGREE] R2-W2: Residual variance 过大** — 与 R1-W5 一致。MATH 43.9% residual 是最大单一来源，需讨论（CoT 路径随机性、parsing variance 等）。\n\n**[REBUT] R2-W3: 10× 效率增益新颖性** — 部分不同意。方向可预期但幅度（10×）和 format-dependence（MC 12× vs FF 21×, Table 5）是 LLM 特有的经验发现。但同意论文缺少 total evaluation cost 分析（55×1,296=71,280 vs 552×1=552 次推理），\"10× fewer items\" 实践含义被高估。建议 Contribution 2 措辞从 \"10× fewer items\" 转向 \"format-dependent efficiency gap\"。\n\n**[AGREE] R2-W4: Model-as-facet 外部效度** — 与 R1-W1 一致。\n\n**[AGREE] R2-W5: 代码/数据可用性** — 同意。\n\n### Minor\n\n**[AGREE]** R2-Minor-1 到 Minor-4 均同意（与 R1 意见重合）。\n\n**[REBUT] R2-Minor-5: Prompt saturation analysis** — 合理关切但有缓解：prompt×item 仅 2.5%（MMLU），bootstrap CI 窄度间接表明稳定，facet specification sensitivity 显示低敏感度。严格 saturation 曲线确实缺失，但列为 minor improvement 即可。\n\n### 关于 Excitement 评分\n\nR2 给 3.0/5，我给 3.5/5。R2 的 \"Messing 2026 已有先例\" 判断过于简化——Messing 研究 LLM-as-judge（judge identity 43.8%）、单基准、无 infrastructure facets，与本文的 generation-based scoring、5 基准、7 facets 有本质区别。Format-associated pattern 即使降级为描述性发现也有概念新颖性。建议 Excitement 上调至 3.0-3.5 区间。\n\n### 两位 Reviewer 的共识问题（建议 Director 重点关注）\n1. **模板错误**（R1-N1 = R2-N1）：必须修复\n2. **p=0.10 统计效力**（R1-N2 = R2-N2）：核心 claim 最大弱点\n3. **Model-as-facet 外部效度**（R1-W1 = R2-W4）：结论适用范围需限定\n4. **Residual variance 未讨论**（R1-W5 = R2-W2）：MATH/GSM8K 近半方差未解释\n\n### 分歧点\n1. **R2-N3 相关工作遗漏**：R2 列 critical，R1 建议降为 Should-Fix\n2. **R2-W3 10× 新颖性**：R2 认为可预期，R1 认为 format-dependent ratio 有经验价值\n3. **Excitement**：R2 给 3.0，R1 给 3.5",
    "reviewer_id": "1",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-22T08:10:30.581014+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3764
}
```

</details>

---


### Assistant

_source line 200 · 2026-05-22T08:10:36.746523+00:00_

交叉回应已提交。总结：

- **7 条 AGREE**：模板错误(N1)、统计效力不足(N2)、ordering facet 误导(W1)、residual 未讨论(W2)、model-as-facet 外部效度(W4)、代码缺失(W5)、多数 minor issues
- **3 条 REBUT**：相关工作遗漏应降级为 Should-Fix 而非 Critical(N3)、10× gain 的 format-dependent ratio 有经验新颖性(W3)、prompt saturation 有缓解因素(Minor-5)
- **Excitement 分歧**：R2 给 3.0 偏低，本文与 Messing 2026 有本质区别，建议上调至 3.0-3.5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1"
}
```

</details>

---


## Round 7

## Round 7

64 recorded events


### User

_source line 201 · 2026-05-22T09:51:00.231130+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。

## 目标 Venue
- **EMNLP 2026** via ACL Rolling Review (ARR)
- 提交截止：2026-05-25
- 正文 ≤8 页（references 无限，Limitations ≤1 页不计入）
- ACL 模板（LaTeX），double-blind
- Overall Assessment 评分标准：5=Consider for Award（~前2.5%），4.5=Borderline Award，4=Conference（主会议可接收），3.5=Borderline Conference，3=Findings，2.5=Borderline Findings，2=Resubmit next cycle，1.5=Resubmit after next cycle，1=Do not resubmit

## 论文路径
- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/submitted.pdf`

## 你的审查侧重

### 1. G-theory 方法论严谨性
- Henderson Method I 用于二值数据的理论依据是否充分？probit simulation (ρ=0.732) 是否足以证明 robustness？
- item-related variance 的 bundling（item + model×item DIF）是否合理？是否存在 inflation 风险？
- 将 8 个 purposively selected models 当作 quasi-random facet 的假设是否站得住脚？LOMO 和 4-model subset 验证是否足够？
- D-study 投影的假设条件是否清晰？

### 2. 实验设计
- 200 items per benchmark 的 stratified sampling 是否有代表性偏差？
- exp-002 的 reduced crossing（BF16 only × 2 temps）相对 exp-001 是否引入混淆？Δ G = 0.0008 的验证是否充分？
- MATH 排除 DeepSeek（7/8 models）对结论的影响？
- Cross-benchmark 比较用 n=5 benchmarks 做 format-associated claim 的统计功效？

### 3. 统计声明
- "no overlap" claim 的严谨性（MC 68-72% vs FF 31-41%）——是否需要更强的 formal test？
- permutation test p=0.10 是否支持 format-associated 结论？论文的 hedging 是否足够？
- 10× efficiency gain 的 robustness（CV=1.9%）——across benchmarks 是否稳定？
- Bootstrap CI 的 item-level resampling 策略在 crossed design 下的合理性

### 4. 二值数据假设
- Section 3.4 的 four-fold 验证（probit sim, Henderson I unbiasedness, GLMM complement, REML comparison）是否 sufficient？
- text-exact-match 下 G 崩溃到 0.007 的 implication 是否讨论充分？

请按 ARR 格式输出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Missing References → Soundness/Presentation/Contribution/Overall/Confidence 评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-22T09:51:09.216722+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-22T09:51:10.068572+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 851
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-22T09:51:10.068901+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-22T09:51:10.169598+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 206 · 2026-05-22T09:51:13.936712+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 207 · 2026-05-22T09:51:15.492607+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/submitted.pdf",
  "project": "nlp_variance_gtheory",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/submitted.pdf",
    "project": "nlp_variance_gtheory",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 208 · 2026-05-22T09:51:15.727368+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-22T09:51:21.154947+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, I found information about ACL Rolling Review 2026 reviewer guidelines and review form criteria:

## Reviewer Guidelines

Reviewers are asked to follow a specific workflow: (1) read the paper and get the first impression, (2) search for related work, and should state in the review if they did not check some major parts, such as proofs, if they feel unqualified to review certain aspects.

Reviewers are provided with a checklist to flag problems that other people may have missed.

ARR has adopted a poli
…[truncated 998 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7218
}
```

</details>

---


### Tool result

_source line 210 · 2026-05-22T09:51:23.217449+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.7}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 537.3}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 564.2}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 544.3}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 475.1}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 518.7}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 465.7}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 467.2}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 567.3}, {\"page\":
…[truncated 438 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7724
}
```

</details>

---


### Tool result

_source line 211 · 2026-05-22T09:51:23.217936+00:00_

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
11	\usepackage{graphicx}
12	\usepackage{amsmath,amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{xcolor}
16	
17	\graphicspath{{../../figures/paper/}}
18	
19	\title{Reproducibility Budgets for Open-Weight LLM Evaluation:\\A Generalizability Theory Analysis}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	\input{abstract}
28	\end{abstract}
29	
30	% === INTRODUCTION ===
31	\input{introduction}
32	
33	% === RELATED WORK ===
34	\input{related_work}
35	
36	% === METHOD ===
37	\input{method}
38	
39	% === EXPERIMENTS ===
40	\input{experiments}
41	
42	% === CONCLUSION ===
43	\input{conclusion}
44	
45	% === LIMITATIONS ===
46	\input{limitations}
47	
48	\bibliography{references}
49	
50	% === APPENDIX ===
51	\input{appendix}
52	
53	\end{document}
54	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 7490
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-22T09:51:31.457596+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form criteria, scoring dimensions, and their scales. Include all fields reviewers must fill in, especially: Overall Assessment scale, Soundness, Excitement/Novelty, Reproducibility, Confidence, and any other rating dimensions with their full scale descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form criteria, scoring dimensions, and their scales. Include all fields reviewers must fill in, especially: Overall Assessment scale, Soundness, Excitement/Novelty, Reproducibility, Confidence, and any other rating dimensions with their full scale descriptions."
  }
}
```

</details>

---


### Tool call

_source line 213 · 2026-05-22T09:51:31.909627+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 214 · 2026-05-22T09:51:32.411304+00:00_

1	Large Language Model (LLM) evaluation results vary across reproductions, but variance sources interact, and their relative importance shifts with the benchmark format. No unified factorial framework exists to decompose these sources simultaneously across benchmarks. We apply Generalizability theory (G-theory) in a crossed design with up to seven facets across eight open-weight 7--9B parameter models and five benchmarks, totaling 2.3 million evaluation records. Our results suggest a format-associated variance pattern: on multiple-choice benchmarks, item-related variance---item difficulty plus model$\times$item differential item functioning (DIF)---concentrates at 68--72\%, while on free-form benchmarks it disperses to 31--41\%, with no overlap across all five benchmarks. Model$\times$item interaction (up to 36\%) is the second-largest component in cross-model analysis, consistent with prior findings on differential item functioning. Under binary scoring, BF16 and FP16 numerical precisions are functionally interchangeable ($<$0.1\% interaction). Multi-facet designs require 10$\times$ fewer items than single-condition designs to reach a generalizability coefficient of 0.80 (55 versus 552 items), and cross-model projections confirm the ratio exceeds 10$\times$ across all benchmarks, with free-form benchmarks showing nearly double the efficiency gain of multiple-choice benchmarks. Within-family scale validation (3B--9B) confirms item dominance is scale-robust. We release an open-source G-theory pipeline and D-study budget calculator for evaluation design optimization.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 215 · 2026-05-22T09:51:32.461965+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 216 · 2026-05-22T09:51:32.864065+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	On multiple-choice benchmarks, item selection drives 34--38\% of evaluation variance while prompt wording is negligible ($<$3\%). On the free-form reasoning task GSM8K, the structure shifts: model$\times$prompt interaction alone accounts for approximately 9\%, while item selection drops to 17\%. These numbers, drawn from our factorial analysis of 2.3 million evaluation records across five benchmarks, reveal that the variance structure of LLM evaluation is not a fixed property of the pipeline but shifts qualitatively with the response format. Current evaluation practice treats variance sources as independent nuisance factors and controls them one at a time: one study perturbs prompts, another varies precision, a third changes item subsets. This piecemeal approach cannot capture interactions between sources, nor can it predict how the relative importance of each source changes across evaluation settings. Leaderboard rankings built on single-condition evaluations are therefore sensitive to methodological choices that remain unreported and uncontrolled \citep{rodriguez2021leaderboards, dehghani2021benchmark}. No unified factorial framework exists to decompose these sources simultaneously, quantify their interactions, and compare the resulting variance structure across benchmarks.
5	
6	Existing studies have examined individual variance sources in isolation, each implicitly assuming separability. \citet{sclar2024formatting} documented up to 76\% accuracy swings from prompt formatting perturbations but held hardware and item selection fixed. BrittleBench \citep{brittlebench2026} found 50\% variance from prompt perturbation under the same constraint. \citet{yuan2025layercast} showed that numerical precision and GPU type cause up to 9\% accuracy variation but provided no factorial attribution to specific sources or their interactions. \citet{messing2026hidden} applied Generalizability theory (G-theory) to LLM evaluatio
…[truncated 4703 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 217 · 2026-05-22T09:51:32.864687+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 218 · 2026-05-22T09:51:33.367344+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Generalizability Theory}
5	\label{sec:gtheory}
6	
7	Generalizability theory (G-theory) treats each measurement as one observation from a universe of admissible conditions defined by the crossed facets of an evaluation design \cite{shavelson1991generalizability, brennan2001generalizability}. The \emph{object of measurement} is the entity whose consistency is of interest. In our setting, test items ($p$) serve as the object of measurement, and the goal is to determine how reliably item-level scores generalize across the methodological conditions under which they are collected.
8	
9	A \emph{G-study} decomposes total observed variance into components $\sigma^2_x$ for each facet $x$ and their interactions. Each component quantifies how much variability that source contributes to the overall measurement. Large interaction components (e.g., $\sigma^2_{pM}$ for item-by-model) indicate that facets do not affect items uniformly but instead create differential difficulty profiles. We estimate variance components via Henderson Method~I, an unbiased ANOVA-based estimator for balanced designs \cite[Ch.~3]{brennan2001generalizability}, with 1,000-resample bootstrap confidence intervals (item-level resampling with replacement, preserving the fully-crossed structure across all other facets) \cite{li2023bootstrap}.
10	
11	A \emph{D-study} projects the generalizability coefficient under hypothetical designs with different numbers of conditions per facet:
12	\begin{equation}
13	G_\text{item} = \frac{\sigma^2_p}{\sigma^2_p + \sigma^2_\text{rel}}
14	\label{eq:gcoeff}
15	\end{equation}
16	where $\sigma^2_\text{rel}$ aggregates all item-by-facet interaction variances, each divided by the number of conditions for the corresponding facets \cite[Ch.~4]{brennan2001generalizability}. This prospective capability distinguishes G-theory from classical ANOVA: rather than only attributing variance post hoc, a D-study enables optimization of ev
…[truncated 8340 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 219 · 2026-05-22T09:51:33.367799+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 220 · 2026-05-22T09:51:34.321360+00:00_

1	\section{Experiments}
2	
3	All experiments use open-weight 7--9B parameter models evaluated with vLLM~0.9.2 on a single NVIDIA RTX PRO 6000 GPU (96GB) with binary correctness scoring.
4	
5	\subsection{Single-Model Baseline}
6	
7	We first establish the variance structure within a single model (Llama-3.1-8B-Instruct) on MMLU to isolate methodological facet contributions before introducing cross-model variation.
8	
9	\paragraph{Design.} The G-study crosses six facets: 200 items $\times$ 3 numerical precisions (BF16, FP16, FP32) $\times$ 6 prompt templates $\times$ 6 random seeds $\times$ 3 temperature levels (0.0, 0.3, 0.7) $\times$ 4 answer orderings, yielding 259,200 binary observations. Variance components are estimated via Henderson Method~I with bootstrap confidence intervals (1,000 resamples).
10	
11	\paragraph{Results.} Under binary scoring, item difficulty (\texttt{item\_id}) accounts for 58.4\% of total variance, with the residual term contributing 23.1\%. All main facet effects are negligible ($<$1\% each): precision 0.9\%, prompt template, temperature, seed, and ordering each $<$0.5\%. The interesting structure appears in item-conditional interactions: prompt$\times$item is the largest at 5.5\%, followed by seed$\times$item (4.7\%), precision$\times$item (3.3\%), temperature$\times$item (2.9\%), and ordering$\times$item (0.8\%). This pattern indicates that methodological choices do not shift performance uniformly across items; instead, specific items are differentially sensitive to specific facets---prompt template variation produces the largest item-conditional effect.
12	
13	The resulting generalizability coefficient is $G_\text{item} = 0.936$, indicating that 200 items under multi-facet conditions produce highly reliable rankings. A D-study projection shows $G \geq 0.80$ is achievable with as few as 55 items in this multi-facet design.
14	
15	For text-exact-match scoring (requiring verbatim string matches), the variance structure shifts dramatically: te
…[truncated 12116 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 221 · 2026-05-22T09:51:34.321735+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 222 · 2026-05-22T09:51:34.773037+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Variance Decomposition in ML/NLP Evaluation.}
5	Factorial decomposition of evaluation variance has roots in the ML reproducibility literature. \citet{bouthillier2021accounting} introduced an ANOVA-based template that decomposes benchmark variance across implementation details, hyperparameters, and data splits, establishing that design choices account for a substantial share of reproducibility failures. Several subsequent studies applied similar decomposition logic to specific facets of model evaluation \citep{dodge2020finetuning, henderson2018deep, magnusson2023reproducibility}. \citet{messing2026hidden} brought Generalizability theory into LLM evaluation, decomposing variance across five methodology facets on a single benchmark; judge identity dominated at 43.8\%, with prompt$\times$judge interaction at 12.4\%. However, this study used a single benchmark, included no infrastructure facets such as numerical precision, and fixed the judge as an LLM evaluator rather than isolating other sources. \citet{madaan2024quantifying} proposed per-factor variance metrics for LLM evaluation benchmarks but did not cross factors simultaneously. Recently, G-theory has been applied to LLM-based writing assessment \citep{wei2025gtheory} and annotation reliability \citep{varannot2025gtheory}, but these studies address scoring consistency rather than benchmark evaluation variance. \citet{kunievsky2025intent} proposed an alternative decomposition that separates intent uncertainty, articulation variance, and model uncertainty, but this framework does not cross infrastructure and methodology facets in a factorial design. Our work extends these approaches by crossing seven facets across five benchmarks, enabling direct comparison of variance structures across evaluation formats.
6	
7	\paragraph{Infrastructure and Prompt Variance.}
8	A parallel line of work examines individual variance sources in isolation. \citet{yuan2025layerc
…[truncated 3170 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 223 · 2026-05-22T09:51:34.773428+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 224 · 2026-05-22T09:51:34.773635+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Our results suggest that the variance structure of LLM evaluation is format-associated: item-related variance (item + model$\times$item DIF) concentrates at 68--72\% on MC benchmarks and disperses to 31--41\% on FF benchmarks, with no overlap. For MC benchmarks, item pool composition is the primary reliability lever; for FF benchmarks, model identity and model$\times$prompt interaction matter equally. Multi-facet designs require 10$\times$ fewer items than single-condition designs ($G \geq 0.80$: 55 vs.\ 552 items), with FF benchmarks showing nearly double the efficiency gain ($\sim$21$\times$ vs.\ $\sim$12$\times$). BF16 and FP16 are interchangeable under binary scoring. The released D-study calculator enables practitioners to determine reproducibility budgets before data collection. Code, data, and the D-study budget calculator will be released upon publication.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 225 · 2026-05-22T09:51:35.274854+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 226 · 2026-05-22T09:51:35.425543+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Our findings are bounded by three scope constraints. First, the primary cross-model analysis covers eight open-weight 7--9B parameter instruction-tuned models; within-family scale validation extends to 3B--9B (Qwen2.5), but results do not generalize to API-based models (where infrastructure is opaque), base (non-instruction-tuned) models, models above 9B parameters, or domain-adapted fine-tuned variants. Extending this validation to larger scales (e.g., 70B+) remains for future work; larger models with higher accuracy could exhibit compressed item variance due to ceiling effects. Second, all experiments run on single-GPU inference (NVIDIA RTX PRO 6000); multi-GPU tensor parallelism introduces additional numerical non-associativity that our design does not capture. Third, the benchmark sample covers three multiple-choice and two free-form tasks ($n = 5$); item-level variance patterns within each benchmark are well-powered, but the format-associated claim rests on a benchmark-level comparison with limited statistical power ($p = 0.10$, permutation test). Other evaluation formats such as code generation, long-form text production, and multi-turn dialogue may exhibit different variance structures. Two natural extensions remain: multi-GPU tensor parallelism (testing precision separability under distributed numerical non-associativity) and fine-tuning variance analysis (quantifying how adaptation reshapes item difficulty profiles).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 227 · 2026-05-22T09:51:35.425853+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 228 · 2026-05-22T09:51:35.476303+00:00_

1	\appendix
2	\section{Additional Robustness Analyses}
3	\label{app:robustness}
4	
5	We report eight robustness analyses that verify the stability of the variance decomposition under alternative analytical choices.
6	
7	\paragraph{GLMM complement.} A generalized linear mixed model (GLMM) with marginal logit link produces variance component rankings that perfectly preserve all seven grouped component orderings ($\rho = 1.0$) relative to Henderson Method~I \cite{jiang2018bayesian, tuerlinckx2006glmm}. This confirms that the linear variance decomposition is robust to the binary outcome distribution.
8	
9	\paragraph{Accuracy-range stability.} The \texttt{item\_id} variance share remains stable across subsets with mean accuracy from 0.62 to 0.72 ($r = -0.048$). This rules out distortion from binary floor or ceiling effects at observed accuracy levels.
10	
11	\paragraph{Estimator robustness.} We compare Henderson Method~I with restricted maximum likelihood (REML-EM, 500 iterations, practical convergence $\Delta < 0.003$ percentage points). All variance components differ by $<$0.5 percentage points between estimators. The largest discrepancy occurs on the residual component (0.47pp); all substantive components (item, model$\times$item, model) differ by $<$0.3pp. Henderson Method~I is preferred for our balanced designs because it produces unbiased estimates without distributional assumptions \cite[Ch.~12]{brennan2001generalizability}.
12	
13	\paragraph{CI method comparison.} Bootstrap (1,000 item-level resamples with replacement) and delete-1 jackknife confidence intervals agree closely: width ratios range from 0.96 to 1.04 across all variance components. The agreement indicates that the dependence structure introduced by item-level bootstrap resampling (which creates $\sim$127 unique items per 200-item resample) does not materially distort interval estimates.
14	
15	\paragraph{Facet specification sensitivity.} Treating temperature and ordering as fixed (rather than random)
…[truncated 8373 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 229 · 2026-05-22T09:51:38.790421+00:00_

# ACL Rolling Review Form: Complete Criteria and Scales

## Primary Rating Dimensions

### Overall Assessment
- **5** = Consider for Award (top 2.5% papers)
- **4.5** = Borderline Award
- **4** = Conference acceptance
- **3.5** = Borderline Conference
- **3** = Findings acceptance
- **2.5** = Borderline Findings
- **2** = Resubmit next cycle
- **1.5** = Resubmit after next cycle
- **1** = Do not resubmit

### Soundness
Evaluates scientific rigor, methodological validity, and adequacy of evidence:
- **5** = Excellent, thorough study
- **4** = Strong, sufficient support with minor gaps acceptable
- **3** = Acceptable, main claims supported adequately
- **2** = Poor, main claims lack sufficient support
- **1** = Major issues, insufficiently thorough

### Excitement
Measures subjective value, innovation, and potential impact:
- **5** = Highly Exciting, recommendable to others
- **4** = Exciting, worth mentioning
- **3** = Interesting, possibly attend presentation
- **2** = Potentially Interesting, limited personal resonance
- **1** = Not Exciting, lacking community relevance

### Reviewer Confidence
Indicates evaluator familiarity and certainty:
- **5** = Very careful reading, familiar with related work
- **4** = Quite sure, checked important points
- **3** = Pretty sure, general knowledge but incomplete detail checking
- **2** = Can defend evaluation but likely missed some aspects
- **1** = Outside expertise area or incomprehensible

### Reproducibility
Assesses sufficiency for replicating results:
- **5** = Easy reproduction
- **4** = Mostly reproducible with minor variations
- **3** = Reproducible with difficulty
- **2** = Hard to reproduce, unavailable data or incomplete details
- **1** = Impossible to reproduce

### Datasets and Software
Both use identical scales for released resources:
- **5** = Enabling, affects research direction choices
- **4** = Useful, recommended for ongoing work
- **3** = Potentially useful for some researchers
- **2** = Documentary value f
…[truncated 521 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 7332
}
```

</details>

---


### Tool call

_source line 230 · 2026-05-22T09:51:53.057918+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/submitted.pdf",
  "project": "nlp_variance_gtheory",
  "pages": "11-12",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/submitted.pdf",
    "project": "nlp_variance_gtheory",
    "pages": "11-12",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 231 · 2026-05-22T09:51:53.311107+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 232 · 2026-05-22T09:51:53.361763+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 512.9}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 332.2}], \"total_pages\": 12, \"rendered_pages\": 2, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 303
}
```

</details>

---


### Tool result

_source line 233 · 2026-05-22T09:51:54.016453+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 705
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-22T09:51:54.067535+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 235 · 2026-05-22T09:51:54.421886+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 236 · 2026-05-22T09:51:55.027410+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool call

_source line 237 · 2026-05-22T09:51:55.027854+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 238 · 2026-05-22T09:51:55.830932+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-22T09:51:56.385191+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1963
}
```

</details>

---


### Tool call

_source line 240 · 2026-05-22T09:51:56.385665+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 241 · 2026-05-22T09:51:56.940765+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1912
}
```

</details>

---


### Tool call

_source line 242 · 2026-05-22T09:51:56.994538+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 243 · 2026-05-22T09:51:57.548082+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 244 · 2026-05-22T09:51:58.201059+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2370
}
```

</details>

---


### Tool result

_source line 245 · 2026-05-22T09:51:59.821739+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3436
}
```

</details>

---


### Tool result

_source line 246 · 2026-05-22T09:52:00.237296+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3242
}
```

</details>

---


### Tool result

_source line 247 · 2026-05-22T09:52:00.490528+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2942
}
```

</details>

---


### Tool call

_source line 248 · 2026-05-22T09:52:05.063568+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-22T09:52:05.869861+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---


### Tool call

_source line 250 · 2026-05-22T09:52:06.021535+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 251 · 2026-05-22T09:52:06.374012+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 252 · 2026-05-22T09:52:06.778373+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 756
}
```

</details>

---


### Tool call

_source line 253 · 2026-05-22T09:52:06.778808+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 254 · 2026-05-22T09:52:07.381436+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1007
}
```

</details>

---


### Tool result

_source line 255 · 2026-05-22T09:52:07.483526+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 704
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-22T09:52:14.906282+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, especially: what dimensions reviewers should rate, what constitutes a good review, what are the scoring criteria for soundness, excitement, reproducibility, overall assessment. Include any specific instructions about how to evaluate methodology, experimental design, and statistical claims."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines, especially: what dimensions reviewers should rate, what constitutes a good review, what are the scoring criteria for soundness, excitement, reproducibility, overall assessment. Include any specific instructions about how to evaluate methodology, experimental design, and statistical claims."
  }
}
```

</details>

---


### Tool result

_source line 257 · 2026-05-22T09:52:23.842664+00:00_

# ARR Reviewer Guidelines: Rating Dimensions and Evaluation Criteria

## Rating Dimensions

ARR reviewers provide **three scores** starting February 2025:

1. **Soundness** - Technical validity and methodological rigor
2. **Excitement** - Personal interest and subjective appeal
3. **Overall Assessment** - Explicit recommendation for acceptance/rejection

## Soundness Evaluation

"The _soundness_ scores must be justified by the text of the review. If you give a low _Soundness_ score without finding any major faults, this means that your review is not a faithful explanation of your recommendation."

Key methodological concerns include:

- **M1. LLM-only evaluation** - Validate automated evaluator reliability in context
- **M2. Reproducibility** - Sufficient detail for replication; code/data availability clearly stated
- **M3. Data quality** - Undisclosed issues with provided datasets
- **M4. Selection justification** - Clear motivation for model/benchmark choices
- **M5. Complete proofs** - All assumptions stated; formal results properly supported

## Excitement vs. Soundness

"Excitement scores reflect our personal taste, and so do not necessarily come with explicit reasons" and are "orthogonal to the assessment of the soundness of the paper."

## Overall Assessment Criteria

This composite score balances multiple factors: "soundness, excitement, and also other factors like novelty and impact. All papers recommended for Findings and main conferences are expected to be sufficiently sound and reproducible."

## Key Review Quality Standards

**Specificity (I1):** Replace vague criticisms with concrete details. "The paper is missing relevant references" becomes "The paper is missing references X, Y, Z."

**Avoiding Common Biases (H1-H17):** Guard against:
- Assuming obvious results lack merit
- Confirmation bias against unexpected findings
- Over-emphasizing SOTA results
- Dismissing negative results, simpler methods, or niche topics

**Experimental Rigor (R-series):**
-
…[truncated 694 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8936
}
```

</details>

---


### Tool call

_source line 258 · 2026-05-22T09:56:52.906427+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 审稿意见 — 方法严谨性 + 实验设计\n\n**论文**: Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Analysis\n**Venue**: EMNLP 2026 via ACL Rolling Review\n\n---\n\n## Paper Summary\n\n本文将 Generalizability theory (G-theory) 应用于 LLM 评测的方差分解，在 8 个开源 7-9B 参数模型和 5 个 benchmark（3 MC + 2 FF）上设计了最多 7 个 facet 的完全交叉实验，共 2.3M 条评测记录。主要发现：(1) item-related variance（item + model×item DIF 的捆绑指标）在 MC benchmark 上集中于 68-72%，在 FF benchmark 上分散至 31-41%，五个 benchmark 无重叠；(2) 多 facet 设计达到 G≥0.80 所需 item 数是单条件设计的 1/10（55 vs 552）；(3) BF16/FP16 在 binary scoring 下功能等价；(4) 发布 D-study 预算计算器。\n\n---\n\n## Summary of Strengths\n\n**S1. 首个大规模多 facet 交叉 G-theory 分析。** 此前研究要么只分解单因素（Sclar et al., 2024; Yuan et al., 2025），要么仅在单个 benchmark 上应用 G-theory（Messing, 2026）。本文同时交叉 7 个 facet、覆盖 5 个 benchmark，实验规模（2.3M 记录）在该领域罕见。设计矩阵（Table 1）清晰地展示了完整的 crossing 结构，Figure 1 的设计图直观有效。\n\n**S2. 极其充分的 robustness 验证。** Appendix A 报告了 8 项独立的鲁棒性分析（GLMM complement、accuracy-range stability、estimator comparison、CI method、facet specification、LOMO、null calibration、reduced crossing validation），主文中还有 3 个独立采样的 CV=3.1% 验证。这种验证深度在同领域论文中极为少见，远超审稿人通常的期望。\n\n**S3. 实用性强的 D-study 贡献。** Table 4 和 Table 5 提供了可直接用于实验设计优化的 item budget 数据，10× efficiency gain 在 cross-model projections 中被 bootstrap CI 确认（所有 benchmark 的 ratio 均 >10×）。D-study calculator 是即时可用的实践工具。\n\n**S4. 与 IRT 方法的正交互补定位。** Section 4.5 中将 IRT-selected 116 items（Zhou et al., 2026）置于单条件 vs 多 facet 条件下对比（G=0.457 vs 0.895），清晰展示了 IRT item selection 和 G-theory protocol optimization 的正交性，避免了与 IRT 文献的虚假对立。\n\n**S5. 论文写作严谨透明。** 通篇使用 \"suggest\"/\"format-associated\" 而非因果性语言；在 Section 4.3 中主动报告 permutation test p=0.10 和 benchmark-level CI 跨零；Limitations 明确承认 n=5 的统计功效限制。\n\n---\n\n## Summary of Weaknesses (numbered)\n\n**N1. [critical] Item-related variance 捆绑指标放大了 \"item 主导\" 叙事**\n\n- **具体位置**: Section 3.1 定义、Abstract、Contribution 1、Section 4.3、Conclusion\n- **问题**: 论文定义 \"item-related variance\" = σ²_p + σ²_pM（item difficulty + model×item DIF），得到 MC 68-72% vs FF 31-41% 的 \"no overlap\" 结论。但 model×item interaction 本质上是双向的——它同时反映 item 和 model 的异质性。从 Table 3 可见，未捆绑的 item_id 单独仅占 MC 34-38% / FF 17-24%，model×item 占 MC 30-36% / FF 15-17%。将 model×item 全部归入 \"item-related\" 使得 item 的表观主导地位翻倍（37.9% → 68.1% on MMLU）。\n- **为什么影响接收**: Abstract 和 Contribution 列表中突出强调 \"68-72% vs 31-41%\" 和 \"no overlap\"，这是论文的 flagship claim。仅阅读 abstract 的读者会严重高估 item 作为 \"primary reliability lever\" 的程度。虽然在 G-theory 教育测量传统中 DIF 归为 item property 有先例（Brennan, 2001, Ch. 4），但 LLM evaluation 场景中 model×item 的含义不同于人类测试中的 person×item——它反映的是 architecture-specific capability profiles，既是 item property 也是 model property。\n- **建议修改方向**: (a) 在 abstract 和 contribution 中同时报告 unbundled 和 bundled 数字（如 \"item difficulty alone: 34-38% MC, 17-24% FF; with model×item DIF: 68-72% vs 31-41%\"）；(b) 在 Section 3.1 讨论 bundling 在 LLM 场景下的具体语义差异；(c) 检验 \"no overlap\" 结论在 unbundled item_id 单独指标上是否同样成立（从 Table 3 看确实成立，但应明确讨论）。\n\n**N2. [critical] Format-associated claim 的统计功效严重不足（n=5 benchmarks, p=0.10）**\n\n- **具体位置**: Section 4.3（permutation test）、Abstract、Contribution 1\n- **问题**: 论文的核心发现——variance structure 是 \"format-associated\"——基于 3 MC vs 2 FF benchmarks 的比较。Permutation test p=0.10（10 exhaustive permutations），benchmark-level CI 跨零 [-1.7, 5.1]。在 n=5 的情况下，即使真实效应很大，统计功效也极低。Cohen's d=1.73 在 item-level 很精确，但 benchmark-level 的推断本质上是 n=5 的观察性比较。\n- **为什么影响接收**: 这是论文 4 个贡献中排名第一的、也是 title 和 abstract 的核心叙事。但如审稿人所见，p=0.10 在常规显著性水平下不显著，且 exhaustive permutation 的分辨率上限就是 p=0.10（1/10）。论文虽然在 Section 4.3 和 Limitations 中承认了这一点，但 abstract 说 \"with no overlap across all five benchmarks\" 时未提及统计功效限制，容易误导读者将 observed pattern 当作 confirmed generalization。\n- **建议修改方向**: (a) Abstract 中应明确标注这是 n=5 的观察性 pattern（如 \"across the five benchmarks studied\"）；(b) 讨论 permutation test 在 n=5 时的 power ceiling——即使真实效应为无穷大，p 最小只能到 0.10；(c) 考虑报告 exact one-sided p 值并讨论 Bayesian 替代分析来补充 frequentist 功效不足的问题；(d) 更明确地将此定位为 \"exploratory finding requiring confirmatory replication\" 而非 established pattern。\n\n**W1. [warning] 8 个 purposively selected models 作为 quasi-random facet 的泛化性有限**\n\n- **具体位置**: Section 3.2, Section 3.4 (model facet validation), Appendix A (LOMO)\n- **问题**: 8 个模型均为 open-weight, instruction-tuned, 7-9B 参数。LOMO 分析和 4-model subset D-study 验证了这 8 个模型之间的内部一致性（LOMO: item_id 36-41%, ΔG ≤ 0.019; 4-model: predicted 0.893 vs observed 0.896），但这只能说明 within-sample stability，不能证明这些模型代表了 \"all admissible models\" 的 universe。API-based models（GPT-4, Claude）、base models、70B+ models、domain-adapted models 均被排除。Scale validation（Section 4.6）仅覆盖 Qwen 3B-9B 单一 family。\n- **建议**: 在 Section 3.4 中更明确地界定 quasi-random facet assumption 的 target universe（如 \"the universe of 7-9B open-weight instruction-tuned models available as of 2025\"），并讨论 larger models 可能因 ceiling effects 改变 variance structure（Limitations 已简略提及，建议更具体量化预期）。\n\n**W2. [warning] Exp-002 reduced crossing 的验证仅基于 MMLU**\n\n- **具体位置**: Section 3.3, Appendix A (Reduced crossing validation)\n- **问题**: Exp-002 将 exp-001 的 3 precisions × 3 temperatures 缩减为 BF16-only × 2 temperatures。验证 ΔG=0.0008 是在 exp-001 的 MMLU 子集上做的。但 exp-002 将此 reduced design 应用到了 ARC、HellaSwag、GSM8K、MATH，这些 benchmark 上没有 full crossing 可供对比验证。特别是 FF benchmarks 的 variance structure 明显不同于 MC（residual 40-44% vs 15-25%），reduced crossing 在 FF 上是否同样 preserving structure 是未验证的假设。\n- **建议**: 明确说明此验证的 transferability assumption，或至少在一个 FF benchmark 上做 sensitivity analysis（如 MATH 的 full crossing 子集）。\n\n**W3. [warning] MATH 排除 DeepSeek（7/8 models）的影响未充分讨论**\n\n- **具体位置**: Section 4.3, Appendix B (footnote on MATH)\n- **问题**: MATH 因 DeepSeek inference 数据不完整（37,400/57,600）而仅用 7 个模型。论文仅在 Table 3 脚注和 Appendix B 简略提及。但 DeepSeek 作为中国主流 LLM 之一，其在 MATH 上的表现可能与其他模型有系统性差异（DeepSeek 系列在数学推理上有特定优化）。排除它可能影响 model×item interaction 的估计，进而影响 FF benchmark 的 item-related variance 比例。\n- **建议**: 报告 DeepSeek 在其他 4 个 benchmark 上的 variance contribution（LOMO 中它是否异常），并讨论其排除对 MATH 结论的可能影响方向。\n\n**W4. [warning] Bootstrap item-level resampling 在 stratified design 下可能产生 representation bias**\n\n- **具体位置**: Section 3.1 (\"1,000-resample bootstrap confidence intervals, item-level resampling with replacement\")\n- **问题**: MMLU 的 200 items 来自 10 个 subjects（每个 20 items），Bootstrap 对 items 做有放回抽样。每次 resample 平均只包含约 127 unique items（200 × (1-1/e)），且不保证每个 subject 都有代表。对于 stratified 设计，标准做法是 stratified bootstrap（在每个 stratum 内分别 resample），否则 CI 可能偏窄或偏宽。\n- **建议**: (a) 报告是否使用 stratified bootstrap；(b) 如果是 unstratified，对比一次 stratified bootstrap 的 CI 宽度。Appendix A 已报告 bootstrap vs jackknife 的宽度比 0.96-1.04，如果 jackknife 是 stratified 的则可作为间接验证。\n\n---\n\n## Questions for Authors\n\n**Q1.** Section 3.1 将 model×item DIF 归入 \"item-related variance\" 并以此为核心叙事。能否提供 unbundled item_id 单独指标下的 format-associated separation 的 permutation test 结果？从 Table 3 看 item_id 在 MC (34-38%) 和 FF (17-24%) 之间也无重叠，是否也做了 formal test？\n\n**Q2.** Probit simulation 的 Spearman ρ=0.732（Section 3.4）意味着 binary vs continuous 下的 variance component rankings 有约 46% 的方差未被保留。能否报告具体哪些 components 的 rank 在 dichotomization 后发生了变化？是否主要影响小的 components（如 seed×item, ordering×item），而大的 components（item, model×item）的 rank 始终一致？\n\n**Q3.** Text-exact-match 下 G 崩溃到 0.007（Section 4.1）是一个重要发现，但讨论较少。这暗示 variance structure 不仅 format-associated，更是 metric-conditional。能否进一步解释为什么 text-exact-match 的 temperature 方差如此巨大（79.7%）？这对使用非 binary scoring metric 的实践者有什么具体指导意义？\n\n**Q4.** D-study 的 cross-model projections（Table 5）使用了 8-model 的 variance components 来投影不同 item 数的 G 值。这些投影假设 variance components 在不同 item 数下稳定。Section 4.7 的 3 个独立 200-item 样本的 CV=3.1% 验证了 200 items 的稳定性，但有无证据表明在 55 items（multi-facet 的 G≥0.80 threshold）时 components 同样稳定？\n\n**Q5.** Section 4.3 报告 MMLU 内 10 个 subject 的 difficulty dispersion 与 item variance share 的 Spearman ρ=0.806 (p=0.005)。high_school_mathematics 的 item variance (10.4%) 低于 GSM8K (16.9%)，论文推断 \"item heterogeneity, not format per se, drives variance allocation\"。但这是基于单个异常 subject 的推断——能否控制 difficulty dispersion 后看 format 是否仍有独立效应？\n\n---\n\n## Missing References\n\n- Mushquash & O'Connor (2006) 和 Jiang & Bayesian G-theory (2018) 在 Related Work 中被提及但仅作为 psychometrics foundations。建议简要讨论 Mushquash & O'Connor 对 binary data 下 G-theory 的具体发现，因为这直接关系到 Section 3.4 的方法选择。\n- Yin et al. (2025, \"From Crowdsourcing to Benchmarking: A Framework for Evaluating LLMs with Human Preferences\") 从 crowdsourcing 角度讨论 LLM evaluation reliability，与本文的 multi-facet reliability 分析有互补关系。\n- Burnell et al. (2023, \"Rethink reporting of evaluation results in AI\") 提出了 evaluation reporting standards，与本文的 reproducibility budgets 贡献直接相关。\n\n---\n\n## Limitations and Societal Impact\n\nLimitations section（约半页，3 个 scope constraints + 2 个 future extensions）覆盖了核心限制，长度适当。建议补充：metric-conditional variance structure（binary vs text-exact-match 的巨大差异）作为第四个 scope constraint，因为所有结论都是 conditional on binary scoring 的。\n\n无明显 ethical concerns。研究对象是公开模型和公开 benchmark。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4/5 | 方法论整体严谨，robustness 验证极为充分（8项附录分析）。主要扣分点：headline claim (format-associated) 的 benchmark-level 统计功效不足 (n=5, p=0.10)；item-related bundling 的语义在 LLM 场景下可被质疑。但论文通篇使用审慎措辞，且主动报告了限制。 |\n| Excitement | 3.5/5 | G-theory 应用于 LLM evaluation 的规模化分析是新颖的（超越 Messing 2026 的单 benchmark 局限），D-study budget calculator 有即时实用价值。但 flagship finding (format-associated pattern) 在 benchmark 水平上 underpowered，限制了结论的影响力。 |\n| Reproducibility | 4/5 | 实验设计详尽（Table 1 完整设计矩阵、Appendix C 模型和 prompt 详情）。vLLM 版本、GPU 型号、所有超参数均明确报告。代码和数据承诺 publication 后发布——如能 camera-ready 时附 anonymous repo link 则更好。唯一扣分点：stratified sampling 的具体实现细节（如非 MMLU benchmark 的 200-item 选择策略）未充分描述。 |\n| Overall Assessment | 3.5 (Borderline Conference) | 方法论贡献扎实（首个大规模多 facet G-theory 分析 + D-study calculator），写作严谨透明。但核心发现 (format-associated variance pattern) 的 benchmark-level evidence 不足（n=5, p=0.10, CI 跨零），且 item-related variance 的 bundling 定义放大了 item 主导叙事。作为 Findings 论文可被接收（Soundness 和 Reproducibility 达标）；若目标是 main conference，需补充 benchmarks 以增强 format claim 的统计支撑。 |\n| Confidence | 4/5 | 本人在实验设计、方差分析和 psychometrics 方法方面有较深背景，仔细阅读了全文和附录，核对了关键统计数据。对 G-theory 的 binary data extensions 不是最深入的专家。 |\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 — Borderline Conference\n\n**一句话总结**: 方法论严谨、robustness 验证充分的大规模 G-theory 分析，但核心 \"format-associated\" claim 在 benchmark 水平上严重 underpowered（n=5, p=0.10），且 item-related variance 的 bundling 操作放大了 item 主导叙事——需要更多 benchmarks 和更透明的 unbundled reporting 才能支撑 main conference 级别的结论。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Item-related variance bundling 放大 item 主导叙事\n- 具体位置：Section 3.1, Abstract, Contribution 1, Conclusion\n- 问题：将 model×item DIF 全部归入 \"item-related\" 使 item 表观贡献翻倍（MMLU: 37.9% → 68.1%）。model×item 在 LLM 场景中同时是 model property（architecture-specific capability profiles）。Abstract 中 \"68-72% vs 31-41%\" 的 flagship claim 依赖此 bundling，未同步报告 unbundled 数字。\n- 为什么影响接收：核心叙事的可信度取决于此定义的合理性。不报告 unbundled 数字 = 信息不对称。\n- 建议：Abstract/Contribution 中并列报告 unbundled 和 bundled 数字；Section 3.1 讨论 bundling 在 LLM vs 教育测量场景中的语义差异。\n\n**N2** [critical] Format-associated claim 的统计支撑不足\n- 具体位置：Section 4.3, Abstract, Contribution 1\n- 问题：n=5 benchmarks, permutation test p=0.10（分辨率上限 = 1/10）, benchmark-level CI 跨零 [-1.7, 5.1]。Abstract \"with no overlap across all five benchmarks\" 未注明统计限制。\n- 为什么影响接收：这是论文排名第一的贡献和 title 的核心内容。读者可能将 observed pattern 误认为 statistically confirmed generalization。\n- 建议：Abstract 明确标注为 n=5 的观察性 pattern；讨论 permutation test 的 power ceiling；考虑 Bayesian 补充分析。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Quasi-random model facet 的 target universe 定义模糊\n- 具体位置：Section 3.2, 3.4\n- 建议：明确界定 target universe 为 \"7-9B open-weight instruction-tuned models\"，讨论 ceiling effects 对 larger models 的预期影响。\n\n**W2** [warning] Reduced crossing 验证仅基于 MMLU，未在 FF benchmark 上验证\n- 具体位置：Section 3.3, Appendix A\n- 建议：至少在一个 FF benchmark 上做 sensitivity check，或明确声明 transferability assumption。\n\n**W3** [warning] MATH 排除 DeepSeek 的影响未讨论\n- 具体位置：Section 4.3, Appendix B\n- 建议：报告 DeepSeek 在其他 benchmark 上的 LOMO 分析结果，讨论其排除对 MATH variance structure 的可能影响。\n\n**W4** [warning] Bootstrap resampling 策略对 stratified design 的适配性\n- 具体位置：Section 3.1\n- 建议：说明是否为 stratified bootstrap；若否，对比一次 stratified bootstrap 的 CI。\n\n---\n\n## 小问题（不影响接收）\n\n- Section 4.1: text-exact-match 下 G=0.007 的 implication 值得更多讨论（1-2 句），这对使用 BLEU/ROUGE 等 non-binary metrics 的实践者有重要参考价值。\n- Table 3 caption: \"prompt\" 列在 MC 和 FF 下含义不同（MC: prompt×item, FF: prompt main effect），虽然 caption 有解释，但在表内加注标记可减少误读。\n- Section 4.6: Qwen 3B vs 7B 的 scale validation 中 \"prompt×item: 12.2% at 7B vs. 8.8% at 3B\"——这个 3.4pp 差异是否 statistically significant？CI 未报告。\n- Appendix A: null calibration 的 \"observed-to-null variance ratio is 1.0008\" 的表述不够直观，建议改为更易解读的形式。\n\n---\n\n## 主要优势\n\n1. **规模和完整性无出其右**：2.3M 记录、7 facets、5 benchmarks、8 models 的完全交叉设计，在 LLM evaluation variance 研究中首屈一指。\n2. **Robustness 验证堪称典范**：8 项附录分析 + 3 个独立采样验证，任何单一分析选择的影响都被系统性地排除。\n3. **写作透明诚实**：主动报告 p=0.10、CI 跨零、hedging language 贯穿全文——这是高质量研究应有的态度。\n4. **D-study 的实践价值**：Table 4-5 可直接指导 evaluation 实验设计优化，10× efficiency gain 在所有 benchmark 上被 bootstrap CI 确认。\n5. **与 IRT 的正交互补定位**：Section 4.5 的 IRT comparison 清晰有力，避免了与 TinyBenchmarks/PSN-IRT 的虚假竞争叙事。\n",
  "reviewer_id": "1",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 审稿意见 — 方法严谨性 + 实验设计\n\n**论文**: Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Analysis\n**Venue**: EMNLP 2026 via ACL Rolling Review\n\n---\n\n## Paper Summary\n\n本文将 Generalizability theory (G-theory) 应用于 LLM 评测的方差分解，在 8 个开源 7-9B 参数模型和 5 个 benchmark（3 MC + 2 FF）上设计了最多 7 个 facet 的完全交叉实验，共 2.3M 条评测记录。主要发现：(1) item-related variance（item + model×item DIF 的捆绑指标）在 MC benchmark 上集中于 68-72%，在 FF benchmark 上分散至 31-41%，五个 benchmark 无重叠；(2) 多 facet 设计达到 G≥0.80 所需 item 数是单条件设计的 1/10（55 vs 552）；(3) BF16/FP16 在 binary scoring 下功能等价；(4) 发布 D-study 预算计算器。\n\n---\n\n## Summary of Strengths\n\n**S1. 首个大规模多 facet 交叉 G-theory 分析。** 此前研究要么只分解单因素（Sclar et al., 2024; Yuan et al., 2025），要么仅在单个 benchmark 上应用 G-theory（Messing, 2026）。本文同时交叉 7 个 facet、覆盖 5 个 benchmark，实验规模（2.3M 记录）在该领域罕见。设计矩阵（Table 1）清晰地展示了完整的 crossing 结构，Figure 1 的设计图直观有效。\n\n**S2. 极其充分的 robustness 验证。** Appendix A 报告了 8 项独立的鲁棒性分析（GLMM complement、accuracy-range stability、estimator comparison、CI method、facet specification、LOMO、null calibration、reduced crossing validation），主文中还有 3 个独立采样的 CV=3.1% 验证。这种验证深度在同领域论文中极为少见，远超审稿人通常的期望。\n\n**S3. 实用性强的 D-study 贡献。** Table 4 和 Table 5 提供了可直接用于实验设计优化的 item budget 数据，10× efficiency gain 在 cross-model projections 中被 bootstrap CI 确认（所有 benchmark 的 ratio 均 >10×）。D-study calculator 是即时可用的实践工具。\n\n**S4. 与 IRT 方法的正交互补定位。** Section 4.5 中将 IRT-selected 116 items（Zhou et al., 2026）置于单条件 vs 多 facet 条件下对比（G=0.457 vs 0.895），清晰展示了 IRT item selection 和 G-theory protocol optimization 的正交性，避免了与 IRT 文献的虚假对立。\n\n**S5. 论文写作严谨透明。** 通篇使用 \"suggest\"/\"format-associated\" 而非因果性语言；在 Section 4.3 中主动报告 permutation test p=0.10 和 benchmark-level CI 跨零；Limitations 明确承认 n=5 的统计功效限制。\n\n---\n\n## Summary of Weaknesses (numbered)\n\n**N1. [critical] Item-related variance 捆绑指标放大了 \"item 主导\" 叙事**\n\n- **具体位置**: Section 3.1 定义、Abstract、Contribution 1、Section 4.3、Conclusion\n- **问题**: 论文定义 \"item-related variance\" = σ²_p + σ²_pM（item difficulty + model×item DIF），得到 MC 68-72% vs FF 31-41% 的 \"no overlap\" 结论。但 model×item interaction 本质上是双向的——它同时反映 item 和 model 的异质性。从 Table 3 可见，未捆绑的 item_id 单独仅占 MC 34-38% / FF 17-24%，model×item 占 MC 30-36% / FF 15-17%。将 model×item 全部归入 \"item-related\" 使得 item 的表观主导地位翻倍（37.9% → 68.1% on MMLU）。\n- **为什么影响接收**: Abstract 和 Contribution 列表中突出强调 \"68-72% vs 31-41%\" 和 \"no overlap\"，这是论文的 flagship claim。仅阅读 abstract 的读者会严重高估 item 作为 \"primary reliability lever\" 的程度。虽然在 G-theory 教育测量传统中 DIF 归为 item property 有先例（Brennan, 2001, Ch. 4），但 LLM evaluation 场景中 model×item 的含义不同于人类测试中的 person×item——它反映的是 architecture-specific capability profiles，既是 item property 也是 model property。\n- **建议修改方向**: (a) 在 abstract 和 contribution 中同时报告 unbundled 和 bundled 数字（如 \"item difficulty alone: 34-38% MC, 17-24% FF; with model×item DIF: 68-72% vs 31-41%\"）；(b) 在 Section 3.1 讨论 bundling 在 LLM 场景下的具体语义差异；(c) 检验 \"no overlap\" 结论在 unbundled item_id 单独指标上是否同样成立（从 Table 3 看确实成立，但应明确讨论）。\n\n**N2. [critical] Format-associated claim 的统计功效严重不足（n=5 benchmarks, p=0.10）**\n\n- **具体位置**: Section 4.3（permutation test）、Abstract、Contribution 1\n- **问题**: 论文的核心发现——variance structure 是 \"format-associated\"——基于 3 MC vs 2 FF benchmarks 的比较。Permutation test p=0.10（10 exhaustive permutations），benchmark-level CI 跨零 [-1.7, 5.1]。在 n=5 的情况下，即使真实效应很大，统计功效也极低。Cohen's d=1.73 在 item-level 很精确，但 benchmark-level 的推断本质上是 n=5 的观察性比较。\n- **为什么影响接收**: 这是论文 4 个贡献中排名第一的、也是 title 和 abstract 的核心叙事。但如审稿人所见，p=0.10 在常规显著性水平下不显著，且 exhaustive permutation 的分辨率上限就是 p=0.10（1/10）。论文虽然在 Section 4.3 和 Limitations 中承认了这一点，但 abstract 说 \"with no overlap across all five benchmarks\" 时未提及统计功效限制，容易误导读者将 observed pattern 当作 confirmed generalization。\n- **建议修改方向**: (a) Abstract 中应明确标注这是 n=5 的观察性 pattern（如 \"across the five benchmarks studied\"）；(b) 讨论 permutation test 在 n=5 时的 power ceiling——即使真实效应为无穷大，p 最小只能到 0.10；(c) 考虑报告 exact one-sided p 值并讨论 Bayesian 替代分析来补充 frequentist 功效不足的问题；(d) 更明确地将此定位为 \"exploratory finding requiring confirmatory replication\" 而非 established pattern。\n\n**W1. [warning] 8 个 purposively selected models 作为 quasi-random facet 的泛化性有限**\n\n- **具体位置**: Section 3.2, Section 3.4 (model facet validation), Appendix A (LOMO)\n- **问题**: 8 个模型均为 open-weight, instruction-tuned, 7-9B 参数。LOMO 分析和 4-model subset D-study 验证了这 8 个模型之间的内部一致性（LOMO: item_id 36-41%, ΔG ≤ 0.019; 4-model: predicted 0.893 vs observed 0.896），但这只能说明 within-sample stability，不能证明这些模型代表了 \"all admissible models\" 的 universe。API-based models（GPT-4, Claude）、base models、70B+ models、domain-adapted models 均被排除。Scale validation（Section 4.6）仅覆盖 Qwen 3B-9B 单一 family。\n- **建议**: 在 Section 3.4 中更明确地界定 quasi-random facet assumption 的 target universe（如 \"the universe of 7-9B open-weight instruction-tuned models available as of 2025\"），并讨论 larger models 可能因 ceiling effects 改变 variance structure（Limitations 已简略提及，建议更具体量化预期）。\n\n**W2. [warning] Exp-002 reduced crossing 的验证仅基于 MMLU**\n\n- **具体位置**: Section 3.3, Appendix A (Reduced crossing validation)\n- **问题**: Exp-002 将 exp-001 的 3 precisions × 3 temperatures 缩减为 BF16-only × 2 temperatures。验证 ΔG=0.0008 是在 exp-001 的 MMLU 子集上做的。但 exp-002 将此 reduced design 应用到了 ARC、HellaSwag、GSM8K、MATH，这些 benchmark 上没有 full crossing 可供对比验证。特别是 FF benchmarks 的 variance structure 明显不同于 MC（residual 40-44% vs 15-25%），reduced crossing 在 FF 上是否同样 preserving structure 是未验证的假设。\n- **建议**: 明确说明此验证的 transferability assumption，或至少在一个 FF benchmark 上做 sensitivity analysis（如 MATH 的 full crossing 子集）。\n\n**W3. [warning] MATH 排除 DeepSeek（7/8 models）的影响未充分讨论**\n\n- **具体位置**: Section 4.3, Appendix B (footnote on MATH)\n- **问题**: MATH 因 DeepSeek inference 数据不完整（37,400/57,600）而仅用 7 个模型。论文仅在 Table 3 脚注和 Appendix B 简略提及。但 DeepSeek 作为中国主流 LLM 之一，其在 MATH 上的表现可能与其他模型有系统性差异（DeepSeek 系列在数学推理上有特定优化）。排除它可能影响 model×item interaction 的估计，进而影响 FF benchmark 的 item-related variance 比例。\n- **建议**: 报告 DeepSeek 在其他 4 个 benchmark 上的 variance contribution（LOMO 中它是否异常），并讨论其排除对 MATH 结论的可能影响方向。\n\n**W4. [warning] Bootstrap item-level resampling 在 stratified design 下可能产生 representation bias**\n\n- **具体位置**: Section 3.1 (\"1,000-resample bootstrap confidence intervals, item-level resampling with replacement\")\n- **问题**: MMLU 的 200 items 来自 10 个 subjects（每个 20 items），Bootstrap 对 items 做有放回抽样。每次 resample 平均只包含约 127 unique items（200 × (1-1/e)），且不保证每个 subject 都有代表。对于 stratified 设计，标准做法是 stratified bootstrap（在每个 stratum 内分别 resample），否则 CI 可能偏窄或偏宽。\n- **建议**: (a) 报告是否使用 stratified bootstrap；(b) 如果是 unstratified，对比一次 stratified bootstrap 的 CI 宽度。Appendix A 已报告 bootstrap vs jackknife 的宽度比 0.96-1.04，如果 jackknife 是 stratified 的则可作为间接验证。\n\n---\n\n## Questions for Authors\n\n**Q1.** Section 3.1 将 model×item DIF 归入 \"item-related variance\" 并以此为核心叙事。能否提供 unbundled item_id 单独指标下的 format-associated separation 的 permutation test 结果？从 Table 3 看 item_id 在 MC (34-38%) 和 FF (17-24%) 之间也无重叠，是否也做了 formal test？\n\n**Q2.** Probit simulation 的 Spearman ρ=0.732（Section 3.4）意味着 binary vs continuous 下的 variance component rankings 有约 46% 的方差未被保留。能否报告具体哪些 components 的 rank 在 dichotomization 后发生了变化？是否主要影响小的 components（如 seed×item, ordering×item），而大的 components（item, model×item）的 rank 始终一致？\n\n**Q3.** Text-exact-match 下 G 崩溃到 0.007（Section 4.1）是一个重要发现，但讨论较少。这暗示 variance structure 不仅 format-associated，更是 metric-conditional。能否进一步解释为什么 text-exact-match 的 temperature 方差如此巨大（79.7%）？这对使用非 binary scoring metric 的实践者有什么具体指导意义？\n\n**Q4.** D-study 的 cross-model projections（Table 5）使用了 8-model 的 variance components 来投影不同 item 数的 G 值。这些投影假设 variance components 在不同 item 数下稳定。Section 4.7 的 3 个独立 200-item 样本的 CV=3.1% 验证了 200 items 的稳定性，但有无证据表明在 55 items（multi-facet 的 G≥0.80 threshold）时 components 同样稳定？\n\n**Q5.** Section 4.3 报告 MMLU 内 10 个 subject 的 difficulty dispersion 与 item variance share 的 Spearman ρ=0.806 (p=0.005)。high_school_mathematics 的 item variance (10.4%) 低于 GSM8K (16.9%)，论文推断 \"item heterogeneity, not format per se, drives variance allocation\"。但这是基于单个异常 subject 的推断——能否控制 difficulty dispersion 后看 format 是否仍有独立效应？\n\n---\n\n## Missing References\n\n- Mushquash & O'Connor (2006) 和 Jiang & Bayesian G-theory (2018) 在 Related Work 中被提及但仅作为 psychometrics foundations。建议简要讨论 Mushquash & O'Connor 对 binary data 下 G-theory 的具体发现，因为这直接关系到 Section 3.4 的方法选择。\n- Yin et al. (2025, \"From Crowdsourcing to Benchmarking: A Framework for Evaluating LLMs with Human Preferences\") 从 crowdsourcing 角度讨论 LLM evaluation reliability，与本文的 multi-facet reliability 分析有互补关系。\n- Burnell et al. (2023, \"Rethink reporting of evaluation results in AI\") 提出了 evaluation reporting standards，与本文的 reproducibility budgets 贡献直接相关。\n\n---\n\n## Limitations and Societal Impact\n\nLimitations section（约半页，3 个 scope constraints + 2 个 future extensions）覆盖了核心限制，长度适当。建议补充：metric-conditional variance structure（binary vs text-exact-match 的巨大差异）作为第四个 scope constraint，因为所有结论都是 conditional on binary scoring 的。\n\n无明显 ethical concerns。研究对象是公开模型和公开 benchmark。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4/5 | 方法论整体严谨，robustness 验证极为充分（8项附录分析）。主要扣分点：headline claim (format-associated) 的 benchmark-level 统计功效不足 (n=5, p=0.10)；item-related bundling 的语义在 LLM 场景下可被质疑。但论文通篇使用审慎措辞，且主动报告了限制。 |\n| Excitement | 3.5/5 | G-theory 应用于 LLM evaluation 的规模化分析是新颖的（超越 Messing 2026 的单 benchmark 局限），D-study budget calculator 有即时实用价值。但 flagship finding (format-associated pattern) 在 benchmark 水平上 underpowered，限制了结论的影响力。 |\n| Reproducibility | 4/5 | 实验设计详尽（Table 1 完整设计矩阵、Appendix C 模型和 prompt 详情）。vLLM 版本、GPU 型号、所有超参数均明确报告。代码和数据承诺 publication 后发布——如能 camera-ready 时附 anonymous repo link 则更好。唯一扣分点：stratified sampling 的具体实现细节（如非 MMLU benchmark 的 200-item 选择策略）未充分描述。 |\n| Overall Assessment | 3.5 (Borderline Conference) | 方法论贡献扎实（首个大规模多 facet G-theory 分析 + D-study calculator），写作严谨透明。但核心发现 (format-associated variance pattern) 的 benchmark-level evidence 不足（n=5, p=0.10, CI 跨零），且 item-related variance 的 bundling 定义放大了 item 主导叙事。作为 Findings 论文可被接收（Soundness 和 Reproducibility 达标）；若目标是 main conference，需补充 benchmarks 以增强 format claim 的统计支撑。 |\n| Confidence | 4/5 | 本人在实验设计、方差分析和 psychometrics 方法方面有较深背景，仔细阅读了全文和附录，核对了关键统计数据。对 G-theory 的 binary data extensions 不是最深入的专家。 |\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 — Borderline Conference\n\n**一句话总结**: 方法论严谨、robustness 验证充分的大规模 G-theory 分析，但核心 \"format-associated\" claim 在 benchmark 水平上严重 underpowered（n=5, p=0.10），且 item-related variance 的 bundling 操作放大了 item 主导叙事——需要更多 benchmarks 和更透明的 unbundled reporting 才能支撑 main conference 级别的结论。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Item-related variance bundling 放大 item 主导叙事\n- 具体位置：Section 3.1, Abstract, Contribution 1, Conclusion\n- 问题：将 model×item DIF 全部归入 \"item-related\" 使 item 表观贡献翻倍（MMLU: 37.9% → 68.1%）。model×item 在 LLM 场景中同时是 model property（architecture-specific capability profiles）。Abstract 中 \"68-72% vs 31-41%\" 的 flagship claim 依赖此 bundling，未同步报告 unbundled 数字。\n- 为什么影响接收：核心叙事的可信度取决于此定义的合理性。不报告 unbundled 数字 = 信息不对称。\n- 建议：Abstract/Contribution 中并列报告 unbundled 和 bundled 数字；Section 3.1 讨论 bundling 在 LLM vs 教育测量场景中的语义差异。\n\n**N2** [critical] Format-associated claim 的统计支撑不足\n- 具体位置：Section 4.3, Abstract, Contribution 1\n- 问题：n=5 benchmarks, permutation test p=0.10（分辨率上限 = 1/10）, benchmark-level CI 跨零 [-1.7, 5.1]。Abstract \"with no overlap across all five benchmarks\" 未注明统计限制。\n- 为什么影响接收：这是论文排名第一的贡献和 title 的核心内容。读者可能将 observed pattern 误认为 statistically confirmed generalization。\n- 建议：Abstract 明确标注为 n=5 的观察性 pattern；讨论 permutation test 的 power ceiling；考虑 Bayesian 补充分析。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Quasi-random model facet 的 target universe 定义模糊\n- 具体位置：Section 3.2, 3.4\n- 建议：明确界定 target universe 为 \"7-9B open-weight instruction-tuned models\"，讨论 ceiling effects 对 larger models 的预期影响。\n\n**W2** [warning] Reduced crossing 验证仅基于 MMLU，未在 FF benchmark 上验证\n- 具体位置：Section 3.3, Appendix A\n- 建议：至少在一个 FF benchmark 上做 sensitivity check，或明确声明 transferability assumption。\n\n**W3** [warning] MATH 排除 DeepSeek 的影响未讨论\n- 具体位置：Section 4.3, Appendix B\n- 建议：报告 DeepSeek 在其他 benchmark 上的 LOMO 分析结果，讨论其排除对 MATH variance structure 的可能影响。\n\n**W4** [warning] Bootstrap resampling 策略对 stratified design 的适配性\n- 具体位置：Section 3.1\n- 建议：说明是否为 stratified bootstrap；若否，对比一次 stratified bootstrap 的 CI。\n\n---\n\n## 小问题（不影响接收）\n\n- Section 4.1: text-exact-match 下 G=0.007 的 implication 值得更多讨论（1-2 句），这对使用 BLEU/ROUGE 等 non-binary metrics 的实践者有重要参考价值。\n- Table 3 caption: \"prompt\" 列在 MC 和 FF 下含义不同（MC: prompt×item, FF: prompt main effect），虽然 caption 有解释，但在表内加注标记可减少误读。\n- Section 4.6: Qwen 3B vs 7B 的 scale validation 中 \"prompt×item: 12.2% at 7B vs. 8.8% at 3B\"——这个 3.4pp 差异是否 statistically significant？CI 未报告。\n- Appendix A: null calibration 的 \"observed-to-null variance ratio is 1.0008\" 的表述不够直观，建议改为更易解读的形式。\n\n---\n\n## 主要优势\n\n1. **规模和完整性无出其右**：2.3M 记录、7 facets、5 benchmarks、8 models 的完全交叉设计，在 LLM evaluation variance 研究中首屈一指。\n2. **Robustness 验证堪称典范**：8 项附录分析 + 3 个独立采样验证，任何单一分析选择的影响都被系统性地排除。\n3. **写作透明诚实**：主动报告 p=0.10、CI 跨零、hedging language 贯穿全文——这是高质量研究应有的态度。\n4. **D-study 的实践价值**：Table 4-5 可直接指导 evaluation 实验设计优化，10× efficiency gain 在所有 benchmark 上被 bootstrap CI 确认。\n5. **与 IRT 的正交互补定位**：Section 4.5 的 IRT comparison 清晰有力，避免了与 TinyBenchmarks/PSN-IRT 的虚假竞争叙事。\n",
    "reviewer_id": "1",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 259 · 2026-05-22T09:56:56.869436+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3963
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-22T09:57:01.338733+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 261 · 2026-05-22T09:57:01.390548+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 262 · 2026-05-22T09:57:05.203867+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_3/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-22T09:57:05.254453+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 264 · 2026-05-22T09:57:11.479317+00:00_

审稿意见已提交给 Review Director。

**评分摘要**: Overall 3.5 (Borderline Conference), Soundness 4/5, Excitement 3.5/5, Reproducibility 4/5, Confidence 4/5。

**两个 Must-Fix 问题**:
1. Item-related variance bundling（σ²_p + σ²_pM）放大了 item 主导叙事——Abstract 应并列报告 unbundled 数字
2. Format-associated claim 的 benchmark-level 统计功效严重不足（n=5, p=0.10, CI 跨零），Abstract 应明确标注为观察性 pattern

**四个 Should-Fix**: quasi-random model facet 的 universe 定义、reduced crossing 仅在 MMLU 上验证、MATH 排除 DeepSeek 的影响未讨论、bootstrap 对 stratified design 的适配性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1"
}
```

</details>

---


## Round 8

## Round 8

8 recorded events


### User

_source line 265 · 2026-05-22T09:59:16.267551+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每一条 Strength/Weakness/Question，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 完整审稿意见

### Summary
本文将 G-theory 应用于 LLM evaluation，7-facet fully crossed factorial experiment，8 模型，5 benchmarks，2.3M records。核心发现：format-associated variance structure、10× item efficiency gain、BF16/FP16 interchangeability、D-study calculator。

### Must-Fix (Critical)

**N1.** Format-associated claim 的统计支撑不足——permutation test p=0.10, benchmark-level CI spans zero。Abstract 和 conclusion 使用 "suggest" 但暗示的结论强度超过统计证据。建议增加 benchmarks 或明确定位为 "observed pattern on 5 benchmarks requiring confirmatory validation"。

**N2.** Format-associated pattern 的 trivial explanation 未充分排除——MC 格式天然约束输出空间为 A/B/C/D，item 作为主导变异源是 response format 的固有属性。high_school_mathematics 的反例证据仅 20 items，属 anecdotal。如果 finding 只是 MC/FF response space constraint 的 tautological consequence，novelty 大幅降低。

### Should-Fix (Warning)

**W1.** Item-related variance 的 bundling 定义（σ²_p + σ²_pM）夸大了 MC/FF 差异。DIF (model×item) 本质上是 model-specific 的 item difficulty profile。合并后差距 ~30pp，unbundled 仅 ~15pp。

**W2.** 模型范围 7-9B 限制 D-study budgets 泛化性——70B+ ceiling effects 可能改变 budget。

**W3.** Binary scoring 作为 FF variance structure 混淆因素——binary 对 FF 丢失 partial credit 信息（reasoning path quality, intermediate steps），可能是 FF 高 residual (40-44%) 的原因，partial/continuous scoring 可能缩小 format gap。

**W4.** Exp-002 reduced crossing 验证仅限 MMLU。

**W5.** References 格式不完整——varannot2025gtheory author 为 "Anonymous"（double-blind 合规疑虑）；多个条目 author 使用 "and others"；kipnis2025metabench, li2025atlas 缺 URL。

### Questions

**Q1.** 使用 0/partial/1 或 rubric-based continuous scoring 替代 binary scoring，FF variance structure 是否实质变化？——排除 binary scoring 作为混淆因素的关键实验。

**Q2.** high_school_mathematics 的 10.4% item variance 是否受 20 items 小样本限制？能否在更多 borderline subjects 上验证？

**Q3.** D-study budgets 是否有 out-of-sample validation？第 9 个模型或新 200-item sample 的验证？

**Q4.** varannot2025gtheory 在 bib 中 author 为 "Anonymous"——是否为自己的工作？ARR double-blind 合规？

### Missing References
- Gruber et al. (2024) "Towards Reproducible LLM Evaluation" (arXiv:2410.03492)
- Wang et al. (2025) "Benchmark2: Systematic Evaluation of LLM Benchmarks" (arXiv:2601.03986)

### 格式合规
- 正文 ≤8 页 ✅
- review mode + Anonymous ✅
- Double-blind ⚠️（varannot2025gtheory "Anonymous" 需确认）
- References ⚠️（部分条目不完整）

### 评分
Overall 3.5 (Borderline Conference), Soundness 4/5, Excitement 2.5/5, Reproducibility 4/5, Confidence 4/5

---

请逐条回应上述所有 Must-Fix (N1-N2)、Should-Fix (W1-W5)、Questions (Q1-Q4)。特别关注：

1. R2-N2 的 "trivial explanation" 论点——你是否同意 MC response space constraint 是 format-associated variance pattern 的 sufficient explanation？
2. R2-W3 的 "binary scoring 混淆" 论点——你是否同意 partial credit scoring 可能缩小 format gap？
3. R2 的 Excitement 评分显著低于你（2.5 vs 3.5）——你如何看待 novelty 评估的分歧？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 266 · 2026-05-22T09:59:51.575070+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex",
  "offset": "42",
  "limit": "35"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex",
    "offset": "42",
    "limit": "35"
  }
}
```

</details>

---


### Tool result

_source line 267 · 2026-05-22T09:59:52.026447+00:00_

42	
43	\subsection{Format-Associated Variance Structure}
44	\label{sec:format_conditional}
45	
46	We extend to five benchmarks (three MC: MMLU, ARC-Challenge, HellaSwag; two FF: GSM8K, MATH) using exp-002 (8 models $\times$ BF16 $\times$ 2 temperatures $\times$ 6 prompts $\times$ 6 seeds $\times$ 4 orderings $\times$ 200 items; MATH uses 7 models due to incomplete DeepSeek inference data). Table~\ref{tab:cross_benchmark} reveals a systematic format-associated pattern. For MMLU and ARC-Challenge, item difficulty and model$\times$item are the two largest components (37.9\% + 30.2\% and 37.9\% + 33.7\% respectively). HellaSwag is the sole MC exception where model$\times$item slightly exceeds item (36.0\% vs.\ 34.3\%), though their sum remains in the MC range. In all three MC benchmarks, item-related variance (item + model$\times$item DIF; e.g., MMLU: 37.9\% + 30.2\% = 68.1\%) concentrates at 68--72\%.
47	
48	Free-form benchmarks differ markedly. On GSM8K, variance distributes across item (16.9\%), model$\times$item (14.6\%), model (10.7\%), and model$\times$prompt (8.5\%); prompt main effect is 5.4\%. MATH shows an intermediate pattern: item leads at 24.0\% with model$\times$item at 17.3\%, but residual variance is substantially larger (43.9\%). The large FF residuals (40--44\%) likely reflect chain-of-thought path diversity, answer extraction variability, and unmodeled higher-order interactions.
49	
50	\begin{table}[t]
51	\centering
52	\caption{Format-associated variance structure across five benchmarks (exp-002, 8 models; MATH: 7). Variance components (\%) per benchmark; MC = multiple-choice, FF = free-form. Bold indicates the dominant non-residual component per benchmark. For MC benchmarks, ``prompt'' reports prompt$\times$item (prompt main effect $<$1\%); for FF benchmarks, it reports the prompt main effect.}
53	\label{tab:cross_benchmark}
54	\scriptsize
55	\begin{tabular}{l rrr rr}
56	\toprule
57	 & \multicolumn{3}{c}{MC} & \multicolumn{2}{c}{FF} \\
58	\cmidrule(l
…[truncated 2319 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-22T09:59:52.026803+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-22T09:59:52.077377+00:00_

1	% references.bib — auto-generated from literature_map.yaml (29 cited papers)
2	% Last synced: 2026-05-21
3	
4	% ====== G-Theory & Evaluation Variance ======
5	
6	@article{messing2026hidden,
7	  title={Hidden Measurement Error in {LLM} Pipelines Distorts Annotation, Evaluation, and Benchmarking},
8	  author={Messing, Solomon},
9	  year={2026},
10	  journal={arXiv preprint arXiv:2604.11581},
11	  url={https://arxiv.org/abs/2604.11581}
12	}
13	
14	@article{wei2025gtheory,
15	  title={Exploring {LLM} Autoscoring Reliability Using Generalizability Theory},
16	  author={Wei, Jiangang and others},
17	  year={2025},
18	  journal={arXiv preprint arXiv:2507.19980},
19	  url={https://arxiv.org/abs/2507.19980}
20	}
21	
22	@article{madaan2024quantifying,
23	  title={Quantifying Variance in Evaluation Benchmarks},
24	  author={Madaan, Lovish and Bhatia, Samarth and Tulio Ribeiro, Marco and Roth, Dan},
25	  year={2024},
26	  journal={arXiv preprint arXiv:2406.10229},
27	  url={https://arxiv.org/abs/2406.10229}
28	}
29	
30	@inproceedings{bouthillier2021accounting,
31	  title={Accounting for Variance in Machine Learning Benchmarks},
32	  author={Bouthillier, Xavier and Delaunay, Pierre and Bronzi, Mirko and Trofimov, Assya and Nichyporuk, Brennan and Szeto, Justin and Sepahvand, Nazanin Mohammadi and Raff, Edward and Madan, Kshitij and Voleti, Vikram and Kahou, Samira Ebrahimi and Michalski, Vincent and Arbel, Tal and Pal, Chris and Varoquaux, Ga{\"e}l and Vincent, Pascal},
33	  booktitle={Proceedings of Machine Learning and Systems (MLSys)},
34	  year={2021},
35	  url={https://arxiv.org/abs/2103.03098}
36	}
37	
38	@book{shavelson1991generalizability,
39	  title={Generalizability Theory: A Primer},
40	  author={Shavelson, Richard J. and Webb, Noreen M.},
41	  year={1991},
42	  publisher={SAGE Publications},
43	  isbn={978-0-8039-3744-4}
44	}
45	
46	@book{brennan2001generalizability,
47	  title={Generalizability Theory},
48	  author={Brennan, Robert L.},
49	  year={2001},
50	  publ
…[truncated 12594 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 270 · 2026-05-22T10:02:15.565829+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix (Critical)\n\n**[AGREE] R2-N1: Format-associated claim 统计支撑不足**\n\n同意，与我的 N2 完全一致。n=5 benchmarks 下 permutation test p=0.10 无法区分真实效应和随机分配（exhaustive permutation 的分辨率上限 = 1/10）。Abstract \"with no overlap across all five benchmarks\" 确实暗示的结论强度超过证据支撑。R2 的建议 \"observed pattern on 5 benchmarks requiring confirmatory validation\" 与我的建议方向一致。\n\n两位 Reviewer 对此问题达成共识，应作为 revision 的首要优先项。\n\n---\n\n**[REBUT] R2-N2: Format-associated pattern 的 trivial explanation（MC response space constraint）**\n\nR2 的论点：MC 天然约束输出到 A/B/C/D，因此 item 主导是 response format 的固有属性——finding 是 tautological consequence，novelty 大幅降低。\n\n我不同意\"tautological\"的强判断，理由如下：\n\n**(1) 论文已提供 within-format 反例。** Section 4.3 报告 `high_school_mathematics`（MC 格式但包含开放式数值题）item variance 仅 10.4%，低于 FF benchmark GSM8K (16.9%)。R2 认为 20 items 属 anecdotal——这是合理顾虑，但关键证据不是这单个 subject，而是 **10 个 MMLU subjects 上的 ρ=0.806 (p=0.005)** 分析。这个相关性表明 item difficulty dispersion（而非 format 本身）是 variance allocation 的驱动因素。如果 MC response space constraint 是 sufficient explanation，则 ALL MC subjects 应展示类似的高 item variance——但实际上 10 个 subjects 间有显著差异。\n\n**(2) HellaSwag 进一步削弱 tautological 论点。** Table 3 显示 HellaSwag (MC) 的 model×item (36.0%) 超过 item difficulty (34.3%)。如果 MC format 机械性地保证 item 主导，HellaSwag 不应出现此反转。\n\n**(3) 但 R2 的关注点有合理内核。** 论文确实没有充分讨论 MC/FF response space 差异与 item variance 的 mechanistic relationship。MC 的 constrained output space 降低了 generation process 的变异性，间接提高了 item 的相对占比——这不是 tautology，而是 confounded mechanism。论文应在 Section 4.3 增加 1-2 段讨论：response space constraint 作为 item variance concentration 的 partial mediator，并明确区分 \"format constrains generation noise\"（mechanistic explanation）和 \"items have more heterogeneous difficulty\"（substantive finding）。\n\n**(4) Novelty 不应仅由 format finding 决定。** 即使 format-associated pattern 有 mechanistic explanation，D-study budgets（Contribution 2）、precision separability（Contribution 3）、和 toolkit（Contribution 4）的 novelty 完全独立于此。10× efficiency gain 及其 cross-benchmark validation 是实践性贡献，不受 trivial explanation 影响。\n\n**结论：R2 的 \"trivial explanation\" concern 值得讨论但不构成 novelty 的根本否定。** 建议作者增加 mechanism discussion，但不应将此升级为 must-fix。我维持此条为 should-fix。\n\n---\n\n### Should-Fix (Warning)\n\n**[AGREE] R2-W1: Item-related variance bundling 夸大 MC/FF 差异**\n\n与我的 N1 一致。R2 的量化更直接：bundled 差距 ~30pp，unbundled 仅 ~15pp。补充一点：从 Table 3 可验证，unbundled item_id 的 MC (34-38%) vs FF (17-24%) 分离同样成立（无重叠），因此 \"no overlap\" claim 在 unbundled 指标下也成立。但 bundling 确实放大了效果的视觉和叙事冲击力。\n\n---\n\n**[AGREE] R2-W2: 模型范围 7-9B 限制泛化性**\n\n与我的 W1 一致。补充：Section 4.6 的 Qwen 3B-9B scale validation 虽然确认了 item dominance 在 3B-9B 范围内的 scale-robustness，但 Limitations 已承认 \"larger models with higher accuracy could exhibit compressed item variance due to ceiling effects\"。D-study budgets 的具体数字（Table 4-5）确实不应被直接外推到 70B+ 模型。\n\n---\n\n**[AGREE] R2-W3: Binary scoring 作为 FF variance structure 混淆因素**\n\n这是 R2 提出的重要新视角，我在 Round 1 审稿中未充分展开（仅在 \"小问题\" 中建议增加 text-exact-match 讨论）。\n\nR2 的论点是 sound 的：binary scoring 将 FF 任务的 partial credit 信息（推理路径质量、中间步骤）压缩为 0/1，这可能是 FF 高 residual (40-44%) 的主要原因。Section 4.1 的 text-exact-match 结果（G 崩溃到 0.007, temperature 主导 79.7%）已经证明 scoring metric 根本性地改变 variance structure，支持 R2 的担忧。\n\n具体而言：\n- FF benchmarks 下，模型可能生成了正确的推理但因 minor formatting 差异被判 0——这部分 variance 被 binary scoring 归入 residual\n- 如果使用 partial credit scoring（0/0.5/1），FF 的 item variance share 可能上升（因为 partial credit 捕获了 item difficulty gradient），model×item 和 model×prompt 可能下降\n- 这意味着 format-associated gap 可能部分是 scoring-metric artifact，而非 format 的 intrinsic property\n\n**建议升级此条为 must-fix level**——至少需要在 Limitations 中明确 \"all conclusions are conditional on binary scoring; partial credit scoring may alter the FF variance structure and reduce the format-associated gap\"。这比我原本的建议（增加 1-2 句讨论）更强，但 R2 的论证说服了我。\n\n---\n\n**[AGREE] R2-W4: Exp-002 reduced crossing 验证仅限 MMLU**\n\n与我的 W2 一致。\n\n---\n\n**[AGREE] R2-W5: References 格式不完整**\n\n已从 references.bib 验证：\n- `varannot2025gtheory`：author 字段为 `{Anonymous}`（line 291），arXiv:2601.02370。如果这是他人的 anonymous preprint，bib 中写 Anonymous 是可接受的。但如果是作者自己的未发表工作，则违反 double-blind policy（ARR guidelines 要求 self-citation 使用第三人称且不 anonymize）。R2 的 flag 合理。\n- `wei2025gtheory`（line 17）、`xiao2025construct`（line 299）、`jin2025psychometrics`（line 307）：均使用 \"and others\" 代替完整 author list。虽然 arXiv preprints 有时确实 author 众多，但标准做法是列出所有作者或使用 \"et al.\" 格式，\"and others\" 不规范。\n- `kipnis2025metabench`（line 184-189）、`li2025atlas`（line 192-196）：确实缺少 URL 字段。\n\n这些是 minor formatting issues，但 varannot2025gtheory 的 double-blind 合规问题需要作者明确回应。\n\n---\n\n### Questions\n\n**[AGREE] R2-Q1: Partial/continuous scoring 对 FF variance structure 的影响**\n\n这是验证 W3 的 key experiment。Binary scoring 下的 FF variance structure 可能与 partial/rubric-based scoring 有质的不同。虽然超出当前稿件范围（需要全新评测 pipeline），但至少应作为 future work 明确提出，且当前结论应加 \"under binary scoring\" 的 scope qualifier。\n\n---\n\n**[REBUT] R2-Q2: high_school_mathematics 的 20 items 小样本问题**\n\nR2 关注 20 items 的小样本限制是合理的，但对证据链的解读不够完整。论文的核心证据不是单个 subject 的 anecdotal observation，而是 **10 个 subjects 上的 Spearman ρ=0.806 (p=0.005)**。这个 correlation 基于 10 个数据点（每个 subject 一个 item variance share 和一个 difficulty dispersion 值），统计功效虽有限但 p=0.005 在 n=10 下有意义。high_school_mathematics 是这个 trend 中的一个特别有说服力的 data point，但不是唯一证据。\n\n但我同意扩展到更多 borderline subjects 会 strengthen 此分析。具体建议：可以利用 MMLU 完整 57 subjects 的数据（而非仅 sample 的 10 个）做全量 correlation。\n\n---\n\n**[AGREE] R2-Q3: D-study budgets 的 out-of-sample validation**\n\nSection 4.7 的 3 个独立 200-item samples（CV=3.1%）和 Section 3.4 的 4-model subset prediction（predicted G=0.893 vs observed 0.896, Δ=0.003）提供了 within-design validation，但没有真正的 out-of-sample validation（如第 9 个模型、新 benchmark、不同时间点的数据）。这是 D-study contributions 的一个泛化性限制。\n\n---\n\n**[AGREE] R2-Q4: varannot2025gtheory double-blind 合规**\n\n从 bib 看 author 为 `{Anonymous}`，这要求作者在 rebuttal 中明确回应：(a) 这是他人的 anonymous preprint（则可接受）；还是 (b) 自己的工作以 anonymous 形式引用（则可能违反 ARR double-blind policy）。\n\n---\n\n### Missing References\n\nR2 建议补充 Gruber et al. (2024) 和 Wang et al. (2025)。我没有独立验证这两篇的具体内容，但从标题看：\n- Gruber et al. \"Towards Reproducible LLM Evaluation\" 与本文的 reproducibility budgets 直接相关，应引用\n- Wang et al. \"Benchmark2: Systematic Evaluation of LLM Benchmarks\" 提供 meta-benchmark 视角，relevant 但非 essential\n\n---\n\n### Director 指定的三个焦点问题\n\n**1. R2-N2 \"trivial explanation\"——MC response space constraint 是否是 sufficient explanation？**\n\n**不是 sufficient explanation，但是 partial mechanism，论文应讨论。** 如上述 REBUT 所述，within-MMLU 的 ρ=0.806 分析和 HellaSwag 反例否定了纯 tautological 解释。但 R2 正确指出了 MC constrained output space 降低 generation noise 的机制效应。论文的 \"item heterogeneity, not format per se\" 结论（Section 4.3 末句）实际上已经部分回应了此问题，但需要更 explicit 的 mechanistic discussion。\n\n**2. R2-W3 \"binary scoring 混淆\"——partial credit scoring 是否可能缩小 format gap？**\n\n**很可能会。** Binary scoring 对 FF 任务丢失信息量更大（MC 的 binary scoring 相对自然——选对就是对，FF 则丢失了推理路径质量差异）。Partial credit 会将目前归入 residual 的 variance 重新分配到 item 和 model×item components，可能提升 FF 的 item-related variance share，从而缩小 format gap。Section 4.1 的 text-exact-match 数据（scoring metric 改变完全颠覆 variance structure）为此提供了直接经验证据。R2 的担忧是有根据的，我已在上面建议升级此条的严重性。\n\n**3. Excitement 2.5 vs 3.5 的分歧**\n\nR2 给 Excitement 2.5/5，我给 3.5/5，差距 1.0。分歧的核心在于 R2 对 format-associated finding 的 novelty 判断。R2 认为如果 finding 是 \"tautological consequence\"，则 novelty 大幅降低（N2）。\n\n我的立场：\n- 即使 format finding 有 mechanistic explanation（部分同意 R2），**D-study budgets 和 toolkit 的实践 novelty 是独立的**。10× efficiency gain 的量化、cross-benchmark budget 表（Table 5），以及 IRT 与 G-theory 正交互补的展示（Table 4）——这些对 evaluation practitioners 有即时价值，novelty 不受 format mechanism 争议的影响。\n- R2 的 2.5 评分可能低估了 methodological novelty：本文是首个在 LLM evaluation 中实施如此规模（7 facets, 5 benchmarks, 2.3M records）的 G-theory 分析，且 robustness 验证达到了该子领域的新标准。\n- 但我也承认，如果读者主要关注 format finding 且接受 trivial explanation，Excitement 确实会打折扣。\n\n**我维持 3.5/5，但认为 R2 的 2.5/5 反映了对 format finding novelty 的不同判断，不是不合理的评估。** 如果需要 consensus，3.0/5 可能是两位 Reviewer 都能接受的折中。\n\n---\n\n### 汇总：两位 Reviewer 的共识与分歧\n\n**共识项（均 AGREE）：**\n- N1/R1-N2: format-associated claim 统计支撑不足（n=5, p=0.10）→ **Critical, must-fix**\n- W1/R1-N1: item-related bundling 夸大叙事 → **Critical/Warning, must-fix**\n- W2/R1-W1: model range 限制泛化性 → Warning\n- W4/R1-W2: reduced crossing 验证仅限 MMLU → Warning\n- W5: references 格式问题 → Minor\n\n**R2 新增、R1 同意：**\n- W3: binary scoring 作为 FF variance confound → **我建议升级为 must-fix level discussion**\n\n**分歧项：**\n- R2-N2 (trivial explanation): R2 判定为 critical/must-fix，我判定为 should-fix（有合理内核但 not tautological）\n- Excitement: R2 2.5 vs R1 3.5（核心分歧在于 format finding novelty）\n",
  "reviewer_id": "1",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix (Critical)\n\n**[AGREE] R2-N1: Format-associated claim 统计支撑不足**\n\n同意，与我的 N2 完全一致。n=5 benchmarks 下 permutation test p=0.10 无法区分真实效应和随机分配（exhaustive permutation 的分辨率上限 = 1/10）。Abstract \"with no overlap across all five benchmarks\" 确实暗示的结论强度超过证据支撑。R2 的建议 \"observed pattern on 5 benchmarks requiring confirmatory validation\" 与我的建议方向一致。\n\n两位 Reviewer 对此问题达成共识，应作为 revision 的首要优先项。\n\n---\n\n**[REBUT] R2-N2: Format-associated pattern 的 trivial explanation（MC response space constraint）**\n\nR2 的论点：MC 天然约束输出到 A/B/C/D，因此 item 主导是 response format 的固有属性——finding 是 tautological consequence，novelty 大幅降低。\n\n我不同意\"tautological\"的强判断，理由如下：\n\n**(1) 论文已提供 within-format 反例。** Section 4.3 报告 `high_school_mathematics`（MC 格式但包含开放式数值题）item variance 仅 10.4%，低于 FF benchmark GSM8K (16.9%)。R2 认为 20 items 属 anecdotal——这是合理顾虑，但关键证据不是这单个 subject，而是 **10 个 MMLU subjects 上的 ρ=0.806 (p=0.005)** 分析。这个相关性表明 item difficulty dispersion（而非 format 本身）是 variance allocation 的驱动因素。如果 MC response space constraint 是 sufficient explanation，则 ALL MC subjects 应展示类似的高 item variance——但实际上 10 个 subjects 间有显著差异。\n\n**(2) HellaSwag 进一步削弱 tautological 论点。** Table 3 显示 HellaSwag (MC) 的 model×item (36.0%) 超过 item difficulty (34.3%)。如果 MC format 机械性地保证 item 主导，HellaSwag 不应出现此反转。\n\n**(3) 但 R2 的关注点有合理内核。** 论文确实没有充分讨论 MC/FF response space 差异与 item variance 的 mechanistic relationship。MC 的 constrained output space 降低了 generation process 的变异性，间接提高了 item 的相对占比——这不是 tautology，而是 confounded mechanism。论文应在 Section 4.3 增加 1-2 段讨论：response space constraint 作为 item variance concentration 的 partial mediator，并明确区分 \"format constrains generation noise\"（mechanistic explanation）和 \"items have more heterogeneous difficulty\"（substantive finding）。\n\n**(4) Novelty 不应仅由 format finding 决定。** 即使 format-associated pattern 有 mechanistic explanation，D-study budgets（Contribution 2）、precision separability（Contribution 3）、和 toolkit（Contribution 4）的 novelty 完全独立于此。10× efficiency gain 及其 cross-benchmark validation 是实践性贡献，不受 trivial explanation 影响。\n\n**结论：R2 的 \"trivial explanation\" concern 值得讨论但不构成 novelty 的根本否定。** 建议作者增加 mechanism discussion，但不应将此升级为 must-fix。我维持此条为 should-fix。\n\n---\n\n### Should-Fix (Warning)\n\n**[AGREE] R2-W1: Item-related variance bundling 夸大 MC/FF 差异**\n\n与我的 N1 一致。R2 的量化更直接：bundled 差距 ~30pp，unbundled 仅 ~15pp。补充一点：从 Table 3 可验证，unbundled item_id 的 MC (34-38%) vs FF (17-24%) 分离同样成立（无重叠），因此 \"no overlap\" claim 在 unbundled 指标下也成立。但 bundling 确实放大了效果的视觉和叙事冲击力。\n\n---\n\n**[AGREE] R2-W2: 模型范围 7-9B 限制泛化性**\n\n与我的 W1 一致。补充：Section 4.6 的 Qwen 3B-9B scale validation 虽然确认了 item dominance 在 3B-9B 范围内的 scale-robustness，但 Limitations 已承认 \"larger models with higher accuracy could exhibit compressed item variance due to ceiling effects\"。D-study budgets 的具体数字（Table 4-5）确实不应被直接外推到 70B+ 模型。\n\n---\n\n**[AGREE] R2-W3: Binary scoring 作为 FF variance structure 混淆因素**\n\n这是 R2 提出的重要新视角，我在 Round 1 审稿中未充分展开（仅在 \"小问题\" 中建议增加 text-exact-match 讨论）。\n\nR2 的论点是 sound 的：binary scoring 将 FF 任务的 partial credit 信息（推理路径质量、中间步骤）压缩为 0/1，这可能是 FF 高 residual (40-44%) 的主要原因。Section 4.1 的 text-exact-match 结果（G 崩溃到 0.007, temperature 主导 79.7%）已经证明 scoring metric 根本性地改变 variance structure，支持 R2 的担忧。\n\n具体而言：\n- FF benchmarks 下，模型可能生成了正确的推理但因 minor formatting 差异被判 0——这部分 variance 被 binary scoring 归入 residual\n- 如果使用 partial credit scoring（0/0.5/1），FF 的 item variance share 可能上升（因为 partial credit 捕获了 item difficulty gradient），model×item 和 model×prompt 可能下降\n- 这意味着 format-associated gap 可能部分是 scoring-metric artifact，而非 format 的 intrinsic property\n\n**建议升级此条为 must-fix level**——至少需要在 Limitations 中明确 \"all conclusions are conditional on binary scoring; partial credit scoring may alter the FF variance structure and reduce the format-associated gap\"。这比我原本的建议（增加 1-2 句讨论）更强，但 R2 的论证说服了我。\n\n---\n\n**[AGREE] R2-W4: Exp-002 reduced crossing 验证仅限 MMLU**\n\n与我的 W2 一致。\n\n---\n\n**[AGREE] R2-W5: References 格式不完整**\n\n已从 references.bib 验证：\n- `varannot2025gtheory`：author 字段为 `{Anonymous}`（line 291），arXiv:2601.02370。如果这是他人的 anonymous preprint，bib 中写 Anonymous 是可接受的。但如果是作者自己的未发表工作，则违反 double-blind policy（ARR guidelines 要求 self-citation 使用第三人称且不 anonymize）。R2 的 flag 合理。\n- `wei2025gtheory`（line 17）、`xiao2025construct`（line 299）、`jin2025psychometrics`（line 307）：均使用 \"and others\" 代替完整 author list。虽然 arXiv preprints 有时确实 author 众多，但标准做法是列出所有作者或使用 \"et al.\" 格式，\"and others\" 不规范。\n- `kipnis2025metabench`（line 184-189）、`li2025atlas`（line 192-196）：确实缺少 URL 字段。\n\n这些是 minor formatting issues，但 varannot2025gtheory 的 double-blind 合规问题需要作者明确回应。\n\n---\n\n### Questions\n\n**[AGREE] R2-Q1: Partial/continuous scoring 对 FF variance structure 的影响**\n\n这是验证 W3 的 key experiment。Binary scoring 下的 FF variance structure 可能与 partial/rubric-based scoring 有质的不同。虽然超出当前稿件范围（需要全新评测 pipeline），但至少应作为 future work 明确提出，且当前结论应加 \"under binary scoring\" 的 scope qualifier。\n\n---\n\n**[REBUT] R2-Q2: high_school_mathematics 的 20 items 小样本问题**\n\nR2 关注 20 items 的小样本限制是合理的，但对证据链的解读不够完整。论文的核心证据不是单个 subject 的 anecdotal observation，而是 **10 个 subjects 上的 Spearman ρ=0.806 (p=0.005)**。这个 correlation 基于 10 个数据点（每个 subject 一个 item variance share 和一个 difficulty dispersion 值），统计功效虽有限但 p=0.005 在 n=10 下有意义。high_school_mathematics 是这个 trend 中的一个特别有说服力的 data point，但不是唯一证据。\n\n但我同意扩展到更多 borderline subjects 会 strengthen 此分析。具体建议：可以利用 MMLU 完整 57 subjects 的数据（而非仅 sample 的 10 个）做全量 correlation。\n\n---\n\n**[AGREE] R2-Q3: D-study budgets 的 out-of-sample validation**\n\nSection 4.7 的 3 个独立 200-item samples（CV=3.1%）和 Section 3.4 的 4-model subset prediction（predicted G=0.893 vs observed 0.896, Δ=0.003）提供了 within-design validation，但没有真正的 out-of-sample validation（如第 9 个模型、新 benchmark、不同时间点的数据）。这是 D-study contributions 的一个泛化性限制。\n\n---\n\n**[AGREE] R2-Q4: varannot2025gtheory double-blind 合规**\n\n从 bib 看 author 为 `{Anonymous}`，这要求作者在 rebuttal 中明确回应：(a) 这是他人的 anonymous preprint（则可接受）；还是 (b) 自己的工作以 anonymous 形式引用（则可能违反 ARR double-blind policy）。\n\n---\n\n### Missing References\n\nR2 建议补充 Gruber et al. (2024) 和 Wang et al. (2025)。我没有独立验证这两篇的具体内容，但从标题看：\n- Gruber et al. \"Towards Reproducible LLM Evaluation\" 与本文的 reproducibility budgets 直接相关，应引用\n- Wang et al. \"Benchmark2: Systematic Evaluation of LLM Benchmarks\" 提供 meta-benchmark 视角，relevant 但非 essential\n\n---\n\n### Director 指定的三个焦点问题\n\n**1. R2-N2 \"trivial explanation\"——MC response space constraint 是否是 sufficient explanation？**\n\n**不是 sufficient explanation，但是 partial mechanism，论文应讨论。** 如上述 REBUT 所述，within-MMLU 的 ρ=0.806 分析和 HellaSwag 反例否定了纯 tautological 解释。但 R2 正确指出了 MC constrained output space 降低 generation noise 的机制效应。论文的 \"item heterogeneity, not format per se\" 结论（Section 4.3 末句）实际上已经部分回应了此问题，但需要更 explicit 的 mechanistic discussion。\n\n**2. R2-W3 \"binary scoring 混淆\"——partial credit scoring 是否可能缩小 format gap？**\n\n**很可能会。** Binary scoring 对 FF 任务丢失信息量更大（MC 的 binary scoring 相对自然——选对就是对，FF 则丢失了推理路径质量差异）。Partial credit 会将目前归入 residual 的 variance 重新分配到 item 和 model×item components，可能提升 FF 的 item-related variance share，从而缩小 format gap。Section 4.1 的 text-exact-match 数据（scoring metric 改变完全颠覆 variance structure）为此提供了直接经验证据。R2 的担忧是有根据的，我已在上面建议升级此条的严重性。\n\n**3. Excitement 2.5 vs 3.5 的分歧**\n\nR2 给 Excitement 2.5/5，我给 3.5/5，差距 1.0。分歧的核心在于 R2 对 format-associated finding 的 novelty 判断。R2 认为如果 finding 是 \"tautological consequence\"，则 novelty 大幅降低（N2）。\n\n我的立场：\n- 即使 format finding 有 mechanistic explanation（部分同意 R2），**D-study budgets 和 toolkit 的实践 novelty 是独立的**。10× efficiency gain 的量化、cross-benchmark budget 表（Table 5），以及 IRT 与 G-theory 正交互补的展示（Table 4）——这些对 evaluation practitioners 有即时价值，novelty 不受 format mechanism 争议的影响。\n- R2 的 2.5 评分可能低估了 methodological novelty：本文是首个在 LLM evaluation 中实施如此规模（7 facets, 5 benchmarks, 2.3M records）的 G-theory 分析，且 robustness 验证达到了该子领域的新标准。\n- 但我也承认，如果读者主要关注 format finding 且接受 trivial explanation，Excitement 确实会打折扣。\n\n**我维持 3.5/5，但认为 R2 的 2.5/5 反映了对 format finding novelty 的不同判断，不是不合理的评估。** 如果需要 consensus，3.0/5 可能是两位 Reviewer 都能接受的折中。\n\n---\n\n### 汇总：两位 Reviewer 的共识与分歧\n\n**共识项（均 AGREE）：**\n- N1/R1-N2: format-associated claim 统计支撑不足（n=5, p=0.10）→ **Critical, must-fix**\n- W1/R1-N1: item-related bundling 夸大叙事 → **Critical/Warning, must-fix**\n- W2/R1-W1: model range 限制泛化性 → Warning\n- W4/R1-W2: reduced crossing 验证仅限 MMLU → Warning\n- W5: references 格式问题 → Minor\n\n**R2 新增、R1 同意：**\n- W3: binary scoring 作为 FF variance confound → **我建议升级为 must-fix level discussion**\n\n**分歧项：**\n- R2-N2 (trivial explanation): R2 判定为 critical/must-fix，我判定为 should-fix（有合理内核但 not tautological）\n- Excitement: R2 2.5 vs R1 3.5（核心分歧在于 format finding novelty）\n",
    "reviewer_id": "1",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-22T10:02:19.484158+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3918
}
```

</details>

---


### Assistant

_source line 272 · 2026-05-22T10:02:27.006004+00:00_

已提交对 Reviewer 2 的逐条回应。核心判断：

- **R2-N1（统计支撑不足）**：[AGREE]，与我的 N2 一致，两位 reviewer 达成共识
- **R2-N2（trivial explanation）**：[REBUT]——ρ=0.806 的 within-MMLU 分析和 HellaSwag 反例否定了纯 tautological 解释，但认同论文应增加 mechanistic discussion
- **R2-W1-W5**：除 W3 外均 [AGREE]；特别将 **W3（binary scoring confound）** 建议升级为 must-fix level，因为 text-exact-match 数据（Section 4.1）已直接证明 scoring metric 颠覆 variance structure
- **Excitement 分歧（2.5 vs 3.5）**：维持 3.5，因为 D-study budgets 和 toolkit 的实践 novelty 独立于 format finding 争议

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1"
}
```

</details>

---


## Round 9

## Round 9

92 recorded events


### User

_source line 273 · 2026-05-22T11:39:53.722037+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性与实验设计** 审查。

## Venue 信息
- **EMNLP 2026** via ACL Rolling Review (ARR)
- Double-blind review
- Long paper: 8 页正文限制（References 无限制，Limitations/Ethics 不计入页数）
- ACL 模板，[review] 选项
- Deadline: 2026-05-25

## 论文文件
- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/submitted.pdf`

## 你的审查重点

### 1. G-theory 方法学正确性
- Henderson Method I 用于 binary 0/1 数据是否合理？论文的辩护（probit simulation、REML comparison、null calibration）是否充分？
- 将 8 个 purposively selected models 当作 quasi-random facet 的理论依据是否站得住脚？leave-one-model-out 和 4-model subset 验证是否足够？
- "item-related variance" 将 item + model×item 捆绑报告——bundling 是否有坚实的心理测量学依据？是否存在过度聚合误导读者的风险？
- DIF（差异项目功能）的操作化定义——LLM 场景 vs 教育测量场景的语义差异处理是否得当？

### 2. 实验设计与统计推断
- exp-001（单模型 MMLU）到 exp-002（5 benchmark 跨模型）的设计缩减（3 precision → 1, 3 temp → 2）是否引入混淆？validation 是否充分？
- Format-associated claim 的统计功效：n=5 benchmarks, permutation p=0.10，item-level d=1.73 vs benchmark-level CI 跨零——论文对此的定位（descriptive observation vs confirmatory finding）是否恰当？
- DeepSeek MATH 排除（7/8 模型）对 variance components 的影响——LOMO 分析是否足以排除偏差？
- Bootstrap CI 方法：item-level resampling 是否 respect 了 stratified design？论文声称差异 <4% 是否可接受？
- D-study 投影的外推有效性：从 200 items 投影到 55 items 的可靠性？从 single-model 到 cross-model 的 transferability？

### 3. 精度可分离性
- BF16/FP16 "functionally interchangeable" 的 claim 基于 <0.1% interaction——在 binary scoring 下这是否已经 trivially 保证？（binary 粗粒度可能掩盖实际差异）
- text-exact-match G=0.007 的讨论——是否充分说明 binary scoring conditional 的边界？

### 4. 鲁棒性检查
- 8 项 robustness check 是否全面？是否遗漏了关键的 sensitivity analysis（如 item sampling strategy、few-shot example selection、model selection bias）？
- Scale validation 仅覆盖 3B-9B（Qwen2.5 家族内）——是否足以支撑 "scale-robust" 的 claim？

请给出结构化审稿意见：Summary → Strengths → Weaknesses（逐条，标注 severity: Must-Fix / Should-Fix / Minor）→ Questions → Missing References → Overall Assessment（评分 + 置信度）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-22T11:40:12.213349+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-22T11:40:12.264224+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-22T11:40:14.269459+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*review-reviewer-session-start*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*review-reviewer-session-start*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519"
  }
}
```

</details>

---


### Tool result

_source line 277 · 2026-05-22T11:40:14.321519+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 278 · 2026-05-22T11:40:16.229544+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start*",
  "path": "/home/ubuntu/agent-ml-research"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start*",
    "path": "/home/ubuntu/agent-ml-research"
  }
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-22T11:40:16.330236+00:00_

/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 280 · 2026-05-22T11:40:18.148008+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-22T11:40:18.199321+00:00_

1	---
2	name: review-reviewer-session-start
3	description: Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。
4	priority: 8
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 2
11	roles: []
12	---
13	
14	# Review Reviewer Session 启动流程
15	
16	执行顺序：
17	1. 读取论文文件（`projects/{project}/paper/main.tex` 或类似路径）
18	2. 检查论文格式状态：
19	   - 页数是否在 venue 要求内（若已知 venue）
20	   - LaTeX 是否可编译（调用 `ssh_execute` 运行 `pdflatex` 或 `latexmk`）
21	   - 图表是否有标题和标签
22	3. 视觉检查：如果已有编译好的 PDF，使用 `paper-visual-review` skill 渲染关键页面（首页、图表页、参考文献页），检查排版溢出、公式渲染、图表质量等视觉问题
23	4. 检查投稿材料清单：
24	   - cover letter 是否存在
25	   - 补充材料是否准备
26	   - 参考文献格式是否正确
27	5. 向 Review Director 汇报（`review_reviewer_post_to_director`）：
28	   - 论文当前状态
29	   - 发现的格式问题（如有）
30	   - 视觉检查结果（如有）
31	   - 缺少的材料（如有）
32	
33	此流程在 Review Director 分配任务后执行。
34	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-22T11:40:22.862317+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 283 · 2026-05-22T11:40:22.963110+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 284 · 2026-05-22T11:40:27.173658+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 285 · 2026-05-22T11:40:29.534099+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/submitted.pdf",
  "pages": "1-8",
  "project": "nlp_variance_gtheory",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/submitted.pdf",
    "pages": "1-8",
    "project": "nlp_variance_gtheory",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 286 · 2026-05-22T11:40:36.314745+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, I found information about ACL Rolling Review 2026 reviewer guidelines and review form criteria:

## Reviewer Guidelines

The reviewing workflow involves: (1) read the paper and get the first impression, (2) search for related work, not deliberately trying to find that particular submission. If you feel that you are qualified to review some aspects of the paper but not others (e.g., experimental results but not the formal proofs), please state in the review if you did not check some major parts, such 
…[truncated 1186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9141
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-22T11:40:37.421401+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 473.7}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 534.8}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 567.8}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 537.8}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 473.5}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 517.6}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 480.9}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 470.2}], \"total_pages\": 13, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images\"}, \"error\": null, \"metadata\": 
…[truncated 5 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7887
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-22T11:40:42.245299+00:00_

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
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
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

_source line 289 · 2026-05-22T11:40:42.350022+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 104
}
```

</details>

---


### Tool call

_source line 290 · 2026-05-22T11:40:46.511914+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form including all dimensions, rating scales, and criteria descriptions. I need the exact scoring scales for: Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other rated dimensions. Include the full text of each criterion description."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form including all dimensions, rating scales, and criteria descriptions. I need the exact scoring scales for: Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other rated dimensions. Include the full text of each criterion description."
  }
}
```

</details>

---


### Tool call

_source line 291 · 2026-05-22T11:40:48.181275+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/submitted.pdf",
  "pages": "9-13",
  "project": "nlp_variance_gtheory",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/submitted.pdf",
    "pages": "9-13",
    "project": "nlp_variance_gtheory",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-22T11:40:48.735064+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 293 · 2026-05-22T11:40:54.970596+00:00_

# ACL Rolling Review Form - Complete Scoring Scales

## Overall Assessment
**Scale: 1-5 (with half-point options)**

- **5**: "Consider for Award: I think this paper could be considered for an outstanding paper award"
- **4.5**: Borderline Award
- **4**: "Conference: I think this paper could be accepted to an *ACL conference"
- **3.5**: Borderline Conference
- **3**: "Findings: I think this paper could be accepted to the Findings of the ACL"
- **2.5**: Borderline Findings
- **2**: Resubmit next cycle for substantial revisions
- **1.5**: Resubmit after next cycle for substantial revisions
- **1**: "Do not resubmit: This paper has to be fully redone"

## Soundness
**Scale: 1-5 (with half-point options)**

- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: "Strong: This study provides sufficient support for all claims"
- **3**: "Acceptable: This study provides sufficient support for main claims"
- **2**: "Poor: Some main claims lack sufficient support"
- **1**: "Major Issues: This study is not yet sufficiently thorough"

## Excitement
**Scale: 1-5 (with half-point options)**

- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points to others"
- **2**: "Potentially Interesting: does not resonate with me personally"
- **1**: "Not Exciting: does not resonate with me, unlikely to with community"

## Reviewer Confidence
**Scale: 1-5**

- **5**: "Positive that my evaluation is correct; familiar with related work"
- **4**: "Quite sure; unlikely I missed something affecting ratings"
- **3**: "Pretty sure; good feel for area but didn't check details carefully"
- **2**: "Willing to defend evaluation; fairly likely I missed details"
- **1**: "Not my area, or paper very hard to understand"

## Reproducibility
**Scale: 1-5**

- **5**: "They could easily reproduce the results"
- **4**: "They could mostly reproduce results despite minor
…[truncated 830 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8458
}
```

</details>

---


### Tool result

_source line 294 · 2026-05-22T11:40:56.231326+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 563.3}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 609.4}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 517.2}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 422.0}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 289.7}], \"total_pages\": 13, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 8050
}
```

</details>

---


### Tool result

_source line 295 · 2026-05-22T11:40:57.037380+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 8302
}
```

</details>

---


### Tool call

_source line 296 · 2026-05-22T11:41:02.556201+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 297 · 2026-05-22T11:41:03.109458+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 298 · 2026-05-22T11:41:03.513961+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 957
}
```

</details>

---


### Tool call

_source line 299 · 2026-05-22T11:41:03.516609+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-22T11:41:04.275280+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 301 · 2026-05-22T11:41:04.678371+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1568
}
```

</details>

---


### Tool result

_source line 302 · 2026-05-22T11:41:05.690357+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2173
}
```

</details>

---


### Tool result

_source line 303 · 2026-05-22T11:41:06.509322+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2234
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-22T11:41:10.435305+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 305 · 2026-05-22T11:41:11.465749+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 306 · 2026-05-22T11:41:11.819209+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-22T11:41:12.728019+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2292
}
```

</details>

---


### Tool result

_source line 308 · 2026-05-22T11:41:14.488196+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3022
}
```

</details>

---


### Tool result

_source line 309 · 2026-05-22T11:41:14.842195+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3022
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-22T11:41:19.320480+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 311 · 2026-05-22T11:41:20.123439+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 802
}
```

</details>

---


### Tool call

_source line 312 · 2026-05-22T11:41:20.274186+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-22T11:41:20.575515+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 314 · 2026-05-22T11:41:20.676513+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 315 · 2026-05-22T11:41:21.078989+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 316 · 2026-05-22T11:41:21.229866+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-22T11:41:21.581259+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 318 · 2026-05-22T11:41:21.581700+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 319 · 2026-05-22T11:41:21.632527+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-22T11:41:31.315920+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "submitted_p*.png",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "submitted_p*.png",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-22T11:41:31.316330+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-22T11:41:35.031430+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "List PDF image directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
    "description": "List PDF image directory"
  }
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-22T11:41:35.182296+00:00_

submitted_p10.png
submitted_p11.png
submitted_p12.png
submitted_p13.png
submitted_p9.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-22T11:41:38.047616+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "realpath /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p9.png",
  "description": "Get real path of page 9 image"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "realpath /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p9.png",
    "description": "Get real path of page 9 image"
  }
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-22T11:41:38.148291+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images/submitted_p9.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-22T11:41:42.367649+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/submitted.pdf",
  "pages": "9-13",
  "project": "nlp_variance_gtheory",
  "dpi": "150",
  "output_dir": "/tmp/nlp_review_pages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/submitted.pdf",
    "pages": "9-13",
    "project": "nlp_variance_gtheory",
    "dpi": "150",
    "output_dir": "/tmp/nlp_review_pages"
  }
}
```

</details>

---


### Tool result

_source line 327 · 2026-05-22T11:41:43.021891+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/tmp/nlp_review_pages/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 563.3}, {\"page\": 10, \"path\": \"/tmp/nlp_review_pages/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 609.4}, {\"page\": 11, \"path\": \"/tmp/nlp_review_pages/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 517.2}, {\"page\": 12, \"path\": \"/tmp/nlp_review_pages/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 422.0}, {\"page\": 13, \"path\": \"/tmp/nlp_review_pages/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 289.7}], \"total_pages\": 13, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/tmp/nlp_review_pages\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 654
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-22T11:41:46.095925+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/nlp_review_pages/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/nlp_review_pages/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 329 · 2026-05-22T11:41:46.096252+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/nlp_review_pages/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/nlp_review_pages/submitted_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-22T11:41:46.971755+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/nlp_review_pages/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/nlp_review_pages/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 331 · 2026-05-22T11:41:47.272811+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/nlp_review_pages/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/nlp_review_pages/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 332 · 2026-05-22T11:41:47.273238+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/nlp_review_pages/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/nlp_review_pages/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-22T11:41:48.781975+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2686
}
```

</details>

---


### Tool result

_source line 334 · 2026-05-22T11:41:48.984196+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2887
}
```

</details>

---


### Tool result

_source line 335 · 2026-05-22T11:41:49.239523+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1966
}
```

</details>

---


### Tool result

_source line 336 · 2026-05-22T11:41:49.693896+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2722
}
```

</details>

---


### Tool result

_source line 337 · 2026-05-22T11:41:49.797328+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2524
}
```

</details>

---


### Tool call

_source line 338 · 2026-05-22T11:43:35.258218+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 339 · 2026-05-22T11:43:35.309027+00:00_

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
11	\usepackage{graphicx}
12	\usepackage{amsmath,amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{xcolor}
16	
17	\graphicspath{{../../figures/paper/}}
18	
19	\title{Reproducibility Budgets for Open-Weight LLM Evaluation:\\A Generalizability Theory Analysis}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	\input{abstract}
28	\end{abstract}
29	
30	% === INTRODUCTION ===
31	\input{introduction}
32	
33	% === RELATED WORK ===
34	\input{related_work}
35	
36	% === METHOD ===
37	\input{method}
38	
39	% === EXPERIMENTS ===
40	\input{experiments}
41	
42	% === CONCLUSION ===
43	\input{conclusion}
44	
45	% === LIMITATIONS ===
46	\input{limitations}
47	
48	\bibliography{references}
49	
50	% === APPENDIX ===
51	\input{appendix}
52	
53	\end{document}
54	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-22T11:43:38.423449+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/*.tex",
  "description": "List all LaTeX source files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/*.tex",
    "description": "List all LaTeX source files"
  }
}
```

</details>

---


### Tool result

_source line 341 · 2026-05-22T11:43:38.474139+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-22T11:43:40.983853+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-22T11:43:41.435657+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Generalizability Theory}
5	\label{sec:gtheory}
6	
7	Generalizability theory (G-theory) treats each measurement as one observation from a universe of admissible conditions defined by the crossed facets of an evaluation design \cite{shavelson1991generalizability, brennan2001generalizability}. The \emph{object of measurement} is the entity whose consistency is of interest. In our setting, test items ($p$) serve as the object of measurement, and the goal is to determine how reliably item-level scores generalize across the methodological conditions under which they are collected.
8	
9	A \emph{G-study} decomposes total observed variance into components $\sigma^2_x$ for each facet $x$ and their interactions. Each component quantifies how much variability that source contributes to the overall measurement. Large interaction components (e.g., $\sigma^2_{pM}$ for item-by-model) indicate that facets do not affect items uniformly but instead create differential difficulty profiles. We estimate variance components via Henderson Method~I, an unbiased ANOVA-based estimator for balanced designs \cite[Ch.~3]{brennan2001generalizability}, with 1,000-resample bootstrap confidence intervals (item-level resampling with replacement, preserving the fully-crossed structure across all other facets) \cite{li2023bootstrap}.
10	
11	A \emph{D-study} projects the generalizability coefficient under hypothetical designs with different numbers of conditions per facet:
12	\begin{equation}
13	G_\text{item} = \frac{\sigma^2_p}{\sigma^2_p + \sigma^2_\text{rel}}
14	\label{eq:gcoeff}
15	\end{equation}
16	where $\sigma^2_\text{rel}$ aggregates all item-by-facet interaction variances, each divided by the number of conditions for the corresponding facets \cite[Ch.~4]{brennan2001generalizability}. This prospective capability distinguishes G-theory from classical ANOVA: rather than only attributing variance post hoc, a D-study enables optimization of ev
…[truncated 9103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-22T11:43:41.436051+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-22T11:43:41.787192+00:00_

1	\section{Experiments}
2	
3	All experiments use open-weight 7--9B parameter models evaluated with vLLM~0.9.2 on a single NVIDIA RTX PRO 6000 GPU (96GB) with binary correctness scoring.
4	
5	\subsection{Single-Model Baseline}
6	
7	We first establish the variance structure within a single model (Llama-3.1-8B-Instruct) on MMLU to isolate methodological facet contributions before introducing cross-model variation.
8	
9	\paragraph{Design.} The G-study crosses six facets: 200 items $\times$ 3 numerical precisions (BF16, FP16, FP32) $\times$ 6 prompt templates $\times$ 6 random seeds $\times$ 3 temperature levels (0.0, 0.3, 0.7) $\times$ 4 answer orderings, yielding 259,200 binary observations. Variance components are estimated via Henderson Method~I with bootstrap confidence intervals (1,000 resamples).
10	
11	\paragraph{Results.} Under binary scoring, item difficulty (\texttt{item\_id}) accounts for 58.4\% of total variance, with the residual term contributing 23.1\%. All main facet effects are negligible ($<$1\% each): precision 0.9\%, prompt template, temperature, seed, and ordering each $<$0.5\%. The interesting structure appears in item-conditional interactions: prompt$\times$item is the largest at 5.5\%, followed by seed$\times$item (4.7\%), precision$\times$item (3.3\%), temperature$\times$item (2.9\%), and ordering$\times$item (0.8\%). This pattern indicates that methodological choices do not shift performance uniformly across items; instead, specific items are differentially sensitive to specific facets---prompt template variation produces the largest item-conditional effect.
12	
13	The resulting generalizability coefficient is $G_\text{item} = 0.936$, indicating that 200 items under multi-facet conditions produce highly reliable rankings. A D-study projection shows $G \geq 0.80$ is achievable with as few as 55 items in this multi-facet design.
14	
15	For text-exact-match scoring (requiring verbatim string matches), the variance structure shifts dramatically: te
…[truncated 12648 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-22T11:43:41.837731+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-22T11:43:41.938591+00:00_

1	\appendix
2	\section{Additional Robustness Analyses}
3	\label{app:robustness}
4	
5	We report eight robustness analyses that verify the stability of the variance decomposition under alternative analytical choices.
6	
7	\paragraph{GLMM complement.} A generalized linear mixed model (GLMM) with marginal logit link produces variance component rankings that perfectly preserve all seven grouped component orderings ($\rho = 1.0$) relative to Henderson Method~I \cite{jiang2018bayesian, tuerlinckx2006glmm}. This confirms that the linear variance decomposition is robust to the binary outcome distribution.
8	
9	\paragraph{Accuracy-range stability.} The \texttt{item\_id} variance share remains stable across subsets with mean accuracy from 0.62 to 0.72 ($r = -0.048$). This rules out distortion from binary floor or ceiling effects at observed accuracy levels.
10	
11	\paragraph{Estimator robustness.} We compare Henderson Method~I with restricted maximum likelihood (REML-EM, 500 iterations, practical convergence $\Delta < 0.003$ percentage points). All variance components differ by $<$0.5 percentage points between estimators. The largest discrepancy occurs on the residual component (0.47pp); all substantive components (item, model$\times$item, model) differ by $<$0.3pp. Henderson Method~I is preferred for our balanced designs because it produces unbiased estimates without distributional assumptions \cite[Ch.~12]{brennan2001generalizability}.
12	
13	\paragraph{CI method comparison.} Bootstrap (1,000 item-level resamples with replacement) and delete-1 jackknife confidence intervals agree closely: width ratios range from 0.96 to 1.04 across all variance components. The agreement indicates that the dependence structure introduced by item-level bootstrap resampling (which creates $\sim$127 unique items per 200-item resample) does not materially distort interval estimates. Stratified resampling by subject (10 subjects $\times$ 20 items) produces CIs within 4\% of simple item-level boots
…[truncated 12177 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-22T11:43:46.806431+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 349 · 2026-05-22T11:43:47.160608+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	On multiple-choice benchmarks, item selection drives 34--38\% of evaluation variance while prompt wording is negligible ($<$3\%). On the free-form reasoning task GSM8K, the structure shifts: model$\times$prompt interaction alone accounts for approximately 9\%, while item selection drops to 17\%. These numbers, drawn from our factorial analysis of approximately 2.3 million evaluation records across five benchmarks, reveal that the variance structure of LLM evaluation is not a fixed property of the pipeline but shifts qualitatively with the response format. Current evaluation practice treats variance sources as independent nuisance factors and controls them one at a time: one study perturbs prompts, another varies precision, a third changes item subsets. This piecemeal approach cannot capture interactions between sources, nor can it predict how the relative importance of each source changes across evaluation settings. Leaderboard rankings built on single-condition evaluations are therefore sensitive to methodological choices that remain unreported and uncontrolled \citep{rodriguez2021leaderboards, dehghani2021benchmark}. No unified factorial framework exists to decompose these sources simultaneously, quantify their interactions, and compare the resulting variance structure across benchmarks.
5	
6	Existing studies examine individual variance sources in isolation. \citet{sclar2024formatting} and BrittleBench \citep{brittlebench2026} documented 50--76\% accuracy swings from prompt formatting; \citet{yuan2025layercast} showed up to 9\% variation from numerical precision; \citet{pezeshkpour2024ordering}, \citet{dodge2020finetuning}, and \citet{henderson2018deep} documented ordering and hyperparameter sensitivity---each holding other factors fixed. \citet{messing2026hidden} applied G-theory to LLM evaluation across five methodology facets on a single benchmark (judge identity: 43.8\%), but excluded infrastructure face
…[truncated 3592 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 354
}
```

</details>

---


### Tool call

_source line 350 · 2026-05-22T11:43:47.311513+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 351 · 2026-05-22T11:43:47.362000+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Our findings are bounded by four scope constraints. First, the cross-model analysis covers eight open-weight 7--9B instruction-tuned models; within-family validation extends to 3B--9B (Qwen2.5), but results do not generalize to API-based, base, or $>$9B models. Second, all experiments run on single-GPU inference; multi-GPU tensor parallelism introduces additional numerical non-associativity not captured here. Third, the benchmark sample ($n = 5$) provides well-powered item-level patterns but limited statistical power for the format-associated claim ($p = 0.10$, permutation test); other formats (code generation, multi-turn dialogue) may differ. Fourth, binary scoring may understate format differences---partial-credit scoring could redistribute FF residual variance (40--44\%) to item or model$\times$item components, narrowing the gap.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 352 · 2026-05-22T11:43:47.412551+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 353 · 2026-05-22T11:43:47.463076+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Multi-facet designs require 10$\times$ fewer items than single-condition designs for $G \geq 0.80$ (55 vs.\ 552), confirmed across all five benchmarks (bootstrap CIs exceed 10$\times$); FF benchmarks show nearly double the gain ($\sim$21$\times$ vs.\ $\sim$12$\times$ for MC). We also observe a format-associated variance pattern: item-related variance concentrates at 68--72\% on MC benchmarks and disperses to 31--41\% on FF benchmarks---a descriptive observation whose confirmatory generalization requires additional benchmarks. BF16 and FP16 are interchangeable under binary scoring. Code, data, and D-study budget calculator will be released upon publication.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 354 · 2026-05-22T11:43:52.560528+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-22T11:43:52.561047+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Variance Decomposition in ML/NLP Evaluation.}
5	Factorial decomposition of evaluation variance has roots in the ML reproducibility literature. \citet{bouthillier2021accounting} introduced an ANOVA-based template that decomposes benchmark variance across implementation details, hyperparameters, and data splits, establishing that design choices account for a substantial share of reproducibility failures. Several subsequent studies applied similar decomposition logic to specific facets of model evaluation \citep{dodge2020finetuning, henderson2018deep, magnusson2023reproducibility}. \citet{messing2026hidden} brought Generalizability theory into LLM evaluation, decomposing variance across five methodology facets on a single benchmark; judge identity dominated at 43.8\%, with prompt$\times$judge interaction at 12.4\%. However, this study used a single benchmark, included no infrastructure facets such as numerical precision, and fixed the judge as an LLM evaluator rather than isolating other sources. \citet{madaan2024quantifying} proposed per-factor variance metrics for LLM evaluation benchmarks but did not cross factors simultaneously. \citet{blackwell2024towards} quantified uncertainty in benchmark scores, and \citet{qian2026benchmark} conducted systematic meta-evaluation of LLM benchmarks; \citet{burnell2023rethink} called for rethinking evaluation reporting standards in AI. Recently, G-theory has been applied to LLM-based writing assessment \citep{wei2025gtheory} and annotation reliability \citep{varannot2025gtheory}, but these studies address scoring consistency rather than benchmark evaluation variance. \citet{kunievsky2025intent} proposed an alternative decomposition that separates intent uncertainty, articulation variance, and model uncertainty, but this framework does not cross infrastructure and methodology facets in a factorial design. Our work extends these approaches by crossing seven facets across
…[truncated 3417 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 356 · 2026-05-22T11:49:17.353710+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 审稿意见：方法严谨性与实验设计\n\n**论文标题**: Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Analysis\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 方法框架选择正确、实验规模可观、robustness 检查到位，但两大核心贡献分别存在统计功效不足和跨benchmark验证缺失的问题，需要补充才能支撑其主张的 generalizability。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心方法学正确，8 项 robustness check 系统且可信；但 format-associated claim 统计功效先天不足（p=0.10 为分辨率下限），D-study budget 的跨 benchmark 验证仅限 MMLU |\n| Excitement | 3.5/5 | G-theory 应用于 LLM evaluation 的时机好，reproducibility budget 有直接实践价值；但对熟悉心理测量学的读者来说方法论迁移较为直接，novelty 主要在应用层面 |\n| Reproducibility | 4/5 | 设计矩阵、facet 定义、prompt 模板（Appendix E）描述清晰；承诺释放代码和 D-study calculator；vLLM 版本和 GPU 型号均已说明 |\n| Confidence | 4/5 | 熟悉 G-theory、IRT 和 LLM evaluation methodology，仔细审查了方法学和统计推断 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **Format-associated claim 在 Abstract/Contributions 中的突出程度与统计支撑不匹配**\n- 具体位置：Abstract 第 1 句、Section 1 Contribution #2、Section 4.3 全节\n- 问题：n=5 benchmarks（3 MC, 2 FF），exhaustive permutation test 仅有 C(5,3)=10 种分割方式，p=0.10 是理论分辨率下限——无论效应多大，在 α=0.05 下都不可能拒绝零假设。Benchmark-level CI 跨零 [-1.7, 5.1]（Section 4.3）。论文在正文中确实将其定位为 \"descriptive observation with strong item-level support\"，但 Abstract 开头 (\"On multiple-choice benchmarks, item selection drives 34–38% of evaluation variance while prompt wording is negligible\") 以及 Contributions #2 的表述给读者的第一印象是 confirmatory finding。item-level d=1.73 虽大，但操作在不同分析层级（within-benchmark），不能弥补 benchmark-level 的功效缺口。\n- 为什么影响接收：这是论文的第二大贡献。如果该 claim 在读者心中的权重超过其统计基础能承受的范围，论文的可信度会受损。\n- 建议修改方向：(a) Abstract 和 Contributions 中明确标注 \"descriptive/exploratory\" 性质，例如 \"We observe a format-associated pattern (n=5; not confirmatory)\"；(b) 考虑将 Contribution #2 降级为 observation 而非 parallel contribution；(c) 补充 2–3 个 benchmark（如 HumanEval、TruthfulQA、WinoGrande）即可将 permutation 分辨率提升至 p<0.05。\n\n**N2** [critical] **D-study budget 的跨 benchmark/跨 item-sample 验证仅限 MMLU**\n- 具体位置：Section 4.7（3 independent 200-item MMLU samples, CV=3.1%）、Appendix B Table 6（5 benchmarks 的 cross-model D-study projections）\n- 问题：论文的第一大贡献——\"multi-facet designs require 10× fewer items\"——在 MMLU 上有三组独立 200-item 样本的交叉验证（item difficulty variance shares: 73.2%, 72.6%, 69.0%），但 ARC、HellaSwag、GSM8K、MATH 的方差成分均来自单个 200-item 样本，无 cross-sample 稳定性验证。Table 6 中这四个 benchmark 的 D-study projections（如 GSM8K 需 128 items for G≥0.80）完全依赖于该单一样本的方差分解。考虑到 FF benchmarks 的 residual 高达 40–44%，方差成分可能对 item 抽样更敏感。\n- 为什么影响接收：这是论文最强的实践贡献（practitioners 直接使用的 budget recommendations），但 4/5 benchmarks 的推荐缺乏 out-of-sample 支撑。\n- 建议修改方向：至少对 1 个 MC benchmark（如 ARC）和 1 个 FF benchmark（如 GSM8K）追加 2–3 组独立 item 样本的方差分解，报告 CV。如果资源受限，至少报告 bootstrap item-resample 的 D-study projection variability（已有 bootstrap CI，但需明确展示 n_{G≥0.80} 的 CI 而非仅 G 值的 CI）。\n\n**N3** [critical] **Binary scoring 粒度对 \"item dominance\" 和 \"precision interchangeability\" 的系统性偏置讨论不充分**\n- 具体位置：Section 4.1, Section 4.4, Table 2\n- 问题：Binary 0/1 是最粗粒度的评分方式。在此粒度下：(a) 任何影响 logit 但不足以翻转 binary decision 的方差源都会表现为 negligible——precision 的 <0.1% interaction 可能反映的是 binary scoring 的测量灵敏度不足而非真正的等价性；(b) item difficulty 天然主导，因为一致性地 easy/hard 的 items 在所有 conditions 下都稳定产出 1/0，而其他方差源的效应被压缩进 25% 的 residual（Table 2）。text-exact-match 对比（G=0.007 vs G=0.936）是论文自身提供的最佳证据：评分粒度根本性地重塑了方差结构。但论文将此视为一个独立发现（Contribution #3 的\"metric-conditional\"caveats），而非系统性地影响所有 findings 的 measurement confound。\n- 为什么影响接收：读者可能将 \"BF16≈FP16\" 解读为通用结论，而非 binary-scoring-conditional 结论。item dominance 的绝对量级（58.4%, 37.9%）在更细粒度评分下可能显著降低。\n- 建议修改方向：在 Section 3.5 或 Section 4.1 开头增加一段系统性讨论 binary scoring 的 measurement resolution confound：明确所有后续发现（包括 item dominance、precision interchangeability、D-study budgets）都是 \"conditional on binary correctness scoring\" 这一前提的推论，而非关于 LLM evaluation variance 的一般性结论。当前的 metric-conditionality 讨论散布在各节中，缺乏统一框架。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **Quasi-random model facet 的 exchangeability 论证不完整**\n- 具体位置：Section 3.6, Appendix A (LOMO)\n- 问题：G-theory 要求 facet levels 从 universe 中（至少近似）随机抽样。论文将 8 个 purposively 选择的模型视为 quasi-random facet，universe 定义为 \"open-weight 7–9B instruction-tuned models from six architecture families\"。LOMO（item_id: 36–41%, G: 0.877–0.889）和 4-model subset（ΔG=0.003）证明了**内部稳定性**，但不能证明**代表性**——换一批同 universe 的 8 个模型是否会产生相似的方差分解？这些模型共享 2024–2025 训练范式（类似的 RLHF/DPO 策略、相似的数据混合），可能存在 temporal correlation 违反 exchangeability。\n- 建议：明确讨论 purposive selection 的局限性；报告 8 个模型间的 pairwise agreement（如 Cohen's κ 分布），展示它们是否确实构成 \"diverse\" 样本；或引用 G-theory 中关于 purposive facet 的理论文献加以辩护。\n\n**W2** [warning] **exp-001 → exp-002 的 design reduction 的 cross-benchmark 验证缺失**\n- 具体位置：Section 3.3, Appendix A (Reduced crossing validation)\n- 问题：exp-001 用 3 precisions × 3 temps，exp-002 缩减为 1 precision × 2 temps。Appendix 的 reduced crossing validation（ΔG=0.0008）是在 **MMLU** 数据的 subset 上进行的，但该缩减实际应用于 4 个新 benchmark。如果 precision×benchmark 或 precision×format 存在 interaction（论文只在 MMLU 上检查了 precision），则在 FF benchmarks 上去除 precision facet 可能产生不同的 confounding。\n- 建议：至少讨论 \"reduced crossing validation 仅在 MMLU 上执行\" 的局限，或提供 1 个非 MMLU benchmark 的 validation。\n\n**W3** [warning] **Scale validation 范围过窄但语言过强**\n- 具体位置：Section 4.6\n- 问题：\"item dominance is scale-robust\" 仅基于 Qwen2.5 家族内的 3B 和 7B 两个规模。这是单一模型家族内的 2 个数据点，不足以支撑 \"scale-robust\" 的一般性语言。2-model crossed design 的 G=0.71 本身确认了 2 个模型不够——但这也意味着跨规模的 G-theory 分析需要更多模型参与。\n- 建议：将 \"scale-robust\" 改为 \"scale-consistent within the Qwen2.5 3B–7B range\"；在 Limitations 中明确 70B+ 和跨家族的 scale validation 是 open question。\n\n**W4** [warning] **Probit simulation ρ=0.732 对 Henderson Method I 的支撑力度中等偏弱**\n- 具体位置：Section 3.5\n- 问题：ρ=0.732 意味着 binary 和 continuous rankings 之间约 46% 的方差不共享。论文用其他 4 个分析（GLMM ρ=1.0、REML <0.5pp、null calibration、accuracy-range stability）来补偿，整体证据链尚可。但 ρ=0.732 作为**第一个报告的**验证指标，会给读者留下负面第一印象。\n- 建议：重新组织验证顺序——先报告 GLMM（rank preservation ρ=1.0）和 REML（<0.5pp），再将 probit simulation 作为 supplementary evidence，并明确说明 ρ=0.732 反映的是 binary scoring 的 information loss 而非 Henderson Method I 的估计偏差。\n\n**W5** [warning] **Missing sensitivity analysis: few-shot example selection**\n- 具体位置：Section 3.2\n- 问题：论文变化了 few-shot examples 的**排列顺序**（4 orderings），但没有变化**哪些 examples 被选中**。Example selection 是已知的方差源（Pezeshkpour & Hrushcka 2024 已讨论），遗漏此 facet 可能导致 underestimation of prompt-related variance。\n- 建议：在 Limitations 中补充讨论，或追加一个 pilot analysis 比较不同 example sets 的方差影响。\n\n---\n\n## 小问题（不影响接收）\n\n- Section 4.6: \"with G = 0.963 and 0.956 respectively\" — PDF 渲染中 \"0.956\" 的 \"9\" 和 \"5\" 在某些分辨率下不易区分，建议检查 LaTeX 中数字的精确性。\n- Table 3 中 \"prompt\" 列对 MC 和 FF 有不同含义（prompt×item vs prompt main effect），表注已说明但容易被忽略。建议用不同列名（如 \"prmpt×item\" vs \"prompt\"）更直观。\n- Section 3.3 提到 ordering facet 对非 MMLU benchmarks \"structurally inert (σ²=0 by construction)\"，但 Table 1 仍将其列为 exp-002 的 facet（4 levels）。虽然数学上不影响 G_item，但可能让读者误以为 ordering 在所有 benchmarks 上都是 informative facet。\n- Appendix D Figure 4 的 x 轴标签 \"std(p_i)\" 应在 caption 中更明确地定义（标准差是跨 models 还是跨 conditions？）。\n- Abstract 称 \"approximately 2.3 million evaluation records\"，但 exp-001 (460,800) + exp-002 (2,304,000) = 2,764,800。\"2.3 million\" 似乎只指 exp-002。建议明确说明是 \"2.3 million in the cross-benchmark analysis\" 还是 \"approximately 2.8 million total\"。\n\n---\n\n## 主要优势\n\n1. **框架选择正确且应用系统**：G-theory 是解决 \"LLM evaluation 中方差来自哪里\" 这一问题的 canonical 工具。论文将其从教育测量成功迁移到 LLM evaluation，crossing 7 facets × 5 benchmarks × 8 models，实验规模在同类工作中最大。与 Messing (2026) 的 single-benchmark 设计和 Madaan et al. (2024) 的 per-factor 方法相比，本文的 factorial crossing 能估计 interaction terms——这是理解方差结构的关键。\n\n2. **Robustness checking 达到顶会水准**：8 项独立检查（GLMM complement、accuracy-range stability、REML comparison、CI method comparison、facet specification sensitivity、LOMO、null calibration、reduced crossing validation）构成了系统的证据链。特别是 null calibration 清晰排除了 Bernoulli p(1-p) artifact（0.08% vs 58.4%），LOMO 的 |ΔG|<0.02 跨 4 个 benchmark 展示了方差分解的模型稳定性。\n\n3. **统计报告诚实透明**：format-associated claim 明确标注 p=0.10 permutation floor 和 benchmark-level CI spanning zero；precision interchangeability 明确标注 metric-conditionality；D-study budgets 提供 bootstrap CI。论文没有 overclaim——这在 LLM evaluation 领域难能可贵。\n\n4. **实践工具价值高**：D-study budget table（Table 4 + Appendix B Table 6）和 intermediate design gradient（Appendix C Table 7）提供了直接可操作的指导。\"3 prompts × 3 seeds\" 作为 minimal sufficient upgrade（G: 0.592→0.766, 成本 9×）的推荐尤其实用。\n\n5. **IRT 互补性论证有力**：Table 4 将 Zhou et al. (2026) 的 IRT-selected 116 items 放入 multi-facet design（G: 0.457→0.895），优雅地展示了 item selection（IRT）和 condition optimization（G-theory）的正交互补性。\n\n---\n\n## Missing References\n\n- Holland, P.W. & Wainer, H. (1993). *Differential Item Functioning*. Lawrence Erlbaum. — DIF 在教育测量中的经典参考文献，论文讨论 DIF 语义差异时可引用。\n- Clauser, B.E. & Mazor, K.M. (1998). Using Statistical Procedures to Identify Differentially Functioning Test Items. *Educational Measurement*. — 补充 DIF 操作化的教育测量背景。\n- Webb, N.M., Shavelson, R.J., & Haertel, E.H. (2006). Reliability Coefficients and Generalizability Theory. *Handbook of Statistics*. — G-theory 关于 random vs fixed facet 分类的讨论，可支撑 quasi-random facet 论证。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 (Borderline Conference)\n**置信度**: 4/5\n\n**理由**: 论文将 G-theory 系统应用于 LLM evaluation variance decomposition，实验设计严谨，robustness 检查全面，统计报告诚实。核心贡献（multi-facet design 的 10× 效率增益）在 MMLU 上有良好支撑。但三个方法学问题共同削弱了 generalizability claim 的说服力：(1) format-associated pattern 作为主要贡献被突出呈现，但 n=5 的统计功效先天不足；(2) D-study budget 推荐对 4/5 benchmarks 缺乏 cross-sample 验证；(3) binary scoring confound 对所有 findings 的系统性影响未被充分讨论为统一框架。如果 N1（重新调整 format claim 的呈现层级）和 N2（至少补充 1–2 个 benchmark 的 cross-sample validation）在 revision 中得到解决，论文可以达到 4.0 (Conference)。当前版本在方法学 execution 上是扎实的，但 evidence-to-claim 的匹配在最广泛的主张上存在缺口。",
  "reviewer_id": "1",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 审稿意见：方法严谨性与实验设计\n\n**论文标题**: Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Analysis\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 方法框架选择正确、实验规模可观、robustness 检查到位，但两大核心贡献分别存在统计功效不足和跨benchmark验证缺失的问题，需要补充才能支撑其主张的 generalizability。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 核心方法学正确，8 项 robustness check 系统且可信；但 format-associated claim 统计功效先天不足（p=0.10 为分辨率下限），D-study budget 的跨 benchmark 验证仅限 MMLU |\n| Excitement | 3.5/5 | G-theory 应用于 LLM evaluation 的时机好，reproducibility budget 有直接实践价值；但对熟悉心理测量学的读者来说方法论迁移较为直接，novelty 主要在应用层面 |\n| Reproducibility | 4/5 | 设计矩阵、facet 定义、prompt 模板（Appendix E）描述清晰；承诺释放代码和 D-study calculator；vLLM 版本和 GPU 型号均已说明 |\n| Confidence | 4/5 | 熟悉 G-theory、IRT 和 LLM evaluation methodology，仔细审查了方法学和统计推断 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **Format-associated claim 在 Abstract/Contributions 中的突出程度与统计支撑不匹配**\n- 具体位置：Abstract 第 1 句、Section 1 Contribution #2、Section 4.3 全节\n- 问题：n=5 benchmarks（3 MC, 2 FF），exhaustive permutation test 仅有 C(5,3)=10 种分割方式，p=0.10 是理论分辨率下限——无论效应多大，在 α=0.05 下都不可能拒绝零假设。Benchmark-level CI 跨零 [-1.7, 5.1]（Section 4.3）。论文在正文中确实将其定位为 \"descriptive observation with strong item-level support\"，但 Abstract 开头 (\"On multiple-choice benchmarks, item selection drives 34–38% of evaluation variance while prompt wording is negligible\") 以及 Contributions #2 的表述给读者的第一印象是 confirmatory finding。item-level d=1.73 虽大，但操作在不同分析层级（within-benchmark），不能弥补 benchmark-level 的功效缺口。\n- 为什么影响接收：这是论文的第二大贡献。如果该 claim 在读者心中的权重超过其统计基础能承受的范围，论文的可信度会受损。\n- 建议修改方向：(a) Abstract 和 Contributions 中明确标注 \"descriptive/exploratory\" 性质，例如 \"We observe a format-associated pattern (n=5; not confirmatory)\"；(b) 考虑将 Contribution #2 降级为 observation 而非 parallel contribution；(c) 补充 2–3 个 benchmark（如 HumanEval、TruthfulQA、WinoGrande）即可将 permutation 分辨率提升至 p<0.05。\n\n**N2** [critical] **D-study budget 的跨 benchmark/跨 item-sample 验证仅限 MMLU**\n- 具体位置：Section 4.7（3 independent 200-item MMLU samples, CV=3.1%）、Appendix B Table 6（5 benchmarks 的 cross-model D-study projections）\n- 问题：论文的第一大贡献——\"multi-facet designs require 10× fewer items\"——在 MMLU 上有三组独立 200-item 样本的交叉验证（item difficulty variance shares: 73.2%, 72.6%, 69.0%），但 ARC、HellaSwag、GSM8K、MATH 的方差成分均来自单个 200-item 样本，无 cross-sample 稳定性验证。Table 6 中这四个 benchmark 的 D-study projections（如 GSM8K 需 128 items for G≥0.80）完全依赖于该单一样本的方差分解。考虑到 FF benchmarks 的 residual 高达 40–44%，方差成分可能对 item 抽样更敏感。\n- 为什么影响接收：这是论文最强的实践贡献（practitioners 直接使用的 budget recommendations），但 4/5 benchmarks 的推荐缺乏 out-of-sample 支撑。\n- 建议修改方向：至少对 1 个 MC benchmark（如 ARC）和 1 个 FF benchmark（如 GSM8K）追加 2–3 组独立 item 样本的方差分解，报告 CV。如果资源受限，至少报告 bootstrap item-resample 的 D-study projection variability（已有 bootstrap CI，但需明确展示 n_{G≥0.80} 的 CI 而非仅 G 值的 CI）。\n\n**N3** [critical] **Binary scoring 粒度对 \"item dominance\" 和 \"precision interchangeability\" 的系统性偏置讨论不充分**\n- 具体位置：Section 4.1, Section 4.4, Table 2\n- 问题：Binary 0/1 是最粗粒度的评分方式。在此粒度下：(a) 任何影响 logit 但不足以翻转 binary decision 的方差源都会表现为 negligible——precision 的 <0.1% interaction 可能反映的是 binary scoring 的测量灵敏度不足而非真正的等价性；(b) item difficulty 天然主导，因为一致性地 easy/hard 的 items 在所有 conditions 下都稳定产出 1/0，而其他方差源的效应被压缩进 25% 的 residual（Table 2）。text-exact-match 对比（G=0.007 vs G=0.936）是论文自身提供的最佳证据：评分粒度根本性地重塑了方差结构。但论文将此视为一个独立发现（Contribution #3 的\"metric-conditional\"caveats），而非系统性地影响所有 findings 的 measurement confound。\n- 为什么影响接收：读者可能将 \"BF16≈FP16\" 解读为通用结论，而非 binary-scoring-conditional 结论。item dominance 的绝对量级（58.4%, 37.9%）在更细粒度评分下可能显著降低。\n- 建议修改方向：在 Section 3.5 或 Section 4.1 开头增加一段系统性讨论 binary scoring 的 measurement resolution confound：明确所有后续发现（包括 item dominance、precision interchangeability、D-study budgets）都是 \"conditional on binary correctness scoring\" 这一前提的推论，而非关于 LLM evaluation variance 的一般性结论。当前的 metric-conditionality 讨论散布在各节中，缺乏统一框架。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **Quasi-random model facet 的 exchangeability 论证不完整**\n- 具体位置：Section 3.6, Appendix A (LOMO)\n- 问题：G-theory 要求 facet levels 从 universe 中（至少近似）随机抽样。论文将 8 个 purposively 选择的模型视为 quasi-random facet，universe 定义为 \"open-weight 7–9B instruction-tuned models from six architecture families\"。LOMO（item_id: 36–41%, G: 0.877–0.889）和 4-model subset（ΔG=0.003）证明了**内部稳定性**，但不能证明**代表性**——换一批同 universe 的 8 个模型是否会产生相似的方差分解？这些模型共享 2024–2025 训练范式（类似的 RLHF/DPO 策略、相似的数据混合），可能存在 temporal correlation 违反 exchangeability。\n- 建议：明确讨论 purposive selection 的局限性；报告 8 个模型间的 pairwise agreement（如 Cohen's κ 分布），展示它们是否确实构成 \"diverse\" 样本；或引用 G-theory 中关于 purposive facet 的理论文献加以辩护。\n\n**W2** [warning] **exp-001 → exp-002 的 design reduction 的 cross-benchmark 验证缺失**\n- 具体位置：Section 3.3, Appendix A (Reduced crossing validation)\n- 问题：exp-001 用 3 precisions × 3 temps，exp-002 缩减为 1 precision × 2 temps。Appendix 的 reduced crossing validation（ΔG=0.0008）是在 **MMLU** 数据的 subset 上进行的，但该缩减实际应用于 4 个新 benchmark。如果 precision×benchmark 或 precision×format 存在 interaction（论文只在 MMLU 上检查了 precision），则在 FF benchmarks 上去除 precision facet 可能产生不同的 confounding。\n- 建议：至少讨论 \"reduced crossing validation 仅在 MMLU 上执行\" 的局限，或提供 1 个非 MMLU benchmark 的 validation。\n\n**W3** [warning] **Scale validation 范围过窄但语言过强**\n- 具体位置：Section 4.6\n- 问题：\"item dominance is scale-robust\" 仅基于 Qwen2.5 家族内的 3B 和 7B 两个规模。这是单一模型家族内的 2 个数据点，不足以支撑 \"scale-robust\" 的一般性语言。2-model crossed design 的 G=0.71 本身确认了 2 个模型不够——但这也意味着跨规模的 G-theory 分析需要更多模型参与。\n- 建议：将 \"scale-robust\" 改为 \"scale-consistent within the Qwen2.5 3B–7B range\"；在 Limitations 中明确 70B+ 和跨家族的 scale validation 是 open question。\n\n**W4** [warning] **Probit simulation ρ=0.732 对 Henderson Method I 的支撑力度中等偏弱**\n- 具体位置：Section 3.5\n- 问题：ρ=0.732 意味着 binary 和 continuous rankings 之间约 46% 的方差不共享。论文用其他 4 个分析（GLMM ρ=1.0、REML <0.5pp、null calibration、accuracy-range stability）来补偿，整体证据链尚可。但 ρ=0.732 作为**第一个报告的**验证指标，会给读者留下负面第一印象。\n- 建议：重新组织验证顺序——先报告 GLMM（rank preservation ρ=1.0）和 REML（<0.5pp），再将 probit simulation 作为 supplementary evidence，并明确说明 ρ=0.732 反映的是 binary scoring 的 information loss 而非 Henderson Method I 的估计偏差。\n\n**W5** [warning] **Missing sensitivity analysis: few-shot example selection**\n- 具体位置：Section 3.2\n- 问题：论文变化了 few-shot examples 的**排列顺序**（4 orderings），但没有变化**哪些 examples 被选中**。Example selection 是已知的方差源（Pezeshkpour & Hrushcka 2024 已讨论），遗漏此 facet 可能导致 underestimation of prompt-related variance。\n- 建议：在 Limitations 中补充讨论，或追加一个 pilot analysis 比较不同 example sets 的方差影响。\n\n---\n\n## 小问题（不影响接收）\n\n- Section 4.6: \"with G = 0.963 and 0.956 respectively\" — PDF 渲染中 \"0.956\" 的 \"9\" 和 \"5\" 在某些分辨率下不易区分，建议检查 LaTeX 中数字的精确性。\n- Table 3 中 \"prompt\" 列对 MC 和 FF 有不同含义（prompt×item vs prompt main effect），表注已说明但容易被忽略。建议用不同列名（如 \"prmpt×item\" vs \"prompt\"）更直观。\n- Section 3.3 提到 ordering facet 对非 MMLU benchmarks \"structurally inert (σ²=0 by construction)\"，但 Table 1 仍将其列为 exp-002 的 facet（4 levels）。虽然数学上不影响 G_item，但可能让读者误以为 ordering 在所有 benchmarks 上都是 informative facet。\n- Appendix D Figure 4 的 x 轴标签 \"std(p_i)\" 应在 caption 中更明确地定义（标准差是跨 models 还是跨 conditions？）。\n- Abstract 称 \"approximately 2.3 million evaluation records\"，但 exp-001 (460,800) + exp-002 (2,304,000) = 2,764,800。\"2.3 million\" 似乎只指 exp-002。建议明确说明是 \"2.3 million in the cross-benchmark analysis\" 还是 \"approximately 2.8 million total\"。\n\n---\n\n## 主要优势\n\n1. **框架选择正确且应用系统**：G-theory 是解决 \"LLM evaluation 中方差来自哪里\" 这一问题的 canonical 工具。论文将其从教育测量成功迁移到 LLM evaluation，crossing 7 facets × 5 benchmarks × 8 models，实验规模在同类工作中最大。与 Messing (2026) 的 single-benchmark 设计和 Madaan et al. (2024) 的 per-factor 方法相比，本文的 factorial crossing 能估计 interaction terms——这是理解方差结构的关键。\n\n2. **Robustness checking 达到顶会水准**：8 项独立检查（GLMM complement、accuracy-range stability、REML comparison、CI method comparison、facet specification sensitivity、LOMO、null calibration、reduced crossing validation）构成了系统的证据链。特别是 null calibration 清晰排除了 Bernoulli p(1-p) artifact（0.08% vs 58.4%），LOMO 的 |ΔG|<0.02 跨 4 个 benchmark 展示了方差分解的模型稳定性。\n\n3. **统计报告诚实透明**：format-associated claim 明确标注 p=0.10 permutation floor 和 benchmark-level CI spanning zero；precision interchangeability 明确标注 metric-conditionality；D-study budgets 提供 bootstrap CI。论文没有 overclaim——这在 LLM evaluation 领域难能可贵。\n\n4. **实践工具价值高**：D-study budget table（Table 4 + Appendix B Table 6）和 intermediate design gradient（Appendix C Table 7）提供了直接可操作的指导。\"3 prompts × 3 seeds\" 作为 minimal sufficient upgrade（G: 0.592→0.766, 成本 9×）的推荐尤其实用。\n\n5. **IRT 互补性论证有力**：Table 4 将 Zhou et al. (2026) 的 IRT-selected 116 items 放入 multi-facet design（G: 0.457→0.895），优雅地展示了 item selection（IRT）和 condition optimization（G-theory）的正交互补性。\n\n---\n\n## Missing References\n\n- Holland, P.W. & Wainer, H. (1993). *Differential Item Functioning*. Lawrence Erlbaum. — DIF 在教育测量中的经典参考文献，论文讨论 DIF 语义差异时可引用。\n- Clauser, B.E. & Mazor, K.M. (1998). Using Statistical Procedures to Identify Differentially Functioning Test Items. *Educational Measurement*. — 补充 DIF 操作化的教育测量背景。\n- Webb, N.M., Shavelson, R.J., & Haertel, E.H. (2006). Reliability Coefficients and Generalizability Theory. *Handbook of Statistics*. — G-theory 关于 random vs fixed facet 分类的讨论，可支撑 quasi-random facet 论证。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.5 (Borderline Conference)\n**置信度**: 4/5\n\n**理由**: 论文将 G-theory 系统应用于 LLM evaluation variance decomposition，实验设计严谨，robustness 检查全面，统计报告诚实。核心贡献（multi-facet design 的 10× 效率增益）在 MMLU 上有良好支撑。但三个方法学问题共同削弱了 generalizability claim 的说服力：(1) format-associated pattern 作为主要贡献被突出呈现，但 n=5 的统计功效先天不足；(2) D-study budget 推荐对 4/5 benchmarks 缺乏 cross-sample 验证；(3) binary scoring confound 对所有 findings 的系统性影响未被充分讨论为统一框架。如果 N1（重新调整 format claim 的呈现层级）和 N2（至少补充 1–2 个 benchmark 的 cross-sample validation）在 revision 中得到解决，论文可以达到 4.0 (Conference)。当前版本在方法学 execution 上是扎实的，但 evidence-to-claim 的匹配在最广泛的主张上存在缺口。",
    "reviewer_id": "1",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 357 · 2026-05-22T11:49:21.268795+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3915
}
```

</details>

---


### Tool call

_source line 358 · 2026-05-22T11:49:25.794072+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 359 · 2026-05-22T11:49:25.794525+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 360 · 2026-05-22T11:49:29.710506+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_4/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 361 · 2026-05-22T11:49:29.961573+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 362 · 2026-05-22T11:49:29.961958+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/tmp/nlp_review_pages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/tmp/nlp_review_pages"
  }
}
```

</details>

---


### Tool result

_source line 363 · 2026-05-22T11:49:30.012424+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"安全限制：只能清理 _pdf_images 目录，当前目标: nlp_review_pages\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 364 · 2026-05-22T11:49:38.684087+00:00_

审稿意见已提交给 Review Director。

**审稿结论**：Overall 3.5 (Borderline Conference)。

三个 Must-Fix 问题：
1. Format-associated claim（Contribution #2）的突出程度超过其统计支撑（n=5, p=0.10 permutation floor），需降级呈现或补充 benchmarks
2. D-study budget 推荐对 4/5 benchmarks 缺乏 cross-sample 验证，仅 MMLU 有 3 组独立样本（CV=3.1%）
3. Binary scoring 对所有 findings 的系统性 measurement resolution confound 未被统一讨论

五个 Should-Fix 和若干小问题也已一并报告。论文方法学 execution 扎实、robustness 检查全面，解决 N1 和 N2 后可达 4.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1"
}
```

</details>

---


## Round 10

## Round 10

4 recorded events


### User

_source line 365 · 2026-05-22T11:50:17.625576+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和主要观点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 的完整审稿意见

### Must-Fix

**N1** [critical] Format-associated claim 的统计功效与呈现方式不匹配
- benchmark-level 置换检验 p=0.10 是分辨率下限（C(5,3)=10），CI 跨零 [-1.7, 5.1]。论文正确标注为 "descriptive observation"，但该 claim 贯穿 title、abstract、贡献列表 #2、§4.3 整节、Figure 2、Table 3、Conclusion。读者很难区分哪些是有统计支撑的发现、哪些仅是观察性假设。

**N2** [critical] Conclusion 过于简短
- §5 仅一段约 6 行。缺少 implications（leaderboard 如何改？benchmark 发布协议？）、与 IRT 的实践互补性、format-associated pattern 的后续验证路线。

### Should-Fix

**W1** Contribution #1 排序问题——D-study budgets 是 G-theory 分析的直接推导，不是独立贡献。

**W2** Method (§3) 与 Experiments (§4) 边界模糊——§3.2-3.6 是实验设计细节。

**W3** MATH 缺少 DeepSeek 的解释不充分——"incomplete inference data" 未说明原因。

**W4** Abstract 信息密度过高——一段内 10+ 个数字/百分比。

**W5** Related Work 遗漏：Benchmark Health Index (2602.11674)、"Measuring what Matters" (2511.04703)、"Establishing Construct Validity...Nomological Networks" (2603.15121)。

**W6** 规模验证仅限 Qwen 3B-9B。

### Missing References
- Benchmark Health Index (2602.11674)
- "Measuring what Matters" (2511.04703)
- "Establishing Construct Validity...Nomological Networks" (2603.15121)

---

请逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 366 · 2026-05-22T11:51:52.133419+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1: Format-associated claim 的统计功效与呈现方式不匹配**\n\n完全同意，这与我的 N1 高度一致。补充两点观察：\n\n1. 论文内部存在**呈现梯度不一致**：Section 4.3 正文中明确写了 \"descriptive observation with strong item-level support rather than a confirmatory finding\"（experiments.tex L72），permutation floor p=0.10 和 benchmark-level CI [-1.7, 5.1] 都如实报告——这部分的统计诚实性是好的。但 Abstract 第 1 句 (\"On multiple-choice benchmarks, item selection drives 34–38%…\") 没有任何 hedging，Contribution #2 虽加了 \"(n=5; not confirmatory)\" 但仍然与 Contribution #1 并列为同等级贡献。Figure 2 和 Table 3 作为独立的图表呈现进一步强化了 \"这是一个 confirmed finding\" 的印象。\n\n2. 论文在 Section 4.3 花了整段篇幅反驳 \"tautology\" 反对意见（HellaSwag 例外 + MMLU subject-level ρ=0.806），这种 defend 力度与 \"descriptive observation\" 的定位不匹配——如果仅是观察，不需要这么重的辩护。\n\n建议与 R2 一致：Abstract 和 Contributions 中需要更一致的 hedging，或补充 benchmarks 提升统计功效。\n\n**[REBUT] R2-N2: Conclusion 过于简短**\n\n不认为这是 Must-Fix。\n\n理由：(1) ACL/EMNLP 顶会论文中简短 Conclusion 是常见且被接受的做法，尤其在 8 页限制下，空间应优先分配给方法学和实验细节。(2) Reviewer 2 要求的 implications（leaderboard 改进、benchmark 发布协议）属于 **Discussion** 内容而非 Conclusion 的核心职责——论文可以选择不写 Discussion section。(3) IRT 互补性已在 Section 4.5（Table 4 的 Zhou et al. 对比）和 Related Work（Positioning 段）中充分讨论，重复会浪费篇幅。(4) format-associated pattern 的后续验证路线已在 Limitations（Section 6: \"other formats (code generation, multi-turn dialogue) may differ\"）中暗示。\n\n不过我同意 Conclusion 可以**适度扩展**（增加 2–3 句 practical takeaway），但定位为 **Minor** 而非 Must-Fix。当前 Conclusion 涵盖了三个主要发现和开源承诺，虽然简洁但完整。\n\n---\n\n### Should-Fix\n\n**[REBUT] R2-W1: D-study budgets 不是独立贡献**\n\n不同意。D-study projections 虽然是 G-theory 的标准步骤，但本文的 budget 贡献有三层超越标准 G-theory 管线的独立价值：\n\n1. **IRT 互补性的实证展示**（Table 4）：将 Zhou et al. (2026) 的 IRT-selected 116 items 放入 multi-facet design（G: 0.457→0.895），展示 item selection 和 condition optimization 的正交互补。这不是 G-theory 的自动输出，而是一个新的实证发现。\n2. **Intermediate design gradient**（Appendix C, Table 7）：从 single-condition 到 full multi-facet 的 6 档渐进升级路径（\"easy upgrade\" 2p×2s → \"minimal sufficient\" 3p×3s → ... → full），提供了 cost-benefit 分析。这是面向 practitioners 的工程化翻译，不是标准 G-theory 文献的常见做法。\n3. **Cross-benchmark budget 对比**（Appendix B, Table 6）：MC 11–13× vs FF 21–22× 的 format-associated efficiency gap 是一个新发现，不是从方差分解中可以直接预测的。\n\n将其降级为 \"G-theory 的推导\" 低估了实践贡献。\n\n**[AGREE] R2-W2: Method/Experiments 边界模糊**\n\n部分同意。Section 3.2（MMLU 设计）、3.3（Cross-benchmark 扩展）和 3.4（Evaluation protocol）确实更像实验设计细节。但在 G-theory 论文中，experimental design 本身就是 method 的核心——不同的 crossing structure 决定了可估计的方差成分。我认为这更多是**组织偏好**而非方法学问题，可以通过将 Section 3 重命名为 \"Method and Experimental Design\" 来解决。不影响评分。\n\n**[AGREE] R2-W3: DeepSeek MATH 排除解释不充分**\n\n同意。论文仅说 \"incomplete inference data\"（experiments.tex L46）和 Appendix B 提到 \"37,400/57,600 expected records\"（约 35% 缺失），但未说明原因。这很重要，因为：\n- 如果是 OOM/timeout → 说明 DeepSeek 在 MATH 上计算更吃力，缺失数据可能是 MNAR（Missing Not At Random），偏向困难题目\n- 如果是 vLLM 兼容性问题 → 则缺失是 MCAR（Missing Completely At Random），影响较小\n- Appendix A 的 LOMO 分析（Table 5）显示去除 DeepSeek 后 |ΔG|<0.02，但这是在**完整数据的 4 个 benchmark** 上做的，不能直接推广到**已有缺失的 MATH**\n\n建议：补充 1–2 句说明缺失原因和 missing data mechanism。\n\n**[REBUT] R2-W4: Abstract 信息密度过高**\n\n不同意。G-theory/psychometrics 方法论文的 Abstract 需要报告关键数值（方差成分、G 系数、效率比、效应量）才能让读者快速判断结果的量级。移除数字会让 Abstract 变成空泛的定性描述。当前 Abstract 在一段内确实包含 10+ 个数字，但每个数字都对应一个核心发现——这符合 ACL 系统的方法论文 norm。\n\n**[AGREE] R2-W5: Missing References**\n\n部分同意。我没有独立检查这三篇论文的存在性和相关性，但从标题判断：\n- \"Benchmark Health Index\" — 可能与 benchmark 质量评估相关，值得在 Related Work 中讨论\n- \"Measuring what Matters\" — 可能与 evaluation methodology 相关\n- \"Establishing Construct Validity...Nomological Networks\" — 与 Related Work 中已引用的 psychometric perspectives (Kearns 2026, Ye 2025) 相关\n\n建议作者验证这三篇论文的真实性和相关性后酌情添加。但 Missing References 通常不影响评分——Related Work 已经涵盖了 variance decomposition、IRT、psychometrics、infrastructure variance 四大方向的核心文献。\n\n**[AGREE] R2-W6: 规模验证仅限 Qwen 3B–9B**\n\n完全同意，与我的 W3 一致。Section 4.6 的 \"scale-robust\" 语言基于单一模型家族内的 2 个数据点（Qwen2.5 3B: 75.3%, 7B: 73.4%），不足以支撑一般性结论。建议改为 \"scale-consistent within the tested range\"。\n\n---\n\n### 总结\n\n与 Reviewer 2 的共识点：**N1（format claim 呈现）**、**W3（DeepSeek 解释）**、**W6（scale validation）**。\n\n分歧点：\n- **N2（Conclusion 长度）**：我认为是 Minor 而非 Must-Fix，当前 Conclusion 在 8 页限制下是可接受的。\n- **W1（D-study 贡献独立性）**：我认为 budget 贡献有超越标准 G-theory 的独立价值，不应降级。\n- **W4（Abstract 密度）**：方法论文 Abstract 的信息密度在 ACL venue 中是正常的。",
  "reviewer_id": "1",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R2-N1: Format-associated claim 的统计功效与呈现方式不匹配**\n\n完全同意，这与我的 N1 高度一致。补充两点观察：\n\n1. 论文内部存在**呈现梯度不一致**：Section 4.3 正文中明确写了 \"descriptive observation with strong item-level support rather than a confirmatory finding\"（experiments.tex L72），permutation floor p=0.10 和 benchmark-level CI [-1.7, 5.1] 都如实报告——这部分的统计诚实性是好的。但 Abstract 第 1 句 (\"On multiple-choice benchmarks, item selection drives 34–38%…\") 没有任何 hedging，Contribution #2 虽加了 \"(n=5; not confirmatory)\" 但仍然与 Contribution #1 并列为同等级贡献。Figure 2 和 Table 3 作为独立的图表呈现进一步强化了 \"这是一个 confirmed finding\" 的印象。\n\n2. 论文在 Section 4.3 花了整段篇幅反驳 \"tautology\" 反对意见（HellaSwag 例外 + MMLU subject-level ρ=0.806），这种 defend 力度与 \"descriptive observation\" 的定位不匹配——如果仅是观察，不需要这么重的辩护。\n\n建议与 R2 一致：Abstract 和 Contributions 中需要更一致的 hedging，或补充 benchmarks 提升统计功效。\n\n**[REBUT] R2-N2: Conclusion 过于简短**\n\n不认为这是 Must-Fix。\n\n理由：(1) ACL/EMNLP 顶会论文中简短 Conclusion 是常见且被接受的做法，尤其在 8 页限制下，空间应优先分配给方法学和实验细节。(2) Reviewer 2 要求的 implications（leaderboard 改进、benchmark 发布协议）属于 **Discussion** 内容而非 Conclusion 的核心职责——论文可以选择不写 Discussion section。(3) IRT 互补性已在 Section 4.5（Table 4 的 Zhou et al. 对比）和 Related Work（Positioning 段）中充分讨论，重复会浪费篇幅。(4) format-associated pattern 的后续验证路线已在 Limitations（Section 6: \"other formats (code generation, multi-turn dialogue) may differ\"）中暗示。\n\n不过我同意 Conclusion 可以**适度扩展**（增加 2–3 句 practical takeaway），但定位为 **Minor** 而非 Must-Fix。当前 Conclusion 涵盖了三个主要发现和开源承诺，虽然简洁但完整。\n\n---\n\n### Should-Fix\n\n**[REBUT] R2-W1: D-study budgets 不是独立贡献**\n\n不同意。D-study projections 虽然是 G-theory 的标准步骤，但本文的 budget 贡献有三层超越标准 G-theory 管线的独立价值：\n\n1. **IRT 互补性的实证展示**（Table 4）：将 Zhou et al. (2026) 的 IRT-selected 116 items 放入 multi-facet design（G: 0.457→0.895），展示 item selection 和 condition optimization 的正交互补。这不是 G-theory 的自动输出，而是一个新的实证发现。\n2. **Intermediate design gradient**（Appendix C, Table 7）：从 single-condition 到 full multi-facet 的 6 档渐进升级路径（\"easy upgrade\" 2p×2s → \"minimal sufficient\" 3p×3s → ... → full），提供了 cost-benefit 分析。这是面向 practitioners 的工程化翻译，不是标准 G-theory 文献的常见做法。\n3. **Cross-benchmark budget 对比**（Appendix B, Table 6）：MC 11–13× vs FF 21–22× 的 format-associated efficiency gap 是一个新发现，不是从方差分解中可以直接预测的。\n\n将其降级为 \"G-theory 的推导\" 低估了实践贡献。\n\n**[AGREE] R2-W2: Method/Experiments 边界模糊**\n\n部分同意。Section 3.2（MMLU 设计）、3.3（Cross-benchmark 扩展）和 3.4（Evaluation protocol）确实更像实验设计细节。但在 G-theory 论文中，experimental design 本身就是 method 的核心——不同的 crossing structure 决定了可估计的方差成分。我认为这更多是**组织偏好**而非方法学问题，可以通过将 Section 3 重命名为 \"Method and Experimental Design\" 来解决。不影响评分。\n\n**[AGREE] R2-W3: DeepSeek MATH 排除解释不充分**\n\n同意。论文仅说 \"incomplete inference data\"（experiments.tex L46）和 Appendix B 提到 \"37,400/57,600 expected records\"（约 35% 缺失），但未说明原因。这很重要，因为：\n- 如果是 OOM/timeout → 说明 DeepSeek 在 MATH 上计算更吃力，缺失数据可能是 MNAR（Missing Not At Random），偏向困难题目\n- 如果是 vLLM 兼容性问题 → 则缺失是 MCAR（Missing Completely At Random），影响较小\n- Appendix A 的 LOMO 分析（Table 5）显示去除 DeepSeek 后 |ΔG|<0.02，但这是在**完整数据的 4 个 benchmark** 上做的，不能直接推广到**已有缺失的 MATH**\n\n建议：补充 1–2 句说明缺失原因和 missing data mechanism。\n\n**[REBUT] R2-W4: Abstract 信息密度过高**\n\n不同意。G-theory/psychometrics 方法论文的 Abstract 需要报告关键数值（方差成分、G 系数、效率比、效应量）才能让读者快速判断结果的量级。移除数字会让 Abstract 变成空泛的定性描述。当前 Abstract 在一段内确实包含 10+ 个数字，但每个数字都对应一个核心发现——这符合 ACL 系统的方法论文 norm。\n\n**[AGREE] R2-W5: Missing References**\n\n部分同意。我没有独立检查这三篇论文的存在性和相关性，但从标题判断：\n- \"Benchmark Health Index\" — 可能与 benchmark 质量评估相关，值得在 Related Work 中讨论\n- \"Measuring what Matters\" — 可能与 evaluation methodology 相关\n- \"Establishing Construct Validity...Nomological Networks\" — 与 Related Work 中已引用的 psychometric perspectives (Kearns 2026, Ye 2025) 相关\n\n建议作者验证这三篇论文的真实性和相关性后酌情添加。但 Missing References 通常不影响评分——Related Work 已经涵盖了 variance decomposition、IRT、psychometrics、infrastructure variance 四大方向的核心文献。\n\n**[AGREE] R2-W6: 规模验证仅限 Qwen 3B–9B**\n\n完全同意，与我的 W3 一致。Section 4.6 的 \"scale-robust\" 语言基于单一模型家族内的 2 个数据点（Qwen2.5 3B: 75.3%, 7B: 73.4%），不足以支撑一般性结论。建议改为 \"scale-consistent within the tested range\"。\n\n---\n\n### 总结\n\n与 Reviewer 2 的共识点：**N1（format claim 呈现）**、**W3（DeepSeek 解释）**、**W6（scale validation）**。\n\n分歧点：\n- **N2（Conclusion 长度）**：我认为是 Minor 而非 Must-Fix，当前 Conclusion 在 8 页限制下是可接受的。\n- **W1（D-study 贡献独立性）**：我认为 budget 贡献有超越标准 G-theory 的独立价值，不应降级。\n- **W4（Abstract 密度）**：方法论文 Abstract 的信息密度在 ACL venue 中是正常的。",
    "reviewer_id": "1",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-22T11:51:55.695845+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3562
}
```

</details>

---


### Assistant

_source line 368 · 2026-05-22T11:52:04.218503+00:00_

已提交对 Reviewer 2 的逐条回应。

核心共识：format-associated claim 的呈现需要与统计功效对齐（N1）、DeepSeek 排除需说明原因（W3）、scale validation 语言需降级（W6）。

核心分歧：Conclusion 长度是 Minor 而非 Must-Fix（N2）、D-study budgets 有独立贡献价值不应降级（W1）、方法论文 Abstract 的数字密度在 ACL venue 中是正常的（W4）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1"
}
```

</details>

---


## Round 11

## Round 11

68 recorded events


### User

_source line 369 · 2026-05-22T12:57:30.302527+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责 **方法严谨性 + 实验有效性** 审查。

## 论文信息
- 标题: "Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Analysis"
- 论文路径: `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/submitted.pdf`
- 目标 venue: **EMNLP 2026** (通过 ARR May cycle 提交)
- 投稿类别: ARR long paper
- Deadline: 2026-05-25

## Venue 格式要求
- 长文正文 **严格 8 页限制**，参考文献无限制
- Limitations 必填（不超过 1 页，不计入页数）
- ACL 模板，double-blind 匿名审稿
- Overall Assessment 评分: 5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit（含 0.5 档中间值）

## 你的审查侧重

**方法严谨性**：
1. G-theory 在 LLM evaluation 中的应用是否合理？binary data 上用 Henderson Method I 的理论辩护是否充分？
2. 方差分解（Henderson Method I）的估计偏差和假设条件是否满足？bootstrap CI 的有效性
3. 交叉设计 (fully crossed) 的平衡性假设是否被违反？reduced crossing (exp-002) 的外推有效性
4. "Item-related variance" bundling (item + model×item) 的心理测量学合理性
5. Quasi-random model facet 假设——8 个 purposively selected models 作为 random facet 的合理性
6. D-study projections 的外推有效性——budget 从 single-model 推到 cross-model 的假设强度

**实验有效性**：
1. 2.3M records 的数据规模和 5 benchmarks 的覆盖面是否充分支持核心 claims？
2. Format-associated pattern (MC 68-72% vs FF 31-41%) 的统计支持强度——n=5 benchmarks, p=0.10 permutation test
3. Precision separability (&lt;0.1% interaction) 是否真正可以推广到所有 precision levels / models？
4. Cross-model LOMO 分析是否足以验证 model exchangeability？
5. Scale validation (3B-7B) 的范围是否过窄？
6. Robustness checks（9 项）的覆盖面和每项的说服力

**立场**：严格、不留情面。像顶会最严格的审稿人一样评估。找出所有方法论上的漏洞和实验设计的不足。

请输出完整审稿意见，包含：Summary（2-3句）、Strengths（逐条）、Weaknesses（逐条，标注 [Must-Fix] 或 [Should-Fix]）、Questions（需要作者回答的问题）、Missing References（遗漏的重要相关工作）、Minor Issues、Overall Assessment（评分 + 理由）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 370 · 2026-05-22T12:59:38.722899+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-22T12:59:39.527552+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-22T12:59:39.578195+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 373 · 2026-05-22T12:59:39.628764+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 374 · 2026-05-22T12:59:43.390405+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 review form criteria scoring rubric"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 review form criteria scoring rubric"
  }
}
```

</details>

---


### Tool call

_source line 375 · 2026-05-22T12:59:44.342562+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review reviewer guidelines review form dimensions 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review reviewer guidelines review form dimensions 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 376 · 2026-05-22T12:59:45.194998+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/submitted.pdf",
  "project": "nlp_variance_gtheory",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/submitted.pdf",
    "project": "nlp_variance_gtheory",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 377 · 2026-05-22T12:59:49.912953+00:00_

Web search results for query: "ACL ARR 2026 review form criteria scoring rubric"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Development and Validation of a Scoring Rubric for Editorial Evaluation of Peer-review Quality: A Pilot Study","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11000557/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"}]

Based on the search results, here's what I found about ACL ARR 2026 review form criteria and scoring:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Overall Recommendation Score Scale

The overall recommendation includes: 5 = Consider for Award (papers in top 2.5%), 2 = Resubmit next cycle (for papers needing substantial revisions completable by next ARR cycle), 1.5 = Resubmit after next cycle (for papers needing substantial revisions not completable by next cycle), and 1 = Do not resubmit (for papers that need to be fully redone or are not relevant to the *ACL community).

## Criteria for Different Venue Types

The main criteria for Findings papers are soundness and reproducibi
…[truncated 504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6522
}
```

</details>

---


### Tool result

_source line 378 · 2026-05-22T12:59:54.232791+00:00_

Web search results for query: "ACL Rolling Review reviewer guidelines review form dimensions 2025 2026"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/changelog"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here is information about the ACL Rolling Review reviewer guidelines and review form dimensions for 2025-2026:

## Reviewer Guidelines - Key Updates for 2025-2026

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Policy Changes Starting May 2025

Starting from May 2025, ACL introduces the awards policy for reviewers & chairs where area chairs or senior area chairs may nominate great reviewers, and senior chairs may also nominate area chairs who perform great service, with nominees receiving more recognition during ACL conferences.

Starting in 
…[truncated 726 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 9890
}
```

</details>

---


### Tool result

_source line 379 · 2026-05-22T12:59:55.639965+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 471.2}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 562.0}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 573.1}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 540.8}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 469.5}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 519.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 502.3}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.3}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 564.2}, {\"page\":
…[truncated 438 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 10444
}
```

</details>

---


### Tool call

_source line 380 · 2026-05-22T13:02:01.248242+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall assessment, and any other dimensions. List the exact scale descriptions for each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include soundness, excitement, overall assessment, and any other dimensions. List the exact scale descriptions for each score level."
  }
}
```

</details>

---


### Tool call

_source line 381 · 2026-05-22T13:02:03.206278+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, especially: what criteria should reviewers evaluate, how to score soundness, excitement, and overall assessment, what constitutes a good review, and any specific rubrics or criteria for each dimension."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines, especially: what criteria should reviewers evaluate, how to score soundness, excitement, and overall assessment, what constitutes a good review, and any specific rubrics or criteria for each dimension."
  }
}
```

</details>

---


### Tool call

_source line 382 · 2026-05-22T13:02:04.161535+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/submitted.pdf",
  "project": "nlp_variance_gtheory",
  "pages": "11-13",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/submitted.pdf",
    "project": "nlp_variance_gtheory",
    "pages": "11-13",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 383 · 2026-05-22T13:02:04.662787+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 384 · 2026-05-22T13:02:05.114001+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 385 · 2026-05-22T13:02:06.116272+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-22T13:02:06.668473+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 387 · 2026-05-22T13:02:06.971263+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 388 · 2026-05-22T13:02:08.175635+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. Reviewer Confidence
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: Quite sure; unlikely to have missed significant details
- **3**: Pretty sure; may have missed some specifics
- **2**: Willing to defend evaluation; likely missed some details
- **1**: "Not my area, or paper is very hard to understand"

## 2. Soundness
Scale: 1-5 (with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: "Strong: This study provides sufficient support for all of its claims"
- **3**: "Acceptable: This study provides sufficient support for its main claims"
- **2**: "Poor: Some of the main claims are not sufficiently supported"
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## 3. Excitement
Scale: 1-5 (with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points"
- **2**: "Potentially Interesting: does not resonate with me, but might with others"
- **1**: "Not Exciting: does not resonate with me, and I don't think it would with others"

## 4. Overall Assessment
Scale: 1-5 (with half-point increments)
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Accept to Findings
- **2**: Resubmit next cycle
- **1**: Do not resubmit

## 5. Reproducibility
Scale: 1-5
- **5**: "They could easily reproduce the results"
- **4**: Mostly reproducible with minor variations
- **3**: Reproducible with difficulty
- **2**: Hard to reproduce; unavailable data or insufficient details
- **1**: "They would not be able to reproduce the results"

## 6. Datasets Value
Scale: 1-5
- **5**: Enabling impact on research direction
- **4**: Useful for other researchers
- **3**: Potentially useful
- **2**: Documentary
…[truncated 470 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6927
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-22T13:02:14.009650+00:00_

# ARR Reviewer Guidelines: Evaluation Criteria and Scoring Framework

## Core Evaluation Dimensions

ARR reviewers assess papers across three primary scoring dimensions:

### 1. **Soundness**
Reviewers evaluate technical correctness and methodological rigor. Soundness scores "must be justified by the text of the review." Low soundness ratings require explicit evidence of flaws; vague assessments without supporting detail violate guidelines.

Key soundness considerations include:
- Technical validity of claims and proofs
- Appropriate statistical analysis and significance testing
- Reproducibility of experiments with sufficient implementation details
- Absence of logical fallacies or unsupported assertions

### 2. **Excitement**
This separate dimension captures subjective interest independent of soundness. A reviewer might find work technically solid but personally uninteresting—or conversely, find novel work that doesn't align with their subfield particularly engaging.

### 3. **Overall Assessment**
This composite recommendation reflects soundness, excitement, novelty, and potential impact. Papers need not be exciting personally to warrant acceptance if they represent significant contributions (e.g., efficiency improvements, resource development for underserved languages).

## What Constitutes a Strong Review

### Specificity Requirements (I1)
Vague critiques are prohibited. Instead of stating "X is unclear," reviewers must identify what information is missing: "Y and Z are absent from the X description." This enables chairs to evaluate critiques without rereading papers.

### Professional Tone (I4)
Reviews must be "professional and neutral, if not kind." Guidelines emphasize that dismissive or sarcastic language causes demonstrable harm and violates the collaborative spirit of peer review.

### Common Review Problems to Avoid (H1-H17)

Reviewers should interrogate whether their critiques reflect legitimate weaknesses or common biases:

- **H1**: "Results are unsurp
…[truncated 1425 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 10803
}
```

</details>

---


### Tool result

_source line 390 · 2026-05-22T13:02:14.666452+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 513.9}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 429.9}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 332.6}], \"total_pages\": 13, \"rendered_pages\": 3, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 10504
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-22T13:02:18.127343+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 13464
}
```

</details>

---


### Tool result

_source line 392 · 2026-05-22T13:02:18.180218+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 11208
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-22T13:02:18.186669+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 12070
}
```

</details>

---


### Tool result

_source line 394 · 2026-05-22T13:02:18.187888+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 11519
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-22T13:02:18.239270+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 13125
}
```

</details>

---


### Tool call

_source line 396 · 2026-05-22T13:02:41.586306+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 397 · 2026-05-22T13:02:42.439930+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-22T13:02:42.641162+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 399 · 2026-05-22T13:02:43.095875+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 400 · 2026-05-22T13:02:43.586525+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 945
}
```

</details>

---


### Tool call

_source line 401 · 2026-05-22T13:02:43.586958+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-22T13:02:43.990232+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 403 · 2026-05-22T13:02:44.744232+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 404 · 2026-05-22T13:02:45.510433+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2414
}
```

</details>

---


### Tool call

_source line 405 · 2026-05-22T13:02:45.510844+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-22T13:02:46.114763+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 407 · 2026-05-22T13:02:47.170754+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3583
}
```

</details>

---


### Tool result

_source line 408 · 2026-05-22T13:02:48.232132+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 4241
}
```

</details>

---


### Tool result

_source line 409 · 2026-05-22T13:02:48.685474+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3941
}
```

</details>

---


### Tool result

_source line 410 · 2026-05-22T13:02:48.687674+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 2572
}
```

</details>

---


### Tool result

_source line 411 · 2026-05-22T13:02:48.788927+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 3278
}
```

</details>

---


### Tool call

_source line 412 · 2026-05-22T13:03:28.027066+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 413 · 2026-05-22T13:03:28.077708+00:00_

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
11	\usepackage{graphicx}
12	\usepackage{amsmath,amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{xcolor}
16	
17	\graphicspath{{../../figures/paper/}}
18	
19	\title{Reproducibility Budgets for Open-Weight LLM Evaluation:\\A Generalizability Theory Analysis}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	\input{abstract}
28	\end{abstract}
29	
30	% === INTRODUCTION ===
31	\input{introduction}
32	
33	% === RELATED WORK ===
34	\input{related_work}
35	
36	% === METHOD ===
37	\input{method}
38	
39	% === EXPERIMENTS ===
40	\input{experiments}
41	
42	% === CONCLUSION ===
43	\input{conclusion}
44	
45	% === LIMITATIONS ===
46	\input{limitations}
47	
48	\bibliography{references}
49	
50	% === APPENDIX ===
51	\input{appendix}
52	
53	\end{document}
54	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 414 · 2026-05-22T13:03:31.693464+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/",
  "description": "List paper source files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/",
    "description": "List paper source files"
  }
}
```

</details>

---


### Tool result

_source line 415 · 2026-05-22T13:03:31.794530+00:00_

_pdf_images
aaai2026.bst
aaai2026.sty
abstract.tex
acl.sty
acl_natbib.bst
appendix.tex
conclusion.tex
experiments.tex
introduction.tex
limitations.tex
main.aux
main.bbl
main.blg
main.fdb_latexmk
main.fls
main.log
main.out
main.pdf
main.tex
method.tex
references.bib
related_work.tex
sections

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 416 · 2026-05-22T13:03:37.731307+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 417 · 2026-05-22T13:03:38.132600+00:00_

1	\section{Method and Experimental Design}
2	\label{sec:method}
3	
4	\subsection{Generalizability Theory}
5	\label{sec:gtheory}
6	
7	Generalizability theory (G-theory) treats each measurement as one observation from a universe of admissible conditions defined by the crossed facets of an evaluation design \cite{shavelson1991generalizability, brennan2001generalizability}. The \emph{object of measurement} is the entity whose consistency is of interest. In our setting, test items ($p$) serve as the object of measurement, and the goal is to determine how reliably item-level scores generalize across the methodological conditions under which they are collected.
8	
9	A \emph{G-study} decomposes total observed variance into components $\sigma^2_x$ for each facet $x$ and their interactions. Each component quantifies how much variability that source contributes to the overall measurement. Large interaction components (e.g., $\sigma^2_{pM}$ for item-by-model) indicate that facets do not affect items uniformly but instead create differential difficulty profiles. We estimate variance components via Henderson Method~I, an unbiased ANOVA-based estimator for balanced designs \cite[Ch.~3]{brennan2001generalizability}, with 1,000-resample bootstrap confidence intervals (item-level resampling with replacement, preserving the fully-crossed structure across all other facets) \cite{li2023bootstrap}.
10	
11	A \emph{D-study} projects the generalizability coefficient under hypothetical designs with different numbers of conditions per facet:
12	\begin{equation}
13	G_\text{item} = \frac{\sigma^2_p}{\sigma^2_p + \sigma^2_\text{rel}}
14	\label{eq:gcoeff}
15	\end{equation}
16	where $\sigma^2_\text{rel}$ aggregates all item-by-facet interaction variances, each divided by the number of conditions for the corresponding facets \cite[Ch.~4]{brennan2001generalizability}. This prospective capability distinguishes G-theory from classical ANOVA: rather than only attributing variance post hoc, a D-study en
…[truncated 9419 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 418 · 2026-05-22T13:03:38.233203+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 419 · 2026-05-22T13:03:38.384199+00:00_

1	\section{Experiments}
2	
3	All experiments use open-weight 7--9B parameter models evaluated with vLLM~0.9.2 on a single NVIDIA RTX PRO 6000 GPU (96GB) with binary correctness scoring.
4	
5	\subsection{Single-Model Baseline}
6	
7	We first establish the variance structure within a single model (Llama-3.1-8B-Instruct) on MMLU to isolate methodological facet contributions before introducing cross-model variation.
8	
9	\paragraph{Design.} The G-study crosses six facets: 200 items $\times$ 3 numerical precisions (BF16, FP16, FP32) $\times$ 6 prompt templates $\times$ 6 random seeds $\times$ 3 temperature levels (0.0, 0.3, 0.7) $\times$ 4 answer orderings, yielding 259,200 binary observations. Variance components are estimated via Henderson Method~I with bootstrap confidence intervals (1,000 resamples).
10	
11	\paragraph{Results.} Under binary scoring, item difficulty (\texttt{item\_id}) accounts for 58.4\% of total variance, with the residual term contributing 23.1\%. All main facet effects are negligible ($<$1\% each): precision 0.9\%, prompt template, temperature, seed, and ordering each $<$0.5\%. The interesting structure appears in item-conditional interactions: prompt$\times$item is the largest at 5.5\%, followed by seed$\times$item (4.7\%), precision$\times$item (3.3\%), temperature$\times$item (2.9\%), and ordering$\times$item (0.8\%). This pattern indicates that methodological choices do not shift performance uniformly across items; instead, specific items are differentially sensitive to specific facets---prompt template variation produces the largest item-conditional effect.
12	
13	The resulting generalizability coefficient is $G_\text{item} = 0.936$, indicating that 200 items under multi-facet conditions produce highly reliable rankings. A D-study projection shows $G \geq 0.80$ is achievable with as few as 55 items in this multi-facet design.
14	
15	For text-exact-match scoring (requiring verbatim string matches), the variance structure shifts dramatically: te
…[truncated 12185 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 420 · 2026-05-22T13:03:38.434962+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 421 · 2026-05-22T13:03:38.535720+00:00_

1	\appendix
2	\section{Additional Robustness Analyses}
3	\label{app:robustness}
4	
5	We report nine robustness analyses that verify the stability of the variance decomposition under alternative analytical choices.
6	
7	\paragraph{GLMM complement.} A generalized linear mixed model (GLMM) with marginal logit link produces variance component rankings that perfectly preserve all seven grouped component orderings ($\rho = 1.0$) relative to Henderson Method~I \cite{jiang2018bayesian, tuerlinckx2006glmm}. This confirms that the linear variance decomposition is robust to the binary outcome distribution.
8	
9	\paragraph{Accuracy-range stability.} The \texttt{item\_id} variance share remains stable across subsets with mean accuracy from 0.62 to 0.72 ($r = -0.048$). This rules out distortion from binary floor or ceiling effects at observed accuracy levels.
10	
11	\paragraph{Estimator robustness.} We compare Henderson Method~I with restricted maximum likelihood (REML-EM, 500 iterations, practical convergence $\Delta < 0.003$ percentage points). All variance components differ by $<$0.5 percentage points between estimators. The largest discrepancy occurs on the residual component (0.47pp); all substantive components (item, model$\times$item, model) differ by $<$0.3pp. Henderson Method~I is preferred for our balanced designs because it produces unbiased estimates without distributional assumptions \cite[Ch.~12]{brennan2001generalizability}.
12	
13	\paragraph{Probit simulation.} A probit simulation matched to our 1,296-condition design confirms that Henderson Method~I recovers variance component rankings from dichotomized data (Spearman $\rho = 0.732$ between binary and continuous rankings; \texttt{item\_id} dominant in all 100 replications).
14	
15	\paragraph{CI method comparison.} Bootstrap (1,000 item-level resamples with replacement) and delete-1 jackknife confidence intervals agree closely: width ratios range from 0.96 to 1.04 across all variance components. The agreement indi
…[truncated 12227 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 422 · 2026-05-22T13:03:43.551917+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 423 · 2026-05-22T13:03:44.004196+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	In our analysis of five benchmarks, item selection drives 34--38\% of evaluation variance on multiple-choice tasks while prompt wording is negligible ($<$3\%). On the free-form reasoning task GSM8K, the structure shifts: model$\times$prompt interaction alone accounts for approximately 9\%, while item selection drops to 17\%. These numbers, drawn from a factorial analysis of approximately 2.3 million evaluation records, reveal that the variance structure of LLM evaluation is not a fixed property of the pipeline but shifts qualitatively with the response format. Current evaluation practice treats variance sources as independent nuisance factors and controls them one at a time: one study perturbs prompts, another varies precision, a third changes item subsets. This piecemeal approach cannot capture interactions between sources, nor can it predict how the relative importance of each source changes across evaluation settings. Leaderboard rankings built on single-condition evaluations are therefore sensitive to methodological choices that remain unreported and uncontrolled \citep{rodriguez2021leaderboards, dehghani2021benchmark}. No unified factorial framework exists to decompose these sources simultaneously, quantify their interactions, and compare the resulting variance structure across benchmarks.
5	
6	Existing studies examine individual variance sources in isolation. \citet{sclar2024formatting} and BrittleBench \citep{brittlebench2026} documented 50--76\% accuracy swings from prompt formatting; \citet{yuan2025layercast} showed up to 9\% variation from numerical precision; \citet{pezeshkpour2024ordering}, \citet{dodge2020finetuning}, and \citet{henderson2018deep} documented ordering and hyperparameter sensitivity---each holding other factors fixed. \citet{messing2026hidden} applied G-theory to LLM evaluation across five methodology facets on a single benchmark (judge identity: 43.8\%), but excluded infrastructure
…[truncated 2944 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 424 · 2026-05-22T13:03:44.054860+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 425 · 2026-05-22T13:03:45.008423+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Our findings are bounded by several scope constraints. First, the eight models share the 2024--2025 instruction-tuning paradigm; temporal correlation may limit exchangeability, and results do not generalize to API-based, base, or $>$9B models. Second, the benchmark sample ($n = 5$) limits statistical power for the format-associated claim ($p = 0.10$); other formats (code generation, multi-turn dialogue) may differ. Third, binary scoring may understate format differences---partial-credit scoring could redistribute FF residual variance (40--44\%). Fourth, our design varies few-shot example ordering but not example identity, a known variance source. The reduced-crossing validation was performed on MMLU only; independent item resampling (three 200-item samples, CV = 3.1\%) likewise covers only MMLU.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 426 · 2026-05-22T13:03:45.008752+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 427 · 2026-05-22T13:03:45.059074+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Multi-facet designs require 10$\times$ fewer items than single-condition designs for $G \geq 0.80$ (55 vs.\ 552), confirmed across all five benchmarks (bootstrap CIs exceed 10$\times$); FF benchmarks show approximately 1.8$\times$ the gain ($\sim$21$\times$ vs.\ $\sim$12$\times$ for MC). We also observe a format-associated variance pattern: item-related variance concentrates at 68--72\% on MC benchmarks and disperses to 31--41\% on FF benchmarks---a descriptive observation whose confirmatory generalization requires additional benchmarks. BF16 and FP16 are interchangeable under binary scoring. For practitioners, even a minimal upgrade---two prompt variants---yields the steepest reliability gain per additional condition (Appendix~\ref{app:intermediate_dstudy}). Code, data, and a D-study budget calculator will be released upon publication.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 428 · 2026-05-22T13:03:45.109597+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 429 · 2026-05-22T13:03:45.210381+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Variance Decomposition in ML/NLP Evaluation.}
5	Factorial decomposition of evaluation variance has roots in the ML reproducibility literature. \citet{bouthillier2021accounting} introduced an ANOVA-based template that decomposes benchmark variance across implementation details, hyperparameters, and data splits, establishing that design choices account for a substantial share of reproducibility failures. Several subsequent studies applied similar decomposition logic to specific facets of model evaluation \citep{dodge2020finetuning, henderson2018deep, magnusson2023reproducibility}. \citet{messing2026hidden} brought Generalizability theory into LLM evaluation, decomposing variance across five methodology facets on a single benchmark; judge identity dominated at 43.8\%, with prompt$\times$judge interaction at 12.4\%. However, this study used a single benchmark, included no infrastructure facets such as numerical precision, and fixed the judge as an LLM evaluator rather than isolating other sources. \citet{madaan2024quantifying} proposed per-factor variance metrics for LLM evaluation benchmarks but did not cross factors simultaneously. \citet{blackwell2024towards} quantified uncertainty in benchmark scores, and \citet{qian2026benchmark} conducted systematic meta-evaluation of LLM benchmarks; \citet{burnell2023rethink} called for rethinking evaluation reporting standards in AI. Recently, G-theory has been applied to LLM-based writing assessment \citep{wei2025gtheory} and annotation reliability \citep{varannot2025gtheory}, but these studies address scoring consistency rather than benchmark evaluation variance. \citet{kunievsky2025intent} proposed an alternative decomposition that separates intent uncertainty, articulation variance, and model uncertainty, but this framework does not cross infrastructure and methodology facets in a factorial design. Our work extends these approaches by crossing seven facets across
…[truncated 3788 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 430 · 2026-05-22T13:05:23.094452+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 431 · 2026-05-22T13:05:23.199663+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 105
}
```

</details>

---


### Tool call

_source line 432 · 2026-05-22T13:05:33.890851+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 433 · 2026-05-22T13:05:33.891268+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_5/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 434 · 2026-05-22T13:08:25.471916+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 审稿意见：方法严谨性 + 实验有效性\n\n## 论文信息\n- **标题**: Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Analysis\n- **Venue**: EMNLP 2026 (ARR May cycle)\n- **审查侧重**: 方法严谨性 + 实验有效性\n\n---\n\n## Summary\n\n本文将 Generalizability Theory (G-theory) 应用于 LLM 评测的方差分解，使用 7 facets × 8 个开源 7-9B 模型 × 5 个 benchmark 的全交叉析因设计（~2.3M 记录）。核心发现：(1) 多 facet 设计所需 item 数量比单条件设计少 10×（55 vs 552 items for G≥0.80）；(2) MC benchmark 的 item-related variance 集中在 68-72%，FF benchmark 分散在 31-41%；(3) BF16/FP16 在 binary scoring 下精度可分离（<0.1% interaction）。论文提供了 D-study budget calculator 和实用工具包。方法论整体严谨、robustness checks 充分，但若干核心假设存在实质性问题。\n\n---\n\n## 总体评分\n\n**Overall Assessment: 3.5 — Borderline Conference**\n\n**一句话总结**: 方法论框架扎实、实验规模可观，但 quasi-random model facet 的理论辩护不足、format-associated pattern 的统计支撑薄弱（p=0.10, n=5），这两个问题共同削弱了核心 claims 的可信度，使论文在 Conference 和 Findings 之间。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | G-theory 应用正确，9 项 robustness checks 覆盖面广；但 model-as-random-facet 假设辩护不充分（W1），format-associated claim 统计功效不足（W2），D-study projection 外推假设未充分验证（W3） |\n| **Excitement** | 3/5 | 将成熟心理测量学框架引入 LLM 评测是有价值的方向，10× budget finding 有实用价值；但核心方法论（G-theory/ANOVA）本身并非新颖，最有趣的 format-associated finding 统计上未确认 |\n| **Reproducibility** | 4/5 | 设计矩阵、模型标识、prompt 模板、评估协议详细完整；承诺发布代码/数据/budget calculator；单 GPU 实验设置清晰可控 |\n| **Reviewer Confidence** | 4/5 | 熟悉 G-theory、心理测量学方法论、LLM 评测文献。仔细阅读了全文含附录 |\n\n---\n\n## 主要优势 (Strengths)\n\n**S1. 系统性的多 facet 交叉设计**\n同时交叉 7 个 facets 是本领域首次，相比 Messing (2026) 的 5 facets 单 benchmark、Madaan et al. (2024) 的逐因素分析，本文的设计能捕获 interaction effects。Table 1 的设计矩阵清晰，Figure 1 的设计图有效传达了交叉结构。\n\n**S2. Robustness checks 覆盖面广且诚实**\n9 项分析（GLMM, probit simulation, accuracy-range stability, estimator comparison, CI method, facet specification, LOMO, null calibration, reduced crossing validation）系统地检验了方法论选择的稳健性。特别是 null calibration（100 Bernoulli replications，item variance 0.08% vs 观测 58.4%）有说服力。\n\n**S3. 对 claims 的适度表述**\n论文在多处正确地 hedge 了结论——benchmark-level CI spanning zero（[-1.7, 5.1]）、p=0.10 的 permutation test、\"descriptive observation\" 的措辞（§4.3, Conclusion）。这种诚实态度值得肯定。\n\n**S4. 实用性贡献**\nD-study budget calculator、intermediate design gradient（Appendix B, Table 7: 从 single-condition 到 full multi-facet 的渐进升级路径）、\"minimal upgrade\" 建议（3p×3s, G_200=0.818）对实践者直接有用。\n\n**S5. IRT 互补性的展示**\nTable 4 展示 IRT-selected 116 items 在 single-condition 下 G=0.457 vs multi-facet 下 G=0.895，清晰论证了 item selection 和 protocol optimization 的正交互补关系。\n\n**S6. Text-exact-match 的对照实验**\n§4.1 报告 text-exact-match scoring 下 G=0.007（temperature 占 79.7%），与 binary scoring 的 G=0.936 形成鲜明对比，有力地展示了 scoring metric 对 variance structure 的根本影响，也为后续分析限定在 binary scoring 提供了合理依据。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1 [critical] Quasi-random model facet: 8 purposively selected models 作为 random facet 的理论辩护不充分**\n\n- **具体位置**: §3.6 (method.tex), §3.2, Appendix A (LOMO)\n- **问题**: G-theory 的基本要求是 facets 为从 admissible universe 中 **随机抽样** 的条件（Shavelson & Webb, 1991; Brennan, 2001, Ch. 2）。论文选择了 8 个模型，每个来自不同 architecture family（\"purposive stratified sampling\"），然后声称这构成 \"quasi-random facet\"。这在根本上违反了 G-theory 的抽样前提：\n  - **零 within-family replication**: 每个 architecture family 仅 1 个模型，无法评估 family-within-model variance\n  - **LOMO 功效极低**: 8 个 leave-one-out subsets（each n=7）无法可靠检测 model-specific distortion；G_item 范围 0.877-0.889（span=0.012）可能仅反映统计噪声\n  - **四模型子集验证是循环论证**: 从同一 8 个模型中抽 4 个，预测 8 模型的 G（Δ=0.003），只证明了这 8 个模型的 **内部一致性**，不证明它们代表更广的 universe\n  - Cross-benchmark LOMO（Table 5）只展示了 DeepSeek 一个模型的 removal effect，而非所有 8 个模型在所有 5 个 benchmark 上的完整矩阵\n- **为什么影响接收**: 所有 G coefficients 和 D-study projections 都假设 model 是 random facet。若 models 实际上是 fixed facet（或 convenience sample），σ²_pM 会从 error term 转入 fixed structure，G coefficients 被高估，D-study budgets 被低估。这影响论文的全部三个核心 contributions。\n- **建议修改方向**: (a) 增加 within-family replication（如 Llama-3.1-8B + Llama-3.2-3B + Llama-3.3-70B）以评估 family variance；(b) 或者明确将 model 作为 fixed facet 重新分析，报告 fixed-model G coefficients 作为下界；(c) 或者引入 Bayesian variance component estimation（如 Jiang & Skorupski, 2018 已被引用）以量化 model facet 的不确定性；(d) 至少展示完整的 8-model × 5-benchmark LOMO 矩阵而非仅 DeepSeek。\n\n**N2 [critical] Format-associated pattern 的统计支撑不足以作为核心贡献**\n\n- **具体位置**: §4.3, Abstract, §1 (Contributions), §5 (Conclusion)\n- **问题**: MC (68-72%) vs FF (31-41%) 的 format-associated pattern 基于 **n=5 benchmarks (3 MC + 2 FF)**：\n  - Exhaustive permutation test p=0.10（C(5,3)=10 partitions 的分辨率下限），无法在任何常规显著性水平下拒绝零假设\n  - Benchmark-level CI spans zero: [-1.7, 5.1], df=3\n  - Item-level effect size d=1.73 **混淆了分析单位**——claim 是关于 benchmarks（n=5）的，但 d 是 item-level 的，这不能替代 benchmark-level 的统计推断\n  - 两组仅有 2-3 个样本（2 FF, 3 MC），一个 outlier（如 HellaSwag 的 item < model×item）就能改变结论\n- **为什么影响接收**: 这是论文的第二核心发现（占据 §4.3 整节 + abstract + conclusion 的显著篇幅），但统计上无法与随机分配区分。论文在部分位置正确 hedge（\"descriptive observation\"），但 abstract 和 contributions list 的措辞仍然过于确定。\n- **建议修改方向**: (a) 增加 benchmarks（如 HumanEval, TriviaQA, WinoGrande 等）以提高统计功效；(b) 或者将 format-associated pattern 从 \"contribution\" 降级为 \"observation / preliminary finding\"，在 abstract 和 contributions 中相应调整措辞；(c) 提供 benchmark-level power analysis：在 n=5, 3 vs 2 分割下，能在 α=0.05 检测到多大的效应？\n\n**N3 [critical] D-study projection 的外推假设强度未充分讨论**\n\n- **具体位置**: §4.5, Table 4, Appendix B (Table 6)\n- **问题**: D-study 假设 variance components 在改变条件数量时保持不变。这个假设在论文中未被充分验证：\n  - Single-model → cross-model 时，MMLU 的 item budget 从 55 跳到 93（69% 增长），说明 variance components 对设计变化敏感\n  - Cross-model projections（Table 6）从 8 模型外推——若增加到 16 或 32 个模型，variance decomposition 可能系统性变化（更多 model×item variance 会被引入），但这未被测试\n  - §4.6 的 scale validation（Qwen2.5 3B/7B, within-family）展示了 item dominance 的一致性，但 G_item 从 0.963/0.956（single-model）降到 0.71（2-model crossed），表明 **模型数量根本性地改变了 G coefficient**，D-study 的 projection 未能预测到这一变化\n  - 四模型子集 D-study（Δ=0.003）仍在同一 universe 内，不构成对外推有效性的强检验\n- **为什么影响接收**: D-study reproducibility budgets 是论文的第一核心贡献（title 中就有 \"Reproducibility Budgets\"）。如果 budgets 对设计变化不稳定，practitioners 按照这些数字设计实验可能得到 misleading 的 reliability estimates。\n- **建议修改方向**: (a) 明确讨论 projection 假设及其局限性（variance component invariance）；(b) 展示 bootstrapped D-study 在不同模型子集大小（4, 6, 8）下的 budget 变化，量化 projection sensitivity；(c) 在 Table 4/6 旁添加 caveat：这些 budgets 仅在所观察的 model universe (8 models, 7-9B, instruction-tuned) 内验证。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1 [warning] \"Item-related variance\" bundling 在 LLM context 下的解释性问题**\n\n- **具体位置**: §3.1, §4.3\n- **问题**: σ²_p（item difficulty，跨模型一致）和 σ²_pM（model×item interaction / DIF，跨模型不一致）在概念上截然不同。前者意味着某些 item 普遍难，后者意味着不同模型在不同 item 上表现异质。论文承认这是 \"dual interpretation\"（§3.1），但主叙事仍以 bundled 指标推动 format-associated pattern。HellaSwag 的 σ²_pM (36.0%) > σ²_p (34.3%) 说明 bundling 可能掩盖重要的 within-format heterogeneity。\n- **建议**: 在 Table 3 和 Figure 2 中同时展示 bundled 和 unbundled 的 MC/FF 比较；在 §4.3 的 format-associated narrative 中明确区分 \"item difficulty gap\" 和 \"DIF gap\" 的贡献。\n\n**W2 [warning] Scale validation 范围过窄（3B-9B, single family）**\n\n- **具体位置**: §4.6\n- **问题**: 仅用 Qwen2.5 3B/7B（within-family）验证 scale invariance。3B-9B 是极窄的范围，且在同一 architecture family 内。当前 LLM 评测的实际需求涵盖 1B-70B+ 以及 API-based models。论文声称 \"item difficulty remains dominant across scales (3B-9B)\" 但这个 range 不足以支持一般性结论。\n- **建议**: 至少增加一个 cross-family scale comparison（如 Llama-8B vs DeepSeek-67B），或者将 scale validation 的 claim 范围限制为 \"within the 3B-9B range of a single architecture family\"。\n\n**W3 [warning] Precision separability claim 的适用范围未充分界定**\n\n- **具体位置**: §4.4\n- **问题**: <0.1% interaction 仅覆盖 BF16/FP16/FP32——均为 full/half precision。实践中广泛使用的 4-bit/8-bit quantization（GPTQ, AWQ, GGUF）未被包含。Practitioners 可能将 \"precision doesn't matter\" 过度泛化到 quantized models，而 quantization 可能引入显著更大的 variance。\n- **建议**: 在 §4.4 明确限定 claim 为 \"full/half-precision formats (BF16, FP16, FP32)\"，并在 limitations 中提及 quantization 未被覆盖。\n\n**W4 [warning] Reduced crossing validation 仅在 MMLU 上执行**\n\n- **具体位置**: Appendix A (Reduced crossing validation), Limitations\n- **问题**: exp-002 在 5 个 benchmark 上使用 reduced crossing（BF16 only × 2 temperatures），但验证 exp-001 → exp-002 的 variance structure preservation 仅在 MMLU 上执行（ΔG=0.0008）。10pp 的 item variance share redistribution（58.4% → 68.5%）是实质性的，在 FF benchmarks 上可能表现不同（FF 的 precision 和 temperature interactions 可能更大）。\n- **建议**: 至少在一个 FF benchmark（GSM8K 或 MATH）上复制 reduced crossing validation。\n\n**W5 [warning] 200-item stratified sample 的代表性未充分验证**\n\n- **具体位置**: §3.2\n- **问题**: 200 items 从 MMLU 57 个 subjects 中选取 10 个（每个 20 items），覆盖 10/57=17.5% 的 subjects 和 200/14042=1.4% 的 items。三次独立 200-item resampling（CV=3.1%）仅在 MMLU 上执行，且都使用了相同的 10-subject stratification。未验证这 10 个 subjects 是否代表完整的 57-subject 分布（difficulty range, domain balance 等）。\n- **建议**: 报告所选 10 subjects 的 mean accuracy 相对于完整 57 subjects 的位置；或额外抽取 10 个不同 subjects 的样本以验证 subject selection robustness。\n\n**W6 [warning] FF benchmarks 的高 residual variance (40-44%) 未被充分解释**\n\n- **具体位置**: §4.3, Table 3\n- **问题**: GSM8K (39.9%) 和 MATH (43.9%) 的 residual 是各自最大的 variance component，但论文仅用一句话解释（\"chain-of-thought path diversity and answer extraction variability\"）。如果近一半的 variance 无法归因于任何已设计的 facet，这对 D-study projection 的可靠性构成威胁——residual 中可能包含未建模的系统性 variance source。\n- **建议**: 讨论 residual 的可能构成（generation randomness beyond temperature, answer extraction error, prompt×seed×item higher-order interactions 等）；考虑是否可通过增加 facets 或更精细的 scoring 来减少 residual。\n\n---\n\n## Questions（需要作者回答）\n\n**Q1.** D-study projections 对模型选择的敏感度如何？你们展示了 4-model subset stability（Δ=0.003），但如果使用完全不同的 8 个模型（不同 families），projections 是否还能成立？\n\n**Q2.** 对于 format-associated pattern，能否提供 benchmark-level power analysis？在 n=5 (3 vs 2) 的设计下，α=0.05 能检测到多大的效应？\n\n**Q3.** FF benchmarks 的 40-44% residual 具体包含哪些来源？是否可以通过增加 generation sampling（如 5 次 generation per condition）来分离 generation randomness？\n\n**Q4.** §4.6 的 scale validation 中，2-model crossed design 的 G=0.71 远低于 8-model 的 G=0.896。这是否意味着 G coefficient 对模型数量不是单调递增的，或者 2-model 是特殊情况？D-study 能否准确预测这一变化？\n\n**Q5.** Henderson Method I 的 unbiased property（Brennan 2001, Ch. 12）是否要求 balanced design？exp-002 中 ordering facet 对非 MMLU benchmarks \"structurally inert\"（σ²=0 by construction），这是否违反了 balanced design 的假设？\n\n**Q6.** Binary scoring 将 partial credit 折叠为 0/1。你们在 limitations 中提到 partial-credit scoring 可能 redistribute FF residual variance。是否可以用 MMLU 的 subject-level accuracy（而非 item-level binary）作为 continuous outcome 进行一次验证性分析？\n\n---\n\n## Missing References\n\n1. **Measurement invariance 文献**（Meredith, 1993; Putnick & Bornstein, 2016）——如果不同模型对 items 不具有 measurement invariance，将它们作为 exchangeable random facet 的前提就不成立。与 W1/N1 直接相关。\n\n2. **Multi-level modeling for LLM evaluation**——items nested within subjects within domains 的层级结构可用 HLM/MLM 更自然地建模，而非假设 fully crossed。\n\n3. **Bootstrapping for ANOVA variance components 的统计理论**——论文引用了 Li (2023) 但未讨论 binary data + ANOVA bootstrap 的 coverage properties。Efron & Tibshirani (1993) 关于 bootstrap CI for variance components 的 cautionary notes 值得提及。\n\n4. **Song et al. (2025) \"Large language model psychometrics\"**（已在 references.bib 中引用但正文引用位置可更突出）——直接讨论了 LLM evaluation 的心理测量学属性。\n\n---\n\n## Minor Issues\n\n1. Table 3 caption 中 \"Prompt row\" 的非对称报告（MC 报 prompt×item interaction, FF 报 prompt main effect）使跨格式比较容易产生误导。建议统一报告方式或在表内用脚注说明。\n\n2. §3.3: ordering facet 对非 MMLU benchmarks \"structurally inert (σ²_ordering = 0 by construction)\" 是设计约束而非实证发现，应更清晰地标注。\n\n3. Figure 1 在印刷尺寸下较小，建议增大字号或简化为关键 facets。\n\n4. Title 中 \"Reproducibility Budgets\" 可能 oversell——这些是特定 model universe 和 scoring metric 下的 item budgets for target G，并非全面的 reproducibility guarantees。\n\n5. Abstract 第二句 \"no unified factorial framework exists\" 过于绝对——Bouthillier et al. (2021) 和 Messing (2026) 已有 factorial/G-theory frameworks，本文的贡献在于 **扩展**（更多 facets + cross-benchmark），而非首创。\n\n6. §4.3 中 within-MMLU correlation（ρ=0.806, p=0.005, n=10 subjects）和 cross-benchmark correlation（ρ=0.82, p=0.089, n=5）方向一致但后者不显著。将两者并列可能给读者造成 cross-benchmark relationship 已被 confirmed 的印象。\n\n---\n\n## Overall Assessment 理由\n\n**评分: 3.5 (Borderline Conference)**\n\n本文将 G-theory 系统地应用于 LLM 评测的方差分解，实验规模可观（2.3M records），robustness checks 覆盖面广，实用工具贡献明确。10× budget finding 和 precision separability 有直接实践价值。\n\n但三个核心方法论问题阻止我推荐 conference acceptance：(1) quasi-random model facet 假设——8 个 purposively selected models 不满足 G-theory 的 random sampling 前提，且验证手段（LOMO with n=8, 4-model subset）功效不足；(2) format-associated pattern——n=5, p=0.10，在 contributions 和 abstract 中的 framing 超出了统计支撑的强度；(3) D-study projection 的外推假设——variance component invariance 未被充分验证，single-model → cross-model 已显示实质性变化。\n\n如果作者能 (a) 增加 model facet 的 within-family replication 或提供 fixed-model 分析，(b) 将 format-associated pattern 降级为 preliminary observation，(c) 更充分地讨论 D-study projection 的假设边界，本文可达到 Conference 水平。当前状态适合 Findings。\n",
  "reviewer_id": "1",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 审稿意见：方法严谨性 + 实验有效性\n\n## 论文信息\n- **标题**: Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Analysis\n- **Venue**: EMNLP 2026 (ARR May cycle)\n- **审查侧重**: 方法严谨性 + 实验有效性\n\n---\n\n## Summary\n\n本文将 Generalizability Theory (G-theory) 应用于 LLM 评测的方差分解，使用 7 facets × 8 个开源 7-9B 模型 × 5 个 benchmark 的全交叉析因设计（~2.3M 记录）。核心发现：(1) 多 facet 设计所需 item 数量比单条件设计少 10×（55 vs 552 items for G≥0.80）；(2) MC benchmark 的 item-related variance 集中在 68-72%，FF benchmark 分散在 31-41%；(3) BF16/FP16 在 binary scoring 下精度可分离（<0.1% interaction）。论文提供了 D-study budget calculator 和实用工具包。方法论整体严谨、robustness checks 充分，但若干核心假设存在实质性问题。\n\n---\n\n## 总体评分\n\n**Overall Assessment: 3.5 — Borderline Conference**\n\n**一句话总结**: 方法论框架扎实、实验规模可观，但 quasi-random model facet 的理论辩护不足、format-associated pattern 的统计支撑薄弱（p=0.10, n=5），这两个问题共同削弱了核心 claims 的可信度，使论文在 Conference 和 Findings 之间。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | G-theory 应用正确，9 项 robustness checks 覆盖面广；但 model-as-random-facet 假设辩护不充分（W1），format-associated claim 统计功效不足（W2），D-study projection 外推假设未充分验证（W3） |\n| **Excitement** | 3/5 | 将成熟心理测量学框架引入 LLM 评测是有价值的方向，10× budget finding 有实用价值；但核心方法论（G-theory/ANOVA）本身并非新颖，最有趣的 format-associated finding 统计上未确认 |\n| **Reproducibility** | 4/5 | 设计矩阵、模型标识、prompt 模板、评估协议详细完整；承诺发布代码/数据/budget calculator；单 GPU 实验设置清晰可控 |\n| **Reviewer Confidence** | 4/5 | 熟悉 G-theory、心理测量学方法论、LLM 评测文献。仔细阅读了全文含附录 |\n\n---\n\n## 主要优势 (Strengths)\n\n**S1. 系统性的多 facet 交叉设计**\n同时交叉 7 个 facets 是本领域首次，相比 Messing (2026) 的 5 facets 单 benchmark、Madaan et al. (2024) 的逐因素分析，本文的设计能捕获 interaction effects。Table 1 的设计矩阵清晰，Figure 1 的设计图有效传达了交叉结构。\n\n**S2. Robustness checks 覆盖面广且诚实**\n9 项分析（GLMM, probit simulation, accuracy-range stability, estimator comparison, CI method, facet specification, LOMO, null calibration, reduced crossing validation）系统地检验了方法论选择的稳健性。特别是 null calibration（100 Bernoulli replications，item variance 0.08% vs 观测 58.4%）有说服力。\n\n**S3. 对 claims 的适度表述**\n论文在多处正确地 hedge 了结论——benchmark-level CI spanning zero（[-1.7, 5.1]）、p=0.10 的 permutation test、\"descriptive observation\" 的措辞（§4.3, Conclusion）。这种诚实态度值得肯定。\n\n**S4. 实用性贡献**\nD-study budget calculator、intermediate design gradient（Appendix B, Table 7: 从 single-condition 到 full multi-facet 的渐进升级路径）、\"minimal upgrade\" 建议（3p×3s, G_200=0.818）对实践者直接有用。\n\n**S5. IRT 互补性的展示**\nTable 4 展示 IRT-selected 116 items 在 single-condition 下 G=0.457 vs multi-facet 下 G=0.895，清晰论证了 item selection 和 protocol optimization 的正交互补关系。\n\n**S6. Text-exact-match 的对照实验**\n§4.1 报告 text-exact-match scoring 下 G=0.007（temperature 占 79.7%），与 binary scoring 的 G=0.936 形成鲜明对比，有力地展示了 scoring metric 对 variance structure 的根本影响，也为后续分析限定在 binary scoring 提供了合理依据。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1 [critical] Quasi-random model facet: 8 purposively selected models 作为 random facet 的理论辩护不充分**\n\n- **具体位置**: §3.6 (method.tex), §3.2, Appendix A (LOMO)\n- **问题**: G-theory 的基本要求是 facets 为从 admissible universe 中 **随机抽样** 的条件（Shavelson & Webb, 1991; Brennan, 2001, Ch. 2）。论文选择了 8 个模型，每个来自不同 architecture family（\"purposive stratified sampling\"），然后声称这构成 \"quasi-random facet\"。这在根本上违反了 G-theory 的抽样前提：\n  - **零 within-family replication**: 每个 architecture family 仅 1 个模型，无法评估 family-within-model variance\n  - **LOMO 功效极低**: 8 个 leave-one-out subsets（each n=7）无法可靠检测 model-specific distortion；G_item 范围 0.877-0.889（span=0.012）可能仅反映统计噪声\n  - **四模型子集验证是循环论证**: 从同一 8 个模型中抽 4 个，预测 8 模型的 G（Δ=0.003），只证明了这 8 个模型的 **内部一致性**，不证明它们代表更广的 universe\n  - Cross-benchmark LOMO（Table 5）只展示了 DeepSeek 一个模型的 removal effect，而非所有 8 个模型在所有 5 个 benchmark 上的完整矩阵\n- **为什么影响接收**: 所有 G coefficients 和 D-study projections 都假设 model 是 random facet。若 models 实际上是 fixed facet（或 convenience sample），σ²_pM 会从 error term 转入 fixed structure，G coefficients 被高估，D-study budgets 被低估。这影响论文的全部三个核心 contributions。\n- **建议修改方向**: (a) 增加 within-family replication（如 Llama-3.1-8B + Llama-3.2-3B + Llama-3.3-70B）以评估 family variance；(b) 或者明确将 model 作为 fixed facet 重新分析，报告 fixed-model G coefficients 作为下界；(c) 或者引入 Bayesian variance component estimation（如 Jiang & Skorupski, 2018 已被引用）以量化 model facet 的不确定性；(d) 至少展示完整的 8-model × 5-benchmark LOMO 矩阵而非仅 DeepSeek。\n\n**N2 [critical] Format-associated pattern 的统计支撑不足以作为核心贡献**\n\n- **具体位置**: §4.3, Abstract, §1 (Contributions), §5 (Conclusion)\n- **问题**: MC (68-72%) vs FF (31-41%) 的 format-associated pattern 基于 **n=5 benchmarks (3 MC + 2 FF)**：\n  - Exhaustive permutation test p=0.10（C(5,3)=10 partitions 的分辨率下限），无法在任何常规显著性水平下拒绝零假设\n  - Benchmark-level CI spans zero: [-1.7, 5.1], df=3\n  - Item-level effect size d=1.73 **混淆了分析单位**——claim 是关于 benchmarks（n=5）的，但 d 是 item-level 的，这不能替代 benchmark-level 的统计推断\n  - 两组仅有 2-3 个样本（2 FF, 3 MC），一个 outlier（如 HellaSwag 的 item < model×item）就能改变结论\n- **为什么影响接收**: 这是论文的第二核心发现（占据 §4.3 整节 + abstract + conclusion 的显著篇幅），但统计上无法与随机分配区分。论文在部分位置正确 hedge（\"descriptive observation\"），但 abstract 和 contributions list 的措辞仍然过于确定。\n- **建议修改方向**: (a) 增加 benchmarks（如 HumanEval, TriviaQA, WinoGrande 等）以提高统计功效；(b) 或者将 format-associated pattern 从 \"contribution\" 降级为 \"observation / preliminary finding\"，在 abstract 和 contributions 中相应调整措辞；(c) 提供 benchmark-level power analysis：在 n=5, 3 vs 2 分割下，能在 α=0.05 检测到多大的效应？\n\n**N3 [critical] D-study projection 的外推假设强度未充分讨论**\n\n- **具体位置**: §4.5, Table 4, Appendix B (Table 6)\n- **问题**: D-study 假设 variance components 在改变条件数量时保持不变。这个假设在论文中未被充分验证：\n  - Single-model → cross-model 时，MMLU 的 item budget 从 55 跳到 93（69% 增长），说明 variance components 对设计变化敏感\n  - Cross-model projections（Table 6）从 8 模型外推——若增加到 16 或 32 个模型，variance decomposition 可能系统性变化（更多 model×item variance 会被引入），但这未被测试\n  - §4.6 的 scale validation（Qwen2.5 3B/7B, within-family）展示了 item dominance 的一致性，但 G_item 从 0.963/0.956（single-model）降到 0.71（2-model crossed），表明 **模型数量根本性地改变了 G coefficient**，D-study 的 projection 未能预测到这一变化\n  - 四模型子集 D-study（Δ=0.003）仍在同一 universe 内，不构成对外推有效性的强检验\n- **为什么影响接收**: D-study reproducibility budgets 是论文的第一核心贡献（title 中就有 \"Reproducibility Budgets\"）。如果 budgets 对设计变化不稳定，practitioners 按照这些数字设计实验可能得到 misleading 的 reliability estimates。\n- **建议修改方向**: (a) 明确讨论 projection 假设及其局限性（variance component invariance）；(b) 展示 bootstrapped D-study 在不同模型子集大小（4, 6, 8）下的 budget 变化，量化 projection sensitivity；(c) 在 Table 4/6 旁添加 caveat：这些 budgets 仅在所观察的 model universe (8 models, 7-9B, instruction-tuned) 内验证。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1 [warning] \"Item-related variance\" bundling 在 LLM context 下的解释性问题**\n\n- **具体位置**: §3.1, §4.3\n- **问题**: σ²_p（item difficulty，跨模型一致）和 σ²_pM（model×item interaction / DIF，跨模型不一致）在概念上截然不同。前者意味着某些 item 普遍难，后者意味着不同模型在不同 item 上表现异质。论文承认这是 \"dual interpretation\"（§3.1），但主叙事仍以 bundled 指标推动 format-associated pattern。HellaSwag 的 σ²_pM (36.0%) > σ²_p (34.3%) 说明 bundling 可能掩盖重要的 within-format heterogeneity。\n- **建议**: 在 Table 3 和 Figure 2 中同时展示 bundled 和 unbundled 的 MC/FF 比较；在 §4.3 的 format-associated narrative 中明确区分 \"item difficulty gap\" 和 \"DIF gap\" 的贡献。\n\n**W2 [warning] Scale validation 范围过窄（3B-9B, single family）**\n\n- **具体位置**: §4.6\n- **问题**: 仅用 Qwen2.5 3B/7B（within-family）验证 scale invariance。3B-9B 是极窄的范围，且在同一 architecture family 内。当前 LLM 评测的实际需求涵盖 1B-70B+ 以及 API-based models。论文声称 \"item difficulty remains dominant across scales (3B-9B)\" 但这个 range 不足以支持一般性结论。\n- **建议**: 至少增加一个 cross-family scale comparison（如 Llama-8B vs DeepSeek-67B），或者将 scale validation 的 claim 范围限制为 \"within the 3B-9B range of a single architecture family\"。\n\n**W3 [warning] Precision separability claim 的适用范围未充分界定**\n\n- **具体位置**: §4.4\n- **问题**: <0.1% interaction 仅覆盖 BF16/FP16/FP32——均为 full/half precision。实践中广泛使用的 4-bit/8-bit quantization（GPTQ, AWQ, GGUF）未被包含。Practitioners 可能将 \"precision doesn't matter\" 过度泛化到 quantized models，而 quantization 可能引入显著更大的 variance。\n- **建议**: 在 §4.4 明确限定 claim 为 \"full/half-precision formats (BF16, FP16, FP32)\"，并在 limitations 中提及 quantization 未被覆盖。\n\n**W4 [warning] Reduced crossing validation 仅在 MMLU 上执行**\n\n- **具体位置**: Appendix A (Reduced crossing validation), Limitations\n- **问题**: exp-002 在 5 个 benchmark 上使用 reduced crossing（BF16 only × 2 temperatures），但验证 exp-001 → exp-002 的 variance structure preservation 仅在 MMLU 上执行（ΔG=0.0008）。10pp 的 item variance share redistribution（58.4% → 68.5%）是实质性的，在 FF benchmarks 上可能表现不同（FF 的 precision 和 temperature interactions 可能更大）。\n- **建议**: 至少在一个 FF benchmark（GSM8K 或 MATH）上复制 reduced crossing validation。\n\n**W5 [warning] 200-item stratified sample 的代表性未充分验证**\n\n- **具体位置**: §3.2\n- **问题**: 200 items 从 MMLU 57 个 subjects 中选取 10 个（每个 20 items），覆盖 10/57=17.5% 的 subjects 和 200/14042=1.4% 的 items。三次独立 200-item resampling（CV=3.1%）仅在 MMLU 上执行，且都使用了相同的 10-subject stratification。未验证这 10 个 subjects 是否代表完整的 57-subject 分布（difficulty range, domain balance 等）。\n- **建议**: 报告所选 10 subjects 的 mean accuracy 相对于完整 57 subjects 的位置；或额外抽取 10 个不同 subjects 的样本以验证 subject selection robustness。\n\n**W6 [warning] FF benchmarks 的高 residual variance (40-44%) 未被充分解释**\n\n- **具体位置**: §4.3, Table 3\n- **问题**: GSM8K (39.9%) 和 MATH (43.9%) 的 residual 是各自最大的 variance component，但论文仅用一句话解释（\"chain-of-thought path diversity and answer extraction variability\"）。如果近一半的 variance 无法归因于任何已设计的 facet，这对 D-study projection 的可靠性构成威胁——residual 中可能包含未建模的系统性 variance source。\n- **建议**: 讨论 residual 的可能构成（generation randomness beyond temperature, answer extraction error, prompt×seed×item higher-order interactions 等）；考虑是否可通过增加 facets 或更精细的 scoring 来减少 residual。\n\n---\n\n## Questions（需要作者回答）\n\n**Q1.** D-study projections 对模型选择的敏感度如何？你们展示了 4-model subset stability（Δ=0.003），但如果使用完全不同的 8 个模型（不同 families），projections 是否还能成立？\n\n**Q2.** 对于 format-associated pattern，能否提供 benchmark-level power analysis？在 n=5 (3 vs 2) 的设计下，α=0.05 能检测到多大的效应？\n\n**Q3.** FF benchmarks 的 40-44% residual 具体包含哪些来源？是否可以通过增加 generation sampling（如 5 次 generation per condition）来分离 generation randomness？\n\n**Q4.** §4.6 的 scale validation 中，2-model crossed design 的 G=0.71 远低于 8-model 的 G=0.896。这是否意味着 G coefficient 对模型数量不是单调递增的，或者 2-model 是特殊情况？D-study 能否准确预测这一变化？\n\n**Q5.** Henderson Method I 的 unbiased property（Brennan 2001, Ch. 12）是否要求 balanced design？exp-002 中 ordering facet 对非 MMLU benchmarks \"structurally inert\"（σ²=0 by construction），这是否违反了 balanced design 的假设？\n\n**Q6.** Binary scoring 将 partial credit 折叠为 0/1。你们在 limitations 中提到 partial-credit scoring 可能 redistribute FF residual variance。是否可以用 MMLU 的 subject-level accuracy（而非 item-level binary）作为 continuous outcome 进行一次验证性分析？\n\n---\n\n## Missing References\n\n1. **Measurement invariance 文献**（Meredith, 1993; Putnick & Bornstein, 2016）——如果不同模型对 items 不具有 measurement invariance，将它们作为 exchangeable random facet 的前提就不成立。与 W1/N1 直接相关。\n\n2. **Multi-level modeling for LLM evaluation**——items nested within subjects within domains 的层级结构可用 HLM/MLM 更自然地建模，而非假设 fully crossed。\n\n3. **Bootstrapping for ANOVA variance components 的统计理论**——论文引用了 Li (2023) 但未讨论 binary data + ANOVA bootstrap 的 coverage properties。Efron & Tibshirani (1993) 关于 bootstrap CI for variance components 的 cautionary notes 值得提及。\n\n4. **Song et al. (2025) \"Large language model psychometrics\"**（已在 references.bib 中引用但正文引用位置可更突出）——直接讨论了 LLM evaluation 的心理测量学属性。\n\n---\n\n## Minor Issues\n\n1. Table 3 caption 中 \"Prompt row\" 的非对称报告（MC 报 prompt×item interaction, FF 报 prompt main effect）使跨格式比较容易产生误导。建议统一报告方式或在表内用脚注说明。\n\n2. §3.3: ordering facet 对非 MMLU benchmarks \"structurally inert (σ²_ordering = 0 by construction)\" 是设计约束而非实证发现，应更清晰地标注。\n\n3. Figure 1 在印刷尺寸下较小，建议增大字号或简化为关键 facets。\n\n4. Title 中 \"Reproducibility Budgets\" 可能 oversell——这些是特定 model universe 和 scoring metric 下的 item budgets for target G，并非全面的 reproducibility guarantees。\n\n5. Abstract 第二句 \"no unified factorial framework exists\" 过于绝对——Bouthillier et al. (2021) 和 Messing (2026) 已有 factorial/G-theory frameworks，本文的贡献在于 **扩展**（更多 facets + cross-benchmark），而非首创。\n\n6. §4.3 中 within-MMLU correlation（ρ=0.806, p=0.005, n=10 subjects）和 cross-benchmark correlation（ρ=0.82, p=0.089, n=5）方向一致但后者不显著。将两者并列可能给读者造成 cross-benchmark relationship 已被 confirmed 的印象。\n\n---\n\n## Overall Assessment 理由\n\n**评分: 3.5 (Borderline Conference)**\n\n本文将 G-theory 系统地应用于 LLM 评测的方差分解，实验规模可观（2.3M records），robustness checks 覆盖面广，实用工具贡献明确。10× budget finding 和 precision separability 有直接实践价值。\n\n但三个核心方法论问题阻止我推荐 conference acceptance：(1) quasi-random model facet 假设——8 个 purposively selected models 不满足 G-theory 的 random sampling 前提，且验证手段（LOMO with n=8, 4-model subset）功效不足；(2) format-associated pattern——n=5, p=0.10，在 contributions 和 abstract 中的 framing 超出了统计支撑的强度；(3) D-study projection 的外推假设——variance component invariance 未被充分验证，single-model → cross-model 已显示实质性变化。\n\n如果作者能 (a) 增加 model facet 的 within-family replication 或提供 fixed-model 分析，(b) 将 format-associated pattern 降级为 preliminary observation，(c) 更充分地讨论 D-study projection 的假设边界，本文可达到 Conference 水平。当前状态适合 Findings。\n",
    "reviewer_id": "1",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 435 · 2026-05-22T13:08:29.289735+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3817
}
```

</details>

---


### Assistant

_source line 436 · 2026-05-22T13:08:42.148143+00:00_

审稿意见已提交给 Review Director。

**审稿结果概要**：

- **Overall: 3.5 (Borderline Conference)**
- Soundness 3.5 | Excitement 3 | Reproducibility 4 | Confidence 4

**三个 Must-Fix 问题**：
1. **N1**: 8 个 purposively selected models 作为 quasi-random facet 的理论辩护不充分——零 within-family replication、LOMO 功效低、四模型验证是循环论证
2. **N2**: Format-associated pattern (MC 68-72% vs FF 31-41%) 统计支撑不足——n=5 benchmarks, p=0.10, benchmark-level CI 包含零
3. **N3**: D-study projection 外推假设强度未充分讨论——variance component invariance 未验证，single→cross-model 时 budget 变化 69%

**六个 Should-Fix 问题** 涵盖 item-related variance bundling 的解释性问题、scale validation 范围过窄（3B-9B single family）、precision separability 未覆盖 quantization、reduced crossing validation 仅在 MMLU 执行、200-item sample 代表性、FF residual variance (40-44%) 解释不足。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1"
}
```

</details>

---


## Round 12

## Round 12

4 recorded events


### User

_source line 437 · 2026-05-22T13:09:21.540054+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见（侧重新颖性 + 完整性 + 写作质量），请逐条回应。

对每个 Strength/Weakness/Question，标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。特别关注你们是否在核心问题上达成一致。

---

## Reviewer 2 审稿意见 — Round 1 (新颖性 + 完整性 + 写作质量)

### 总体评分
**Overall**: 3.0 — Findings

### Summary
本文将 Generalizability theory 应用于开源 LLM 评测，在 8 个 7-9B 模型和 5 个 benchmark 上交叉最多 7 个 facet（约 230 万条记录），进行方差分解。主要发现：(1) MC benchmark 上 item-related variance 集中在 68-72%，FF benchmark 分散至 31-41%；(2) Multi-facet 设计比 single-condition 需要 10× 更少的 items 达到 G≥0.80；(3) BF16/FP16 在 binary scoring 下可互换。

### Must-Fix 问题

**N1** [critical] **与 Messing (2026) 的增量贡献界定不充分**
- Messing (2026, arXiv:2604.11581) 已将 G-theory 引入 LLM evaluation（TEE 框架），同样考虑了 prompt/temperature/judge 的 variance 和 design-study projections。当前 §2 仅一句话区分（"fix the judge + multiple benchmarks"），低估了 Messing 的工作范围。如果无法清楚论证实质性增量贡献，新颖性不足以支撑 conference-level 接收。

**N2** [critical] **Format-associated pattern 统计功效不足，但叙事权重过高**
- 仅 5 benchmarks（3 MC + 2 FF），permutation test p=0.10 是分辨率下限；benchmark-level CI [-1.7, 5.1] 跨零；cross-benchmark ρ=0.82 但 p=0.089。§4.3 诚实承认限制，但 Abstract 仍将其作为核心卖点。

**N3** [critical] **"10× fewer items" 隐藏 129× 总评估量增长**
- Multi-facet 55 items × 1,296 conditions = 71,280 次评估 vs. single-condition 552 × 1 = 552 次。总计算量增长 129×。这个 trade-off 在 Abstract/Contributions 中被完全回避。

### Should-Fix 问题

**W1** 模型范围过窄（仅 7-9B instruction-tuned），Abstract claim 语气未相应降级。
**W2** FF benchmarks 高残差（40-44%）归因于 "CoT path diversity" 是推测性的。
**W3** IRT 对比（Table 4）混淆了 item selection quality 和 evaluation design 两个维度。
**W4** 所有发现仅限 binary scoring，未探索 partial credit 等中间方案。
**W5** Abstract 数字过密（>20 个数值），可读性受损。

### Questions
Q1: "10× (55 vs 552)" 来自 single-model，"ratio exceeds 10× across all benchmarks" 来自 cross-model。混合表述是否误导？
Q2: 换入不同模型（Phi-3, CodeLlama 等），variance structure 是否会实质性变化？
Q3: HellaSwag model×item > item 是否暗示 format 之外的因素在驱动 variance？
Q4: Item resampling stability（CV=3.1%）仅限 MMLU，GSM8K 是否同样稳定？
Q5: Seed facet variance <0.5%，是否说明 CUDA nondeterminism 在实践中可忽略？

### Missing References
1. Mizrahi et al. (2024), "State of What Art?", TACL — 最关键遗漏
2. Lu et al. (2022), "Fantastically Ordered Prompts", ACL
3. Liang et al. (2023), HELM

### Minor
- Table 3 "Prompt" 行 MC vs FF 报告不同量，易误读
- Figure 2 灰度打印下难区分
- §4.6 G=0.71 也可能反映 within-family high similarity

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 438 · 2026-05-22T13:11:10.981689+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n## 对 Must-Fix 问题的回应\n\n### R2-N1: 与 Messing (2026) 的增量贡献界定不充分\n\n**[REBUT]** 部分同意需要更充分的区分，但不同意新颖性不足。\n\nReviewer 2 低估了本文相对于 Messing (2026) 的实质性增量。§2 (Related Work, Positioning paragraph) 已明确列出三个区别维度：(1) fix the judge（消除 judge identity 这一 Messing 中占 43.8% 的主导 facet，转为 generation-based scoring）；(2) extend to 5 benchmarks（Messing 仅 1 个 benchmark），这使得 cross-benchmark variance structure comparison 成为可能；(3) 增加 infrastructure facets（numerical precision），Messing 未覆盖。\n\n更关键的是，本文的核心贡献——**design-dependent reproducibility budgets**（D-study projections 从 single-condition 到 multi-facet 的 budget 对比）和 **format-associated variance structure**（MC vs FF 的系统性差异）——在 Messing (2026) 中完全没有。Messing 的 D-study 仅在单 benchmark 内投射，无法产生跨格式的 budget 对比。\n\n不过，我同意 §2 的区分确实可以更详细。建议作者用 2-3 句话展开 Messing 的具体范围（5 facets, 单 benchmark, judge-centric），然后逐点论证本文的增量。这是写作问题，不是新颖性问题。\n\n### R2-N2: Format-associated pattern 统计功效不足，叙事权重过高\n\n**[AGREE]** 与我的 N2 完全一致。\n\n我在自己的审稿中已将此列为 critical issue（R1-N2）。n=5, p=0.10, benchmark-level CI [-1.7, 5.1] 跨零，这些数字不支持将 format-associated pattern 作为核心贡献。论文在 §4.3 内部确实 hedge 了（\"descriptive observation\"），但 Abstract 和 Contribution list 的措辞仍然过于确定。\n\n两位 Reviewer 在这一点上达成一致，建议 Director 将此标记为 **共识性 must-fix**。\n\n### R2-N3: \"10× fewer items\" 隐藏 129× 总评估量增长\n\n**[REBUT]** 这个批评在方向上合理，但严重程度被高估了。\n\n首先，论文在 §4.5 (Table 4) 中**明确报告了总评估量**：multi-facet 55 items × 1,296 conditions = 71,280 total evals，single-condition 552 × 1 = 552 total evals。这个信息并未被隐藏。\n\n其次，这个 trade-off 的本质是 **measurement reliability 的经济学**，而不是 computational cost minimization。G-theory D-study 的核心目的就是告诉 practitioners：要达到同样的 reliability（G≥0.80），你需要多少 items？multi-facet 设计用更少的 items 实现更高的 reliability，代价是每个 item 需要更多 conditions。这是 G-theory 的标准解读方式（Brennan 2001, Ch. 4），不是本文独有的 framing。\n\n不过，我同意 Abstract/Contributions 可以更平衡地呈现。建议增加一句类似：\"Multi-facet designs achieve this efficiency by evaluating each item under multiple conditions (1,296 per item), trading total evaluation volume for item-level reliability\"。这是措辞改进，不是方法论缺陷。\n\n此外，Appendix B (Table 7) 的 intermediate designs 已提供了实用的 cost-reliability gradient——\"minimal upgrade\" 仅需 3p×3s=9 conditions（G_200=0.818），总评估量 200×9=1,800，远低于 71,280。这说明 practitioners 不需要采用 full multi-facet design 就能获得显著的 reliability 提升。\n\n---\n\n## 对 Should-Fix 问题的回应\n\n### R2-W1: 模型范围过窄（仅 7-9B instruction-tuned）\n\n**[AGREE]** 与我的 W2 (Should-Fix) 一致。§4.6 的 scale validation（Qwen2.5 3B/7B, within-family）范围过窄。但论文在 §3.6 和 Limitations 中已明确限定 universe 为 \"open-weight, instruction-tuned models in the 7-9B parameter range, sampled from six architecture families\"。问题在于 Abstract 和 Conclusion 的语气未完全对齐这一限定。\n\n### R2-W2: FF benchmarks 高残差（40-44%）归因推测性\n\n**[AGREE]** 与我的 W6 (Should-Fix) 一致。§4.3 仅用一句话解释 \"chain-of-thought path diversity and answer extraction variability\"，对占据近一半 variance 的 component 来说不够。论文应讨论 residual 的可能构成，或至少承认这是当前设计无法进一步分解的限制。\n\n### R2-W3: IRT 对比（Table 4）混淆了 item selection quality 和 evaluation design\n\n**[REBUT]** 我认为 Table 4 的对比是合理的，未混淆两个维度。\n\nTable 4 的目的正是展示 item selection（IRT）和 evaluation design（G-theory multi-facet）是**正交互补**的。论文在 §4.5 明确写道：\"IRT item selection and G-theory protocol optimization are orthogonal and complementary.\" IRT-selected 116 items 在 single-condition 下 G=0.457 vs multi-facet 下 G=0.895——这清晰地展示了即使使用了最优 item selection，如果 evaluation design 不充分，reliability 仍然低。\n\n这不是混淆，而是有意的 2×2 对比（IRT vs random items × single-condition vs multi-facet）。我认为这是论文的一个 strength（我在 S5 中已标注）。\n\n### R2-W4: 所有发现仅限 binary scoring\n\n**[AGREE]** 论文在 §3.5 和 Limitations 中承认了这一点。text-exact-match 的 G=0.007（§4.1）已经展示了 scoring metric 的根本影响。但未探索 partial credit（如 reasoning quality 的 1-5 scale scoring）确实限制了 generalizability。这是合理的 should-fix，但考虑到 binary scoring 在当前 LLM evaluation 中的主流地位，我不认为这应升级为 must-fix。\n\n### R2-W5: Abstract 数字过密（>20 个数值）\n\n**[AGREE]** Abstract 确实塞入了过多数字。建议保留 3-4 个最关键的数字（10×, 55 vs 552, 68-72% vs 31-41%），其余移入正文。这是纯写作问题，易修。\n\n---\n\n## 对 Questions 的回应\n\n### R2-Q1: \"10× (55 vs 552)\" single-model vs \"ratio exceeds 10× across all benchmarks\" cross-model 混合表述\n\n**[AGREE]** 这个指出合理。§4.5 和 Contribution 1 确实在 single-model 数字和 cross-model claim 之间跳转。55 vs 552 来自 Table 4（single-model, Llama, MMLU），而 \"across all five benchmarks\" 来自 Table 6（cross-model, 8 models）。建议作者在 Contribution 1 中明确标注数字来源，或统一使用 cross-model 数字。\n\n### R2-Q2: 换入不同模型是否会改变 variance structure\n\n**[AGREE]** 这与我的 N1 高度相关。8 个 purposively selected models 作为 quasi-random facet 的假设需要更强的验证。LOMO with n=8 功效不足。如果换入 Phi-3, CodeLlama 等不同类型的模型，variance structure 确实可能实质性变化。\n\n### R2-Q3: HellaSwag model×item > item 暗示 format 之外的因素\n\n**[AGREE]** 好问题。HellaSwag 的 σ²_pM (36.0%) > σ²_p (34.3%) 确实暗示不是 format 单一因素在驱动 variance structure。论文在 §4.3 试图用 item difficulty heterogeneity（std(p_i) 与 item_id share 的相关性）来解释，但 HellaSwag 的这个特殊表现削弱了纯 format 的解释力。这为 N2（format-associated pattern 的统计支撑不足）提供了额外证据。\n\n### R2-Q4: Item resampling stability（CV=3.1%）仅限 MMLU\n\n**[AGREE]** 与我的 W5 一致。三次独立 200-item resampling 仅在 MMLU 上执行。GSM8K 的 item heterogeneity 更低（std(p_i)=0.22 vs MMLU 的 0.27-0.31），且 residual variance 更大（39.9%），resampling stability 可能不同。\n\n### R2-Q5: Seed facet variance <0.5%，是否说明 CUDA nondeterminism 可忽略\n\n**[REBUT]** Seed facet 的低 variance 不能直接等同于 \"CUDA nondeterminism 可忽略\"。§3.4 明确说明 inference 使用 vLLM 0.9.2 **without batch-invariant kernels**，preserving CUDA-level nondeterminism as a measurable variance source。Seed facet 捕获的是 seed×item interaction（4.7% in single-model, §4.1），说明不同 seed 对不同 items 的影响是差异性的而非均匀的。Main effect 小不意味着 interaction 小。此外，seed variance 在 binary scoring 下被压缩——text-exact-match 可能显示更大的 seed effect。结论应该是 \"seed main effect is negligible under binary scoring, but seed×item interactions contribute ~5% of variance in single-model settings\"。\n\n---\n\n## 对 Missing References 的回应\n\n### Mizrahi et al. (2024), \"State of What Art?\", TACL\n\n**[AGREE]** 这确实是重要遗漏。Mizrahi et al. 系统性地分析了 benchmark evaluation 中的 methodology choices 对 leaderboard rankings 的影响，与本文的 motivation 高度相关。应在 §1 或 §2 (Variance Decomposition in ML/NLP Evaluation) 中引用。\n\n### Lu et al. (2022), \"Fantastically Ordered Prompts\", ACL\n\n**[REBUT]** 论文已引用 Pezeshkpour & Husseini (2024) 作为 ordering sensitivity 的参考。Lu et al. (2022) 侧重于 in-context learning 的 example ordering，与本文的 few-shot demo ordering 有关但不是核心。可在 §2 中补充引用，但不是 critical omission。\n\n### Liang et al. (2023), HELM\n\n**[AGREE]** HELM 是 LLM evaluation 的重要基准工作，考虑到 holistic evaluation 的 standardization effort 与本文对 evaluation design 的关注直接相关，应在 §2 中引用。\n\n---\n\n## 对 Minor Issues 的回应\n\n### Table 3 \"Prompt\" 行 MC vs FF 报告不同量\n\n**[AGREE]** 与我的 Minor 第 1 条一致。两位 Reviewer 都指出了这个问题。\n\n### Figure 2 灰度打印下难区分\n\n**[AGREE]** 合理的排版建议。\n\n### §4.6 G=0.71 也可能反映 within-family high similarity\n\n**[AGREE]** 好观察。Qwen2.5 3B 和 7B 同属一个 architecture family，其高 within-family similarity 可能使 model×item variance 偏低（两个模型在相同 items 上行为相似），导致 G 偏低（因为 2 models 提供的 independent information 不足）。这与 between-family 的 8-model design 不可直接比较。论文应在 §4.6 中讨论这一混淆。\n\n---\n\n## R1-R2 共识总结\n\n**强共识（两位 Reviewer 独立达成一致）：**\n1. Format-associated pattern 统计支撑不足 + 叙事权重过高（R1-N2, R2-N2）\n2. 模型范围过窄，Abstract/claims 语气未对齐（R1-W2, R2-W1）\n3. FF residual variance 解释不充分（R1-W6, R2-W2）\n4. Table 3 Prompt 行的非对称报告（R1-Minor-1, R2-Minor-1）\n5. Item resampling stability 仅限 MMLU（R1-W5, R2-Q4）\n\n**R1 独有但 R2 未覆盖的关键问题：**\n1. **Quasi-random model facet 假设**（R1-N1, critical）——这是我认为的最重要方法论问题\n2. **D-study projection 外推假设**（R1-N3, critical）——variance component invariance 未充分验证\n3. Precision separability 的适用范围限定（R1-W3）\n\n**R2 独有的有价值观点：**\n1. **Messing (2026) 增量贡献界定**（R2-N1）——写作层面合理，但我不同意新颖性不足\n2. **\"10× fewer items\" 隐藏 129× 总评估量增长**（R2-N3）——方向合理但严重程度被高估\n3. Missing references（Mizrahi et al., HELM）——合理补充\n",
  "reviewer_id": "1",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n## 对 Must-Fix 问题的回应\n\n### R2-N1: 与 Messing (2026) 的增量贡献界定不充分\n\n**[REBUT]** 部分同意需要更充分的区分，但不同意新颖性不足。\n\nReviewer 2 低估了本文相对于 Messing (2026) 的实质性增量。§2 (Related Work, Positioning paragraph) 已明确列出三个区别维度：(1) fix the judge（消除 judge identity 这一 Messing 中占 43.8% 的主导 facet，转为 generation-based scoring）；(2) extend to 5 benchmarks（Messing 仅 1 个 benchmark），这使得 cross-benchmark variance structure comparison 成为可能；(3) 增加 infrastructure facets（numerical precision），Messing 未覆盖。\n\n更关键的是，本文的核心贡献——**design-dependent reproducibility budgets**（D-study projections 从 single-condition 到 multi-facet 的 budget 对比）和 **format-associated variance structure**（MC vs FF 的系统性差异）——在 Messing (2026) 中完全没有。Messing 的 D-study 仅在单 benchmark 内投射，无法产生跨格式的 budget 对比。\n\n不过，我同意 §2 的区分确实可以更详细。建议作者用 2-3 句话展开 Messing 的具体范围（5 facets, 单 benchmark, judge-centric），然后逐点论证本文的增量。这是写作问题，不是新颖性问题。\n\n### R2-N2: Format-associated pattern 统计功效不足，叙事权重过高\n\n**[AGREE]** 与我的 N2 完全一致。\n\n我在自己的审稿中已将此列为 critical issue（R1-N2）。n=5, p=0.10, benchmark-level CI [-1.7, 5.1] 跨零，这些数字不支持将 format-associated pattern 作为核心贡献。论文在 §4.3 内部确实 hedge 了（\"descriptive observation\"），但 Abstract 和 Contribution list 的措辞仍然过于确定。\n\n两位 Reviewer 在这一点上达成一致，建议 Director 将此标记为 **共识性 must-fix**。\n\n### R2-N3: \"10× fewer items\" 隐藏 129× 总评估量增长\n\n**[REBUT]** 这个批评在方向上合理，但严重程度被高估了。\n\n首先，论文在 §4.5 (Table 4) 中**明确报告了总评估量**：multi-facet 55 items × 1,296 conditions = 71,280 total evals，single-condition 552 × 1 = 552 total evals。这个信息并未被隐藏。\n\n其次，这个 trade-off 的本质是 **measurement reliability 的经济学**，而不是 computational cost minimization。G-theory D-study 的核心目的就是告诉 practitioners：要达到同样的 reliability（G≥0.80），你需要多少 items？multi-facet 设计用更少的 items 实现更高的 reliability，代价是每个 item 需要更多 conditions。这是 G-theory 的标准解读方式（Brennan 2001, Ch. 4），不是本文独有的 framing。\n\n不过，我同意 Abstract/Contributions 可以更平衡地呈现。建议增加一句类似：\"Multi-facet designs achieve this efficiency by evaluating each item under multiple conditions (1,296 per item), trading total evaluation volume for item-level reliability\"。这是措辞改进，不是方法论缺陷。\n\n此外，Appendix B (Table 7) 的 intermediate designs 已提供了实用的 cost-reliability gradient——\"minimal upgrade\" 仅需 3p×3s=9 conditions（G_200=0.818），总评估量 200×9=1,800，远低于 71,280。这说明 practitioners 不需要采用 full multi-facet design 就能获得显著的 reliability 提升。\n\n---\n\n## 对 Should-Fix 问题的回应\n\n### R2-W1: 模型范围过窄（仅 7-9B instruction-tuned）\n\n**[AGREE]** 与我的 W2 (Should-Fix) 一致。§4.6 的 scale validation（Qwen2.5 3B/7B, within-family）范围过窄。但论文在 §3.6 和 Limitations 中已明确限定 universe 为 \"open-weight, instruction-tuned models in the 7-9B parameter range, sampled from six architecture families\"。问题在于 Abstract 和 Conclusion 的语气未完全对齐这一限定。\n\n### R2-W2: FF benchmarks 高残差（40-44%）归因推测性\n\n**[AGREE]** 与我的 W6 (Should-Fix) 一致。§4.3 仅用一句话解释 \"chain-of-thought path diversity and answer extraction variability\"，对占据近一半 variance 的 component 来说不够。论文应讨论 residual 的可能构成，或至少承认这是当前设计无法进一步分解的限制。\n\n### R2-W3: IRT 对比（Table 4）混淆了 item selection quality 和 evaluation design\n\n**[REBUT]** 我认为 Table 4 的对比是合理的，未混淆两个维度。\n\nTable 4 的目的正是展示 item selection（IRT）和 evaluation design（G-theory multi-facet）是**正交互补**的。论文在 §4.5 明确写道：\"IRT item selection and G-theory protocol optimization are orthogonal and complementary.\" IRT-selected 116 items 在 single-condition 下 G=0.457 vs multi-facet 下 G=0.895——这清晰地展示了即使使用了最优 item selection，如果 evaluation design 不充分，reliability 仍然低。\n\n这不是混淆，而是有意的 2×2 对比（IRT vs random items × single-condition vs multi-facet）。我认为这是论文的一个 strength（我在 S5 中已标注）。\n\n### R2-W4: 所有发现仅限 binary scoring\n\n**[AGREE]** 论文在 §3.5 和 Limitations 中承认了这一点。text-exact-match 的 G=0.007（§4.1）已经展示了 scoring metric 的根本影响。但未探索 partial credit（如 reasoning quality 的 1-5 scale scoring）确实限制了 generalizability。这是合理的 should-fix，但考虑到 binary scoring 在当前 LLM evaluation 中的主流地位，我不认为这应升级为 must-fix。\n\n### R2-W5: Abstract 数字过密（>20 个数值）\n\n**[AGREE]** Abstract 确实塞入了过多数字。建议保留 3-4 个最关键的数字（10×, 55 vs 552, 68-72% vs 31-41%），其余移入正文。这是纯写作问题，易修。\n\n---\n\n## 对 Questions 的回应\n\n### R2-Q1: \"10× (55 vs 552)\" single-model vs \"ratio exceeds 10× across all benchmarks\" cross-model 混合表述\n\n**[AGREE]** 这个指出合理。§4.5 和 Contribution 1 确实在 single-model 数字和 cross-model claim 之间跳转。55 vs 552 来自 Table 4（single-model, Llama, MMLU），而 \"across all five benchmarks\" 来自 Table 6（cross-model, 8 models）。建议作者在 Contribution 1 中明确标注数字来源，或统一使用 cross-model 数字。\n\n### R2-Q2: 换入不同模型是否会改变 variance structure\n\n**[AGREE]** 这与我的 N1 高度相关。8 个 purposively selected models 作为 quasi-random facet 的假设需要更强的验证。LOMO with n=8 功效不足。如果换入 Phi-3, CodeLlama 等不同类型的模型，variance structure 确实可能实质性变化。\n\n### R2-Q3: HellaSwag model×item > item 暗示 format 之外的因素\n\n**[AGREE]** 好问题。HellaSwag 的 σ²_pM (36.0%) > σ²_p (34.3%) 确实暗示不是 format 单一因素在驱动 variance structure。论文在 §4.3 试图用 item difficulty heterogeneity（std(p_i) 与 item_id share 的相关性）来解释，但 HellaSwag 的这个特殊表现削弱了纯 format 的解释力。这为 N2（format-associated pattern 的统计支撑不足）提供了额外证据。\n\n### R2-Q4: Item resampling stability（CV=3.1%）仅限 MMLU\n\n**[AGREE]** 与我的 W5 一致。三次独立 200-item resampling 仅在 MMLU 上执行。GSM8K 的 item heterogeneity 更低（std(p_i)=0.22 vs MMLU 的 0.27-0.31），且 residual variance 更大（39.9%），resampling stability 可能不同。\n\n### R2-Q5: Seed facet variance <0.5%，是否说明 CUDA nondeterminism 可忽略\n\n**[REBUT]** Seed facet 的低 variance 不能直接等同于 \"CUDA nondeterminism 可忽略\"。§3.4 明确说明 inference 使用 vLLM 0.9.2 **without batch-invariant kernels**，preserving CUDA-level nondeterminism as a measurable variance source。Seed facet 捕获的是 seed×item interaction（4.7% in single-model, §4.1），说明不同 seed 对不同 items 的影响是差异性的而非均匀的。Main effect 小不意味着 interaction 小。此外，seed variance 在 binary scoring 下被压缩——text-exact-match 可能显示更大的 seed effect。结论应该是 \"seed main effect is negligible under binary scoring, but seed×item interactions contribute ~5% of variance in single-model settings\"。\n\n---\n\n## 对 Missing References 的回应\n\n### Mizrahi et al. (2024), \"State of What Art?\", TACL\n\n**[AGREE]** 这确实是重要遗漏。Mizrahi et al. 系统性地分析了 benchmark evaluation 中的 methodology choices 对 leaderboard rankings 的影响，与本文的 motivation 高度相关。应在 §1 或 §2 (Variance Decomposition in ML/NLP Evaluation) 中引用。\n\n### Lu et al. (2022), \"Fantastically Ordered Prompts\", ACL\n\n**[REBUT]** 论文已引用 Pezeshkpour & Husseini (2024) 作为 ordering sensitivity 的参考。Lu et al. (2022) 侧重于 in-context learning 的 example ordering，与本文的 few-shot demo ordering 有关但不是核心。可在 §2 中补充引用，但不是 critical omission。\n\n### Liang et al. (2023), HELM\n\n**[AGREE]** HELM 是 LLM evaluation 的重要基准工作，考虑到 holistic evaluation 的 standardization effort 与本文对 evaluation design 的关注直接相关，应在 §2 中引用。\n\n---\n\n## 对 Minor Issues 的回应\n\n### Table 3 \"Prompt\" 行 MC vs FF 报告不同量\n\n**[AGREE]** 与我的 Minor 第 1 条一致。两位 Reviewer 都指出了这个问题。\n\n### Figure 2 灰度打印下难区分\n\n**[AGREE]** 合理的排版建议。\n\n### §4.6 G=0.71 也可能反映 within-family high similarity\n\n**[AGREE]** 好观察。Qwen2.5 3B 和 7B 同属一个 architecture family，其高 within-family similarity 可能使 model×item variance 偏低（两个模型在相同 items 上行为相似），导致 G 偏低（因为 2 models 提供的 independent information 不足）。这与 between-family 的 8-model design 不可直接比较。论文应在 §4.6 中讨论这一混淆。\n\n---\n\n## R1-R2 共识总结\n\n**强共识（两位 Reviewer 独立达成一致）：**\n1. Format-associated pattern 统计支撑不足 + 叙事权重过高（R1-N2, R2-N2）\n2. 模型范围过窄，Abstract/claims 语气未对齐（R1-W2, R2-W1）\n3. FF residual variance 解释不充分（R1-W6, R2-W2）\n4. Table 3 Prompt 行的非对称报告（R1-Minor-1, R2-Minor-1）\n5. Item resampling stability 仅限 MMLU（R1-W5, R2-Q4）\n\n**R1 独有但 R2 未覆盖的关键问题：**\n1. **Quasi-random model facet 假设**（R1-N1, critical）——这是我认为的最重要方法论问题\n2. **D-study projection 外推假设**（R1-N3, critical）——variance component invariance 未充分验证\n3. Precision separability 的适用范围限定（R1-W3）\n\n**R2 独有的有价值观点：**\n1. **Messing (2026) 增量贡献界定**（R2-N1）——写作层面合理，但我不同意新颖性不足\n2. **\"10× fewer items\" 隐藏 129× 总评估量增长**（R2-N3）——方向合理但严重程度被高估\n3. Missing references（Mizrahi et al., HELM）——合理补充\n",
    "reviewer_id": "1",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 439 · 2026-05-22T13:11:14.849603+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3867
}
```

</details>

---


### Assistant

_source line 440 · 2026-05-22T13:11:31.630079+00:00_

交叉回应已提交。总结关键共识：

1. **两位 Reviewer 强共识**：format-associated pattern 统计支撑不足（p=0.10, n=5）但叙事权重过高；模型范围窄而 claims 过宽；FF residual 40-44% 解释不充分。

2. **我的独有关键问题**（R2 未覆盖）：quasi-random model facet 假设辩护不足（N1）、D-study projection 外推假设未验证（N3）——这两个是我认为最影响接收决定的方法论问题。

3. **对 R2 的反驳**：Messing (2026) 增量贡献充分（R2-N1 是写作问题非新颖性问题）；"129× 总评估量" 的批评方向合理但严重程度被高估（Table 4 已报告总量，Appendix B 提供了低成本中间方案）；IRT 对比（R2-W3）实际上是论文的 strength 而非 weakness。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1"
}
```

</details>

---


## Round 13

## Round 13

50 recorded events


### User

_source line 441 · 2026-05-22T14:24:16.462188+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性 + 实验设计**审查。

## Venue 信息
- **目标**: EMNLP 2026 via ARR May 2026 cycle
- **Deadline**: 2026-05-25
- **格式**: ACL template [review], long paper 正文 ≤8 页, References 不限, Limitations/Ethics 不计入页数
- **匿名**: double-blind
- **评分标准**: Overall Assessment 1-5 分制（5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit）

## 论文路径
- LaTeX: `projects/nlp_variance_gtheory/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/submitted.pdf`

## 你的审查侧重

**重点关注以下方面，逐条给出评价（Strength/Weakness/Question）：**

1. **G-theory 方法论合理性**：Henderson Method I 是否适用于 binary outcome data？binary data 违反正态性假设的 robustness 辩护是否充分？方差分解估计的无偏性论证。

2. **实验设计**：7-facet fully crossed design 是否合理？200-item stratified sample 是否有代表性问题？8 models 作为 quasi-random facet 的 exchangeability 辩护是否充分？reduced crossing (exp-002) 的 validity。

3. **统计推断**：Bootstrap CI 方法是否合适？D-study projection 的 variance component invariance 假设是否讨论充分？Forward prediction validation 的说服力。

4. **Format-associated pattern**：n=5 benchmarks 的统计功效 (p=0.10) 是否支撑论文对 format 差异的论述？该发现的呈现层级是否与证据强度匹配？

5. **Binary scoring limitation**：所有发现限于 binary correctness scoring，partial-credit pilot (GSM8K) 是否足以缓解这一限制？D-study budgets 的跨 metric 可迁移性。

6. **Robustness checks**：LOMO analysis、resampling stability、estimator comparison、probit simulation、null calibration 是否全面？是否有遗漏的 robustness 检查？

7. **Reproducibility**：代码/数据是否承诺开源？实验能否被独立复现？

请以 ARR 审稿标准输出完整审稿意见，格式：Summary → Strengths (S1, S2, ...) → Weaknesses (W1, W2, ...) → Questions (Q1, Q2, ...) → Missing References → Overall Assessment (分数 + 置信度 + 理由)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 442 · 2026-05-22T14:24:24.844000+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 443 · 2026-05-22T14:24:26.499311+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1655
}
```

</details>

---


### Tool call

_source line 444 · 2026-05-22T14:24:26.549810+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 445 · 2026-05-22T14:24:26.600362+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 446 · 2026-05-22T14:24:31.359452+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 447 · 2026-05-22T14:24:33.521627+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/submitted.pdf",
  "pages": "1-5",
  "project": "nlp_variance_gtheory",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/submitted.pdf",
    "pages": "1-5",
    "project": "nlp_variance_gtheory",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 448 · 2026-05-22T14:24:38.203116+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines and review form criteria:

## Reviewer Guidelines Overview

Reviewers are asked to follow a workflow of reading the paper for a first impression and then searching fo
…[truncated 1149 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 6843
}
```

</details>

---


### Tool result

_source line 449 · 2026-05-22T14:24:38.905269+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 465.7}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 520.7}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 581.8}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 537.9}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.8}], \"total_pages\": 14, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 5383
}
```

</details>

---


### Tool call

_source line 450 · 2026-05-22T14:24:45.552535+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all dimensions, scoring scales, and descriptions. I need every field reviewers must fill out, including Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, Confidence, and any other dimensions. Include the exact scoring rubrics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all dimensions, scoring scales, and descriptions. I need every field reviewers must fill out, including Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, Confidence, and any other dimensions. Include the exact scoring rubrics."
  }
}
```

</details>

---


### Tool call

_source line 451 · 2026-05-22T14:24:47.461035+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, especially: what reviewers should focus on, how to evaluate soundness, novelty, experimental design, and what constitutes a good vs bad review. Include any specific instructions about statistical rigor, reproducibility, or methodology evaluation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines, especially: what reviewers should focus on, how to evaluate soundness, novelty, experimental design, and what constitutes a good vs bad review. Include any specific instructions about statistical rigor, reproducibility, or methodology evaluation."
  }
}
```

</details>

---


### Tool call

_source line 452 · 2026-05-22T14:24:47.914074+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 453 · 2026-05-22T14:24:48.723752+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 809
}
```

</details>

---


### Tool call

_source line 454 · 2026-05-22T14:24:48.874405+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 455 · 2026-05-22T14:24:49.275767+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 456 · 2026-05-22T14:24:49.730061+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 457 · 2026-05-22T14:24:49.730491+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 458 · 2026-05-22T14:24:50.182760+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 459 · 2026-05-22T14:24:50.183205+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 460 · 2026-05-22T14:24:50.786193+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1055
}
```

</details>

---


### Tool result

_source line 461 · 2026-05-22T14:24:51.088125+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool result

_source line 462 · 2026-05-22T14:24:52.091582+00:00_

# ACL Rolling Review Form - Complete Dimensions

## Primary Review Dimensions

**1. Paper Summary**
Reviewer describes the paper's topic to clarify understanding.

**2. Summary of Strengths**
Document reasons for publication, including "novel and useful methodology, insightful empirical results or theoretical analysis."

**3. Summary of Weaknesses**
Numbered concerns about correctness, impact, clarity, or other factors affecting publication priority.

**4. Comments/Suggestions/Typos**
Additional improvement suggestions beyond addressing weaknesses.

## Scoring Dimensions

**Reviewer Confidence** (1-5 scale)
- 5: Positive evaluation is correct; familiar with related work
- 4: Quite sure; unlikely to have missed critical details
- 3: Pretty sure; may not have verified all technical details
- 2: Willing to defend but likely missed some aspects
- 1: Outside expertise area or paper very difficult to understand

**Soundness** (1-5 with half-points)
- 5: Excellent; exceptionally thorough
- 4: Strong; sufficient support for claims
- 3: Acceptable; main claims supported
- 2: Poor; major technical/methodological problems
- 1: Major issues; insufficient for publication

**Excitement** (1-5 with half-points)
Subjective evaluation of innovation, impact, or relevance, ranging from "Highly Exciting" to "Not Exciting."

**Overall Assessment** (1-5 scale)
- 5: Consider for Award
- 4: Conference acceptance
- 3: Findings track
- 2: Resubmit next cycle
- 1: Do not resubmit

## Additional Required Dimensions

- **Limitations and Societal Impact**
- **Ethical Concerns**
- **Reproducibility** (1-5 scale)
- **Datasets** (1-5 scale, if applicable)
- **Software** (1-5 scale, if applicable)
- **Author Identity Knowledge** (1-5 scale, confidential)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 6539
}
```

</details>

---


### Tool result

_source line 463 · 2026-05-22T14:24:55.655761+00:00_

# ARR Reviewer Guidelines: Key Focus Areas

## Core Reviewing Responsibilities

Reviewers must complete four primary tasks:

1. **Allocate calendar time** for reviewing and discussion periods
2. **Check assignments** for expertise match and conflicts of interest
3. **Write substantive reviews** with specific, justified feedback
4. **Engage with author responses** and update assessments accordingly

## Evaluating Soundness

The guidelines emphasize that "soundness scores must be justified by the review text." Reviewers should assess:

- **Technical validity**: Are methods sound? Are proofs complete and correct?
- **Reproducibility**: Are sufficient implementation details provided? Will code/data be available?
- **Statistical rigor**: Do results include confidence intervals, significance tests, or effect sizes?
- **Clear assumptions**: Are all methodological assumptions explicitly stated?

## Assessing Novelty & Contribution

Novelty evaluation requires caution. The guidelines warn against common pitfalls:

- Dismissing work as "not novel" without specific prior references
- Rejecting papers for lacking SOTA results (soundness ≠ SOTA achievement)
- Undervaluing reproduction studies, resource papers, or negative results
- Requiring unnecessary additional experiments beyond what claims demand

Contributions should match the scope specified in the CFP.

## Experimental Design Standards

Reviewers should verify:

- **Appropriate baselines**: Selections should align with stated claims
- **Fair comparisons**: Are baselines similarly tuned and evaluated?
- **Representative sampling**: Do evaluations reflect the population discussed?
- **Disclosed limitations**: Are data quality issues and experimental constraints acknowledged?

## Red Flags for Poor Reviews

The guidelines identify problematic patterns (coded I1-I12):

- **Vague criticism**: "Not clear" without specifying what's missing
- **Unjustified scores**: Low soundness ratings without supporting evidence
- **Unconscio
…[truncated 776 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebFetch",
  "elapsed_ms": 8194
}
```

</details>

---


### Tool call

_source line 464 · 2026-05-22T14:25:04.534734+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/submitted.pdf",
  "pages": "6-10",
  "project": "nlp_variance_gtheory",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/submitted.pdf",
    "pages": "6-10",
    "project": "nlp_variance_gtheory",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 465 · 2026-05-22T14:25:05.188546+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 497.5}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 511.2}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 489.6}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 568.7}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 598.2}], \"total_pages\": 14, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 653
}
```

</details>

---


### Tool call

_source line 466 · 2026-05-22T14:25:10.757244+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 467 · 2026-05-22T14:25:11.665007+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 468 · 2026-05-22T14:25:11.715572+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 469 · 2026-05-22T14:25:12.218307+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 470 · 2026-05-22T14:25:12.670476+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 471 · 2026-05-22T14:25:12.670862+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 472 · 2026-05-22T14:25:13.025116+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 806
}
```

</details>

---


### Tool call

_source line 473 · 2026-05-22T14:25:13.026199+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 474 · 2026-05-22T14:25:13.480839+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 809
}
```

</details>

---


### Tool result

_source line 475 · 2026-05-22T14:25:13.883288+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 476 · 2026-05-22T14:25:20.302546+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/submitted.pdf",
  "pages": "11-14",
  "project": "nlp_variance_gtheory",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/submitted.pdf",
    "pages": "11-14",
    "project": "nlp_variance_gtheory",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 477 · 2026-05-22T14:25:20.754217+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 548.0}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 496.4}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 407.1}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 257.3}], \"total_pages\": 14, \"rendered_pages\": 4, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 478 · 2026-05-22T14:25:27.479626+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 479 · 2026-05-22T14:25:28.433357+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 480 · 2026-05-22T14:25:28.433804+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 481 · 2026-05-22T14:25:28.937827+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool call

_source line 482 · 2026-05-22T14:25:29.289024+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 483 · 2026-05-22T14:25:29.341014+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool result

_source line 484 · 2026-05-22T14:25:29.847109+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 909
}
```

</details>

---


### Tool result

_source line 485 · 2026-05-22T14:25:30.402701+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 1113
}
```

</details>

---


### Tool call

_source line 486 · 2026-05-22T14:30:07.662175+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 487 · 2026-05-22T14:30:07.662652+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 488 · 2026-05-22T14:32:30.977062+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 审稿意见：方法严谨性 + 实验设计\n\n**论文标题**: Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Analysis\n**Venue**: EMNLP 2026 via ARR May 2026 cycle\n\n---\n\n## Paper Summary\n\n本文将 Generalizability Theory (G-theory) 系统应用于 LLM 评估的方差分解，设计了最多 7 facet 的 fully crossed factorial 实验（exp-001: MMLU 单基准; exp-002: 跨 5 个基准的 reduced crossing），覆盖 8 个 7-9B 参数开源指令微调模型和约 230 万条评估记录。主要发现：(1) 多 facet 设计比单条件设计需要少 10× 的 items 达到 G ≥ 0.80；(2) BF16/FP16 精度功能上可互换（<0.1% 交互）；(3) model×item 交互占总方差高达 36%；(4) MC vs FF 格式间的方差结构差异模式。论文还提供了 D-study budget calculator 作为实用工具。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | G-theory 核心应用正确，robustness 分析全面（8 项独立检查），但模型 facet exchangeability 论证有缺口，format pattern 统计推断力不足 |\n| **Excitement** | 3.5/5 | 首次将 G-theory 系统应用于 LLM 评估，D-study budget 工具有直接实用价值；但核心发现限于 binary scoring，partial-credit pilot 显示方差结构会根本性改变 |\n| **Reproducibility** | 4/5 | 承诺开源代码/数据/D-study calculator，实验描述详细（facet levels、sampling strategy、bootstrap 参数均有说明），但当前匿名阶段无法验证 |\n| **Confidence** | 4/5 | 熟悉 G-theory 方法论、factorial 实验设计和 LLM 评估文献 |\n\n---\n\n## 主要优势 (Strengths)\n\n**S1. 首个系统性多 facet G-theory 分析 LLM 评估方差**\n据我所知，这是第一项同时交叉 infrastructure facets（precision, seed, temperature）和 methodology facets（prompt, ordering）并与 item/model 联合分解的工作。相比 Boutilier et al. (2021) 的单 facet ANOVA 和 Madan et al. (2024) 的不交叉 infrastructure/methodology facets，本文的设计在 completeness 上有质的提升。7-facet fully crossed design（Section 3.2, Table 1）真正实现了 G-theory 所需的 multi-facet 交叉结构。\n\n**S2. Robustness 分析的深度和广度超出 NLP 论文常见水平**\nAppendix A 包含 8 项独立的 robustness 检查：GLMM complement（ρ = 1.0 排序一致）、accuracy-range stability（σ < 0.05）、estimator comparison（Henderson I vs REML, Δ < 0.003）、probit simulation null calibration（observed-to-null ratio = 1.0008）、CI method comparison（bootstrap vs jackknife, ratio 0.96-1.04）、LOMO 分析（Table 5, CV ≤ 1.25%）、scoring metric sensitivity、fact specification sensitivity。这种全面性在 NLP 实验论文中很少见。\n\n**S3. Precision separability 发现有即时实用价值**\nSection 4.4 证明 BF16 和 FP16 功能上可互换（均差 0.21 个百分点，所有 precision×methodology 交互 < 0.1%），这为评估实践提供了直接可操作的简化建议。证据充分，基于 3 个 precision level 的 fully crossed 比较。\n\n**S4. D-study budget 工具的实践意义**\nTable 4 的 D-study budget projections 将抽象的方差分量转化为具体的实验设计建议（multi-facet 93 items vs single-condition 552 items for G ≥ 0.80），并承诺开源 calculator。这使得方法论贡献可以直接被社区使用。\n\n**S5. Forward prediction validation 设计合理**\nSection 4.6 用 4 个 exp-001 模型的方差分量预测 8 模型的 G coefficient（|ΔG| = 0.035 across 5 benchmarks），提供了 D-study projection 的初步验证。虽然是 within-experiment 验证，但在 G-theory 应用文献中已属良好实践。\n\n**S6. 写作清晰，结构组织良好**\n论文从 single-model baseline (§4.1) → cross-model variance (§4.2) → format-associated structure (§4.3) → precision separability (§4.4) → D-study budgets (§4.5) 逐步展开，逻辑链清晰。G-theory 背景介绍 (§3.1) 对 NLP 读者友好。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 8 个模型作为 quasi-random facet 的 exchangeability 论证存在关键缺口\n\n- **具体位置**: Section 3.2 (设计描述), Section 6 (Limitations), Appendix A (LOMO, Table 5)\n- **问题**: G-theory 要求 facet 水平从定义良好的 universe 中随机（或可交换地）抽取，方差分量才能推广到该 universe 的其他水平（Brennan, 2001, Ch. 2; Shavelson & Webb, 1991）。本文的 8 个模型是从 8 个不同架构家族中 purposively 选取的 7-9B 指令微调模型，这不是随机抽样。\n\n  LOMO 分析（Table 5, CV ≤ 1.25%）证明的是 **内部一致性**（移除任一模型不大幅改变 G），而非 **外部代表性**（这 8 个模型的方差结构是否代表更广泛的 7-9B 模型群体）。如果这 8 个模型恰好在 item difficulty profiles 上异常相似或异常不同，model variance component（~14-17%）可能被系统性低估或高估，进而导致 D-study budget 建议（Table 4）的系统性偏差。\n\n  Forward prediction validation（4→8 models, |ΔG| = 0.035）是 within-sample interpolation，不是 out-of-sample 验证。Section 4.6 的 Qwen 3B/7B within-family 验证也仅限于同一架构家族。\n\n- **为什么影响接收**: D-study budget 建议是论文的核心实践贡献（Contribution 1, Abstract），其可靠性直接取决于方差分量估计的可推广性。如果 exchangeability 假设不成立，10× 效率提升的 claim 可能不适用于未见过的模型。\n\n- **建议修改方向**:\n  (a) 增加至少 1-2 个 held-out 模型（不在原始 8 个中）的 out-of-sample validation；或\n  (b) 从更大的模型池（如 Open LLM Leaderboard 的 7-9B 模型列表）中进行 bootstrap 子集抽样，展示模型方差分量在不同子集间的稳定性；或\n  (c) 至少在 Section 3.2 中明确定义 model universe 的边界（不仅仅在 Limitations 中提及），并量化 exchangeability 假设失败时 D-study projections 的 sensitivity。\n\n**N2** [critical] Format-associated pattern 的呈现层级与统计证据强度严重不匹配\n\n- **具体位置**: Section 4.3, Table 3, Figure 3; Abstract (贡献 b); Section 1 Contributions list\n- **问题**: 本文用 n = 5 个 benchmarks（3 MC + 2 FF）的 exhaustive permutation test 检验 MC vs FF 格式间的方差结构差异。由于 C(5,2) = 10 种划分方式，permutation test 的 resolution floor 为 p = 0.10，这意味着 **即使观察到的检验统计量是所有可能划分中最极端的，p 值也永远无法低于 0.10**。在 α = 0.05 的常规标准下，这个检验在设计上就无法达到统计显著性。\n\n  论文在 Section 4.3 末尾确实使用了 \"descriptive observation\" 和 \"exploratory\" 等措辞，benchmark-level CI spans zero ([-1.7, 5.1], df = 3) 也如实报告。但同时，这一发现被列为 Abstract 的三大贡献之一（\"compared variance structures across response formats\"）、Section 1 的 Contribution 2（\"precision separability\"）、占据了完整的 Section 4.3（含 Table 3 和 Figure 3），在呈现结构上获得了与其他经 rigorous 验证的发现同等的显著位置。\n\n  这造成了 **framing 与 evidence 的不一致**：一个统计上无法达到显著性的 5-benchmark 观察被结构性地呈现为论文的核心发现之一。\n\n- **为什么影响接收**: 如果 reviewer 或 AC 注意到核心贡献之一基于 inherently underpowered 的检验，可能质疑论文整体的统计严谨性判断。\n\n- **建议修改方向**:\n  (a) 将 format pattern 从 contributions list 降级为 \"Exploratory observation\" 或 \"Hypothesis for future work\"，在 Abstract 中使用更谨慎的语言（如 \"we observe suggestive but statistically underpowered differences\"）；\n  (b) 明确指出 permutation test 的 power limitation 不是因为效应小，而是因为 benchmark 数量的 fundamental constraint（n=5 使 resolution floor = 0.10）；\n  (c) 保留 Section 4.3 的内容但调整标题和定位，例如 \"Exploratory: Format-Associated Variance Patterns\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Binary scoring limitation 的影响可能被低估\n\n- **具体位置**: Section 3.5, Appendix A (Scoring metric sensitivity)\n- **问题**: GSM8K partial-credit pilot 显示方差结构发生根本性改变：prompt template 方差从 25.5% 降至 1.2%，residual 从 28.2% 升至 46.6%，G_abs 从 0.770 降至 0.553（item reliability decrease 从 0.26 到 0.26）。这表明 binary scoring 不仅是一个精度损失，而是会 **系统性地重塑方差分解结构**——prompt 变异在 partial credit 下几乎消失，因为推理路径的质量差异被 binary cutoff 放大为 pass/fail 差异。\n  \n  然而，该 pilot 仅使用 **1 个模型**（Llama），无法估计 model-related 方差分量（model main effect, model×item interaction），而后者在 binary 分析中占 ~30-37%（Table 2）。换言之，pilot 的设计无法回答最关键的问题：partial credit 下 model×item interaction（本文最重要的发现之一）是否仍然占主导地位。\n\n  Section 5 (Conclusion) 的 D-study budget 建议（\"multi-facet designs require 10× fewer items\"）没有明确限定其适用范围为 binary scoring benchmarks。如果 partial credit 下方差结构完全不同，这些 budgets 的迁移性存疑。\n\n- **建议**: (a) 在 Conclusion 的 D-study budget 建议中明确加上 \"under binary correctness scoring\" 的 scope qualifier; (b) 讨论 partial-credit pilot 无法估计 model-related components 的局限; (c) 将 \"D-study budgets 不可迁移至 finer-grained scoring\" 作为 Limitations 的重点之一（目前 Section 6 对此仅一句带过）。\n\n**W2** [warning] D-study projection 的 variance component invariance 假设讨论不充分\n\n- **具体位置**: Section 4.5, Section 3.1 (D-study 定义)\n- **问题**: D-study 的核心假设是从 G-study 估计的方差分量在条件数量变化时保持不变（Brennan, 2001, Ch. 4）。Section 4.5 末尾的 \"Projection assumptions\" 段落提到 \"cross-model budgets increase to 93 items because model×item interaction enters the relative error variance\" 和 \"all projections assume for the 2024-2025 model generation and should be treated as order-of-magnitude guides\"。\n\n  但以下 invariance 威胁未充分讨论:\n  1. **Item pool expansion**: 从 200 items 投射到 55 items 是缩减，但如果实际使用者从不同 item pool 抽取（如 MMLU 的其他 47 个 subjects），方差分量可能不同。\n  2. **Model universe expansion**: D-study 投射假设新增模型与现有 8 个模型具有相同的方差结构，但如 N1 所述，这一假设的验证不足。\n  3. **Temporal drift**: 模型代际更替可能改变 model×item interaction 的大小和结构。\n\n- **建议**: 在 Section 4.5 \"Projection assumptions\" 段落中增加对上述 invariance 威胁的明确讨论，并建议定期重新估计方差分量（如每个 ARR cycle）。\n\n**W3** [warning] 200-item stratified sample 代表性的验证不完整\n\n- **具体位置**: Section 3.2 (Facets), Section 4.7 (Robustness Checks)\n- **问题**: 200 items 从 MMLU 的 57 个 subjects 中选取 10 个（每个 20 题），覆盖 4 个学科领域。Section 4.7 的 resampling stability（CV ≈ 3.1%）验证的是 **sampling variance**（重复抽取 200 题的变异），而非 **representativeness**（这 10 个 subjects 是否代表 57 个 subjects 的方差结构）。\n\n  如果某些未被选中的 subjects（如 formal logic, jurisprudence, econometrics）具有显著不同的 item difficulty distribution 或 model×item interaction 结构，aggregate 方差分解可能不代表 full MMLU。\n\n- **建议**: (a) 报告所选 10 个 subjects 与 full 57 subjects 在 mean accuracy 和 difficulty variance 上的比较; (b) 或在不同的 10-subject subset 上重复方差分解，验证 subject-level heterogeneity 的影响。\n\n**W4** [warning] exp-002 跨基准比较的设计不对称性\n\n- **具体位置**: Section 3.3, Table 1\n- **问题**: exp-002 的 reduced crossing 在不同 benchmarks 间不对称：ordering facet 仅对 MMLU 有效（MC 基准的 few-shot demo 排列），对 FF 基准（GSM8K, MATH）结构性无效；prompt facet 在 MC 和 FF 基准间的含义不同（MC: 问题格式/选项呈现方式; FF: chain-of-thought elicitation strategy）。\n\n  这意味着 Table 3 中 MC vs FF 的方差分解差异可能部分源于 **设计结构的差异**（facet 含义不同），而非纯粹的 **format effect**。论文在 Table 3 注释中提到 \"for FF, reports the prompt main effect\" 和 ordering 被吸收到 residual，但这种设计不对称性对 Section 4.3 的 format-associated pattern 解释构成混淆。\n\n- **建议**: 在 Section 4.3 中明确讨论设计不对称性作为 confound 的可能性——MC vs FF 的方差结构差异是否可能部分由 prompt facet 语义差异或 ordering facet 的有无造成？\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Section 3.2 提到 \"deterministic selection with seed 42\"，建议简要说明 seed 42 选择的原因或声明为任意选取，避免 reviewer 质疑是否 cherry-picked。\n- **M2**: Table 2 的 \"all others: 0.0\" 建议改为 \"< 0.1%\" 或给出具体数值，避免读者误以为某些方差分量恰好为零。\n- **M3**: Section 4.6 的 Qwen 3B/7B scale validation 仅涉及同一架构家族，建议在该段末尾明确此为初步验证，不宜据此推广到跨架构的 scale transfer。\n- **M4**: Appendix E 的 prompt templates（page 14）建议标注每个 template 的设计理由（为何选择这些特定变体），增强 reproducibility。\n\n---\n\n## Questions\n\n**Q1**: 关于 binary data 的 GLMM complement（Appendix A）：GLMM 和 Henderson Method I 的方差分量 **绝对值** 差异是多少？目前只报告了排序一致性（ρ = 1.0），但对于 D-study budget 计算，绝对值的准确性同样重要。如果 GLMM 给出不同的 G coefficient，D-study budgets 是否需要调整？\n\n**Q2**: 关于 exchangeability：如果将 8 个模型视为 fixed facet（而非 random），对 G coefficient 和 D-study budget 的影响有多大？这将给出一个 lower bound 估计，帮助读者理解 random vs fixed 假设的实际差别。\n\n**Q3**: 关于 forward prediction（Section 4.6）：4→8 模型的预测准确度 |ΔG| = 0.035，这个误差在实际应用中是否足够小？例如，0.035 的 G 差异是否会导致 D-study budget 建议发生实质性变化（如从 55 items 变为 70 items）？\n\n**Q4**: 关于 partial-credit pilot：是否考虑过对 GSM8K 进行多模型 partial-credit 实验（即使是 2-3 个模型），以估计 partial credit 下的 model×item interaction？这将极大增强 Section 3.5 的 limitation discussion。\n\n**Q5**: Table 4 的 D-study budget 建议 \"order-of-magnitude guides\" 的量化含义是什么？预期的投射误差范围是 ±10%, ±30%, 还是 ±50%？\n\n**Q6**: 关于 exp-002 的 reduced crossing validation（ΔG = 0.008）：这个验证是在 MMLU 上进行的（比较 full vs reduced design），是否也在其他 benchmarks 上验证了 reduced crossing 的有效性？\n\n---\n\n## Missing References\n\n未发现明显的 critical missing references。G-theory 核心文献（Brennan, 2001; Shavelson & Webb, 1991/1999）、binary data extensions（Jiang & Strijbos, 2018; Tuerlinckx et al., 2006）、LLM 评估方差文献（Boutilier et al., 2021; Madan et al., 2024; Yuan et al., 2025; Pezeshkpour & Hruschka, 2024）均已覆盖。\n\n**可选补充**: Cardinet, Johnson & Pini (2010) \"Applying Generalizability Theory using EduG\" 作为 G-theory 应用方法论参考可能对不熟悉 G-theory 的 NLP 读者有帮助，但非必需。\n\n---\n\n## Overall Assessment\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n\n**Confidence**: 4 / 5\n\n**理由**:\n\n本文做出了 genuine methodological contribution——首次将 G-theory 系统应用于 LLM 评估方差分解，规模大（230 万记录）、robustness 检查全面（8 项）、实践工具有用（D-study calculator）。写作质量高，结构清晰。\n\n给 3.5 而非 4 的核心原因是两个 Must-Fix 问题的叠加效应：\n\n1. **N1 (exchangeability)** 削弱了 D-study budget 建议（论文最核心的实践贡献）的可推广性——8 个 purposively 选择的模型不能保证方差分量可迁移到 unseen models，而论文的验证（LOMO、forward prediction）均为 within-sample。\n2. **N2 (format pattern)** 将一个 inherently underpowered (p ≥ 0.10 by design) 的探索性观察以核心贡献的结构地位呈现，这在统计方法论论文中是一个 framing 问题。\n\n如果作者 (a) 提供 out-of-sample model validation 或更充分的 exchangeability sensitivity analysis，(b) 将 format pattern 降级为 exploratory observation，我认为本文可以达到 4.0 (Conference) 的水平。当前版本的其余 should-fix 问题（W1-W4）均为可在 revision 中解决的增量改进。\n\n**简言之**: 方法论框架正确且有价值，执行规模令人印象深刻，但两个关键假设（model exchangeability, format pattern significance）的论证需要加强才能支撑论文的核心 claims。\n",
  "reviewer_id": "1",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 审稿意见：方法严谨性 + 实验设计\n\n**论文标题**: Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Analysis\n**Venue**: EMNLP 2026 via ARR May 2026 cycle\n\n---\n\n## Paper Summary\n\n本文将 Generalizability Theory (G-theory) 系统应用于 LLM 评估的方差分解，设计了最多 7 facet 的 fully crossed factorial 实验（exp-001: MMLU 单基准; exp-002: 跨 5 个基准的 reduced crossing），覆盖 8 个 7-9B 参数开源指令微调模型和约 230 万条评估记录。主要发现：(1) 多 facet 设计比单条件设计需要少 10× 的 items 达到 G ≥ 0.80；(2) BF16/FP16 精度功能上可互换（<0.1% 交互）；(3) model×item 交互占总方差高达 36%；(4) MC vs FF 格式间的方差结构差异模式。论文还提供了 D-study budget calculator 作为实用工具。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | G-theory 核心应用正确，robustness 分析全面（8 项独立检查），但模型 facet exchangeability 论证有缺口，format pattern 统计推断力不足 |\n| **Excitement** | 3.5/5 | 首次将 G-theory 系统应用于 LLM 评估，D-study budget 工具有直接实用价值；但核心发现限于 binary scoring，partial-credit pilot 显示方差结构会根本性改变 |\n| **Reproducibility** | 4/5 | 承诺开源代码/数据/D-study calculator，实验描述详细（facet levels、sampling strategy、bootstrap 参数均有说明），但当前匿名阶段无法验证 |\n| **Confidence** | 4/5 | 熟悉 G-theory 方法论、factorial 实验设计和 LLM 评估文献 |\n\n---\n\n## 主要优势 (Strengths)\n\n**S1. 首个系统性多 facet G-theory 分析 LLM 评估方差**\n据我所知，这是第一项同时交叉 infrastructure facets（precision, seed, temperature）和 methodology facets（prompt, ordering）并与 item/model 联合分解的工作。相比 Boutilier et al. (2021) 的单 facet ANOVA 和 Madan et al. (2024) 的不交叉 infrastructure/methodology facets，本文的设计在 completeness 上有质的提升。7-facet fully crossed design（Section 3.2, Table 1）真正实现了 G-theory 所需的 multi-facet 交叉结构。\n\n**S2. Robustness 分析的深度和广度超出 NLP 论文常见水平**\nAppendix A 包含 8 项独立的 robustness 检查：GLMM complement（ρ = 1.0 排序一致）、accuracy-range stability（σ < 0.05）、estimator comparison（Henderson I vs REML, Δ < 0.003）、probit simulation null calibration（observed-to-null ratio = 1.0008）、CI method comparison（bootstrap vs jackknife, ratio 0.96-1.04）、LOMO 分析（Table 5, CV ≤ 1.25%）、scoring metric sensitivity、fact specification sensitivity。这种全面性在 NLP 实验论文中很少见。\n\n**S3. Precision separability 发现有即时实用价值**\nSection 4.4 证明 BF16 和 FP16 功能上可互换（均差 0.21 个百分点，所有 precision×methodology 交互 < 0.1%），这为评估实践提供了直接可操作的简化建议。证据充分，基于 3 个 precision level 的 fully crossed 比较。\n\n**S4. D-study budget 工具的实践意义**\nTable 4 的 D-study budget projections 将抽象的方差分量转化为具体的实验设计建议（multi-facet 93 items vs single-condition 552 items for G ≥ 0.80），并承诺开源 calculator。这使得方法论贡献可以直接被社区使用。\n\n**S5. Forward prediction validation 设计合理**\nSection 4.6 用 4 个 exp-001 模型的方差分量预测 8 模型的 G coefficient（|ΔG| = 0.035 across 5 benchmarks），提供了 D-study projection 的初步验证。虽然是 within-experiment 验证，但在 G-theory 应用文献中已属良好实践。\n\n**S6. 写作清晰，结构组织良好**\n论文从 single-model baseline (§4.1) → cross-model variance (§4.2) → format-associated structure (§4.3) → precision separability (§4.4) → D-study budgets (§4.5) 逐步展开，逻辑链清晰。G-theory 背景介绍 (§3.1) 对 NLP 读者友好。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 8 个模型作为 quasi-random facet 的 exchangeability 论证存在关键缺口\n\n- **具体位置**: Section 3.2 (设计描述), Section 6 (Limitations), Appendix A (LOMO, Table 5)\n- **问题**: G-theory 要求 facet 水平从定义良好的 universe 中随机（或可交换地）抽取，方差分量才能推广到该 universe 的其他水平（Brennan, 2001, Ch. 2; Shavelson & Webb, 1991）。本文的 8 个模型是从 8 个不同架构家族中 purposively 选取的 7-9B 指令微调模型，这不是随机抽样。\n\n  LOMO 分析（Table 5, CV ≤ 1.25%）证明的是 **内部一致性**（移除任一模型不大幅改变 G），而非 **外部代表性**（这 8 个模型的方差结构是否代表更广泛的 7-9B 模型群体）。如果这 8 个模型恰好在 item difficulty profiles 上异常相似或异常不同，model variance component（~14-17%）可能被系统性低估或高估，进而导致 D-study budget 建议（Table 4）的系统性偏差。\n\n  Forward prediction validation（4→8 models, |ΔG| = 0.035）是 within-sample interpolation，不是 out-of-sample 验证。Section 4.6 的 Qwen 3B/7B within-family 验证也仅限于同一架构家族。\n\n- **为什么影响接收**: D-study budget 建议是论文的核心实践贡献（Contribution 1, Abstract），其可靠性直接取决于方差分量估计的可推广性。如果 exchangeability 假设不成立，10× 效率提升的 claim 可能不适用于未见过的模型。\n\n- **建议修改方向**:\n  (a) 增加至少 1-2 个 held-out 模型（不在原始 8 个中）的 out-of-sample validation；或\n  (b) 从更大的模型池（如 Open LLM Leaderboard 的 7-9B 模型列表）中进行 bootstrap 子集抽样，展示模型方差分量在不同子集间的稳定性；或\n  (c) 至少在 Section 3.2 中明确定义 model universe 的边界（不仅仅在 Limitations 中提及），并量化 exchangeability 假设失败时 D-study projections 的 sensitivity。\n\n**N2** [critical] Format-associated pattern 的呈现层级与统计证据强度严重不匹配\n\n- **具体位置**: Section 4.3, Table 3, Figure 3; Abstract (贡献 b); Section 1 Contributions list\n- **问题**: 本文用 n = 5 个 benchmarks（3 MC + 2 FF）的 exhaustive permutation test 检验 MC vs FF 格式间的方差结构差异。由于 C(5,2) = 10 种划分方式，permutation test 的 resolution floor 为 p = 0.10，这意味着 **即使观察到的检验统计量是所有可能划分中最极端的，p 值也永远无法低于 0.10**。在 α = 0.05 的常规标准下，这个检验在设计上就无法达到统计显著性。\n\n  论文在 Section 4.3 末尾确实使用了 \"descriptive observation\" 和 \"exploratory\" 等措辞，benchmark-level CI spans zero ([-1.7, 5.1], df = 3) 也如实报告。但同时，这一发现被列为 Abstract 的三大贡献之一（\"compared variance structures across response formats\"）、Section 1 的 Contribution 2（\"precision separability\"）、占据了完整的 Section 4.3（含 Table 3 和 Figure 3），在呈现结构上获得了与其他经 rigorous 验证的发现同等的显著位置。\n\n  这造成了 **framing 与 evidence 的不一致**：一个统计上无法达到显著性的 5-benchmark 观察被结构性地呈现为论文的核心发现之一。\n\n- **为什么影响接收**: 如果 reviewer 或 AC 注意到核心贡献之一基于 inherently underpowered 的检验，可能质疑论文整体的统计严谨性判断。\n\n- **建议修改方向**:\n  (a) 将 format pattern 从 contributions list 降级为 \"Exploratory observation\" 或 \"Hypothesis for future work\"，在 Abstract 中使用更谨慎的语言（如 \"we observe suggestive but statistically underpowered differences\"）；\n  (b) 明确指出 permutation test 的 power limitation 不是因为效应小，而是因为 benchmark 数量的 fundamental constraint（n=5 使 resolution floor = 0.10）；\n  (c) 保留 Section 4.3 的内容但调整标题和定位，例如 \"Exploratory: Format-Associated Variance Patterns\"。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Binary scoring limitation 的影响可能被低估\n\n- **具体位置**: Section 3.5, Appendix A (Scoring metric sensitivity)\n- **问题**: GSM8K partial-credit pilot 显示方差结构发生根本性改变：prompt template 方差从 25.5% 降至 1.2%，residual 从 28.2% 升至 46.6%，G_abs 从 0.770 降至 0.553（item reliability decrease 从 0.26 到 0.26）。这表明 binary scoring 不仅是一个精度损失，而是会 **系统性地重塑方差分解结构**——prompt 变异在 partial credit 下几乎消失，因为推理路径的质量差异被 binary cutoff 放大为 pass/fail 差异。\n  \n  然而，该 pilot 仅使用 **1 个模型**（Llama），无法估计 model-related 方差分量（model main effect, model×item interaction），而后者在 binary 分析中占 ~30-37%（Table 2）。换言之，pilot 的设计无法回答最关键的问题：partial credit 下 model×item interaction（本文最重要的发现之一）是否仍然占主导地位。\n\n  Section 5 (Conclusion) 的 D-study budget 建议（\"multi-facet designs require 10× fewer items\"）没有明确限定其适用范围为 binary scoring benchmarks。如果 partial credit 下方差结构完全不同，这些 budgets 的迁移性存疑。\n\n- **建议**: (a) 在 Conclusion 的 D-study budget 建议中明确加上 \"under binary correctness scoring\" 的 scope qualifier; (b) 讨论 partial-credit pilot 无法估计 model-related components 的局限; (c) 将 \"D-study budgets 不可迁移至 finer-grained scoring\" 作为 Limitations 的重点之一（目前 Section 6 对此仅一句带过）。\n\n**W2** [warning] D-study projection 的 variance component invariance 假设讨论不充分\n\n- **具体位置**: Section 4.5, Section 3.1 (D-study 定义)\n- **问题**: D-study 的核心假设是从 G-study 估计的方差分量在条件数量变化时保持不变（Brennan, 2001, Ch. 4）。Section 4.5 末尾的 \"Projection assumptions\" 段落提到 \"cross-model budgets increase to 93 items because model×item interaction enters the relative error variance\" 和 \"all projections assume for the 2024-2025 model generation and should be treated as order-of-magnitude guides\"。\n\n  但以下 invariance 威胁未充分讨论:\n  1. **Item pool expansion**: 从 200 items 投射到 55 items 是缩减，但如果实际使用者从不同 item pool 抽取（如 MMLU 的其他 47 个 subjects），方差分量可能不同。\n  2. **Model universe expansion**: D-study 投射假设新增模型与现有 8 个模型具有相同的方差结构，但如 N1 所述，这一假设的验证不足。\n  3. **Temporal drift**: 模型代际更替可能改变 model×item interaction 的大小和结构。\n\n- **建议**: 在 Section 4.5 \"Projection assumptions\" 段落中增加对上述 invariance 威胁的明确讨论，并建议定期重新估计方差分量（如每个 ARR cycle）。\n\n**W3** [warning] 200-item stratified sample 代表性的验证不完整\n\n- **具体位置**: Section 3.2 (Facets), Section 4.7 (Robustness Checks)\n- **问题**: 200 items 从 MMLU 的 57 个 subjects 中选取 10 个（每个 20 题），覆盖 4 个学科领域。Section 4.7 的 resampling stability（CV ≈ 3.1%）验证的是 **sampling variance**（重复抽取 200 题的变异），而非 **representativeness**（这 10 个 subjects 是否代表 57 个 subjects 的方差结构）。\n\n  如果某些未被选中的 subjects（如 formal logic, jurisprudence, econometrics）具有显著不同的 item difficulty distribution 或 model×item interaction 结构，aggregate 方差分解可能不代表 full MMLU。\n\n- **建议**: (a) 报告所选 10 个 subjects 与 full 57 subjects 在 mean accuracy 和 difficulty variance 上的比较; (b) 或在不同的 10-subject subset 上重复方差分解，验证 subject-level heterogeneity 的影响。\n\n**W4** [warning] exp-002 跨基准比较的设计不对称性\n\n- **具体位置**: Section 3.3, Table 1\n- **问题**: exp-002 的 reduced crossing 在不同 benchmarks 间不对称：ordering facet 仅对 MMLU 有效（MC 基准的 few-shot demo 排列），对 FF 基准（GSM8K, MATH）结构性无效；prompt facet 在 MC 和 FF 基准间的含义不同（MC: 问题格式/选项呈现方式; FF: chain-of-thought elicitation strategy）。\n\n  这意味着 Table 3 中 MC vs FF 的方差分解差异可能部分源于 **设计结构的差异**（facet 含义不同），而非纯粹的 **format effect**。论文在 Table 3 注释中提到 \"for FF, reports the prompt main effect\" 和 ordering 被吸收到 residual，但这种设计不对称性对 Section 4.3 的 format-associated pattern 解释构成混淆。\n\n- **建议**: 在 Section 4.3 中明确讨论设计不对称性作为 confound 的可能性——MC vs FF 的方差结构差异是否可能部分由 prompt facet 语义差异或 ordering facet 的有无造成？\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Section 3.2 提到 \"deterministic selection with seed 42\"，建议简要说明 seed 42 选择的原因或声明为任意选取，避免 reviewer 质疑是否 cherry-picked。\n- **M2**: Table 2 的 \"all others: 0.0\" 建议改为 \"< 0.1%\" 或给出具体数值，避免读者误以为某些方差分量恰好为零。\n- **M3**: Section 4.6 的 Qwen 3B/7B scale validation 仅涉及同一架构家族，建议在该段末尾明确此为初步验证，不宜据此推广到跨架构的 scale transfer。\n- **M4**: Appendix E 的 prompt templates（page 14）建议标注每个 template 的设计理由（为何选择这些特定变体），增强 reproducibility。\n\n---\n\n## Questions\n\n**Q1**: 关于 binary data 的 GLMM complement（Appendix A）：GLMM 和 Henderson Method I 的方差分量 **绝对值** 差异是多少？目前只报告了排序一致性（ρ = 1.0），但对于 D-study budget 计算，绝对值的准确性同样重要。如果 GLMM 给出不同的 G coefficient，D-study budgets 是否需要调整？\n\n**Q2**: 关于 exchangeability：如果将 8 个模型视为 fixed facet（而非 random），对 G coefficient 和 D-study budget 的影响有多大？这将给出一个 lower bound 估计，帮助读者理解 random vs fixed 假设的实际差别。\n\n**Q3**: 关于 forward prediction（Section 4.6）：4→8 模型的预测准确度 |ΔG| = 0.035，这个误差在实际应用中是否足够小？例如，0.035 的 G 差异是否会导致 D-study budget 建议发生实质性变化（如从 55 items 变为 70 items）？\n\n**Q4**: 关于 partial-credit pilot：是否考虑过对 GSM8K 进行多模型 partial-credit 实验（即使是 2-3 个模型），以估计 partial credit 下的 model×item interaction？这将极大增强 Section 3.5 的 limitation discussion。\n\n**Q5**: Table 4 的 D-study budget 建议 \"order-of-magnitude guides\" 的量化含义是什么？预期的投射误差范围是 ±10%, ±30%, 还是 ±50%？\n\n**Q6**: 关于 exp-002 的 reduced crossing validation（ΔG = 0.008）：这个验证是在 MMLU 上进行的（比较 full vs reduced design），是否也在其他 benchmarks 上验证了 reduced crossing 的有效性？\n\n---\n\n## Missing References\n\n未发现明显的 critical missing references。G-theory 核心文献（Brennan, 2001; Shavelson & Webb, 1991/1999）、binary data extensions（Jiang & Strijbos, 2018; Tuerlinckx et al., 2006）、LLM 评估方差文献（Boutilier et al., 2021; Madan et al., 2024; Yuan et al., 2025; Pezeshkpour & Hruschka, 2024）均已覆盖。\n\n**可选补充**: Cardinet, Johnson & Pini (2010) \"Applying Generalizability Theory using EduG\" 作为 G-theory 应用方法论参考可能对不熟悉 G-theory 的 NLP 读者有帮助，但非必需。\n\n---\n\n## Overall Assessment\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n\n**Confidence**: 4 / 5\n\n**理由**:\n\n本文做出了 genuine methodological contribution——首次将 G-theory 系统应用于 LLM 评估方差分解，规模大（230 万记录）、robustness 检查全面（8 项）、实践工具有用（D-study calculator）。写作质量高，结构清晰。\n\n给 3.5 而非 4 的核心原因是两个 Must-Fix 问题的叠加效应：\n\n1. **N1 (exchangeability)** 削弱了 D-study budget 建议（论文最核心的实践贡献）的可推广性——8 个 purposively 选择的模型不能保证方差分量可迁移到 unseen models，而论文的验证（LOMO、forward prediction）均为 within-sample。\n2. **N2 (format pattern)** 将一个 inherently underpowered (p ≥ 0.10 by design) 的探索性观察以核心贡献的结构地位呈现，这在统计方法论论文中是一个 framing 问题。\n\n如果作者 (a) 提供 out-of-sample model validation 或更充分的 exchangeability sensitivity analysis，(b) 将 format pattern 降级为 exploratory observation，我认为本文可以达到 4.0 (Conference) 的水平。当前版本的其余 should-fix 问题（W1-W4）均为可在 revision 中解决的增量改进。\n\n**简言之**: 方法论框架正确且有价值，执行规模令人印象深刻，但两个关键假设（model exchangeability, format pattern significance）的论证需要加强才能支撑论文的核心 claims。\n",
    "reviewer_id": "1",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 489 · 2026-05-22T14:32:34.792032+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3814
}
```

</details>

---


### Assistant

_source line 490 · 2026-05-22T14:32:47.454446+00:00_

审稿意见已提交给 Review Director。

**总结**: 给出 Overall 3.5 (Borderline Conference)，Soundness 3.5，Excitement 3.5，Reproducibility 4.0，Confidence 4。

两个 Must-Fix 问题：
- **N1**: 8 个模型作为 quasi-random facet 的 exchangeability 论证不足——LOMO 和 forward prediction 都是 within-sample 验证，无法保证 D-study budgets 对 unseen models 的可迁移性
- **N2**: Format-associated pattern (n=5, permutation test resolution floor p=0.10) 被列为核心贡献，但统计检验在设计上就无法达到 α=0.05 显著性，呈现层级与证据强度不匹配

四个 Should-Fix 问题涉及 binary scoring limitation 被低估、D-study invariance 假设讨论不足、200-item sample 代表性验证不完整、exp-002 跨基准设计不对称性。如果 N1 和 N2 得到解决，评分可提升至 4.0 (Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1"
}
```

</details>

---


## Round 14

## Round 14

4 recorded events


### User

_source line 491 · 2026-05-22T14:34:03.780000+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 2 的完整审稿意见。请逐条回应：[AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 2 完整审稿意见

**Overall**: 3.5/5 (Borderline Conference)
**Soundness**: 3.5, **Excitement**: 3, **Confidence**: 4

### Strengths
- S1: 全面的析因实验设计（230万条记录，7 facet × 5 benchmark）
- S2: 出色的 robustness 基础设施（GLMM、LOMO、bootstrap CI、probit simulation）
- S3: 可操作的实践贡献（D-study 预算投影，3×3 推荐设计）
- S4: 跨 benchmark 格式关联发现（MC vs FF 方差结构差异）
- S5: Precision separability 实证（BF16/FP16 功能等价）

### Must-Fix 问题

**W1 [Critical]: "10× fewer items" framing 隐藏总评估量 129× 增长**
Abstract 声称 multi-facet 设计需要 10× fewer items（55 vs 552），但 55 items 对应 1,296 conditions/item（总评估量 71,280/model），而 single-condition 仅 552/model——总计算成本增长 129×。Abstract 虽提及 "proportional increase in per-item evaluation conditions" 和 "e.g., the recommended 3-prompt × 3-seed design evaluates each item 9 times"，但读者容易将 55 items 与 9 conditions 关联（55×9=495），而实际 55 items 是在 1,296 conditions 下得到的。LLM 评估主要成本是推理计算量而非 item 编写量，privileging item count over total evaluation budget 与实践者核心关切错位。

**W2 [Critical]: Target universe 窄但 framing 宽**
所有实验仅用 7-9B instruct 模型，model 主效应仅 2.5%。标题 "Open-Weight LLM Evaluation" 和 D-study 推荐表的通用表述可能导致读者将 budgets 推广到能力差异更大的场景（1B vs 70B、base vs chat vs reasoning）。Limitations 提及范围限制但 Abstract/Conclusion 未声明。

### Should-Fix 问题

**W3 [Warning]: 相对 Messing (2026) 增量有限**
扩展——增加 infrastructure facets、跨 benchmark、D-study projection——均为标准 G-theory 机制的直接应用，概念上不构成新框架。"crossing infrastructure and methodology facets" 本质是"在更多维度上做同样的事"。

**W4 [Warning]: 仅使用二值评分**
排除了连续指标（BLEU, ROUGE, human ratings）和 log-likelihood 评估。G-theory 本身更适合连续结果变量。

**W5 [Warning]: 跨 benchmark 分析缺乏解释性深度**
MC vs FF 差异仅描述性报告，未分析 item 特征（难度、主题、推理类型）如何预测 model×item 交互大小。

### 小问题
- P1: σ²_τ 和 σ²_δ 定义建议用独立公式编号
- P2: Table 2 "all others" 建议列出具体交互项
- P3: Figure 1 仅 MMLU，建议提供全 5 benchmark D-study 曲线
- P4: Section 4.2 "(1.1 c.u., 1.0)" 含义不明
- P5: Anonymous (2025) arXiv:2601.00822 匿名性风险
- P6: Section 4.6 G_obs=0.71 for sub-families 的重要限制未充分强调

### Questions
- Q1: 推荐 3×3 设计在 G≥0.80 时需多少 items？
- Q2: 加入 1B/70B 模型后 budget ratio 如何变化？
- Q3: Item 特征与 model×item 交互大小是否有系统关系？
- Q4: Ordering facet 仅作用于 MMLU 如何影响跨 benchmark 可比性？
- Q5: 加入 few-shot example identity facet 后 budgets 如何变化？
- Q6: G_obs=0.71 (sub-family) 是否意味着 budgets 仅对跨架构比较有效？

### Missing References
- Gao et al. (2024) lm-evaluation-harness
- Kunovsky and Evans (2025) 引用准确性需确认
- 建议讨论 G-theory 在其他领域的 D-study 实践经验

---

请逐条回应每个 Must-Fix、Should-Fix、Minor、Question 和 Missing Reference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 492 · 2026-05-22T14:36:48.569069+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R2-W1: \"10× fewer items\" framing 隐藏总评估量增长**\n\n同意这是一个重要的 framing 问题。Abstract 的 \"55 versus 552 items\" 比较在 item count 维度上成立，但对 LLM 评估实践者而言，核心成本是推理计算量（inference FLOPs），不是 item 编写量。R2 的计算正确：55 items × 1,296 conditions/item = 71,280 evaluations/model vs single-condition 552 evaluations/model，总计算量增长约 129×。\n\n补充两点：\n1. Abstract 确实提到 \"proportional increase in per-item evaluation conditions\" 并给出了 3×3 = 9 conditions 的推荐示例，但 55 items 的 D-study 投射是在 full 1,296-condition 设计下做出的。如果仅用 3×3 = 9 conditions，需要的 items 数会显著高于 55，但论文 **没有给出这个数字**——这正是 R2-Q1 追问的问题。这个缺失信息使读者无法评估推荐设计的实际总成本。\n2. 这个 framing 问题与我的 N1（exchangeability）叠加——如果 D-study budgets 的可靠性本身就因模型 exchangeability 存疑而打折，而实际计算成本又被低估，论文最核心的实践建议的可信度会进一步下降。\n\n**建议**：Section 4.5 应增加一张 \"total evaluation budget\" 对比表（items × conditions = total evaluations），使读者能直接比较不同设计方案的实际推理成本。\n\n---\n\n**[AGREE] R2-W2: Target universe 窄但 framing 宽**\n\n完全同意，这与我的 N1 高度重叠。补充一个 R2 指出而我遗漏的具体证据：model 主效应仅 2.5%（Table 2），这正是因为 8 个模型都是 7-9B instruct、能力差距有限。如果引入 1B vs 70B 或 base vs chat 的对比，model 主效应和 model×item 交互的比例可能根本性改变，D-study budgets 随之失效。\n\n论文标题 \"Open-Weight LLM Evaluation\" 和 Section 5 结论段的通用建议措辞（\"multi-facet designs require 10× fewer items\"）确实超出了实验支撑的范围。至少 Abstract 和 Conclusion 应加上 \"for 7-9B instruction-tuned models\" 的 scope qualifier。\n\n---\n\n## Should-Fix 问题\n\n**[REBUT] R2-W3: 相对 Messing (2026) 增量有限**\n\n不同意 \"增量有限\" 的判断，理由如下：\n\n1. **交叉 infrastructure 和 methodology facets 不是简单地 \"在更多维度上做同样的事\"**。Messing (2026) 仅分解了 5 个 methodology facets（judge identity: 43.8%），但排除了 infrastructure facets（precision, seed, temperature）。本文的关键发现之一正是 infrastructure×methodology 交互的结构：precision 的贡献极小（< 0.1%），而 prompt×item 交互（2.5%）和 model×item 交互（30-37%）的 joint structure 只有在同时交叉两类 facets 时才能被识别。如果只看 methodology facets，研究者无法知道 seed/temperature 的贡献是否可忽略——这对评估设计的简化建议（如 Section 4.4 的 precision separability）至关重要。\n\n2. **跨 benchmark 扩展产生了 Messing (2026) 无法提供的新经验知识**。Messing 仅在单一 benchmark 上工作。本文的 exp-002 跨 5 个 benchmarks 发现了 MC vs FF 的方差结构差异模式（Table 3, Figure 3），尽管统计功效有限（如我的 N2 所述），但这一经验观察本身是新的。\n\n3. **D-study budget calculator 是从方法到工具的转化**。G-theory 的 D-study 机制本身不新，但将方差分量转化为可供社区直接使用的 budget 工具，降低了方法的使用门槛。这在 NLP 社区中属于有价值的 resource contribution（ARR CFP 明确列出 resource papers 为可接受的贡献类型）。\n\n综上，我认为论文的贡献不在于 G-theory 的方法论创新，而在于 **首次在 LLM 评估场景下进行系统性多 facet 应用并产生可操作的实践建议**。对于 EMNLP 这样以应用为导向的 venue，这构成充分的贡献。\n\n---\n\n**[AGREE] R2-W4: 仅使用二值评分**\n\n同意，这与我的 W1 一致。补充：R2 正确指出 G-theory 本身更适合连续结果变量（Brennan, 2001 的 formulation 基于连续分数）。论文的 binary data robustness 检查（Appendix A: GLMM, probit simulation, null calibration）虽然全面，但本质上都是在验证 \"binary data 下 Method I 没有严重偏差\"，而非论证 \"binary data 是最佳选择\"。如果作者能在至少一个 benchmark 上用连续指标（如 GSM8K 的 step-level partial credit 或 log-likelihood scoring）做完整的多模型 G-study，说服力会大幅提升。\n\n---\n\n**[PARTIALLY AGREE] R2-W5: 跨 benchmark 分析缺乏解释性深度**\n\n部分同意。R2 提出的 \"item 特征（难度、主题、推理类型）如何预测 model×item 交互大小\" 是一个有价值的分析方向，但我认为它属于 **future work** 而非当前论文的 weakness：\n\n- 论文的核心贡献是方差分解框架和 D-study budgets，不是解释 model×item 交互的来源。\n- 将 model×item 交互与 item 特征关联需要额外的 item metadata 编码和回归分析，工作量相当于另一篇论文。\n- 不过，Section 4.3 对 MC vs FF 差异 **仅有描述性报告而无机制解释** 确实降低了该 section 的深度。如果作者能增加 1-2 段关于可能机制的讨论（例如：FF benchmarks 的方差分散可能源于生成过程的随机性更高、评分粒度更粗等），即使无定量分析也会改善。\n\n---\n\n## 小问题\n\n**[AGREE] R2-P1**: σ²_τ 和 σ²_δ 的公式编号建议合理，有助于后续引用。\n\n**[AGREE] R2-P2**: 与我的 M2 一致。Table 2 的 \"all others: 0.0\" 应列出具体交互项名称和数值（即使 < 0.1%）。\n\n**[PARTIALLY AGREE] R2-P3**: Figure 1 仅展示 MMLU 的 D-study 曲线，在正文空间有限的情况下可以理解。但 Appendix B 的 Table 7 已提供了全 5 benchmark 的 cross-model D-study budgets。建议折中：在 Appendix 中增加 5-benchmark D-study 曲线图。论文正文提到 Figure 1 \"visualizes the D-study curves\"（Section 4.5 末尾），如果该句能改为 \"Figure 1 visualizes the D-study curves for MMLU; analogous curves for all benchmarks appear in Appendix B\"，信息完整性即可满足。\n\n**[AGREE] R2-P4**: \"(1.1 c.u., 1.0)\" 含义确实不明。我阅读 Section 4.2 时也注意到这个缩写未被定义。如果 \"c.u.\" 指 \"conditional units\" 或类似概念，需要在首次使用时给出定义。\n\n**[AGREE] R2-P5**: Anonymous (2025) arXiv:2601.00822 确实存在匿名性风险。在 double-blind review 下，如果该引用是作者自引，应在 camera-ready 阶段处理。如果不是自引，则可能暴露了一个作者未注意的 de-anonymization 线索。\n\n**[AGREE] R2-P6**: 与我的 M3 一致。Section 4.6 的 G_obs = 0.71 (2-model sub-family) 意味着 2 个同架构模型不足以提供可靠的跨模型测量，这一重要限制应更突出地讨论，而非仅在段末一带而过。\n\n---\n\n## Questions\n\n**[AGREE relevance] R2-Q1**: 推荐 3×3 设计在 G ≥ 0.80 时需多少 items——这正是解决 R2-W1 framing 问题的关键数据。论文应提供 recommended design（3 prompts × 3 seeds = 9 conditions/item）下的 D-study 投射，而非仅在 full 1,296-condition 设计下报告。\n\n**[AGREE relevance] R2-Q2**: 加入 1B/70B 模型后 budget ratio 变化——与 R2-W2 和我的 N1 直接相关。model 主效应 2.5% 在同质化的 7-9B 模型下或许合理，但能力差异更大时会显著上升。作者至少应在 discussion 中定性分析预期方向。\n\n**[PARTIALLY AGREE] R2-Q3**: Item 特征与 model×item 交互的关系——有价值的问题但超出当前论文范围（如我对 W5 的回应）。建议作者在 future work 中提及。\n\n**[AGREE relevance] R2-Q4**: Ordering facet 仅作用于 MMLU——与我的 W4 一致。这不仅影响跨 benchmark 可比性，还可能是 MC vs FF 方差结构差异的 confound 之一。\n\n**[NEUTRAL] R2-Q5**: Few-shot example identity facet——有趣的扩展建议但不是当前论文的缺陷。论文的 facet selection 已经相当全面，增加 example identity 会导致设计规模爆炸。\n\n**[AGREE relevance] R2-Q6**: G_obs = 0.71 (sub-family) 是否意味着 budgets 仅对跨架构有效——这是 Section 4.6 scale validation 结论的直接推论，论文应明确回答。\n\n---\n\n## Missing References\n\n**[AGREE] Gao et al. (2024) lm-evaluation-harness**: 论文使用标准 benchmarks（MMLU, ARC, HellaSwag, GSM8K, MATH）进行评估，lm-evaluation-harness 是该领域最广泛使用的评估框架。即使论文未使用该框架实现实验，作为评估基础设施的引用也应包含。\n\n**[AGREE] Kunovsky and Evans (2025) 引用准确性**: 应由作者确认该引用的完整信息。\n\n**[NEUTRAL] G-theory 在其他领域的 D-study 实践经验**: 有参考价值但非必需。论文已引用 Brennan (2001)、Shavelson & Webb (1991/1999) 等核心文献。\n\n---\n\n## 总结：与 R2 的共识与分歧\n\n### 主要共识\n1. **D-study budget 的 total evaluation cost framing 需要修正**（R2-W1）——我补充了这一 framing 问题与 exchangeability 问题的叠加效应\n2. **Target universe 窄但 framing 宽**（R2-W2 ≈ 我的 N1）——核心 exchangeability concern 一致\n3. **Binary scoring 限制**（R2-W4 ≈ 我的 W1）——partial-credit pilot 不足以缓解\n4. **Table 2 / G_obs=0.71 等具体呈现问题**（R2-P2, P6 ≈ 我的 M2, M3）\n\n### 主要分歧\n1. **R2-W3 (增量有限)**: 我反驳了这一判断——论文的贡献在于首次系统性应用，交叉 infrastructure + methodology facets 的联合分析不是 trivial extension，D-study calculator 作为 resource 有独立价值\n2. **R2-W5 (解释性深度)**: 我认为 item 特征分析属于 future work 而非 weakness，但同意 Section 4.3 应增加机制讨论\n\n### 对 Overall Score 的影响\nR2 给 3.5，我也给 3.5。R2 的 W1（cost framing）是我原审中未充分关注的有效新问题。这进一步支持 borderline conference 的判断：论文方法论框架正确、规模大、robustness 全面，但核心实践建议（D-study budgets）的 framing 和 generalizability 存在多个需要修正的问题。修正后（明确 scope、增加 total cost 对比、提供推荐设计的 D-study 投射）有望达到 4.0 (Conference)。\n",
  "reviewer_id": "1",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 1 对 Reviewer 2 审稿意见的逐条回应\n\n---\n\n## Must-Fix 问题\n\n**[AGREE] R2-W1: \"10× fewer items\" framing 隐藏总评估量增长**\n\n同意这是一个重要的 framing 问题。Abstract 的 \"55 versus 552 items\" 比较在 item count 维度上成立，但对 LLM 评估实践者而言，核心成本是推理计算量（inference FLOPs），不是 item 编写量。R2 的计算正确：55 items × 1,296 conditions/item = 71,280 evaluations/model vs single-condition 552 evaluations/model，总计算量增长约 129×。\n\n补充两点：\n1. Abstract 确实提到 \"proportional increase in per-item evaluation conditions\" 并给出了 3×3 = 9 conditions 的推荐示例，但 55 items 的 D-study 投射是在 full 1,296-condition 设计下做出的。如果仅用 3×3 = 9 conditions，需要的 items 数会显著高于 55，但论文 **没有给出这个数字**——这正是 R2-Q1 追问的问题。这个缺失信息使读者无法评估推荐设计的实际总成本。\n2. 这个 framing 问题与我的 N1（exchangeability）叠加——如果 D-study budgets 的可靠性本身就因模型 exchangeability 存疑而打折，而实际计算成本又被低估，论文最核心的实践建议的可信度会进一步下降。\n\n**建议**：Section 4.5 应增加一张 \"total evaluation budget\" 对比表（items × conditions = total evaluations），使读者能直接比较不同设计方案的实际推理成本。\n\n---\n\n**[AGREE] R2-W2: Target universe 窄但 framing 宽**\n\n完全同意，这与我的 N1 高度重叠。补充一个 R2 指出而我遗漏的具体证据：model 主效应仅 2.5%（Table 2），这正是因为 8 个模型都是 7-9B instruct、能力差距有限。如果引入 1B vs 70B 或 base vs chat 的对比，model 主效应和 model×item 交互的比例可能根本性改变，D-study budgets 随之失效。\n\n论文标题 \"Open-Weight LLM Evaluation\" 和 Section 5 结论段的通用建议措辞（\"multi-facet designs require 10× fewer items\"）确实超出了实验支撑的范围。至少 Abstract 和 Conclusion 应加上 \"for 7-9B instruction-tuned models\" 的 scope qualifier。\n\n---\n\n## Should-Fix 问题\n\n**[REBUT] R2-W3: 相对 Messing (2026) 增量有限**\n\n不同意 \"增量有限\" 的判断，理由如下：\n\n1. **交叉 infrastructure 和 methodology facets 不是简单地 \"在更多维度上做同样的事\"**。Messing (2026) 仅分解了 5 个 methodology facets（judge identity: 43.8%），但排除了 infrastructure facets（precision, seed, temperature）。本文的关键发现之一正是 infrastructure×methodology 交互的结构：precision 的贡献极小（< 0.1%），而 prompt×item 交互（2.5%）和 model×item 交互（30-37%）的 joint structure 只有在同时交叉两类 facets 时才能被识别。如果只看 methodology facets，研究者无法知道 seed/temperature 的贡献是否可忽略——这对评估设计的简化建议（如 Section 4.4 的 precision separability）至关重要。\n\n2. **跨 benchmark 扩展产生了 Messing (2026) 无法提供的新经验知识**。Messing 仅在单一 benchmark 上工作。本文的 exp-002 跨 5 个 benchmarks 发现了 MC vs FF 的方差结构差异模式（Table 3, Figure 3），尽管统计功效有限（如我的 N2 所述），但这一经验观察本身是新的。\n\n3. **D-study budget calculator 是从方法到工具的转化**。G-theory 的 D-study 机制本身不新，但将方差分量转化为可供社区直接使用的 budget 工具，降低了方法的使用门槛。这在 NLP 社区中属于有价值的 resource contribution（ARR CFP 明确列出 resource papers 为可接受的贡献类型）。\n\n综上，我认为论文的贡献不在于 G-theory 的方法论创新，而在于 **首次在 LLM 评估场景下进行系统性多 facet 应用并产生可操作的实践建议**。对于 EMNLP 这样以应用为导向的 venue，这构成充分的贡献。\n\n---\n\n**[AGREE] R2-W4: 仅使用二值评分**\n\n同意，这与我的 W1 一致。补充：R2 正确指出 G-theory 本身更适合连续结果变量（Brennan, 2001 的 formulation 基于连续分数）。论文的 binary data robustness 检查（Appendix A: GLMM, probit simulation, null calibration）虽然全面，但本质上都是在验证 \"binary data 下 Method I 没有严重偏差\"，而非论证 \"binary data 是最佳选择\"。如果作者能在至少一个 benchmark 上用连续指标（如 GSM8K 的 step-level partial credit 或 log-likelihood scoring）做完整的多模型 G-study，说服力会大幅提升。\n\n---\n\n**[PARTIALLY AGREE] R2-W5: 跨 benchmark 分析缺乏解释性深度**\n\n部分同意。R2 提出的 \"item 特征（难度、主题、推理类型）如何预测 model×item 交互大小\" 是一个有价值的分析方向，但我认为它属于 **future work** 而非当前论文的 weakness：\n\n- 论文的核心贡献是方差分解框架和 D-study budgets，不是解释 model×item 交互的来源。\n- 将 model×item 交互与 item 特征关联需要额外的 item metadata 编码和回归分析，工作量相当于另一篇论文。\n- 不过，Section 4.3 对 MC vs FF 差异 **仅有描述性报告而无机制解释** 确实降低了该 section 的深度。如果作者能增加 1-2 段关于可能机制的讨论（例如：FF benchmarks 的方差分散可能源于生成过程的随机性更高、评分粒度更粗等），即使无定量分析也会改善。\n\n---\n\n## 小问题\n\n**[AGREE] R2-P1**: σ²_τ 和 σ²_δ 的公式编号建议合理，有助于后续引用。\n\n**[AGREE] R2-P2**: 与我的 M2 一致。Table 2 的 \"all others: 0.0\" 应列出具体交互项名称和数值（即使 < 0.1%）。\n\n**[PARTIALLY AGREE] R2-P3**: Figure 1 仅展示 MMLU 的 D-study 曲线，在正文空间有限的情况下可以理解。但 Appendix B 的 Table 7 已提供了全 5 benchmark 的 cross-model D-study budgets。建议折中：在 Appendix 中增加 5-benchmark D-study 曲线图。论文正文提到 Figure 1 \"visualizes the D-study curves\"（Section 4.5 末尾），如果该句能改为 \"Figure 1 visualizes the D-study curves for MMLU; analogous curves for all benchmarks appear in Appendix B\"，信息完整性即可满足。\n\n**[AGREE] R2-P4**: \"(1.1 c.u., 1.0)\" 含义确实不明。我阅读 Section 4.2 时也注意到这个缩写未被定义。如果 \"c.u.\" 指 \"conditional units\" 或类似概念，需要在首次使用时给出定义。\n\n**[AGREE] R2-P5**: Anonymous (2025) arXiv:2601.00822 确实存在匿名性风险。在 double-blind review 下，如果该引用是作者自引，应在 camera-ready 阶段处理。如果不是自引，则可能暴露了一个作者未注意的 de-anonymization 线索。\n\n**[AGREE] R2-P6**: 与我的 M3 一致。Section 4.6 的 G_obs = 0.71 (2-model sub-family) 意味着 2 个同架构模型不足以提供可靠的跨模型测量，这一重要限制应更突出地讨论，而非仅在段末一带而过。\n\n---\n\n## Questions\n\n**[AGREE relevance] R2-Q1**: 推荐 3×3 设计在 G ≥ 0.80 时需多少 items——这正是解决 R2-W1 framing 问题的关键数据。论文应提供 recommended design（3 prompts × 3 seeds = 9 conditions/item）下的 D-study 投射，而非仅在 full 1,296-condition 设计下报告。\n\n**[AGREE relevance] R2-Q2**: 加入 1B/70B 模型后 budget ratio 变化——与 R2-W2 和我的 N1 直接相关。model 主效应 2.5% 在同质化的 7-9B 模型下或许合理，但能力差异更大时会显著上升。作者至少应在 discussion 中定性分析预期方向。\n\n**[PARTIALLY AGREE] R2-Q3**: Item 特征与 model×item 交互的关系——有价值的问题但超出当前论文范围（如我对 W5 的回应）。建议作者在 future work 中提及。\n\n**[AGREE relevance] R2-Q4**: Ordering facet 仅作用于 MMLU——与我的 W4 一致。这不仅影响跨 benchmark 可比性，还可能是 MC vs FF 方差结构差异的 confound 之一。\n\n**[NEUTRAL] R2-Q5**: Few-shot example identity facet——有趣的扩展建议但不是当前论文的缺陷。论文的 facet selection 已经相当全面，增加 example identity 会导致设计规模爆炸。\n\n**[AGREE relevance] R2-Q6**: G_obs = 0.71 (sub-family) 是否意味着 budgets 仅对跨架构有效——这是 Section 4.6 scale validation 结论的直接推论，论文应明确回答。\n\n---\n\n## Missing References\n\n**[AGREE] Gao et al. (2024) lm-evaluation-harness**: 论文使用标准 benchmarks（MMLU, ARC, HellaSwag, GSM8K, MATH）进行评估，lm-evaluation-harness 是该领域最广泛使用的评估框架。即使论文未使用该框架实现实验，作为评估基础设施的引用也应包含。\n\n**[AGREE] Kunovsky and Evans (2025) 引用准确性**: 应由作者确认该引用的完整信息。\n\n**[NEUTRAL] G-theory 在其他领域的 D-study 实践经验**: 有参考价值但非必需。论文已引用 Brennan (2001)、Shavelson & Webb (1991/1999) 等核心文献。\n\n---\n\n## 总结：与 R2 的共识与分歧\n\n### 主要共识\n1. **D-study budget 的 total evaluation cost framing 需要修正**（R2-W1）——我补充了这一 framing 问题与 exchangeability 问题的叠加效应\n2. **Target universe 窄但 framing 宽**（R2-W2 ≈ 我的 N1）——核心 exchangeability concern 一致\n3. **Binary scoring 限制**（R2-W4 ≈ 我的 W1）——partial-credit pilot 不足以缓解\n4. **Table 2 / G_obs=0.71 等具体呈现问题**（R2-P2, P6 ≈ 我的 M2, M3）\n\n### 主要分歧\n1. **R2-W3 (增量有限)**: 我反驳了这一判断——论文的贡献在于首次系统性应用，交叉 infrastructure + methodology facets 的联合分析不是 trivial extension，D-study calculator 作为 resource 有独立价值\n2. **R2-W5 (解释性深度)**: 我认为 item 特征分析属于 future work 而非 weakness，但同意 Section 4.3 应增加机制讨论\n\n### 对 Overall Score 的影响\nR2 给 3.5，我也给 3.5。R2 的 W1（cost framing）是我原审中未充分关注的有效新问题。这进一步支持 borderline conference 的判断：论文方法论框架正确、规模大、robustness 全面，但核心实践建议（D-study budgets）的 framing 和 generalizability 存在多个需要修正的问题。修正后（明确 scope、增加 total cost 对比、提供推荐设计的 D-study 投射）有望达到 4.0 (Conference)。\n",
    "reviewer_id": "1",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 493 · 2026-05-22T14:36:52.281664+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3712
}
```

</details>

---


### Assistant

_source line 494 · 2026-05-22T14:37:00.206038+00:00_

交叉回应已提交。

核心结论：与 R2 在多数问题上达成共识（cost framing、narrow universe、binary limitation），但在 **W3 (增量有限)** 上明确反驳——首次系统性多 facet 应用 + D-study calculator 构成 EMNLP 可接受的贡献。R2 的 W1（total evaluation cost）是我原审遗漏的有效新问题，进一步支持 3.5 (Borderline Conference) 的评分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1"
}
```

</details>

---


## Round 15

## Round 15

50 recorded events


### User

_source line 495 · 2026-05-22T15:07:31.181780+00:00_

[Round 1 审稿请求]:
你是 Reviewer 1，负责**方法严谨性**审查。

## Venue 信息
- **目标会议**: EMNLP 2026（通过 ACL Rolling Review 统一审稿）
- **截止日期**: 2026-05-25
- **格式**: ACL 模板，Long paper 正文 ≤8 页，参考文献不限，Limitations 必写（不计入页数），Ethics 可选（不计入页数）
- **匿名**: Double-blind

## 论文文件
- LaTeX: `projects/nlp_variance_gtheory/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/submitted.pdf`

## 你的审查侧重

重点评估以下方面：

1. **G-theory 应用正确性**：Henderson Method I 在 binary 数据上的适用性论证是否充分？probit simulation、GLMM complement、accuracy-range stability 等 robustness analyses 是否令人信服？
2. **统计方法**：bootstrap CI 的 item-level resampling 策略是否合理？stratified bootstrap 是否必要？jackknife 对比是否充分？
3. **实验设计**：7-facet fully crossed design 的合理性——200 items 从 10/57 subjects 分层抽样的代表性？8 purposively selected models 作为 quasi-random facet 的辩护？reduced crossing (exp-002) 的 validity？
4. **D-study projection**：方差分量不变性假设（variance component invariance）在 item pool expansion、model universe expansion、temporal drift 下是否成立？forward prediction validation 的解释力？
5. **Binary scoring limitation**：所有发现限于 binary correctness scoring，partial-credit pilot (GSM8K) 显示方差结构根本性改变——这对核心结论的限制是否被充分讨论？
6. **Format-associated patterns (§4.3)**：n=5 benchmarks 下 permutation test p=0.10 的统计功效；MC vs FF 设计不对称性（ordering 仅 MC，prompt semantics 不同）是否可能混淆格式效应？
7. **Scope claims**：标题 "Open-Weight LLM Evaluation" vs 实际范围（7-9B instruction-tuned, binary scoring）——是否存在 overclaiming？

请按 ARR 审稿标准给出完整审稿意见，包括 Summary、Strengths、Weaknesses（逐条编号）、Questions、Missing References、Overall Assessment。Weaknesses 必须严格、具体，引用论文具体 Section/Table/Figure。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 496 · 2026-05-22T15:07:37.572345+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 497 · 2026-05-22T15:07:38.375544+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_1_2814bee3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 498 · 2026-05-22T15:07:38.526368+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 499 · 2026-05-22T15:07:38.627100+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 500 · 2026-05-22T15:07:43.790236+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 501 · 2026-05-22T15:07:44.592499+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/submitted.pdf",
  "project": "nlp_variance_gtheory",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/submitted.pdf",
    "project": "nlp_variance_gtheory",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 502 · 2026-05-22T15:07:51.684547+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"}]

Based on the search results, I found information about ACL Rolling Review (ARR) 2026 guidelines. Here's what I found:

## ARR Reviewer Guidelines

If you feel qualified to review some aspects of the paper but not others (e.g. experimental results but not formal proofs), please state in the review if you did not check some major parts, such as proofs.

The third check is on academic conflicts of interest. If the submission looks like something that is very close to your own work about to be submitted, it is best to recuse yourself.

## Review Standards

The reviews will not be specific to a conference/venue, but the standards expected by reviewers are those o
…[truncated 708 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "WebSearch",
  "elapsed_ms": 7894
}
```

</details>

---


### Tool result

_source line 503 · 2026-05-22T15:07:53.999855+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.7}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 497.2}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 585.9}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 548.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 488.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 500.1}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 504.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 503.0}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 553.9}, {\"page\":
…[truncated 438 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 9407
}
```

</details>

---


### Tool call

_source line 504 · 2026-05-22T15:07:58.615543+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/submitted.pdf",
  "project": "nlp_variance_gtheory",
  "pages": "11-14",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/submitted.pdf",
    "project": "nlp_variance_gtheory",
    "pages": "11-14",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 505 · 2026-05-22T15:08:00.972257+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 566.3}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.6}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 413.5}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 301.5}], \"total_pages\": 14, \"rendered_pages\": 4, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_1",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2356
}
```

</details>

---
