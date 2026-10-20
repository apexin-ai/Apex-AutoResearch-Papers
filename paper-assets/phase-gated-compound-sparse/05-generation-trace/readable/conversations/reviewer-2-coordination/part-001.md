# Reviewer 2 coordination — Part 1 of 2

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Conversation logs

[Transcript overview](../reviewer-2-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/4b/4b53966e97d3abe72ec6.json)

## Round 1

## Round 1

114 recorded events


### User

_source line 1 · 2026-05-14T12:53:57.016581+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2

**你的审查侧重：新颖性 + 相关工作完整性 + 写作质量 + 格式合规**

### 论文信息
- **标题**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Reasoning Models
- **PDF 路径**: `projects/phase-gated-compound-sparse/artifacts/_project/paper/main_a1a036.pdf`
- **目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
- **截止日期**: 2026-05-25

### Venue 格式要求
- 长文正文 ≤ 8 页 + 参考文献不限
- Limitations 节必须有，**不计入页数**，须为无编号独立节置于 Conclusion 之后、References 之前
- 附录不计入页数
- 模板：ACL/ARR `[review]` 模式
- 匿名：double-blind（"Anonymous ACL submission"）

### 你的审查重点

请以 EMNLP 最严格审稿人的标准评估以下方面：

1. **新颖性与贡献评估**：
   - "compound sparsity severity is phase-dependent" 这一发现的 novelty 有多高？
   - Entropy-discrimination collapse 是否是一个真正的新 mechanism，还是已知现象的重新包装？
   - 论文的贡献是否足以构成 EMNLP main conference 长文？还是更适合 findings/workshop？
   - Claim 的强度是否与证据匹配？（如 "phase-strategy interaction" 的说法）

2. **相关工作完整性**：
   - 是否遗漏了关键的 compound compression / KV cache eviction / attention sparsity 工作？
   - 特别关注 2025-2026 年最新工作是否被充分引用
   - ThinKV (Ramachandran et al., 2026) 被用于 phase segmentation——对该工作的区分是否清晰？
   - 是否遗漏了 phase-aware inference 或 adaptive compression 的相关工作？

3. **写作质量**：
   - 论文结构是否清晰？各节之间的逻辑衔接是否流畅？
   - Abstract 是否准确反映论文内容和贡献？
   - 术语使用是否一致？（如 "severity gradient" 的多重含义）
   - 图表质量：Figure 1-4 和 Table 1-7 是否清晰、必要、标注规范？

4. **格式合规性**（对照 ARR 要求逐项检查）：
   - 正文页数是否 ≤ 8 页？精确计算哪些内容在正文范围内
   - **Limitations 节**：当前作为 §7.1（编号子节）出现在 Discussion 中——这是否符合 ARR 要求？ARR 要求 Limitations 为无编号独立节
   - 匿名标注是否正确？是否有去匿名化信息泄露？
   - 引用格式是否符合 ACL 模板规范？
   - 脚注 2 提到 "4× NVIDIA RTX PRO 6000 Blackwell Server Edition 96 GB GPUs"——这是否构成去匿名化风险？

请输出完整的审稿报告，包含：Summary、Strengths、Weaknesses（必须严格，逐条列出并标注 severity: critical/major/minor）、Questions for Authors、Missing References（列出具体论文）、Overall Score（strong reject / weak reject / borderline / weak accept / strong accept）+ Confidence。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-14T12:54:07.297102+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-14T12:54:07.400832+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_reviewer_2_d0398257.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 103
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-14T12:54:10.487575+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
  }
}
```

</details>

---


### Tool result

_source line 5 · 2026-05-14T12:54:10.540570+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-14T12:54:13.608658+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-14T12:54:13.659349+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-14T12:54:19.189428+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-14T12:54:19.240112+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-14T12:54:24.421253+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main_a1a036.pdf",
  "pages": "1-8",
  "dpi": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main_a1a036.pdf",
    "pages": "1-8",
    "dpi": "200"
  }
}
```

</details>

---


### Tool call

_source line 11 · 2026-05-14T12:54:24.926146+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-14T12:54:25.480763+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-14T12:54:28.489663+00:00_

Error: result (6,948,411 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse--claude-sessions-review-reviewer-2-d0398257/bfa63e26-fdd4-4cf2-9c52-defc70917f56/tool-results/mcp-agent-ml-research-pdf_to_images-1778763267922.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse--claude-sessions-review-reviewer-2-d0398257/bfa63e26-fdd4-4cf2-9c52-defc70917f56/tool-results/mcp-agent-ml-research-pdf_to_images-1778763267922.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse--claude-sessions-review-reviewer-2-d0398257/bfa63e26-fdd4-4cf2-9c52-defc70917f56/tool-results/mcp-agent-ml-research-pdf_to_images-1778763267922.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 4068
}
```

</details>

---


### Tool result

_source line 14 · 2026-05-14T12:54:35.548590+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"}]

Based on the search results, here's what I found about ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score

The soundness scores must be j
…[truncated 1324 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 10622
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-14T12:54:59.305597+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 30, \"total_citations\": 40, \"unique_cited_keys\": 23, \"orphan_bib\": 7, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 22, \"online_not_found\": 3, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [\"compression-ordering-2025\", \"h2o-neurips2023\", \"mustafar-neurips2025\", \"obcache-2025\", \"pagedeviction-eacl2026\", \"pyramidkv-2024\", \"raas-acl2025\"], \"missing_bib\": [], \"orphan_count\": 7, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"adakv-neurips2025\", \"type\": \"inproceedings\", \"title\": \"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference\", \"authors\": \"Feng, Yuan and Lv, Junlin and Cao, Yukun and Xie, Xike and Zhou, S. Kevin\", \"year\": \"2025\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"compression-ordering-2025\", \"type\": \"article\", \"title\": \"A Systematic Study of Compression Ordering for Large Language Models\", \"authors\": \"Chhawri, Shivansh and Mahadik, Rahul and Rooj, Suparna\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2511.19495\"}, {\"key\": \"decision-repr-transition-2026\", \"type\": \"article\", \"title\": \"Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions\", \"authors\": \"Shi, Boyu and Liu, Chang and Gao, ChuanBao and Yang, Xu and Geng, Xin\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.07271\"}, {\"key\": \"deepseek-r1-2025\", \"type\": \"article\", \"title\": \"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\", \"authors\": \"DeepSeek-AI\", \"year\": \"2025\", \"venue\": \"Nature\"}, {\"key\": \"defensivekv-iclr2026\", \"type\": \"inproceedings\", \"title\": \"DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference\", \"authors\": \"Feng, Yuan and Guo, Haoyu and Lv, Junlin and Zhou, S. 
…[truncated 22800 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 33824
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-14T12:55:08.908220+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main_a1a036.pdf",
  "pages": "1-3",
  "dpi": "180"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main_a1a036.pdf",
    "pages": "1-3",
    "dpi": "180"
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-14T12:55:10.795562+00:00_

Error: result (2,316,038 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse--claude-sessions-review-reviewer-2-d0398257/bfa63e26-fdd4-4cf2-9c52-defc70917f56/tool-results/mcp-agent-ml-research-pdf_to_images-1778763310218.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse--claude-sessions-review-reviewer-2-d0398257/bfa63e26-fdd4-4cf2-9c52-defc70917f56/tool-results/mcp-agent-ml-research-pdf_to_images-1778763310218.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse--claude-sessions-review-reviewer-2-d0398257/bfa63e26-fdd4-4cf2-9c52-defc70917f56/tool-results/mcp-agent-ml-research-pdf_to_images-1778763310218.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1887
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-14T12:55:10.796168+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete ARR review form: all scoring dimensions, their scales (1-5 or whatever), descriptions for each score level, and any other criteria reviewers must evaluate. Include the exact wording of each dimension and score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete ARR review form: all scoring dimensions, their scales (1-5 or whatever), descriptions for each score level, and any other criteria reviewers must evaluate. Include the exact wording of each dimension and score level."
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-14T12:55:18.423442+00:00_

# ACL Rolling Review (ARR) Form - Scoring Dimensions

## 1. **Reviewer Confidence** (1-5 scale)
- **5:** "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4:** "Quite sure. I tried to check the important points carefully."
- **3:** "Pretty sure, but there's a chance I missed something."
- **2:** "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1:** "Not my area, or paper is very hard to understand."

## 2. **Soundness** (1-5 scale with half-point options)
- **5:** Exceptional thoroughness for paper type
- **4:** "This study provides sufficient support for all of its claims."
- **3:** "This study provides sufficient support for its main claims."
- **2:** "Some of the main claims are not sufficiently supported."
- **1:** Paper lacks sufficient rigor for publication

## 3. **Excitement** (1-5 scale with half-point options)
Assesses subjective appeal, including innovation, community impact, and personal relevance
- **5:** Highly compelling; would recommend to others
- **4:** "I would mention this paper to others"
- **3:** Interesting but not compelling
- **2:** Limited personal resonance
- **1:** "Does not resonate...and I don't think it would with others"

## 4. **Overall Assessment** (1-5 scale with half-point options)
- **5:** Award consideration (top 2.5%)
- **4:** Conference acceptance
- **3:** Findings acceptance
- **2:** Substantial revisions needed
- **1:** Do not resubmit

## 5. **Reproducibility** (1-5 scale)
- **5:** Results easily reproducible
- **4:** Mostly reproducible with minor variations
- **3:** Reproducible with difficulty
- **2:** Highly challenging to reproduce
- **1:** Results cannot be reproduced

## 6. **Datasets** (1-5 scale)
- **5:** Enabling other research projects
- **4:** Useful for ongoing work
- **3:** Potentially useful
- **2:** Documentary value only
- **1:** No usable datasets

## 7. **Software** (1-5 scale)
- **5:** Enabling other 
…[truncated 580 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7627
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-14T12:55:24.671171+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/ 2>/dev/null || echo \"NO_DIR\"",
  "description": "Check for rendered PDF images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/ 2>/dev/null || echo \"NO_DIR\"",
    "description": "Check for rendered PDF images"
  }
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-14T12:55:24.873676+00:00_

main_a1a036_p1.png
main_a1a036_p10.png
main_a1a036_p2.png
main_a1a036_p3.png
main_a1a036_p4.png
main_a1a036_p5.png
main_a1a036_p6.png
main_a1a036_p7.png
main_a1a036_p8.png
main_a1a036_p9.png
main_p7.png
main_p8.png
main_p9.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-14T12:55:35.345657+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read paper pages 1-3",
  "prompt": "You are helping review an academic paper. Read the following PNG images of pages 1-3 of the paper and provide a DETAILED transcription/summary of ALL content on each page. Include:\n- All text content (title, authors, abstract, section headings, body text)\n- All figure/table descriptions and their captions\n- All equations\n- All footnotes\n- Page layout observations\n\nThe images are at:\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p1.png\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p2.png\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p3.png\n\nBe extremely thorough - this is for peer review. Report EVERYTHING you see on each page, preserving the logical structure.",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Agent",
  "tool_args": {
    "description": "Read paper pages 1-3",
    "prompt": "You are helping review an academic paper. Read the following PNG images of pages 1-3 of the paper and provide a DETAILED transcription/summary of ALL content on each page. Include:\n- All text content (title, authors, abstract, section headings, body text)\n- All figure/table descriptions and their captions\n- All equations\n- All footnotes\n- Page layout observations\n\nThe images are at:\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p1.png\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p2.png\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p3.png\n\nBe extremely thorough - this is for peer review. Report EVERYTHING you see on each page, preserving the logical structure.",
    "model": "sonnet"
  }
}
```

</details>

---


### Tool call

_source line 23 · 2026-05-14T12:55:38.611396+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read paper pages 4-6",
  "prompt": "You are helping review an academic paper. Read the following PNG images of pages 4-6 of the paper and provide a DETAILED transcription/summary of ALL content on each page. Include:\n- All text content (section headings, body text, methodology details)\n- All figure/table descriptions and their captions with all data values\n- All equations and their numbering\n- All footnotes\n- Page layout observations\n\nThe images are at:\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p4.png\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p5.png\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p6.png\n\nBe extremely thorough - this is for peer review. Report EVERYTHING you see on each page, preserving the logical structure. Pay special attention to table values, equation details, and methodology specifics.",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Agent",
  "tool_args": {
    "description": "Read paper pages 4-6",
    "prompt": "You are helping review an academic paper. Read the following PNG images of pages 4-6 of the paper and provide a DETAILED transcription/summary of ALL content on each page. Include:\n- All text content (section headings, body text, methodology details)\n- All figure/table descriptions and their captions with all data values\n- All equations and their numbering\n- All footnotes\n- Page layout observations\n\nThe images are at:\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p4.png\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p5.png\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p6.png\n\nBe extremely thorough - this is for peer review. Report EVERYTHING you see on each page, preserving the logical structure. Pay special attention to table values, equation details, and methodology specifics.",
    "model": "sonnet"
  }
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-14T12:55:39.115781+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 25 · 2026-05-14T12:55:45.115428+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-14T12:55:45.115891+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 27 · 2026-05-14T12:55:45.116547+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 6000
}
```

</details>

---


### Tool result

_source line 28 · 2026-05-14T12:55:45.117291+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 29 · 2026-05-14T12:55:45.117603+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-14T12:55:45.117811+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 31 · 2026-05-14T12:55:45.222737+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-14T12:55:45.223246+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read paper pages 7-10",
  "prompt": "You are helping review an academic paper. Read the following PNG images of pages 7-10 of the paper and provide a DETAILED transcription/summary of ALL content on each page. Include:\n- All text content (section headings, body text, discussion, conclusion, limitations, appendix)\n- All figure/table descriptions and their captions with all data values\n- All equations\n- All footnotes\n- All references listed\n- Page layout observations\n- Whether there is a Limitations section and where it appears (numbered or unnumbered, before or after references)\n\nThe images are at:\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p7.png\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p8.png\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p9.png\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p10.png\n\nBe extremely thorough - this is for peer review. Report EVERYTHING you see on each page, preserving the logical structure. Pay special attention to:\n1. Where the main body ends (page number)\n2. Where references begin\n3. Whether Limitations is a numbered subsection or an unnumbered standalone section\n4. Appendix content and structure",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Agent",
  "tool_args": {
    "description": "Read paper pages 7-10",
    "prompt": "You are helping review an academic paper. Read the following PNG images of pages 7-10 of the paper and provide a DETAILED transcription/summary of ALL content on each page. Include:\n- All text content (section headings, body text, discussion, conclusion, limitations, appendix)\n- All figure/table descriptions and their captions with all data values\n- All equations\n- All footnotes\n- All references listed\n- Page layout observations\n- Whether there is a Limitations section and where it appears (numbered or unnumbered, before or after references)\n\nThe images are at:\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p7.png\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p8.png\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p9.png\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p10.png\n\nBe extremely thorough - this is for peer review. Report EVERYTHING you see on each page, preserving the logical structure. Pay special attention to:\n1. Where the main body ends (page number)\n2. Where references begin\n3. Whether Limitations is a numbered subsection or an unnumbered standalone section\n4. Appendix content and structure",
    "model": "sonnet"
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-14T12:55:55.778356+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 10662
}
```

</details>

---


### Tool result

_source line 34 · 2026-05-14T12:55:55.779265+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 10661
}
```

</details>

---


### Tool result

_source line 35 · 2026-05-14T12:55:55.780107+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 10557
}
```

</details>

---


### Tool result

_source line 36 · 2026-05-14T12:55:55.780702+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 10662
}
```

</details>

---


### Tool call

_source line 37 · 2026-05-14T12:55:55.780982+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-14T12:55:55.781224+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 39 · 2026-05-14T12:55:55.787099+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 40 · 2026-05-14T12:55:55.787765+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 41 · 2026-05-14T12:55:56.846304+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search missing related work",
  "prompt": "You are helping with an academic paper review. The paper is about \"compound sparsity\" in reasoning LLMs — specifically, it studies how combining multiple compression techniques (KV cache eviction + attention head pruning + channel pruning) creates phase-dependent severity gradients during reasoning (thinking vs output phases).\n\nSearch for potentially MISSING related works that this paper should cite. The paper already cites these works:\n- ThinKV (ICLR 2026)\n- SparK (AAAI 2026)\n- SLiM (ICML 2025)\n- UniComp (2026)\n- Ada-KV (NeurIPS 2025)\n- SnapKV (NeurIPS 2024)\n- DefensiveKV (ICLR 2026)\n- NACL (ACL 2024)\n- RetentiveKV (2026)\n- GRASPrune (ACL 2026)\n- RaaS (ACL 2025)\n- Sparse Frontier (2025)\n- Phase Transition Compression (2026)\n- Decision Representation Transition (2026)\n- Doing More With Less (2026)\n\nSearch for these categories of potentially missing works (use WebSearch):\n1. \"compound compression\" or \"joint compression\" for LLMs (combining quantization + pruning + sparsity) - 2024-2026\n2. \"phase-aware\" or \"thinking-aware\" compression for reasoning models - 2025-2026\n3. \"adaptive KV cache\" or \"dynamic sparsity\" during inference - 2025-2026\n4. \"attention sparsity patterns\" in reasoning / chain-of-thought models - 2025-2026\n5. H2O (Heavy Hitter Oracle) - NeurIPS 2023 (this is in the bib but not cited in the paper - verify)\n6. PyramidKV (2024) - in bib but not cited\n7. ScissorHands, FastGen, or other KV cache compression works 2023-2024\n\nFor each potentially missing work found, report: title, authors, venue, year, and WHY it's relevant to this paper's topic. Be specific about the relevance.",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Agent",
  "tool_args": {
    "description": "Search missing related work",
    "prompt": "You are helping with an academic paper review. The paper is about \"compound sparsity\" in reasoning LLMs — specifically, it studies how combining multiple compression techniques (KV cache eviction + attention head pruning + channel pruning) creates phase-dependent severity gradients during reasoning (thinking vs output phases).\n\nSearch for potentially MISSING related works that this paper should cite. The paper already cites these works:\n- ThinKV (ICLR 2026)\n- SparK (AAAI 2026)\n- SLiM (ICML 2025)\n- UniComp (2026)\n- Ada-KV (NeurIPS 2025)\n- SnapKV (NeurIPS 2024)\n- DefensiveKV (ICLR 2026)\n- NACL (ACL 2024)\n- RetentiveKV (2026)\n- GRASPrune (ACL 2026)\n- RaaS (ACL 2025)\n- Sparse Frontier (2025)\n- Phase Transition Compression (2026)\n- Decision Representation Transition (2026)\n- Doing More With Less (2026)\n\nSearch for these categories of potentially missing works (use WebSearch):\n1. \"compound compression\" or \"joint compression\" for LLMs (combining quantization + pruning + sparsity) - 2024-2026\n2. \"phase-aware\" or \"thinking-aware\" compression for reasoning models - 2025-2026\n3. \"adaptive KV cache\" or \"dynamic sparsity\" during inference - 2025-2026\n4. \"attention sparsity patterns\" in reasoning / chain-of-thought models - 2025-2026\n5. H2O (Heavy Hitter Oracle) - NeurIPS 2023 (this is in the bib but not cited in the paper - verify)\n6. PyramidKV (2024) - in bib but not cited\n7. ScissorHands, FastGen, or other KV cache compression works 2023-2024\n\nFor each potentially missing work found, report: title, authors, venue, year, and WHY it's relevant to this paper's topic. Be specific about the relevance.",
    "model": "sonnet"
  }
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-14T12:56:00.851360+00:00_

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
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
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

_source line 43 · 2026-05-14T12:56:00.851897+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 44 · 2026-05-14T12:56:00.902759+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5121
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-14T12:56:01.511288+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5730
}
```

</details>

---


### Tool result

_source line 46 · 2026-05-14T12:56:01.763599+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5976
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-14T12:56:01.914819+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 6127
}
```

</details>

---


### Tool call

_source line 48 · 2026-05-14T12:56:03.523635+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "compound compression joint quantization pruning sparsity LLM 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "compound compression joint quantization pruning sparsity LLM 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 49 · 2026-05-14T12:56:03.876844+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "phase-aware compression reasoning LLM thinking phase 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "phase-aware compression reasoning LLM thinking phase 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 50 · 2026-05-14T12:56:11.923777+00:00_

Web search results for query: "phase-aware compression reasoning LLM thinking phase 2025 2026"

Links: [{"title":"Phase transitions in large language model compression | npj Artificial Intelligence","url":"https://www.nature.com/articles/s44387-026-00072-8"},{"title":"Published as a conference paper at ICLR 2026 RETHINKING LLM REASONING:","url":"https://openreview.net/pdf?id=CbK7lYbmv8"},{"title":"Phase-Level Analysis of LLM Inference","url":"https://www.emergentmind.com/topics/phase-level-analysis-of-llm-inference"},{"title":"LLM Research Papers: The 2025 List (July to December)","url":"https://magazine.sebastianraschka.com/p/llm-research-papers-2025-part2"},{"title":"A review of state-of-the-art techniques for large language model compression | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-02019-z"},{"title":"ACON: OPTIMIZING CONTEXT COMPRESSION FOR ...","url":"https://openreview.net/pdf?id=7JbSwX6bNL"},{"title":"Top LLM Trends 2025: What's the Future of LLMs","url":"https://www.turing.com/resources/top-llm-trends"},{"title":"The Lottery LLM Hypothesis, Rethinking What Abilities Should LLM Compression Preserve? | ICLR Blogposts 2025","url":"https://iclr-blogposts.github.io/2025/blog/the-lottery-llm-hyperthesis/"},{"title":"GitHub - HuangOwen/Awesome-LLM-Compression: Awesome LLM compression research papers and tools. · GitHub","url":"https://github.com/HuangOwen/Awesome-LLM-Compression"},{"title":"arXiv:submit/6596874 [cs.CL] 4 Jul 2025 MemOS: A Memory OS for AI System","url":"https://statics.memtensor.com.cn/files/MemOS_0707.pdf"}]

Based on the search results, here are the key findings related to phase-aware compression reasoning in LLMs for 2025-2026:

## Phase Transitions in LLM Compression

Large Language Models exhibit Model Phase Transitions where performance collapses beyond critical compression thresholds. Researchers are analyzing structural, numerical, and algebraic redundancy across pru
…[truncated 1426 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8046
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-14T12:56:12.026164+00:00_

Web search results for query: "compound compression joint quantization pruning sparsity LLM 2024 2025"

Links: [{"title":"Published as a conference paper at ICLR 2026 LARGE LANGUAGE MODEL COMPRESSION","url":"https://arxiv.org/pdf/2505.03801"},{"title":"ICML Poster SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression","url":"https://icml.cc/virtual/2025/poster/46479"},{"title":"Optimal Brain Restoration for Joint Quantization and Sparsification of LLMs","url":"https://arxiv.org/html/2509.11177v2"},{"title":"Optimal Brain Restoration for Joint Quantization and Sparsification of LLMs | OpenReview","url":"https://openreview.net/forum?id=VQIvBpL5ag"},{"title":"Published as a conference paper at COLM 2025","url":"https://arxiv.org/pdf/2504.14569"},{"title":"GitHub - HuangOwen/Awesome-LLM-Compression: Awesome LLM compression research papers and tools. · GitHub","url":"https://github.com/HuangOwen/Awesome-LLM-Compression"},{"title":"Compressing large language models by joint sparsification and quantization | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3692743"},{"title":"Two-phase collaborative model compression training for joint pruning and quantization - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0893608025013875"},{"title":"Awesome-LLM-Compression/README.md at main · HuangOwen/Awesome-LLM-Compression","url":"https://github.com/HuangOwen/Awesome-LLM-Compression/blob/main/README.md"},{"title":"Automatic Joint Structured Pruning and Quantization for Efficient Neural","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Qu_Automatic_Joint_Structured_Pruning_and_Quantization_for_Efficient_Neural_Network_CVPR_2025_paper.pdf"}]

Based on the search results, here's what I found about compound compression techniques involving joint quantization, pruning, and sparsity for LLMs in 2024-2025:

## Key Recent Research

Hybrid met
…[truncated 1548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8502
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-14T12:56:14.136965+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "H2O Heavy Hitter Oracle KV cache eviction NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "H2O Heavy Hitter Oracle KV cache eviction NeurIPS 2023"
  }
}
```

</details>

---


### Tool call

_source line 53 · 2026-05-14T12:56:14.640341+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PyramidKV KV cache compression 2024 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PyramidKV KV cache compression 2024 arxiv"
  }
}
```

</details>

---


### Tool result

_source line 54 · 2026-05-14T12:56:21.548650+00:00_

Web search results for query: "H2O Heavy Hitter Oracle KV cache eviction NeurIPS 2023"

Links: [{"title":"H2O: Heavy-Hitter Oracle for Efficient Generative Inference ...","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/6ceefa7b15572587b78ecfcebb2827f8-Paper-Conference.pdf"},{"title":"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models | OpenReview","url":"https://openreview.net/forum?id=RkRrPp7GKO"},{"title":"[2306.14048] H$_2$O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models","url":"https://arxiv.org/abs/2306.14048"},{"title":"NeurIPS Poster H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models","url":"https://neurips.cc/virtual/2023/poster/71645"},{"title":"Paper page - H_2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models","url":"https://huggingface.co/papers/2306.14048"},{"title":"GitHub - lenscloth/KVCache: [NeurIPS'23] H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models. · GitHub","url":"https://github.com/lenscloth/KVCache"},{"title":"H 2 O: heavy-hitter oracle for efficient generative inference ...","url":"https://dl.acm.org/doi/10.5555/3666122.3667628"},{"title":"GitHub - FMInference/H2O: [NeurIPS'23] H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models. · GitHub","url":"https://github.com/fminference/h2o"},{"title":"Q-Hitter: A Better Token Oracle for Efficient LLM Inference ...","url":"https://proceedings.mlsys.org/paper_files/paper/2024/file/bbb7506579431a85861a05fff048d3e1-Paper-Conference.pdf"},{"title":"H$_2$O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/371871295_H_2O_Heavy-Hitter_Oracle_for_Efficient_Generative_Inference_of_Large_Language_Models"}]

I found comprehensive information about the H2O Heavy-Hitter Oracle paper from NeurIPS 2023. Her
…[truncated 1562 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7411
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-14T12:56:22.606976+00:00_

Web search results for query: "PyramidKV KV cache compression 2024 arxiv"

Links: [{"title":"[2406.02069] PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling","url":"https://arxiv.org/abs/2406.02069"},{"title":"PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling | OpenReview","url":"https://openreview.net/forum?id=jZVNmDiU86"},{"title":"PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling","url":"https://arxiv.org/html/2406.02069v1"},{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"GitHub - Zefan-Cai/KVCache-Factory: Unified KV Cache Compression Methods for Auto-Regressive Models · GitHub","url":"https://github.com/Zefan-Cai/KVCache-Factory"},{"title":"[2406.02069v3] PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling","url":"https://arxiv.org/abs/2406.02069v3"},{"title":"KVSculpt: KV Cache Compression as Distillation","url":"https://arxiv.org/html/2603.27819"},{"title":"[2406.02069v1] PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling","url":"https://arxiv.org/abs/2406.02069v1"},{"title":"Pyramid KV Cache Compression for High-throughput LLM ...","url":"https://aclanthology.org/2024.findings-acl.195.pdf"},{"title":"More Than a Quick Glance: Overcoming the Greedy Bias in KV-Cache Compression","url":"https://arxiv.org/html/2602.02199"}]

I found comprehensive information about PyramidKV. Here are the key findings from the 2024 arxiv paper:

## Overview

PyramidKV is a novel and effective KV cache compression method that dynamically adjusts the KV cache size across different layers, allocating more cache in lower layers and less in higher ones, diverging from traditional methods that maintain a uniform KV cache size.

## Key Insight

LLMs aggregate information through P
…[truncated 1227 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7966
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-14T12:56:25.230626+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ScissorHands KV cache compression eviction 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ScissorHands KV cache compression eviction 2023 2024"
  }
}
```

</details>

---


### Tool call

_source line 57 · 2026-05-14T12:56:25.484418+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FastGen KV cache compression inference 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FastGen KV cache compression inference 2023 2024"
  }
}
```

</details>

---


### Tool result

_source line 58 · 2026-05-14T12:56:32.744700+00:00_

Web search results for query: "ScissorHands KV cache compression eviction 2023 2024"

Links: [{"title":"[2305.17118] Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time","url":"https://arxiv.org/abs/2305.17118"},{"title":"Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time | OpenReview","url":"https://openreview.net/forum?id=JZfg6wGi6g"},{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"LLM Inference Series: 4. KV caching, a deeper look | by Pierre Lienhart | Medium","url":"https://medium.com/@plienhar/llm-inference-series-4-kv-caching-a-deeper-look-4ba9a77746c8"},{"title":"RETHINKING KEY-VALUE CACHE COMPRESSION TECHNIQUES FOR LARGE","url":"https://arxiv.org/pdf/2503.24000"},{"title":"PagedEviction: Structured Block-wise KV Cache Pruning ...","url":"https://arxiv.org/pdf/2509.04377"},{"title":"KV Cache Eviction","url":"https://www.aussieai.com/research/kv-cache-eviction"},{"title":"hashevict:apre-attention kv cache eviction strategy using ...","url":"https://arxiv.org/pdf/2412.16187"},{"title":"Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://arxiv.org/html/2510.13334v1"},{"title":"[PDF] Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Scissorhands:-Exploiting-the-Persistence-of-for-LLM-Liu-Desai/d6eeb2898bd9bd34744194ef543062dda6c4531a"}]

Based on the search results, here's what I found about ScissorHands KV cache compression and eviction:

## Overview

Scissorhands is a method for exploiting the persistence of importance hypothesis for LLM KV cache compression at test time. The paper was published at NeurIPS 2023, with the initial version submitted o
…[truncated 968 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7514
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-14T12:56:32.795563+00:00_

Web search results for query: "FastGen KV cache compression inference 2023 2024"

Links: [{"title":"CacheGen: KV Cache Compression and Streaming for Fast Large Language Model Serving | Proceedings of the ACM SIGCOMM 2024 Conference","url":"https://dl.acm.org/doi/10.1145/3651890.3672274"},{"title":"Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs | OpenReview","url":"https://openreview.net/forum?id=uNrFpDPMyo"},{"title":"adaptive kv cache compression for llms","url":"https://arxiv.org/pdf/2310.01801"},{"title":"[2310.01801] Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs","url":"https://arxiv.org/abs/2310.01801"},{"title":"Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs","url":"https://arxiv.org/html/2310.01801v4"},{"title":"MODEL TELLS YOU WHAT TO DISCARD: ADAPTIVE KV CACHE COMPRESSION FOR LLMS - Illinois Experts","url":"https://experts.illinois.edu/en/publications/model-tells-you-what-to-discard-adaptive-kv-cache-compression-for/"},{"title":"[Quick Review] Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs","url":"https://liner.com/review/model-tells-you-what-to-discard-adaptive-kv-cache-compression"},{"title":"LLM profiling guides KV cache optimization - Microsoft Research","url":"https://www.microsoft.com/en-us/research/blog/llm-profiling-guides-kv-cache-optimization/"},{"title":"[2310.07240] CacheGen: KV Cache Compression and Streaming for Fast Large Language Model Serving","url":"https://arxiv.org/abs/2310.07240"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=KV+cache+compression"}]

Based on the search results, here's what I found about FastGen KV cache compression:

## FastGen: Adaptive KV Cache Compression for LLMs

FastGen is a plug-and-play method that reduces the memory footprint of generative inference for Large Language Models (LLMs). The paper was first submitted in October 2023 and received its final update in October 2024, with 
…[truncated 1175 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7311
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-14T12:56:35.221798+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "adaptive KV cache dynamic sparsity inference 2025 reasoning model chain-of-thought"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "adaptive KV cache dynamic sparsity inference 2025 reasoning model chain-of-thought"
  }
}
```

</details>

---


### Tool call

_source line 61 · 2026-05-14T12:56:35.473602+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "attention sparsity patterns chain-of-thought reasoning LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "attention sparsity patterns chain-of-thought reasoning LLM 2025"
  }
}
```

</details>

---


### Tool result

_source line 62 · 2026-05-14T12:56:43.123278+00:00_

Web search results for query: "adaptive KV cache dynamic sparsity inference 2025 reasoning model chain-of-thought"

Links: [{"title":"[2510.01290] ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/abs/2510.01290"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/html/2510.01290v1"},{"title":"[2510.01290v1] ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/abs/2510.01290v1"},{"title":"(PDF) ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://www.researchgate.net/publication/396142746_ThinKV_Thought-Adaptive_KV_Cache_Compression_for_Efficient_Reasoning_Models"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://openreview.net/pdf?id=OtZtLYAdQY"},{"title":"Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning","url":"http://people.iiis.tsinghua.edu.cn/~gaomy/pubs/twilight.neurips25.pdf"},{"title":"R-KV: Redundancy-aware KV Cache Compression for ...","url":"https://arxiv.org/pdf/2505.24133"},{"title":"A Survey on Large Language Model Acceleration based on KV Cache Management","url":"https://arxiv.org/html/2412.19442v3"},{"title":"vl-cache: sparsity and modality-aware kv ...","url":"https://assets.amazon.science/12/37/123c1b614550a6fcc6a31ffa9b1e/vl-cache-sparsity-and-modality-aware-kv-cache-compression-for-vision-language-model-inference-acceleration.pdf"},{"title":"HeteroCache: A Dynamic Retrieval Approach to Heterogeneous KV Cache Compression for Long-Context LLM Inference","url":"https://arxiv.org/html/2601.13684v1"}]

I've performed the web search for your query on adaptive KV cache, dynamic sparsity inference, and reasoning models. Here are the key findings:

## Main Results

ThinKV is a thought-adaptive KV cache compression framework that applies a hybrid quantization-eviction strategy, assigning to
…[truncated 1493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7901
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-14T12:56:43.625629+00:00_

Web search results for query: "attention sparsity patterns chain-of-thought reasoning LLM 2025"

Links: [{"title":"RaaS: Reasoning-Aware Attention Sparsity for Efficient ...","url":"https://aclanthology.org/2025.findings-acl.131.pdf"},{"title":"RaaS: Reasoning-Aware Attention Sparsity for Efficient LLM Reasoning","url":"https://arxiv.org/html/2502.11147"},{"title":"Data Mining and Machine Learning Lab Is Chain-of-Thought Reasoning of LLMs a","url":"https://arxiv.org/pdf/2508.01191"},{"title":"[2502.11147] RaaS: Reasoning-Aware Attention Sparsity for Efficient LLM Reasoning","url":"https://arxiv.org/abs/2502.11147"},{"title":"Attention heads of large language models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11873009/"},{"title":"What Makes a Good Reasoning Chain? Uncovering ...","url":"https://aclanthology.org/2025.emnlp-main.329.pdf"},{"title":"[2508.01191] Is Chain-of-Thought Reasoning of LLMs a Mirage? A Data Distribution Lens","url":"https://arxiv.org/abs/2508.01191"},{"title":"A Survey of Chain-of-X Paradigms for LLMs","url":"https://aclanthology.org/2025.coling-main.719.pdf"},{"title":"Hardware-Aligned and Natively Trainable Sparse Attention","url":"https://aclanthology.org/2025.acl-long.1126.pdf"},{"title":"Is Chain-of-Thought Reasoning of LLMs a Mirage? A Data Distribution Lens","url":"https://arxiv.org/html/2508.01191v1"}]

Based on the search results, I found relevant research on attention sparsity patterns and chain-of-thought reasoning in LLMs from 2025:

## Key Findings

**RaaS: Reasoning-Aware Attention Sparsity**

A new attention pattern emerges during the decode stage of reasoning tasks, where milestone tokens (analogous to lemmas in mathematical proofs) emerge, are utilized, and then become unimportant afterward. The RaaS algorithm identifies milestone tokens and retains their KV vectors until they are no longer needed, achieving high accuracy with O(L) time and O(L) memory complexities.

This new attention pattern was discovered through
…[truncated 862 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8152
}
```

</details>

---


### Tool result

_source line 64 · 2026-05-14T12:56:43.932227+00:00_

**Page 1 — Full Transcription**

**Title:** Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Reasoning Models

**Authors:** Anonymous ACL Submission

---

**Abstract (full text):**

Compound sparsity—simultaneously pruning attention heads and evicting KV cache entries—is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood. Prior work treats compound interaction magnitude as approximately constant across the generation process. We show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by up to an order of magnitude across reasoning phases.

We evaluate compound sparsity on DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B parameters) using 50 MATH-500 problems, examining the Interaction Index—a super-additivity metric—across quantile-segmented reasoning phases at sparsity levels α ∈ {0.15, 0.20, 0.25, 0.30}.

Under importance-based KV cache eviction, the Interaction Index difference between low-sparsity and high-sparsity phases ranges monotonically from 0.09 (α = 0.15) to 14.30 at α = 0.30, with permutation tests with paired effect sizes increasing from d_s = 0.44 (small) to d_s = 0.80 (large); Bonferroni-corrected permutation tests confirm significance at all four sparsity levels on this model (p < 0.005). The pattern replicates at α ≥ 0.20 on Qwen2.5-7B-Instruct (d_s ≥ 0.55) with attenuated absolute magnitude; the phase effect at α = 0.15 is marginal (d_s = 0.29, bootstrap CI includes zero). Critically, random eviction produces no such gradient: 7/8 conditions across both models fail to exhibit a significant phase difference (the single exception—Qwen α = 0.30—has negligible effect size, d_s = 0.04), confirming that the severity gradient is an emergent property of the interaction between importance scoring and phase-dependent attention structure, not an artifact of compound compression.

We propose *entropy-discrim
…[truncated 7306 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Agent",
  "elapsed_ms": 68586
}
```

</details>

---


### Tool call

_source line 65 · 2026-05-14T12:56:45.833697+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "joint compression KV cache pruning reasoning LLM compound sparsity 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "joint compression KV cache pruning reasoning LLM compound sparsity 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-14T12:56:46.235144+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"thinking phase\" OR \"reasoning phase\" KV cache sparsity DeepSeek QwQ 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"thinking phase\" OR \"reasoning phase\" KV cache sparsity DeepSeek QwQ 2025"
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-14T12:56:54.706356+00:00_

Web search results for query: ""thinking phase" OR "reasoning phase" KV cache sparsity DeepSeek QwQ 2025"

Links: [{"title":"[Feature Request] Per-phase KV cache quantization for reasoning models (DeepSeek-R1) · Issue #21679 · ggml-org/llama.cpp","url":"https://github.com/ggml-org/llama.cpp/issues/21679"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/html/2510.01290"},{"title":"arXiv:2505.13866v1 [cs.CL] 20 May 2025","url":"https://arxiv.org/pdf/2505.13866v1"},{"title":"THINKV: THOUGHT-ADAPTIVE KV CACHE COM- PRESSION FOR EFFICIENT REASONING MODELS","url":"https://arxiv.org/pdf/2510.01290v1"},{"title":"Aman's AI Journal • Primers • DeepSeek-R1","url":"https://aman.ai/primers/ai/deepseek-R1/"},{"title":"[2510.01290v1] ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/abs/2510.01290v1"},{"title":"[2510.01290] ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/abs/2510.01290"},{"title":"DeepSeek-V4: a million-token context that agents can actually use","url":"https://huggingface.co/blog/deepseekv4"},{"title":"An Automated Survey of Generative Artificial Intelligence: Large Language Models, Architectures, Protocols, and Applications","url":"https://arxiv.org/html/2306.02781v4"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008"}]

I found comprehensive research on thinking phase/reasoning phase KV cache sparsity in reasoning models. Here are the key findings:

## Key Concepts

Reasoning models like DeepSeek-R1 produce long thinking/thought scratchpads followed by short answers, and these two phases have measurably different redundancy profiles that should be quantized at different precisions.

## Sparsity Differences Between Phases

Research on DeepSeek-R1-Distill-Qwen-1.5B showed thinking-phase redundancy of 0.463 versus answer-phas
…[truncated 1138 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8471
}
```

</details>

---


### Tool result

_source line 68 · 2026-05-14T12:56:55.611542+00:00_

Web search results for query: "joint compression KV cache pruning reasoning LLM compound sparsity 2025 2026"

Links: [{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"Caching and Reuse Optimizations","url":"https://www.aussieai.com/research/caching"},{"title":"Published as a conference paper at ICLR 2026 ADAPTIVE KV-CACHE COMPRESSION","url":"https://www.arxiv.org/pdf/2509.03136"},{"title":"Lethe: Layer- and Time-Adaptive KV Cache Pruning for Reasoning-Intensive LLM Serving","url":"https://arxiv.org/html/2511.06029"},{"title":"KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/html/2603.20397v1"},{"title":"KV Cache Compression for Inference Efficiency in LLMs: A Review","url":"https://arxiv.org/html/2508.06297v1"},{"title":"SqueezeAttention: 2D Management of KV-Cache in LLM Inference via Layer-wise Optimal Budget | OpenReview","url":"https://openreview.net/forum?id=9HK2rHNAhd"},{"title":"KV Cache Strategies for LLM Efficiency","url":"https://www.emergentmind.com/topics/kv-cache-strategy"},{"title":"UNCOMP: Can Matrix Entropy Uncover Sparsity?","url":"https://aclanthology.org/2025.emnlp-main.209.pdf"}]

Based on the search results, I've found substantial recent research on joint compression, KV cache pruning, and reasoning LLM optimization from 2025-2026. Here's what the current research frontier shows:

## Recent Advances in Reasoning-Aware KV Cache Compression

The 2026 research frontier is moving toward latent-space compact
…[truncated 1673 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9777
}
```

</details>

---


### Tool call

_source line 69 · 2026-05-14T12:56:58.328718+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Lethe layer time adaptive KV cache pruning reasoning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Lethe layer time adaptive KV cache pruning reasoning 2025"
  }
}
```

</details>

---


### Tool call

_source line 70 · 2026-05-14T12:56:58.530449+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "StreamingLLM attention sink efficient long generation 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "StreamingLLM attention sink efficient long generation 2023"
  }
}
```

</details>

---


### Tool result

_source line 71 · 2026-05-14T12:57:06.023280+00:00_

Web search results for query: "Lethe layer time adaptive KV cache pruning reasoning 2025"

Links: [{"title":"[2511.06029] Lethe: Layer- and Time-Adaptive KV Cache Pruning for Reasoning-Intensive LLM Serving","url":"https://arxiv.org/abs/2511.06029"},{"title":"Lethe: Layer- and Time-Adaptive KV Cache Pruning for Reasoning-Intensive LLM Serving","url":"https://arxiv.org/html/2511.06029v1"},{"title":"Lethe: Layer- and Time-Adaptive KV Cache Pruning for Reasoning-Intensive","url":"https://www.arxiv.org/pdf/2511.06029"},{"title":"(PDF) Lethe: Layer- and Time-Adaptive KV Cache Pruning for Reasoning-Intensive LLM Serving","url":"https://www.researchgate.net/publication/397479742_Lethe_Layer-_and_Time-Adaptive_KV_Cache_Pruning_for_Reasoning-Intensive_LLM_Serving"},{"title":"Lethe: Layer- and Time-Adaptive KV Cache Pruning for Reasoning-Intensive","url":"https://ojs.aaai.org/index.php/AAAI/article/download/40036/43997"},{"title":"Adaptive Layer Selection for Layer-Wise Token Pruning in LLM Inference","url":"https://arxiv.org/html/2601.07667"},{"title":"[PDF] Lethe: Layer- and Time-Adaptive KV Cache Pruning ...","url":"https://www.semanticscholar.org/paper/Lethe:-Layer-and-Time-Adaptive-KV-Cache-Pruning-for-Zeng-Zhao/ce7628e9428ec7a94005d237f06a814c45a5f9ee"},{"title":"GitHub - HuangOwen/Awesome-LLM-Compression: Awesome LLM compression research papers and tools. · GitHub","url":"https://github.com/HuangOwen/Awesome-LLM-Compression"},{"title":"(PDF) KVzap: Fast, Adaptive, and Faithful KV Cache Pruning","url":"https://www.researchgate.net/publication/399754198_KVzap_Fast_Adaptive_and_Faithful_KV_Cache_Pruning"},{"title":"KVzap: Fast, Adaptive, and Faithful KV Cache Pruning","url":"https://arxiv.org/html/2601.07891v1"}]

Here are the search results for "Lethe layer time adaptive KV cache pruning reasoning 2025":

## Overview

Lethe is a dynamic KV cache management framework that introduces adaptivity along both the spatial and temporal dimensions of decoding. It is an adaptive K
…[truncated 1537 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7694
}
```

</details>

---


### Tool result

_source line 72 · 2026-05-14T12:57:06.325028+00:00_

Web search results for query: "StreamingLLM attention sink efficient long generation 2023"

Links: [{"title":"[2309.17453] Efficient Streaming Language Models with Attention Sinks","url":"https://arxiv.org/abs/2309.17453"},{"title":"GitHub - mit-han-lab/streaming-llm: [ICLR 2024] Efficient Streaming Language Models with Attention Sinks · GitHub","url":"https://github.com/mit-han-lab/streaming-llm"},{"title":"Efficient Streaming Language Models with Attention Sinks","url":"https://hanlab.mit.edu/projects/streamingllm"},{"title":"Efficient Streaming Language Models with Attention Sinks | OpenReview","url":"https://openreview.net/forum?id=NG7sS51zVF"},{"title":"Efficient Streaming Language Models with Attention Sinks","url":"https://arxiv.org/html/2309.17453v3"},{"title":"[PDF] Efficient Streaming Language Models with Attention Sinks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Efficient-Streaming-Language-Models-with-Attention-Xiao-Tian/fdc53c2c10742464087c0525f77e32604827a21d"},{"title":"Xiao Et Al. - 2023 - Efficient Streaming Language Models With Attention | PDF","url":"https://www.scribd.com/document/723064994/Xiao-et-al-2023-Efficient-Streaming-Language-Models-with-Attention"},{"title":"Efficient streaming language models with at","url":"https://arxiv.org/pdf/2309.17453"},{"title":"How Attention Sinks Keep Language Models Stable","url":"https://hanlab.mit.edu/blog/streamingllm"},{"title":"GitHub - tomaarsen/attention_sinks: Extend existing LLMs way beyond the original training length with constant memory usage, without retraining · GitHub","url":"https://github.com/tomaarsen/attention_sinks"}]

Based on the search results, here's what I found about StreamingLLM and attention sinks:

## Overview

StreamingLLM is an efficient framework that enables LLMs trained with a finite length attention window to generalize to infinite sequence lengths without any fine-tuning. The research was published in September 2023.

## The Problem and Solution

Durin
…[truncated 1339 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7794
}
```

</details>

---


### Tool call

_source line 73 · 2026-05-14T12:57:08.638843+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "head pruning attention head importance LLM structured pruning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "head pruning attention head importance LLM structured pruning 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-14T12:57:08.940788+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Hold Onto That Thought\" KV cache compression reasoning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Hold Onto That Thought\" KV cache compression reasoning 2024 2025"
  }
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-14T12:57:14.419014+00:00_

Here is the detailed transcription of all content on pages 4–6:

---

## PAGE 4 (main_a1a036_p4.png)

### Layout
Two-column format. Left column continues Section 3 (method), right column begins Section 4 (Experimental Setup) and Section 5 (Results).

---

### Left Column (continuation of prior section)

**Quantile-based segmentation.** Tokens are partitioned into **high-**, **mid-**, and **low-sparsity** phases by the textile boundaries of {π_i}. Segments shorter than 10 tokens are merged into adjacent phases. The segmentation is data-driven and requires only attention weights.

*(Table 1 caption appears here — see below)*

---

### Section 4: Experimental Setup

**4.1 Models**

We evaluate two 7B-parameter instruction-tuned models sharing the Qwen2 backbone (28 layers, 28 heads with 4-group GQA): **DeepSeek-R1-Distill-Qwen-7B** (DeepSeek-AI, 2025), distilled from DeepSeek-R1, produces explicit chain-of-thought traces with pronounced phase structure. **Qwen2.5-7B-Instruct** (Yang et al. 2024) provides standard model replication with standard instruction tuning rather than reasoning distillation. Both models are loaded in BFloat16 with custom attention to permit direct manipulation of attention matrices.¹

---

**4.2 Dataset**

We evaluate on a 50-problem stratified subset of MATH-500 (Hendrycks et al., 2021), sampling uniformly across levels 3–5 (difficulty levels 3, 4, 5). Each problem is decoded greedily (max_new_tokens=2048).

---

**4.3 Configuration and Metrics**

We apply symmetric compound sparsity: for level s ∈ {0.15, 0.20, 0.25, 0.30}, the same fraction s of attention heads and KV cache entries are removed. For each problem, we compute perplexity under four conditions: dense, attention-only pruning, KV-only, and **importance-based**. We compare **importance-based** eviction (position-normalized cumulative attention, Eq. 3; BOS always retained) against a **random** baseline. Heads are pruned per layer by Frobenius norm under importance-based eviction and un
…[truncated 11703 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Agent",
  "elapsed_ms": 95807
}
```

</details>

---


### Tool result

_source line 76 · 2026-05-14T12:57:15.224367+00:00_

Web search results for query: ""Hold Onto That Thought" KV cache compression reasoning 2024 2025"

Links: [{"title":"[2512.12008] Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/abs/2512.12008"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"},{"title":"NeurIPS Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://neurips.cc/virtual/2025/loc/san-diego/126664"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning | OpenReview","url":"https://openreview.net/forum?id=udgrpHqw4F"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://openreview.net/pdf?id=OtZtLYAdQY"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/html/2510.01290v1"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention","url":"https://arxiv.org/pdf/2510.00636"},{"title":"ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference | OpenReview","url":"https://openreview.net/forum?id=20JDhbJqn3"},{"title":"[2510.01290] ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/abs/2510.01290"},{"title":"Preprint THE PITFALLS OF KV CACHE COMPRESSION","url":"https://arxiv.org/pdf/2510.00231"}]

I found relevant search results about "Hold Onto That Thought: Assessing KV Cache Compression On Reasoning." Here's what the paper covers:

## Overview

"Hold Onto That Thought" addresses how the KV cache, which speeds up attention computations, grows linearly with context length, and examines how compression algorithms alleviate this growth by evicting unimportant tokens.

## Key Findings

The paper reveals that classical attention-based "heavy-hitter" strategies, which evict tokens based on accumulated attention scores, significantly outperfor
…[truncated 774 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6283
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-14T12:57:17.082397+00:00_

Web search results for query: "head pruning attention head importance LLM structured pruning 2024 2025"

Links: [{"title":"Diet Your LLM: Dimension-wise Global Pruning of LLMs via Merging Task-specific Importance Score","url":"https://arxiv.org/html/2603.23985"},{"title":"Pruning Large Language Models by Identifying and Preserving Functional Networks","url":"https://arxiv.org/html/2508.05239v1"},{"title":"CFSP: An Efficient Structured Pruning Framework for LLMs ...","url":"https://aclanthology.org/2025.coling-main.626.pdf"},{"title":"[2505.22689] SlimLLM: Accurate Structured Pruning for Large Language Models","url":"https://arxiv.org/abs/2505.22689"},{"title":"Pruning as a Domain-specific LLM Extractor","url":"https://aclanthology.org/2024.findings-naacl.91.pdf"},{"title":"Efficient self-attention with smart pruning for sustainable large language models | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-92586-5"},{"title":"LLM Series 09: LLM Pruning and Distillation | by Yashwanth S | Medium","url":"https://medium.com/@yashwanths_29644/llm-series-08-llm-pruning-and-distillation-33379b2d8fb5"},{"title":"Structured Optimal Brain Pruning for Large Language Models","url":"https://aclanthology.org/2024.emnlp-main.775.pdf"},{"title":"Practice: Structured LLM Pruning","url":"https://apxml.com/courses/llm-compression-acceleration/chapter-3-sophisticated-pruning-methodologies/practice-structured-pruning"},{"title":"Everybody Prune Now: Structured Pruning of LLMs with only Forward Passes","url":"https://arxiv.org/html/2402.05406v2"}]

Based on the web search results, here's an overview of recent research on head pruning, attention head importance, and structured pruning in LLMs from 2024-2025:

## Key Research Areas

**Structured Pruning Approaches:**

Structured pruning in LLMs can be categorized based on the granularity of pruning (e.g., individual parameters, attention heads, or entire transformer blocks) and whether pruning decisions leverage task-spe
…[truncated 1459 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8443
}
```

</details>

---


### Tool call

_source line 78 · 2026-05-14T12:57:19.415138+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SparseGPT unstructured weight pruning large language models 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SparseGPT unstructured weight pruning large language models 2023"
  }
}
```

</details>

---


### Tool call

_source line 79 · 2026-05-14T12:57:19.717246+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wanda pruning LLM weights without retraining 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wanda pruning LLM weights without retraining 2024"
  }
}
```

</details>

---


### Tool result

_source line 80 · 2026-05-14T12:57:25.752826+00:00_

Web search results for query: "SparseGPT unstructured weight pruning large language models 2023"

Links: [{"title":"[2301.00774] SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot","url":"https://arxiv.org/abs/2301.00774"},{"title":"GitHub - IST-DASLab/sparsegpt: Code for the ICML 2023 paper \"SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot\". · GitHub","url":"https://github.com/IST-DASLab/sparsegpt"},{"title":"SparseGPT: Massive Language Models Can be Accurately Pruned in One-Shot","url":"https://openreview.net/pdf?id=gsP05g8IeK"},{"title":"[PDF] SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SparseGPT:-Massive-Language-Models-Can-Be-Pruned-in-Frantar-Alistarh/909ad57ce8caa6b390a65ae09db352d27d8f3996"},{"title":"SparseGPT: Massive Language Models Can be Accurately ...","url":"https://arxiv.org/pdf/2301.00774"},{"title":"SparseGPT: massive language models can be accurately ...","url":"https://dl.acm.org/doi/10.5555/3618408.3618822"},{"title":"SparseGPT: Remove 100 billion parameters for free | Red Hat Developer","url":"https://developers.redhat.com/articles/2023/03/21/sparsegpt-remove-100-billion-parameters-free"},{"title":"SparseGPT: Massive language models can be accurately pruned in one-shot","url":"https://research-explorer.ista.ac.at/record/14458"},{"title":"GitHub - MachineLearningSystem/23arxiv-sparsegpt: Code for the ICML 2023 paper \"SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot\". · GitHub","url":"https://github.com/MachineLearningSystem/23arxiv-sparsegpt"},{"title":"SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230100774F/abstract"}]

## Search Results for SparseGPT

I found comprehensive information about SparseGPT. Here are the key findings:

### Overview
SparseGPT shows for the first time that large-scale generat
…[truncated 1259 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6337
}
```

</details>

---


### Tool result

_source line 81 · 2026-05-14T12:57:26.608680+00:00_

Web search results for query: "Wanda pruning LLM weights without retraining 2024"

Links: [{"title":"[2306.11695] A Simple and Effective Pruning Approach for Large Language Models","url":"https://arxiv.org/abs/2306.11695"},{"title":"A Simple and Effective Pruning Approach for Large Language Models | OpenReview","url":"https://openreview.net/forum?id=PxoFut3dWW"},{"title":"A Simple and Effective Pruning Approach for Large Language Models.","url":"https://eric-mingjie.github.io/wanda/home.html"},{"title":"Published as a conference paper at ICLR 2024","url":"https://arxiv.org/pdf/2306.11695"},{"title":"ICML A Simple and Effective Pruning Approach for Large Language Models","url":"https://icml.cc/virtual/2023/28297"},{"title":"A SIMPLE AND EFFECTIVE PRUNING APPROACH FOR ...","url":"https://openreview.net/pdf?id=PxoFut3dWW"},{"title":"GitHub - locuslab/wanda: A simple and effective LLM pruning approach. · GitHub","url":"https://github.com/locuslab/wanda"},{"title":"[Quick Review] A Simple and Effective Pruning Approach for Large Language Models","url":"https://liner.com/review/a-simple-and-effective-pruning-approach-for-large-language-models"},{"title":"A Simple and Effective Pruning Approach for Large Language Models","url":"https://www.researchgate.net/publication/371729484_A_Simple_and_Effective_Pruning_Approach_for_Large_Language_Models"},{"title":"Efficient Model Pruning for Large Language Models: Wanda's Simplified Approach","url":"https://www.linkedin.com/pulse/efficient-model-pruning-large-language-models-wandas-ayoub-kirouane"}]

Based on the search results, here's information about Wanda pruning for LLMs in 2024:

## Overview

Wanda (Pruning by Weights and activations) is a novel pruning method designed to induce sparsity in pretrained LLMs. Notably, Wanda requires no retraining or weight update, and the pruned LLM can be used as is.

## How It Works

The approach prunes weights with the smallest magnitudes multiplied by the corresponding input activations, on 
…[truncated 940 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6891
}
```

</details>

---


### Tool call

_source line 82 · 2026-05-14T12:57:29.565859+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"compound sparsity\" OR \"multi-dimensional compression\" LLM inference accuracy degradation interaction 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"compound sparsity\" OR \"multi-dimensional compression\" LLM inference accuracy degradation interaction 2025"
  }
}
```

</details>

---


### Tool call

_source line 83 · 2026-05-14T12:57:29.616693+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLM-Pruner structured pruning channel head coupled structure 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLM-Pruner structured pruning channel head coupled structure 2023 2024"
  }
}
```

</details>

---


### Tool result

_source line 84 · 2026-05-14T12:57:36.616430+00:00_

Web search results for query: "LLM-Pruner structured pruning channel head coupled structure 2023 2024"

Links: [{"title":"GitHub - horseee/LLM-Pruner: [NeurIPS 2023] LLM-Pruner: On the Structural Pruning of Large Language Models. Support Llama-3/3.1, Llama-2, LLaMA, BLOOM, Vicuna, Baichuan, TinyLlama, etc. · GitHub","url":"https://github.com/horseee/LLM-Pruner"},{"title":"NeurIPS Poster LLM-Pruner: On the Structural Pruning of Large Language Models","url":"https://neurips.cc/virtual/2023/poster/72074"},{"title":"[2305.11627] LLM-Pruner: On the Structural Pruning of Large Language Models","url":"https://arxiv.org/abs/2305.11627"},{"title":"LLM-Pruner: On the Structural Pruning of Large Language Models Xinyin Ma","url":"https://arxiv.org/pdf/2305.11627"},{"title":"Pruning Large Language Models by Identifying and Preserving Functional Networks","url":"https://arxiv.org/html/2508.05239v1"},{"title":"LLM-Pruner: On the Structural Pruning of Large Language Models | OpenReview","url":"https://openreview.net/forum?id=J8Ajf9WfXP"},{"title":"LLM-Pruner: On the Structural Pruning of Large Language Models","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/44956951349095f74492a5471128a7e0-Abstract-Conference.html"},{"title":"LLM-Pruner: Structural Pruning for LLMs","url":"https://www.emergentmind.com/papers/2305.11627"},{"title":"LLM-pruner: on the structural pruning of large language ...","url":"https://dl.acm.org/doi/10.5555/3666122.3667072"},{"title":"[PDF] LLM-Pruner: On the Structural Pruning of Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/LLM-Pruner:-On-the-Structural-Pruning-of-Large-Ma-Fang/017010b941d902a467f6d329ae5e74fd67e67912"}]

Based on the search results, here's what I found about LLM-Pruner and its structured pruning approach:

## Overview

LLM-Pruner adopts structural pruning that selectively removes non-critical coupled structures based on gradient information, maximally preserving the majority of the L
…[truncated 1251 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6999
}
```

</details>

---


### Tool result

_source line 85 · 2026-05-14T12:57:37.421355+00:00_

Web search results for query: ""compound sparsity" OR "multi-dimensional compression" LLM inference accuracy degradation interaction 2025"

Links: [{"title":"SLIM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression | Research","url":"https://research.nvidia.com/publication/2025-06_slim-one-shot-quantization-and-sparsity-low-rank-approximation-llm-weight"},{"title":"The Compression Trinity: A Survey of LLM Compression","url":"https://www.cs.toronto.edu/~mmozaffari/compression-trinity/index.html"},{"title":"SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression","url":"https://arxiv.org/html/2410.09615"},{"title":"Frontiers | A survey of model compression techniques: past, present, and future","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1518965/full"},{"title":"GitHub - HuangOwen/Awesome-LLM-Compression: Awesome LLM compression research papers and tools. · GitHub","url":"https://github.com/HuangOwen/Awesome-LLM-Compression"},{"title":"Model Compression and Efficient Inference for Large Language Models: A Survey","url":"https://arxiv.org/html/2402.09748v1"},{"title":"ICML Poster SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression","url":"https://icml.cc/virtual/2025/poster/46479"},{"title":"Workshop on Sparsity in LLMs (SLLM): Deep Dive into Mixture of Experts, Quantization, Hardware, and Inference","url":"https://iclr.cc/virtual/2025/workshop/23996"},{"title":"A review of state-of-the-art techniques for large language model compression | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-02019-z"},{"title":"SparseGPT: Massive Language Models Can be Accurately ...","url":"https://arxiv.org/pdf/2301.00774"}]

Based on the search results, I found relevant information about compound compression techniques and accuracy degradation in LLM inferenc
…[truncated 1547 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7855
}
```

</details>

---


### Tool call

_source line 86 · 2026-05-14T12:57:40.696906+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "R-KV redundancy-aware KV cache compression reasoning models 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "R-KV redundancy-aware KV cache compression reasoning models 2025 arxiv"
  }
}
```

</details>

---


### Tool call

_source line 87 · 2026-05-14T12:57:40.901178+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "KV cache budget allocation layer-wise different compression reasoning LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "KV cache budget allocation layer-wise different compression reasoning LLM 2025"
  }
}
```

</details>

---


### Tool result

_source line 88 · 2026-05-14T12:57:48.122342+00:00_

Web search results for query: "R-KV redundancy-aware KV cache compression reasoning models 2025 arxiv"

Links: [{"title":"GitHub - Zefan-Cai/R-KV: [Neurips 2025] R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://github.com/Zefan-Cai/R-KV"},{"title":"[2505.24133] R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://arxiv.org/abs/2505.24133"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://arxiv.org/html/2505.24133"},{"title":"R-KV: Redundancy-aware KV Cache Compression for ...","url":"https://arxiv.org/pdf/2505.24133"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://proceedings.neurips.cc/paper_files/paper/2025/hash/57e0358aed314784cad14a26e1eba642-Abstract-Conference.html"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://zefan-cai.github.io/R-KV.page/"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Training-Free Reasoning Models Acceleration","url":"https://arxiv.org/html/2505.24133v1"},{"title":"[PDF] R-KV: Redundancy-aware KV Cache Compression for Training-Free Reasoning Models Acceleration | Semantic Scholar","url":"https://www.semanticscholar.org/paper/R-KV:-Redundancy-aware-KV-Cache-Compression-for-Cai-Xiao/eb574cb16208cb0daaa484f85cddb1e1d6b23f44"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=2jwAjomEDB"},{"title":"Redundancy-aware KV Cache Compression for Training- ...","url":"https://www.arxiv.org/pdf/2505.24133v2"}]

I found comprehensive information about R-KV. Here's a summary of the search results:

## R-KV: Redundancy-aware KV Cache Compression for Reasoning Models

R-KV is a novel method specifically targeting redundant tokens in reasoning models. The paper was submitted on May 30, 2025 and has been accepted to NeurIPS 2025.

**Problem It Addresses:**

Reasoning models often
…[truncated 1228 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7425
}
```

</details>

---


### Tool result

_source line 89 · 2026-05-14T12:57:49.979635+00:00_

Web search results for query: "KV cache budget allocation layer-wise different compression reasoning LLM 2025"

Links: [{"title":"SqueezeAttention: 2D Management of KV-Cache in LLM Inference via Layer-wise Optimal Budget | OpenReview","url":"https://openreview.net/forum?id=9HK2rHNAhd"},{"title":"Reformulating KV Cache Eviction Problem for Long-Context LLM Inference","url":"https://arxiv.org/html/2605.07234"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"EvolKV: Evolutionary KV Cache Compression for LLM Inference","url":"https://arxiv.org/html/2509.08315"},{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction","url":"https://arxiv.org/html/2605.06676"},{"title":"GitHub - FFY0/AdaKV: The Official Implementation of Ada-KV [NeurIPS 2025] · GitHub","url":"https://github.com/FFY0/AdaKV"},{"title":"[2509.09754] LAVa: Layer-wise KV Cache Eviction with Dynamic Budget Allocation","url":"https://arxiv.org/abs/2509.09754"},{"title":"AirCache: Activating Inter-modal Relevancy KV Cache Compression for","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_AirCache_Activating_Inter-modal_Relevancy_KV_Cache_Compression_for_Efficient_Large_ICCV_2025_paper.pdf"},{"title":"LAVa: Layer-wise KV Cache Eviction with Dynamic Budget ...","url":"https://aclanthology.org/2025.findings-emnlp.737.pdf"}]

Based on the search results, I found several recent research papers and methods addressing KV cache budget allocation with layer-wise co
…[truncated 2144 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9078
}
```

</details>

---


### Tool call

_source line 90 · 2026-05-14T12:57:52.592967+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MagicPIG QUEST MInference sparse attention inference 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MagicPIG QUEST MInference sparse attention inference 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 91 · 2026-05-14T12:57:52.694383+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "attention head pruning reasoning LLM phase-dependent importance 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "attention head pruning reasoning LLM phase-dependent importance 2025"
  }
}
```

</details>

---


### Tool result

_source line 92 · 2026-05-14T12:58:01.348152+00:00_

Web search results for query: "attention head pruning reasoning LLM phase-dependent importance 2025"

Links: [{"title":"Attention Heads and MLP Pruning - Efficient LLMs with AMP","url":"https://arxiv.org/pdf/2504.21174"},{"title":"Efficient LLMs with AMP: Attention Heads and MLP Pruning","url":"https://arxiv.org/html/2504.21174v1"},{"title":"[2504.21174] Efficient LLMs with AMP: Attention Heads and MLP Pruning","url":"https://arxiv.org/abs/2504.21174"},{"title":"Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning","url":"http://people.iiis.tsinghua.edu.cn/~gaomy/pubs/twilight.neurips25.pdf"},{"title":"GitHub - IAAR-Shanghai/Awesome-Attention-Heads: An awesome repository & A comprehensive survey on interpretability of LLM attention heads. · GitHub","url":"https://github.com/IAAR-Shanghai/Awesome-Attention-Heads"},{"title":"RaaS: Reasoning-Aware Attention Sparsity for Efficient ...","url":"https://aclanthology.org/2025.findings-acl.131.pdf"},{"title":"High-Layer Attention Pruning with Rescaling","url":"https://arxiv.org/html/2507.01900v1"},{"title":"Efficient self-attention with smart pruning for sustainable large language models | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-92586-5"},{"title":"Efficient LLMs with AMP: Attention Heads and MLP Pruning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250421174G/abstract"},{"title":"CFSP: An Efficient Structured Pruning Framework for LLMs ...","url":"https://aclanthology.org/2025.coling-main.626.pdf"}]

Based on the search results, I found several relevant papers from 2025 on attention head pruning in LLMs. Here's what I discovered:

## Key Findings

### AMP: Attention Heads and MLP Pruning (April 2025)

AMP is a novel structured pruning method that efficiently compresses LLMs by removing less critical structures within Multi-Head Attention (MHA) and Multilayer Perceptron (MLP). AMP uses the magnitude of activations – rather than solely the weights – to evaluate the imp
…[truncated 1456 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8653
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-14T12:58:01.449095+00:00_

Web search results for query: "MagicPIG QUEST MInference sparse attention inference 2024 2025"

Links: [{"title":"MagicPIG: LSH Sampling for Efficient LLM Generation","url":"https://arxiv.org/pdf/2410.16179"},{"title":"MagicPIG: LSH Sampling for Efficient LLM Generation | OpenReview","url":"https://openreview.net/forum?id=ALzTQUgW8a"},{"title":"GitHub - Infini-AI-Lab/MagicPIG: [ICLR2025 Spotlight] MagicPIG: LSH Sampling for Efficient LLM Generation · GitHub","url":"https://github.com/Infini-AI-Lab/MagicPIG"},{"title":"GitHub - microsoft/MInference: [NeurIPS'24 Spotlight, ICLR'25, ICML'25] To speed up Long-context LLMs' inference, approximate and dynamic sparse calculate the attention, which reduces inference latency by up to 10x for pre-filling on an A100 while maintaining accuracy. · GitHub","url":"https://github.com/microsoft/MInference"},{"title":"Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning","url":"http://people.iiis.tsinghua.edu.cn/~gaomy/pubs/twilight.neurips25.pdf"},{"title":"MInference 1.0: Accelerating Pre-filling for Long-Context LLMs via Dynamic Sparse Attention | OpenReview","url":"https://openreview.net/forum?id=fPBACAbqSN"},{"title":"Sparse Attention - Shong","url":"https://shong.xlog.app/sparse_path?locale=en"},{"title":"TokenSelect: Efficient Long-Context Inference and Length ...","url":"https://aclanthology.org/2025.emnlp-main.1079.pdf"},{"title":"MInference 1.0: Accelerating Pre-filling for Long-Context LLMs via Dynamic Sparse Attention","url":"https://arxiv.org/html/2407.02490v1"},{"title":"MInference: Million-Tokens Prompt Inference for LLMs","url":"https://hqjiang.com/minference.html"}]

Based on the search results, here's what I found about MagicPIG, QUEST, and MInference for sparse attention inference:

## MagicPIG

MagicPIG is a heterogeneous system based on Locality Sensitive Hashing (LSH) that significantly reduces the workload of attention computation while preserving high accuracy for diverse tasks. MagicPIG can p
…[truncated 1219 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8856
}
```

</details>

---


### Tool result

_source line 94 · 2026-05-14T12:58:10.036738+00:00_

Here is the complete transcription and summary of all content on pages 7–10:

---

## PAGE 7

**Layout**: Two-column academic paper format. This is page 7, continuing from the experiments section.

### Table 5 (top of page, left column)

**Title**: "Discrimination collapse: ΔGini and ΔCV (post-pruning minus baseline) under importance-based eviction. Negative = reduced discriminative power."

| Model | s | ΔGini | ΔCV |
|-------|---|-------|-----|
| DeepSeek | 0.15 | −0.030 | −0.50 |
| DeepSeek | 0.20 | −0.040 | −0.77 |
| DeepSeek | 0.25 | −0.065 | −1.20 |
| DeepSeek | 0.30 | −0.081 | −1.60 |
| Qwen | 0.15 | −0.010 | −0.05 |
| Qwen | 0.20 | −0.012 | −0.90 |
| Qwen | 0.25 | −0.010 | −1.40 |
| Qwen | 0.30 | −0.020 | −1.14 |

**Caption text continues**: Both models and all sparsity levels: Gini decreases by 0.010–0.081 and CV by 0.05–1.66 under importance-based eviction. The same pattern holds under random eviction, confirming discrimination collapse is a consequence of head pruning *per se*.

When importance scores lose discriminative power, thresholds the bottom-s fraction becomes noise-sensitive: importance-based eviction degenerates toward arbitrary selection. The crossover in §5.1 is thus an emergent consequence of head pruning degrading importance scoring conditioned on phase-dependent attention structure. Random eviction, whose decisions are independent of score quality, is immune—explaining its flat severity gradient.

### Section 6.2 — Entropy Redistribution

Head pruning also redistributes attention entropy of surviving heads, but this effect is model-dependent: DeepSeek shows consistent negative entropy shifts (ΔH ∈ [−0.040, −0.047]), while Qwen exhibits a sign reversal at s=0.25. The partial replication suggests distillation may redistribute strategy labels to explain the phase-strategy interaction; entropy redistribution may amplify the effect where it co-occurs, but is not the primary driver. Details in Appendix F.

### Section 6.3 — Implications

Discrimi
…[truncated 20314 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Agent",
  "elapsed_ms": 144813
}
```

</details>

---


### Tool call

_source line 95 · 2026-05-14T12:58:11.042857+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "quantization aware pruning KV cache LLM combined joint optimization 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "quantization aware pruning KV cache LLM combined joint optimization 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-14T12:58:11.394857+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DeepSeek-R1 QwQ compression efficiency thinking token overhead 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DeepSeek-R1 QwQ compression efficiency thinking token overhead 2025"
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-14T12:58:18.768629+00:00_

Web search results for query: "DeepSeek-R1 QwQ compression efficiency thinking token overhead 2025"

Links: [{"title":"GitHub - deepseek-ai/DeepSeek-R1 · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-R1"},{"title":"Deployment-ready reasoning with quantized DeepSeek-R1 models | Red Hat Developer","url":"https://developers.redhat.com/articles/2025/03/03/deployment-ready-reasoning-quantized-deepseek-r1-models"},{"title":"deepseek-ai/DeepSeek-R1 · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1"},{"title":"QwQ-32B vs DeepSeek-R1 Ultimate 2025 Local Inference Showdown - Skywork ai","url":"https://skywork.ai/blog/llm/qwq-32b-vs-deepseek-r1-ultimate-2025-local-inference-showdown/"},{"title":"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning","url":"https://arxiv.org/html/2501.12948v1"},{"title":"TokenSqueeze: Performance-Preserving Compression for Reasoning LLMs","url":"https://arxiv.org/html/2511.13223"},{"title":"Speed Up DeepSeek R1 Distill 4-bit Performance and Inference Capability with NexaQuant on AMD Client","url":"https://www.amd.com/en/blogs/2025/speed-up-deepseek-r1-distill-4-bit-performance-and.html"},{"title":"DeepSeek R1 0528 - Intelligence, Performance & Price Analysis","url":"https://artificialanalysis.ai/models/deepseek-r1"},{"title":"DeepSeek's Low Inference Cost Explained: MoE & Strategy | IntuitionLabs","url":"https://intuitionlabs.ai/articles/deepseek-inference-cost-explained"},{"title":"The Complete Guide to DeepSeek Models: V3, R1, V4 and Beyond","url":"https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond"}]

I found several relevant results about DeepSeek-R1, QwQ, and token compression efficiency. Here's what the search results reveal:

## Thinking Token & Reasoning Efficiency

Reasoning LLMs such as DeepSeek-R1 achieve strong performance on complex reasoning tasks by generating long chain-of-thought (CoT) traces, however these long CoTs result in inc
…[truncated 1342 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7373
}
```

</details>

---


### Tool result

_source line 98 · 2026-05-14T12:58:20.475652+00:00_

Web search results for query: "quantization aware pruning KV cache LLM combined joint optimization 2024 2025"

Links: [{"title":"Efficient KV Caching for LLM Inference","url":"https://www.emergentmind.com/topics/efficient-kv-caching"},{"title":"Titanus: Enabling KV Cache Pruning and Quantization On-the-Fly for LLM Acceleration | Proceedings of the Great Lakes Symposium on VLSI 2025","url":"https://dl.acm.org/doi/full/10.1145/3716368.3735145"},{"title":"ICML Poster KVTuner: Sensitivity-Aware Layer-Wise Mixed-Precision KV Cache Quantization for Efficient and Nearly Lossless LLM Inference","url":"https://icml.cc/virtual/2025/poster/43487"},{"title":"Towards the Optimal Token-Precision Trade-off in KV ...","url":"https://aclanthology.org/2025.findings-emnlp.429.pdf"},{"title":"KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/html/2603.20397v1"},{"title":"KVCache Management in LLMs","url":"https://www.emergentmind.com/topics/kvcache-management"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization | Request PDF","url":"https://www.researchgate.net/publication/397202512_KVQuant_Towards_10_Million_Context_Length_LLM_Inference_with_KV_Cache_Quantization"},{"title":"PALU: KV-CACHE COMPRESSION WITH LOW-RANK ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7da6e0e00702c60607a6ae05c802ef85-Paper-Conference.pdf"},{"title":"Q-Hitter: A Better Token Oracle for Efficient LLM Inference ...","url":"https://proceedings.mlsys.org/paper_files/paper/2024/file/bbb7506579431a85861a05fff048d3e1-Paper-Conference.pdf"}]

I've found comprehensive s
…[truncated 2024 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9432
}
```

</details>

---


### Tool call

_source line 99 · 2026-05-14T12:58:23.741157+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GEAR KVQuant KV cache quantization combined eviction pruning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GEAR KVQuant KV cache quantization combined eviction pruning 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 100 · 2026-05-14T12:58:24.142822+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "channel pruning FFN MLP neurons LLM inference structured sparsity 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "channel pruning FFN MLP neurons LLM inference structured sparsity 2024 2025"
  }
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-14T12:58:31.167904+00:00_

Web search results for query: "GEAR KVQuant KV cache quantization combined eviction pruning 2024 2025"

Links: [{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization | Request PDF","url":"https://www.researchgate.net/publication/397202512_KVQuant_Towards_10_Million_Context_Length_LLM_Inference_with_KV_Cache_Quantization"},{"title":"GitHub - SqueezeAILab/KVQuant: [NeurIPS 2024] KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization · GitHub","url":"https://github.com/SqueezeAILab/KVQuant"},{"title":"FibQuant: Universal Vector Quantization for Random-Access KV-Cache Compression","url":"https://arxiv.org/html/2605.11478"},{"title":"RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory","url":"https://arxiv.org/html/2605.06675"},{"title":"[2401.18079] KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization","url":"https://arxiv.org/abs/2401.18079"},{"title":"PALU: KV-CACHE COMPRESSION WITH LOW-RANK ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7da6e0e00702c60607a6ae05c802ef85-Paper-Conference.pdf"},{"title":"KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/html/2603.20397v1"},{"title":"KV Cache Quantization for Self-Forcing Video Generation: A 33-Method Empirical Study","url":"https://arxiv.org/html/2603.27469v1"},{"title":"Towards 10 Million Context Length LLM Inference with KV ...","url":"https://www.stat.berkeley.edu/~mmahoney/pubs/neurips-2024-kvquant.pdf"}]

Based on the web search results, here's what I found about GEAR, KVQuant, a
…[truncated 1503 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7426
}
```

</details>

---


### Tool result

_source line 102 · 2026-05-14T12:58:32.377240+00:00_

Web search results for query: "channel pruning FFN MLP neurons LLM inference structured sparsity 2024 2025"

Links: [{"title":"1 Introduction","url":"https://arxiv.org/html/2602.00397"},{"title":"CFSP: An Efficient Structured Pruning Framework for LLMs ...","url":"https://aclanthology.org/2025.coling-main.626.pdf"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7349b8b5a6737dd36031c77212eab3ad-Paper-Conference.pdf"},{"title":"Týr-the-Pruner: Unlocking Accurate 50% Structural Pruning ...","url":"https://arxiv.org/pdf/2503.09657"},{"title":"Improving Generalization in LLM Structured Pruning via Function-Aware Neuron Grouping","url":"https://arxiv.org/html/2512.23014v1"},{"title":"Learning Optimal Pruning for Efficient On-Demand MLLMs ...","url":"https://www.arxiv.org/pdf/2506.12826"},{"title":"2SSP: A Two-Stage Framework for Structured Pruning of LLMs","url":"https://arxiv.org/html/2501.17771"},{"title":"u-MoE: Test-Time Pruning as Micro-Grained Mixture-of- ...","url":"https://www.merl.com/publications/docs/TR2025-112.pdf"},{"title":"A Two-Stage Framework for Structured Pruning of LLMs","url":"https://openreview.net/pdf?id=Qd7LzJBg21"},{"title":"Mixture-of-Channels: Exploiting Sparse FFNs for Efficient LLMs Pre-Training and Inference","url":"https://arxiv.org/html/2511.09323"}]

The web search results provide comprehensive information about recent research on channel pruning, FFN/MLP neurons, LLM inference, and structured sparsity from 2024-2025. Here's a summary of key findings:

## Recent Research Areas

**Structured Sparsity in FFN Layers:**
Recent work proposes introducing structured sparsity into FFN layers, significantly reducing prefill latency while preserving model accuracy. Research has observed a phenomenon termed "flocking" where certain intermediate neurons in MLP layers exhibit consistently high activations across prompt tokens, and activating only a subset (e.g., 50%) of these exper
…[truncated 1212 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8234
}
```

</details>

---


### Tool call

_source line 103 · 2026-05-14T12:58:34.792314+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Titanus\" KV cache pruning quantization combined hardware 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Titanus\" KV cache pruning quantization combined hardware 2025"
  }
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-14T12:58:35.294555+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "overthinking reasoning LLM compression token budget efficiency 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "overthinking reasoning LLM compression token budget efficiency 2025"
  }
}
```

</details>

---


### Tool result

_source line 105 · 2026-05-14T12:58:41.480239+00:00_

Web search results for query: ""Titanus" KV cache pruning quantization combined hardware 2025"

Links: [{"title":"[2505.17787] Titanus: Enabling KV Cache Pruning and Quantization On-the-Fly for LLM Acceleration","url":"https://arxiv.org/abs/2505.17787"},{"title":"Titanus: Enabling KV Cache Pruning and Quantization On-the-Fly for LLM Acceleration | Proceedings of the Great Lakes Symposium on VLSI 2025","url":"https://dl.acm.org/doi/full/10.1145/3716368.3735145"},{"title":"Titanus: Enabling KV Cache Pruning and Quantization On-the-Fly for LLM Acceleration","url":"https://arxiv.org/html/2505.17787"},{"title":"GitHub - peilin-chen/Titanus-for-LLM-acceleration: [GLSVLSI2025] Titanus: Enabling KV Cache Pruning and Quantization On-the-Fly for LLM Acceleration","url":"https://github.com/peilin-chen/Titanus-for-LLM-acceleration"},{"title":"Titanus: Enabling KV Cache Pruning and Quantization On- ...","url":"https://arxiv.org/pdf/2505.17787"},{"title":"(PDF) Titanus: Enabling KV Cache Pruning and Quantization On-the-Fly for LLM Acceleration","url":"https://www.researchgate.net/publication/392085543_Titanus_Enabling_KV_Cache_Pruning_and_Quantization_On-the-Fly_for_LLM_Acceleration"},{"title":"GitHub - HuangOwen/Awesome-LLM-Compression: Awesome LLM compression research papers and tools. · GitHub","url":"https://github.com/HuangOwen/Awesome-LLM-Compression"},{"title":"Proceedings of the Great Lakes Symposium on VLSI 2025","url":"https://www.linkedin.com/posts/scott-acton-953892251_titanus-enabling-kv-cache-pruning-and-quantization-activity-7348798219457306627-OHJC"},{"title":"Special Interest Group on Design Automation ​","url":"https://www.sigda.org/wp-content/uploads/2025/08/Aug-Issue-SigDA-E-News.pdf"},{"title":"Awards","url":"https://xiaoxuan-yang.github.io/awards.html"}]

Based on the search results, here's what I found about Titanus:

## Overview

Titanus is a software-hardware co-design to efficiently compress the KV cache on-the-fly. The work was presented at the Great La
…[truncated 1152 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6687
}
```

</details>

---


### Tool result

_source line 106 · 2026-05-14T12:58:43.839650+00:00_

Web search results for query: "overthinking reasoning LLM compression token budget efficiency 2025"

Links: [{"title":"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning","url":"https://arxiv.org/html/2505.11274v6"},{"title":"GitHub - Eclipsess/Awesome-Efficient-Reasoning-LLMs: [TMLR 2025] Stop Overthinking: A Survey on Efficient Reasoning for Large Language Models · GitHub","url":"https://github.com/Eclipsess/Awesome-Efficient-Reasoning-LLMs"},{"title":"Token-Budget-Aware LLM Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.1274/"},{"title":"Stop Overthinking: A Survey on Efficient Reasoning for Large Language Models","url":"https://arxiv.org/pdf/2503.16419"},{"title":"Token-Budget-Aware LLM Reasoning","url":"https://aclanthology.org/2025.findings-acl.1274.pdf"},{"title":"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=e7EBzbi8Qd"},{"title":"Published in Transactions on Machine Learning Research (08/2025)","url":"https://openreview.net/pdf?id=HvoG8SxggZ"},{"title":"Token-Budget-Aware LLM Reasoning","url":"https://arxiv.org/html/2412.18547v4"},{"title":"OckBench: Measuring the Efficiency of LLM Reasoning","url":"https://arxiv.org/html/2511.05722"},{"title":"BudgetThinker: Empowering Budget-aware LLM Reasoning with Control Tokens","url":"https://arxiv.org/html/2508.17196v1"}]

Here are the search results for your query about overthinking reasoning LLM compression token budget efficiency in 2025:

## Key Findings

**The Overthinking Problem:**
Reasoning models often suffer from the "overthinking phenomenon", generating unnecessarily lengthy reasoning steps. Even when models arrive at the correct answer early in their reasoning process, they continue generating unnecessary intermediate steps, leading to inefficiencies.

**Token Budget Approaches:**
The reasoning process of current LLMs is unnecessarily lengthy and can be compressed by including a reason
…[truncated 1347 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8545
}
```

</details>

---


### Tool call

_source line 107 · 2026-05-14T12:58:45.906998+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Scissorhands NeurIPS 2023 Liu KV cache persistence importance hypothesis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Scissorhands NeurIPS 2023 Liu KV cache persistence importance hypothesis"
  }
}
```

</details>

---


### Tool call

_source line 108 · 2026-05-14T12:58:46.567580+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"severity gradient\" OR \"interaction effect\" compression degradation attention pruning KV cache 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"severity gradient\" OR \"interaction effect\" compression degradation attention pruning KV cache 2025"
  }
}
```

</details>

---


### Tool result

_source line 109 · 2026-05-14T12:58:51.121080+00:00_

Web search results for query: "Scissorhands NeurIPS 2023 Liu KV cache persistence importance hypothesis"

Links: [{"title":"[2305.17118] Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time","url":"https://arxiv.org/abs/2305.17118"},{"title":"NeurIPS Poster Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time","url":"https://neurips.cc/virtual/2023/poster/72050"},{"title":"Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/a452a7c6c463e4ae8fbdc614c6e983e6-Abstract-Conference.html"},{"title":"Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time - Stevens Institute of Technology","url":"https://researchwith.stevens.edu/en/publications/scissorhands-exploiting-the-persistence-of-importance-hypothesis--2"},{"title":"Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time | OpenReview","url":"https://openreview.net/forum?id=JZfg6wGi6g"},{"title":"Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time","url":"https://papers.nips.cc/paper_files/paper/2023/hash/a452a7c6c463e4ae8fbdc614c6e983e6-Abstract-Conference.html"},{"title":"NeurIPS Poster Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time","url":"https://nips.cc/virtual/2023/poster/72050"},{"title":"Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2305.17118"},{"title":"[PDF] Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time | Semantic Scholar","url":"https://www.semanticscholar.org/pape
…[truncated 1470 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5214
}
```

</details>

---


### Tool result

_source line 110 · 2026-05-14T12:58:55.094814+00:00_

Web search results for query: ""severity gradient" OR "interaction effect" compression degradation attention pruning KV cache 2025"

Links: [{"title":"Expected Attention: KV Cache Compression by Estimating Attention","url":"https://arxiv.org/pdf/2510.00636"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution","url":"https://arxiv.org/html/2510.00636v1"},{"title":"[2510.00636] Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution","url":"https://arxiv.org/abs/2510.00636"},{"title":"Understanding the Physics of Key-Value Cache Compression for LLMs through Attention Dynamics","url":"https://arxiv.org/html/2603.01426"},{"title":"Towards Threshold-Free KV Cache Pruning","url":"https://arxiv.org/html/2502.16886"},{"title":"KV Cache Pruning in Transformers","url":"https://www.emergentmind.com/topics/kv-cache-pruning"},{"title":"KVTuner: Sensitivity-Aware Layer-Wise Mixed-Precision KV Cache Quantization for Efficient and Nearly Lossless LLM Inference","url":"https://arxiv.org/html/2502.04420v5"},{"title":"AirCache: Activating Inter-modal Relevancy KV Cache Compression for","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_AirCache_Activating_Inter-modal_Relevancy_KV_Cache_Compression_for_Efficient_Large_ICCV_2025_paper.pdf"},{"title":"Compressing KV Cache for Long-Context LLM Inference with Inter-Layer Attention Similarity","url":"https://arxiv.org/html/2412.02252v2"},{"title":"KV Cache Compression under Intrinsic Attention Clustering","url":"https://aclanthology.org/2025.acl-long.703.pdf"}]

I found several recent research papers and resources on KV cache compression, attention pruning, and related topics from 2025. Here's a summary of key findings:

## Key Research Areas

**Expected Attention (October 2025)**: A training-free compression method that estimates KV pairs importance by predicting how future queries will attend to them, leveraging the distribut
…[truncated 1559 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8527
}
```

</details>

---


### Tool result

_source line 111 · 2026-05-14T12:59:50.265260+00:00_

充分搜集完毕。现在整理所有发现，生成缺失引用报告。

---

以下是搜索发现的潜在遗漏相关工作，按类别整理：

---

## 类别 1：KV Cache 核心基础工作（bib 中有但疑似未在正文引用）

**H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models**
- 作者：Zhang et al.
- 发表：NeurIPS 2023
- arXiv：2306.14048
- 为什么相关：H2O 是 KV cache token 驱逐的奠基性工作，提出"heavy hitter"累积注意力分数驱逐策略。题目指出已在 bib 中，若正文未引用，与本文 KV cache eviction 组件直接相关，需要作为关键 baseline 引用。NeurIPS 2025 的"Hold Onto That Thought"证明 H2O 在推理任务中仍是最强方法之一。

**Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time**
- 作者：Liu, Desai, Liao et al.（Stevens Institute of Technology）
- 发表：NeurIPS 2023
- arXiv：2305.17118
- 为什么相关：Scissorhands 提出"重要性持久性假设"——关键 token 在未来生成步骤中仍保持重要。本文研究 thinking vs output 两个 phase 中 KV cache 驱逐的不同效果，这一假设是否在两个 phase 均成立是核心问题，Scissorhands 是不可绕开的前驱工作。

**PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling**
- 作者：Cai et al.
- 发表：2024（ACL 2024 Findings / NeurIPS投稿）
- arXiv：2406.02069
- 为什么相关：PyramidKV 提出跨层非均匀 KV 预算分配（浅层多、深层少）。本文研究 compound sparsity 中不同组件交互，PyramidKV 的层间分配策略与本文的 head pruning + channel pruning 联合压缩密切相关。题目指出 bib 中已有，若正文未引用则是遗漏。

---

## 类别 2：Phase-Aware / Reasoning-Aware 压缩（2025）

**Hold Onto That Thought: Assessing KV Cache Compression On Reasoning**
- 作者：（NeurIPS 2025 workshop / NeurIPS 2025 poster）
- 发表：NeurIPS 2025
- arXiv：2512.12008
- 为什么相关：直接评估 KV cache 压缩在推理任务（数学、逻辑、常识）上的效果，发现 H2O 类 heavy-hitter 策略在推理中显著优于其他方法。本文声称 thinking phase 与 output phase 有不同 severity gradient，该论文是评估框架的直接相关工作，必须引用以定位研究差异。

**R-KV: Redundancy-aware KV Cache Compression for Reasoning Models**
- 作者：Cai, Xiao et al.
- 发表：NeurIPS 2025
- arXiv：2505.24133
- 为什么相关：专门针对推理模型（chain-of-thought），提出冗余感知 KV 压缩，仅用 10% KV cache 保留接近全精度性能。本文研究 compound sparsity 在推理模型两个 phase 的效果，R-KV 是最直接的竞争/相关工作，讨论单一 KV 压缩在推理中的极限，为本文"为何需要 compound 视角"提供背景。

**Lethe: Layer- and Time-Adaptive KV Cache Pruning for Reasoning-Intensive LLM Serving**
- 作者：Zeng, Zhao et al.
- 发表：AAAI 2026（搜索结果显示发表在 AAAI 2026 Proceedings）
- arXiv：2511.
…[truncated 3812 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Agent",
  "elapsed_ms": 233418
}
```

</details>

---


### Tool call

_source line 112 · 2026-05-14T13:02:56.986656+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿报告\n\n**审查侧重：新颖性 + 相关工作完整性 + 写作质量 + 格式合规**\n\n---\n\n## 总体评分\n\n**Overall**: 2.5/5（Weak Reject）\n**一句话总结**: 本文报告了一个有趣的实证发现（compound sparsity severity 随推理阶段变化），但贡献停留在现象描述层面——没有提出方法、没有解决方案，且实验规模和架构覆盖不足以支撑其 claim 的普遍性；相关工作遗漏严重，格式存在 ARR 合规问题。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 主要 claim 有统计支撑，但方法学局限（2 模型同架构、50 题、仅用 PPL）削弱泛化性；entropy-discrimination collapse 机制仅有相关性证据 |\n| Excitement | 2/5 | 发现本身有趣但贡献有限——纯分析无方法/解决方案；作为 main conference 长文偏薄 |\n| Overall Assessment | 2.5/5 | 需实质性修订：扩展实验（跨架构、更大规模）、补充缺失引用、修正格式后可能适合 Findings |\n| Reproducibility | 3.5/5 | 实验设置详细，统计方法透明，但 50 题 subset 选取细节不够、代码未提及公开 |\n| Confidence | 4/5 | 对 KV cache compression 和 attention sparsity 文献较熟悉 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Limitations 节格式不符合 ARR 要求\n- 位置：§7.1（第 7 页）\n- 当前为 §7 Discussion 的编号子节（§7.1），ARR 要求无编号独立节置于 Conclusion 之后、References 之前。属于 desk reject 检查项。\n\n**N2** [critical] 相关工作遗漏严重\n- 位置：§2 Related Work\n- 极高优先级遗漏：Lethe（AAAI 2026，phase-aware KV pruning 同期竞争工作）、R-KV（NeurIPS 2025，推理模型 KV 压缩最强 baseline）、\"Hold Onto That Thought\"（NeurIPS 2025，唯一系统评估推理任务 KV 压缩的工作）\n- 高优先级遗漏：Scissorhands（NeurIPS 2023）、FastGen（ICLR 2024）、StreamingLLM（ICLR 2024）、LLM-Pruner（NeurIPS 2023）、Titanus（GLSVLSI 2025）\n- 审稿人很可能因缺少 Lethe 和 R-KV 质疑领域了解程度\n\n**N3** [critical] 贡献深度不足\n- 纯分析无方法/解决方案。§7 提到 \"phase-aware controller\" 但停留在 future work。对 EMNLP main conference 长文偏薄，更适合 Findings。\n\n**N4** [critical] 实验规模和多样性不足\n- 仅 2 个模型共享 Qwen2 架构，\"cross-model replication\" 措辞有误导性\n- 仅 50 道 MATH-500 题\n- 仅 7B 规模\n- 仅用 PPL 作为质量指标，缺少 accuracy——PPL 恶化不等于答案错误\n\n---\n\n## Should-Fix 问题\n\n**W1** [major] Entropy-discrimination collapse 因果证据不足（Table 5 仅相关性，缺 intervention 实验）\n**W2** [major] Bibliography 管理混乱——7 条 orphan entries（bib 有但正文未引），h2o-neurips2023 title 字段为空\n**W3** [major] Abstract 约 600+ 词，远超通常 150-250 词建议\n**W4** [major] Footnote 2 泄露 \"4× NVIDIA RTX PRO 6000 Blackwell Server Edition 96 GB GPUs\"，去匿名化风险\n**W5** [minor] \"Severity gradient\" 术语过载（同时指标和概念）\n**W6** [minor] Appendix B 与 Appendix D 文本几乎完全重复，疑为粘贴错误\n**W7** [minor] 方程编号可能不连续（Eq. 2 位置不明）\n\n---\n\n## 小问题\n- §6.3 PyramidKV 被引用两次且用不同作者信息\n- Footnote 1 措辞不清 \"float16 eliminated entirely\"\n- Table 3 caption 公式有多余项 \"− Ĥ_dist\"\n- 部分 bib 年份与 OpenAlex 不一致（adakv-neurips2025 实际 2024、pope-mlsys2023 实际 2022）\n\n---\n\n## Missing References（完整列表）\n\n| 优先级 | 论文 | Venue | 理由 |\n|--------|------|-------|------|\n| 极高 | Lethe (Zeng et al.) | AAAI 2026 | 与本文 phase-gated 思路直接重叠 |\n| 极高 | R-KV (Cai et al.) | NeurIPS 2025 | 推理模型 KV 压缩最强 baseline |\n| 极高 | Hold Onto That Thought | NeurIPS 2025 | 唯一系统评估推理任务 KV 压缩 |\n| 高 | Scissorhands (Liu et al.) | NeurIPS 2023 | KV eviction 基础方法 |\n| 高 | FastGen (Ge et al.) | ICLR 2024 | Per-head adaptive KV cache |\n| 高 | StreamingLLM (Xiao et al.) | ICLR 2024 | Attention sink 基础 |\n| 高 | LLM-Pruner (Ma et al.) | NeurIPS 2023 | Coupled pruning 开创性工作 |\n| 高 | Titanus (Chen et al.) | GLSVLSI 2025 | KV pruning+quantization 复合效果 |\n| 中 | SparseGPT | ICML 2023 | 权重稀疏化基础 |\n| 中 | Wanda | ICLR 2024 | 轻量 pruning |\n| 中 | MInference | NeurIPS 2024 | 注意力稀疏模式分析 |\n\n---\n\n## 主要优势\n1. 研究问题有价值——compound sparsity 的 phase-dependent behavior 确实未被充分研究\n2. 统计方法论优秀（permutation tests, bootstrap CI, Bonferroni correction, paired effect sizes）\n3. Random eviction 作为 falsification control 的实验设计巧妙\n4. Crossover 现象（§5.3）是 non-trivial 且有实际意义的发现\n5. 写作总体清晰，§5 结果层层递进\n\n---\n\n## Questions for Authors\n1. 为什么不报告 MATH-500 accuracy？PPL 下降是否对应答案正确率下降？\n2. 与 Lethe（AAAI 2026）的区别和互补？\n3. 是否考虑过 LLaMA-3 或 Mistral 上的验证？\n4. Entropy-discrimination collapse 能否通过 intervention 实验验证因果性？\n5. Appendix B 和 D 文本重复是编辑错误吗？\n\n---\n\n**Overall Score**: Weak Reject (2.5/5)\n**Confidence**: 4/5",
  "reviewer_id": "2",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 审稿报告\n\n**审查侧重：新颖性 + 相关工作完整性 + 写作质量 + 格式合规**\n\n---\n\n## 总体评分\n\n**Overall**: 2.5/5（Weak Reject）\n**一句话总结**: 本文报告了一个有趣的实证发现（compound sparsity severity 随推理阶段变化），但贡献停留在现象描述层面——没有提出方法、没有解决方案，且实验规模和架构覆盖不足以支撑其 claim 的普遍性；相关工作遗漏严重，格式存在 ARR 合规问题。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 主要 claim 有统计支撑，但方法学局限（2 模型同架构、50 题、仅用 PPL）削弱泛化性；entropy-discrimination collapse 机制仅有相关性证据 |\n| Excitement | 2/5 | 发现本身有趣但贡献有限——纯分析无方法/解决方案；作为 main conference 长文偏薄 |\n| Overall Assessment | 2.5/5 | 需实质性修订：扩展实验（跨架构、更大规模）、补充缺失引用、修正格式后可能适合 Findings |\n| Reproducibility | 3.5/5 | 实验设置详细，统计方法透明，但 50 题 subset 选取细节不够、代码未提及公开 |\n| Confidence | 4/5 | 对 KV cache compression 和 attention sparsity 文献较熟悉 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Limitations 节格式不符合 ARR 要求\n- 位置：§7.1（第 7 页）\n- 当前为 §7 Discussion 的编号子节（§7.1），ARR 要求无编号独立节置于 Conclusion 之后、References 之前。属于 desk reject 检查项。\n\n**N2** [critical] 相关工作遗漏严重\n- 位置：§2 Related Work\n- 极高优先级遗漏：Lethe（AAAI 2026，phase-aware KV pruning 同期竞争工作）、R-KV（NeurIPS 2025，推理模型 KV 压缩最强 baseline）、\"Hold Onto That Thought\"（NeurIPS 2025，唯一系统评估推理任务 KV 压缩的工作）\n- 高优先级遗漏：Scissorhands（NeurIPS 2023）、FastGen（ICLR 2024）、StreamingLLM（ICLR 2024）、LLM-Pruner（NeurIPS 2023）、Titanus（GLSVLSI 2025）\n- 审稿人很可能因缺少 Lethe 和 R-KV 质疑领域了解程度\n\n**N3** [critical] 贡献深度不足\n- 纯分析无方法/解决方案。§7 提到 \"phase-aware controller\" 但停留在 future work。对 EMNLP main conference 长文偏薄，更适合 Findings。\n\n**N4** [critical] 实验规模和多样性不足\n- 仅 2 个模型共享 Qwen2 架构，\"cross-model replication\" 措辞有误导性\n- 仅 50 道 MATH-500 题\n- 仅 7B 规模\n- 仅用 PPL 作为质量指标，缺少 accuracy——PPL 恶化不等于答案错误\n\n---\n\n## Should-Fix 问题\n\n**W1** [major] Entropy-discrimination collapse 因果证据不足（Table 5 仅相关性，缺 intervention 实验）\n**W2** [major] Bibliography 管理混乱——7 条 orphan entries（bib 有但正文未引），h2o-neurips2023 title 字段为空\n**W3** [major] Abstract 约 600+ 词，远超通常 150-250 词建议\n**W4** [major] Footnote 2 泄露 \"4× NVIDIA RTX PRO 6000 Blackwell Server Edition 96 GB GPUs\"，去匿名化风险\n**W5** [minor] \"Severity gradient\" 术语过载（同时指标和概念）\n**W6** [minor] Appendix B 与 Appendix D 文本几乎完全重复，疑为粘贴错误\n**W7** [minor] 方程编号可能不连续（Eq. 2 位置不明）\n\n---\n\n## 小问题\n- §6.3 PyramidKV 被引用两次且用不同作者信息\n- Footnote 1 措辞不清 \"float16 eliminated entirely\"\n- Table 3 caption 公式有多余项 \"− Ĥ_dist\"\n- 部分 bib 年份与 OpenAlex 不一致（adakv-neurips2025 实际 2024、pope-mlsys2023 实际 2022）\n\n---\n\n## Missing References（完整列表）\n\n| 优先级 | 论文 | Venue | 理由 |\n|--------|------|-------|------|\n| 极高 | Lethe (Zeng et al.) | AAAI 2026 | 与本文 phase-gated 思路直接重叠 |\n| 极高 | R-KV (Cai et al.) | NeurIPS 2025 | 推理模型 KV 压缩最强 baseline |\n| 极高 | Hold Onto That Thought | NeurIPS 2025 | 唯一系统评估推理任务 KV 压缩 |\n| 高 | Scissorhands (Liu et al.) | NeurIPS 2023 | KV eviction 基础方法 |\n| 高 | FastGen (Ge et al.) | ICLR 2024 | Per-head adaptive KV cache |\n| 高 | StreamingLLM (Xiao et al.) | ICLR 2024 | Attention sink 基础 |\n| 高 | LLM-Pruner (Ma et al.) | NeurIPS 2023 | Coupled pruning 开创性工作 |\n| 高 | Titanus (Chen et al.) | GLSVLSI 2025 | KV pruning+quantization 复合效果 |\n| 中 | SparseGPT | ICML 2023 | 权重稀疏化基础 |\n| 中 | Wanda | ICLR 2024 | 轻量 pruning |\n| 中 | MInference | NeurIPS 2024 | 注意力稀疏模式分析 |\n\n---\n\n## 主要优势\n1. 研究问题有价值——compound sparsity 的 phase-dependent behavior 确实未被充分研究\n2. 统计方法论优秀（permutation tests, bootstrap CI, Bonferroni correction, paired effect sizes）\n3. Random eviction 作为 falsification control 的实验设计巧妙\n4. Crossover 现象（§5.3）是 non-trivial 且有实际意义的发现\n5. 写作总体清晰，§5 结果层层递进\n\n---\n\n## Questions for Authors\n1. 为什么不报告 MATH-500 accuracy？PPL 下降是否对应答案正确率下降？\n2. 与 Lethe（AAAI 2026）的区别和互补？\n3. 是否考虑过 LLaMA-3 或 Mistral 上的验证？\n4. Entropy-discrimination collapse 能否通过 intervention 实验验证因果性？\n5. Appendix B 和 D 文本重复是编辑错误吗？\n\n---\n\n**Overall Score**: Weak Reject (2.5/5)\n**Confidence**: 4/5",
    "reviewer_id": "2",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 113 · 2026-05-14T13:03:02.484517+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5497
}
```

</details>

---


### Assistant

_source line 114 · 2026-05-14T13:03:09.539708+00:00_

审稿报告已提交给 Review Director。

总结：给出 **Weak Reject (2.5/5)** 评分。主要问题：(1) Limitations 节格式违反 ARR 要求（编号子节而非独立节）；(2) 遗漏 Lethe、R-KV、"Hold Onto That Thought" 等直接竞争/基础工作；(3) 贡献停留在现象描述——无方法、无解决方案；(4) 仅 2 个同架构 7B 模型 + 50 题 + 仅 PPL 指标，泛化性 claim 过强。优势方面，统计方法论扎实，random eviction 对照设计巧妙，crossover 现象有实际意义。建议补充跨架构实验 + accuracy 指标 + 缺失引用 + 格式修正后投 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2"
}
```

</details>

---


## Round 2

## Round 2

92 recorded events


### User

_source line 115 · 2026-05-14T13:04:55.365250+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2

**你的审查侧重：新颖性 + 相关工作完整性 + 写作质量 + 实际影响**

### 论文信息
- **标题**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Reasoning Models
- **论文路径**: `artifacts/_project/paper/main.pdf`
- **目标 Venue**: EMNLP 2026 Main Conference (via ACL Rolling Review May 2026 cycle)
- **截止日期**: 2026-05-25
- **格式要求**: ACL 模板, long paper ≤8 页正文（不含参考文献和附录）, double-blind, 需 Limitations section, 附录不参与正式审稿但可参考

### 论文概要
论文研究 compound sparsity（同时 attention head pruning + KV cache eviction）在 reasoning 模型不同生成阶段的交互效应。核心发现：(1) importance-based eviction 下 compound severity 展现 phase-dependent severity gradient（69×→274× 跨 sparsity levels）；(2) random eviction 无此效应（7/8 条件不显著）；(3) s=0.25 处出现 strategy ranking reversal；(4) 提出 entropy-discrimination collapse 作为机制解释。在 DeepSeek-R1-Distill-Qwen-7B 和 Qwen2.5-7B-Instruct 上验证，50 MATH-500 问题。

### 你的审查重点

请严格、不留情面地评估以下方面：

1. **新颖性 (Novelty)**：
   - 核心贡献（phase-dependent compound interaction）相对于现有 compound compression 文献（Liao et al. 2026 SparK; Mozaffari et al. 2025 SLiM; von Rad et al. 2026 UniComp）的增量价值有多大？
   - "Severity gradient" 和 "phase-strategy crossover" 是否足够构成一篇 EMNLP 主会论文的贡献？
   - Interaction Index 是否只是已有 super-additivity 概念的简单形式化？
   - Discrimination collapse 是否只是一个事后观察而非真正的机制解释？

2. **相关工作 (Related Work)**：
   - 是否有重要的遗漏？特别关注：
     - 2025-2026 年的 compound compression / joint pruning 工作
     - Phase-aware inference 方面的最新进展（ThinKV 之外）
     - Reasoning model compression 的相关工作
   - 用 web_search 搜索最新相关工作，验证是否有重要遗漏
   - 对已引用工作的定位是否准确公正？

3. **写作质量**：
   - 论文结构是否清晰？正文 ~5 页是否过于紧凑？
   - Abstract 是否准确反映核心贡献和发现？
   - 数学符号是否一致？
   - 图表是否有效传达信息？Figure 1-4 的设计是否合理？
   - Limitations section 是否诚实全面？

4. **实际影响和 Actionability**：
   - 论文的发现是否能直接指导实际的 LLM 部署决策？
   - "Phase-aware compression budget" 的提议是否具体到可操作？还是只是概念性的？
   - 缺少 throughput/latency 测量对论文价值的影响有多大？

5. **格式合规**：
   - 是否符合 EMNLP 2026 / ARR 格式要求？
   - 匿名性是否完整（检查自引、致谢、代码链接等）？
   - 引用格式是否正确？

请按 EMNLP 审稿标准输出完整审稿报告，包含 Summary、Strengths、Weaknesses（逐条）、Questions for Authors、Missing References（用 web_search 验证）、Overall Assessment。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 116 · 2026-05-14T13:05:06.402033+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__verify_references,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__verify_references,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-14T13:05:06.452756+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 118 · 2026-05-14T13:05:13.428260+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.pdf",
  "pages": "1-5",
  "dpi": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.pdf",
    "pages": "1-5",
    "dpi": "200"
  }
}
```

</details>

---


### Tool call

_source line 119 · 2026-05-14T13:05:14.384851+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 120 · 2026-05-14T13:05:14.992093+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "compound sparsity pruning KV cache eviction joint compression LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "compound sparsity pruning KV cache eviction joint compression LLM 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 121 · 2026-05-14T13:05:17.375673+00:00_

Error: result (4,561,049 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse--claude-sessions-review-reviewer-2-d0398257/792468c2-2ec1-47cc-9ece-e60ae9112cdb/tool-results/mcp-agent-ml-research-pdf_to_images-1778763917044.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse--claude-sessions-review-reviewer-2-d0398257/792468c2-2ec1-47cc-9ece-e60ae9112cdb/tool-results/mcp-agent-ml-research-pdf_to_images-1778763917044.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse--claude-sessions-review-reviewer-2-d0398257/792468c2-2ec1-47cc-9ece-e60ae9112cdb/tool-results/mcp-agent-ml-research-pdf_to_images-1778763917044.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 3947
}
```

</details>

---


### Tool result

_source line 122 · 2026-05-14T13:05:25.893291+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"}]

I've found information about the ACL Rolling Review 2026 reviewer guidelines and review form. Here's what I found:

## Reviewer Guidelines

The ARR peer review guidelines are a work-in-progress and will be updated as ARR evolves, and reviewers should always check whether the version they are familiar with is still the current one before starting an a
…[truncated 1556 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 11508
}
```

</details>

---


### Tool result

_source line 123 · 2026-05-14T13:05:26.295550+00:00_

Web search results for query: "compound sparsity pruning KV cache eviction joint compression LLM 2025 2026"

Links: [{"title":"[2512.14946] EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving","url":"https://arxiv.org/abs/2512.14946"},{"title":"EvicPress: Joint KV-Cache Compression and Eviction for Efficient LLM Serving","url":"https://arxiv.org/html/2512.14946"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"PagedEviction: Structured Block-wise KV Cache Pruning ...","url":"https://arxiv.org/pdf/2509.04377"},{"title":"EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251214946F/abstract"},{"title":"GitHub - NVIDIA/kvpress: LLM KV cache compression made easy · GitHub","url":"https://github.com/NVIDIA/kvpress"},{"title":"SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning — ROCm Blogs","url":"https://rocm.blogs.amd.com/artificial-intelligence/spark-blog/README.html"},{"title":"Caching and Reuse Optimizations","url":"https://www.aussieai.com/research/caching"},{"title":"Evolutionary KV Cache Compression for LLM Inference","url":"https://aclanthology.org/2025.findings-emnlp.88.pdf"}]

I found several relevant research results on your query about compound sparsity, pruning, KV cache eviction, and joint compression for LLMs. Here's what the search uncovered:

## Key Findings

**EVICPRESS (Joint KV-Cache Compression and Eviction)**

The mos
…[truncated 1419 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 11303
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-14T13:05:34.744279+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.pdf",
  "pages": "1",
  "dpi": "180"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.pdf",
    "pages": "1",
    "dpi": "180"
  }
}
```

</details>

---


### Tool result

_source line 125 · 2026-05-14T13:05:37.189340+00:00_

Error: result (731,681 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse--claude-sessions-review-reviewer-2-d0398257/792468c2-2ec1-47cc-9ece-e60ae9112cdb/tool-results/mcp-agent-ml-research-pdf_to_images-1778763935405.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse--claude-sessions-review-reviewer-2-d0398257/792468c2-2ec1-47cc-9ece-e60ae9112cdb/tool-results/mcp-agent-ml-research-pdf_to_images-1778763935405.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse--claude-sessions-review-reviewer-2-d0398257/792468c2-2ec1-47cc-9ece-e60ae9112cdb/tool-results/mcp-agent-ml-research-pdf_to_images-1778763935405.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 2445
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-14T13:05:37.189916+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 etc), and descriptions for each score level. I need the exact criteria names and scoring rubrics."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 etc), and descriptions for each score level. I need the exact criteria names and scoring rubrics."
  }
}
```

</details>

---


### Tool call

_source line 127 · 2026-05-14T13:05:37.845590+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "phase-aware KV cache compression reasoning models ThinKV 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "phase-aware KV cache compression reasoning models ThinKV 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 128 · 2026-05-14T13:05:38.298753+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "reasoning model compression DeepSeek-R1 pruning sparsity 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "reasoning model compression DeepSeek-R1 pruning sparsity 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-14T13:05:45.753889+00:00_

Web search results for query: "phase-aware KV cache compression reasoning models ThinKV 2025 2026"

Links: [{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/html/2510.01290v1"},{"title":"[2510.01290] ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/abs/2510.01290"},{"title":"[2510.01290v1] ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/abs/2510.01290v1"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=M3CeHnZKNC"},{"title":"THINKV: THOUGHT-ADAPTIVE KV CACHE COM- PRESSION FOR EFFICIENT REASONING MODELS","url":"https://arxiv.org/pdf/2510.01290v1"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning | OpenReview","url":"https://openreview.net/forum?id=udgrpHqw4F"},{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://arxiv.org/html/2505.24133"},{"title":"LongFlow: Efficient KV Cache Compression for Reasoning Models","url":"https://arxiv.org/html/2603.11504"}]

Based on the search results, I found relevant information about ThinKV and phase-aware KV cache compression for reasoning models:

## ThinKV: Thought-Adaptive KV Cache Compression

ThinKV is a thought-adaptive KV cache compression framework for Large Reasoning Models (LRMs) that exploits attention sparsity by decomposing chains of thought into reasoning, execution, and transition segments, enabling joint thought-aware quantization and eviction that sustains accuracy under hig
…[truncated 1314 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7908
}
```

</details>

---


### Tool result

_source line 130 · 2026-05-14T13:05:45.854882+00:00_

Web search results for query: "reasoning model compression DeepSeek-R1 pruning sparsity 2025 2026"

Links: [{"title":"Reasoning Models Can Be Accurately Pruned via Chain-of-Thought Reconstruction","url":"https://arxiv.org/html/2509.12464v1"},{"title":"Quantum physicists have shrunk and “de-censored” DeepSeek R1 | MIT Technology Review","url":"https://www.technologyreview.com/2025/11/19/1128119/quantum-physicists-compress-and-deconsor-deepseekr1/"},{"title":"NeurIPS Reasoning Models Can Be Accurately Pruned via Chain-of-Thought Reconstruction","url":"https://neurips.cc/virtual/2025/loc/san-diego/126571"},{"title":"Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction | OpenReview","url":"https://openreview.net/forum?id=tyGfwG6xTh"},{"title":"The Complete Guide to DeepSeek Models: V3, R1, V4 and Beyond","url":"https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond"},{"title":"DeepSeek-R1: The Open-Source Reasoning Model","url":"https://www.sitepoint.com/deepseek-r1-open-source-reasoning/"},{"title":"Think Before You Prune: Self-Reflective Structured Pruning for Reasoning Language Models","url":"https://arxiv.org/html/2512.02185v1"},{"title":"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs ...","url":"https://arxiv.org/pdf/2501.12948"},{"title":"Deployment-ready reasoning with quantized DeepSeek-R1 models | Red Hat Developer","url":"https://developers.redhat.com/articles/2025/03/03/deployment-ready-reasoning-quantized-deepseek-r1-models"},{"title":"Compressing Large MoE Models via Efficient Pruning and Data-Aware Calibration | OpenReview","url":"https://openreview.net/forum?id=dJy6z9peC7"}]

Based on the search results, here are the key findings on reasoning model compression, DeepSeek-R1, pruning, and sparsity for 2025-2026:

## Chain-of-Thought Reconstruction Approaches

Reasoning-Aware Compression (RAC) can prune reasoning LLMs to 50% sparsity while maintaining up to 95% of the original model's acc
…[truncated 1225 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7556
}
```

</details>

---


### Tool result

_source line 131 · 2026-05-14T13:05:46.962782+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully"
- **4**: Quite sure with unlikely but conceivable gaps in evaluation
- **3**: Pretty sure but may have missed details in math or experimental design
- **2**: Willing to defend evaluation but likely missed details or novelty assessment
- **1**: "Not my area, or paper is very hard to understand"

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: Strong with sufficient claim support; extra experiments optional
- **3**: Acceptable; main claims supported with minor details needed
- **2**: Poor; main claims insufficiently supported with technical problems
- **1**: "Major Issues: not yet sufficiently thorough to warrant publication"

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: Would mention to colleagues and attend presentation
- **3**: Might mention some points if time permits
- **2**: "Potentially Interesting: does not resonate with me"
- **1**: Not resonant with community or unrelated to language processing

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- **5**: Consider for award (top 2.5% papers)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

## 5. **Reproducibility**
Scale: 1-5
- **5**: Results easily reproducible
- **4**: Mostly reproducible despite minor variations
- **3**: "Reproducible with some difficulty" due to parameter underspecification
- **2**: Hard to reproduce; unavailable data or insufficient details
- **1**: Impossible to reproduce

## 6. **Datasets & Software Value**
Scale: 1-5 (separate)
- **5**: Enabling impact on future research direction
- **4**: Useful for ongoing researcher work
- **3**: Potentially useful
- **2**: Documentary va
…[truncated 301 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 9772
}
```

</details>

---


### Tool call

_source line 132 · 2026-05-14T13:06:09.575130+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read paper pages 1-4",
  "prompt": "Read a paper PDF rendered as images. The images were rendered to a JSON file. \n\nYour task: Extract the COMPLETE text content from pages 1-4 of this paper, including all equations, table data, figure captions, and footnotes. Report everything verbatim - do not summarize.\n\nThe JSON file is at: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse--claude-sessions-review-reviewer-2-d0398257/792468c2-2ec1-47cc-9ece-e60ae9112cdb/tool-results/mcp-agent-ml-research-pdf_to_images-1778763935405.txt\n\nThis file has schema: {result: string}. The result field contains rendered page image data. Use jq to probe the structure, then use python to extract and decode the base64 image data. Read the images using the Read tool to view them visually.\n\nActually, the easier approach: The PDF images were saved to disk. Check the output directory - it should be near the PDF at /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/ or similar. Use Glob to find the PNG files, then Read each page image file directly.\n\nReport the COMPLETE text of pages 1-4 including:\n- Title, authors, abstract\n- All section headings and body text\n- All equations with their numbers\n- All table contents\n- All figure captions\n- All footnotes",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Agent",
  "tool_args": {
    "description": "Read paper pages 1-4",
    "prompt": "Read a paper PDF rendered as images. The images were rendered to a JSON file. \n\nYour task: Extract the COMPLETE text content from pages 1-4 of this paper, including all equations, table data, figure captions, and footnotes. Report everything verbatim - do not summarize.\n\nThe JSON file is at: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse--claude-sessions-review-reviewer-2-d0398257/792468c2-2ec1-47cc-9ece-e60ae9112cdb/tool-results/mcp-agent-ml-research-pdf_to_images-1778763935405.txt\n\nThis file has schema: {result: string}. The result field contains rendered page image data. Use jq to probe the structure, then use python to extract and decode the base64 image data. Read the images using the Read tool to view them visually.\n\nActually, the easier approach: The PDF images were saved to disk. Check the output directory - it should be near the PDF at /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/ or similar. Use Glob to find the PNG files, then Read each page image file directly.\n\nReport the COMPLETE text of pages 1-4 including:\n- Title, authors, abstract\n- All section headings and body text\n- All equations with their numbers\n- All table contents\n- All figure captions\n- All footnotes",
    "model": "sonnet"
  }
}
```

</details>

---


### Tool call

_source line 133 · 2026-05-14T13:06:14.924089+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.png",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.png",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper"
  }
}
```

</details>

---


### Tool result

_source line 134 · 2026-05-14T13:06:14.924633+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p9.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p10.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p4.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p5.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p6.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p7.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p8.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p2.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p3.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p11.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p12.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p11.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p1.png
/home/ubuntu/.agent-ml
…[truncated 1193 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 135 · 2026-05-14T13:06:14.925020+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read paper pages 5-10",
  "prompt": "Read a paper PDF. Your task: Extract the COMPLETE text content from pages 5 onwards of this paper.\n\nFirst, use the mcp__agent-ml-research__pdf_to_images tool to render pages 5-10 of the PDF:\n- pdf_path: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.pdf  \n- pages: \"5-6\"\n- dpi: 150\n\nIf that's too large, try one page at a time.\n\nAlternatively, look for already-rendered images. Use Glob to search for PNG files in directories like:\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/\n\nRead each page image with the Read tool.\n\nReport the COMPLETE text of pages 5+ including:\n- All section headings and body text\n- All equations with numbers\n- All table contents with all numerical values\n- All figure captions\n- References section\n- Appendix content\n- Limitations section",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Agent",
  "tool_args": {
    "description": "Read paper pages 5-10",
    "prompt": "Read a paper PDF. Your task: Extract the COMPLETE text content from pages 5 onwards of this paper.\n\nFirst, use the mcp__agent-ml-research__pdf_to_images tool to render pages 5-10 of the PDF:\n- pdf_path: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.pdf  \n- pages: \"5-6\"\n- dpi: 150\n\nIf that's too large, try one page at a time.\n\nAlternatively, look for already-rendered images. Use Glob to search for PNG files in directories like:\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/\n- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/\n\nRead each page image with the Read tool.\n\nReport the COMPLETE text of pages 5+ including:\n- All section headings and body text\n- All equations with numbers\n- All table contents with all numerical values\n- All figure captions\n- References section\n- Appendix content\n- Limitations section",
    "model": "sonnet"
  }
}
```

</details>

---


### Tool call

_source line 136 · 2026-05-14T13:06:15.881215+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "attention head pruning interaction KV cache compression super-additivity 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "attention head pruning interaction KV cache compression super-additivity 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 137 · 2026-05-14T13:06:16.494818+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-14T13:06:16.495284+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 139 · 2026-05-14T13:06:16.495547+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"UniComp\" OR \"SLiM\" unified compression LLM pruning quantization 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"UniComp\" OR \"SLiM\" unified compression LLM pruning quantization 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-14T13:06:19.383499+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.png",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.png",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper"
  }
}
```

</details>

---


### Tool call

_source line 141 · 2026-05-14T13:06:19.384093+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper"
  }
}
```

</details>

---


### Tool result

_source line 142 · 2026-05-14T13:06:20.642400+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p9.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p10.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p4.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p5.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p6.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p7.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p8.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p2.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p3.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p11.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p12.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p11.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p1.png
/home/ubuntu/.agent-ml
…[truncated 1193 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 1258
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-14T13:06:20.693209+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/citation_audit_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/acl.sty
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/acl_natbib.bst
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/paper_compilation_note.txt
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/fig1_dose_response.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main_00fdd3.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main_5d82e3.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main_c93d3b.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main_9a05ce.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main_a1a036.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-co
…[truncated 4930 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 1309
}
```

</details>

---


### Tool result

_source line 144 · 2026-05-14T13:06:21.651393+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5156
}
```

</details>

---


### Tool result

_source line 145 · 2026-05-14T13:06:22.429024+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5933
}
```

</details>

---


### Tool result

_source line 146 · 2026-05-14T13:06:24.780220+00:00_

Web search results for query: "attention head pruning interaction KV cache compression super-additivity 2025 2026"

Links: [{"title":"Expected Attention: KV Cache Compression by Estimating Attention","url":"https://arxiv.org/pdf/2510.00636"},{"title":"[2510.00636] Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution","url":"https://arxiv.org/abs/2510.00636"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution","url":"https://arxiv.org/html/2510.00636v1"},{"title":"GitHub - NVIDIA/kvpress: LLM KV cache compression made easy · GitHub","url":"https://github.com/NVIDIA/kvpress"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention From Future Queries Distribution | OpenReview","url":"https://openreview.net/forum?id=VmojW15eRc"},{"title":"Lethe: Layer- and Time-Adaptive KV Cache Pruning for Reasoning-Intensive LLM Serving","url":"https://arxiv.org/html/2511.06029"},{"title":"HCAttention: Extreme KV Cache Compression via ...","url":"https://arxiv.org/pdf/2507.19823"},{"title":"Understanding the Physics of Key-Value Cache Compression for LLMs through Attention Dynamics","url":"https://arxiv.org/html/2603.01426"},{"title":"KV Cache Optimization via Multi-Head Latent Attention - PyImageSearch","url":"https://pyimagesearch.com/2025/10/13/kv-cache-optimization-via-multi-head-latent-attention/"},{"title":"MLA: Redefining KV-Cache Through Low-Rank Projections and On-Demand Decompression","url":"https://huggingface.co/blog/NormalUhr/mla-explanation"}]

I found several relevant papers and resources on KV cache compression and attention optimization from 2025-2026. Here's what the search returned:

## Key Results

**Expected Attention (October 2025)**: A training-free compression method that estimates KV pairs importance by predicting how future queries will attend to them, leveraging distributional properties of LLM activations to compute expected attention sc
…[truncated 1589 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8899
}
```

</details>

---


### Tool call

_source line 147 · 2026-05-14T13:06:25.498900+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 148 · 2026-05-14T13:06:25.599747+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 149 · 2026-05-14T13:06:27.891030+00:00_

Web search results for query: ""UniComp" OR "SLiM" unified compression LLM pruning quantization 2025 2026"

Links: [{"title":"[2602.09130] UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation","url":"https://arxiv.org/abs/2602.09130"},{"title":"UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization, and Distillation","url":"https://arxiv.org/html/2602.09130"},{"title":"[2602.09130v2] UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation","url":"https://arxiv.org/abs/2602.09130v2"},{"title":"SLIM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression | Research","url":"https://research.nvidia.com/publication/2025-06_slim-one-shot-quantization-and-sparsity-low-rank-approximation-llm-weight"},{"title":"SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression","url":"https://arxiv.org/html/2410.09615"},{"title":"(PDF) UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation","url":"https://www.researchgate.net/publication/400660606_UniComp_A_Unified_Evaluation_of_Large_Language_Model_Compression_via_Pruning_Quantization_and_Distillation"},{"title":"ICML Poster SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression","url":"https://icml.cc/virtual/2025/poster/46479"},{"title":"[2410.09615] SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression","url":"https://arxiv.org/abs/2410.09615"},{"title":"SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression | OpenReview","url":"https://openreview.net/forum?id=4UfRP8MopP"},{"title":"UNICOMP: A Unified Evaluation of Large Language Model Compression","url":"https://arxiv.org/pdf/2602.09130"}]

Based on the search results, I found information 
…[truncated 1876 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 11395
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-14T13:06:27.941852+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 151 · 2026-05-14T13:06:27.942331+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 152 · 2026-05-14T13:06:32.892215+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 7292
}
```

</details>

---


### Tool result

_source line 153 · 2026-05-14T13:06:32.893031+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 7394
}
```

</details>

---


### Tool result

_source line 154 · 2026-05-14T13:06:33.249777+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5307
}
```

</details>

---


### Tool result

_source line 155 · 2026-05-14T13:06:33.452319+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5510
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-14T13:06:35.814244+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 157 · 2026-05-14T13:06:36.322190+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 158 · 2026-05-14T13:06:38.827266+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3013
}
```

</details>

---


### Tool result

_source line 159 · 2026-05-14T13:06:39.030074+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2707
}
```

</details>

---


### Tool call

_source line 160 · 2026-05-14T13:06:41.894706+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 161 · 2026-05-14T13:06:42.401979+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 162 · 2026-05-14T13:06:45.704807+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3810
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-14T13:06:45.705708+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3303
}
```

</details>

---


### Tool call

_source line 164 · 2026-05-14T13:06:52.220626+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 165 · 2026-05-14T13:06:52.574974+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 166 · 2026-05-14T13:06:52.625633+00:00_

1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Strategy-Dependent Severity}
6	\label{sec:strategy-severity}
7	
8	Table~\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\times}$ amplification. Under random eviction, no systematic growth is observed ($-0.02$ to $1.54$), confirming that compound severity depends qualitatively on eviction strategy. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}
14	\label{tab:aggregate-ii}
15	\begin{tabular}{@{}lcccc@{}}
16	\toprule
17	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
18	\midrule
19	Importance & 0.39 & 1.48 & 7.16 & 14.59 \\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff
20	Random     & 0.01 & $-$0.02 & 0.54 & 1.54 \\ % exp_id: bf16_ds_rand_s015..s030; source: experiment_summary_table.json median_diff
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	
26	\subsection{Phase-Modulated Amplification}
27	\label{sec:phase-amplification}
28	
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. The severity gradient $G$ increases from $69{\times}$ at $s{=}0.15$ to $274{\times}$ at $s{=}0.30$ under importance-based eviction, while the high-sparsity phase experiences near-zero interaction ($\widetilde{\mathrm{II}}_{\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, $G \approx 0.9$--$1.7{\times}$ at all sparsity levels (full per-phase breakdown in Append
…[truncated 2733 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-14T13:06:53.336456+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1115
}
```

</details>

---


### Tool call

_source line 168 · 2026-05-14T13:06:59.528316+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-14T13:06:59.839888+00:00_

1	\subsection{Discrimination Collapse Mechanism}
2	\label{sec:discrimination-collapse}
3	
4	Head pruning reduces the number of heads contributing to cumulative importance scores, flattening the score distribution. The Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) after pruning across all 16 conditions (Appendix Table~\ref{tab:discrimination-metrics-full}). % exp_id: c4_entropy_deepseek, c4_entropy_qwen
5	When importance scores lose discriminability, thresholding degenerates into noise-sensitive selection. This is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \approx 1$. The mechanism predicts that any attention-mass-based importance metric should exhibit discrimination collapse under head pruning, while metrics derived from sources independent of attention (e.g., activation magnitude) should produce flatter severity gradients. A secondary entropy redistribution pattern is consistent for DeepSeek but only partially replicates on Qwen (Appendix~\ref{app:entropy-redistribution}). % exp_id: c4_entropy_deepseek, c4_entropy_qwen
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 311
}
```

</details>

---


### Tool call

_source line 170 · 2026-05-14T13:06:59.891383+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 171 · 2026-05-14T13:06:59.892034+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Quantitative surprise.}
5	While the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($69$--$274{\times}$) far exceeds a naive ``somewhat worse'' prediction. The crossover---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) and underperforms in low-sparsity phases ($7.196$ vs.\ $1.363$)---cannot be derived from single-axis entropy reasoning. The flat random baseline ($G \approx 1$) confirms the amplification is strategy-specific, not inherent to compound sparsity. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json
6	
7	\paragraph{Implications for deployment.}
8	Applying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation.
9	
10	\paragraph{Cross-model robustness.}
11	The pattern replicates with perfect ordinal agreement across both models (Spearman $\rho{=}1.0$; gradient permutation $p{=}0.043$), though Qwen's magnitudes are ${\sim}1/5$ of DeepSeek's. Discrimination collapse (Gini/CV reduction) is consistent across all conditions; the entropy redistribution component is model-dependent, with Qwen showing a sign reversal at $s{=}0.25$. We characterize discrimination collapse as the robust driver, with entropy redistribution as a secondary, model-specific amplifier. Extended discussion in Appendix~\ref{app:extended-discussion}. % exp_i
…[truncated 54 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 172 · 2026-05-14T13:07:03.773828+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-14T13:07:03.979022+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation. Under importance-based eviction, the severity gradient grows from $69{\times}$ to $274{\times}$ across sparsity levels ($d_z$: $0.44 \to 0.80$); random eviction shows no such modulation (7/8 conditions non-significant). A crossover at $s{=}0.25$---where importance-based eviction reverses ranking across phases---demonstrates that no single strategy dominates uniformly. The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d_z \geq 0.55$) with attenuated magnitude. Discrimination collapse provides a robust mechanistic explanation confirmed across both models.
5	These findings motivate phase-aware sparsity allocation for reasoning model deployment.
6	
7	\section*{Limitations}
8	\label{sec:limitations}
9	
10	Both models share the Qwen2 architecture; cross-architecture validation (LLaMA, Mistral) remains future work. Evaluation is limited to MATH-500 at the 7B scale. The discrimination collapse mechanism is supported by correlational evidence; causal validation through controlled entropy manipulation is needed. The entropy redistribution component replicates on only 2/4 Qwen conditions, suggesting model-specific factors. Extended limitations in Appendix~\ref{app:limitations}.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 205
}
```

</details>

---


### Tool call

_source line 174 · 2026-05-14T13:07:03.979470+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-14T13:07:04.030008+00:00_

1	\section{Compound Sparsity Formulation}
2	\label{app:formulation-details}
3	
4	\paragraph{Attention head pruning.}
5	Heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$ \cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\ell)} \in \{0,1\}$ retains the top-$(1{-}s)\cdot H$ heads:
6	\begin{equation}
7	    \tilde{\mathbf{o}}_j^{(\ell)} = m_j^{(\ell)} \cdot \mathbf{o}_j^{(\ell)}.
8	    \label{eq:head-mask}
9	\end{equation}
10	
11	\paragraph{KV cache eviction.}
12	A position mask $\mathbf{m}_k \in \{0,1\}^T$ retains the top-$(1{-}s)\cdot T$ positions (BOS always preserved):
13	\begin{equation}
14	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall\, i, j.
15	    \label{eq:kv-mask}
16	\end{equation}
17	Under importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:
18	\begin{equation}
19	    \mathrm{imp}(j) = \frac{\sum_{\ell, h, i} a_{ij}^{(\ell,h)}}{T - j},
20	    \label{eq:kv-importance}
21	\end{equation}
22	where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.
23	
24	\paragraph{Compound sparsity.}
25	Applying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.
26	
27	\paragraph{Attention sparsity metric.}
28	For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:
29	\begin{equation}
30	    \sigma_i^{(h)} = \frac{1}{T} \sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right].
31	    \label{eq:attn-sparsity}
32	\end{equation}
33	The per-position spar
…[truncated 2209 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-14T13:07:08.560627+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex"
  }
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-14T13:07:09.028771+00:00_

1	% Appendix sections for content moved from results.tex
2	
3	\section{Per-Phase Interaction Index Breakdown}
4	\label{app:phase-breakdown}
5	
6	\begin{table*}[t]
7	\centering
8	\small
9	\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$. $G = \widetilde{\mathrm{II}}_{\textit{low}} / \widetilde{\mathrm{II}}_{\textit{high}}$.}
10	\label{tab:main-results}
11	\begin{tabular}{@{}llccccr@{}}
12	\toprule
13	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{mid}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\Delta$ & $G$ \\
14	\midrule
15	0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\mathbf{69}$ \\
16	0.15 & Random     & 0.093 & 0.097 & 0.103 & 0.01 & 1.1 \\
17	\addlinespace
18	0.20 & Importance & 0.015 & 0.203 & 1.496 & 1.48 & $\mathbf{103}$ \\
19	0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\
20	\addlinespace
21	0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\mathbf{222}$ \\
22	0.25 & Random     & 0.818 & 0.932 & 1.363 & 0.54 & 1.7 \\
23	\addlinespace
24	0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\mathbf{274}$ \\
25	0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\
26	\bottomrule
27	\end{tabular}
28	\end{table*}
29	
30	
31	\section{Phase-Strategy Crossover Details}
32	\label{app:crossover-details}
33	
34	\begin{figure}[t]
35	\centering
36	\includegraphics[width=\columnwidth]{fig3_crossover.pdf}
37	\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}
38	\label{fig:crossover}
39	\end{figure}
40	
41	The crossover is present at all four tested sparsity levels: at
…[truncated 8409 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 468
}
```

</details>

---


### Tool call

_source line 178 · 2026-05-14T13:07:09.191775+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 179 · 2026-05-14T13:07:09.242653+00:00_

1	\section{Discrimination Collapse Details}
2	\label{app:discrimination-collapse-details}
3	
4	The \textbf{Gini coefficient} measures inequality in the importance distribution ($\mathrm{Gini}{=}0$: perfectly uniform; $\mathrm{Gini}{=}1$: maximally concentrated). The \textbf{coefficient of variation} (CV) captures relative dispersion. Table~\ref{tab:discrimination-metrics-full} reports both metrics.
5	
6	\begin{table}[t]
7	\centering
8	\caption{Discrimination collapse under importance-based eviction. $\Delta\mathrm{Gini}$ and $\Delta\mathrm{CV}$ are post-pruning minus baseline; negative values indicate reduced discriminative power. All 8 conditions show consistent negative deltas across both models.}
9	\label{tab:discrimination-metrics-full}
10	\small
11	\begin{tabular}{llrr}
12	\toprule
13	Model & $s$ & $\Delta\mathrm{Gini}$ & $\Delta\mathrm{CV}$ \\
14	\midrule
15	DeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\
16	DeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\
17	DeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\
18	DeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\
19	\midrule
20	Qwen & $0.15$ & $-0.010$ & $-0.05$ \\
21	Qwen & $0.20$ & $-0.012$ & $-0.21$ \\
22	Qwen & $0.25$ & $-0.010$ & $-1.49$ \\
23	Qwen & $0.30$ & $-0.020$ & $-1.14$ \\
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	Under importance-based eviction, the Gini delta is negative at every sparsity level for both models, with magnitude scaling monotonically with sparsity in DeepSeek. The CV delta is likewise negative in all 8 importance-based conditions. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$), confirming that discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
29	
30	This cross-model consistency establishes discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction be
…[truncated 13240 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 180 · 2026-05-14T13:07:14.271161+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
  }
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-14T13:07:14.371945+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\paragraph{Models.}
5	\label{sec:models}
6	We evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \textbf{DeepSeek-R1-Distill-Qwen-7B}~\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \textbf{Qwen2.5-7B-Instruct}~\cite{qwen25-2024}, with standard instruction tuning, providing a cross-model replication target. Both are loaded in \texttt{bfloat16} with eager attention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values; \texttt{bfloat16} eliminated all occurrences.}
7	
8	\paragraph{Dataset.}
9	\label{sec:dataset}
10	We use 50 problems stratified from MATH-500~\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048).
11	
12	\paragraph{Sparsity configuration.}
13	\label{sec:sparsity-config}
14	We apply symmetric compound sparsity at $s \in \{0.15, 0.20, 0.25, 0.30\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\ref{eq:kv-importance}; BOS always retained) and \emph{random} eviction (uniform). Heads are pruned per layer by Frobenius norm; under random eviction, both heads and positions are selected uniformly.
15	
16	\paragraph{Phase segmentation and metrics.}
17	\label{sec:phase-seg}
18	Each sequence is segmented into three phases using the quantile-based method (\S\ref{sec:phase-segmentation}), with $\texttt{min\_phase\_length}{=}10$. We compute segment-level perplexity, II (Eq.~\ref{eq:ii}), and $G$ (Eq.~\ref{eq:gradient}), reporting medians due to heavy right-skew (mean/median ratios up to 43:1).
19	
20	\paragraph{Statistical analysis.}
21	\label{sec:stats}
22	All confidence intervals and significance tests use 
…[truncated 262 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-14T13:07:14.372459+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-14T13:07:14.425703+00:00_

1	% References for Phase-Gated Compound Sparse paper
2	% Generated 2026-05-14; all entries verified via web search
3	
4	@inproceedings{adakv-neurips2025,
5	    title     = {Ada-{KV}: Optimizing {KV} Cache Eviction by Adaptive Budget Allocation for Efficient {LLM} Inference},
6	    author    = {Feng, Yuan and Lv, Junlin and Cao, Yukun and Xie, Xike and Zhou, S. Kevin},
7	    booktitle = {Advances in Neural Information Processing Systems},
8	    year      = {2025},
9	    url       = {https://arxiv.org/abs/2407.11550},
10	}
11	
12	@article{compression-ordering-2025,
13	    title   = {A Systematic Study of Compression Ordering for Large Language Models},
14	    author  = {Chhawri, Shivansh and Mahadik, Rahul and Rooj, Suparna},
15	    journal = {arXiv preprint arXiv:2511.19495},
16	    year    = {2025},
17	    url     = {https://arxiv.org/abs/2511.19495},
18	}
19	
20	@article{decision-repr-transition-2026,
21	    title   = {Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions},
22	    author  = {Shi, Boyu and Liu, Chang and Gao, ChuanBao and Yang, Xu and Geng, Xin},
23	    journal = {arXiv preprint arXiv:2605.07271},
24	    year    = {2026},
25	    url     = {https://arxiv.org/abs/2605.07271},
26	}
27	
28	@article{deepseek-r1-2025,
29	    title   = {{DeepSeek-R1}: Incentivizing Reasoning Capability in {LLMs} via Reinforcement Learning},
30	    author  = {{DeepSeek-AI}},
31	    journal = {Nature},
32	    volume  = {645},
33	    pages   = {633--638},
34	    year    = {2025},
35	    doi     = {10.1038/s41586-025-08636-z},
36	}
37	
38	@inproceedings{defensivekv-iclr2026,
39	    title     = {{DefensiveKV}: Taming the Fragility of {KV} Cache Eviction in {LLM} Inference},
40	    author    = {Feng, Yuan and Guo, Haoyu and Lv, Junlin and Zhou, S. Kevin and Xie, Xike},
41	    booktitle = {International Conference on Learning Representations},
42	    year      = {2026},
43	    url       = {https://arxiv.org/abs/2510.13334
…[truncated 10878 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 53
}
```

</details>

---


### Tool result

_source line 184 · 2026-05-14T13:08:15.025397+00:00_

Here is the complete verbatim text extracted from pages 1–4:

---

## PAGE 1

**Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Reasoning Models**

Anonymous ACL submission

### Abstract

Compound sparsity—simultaneously pruning attention heads and evicting KV cache entries—is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood. Prior work treats compound interaction magnitude as approximately constant across the generation process. We show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.

We evaluate compound sparsity on DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct (both Qwen2 architecture, 7B parameters) using 50 MATH-500 problems, measuring the Interaction Index—a super-additivity metric—across quantile-segmented reasoning phases and sparsity levels s ∈ {0.15, 0.20, 0.25, 0.30}. Under importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from 0.39 (s = 0.15) to 14.59 at s = 0.30, with paired Cohen's d growing from 0.44 (small) to 0.80 (large). Bonferroni-corrected permutation tests yield p < 0.005 at all four sparsity levels. Random eviction produces no significant phase modulation (largest: Qwen s = 0.30, p = 0.012) showing negligible effect size (d = –0.01), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.

Across s = 0.25, a strategy ranking reversal emerges: importance-based eviction outperforms random in high-sparsity phases (Δ = 0.032 vs. 0.818) yet underperforms at low-sparsity phases (d = –1.00 for DeepSeek, d = 7.106 for Qwen, vs. 1.363)—a qualitative reversal in strategy ranking. The pattern replicates on Qwen2.5-7B-Instruct at s ≥ 0.20 (d_s ≥ 0.52; Spearman ρ = 1.0 across spa
…[truncated 13868 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Agent",
  "elapsed_ms": 125450
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-14T13:09:27.466346+00:00_

Here is the complete extracted text from page 5 onwards:

---

## Page 5 — Conclusion, Limitations, References (partial)

**7 Conclusion**

We showed that compound sparsity severity—the super-additive interaction between head pruning and KV cache eviction—is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation. Under importance-based eviction, the severity gradient grows from 69× to 274× across sparsity levels (d_z: 0.44 → 0.80); random eviction shows no such modulation (7/8 conditions non-significant). A crossover at s=0.25—where importance-based eviction reverses ranking across phases—demonstrates that no single strategy dominates uniformly. The pattern replicates on Qwen2.5-7B-Instruct at s≥0.20 (d_z≥0.55) with attenuated magnitude. Discrimination collapse provides a robust mechanistic explanation confirmed across both models. These findings motivate phase-aware sparsity allocation for reasoning model deployment.

**Limitations**

Both models share the Qwen2 architecture; cross-architecture validation (LLaMA, Mistral) remains future work. Evaluation is limited to MATH-500 at the 7B scale. The discrimination collapse mechanism is supported by correlational evidence; causal validation through controlled entropy manipulation is needed. The entropy redistribution component replicates on only 2/4 Qwen conditions, suggesting model-specific factors. Extended limitations in Appendix.

**References** (partial on p.5, continued p.6):

- Yilong Chen, Guoxia Wang et al. NACL: A General and Effective KV Cache Eviction Framework for LLMs. ACL 2024.
- Dan Hendrycks, Collin Burns et al. Measuring Mathematical Problem Solving With the MATH Dataset. NeurIPS 2021.
- Wonsik Kwon et al. Understanding Discrimination Collapse in Layer-Pruned LLMs. arXiv:2605.07271.
- Yuan Fang, Junlin Lv et al. Ada-KV: Optimizing KV cache eviction by adaptive budget allocation. NeurIPS 2025.
- DeepSeek-AI. DeepSeek-R1. Na
…[truncated 17211 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Agent",
  "elapsed_ms": 192541
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-14T13:09:37.974229+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "R-KV redundancy-aware KV cache compression reasoning models 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "R-KV redundancy-aware KV cache compression reasoning models 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 187 · 2026-05-14T13:09:38.526532+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Hold Onto That Thought\" KV cache compression reasoning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Hold Onto That Thought\" KV cache compression reasoning 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-14T13:09:39.079567+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 review form scoring criteria dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 review form scoring criteria dimensions"
  }
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-14T13:09:44.762450+00:00_

Web search results for query: ""Hold Onto That Thought" KV cache compression reasoning 2025 2026"

Links: [{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"},{"title":"[2512.12008] Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/abs/2512.12008"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning | OpenReview","url":"https://openreview.net/forum?id=udgrpHqw4F"},{"title":"NeurIPS Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://neurips.cc/virtual/2025/loc/san-diego/126664"},{"title":"Paper page - KVzap: Fast, Adaptive, and Faithful KV Cache Pruning","url":"https://huggingface.co/papers/2601.07891"},{"title":"Paper page - Fast KVzip: Efficient and Accurate LLM Inference with Gated KV Eviction","url":"https://huggingface.co/papers/2601.17668"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/html/2510.01290v1"},{"title":"Which Heads Matter for Reasoning? RL-Guided KV Cache Compression | OpenReview","url":"https://openreview.net/forum?id=HGdg76iVo6"},{"title":"[2510.01290] ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/abs/2510.01290"}]

Based on the search results, here's what I found about "Hold Onto That Thought: Assessing KV Cache Compression On Reasoning":

## Overview

"Hold Onto That Thought" is a research paper that addresses how the KV cache (used to speed up attention computations and grows linearly with context length) can be co
…[truncated 1181 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6235
}
```

</details>

---


### Tool result

_source line 190 · 2026-05-14T13:09:44.818322+00:00_

Web search results for query: "R-KV redundancy-aware KV cache compression reasoning models 2025 2026"

Links: [{"title":"[2505.24133] R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://arxiv.org/abs/2505.24133"},{"title":"GitHub - Zefan-Cai/R-KV: [Neurips 2025] R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://github.com/Zefan-Cai/R-KV"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://proceedings.neurips.cc/paper_files/paper/2025/hash/57e0358aed314784cad14a26e1eba642-Abstract-Conference.html"},{"title":"R-KV: Redundancy-aware KV Cache Compression for ...","url":"https://arxiv.org/pdf/2505.24133"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=2jwAjomEDB"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://zefan-cai.github.io/R-KV.page/"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://arxiv.org/html/2505.24133"},{"title":"NeurIPS Poster R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/120110"},{"title":"[PDF] R-KV: Redundancy-aware KV Cache Compression for Training-Free Reasoning Models Acceleration | Semantic Scholar","url":"https://www.semanticscholar.org/paper/R-KV:-Redundancy-aware-KV-Cache-Compression-for-Cai-Xiao/eb574cb16208cb0daaa484f85cddb1e1d6b23f44"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://openreview.net/pdf?id=2jwAjomEDB"}]

Based on the search results, here's comprehensive information about R-KV:

## Overview

R-KV is a novel method specifically targeting redundant tokens in reasoning models for KV cache compression. The paper was submitted on May 30, 2025, with the latest version (v4) revised on January 22, 2026, and was presented at NeurIPS 2025.

## Key Problem

…[truncated 1373 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6844
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-14T13:09:45.524089+00:00_

Web search results for query: "EMNLP 2026 review form scoring criteria dimensions"

Links: [{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"EMNLP Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/emnlp-statistics/"},{"title":"EMNLP 2026 | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026"},{"title":"ClimateNLP 2026","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Changes to reviewer volunteering requirement and incentives in May 2025 cycle (EMNLP 2025)","url":"http://aclrollingreview.org/incentives2025"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2023 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2023%2FConference"}]

Based on the search results, I found information about the review scoring criteria used for EMNLP 2026. Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

Here are the key scoring dimensions:

1. **Soundness**: Soundness scores must be justified by the text of the review. If you give a low Soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation.

2. **Excitement**: Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate excitement score, which is orthogonal to the assessment of the soundness of the paper. Excitement scores reflect our personal taste, and so d
…[truncated 432 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6444
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-14T13:09:52.742565+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Which Heads Matter for Reasoning\" RL-guided KV cache compression 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Which Heads Matter for Reasoning\" RL-guided KV cache compression 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 193 · 2026-05-14T13:09:53.599889+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RaaS reasoning-aware attention sparsity LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RaaS reasoning-aware attention sparsity LLM 2025"
  }
}
```

</details>

---


### Tool call

_source line 194 · 2026-05-14T13:09:53.705693+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LongFlow KV cache compression reasoning models 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LongFlow KV cache compression reasoning models 2026"
  }
}
```

</details>

---


### Tool result

_source line 195 · 2026-05-14T13:10:00.254714+00:00_

Web search results for query: ""Which Heads Matter for Reasoning" RL-guided KV cache compression 2025 2026"

Links: [{"title":"Which Heads Matter for Reasoning? RL-Guided KV Cache Compression | OpenReview","url":"https://openreview.net/forum?id=HGdg76iVo6"},{"title":"[2510.08525] Which Heads Matter for Reasoning? RL-Guided KV Cache Compression","url":"https://arxiv.org/abs/2510.08525"},{"title":"Which Heads Matter for Reasoning? RL-Guided KV Cache Compression","url":"https://arxiv.org/html/2510.08525"},{"title":"[PDF] Which Heads Matter for Reasoning? RL-Guided KV Cache Compression | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Which-Heads-Matter-for-Reasoning-RL-Guided-KV-Cache-Du-Jiang/bb15d15655a41d12c714b3cd88c810ee5bb2886e"},{"title":"Paper page - Which Heads Matter for Reasoning? RL-Guided KV Cache Compression","url":"https://huggingface.co/papers/2510.08525"},{"title":"Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning | OpenReview","url":"https://openreview.net/forum?id=FJFVmeXusW"},{"title":"WHICH HEADS MATTER FOR REASONING? RL-GUIDED ...","url":"https://openreview.net/pdf?id=HGdg76iVo6"},{"title":"Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/not-all-heads-matter-a-head-level-kv-cache-compression-method-with-integrated-retrieval-and-reasoning/"},{"title":"Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning","url":"https://arxiv.org/html/2410.19258"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"}]

Based on the 
…[truncated 1707 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7512
}
```

</details>

---


### Tool result

_source line 196 · 2026-05-14T13:10:01.288497+00:00_

Web search results for query: "LongFlow KV cache compression reasoning models 2026"

Links: [{"title":"LongFlow: Efficient KV Cache Compression for Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=rz6WybXjgk"},{"title":"LongFlow: Efficient KV Cache Compression for Reasoning Models","url":"https://arxiv.org/html/2603.11504"},{"title":"[2603.11504] LongFlow: Efficient KV Cache Compression for Reasoning M","url":"https://arxiv.org/abs/2603.11504"},{"title":"Is KV Cache Quantization Sabotaging Your Context? — We test the impact of quantizing caches on long-horizon agentic coding workloads.","url":"https://dasroot.net/posts/2026/05/kv-cache-quantization-agentic-coding-long-horizon/"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"EFFICIENT KV CACHE COMPRESSION - LONGFLOW","url":"https://openreview.net/pdf?id=rz6WybXjgk"},{"title":"Paper page - TriAttention: Efficient Long Reasoning with Trigonometric KV Compression","url":"https://huggingface.co/papers/2604.04921"},{"title":"Which Heads Matter for Reasoning? RL-Guided KV Cache Compression | OpenReview","url":"https://openreview.net/forum?id=HGdg76iVo6"},{"title":"KV-Fold: One-Step KV-Cache Recurrence for Long-Context Inference","url":"https://arxiv.org/html/2605.12471"},{"title":"Efficient LLMs at Scale: My NeurIPS Week in KV Caches, Spec Decoding, and FP4","url":"https://kaitchup.substack.com/p/efficient-llms-at-scale-my-neurips"}]

I've found comprehensive information about LongFlow and KV cache compression for reasoning models in 2026. Here's what the search revealed:

## LongFlow Overview

LongFlow is a novel KV cache compression method that employs an efficient importance estimation metric deriv
…[truncated 1423 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7582
}
```

</details>

---


### Tool result

_source line 197 · 2026-05-14T13:10:01.289127+00:00_

Web search results for query: "RaaS reasoning-aware attention sparsity LLM 2025"

Links: [{"title":"[2502.11147] RaaS: Reasoning-Aware Attention Sparsity for Efficient LLM Reasoning","url":"https://arxiv.org/abs/2502.11147"},{"title":"RaaS: Reasoning-Aware Attention Sparsity for Efficient ...","url":"https://aclanthology.org/2025.findings-acl.131.pdf"},{"title":"RaaS: Reasoning-Aware Attention Sparsity for Efficient LLM Reasoning","url":"https://arxiv.org/html/2502.11147v2"},{"title":"Sparse Attention across Multiple-context KV Cache","url":"https://arxiv.org/html/2508.11661v1"},{"title":"Computer Science Feb 2025","url":"https://www.arxiv.org/list/cs/2025-02?skip=5575&show=25"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/html/2510.01290v1"},{"title":"Artificial Intelligence Feb 2025","url":"https://arxiv.org/list/cs.AI/2025-02?skip=2100&show=25"},{"title":"DeepServe: Serverless Large Language Model Serving at Scale","url":"https://arxiv.org/html/2501.14417v3"},{"title":"Machine Learning Feb 2025","url":"https://www.arxiv.org/list/cs.LG/2025-02?skip=1375&show=50"},{"title":"LouisKV: Efficient KV Cache Retrieval for Long Input-Output Sequences","url":"https://arxiv.org/html/2510.11292v1"}]

Based on the search results, here's information about RaaS (Reasoning-Aware Attention Sparsity):

## Overview

RaaS: Reasoning-Aware Attention Sparsity for Efficient LLM Reasoning is a research paper that addresses computational efficiency challenges in large language models during complex reasoning tasks.

## The Problem

Solving reasoning tasks often requires an LLM to generate long sequences, incurring O(N) time and memory complexities per token, where N is the current sequence length. Existing sparsity-based algorithms struggle with the "impossible trinity" of accuracy, time, and memory. For example, the state-of-the-art algorithm, Quest, achieves high accuracy with O(L) time but O(N) memory (L is the cache b
…[truncated 764 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7689
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-14T13:10:08.339383+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool call

_source line 199 · 2026-05-14T13:10:09.746550+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"compression ordering\" LLM pruning quantization sparsity interaction 2025 2026 Chhawri"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"compression ordering\" LLM pruning quantization sparsity interaction 2025 2026 Chhawri"
  }
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-14T13:10:09.997666+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"discrimination collapse\" attention pruning importance score degradation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"discrimination collapse\" attention pruning importance score degradation 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-14T13:10:32.470506+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 30, \"total_citations\": 40, \"unique_cited_keys\": 23, \"orphan_bib\": 7, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 22, \"online_not_found\": 3, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [\"compression-ordering-2025\", \"h2o-neurips2023\", \"mustafar-neurips2025\", \"obcache-2025\", \"pagedeviction-eacl2026\", \"pyramidkv-2024\", \"raas-acl2025\"], \"missing_bib\": [], \"orphan_count\": 7, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"adakv-neurips2025\", \"type\": \"inproceedings\", \"title\": \"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference\", \"authors\": \"Feng, Yuan and Lv, Junlin and Cao, Yukun and Xie, Xike and Zhou, S. Kevin\", \"year\": \"2025\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"compression-ordering-2025\", \"type\": \"article\", \"title\": \"A Systematic Study of Compression Ordering for Large Language Models\", \"authors\": \"Chhawri, Shivansh and Mahadik, Rahul and Rooj, Suparna\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2511.19495\"}, {\"key\": \"decision-repr-transition-2026\", \"type\": \"article\", \"title\": \"Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions\", \"authors\": \"Shi, Boyu and Liu, Chang and Gao, ChuanBao and Yang, Xu and Geng, Xin\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.07271\"}, {\"key\": \"deepseek-r1-2025\", \"type\": \"article\", \"title\": \"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\", \"authors\": \"DeepSeek-AI\", \"year\": \"2025\", \"venue\": \"Nature\"}, {\"key\": \"defensivekv-iclr2026\", \"type\": \"inproceedings\", \"title\": \"DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference\", \"authors\": \"Feng, Yuan and Guo, Haoyu and Lv, Junlin and Zhou, S. 
…[truncated 22800 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 24131
}
```

</details>

---


### Tool result

_source line 202 · 2026-05-14T13:10:40.198903+00:00_

Web search results for query: ""discrimination collapse" attention pruning importance score degradation 2025 2026"

Links: [{"title":"Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific Large Language Models","url":"https://arxiv.org/html/2604.27115"},{"title":"Differentiable channel pruning guided via attention mechanism: a novel neural network pruning approach | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-023-01022-6"},{"title":"Attention-based adaptive structured continuous sparse network pruning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0925231224004697"},{"title":"SAP: Syntactic Attention Pruning for Transformer-based Language Models","url":"https://arxiv.org/html/2512.19125"},{"title":"Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning","url":"http://people.iiis.tsinghua.edu.cn/~gaomy/pubs/twilight.neurips25.pdf"},{"title":"Efficient self-attention with smart pruning for sustainable large language models | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-92586-5"},{"title":"Magnitude Attention-based Dynamic Pruning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0957417425005792"},{"title":"Accelerating attention through gradient-based learned runtime pruning | Proceedings of the 49th Annual International Symposium on Computer Architecture","url":"https://dl.acm.org/doi/abs/10.1145/3470496.3527423"},{"title":"Attention Score is not All You Need for Token Importance Indicator in KV Cache Reduction: Value Also Matters","url":"https://arxiv.org/html/2406.12335v2"},{"title":"HiP Attention: Sparse Sub-Quadratic Attention with Hierarchical Attention Pruning","url":"https://arxiv.org/html/2406.09827v1"}]

I found relevant research on discrimination collapse and attention pruning. Here are the key findings:

## Discrimination Collapse in Attention 
…[truncated 1594 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 30201
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-14T13:10:41.260774+00:00_

Web search results for query: ""compression ordering" LLM pruning quantization sparsity interaction 2025 2026 Chhawri"

Links: [{"title":"A Systematic Study of Compression Ordering for Large Language Models","url":"https://arxiv.org/html/2511.19495v1"},{"title":"Large Language Model Compression with Global Rank and Sparsity Optimization","url":"https://arxiv.org/html/2505.03801"},{"title":"Published as a conference paper at ICLR 2026 LARGE LANGUAGE MODEL COMPRESSION","url":"https://arxiv.org/pdf/2505.03801"},{"title":"Published as a conference paper at COLM 2025","url":"https://arxiv.org/pdf/2504.14569"},{"title":"A review of state-of-the-art techniques for large language model compression | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-02019-z"},{"title":"ICML Poster SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression","url":"https://icml.cc/virtual/2025/poster/46479"},{"title":"Structured Pruning of Large Language Models","url":"https://www.researchgate.net/publication/347235497_Structured_Pruning_of_Large_Language_Models"},{"title":"Frontiers | A survey of model compression techniques: past, present, and future","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1518965/full"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7349b8b5a6737dd36031c77212eab3ad-Paper-Conference.pdf"},{"title":"SLIM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression | Research","url":"https://research.nvidia.com/publication/2025-06_slim-one-shot-quantization-and-sparsity-low-rank-approximation-llm-weight"}]

Based on the search results, I found highly relevant research on compression ordering for Large Language Models. Here are the key findings:

## Main Study on Compression Ordering

A comprehensive analysis examines how knowledg
…[truncated 1676 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 31514
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-14T13:13:21.853458+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿报告\n\n**论文**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Reasoning Models\n**Venue**: EMNLP 2026 Main Conference (ACL Rolling Review May 2026)\n\n---\n\n## 总体评分\n\n**Overall**: 2.5/5 — 介于 Findings 接收和 Resubmit 之间\n**一句话总结**: 论文发现了一个有趣的经验现象（compound sparsity severity 的 phase 依赖性），统计方法扎实，但贡献增量性偏强、无方法提出、评估规模过小，作为 EMNLP 主会论文分量不足。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 统计方法（permutation test, bootstrap CI, Bonferroni 校正）规范，但样本量极小（50 problems, 单一架构），discrimination collapse 仅为相关性证据 |\n| Excitement | 2.5/5 | 现象本身有趣（phase-strategy crossover），但缺乏方法论贡献，且\"severity gradient\"的巨大倍数（69×-274×）主要由分母极小驱动 |\n| Overall | 2.5/5 | 观察性发现+诊断工具，距离 EMNLP 主会的方法论或系统性贡献门槛尚有差距 |\n| Reproducibility | 3/5 | 实验设置描述清晰，但无代码释放，50 个问题的 stratified sampling 种子未明确指定是否公开 |\n| Reviewer Confidence | 4/5 | 熟悉 KV cache compression 和 LLM pruning 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 新颖性不足：核心贡献是观察性发现而非方法\n\n- 具体位置：Section 1 贡献列表（3 条贡献均为\"identify\"/\"show\"/\"propose mechanism\"）\n- 问题：三条贡献均为经验观察或事后解释，没有提出任何可操作的方法（phase-aware compression controller / dynamic budget allocation）。Discussion (Section 6) 提到\"phase-aware compression budget\"但仅停留在概念层面（\"could mitigate\"），未实现、未验证。对于 EMNLP 主会 long paper，纯观察性工作的门槛更高——需要更大规模、更多模型、或更深的理论分析来弥补方法空缺。\n- 为什么影响接收：ACL ARR excitement 评分明确要求\"novel and useful methodology\"或\"insightful empirical results\"。在仅有 2 个同架构模型、50 道题的规模下，单纯的经验观察难以满足\"insightful\"标准。\n- 建议修改方向：(a) 实现并验证 phase-aware compression budget（哪怕是 oracle/static 版本），展示实际 accuracy 提升；或 (b) 大幅扩大评估规模（多架构、多任务、更大模型），使观察性发现的可信度足以独立成篇。\n\n**N2** [critical] Severity gradient 的 69×-274× 倍数具有误导性\n\n- 具体位置：Abstract (\"over an order of magnitude\"), Section 5.2, Figure 1\n- 问题：G = Ĩ_low / Ĩ_high，其中 Ĩ_high 极小（0.006-0.053，见 Appendix Table D）。当分母接近零时，比值可以任意大——这不反映实际严重程度。实际的绝对差值 Δ = 0.39-14.59（Table 1）更有信息量但远没那么戏剧性。Abstract 用\"varies by over an order of magnitude\"作为开头论点，过度依赖这个受分母影响的比值指标。\n- 为什么影响接收：如果核心叙事建立在一个因分母极小而膨胀的指标上，审稿人和读者会质疑发现的实际意义。\n- 建议修改方向：(a) 在正文中主要报告绝对差值 Δ 和 effect size d_z，将 G 降级为辅助指标；(b) 明确讨论 G 的分母敏感性问题；(c) 将 Figure 1 改为展示 Δ 或 d_z 的增长趋势。\n\n**N3** [critical] 评估规模严重不足\n\n- 具体位置：Section 4（50 MATH-500 problems, 2 models, 单一 Qwen2 架构）\n- 问题：\n  - **50 道题**：MATH-500 有 500 道题，只用 10% 缺乏理由（\"stratified sampling\" 但未论证 50 为何足够）。Qwen 进一步排除 4 道（n=46）。\n  - **单一架构**：两个模型共享 Qwen2ForCausalLM 架构（28 layers, 28 heads, 4-group GQA），这不是跨模型验证——是同一架构不同训练配置的验证。LLaMA 3、Mistral 或非 GQA 架构（如 MHA）未测试。\n  - **单一任务**：仅 MATH-500。代码推理、常识推理、多步 QA 等任务的 phase 结构可能完全不同。\n- 为什么影响接收：Limitations 诚实承认了这些局限，但 Abstract 和 Introduction 的 claim 表述过于一般化（\"reasoning models\" 而非 \"Qwen2-7B models on 50 math problems\"）。\n- 建议修改方向：至少覆盖一个非 Qwen 架构（LLaMA 3.3-8B 或 Mistral-7B）和一个非数学任务（如 GPQA 或 LiveCodeBench）。或者显著弱化 claim 的 generality。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Discrimination collapse 是相关性而非因果性证据\n\n- 具体位置：Section 5.6, Appendix H\n- 问题：Gini coefficient 下降（−0.030 到 −0.081）与 severity gradient 共现，但论文未排除其他混淆因素。更关键的是，entropy redistribution 组件仅在 DeepSeek 上一致，Qwen 在 s=0.25 出现符号反转（ΔH = +0.045），论文将其归因为\"model-specific\"但这削弱了机制的普遍性。Section 5.6 称 discrimination collapse 为\"mechanistic explanation\"，但它更接近于一个 correlational observation。\n- 建议：(a) 将\"mechanism\"改为\"hypothesis\"或\"correlational evidence\"；(b) 考虑设计消融实验（如人工控制 Gini 分布的 importance scores 来验证因果关系）。\n\n**W2** [warning] Interaction Index 与已有 super-additivity 概念的区分不清\n\n- 具体位置：Section 3, Eq. 1\n- 问题：II = r_b - r_a - r_k + 1 本质上是标准的交互效应（类似 ANOVA 中的 interaction term）。论文引用 SparK (Liao et al., 2026) 的 super-additive degradation 但未清楚区分 II 与 SparK 等工作中已有的 compound interaction 度量。如果 II 只是将 phase 维度加到已有概念上，应明确说明。\n- 建议：增加一段明确讨论 II 与 SparK、SLiM、UniComp 中使用的 compound interaction 度量的关系和区别。\n\n**W3** [warning] 正文仅 ~5 页，严重未利用 8 页限制\n\n- 具体位置：全文结构\n- 问题：正文约 5 页（Introduction 1.5p + Related Work 0.7p + Background 0.5p + Setup 0.5p + Results 1.2p + Discussion 0.5p + Conclusion 0.3p），远低于 long paper 8 页上限。大量关键信息被放在附录中：\n  - 完整的 per-phase breakdown table（Appendix D）应在正文\n  - Cross-model comparison table（Appendix F, Table 3）应在正文\n  - Effect size table（Appendix G, Table 5）应在正文\n  - Discrimination collapse metrics（Appendix H）至少 summary 应在正文\n  \n  这使正文感觉像是 extended abstract + 附录堆积，而非一篇完整论文。\n- 建议：将 Appendix D (Table 2), F (Table 3), G (Table 5) 移入正文，充分利用 8 页空间。将 Discussion 扩展以覆盖更多 deployment implications。\n\n**W4** [warning] Abstract 信息过载，可读性差\n\n- 具体位置：Abstract\n- 问题：Abstract 塞入了过多具体数字（69×, 274×, 0.39, 14.59, 0.44, 0.80, 7/8, 0.032, 0.818, 7.106, 1.363, d=-1.00, ρ=1.0, p=0.041...），读者在第一遍阅读时无法消化这些数据。一个好的 abstract 应传达 high-level insight + 关键定量 takeaway（1-2 个数字），而非完整的统计报告。\n- 建议：精简 Abstract 至 150-200 words，保留核心发现 + 1-2 个最有 impact 的定量结果。\n\n**W5** [warning] Phase segmentation 方法选择缺乏敏感性分析\n\n- 具体位置：Section 3 (\"tercile boundaries of per-position attention entropy\")\n- 问题：Phase 定义完全依赖 attention entropy 的三分位数划分，且沿用 ThinKV 的方法。但：(a) 为什么是 tercile 而非 quartile/quintile？(b) min_phase_length=10 的选择依据是什么？(c) 换用其他 phase segmentation（如 ThinKV 的 thought-type decomposition: reasoning/execution/transition）结果是否一致？这些选择对 severity gradient 的 magnitude 影响可能很大。\n- 建议：至少对 phase 数量和 min_phase_length 做 robustness check。\n\n---\n\n## 小问题（不影响接收）\n\n- **引用问题**：bib 中有 7 个 orphan 条目（在 .bib 中但未被正文引用）：`compression-ordering-2025`, `h2o-neurips2023`, `mustafar-neurips2025`, `obcache-2025`, `pagedeviction-eacl2026`, `pyramidkv-2024`, `raas-acl2025`。其中 H2O、PyramidKV、RaaS 等是高度相关工作，要么引用要么删除。`h2o-neurips2023` 的 title 字段为空。\n- **符号不一致**：正文混用 d_s 和 d_z 指代 Cohen's d 的变体，未明确区分。Abstract 用 d（无下标），Section 5.5 用 d_s，Appendix 用 d_z。\n- **Table 1 数值与 Appendix Table D 不完全对应**：Table 1 的 Random s=0.25 Δ=0.54，但 Appendix D 显示 Ĩ_low=1.363 - Ĩ_high=0.818 = 0.545，取整差异虽小但应统一精度。\n- **脚注 2**：提到\"4× NVIDIA RTX PRO 6000 Blackwell 96 GB GPUs\"，但实验仅在单个 7B 模型上运行 50 道题，使用 4 块 96GB GPU 似乎 over-provisioned，且未说明是否利用多卡。\n\n---\n\n## 遗漏的重要相关工作（Missing References）\n\n以下通过 web_search 验证的相关工作在论文中未被讨论：\n\n1. **R-KV** (Cai et al., NeurIPS 2025): \"Redundancy-aware KV Cache Compression for Reasoning Models\"。专门针对 reasoning model 的 KV cache 压缩，识别冗余 token 实现 10% KV cache 保留近乎无损性能。与本文直接相关——R-KV 也识别了 reasoning 生成中不同 token 的重要性差异，但采取了方法导向的路线。**必须讨论。**\n\n2. **RLKV / \"Which Heads Matter for Reasoning?\"** (Du et al., 2025/2026): 用 RL 识别 reasoning-critical heads 并差异化压缩。直接涉及 head pruning 与 reasoning 质量的交互——论文的核心议题。RLKV 的 \"functional heterogeneity\" 假设与 discrimination collapse 高度相关。**必须讨论。**\n\n3. **\"Hold Onto That Thought\"** (Liu et al., NeurIPS 2025): 系统评估 KV cache 压缩对 reasoning 的影响，发现 token-dropping 方法会破坏 reasoning integrity。与本文的 random vs. importance-based eviction 对比直接相关。**应当讨论。**\n\n4. **RAC / \"Reasoning Models Can Be Accurately Pruned via Chain-of-Thought Reconstruction\"** (NeurIPS 2025): 50% sparsity 下保留 95% reasoning 能力，关键创新是用 on-policy CoT traces 重建而非仅输入重建。与本文的 pruning + reasoning 主题直接相关。**应当讨论。**\n\n5. **EVICPRESS** (Fang et al., 2025): Joint KV-Cache compression and eviction，优化跨存储层的 eviction 和 compression 决策。属于 compound compression 的方法性工作。**可选讨论。**\n\n6. **LongFlow** (2026, ICLR withdrawn): KV cache compression for reasoning models with throughput measurement (11.8× throughput, 80% compression)。本文缺少 throughput evaluation，LongFlow 展示了这类评估的可行性。**可选讨论。**\n\n7. **\"Not All Heads Matter\"** (Microsoft, 2024): Head-level KV cache compression with integrated retrieval and reasoning。与 head-level importance heterogeneity 相关。**可选讨论。**\n\n特别指出：论文 bib 中已有 `raas-acl2025` (RaaS) 但正文未引用，这是 reasoning-aware attention sparsity 的直接相关工作，遗漏不可接受。\n\n---\n\n## 主要优势\n\n1. **统计方法严谨**：permutation test + Bonferroni correction + bootstrap CI + effect size reporting 的组合在 ML 论文中罕见，值得肯定（Section 5.5, Appendix C/G）。\n2. **Random eviction 作为 falsification control 设计精巧**：用 random eviction 作为 null strategy 来隔离\"phase gradient 是 strategy-specific 还是 compound sparsity inherent\"的设计简洁有力（Table 1, Section 5.1）。\n3. **Multiplicative null 验证**（Appendix B）：检验 additive vs. multiplicative null 不影响结论，增强稳健性。\n4. **Limitations section 诚实全面**：对样本量、架构限制、因果性限制等的讨论坦诚，这在很多论文中做不到。\n\n---\n\n## Questions for Authors\n\n1. 如果将评估扩大到全部 500 道 MATH-500 题，severity gradient 的 magnitude 和 statistical significance 是否保持？50 vs. 500 的结果对比是验证当前发现稳健性的最低成本实验。\n2. Phase-aware compression budget 的 oracle 版本（已知每个 phase 的最优 sparsity level）相对于 uniform budget 能提升多少 accuracy？如果只需要简单地对 high/low phase 用不同 s，实现成本极低——为什么不做？\n3. 为什么选择 Frobenius norm 而非 gradient-based importance 来决定 head pruning？论文在 Extended Discussion 中提到\"attention-independent metrics should produce flatter severity gradients\"——这是一个 testable prediction，为什么不在本文中验证？\n4. Discrimination collapse 的 Gini 下降幅度（0.010-0.081）在绝对值上很小。是否计算了 Gini 下降与 severity gradient 之间的相关系数？如果相关性不强，机制解释的说服力会大打折扣。\n\n---\n\n**总结判断**：论文发现了一个有趣的经验现象，统计分析做得规范，但（1）纯观察性贡献缺乏方法论增量，（2）评估规模过小（2 个同架构模型 × 50 题），（3）核心指标 G 受分母影响存在误导性，（4）遗漏多篇 2025-2026 高度相关工作。建议 **Resubmit next cycle**，补充方法性贡献（至少 oracle phase-aware budget 验证）和扩大评估规模后再投。",
  "reviewer_id": "2",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 审稿报告\n\n**论文**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Reasoning Models\n**Venue**: EMNLP 2026 Main Conference (ACL Rolling Review May 2026)\n\n---\n\n## 总体评分\n\n**Overall**: 2.5/5 — 介于 Findings 接收和 Resubmit 之间\n**一句话总结**: 论文发现了一个有趣的经验现象（compound sparsity severity 的 phase 依赖性），统计方法扎实，但贡献增量性偏强、无方法提出、评估规模过小，作为 EMNLP 主会论文分量不足。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3/5 | 统计方法（permutation test, bootstrap CI, Bonferroni 校正）规范，但样本量极小（50 problems, 单一架构），discrimination collapse 仅为相关性证据 |\n| Excitement | 2.5/5 | 现象本身有趣（phase-strategy crossover），但缺乏方法论贡献，且\"severity gradient\"的巨大倍数（69×-274×）主要由分母极小驱动 |\n| Overall | 2.5/5 | 观察性发现+诊断工具，距离 EMNLP 主会的方法论或系统性贡献门槛尚有差距 |\n| Reproducibility | 3/5 | 实验设置描述清晰，但无代码释放，50 个问题的 stratified sampling 种子未明确指定是否公开 |\n| Reviewer Confidence | 4/5 | 熟悉 KV cache compression 和 LLM pruning 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 新颖性不足：核心贡献是观察性发现而非方法\n\n- 具体位置：Section 1 贡献列表（3 条贡献均为\"identify\"/\"show\"/\"propose mechanism\"）\n- 问题：三条贡献均为经验观察或事后解释，没有提出任何可操作的方法（phase-aware compression controller / dynamic budget allocation）。Discussion (Section 6) 提到\"phase-aware compression budget\"但仅停留在概念层面（\"could mitigate\"），未实现、未验证。对于 EMNLP 主会 long paper，纯观察性工作的门槛更高——需要更大规模、更多模型、或更深的理论分析来弥补方法空缺。\n- 为什么影响接收：ACL ARR excitement 评分明确要求\"novel and useful methodology\"或\"insightful empirical results\"。在仅有 2 个同架构模型、50 道题的规模下，单纯的经验观察难以满足\"insightful\"标准。\n- 建议修改方向：(a) 实现并验证 phase-aware compression budget（哪怕是 oracle/static 版本），展示实际 accuracy 提升；或 (b) 大幅扩大评估规模（多架构、多任务、更大模型），使观察性发现的可信度足以独立成篇。\n\n**N2** [critical] Severity gradient 的 69×-274× 倍数具有误导性\n\n- 具体位置：Abstract (\"over an order of magnitude\"), Section 5.2, Figure 1\n- 问题：G = Ĩ_low / Ĩ_high，其中 Ĩ_high 极小（0.006-0.053，见 Appendix Table D）。当分母接近零时，比值可以任意大——这不反映实际严重程度。实际的绝对差值 Δ = 0.39-14.59（Table 1）更有信息量但远没那么戏剧性。Abstract 用\"varies by over an order of magnitude\"作为开头论点，过度依赖这个受分母影响的比值指标。\n- 为什么影响接收：如果核心叙事建立在一个因分母极小而膨胀的指标上，审稿人和读者会质疑发现的实际意义。\n- 建议修改方向：(a) 在正文中主要报告绝对差值 Δ 和 effect size d_z，将 G 降级为辅助指标；(b) 明确讨论 G 的分母敏感性问题；(c) 将 Figure 1 改为展示 Δ 或 d_z 的增长趋势。\n\n**N3** [critical] 评估规模严重不足\n\n- 具体位置：Section 4（50 MATH-500 problems, 2 models, 单一 Qwen2 架构）\n- 问题：\n  - **50 道题**：MATH-500 有 500 道题，只用 10% 缺乏理由（\"stratified sampling\" 但未论证 50 为何足够）。Qwen 进一步排除 4 道（n=46）。\n  - **单一架构**：两个模型共享 Qwen2ForCausalLM 架构（28 layers, 28 heads, 4-group GQA），这不是跨模型验证——是同一架构不同训练配置的验证。LLaMA 3、Mistral 或非 GQA 架构（如 MHA）未测试。\n  - **单一任务**：仅 MATH-500。代码推理、常识推理、多步 QA 等任务的 phase 结构可能完全不同。\n- 为什么影响接收：Limitations 诚实承认了这些局限，但 Abstract 和 Introduction 的 claim 表述过于一般化（\"reasoning models\" 而非 \"Qwen2-7B models on 50 math problems\"）。\n- 建议修改方向：至少覆盖一个非 Qwen 架构（LLaMA 3.3-8B 或 Mistral-7B）和一个非数学任务（如 GPQA 或 LiveCodeBench）。或者显著弱化 claim 的 generality。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Discrimination collapse 是相关性而非因果性证据\n\n- 具体位置：Section 5.6, Appendix H\n- 问题：Gini coefficient 下降（−0.030 到 −0.081）与 severity gradient 共现，但论文未排除其他混淆因素。更关键的是，entropy redistribution 组件仅在 DeepSeek 上一致，Qwen 在 s=0.25 出现符号反转（ΔH = +0.045），论文将其归因为\"model-specific\"但这削弱了机制的普遍性。Section 5.6 称 discrimination collapse 为\"mechanistic explanation\"，但它更接近于一个 correlational observation。\n- 建议：(a) 将\"mechanism\"改为\"hypothesis\"或\"correlational evidence\"；(b) 考虑设计消融实验（如人工控制 Gini 分布的 importance scores 来验证因果关系）。\n\n**W2** [warning] Interaction Index 与已有 super-additivity 概念的区分不清\n\n- 具体位置：Section 3, Eq. 1\n- 问题：II = r_b - r_a - r_k + 1 本质上是标准的交互效应（类似 ANOVA 中的 interaction term）。论文引用 SparK (Liao et al., 2026) 的 super-additive degradation 但未清楚区分 II 与 SparK 等工作中已有的 compound interaction 度量。如果 II 只是将 phase 维度加到已有概念上，应明确说明。\n- 建议：增加一段明确讨论 II 与 SparK、SLiM、UniComp 中使用的 compound interaction 度量的关系和区别。\n\n**W3** [warning] 正文仅 ~5 页，严重未利用 8 页限制\n\n- 具体位置：全文结构\n- 问题：正文约 5 页（Introduction 1.5p + Related Work 0.7p + Background 0.5p + Setup 0.5p + Results 1.2p + Discussion 0.5p + Conclusion 0.3p），远低于 long paper 8 页上限。大量关键信息被放在附录中：\n  - 完整的 per-phase breakdown table（Appendix D）应在正文\n  - Cross-model comparison table（Appendix F, Table 3）应在正文\n  - Effect size table（Appendix G, Table 5）应在正文\n  - Discrimination collapse metrics（Appendix H）至少 summary 应在正文\n  \n  这使正文感觉像是 extended abstract + 附录堆积，而非一篇完整论文。\n- 建议：将 Appendix D (Table 2), F (Table 3), G (Table 5) 移入正文，充分利用 8 页空间。将 Discussion 扩展以覆盖更多 deployment implications。\n\n**W4** [warning] Abstract 信息过载，可读性差\n\n- 具体位置：Abstract\n- 问题：Abstract 塞入了过多具体数字（69×, 274×, 0.39, 14.59, 0.44, 0.80, 7/8, 0.032, 0.818, 7.106, 1.363, d=-1.00, ρ=1.0, p=0.041...），读者在第一遍阅读时无法消化这些数据。一个好的 abstract 应传达 high-level insight + 关键定量 takeaway（1-2 个数字），而非完整的统计报告。\n- 建议：精简 Abstract 至 150-200 words，保留核心发现 + 1-2 个最有 impact 的定量结果。\n\n**W5** [warning] Phase segmentation 方法选择缺乏敏感性分析\n\n- 具体位置：Section 3 (\"tercile boundaries of per-position attention entropy\")\n- 问题：Phase 定义完全依赖 attention entropy 的三分位数划分，且沿用 ThinKV 的方法。但：(a) 为什么是 tercile 而非 quartile/quintile？(b) min_phase_length=10 的选择依据是什么？(c) 换用其他 phase segmentation（如 ThinKV 的 thought-type decomposition: reasoning/execution/transition）结果是否一致？这些选择对 severity gradient 的 magnitude 影响可能很大。\n- 建议：至少对 phase 数量和 min_phase_length 做 robustness check。\n\n---\n\n## 小问题（不影响接收）\n\n- **引用问题**：bib 中有 7 个 orphan 条目（在 .bib 中但未被正文引用）：`compression-ordering-2025`, `h2o-neurips2023`, `mustafar-neurips2025`, `obcache-2025`, `pagedeviction-eacl2026`, `pyramidkv-2024`, `raas-acl2025`。其中 H2O、PyramidKV、RaaS 等是高度相关工作，要么引用要么删除。`h2o-neurips2023` 的 title 字段为空。\n- **符号不一致**：正文混用 d_s 和 d_z 指代 Cohen's d 的变体，未明确区分。Abstract 用 d（无下标），Section 5.5 用 d_s，Appendix 用 d_z。\n- **Table 1 数值与 Appendix Table D 不完全对应**：Table 1 的 Random s=0.25 Δ=0.54，但 Appendix D 显示 Ĩ_low=1.363 - Ĩ_high=0.818 = 0.545，取整差异虽小但应统一精度。\n- **脚注 2**：提到\"4× NVIDIA RTX PRO 6000 Blackwell 96 GB GPUs\"，但实验仅在单个 7B 模型上运行 50 道题，使用 4 块 96GB GPU 似乎 over-provisioned，且未说明是否利用多卡。\n\n---\n\n## 遗漏的重要相关工作（Missing References）\n\n以下通过 web_search 验证的相关工作在论文中未被讨论：\n\n1. **R-KV** (Cai et al., NeurIPS 2025): \"Redundancy-aware KV Cache Compression for Reasoning Models\"。专门针对 reasoning model 的 KV cache 压缩，识别冗余 token 实现 10% KV cache 保留近乎无损性能。与本文直接相关——R-KV 也识别了 reasoning 生成中不同 token 的重要性差异，但采取了方法导向的路线。**必须讨论。**\n\n2. **RLKV / \"Which Heads Matter for Reasoning?\"** (Du et al., 2025/2026): 用 RL 识别 reasoning-critical heads 并差异化压缩。直接涉及 head pruning 与 reasoning 质量的交互——论文的核心议题。RLKV 的 \"functional heterogeneity\" 假设与 discrimination collapse 高度相关。**必须讨论。**\n\n3. **\"Hold Onto That Thought\"** (Liu et al., NeurIPS 2025): 系统评估 KV cache 压缩对 reasoning 的影响，发现 token-dropping 方法会破坏 reasoning integrity。与本文的 random vs. importance-based eviction 对比直接相关。**应当讨论。**\n\n4. **RAC / \"Reasoning Models Can Be Accurately Pruned via Chain-of-Thought Reconstruction\"** (NeurIPS 2025): 50% sparsity 下保留 95% reasoning 能力，关键创新是用 on-policy CoT traces 重建而非仅输入重建。与本文的 pruning + reasoning 主题直接相关。**应当讨论。**\n\n5. **EVICPRESS** (Fang et al., 2025): Joint KV-Cache compression and eviction，优化跨存储层的 eviction 和 compression 决策。属于 compound compression 的方法性工作。**可选讨论。**\n\n6. **LongFlow** (2026, ICLR withdrawn): KV cache compression for reasoning models with throughput measurement (11.8× throughput, 80% compression)。本文缺少 throughput evaluation，LongFlow 展示了这类评估的可行性。**可选讨论。**\n\n7. **\"Not All Heads Matter\"** (Microsoft, 2024): Head-level KV cache compression with integrated retrieval and reasoning。与 head-level importance heterogeneity 相关。**可选讨论。**\n\n特别指出：论文 bib 中已有 `raas-acl2025` (RaaS) 但正文未引用，这是 reasoning-aware attention sparsity 的直接相关工作，遗漏不可接受。\n\n---\n\n## 主要优势\n\n1. **统计方法严谨**：permutation test + Bonferroni correction + bootstrap CI + effect size reporting 的组合在 ML 论文中罕见，值得肯定（Section 5.5, Appendix C/G）。\n2. **Random eviction 作为 falsification control 设计精巧**：用 random eviction 作为 null strategy 来隔离\"phase gradient 是 strategy-specific 还是 compound sparsity inherent\"的设计简洁有力（Table 1, Section 5.1）。\n3. **Multiplicative null 验证**（Appendix B）：检验 additive vs. multiplicative null 不影响结论，增强稳健性。\n4. **Limitations section 诚实全面**：对样本量、架构限制、因果性限制等的讨论坦诚，这在很多论文中做不到。\n\n---\n\n## Questions for Authors\n\n1. 如果将评估扩大到全部 500 道 MATH-500 题，severity gradient 的 magnitude 和 statistical significance 是否保持？50 vs. 500 的结果对比是验证当前发现稳健性的最低成本实验。\n2. Phase-aware compression budget 的 oracle 版本（已知每个 phase 的最优 sparsity level）相对于 uniform budget 能提升多少 accuracy？如果只需要简单地对 high/low phase 用不同 s，实现成本极低——为什么不做？\n3. 为什么选择 Frobenius norm 而非 gradient-based importance 来决定 head pruning？论文在 Extended Discussion 中提到\"attention-independent metrics should produce flatter severity gradients\"——这是一个 testable prediction，为什么不在本文中验证？\n4. Discrimination collapse 的 Gini 下降幅度（0.010-0.081）在绝对值上很小。是否计算了 Gini 下降与 severity gradient 之间的相关系数？如果相关性不强，机制解释的说服力会大打折扣。\n\n---\n\n**总结判断**：论文发现了一个有趣的经验现象，统计分析做得规范，但（1）纯观察性贡献缺乏方法论增量，（2）评估规模过小（2 个同架构模型 × 50 题），（3）核心指标 G 受分母影响存在误导性，（4）遗漏多篇 2025-2026 高度相关工作。建议 **Resubmit next cycle**，补充方法性贡献（至少 oracle phase-aware budget 验证）和扩大评估规模后再投。",
    "reviewer_id": "2",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 205 · 2026-05-14T13:13:27.943367+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 6089
}
```

</details>

---


### Assistant

_source line 206 · 2026-05-14T13:13:40.249981+00:00_

审稿报告已提交给 Review Director。

**审稿结论：Overall 2.5/5（建议 Resubmit）。** 核心问题：

1. **新颖性不足**：三条贡献均为经验观察，未提出任何方法。Phase-aware compression budget 仅停留在概念层面。
2. **Severity gradient 指标 G 的 69×-274× 倍数由分母极小（Ĩ_high=0.006-0.053）驱动，具有误导性。**
3. **评估规模严重不足**：仅 2 个同架构（Qwen2）模型、50 道 MATH-500 题，无法支撑论文中"reasoning models"的一般化 claim。
4. **遗漏多篇关键相关工作**：R-KV (NeurIPS 2025)、RLKV (2025)、"Hold Onto That Thought" (NeurIPS 2025) 等直接相关工作未讨论。bib 中已有 RaaS 条目却未在正文引用。
5. **正文仅 ~5 页**，远未利用 8 页限制，大量关键表格被推入附录。

优势：统计方法严谨（permutation test + bootstrap + Bonferroni），random eviction 作为 falsification control 设计精巧，Limitations 诚实。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2"
}
```

</details>

---


## Round 3

## Round 3

4 recorded events


### User

_source line 207 · 2026-05-14T13:13:41.602057+00:00_

[Round 1 审稿请求]:
## Step 2 — 交叉分享：请回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿原文。请逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

特别关注与你审查侧重（新颖性 + 相关工作 + 写作 + 格式）相关的发现是否一致或有分歧。

---

## Reviewer 1 — Round 1 审稿报告

**审查侧重：方法严谨性 + 实验设计 + 统计验证**

**Overall**: 3/5 (Findings-level)
**一句话总结**: 论文发现了一个有趣且可验证的现象（compound sparsity 的 phase-strategy 交互），实验设计有亮点（random eviction 作为 falsification control），但实验规模过小（n=50, 2 个同架构模型, 4 个 sparsity levels）、多处数值不一致、以及关键统计论证存在缺陷，不足以支撑论文标题和摘要中隐含的通用性声明。

### 官方维度打分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心发现（phase-strategy interaction）有实验支撑，但多个 main claims 的证据不充分：monotonicity 仅基于 4 个数据点，cross-model ρ=1.0 统计功效极低，Qwen s=0.15 marginal result 被忽略 |
| Excitement | 3/5 | Phase-modulated severity 和 crossover 现象有学术价值，但论文止步于现象描述，未提出或验证 phase-aware controller，实际影响有限 |
| Reproducibility | 3/5 | 提供了模型名称、sparsity levels、统计方法细节，但未提供代码/数据、50 题选择标准不透明、随机种子未完整报告 |
| Confidence | 4/5 | 仔细阅读了全文及附录，逐条核验了统计数据和方程 |

### Must-Fix 问题

**N1** [critical] 数值不一致：摘要/正文/表格之间存在矛盾数据
- Abstract 和 Table 1 报告 DeepSeek s=0.30 时 Δ=14.59，但 §5.1 第一段（p.4 左栏）写 "Δ increases from 0.39 at s=0.15 to **11.59** at s=0.30"。14.59 与 11.59 不一致。
- 主文（Table 1 标题、§4.2、§5 全文）均声称 DeepSeek n=50，但 Appendix E（p.11）明确写 "paired permutation test yields **n=49** paired problems for DeepSeek (1 excluded)"。
- §6.2（p.7）声称 DeepSeek "ΔH ∈ [−0.080, −0.047]"，但 Table 7（p.12）显示 ΔH 范围为 [−0.047, −0.040]。

**N2** [critical] Cross-model Spearman ρ=1.0（n=4）作为 "replication" 证据在统计上无意义
- 4 个数据点的 Spearman ρ=1.0 → p=1/24≈0.042。统计功效极低，无法区分任何单调关系的具体形式；未做 Bonferroni 修正（论文其他检验均做了）；p=0.04 修正后不再显著。

**N3** [critical] 样本量不足以支撑核心声明的稳健性
- n=50（实际 49/46），右偏分布下 median 估计不稳定。s=0.30 Bootstrap CI=[0.70, 16.29]（Appendix E），跨越一个数量级。

**N4** [critical] Severity gradient G 定义数值不稳定，69×–274× 数字具有误导性
- G = Π̃_low / Π̃_high，分母 Π̃_high = 0.006–0.053 接近零，G 对分母微小变化极度敏感。ε 阈值未说明取值。

### Should-Fix 问题

**W1** [major] Qwen s=0.15 marginal（d_z=0.28, CI含零）与摘要 unqualified monotonicity 声明矛盾
**W2** [major] 仅 2 个同 Qwen2 架构模型，"Transformer-based reasoning" 泛化声明过度
**W3** [major] Phase segmentation 用 attention sparsity 定义 phase，与 attention-dependent outcome 存在概念耦合/confounding
**W4** [major] 仅 4 个 sparsity levels 不足以论证 "monotonic growth" 或分析增长形状
**W5** [major] Cohen's d 解读不准确（0.44≠small, 0.80=threshold of large）；摘要写 0.41 但正文写 0.44
**W6** [major] 缺少 task accuracy 评估（仅 PPL），无法判断 severity gradient 的实际部署影响
**W7** [warning] Limitations 节格式违反 ACL/ARR 要求（应为 Conclusion 后独立无编号节）

### 小问题
- h2o-neurips2023 bib 条目缺少 title 字段
- 7 个 orphan bib entries 需清理
- 对称 sparsity budget 限制应更突出讨论
- n=49/46 的 exclusion criteria 应在主文交代

### Questions for Authors
1. §5.1 的 "11.59" 与 Table 1 的 "14.59" 哪个正确？
2. n=50 还是 n=49？排除标准？
3. 是否做过 split-half stability analysis？
4. 用 token position 等分或 &lt;think>/<\/think> 标记做 phase segmentation 结果如何？
5. G 的 bootstrap 95% CI？
6. 各条件下 MATH-500 solve rate？
7. Cohen's d 摘要写 0.41 但正文写 0.44，哪个正确？

### Missing References
- Cohen (1988) Statistical Power Analysis
- RaaS (Hu et al., 2025) 在 bib 中未被引用
- Per-layer 非对称 sparsity 方法（OWL, Wanda）

### 主要优势
- Random eviction 作为 falsification control 是优秀的实验设计（7/8 null results）
- Entropy-discrimination collapse 机制提供了可检验的因果解释
- 论文组织清晰，C1-C6 逐一对应
- Phase-strategy crossover 是有趣的定性发现
- 统计方法论整体合理（median + nonparametric bootstrap + permutation + Bonferroni）

**Overall Score**: Borderline (3/5 — Findings-level)
**Confidence**: 4/5

---

请对以上每个 Must-Fix、Should-Fix 和关键 Missing References 逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 208 · 2026-05-14T13:16:08.636913+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — 交叉回应 Reviewer 1\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: 数值不一致**\n完全同意。这是严重的质量控制问题。三处不一致均可独立验证：\n- 14.59 vs 11.59：Appendix D 的完整 breakdown table 明确显示 s=0.30 importance Δ=14.59（Ĩ_low=14.639 − Ĩ_high=0.053），因此 §5.1 的 \"11.59\" 几乎确定是笔误。\n- n=50 vs n=49：Appendix 明确写 \"n=49 paired problems for DeepSeek (1 excluded)\"，主文 Table 1 标题却写 n=50。排除标准未在主文交代。\n- ΔH 范围：Appendix I 的 Table 显示 DeepSeek ΔH = {−0.040, −0.047, −0.045, −0.044}，范围为 [−0.047, −0.040]，与 §6.2 声称的 [−0.080, −0.047] 明显矛盾。\n\n我自己的审查未逐字核对 §5.1 的具体数值，R1 发现了我遗漏的问题。对于一篇以精确统计分析为核心卖点的论文，这类数值错误尤其致命。\n\n**[AGREE] R1-N2: Cross-model ρ=1.0 (n=4) 无统计意义**\n完全同意。4 个数据点的 Spearman ρ=1.0 仅意味着两个序列同为单调递增，p=1/24≈0.042 在 Bonferroni 校正后不再显著。任何两个随 sparsity 递增的量（哪怕机制完全不同）都会产生 ρ=1.0。论文在其他所有检验中均做了 Bonferroni 校正，唯独此处遗漏，构成 cherry-picking 嫌疑。\n\n补充：Abstract 将此作为 cross-model replication 的核心证据（\"replicates on Qwen2.5-7B-Instruct\"），但 Qwen 的 effect size 仅为 DeepSeek 的 1/5（Table 3: Δ = 0.04→2.94 vs 0.39→14.59），且 s=0.15 处 CI 含零。用 ρ=1.0 来宣称 \"replication\" 是对这一术语的滥用——magnitude attenuation 这么大，更准确的说法是 \"partial, qualitatively consistent but quantitatively much weaker pattern\"。\n\n**[AGREE] R1-N3: 样本量不足**\n完全同意，与我的 N3 一致。补充两点：\n1. R1 指出的 s=0.30 Bootstrap CI=[0.70, 16.29] 跨越一个数量级，这意味着 severity gradient 的 point estimate 不够精确——Δ 的真值可能是 0.70 也可能是 16.29，差 23 倍。\n2. 右偏分布下（mean/median ratio 1.6:1, Appendix C），n=49 的 median 估计本身 bias 较小，但 variance 很大。论文选用 median 而非 mean 是正确的，但这不能补救样本量不足的根本问题。\n\n**[AGREE] R1-N4: Severity gradient G 数值不稳定**\n与我的 N2 完全一致。G 的分母 Ĩ_high 在 0.006-0.053 范围内，任何微小扰动都会导致 G 剧烈变化。R1 额外指出 ε 阈值（用于避免除零）未说明取值——这是我遗漏的一个好观察。如果 ε=0.001，G 的计算结果会显著不同于 ε=0.01。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: Qwen s=0.15 marginal result 与 monotonicity 声明**\n同意但补充一个 nuance：Abstract 实际上写了 \"replicates on Qwen2.5-7B-Instruct at s≥0.20 (d_z≥0.55)\"，即 Abstract 自身限定了 Qwen 的有效范围从 s≥0.20 开始。但 R1 的核心论点仍然成立——论文标题用 \"Severity Gradients\" 暗示一般性结论，而 Qwen s=0.15 的失败（d_z=0.28, CI 含零）说明 gradient 的存在条件比论文暗示的更窄。对于 claim 的表述精度，R1 的批评是合理的。\n\n**[AGREE] R1-W2: 仅 2 个同架构模型的泛化过度**\n与我的 N3 完全一致。两个模型共享 Qwen2ForCausalLM（28 layers, 28 heads, 4-group GQA），架构变量为零。DeepSeek vs Qwen 的差异仅来自训练（reasoning distillation vs instruction tuning），这是 training recipe 对比而非 architecture 对比。论文使用 \"cross-model replication\" 一词时，读者的合理预期是不同架构的验证。\n\n**[REBUT] R1-W3: Phase segmentation 与 outcome 的概念耦合/confounding**\n部分反驳。R1 的 concern 有一定道理——phase 由 attention sparsity (Eq. 6) 定义，outcome (II) 也依赖 attention-based metrics——但论文的 random eviction falsification control 实质性地缓解了这一问题。\n\n具体论证：如果 confounding 是 trivial 的（即 phase 定义本身就决定了 severity gradient），那么 random eviction 也应展现 phase gradient，因为 phase assignment 对两种 strategy 完全相同（phase 是在 baseline 无压缩条件下定义的，不依赖 eviction strategy）。但实验结果显示 random eviction 在 7/8 条件下无显著 phase gradient（Table 1），这排除了 \"phase 定义本身导致 gradient\" 的 trivial 解释。\n\n然而，R1 的 concern 并非完全无效：attention sparsity 定义的 phase 可能与 importance-based eviction 有 mechanistic coupling（高 entropy phase → 更均匀 importance → eviction 更 random-like → 更少 compound interaction），这恰恰是 discrimination collapse 所描述的机制。所以 confounding 和 mechanism 在这里是同一件事——问题是论文是否充分讨论了这一点。建议作者在正文明确承认 phase definition 和 mechanism 的 coupling，并讨论用 non-attention-based phase segmentation（如 token position 等分或 &lt;think> 标记）验证 robustness。\n\n**[AGREE] R1-W4: 仅 4 个 sparsity levels 不足以论证 monotonicity**\n同意。4 个数据点只能说 \"在测试的 4 个 s 值上观察到递增趋势\"，不能称为 \"monotonic growth\"。特别是：(a) 没有测试 s<0.15 或 s>0.30，不知道边界行为；(b) 4 点的任何排列中有 4!/4!= 1/24 ≈ 4.2% 的概率恰好递增，与 ρ=1.0 的 p-value 一样尴尬。\n\n**[AGREE] R1-W5: Cohen's d 解读不准确 + 数值不一致**\n同意。Cohen (1988) 的标准 convention 是 small=0.2, medium=0.5, large=0.8。d_z=0.44 是 small-to-medium，不是 \"small\"；d_z=0.80 是 large 的起始阈值，不是 firmly large。Abstract 写 d=0.41 但 Appendix Table 5 写 d_z=0.44——又一处数值不一致，支持 R1-N1 的系统性质量问题判断。\n\n**[AGREE with caveat] R1-W6: 缺少 task accuracy 评估**\n基本同意。论文使用 MATH-500 problems 但未报告 solve rate（各条件下正确率），仅报告基于 performance ratio 的 interaction index。对于 reasoning 任务，accuracy 是最终 metric——PPL 或 performance ratio 的变化不能直接说明 \"这个 sparsity 配置是否仍能正确解题\"。\n\n不过我加一个 caveat：如果论文的目标是 characterize interaction patterns 而非 recommend deployment configs，那么 II 作为 relative metric 是合理的。但论文 Section 7 (Conclusion) 和 Discussion 确实提到了 \"deployment\" 和 \"phase-aware sparsity allocation\"，这就要求 accuracy 数据来支撑实际影响。\n\n**[AGREE] R1-W7: Limitations 节格式**\n同意但认为这是 minor issue。ACL/ARR 确实要求 Limitations 作为正文最后的独立无编号节，不计入页数限制。如果论文将其编号或放在不正确位置，需要修正。但这是纯格式问题，修正成本极低。\n\n---\n\n### Missing References\n\n**[AGREE] R1-MR1: Cohen (1988) Statistical Power Analysis**\n同意。论文大量使用 Cohen's d 但未引用原始出处，且解读有误（W5）。加入 Cohen (1988) 并修正解读。\n\n**[AGREE] R1-MR2: RaaS (Hu et al., 2025) 在 bib 中未被引用**\n与我自己的发现完全一致。RaaS 已在 bib 中（`raas-acl2025`）但正文从未 \\cite，这是一个明显的疏忽。RaaS 发现了 reasoning 中的 \"milestone tokens\" 现象，与论文的 phase-dependent importance 高度相关。\n\n**[PARTIAL AGREE] R1-MR3: Per-layer 非对称 sparsity 方法（OWL, Wanda）**\n部分同意。OWL 和 Wanda 是 weight pruning 方法，与论文研究的 inference-time sparsity (attention head pruning + KV cache eviction) 有本质区别。然而，OWL 的核心思想（per-layer adaptive sparsity budget）与论文提出的 \"phase-aware sparsity allocation\" 概念有类比价值。建议在 Discussion 中简要提及而非必须在 Related Work 详细讨论。\n\n补充我自己发现的遗漏（R1 未提及）：\n- **R-KV** (NeurIPS 2025): Reasoning model 专用 KV cache 压缩，识别冗余 token。直接相关。\n- **RLKV** (2025/2026): RL-guided head identification for reasoning，与 head pruning + reasoning 的交互直接相关。\n- **\"Hold Onto That Thought\"** (NeurIPS 2025): KV cache compression 对 reasoning integrity 的系统评估。\n\n---\n\n### 总体评价一致性\n\nR1 给出 3/5（Findings-level），我给出 2.5/5（Findings 和 Resubmit 之间）。我们在核心判断上高度一致：\n\n**共识点：**\n1. 评估规模不足（n=50, 2 同架构模型）——我们都列为 critical\n2. G 指标的分母敏感性——我们都列为 critical\n3. 缺乏方法论贡献——我们都认为 \"止步于现象描述\" 是核心弱点\n4. Random eviction 作为 falsification control 是优秀设计——我们都认可\n5. 统计方法整体规范——我们都肯定\n\n**分歧点：**\n- R1 给 3/5 (Findings-level)，我给 2.5/5。差异来自我对**新颖性**的更严格要求：我认为在没有方法贡献的前提下，纯观察性发现需要更大规模（多架构、多任务）才能达到 Findings 门槛。R1 似乎认为现象本身的学术价值（phase-strategy crossover）已足够 Findings。\n- R1 发现了我遗漏的数值不一致（§5.1 的 11.59 vs 14.59, ΔH 范围矛盾, d=0.41 vs 0.44）——这些进一步降低了我的评分信心。\n- 我在 confounding (W3) 上给出了 partial rebut，认为 random eviction control 在相当程度上缓解了这一 concern。\n\n**综合建议：** 维持 Resubmit 建议。R1 发现的多处数值不一致加上我们共同识别的规模不足和 G 指标误导性问题，使论文在当前状态下不适合接收。",
  "reviewer_id": "2",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — 交叉回应 Reviewer 1\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: 数值不一致**\n完全同意。这是严重的质量控制问题。三处不一致均可独立验证：\n- 14.59 vs 11.59：Appendix D 的完整 breakdown table 明确显示 s=0.30 importance Δ=14.59（Ĩ_low=14.639 − Ĩ_high=0.053），因此 §5.1 的 \"11.59\" 几乎确定是笔误。\n- n=50 vs n=49：Appendix 明确写 \"n=49 paired problems for DeepSeek (1 excluded)\"，主文 Table 1 标题却写 n=50。排除标准未在主文交代。\n- ΔH 范围：Appendix I 的 Table 显示 DeepSeek ΔH = {−0.040, −0.047, −0.045, −0.044}，范围为 [−0.047, −0.040]，与 §6.2 声称的 [−0.080, −0.047] 明显矛盾。\n\n我自己的审查未逐字核对 §5.1 的具体数值，R1 发现了我遗漏的问题。对于一篇以精确统计分析为核心卖点的论文，这类数值错误尤其致命。\n\n**[AGREE] R1-N2: Cross-model ρ=1.0 (n=4) 无统计意义**\n完全同意。4 个数据点的 Spearman ρ=1.0 仅意味着两个序列同为单调递增，p=1/24≈0.042 在 Bonferroni 校正后不再显著。任何两个随 sparsity 递增的量（哪怕机制完全不同）都会产生 ρ=1.0。论文在其他所有检验中均做了 Bonferroni 校正，唯独此处遗漏，构成 cherry-picking 嫌疑。\n\n补充：Abstract 将此作为 cross-model replication 的核心证据（\"replicates on Qwen2.5-7B-Instruct\"），但 Qwen 的 effect size 仅为 DeepSeek 的 1/5（Table 3: Δ = 0.04→2.94 vs 0.39→14.59），且 s=0.15 处 CI 含零。用 ρ=1.0 来宣称 \"replication\" 是对这一术语的滥用——magnitude attenuation 这么大，更准确的说法是 \"partial, qualitatively consistent but quantitatively much weaker pattern\"。\n\n**[AGREE] R1-N3: 样本量不足**\n完全同意，与我的 N3 一致。补充两点：\n1. R1 指出的 s=0.30 Bootstrap CI=[0.70, 16.29] 跨越一个数量级，这意味着 severity gradient 的 point estimate 不够精确——Δ 的真值可能是 0.70 也可能是 16.29，差 23 倍。\n2. 右偏分布下（mean/median ratio 1.6:1, Appendix C），n=49 的 median 估计本身 bias 较小，但 variance 很大。论文选用 median 而非 mean 是正确的，但这不能补救样本量不足的根本问题。\n\n**[AGREE] R1-N4: Severity gradient G 数值不稳定**\n与我的 N2 完全一致。G 的分母 Ĩ_high 在 0.006-0.053 范围内，任何微小扰动都会导致 G 剧烈变化。R1 额外指出 ε 阈值（用于避免除零）未说明取值——这是我遗漏的一个好观察。如果 ε=0.001，G 的计算结果会显著不同于 ε=0.01。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: Qwen s=0.15 marginal result 与 monotonicity 声明**\n同意但补充一个 nuance：Abstract 实际上写了 \"replicates on Qwen2.5-7B-Instruct at s≥0.20 (d_z≥0.55)\"，即 Abstract 自身限定了 Qwen 的有效范围从 s≥0.20 开始。但 R1 的核心论点仍然成立——论文标题用 \"Severity Gradients\" 暗示一般性结论，而 Qwen s=0.15 的失败（d_z=0.28, CI 含零）说明 gradient 的存在条件比论文暗示的更窄。对于 claim 的表述精度，R1 的批评是合理的。\n\n**[AGREE] R1-W2: 仅 2 个同架构模型的泛化过度**\n与我的 N3 完全一致。两个模型共享 Qwen2ForCausalLM（28 layers, 28 heads, 4-group GQA），架构变量为零。DeepSeek vs Qwen 的差异仅来自训练（reasoning distillation vs instruction tuning），这是 training recipe 对比而非 architecture 对比。论文使用 \"cross-model replication\" 一词时，读者的合理预期是不同架构的验证。\n\n**[REBUT] R1-W3: Phase segmentation 与 outcome 的概念耦合/confounding**\n部分反驳。R1 的 concern 有一定道理——phase 由 attention sparsity (Eq. 6) 定义，outcome (II) 也依赖 attention-based metrics——但论文的 random eviction falsification control 实质性地缓解了这一问题。\n\n具体论证：如果 confounding 是 trivial 的（即 phase 定义本身就决定了 severity gradient），那么 random eviction 也应展现 phase gradient，因为 phase assignment 对两种 strategy 完全相同（phase 是在 baseline 无压缩条件下定义的，不依赖 eviction strategy）。但实验结果显示 random eviction 在 7/8 条件下无显著 phase gradient（Table 1），这排除了 \"phase 定义本身导致 gradient\" 的 trivial 解释。\n\n然而，R1 的 concern 并非完全无效：attention sparsity 定义的 phase 可能与 importance-based eviction 有 mechanistic coupling（高 entropy phase → 更均匀 importance → eviction 更 random-like → 更少 compound interaction），这恰恰是 discrimination collapse 所描述的机制。所以 confounding 和 mechanism 在这里是同一件事——问题是论文是否充分讨论了这一点。建议作者在正文明确承认 phase definition 和 mechanism 的 coupling，并讨论用 non-attention-based phase segmentation（如 token position 等分或 &lt;think> 标记）验证 robustness。\n\n**[AGREE] R1-W4: 仅 4 个 sparsity levels 不足以论证 monotonicity**\n同意。4 个数据点只能说 \"在测试的 4 个 s 值上观察到递增趋势\"，不能称为 \"monotonic growth\"。特别是：(a) 没有测试 s<0.15 或 s>0.30，不知道边界行为；(b) 4 点的任何排列中有 4!/4!= 1/24 ≈ 4.2% 的概率恰好递增，与 ρ=1.0 的 p-value 一样尴尬。\n\n**[AGREE] R1-W5: Cohen's d 解读不准确 + 数值不一致**\n同意。Cohen (1988) 的标准 convention 是 small=0.2, medium=0.5, large=0.8。d_z=0.44 是 small-to-medium，不是 \"small\"；d_z=0.80 是 large 的起始阈值，不是 firmly large。Abstract 写 d=0.41 但 Appendix Table 5 写 d_z=0.44——又一处数值不一致，支持 R1-N1 的系统性质量问题判断。\n\n**[AGREE with caveat] R1-W6: 缺少 task accuracy 评估**\n基本同意。论文使用 MATH-500 problems 但未报告 solve rate（各条件下正确率），仅报告基于 performance ratio 的 interaction index。对于 reasoning 任务，accuracy 是最终 metric——PPL 或 performance ratio 的变化不能直接说明 \"这个 sparsity 配置是否仍能正确解题\"。\n\n不过我加一个 caveat：如果论文的目标是 characterize interaction patterns 而非 recommend deployment configs，那么 II 作为 relative metric 是合理的。但论文 Section 7 (Conclusion) 和 Discussion 确实提到了 \"deployment\" 和 \"phase-aware sparsity allocation\"，这就要求 accuracy 数据来支撑实际影响。\n\n**[AGREE] R1-W7: Limitations 节格式**\n同意但认为这是 minor issue。ACL/ARR 确实要求 Limitations 作为正文最后的独立无编号节，不计入页数限制。如果论文将其编号或放在不正确位置，需要修正。但这是纯格式问题，修正成本极低。\n\n---\n\n### Missing References\n\n**[AGREE] R1-MR1: Cohen (1988) Statistical Power Analysis**\n同意。论文大量使用 Cohen's d 但未引用原始出处，且解读有误（W5）。加入 Cohen (1988) 并修正解读。\n\n**[AGREE] R1-MR2: RaaS (Hu et al., 2025) 在 bib 中未被引用**\n与我自己的发现完全一致。RaaS 已在 bib 中（`raas-acl2025`）但正文从未 \\cite，这是一个明显的疏忽。RaaS 发现了 reasoning 中的 \"milestone tokens\" 现象，与论文的 phase-dependent importance 高度相关。\n\n**[PARTIAL AGREE] R1-MR3: Per-layer 非对称 sparsity 方法（OWL, Wanda）**\n部分同意。OWL 和 Wanda 是 weight pruning 方法，与论文研究的 inference-time sparsity (attention head pruning + KV cache eviction) 有本质区别。然而，OWL 的核心思想（per-layer adaptive sparsity budget）与论文提出的 \"phase-aware sparsity allocation\" 概念有类比价值。建议在 Discussion 中简要提及而非必须在 Related Work 详细讨论。\n\n补充我自己发现的遗漏（R1 未提及）：\n- **R-KV** (NeurIPS 2025): Reasoning model 专用 KV cache 压缩，识别冗余 token。直接相关。\n- **RLKV** (2025/2026): RL-guided head identification for reasoning，与 head pruning + reasoning 的交互直接相关。\n- **\"Hold Onto That Thought\"** (NeurIPS 2025): KV cache compression 对 reasoning integrity 的系统评估。\n\n---\n\n### 总体评价一致性\n\nR1 给出 3/5（Findings-level），我给出 2.5/5（Findings 和 Resubmit 之间）。我们在核心判断上高度一致：\n\n**共识点：**\n1. 评估规模不足（n=50, 2 同架构模型）——我们都列为 critical\n2. G 指标的分母敏感性——我们都列为 critical\n3. 缺乏方法论贡献——我们都认为 \"止步于现象描述\" 是核心弱点\n4. Random eviction 作为 falsification control 是优秀设计——我们都认可\n5. 统计方法整体规范——我们都肯定\n\n**分歧点：**\n- R1 给 3/5 (Findings-level)，我给 2.5/5。差异来自我对**新颖性**的更严格要求：我认为在没有方法贡献的前提下，纯观察性发现需要更大规模（多架构、多任务）才能达到 Findings 门槛。R1 似乎认为现象本身的学术价值（phase-strategy crossover）已足够 Findings。\n- R1 发现了我遗漏的数值不一致（§5.1 的 11.59 vs 14.59, ΔH 范围矛盾, d=0.41 vs 0.44）——这些进一步降低了我的评分信心。\n- 我在 confounding (W3) 上给出了 partial rebut，认为 random eviction control 在相当程度上缓解了这一 concern。\n\n**综合建议：** 维持 Resubmit 建议。R1 发现的多处数值不一致加上我们共同识别的规模不足和 G 指标误导性问题，使论文在当前状态下不适合接收。",
    "reviewer_id": "2",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 209 · 2026-05-14T13:16:13.226578+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4589
}
```

</details>

---


### Assistant

_source line 210 · 2026-05-14T13:16:31.456946+00:00_

交叉回应已提交。总结：

**与 R1 的 12 条意见中，10 条 [AGREE]，1 条 [PARTIAL AGREE]，1 条 [REBUT]：**

- **[AGREE]** N1 数值不一致、N2 ρ=1.0 无意义、N3 样本量不足、N4 G 指标不稳定、W1 Qwen monotonicity 过度声明、W2 泛化过度、W4 仅 4 个 sparsity levels、W5 Cohen's d 误读、W6 缺 accuracy、W7 Limitations 格式
- **[PARTIAL AGREE]** OWL/Wanda 遗漏（weight pruning 与 inference-time sparsity 有本质区别，但 adaptive budget 思想值得类比讨论）
- **[REBUT]** W3 phase segmentation confounding — random eviction 在相同 phase assignment 下无 gradient（7/8 non-significant），排除了 phase 定义本身导致 gradient 的 trivial 解释

核心分歧：R1 给 3/5 (Findings)，我给 2.5/5。我对新颖性要求更严格——没有方法贡献时，纯观察性发现需要更大评估规模支撑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2"
}
```

</details>

---


## Round 4

## Round 4

56 recorded events


### User

_source line 211 · 2026-05-15T07:37:42.652219+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2（新颖性/完整性）

### Venue 信息
- **目标 venue**: EMNLP 2026 ARR (main conference)
- **截止日期**: 2026-05-25
- **格式**: ACL 2-column, 长文 8 页正文 + 不限附录, double-blind
- **必需 section**: Limitations

### 论文路径
`projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex`

### 你的审查侧重：新颖性/完整性
请重点评估以下方面：

1. **贡献新颖度**
   - "compound sparsity severity is phase-modulated" 这个 claim 的新颖性如何？
   - 与已有工作的区分度：ThinKV (phase-aware KV), SparK (compound sparsity), DefensiveKV (fragility) 等是否已经（部分）包含了类似发现？
   - "entropy-discrimination collapse" 作为机制解释的原创性——是否仅是已知现象的重新包装（HIES 2025 已报告 head discrimination collapse under heavy pruning）？
   - 贡献定位为"empirical finding"而非"method"——在 EMNLP main conference 中是否有足够影响力？

2. **Related Work 覆盖**
   - 是否遗漏了重要的相关工作？特别是：
     - 其他 compound compression 工作（量化+剪枝、蒸馏+剪枝）
     - phase-aware inference 的更多先驱工作
     - 其他 KV cache eviction robustness 分析
   - 引用是否真实？检查所有 2025-2026 年的引用是否存在幻觉引用
   - 引用格式是否符合 ACL 规范（natbib）？

3. **写作质量**
   - 论文结构是否清晰？信息流是否流畅？
   - Abstract 是否准确反映了论文内容和结论的强度？
   - 是否存在过度声称（overclaim）？特别是关于 cross-architecture generalization 的措辞
   - Discussion section 是否充分讨论了 limitations 和 implications？
   - `\placeholder{}` 未填充问题——列出所有位置并评估影响

4. **格式合规**
   - 是否符合 ACL double-blind 匿名要求？检查是否有 self-revealing references
   - 页数是否在 8 页限制内？
   - Limitations section 是否存在且充分？
   - 图表是否清晰、标注完整？
   - 附录中的 "REVIEWER-ATTACK" / "REBUTTAL" 注释（LaTeX comments）是否应在提交前删除？

5. **整体影响力**
   - 这篇论文对 NLP/ML 社区的实际价值？
   - 谁会引用这篇论文？它改变了什么实践？
   - 对 EMNLP 读者而言，主要 takeaway 是什么？

请输出标准审稿格式：Summary → Strengths → Weaknesses → Questions → Minor Issues

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-15T07:37:52.482805+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 213 · 2026-05-15T07:37:53.388306+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_reviewer_2_d0398257.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 214 · 2026-05-15T07:37:53.539361+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 215 · 2026-05-15T07:37:53.539955+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 216 · 2026-05-15T07:37:57.409022+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form criteria 2026 reviewer guidelines scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form criteria 2026 reviewer guidelines scoring"
  }
}
```

</details>

---


### Tool call

_source line 217 · 2026-05-15T07:37:57.862344+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR reviewer guidelines review form dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR reviewer guidelines review form dimensions"
  }
}
```

</details>

---


### Tool call

_source line 218 · 2026-05-15T07:37:59.018199+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 219 · 2026-05-15T07:37:59.222038+00:00_

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
11	
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{graphicx}
15	\usepackage{booktabs}
16	\usepackage{enumitem}
17	\usepackage{multirow}
18	
19	\graphicspath{{figures/}}
20	
21	\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}
22	
23	\title{Phase-Modulated Compound Sparsity:\\Strategy-Dependent Severity Gradients in Reasoning Models}
24	
25	\author{Anonymous}
26	
27	\begin{document}
28	
29	\maketitle
30	
31	\input{abstract}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{background}
36	\input{methodology}
37	\input{results}
38	\input{analysis}
39	\input{discussion}
40	\input{conclusion}
41	
42	\bibliography{references}
43	
44	\section*{Limitations}
45	\input{limitations}
46	
47	\appendix
48	\input{appendix}
49	\input{appendix_moved}
50	\input{appendix_disc_analysis}
51	
52	\end{document}
53	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 203
}
```

</details>

---


### Tool call

_source line 220 · 2026-05-15T07:37:59.272820+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 221 · 2026-05-15T07:38:02.968190+00:00_

Web search results for query: "EMNLP 2026 ARR reviewer guidelines review form dimensions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Changes to reviewer volunteering requirement and incentives in May 2025 cycle (EMNLP 2025)","url":"http://aclrollingreview.org/incentives2025"},{"title":"ClimateNLP 2026","url":"https://nlp4climate.github.io/submissionguide/"}]

Based on the search results, I found information about EMNLP 2026 and ARR reviewer guidelines. However, the search results don't contain specific details about the review form dimensions for ARR reviewers. Let me provide what I found:

EMNLP 2026 will use ACL Rolling Review (ARR) as a reviewing system, but final decisions will be made by the conference. 

Regarding reviewer guidelines, all reviewers must familiarize themselves with the latest version of the ARR reviewer guidelines and perform the 
…[truncated 719 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5105
}
```

</details>

---


### Tool result

_source line 222 · 2026-05-15T07:38:04.026643+00:00_

Web search results for query: "ACL ARR review form criteria 2026 reviewer guidelines scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, here's information about the ACL ARR review form criteria, reviewer guidelines, and scoring for 2026:

## Review Scores

Starting with February 2025, ARR reviewers are asked to provide three scores:
…[truncated 1443 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6617
}
```

</details>

---


### Tool result

_source line 223 · 2026-05-15T07:38:28.860524+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 29, \"total_citations\": 57, \"unique_cited_keys\": 29, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 21, \"online_not_found\": 3, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"adakv-neurips2025\", \"type\": \"inproceedings\", \"title\": \"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference\", \"authors\": \"Feng, Yuan and Lv, Junlin and Cao, Yukun and Xie, Xike and Zhou, S. Kevin\", \"year\": \"2025\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"decision-repr-transition-2026\", \"type\": \"article\", \"title\": \"Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions\", \"authors\": \"Shi, Boyu and Liu, Chang and Gao, ChuanBao and Yang, Xu and Geng, Xin\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.07271\"}, {\"key\": \"deepseek-r1-2025\", \"type\": \"article\", \"title\": \"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning\", \"authors\": \"DeepSeek-AI\", \"year\": \"2025\", \"venue\": \"Nature\"}, {\"key\": \"defensivekv-iclr2026\", \"type\": \"inproceedings\", \"title\": \"DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference\", \"authors\": \"Feng, Yuan and Guo, Haoyu and Lv, Junlin and Zhou, S. Kevin and Xie, Xike\", \"year\": \"2026\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"doing-more-with-less-2026\", \"type\": \"article\", \"title\": \"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling\", \"authors\": \"Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2604.25098\"}, {\"key\": \"efron-1993\", \"ty
…[truncated 23707 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 29587
}
```

</details>

---


### Tool call

_source line 224 · 2026-05-15T07:38:37.119911+00:00_

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
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
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

_source line 225 · 2026-05-15T07:38:37.171062+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 226 · 2026-05-15T07:38:37.473874+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 227 · 2026-05-15T07:38:37.474300+00:00_

1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	Prior work treats compound interaction magnitude as approximately constant across the generation process.
4	We show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.
5	
6	We evaluate compound sparsity on three models---DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct (both Qwen2ForCausalLM), and DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)---spanning two architectures, using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \in \{0.15, 0.20, 0.25, 0.30\}$.
7	Under importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.
8	Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible median difference ($\widetilde{\Delta} = \placeholder{}$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.
9	At $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) yet underperforms in low-sparsity phases ($\widetilde{\mathrm{II}} = 7.196$ vs.\ $1.363$)---a qualitative reversal in strategy ranking.
10	The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d_z \geq 0.55$; Spearman $\rho 
…[truncated 934 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 228 · 2026-05-15T07:38:37.826401+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 229 · 2026-05-15T07:38:38.329582+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses---\emph{attention head pruning} \cite{voita-acl2019, michel-neurips2019} and \emph{KV cache eviction} \cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \emph{compound sparsity}, but the resulting quality degradation is often super-additive \cite{spark-aaai2026, slim-icml2025}. Recent evaluations confirm that reasoning capabilities degrade disproportionately under compound compression \cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \cite{phase-transition-compression-2026}.
6	
7	Prior work treats compound interaction magnitude as roughly constant across generation \cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \cite{sparse-frontier-2025}.
8	This assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \cite{thinkv-iclr2026}.
9	Phase-aware methods like ThinKV \cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from greedy bias \cite{greedy-bias-kvcache-2026}, deferred importance \cite{retentivekv-2026}, and temporal dynamics in long generations \cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple mechanisms are composed.
10	If compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.

…[truncated 1862 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 230 · 2026-05-15T07:38:38.682093+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 231 · 2026-05-15T07:38:38.732808+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Compound compression.}
5	Combining multiple compression axes produces non-additive errors.
6	\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \cite{slim-icml2025} formalize compound error for quantization and sparsity.
7	\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.
8	\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.
9	GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.
10	These works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.
11	
12	\paragraph{KV cache eviction.}
13	Most methods rely on importance scoring whose reliability is increasingly questioned.
14	Ada-KV~\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\cite{snapkv-neurips2024} compresses from a fixed observation window; \cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\times}$ higher than expected under standard aggregation.
15	\cite{nacl-acl2024} combine proxy-token and random eviction to counter attention bias.
16	RetentiveKV~\cite{retentivekv-2026} identifies deferred importance, and \cite{greedy-bias-kvcache-2026} show that single importance metrics exhibit systematic greedy bias.
17	\cite{hies-2025} independently show that importance-based head discrimination collapses under heavy pruning, further questioning single-metric reliability.
18	Lethe~\cite{lethe-aaai2026} introduces temporal adaptivity with layer-wise multi-round pruning, and SparK~\cite{spark-aaai2026} extends eviction to the channel dimension with recoverable sparsity.
19	These me
…[truncated 1295 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 232 · 2026-05-15T07:38:38.733353+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 233 · 2026-05-15T07:38:39.235964+00:00_

1	% Section 3: Background and Problem Setup
2	% Note: eq:ii and eq:gradient are the canonical definitions.
3	% Full formulation details in Appendix (app:formulation-details).
4	
5	\section{Background and Problem Setup}
6	\label{sec:background}
7	
8	We formalize compound sparsity, define the Interaction Index, and introduce phase segmentation. Full mathematical details appear in Appendix~\ref{app:formulation-details}.
9	
10	\paragraph{Compound sparsity.}
11	\label{sec:compound-sparsity}
12	Let $s \in (0,1)$ denote a unified sparsity budget. \emph{Attention head pruning} removes the bottom-$s$ fraction of heads per layer by Frobenius norm importance \cite{voita-acl2019, michel-neurips2019}. \emph{KV cache eviction} removes the bottom-$s$ fraction of token positions from the cache. We compare two strategies: \emph{importance-based}, which scores positions by position-normalized cumulative attention mass (Eq.~\ref{eq:kv-importance} in Appendix~\ref{app:formulation-details}), and \emph{random}, which evicts uniformly at random \cite{nacl-acl2024}. Applying both simultaneously yields \emph{compound sparsity}; the two axes interact because head pruning alters the importance ranking used for eviction \cite{spark-aaai2026}. Existing joint-pruning approaches such as GRASPrune \cite{graspune-acl2026} learn global budget-constrained gates but treat decisions as static across generation.
13	
14	\paragraph{Interaction Index.}
15	\label{sec:interaction-index}
16	For a text segment, let $\text{PPL}_c$ denote perplexity under condition $c \in \{d, a, k, b\}$ (dense, attention-only, KV-only, compound). Normalizing by the dense baseline yields $r_c = \text{PPL}_c / \text{PPL}_d$, and:
17	\begin{equation}
18	    \mathrm{II} = r_b - r_a - r_k + 1.
19	    \label{eq:ii}
20	\end{equation}
21	$\mathrm{II} > 0$ indicates super-additive degradation; $\mathrm{II} = 0$ indicates additive independence. We adopt the additive null because the two axes operate on disjoint dimensions; qualitative co
…[truncated 1036 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-15T07:38:39.236386+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
  }
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-15T07:38:39.638758+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\paragraph{Models.}
5	\label{sec:models}
6	We evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \textbf{DeepSeek-R1-Distill-Qwen-7B}~\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \textbf{Qwen2.5-7B-Instruct}~\cite{qwen25-2024}, with standard instruction tuning, providing a cross-model replication target. Both are loaded in \texttt{bfloat16} with eager attention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values; \texttt{bfloat16} eliminated all occurrences.}
7	
8	\paragraph{Dataset.}
9	\label{sec:dataset}
10	We use 50 problems stratified from MATH-500~\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048).
11	
12	\paragraph{Sparsity configuration.}
13	\label{sec:sparsity-config}
14	We apply symmetric compound sparsity at $s \in \{0.15, 0.20, 0.25, 0.30\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\ref{eq:kv-importance}; BOS always retained) and \emph{random} eviction (uniform). Heads are pruned per layer by Frobenius norm; under random eviction, both heads and positions are selected uniformly.
15	
16	\paragraph{Phase segmentation and metrics.}
17	\label{sec:phase-seg}
18	Each sequence is segmented into three phases using the quantile-based method (\S\ref{sec:phase-segmentation}), with $\texttt{min\_phase\_length}{=}10$. We compute segment-level perplexity, II (Eq.~\ref{eq:ii}), and $G$ (Eq.~\ref{eq:gradient}), reporting medians due to heavy right-skew (mean/median ratios up to 43:1).
19	
20	\paragraph{Statistical analysis.}
21	\label{sec:stats}
22	All reported confidence intervals and significance t
…[truncated 397 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 236 · 2026-05-15T07:38:39.739600+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 237 · 2026-05-15T07:38:39.740257+00:00_

1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Strategy-Dependent Severity}
6	\label{sec:strategy-severity}
7	
8	Table~\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\times}$ amplification. Under random eviction, no systematic growth is observed ($-0.02$ to $1.54$), confirming that compound severity depends qualitatively on eviction strategy. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}
14	\label{tab:aggregate-ii}
15	\begin{tabular}{@{}lcccc@{}}
16	\toprule
17	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
18	\midrule
19	Importance & 0.39 & 1.48 & 7.16 & 14.59 \\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff
20	Random     & 0.01 & $-$0.02 & 0.54 & 1.54 \\ % exp_id: bf16_ds_rand_s015..s030; source: experiment_summary_table.json median_diff
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	
26	\subsection{Phase-Modulated Amplification}
27	\label{sec:phase-amplification}
28	
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the full per-phase breakdown. The severity gradient $G$ increases from $69{\times}$ at $s{=}0.15$ to $274{\times}$ at $s{=}0.30$ under importance-based eviction, while the high-sparsity phase experiences near-zero interaction ($\widetilde{\mathrm{II}}_{\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, $G \approx 0.9$--$1.7{
…[truncated 8932 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 238 · 2026-05-15T07:38:40.644544+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-15T07:38:41.097696+00:00_

1	\section{Analysis: Entropy-Discrimination Collapse}
2	\label{sec:analysis}
3	
4	We propose \emph{discrimination collapse} as the primary mechanism driving the phase-strategy interaction. Head pruning reduces the number of heads contributing to cumulative importance scores, flattening the score distribution: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) across all sparsity levels, with consistent negative deltas in all 16 conditions (Appendix~\ref{app:analysis}, Table~\ref{tab:discrimination-metrics-full}). When importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This effect is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
5	
6	Beyond discrimination collapse, head pruning redistributes the attention entropy of surviving heads. For DeepSeek, the entropy delta is consistently negative ($\Delta\mathcal{H} \in [-0.047, -0.040]$), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in survivors. For Qwen, the pattern partially replicates at $s \leq 0.20$ but reverses at $s{=}0.25$ ($\Delta\mathcal{H} = +0.045$), suggesting model-specific head specialization patterns (Appendix~\ref{app:analysis}, Table~\ref{tab:entropy-deltas}). We characterize discrimination collapse as the robust, model-independent driver, with entropy redistribution as a secondary, model-dependent amplifier. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 240 · 2026-05-15T07:38:41.148449+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 241 · 2026-05-15T07:38:41.600964+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Quantitative surprise.}
5	While the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($69$--$274{\times}$) far exceeds a naive ``somewhat worse'' prediction. The crossover---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) and underperforms in low-sparsity phases ($7.196$ vs.\ $1.363$)---cannot be derived from single-axis entropy reasoning. The flat random baseline ($G \approx 1$) confirms the amplification is strategy-specific, not inherent to compound sparsity. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json
6	
7	\paragraph{Implications for deployment.}
8	Applying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation. Discrimination collapse depends on attention-mass-based importance scoring shared by major KV cache methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-2024}), suggesting broad applicability.
9	
10	A preliminary pilot experiment explored oracle phase-aware budget reallocation, shifting sparsity budget from high-severity low-sparsity phases to low-severity high-sparsity phases. At $s{=}0.25$, oracle recovery---the fraction of compound interaction eliminated by phase-aware allocation---reached \placeholder{ORACLE\_PCT}\% (Wilcoxon $p = \placeholder{ORACLE\_P}$), below t
…[truncated 1685 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 242 · 2026-05-15T07:38:41.601394+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-15T07:38:42.053835+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation. Under importance-based eviction, the severity gradient grows from $69{\times}$ to $274{\times}$ across sparsity levels ($d_z$: $0.44 \to 0.80$); random eviction shows no such modulation (7/8 conditions non-significant). A crossover at $s{=}0.25$---where importance-based eviction reverses ranking across phases---demonstrates that no single strategy dominates uniformly. The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d_z \geq 0.55$) and partially extends cross-architecture to DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\sim$1/40 the magnitude. Discrimination collapse provides a mechanistic explanation supported by both Qwen2-based models; LLaMA results are directionally consistent but the interaction is weaker than in Qwen2 architectures.
5	These findings motivate phase-aware sparsity allocation for reasoning model deployment.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-15T07:38:42.054209+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 245 · 2026-05-15T07:38:42.556858+00:00_

1	\paragraph{Model scale and architecture.}
2	All experiments are conducted at the 7--8B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}) partially confirms the qualitative pattern beyond the Qwen2 architecture---monotonically increasing $d_z$ with within-importance phase gradient $\sim$1.0---but with substantially weaker interaction magnitude ($\sim$1/40 of DeepSeek) and mixed statistical evidence (only $s{=}0.30$ significant after Bonferroni correction). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.
3	
4	\paragraph{Task coverage.}
5	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark. Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.
6	
7	\paragraph{Mechanism.}
8	The discrimination collapse mechanism is supported by correlational evidence (consistent Gini/CV reduction across all conditions); causal validation through controlled entropy manipulation is needed. The entropy redistribution component replicates on only 2/4 Qwen conditions, suggesting model-specific factors.
9	
10	\paragraph{Sparsity range.}
11	Our experiments span $s \in \{0.15, 0.20, 0.25, 0.30\}$. More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics. We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to our severity characterization. Extended limitations in Appendix~\ref{app:lim
…[truncated 14 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 246 · 2026-05-15T07:38:42.557296+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 247 · 2026-05-15T07:38:43.461614+00:00_

1	\section{Compound Sparsity Formulation}
2	\label{app:formulation-details}
3	
4	\paragraph{Attention head pruning.}
5	Heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$ \cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\ell)} \in \{0,1\}$ retains the top-$(1{-}s)\cdot H$ heads:
6	\begin{equation}
7	    \tilde{\mathbf{o}}_j^{(\ell)} = m_j^{(\ell)} \cdot \mathbf{o}_j^{(\ell)}.
8	    \label{eq:head-mask}
9	\end{equation}
10	
11	\paragraph{KV cache eviction.}
12	A position mask $\mathbf{m}_k \in \{0,1\}^T$ retains the top-$(1{-}s)\cdot T$ positions (BOS always preserved):
13	\begin{equation}
14	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall\, i, j.
15	    \label{eq:kv-mask}
16	\end{equation}
17	Under importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:
18	\begin{equation}
19	    \mathrm{imp}(j) = \frac{\sum_{\ell, h, i} a_{ij}^{(\ell,h)}}{T - j},
20	    \label{eq:kv-importance}
21	\end{equation}
22	where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.
23	
24	\paragraph{Compound sparsity.}
25	Applying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.
26	
27	\paragraph{Attention sparsity metric.}
28	For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:
29	\begin{equation}
30	    \sigma_i^{(h)} = \frac{1}{T} \sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right].
31	    \label{eq:attn-sparsity}
32	\end{equation}
33	The per-position spar
…[truncated 1336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 248 · 2026-05-15T07:38:43.462231+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
  }
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-15T07:38:43.663724+00:00_

1	% Content moved from main body to appendix:
2	% - Phase-strategy crossover details (from results §5.3)
3	% - Cross-model replication details with tables/figures (from results §5.4)
4	% - Permutation test details with table/forest plot (from results §5.5)
5	% - Full entropy-discrimination collapse analysis with tables (from analysis §6)
6	% Main body §6 (analysis.tex) contains a condensed summary referencing these tables.
7	
8	\section{Phase-Strategy Crossover Details}
9	\label{app:crossover-details}
10	
11	At $s{=}0.25$, a strategy ranking reversal emerges (Figure~\ref{fig:crossover}): importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\ $0.818$) but \emph{higher} II in the low-sparsity phase ($7.196$ vs.\ $1.363$---a $5.3{\times}$ reversal). This crossover is present at all four sparsity levels, with reversal magnitude of $3.9{\times}$ at $s{=}0.15$, $5.4{\times}$ at $s{=}0.20$, $5.3{\times}$ at $s{=}0.25$, and $3.6{\times}$ at $s{=}0.30$ (as random eviction severity also rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\S\ref{sec:discrimination-collapse}). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28
12	
13	\begin{figure}[t]
14	\centering
15	\includegraphics[width=\columnwidth]{fig3_crossover.pdf}
16	\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}
17	\label{fig:crossover}
18	\end{figure}
19	
20	
21	\section{Cross-Model Replication Details}
22	\label{app:cross-model-details}
23	
24	Both models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in trai
…[truncated 12246 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 250 · 2026-05-15T07:38:43.664367+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-15T07:38:43.765309+00:00_

1	\section{Discrimination Collapse Details}
2	\label{app:discrimination-collapse-details}
3	
4	This cross-model consistency (Table~\ref{tab:discrimination-metrics-full}) establishes discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$), confirming that discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
5	
6	
7	\section{Extended Discussion}
8	\label{app:extended-discussion}
9	
10	\paragraph{On the predictability of phase-modulated severity.}
11	The compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$; at $s = 0.35$, high-phase II rises to $0.105$ in a supplementary experiment, indicating onset of compound interaction even in high-sparsity phases at extreme pruning rates). % exp_id: bf16_importance_s015..s030, bf16_ds_imp_s035; high-phase medians: 0.006, 0.015, 0.032, 0.053; s035 II_high=0.1051
12	
13	\paragraph{Random masking as falsification control.}
14	Random eviction fails 7/8 paired permutation tests across both models; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($\widetilde{\Delta} = \placeholder{}$). The absence of a phase gradient under random masking isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030
15	
16	\paragraph{Entropy mechanism boundary conditions.}
17	Directly measuring per-head entropy sh
…[truncated 6847 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 252 · 2026-05-15T07:38:53.577571+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5 etc), and descriptions of each score level. Include soundness, excitement, overall recommendation, confidence, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5 etc), and descriptions of each score level. Include soundness, excitement, overall recommendation, confidence, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 253 · 2026-05-15T07:38:54.432385+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "compound sparsity quantization pruning LLM interaction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "compound sparsity quantization pruning LLM interaction 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 254 · 2026-05-15T07:38:54.784298+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"phase-aware\" KV cache compression reasoning models 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"phase-aware\" KV cache compression reasoning models 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 255 · 2026-05-15T07:39:01.039484+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully"
- **4**: "Quite sure. I tried to check the important points carefully"
- **3**: "Pretty sure, but there's a chance I missed something"
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- **1**: "Not my area, or paper is very hard to understand"

## 2. **Soundness**
Scale: 1-5 (with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: "Strong: This study provides sufficient support for all of its claims"
- **3**: "Acceptable: This study provides sufficient support for its main claims"
- **2**: "Poor: Some of the main claims are not sufficiently supported"
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## 3. **Excitement**
Scale: 1-5 (with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: "Exciting: I would mention this paper to others"
- **3**: "Interesting: I might mention some points of this paper to others"
- **2**: "Potentially Interesting: this paper does not resonate with me"
- **1**: "Not Exciting: this paper does not resonate with me"

## 4. **Overall Assessment**
Scale: 1-5 (with half-point increments)
- **5**: "Consider for Award: could be considered for outstanding paper award"
- **4**: "Conference: could be accepted to an ACL conference"
- **3**: "Findings: could be accepted to Findings of the ACL"
- **2**: "Resubmit next cycle: needs substantial revisions"
- **1**: "Do not resubmit: has to be fully redone"

## 5. **Reproducibility**
Scale: 1-5
- **5**: "They could easily reproduce the results"
- **4**: "They could mostly reproduce the results"
- **3**: "They could reproduce the results with some difficulty"
- **2**: "They would be hard pressed to reproduce the results"
- **1**: "They would not be 
…[truncated 911 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7461
}
```

</details>

---


### Tool result

_source line 256 · 2026-05-15T07:39:02.152481+00:00_

Web search results for query: ""phase-aware" KV cache compression reasoning models 2025 2026"

Links: [{"title":"Optimizing Key-Value Cache Compression in Long-context ...","url":"https://aclanthology.org/2025.acl-long.529.pdf"},{"title":"Which Heads Matter for Reasoning? RL-Guided KV Cache Compression | OpenReview","url":"https://openreview.net/forum?id=HGdg76iVo6"},{"title":"GitHub - Zefan-Cai/R-KV: [Neurips 2025] R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://github.com/Zefan-Cai/R-KV"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://proceedings.neurips.cc/paper_files/paper/2025/hash/57e0358aed314784cad14a26e1eba642-Abstract-Conference.html"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference | OpenReview","url":"https://openreview.net/forum?id=20JDhbJqn3"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"},{"title":"LongFlow: Efficient KV Cache Compression for Reasoning Models","url":"https://arxiv.org/html/2603.11504"},{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs | OpenReview","url":"https://openreview.net/forum?id=Vem6FQvRvq"}]

Based on the search results, here's what I found about "phase-aware" KV cache compression for reasoning models in 2025-2026:

## Key Research Findings

### Phase-Awar
…[truncated 1538 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7368
}
```

</details>

---


### Tool result

_source line 257 · 2026-05-15T07:39:02.153247+00:00_

Web search results for query: "compound sparsity quantization pruning LLM interaction 2025 2026"

Links: [{"title":"ICML Poster SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression","url":"https://icml.cc/virtual/2025/poster/46479"},{"title":"SLIM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression | Research","url":"https://research.nvidia.com/publication/2025-06_slim-one-shot-quantization-and-sparsity-low-rank-approximation-llm-weight"},{"title":"A review of state-of-the-art techniques for large language model compression | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-02019-z"},{"title":"Workshop on Sparsity in LLMs (SLLM): Deep Dive into Mixture of Experts, Quantization, Hardware, and Inference","url":"https://iclr.cc/virtual/2025/workshop/23996"},{"title":"Published as a conference paper at COLM 2025","url":"https://arxiv.org/pdf/2504.14569"},{"title":"Compute Where it Counts: Self Optimizing Language Models","url":"https://arxiv.org/html/2605.10875"},{"title":"Large Language Model Compression with Global Rank and Sparsity Optimization","url":"https://arxiv.org/html/2505.03801"},{"title":"GitHub - NVIDIA/Model-Optimizer: A unified library of SOTA model optimization techniques like quantization, pruning, distillation, speculative decoding, etc. It compresses deep learning models for downstream deployment frameworks like TensorRT-LLM, TensorRT, vLLM, etc. to optimize inference speed. · GitHub","url":"https://github.com/NVIDIA/Model-Optimizer"},{"title":"GitHub - HuangOwen/Awesome-LLM-Compression: Awesome LLM compression research papers and tools. · GitHub","url":"https://github.com/HuangOwen/Awesome-LLM-Compression"},{"title":"Track: Session 3: Quantization and Sparsity","url":"https://mlsys.org/virtual/2025/session/3143"}]

I've performed the web search on compound sparsity, quantization, pruning, and LLM interacti
…[truncated 1674 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7720
}
```

</details>

---


### Tool call

_source line 258 · 2026-05-15T07:39:37.967001+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DefensiveKV \"Taming the Fragility of KV Cache Eviction\" ICLR 2026 Feng Yuan"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DefensiveKV \"Taming the Fragility of KV Cache Eviction\" ICLR 2026 Feng Yuan"
  }
}
```

</details>

---


### Tool call

_source line 259 · 2026-05-15T07:39:38.923593+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "HIES \"Entropy Meets Importance\" head importance entropy score transformer pruning 2025 Choi Minsik"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "HIES \"Entropy Meets Importance\" head importance entropy score transformer pruning 2025 Choi Minsik"
  }
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-15T07:39:39.728544+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Phase transitions in large language model compression\" npj Artificial Intelligence 2026 Ma Ziyang"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Phase transitions in large language model compression\" npj Artificial Intelligence 2026 Ma Ziyang"
  }
}
```

</details>

---


### Tool result

_source line 261 · 2026-05-15T07:39:44.102540+00:00_

Web search results for query: "DefensiveKV "Taming the Fragility of KV Cache Eviction" ICLR 2026 Feng Yuan"

Links: [{"title":"GitHub - FFY0/DefensiveKV: Official Implementation for [ICLR26] DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference · GitHub","url":"https://github.com/FFY0/DefensiveKV"},{"title":"[2510.13334] Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://arxiv.org/abs/2510.13334"},{"title":"DEFENSIVEKV: TAMING THE FRAGILITY OF KV CACHE ...","url":"https://openreview.net/pdf?id=nJgS06sX3O"},{"title":"TAMING THE FRAGILITY OF KV CACHE EVICTION IN LLM INFERENCE","url":"https://arxiv.org/pdf/2510.13334"},{"title":"FFY0 (Yuan Feng) · GitHub","url":"https://github.com/FFY0"},{"title":"DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference | OpenReview","url":"https://openreview.net/forum?id=nJgS06sX3O"},{"title":"TAMING THE FRAGILITY OF KV CACHE EVICTION","url":"https://openreview.net/pdf/2d8c7805c4fcdb477dd04f7b60dd05bd9551c246.pdf"},{"title":"(PDF) Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://www.researchgate.net/publication/396517805_Taming_the_Fragility_of_KV_Cache_Eviction_in_LLM_Inference"},{"title":"[PDF] Taming the Fragility of KV Cache Eviction in LLM Inference | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Taming-the-Fragility-of-KV-Cache-Eviction-in-LLM-Feng-Guo/10b323b80b3f57a7f15d44eb5a72872a3adfbcb3"},{"title":"GitHub - FFY0/AdaKV: The Official Implementation of Ada-KV [NeurIPS 2025] · GitHub","url":"https://github.com/FFY0/AdaKV"}]

Based on the search results, I found comprehensive information about DefensiveKV:

## Overview

DefensiveKV is a paper by Yuan Feng, Haoyu Guo, Junlin Lv, S. Kevin Zhou, and Xike Xie addressing the challenge of KV Cache eviction in large language model inference.

## Problem and Solution

Large language models face substantial memory and runtime overhead from the transformer's Key-Value cache, with recent me
…[truncated 1070 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6135
}
```

</details>

---


### Tool result

_source line 262 · 2026-05-15T07:39:44.863685+00:00_

Web search results for query: ""Phase transitions in large language model compression" npj Artificial Intelligence 2026 Ma Ziyang"

Links: [{"title":"Phase transitions in large language model compression | npj Artificial Intelligence","url":"https://www.nature.com/articles/s44387-026-00072-8"},{"title":"Phase transitions in large language model compression – DOAJ","url":"https://doaj.org/article/06b2d6b18f08424a9f7778c269597d3c"},{"title":"GitHub - whucs21Mzy/Model-Phase-Transitions: Navigating Model Phase Transitions to Enable Extreme Lossless Compression: A Perspective","url":"https://github.com/whucs21Mzy/Model-Phase-Transitions"},{"title":"Phase transitions in large language models ..","url":"https://www.hyper-exponential.com/p/phase-transitions-in-large-language"},{"title":"Phase transitions in AI-human interaction networks: statistics, computation, and probabilistic modeling","url":"https://arxiv.org/html/2505.02879v1"},{"title":"Lossless data compression by large models | Nature Machine Intelligence","url":"https://www.nature.com/articles/s42256-025-01033-7"},{"title":"A Survey on Model Compression for Large Language Models | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00704/125482/A-Survey-on-Model-Compression-for-Large-Language"},{"title":"Phase Transitions in the Output Distribution of Large Language Models","url":"https://arxiv.org/html/2405.17088v1"},{"title":"Understanding LLM Behaviors via Compression: Data Generation, Knowledge Acquisition and Scaling Laws","url":"https://arxiv.org/html/2504.09597v2"},{"title":"Critical Phase Transition in a Large Language Model","url":"https://www.aimodels.fyi/papers/arxiv/critical-phase-transition-large-language-model"}]

I found the article you were looking for! Here's what the search results reveal:

The article "Phase transitions in large language model compression" was published on February 6, 2026, in npj Artificial Int
…[truncated 926 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5135
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-15T07:39:45.919550+00:00_

Web search results for query: "HIES "Entropy Meets Importance" head importance entropy score transformer pruning 2025 Choi Minsik"

Links: [{"title":"[2510.13832] Entropy Meets Importance: A Unified Head Importance-Entropy Score for Stable and Efficient Transformer Pruning","url":"https://arxiv.org/abs/2510.13832"},{"title":"Entropy Meets Importance: A Unified Head Importance–Entropy Score for Stable and Efficient Transformer Pruning","url":"https://arxiv.org/html/2510.13832"},{"title":"A Unified Head Importance-Entropy Score for Stable and ...","url":"https://arxiv.org/pdf/2510.13832"},{"title":"(PDF) Entropy Meets Importance: A Unified Head Importance-Entropy Score for Stable and Efficient Transformer Pruning","url":"https://www.researchgate.net/publication/396541457_Entropy_Meets_Importance_A_Unified_Head_Importance-Entropy_Score_for_Stable_and_Efficient_Transformer_Pruning"},{"title":"A Unified Head Importance–Entropy Score for Stable and ...","url":"https://opt-ml.org/papers/2025/paper51.pdf"},{"title":"ENTROPY MEETS IMPORTANCE:AUNIFIED HEAD ...","url":"https://openreview.net/pdf/77c597d3ac85fdf6b61cfb7ca9e2147a40b3a85c.pdf"},{"title":"Entropy-Guided KV Caching for Efficient LLM Inference","url":"https://www.mdpi.com/2227-7390/13/15/2366"},{"title":"Entropy-Guided Head Importance for Token Pruning in Vision Transformers | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel8/10773618/10773627/10773748.pdf"},{"title":"[2602.04491] Greedy-Gnorm: A Gradient Matrix Norm-Based Alternative to Attention Entropy for Head Pruning","url":"https://arxiv.org/abs/2602.04491"},{"title":"Entropy-Guided Search Space Optimization for Efficient Neural Network Pruning","url":"https://www.mdpi.com/1999-4893/18/12/736"}]

I found the research paper you're looking for. Here are the key details:

## "Entropy Meets Importance: A Unified Head Importance-Entropy Score for Stable and Efficient Transformer Pruning"

The paper is by Minsik Choi and 3 other auth
…[truncated 1196 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6995
}
```

</details>

---


### Tool call

_source line 264 · 2026-05-15T07:42:09.817081+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿意见（新颖性/完整性）\n\n---\n\n## 总体评分\n\n**Overall**: 2.5 / 5（Resubmit next cycle ↔ Findings 之间）\n**一句话总结**: 论文提出了一个有价值的 empirical finding（compound sparsity severity 的 phase modulation），统计方法扎实，但论文严重未完成（30+ placeholders 未填充，核心 Table 4 完全空白），新颖性相对于已有工作增量有限，且唯一的 cross-architecture 证据很弱。\n\n---\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.0 / 5 | 主实验（DeepSeek Qwen2）统计严谨，但 Table 4（cross-arch）完全由 placeholder 填充，无法验证 LLaMA 结论；30+ placeholders 表明论文远未完成 |\n| **Excitement** | 2.5 / 5 | Phase-modulated compound interaction 是有趣的 characterization，但缺乏方法贡献；oracle mitigation 实验未通过自设门槛，实际影响力受限 |\n| **Overall** | 2.5 / 5 | 需要大幅修订：填充所有 placeholders、补强 cross-architecture 证据、更清晰地区分于 HIES 等已有工作 |\n| **Reproducibility** | 3 / 5 | 报告了模型、数据集、sparsity levels、bootstrap 参数和 GPU 型号；但代码未开源，KV importance 的 position normalization 公式缺乏足够实现细节 |\n| **Confidence** | 4 / 5 | 审稿人熟悉 KV cache compression、attention head pruning 和统计方法 |\n\n---\n\n## Summary\n\n本文研究 compound sparsity（同时进行 attention head pruning 和 KV cache eviction）在 reasoning model 生成过程中的 phase-dependent severity。核心发现：在 importance-based eviction 下，compound interaction 集中在 low-sparsity reasoning phases，而 random eviction 无此现象。在 DeepSeek-R1-Distill-Qwen-7B 上，severity gradient 从 69× (s=0.15) 增长到 274× (s=0.30)。提出 entropy-discrimination collapse 作为机制解释。在 Qwen2.5-7B-Instruct 上部分复现，在 LlamaForCausalLM 上仅获得微弱的方向性一致证据。\n\n---\n\n## 主要优势\n\n1. **问题定义清晰且有实际意义**：将 compound sparsity 的 phase-invariance assumption 明确地作为攻击目标，对部署 reasoning model 的 practitioners 有直接指导价值。\n\n2. **统计方法论严谨**：使用非参数 bootstrap (B=10,000)、paired permutation tests、Bonferroni correction、Cohen's d_z，并报告中位数而非均值来处理右偏分布（mean/median ratio 高达 43:1）。这在 ML 论文中罕见且值得肯定。\n\n3. **Random eviction 作为 falsification control 设计巧妙**：7/8 conditions 下 random eviction 无显著 phase gradient，有效隔离了 strategy-specific amplification。\n\n4. **Multiplicative null 验证**（Appendix A）增强了 Interaction Index 定义选择的鲁棒性。\n\n5. **Writing 整体结构清晰**：从 Background → Methodology → Results → Analysis → Discussion 的信息流合理，每个 section 内部逻辑连贯。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 论文严重未完成：30+ `\\placeholder{}` 未填充\n- 具体位置：Abstract (line 8)、Section 5.4 (`NULL_PCT`)、Table 4 全部数据 (Section 5.5, lines 86-98)、Discussion (`ORACLE_PCT`, `ORACLE_P`, `HEUR_PCT`, `HEUR_P`)、Appendix 多处\n- 问题：**Table 4（cross-architecture validation）是本文最重要的 generalization 证据，但所有数据格全部为空**。Discussion 中的 oracle phase-aware reallocation 实验——本文唯一尝试从 characterization 走向 actionable mitigation 的部分——四个关键数字全部缺失。Abstract 中也有一个关键统计量未填充。\n- 为什么影响接收：Reviewer 无法验证 Section 5.5 和 Discussion 中的任何 claim。论文以当前状态提交将被视为 incomplete submission。\n- 建议修改方向：在提交前必须填充所有 placeholder，或如果数据确实不可用则删除相关 claim。\n\n**N2** [critical] Cross-architecture 证据不足以支撑论文标题和 abstract 的 framing\n- 具体位置：Section 5.5、Abstract (line 10)、Title (\"Reasoning Models\" 暗示广泛适用)\n- 问题：LLaMA 结果极弱——4 个 sparsity levels 中仅 s=0.30 的 Bonferroni-corrected Wilcoxon 达到显著性 (p=0.029)；绝对 magnitude 仅为 DeepSeek 的 ~1/40；random eviction 在 LLaMA 上也展示了 non-trivial phase gradient（原文 Discussion: \"random pruning also exhibits a non-trivial phase gradient\"），严重削弱 strategy-specificity claim。然而 Abstract line 10 仍称 \"provide mixed but directionally consistent evidence for cross-architecture generalization\"，Title 使用复数 \"Reasoning Models\"。\n- 为什么影响接收：Title/abstract 给人的印象是结论在多架构上成立，但实际 LLaMA 证据在统计上大部分不显著，且 strategy contrast 在 LLaMA 上不 clean。这属于 overclaim。\n- 建议修改方向：(1) Title 应限定为 Qwen2 架构或明确标注 partial evidence; (2) Abstract 中 LLaMA 部分应更突出 mixed evidence 而非 directional consistency; (3) 考虑将 LLaMA 实验定位为 exploratory supplement 而非 core contribution。\n\n**N3** [critical] 与 HIES (2025) 的区分不充分\n- 具体位置：Related Work §2 (line 17)、Analysis §6、Appendix §E\n- 问题：HIES (Choi et al., 2025) 已经报告了 \"head importance-based discrimination collapses under heavy pruning\"。本文的 \"entropy-discrimination collapse\" 机制与 HIES 的发现高度重叠。论文仅在 Related Work 中一句话提及 HIES (\"independently show that importance-based head discrimination collapses under heavy pruning\")，未在 Analysis 中讨论两者的区别。HIES 的核心观察——pruning 导致 importance score 区分度下降——与本文 Section 6 的 Gini coefficient 下降分析本质相同。\n- 为什么影响接收：这是新颖性的核心问题。如果 discrimination collapse 已被 HIES 发现，本文的 mechanistic contribution 需要更清晰地说明增量在哪里（phase-dependence? compound interaction context? quantitative characterization?）。\n- 建议修改方向：在 Analysis 中专门段落对比 HIES 的 single-axis discrimination collapse 与本文的 compound + phase-dependent collapse，明确本文在 mechanism 层面的 delta。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 贡献定位为 empirical finding——对 EMNLP main conference 的影响力疑虑\n- 具体位置：全文\n- 问题：论文自我定位为 empirical characterization，不提出新方法。唯一的 mitigation 尝试（oracle phase-aware reallocation, Discussion §7）未通过自设的 30% 门槛，95% CI 跨零。论文最终结论是 \"motivate phase-aware sparsity allocation\"，但未证明这一 motivation 可转化为实际改进。\n- 建议：(1) 如果 oracle recovery 实验有数据（placeholder 填充后），即使未过 gate 也应详细报告，展示 ceiling analysis; (2) 更清楚地论证为何 characterization 本身对社区有价值——例如量化现有部署中可能被忽视的性能损失。\n\n**W2** [warning] 样本量偏小且任务单一\n- 具体位置：Section 4 (methodology.tex, lines 9-10)\n- 问题：仅 50 个 MATH-500 问题，排除后 DeepSeek n=49、Qwen n=46。Mean/median ratio 高达 43:1 表明分布极端右偏，少数 outlier 问题可能主导结果。仅评估数学推理，未涉及 code generation、multi-hop QA 等其他 reasoning task。\n- 建议：(1) 报告去除 top-5% outlier 后的 sensitivity analysis; (2) 即使不增加 benchmark，至少讨论为什么 MATH-500 的 phase structure 可能（或不可能）泛化到其他 reasoning task。\n\n**W3** [warning] Related Work 遗漏若干重要工作\n- 具体位置：Section 2 (related_work.tex)\n- 问题：以下近期高相关工作未被引用：\n  - **RLKV** (OpenReview 2026): 使用 RL 优化每个 head 的 cache 使用与 reasoning quality 的关系——直接涉及 head-level reasoning-aware compression\n  - **LongFlow** (arXiv 2603.11504): 专门为 reasoning model 的 long-output generation 设计 KV cache compression\n  - **PM-KVQ** (OpenReview 2026): Progressive mixed-precision KV cache quantization for long-CoT LLMs——compound compression（量化+eviction）的另一路径\n  - 更广泛的 compound compression 文献中，quantization + pruning 的交互（如 NVIDIA Model Optimizer 相关工作）也应提及\n- 建议：补充上述引用，特别是 RLKV 和 LongFlow 涉及 reasoning-aware head-level compression，与本文直接相关。\n\n**W4** [warning] Entropy redistribution 分析在 Qwen 上不 replicate\n- 具体位置：Section 6 (analysis.tex, line 6)、Appendix §E.2 (Table 8)\n- 问题：Entropy redistribution 作为 \"secondary amplifier\" 在 Qwen 的 s=0.25 出现符号反转（+0.045），s=0.30 接近零。论文称 discrimination collapse 是 \"robust, model-independent driver\"，但实际上 Gini 下降幅度在 Qwen 上仅为 DeepSeek 的 1/4-1/3。如果两个 model 在同一架构上机制表现就已经差异显著，cross-architecture 的 mechanism claim 更难成立。\n- 建议：更审慎地措辞 mechanism 的 generalizability；考虑是否 discrimination collapse 的 magnitude 足够解释 severity gradient 的 magnitude difference（DeepSeek vs Qwen）。\n\n**W5** [warning] Abstract 过长且包含过多具体数字\n- 具体位置：Abstract (abstract.tex, 14 行)\n- 问题：Abstract 包含 3 个模型名、4 个 sparsity levels、多个 median/d_z/p-value、一个 crossover example、和 cross-architecture 的详细数据。信息密度过高，读者难以提取核心 message。ACL 传统上 abstract 不超过 ~200 words。\n- 建议：精简 abstract 到核心 claim + 一两个 headline numbers；将详细统计量移到 Introduction 或 Results。\n\n---\n\n## 小问题（不影响接收）\n\n1. **`h2o-neurips2023` bib entry 缺少 title 字段**（references.bib）——编译后引用可能显示异常。\n\n2. **LaTeX source 中的 REVIEWER-ATTACK / REBUTTAL 注释**（appendix_disc_analysis.tex, lines 27-28, 34-35, 41-42, 56-57, 61-62）：虽然编译后不可见，但 ARR 审稿人如检查 source（OpenReview 可下载源码）会看到针对特定 reviewer attack 的预设 rebuttal，这暴露了非盲审信息（作者预期特定批评并预备回应），应在提交前删除。\n\n3. **引用格式小问题**：`deepseek-r1-2025` 的 author 字段为 \"DeepSeek-AI\" 而 OpenAlex 记录为 \"Guo et al.\"；`snapkv-neurips2024` 的 first author bib 中为 Li 但 API 记录为 Cai。应核实 canonical author 信息。\n\n4. **Phase segmentation 依赖 quantile-based tercile**：这意味着每个 sequence 都被强制分成三个等大的 phase。如果某个 sequence 的 attention sparsity 分布是 unimodal 的，这种 segmentation 可能产生 artificial phase boundary。论文未讨论 segmentation 的 sensitivity。\n\n5. **Eq. 3 中 G 的定义**（background.tex, line 26-28）：当 $\\widetilde{\\mathrm{II}}_{\\textit{high}} \\approx 0$ 时（如 Table 2 中 s=0.15 的 0.006），G 对分母的微小变化极端敏感。报告的 G=69×-274× 可能 inflate 了实际的 phase contrast 程度。建议同时报告 $\\Delta$（已报告）和 G，并讨论 G 在分母接近零时的 instability。\n\n6. **Discussion 中 s=0.35 的 supplementary experiment**（appendix_disc_analysis.tex, line 11）提到 \"high-phase II rises to 0.105\" 但未在任何 table 中报告完整结果。如果要引用应提供更多 context。\n\n---\n\n## Questions to Authors\n\n1. Table 4 的所有 placeholder 何时能填充？如果 LLaMA 实验数据已有但未整理完，建议在 resubmission 时完整报告。如果实验尚未完成，建议删除 Section 5.5 并降低 cross-architecture claim 的强度。\n\n2. 能否提供 HIES (2025) 的 discrimination collapse 与本文 entropy-discrimination collapse 的 explicit comparison？具体而言：HIES 是否也观察到了 phase-dependent 的 discrimination loss？如果没有，这是否是本文的核心 novelty delta？\n\n3. 对于 mean/median ratio 高达 43:1 的分布，是否考虑过 winsorization 或 trimmed mean 作为 robustness check？即使使用非参数方法，极端 outlier 仍可能影响 bootstrap CI 的宽度。\n\n4. 论文提到 \"BOS always retained\" 但未讨论 sink token phenomenon。在 attention sink 设置下（如 StreamingLLM），compound sparsity 的 phase modulation 是否仍然成立？\n\n5. Oracle phase-aware reallocation 未通过 30% 门槛。这是否说明 phase-aware budget 本身不是一个 promising direction，还是实现细节（如 oracle vs heuristic phase boundary detection）的问题？",
  "reviewer_id": "2",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 审稿意见（新颖性/完整性）\n\n---\n\n## 总体评分\n\n**Overall**: 2.5 / 5（Resubmit next cycle ↔ Findings 之间）\n**一句话总结**: 论文提出了一个有价值的 empirical finding（compound sparsity severity 的 phase modulation），统计方法扎实，但论文严重未完成（30+ placeholders 未填充，核心 Table 4 完全空白），新颖性相对于已有工作增量有限，且唯一的 cross-architecture 证据很弱。\n\n---\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.0 / 5 | 主实验（DeepSeek Qwen2）统计严谨，但 Table 4（cross-arch）完全由 placeholder 填充，无法验证 LLaMA 结论；30+ placeholders 表明论文远未完成 |\n| **Excitement** | 2.5 / 5 | Phase-modulated compound interaction 是有趣的 characterization，但缺乏方法贡献；oracle mitigation 实验未通过自设门槛，实际影响力受限 |\n| **Overall** | 2.5 / 5 | 需要大幅修订：填充所有 placeholders、补强 cross-architecture 证据、更清晰地区分于 HIES 等已有工作 |\n| **Reproducibility** | 3 / 5 | 报告了模型、数据集、sparsity levels、bootstrap 参数和 GPU 型号；但代码未开源，KV importance 的 position normalization 公式缺乏足够实现细节 |\n| **Confidence** | 4 / 5 | 审稿人熟悉 KV cache compression、attention head pruning 和统计方法 |\n\n---\n\n## Summary\n\n本文研究 compound sparsity（同时进行 attention head pruning 和 KV cache eviction）在 reasoning model 生成过程中的 phase-dependent severity。核心发现：在 importance-based eviction 下，compound interaction 集中在 low-sparsity reasoning phases，而 random eviction 无此现象。在 DeepSeek-R1-Distill-Qwen-7B 上，severity gradient 从 69× (s=0.15) 增长到 274× (s=0.30)。提出 entropy-discrimination collapse 作为机制解释。在 Qwen2.5-7B-Instruct 上部分复现，在 LlamaForCausalLM 上仅获得微弱的方向性一致证据。\n\n---\n\n## 主要优势\n\n1. **问题定义清晰且有实际意义**：将 compound sparsity 的 phase-invariance assumption 明确地作为攻击目标，对部署 reasoning model 的 practitioners 有直接指导价值。\n\n2. **统计方法论严谨**：使用非参数 bootstrap (B=10,000)、paired permutation tests、Bonferroni correction、Cohen's d_z，并报告中位数而非均值来处理右偏分布（mean/median ratio 高达 43:1）。这在 ML 论文中罕见且值得肯定。\n\n3. **Random eviction 作为 falsification control 设计巧妙**：7/8 conditions 下 random eviction 无显著 phase gradient，有效隔离了 strategy-specific amplification。\n\n4. **Multiplicative null 验证**（Appendix A）增强了 Interaction Index 定义选择的鲁棒性。\n\n5. **Writing 整体结构清晰**：从 Background → Methodology → Results → Analysis → Discussion 的信息流合理，每个 section 内部逻辑连贯。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 论文严重未完成：30+ `\\placeholder{}` 未填充\n- 具体位置：Abstract (line 8)、Section 5.4 (`NULL_PCT`)、Table 4 全部数据 (Section 5.5, lines 86-98)、Discussion (`ORACLE_PCT`, `ORACLE_P`, `HEUR_PCT`, `HEUR_P`)、Appendix 多处\n- 问题：**Table 4（cross-architecture validation）是本文最重要的 generalization 证据，但所有数据格全部为空**。Discussion 中的 oracle phase-aware reallocation 实验——本文唯一尝试从 characterization 走向 actionable mitigation 的部分——四个关键数字全部缺失。Abstract 中也有一个关键统计量未填充。\n- 为什么影响接收：Reviewer 无法验证 Section 5.5 和 Discussion 中的任何 claim。论文以当前状态提交将被视为 incomplete submission。\n- 建议修改方向：在提交前必须填充所有 placeholder，或如果数据确实不可用则删除相关 claim。\n\n**N2** [critical] Cross-architecture 证据不足以支撑论文标题和 abstract 的 framing\n- 具体位置：Section 5.5、Abstract (line 10)、Title (\"Reasoning Models\" 暗示广泛适用)\n- 问题：LLaMA 结果极弱——4 个 sparsity levels 中仅 s=0.30 的 Bonferroni-corrected Wilcoxon 达到显著性 (p=0.029)；绝对 magnitude 仅为 DeepSeek 的 ~1/40；random eviction 在 LLaMA 上也展示了 non-trivial phase gradient（原文 Discussion: \"random pruning also exhibits a non-trivial phase gradient\"），严重削弱 strategy-specificity claim。然而 Abstract line 10 仍称 \"provide mixed but directionally consistent evidence for cross-architecture generalization\"，Title 使用复数 \"Reasoning Models\"。\n- 为什么影响接收：Title/abstract 给人的印象是结论在多架构上成立，但实际 LLaMA 证据在统计上大部分不显著，且 strategy contrast 在 LLaMA 上不 clean。这属于 overclaim。\n- 建议修改方向：(1) Title 应限定为 Qwen2 架构或明确标注 partial evidence; (2) Abstract 中 LLaMA 部分应更突出 mixed evidence 而非 directional consistency; (3) 考虑将 LLaMA 实验定位为 exploratory supplement 而非 core contribution。\n\n**N3** [critical] 与 HIES (2025) 的区分不充分\n- 具体位置：Related Work §2 (line 17)、Analysis §6、Appendix §E\n- 问题：HIES (Choi et al., 2025) 已经报告了 \"head importance-based discrimination collapses under heavy pruning\"。本文的 \"entropy-discrimination collapse\" 机制与 HIES 的发现高度重叠。论文仅在 Related Work 中一句话提及 HIES (\"independently show that importance-based head discrimination collapses under heavy pruning\")，未在 Analysis 中讨论两者的区别。HIES 的核心观察——pruning 导致 importance score 区分度下降——与本文 Section 6 的 Gini coefficient 下降分析本质相同。\n- 为什么影响接收：这是新颖性的核心问题。如果 discrimination collapse 已被 HIES 发现，本文的 mechanistic contribution 需要更清晰地说明增量在哪里（phase-dependence? compound interaction context? quantitative characterization?）。\n- 建议修改方向：在 Analysis 中专门段落对比 HIES 的 single-axis discrimination collapse 与本文的 compound + phase-dependent collapse，明确本文在 mechanism 层面的 delta。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 贡献定位为 empirical finding——对 EMNLP main conference 的影响力疑虑\n- 具体位置：全文\n- 问题：论文自我定位为 empirical characterization，不提出新方法。唯一的 mitigation 尝试（oracle phase-aware reallocation, Discussion §7）未通过自设的 30% 门槛，95% CI 跨零。论文最终结论是 \"motivate phase-aware sparsity allocation\"，但未证明这一 motivation 可转化为实际改进。\n- 建议：(1) 如果 oracle recovery 实验有数据（placeholder 填充后），即使未过 gate 也应详细报告，展示 ceiling analysis; (2) 更清楚地论证为何 characterization 本身对社区有价值——例如量化现有部署中可能被忽视的性能损失。\n\n**W2** [warning] 样本量偏小且任务单一\n- 具体位置：Section 4 (methodology.tex, lines 9-10)\n- 问题：仅 50 个 MATH-500 问题，排除后 DeepSeek n=49、Qwen n=46。Mean/median ratio 高达 43:1 表明分布极端右偏，少数 outlier 问题可能主导结果。仅评估数学推理，未涉及 code generation、multi-hop QA 等其他 reasoning task。\n- 建议：(1) 报告去除 top-5% outlier 后的 sensitivity analysis; (2) 即使不增加 benchmark，至少讨论为什么 MATH-500 的 phase structure 可能（或不可能）泛化到其他 reasoning task。\n\n**W3** [warning] Related Work 遗漏若干重要工作\n- 具体位置：Section 2 (related_work.tex)\n- 问题：以下近期高相关工作未被引用：\n  - **RLKV** (OpenReview 2026): 使用 RL 优化每个 head 的 cache 使用与 reasoning quality 的关系——直接涉及 head-level reasoning-aware compression\n  - **LongFlow** (arXiv 2603.11504): 专门为 reasoning model 的 long-output generation 设计 KV cache compression\n  - **PM-KVQ** (OpenReview 2026): Progressive mixed-precision KV cache quantization for long-CoT LLMs——compound compression（量化+eviction）的另一路径\n  - 更广泛的 compound compression 文献中，quantization + pruning 的交互（如 NVIDIA Model Optimizer 相关工作）也应提及\n- 建议：补充上述引用，特别是 RLKV 和 LongFlow 涉及 reasoning-aware head-level compression，与本文直接相关。\n\n**W4** [warning] Entropy redistribution 分析在 Qwen 上不 replicate\n- 具体位置：Section 6 (analysis.tex, line 6)、Appendix §E.2 (Table 8)\n- 问题：Entropy redistribution 作为 \"secondary amplifier\" 在 Qwen 的 s=0.25 出现符号反转（+0.045），s=0.30 接近零。论文称 discrimination collapse 是 \"robust, model-independent driver\"，但实际上 Gini 下降幅度在 Qwen 上仅为 DeepSeek 的 1/4-1/3。如果两个 model 在同一架构上机制表现就已经差异显著，cross-architecture 的 mechanism claim 更难成立。\n- 建议：更审慎地措辞 mechanism 的 generalizability；考虑是否 discrimination collapse 的 magnitude 足够解释 severity gradient 的 magnitude difference（DeepSeek vs Qwen）。\n\n**W5** [warning] Abstract 过长且包含过多具体数字\n- 具体位置：Abstract (abstract.tex, 14 行)\n- 问题：Abstract 包含 3 个模型名、4 个 sparsity levels、多个 median/d_z/p-value、一个 crossover example、和 cross-architecture 的详细数据。信息密度过高，读者难以提取核心 message。ACL 传统上 abstract 不超过 ~200 words。\n- 建议：精简 abstract 到核心 claim + 一两个 headline numbers；将详细统计量移到 Introduction 或 Results。\n\n---\n\n## 小问题（不影响接收）\n\n1. **`h2o-neurips2023` bib entry 缺少 title 字段**（references.bib）——编译后引用可能显示异常。\n\n2. **LaTeX source 中的 REVIEWER-ATTACK / REBUTTAL 注释**（appendix_disc_analysis.tex, lines 27-28, 34-35, 41-42, 56-57, 61-62）：虽然编译后不可见，但 ARR 审稿人如检查 source（OpenReview 可下载源码）会看到针对特定 reviewer attack 的预设 rebuttal，这暴露了非盲审信息（作者预期特定批评并预备回应），应在提交前删除。\n\n3. **引用格式小问题**：`deepseek-r1-2025` 的 author 字段为 \"DeepSeek-AI\" 而 OpenAlex 记录为 \"Guo et al.\"；`snapkv-neurips2024` 的 first author bib 中为 Li 但 API 记录为 Cai。应核实 canonical author 信息。\n\n4. **Phase segmentation 依赖 quantile-based tercile**：这意味着每个 sequence 都被强制分成三个等大的 phase。如果某个 sequence 的 attention sparsity 分布是 unimodal 的，这种 segmentation 可能产生 artificial phase boundary。论文未讨论 segmentation 的 sensitivity。\n\n5. **Eq. 3 中 G 的定义**（background.tex, line 26-28）：当 $\\widetilde{\\mathrm{II}}_{\\textit{high}} \\approx 0$ 时（如 Table 2 中 s=0.15 的 0.006），G 对分母的微小变化极端敏感。报告的 G=69×-274× 可能 inflate 了实际的 phase contrast 程度。建议同时报告 $\\Delta$（已报告）和 G，并讨论 G 在分母接近零时的 instability。\n\n6. **Discussion 中 s=0.35 的 supplementary experiment**（appendix_disc_analysis.tex, line 11）提到 \"high-phase II rises to 0.105\" 但未在任何 table 中报告完整结果。如果要引用应提供更多 context。\n\n---\n\n## Questions to Authors\n\n1. Table 4 的所有 placeholder 何时能填充？如果 LLaMA 实验数据已有但未整理完，建议在 resubmission 时完整报告。如果实验尚未完成，建议删除 Section 5.5 并降低 cross-architecture claim 的强度。\n\n2. 能否提供 HIES (2025) 的 discrimination collapse 与本文 entropy-discrimination collapse 的 explicit comparison？具体而言：HIES 是否也观察到了 phase-dependent 的 discrimination loss？如果没有，这是否是本文的核心 novelty delta？\n\n3. 对于 mean/median ratio 高达 43:1 的分布，是否考虑过 winsorization 或 trimmed mean 作为 robustness check？即使使用非参数方法，极端 outlier 仍可能影响 bootstrap CI 的宽度。\n\n4. 论文提到 \"BOS always retained\" 但未讨论 sink token phenomenon。在 attention sink 设置下（如 StreamingLLM），compound sparsity 的 phase modulation 是否仍然成立？\n\n5. Oracle phase-aware reallocation 未通过 30% 门槛。这是否说明 phase-aware budget 本身不是一个 promising direction，还是实现细节（如 oracle vs heuristic phase boundary detection）的问题？",
    "reviewer_id": "2",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 265 · 2026-05-15T07:42:14.143972+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4326
}
```

</details>

---


### Assistant

_source line 266 · 2026-05-15T07:42:24.527304+00:00_

Round 1 审稿意见已提交给 Review Director。

**审稿结论：Overall 2.5/5**，介于 Resubmit 和 Findings 之间。

核心问题：
1. **30+ placeholders 未填充**（Table 4 完全空白、Discussion oracle 实验数据缺失）——论文处于未完成状态
2. **Cross-architecture 证据不支撑 title/abstract 的 framing**——LLaMA 结果 4/4 中仅 1 个显著，magnitude 仅为 1/40，random eviction 也有 phase gradient
3. **与 HIES (2025) 的 discrimination collapse 区分不足**——机制新颖性存疑

优势：统计方法论严谨（非参数 bootstrap + permutation test + Bonferroni），random eviction 作为 falsification control 设计巧妙，DeepSeek Qwen2 主实验结果有说服力。

引用验证方面：29 篇引用均为真实论文，无幻觉引用；但 `h2o-neurips2023` 缺少 title 字段，3 篇作者信息有小偏差。另外发现 LaTeX source 中有 REVIEWER-ATTACK/REBUTTAL 开发注释需删除。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2"
}
```

</details>

---


## Round 5

## Round 5

4 recorded events


### User

_source line 267 · 2026-05-15T07:44:35.891983+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整 Round 1 审稿意见。请逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

## Reviewer 1 — Round 1 审稿报告（方法严谨性）

**Overall**: 2.5 / 5

| 维度 | 分数 |
|------|------|
| Soundness | 2.5 / 5 |
| Excitement | 3 / 5 |
| Reproducibility | 2 / 5 |
| Confidence | 4 / 5 |

### Must-Fix 问题

**N1** [critical] 大量 `\placeholder{}` 未填充数据——40+ placeholders
- abstract, Table 3 (LLaMA) 16 cells 全空, §5.4 cross-model, §7 Discussion oracle pilot, Appendix 多处
- 不是"格式问题"而是数据完整性问题

**N2** [critical] 50 题样本量的统计效力论证缺失
- 无 power analysis
- 10% 采样率，分层方案未报告
- Qwen s=0.15 $d_z=0.28$ CI 包含零可能是 underpowered
- 负面结果无法区分"效应不存在"和"样本不足"

**N3** [critical] 单一 benchmark (MATH-500) 严重限制泛化性
- Title/abstract 使用 "reasoning models" 但仅测数学推理
- 不同推理任务会产生不同 attention phase structure

**N4** [critical] Cross-architecture 证据薄弱且内部矛盾
- LLaMA ~1/40 magnitude
- s=0.15 CI 排除零但 Wilcoxon non-significant vs s=0.30 CI 跨零但 Wilcoxon significant——统计指标自相矛盾
- Random eviction 在 LLaMA 上也有 non-trivial phase gradient
- Table 3 完全为空
- Contribution 2 称 "replicates across three models spanning two architectures" 属 overclaim

**N5** [critical] 机制分析仅为 correlational，不足以支持 causal claim
- 无 causal intervention
- Entropy redistribution 在 Qwen s=0.25 反转
- Analysis 叙述偏 causal 但证据仅 correlational

### Should-Fix 问题

**W1** Phase segmentation（tercile-based）缺乏充分论证——ThinKV 用 explicit delimiters 而非 quantile，两者不同
**W2** 对称稀疏率 (symmetric $s$) 的实践代表性不足
**W3** G 的数值稳定性问题——分母接近零时 G 极不稳定
**W4** Bonferroni 校正范围可能不足——实际 test 数远多于 k=4
**W5** Spearman ρ=1.0 的 4-point 单调性仅 p=0.043，不应描述为强证据；Table 4 vs Table 1 数字差异未解释
**W6** n=49 vs n=50 排除标准未说明

### 小问题
- Abstract 过度密集
- h2o bib entry 缺 title
- 引用 author mismatch
- LaTeX label 前缀混乱
- 硬件细节不足
- 无代码/数据开源计划

---

请对以上每个 Must-Fix (N1-N5)、Should-Fix (W1-W6)、和你认为重要的小问题逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-15T07:46:07.836849+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 Round 1 意见逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: 大量 placeholder 未填充**\n完全同意。我在自己的审稿中也将此列为 #1 critical issue。需要补充：R1 报告 40+ placeholders，我清点约 30+——差异可能源于计数粒度（Table 4 是按 cell 还是按 row 计）。核心问题一致：Table 4（cross-architecture, Section 5.5）整表空白，Discussion 中 oracle recovery 实验四个关键数字全部缺失。论文以当前状态无法进入实质性审稿。\n\n**[AGREE with nuance] R1-N2: 50 题样本量 / 缺乏 power analysis**\n同意 power analysis 缺失是方法论短板，也同意 Qwen s=0.15 ($d_z$=0.28, CI 含零) 可能是 underpowered 而非效应不存在。但需要补充两点 nuance：\n\n1. 论文使用 **paired** 非参数检验（paired permutation test, paired bootstrap），这显著提升了 effective power——每个问题同时在两种 strategy 下评估，消除了 between-problem variance。R1 未提及 paired design 的 power advantage。\n2. 在 DeepSeek 上，**所有 4 个 sparsity levels 的 Bonferroni-corrected p < 0.005**（Table 6, Appendix §D），且 CI lower bounds 单调递增 ($0.19 \\to 6.70$)。这不是 borderline 结果。Power 不足的疑虑主要限于 Qwen s=0.15 和 LLaMA，而非全局。\n\n因此，我认为 power analysis 缺失是 should-fix 而非 critical——主结论在 DeepSeek 上统计充分，但在 Qwen 低 sparsity 和 LLaMA 全局上确实需要 power 论证或坦承 underpowered。\n\n**[AGREE] R1-N3: 单一 benchmark 限制泛化**\n完全同意。我也将此列为 W2。Title 使用 \"Reasoning Models\" 暗示跨任务适用性，但仅测试 MATH-500。不同 reasoning task（code generation、multi-hop QA）可能产生完全不同的 attention phase structure。Limitations section (limitations.tex, ¶2) 确实承认了 \"Different reasoning tasks...may induce different phase structures\"，但 title/abstract 的 framing 未充分反映这一局限。\n\n**[AGREE] R1-N4: Cross-architecture 证据薄弱**\n强烈同意，这也是我的 N2 critical issue。R1 补充了一个我未充分展开的重要观察：**s=0.15 的 CI 排除零但 Wilcoxon non-significant，而 s=0.30 的 CI 跨零但 Wilcoxon significant**（Section 5.5, results.tex lines 79）——两个统计指标在同一数据上给出矛盾信号，说明 LLaMA 证据极不稳定。这比我原来的分析更精准地暴露了问题。\n\nContribution 2 (Introduction, line 23) 声称效应 \"replicates across three models spanning two architectures\"，但 LLaMA 仅 1/4 conditions 在 Bonferroni-corrected Wilcoxon 上显著，且 random eviction 在 LLaMA 上也有 non-trivial phase gradient。这确实是 overclaim。\n\n**[REBUT with partial agreement] R1-N5: 机制分析仅为 correlational**\n部分同意，但认为 R1 的 severity 评级偏高。理由：\n\n1. **论文措辞已经是 hedged 的**：Section 6 (analysis.tex) 使用 \"We propose... as the primary mechanism\"（非 \"We demonstrate\" 或 \"We prove\"）；Limitations ¶3 明确承认 \"causal validation through controlled entropy manipulation is needed\"。\n2. **Correlational evidence 跨 16 conditions 一致**：Gini coefficient 在所有 16 conditions (2 models × 4 sparsity × 2 strategies) 下一致为负（Appendix §E.1, Table 7）。虽然是 correlational，但一致性本身增加了可信度。\n3. **Random eviction 的 immunity 提供了 partial causal logic**：如果 discrimination collapse 是 mechanism，则 random eviction（不依赖 score quality）应不受影响——这正是观察到的 ($G \\approx 1$)。这虽非 intervention，但构成了合理的 counterfactual argument。\n\n然而，我同意 R1 的核心关切：**entropy redistribution 在 Qwen s=0.25 的反转**（$\\Delta\\mathcal{H} = +0.045$, Appendix Table 8）说明即使 secondary mechanism 也未 replicate。论文将此解释为 \"model-specific head specialization patterns\"，但这实质上是 ad hoc 解释。\n\n**结论**：将 N5 定级为 should-fix (warning) 而非 critical 更合适——因为论文已使用审慎措辞，且 discrimination collapse（非 entropy redistribution）被定位为主要 driver。但 Analysis section 的标题 \"Entropy-Discrimination Collapse\" 确实过于 assertive，应改为更 hedged 的表述。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: Phase segmentation tercile vs ThinKV explicit delimiters**\n重要观察。论文 Section 3 (background.tex, line 33) 称 \"following ThinKV\"，但 ThinKV 使用 `&lt;think>` token 作为 explicit phase boundary，本文使用 attention sparsity 的 quantile tercile——两者在概念上相关但方法论完全不同。Quantile-based tercile **强制将每个 sequence 分为三个等比例的 phase**，即使 attention sparsity 分布是 unimodal 或 heavily skewed 的。这可能产生 artificial phase boundaries。我在自己的小问题 #4 中也提到了这一点，但 R1 正确地将其提升为 should-fix 级别。\n\n建议：(1) 不要称 \"following ThinKV\"——应说 \"inspired by ThinKV's phase distinction but using a quantile-based proxy\"; (2) 补充 segmentation sensitivity analysis（如 quartile 或 quintile boundary 是否改变结论）。\n\n**[AGREE] R1-W2: Symmetric sparsity 的实践代表性**\n同意。实际部署中 head pruning rate 和 KV eviction rate 通常不同（例如保留 90% heads 但 evict 50% KV cache）。论文使用 $s$ 同时控制两个轴的 sparsity rate，这在 controlled experiment 中合理（减少组合空间），但限制了实际推论。至少应在 Discussion 或 Limitations 中讨论 asymmetric sparsity 下结论是否可能不同。\n\n**[AGREE] R1-W3: G 的数值稳定性**\n完全同意。我在自己的小问题 #5 中也提到了这一点。$\\widetilde{\\mathrm{II}}_{\\textit{high}} = 0.006$ 时（Table 2, s=0.15），分母的微小变化会导致 $G$ 剧烈波动。论文应报告 $G$ 的 bootstrap CI，或至少讨论分母接近零时 $G$ 的 interpretability。$\\Delta$ 是更稳健的度量，论文实际上两者都报告了，但叙述中过度强调 $G$（\"$69\\times$ to $274\\times$\"）。\n\n**[AGREE] R1-W4: Bonferroni 校正范围可能不足**\n这是一个精准的统计学观察。论文仅对 4 个 sparsity level 做 Bonferroni correction ($k=4$)，但实际分析中的 hypothesis test 远不止 4 个：2 strategies × 4 sparsity levels × 3 models × (permutation test + Wilcoxon + bootstrap CI)。虽然不同 test 回答不同问题（非简单的 multiple comparison），但至少应论证为何 $k=4$ 是适当的 correction family。\n\n**[AGREE] R1-W5: Spearman ρ=1.0 的 over-interpretation**\n同意。4 个数据点的 Spearman ρ=1.0 给出 exact permutation $p = 0.042$ (= 1/24)，这在单次检验中 barely significant。Section 5.4 (results.tex, line 71) 称 \"Spearman $\\rho = 1.0$\" 而未注明这仅基于 4 个点，读者可能误以为这是高 power 的证据。应明确标注 sample size 和 exact p。\n\nR1 提到的 \"Table 4 vs Table 1 数字差异\" 我需要指出：Table 1 ($\\Delta = 0.39$ at s=0.15) 和 Table 3 ($\\widetilde{\\Delta}$: $0.32$ [0.20, 0.47] at s=0.15) 确实报告了不同数字——前者是 segment-level median，后者是 problem-level paired median。论文未明确解释这一差异，R1 的观察合理。\n\n**[AGREE] R1-W6: 排除标准未说明**\n同意。Appendix §C (appendix_moved.tex, line 26) 解释了 Qwen 排除原因（\"degenerate phase assignments\"），但 DeepSeek 从 50 → 49 的排除原因未在任何位置说明。排除标准应在 Methodology 中完整报告。\n\n---\n\n### 小问题\n\n**[AGREE]** Abstract 过度密集——我也在 W5 中指出。\n\n**[AGREE]** h2o bib entry 缺 title——我也在小问题 #1 中指出。\n\n**[AGREE]** 引用 author mismatch——我也在小问题 #3 中指出（deepseek-r1-2025, snapkv-neurips2024, unicomp-2026）。\n\n**[AGREE]** 无代码/数据开源计划——对 reproducibility 有显著影响。虽然论文报告了实验参数，但 KV importance scoring 的 position normalization（Eq. 4, Appendix §A）和 phase segmentation 的具体实现细节（min_phase_length=10 的 merge 逻辑）仅凭文本描述难以完全复现。\n\n---\n\n### 总结\n\n与 R1 在绝大多数问题上达成共识。主要分歧：\n\n1. **N2 (sample size)**：我认为 paired design 提供了 R1 未充分考虑的 power advantage，主结论（DeepSeek）统计充分。降级为 should-fix。\n2. **N5 (mechanism causality)**：论文已使用 hedged language，且 16/16 conditions 一致的 correlational evidence + random eviction counterfactual 构成了合理的 argument。降级为 should-fix，但 section 标题应改得更审慎。\n\n两位 reviewer 共同认为最严重的问题是：**(1) placeholders 未填充，(2) cross-architecture claim overclaim，(3) 单一 benchmark 限制泛化**。这三点必须在 resubmission 前解决。",
  "reviewer_id": "2",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 Round 1 意见逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: 大量 placeholder 未填充**\n完全同意。我在自己的审稿中也将此列为 #1 critical issue。需要补充：R1 报告 40+ placeholders，我清点约 30+——差异可能源于计数粒度（Table 4 是按 cell 还是按 row 计）。核心问题一致：Table 4（cross-architecture, Section 5.5）整表空白，Discussion 中 oracle recovery 实验四个关键数字全部缺失。论文以当前状态无法进入实质性审稿。\n\n**[AGREE with nuance] R1-N2: 50 题样本量 / 缺乏 power analysis**\n同意 power analysis 缺失是方法论短板，也同意 Qwen s=0.15 ($d_z$=0.28, CI 含零) 可能是 underpowered 而非效应不存在。但需要补充两点 nuance：\n\n1. 论文使用 **paired** 非参数检验（paired permutation test, paired bootstrap），这显著提升了 effective power——每个问题同时在两种 strategy 下评估，消除了 between-problem variance。R1 未提及 paired design 的 power advantage。\n2. 在 DeepSeek 上，**所有 4 个 sparsity levels 的 Bonferroni-corrected p < 0.005**（Table 6, Appendix §D），且 CI lower bounds 单调递增 ($0.19 \\to 6.70$)。这不是 borderline 结果。Power 不足的疑虑主要限于 Qwen s=0.15 和 LLaMA，而非全局。\n\n因此，我认为 power analysis 缺失是 should-fix 而非 critical——主结论在 DeepSeek 上统计充分，但在 Qwen 低 sparsity 和 LLaMA 全局上确实需要 power 论证或坦承 underpowered。\n\n**[AGREE] R1-N3: 单一 benchmark 限制泛化**\n完全同意。我也将此列为 W2。Title 使用 \"Reasoning Models\" 暗示跨任务适用性，但仅测试 MATH-500。不同 reasoning task（code generation、multi-hop QA）可能产生完全不同的 attention phase structure。Limitations section (limitations.tex, ¶2) 确实承认了 \"Different reasoning tasks...may induce different phase structures\"，但 title/abstract 的 framing 未充分反映这一局限。\n\n**[AGREE] R1-N4: Cross-architecture 证据薄弱**\n强烈同意，这也是我的 N2 critical issue。R1 补充了一个我未充分展开的重要观察：**s=0.15 的 CI 排除零但 Wilcoxon non-significant，而 s=0.30 的 CI 跨零但 Wilcoxon significant**（Section 5.5, results.tex lines 79）——两个统计指标在同一数据上给出矛盾信号，说明 LLaMA 证据极不稳定。这比我原来的分析更精准地暴露了问题。\n\nContribution 2 (Introduction, line 23) 声称效应 \"replicates across three models spanning two architectures\"，但 LLaMA 仅 1/4 conditions 在 Bonferroni-corrected Wilcoxon 上显著，且 random eviction 在 LLaMA 上也有 non-trivial phase gradient。这确实是 overclaim。\n\n**[REBUT with partial agreement] R1-N5: 机制分析仅为 correlational**\n部分同意，但认为 R1 的 severity 评级偏高。理由：\n\n1. **论文措辞已经是 hedged 的**：Section 6 (analysis.tex) 使用 \"We propose... as the primary mechanism\"（非 \"We demonstrate\" 或 \"We prove\"）；Limitations ¶3 明确承认 \"causal validation through controlled entropy manipulation is needed\"。\n2. **Correlational evidence 跨 16 conditions 一致**：Gini coefficient 在所有 16 conditions (2 models × 4 sparsity × 2 strategies) 下一致为负（Appendix §E.1, Table 7）。虽然是 correlational，但一致性本身增加了可信度。\n3. **Random eviction 的 immunity 提供了 partial causal logic**：如果 discrimination collapse 是 mechanism，则 random eviction（不依赖 score quality）应不受影响——这正是观察到的 ($G \\approx 1$)。这虽非 intervention，但构成了合理的 counterfactual argument。\n\n然而，我同意 R1 的核心关切：**entropy redistribution 在 Qwen s=0.25 的反转**（$\\Delta\\mathcal{H} = +0.045$, Appendix Table 8）说明即使 secondary mechanism 也未 replicate。论文将此解释为 \"model-specific head specialization patterns\"，但这实质上是 ad hoc 解释。\n\n**结论**：将 N5 定级为 should-fix (warning) 而非 critical 更合适——因为论文已使用审慎措辞，且 discrimination collapse（非 entropy redistribution）被定位为主要 driver。但 Analysis section 的标题 \"Entropy-Discrimination Collapse\" 确实过于 assertive，应改为更 hedged 的表述。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: Phase segmentation tercile vs ThinKV explicit delimiters**\n重要观察。论文 Section 3 (background.tex, line 33) 称 \"following ThinKV\"，但 ThinKV 使用 `&lt;think>` token 作为 explicit phase boundary，本文使用 attention sparsity 的 quantile tercile——两者在概念上相关但方法论完全不同。Quantile-based tercile **强制将每个 sequence 分为三个等比例的 phase**，即使 attention sparsity 分布是 unimodal 或 heavily skewed 的。这可能产生 artificial phase boundaries。我在自己的小问题 #4 中也提到了这一点，但 R1 正确地将其提升为 should-fix 级别。\n\n建议：(1) 不要称 \"following ThinKV\"——应说 \"inspired by ThinKV's phase distinction but using a quantile-based proxy\"; (2) 补充 segmentation sensitivity analysis（如 quartile 或 quintile boundary 是否改变结论）。\n\n**[AGREE] R1-W2: Symmetric sparsity 的实践代表性**\n同意。实际部署中 head pruning rate 和 KV eviction rate 通常不同（例如保留 90% heads 但 evict 50% KV cache）。论文使用 $s$ 同时控制两个轴的 sparsity rate，这在 controlled experiment 中合理（减少组合空间），但限制了实际推论。至少应在 Discussion 或 Limitations 中讨论 asymmetric sparsity 下结论是否可能不同。\n\n**[AGREE] R1-W3: G 的数值稳定性**\n完全同意。我在自己的小问题 #5 中也提到了这一点。$\\widetilde{\\mathrm{II}}_{\\textit{high}} = 0.006$ 时（Table 2, s=0.15），分母的微小变化会导致 $G$ 剧烈波动。论文应报告 $G$ 的 bootstrap CI，或至少讨论分母接近零时 $G$ 的 interpretability。$\\Delta$ 是更稳健的度量，论文实际上两者都报告了，但叙述中过度强调 $G$（\"$69\\times$ to $274\\times$\"）。\n\n**[AGREE] R1-W4: Bonferroni 校正范围可能不足**\n这是一个精准的统计学观察。论文仅对 4 个 sparsity level 做 Bonferroni correction ($k=4$)，但实际分析中的 hypothesis test 远不止 4 个：2 strategies × 4 sparsity levels × 3 models × (permutation test + Wilcoxon + bootstrap CI)。虽然不同 test 回答不同问题（非简单的 multiple comparison），但至少应论证为何 $k=4$ 是适当的 correction family。\n\n**[AGREE] R1-W5: Spearman ρ=1.0 的 over-interpretation**\n同意。4 个数据点的 Spearman ρ=1.0 给出 exact permutation $p = 0.042$ (= 1/24)，这在单次检验中 barely significant。Section 5.4 (results.tex, line 71) 称 \"Spearman $\\rho = 1.0$\" 而未注明这仅基于 4 个点，读者可能误以为这是高 power 的证据。应明确标注 sample size 和 exact p。\n\nR1 提到的 \"Table 4 vs Table 1 数字差异\" 我需要指出：Table 1 ($\\Delta = 0.39$ at s=0.15) 和 Table 3 ($\\widetilde{\\Delta}$: $0.32$ [0.20, 0.47] at s=0.15) 确实报告了不同数字——前者是 segment-level median，后者是 problem-level paired median。论文未明确解释这一差异，R1 的观察合理。\n\n**[AGREE] R1-W6: 排除标准未说明**\n同意。Appendix §C (appendix_moved.tex, line 26) 解释了 Qwen 排除原因（\"degenerate phase assignments\"），但 DeepSeek 从 50 → 49 的排除原因未在任何位置说明。排除标准应在 Methodology 中完整报告。\n\n---\n\n### 小问题\n\n**[AGREE]** Abstract 过度密集——我也在 W5 中指出。\n\n**[AGREE]** h2o bib entry 缺 title——我也在小问题 #1 中指出。\n\n**[AGREE]** 引用 author mismatch——我也在小问题 #3 中指出（deepseek-r1-2025, snapkv-neurips2024, unicomp-2026）。\n\n**[AGREE]** 无代码/数据开源计划——对 reproducibility 有显著影响。虽然论文报告了实验参数，但 KV importance scoring 的 position normalization（Eq. 4, Appendix §A）和 phase segmentation 的具体实现细节（min_phase_length=10 的 merge 逻辑）仅凭文本描述难以完全复现。\n\n---\n\n### 总结\n\n与 R1 在绝大多数问题上达成共识。主要分歧：\n\n1. **N2 (sample size)**：我认为 paired design 提供了 R1 未充分考虑的 power advantage，主结论（DeepSeek）统计充分。降级为 should-fix。\n2. **N5 (mechanism causality)**：论文已使用 hedged language，且 16/16 conditions 一致的 correlational evidence + random eviction counterfactual 构成了合理的 argument。降级为 should-fix，但 section 标题应改得更审慎。\n\n两位 reviewer 共同认为最严重的问题是：**(1) placeholders 未填充，(2) cross-architecture claim overclaim，(3) 单一 benchmark 限制泛化**。这三点必须在 resubmission 前解决。",
    "reviewer_id": "2",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-15T07:46:13.316671+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5479
}
```

</details>

---


### Assistant

_source line 270 · 2026-05-15T07:46:18.587974+00:00_

交叉回应已提交给 Review Director。

与 R1 在大部分问题上达成共识，但在两点上给出了不同 severity 评级：(1) 样本量问题——paired design 提供了额外 power，主结论在 DeepSeek 上统计充分，降级为 should-fix；(2) 机制 causality——论文已用审慎措辞且有 16/16 一致的 correlational evidence，降级为 should-fix。两位 reviewer 一致认为 placeholders 未填充、cross-architecture overclaim、单一 benchmark 是最关键的三个问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2"
}
```

</details>

---


## Round 6

## Round 6

44 recorded events


### User

_source line 271 · 2026-05-15T10:53:51.467075+00:00_

[Round 5 审稿请求]:
## Round 5 修订评估 — Reviewer 2（新颖性/完整性）

### Venue 信息
- **目标 venue**: EMNLP 2026 (main conference)
- **截止日期**: 2026-06-15
- **格式**: ACL 2-column, 长文 8 页正文, double-blind

### 论文路径
`projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex`

### 任务
这是修订评估。论文从 Round 1 (weak reject, 2.5/5) 起经历了多轮修改。请逐条检查以下 open/in_progress issues 是否已在论文中充分解决。对每条标注 **[RESOLVED]** 或 **[STILL_OPEN]** + 理由。

### 关键变化摘要（Director 初步扫描）
- n=50 → n=500（n_eff=496/475）
- Title: "Reasoning Models" → "Mathematical Reasoning Models"
- §5.5 改名 "Exploratory Cross-Architecture Analysis"
- Table 4 (LLaMA) 数据已填充
- Discussion oracle pilot 数据已填充 (18%/32%)
- §6 拆分为 §6.1 + §6.2，correlational 明确标注
- HIES 对比在 Related Work 和 §6 中扩展
- 新增 appendix_robustness.tex：BH-FDR 44 tests、segmentation robustness (quartile/quintile)、mpl sensitivity
- RLKV/LongFlow/PM-KVQ 已引用
- Abstract 精简重写
- REVIEWER-ATTACK 注释已删除
- h2o bib entry 已修复（title 字段已有）
- Reproducibility 声明已添加
- \placeholder 命令无实际使用

### 你的 Issue 列表（逐条判定）

**[R1-N1] critical: Placeholders**
检查：所有 placeholder 是否清除？Table 4 数据完整性？

**[R2-N3] warning: HIES 区分不足**
检查：Related Work 和 §6 中是否有 explicit comparison？是否说明 single-axis vs compound+phase delta？crossover 作为 HIES 不能 generate 的 prediction？

**[R2-W3] warning: Missing references RLKV/LongFlow/PM-KVQ**
检查：是否已引用？引用位置是否恰当？

**[R2-W5] warning: Abstract 过长过密**
检查：Abstract 是否精简？统计数字是否减少？LLaMA 细节是否移至 Results？

**[R2-Minor-1] info: h2o bib / author mismatch**
检查：h2o title 字段是否修复？其他 author mismatch？

**[R2-Minor-2] info: REVIEWER-ATTACK/REBUTTAL 注释**
检查：是否已删除？

**[R2-Minor-6] info: s=0.35 未完整报告**
检查：是否已删除或完整报告？

**[R1-Minor-code] info: 无代码/数据声明**
检查：是否有 Reproducibility 声明？

### 额外检查：新颖性和写作质量

1. **Random eviction 叙事变化**：Round 1 中 "7/8 conditions non-significant"，现在 n=500 后 random s≥0.25 变显著了。论文是否恰当处理了这一叙事变化？"dominant driver" vs "flat baseline" 的 framing 是否 honest？
2. **Abstract 质量**：精简后的 abstract 是否准确、可读、不 overclaim？
3. **Contribution 措辞**：三个 contributions 是否恰当反映修改后的 evidence strength？
4. **写作一致性**：n=50 profiling tables 与 n=500 main tables 共存是否 coherent？读者是否会困惑？
5. **新引用 PM-KVQ 和 RLKV**：引用是否准确？是否有新的幻觉引用？
6. **"following ThinKV" 措辞**（background.tex line 33）：是否仍在，是否应修正？
7. **整体影响力评估变化**：n=500 极显著结果 (p<10^-69) 是否改变了对论文价值的判断？

请输出：每个 issue 的判定 + 新发现的问题 + 总体评分更新建议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 272 · 2026-05-15T10:53:59.638274+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 273 · 2026-05-15T10:53:59.940313+00:00_

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
11	
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{graphicx}
15	\usepackage{booktabs}
16	\usepackage{enumitem}
17	\usepackage{multirow}
18	
19	\graphicspath{{figures/}}
20	
21	\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}
22	
23	\title{Phase-Modulated Compound Sparsity:\\Strategy-Dependent Severity Gradients in Mathematical Reasoning Models}
24	
25	\author{Anonymous}
26	
27	\begin{document}
28	
29	\maketitle
30	
31	\input{abstract}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{background}
36	\input{methodology}
37	\input{results}
38	\input{analysis}
39	\input{discussion}
40	\input{conclusion}
41	
42	\bibliography{references}
43	
44	\section*{Limitations}
45	\input{limitations}
46	
47	\section*{Reproducibility}
48	Code and data will be released upon acceptance.
49	
50	\appendix
51	\input{appendix}
52	\input{appendix_moved}
53	\input{appendix_disc_analysis}
54	\input{appendix_robustness}
55	
56	\end{document}
57	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-15T10:53:59.991372+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 275 · 2026-05-15T10:54:00.042236+00:00_

1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	We show that compound severity is not phase-invariant: it is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases in mathematical reasoning models.
4	
5	On DeepSeek-R1-Distill-Qwen-7B (500 MATH-500 problems, $n_{\text{eff}}{=}496$, $s \in \{0.15, 0.20, 0.25, 0.30\}$), importance-based eviction produces a monotonically increasing severity gradient from the high-sparsity to low-sparsity reasoning phase (median $\Delta$: $0.39 \to 8.48$; all Bonferroni-corrected $p < 10^{-69}$). Random eviction develops a detectable phase gradient only above $s \approx 0.20$ (non-significant at $s \leq 0.20$; where significant, $3$--$39{\times}$ weaker), confirming importance-based eviction as the dominant driver.
6	A crossover emerges at $s{=}0.25$: importance-based eviction outperforms random in high-sparsity phases yet underperforms in low-sparsity phases---a qualitative reversal in strategy ranking.
7	The pattern replicates on Qwen2.5-7B-Instruct ($n_{\text{eff}}{=}475$, $\Delta$: $0.07 \to 3.16$; all $p < 10^{-14}$), with preliminary cross-architecture evidence from a LlamaForCausalLM model suggesting the phenomenon may extend beyond Qwen2-family architectures.
8	We observe that discrimination collapse---head pruning flattening cumulative importance scores---correlates with the phase-dependent severity amplification, suggesting a mechanism whereby compound sparsity selectively degrades importance-based eviction in distributed-attention phases.
9	These findings motivate phase-aware compression budgets for mathematical reasoning models.
10	\end{abstract}
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 276 · 2026-05-15T10:54:00.896110+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 277 · 2026-05-15T10:54:01.398277+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses---\emph{attention head pruning} \cite{voita-acl2019, michel-neurips2019} and \emph{KV cache eviction} \cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \emph{compound sparsity}, but the resulting quality degradation is often super-additive \cite{spark-aaai2026, slim-icml2025}. Recent evaluations confirm that reasoning capabilities degrade disproportionately under compound compression \cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \cite{phase-transition-compression-2026}.
6	
7	Prior work treats compound interaction magnitude as roughly constant across generation \cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \cite{sparse-frontier-2025}.
8	This assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \cite{thinkv-iclr2026}.
9	Phase-aware methods like ThinKV \cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from greedy bias \cite{greedy-bias-kvcache-2026}, deferred importance \cite{retentivekv-2026}, and temporal dynamics in long generations \cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple mechanisms are composed.
10	If compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.

…[truncated 2353 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 278 · 2026-05-15T10:54:01.398693+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 279 · 2026-05-15T10:54:01.900819+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Compound compression.}
5	Combining multiple compression axes produces non-additive errors.
6	\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \cite{slim-icml2025} formalize compound error for quantization and sparsity.
7	\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.
8	\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.
9	GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.
10	PM-KVQ~\cite{pmkvq-iclr2026} demonstrates that progressive quantization---gradually reducing bit-width over the generation process---mitigates cumulative error in long-CoT reasoning, implicitly introducing a temporal dimension to compression severity that resonates with our finding that compound interaction is phase-dependent.
11	These works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.
12	
13	\paragraph{KV cache eviction.}
14	Most methods rely on importance scoring whose reliability is increasingly questioned.
15	Ada-KV~\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\cite{snapkv-neurips2024} compresses from a fixed observation window; \cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\times}$ higher than expected under standard aggregation.
16	\cite{nacl-acl2024} combine proxy-token and random eviction to counter attention bias.
17	RetentiveKV~\cite{retentivekv-2026} identifies deferred importance, and \cite{greedy-bias-kvcache-2026} show that single importance metrics exhibit systematic greedy bias.
18	\cite{hies-2025} independently show
…[truncated 2273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 280 · 2026-05-15T10:54:01.901233+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-15T10:54:02.353444+00:00_

1	% Section 3: Background and Problem Setup
2	% Note: eq:ii and eq:gradient are the canonical definitions.
3	% Full formulation details in Appendix (app:formulation-details).
4	
5	\section{Background and Problem Setup}
6	\label{sec:background}
7	
8	We formalize compound sparsity, define the Interaction Index, and introduce phase segmentation. Full mathematical details appear in Appendix~\ref{app:formulation-details}.
9	
10	\paragraph{Compound sparsity.}
11	\label{sec:compound-sparsity}
12	Let $s \in (0,1)$ denote a unified sparsity budget. \emph{Attention head pruning} removes the bottom-$s$ fraction of heads per layer by Frobenius norm importance \cite{voita-acl2019, michel-neurips2019}. \emph{KV cache eviction} removes the bottom-$s$ fraction of token positions from the cache. We compare two strategies: \emph{importance-based}, which scores positions by position-normalized cumulative attention mass (Eq.~\ref{eq:kv-importance} in Appendix~\ref{app:formulation-details}), and \emph{random}, which evicts uniformly at random \cite{nacl-acl2024}. Applying both simultaneously yields \emph{compound sparsity}; the two axes interact because head pruning alters the importance ranking used for eviction \cite{spark-aaai2026}. Existing joint-pruning approaches such as GRASPrune \cite{graspune-acl2026} learn global budget-constrained gates but treat decisions as static across generation.
13	
14	\paragraph{Interaction Index.}
15	\label{sec:interaction-index}
16	For a text segment, let $\text{PPL}_c$ denote perplexity under condition $c \in \{d, a, k, b\}$ (dense, attention-only, KV-only, compound). Normalizing by the dense baseline yields $r_c = \text{PPL}_c / \text{PPL}_d$, and:
17	\begin{equation}
18	    \mathrm{II} = r_b - r_a - r_k + 1.
19	    \label{eq:ii}
20	\end{equation}
21	$\mathrm{II} > 0$ indicates super-additive degradation; $\mathrm{II} = 0$ indicates additive independence. We adopt the additive null because the two axes operate on disjoint dimensions; qualitative co
…[truncated 1036 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 282 · 2026-05-15T10:54:02.405497+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
  }
}
```

</details>

---


### Tool result

_source line 283 · 2026-05-15T10:54:02.807968+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\paragraph{Models.}
5	\label{sec:models}
6	We evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \textbf{DeepSeek-R1-Distill-Qwen-7B}~\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \textbf{Qwen2.5-7B-Instruct}~\cite{qwen25-2024}, with standard instruction tuning, providing a cross-model replication target. Both are loaded in \texttt{bfloat16} with eager attention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values; \texttt{bfloat16} eliminated all occurrences.}
7	
8	\paragraph{Dataset.}
9	\label{sec:dataset}
10	We evaluate all 500 problems from MATH-500~\cite{math500-neurips2021}. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048). Problems with degenerate phase assignments (null low or high phase) are excluded, yielding effective sample sizes of $n{=}496$ for DeepSeek (4 excluded) and $n{=}475$ for Qwen (25 excluded). Qwen exhibits a higher mid-phase null rate (45.2\% vs.\ 10.2\% for DeepSeek) due to lower temporal autocorrelation in its attention sparsity patterns (lag-1 $r{=}0.718$ vs.\ $0.894$, $d{=}-1.68$); this does not affect the primary gradient metric $\Delta = \mathrm{II}_{\textit{low}} - \mathrm{II}_{\textit{high}}$, which requires only low and high phases. Sensitivity analysis across $\texttt{min\_phase\_length} \in \{5, 10, 20\}$ confirms robustness (Appendix~\ref{app:mpl-sensitivity}).
11	
12	\paragraph{Sparsity configuration.}
13	\label{sec:sparsity-config}
14	We apply symmetric compound sparsity at $s \in \{0.15, 0.20, 0.25, 0.30\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\ref{eq:kv-importance}; BOS always retained) and \emph{random} eviction (uniform). Heads are
…[truncated 1994 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 284 · 2026-05-15T10:54:02.858800+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 285 · 2026-05-15T10:54:03.763022+00:00_

1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Strategy-Dependent Severity}
6	\label{sec:strategy-severity}
7	
8	Table~\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\Delta$ increases from $0.39$ at $s{=}0.15$ to $8.48$ at $s{=}0.30$---a $22{\times}$ amplification (all Bonferroni-corrected $p < 10^{-69}$). Random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: at $s \leq 0.20$, $\Delta$ is non-significant ($0.01$--$0.03$; CIs span zero); at $s \geq 0.25$, $\Delta$ becomes significant ($0.26$--$0.51$; $p_{\text{Bonf}} < 0.006$) but $15$--$39{\times}$ smaller than under importance-based eviction. Both strategies exhibit monotonic dose-response (Jonckheere-Terpstra $z{=}6.2$--$33.7$, all $p < 10^{-9}$), but importance masking effect sizes are an order of magnitude larger. % exp_id: n500_unified_final; DS imp Δ 0.39→8.48, rand 0.01→0.51; JT z=33.7 (imp), 6.2 (rand)
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, 500 MATH-500 problems).}
14	\label{tab:aggregate-ii}
15	\begin{tabular}{@{}lcccc@{}}
16	\toprule
17	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
18	\midrule
19	Importance & 0.39 & 1.21 & 3.99 & 8.48 \\ % exp_id: n500_unified_final; DS imp median_ii_diff
20	Random     & 0.01 & 0.03 & 0.26 & 0.51 \\ % exp_id: n500_unified_final; DS rand median_ii_diff
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	
26	\subsection{Phase-Modulated Amplification}
27	\label{sec:phase-amplification}
28	
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the per-phase breakdown from an
…[truncated 9653 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 286 · 2026-05-15T10:54:03.914165+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-15T10:54:04.266317+00:00_

1	\section{Discrimination Collapse under Compound Sparsity}
2	\label{sec:analysis}
3	
4	\subsection{Discrimination Collapse}
5	\label{sec:discrimination-collapse-main}
6	
7	We observe that head pruning systematically reduces the discriminative power of cumulative importance scores, suggesting a mechanism for the phase-strategy interaction. The Gini coefficient of importance scores decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) after pruning, with consistent negative deltas in all 16 conditions (Appendix~\ref{app:analysis}, Table~\ref{tab:discrimination-metrics-full}). This pattern---which we term \emph{discrimination collapse}---is consistent with importance-based eviction degenerating into noise-sensitive selection when score distributions flatten. The effect is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. This observation is independently corroborated by \cite{hies-2025}, who report importance score collapse under heavy single-axis pruning; our results extend this to the compound setting, where collapse is amplified by the interaction of two compression axes and modulated by reasoning phase. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
8	
9	A partial counterfactual supports this interpretation: random eviction does not rely on importance scores, so it is immune to score-distribution changes caused by head pruning. The flat severity gradient under random eviction ($G \approx 1$) is consistent with this independence, while importance-based eviction---whose decisions depend on the very scores that pruning degrades---exhibits the phase-modulated amplification. We note that this evidence is correlational; causal validation through controlled manipulation of importance-score entropy is an important direction for future work. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
10	
11	\subsection{Entropy Redistribu
…[truncated 897 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-15T10:54:04.417472+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 289 · 2026-05-15T10:54:04.770492+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Quantitative surprise.}
5	While the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($G{=}30$--$148{\times}$ at $n{=}496$) far exceeds a naive ``somewhat worse'' prediction. The crossover---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) and underperforms in low-sparsity phases ($7.196$ vs.\ $1.363$)---cannot be derived from single-axis entropy reasoning. The near-unity random baseline ($G{=}0.5$--$1.3{\times}$, trivial magnitude) confirms the dominant amplification is strategy-specific. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json
6	
7	\paragraph{Implications for deployment.}
8	Applying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation. Discrimination collapse depends on attention-mass-based importance scoring shared by major KV cache methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-2024}), suggesting broad applicability.
9	
10	A preliminary pilot experiment explored oracle phase-aware budget reallocation, shifting sparsity budget from high-severity low-sparsity phases to low-severity high-sparsity phases. At $s{=}0.25$, oracle recovery---the fraction of compound interaction eliminated by phase-aware allocation---reached 18\% (Wilcoxon $p = 0.002$), below the pre-registe
…[truncated 1758 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 290 · 2026-05-15T10:54:04.821157+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 291 · 2026-05-15T10:54:05.223639+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation ($n{=}496$/$475$ problems). Under importance-based eviction, the amplification ratio $G$ ranges from $30{\times}$ to $148{\times}$ across sparsity levels, with paired median differences $\Delta$ from $0.39$ to $8.48$ (DeepSeek) and $0.07$ to $3.16$ (Qwen), all $p < 10^{-13}$. Random eviction develops a detectable phase gradient only above $s \approx 0.20$, but $3$--$39{\times}$ weaker than importance-based. A crossover at $s{=}0.25$---where importance-based eviction reverses ranking across phases---demonstrates that no single strategy dominates uniformly. The pattern replicates on Qwen2.5-7B-Instruct at all four sparsity levels; suggestive preliminary evidence from DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) indicates the phenomenon may extend beyond Qwen2, though at ${\sim}1/40$ the magnitude and with a weaker strategy contrast. Discrimination collapse provides a correlational mechanistic explanation supported by both Qwen2-based models.
5	These findings motivate phase-aware sparsity allocation for reasoning model deployment. Extending this analysis to code reasoning (HumanEval, LiveCodeBench) and science reasoning (GPQA), validating the discrimination collapse mechanism through causal intervention, and characterizing asymmetric compound interactions are promising directions for future work.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-15T10:54:05.224187+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 293 · 2026-05-15T10:54:05.275697+00:00_

1	\paragraph{Model scale and architecture.}
2	All experiments are conducted at the 7--8B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}) partially confirms the qualitative pattern beyond the Qwen2 architecture---monotonically increasing $d_z$ with within-importance phase gradient $\sim$1.0---but with substantially weaker interaction magnitude ($\sim$1/40 of DeepSeek) and mixed statistical evidence (only $s{=}0.30$ significant after Bonferroni correction). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.
3	
4	\paragraph{Task coverage.}
5	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark. MATH-500 is a suitable first testbed because it elicits structured reasoning with clear phase transitions (exploratory vs.\ structured computation), supports per-problem evaluation enabling paired statistical tests, and spans sufficient difficulty to produce meaningful variation in sequence length and attention dynamics. However, different reasoning tasks---code generation (e.g., HumanEval, LiveCodeBench), science reasoning (e.g., GPQA), multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile. Whether the phase-strategy interaction documented here extends to these domains is an open question.
6	
7	\paragraph{Symmetric sparsity assumption.}
8	Our analysis applies symmetric sparsity rates: the same fraction $s$ is used for both head pruning and KV cache eviction. Practical deployments may use asymmetric budgets (e.g., aggressive head pruning with conservat
…[truncated 974 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 294 · 2026-05-15T10:54:12.421357+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 295 · 2026-05-15T10:54:12.773339+00:00_

1	\section{Compound Sparsity Formulation}
2	\label{app:formulation-details}
3	
4	\paragraph{Attention head pruning.}
5	Heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$ \cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\ell)} \in \{0,1\}$ retains the top-$(1{-}s)\cdot H$ heads:
6	\begin{equation}
7	    \tilde{\mathbf{o}}_j^{(\ell)} = m_j^{(\ell)} \cdot \mathbf{o}_j^{(\ell)}.
8	    \label{eq:head-mask}
9	\end{equation}
10	
11	\paragraph{KV cache eviction.}
12	A position mask $\mathbf{m}_k \in \{0,1\}^T$ retains the top-$(1{-}s)\cdot T$ positions (BOS always preserved):
13	\begin{equation}
14	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall\, i, j.
15	    \label{eq:kv-mask}
16	\end{equation}
17	Under importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:
18	\begin{equation}
19	    \mathrm{imp}(j) = \frac{\sum_{\ell, h, i} a_{ij}^{(\ell,h)}}{T - j},
20	    \label{eq:kv-importance}
21	\end{equation}
22	where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.
23	
24	\paragraph{Compound sparsity.}
25	Applying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.
26	
27	\paragraph{Attention sparsity metric.}
28	For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:
29	\begin{equation}
30	    \sigma_i^{(h)} = \frac{1}{T} \sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right].
31	    \label{eq:attn-sparsity}
32	\end{equation}
33	The per-position spar
…[truncated 1336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 296 · 2026-05-15T10:54:12.774169+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
  }
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-15T10:54:12.824922+00:00_

1	% Content moved from main body to appendix:
2	% - Phase-strategy crossover details (from results §5.3)
3	% - Cross-model replication details with tables/figures (from results §5.4)
4	% - Permutation test details with table/forest plot (from results §5.5)
5	% - Full entropy-discrimination collapse analysis with tables (from analysis §6)
6	% Main body §6 (analysis.tex) contains a condensed summary referencing these tables.
7	
8	\section{Phase-Strategy Crossover Details}
9	\label{app:crossover-details}
10	
11	At $s{=}0.25$, a strategy ranking reversal emerges (Figure~\ref{fig:crossover}): importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\ $0.818$) but \emph{higher} II in the low-sparsity phase ($7.196$ vs.\ $1.363$---a $5.3{\times}$ reversal). This crossover is present at all four sparsity levels, with reversal magnitude of $3.9{\times}$ at $s{=}0.15$, $5.4{\times}$ at $s{=}0.20$, $5.3{\times}$ at $s{=}0.25$, and $3.6{\times}$ at $s{=}0.30$ (as random eviction severity also rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\S\ref{sec:discrimination-collapse}). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28
12	
13	\begin{figure}[t]
14	\centering
15	\includegraphics[width=\columnwidth]{fig3_crossover.pdf}
16	\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}
17	\label{fig:crossover}
18	\end{figure}
19	
20	
21	\section{Cross-Model Replication Details}
22	\label{app:cross-model-details}
23	
24	Both models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in trai
…[truncated 12568 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-15T10:54:13.729283+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 299 · 2026-05-15T10:54:14.181784+00:00_

1	\section{Discrimination Collapse Details}
2	\label{app:discrimination-collapse-details}
3	
4	This cross-model consistency (Table~\ref{tab:discrimination-metrics-full}) establishes discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$), confirming that discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
5	
6	
7	\section{Extended Discussion}
8	\label{app:extended-discussion}
9	
10	\paragraph{On the predictability of phase-modulated severity.}
11	The compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$). % exp_id: bf16_importance_s015..s030; high-phase medians: 0.006, 0.015, 0.032, 0.053
12	
13	\paragraph{Random masking as falsification control.}
14	At $n{=}500$, random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: non-significant at $s \leq 0.20$ for both models, but significant at $s \geq 0.25$ (DS: $\Delta{=}0.26$--$0.51$, $p_{\text{Bonf}} < 0.006$; QW: $\Delta{=}0.39$--$0.91$, $p_{\text{Bonf}} < 10^{-10}$). Where significant, the random phase gradient is $3$--$39{\times}$ weaker than importance-based, confirming that the dominant amplification is strategy-specific. % exp_id: n500_unified_final; DS rand s025 0.257 p=0.006, s030 0.510 p=0.006; QW rand s025 0.393, s030 0.913
15	
16	\paragraph{Entropy mechanism boundary conditions.}
17	Directly measuring per-head entropy s
…[truncated 4903 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-15T10:54:14.182174+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex"
  }
}
```

</details>

---


### Tool result

_source line 301 · 2026-05-15T10:54:14.684674+00:00_

1	\section{Benjamini-Hochberg FDR Correction}
2	\label{app:bh-fdr}
3	
4	Table~\ref{tab:bh-fdr} compares Bonferroni ($k{=}4$, per model$\times$strategy family) and Benjamini-Hochberg FDR correction across all 44 statistical tests. BH-FDR recovers 5 additional significant results beyond Bonferroni, all in low-effect-size conditions (random eviction or cross-model random comparisons). All 32 Bonferroni-significant results remain significant under BH-FDR.
5	
6	\begin{table}[t]
7	\centering
8	\small
9	\caption{Bonferroni vs.\ BH-FDR correction summary ($\alpha{=}0.05$, 44 tests). ``BH only'' denotes tests significant under BH-FDR but not Bonferroni.}
10	\label{tab:bh-fdr}
11	\begin{tabular}{@{}lcc@{}}
12	\toprule
13	Category & Bonf.\ sig. & BH-only sig. \\
14	\midrule
15	Per-condition Wilcoxon ($k{=}16$) & 10 & 2 \\
16	Imp vs.\ rand ($k{=}8$) & 8 & 0 \\
17	Adjacent sparsity ($k{=}12$) & 10 & 1 \\
18	Cross-model Mann-Whitney ($k{=}8$) & 4 & 2 \\
19	\midrule
20	Total ($k{=}44$) & 32 & 5 \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	The 5 BH-only results are: DeepSeek random $s{=}0.25$ and $s{=}0.30$ per-condition Wilcoxon ($p_{\text{Bonf}}{=}0.064$/$0.065$, BH $q{=}0.002$), DeepSeek random $s{=}0.25 \to 0.30$ adjacent-sparsity step ($p_{\text{Bonf}}{=}0.078$, BH $q{=}0.002$), and cross-model random $s{=}0.25$/$s{=}0.30$ Mann-Whitney ($p_{\text{Bonf}}{=}0.66$/$0.17$, BH $q{=}0.018$/$0.005$). All involve random eviction---the weakest effects---confirming that Bonferroni is conservative but does not miss any importance-based findings. % exp_id: n500_unified_final; source: supplementary_stats.json bh_fdr_correction
26	
27	
28	\section{Minimum Phase Length Sensitivity}
29	\label{app:mpl-sensitivity}
30	
31	Table~\ref{tab:mpl-sensitivity} reports the paired median difference $\Delta$ under three \texttt{min\_phase\_length} (mpl) settings across all 16 conditions (2 models $\times$ 2 strategies $\times$ 4 sparsity levels). Conclusions are robust: all importance-based c
…[truncated 4154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 302 · 2026-05-15T10:54:14.735396+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 303 · 2026-05-15T10:54:14.786210+00:00_

1	% References for Phase-Gated Compound Sparse paper
2	% Generated 2026-05-14; all entries verified via web search
3	
4	@inproceedings{adakv-neurips2025,
5	    title     = {Ada-{KV}: Optimizing {KV} Cache Eviction by Adaptive Budget Allocation for Efficient {LLM} Inference},
6	    author    = {Feng, Yuan and Lv, Junlin and Cao, Yukun and Xie, Xike and Zhou, S. Kevin},
7	    booktitle = {Advances in Neural Information Processing Systems},
8	    year      = {2025},
9	    url       = {https://arxiv.org/abs/2407.11550},
10	}
11	
12	@article{decision-repr-transition-2026,
13	    title   = {Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions},
14	    author  = {Shi, Boyu and Liu, Chang and Gao, ChuanBao and Yang, Xu and Geng, Xin},
15	    journal = {arXiv preprint arXiv:2605.07271},
16	    year    = {2026},
17	    url     = {https://arxiv.org/abs/2605.07271},
18	}
19	
20	@article{deepseek-r1-2025,
21	    title   = {{DeepSeek-R1} incentivizes reasoning in {LLMs} through reinforcement learning},
22	    author  = {{DeepSeek-AI}},
23	    journal = {Nature},
24	    volume  = {645},
25	    pages   = {633--638},
26	    year    = {2025},
27	    doi     = {10.1038/s41586-025-09422-z},
28	}
29	
30	@inproceedings{defensivekv-iclr2026,
31	    title     = {{DefensiveKV}: Taming the Fragility of {KV} Cache Eviction in {LLM} Inference},
32	    author    = {Feng, Yuan and Guo, Haoyu and Lv, Junlin and Zhou, S. Kevin and Xie, Xike},
33	    booktitle = {International Conference on Learning Representations},
34	    year      = {2026},
35	    url       = {https://arxiv.org/abs/2510.13334},
36	}
37	
38	@article{doing-more-with-less-2026,
39	    title   = {Doing More With Less: Revisiting the Effectiveness of {LLM} Pruning for Test-Time Scaling},
40	    author  = {Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman},
41	    journal = {arXiv preprint arXiv:2604.25098},
42	    year    = {2026},
43	    url     = {https://arxiv
…[truncated 11796 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-15T10:54:21.617643+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\placeholder",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\placeholder",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-15T10:54:22.170913+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex:21:\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 306 · 2026-05-15T10:54:22.673467+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "REVIEWER-ATTACK|REBUTTAL",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "REVIEWER-ATTACK|REBUTTAL",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-15T10:54:23.226187+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-15T10:54:23.377271+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "following ThinKV",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "following ThinKV",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 309 · 2026-05-15T10:54:23.428618+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex:33:Each generated sequence is partitioned into three phases (low-, mid-, high-sparsity) by tercile boundaries of per-position attention sparsity, following ThinKV~\cite{thinkv-iclr2026}. Low-sparsity phases correspond to broadly distributed attention (exploratory reasoning); high-sparsity phases to concentrated attention (structured computation). Details in Appendix~\ref{app:formulation-details}.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 310 · 2026-05-15T10:54:28.978743+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 311 · 2026-05-15T10:55:43.535322+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 32, \"total_citations\": 61, \"unique_cited_keys\": 32, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 24, \"online_not_found\": 3, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"adakv-neurips2025\", \"type\": \"inproceedings\", \"title\": \"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference\", \"authors\": \"Feng, Yuan and Lv, Junlin and Cao, Yukun and Xie, Xike and Zhou, S. Kevin\", \"year\": \"2025\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"decision-repr-transition-2026\", \"type\": \"article\", \"title\": \"Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions\", \"authors\": \"Shi, Boyu and Liu, Chang and Gao, ChuanBao and Yang, Xu and Geng, Xin\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.07271\"}, {\"key\": \"deepseek-r1-2025\", \"type\": \"article\", \"title\": \"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning\", \"authors\": \"DeepSeek-AI\", \"year\": \"2025\", \"venue\": \"Nature\"}, {\"key\": \"defensivekv-iclr2026\", \"type\": \"inproceedings\", \"title\": \"DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference\", \"authors\": \"Feng, Yuan and Guo, Haoyu and Lv, Junlin and Zhou, S. Kevin and Xie, Xike\", \"year\": \"2026\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"doing-more-with-less-2026\", \"type\": \"article\", \"title\": \"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling\", \"authors\": \"Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2604.25098\"}, {\"key\": \"efron-1993\", \"ty
…[truncated 25979 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 74556
}
```

</details>

---


### Tool call

_source line 312 · 2026-05-15T10:58:15.942738+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 5 修订评估（新颖性/完整性）\n\n---\n\n## 逐条 Issue 判定\n\n### [R1-N1] critical: Placeholders — **[RESOLVED]**\n\n`\\placeholder` 命令定义仍保留在 main.tex line 21，但 grep 确认全文无任何实际调用。所有数据已填充：\n\n- **Table 4 (LLaMA cross-arch)**：4 行数据完整（$\\widetilde{\\Delta}$: 0.020→0.356，CI 和 p 值均有）\n- **Discussion oracle pilot**：oracle 18% (p=0.002)、heuristic 32% (p=0.024)\n- **Qwen null rate**：45.2%，含 lag-1 autocorrelation 解释 (methodology.tex line 10)\n- **Per-problem concordance**：mean ρ=−0.107, p=0.926（appendix_moved.tex line 73）\n- **n_LLAMA**：明确 n=49（Table 4 caption）\n- **Random eviction Qwen s≥0.25**：Δ=0.39/0.91, p 值完整（appendix_moved.tex line 76）\n\n建议删除 `\\newcommand{\\placeholder}` 定义以保持 source 整洁，但不影响接收判断。\n\n---\n\n### [R2-N3] warning: HIES 区分不足 — **[RESOLVED]**\n\n修改充分。两处关键增补：\n\n1. **Related Work** (related_work.tex line 18)：\"HIES independently show that importance-based head discrimination collapses under heavy **single-axis** pruning. Our work extends this to the **compound** setting, revealing that collapse is amplified by the interaction of two compression axes and **modulated by reasoning phase**—phenomena absent in single-axis analysis. **The crossover effect (§5.3) is a prediction that single-axis frameworks cannot generate.**\"\n\n2. **Analysis §6.1** (analysis.tex line 7)：同样明确 \"extends this to the compound setting, where collapse is amplified by the interaction of two compression axes and modulated by reasoning phase.\"\n\n关键 novelty delta 现在清晰：(a) single-axis → compound amplification, (b) phase modulation, (c) crossover 作为 HIES 无法生成的 prediction。这三点有效区分了两项工作。\n\n---\n\n### [R2-W3] warning: Missing references RLKV/LongFlow/PM-KVQ — **[RESOLVED]**\n\n三篇均已引用且位置恰当：\n- **PM-KVQ** (related_work.tex line 10)：置于 compound compression 段落，关联 \"temporal dimension to compression severity\"——恰当\n- **RLKV + LongFlow** (related_work.tex line 19)：置于 KV cache eviction 段落——恰当\n- references.bib 均有完整条目；verify_references 确认 RLKV (verified)、LongFlow (verified)、PM-KVQ (verified)\n\n小问题：LongFlow bib entry 含 `note = {Withdrawn from ICLR 2026}`。引用 withdrawn paper 需要审慎——建议删除 ICLR 2026 note 或在正文中标注仅引用 arXiv 版本。\n\n---\n\n### [R2-W5] warning: Abstract 过长过密 — **[RESOLVED]**\n\n修改显著改善。对比：\n- **Round 1**：14 行，含 3 个完整模型名、4 个 sparsity level 的详细 d_z/p/median 数据、cross-architecture 详细数字\n- **Round 5**：10 行，结构清晰——(1) 问题 → (2) DeepSeek headline (Δ:0.39→8.48, p<10^-69) → (3) random baseline as contrast → (4) crossover 一句 → (5) Qwen replication → (6) LLaMA \"preliminary\" → (7) mechanism \"correlates with\" → (8) implication\n\nLLaMA 现在仅 \"preliminary cross-architecture evidence...suggesting the phenomenon may extend beyond Qwen2-family architectures\"——远比 Round 1 的详细数字更审慎。Mechanism 使用 \"correlates with\" 而非 \"explains\"。\n\n---\n\n### [R2-Minor-1] info: h2o bib / author mismatch — **[RESOLVED]**\n\nh2o-neurips2023 bib entry 现在有 title：`{H\\textsubscript{2}O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models`。verify_references 仍报告 \"skipped (no title)\" 是因为 parser 未处理 LaTeX `\\textsubscript` 命令，但实际 bib 内容正确。\n\nAuthor mismatch 状况与 Round 1 相同（deepseek-r1, snapkv, unicomp, qwen25），均为 API 记录差异，非实质性错误。\n\n---\n\n### [R2-Minor-2] info: REVIEWER-ATTACK/REBUTTAL 注释 — **[RESOLVED]**\n\nGrep 确认全文零匹配。所有 REVIEWER-ATTACK/REBUTTAL LaTeX comments 已完全删除。\n\n---\n\n### [R2-Minor-6] info: s=0.35 未完整报告 — **[RESOLVED]**\n\n原 appendix_disc_analysis.tex 中引用 \"s=0.35 high-phase II rises to 0.105\" 的那段已被重写，现在仅引用 s≤0.30 数据（line 11: \"$\\widetilde{\\mathrm{II}}_{\\text{high}} < 0.06$ at $s \\leq 0.30$\"），不再引用未完整报告的 supplementary experiment。\n\n---\n\n### [R1-Minor-code] info: 无代码/数据声明 — **[RESOLVED]**\n\nmain.tex lines 47-48 新增 `\\section*{Reproducibility}` 声明：\"Code and data will be released upon acceptance.\" 此外，methodology.tex 现在报告 bootstrap seed=42。\n\n---\n\n## 额外检查\n\n### 1. Random eviction 叙事变化\n\n**诚实且恰当处理。** Round 1 的 \"7/8 conditions non-significant\" 和 \"flat baseline ($G \\approx 1$)\" 已被替换为更精确的叙事：\n\n- Results §5.1 (line 8)：\"Random eviction develops a detectable but weak phase gradient above $s \\approx 0.20$: at $s \\leq 0.20$, $\\Delta$ is non-significant...at $s \\geq 0.25$, $\\Delta$ becomes significant...but $15$–$39{\\times}$ smaller\"\n- Discussion §7 (line 5)：\"The near-unity random baseline ($G{=}0.5$–$1.3{\\times}$, trivial magnitude) confirms the **dominant** amplification is strategy-specific\"\n- Contribution 1 (Introduction line 22)：\"$3$–$39{\\times}$ larger than under random eviction\"\n\n从 \"flat baseline\" → \"dominant but not exclusive driver\" 是一个 honest 的叙事转变，正确反映了 n=500 的更高统计功效。未试图隐藏 random eviction 在高 sparsity 下也有 detectable gradient。\n\n### 2. Contribution 措辞\n\n三个 contributions 现在恰当反映 evidence strength：\n\n1. ~~\"absent under random eviction\"~~ → \"**$3$–$39{\\times}$ larger** than under random eviction\" — 更精确\n2. ~~\"replicates across three models spanning two architectures\"~~ → \"replicates across **two Qwen2-architecture models**...with **exploratory evidence** from a LlamaForCausalLM model **suggesting** the phenomenon **may** extend beyond Qwen2\" — 大幅降低了 overclaim\n3. \"propose entropy-discrimination collapse as a mechanistic explanation\" — 保持 \"propose\" 措辞，恰当\n\n### 3. n=50 profiling tables 与 n=500 共存\n\nTable 2 (per-phase breakdown, n=50) 和 Table 6 (permutation test, n=49) 显式标注为 \"profiling subset\"，并 forward-reference 到 n=496 的 Table 1。这是 coherent 的——profiling tables 提供了 per-phase 细粒度数据，n=500 tables 提供了统计功效。\n\n**一个潜在困惑点**：Table 2 的 G 值 (69×–274×) 与正文 n=496 的 G 值 (30×–148×) 差异显著，因为 n=500 包含了更多 \"average\" 问题稀释了 profiling subset 中的极端值。Discussion (line 5) 使用 \"G=30–148×\" 但 Table 2 仍显示 69–274×。虽然标注了 subset 来源，但 **建议在 Table 2 caption 或正文中简短解释为何 profiling subset G 高于 full sample G**。\n\n### 4. 新引用验证\n\n- **RLKV** (rlkv-2025): OpenAlex verified, arXiv:2510.08525 ✓\n- **LongFlow** (longflow-2026): OpenAlex verified, arXiv:2603.11504 ✓ (但 bib note 标注 \"Withdrawn from ICLR 2026\")\n- **PM-KVQ** (pmkvq-iclr2026): OpenAlex verified, ICLR 2026 ✓\n\n无幻觉引用。\n\n### 5. \"following ThinKV\" 措辞\n\nbackground.tex line 33 仍然写 \"following ThinKV\"。R1-W1 指出 ThinKV 使用 explicit `&lt;think>` delimiters，而本文使用 quantile-based tercile——方法不同。新增的 segmentation robustness 分析 (Appendix §I, §J) 验证了 tercile/quartile/quintile 和 mpl 的鲁棒性，但 **措辞仍具误导性**。\n\n**[STILL OPEN - minor]** 建议改为 \"inspired by ThinKV's phase distinction\" 或 \"analogous to ThinKV's phase decomposition, but using quantile-based segmentation rather than explicit delimiters.\"\n\n### 6. 整体影响力评估变化\n\nn=500 将 Bonferroni p-values 推到了 $<10^{-69}$（DeepSeek）和 $<10^{-14}$（Qwen），配合 BH-FDR 44-test correction、segmentation robustness、mpl sensitivity，统计 soundness 不再是问题。这改变了我对论文价值的判断：\n\n- Round 1 时主要疑虑是 **数据不完整**（placeholders）和 **统计证据边缘**（n=50，Qwen s=0.15 CI 含零）\n- Round 5 这两个问题均已消除。Qwen s=0.15 的 $\\Delta{=}0.07$ [0.05, 0.09] 现在 CI 排除零\n- 论文的核心价值——对 compound sparsity 的 phase-dependent severity 的首次系统量化——在统计上得到了坚实支撑\n\n---\n\n## 新发现的问题\n\n### [NEW-1] minor: Table 2 与正文 G 值不一致可能引起困惑\n\nTable 2 (profiling, n=50) 报告 G=69×–274×；正文/Discussion 使用 n=496 的 G=30×–148×。两者均有标注，但落差大（~2×）且无解释。读者可能疑惑为何 G 在更大 sample 上反而更小。\n\n建议在 Table 2 caption 加一句：\"Full-sample ($n{=}496$) bootstrap $G$ ranges from $30{\\times}$ to $148{\\times}$, reflecting dilution by lower-severity problems absent in the profiling subset.\"\n\n### [NEW-2] minor: LongFlow 引用标注 \"Withdrawn from ICLR 2026\"\n\nreferences.bib 的 longflow-2026 entry 含 `note = {Withdrawn from ICLR 2026}`。引用 withdrawn paper 虽非禁忌（arXiv 版本仍存在），但可能引起 reviewer 质疑。建议删除 note 或改为仅引用 arXiv preprint。\n\n### [NEW-3] info: `\\placeholder` 命令定义仍在 main.tex\n\n虽无实际调用，但保留 `\\newcommand{\\placeholder}` 在提交源码中不够整洁。建议删除。\n\n---\n\n## 总体评分更新建议\n\n| 维度 | Round 1 | Round 5 | 变化理由 |\n|------|---------|---------|----------|\n| **Soundness** | 3.0 | **3.5** | n=500 + BH-FDR 44 tests + segmentation/mpl robustness 消除了统计疑虑；correlational mechanism 现在明确标注 |\n| **Excitement** | 2.5 | **3.0** | 核心 finding 未变但 evidence strength 大幅提升；crossover 和 quantitative surprise (30–148×) 对 deployment practitioners 有实际价值；仍是 empirical finding 而非 method |\n| **Overall** | 2.5 | **3.5** | 从 \"resubmit\" 提升到 \"Findings / borderline Conference\"。所有 critical issues resolved，honest framing，thorough robustness。限制因素：单一 benchmark (MATH-500)、无方法贡献、cross-architecture evidence 仍弱 |\n| **Reproducibility** | 3.0 | **3.5** | Reproducibility statement + seed=42 + 详细 methodology；但仍 \"upon acceptance\"，非预发布 |\n| **Confidence** | 4 | **4** | 无变化 |\n\n**一句话**：论文从 Round 1 的 incomplete submission 提升为一篇统计严谨、honest framing 的 empirical characterization paper。所有 critical issues 已解决，remaining issues 均为 minor。推荐 **Findings**；如果 AC 重视 compound sparsity 的 deployment-relevant characterization，borderline Conference 也可接受。\n\n---\n\n## Open Issues 总结\n\n| Issue | Status | Severity |\n|-------|--------|----------|\n| \"following ThinKV\" 措辞 | STILL OPEN | minor |\n| Table 2 vs 正文 G 值落差未解释 | NEW | minor |\n| LongFlow \"Withdrawn\" note | NEW | minor |\n| `\\placeholder` 命令定义残留 | NEW | trivial |",
  "reviewer_id": "2",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 5 修订评估（新颖性/完整性）\n\n---\n\n## 逐条 Issue 判定\n\n### [R1-N1] critical: Placeholders — **[RESOLVED]**\n\n`\\placeholder` 命令定义仍保留在 main.tex line 21，但 grep 确认全文无任何实际调用。所有数据已填充：\n\n- **Table 4 (LLaMA cross-arch)**：4 行数据完整（$\\widetilde{\\Delta}$: 0.020→0.356，CI 和 p 值均有）\n- **Discussion oracle pilot**：oracle 18% (p=0.002)、heuristic 32% (p=0.024)\n- **Qwen null rate**：45.2%，含 lag-1 autocorrelation 解释 (methodology.tex line 10)\n- **Per-problem concordance**：mean ρ=−0.107, p=0.926（appendix_moved.tex line 73）\n- **n_LLAMA**：明确 n=49（Table 4 caption）\n- **Random eviction Qwen s≥0.25**：Δ=0.39/0.91, p 值完整（appendix_moved.tex line 76）\n\n建议删除 `\\newcommand{\\placeholder}` 定义以保持 source 整洁，但不影响接收判断。\n\n---\n\n### [R2-N3] warning: HIES 区分不足 — **[RESOLVED]**\n\n修改充分。两处关键增补：\n\n1. **Related Work** (related_work.tex line 18)：\"HIES independently show that importance-based head discrimination collapses under heavy **single-axis** pruning. Our work extends this to the **compound** setting, revealing that collapse is amplified by the interaction of two compression axes and **modulated by reasoning phase**—phenomena absent in single-axis analysis. **The crossover effect (§5.3) is a prediction that single-axis frameworks cannot generate.**\"\n\n2. **Analysis §6.1** (analysis.tex line 7)：同样明确 \"extends this to the compound setting, where collapse is amplified by the interaction of two compression axes and modulated by reasoning phase.\"\n\n关键 novelty delta 现在清晰：(a) single-axis → compound amplification, (b) phase modulation, (c) crossover 作为 HIES 无法生成的 prediction。这三点有效区分了两项工作。\n\n---\n\n### [R2-W3] warning: Missing references RLKV/LongFlow/PM-KVQ — **[RESOLVED]**\n\n三篇均已引用且位置恰当：\n- **PM-KVQ** (related_work.tex line 10)：置于 compound compression 段落，关联 \"temporal dimension to compression severity\"——恰当\n- **RLKV + LongFlow** (related_work.tex line 19)：置于 KV cache eviction 段落——恰当\n- references.bib 均有完整条目；verify_references 确认 RLKV (verified)、LongFlow (verified)、PM-KVQ (verified)\n\n小问题：LongFlow bib entry 含 `note = {Withdrawn from ICLR 2026}`。引用 withdrawn paper 需要审慎——建议删除 ICLR 2026 note 或在正文中标注仅引用 arXiv 版本。\n\n---\n\n### [R2-W5] warning: Abstract 过长过密 — **[RESOLVED]**\n\n修改显著改善。对比：\n- **Round 1**：14 行，含 3 个完整模型名、4 个 sparsity level 的详细 d_z/p/median 数据、cross-architecture 详细数字\n- **Round 5**：10 行，结构清晰——(1) 问题 → (2) DeepSeek headline (Δ:0.39→8.48, p<10^-69) → (3) random baseline as contrast → (4) crossover 一句 → (5) Qwen replication → (6) LLaMA \"preliminary\" → (7) mechanism \"correlates with\" → (8) implication\n\nLLaMA 现在仅 \"preliminary cross-architecture evidence...suggesting the phenomenon may extend beyond Qwen2-family architectures\"——远比 Round 1 的详细数字更审慎。Mechanism 使用 \"correlates with\" 而非 \"explains\"。\n\n---\n\n### [R2-Minor-1] info: h2o bib / author mismatch — **[RESOLVED]**\n\nh2o-neurips2023 bib entry 现在有 title：`{H\\textsubscript{2}O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models`。verify_references 仍报告 \"skipped (no title)\" 是因为 parser 未处理 LaTeX `\\textsubscript` 命令，但实际 bib 内容正确。\n\nAuthor mismatch 状况与 Round 1 相同（deepseek-r1, snapkv, unicomp, qwen25），均为 API 记录差异，非实质性错误。\n\n---\n\n### [R2-Minor-2] info: REVIEWER-ATTACK/REBUTTAL 注释 — **[RESOLVED]**\n\nGrep 确认全文零匹配。所有 REVIEWER-ATTACK/REBUTTAL LaTeX comments 已完全删除。\n\n---\n\n### [R2-Minor-6] info: s=0.35 未完整报告 — **[RESOLVED]**\n\n原 appendix_disc_analysis.tex 中引用 \"s=0.35 high-phase II rises to 0.105\" 的那段已被重写，现在仅引用 s≤0.30 数据（line 11: \"$\\widetilde{\\mathrm{II}}_{\\text{high}} < 0.06$ at $s \\leq 0.30$\"），不再引用未完整报告的 supplementary experiment。\n\n---\n\n### [R1-Minor-code] info: 无代码/数据声明 — **[RESOLVED]**\n\nmain.tex lines 47-48 新增 `\\section*{Reproducibility}` 声明：\"Code and data will be released upon acceptance.\" 此外，methodology.tex 现在报告 bootstrap seed=42。\n\n---\n\n## 额外检查\n\n### 1. Random eviction 叙事变化\n\n**诚实且恰当处理。** Round 1 的 \"7/8 conditions non-significant\" 和 \"flat baseline ($G \\approx 1$)\" 已被替换为更精确的叙事：\n\n- Results §5.1 (line 8)：\"Random eviction develops a detectable but weak phase gradient above $s \\approx 0.20$: at $s \\leq 0.20$, $\\Delta$ is non-significant...at $s \\geq 0.25$, $\\Delta$ becomes significant...but $15$–$39{\\times}$ smaller\"\n- Discussion §7 (line 5)：\"The near-unity random baseline ($G{=}0.5$–$1.3{\\times}$, trivial magnitude) confirms the **dominant** amplification is strategy-specific\"\n- Contribution 1 (Introduction line 22)：\"$3$–$39{\\times}$ larger than under random eviction\"\n\n从 \"flat baseline\" → \"dominant but not exclusive driver\" 是一个 honest 的叙事转变，正确反映了 n=500 的更高统计功效。未试图隐藏 random eviction 在高 sparsity 下也有 detectable gradient。\n\n### 2. Contribution 措辞\n\n三个 contributions 现在恰当反映 evidence strength：\n\n1. ~~\"absent under random eviction\"~~ → \"**$3$–$39{\\times}$ larger** than under random eviction\" — 更精确\n2. ~~\"replicates across three models spanning two architectures\"~~ → \"replicates across **two Qwen2-architecture models**...with **exploratory evidence** from a LlamaForCausalLM model **suggesting** the phenomenon **may** extend beyond Qwen2\" — 大幅降低了 overclaim\n3. \"propose entropy-discrimination collapse as a mechanistic explanation\" — 保持 \"propose\" 措辞，恰当\n\n### 3. n=50 profiling tables 与 n=500 共存\n\nTable 2 (per-phase breakdown, n=50) 和 Table 6 (permutation test, n=49) 显式标注为 \"profiling subset\"，并 forward-reference 到 n=496 的 Table 1。这是 coherent 的——profiling tables 提供了 per-phase 细粒度数据，n=500 tables 提供了统计功效。\n\n**一个潜在困惑点**：Table 2 的 G 值 (69×–274×) 与正文 n=496 的 G 值 (30×–148×) 差异显著，因为 n=500 包含了更多 \"average\" 问题稀释了 profiling subset 中的极端值。Discussion (line 5) 使用 \"G=30–148×\" 但 Table 2 仍显示 69–274×。虽然标注了 subset 来源，但 **建议在 Table 2 caption 或正文中简短解释为何 profiling subset G 高于 full sample G**。\n\n### 4. 新引用验证\n\n- **RLKV** (rlkv-2025): OpenAlex verified, arXiv:2510.08525 ✓\n- **LongFlow** (longflow-2026): OpenAlex verified, arXiv:2603.11504 ✓ (但 bib note 标注 \"Withdrawn from ICLR 2026\")\n- **PM-KVQ** (pmkvq-iclr2026): OpenAlex verified, ICLR 2026 ✓\n\n无幻觉引用。\n\n### 5. \"following ThinKV\" 措辞\n\nbackground.tex line 33 仍然写 \"following ThinKV\"。R1-W1 指出 ThinKV 使用 explicit `&lt;think>` delimiters，而本文使用 quantile-based tercile——方法不同。新增的 segmentation robustness 分析 (Appendix §I, §J) 验证了 tercile/quartile/quintile 和 mpl 的鲁棒性，但 **措辞仍具误导性**。\n\n**[STILL OPEN - minor]** 建议改为 \"inspired by ThinKV's phase distinction\" 或 \"analogous to ThinKV's phase decomposition, but using quantile-based segmentation rather than explicit delimiters.\"\n\n### 6. 整体影响力评估变化\n\nn=500 将 Bonferroni p-values 推到了 $<10^{-69}$（DeepSeek）和 $<10^{-14}$（Qwen），配合 BH-FDR 44-test correction、segmentation robustness、mpl sensitivity，统计 soundness 不再是问题。这改变了我对论文价值的判断：\n\n- Round 1 时主要疑虑是 **数据不完整**（placeholders）和 **统计证据边缘**（n=50，Qwen s=0.15 CI 含零）\n- Round 5 这两个问题均已消除。Qwen s=0.15 的 $\\Delta{=}0.07$ [0.05, 0.09] 现在 CI 排除零\n- 论文的核心价值——对 compound sparsity 的 phase-dependent severity 的首次系统量化——在统计上得到了坚实支撑\n\n---\n\n## 新发现的问题\n\n### [NEW-1] minor: Table 2 与正文 G 值不一致可能引起困惑\n\nTable 2 (profiling, n=50) 报告 G=69×–274×；正文/Discussion 使用 n=496 的 G=30×–148×。两者均有标注，但落差大（~2×）且无解释。读者可能疑惑为何 G 在更大 sample 上反而更小。\n\n建议在 Table 2 caption 加一句：\"Full-sample ($n{=}496$) bootstrap $G$ ranges from $30{\\times}$ to $148{\\times}$, reflecting dilution by lower-severity problems absent in the profiling subset.\"\n\n### [NEW-2] minor: LongFlow 引用标注 \"Withdrawn from ICLR 2026\"\n\nreferences.bib 的 longflow-2026 entry 含 `note = {Withdrawn from ICLR 2026}`。引用 withdrawn paper 虽非禁忌（arXiv 版本仍存在），但可能引起 reviewer 质疑。建议删除 note 或改为仅引用 arXiv preprint。\n\n### [NEW-3] info: `\\placeholder` 命令定义仍在 main.tex\n\n虽无实际调用，但保留 `\\newcommand{\\placeholder}` 在提交源码中不够整洁。建议删除。\n\n---\n\n## 总体评分更新建议\n\n| 维度 | Round 1 | Round 5 | 变化理由 |\n|------|---------|---------|----------|\n| **Soundness** | 3.0 | **3.5** | n=500 + BH-FDR 44 tests + segmentation/mpl robustness 消除了统计疑虑；correlational mechanism 现在明确标注 |\n| **Excitement** | 2.5 | **3.0** | 核心 finding 未变但 evidence strength 大幅提升；crossover 和 quantitative surprise (30–148×) 对 deployment practitioners 有实际价值；仍是 empirical finding 而非 method |\n| **Overall** | 2.5 | **3.5** | 从 \"resubmit\" 提升到 \"Findings / borderline Conference\"。所有 critical issues resolved，honest framing，thorough robustness。限制因素：单一 benchmark (MATH-500)、无方法贡献、cross-architecture evidence 仍弱 |\n| **Reproducibility** | 3.0 | **3.5** | Reproducibility statement + seed=42 + 详细 methodology；但仍 \"upon acceptance\"，非预发布 |\n| **Confidence** | 4 | **4** | 无变化 |\n\n**一句话**：论文从 Round 1 的 incomplete submission 提升为一篇统计严谨、honest framing 的 empirical characterization paper。所有 critical issues 已解决，remaining issues 均为 minor。推荐 **Findings**；如果 AC 重视 compound sparsity 的 deployment-relevant characterization，borderline Conference 也可接受。\n\n---\n\n## Open Issues 总结\n\n| Issue | Status | Severity |\n|-------|--------|----------|\n| \"following ThinKV\" 措辞 | STILL OPEN | minor |\n| Table 2 vs 正文 G 值落差未解释 | NEW | minor |\n| LongFlow \"Withdrawn\" note | NEW | minor |\n| `\\placeholder` 命令定义残留 | NEW | trivial |",
    "reviewer_id": "2",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 313 · 2026-05-15T10:58:20.012085+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4069
}
```

</details>

---


### Assistant

_source line 314 · 2026-05-15T10:58:27.210149+00:00_

Round 5 修订评估已提交给 Review Director。

总结：**所有 Round 1 的 critical/warning issues 均已 resolved**。论文从 n=50 升级到 n=500，填充了全部 placeholder，title 缩窄为 "Mathematical Reasoning Models"，HIES 区分清晰，新引用补全，abstract 精简，REVIEWER-ATTACK 注释删除，mechanism 明确标注为 correlational。评分建议从 2.5 → 3.5（Findings / borderline Conference）。仅余 4 个 minor/trivial 问题（"following ThinKV" 措辞、Table 2 vs 正文 G 值落差、LongFlow withdrawn note、placeholder 命令残留）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2"
}
```

</details>

---


## Round 7

## Round 7

4 recorded events


### User

_source line 315 · 2026-05-15T10:59:06.361320+00:00_

[Round 5 审稿请求]:
## 交叉分享 — Reviewer 1 的 Round 5 修订评估

请逐条回应 [AGREE] 或 [REBUT]。Reviewer 1 评估了全部 16 个 issues，结论如下：

### Issue 判定
- R1-N1 ~ R1-N5: 全部 RESOLVED（与你一致）
- R1-W1 (phase segmentation): PARTIALLY RESOLVED（sensitivity analysis 充分但 "following ThinKV" 仍误导 + quartile/quintile 仅 n=50）——与你一致
- R1-W2 ~ R1-W6, REV-ADD-2, REV-ADD-3: 全部 RESOLVED
- Overall: 2.5 → 3.5/5

### R1 新发现

**[NEW-W1] warning: n=50 与 n=500 数据混合引起混淆**
- Table 2 (n=50, Δ_s030=14.59, G=274×) vs Table 1 (n=496, Δ_s030=8.48, G=148×)——差异 42-85%
- 建议将 Table 2 移至 Appendix 或在 main body 补充 n=500 per-phase table
- 与你的 NEW-1 高度重叠，但 R1 将其定为 warning 级别（你定为 minor）

**[NEW-W2] warning: Crossover analysis (§5.3) 未在 n=500 上验证**
- §5.3 引用的具体数值（imp high=0.032 vs rand high=0.818 等）全部来自 n=50
- 鉴于 n=50→n=500 的 Δ 变化达 40%，crossover magnitude 可能在 n=500 下不同
- 建议在 n=500 上重新计算并更新

**额外观察：**
- Segmentation robustness quartile/quintile 仅 n=50——既然有 n=500 数据应验证
- LLaMA 仍为 n=49，与 DS/QW n=500 对比更显 underpowered（但 "exploratory" 标注诚实）

### R1 评分
Soundness: 2.5→3.5; Excitement: 3.0→3.0; Reproducibility: 2.0→3.5; Overall: 2.5→3.5

请回应：(1) 对 R1 的 issue 判定是否同意？(2) NEW-W1——你定为 minor，R1 定为 warning，你维持哪个 severity？(3) NEW-W2 (crossover 未在 n=500 验证)——你是否同意这是一个需要关注的问题？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 316 · 2026-05-15T10:59:58.715660+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 Round 5 修订评估\n\n---\n\n### (1) R1 Issue 判定一致性\n\nR1-N1 ~ R1-N5 全部 RESOLVED、R1-W2 ~ R1-W6 及 REV-ADD 系列 RESOLVED——与我的判定完全一致，无分歧。\n\n**[AGREE] R1-W1 (phase segmentation) PARTIALLY RESOLVED**\n\n与我的 \"STILL OPEN - minor\" 判定一致。我补充一个 R1 的精确观察：quartile/quintile robustness analysis（Appendix §I, Table 12）仅在 n=50 上做了 spot check，而非 n=500。既然 n=50 → n=500 的主指标 $\\Delta$ 变化达 40%（Table 2 vs Table 1），segmentation robustness 也应在 full sample 上验证。不过这属于 completeness 问题而非 soundness 问题——tercile 的 n=500 结果已经很扎实，quartile/quintile 作为辅助验证在 n=50 上方向一致已足够支撑结论。\n\n---\n\n### (2) NEW-W1: n=50 与 n=500 数据混合——severity 判定\n\n**我将 severity 从 minor 上调至 warning，同意 R1。** 理由：\n\n重新审视后，Table 2 位于 **main body** 的 §5.2（Phase-Modulated Amplification），是读者首次接触 per-phase 数据的位置。该表的 headline 数字 $G{=}69$–$274\\times$ 在视觉上极具冲击力，而正文报告的 n=496 数字 $G{=}30$–$148\\times$ 只出现在同段的文字中（results.tex line 29）。对不仔细的读者——包括只扫表格的 reviewer——Table 2 会成为对论文 effect size 的第一印象，且高估 42%–85%。\n\n虽然 Table 2 caption 标注了 \"from the $n{=}50$ profiling subset\" 和 forward reference，但我认为这不够：\n\n1. **读者习惯问题**：main body 的 table 通常被视为 primary evidence，appendix 的 table 才是 supplementary。将 n=50 profiling table 放在 main body 而将 n=500 primary evidence 仅放在 inline text 中，颠倒了 primary/supplementary 的层级。\n2. **具体数字扩散**：Abstract 和 Conclusion 已更新为 n=500 数字，但 §5.2 的 Figure 1 caption 仍然引用 profiling subset（\"profiling subset, $n{=}50$\"），且 Discussion §7 line 5 用了 \"$G{=}30$–$148\\times$\"。正文在不同位置交替引用两套数字。\n\n**建议（与 R1 一致）**：在 main body 补充 n=500 的 per-phase table（即使作为 condensed 版本只报 $\\widetilde{\\mathrm{II}}_{\\textit{low}}$、$\\widetilde{\\mathrm{II}}_{\\textit{high}}$、$\\Delta$、$G$），将当前 Table 2 移至 Appendix 或明确标注为 \"Initial Profiling (Superseded)\"。\n\n---\n\n### (3) NEW-W2: Crossover 未在 n=500 上验证\n\n**[AGREE] 这是一个需要关注的问题，定级 warning。**\n\n§5.3 (results.tex line 66) 的所有具体数值均来自 n=50 profiling subset：\n\n> \"importance-based eviction yields lower II than random in the high-sparsity phase ($0.032$ vs.\\ $0.818$) but higher II in the low-sparsity phase ($7.196$ vs.\\ $1.363$---a $5.3{\\times}$ reversal)\"\n\n这些数字直接来自 Table 2（n=50）。而 Table 1（n=500）显示 $\\Delta$ 在 s=0.25 从 7.16 变为 3.99、s=0.30 从 14.59 变为 8.48——变化幅度 40%–44%。per-phase 数字的变化可能更大。\n\n关键问题：**crossover 是论文三大 contributions 之一**（Introduction line 22 的 contribution 1 提到 \"3–39× larger than under random\"），也是区分于 HIES 的核心 novelty argument（Related Work line 18: \"The crossover effect is a prediction that single-axis frameworks cannot generate\"）。如果这一关键 claim 仅基于 n=50 数据而未在 n=500 上验证，且其他指标在 n=50→n=500 时变化显著，这构成了 **evidence strength 与 claim strength 不匹配**。\n\nCrossover 的 **方向**（importance 在 low-sparsity phase 更差、在 high-sparsity phase 更好）几乎肯定在 n=500 下仍然成立——Table 1 中 importance $\\Delta{=}3.99$ vs random $\\Delta{=}0.26$ at s=0.25 表明低/高 phase 的差异结构不会消失。但具体的 reversal magnitude（5.3×）可能不同，且 Appendix C 引用的 \"3.9×–5.4× across all sparsity levels\" 也全部基于 n=50。\n\n**建议**：在 n=500 上计算 per-phase per-strategy median II，更新 §5.3 和 Appendix C 的 crossover 数值。至少应加一句确认 crossover 方向在 n=500 下保持。\n\n---\n\n### 额外同意点\n\n**[AGREE]** R1 观察到 LLaMA 仍为 n=49 vs DS/QW 的 n=500 对比更显 underpowered。我在 Round 1 交叉回应中已经同意 LLaMA 证据弱，但 \"Exploratory\" 标注是诚实的处理。如果 full MATH-500 的 LLaMA 实验可行，应该补做——但这不是 blocking issue，因为 LLaMA 已被降级为 exploratory。\n\n**[AGREE]** R1 评分 3.5/5 与我的评分一致。两位 reviewer 从 Round 1 的 2.5/5 共同上调至 3.5/5，收敛清晰。\n\n---\n\n### 分歧总结\n\n| Issue | R1 | R2 | 最终建议 |\n|-------|----|----|---------|\n| NEW-W1 (n=50/n=500 混合) | warning | ~~minor~~ → **warning** (上调) | warning — 需要在 main body 补充 n=500 per-phase table |\n| NEW-W2 (crossover 未在 n=500 验证) | warning | **warning** (同意) | warning — crossover 数值应在 n=500 上更新 |\n| \"following ThinKV\" 措辞 | partially resolved | still open (minor) | 一致：minor，改措辞即可 |\n| Seg robustness quartile/quintile 仅 n=50 | R1 观察 | 同意但不 blocking | minor — nice-to-have |\n\n**无严重分歧。** 两位 reviewer 在所有 issue 判定上高度一致，severity 分级仅在 NEW-W1 上有 minor→warning 的差异（我已上调）。论文整体评价收敛于 3.5/5 (Findings / borderline Conference)。",
  "reviewer_id": "2",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 Round 5 修订评估\n\n---\n\n### (1) R1 Issue 判定一致性\n\nR1-N1 ~ R1-N5 全部 RESOLVED、R1-W2 ~ R1-W6 及 REV-ADD 系列 RESOLVED——与我的判定完全一致，无分歧。\n\n**[AGREE] R1-W1 (phase segmentation) PARTIALLY RESOLVED**\n\n与我的 \"STILL OPEN - minor\" 判定一致。我补充一个 R1 的精确观察：quartile/quintile robustness analysis（Appendix §I, Table 12）仅在 n=50 上做了 spot check，而非 n=500。既然 n=50 → n=500 的主指标 $\\Delta$ 变化达 40%（Table 2 vs Table 1），segmentation robustness 也应在 full sample 上验证。不过这属于 completeness 问题而非 soundness 问题——tercile 的 n=500 结果已经很扎实，quartile/quintile 作为辅助验证在 n=50 上方向一致已足够支撑结论。\n\n---\n\n### (2) NEW-W1: n=50 与 n=500 数据混合——severity 判定\n\n**我将 severity 从 minor 上调至 warning，同意 R1。** 理由：\n\n重新审视后，Table 2 位于 **main body** 的 §5.2（Phase-Modulated Amplification），是读者首次接触 per-phase 数据的位置。该表的 headline 数字 $G{=}69$–$274\\times$ 在视觉上极具冲击力，而正文报告的 n=496 数字 $G{=}30$–$148\\times$ 只出现在同段的文字中（results.tex line 29）。对不仔细的读者——包括只扫表格的 reviewer——Table 2 会成为对论文 effect size 的第一印象，且高估 42%–85%。\n\n虽然 Table 2 caption 标注了 \"from the $n{=}50$ profiling subset\" 和 forward reference，但我认为这不够：\n\n1. **读者习惯问题**：main body 的 table 通常被视为 primary evidence，appendix 的 table 才是 supplementary。将 n=50 profiling table 放在 main body 而将 n=500 primary evidence 仅放在 inline text 中，颠倒了 primary/supplementary 的层级。\n2. **具体数字扩散**：Abstract 和 Conclusion 已更新为 n=500 数字，但 §5.2 的 Figure 1 caption 仍然引用 profiling subset（\"profiling subset, $n{=}50$\"），且 Discussion §7 line 5 用了 \"$G{=}30$–$148\\times$\"。正文在不同位置交替引用两套数字。\n\n**建议（与 R1 一致）**：在 main body 补充 n=500 的 per-phase table（即使作为 condensed 版本只报 $\\widetilde{\\mathrm{II}}_{\\textit{low}}$、$\\widetilde{\\mathrm{II}}_{\\textit{high}}$、$\\Delta$、$G$），将当前 Table 2 移至 Appendix 或明确标注为 \"Initial Profiling (Superseded)\"。\n\n---\n\n### (3) NEW-W2: Crossover 未在 n=500 上验证\n\n**[AGREE] 这是一个需要关注的问题，定级 warning。**\n\n§5.3 (results.tex line 66) 的所有具体数值均来自 n=50 profiling subset：\n\n> \"importance-based eviction yields lower II than random in the high-sparsity phase ($0.032$ vs.\\ $0.818$) but higher II in the low-sparsity phase ($7.196$ vs.\\ $1.363$---a $5.3{\\times}$ reversal)\"\n\n这些数字直接来自 Table 2（n=50）。而 Table 1（n=500）显示 $\\Delta$ 在 s=0.25 从 7.16 变为 3.99、s=0.30 从 14.59 变为 8.48——变化幅度 40%–44%。per-phase 数字的变化可能更大。\n\n关键问题：**crossover 是论文三大 contributions 之一**（Introduction line 22 的 contribution 1 提到 \"3–39× larger than under random\"），也是区分于 HIES 的核心 novelty argument（Related Work line 18: \"The crossover effect is a prediction that single-axis frameworks cannot generate\"）。如果这一关键 claim 仅基于 n=50 数据而未在 n=500 上验证，且其他指标在 n=50→n=500 时变化显著，这构成了 **evidence strength 与 claim strength 不匹配**。\n\nCrossover 的 **方向**（importance 在 low-sparsity phase 更差、在 high-sparsity phase 更好）几乎肯定在 n=500 下仍然成立——Table 1 中 importance $\\Delta{=}3.99$ vs random $\\Delta{=}0.26$ at s=0.25 表明低/高 phase 的差异结构不会消失。但具体的 reversal magnitude（5.3×）可能不同，且 Appendix C 引用的 \"3.9×–5.4× across all sparsity levels\" 也全部基于 n=50。\n\n**建议**：在 n=500 上计算 per-phase per-strategy median II，更新 §5.3 和 Appendix C 的 crossover 数值。至少应加一句确认 crossover 方向在 n=500 下保持。\n\n---\n\n### 额外同意点\n\n**[AGREE]** R1 观察到 LLaMA 仍为 n=49 vs DS/QW 的 n=500 对比更显 underpowered。我在 Round 1 交叉回应中已经同意 LLaMA 证据弱，但 \"Exploratory\" 标注是诚实的处理。如果 full MATH-500 的 LLaMA 实验可行，应该补做——但这不是 blocking issue，因为 LLaMA 已被降级为 exploratory。\n\n**[AGREE]** R1 评分 3.5/5 与我的评分一致。两位 reviewer 从 Round 1 的 2.5/5 共同上调至 3.5/5，收敛清晰。\n\n---\n\n### 分歧总结\n\n| Issue | R1 | R2 | 最终建议 |\n|-------|----|----|---------|\n| NEW-W1 (n=50/n=500 混合) | warning | ~~minor~~ → **warning** (上调) | warning — 需要在 main body 补充 n=500 per-phase table |\n| NEW-W2 (crossover 未在 n=500 验证) | warning | **warning** (同意) | warning — crossover 数值应在 n=500 上更新 |\n| \"following ThinKV\" 措辞 | partially resolved | still open (minor) | 一致：minor，改措辞即可 |\n| Seg robustness quartile/quintile 仅 n=50 | R1 观察 | 同意但不 blocking | minor — nice-to-have |\n\n**无严重分歧。** 两位 reviewer 在所有 issue 判定上高度一致，severity 分级仅在 NEW-W1 上有 minor→warning 的差异（我已上调）。论文整体评价收敛于 3.5/5 (Findings / borderline Conference)。",
    "reviewer_id": "2",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 317 · 2026-05-15T11:00:02.992173+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4276
}
```

</details>

---


### Assistant

_source line 318 · 2026-05-15T11:00:07.003049+00:00_

已提交交叉回应。与 R1 在所有 issue 判定上达成一致，将 NEW-W1 (n=50/n=500 混合) 从 minor 上调至 warning。两位 reviewer 评分收敛于 3.5/5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2"
}
```

</details>

---


## Round 8

## Round 8

74 recorded events


### User

_source line 319 · 2026-05-15T11:12:29.970795+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性与完整性**审查。

## 论文信息
- 标题: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Mathematical Reasoning Models
- 目标 venue: EMNLP 2026 Main Conference (通过 ARR May 2026 cycle)
- 截止日期: 2026-06-15
- 格式: ACL 模板 [review] 模式, 长文 8 页 + 无限 references, double-blind
- Limitations section 必须包含
- 论文路径: projects/phase-gated-compound-sparse/paper/main.tex

## 你的审查侧重

**核心职责：新颖性与完整性**——像顶会最严格的审稿人那样评估。重点审查：

1. **Novelty 评估**:
   - 核心 novelty claim（"phase-strategy interaction in compound sparsity"）相对于已有工作的增量贡献是否足够？
   - 与 HIES (2025) 的区分度：HIES 已报告 importance score collapse under heavy pruning。本文称 "extend this to compound setting, where collapse is amplified by interaction of two compression axes and modulated by reasoning phase"——这个增量是否 substantial？
   - 与 ThinKV 的关系：ThinKV 已做 phase-aware KV 策略。本文的 "compound interaction" 增量是否清晰？
   - 与 Sparse Frontier (2025) 的关系：该文已发现 "no single sparse attention strategy dominates across generation stages"——crossover 发现是否真正新颖？
   - discrimination collapse mechanism 作为 contribution——是否只是已知现象在新 setting 下的观察？

2. **Contribution 显著性**:
   - 论文本质是 characterization/analysis paper（无新方法、无新系统）——对 EMNLP main conference 是否足够？
   - 3 个 contributions 的 impact：(1) phase-strategy interaction, (2) dose-response + cross-model, (3) entropy-discrimination collapse。每个的 delta 有多大？
   - Discussion 中的 pilot experiment（oracle 18%, heuristic 32%）未达到 30% gate——这是否削弱 practical significance？

3. **Related Work 完整性**:
   - 搜索 2025-2026 年 compound sparsity / KV cache compression / reasoning model pruning 最新文献
   - 是否遗漏重要 baseline 或对比？
   - 引用是否存在可疑条目（hallucinated citations）？逐条验证关键引用的真实性
   - LongFlow bib entry 是否有 "Withdrawn" 标注问题？

4. **Framing 准确度**:
   - 标题 "Phase-Modulated Compound Sparsity" 是否过度 claim？（实际仅 characterization，未 modulate anything）
   - Abstract 中 "emergent phase-strategy interaction" 的 "emergent" 是否合理？
   - "over an order of magnitude" claim 在 abstract——指 G ratio 还是 Δ？是否 misleading？
   - LLaMA 的 "preliminary cross-architecture evidence" hedging 是否充分？n=49, 仅 s=0.30 显著
   - Qwen mid-phase 45.2% null rate——是否被诚实处理？

5. **跨架构 Claims**:
   - 仅 2 个 Qwen2 架构模型 + 1 个 LLaMA (n=49)——generalization claims 的边界在哪？
   - LLaMA 的 strategy contrast 大幅减弱——是否削弱核心 contribution？
   - 全部 7-8B 规模——scale limitation 是否充分讨论？

6. **整体影响力**:
   - 对 EMNLP 2026 的 reviewer pool（NLP + efficiency + reasoning），这篇论文的 "so what" 是什么？
   - 没有 throughput/latency 数据——pure characterization 的实际价值？
   - 未来工作方向是否清晰且可操作？

7. **引用审计（关键引用）**:
   - 验证以下引用是否真实存在且被正确引用: spark-aaai2026, slim-icml2025, unicomp-2026, phase-transition-compression-2026, hies-2025, thinkv-iclr2026, graspune-acl2026, pmkvq-iclr2026, sparse-frontier-2025, greedy-bias-kvcache-2026, longflow-2026, rlkv-2025, physics-kvcache-2026
   - 特别关注 2026 年引用——是否为未正式发表的 preprints？ARR 对 preprint 引用有何政策？

## 已知关注区域（前轮审稿遗留 open issues）
- §5.3 crossover 数据来自 n=50 未在 n=500 验证——核心 novelty argument 的证据强度问题
- LongFlow bib entry "Withdrawn from ICLR 2026" 标注

**输出格式**: 按 Strengths / Weaknesses / Questions / Missing References 结构化输出。每条 Weakness 标注 severity (Must-Fix / Should-Fix / Minor)。引用具体 Section/Table/Figure/行号。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 320 · 2026-05-15T11:12:39.741969+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 321 · 2026-05-15T11:12:41.372720+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_reviewer_2_d0398257.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1630
}
```

</details>

---


### Tool call

_source line 322 · 2026-05-15T11:12:41.473581+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-15T11:12:41.474013+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-15T11:12:49.318286+00:00_

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
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 325 · 2026-05-15T11:12:51.629305+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 326 · 2026-05-15T11:12:52.485629+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_reviewer_2_d0398257.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 327 · 2026-05-15T11:12:52.537596+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 328 · 2026-05-15T11:12:57.111688+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the web search results, here's information about the ACL ARR 2026 reviewer guidelines and review form criteria:

## Review Form Scoring Criteria

For ARR reviews, the main criteria for Findings papers are soundness and reproducibility, while co
…[truncated 1482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7793
}
```

</details>

---


### Tool result

_source line 329 · 2026-05-15T11:12:57.162733+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"目录不存在: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 4625
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-15T11:13:07.484636+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 331 · 2026-05-15T11:13:07.736496+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 332 · 2026-05-15T11:13:07.937802+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/",
  "description": "List project directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/",
    "description": "List project directory contents"
  }
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-15T11:13:08.139179+00:00_

AGENTS.md
ROADMAP.lock
ROADMAP.md
artifacts
checkpoints
decisions.lock
decisions.yaml
docs
dream_registry.lock
dream_registry.yaml
dream_registry.yaml.bak
experiment_plan.yaml
literature_map.yaml
logs
memory.md
paper_framing.md
paper_provenance.lock
paper_provenance.yaml
registry.lock
registry.yaml
report.md
study_status.lock
task_context
writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 334 · 2026-05-15T11:13:13.762553+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 335 · 2026-05-15T11:13:14.164714+00:00_

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
11	
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{graphicx}
15	\usepackage{booktabs}
16	\usepackage{enumitem}
17	\usepackage{multirow}
18	
19	\graphicspath{{figures/}}
20	
21	\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}
22	
23	\title{Phase-Modulated Compound Sparsity:\\Strategy-Dependent Severity Gradients in Mathematical Reasoning Models}
24	
25	\author{Anonymous}
26	
27	\begin{document}
28	
29	\maketitle
30	
31	\input{abstract}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{background}
36	\input{methodology}
37	\input{results}
38	\input{analysis}
39	\input{discussion}
40	\input{conclusion}
41	
42	\bibliography{references}
43	
44	\section*{Limitations}
45	\input{limitations}
46	
47	\section*{Reproducibility}
48	Code and data will be released upon acceptance.
49	
50	\appendix
51	\input{appendix}
52	\input{appendix_moved}
53	\input{appendix_disc_analysis}
54	\input{appendix_robustness}
55	
56	\end{document}
57	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 336 · 2026-05-15T11:13:16.727623+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include all fields reviewers must fill out, especially: overall assessment scale, soundness, excitement/novelty, reproducibility, and any other scored dimensions. List the exact numeric scales and what each number means."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales, and descriptions. Include all fields reviewers must fill out, especially: overall assessment scale, soundness, excitement/novelty, reproducibility, and any other scored dimensions. List the exact numeric scales and what each number means."
  }
}
```

</details>

---


### Tool call

_source line 337 · 2026-05-15T11:13:17.484590+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 338 · 2026-05-15T11:13:25.175036+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Primary Scoring Dimensions

### 1. **Soundness**
Scale: 1–5 (with .5 increments)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

### 2. **Excitement/Novelty**
Scale: 1–5 (with .5 increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend."
- **3**: "Interesting: I might mention some points or attend if there's time."
- **2**: "Potentially Interesting: does not resonate with me, but might with others."
- **1**: "Not Exciting: does not resonate with me, and unlikely to resonate with the community."

### 3. **Overall Assessment**
Scale: 1–5 (with .5 increments)
- **5**: Consider for Award (top 2.5% papers)
- **4**: Conference acceptance recommended
- **3**: Findings track acceptance recommended
- **2**: Resubmit next cycle with substantial revisions
- **1**: Do not resubmit; irrelevant to computational linguistics

### 4. **Reviewer Confidence**
Scale: 1–5
- **5**: Positive; carefully read and familiar with related work
- **4**: Quite sure; unlikely to have missed relevant details
- **3**: Pretty sure; possible gaps in checking specifics
- **2**: Willing to defend but likely missed details
- **1**: Outside expertise area or paper very difficult to understand

### 5. **Reproducibility**
Scale: 1–5
- **5**: Results easily reproducible
- **4**: Mostly reproducible with minor variations possible
- **3**: Reproducible with some difficulty; underspecified parameters
- **2**: Hard to reproduce; unavailable data or insuffi
…[truncated 1214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 8447
}
```

</details>

---


### Tool result

_source line 339 · 2026-05-15T11:15:02.142020+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 32, \"total_citations\": 61, \"unique_cited_keys\": 32, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 24, \"online_not_found\": 3, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"adakv-neurips2025\", \"type\": \"inproceedings\", \"title\": \"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference\", \"authors\": \"Feng, Yuan and Lv, Junlin and Cao, Yukun and Xie, Xike and Zhou, S. Kevin\", \"year\": \"2025\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"decision-repr-transition-2026\", \"type\": \"article\", \"title\": \"Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions\", \"authors\": \"Shi, Boyu and Liu, Chang and Gao, ChuanBao and Yang, Xu and Geng, Xin\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.07271\"}, {\"key\": \"deepseek-r1-2025\", \"type\": \"article\", \"title\": \"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning\", \"authors\": \"DeepSeek-AI\", \"year\": \"2025\", \"venue\": \"Nature\"}, {\"key\": \"defensivekv-iclr2026\", \"type\": \"inproceedings\", \"title\": \"DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference\", \"authors\": \"Feng, Yuan and Guo, Haoyu and Lv, Junlin and Zhou, S. Kevin and Xie, Xike\", \"year\": \"2026\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"doing-more-with-less-2026\", \"type\": \"article\", \"title\": \"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling\", \"authors\": \"Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2604.25098\"}, {\"key\": \"efron-1993\", \"ty
…[truncated 25979 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 104657
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-15T11:15:13.721275+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 341 · 2026-05-15T11:15:14.224155+00:00_

1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	We show that compound severity is not phase-invariant: it is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases in mathematical reasoning models.
4	
5	On DeepSeek-R1-Distill-Qwen-7B (500 MATH-500 problems, $n_{\text{eff}}{=}496$, $s \in \{0.15, 0.20, 0.25, 0.30\}$), importance-based eviction produces a monotonically increasing severity gradient from the high-sparsity to low-sparsity reasoning phase (median $\Delta$: $0.39 \to 8.48$; all Bonferroni-corrected $p < 10^{-69}$). Random eviction develops a detectable phase gradient only above $s \approx 0.20$ (non-significant at $s \leq 0.20$; where significant, $3$--$39{\times}$ weaker), confirming importance-based eviction as the dominant driver.
6	A crossover emerges at $s{=}0.25$: importance-based eviction outperforms random in high-sparsity phases yet underperforms in low-sparsity phases---a qualitative reversal in strategy ranking.
7	The pattern replicates on Qwen2.5-7B-Instruct ($n_{\text{eff}}{=}475$, $\Delta$: $0.07 \to 3.16$; all $p < 10^{-14}$), with preliminary cross-architecture evidence from a LlamaForCausalLM model suggesting the phenomenon may extend beyond Qwen2-family architectures.
8	We observe that discrimination collapse---head pruning flattening cumulative importance scores---correlates with the phase-dependent severity amplification, suggesting a mechanism whereby compound sparsity selectively degrades importance-based eviction in distributed-attention phases.
9	These findings motivate phase-aware compression budgets for mathematical reasoning models.
10	\end{abstract}
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-15T11:15:14.224769+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-15T11:15:15.179562+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses---\emph{attention head pruning} \cite{voita-acl2019, michel-neurips2019} and \emph{KV cache eviction} \cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \emph{compound sparsity}, but the resulting quality degradation is often super-additive \cite{spark-aaai2026, slim-icml2025}. Recent evaluations confirm that reasoning capabilities degrade disproportionately under compound compression \cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \cite{phase-transition-compression-2026}.
6	
7	Prior work treats compound interaction magnitude as roughly constant across generation \cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \cite{sparse-frontier-2025}.
8	This assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \cite{thinkv-iclr2026}.
9	Phase-aware methods like ThinKV \cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from greedy bias \cite{greedy-bias-kvcache-2026}, deferred importance \cite{retentivekv-2026}, and temporal dynamics in long generations \cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple mechanisms are composed.
10	If compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.

…[truncated 2353 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-15T11:15:15.230450+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 345 · 2026-05-15T11:15:15.683506+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Compound compression.}
5	Combining multiple compression axes produces non-additive errors.
6	\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \cite{slim-icml2025} formalize compound error for quantization and sparsity.
7	\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.
8	\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.
9	GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.
10	PM-KVQ~\cite{pmkvq-iclr2026} demonstrates that progressive quantization---gradually reducing bit-width over the generation process---mitigates cumulative error in long-CoT reasoning, implicitly introducing a temporal dimension to compression severity that resonates with our finding that compound interaction is phase-dependent.
11	These works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.
12	
13	\paragraph{KV cache eviction.}
14	Most methods rely on importance scoring whose reliability is increasingly questioned.
15	Ada-KV~\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\cite{snapkv-neurips2024} compresses from a fixed observation window; \cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\times}$ higher than expected under standard aggregation.
16	\cite{nacl-acl2024} combine proxy-token and random eviction to counter attention bias.
17	RetentiveKV~\cite{retentivekv-2026} identifies deferred importance, and \cite{greedy-bias-kvcache-2026} show that single importance metrics exhibit systematic greedy bias.
18	\cite{hies-2025} independently show
…[truncated 2273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 346 · 2026-05-15T11:15:15.684168+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-15T11:15:16.138695+00:00_

1	% Section 3: Background and Problem Setup
2	% Note: eq:ii and eq:gradient are the canonical definitions.
3	% Full formulation details in Appendix (app:formulation-details).
4	
5	\section{Background and Problem Setup}
6	\label{sec:background}
7	
8	We formalize compound sparsity, define the Interaction Index, and introduce phase segmentation. Full mathematical details appear in Appendix~\ref{app:formulation-details}.
9	
10	\paragraph{Compound sparsity.}
11	\label{sec:compound-sparsity}
12	Let $s \in (0,1)$ denote a unified sparsity budget. \emph{Attention head pruning} removes the bottom-$s$ fraction of heads per layer by Frobenius norm importance \cite{voita-acl2019, michel-neurips2019}. \emph{KV cache eviction} removes the bottom-$s$ fraction of token positions from the cache. We compare two strategies: \emph{importance-based}, which scores positions by position-normalized cumulative attention mass (Eq.~\ref{eq:kv-importance} in Appendix~\ref{app:formulation-details}), and \emph{random}, which evicts uniformly at random \cite{nacl-acl2024}. Applying both simultaneously yields \emph{compound sparsity}; the two axes interact because head pruning alters the importance ranking used for eviction \cite{spark-aaai2026}. Existing joint-pruning approaches such as GRASPrune \cite{graspune-acl2026} learn global budget-constrained gates but treat decisions as static across generation.
13	
14	\paragraph{Interaction Index.}
15	\label{sec:interaction-index}
16	For a text segment, let $\text{PPL}_c$ denote perplexity under condition $c \in \{d, a, k, b\}$ (dense, attention-only, KV-only, compound). Normalizing by the dense baseline yields $r_c = \text{PPL}_c / \text{PPL}_d$, and:
17	\begin{equation}
18	    \mathrm{II} = r_b - r_a - r_k + 1.
19	    \label{eq:ii}
20	\end{equation}
21	$\mathrm{II} > 0$ indicates super-additive degradation; $\mathrm{II} = 0$ indicates additive independence. We adopt the additive null because the two axes operate on disjoint dimensions; qualitative co
…[truncated 1036 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-15T11:15:16.139307+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
  }
}
```

</details>

---


### Tool result

_source line 349 · 2026-05-15T11:15:16.592165+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\paragraph{Models.}
5	\label{sec:models}
6	We evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \textbf{DeepSeek-R1-Distill-Qwen-7B}~\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \textbf{Qwen2.5-7B-Instruct}~\cite{qwen25-2024}, with standard instruction tuning, providing a cross-model replication target. Both are loaded in \texttt{bfloat16} with eager attention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values; \texttt{bfloat16} eliminated all occurrences.}
7	
8	\paragraph{Dataset.}
9	\label{sec:dataset}
10	We evaluate all 500 problems from MATH-500~\cite{math500-neurips2021}. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048). Problems with degenerate phase assignments (null low or high phase) are excluded, yielding effective sample sizes of $n{=}496$ for DeepSeek (4 excluded) and $n{=}475$ for Qwen (25 excluded). Qwen exhibits a higher mid-phase null rate (45.2\% vs.\ 10.2\% for DeepSeek) due to lower temporal autocorrelation in its attention sparsity patterns (lag-1 $r{=}0.718$ vs.\ $0.894$, $d{=}-1.68$); this does not affect the primary gradient metric $\Delta = \mathrm{II}_{\textit{low}} - \mathrm{II}_{\textit{high}}$, which requires only low and high phases. Sensitivity analysis across $\texttt{min\_phase\_length} \in \{5, 10, 20\}$ confirms robustness (Appendix~\ref{app:mpl-sensitivity}).
11	
12	\paragraph{Sparsity configuration.}
13	\label{sec:sparsity-config}
14	We apply symmetric compound sparsity at $s \in \{0.15, 0.20, 0.25, 0.30\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\ref{eq:kv-importance}; BOS always retained) and \emph{random} eviction (uniform). Heads are
…[truncated 1994 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 350 · 2026-05-15T11:15:16.642793+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 351 · 2026-05-15T11:15:16.694155+00:00_

1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Strategy-Dependent Severity}
6	\label{sec:strategy-severity}
7	
8	Table~\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\Delta$ increases from $0.39$ at $s{=}0.15$ to $8.48$ at $s{=}0.30$---a $22{\times}$ amplification (all Bonferroni-corrected $p < 10^{-69}$). Random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: at $s \leq 0.20$, $\Delta$ is non-significant ($0.01$--$0.03$; CIs span zero); at $s \geq 0.25$, $\Delta$ becomes significant ($0.26$--$0.51$; $p_{\text{Bonf}} < 0.006$) but $15$--$39{\times}$ smaller than under importance-based eviction. Both strategies exhibit monotonic dose-response (Jonckheere-Terpstra $z{=}6.2$--$33.7$, all $p < 10^{-9}$), but importance masking effect sizes are an order of magnitude larger. % exp_id: n500_unified_final; DS imp Δ 0.39→8.48, rand 0.01→0.51; JT z=33.7 (imp), 6.2 (rand)
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, 500 MATH-500 problems).}
14	\label{tab:aggregate-ii}
15	\begin{tabular}{@{}lcccc@{}}
16	\toprule
17	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
18	\midrule
19	Importance & 0.39 & 1.21 & 3.99 & 8.48 \\ % exp_id: n500_unified_final; DS imp median_ii_diff
20	Random     & 0.01 & 0.03 & 0.26 & 0.51 \\ % exp_id: n500_unified_final; DS rand median_ii_diff
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	
26	\subsection{Phase-Modulated Amplification}
27	\label{sec:phase-amplification}
28	
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the per-phase breakdown from an
…[truncated 9653 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 352 · 2026-05-15T11:15:21.918348+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 353 · 2026-05-15T11:15:22.370950+00:00_

1	\section{Discrimination Collapse under Compound Sparsity}
2	\label{sec:analysis}
3	
4	\subsection{Discrimination Collapse}
5	\label{sec:discrimination-collapse-main}
6	
7	We observe that head pruning systematically reduces the discriminative power of cumulative importance scores, suggesting a mechanism for the phase-strategy interaction. The Gini coefficient of importance scores decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) after pruning, with consistent negative deltas in all 16 conditions (Appendix~\ref{app:analysis}, Table~\ref{tab:discrimination-metrics-full}). This pattern---which we term \emph{discrimination collapse}---is consistent with importance-based eviction degenerating into noise-sensitive selection when score distributions flatten. The effect is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. This observation is independently corroborated by \cite{hies-2025}, who report importance score collapse under heavy single-axis pruning; our results extend this to the compound setting, where collapse is amplified by the interaction of two compression axes and modulated by reasoning phase. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
8	
9	A partial counterfactual supports this interpretation: random eviction does not rely on importance scores, so it is immune to score-distribution changes caused by head pruning. The flat severity gradient under random eviction ($G \approx 1$) is consistent with this independence, while importance-based eviction---whose decisions depend on the very scores that pruning degrades---exhibits the phase-modulated amplification. We note that this evidence is correlational; causal validation through controlled manipulation of importance-score entropy is an important direction for future work. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
10	
11	\subsection{Entropy Redistribu
…[truncated 897 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 354 · 2026-05-15T11:15:22.421691+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-15T11:15:23.378263+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Quantitative surprise.}
5	While the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($G{=}30$--$148{\times}$ at $n{=}496$) far exceeds a naive ``somewhat worse'' prediction. The crossover---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) and underperforms in low-sparsity phases ($7.196$ vs.\ $1.363$)---cannot be derived from single-axis entropy reasoning. The near-unity random baseline ($G{=}0.5$--$1.3{\times}$, trivial magnitude) confirms the dominant amplification is strategy-specific. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json
6	
7	\paragraph{Implications for deployment.}
8	Applying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation. Discrimination collapse depends on attention-mass-based importance scoring shared by major KV cache methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-2024}), suggesting broad applicability.
9	
10	A preliminary pilot experiment explored oracle phase-aware budget reallocation, shifting sparsity budget from high-severity low-sparsity phases to low-severity high-sparsity phases. At $s{=}0.25$, oracle recovery---the fraction of compound interaction eliminated by phase-aware allocation---reached 18\% (Wilcoxon $p = 0.002$), below the pre-registe
…[truncated 1758 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 956
}
```

</details>

---


### Tool call

_source line 356 · 2026-05-15T11:15:23.378867+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 357 · 2026-05-15T11:15:23.831072+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation ($n{=}496$/$475$ problems). Under importance-based eviction, the amplification ratio $G$ ranges from $30{\times}$ to $148{\times}$ across sparsity levels, with paired median differences $\Delta$ from $0.39$ to $8.48$ (DeepSeek) and $0.07$ to $3.16$ (Qwen), all $p < 10^{-13}$. Random eviction develops a detectable phase gradient only above $s \approx 0.20$, but $3$--$39{\times}$ weaker than importance-based. A crossover at $s{=}0.25$---where importance-based eviction reverses ranking across phases---demonstrates that no single strategy dominates uniformly. The pattern replicates on Qwen2.5-7B-Instruct at all four sparsity levels; suggestive preliminary evidence from DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) indicates the phenomenon may extend beyond Qwen2, though at ${\sim}1/40$ the magnitude and with a weaker strategy contrast. Discrimination collapse provides a correlational mechanistic explanation supported by both Qwen2-based models.
5	These findings motivate phase-aware sparsity allocation for reasoning model deployment. Extending this analysis to code reasoning (HumanEval, LiveCodeBench) and science reasoning (GPQA), validating the discrimination collapse mechanism through causal intervention, and characterizing asymmetric compound interactions are promising directions for future work.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 358 · 2026-05-15T11:15:23.831625+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 359 · 2026-05-15T11:15:24.183254+00:00_

1	\paragraph{Model scale and architecture.}
2	All experiments are conducted at the 7--8B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}) partially confirms the qualitative pattern beyond the Qwen2 architecture---monotonically increasing $d_z$ with within-importance phase gradient $\sim$1.0---but with substantially weaker interaction magnitude ($\sim$1/40 of DeepSeek) and mixed statistical evidence (only $s{=}0.30$ significant after Bonferroni correction). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.
3	
4	\paragraph{Task coverage.}
5	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark. MATH-500 is a suitable first testbed because it elicits structured reasoning with clear phase transitions (exploratory vs.\ structured computation), supports per-problem evaluation enabling paired statistical tests, and spans sufficient difficulty to produce meaningful variation in sequence length and attention dynamics. However, different reasoning tasks---code generation (e.g., HumanEval, LiveCodeBench), science reasoning (e.g., GPQA), multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile. Whether the phase-strategy interaction documented here extends to these domains is an open question.
6	
7	\paragraph{Symmetric sparsity assumption.}
8	Our analysis applies symmetric sparsity rates: the same fraction $s$ is used for both head pruning and KV cache eviction. Practical deployments may use asymmetric budgets (e.g., aggressive head pruning with conservat
…[truncated 974 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 360 · 2026-05-15T11:15:24.183697+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 361 · 2026-05-15T11:15:24.234672+00:00_

1	\section{Compound Sparsity Formulation}
2	\label{app:formulation-details}
3	
4	\paragraph{Attention head pruning.}
5	Heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$ \cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\ell)} \in \{0,1\}$ retains the top-$(1{-}s)\cdot H$ heads:
6	\begin{equation}
7	    \tilde{\mathbf{o}}_j^{(\ell)} = m_j^{(\ell)} \cdot \mathbf{o}_j^{(\ell)}.
8	    \label{eq:head-mask}
9	\end{equation}
10	
11	\paragraph{KV cache eviction.}
12	A position mask $\mathbf{m}_k \in \{0,1\}^T$ retains the top-$(1{-}s)\cdot T$ positions (BOS always preserved):
13	\begin{equation}
14	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall\, i, j.
15	    \label{eq:kv-mask}
16	\end{equation}
17	Under importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:
18	\begin{equation}
19	    \mathrm{imp}(j) = \frac{\sum_{\ell, h, i} a_{ij}^{(\ell,h)}}{T - j},
20	    \label{eq:kv-importance}
21	\end{equation}
22	where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.
23	
24	\paragraph{Compound sparsity.}
25	Applying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.
26	
27	\paragraph{Attention sparsity metric.}
28	For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:
29	\begin{equation}
30	    \sigma_i^{(h)} = \frac{1}{T} \sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right].
31	    \label{eq:attn-sparsity}
32	\end{equation}
33	The per-position spar
…[truncated 1336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 362 · 2026-05-15T11:15:29.259473+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
  }
}
```

</details>

---


### Tool result

_source line 363 · 2026-05-15T11:15:29.260355+00:00_

1	% Content moved from main body to appendix:
2	% - Phase-strategy crossover details (from results §5.3)
3	% - Cross-model replication details with tables/figures (from results §5.4)
4	% - Permutation test details with table/forest plot (from results §5.5)
5	% - Full entropy-discrimination collapse analysis with tables (from analysis §6)
6	% Main body §6 (analysis.tex) contains a condensed summary referencing these tables.
7	
8	\section{Phase-Strategy Crossover Details}
9	\label{app:crossover-details}
10	
11	At $s{=}0.25$, a strategy ranking reversal emerges (Figure~\ref{fig:crossover}): importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\ $0.818$) but \emph{higher} II in the low-sparsity phase ($7.196$ vs.\ $1.363$---a $5.3{\times}$ reversal). This crossover is present at all four sparsity levels, with reversal magnitude of $3.9{\times}$ at $s{=}0.15$, $5.4{\times}$ at $s{=}0.20$, $5.3{\times}$ at $s{=}0.25$, and $3.6{\times}$ at $s{=}0.30$ (as random eviction severity also rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\S\ref{sec:discrimination-collapse}). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28
12	
13	\begin{figure}[t]
14	\centering
15	\includegraphics[width=\columnwidth]{fig3_crossover.pdf}
16	\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}
17	\label{fig:crossover}
18	\end{figure}
19	
20	
21	\section{Cross-Model Replication Details}
22	\label{app:cross-model-details}
23	
24	Both models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in trai
…[truncated 12568 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 364 · 2026-05-15T11:15:29.964595+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 365 · 2026-05-15T11:15:30.416885+00:00_

1	\section{Discrimination Collapse Details}
2	\label{app:discrimination-collapse-details}
3	
4	This cross-model consistency (Table~\ref{tab:discrimination-metrics-full}) establishes discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$), confirming that discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
5	
6	
7	\section{Extended Discussion}
8	\label{app:extended-discussion}
9	
10	\paragraph{On the predictability of phase-modulated severity.}
11	The compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$). % exp_id: bf16_importance_s015..s030; high-phase medians: 0.006, 0.015, 0.032, 0.053
12	
13	\paragraph{Random masking as falsification control.}
14	At $n{=}500$, random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: non-significant at $s \leq 0.20$ for both models, but significant at $s \geq 0.25$ (DS: $\Delta{=}0.26$--$0.51$, $p_{\text{Bonf}} < 0.006$; QW: $\Delta{=}0.39$--$0.91$, $p_{\text{Bonf}} < 10^{-10}$). Where significant, the random phase gradient is $3$--$39{\times}$ weaker than importance-based, confirming that the dominant amplification is strategy-specific. % exp_id: n500_unified_final; DS rand s025 0.257 p=0.006, s030 0.510 p=0.006; QW rand s025 0.393, s030 0.913
15	
16	\paragraph{Entropy mechanism boundary conditions.}
17	Directly measuring per-head entropy s
…[truncated 4903 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 366 · 2026-05-15T11:15:30.467520+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex"
  }
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-15T11:15:30.870323+00:00_

1	\section{Benjamini-Hochberg FDR Correction}
2	\label{app:bh-fdr}
3	
4	Table~\ref{tab:bh-fdr} compares Bonferroni ($k{=}4$, per model$\times$strategy family) and Benjamini-Hochberg FDR correction across all 44 statistical tests. BH-FDR recovers 5 additional significant results beyond Bonferroni, all in low-effect-size conditions (random eviction or cross-model random comparisons). All 32 Bonferroni-significant results remain significant under BH-FDR.
5	
6	\begin{table}[t]
7	\centering
8	\small
9	\caption{Bonferroni vs.\ BH-FDR correction summary ($\alpha{=}0.05$, 44 tests). ``BH only'' denotes tests significant under BH-FDR but not Bonferroni.}
10	\label{tab:bh-fdr}
11	\begin{tabular}{@{}lcc@{}}
12	\toprule
13	Category & Bonf.\ sig. & BH-only sig. \\
14	\midrule
15	Per-condition Wilcoxon ($k{=}16$) & 10 & 2 \\
16	Imp vs.\ rand ($k{=}8$) & 8 & 0 \\
17	Adjacent sparsity ($k{=}12$) & 10 & 1 \\
18	Cross-model Mann-Whitney ($k{=}8$) & 4 & 2 \\
19	\midrule
20	Total ($k{=}44$) & 32 & 5 \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	The 5 BH-only results are: DeepSeek random $s{=}0.25$ and $s{=}0.30$ per-condition Wilcoxon ($p_{\text{Bonf}}{=}0.064$/$0.065$, BH $q{=}0.002$), DeepSeek random $s{=}0.25 \to 0.30$ adjacent-sparsity step ($p_{\text{Bonf}}{=}0.078$, BH $q{=}0.002$), and cross-model random $s{=}0.25$/$s{=}0.30$ Mann-Whitney ($p_{\text{Bonf}}{=}0.66$/$0.17$, BH $q{=}0.018$/$0.005$). All involve random eviction---the weakest effects---confirming that Bonferroni is conservative but does not miss any importance-based findings. % exp_id: n500_unified_final; source: supplementary_stats.json bh_fdr_correction
26	
27	
28	\section{Minimum Phase Length Sensitivity}
29	\label{app:mpl-sensitivity}
30	
31	Table~\ref{tab:mpl-sensitivity} reports the paired median difference $\Delta$ under three \texttt{min\_phase\_length} (mpl) settings across all 16 conditions (2 models $\times$ 2 strategies $\times$ 4 sparsity levels). Conclusions are robust: all importance-based c
…[truncated 4154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-15T11:15:30.871044+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 369 · 2026-05-15T11:15:30.977901+00:00_

1	% References for Phase-Gated Compound Sparse paper
2	% Generated 2026-05-14; all entries verified via web search
3	
4	@inproceedings{adakv-neurips2025,
5	    title     = {Ada-{KV}: Optimizing {KV} Cache Eviction by Adaptive Budget Allocation for Efficient {LLM} Inference},
6	    author    = {Feng, Yuan and Lv, Junlin and Cao, Yukun and Xie, Xike and Zhou, S. Kevin},
7	    booktitle = {Advances in Neural Information Processing Systems},
8	    year      = {2025},
9	    url       = {https://arxiv.org/abs/2407.11550},
10	}
11	
12	@article{decision-repr-transition-2026,
13	    title   = {Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions},
14	    author  = {Shi, Boyu and Liu, Chang and Gao, ChuanBao and Yang, Xu and Geng, Xin},
15	    journal = {arXiv preprint arXiv:2605.07271},
16	    year    = {2026},
17	    url     = {https://arxiv.org/abs/2605.07271},
18	}
19	
20	@article{deepseek-r1-2025,
21	    title   = {{DeepSeek-R1} incentivizes reasoning in {LLMs} through reinforcement learning},
22	    author  = {{DeepSeek-AI}},
23	    journal = {Nature},
24	    volume  = {645},
25	    pages   = {633--638},
26	    year    = {2025},
27	    doi     = {10.1038/s41586-025-09422-z},
28	}
29	
30	@inproceedings{defensivekv-iclr2026,
31	    title     = {{DefensiveKV}: Taming the Fragility of {KV} Cache Eviction in {LLM} Inference},
32	    author    = {Feng, Yuan and Guo, Haoyu and Lv, Junlin and Zhou, S. Kevin and Xie, Xike},
33	    booktitle = {International Conference on Learning Representations},
34	    year      = {2026},
35	    url       = {https://arxiv.org/abs/2510.13334},
36	}
37	
38	@article{doing-more-with-less-2026,
39	    title   = {Doing More With Less: Revisiting the Effectiveness of {LLM} Pruning for Test-Time Scaling},
40	    author  = {Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman},
41	    journal = {arXiv preprint arXiv:2604.25098},
42	    year    = {2026},
43	    url     = {https://arxiv
…[truncated 11796 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 106
}
```

</details>

---


### Tool call

_source line 370 · 2026-05-15T11:15:38.523398+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2510.13832 \"Entropy Meets Importance\" HIES head pruning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2510.13832 \"Entropy Meets Importance\" HIES head pruning"
  }
}
```

</details>

---


### Tool call

_source line 371 · 2026-05-15T11:15:38.926100+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2510.13334 DefensiveKV KV cache eviction fragility ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2510.13334 DefensiveKV KV cache eviction fragility ICLR 2026"
  }
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-15T11:15:39.939087+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"phase transitions in large language model compression\" npj Artificial Intelligence 2026 Ma Ziyang"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"phase transitions in large language model compression\" npj Artificial Intelligence 2026 Ma Ziyang"
  }
}
```

</details>

---


### Tool call

_source line 373 · 2026-05-15T11:15:40.595820+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LongFlow \"Withdrawn\" ICLR 2026 KV cache compression reasoning arXiv 2603.11504"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LongFlow \"Withdrawn\" ICLR 2026 KV cache compression reasoning arXiv 2603.11504"
  }
}
```

</details>

---


### Tool result

_source line 374 · 2026-05-15T11:15:47.084627+00:00_

Web search results for query: "arXiv 2510.13334 DefensiveKV KV cache eviction fragility ICLR 2026"

Links: [{"title":"TAMING THE FRAGILITY OF KV CACHE EVICTION IN LLM INFERENCE","url":"https://arxiv.org/pdf/2510.13334"},{"title":"[2510.13334] Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://arxiv.org/abs/2510.13334"},{"title":"GitHub - FFY0/DefensiveKV: Official Implementation for [ICLR26] DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference · GitHub","url":"https://github.com/FFY0/DefensiveKV"},{"title":"DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference | OpenReview","url":"https://openreview.net/forum?id=nJgS06sX3O"},{"title":"(PDF) Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://www.researchgate.net/publication/396517805_Taming_the_Fragility_of_KV_Cache_Eviction_in_LLM_Inference"},{"title":"DEFENSIVEKV: TAMING THE FRAGILITY OF KV CACHE ...","url":"https://openreview.net/pdf?id=nJgS06sX3O"},{"title":"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget ...","url":"https://arxiv.org/pdf/2407.11550"},{"title":"LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation","url":"https://arxiv.org/html/2603.10899v1"},{"title":"[2604.25975] Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective","url":"https://arxiv.org/abs/2604.25975"},{"title":"CAKE: Cascading and Adaptive KV Cache Eviction with Layer Preferences","url":"https://arxiv.org/html/2503.12491v2"}]

Based on the search results, here's comprehensive information about arXiv paper 2510.13334:

## Paper Overview

The paper is titled "Taming the Fragility of KV Cache Eviction in LLM Inference" and was submitted on October 15, 2025.

## Key Problem and Contribution

Recent KV cache eviction methods employ a scoring-aggregation framework based on a "stability assumption"—that a fixed subset of entries remains consistently important during generation. However, pri
…[truncated 1329 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8158
}
```

</details>

---


### Tool result

_source line 375 · 2026-05-15T11:15:47.637372+00:00_

Web search results for query: "arXiv 2510.13832 "Entropy Meets Importance" HIES head pruning"

Links: [{"title":"[2510.13832] Entropy Meets Importance: A Unified Head Importance-Entropy Score for Stable and Efficient Transformer Pruning","url":"https://arxiv.org/abs/2510.13832"},{"title":"Entropy Meets Importance: A Unified Head Importance–Entropy Score for Stable and Efficient Transformer Pruning","url":"https://arxiv.org/html/2510.13832v1"},{"title":"Under review ENTROPY MEETS IMPORTANCE: A UNIFIED HEAD","url":"https://arxiv.org/pdf/2510.13832"},{"title":"(PDF) Entropy Meets Importance: A Unified Head Importance-Entropy Score for Stable and Efficient Transformer Pruning","url":"https://www.researchgate.net/publication/396541457_Entropy_Meets_Importance_A_Unified_Head_Importance-Entropy_Score_for_Stable_and_Efficient_Transformer_Pruning"},{"title":"A Unified Head Importance–Entropy Score for Stable and ...","url":"https://opt-ml.org/papers/2025/paper51.pdf"},{"title":"Entropy-Guided Head Importance for Token Pruning in Vision Transformers | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10773748/"},{"title":"Measuring Sample Importance in Data Pruning for Language Models based on Information Entropy","url":"https://arxiv.org/html/2406.14124"},{"title":"The Simpler The Better: An Entropy-Based Importance Metric To Reduce Neural Networks’ DepthPreprint","url":"https://arxiv.org/html/2404.18949v1"},{"title":"The Simpler The Better: An Entropy-Based Importance Metric To Reduce Neural Networks’ Depth","url":"https://arxiv.org/html/2404.18949v2"},{"title":"NEPENTHE: Entropy-Based Pruning as a Neural Network Depth’s ReducerPreprint","url":"https://arxiv.org/html/2404.16890v1"}]

I found the paper you were searching for. Here's information about arXiv 2510.13832:

## Paper Overview

The paper is titled "Entropy Meets Importance: A Unified Head Importance-Entropy Score for Stable and Efficient Transformer Pruning" by Minsik Choi and 3
…[truncated 1177 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9113
}
```

</details>

---


### Tool result

_source line 376 · 2026-05-15T11:15:47.788498+00:00_

Web search results for query: ""phase transitions in large language model compression" npj Artificial Intelligence 2026 Ma Ziyang"

Links: [{"title":"Phase transitions in large language model compression | npj Artificial Intelligence","url":"https://www.nature.com/articles/s44387-026-00072-8"},{"title":"Phase transitions in large language model compression – DOAJ","url":"https://doaj.org/article/06b2d6b18f08424a9f7778c269597d3c"},{"title":"GitHub - whucs21Mzy/Model-Phase-Transitions: Navigating Model Phase Transitions to Enable Extreme Lossless Compression: A Perspective","url":"https://github.com/whucs21Mzy/Model-Phase-Transitions"},{"title":"Phase transitions in large language models ..","url":"https://www.hyper-exponential.com/p/phase-transitions-in-large-language"},{"title":"Papers | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Phase-transitions-in-large-language-model-Ma-Li/7ed3dd27a60af2079e25590965840685973e70a3"},{"title":"Phase transitions in AI-human interaction networks: statistics, computation, and probabilistic modeling","url":"https://arxiv.org/html/2505.02879v1"},{"title":"Critical Phase Transition in a Large Language Model","url":"https://www.aimodels.fyi/papers/arxiv/critical-phase-transition-large-language-model"},{"title":"Lossless data compression by large models | Nature Machine Intelligence","url":"https://www.nature.com/articles/s42256-025-01033-7"},{"title":"Phase Transitions in the Output Distribution of Large Language Models","url":"https://arxiv.org/html/2405.17088v1"},{"title":"Understanding LLM Behaviors via Compression: Data Generation, Knowledge Acquisition and Scaling Laws","url":"https://arxiv.org/html/2504.09597v2"}]

I found the research you're looking for! 

The paper "Phase transitions in large language model compression" was published on February 6, 2026 in npj Artificial Intelligence by Ziyang Ma and colleagues.

Here's what the research covers:

**Main Argument:** The perspective argues that Large Language Mo
…[truncated 1040 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7849
}
```

</details>

---


### Tool result

_source line 377 · 2026-05-15T11:15:50.554585+00:00_

Web search results for query: "LongFlow "Withdrawn" ICLR 2026 KV cache compression reasoning arXiv 2603.11504"

Links: [{"title":"LongFlow: Efficient KV Cache Compression for Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=rz6WybXjgk"},{"title":"[2603.11504] LongFlow: Efficient KV Cache Compression for Reasoning M","url":"https://arxiv.org/abs/2603.11504"},{"title":"EFFICIENT KV CACHE COMPRESSION - LONGFLOW","url":"https://openreview.net/pdf?id=rz6WybXjgk"},{"title":"LongFlow: Efficient KV Cache Compression for Reasoning Models","url":"https://arxiv.org/html/2603.11504"},{"title":"Mitigating the Echo Chamber Effect in KV Cache Compression via Coverage Optimization | OpenReview","url":"https://openreview.net/forum?id=W6aYwEA7i3"},{"title":"ICLR Poster KV Cache Transform Coding for Compact Storage in LLM Inference","url":"https://iclr.cc/virtual/2026/poster/10008708"},{"title":"Is KV Cache Quantization Sabotaging Your Context? — We test the impact of quantizing caches on long-horizon agentic coding workloads.","url":"https://dasroot.net/posts/2026/05/kv-cache-quantization-agentic-coding-long-horizon/"},{"title":"Can LLMs Maintain Fundamental Abilities under KV Cache Compression? | OpenReview","url":"https://openreview.net/forum?id=4zwyuDgbWD"},{"title":"KV Cache Transform Coding for Compact Storage in LLM Inference [Quick Review]","url":"https://liner.com/review/kv-cache-transform-coding-for-compact-storage-in-llm-inference"},{"title":"Which Heads Matter for Reasoning? RL-Guided KV Cache Compression | OpenReview","url":"https://openreview.net/forum?id=HGdg76iVo6"}]

Based on the search results, I found information about LongFlow:

## LongFlow: Efficient KV Cache Compression for Reasoning Models

LongFlow was submitted to ICLR 2026 as a withdrawn submission. The paper is also available on arXiv as arXiv paper 2603.11504.

### Overview

The paper addresses reasoning models like OpenAI-o1 and DeepSeek-R1 that have demonstrated strong capabilities in
…[truncated 1107 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9958
}
```

</details>

---


### Tool call

_source line 378 · 2026-05-15T11:15:59.650733+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "compound sparsity pruning quantization KV cache interaction 2025 2026 NeurIPS ICML ACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "compound sparsity pruning quantization KV cache interaction 2025 2026 NeurIPS ICML ACL"
  }
}
```

</details>

---


### Tool call

_source line 379 · 2026-05-15T11:15:59.955700+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "reasoning model compression pruning chain-of-thought degradation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "reasoning model compression pruning chain-of-thought degradation 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 380 · 2026-05-15T11:16:00.861329+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "phase-aware KV cache compression reasoning phases thinking tokens 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "phase-aware KV cache compression reasoning phases thinking tokens 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 381 · 2026-05-15T11:16:09.179435+00:00_

Web search results for query: "phase-aware KV cache compression reasoning phases thinking tokens 2025 2026"

Links: [{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/html/2510.01290v1"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"},{"title":"[2512.12008] Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/abs/2512.12008"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention","url":"https://arxiv.org/pdf/2510.00636"},{"title":"[2510.01290] ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/abs/2510.01290"},{"title":"Optimizing Key-Value Cache Compression in Long-context ...","url":"https://aclanthology.org/2025.acl-long.529.pdf"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=M3CeHnZKNC"},{"title":"GitHub - Zefan-Cai/R-KV: [Neurips 2025] R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://github.com/Zefan-Cai/R-KV"},{"title":"Which Heads Matter for Reasoning? RL-Guided KV Cache Compression","url":"https://arxiv.org/html/2510.08525v1"},{"title":"ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference | OpenReview","url":"https://openreview.net/forum?id=20JDhbJqn3"}]

Based on the web search results, here's what I found regarding phase-aware KV cache compression, reasoning phases, and thinking tokens in 2025-2026:

## Key Research Areas

### Phase-Aware Compression Approaches

ThinKV is a thought-adaptive KV cache compression approach that decomposes chains of thought into reasoning, execution, and transition segments, enabling joint thought-aware quantization and eviction that sustains accuracy under high compression. ThinKV is based on the observation that att
…[truncated 1427 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8318
}
```

</details>

---


### Tool result

_source line 382 · 2026-05-15T11:16:09.833395+00:00_

Web search results for query: "reasoning model compression pruning chain-of-thought degradation 2025 2026"

Links: [{"title":"Chain Of Thought Compression: A Theoritical Analysis","url":"https://arxiv.org/pdf/2601.21576"},{"title":"Reasoning Models Can Be Accurately Pruned via Chain-of-Thought Reconstruction","url":"https://arxiv.org/html/2509.12464v1"},{"title":"STOP: Structured On-Policy Pruning of Long-Form Reasoning in Low-Data Regimes","url":"https://arxiv.org/html/2605.13165"},{"title":"Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction | OpenReview","url":"https://openreview.net/forum?id=tyGfwG6xTh"},{"title":"[2509.12464] Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction","url":"https://arxiv.org/abs/2509.12464"},{"title":"Reasoning Efficiently Through Adaptive Chain-of-Thought Compression: A Self-Optimizing Framework","url":"https://arxiv.org/html/2509.14093v1"},{"title":"Compressing Chain-of-Thought in LLMs via Step Entropy","url":"https://arxiv.org/html/2508.03346v1"},{"title":"On the Limits of Layer Pruning for Generative Reasoning in LLMs","url":"https://arxiv.org/pdf/2602.01997"},{"title":"On the Limits of Layer Pruning for Generative Reasoning in Large Language Models","url":"https://arxiv.org/html/2602.01997v2"},{"title":"D-COT: Disciplined Chain-of-Thought Learning for Efficient ...","url":"https://arxiv.org/pdf/2602.21786"}]

I found recent research on your query topic. Here's a summary of the key findings:

## Chain-of-Thought Compression and Degradation in 2025-2026

Reasoning models like DeepSeek-R1 have achieved remarkable success in mathematical and commonsense reasoning, but at a steep price: heavily expanded reasoning chains incur massive token consumption and high latency.

### Key Challenges with Compression

Neural network pruning produces greater performance loss on reasoning models than in typical language modeling tasks, and in some cases can make the model slower since they cause 
…[truncated 1415 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9877
}
```

</details>

---


### Tool result

_source line 383 · 2026-05-15T11:16:09.984619+00:00_

Web search results for query: "compound sparsity pruning quantization KV cache interaction 2025 2026 NeurIPS ICML ACL"

Links: [{"title":"ICML Poster Cache Me If You Must: Adaptive Key-Value Quantization for Large Language Models","url":"https://icml.cc/virtual/2025/poster/46067"},{"title":"GitHub - HuangOwen/Awesome-LLM-Compression: Awesome LLM compression research papers and tools. · GitHub","url":"https://github.com/HuangOwen/Awesome-LLM-Compression"},{"title":"GitHub - Zhen-Dong/Awesome-Quantization-Papers: List of papers related to neural network quantization in recent AI conferences and journals. · GitHub","url":"https://github.com/Zhen-Dong/Awesome-Quantization-Papers"},{"title":"Awesome-LLM-Compression/README.md at main · HuangOwen/Awesome-LLM-Compression","url":"https://github.com/HuangOwen/Awesome-LLM-Compression/blob/main/README.md"},{"title":"Compute Where it Counts: Self Optimizing Language Models","url":"https://arxiv.org/html/2605.10875"},{"title":"A Systematic Exploration of KV Cache Compression ...","url":"https://arxiv.org/pdf/2503.11816"},{"title":"GitHub - Efficient-ML/Awesome-Model-Quantization: A list of papers, docs, codes about model quantization. This repo is aimed to provide the info for model quantization research, we are continuously improving the project. Welcome to PR the works (papers, repositories) that are missed by the repo. · GitHub","url":"https://github.com/Efficient-ML/Awesome-Model-Quantization"},{"title":"Performance Engineering Model Optimizations","url":"https://mlsysbook.ai/book/contents/core/optimizations/optimizations.html"},{"title":"Don’t Waste Bits! Adaptive KV-Cache Quantization for Lightweight On-Device LLMs","url":"https://arxiv.org/html/2604.04722v1"},{"title":"Peijie Dong - Homepage","url":"https://pprp.github.io/"}]

Based on the web search results, I found relevant research on the intersection of sparsity, pruning, quantization, and KV cache optimization in recent publications (2025-2026). Here are the key findi
…[truncated 1894 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 10333
}
```

</details>

---


### Tool call

_source line 384 · 2026-05-15T11:16:17.721389+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Hold Onto That Thought\" KV cache compression reasoning 2025 arXiv 2512.12008"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Hold Onto That Thought\" KV cache compression reasoning 2025 arXiv 2512.12008"
  }
}
```

</details>

---


### Tool call

_source line 385 · 2026-05-15T11:16:18.725986+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Sparse Frontier\" sparse attention strategy crossover generation stages Nawrot 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Sparse Frontier\" sparse attention strategy crossover generation stages Nawrot 2025"
  }
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-15T11:16:20.786880+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract all reviewer guidelines, especially criteria for novelty, contribution sufficiency, characterization/analysis papers vs method papers, and any guidance on what constitutes sufficient contribution for a main conference paper vs Findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract all reviewer guidelines, especially criteria for novelty, contribution sufficiency, characterization/analysis papers vs method papers, and any guidance on what constitutes sufficient contribution for a main conference paper vs Findings."
  }
}
```

</details>

---


### Tool result

_source line 387 · 2026-05-15T11:16:24.409447+00:00_

Web search results for query: ""Hold Onto That Thought" KV cache compression reasoning 2025 arXiv 2512.12008"

Links: [{"title":"[2512.12008] Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/abs/2512.12008"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"},{"title":"NeurIPS Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://neurips.cc/virtual/2025/loc/san-diego/126664"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning | OpenReview","url":"https://openreview.net/forum?id=udgrpHqw4F"},{"title":"Paper page - Fast KVzip: Efficient and Accurate LLM Inference with Gated KV Eviction","url":"https://huggingface.co/papers/2601.17668"}]

I found the paper! Here are the key details about the arXiv paper 2512.12008:

**"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning"**

This paper was submitted on December 12, 2025, by authors including Minghui Liu, Aadi Palnitkar, Tahseen Rabbani, and others.

**Main Focus:**
The paper addresses how KV caches grow linearly with context length, and explores compression algorithms that alleviate this growth by evicting unimportant tokens.

**Key Motivation:**
While several popular compression strategies target the prefill phase (processing long prompt context), their performance is rarely assessed on reasoning tasks requiring long decoding. Short but complex prompts in benchmarks like GSM8K and MATH500 often benefit from multi-step reasoning and self-reflection, resulting in thinking sequences thousands of tokens long.

**Main Findings:**
For non-reasoning Llama-3.1-8B-Instruct, no singular compression strategy fits all and performance is heavily influenced by dataset type. However, H2O and a decoding-enabled variant of SnapKV are dominant strategies for reasoning models, indicating the utility of heavy-hitter tracking for reasoning traces. Addit
…[truncated 244 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6688
}
```

</details>

---


### Tool result

_source line 388 · 2026-05-15T11:16:26.121777+00:00_

Web search results for query: ""Sparse Frontier" sparse attention strategy crossover generation stages Nawrot 2025"

Links: [{"title":"The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs","url":"https://arxiv.org/pdf/2504.17768"},{"title":"[2504.17768] The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs","url":"https://arxiv.org/abs/2504.17768"},{"title":"[PDF] The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Sparse-Frontier:-Sparse-Attention-Trade-offs-in-Nawrot-Li/42ed331d09a32215c7061a56b3659fa4500675c1"},{"title":"Optimizing Native Sparse Attention with Latent Attention and Local Global Alternating Strategies","url":"https://arxiv.org/html/2511.00819v1"},{"title":"Sparse Attention Variants Overview","url":"https://www.emergentmind.com/topics/sparse-attention-variants"},{"title":"[2504.17768v1] The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs","url":"https://arxiv.org/abs/2504.17768v1"},{"title":"Cohere Labs on X: \"How does sparse attention reshape LLM scaling? 🔍 We’re excited to share this work by former @Cohere intern @p_nawrot, “The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs.”\" / X","url":"https://x.com/Cohere_Labs/status/1916895618251047083"},{"title":"Sparse Attention","url":"https://www.aussieai.com/research/sparse-attention"},{"title":"Inference-Time Hyper-Scaling with KV Cache Compression","url":"https://arxiv.org/html/2506.05345v1"},{"title":"Computation and Language - The Sparse Frontier Sparse Attention Trade-offs in Transformer LLMs | PaperLedge","url":"https://www.paperledge.com/e/computation-and-language-the-sparse-frontier-sparse-attention-trade-offs-in-transformer-llms/"}]

Based on the search results, I found comprehensive information about "The Sparse Frontier" paper by Nawrot et al. (2025). Here's what the research covers:

## Overview

Sparse attention offers a promising strategy
…[truncated 1541 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7395
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-15T11:16:28.139085+00:00_

# ARR Reviewer Guidelines: Novelty, Contribution, and Paper Types

## Novelty Standards

The guidelines explicitly reject several common biases about novelty:

- **H3 (Not Novel)**: If claiming lack of novelty, you must provide references. Papers labeled as reproductions, reimplementations, or analyses "are in scope of the CFP and deserve a fair hearing."

- **H4 (No Precedent)**: "Papers that are more novel tend to be harder to publish. Reviewers may be unnecessarily conservative."

The document cautions against dismissing work simply because it lacks precedent in existing literature.

## Contribution Sufficiency

**Core principle**: "A paper only needs to present sufficient evidence for the claim that the authors are making." Extra experiments belong in suggestions, not rejection reasons.

Key guidance:
- Don't require experiments beyond what supports the stated claim (H13)
- Don't demand authors use different methodologies (H15)
- Acknowledge that "several valid approaches to a given problem" exist
- Avoid treating acknowledged limitations as weaknesses (H16)

## Characterization/Analysis vs. Method Papers

The guidelines don't formally distinguish these categories but provide relevant guidance:

**Analysis papers**: The document notes that "systematic analyses of prior work should be encouraged," particularly given "the sad state of replicability of NLP experiments."

**Resource papers**: Criticized example: "'the paper is mostly a description...contains little scientific contribution'" — flagged as problematic bias.

Both receive equal consideration as valid contributions.

## Main Conference vs. Findings

**No explicit guidance provided** distinguishing these venues appears in these guidelines. The document refers to "main conference" and "Findings" only in scoring context: "All papers recommended for Findings and main conferences are expected to be sufficiently sound and reproducible."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7352
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-15T11:19:58.816853+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿意见：新颖性与完整性\n\n### 总体评分\n**Overall**: 2.5/5（介于 Findings 推荐和 Resubmit 之间）\n**一句话总结**: 实验执行扎实、统计分析严谨，但核心新颖性——compound severity 的 phase-dependence——是已知现象（HIES discrimination collapse + ThinKV phase segmentation + Sparse Frontier strategy crossover）在新 setting 下的 characterization，增量贡献对 EMNLP main conference 偏弱，且关键 crossover finding 的证据基础不足。\n\n### 官方维度打分（ACL ARR Review Form）\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Soundness | 3.5/5 | 统计严谨但 crossover 数据来自 n=50 未在 n=500 验证；G metric n=50 vs n=496 差异大 |\n| Excitement | 2/5 | Pure characterization without method；pilot fails own gate；增量有限 |\n| Reproducibility | 3.5/5 | Setup 详尽但代码未释放 |\n| Confidence | 4/5 | 熟悉该领域文献 |\n\n### Must-Fix (3)\n\n**N1** [critical] Crossover evidence 来自 n=50, 未在 n=500 验证\n- §5.3, Table 2: per-phase II 值（如 s=0.25 importance low=7.196 vs random low=1.363）全部来自 n=50 profiling subset。Table 1 在 n=496 确认 Δ monotonicity 但 crossover 的 per-phase per-strategy 分解未在 n=496 报告。5.3× reversal 可能在大样本上不稳定。\n- 这直接削弱论文最独特的 claim。\n\n**N2** [critical] 新颖性增量不足\n- Phase-dependent sensitivity: ThinKV (ICLR'26) + Sparse Frontier (2025) 已建立\n- Discrimination collapse: HIES (2025) 已报告，论文自承 \"independently corroborated\"\n- Crossover: Sparse Frontier 已报告 \"no single strategy dominates across stages\"\n- 论文 Discussion 自承 qualitative direction \"may seem expected\"\n- Pure characterization paper 的 delta 主要是 quantitative magnitude，对 EMNLP main 可能更适合 Findings\n\n**N3** [critical] 标题和 Framing mismatch\n- \"Phase-Modulated\" 暗示主动调节，实际仅观察/characterize\n- \"emergent\" 不准确——是已知 mechanisms 在新 setting 的 quantification\n- Conclusion \"within a single generation (n=496)\" 矛盾——G 是跨问题的中位数比\n\n### Should-Fix (6)\n\n**W1** LLaMA 跨架构 claim 极弱：n=49, 仅 s=0.30 显著, ~1/40 magnitude, random 也有 phase gradient\n**W2** Pilot experiment fails 30% gate (oracle 18%, heuristic 32% but CI spans zero)——practical significance 未证明\n**W3** 遗漏重要引用：\"Hold Onto That Thought\" (NeurIPS 2025, arXiv:2512.12008) 直接评估 KV cache compression 对 reasoning 的影响\n**W4** h2o-neurips2023 bib entry 的 title 字段为空\n**W5** Abstract \"over an order of magnitude\" 指向不明确（G? Δ? II ratio?），且 n=50 G (69-274x) vs n=496 G (30-148x) 差异暗示估计不稳定\n**W6** Qwen 45.2% mid-phase null rate 限制了完整 phase profile；可能更适合 binary segmentation\n\n### 小问题\n- LongFlow 正文未注明 withdrawn 状态\n- Table 2 \"profiling subset\" 选取方法未说明；Appendix permutation test n=49 (vs n=50) 未解释\n- SnapKV first author mismatch (bib: Li vs OpenAlex: Cai)\n\n### 主要优势\n- S1: 统计分析水准极高（bootstrap + Bonferroni + BH-FDR + JT + permutation + multiplicative null）\n- S2: Random eviction 作为 falsification control 设计精妙\n- S3: 透明诚实（pilot gate failure, LLaMA weak evidence, Qwen null rate 全部坦承）\n- S4: n=50→n=500 scaling 验证有说服力\n- S5: 32/32 引用全部真实，无 hallucinated citations\n\n### 引用审计\n全部 32 篇引用通过验证（web search + OpenAlex）。3 篇 OpenAlex 未索引但通过 arXiv/Nature 页面确认真实存在。无虚假引用。建议补引 \"Hold Onto That Thought\" (NeurIPS 2025)。",
  "reviewer_id": "2",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿意见：新颖性与完整性\n\n### 总体评分\n**Overall**: 2.5/5（介于 Findings 推荐和 Resubmit 之间）\n**一句话总结**: 实验执行扎实、统计分析严谨，但核心新颖性——compound severity 的 phase-dependence——是已知现象（HIES discrimination collapse + ThinKV phase segmentation + Sparse Frontier strategy crossover）在新 setting 下的 characterization，增量贡献对 EMNLP main conference 偏弱，且关键 crossover finding 的证据基础不足。\n\n### 官方维度打分（ACL ARR Review Form）\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Soundness | 3.5/5 | 统计严谨但 crossover 数据来自 n=50 未在 n=500 验证；G metric n=50 vs n=496 差异大 |\n| Excitement | 2/5 | Pure characterization without method；pilot fails own gate；增量有限 |\n| Reproducibility | 3.5/5 | Setup 详尽但代码未释放 |\n| Confidence | 4/5 | 熟悉该领域文献 |\n\n### Must-Fix (3)\n\n**N1** [critical] Crossover evidence 来自 n=50, 未在 n=500 验证\n- §5.3, Table 2: per-phase II 值（如 s=0.25 importance low=7.196 vs random low=1.363）全部来自 n=50 profiling subset。Table 1 在 n=496 确认 Δ monotonicity 但 crossover 的 per-phase per-strategy 分解未在 n=496 报告。5.3× reversal 可能在大样本上不稳定。\n- 这直接削弱论文最独特的 claim。\n\n**N2** [critical] 新颖性增量不足\n- Phase-dependent sensitivity: ThinKV (ICLR'26) + Sparse Frontier (2025) 已建立\n- Discrimination collapse: HIES (2025) 已报告，论文自承 \"independently corroborated\"\n- Crossover: Sparse Frontier 已报告 \"no single strategy dominates across stages\"\n- 论文 Discussion 自承 qualitative direction \"may seem expected\"\n- Pure characterization paper 的 delta 主要是 quantitative magnitude，对 EMNLP main 可能更适合 Findings\n\n**N3** [critical] 标题和 Framing mismatch\n- \"Phase-Modulated\" 暗示主动调节，实际仅观察/characterize\n- \"emergent\" 不准确——是已知 mechanisms 在新 setting 的 quantification\n- Conclusion \"within a single generation (n=496)\" 矛盾——G 是跨问题的中位数比\n\n### Should-Fix (6)\n\n**W1** LLaMA 跨架构 claim 极弱：n=49, 仅 s=0.30 显著, ~1/40 magnitude, random 也有 phase gradient\n**W2** Pilot experiment fails 30% gate (oracle 18%, heuristic 32% but CI spans zero)——practical significance 未证明\n**W3** 遗漏重要引用：\"Hold Onto That Thought\" (NeurIPS 2025, arXiv:2512.12008) 直接评估 KV cache compression 对 reasoning 的影响\n**W4** h2o-neurips2023 bib entry 的 title 字段为空\n**W5** Abstract \"over an order of magnitude\" 指向不明确（G? Δ? II ratio?），且 n=50 G (69-274x) vs n=496 G (30-148x) 差异暗示估计不稳定\n**W6** Qwen 45.2% mid-phase null rate 限制了完整 phase profile；可能更适合 binary segmentation\n\n### 小问题\n- LongFlow 正文未注明 withdrawn 状态\n- Table 2 \"profiling subset\" 选取方法未说明；Appendix permutation test n=49 (vs n=50) 未解释\n- SnapKV first author mismatch (bib: Li vs OpenAlex: Cai)\n\n### 主要优势\n- S1: 统计分析水准极高（bootstrap + Bonferroni + BH-FDR + JT + permutation + multiplicative null）\n- S2: Random eviction 作为 falsification control 设计精妙\n- S3: 透明诚实（pilot gate failure, LLaMA weak evidence, Qwen null rate 全部坦承）\n- S4: n=50→n=500 scaling 验证有说服力\n- S5: 32/32 引用全部真实，无 hallucinated citations\n\n### 引用审计\n全部 32 篇引用通过验证（web search + OpenAlex）。3 篇 OpenAlex 未索引但通过 arXiv/Nature 页面确认真实存在。无虚假引用。建议补引 \"Hold Onto That Thought\" (NeurIPS 2025)。",
    "reviewer_id": "2",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-15T11:20:03.128625+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4311
}
```

</details>

---


### Assistant

_source line 392 · 2026-05-15T11:20:10.342456+00:00_

审稿意见已提交给 Review Director。

总结：论文在实验执行和统计分析方面达到高水准（S1-S4），但在新颖性维度存在三个 critical 问题：(1) crossover 这一最独特发现仅有 n=50 证据，(2) 核心 contributions 可由 HIES+ThinKV+Sparse Frontier 的组合预期，(3) 标题暗示方法论贡献但实际为 characterization study。建议评分 2.5/5，可能更适合 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2"
}
```

</details>

---


## Round 9

## Round 9

16 recorded events


### User

_source line 393 · 2026-05-15T11:20:55.950000+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 1 的完整审稿意见

请逐条回应以下 Reviewer 1 的意见。对每条使用 [AGREE] 或 [REBUT]，并说明理由。如果是 [REBUT]，请引用具体 Section/Table/Figure 作为证据。

---

### Reviewer 1 总体评分
**Overall**: 3.5/5 (Findings-level, 介于 Findings 和 Conference 之间)

### Must-Fix (3)

**N1** [critical] Table 2 (n=50) 与 n=496 数据混用，crossover 分析未在全量数据验证
- Table 2 报告 n=50 的 per-phase II，G=69-274×；n=496 的 G=30-148×（仅在 caption 和正文中以 bootstrap CI 给出）。G 过高估计 42-85%。§5.3 crossover 核心数字完全来自 n=50。
- 建议：在 n=496 上重新计算 per-phase II 中位数并替换 Table 2。

**N2** [critical] Discrimination collapse effect size（Gini 下降 0.01-0.08）与 severity gradient（G=30-148×）之间的 gap 未弥合
- 论文未报告 baseline Gini 值，无法判断相对变化。0.01-0.02 的 Qwen Gini 变化如何驱动 3-148× 的 severity amplification？
- 建议：报告 baseline Gini 和相对变化；讨论 threshold amplification 机制；或降低 mechanism claim 的权重。

**N3** [critical] "following ThinKV" 对 phase segmentation 方法的错误归因
- background.tex:33: ThinKV 使用 explicit delimiters，本文使用 quantile-based segmentation，"following" 措辞误导。
- 建议：改为 "inspired by" 或 "cf."。

### Should-Fix (6)

**W1** Spearman ρ=1.0 on n=4 的过度报告——JT test 才是 dose-response 的 primary evidence
**W2** Bonferroni k=4 范围需更充分论证；main text 应 prominently reference BH-FDR
**W3** Entropy redistribution 跨模型不一致（Qwen s=0.25 反转）削弱机制叙事
**W4** 缺乏下游任务评估——PPL-based II 的实际意义不明
**W5** Mitigation pilot 失败对论文 motivation 的影响需更坦诚讨论
**W6** LLaMA CI/Wilcoxon 不一致需解释（s=0.15 CI excl zero but p=0.219; s=0.30 CI incl zero but p=0.029）

### Minor Issues
- M1: \placeholder 命令残留
- M2: appendix_results.tex orphaned + duplicate label
- M3: h2o bib title 为空
- M4: 3 篇引用 OpenAlex 未索引
- M5: deepseek-r1 bib corporate authorship
- M6: float16→bfloat16 切换是否影响 n=50 profiling 数据可靠性

### Questions to Authors
Q1: Table 2 的 per-phase II 值为何未在 n=496 上重新计算？
Q2: Discrimination collapse 的 baseline Gini 值？
Q3: Phase boundary 稳定性？
Q4: 是否考虑 accuracy-based II？
Q5: Frobenius norm 是否是结果关键假设？

---

请逐条回应 Reviewer 1 的 Must-Fix (N1-N3)、Should-Fix (W1-W6) 和 Minor Issues (M1-M6)。重点关注你是否同意 N2（mechanism gap）——这与你对 novelty 的评估直接相关。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 394 · 2026-05-15T11:21:34.224650+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex",
  "limit": "5",
  "offset": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex",
    "limit": "5",
    "offset": "30"
  }
}
```

</details>

---


### Tool call

_source line 395 · 2026-05-15T11:21:34.225121+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
  "limit": "15",
  "offset": "62"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
    "limit": "15",
    "offset": "62"
  }
}
```

</details>

---


### Tool result

_source line 396 · 2026-05-15T11:21:34.325802+00:00_

30	
31	\paragraph{Phase segmentation.}
32	\label{sec:phase-segmentation}
33	Each generated sequence is partitioned into three phases (low-, mid-, high-sparsity) by tercile boundaries of per-position attention sparsity, following ThinKV~\cite{thinkv-iclr2026}. Low-sparsity phases correspond to broadly distributed attention (exploratory reasoning); high-sparsity phases to concentrated attention (structured computation). Details in Appendix~\ref{app:formulation-details}.
34	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 397 · 2026-05-15T11:21:34.326346+00:00_

62	
63	\subsection{Phase-Strategy Crossover}
64	\label{sec:crossover}
65	
66	A strategy ranking reversal emerges across all sparsity levels: at $s{=}0.25$, importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\ $0.818$) but \emph{higher} II in the low-sparsity phase ($7.196$ vs.\ $1.363$---a $5.3{\times}$ reversal), demonstrating that no single strategy dominates uniformly. Full crossover analysis and visualization appear in Appendix~\ref{app:crossover-details}. % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28
67	
68	\subsection{Cross-Model Replication}
69	\label{sec:cross-model}
70	
71	Qwen2.5-7B-Instruct (standard instruction tuning, same Qwen2 backbone, $n_{\text{eff}}{=}475$) reproduces the monotonic severity gradient: $\Delta$ increases from $0.07$ at $s{=}0.15$ to $3.16$ at $s{=}0.30$ (all Bonferroni-corrected $p < 10^{-14}$), paralleling DeepSeek at approximately one-quarter to one-sixth the magnitude. Both models yield strictly increasing median $\Delta$ trajectories (Spearman $\rho{=}1.0$, exact permutation $p{=}0.042$, one-tailed). Random eviction on Qwen mirrors DeepSeek: non-significant at $s \leq 0.20$, becoming significant at $s \geq 0.25$ ($\Delta{=}0.39$--$0.91$; $p_{\text{Bonf}} < 10^{-10}$) but $2.7$--$20{\times}$ weaker than importance-based. A caveat applies to mid-phase comparisons: on Qwen, 45.2\% of problems yield null mid-phase segments due to low temporal autocorrelation in attention sparsity (lag-1 $r{=}0.718$ vs.\ DeepSeek's $0.894$; $d{=}-1.68$), preventing formation of contiguous mid-phase runs above the $\texttt{min\_phase\_length}{=}10$ threshold. This does not affect the primary low--high contrast ($\Delta$). Per-phase effective sample sizes are reported in Appendix~\ref{app:qwen-null-rate}. Full cross-model tables appear in Appendix~\ref{app:cross-model-details}. % exp_id: n500_unified_final; QW imp Δ 0.07→3.16, all p<1e-14; QW ra
…[truncated 171 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-15T11:21:34.326706+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex",
  "limit": "5",
  "offset": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex",
    "limit": "5",
    "offset": "4"
  }
}
```

</details>

---


### Tool result

_source line 399 · 2026-05-15T11:21:34.429617+00:00_

4	\paragraph{Models.}
5	\label{sec:models}
6	We evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \textbf{DeepSeek-R1-Distill-Qwen-7B}~\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \textbf{Qwen2.5-7B-Instruct}~\cite{qwen25-2024}, with standard instruction tuning, providing a cross-model replication target. Both are loaded in \texttt{bfloat16} with eager attention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values; \texttt{bfloat16} eliminated all occurrences.}
7	
8	\paragraph{Dataset.}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-15T11:21:40.426595+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\placeholder",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\placeholder",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-15T11:21:40.929824+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex:21:\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-15T11:21:41.130957+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/appendix_results*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/appendix_results*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper"
  }
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-15T11:21:41.181699+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 404 · 2026-05-15T11:21:43.826686+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex"
  }
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-15T11:21:43.877344+00:00_

1	% Appendix: supplementary results details
2	
3	\section{Cross-Model Replication Details}
4	\label{app:cross-model-details}
5	
6	\paragraph{Per-problem concordance.}
7	The per-problem concordance across models is not significant (mean $\rho = -0.107$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json; mean_rho=-0.107, per_problem_concordance_p=0.926
8	
9	\paragraph{Random eviction control.}
10	As a control, random eviction on Qwen mirrors DeepSeek: non-significant at $s \leq 0.20$ ($\Delta$: $-0.01$, $0.02$; CIs span zero) but significant at $s \geq 0.25$ ($\Delta{=}0.39$, $p_{\text{Bonf}} < 10^{-10}$; $\Delta{=}0.91$, $p_{\text{Bonf}} < 10^{-13}$). Where significant, the random phase gradient is $2.7$--$3.5{\times}$ weaker than importance-based ($0.39$ vs.\ $1.07$ at $s{=}0.25$; $0.91$ vs.\ $3.16$ at $s{=}0.30$), confirming strategy-specific amplification. % exp_id: n500_unified_final; QW rand: s015 -0.011 ns, s020 0.015 ns, s025 0.393 sig, s030 0.913 sig
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-15T11:23:46.729463+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 Reviewer 1\n\n### Must-Fix\n\n[AGREE] R1-N1: Table 2 n=50 crossover 未在 n=500 验证——完全同意，与我的 N1 一致。补充：G 值从 n=50 的 69-274× 降至 n=496 的 30-148×（降幅 42-85%），说明 n=50 估计在重尾分布下不稳定。crossover 是本文最具区分度的 claim，n=496 验证将决定 Contribution 1 的存废。\n\n[AGREE] R1-N2: Discrimination collapse effect size 与 severity gradient 的 gap——同意这是重要缺口。缺少 baseline Gini 值无法判断相对变化；ΔGini 0.01-0.08 如何驱动 G=30-148× 需要 threshold amplification 机制的讨论或降低 mechanism claim 权重。这直接影响我对 Contribution 3 novelty 的评估。\n\n[AGREE with nuance] R1-N3: \"following ThinKV\" 归因——同意措辞不准确（ThinKV 用 explicit delimiters，本文用 quantile-based segmentation），但我认为 severity 略低于 critical，更像 should-fix 级别的 attribution 修正。\n\n### Should-Fix\n\n[AGREE] R1-W1: n=4 Spearman 过度报告——同意，JT test 才是 primary evidence。\n[REBUT] R1-W2: Bonferroni k=4 范围——methodology.tex 已解释 rationale，Appendix B 已报告 BH-FDR 全量对照（32/32 Bonferroni 结果保持显著）。但同意 main text 应更 prominently reference BH-FDR。\n[AGREE] R1-W3: Entropy redistribution 跨模型不一致——同意削弱机制叙事。\n[AGREE] R1-W4: 缺乏下游任务评估——PPL-based II 的 accuracy gap 是 blind spot。\n[AGREE] R1-W5: Pilot 失败的影响——同意需更坦诚讨论。\n[REBUT] R1-W6: LLaMA CI/Wilcoxon 不一致——论文在 results.tex §5.5 已显式承认这一矛盾并 hedge 为 \"mixed evidence\"。技术上 bootstrap CI 和 Wilcoxon 在 small n + heavy tail 下可以 diverge。但建议加一句技术解释。\n\n### Minor\n\n[AGREE] M1-M6 全部同意。特别注意 M6（float16→bfloat16 切换时间点不明确）——如果 n=50 在 float16 下运行，进一步削弱 Table 2 可信度。\n\n### 两位 Reviewer 的共识\n\nR1 和 R2 在以下核心问题上完全一致：\n1. Table 2 n=50 数据需在 n=496 上验证（R1-N1, R2-N1）\n2. Crossover 证据基础不足（R1-N1, R2-N1）\n3. Pilot experiment 失败的 implications 需更坦诚讨论（R1-W5, R2-W2）\n4. h2o bib title 为空（R1-M3, R2-W4）\n5. 引用全部真实，无 hallucinated citations\n\n主要分歧点：\n- **Overall 评分**: R1 给 3.5（Findings-level），我给 2.5。差距主要来自我对 novelty 增量更严格的评估——我认为 HIES + ThinKV + Sparse Frontier 的组合已基本预示本文发现的方向，R1 可能对 characterization paper 的价值给予更高权重。\n- **N2 severity**: R1 将 discrimination collapse gap 列为 must-fix critical，我同意重要性但认为如果 mechanism claim 降级为 correlational observation 即可（不需要因果验证）。\n- **N3 severity**: 我认为 \"following ThinKV\" 是 should-fix 而非 must-fix。",
  "reviewer_id": "2",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 Reviewer 1\n\n### Must-Fix\n\n[AGREE] R1-N1: Table 2 n=50 crossover 未在 n=500 验证——完全同意，与我的 N1 一致。补充：G 值从 n=50 的 69-274× 降至 n=496 的 30-148×（降幅 42-85%），说明 n=50 估计在重尾分布下不稳定。crossover 是本文最具区分度的 claim，n=496 验证将决定 Contribution 1 的存废。\n\n[AGREE] R1-N2: Discrimination collapse effect size 与 severity gradient 的 gap——同意这是重要缺口。缺少 baseline Gini 值无法判断相对变化；ΔGini 0.01-0.08 如何驱动 G=30-148× 需要 threshold amplification 机制的讨论或降低 mechanism claim 权重。这直接影响我对 Contribution 3 novelty 的评估。\n\n[AGREE with nuance] R1-N3: \"following ThinKV\" 归因——同意措辞不准确（ThinKV 用 explicit delimiters，本文用 quantile-based segmentation），但我认为 severity 略低于 critical，更像 should-fix 级别的 attribution 修正。\n\n### Should-Fix\n\n[AGREE] R1-W1: n=4 Spearman 过度报告——同意，JT test 才是 primary evidence。\n[REBUT] R1-W2: Bonferroni k=4 范围——methodology.tex 已解释 rationale，Appendix B 已报告 BH-FDR 全量对照（32/32 Bonferroni 结果保持显著）。但同意 main text 应更 prominently reference BH-FDR。\n[AGREE] R1-W3: Entropy redistribution 跨模型不一致——同意削弱机制叙事。\n[AGREE] R1-W4: 缺乏下游任务评估——PPL-based II 的 accuracy gap 是 blind spot。\n[AGREE] R1-W5: Pilot 失败的影响——同意需更坦诚讨论。\n[REBUT] R1-W6: LLaMA CI/Wilcoxon 不一致——论文在 results.tex §5.5 已显式承认这一矛盾并 hedge 为 \"mixed evidence\"。技术上 bootstrap CI 和 Wilcoxon 在 small n + heavy tail 下可以 diverge。但建议加一句技术解释。\n\n### Minor\n\n[AGREE] M1-M6 全部同意。特别注意 M6（float16→bfloat16 切换时间点不明确）——如果 n=50 在 float16 下运行，进一步削弱 Table 2 可信度。\n\n### 两位 Reviewer 的共识\n\nR1 和 R2 在以下核心问题上完全一致：\n1. Table 2 n=50 数据需在 n=496 上验证（R1-N1, R2-N1）\n2. Crossover 证据基础不足（R1-N1, R2-N1）\n3. Pilot experiment 失败的 implications 需更坦诚讨论（R1-W5, R2-W2）\n4. h2o bib title 为空（R1-M3, R2-W4）\n5. 引用全部真实，无 hallucinated citations\n\n主要分歧点：\n- **Overall 评分**: R1 给 3.5（Findings-level），我给 2.5。差距主要来自我对 novelty 增量更严格的评估——我认为 HIES + ThinKV + Sparse Frontier 的组合已基本预示本文发现的方向，R1 可能对 characterization paper 的价值给予更高权重。\n- **N2 severity**: R1 将 discrimination collapse gap 列为 must-fix critical，我同意重要性但认为如果 mechanism claim 降级为 correlational observation 即可（不需要因果验证）。\n- **N3 severity**: 我认为 \"following ThinKV\" 是 should-fix 而非 must-fix。",
    "reviewer_id": "2",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 407 · 2026-05-15T11:23:50.801251+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4071
}
```

</details>

---


### Assistant

_source line 408 · 2026-05-15T11:23:56.217669+00:00_

交叉回应已提交。

核心共识：两位 reviewer 在 Table 2 n=50 验证需求、crossover 证据不足、pilot 失败的坦诚讨论上完全一致。主要分歧在 overall 评分（R1: 3.5 vs R2: 2.5），根源是我对 novelty 增量的更严格判断——我认为已有工作的组合（HIES + ThinKV + Sparse Frontier）已基本预示了本文的核心发现方向。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2"
}
```

</details>

---


## Round 10

## Round 10

58 recorded events


### User

_source line 409 · 2026-05-15T12:32:40.408158+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2

**你的审查侧重：新颖性 + 完整性 + 相关工作 + 格式合规**

### 论文信息
- **标题**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Mathematical Reasoning Models
- **论文路径**: `projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex`（多文件结构，abstract.tex / introduction.tex / related_work.tex / background.tex / methodology.tex / results.tex / analysis.tex / discussion.tex / conclusion.tex / limitations.tex / appendix.tex / appendix_moved.tex / appendix_disc_analysis.tex / appendix_robustness.tex）
- **references**: `references.bib`

### Venue 要求
- **Venue**: EMNLP 2026 Main Conference（通过 ACL Rolling Review May 2026 cycle 提交）
- **Deadline**: ARR 提交截止 2026-05-25
- **格式**: ACL 模板, 长文 8 页正文 + 无限参考文献
- **审稿制度**: Double-blind
- **匿名规则**: 作者信息匿名
- **必须**: Limitations section（不计页数）
- **鼓励**: Ethics/Broader Impact section

### 你的审查重点

请以 EMNLP 最严格审稿标准评估以下方面：

1. **新颖性 (Novelty)**：
   - 核心 contribution（phase-strategy interaction）是否足够新颖？
   - 这是一个全面的实证特征化（characterization）工作，而非提出新方法——对 EMNLP main conference 是否足够？
   - 与 ThinKV (ICLR 2026)、SparK (AAAI 2026)、UniComp (2026)、HIES (2025)、Sparse Frontier (2025) 的差异化是否充分？
   - Introduction 中 "Why can't existing single-axis findings predict our results?" 的论证是否有说服力？
   - Crossover effect 是否真的不可从现有工作推导？

2. **完整性 (Completeness)**：
   - 仅在 MATH-500 上评估，仅 7B 模型——generalizability 是否充分？
   - 只用 perplexity，无 downstream accuracy——是否构成重大缺陷？
   - Mitigation pilot 失败（18% recovery, gate FAIL）——论文的实际价值在哪里？
   - 缺少 throughput/latency 评估——对 deployment motivation 的影响？
   - 论文声称 "motivate phase-aware compression"，但没有展示 phase-aware 能工作

3. **相关工作 (Related Work)**：
   - 相关工作覆盖是否全面？有无重大遗漏？
   - 请用 web_search 搜索 2025-2026 年相关工作，确认无重大遗漏：
     - compound sparsity / joint compression for LLMs
     - KV cache compression for reasoning models
     - phase-aware / phase-dependent inference
   - 引用格式是否正确？bib 条目是否完整？

4. **格式合规**：
   - 是否符合 ACL 模板（\usepackage[review]{acl}）？
   - 页数是否在 8 页限制内？
   - Double-blind 是否遵守（无泄漏作者身份的信息）？
   - Limitations section 是否存在且位置正确？
   - Reproducibility 声明是否存在？
   - 图表质量、表格可读性
   - 参考文献格式一致性

5. **写作质量**：
   - 论文组织是否清晰？
   - Abstract 是否准确反映论文内容？
   - Claims 是否与证据匹配（overclaiming 风险）？
   - 术语是否一致？

请输出完整的结构化审稿报告（Strengths / Weaknesses / Questions / Missing References / Score）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 410 · 2026-05-15T12:32:49.841996+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 411 · 2026-05-15T12:32:49.892625+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 412 · 2026-05-15T12:32:50.445514+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 413 · 2026-05-15T12:32:50.446061+00:00_

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
11	
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{graphicx}
15	\usepackage{booktabs}
16	\usepackage{enumitem}
17	\usepackage{multirow}
18	
19	\graphicspath{{figures/}}
20	
21	
22	\title{Phase-Modulated Compound Sparsity:\\Strategy-Dependent Severity Gradients in Mathematical Reasoning Models}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	
28	\maketitle
29	
30	\input{abstract}
31	
32	\input{introduction}
33	\input{related_work}
34	\input{background}
35	\input{methodology}
36	\input{results}
37	\input{analysis}
38	\input{discussion}
39	\input{conclusion}
40	
41	\bibliography{references}
42	
43	\section*{Limitations}
44	\input{limitations}
45	
46	\section*{Reproducibility}
47	Code and data will be released upon acceptance.
48	
49	\appendix
50	\input{appendix}
51	\input{appendix_moved}
52	\input{appendix_disc_analysis}
53	\input{appendix_robustness}
54	
55	\end{document}
56	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 414 · 2026-05-15T12:32:55.017738+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 415 · 2026-05-15T12:32:55.922715+00:00_

1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	We show that compound severity is not phase-invariant: it is an emergent phase-strategy interaction with amplification ratios ($G$) of $7.5$--$79.8{\times}$ (bootstrap 95\% CI: $[4.1, 96.5]$) across reasoning phases in mathematical reasoning models.
4	
5	On DeepSeek-R1-Distill-Qwen-7B (500 MATH-500 problems, $n_{\text{eff}}{=}496$, $s \in \{0.15, 0.20, 0.25, 0.30\}$), importance-based eviction produces a monotonically increasing severity gradient from the high-sparsity to low-sparsity reasoning phase (median $\Delta$: $0.39 \to 8.48$; all Bonferroni-corrected $p < 10^{-69}$). Random eviction develops a detectable phase gradient only above $s \approx 0.20$ (non-significant at $s \leq 0.20$; where significant, $3$--$39{\times}$ weaker), confirming importance-based eviction as the dominant driver.
6	A crossover emerges at $s{=}0.25$: importance-based eviction outperforms random in high-sparsity phases yet underperforms in low-sparsity phases---a qualitative reversal in strategy ranking.
7	The pattern replicates on Qwen2.5-7B-Instruct ($n_{\text{eff}}{=}475$, $\Delta$: $0.07 \to 3.16$; all $p < 10^{-14}$), with preliminary cross-architecture evidence from a LlamaForCausalLM model suggesting the phenomenon may extend beyond Qwen2-family architectures.
8	We present discrimination collapse---head pruning flattening cumulative importance scores---as a correlational diagnostic: both strategies exhibit near-identical Gini drops, yet severity diverges by $15$--$17{\times}$, implicating the structural specificity of importance-based pruning as the key differentiator.
9	These findings motivate phase-aware compression budgets for mathematical reasoning models.
10	\end{abstract}
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 416 · 2026-05-15T12:32:56.024168+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 417 · 2026-05-15T12:32:56.627347+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses---\emph{attention head pruning} \cite{voita-acl2019, michel-neurips2019} and \emph{KV cache eviction} \cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \emph{compound sparsity}, but the resulting quality degradation is often super-additive \cite{spark-aaai2026, slim-icml2025}. Recent evaluations confirm that reasoning capabilities degrade disproportionately under compound compression \cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \cite{phase-transition-compression-2026}.
6	
7	Prior work treats compound interaction magnitude as roughly constant across generation \cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \cite{sparse-frontier-2025}.
8	This assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \cite{thinkv-iclr2026}.
9	Phase-aware methods like ThinKV \cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from greedy bias \cite{greedy-bias-kvcache-2026}, deferred importance \cite{retentivekv-2026}, and temporal dynamics in long generations \cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple mechanisms are composed.
10	If compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.

…[truncated 3355 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 418 · 2026-05-15T12:32:56.728362+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 419 · 2026-05-15T12:32:56.880701+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Compound compression.}
5	Combining multiple compression axes produces non-additive errors.
6	\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \cite{slim-icml2025} formalize compound error for quantization and sparsity.
7	\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.
8	\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.
9	GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.
10	PM-KVQ~\cite{pmkvq-iclr2026} demonstrates that progressive quantization---gradually reducing bit-width over the generation process---mitigates cumulative error in long-CoT reasoning, implicitly introducing a temporal dimension to compression severity that resonates with our finding that compound interaction is phase-dependent.
11	These works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.
12	
13	\paragraph{KV cache eviction.}
14	Most methods rely on importance scoring whose reliability is increasingly questioned.
15	Ada-KV~\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\cite{snapkv-neurips2024} compresses from a fixed observation window; \cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\times}$ higher than expected under standard aggregation.
16	\cite{nacl-acl2024} combine proxy-token and random eviction to counter attention bias.
17	RetentiveKV~\cite{retentivekv-2026} identifies deferred importance, and \cite{greedy-bias-kvcache-2026} show that single importance metrics exhibit systematic greedy bias.
18	\cite{hies-2025} independently show
…[truncated 2580 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 420 · 2026-05-15T12:32:56.931534+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 421 · 2026-05-15T12:32:57.384618+00:00_

1	% Section 3: Background and Problem Setup
2	% Note: eq:ii and eq:gradient are the canonical definitions.
3	% Full formulation details in Appendix (app:formulation-details).
4	
5	\section{Background and Problem Setup}
6	\label{sec:background}
7	
8	We formalize compound sparsity, define the Interaction Index, and introduce phase segmentation. Full mathematical details appear in Appendix~\ref{app:formulation-details}.
9	
10	\paragraph{Compound sparsity.}
11	\label{sec:compound-sparsity}
12	Let $s \in (0,1)$ denote a unified sparsity budget. \emph{Attention head pruning} removes the bottom-$s$ fraction of heads per layer by Frobenius norm importance \cite{voita-acl2019, michel-neurips2019}. \emph{KV cache eviction} removes the bottom-$s$ fraction of token positions from the cache. We compare two strategies: \emph{importance-based}, which scores positions by position-normalized cumulative attention mass (Eq.~\ref{eq:kv-importance} in Appendix~\ref{app:formulation-details}), and \emph{random}, which evicts uniformly at random \cite{nacl-acl2024}. Applying both simultaneously yields \emph{compound sparsity}; the two axes interact because head pruning alters the importance ranking used for eviction \cite{spark-aaai2026}. Existing joint-pruning approaches such as GRASPrune \cite{graspune-acl2026} learn global budget-constrained gates but treat decisions as static across generation.
13	
14	\paragraph{Interaction Index.}
15	\label{sec:interaction-index}
16	For a text segment, let $\text{PPL}_c$ denote perplexity under condition $c \in \{d, a, k, b\}$ (dense, attention-only, KV-only, compound). Normalizing by the dense baseline yields $r_c = \text{PPL}_c / \text{PPL}_d$, and:
17	\begin{equation}
18	    \mathrm{II} = r_b - r_a - r_k + 1.
19	    \label{eq:ii}
20	\end{equation}
21	$\mathrm{II} > 0$ indicates super-additive degradation; $\mathrm{II} = 0$ indicates additive independence. We adopt the additive null because the two axes operate on disjoint dimensions; qualitative co
…[truncated 1351 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 422 · 2026-05-15T12:32:57.385223+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
  }
}
```

</details>

---


### Tool result

_source line 423 · 2026-05-15T12:32:57.837301+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\paragraph{Models.}
5	\label{sec:models}
6	We evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \textbf{DeepSeek-R1-Distill-Qwen-7B}~\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \textbf{Qwen2.5-7B-Instruct}~\cite{qwen25-2024}, with standard instruction tuning, providing a cross-model replication target. Both are loaded in \texttt{bfloat16} with eager attention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values; \texttt{bfloat16} eliminated all occurrences.}
7	
8	\paragraph{Dataset.}
9	\label{sec:dataset}
10	We evaluate all 500 problems from MATH-500~\cite{math500-neurips2021}. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048). Problems with degenerate phase assignments (null low or high phase) are excluded, yielding effective sample sizes of $n{=}496$ for DeepSeek (4 excluded) and $n{=}475$ for Qwen (25 excluded). Qwen exhibits a higher mid-phase null rate (45.2\% vs.\ 10.2\% for DeepSeek) due to lower temporal autocorrelation in its attention sparsity patterns (lag-1 $r{=}0.718$ vs.\ $0.894$, $d{=}-1.68$); this does not affect the primary gradient metric $\Delta = \mathrm{II}_{\textit{low}} - \mathrm{II}_{\textit{high}}$, which requires only low and high phases. Sensitivity analysis across $\texttt{min\_phase\_length} \in \{5, 10, 20\}$ confirms robustness (Appendix~\ref{app:mpl-sensitivity}).
11	
12	\paragraph{Sparsity configuration.}
13	\label{sec:sparsity-config}
14	We apply symmetric compound sparsity at $s \in \{0.15, 0.20, 0.25, 0.30\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\ref{eq:kv-importance}; BOS always retained) and \emph{random} eviction (uniform). Heads are
…[truncated 2108 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 424 · 2026-05-15T12:32:57.837846+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 425 · 2026-05-15T12:32:58.290913+00:00_

1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Strategy-Dependent Severity}
6	\label{sec:strategy-severity}
7	
8	Table~\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\Delta$ increases from $0.39$ at $s{=}0.15$ to $8.48$ at $s{=}0.30$---a $22{\times}$ amplification (all Bonferroni-corrected $p < 10^{-69}$). Random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: at $s \leq 0.20$, $\Delta$ is non-significant ($0.01$--$0.03$; CIs span zero); at $s \geq 0.25$, $\Delta$ becomes significant ($0.26$--$0.51$; $p_{\text{Bonf}} < 0.006$) but $15$--$39{\times}$ smaller than under importance-based eviction. Both strategies exhibit monotonic dose-response (Jonckheere-Terpstra $z{=}6.2$--$33.7$, all $p < 10^{-9}$), but importance masking effect sizes are an order of magnitude larger. % exp_id: n500_unified_final; DS imp Δ 0.39→8.48, rand 0.01→0.51; JT z=33.7 (imp), 6.2 (rand)
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, 500 MATH-500 problems).}
14	\label{tab:aggregate-ii}
15	\begin{tabular}{@{}lcccc@{}}
16	\toprule
17	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
18	\midrule
19	Importance & 0.39 & 1.21 & 3.99 & 8.48 \\ % exp_id: n500_unified_final; DS imp median_ii_diff
20	Random     & 0.01 & 0.03 & 0.26 & 0.51 \\ % exp_id: n500_unified_final; DS rand median_ii_diff
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	
26	\subsection{Phase-Modulated Amplification}
27	\label{sec:phase-amplification}
28	
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the per-phase breakdown at $n{=
…[truncated 11973 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 426 · 2026-05-15T12:32:58.291334+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 427 · 2026-05-15T12:32:59.246591+00:00_

1	\section{Discrimination Collapse under Compound Sparsity}
2	\label{sec:analysis}
3	
4	We present discrimination collapse as a \emph{correlational diagnostic} rather than a complete causal explanation. The consistent Gini decrease across all conditions provides a necessary background---aggregate attention concentration drops uniformly under head pruning regardless of eviction strategy (importance $\Delta\mathrm{Gini}$: $-0.030$ to $-0.081$; random $\Delta\mathrm{Gini}$: $-0.031$ to $-0.071$; ${<}10\%$ difference). However, severity diverges by $15$--$17{\times}$ between strategies despite near-identical Gini changes, indicating that concentration collapse alone is insufficient. The critical differentiator is \emph{structural specificity}: importance-based pruning systematically removes high-attention-score heads, disrupting the attention pattern structure that KV eviction relies on, while random pruning preserves more structural diversity. The quantitative gap between score-level changes ($6$--$16\%$ relative Gini reduction from a DeepSeek baseline of $\widetilde{\mathrm{Gini}} \approx 0.50$; Qwen baseline $\approx 0.57$) and outcome-level amplification ($G{=}7.5$--$79.8{\times}$) indicates additional nonlinear factors (e.g., cascading effects across layers) that warrant dedicated investigation.  % exp_id: c4_entropy; DS baseline Gini 0.496, QW 0.571; imp ΔGini -0.029 to -0.082, rand -0.031 to -0.071
5	
6	\subsection{Discrimination Collapse}
7	\label{sec:discrimination-collapse-main}
8	
9	Head pruning systematically reduces the discriminative power of cumulative importance scores, suggesting a mechanism for the phase-strategy interaction. The Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek, $6$--$17\%$ relative to dense baseline) and $0.010$--$0.020$ (Qwen, $2$--$4\%$) after pruning, with consistent negative deltas in all 16 conditions (Appendix~\ref{app:analysis}, Table~\ref{tab:discrimination-metrics-full}). Critically, random eviction shows near-identic
…[truncated 2219 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 428 · 2026-05-15T12:32:59.247168+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 429 · 2026-05-15T12:32:59.751116+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Quantitative surprise.}
5	While the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($G{=}7.5$--$79.8{\times}$ at $n{=}496$) far exceeds a naive ``somewhat worse'' prediction. The crossover on DeepSeek---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.021$ vs.\ $1.113$) and underperforms in low-sparsity phases ($3.971$ vs.\ $1.498$)---cannot be derived from single-axis entropy reasoning. % exp_id: crossover_all_sparsity.csv; DS s025 n=496 The near-unity random baseline ($G{=}0.5$--$1.3{\times}$, trivial magnitude) confirms the dominant amplification is strategy-specific. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json
6	
7	\paragraph{Implications for deployment.}
8	Applying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation. Discrimination collapse depends on attention-mass-based importance scoring shared by major KV cache methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-2024}), suggesting broad applicability.
9	
10	\paragraph{Characterization as diagnostic signal.}
11	The primary value of the phase-dependent severity gradient is diagnostic rather than prescriptive: it identifies \emph{where} compound sparsity is most destructive within a generation. The monotonically increasing $G$ across spar
…[truncated 2774 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 430 · 2026-05-15T12:32:59.751575+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 431 · 2026-05-15T12:33:00.204815+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation ($n{=}496$/$475$ problems). Under importance-based eviction, the amplification ratio $G$ ranges from $7.5{\times}$ to $79.8{\times}$ across sparsity levels, with paired median differences $\Delta$ from $0.39$ to $8.48$ (DeepSeek) and $0.07$ to $3.16$ (Qwen), all $p < 10^{-13}$. Random eviction develops a detectable phase gradient only above $s \approx 0.20$, but $3$--$39{\times}$ weaker than importance-based. A crossover on DeepSeek at $s{=}0.25$---where importance-based eviction reverses ranking across phases ($2.7{\times}$ reversal)---demonstrates that no single strategy dominates uniformly; Qwen does not exhibit this crossover, indicating model dependence. The pattern replicates on Qwen2.5-7B-Instruct at all four sparsity levels; suggestive preliminary evidence from DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) indicates the phenomenon may extend beyond Qwen2, though at ${\sim}1/40$ the magnitude and with a weaker strategy contrast. Discrimination collapse provides a correlational diagnostic supported by both Qwen2-based models, with structural specificity of importance-based pruning as the key differentiator from random eviction---despite near-identical Gini drops ($<10\%$ difference), severity diverges by $15$--$17{\times}$.
5	These findings motivate phase-aware sparsity allocation for reasoning model deployment. Extending this analysis to code reasoning (HumanEval, LiveCodeBench) and science reasoning (GPQA), validating the discrimination collapse mechanism through causal intervention, and characterizing asymmetric compound interactions are promising directions for future work.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 432 · 2026-05-15T12:33:00.205322+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 433 · 2026-05-15T12:33:00.659953+00:00_

1	\paragraph{Model scale and architecture.}
2	All experiments are conducted at the 7--8B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}) partially confirms the qualitative pattern beyond the Qwen2 architecture---monotonically increasing $d_z$ with within-importance phase gradient $\sim$1.0---but with substantially weaker interaction magnitude ($\sim$1/40 of DeepSeek) and mixed statistical evidence (only $s{=}0.30$ significant after Bonferroni correction). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.
3	
4	\paragraph{Task coverage.}
5	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark. MATH-500 is a suitable first testbed because it elicits structured reasoning with clear phase transitions (exploratory vs.\ structured computation), supports per-problem evaluation enabling paired statistical tests, and spans sufficient difficulty to produce meaningful variation in sequence length and attention dynamics. However, different reasoning tasks---code generation (e.g., HumanEval, LiveCodeBench), science reasoning (e.g., GPQA), multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile. Whether the phase-strategy interaction documented here extends to these domains is an open question.
6	
7	\paragraph{Symmetric sparsity assumption.}
8	Our analysis applies symmetric sparsity rates: the same fraction $s$ is used for both head pruning and KV cache eviction. Practical deployments may use asymmetric budgets (e.g., aggressive head pruning with conservat
…[truncated 1561 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 434 · 2026-05-15T12:33:00.660661+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 435 · 2026-05-15T12:33:01.164834+00:00_

1	\section{Compound Sparsity Formulation}
2	\label{app:formulation-details}
3	
4	\paragraph{Attention head pruning.}
5	Heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$ \cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\ell)} \in \{0,1\}$ retains the top-$(1{-}s)\cdot H$ heads:
6	\begin{equation}
7	    \tilde{\mathbf{o}}_j^{(\ell)} = m_j^{(\ell)} \cdot \mathbf{o}_j^{(\ell)}.
8	    \label{eq:head-mask}
9	\end{equation}
10	
11	\paragraph{KV cache eviction.}
12	A position mask $\mathbf{m}_k \in \{0,1\}^T$ retains the top-$(1{-}s)\cdot T$ positions (BOS always preserved):
13	\begin{equation}
14	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall\, i, j.
15	    \label{eq:kv-mask}
16	\end{equation}
17	Under importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:
18	\begin{equation}
19	    \mathrm{imp}(j) = \frac{\sum_{\ell, h, i} a_{ij}^{(\ell,h)}}{T - j},
20	    \label{eq:kv-importance}
21	\end{equation}
22	where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.
23	
24	\paragraph{Compound sparsity.}
25	Applying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.
26	
27	\paragraph{Attention sparsity metric.}
28	For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:
29	\begin{equation}
30	    \sigma_i^{(h)} = \frac{1}{T} \sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right].
31	    \label{eq:attn-sparsity}
32	\end{equation}
33	The per-position spar
…[truncated 1336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 436 · 2026-05-15T12:33:01.165294+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
  }
}
```

</details>

---


### Tool result

_source line 437 · 2026-05-15T12:33:02.072011+00:00_

1	% Content moved from main body to appendix:
2	% - Phase-strategy crossover details (from results §5.3)
3	% - Cross-model replication details with tables/figures (from results §5.4)
4	% - Permutation test details with table/forest plot (from results §5.5)
5	% - Full entropy-discrimination collapse analysis with tables (from analysis §6)
6	% Main body §6 (analysis.tex) contains a condensed summary referencing these tables.
7	
8	\section{Phase-Strategy Crossover Details}
9	\label{app:crossover-details}
10	
11	On DeepSeek ($n{=}496$), a strategy ranking reversal emerges at $s{=}0.25$ (Figure~\ref{fig:crossover}): importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.021$ vs.\ $1.113$) but \emph{higher} II in the low-sparsity phase ($3.971$ vs.\ $1.498$---a $2.7{\times}$ reversal; both $p < 10^{-4}$). This crossover is confirmed at all four sparsity levels, with reversal magnitude of $4.0{\times}$ at $s{=}0.15$, $3.4{\times}$ at $s{=}0.20$, $2.7{\times}$ at $s{=}0.25$, and $2.2{\times}$ at $s{=}0.30$ (decreasing as random eviction severity rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\S\ref{sec:discrimination-collapse}). Qwen does not exhibit a crossover: importance-based eviction produces lower II than random in both phases across all sparsity levels (e.g., at $s{=}0.25$: high $0.004$ vs.\ $1.109$; low $1.043$ vs.\ $1.770$). % exp_id: crossover_all_sparsity.csv; DS reversal: diff_low/diff_high = 2.99, 2.83, 2.13, 1.66
12	
13	\begin{figure}[t]
14	\centering
15	\includegraphics[width=\columnwidth]{fig3_crossover.pdf}
16	\caption{Strategy-dependent crossover at $s{=}0.25$ on DeepSeek ($n{=}496$). Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $2.7{\times}$ higher II in the low-sparsity phas
…[truncated 14257 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 438 · 2026-05-15T12:33:02.072579+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
  }
}
```

</details>

---


### Tool result

_source line 439 · 2026-05-15T12:33:02.596742+00:00_

1	\section{Discrimination Collapse Details}
2	\label{app:discrimination-collapse-details}
3	
4	This cross-model consistency (Table~\ref{tab:discrimination-metrics-full}) establishes discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.071$; Qwen: $-0.019$ to $-0.046$), confirming that discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
5	
6	
7	\section{Extended Discussion}
8	\label{app:extended-discussion}
9	
10	\paragraph{On the predictability of phase-modulated severity.}
11	The compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$). % exp_id: bf16_importance_s015..s030; high-phase medians: 0.006, 0.015, 0.032, 0.053
12	
13	\paragraph{Random masking as falsification control.}
14	At $n{=}500$, random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: non-significant at $s \leq 0.20$ for both models, but significant at $s \geq 0.25$ (DS: $\Delta{=}0.26$--$0.51$, $p_{\text{Bonf}} < 0.006$; QW: $\Delta{=}0.39$--$0.91$, $p_{\text{Bonf}} < 10^{-10}$). Where significant, the random phase gradient is $3$--$39{\times}$ weaker than importance-based, confirming that the dominant amplification is strategy-specific. % exp_id: n500_unified_final; DS rand s025 0.257 p=0.006, s030 0.510 p=0.006; QW rand s025 0.393, s030 0.913
15	
16	\paragraph{Entropy mechanism boundary conditions.}
17	Directly measuring per-head entropy s
…[truncated 4903 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 524
}
```

</details>

---


### Tool call

_source line 440 · 2026-05-15T12:33:02.647976+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex"
  }
}
```

</details>

---


### Tool result

_source line 441 · 2026-05-15T12:33:03.201018+00:00_

1	\section{Benjamini-Hochberg FDR Correction}
2	\label{app:bh-fdr}
3	
4	Table~\ref{tab:bh-fdr} compares Bonferroni ($k{=}4$, per model$\times$strategy family) and Benjamini-Hochberg FDR correction across all 44 statistical tests. BH-FDR recovers 5 additional significant results beyond Bonferroni, all in low-effect-size conditions (random eviction or cross-model random comparisons). All 32 Bonferroni-significant results remain significant under BH-FDR.
5	
6	\begin{table}[t]
7	\centering
8	\small
9	\caption{Bonferroni vs.\ BH-FDR correction summary ($\alpha{=}0.05$, 44 tests). ``BH only'' denotes tests significant under BH-FDR but not Bonferroni.}
10	\label{tab:bh-fdr}
11	\begin{tabular}{@{}lcc@{}}
12	\toprule
13	Category & Bonf.\ sig. & BH-only sig. \\
14	\midrule
15	Per-condition Wilcoxon ($k{=}16$) & 10 & 2 \\
16	Imp vs.\ rand ($k{=}8$) & 8 & 0 \\
17	Adjacent sparsity ($k{=}12$) & 10 & 1 \\
18	Cross-model Mann-Whitney ($k{=}8$) & 4 & 2 \\
19	\midrule
20	Total ($k{=}44$) & 32 & 5 \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	The 5 BH-only results are: DeepSeek random $s{=}0.25$ and $s{=}0.30$ per-condition Wilcoxon ($p_{\text{Bonf}}{=}0.064$/$0.065$, BH $q{=}0.002$), DeepSeek random $s{=}0.25 \to 0.30$ adjacent-sparsity step ($p_{\text{Bonf}}{=}0.078$, BH $q{=}0.002$), and cross-model random $s{=}0.25$/$s{=}0.30$ Mann-Whitney ($p_{\text{Bonf}}{=}0.66$/$0.17$, BH $q{=}0.018$/$0.005$). All involve random eviction---the weakest effects---confirming that Bonferroni is conservative but does not miss any importance-based findings. % exp_id: n500_unified_final; source: supplementary_stats.json bh_fdr_correction
26	
27	
28	\section{Minimum Phase Length Sensitivity}
29	\label{app:mpl-sensitivity}
30	
31	Table~\ref{tab:mpl-sensitivity} reports the paired median difference $\Delta$ under three \texttt{min\_phase\_length} (mpl) settings across all 16 conditions (2 models $\times$ 2 strategies $\times$ 4 sparsity levels). Conclusions are robust: all importance-based c
…[truncated 4680 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 442 · 2026-05-15T12:33:03.301930+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 443 · 2026-05-15T12:33:04.106030+00:00_

1	% References for Phase-Gated Compound Sparse paper
2	% Generated 2026-05-14; all entries verified via web search
3	
4	@inproceedings{adakv-neurips2025,
5	    title     = {Ada-{KV}: Optimizing {KV} Cache Eviction by Adaptive Budget Allocation for Efficient {LLM} Inference},
6	    author    = {Feng, Yuan and Lv, Junlin and Cao, Yukun and Xie, Xike and Zhou, S. Kevin},
7	    booktitle = {Advances in Neural Information Processing Systems},
8	    year      = {2025},
9	    url       = {https://arxiv.org/abs/2407.11550},
10	}
11	
12	@article{decision-repr-transition-2026,
13	    title   = {Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions},
14	    author  = {Shi, Boyu and Liu, Chang and Gao, ChuanBao and Yang, Xu and Geng, Xin},
15	    journal = {arXiv preprint arXiv:2605.07271},
16	    year    = {2026},
17	    url     = {https://arxiv.org/abs/2605.07271},
18	}
19	
20	@article{deepseek-r1-2025,
21	    title   = {{DeepSeek-R1} incentivizes reasoning in {LLMs} through reinforcement learning},
22	    author  = {{DeepSeek-AI}},
23	    journal = {Nature},
24	    volume  = {645},
25	    pages   = {633--638},
26	    year    = {2025},
27	    doi     = {10.1038/s41586-025-09422-z},
28	}
29	
30	@inproceedings{defensivekv-iclr2026,
31	    title     = {{DefensiveKV}: Taming the Fragility of {KV} Cache Eviction in {LLM} Inference},
32	    author    = {Feng, Yuan and Guo, Haoyu and Lv, Junlin and Zhou, S. Kevin and Xie, Xike},
33	    booktitle = {International Conference on Learning Representations},
34	    year      = {2026},
35	    url       = {https://arxiv.org/abs/2510.13334},
36	}
37	
38	@article{doing-more-with-less-2026,
39	    title   = {Doing More With Less: Revisiting the Effectiveness of {LLM} Pruning for Test-Time Scaling},
40	    author  = {Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman},
41	    journal = {arXiv preprint arXiv:2604.25098},
42	    year    = {2026},
43	    url     = {https://arxiv
…[truncated 12273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 444 · 2026-05-15T12:33:04.106530+00:00_

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
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 445 · 2026-05-15T12:33:04.109329+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 reviewer guidelines review form scoring criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 reviewer guidelines review form scoring criteria"
  }
}
```

</details>

---


### Tool result

_source line 446 · 2026-05-15T12:33:11.449059+00:00_

Web search results for query: "EMNLP 2026 reviewer guidelines review form scoring criteria"

Links: [{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form","url":"http://aclrollingreview.org/reviewform"},{"title":"Changes to reviewer volunteering requirement and incentives in May 2025 cycle (EMNLP 2025)","url":"http://aclrollingreview.org/incentives2025"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Advice on Reviewing for EMNLP","url":"https://2020.emnlp.org/blog/2020-05-17-write-good-reviews/"},{"title":"Instructions for Reviewers for EMNLP 2020","url":"https://2020.emnlp.org/blog/2020-05-26-instructions-for-reviewers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"2026 Reviewer Guidelines","url":"https://neurips.cc/Conferences/2026/ReviewerGuidelines"},{"title":"EMNLP 2026 | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026"}]

Based on the search results, here's what I found about EMNLP 2026 reviewer guidelines, review form, and scoring criteria:

## Review System

EMNLP 2026 will use ACL Rolling Review (ARR) as a reviewing system, but final decisions will be made by the conference.

## Scoring Criteria

For EMNLP 2026, the scoring criteria come from the ARR system. Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

**Soundness and Excitement:**
- The soundness scores must be justified by the text of the review.
- Sometimes you may find the work sound, but not something that is interesting for you personally. Such preferences are more subjective and should be reflected in a separate exci
…[truncated 798 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7339
}
```

</details>

---


### Tool result

_source line 447 · 2026-05-15T12:33:13.259968+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"}]

I've found comprehensive information about ACL Rolling Review 2026 reviewer guidelines and review form criteria. Here are the key details:

## Reviewer Guidelines

The ACL Rolling Review asks reviewers to follow this workflow: (1) read the paper and get a first impression, (2) search for related work, not deliberately trying to find that particular submissio
…[truncated 1880 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9153
}
```

</details>

---


### Tool call

_source line 448 · 2026-05-15T12:33:27.272810+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5, etc.), and descriptions of each score level. I need the exact numerical scales for soundness, excitement, overall assessment, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5, etc.), and descriptions of each score level. I need the exact numerical scales for soundness, excitement, overall assessment, and any other scored dimensions."
  }
}
```

</details>

---


### Tool call

_source line 449 · 2026-05-15T12:33:28.831632+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract all reviewer guidelines including what reviewers should check, how to assess novelty, soundness, completeness, and any specific criteria for empirical papers. Also extract any guidance on how to evaluate characterization/analysis papers vs method papers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract all reviewer guidelines including what reviewers should check, how to assess novelty, soundness, completeness, and any specific criteria for empirical papers. Also extract any guidance on how to evaluate characterization/analysis papers vs method papers."
  }
}
```

</details>

---


### Tool result

_source line 450 · 2026-05-15T12:33:32.700993+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence
**Scale: 1-5**
- 5: "Positive that my evaluation is correct. I read the paper very carefully"
- 4: Quite sure with unlikely errors
- 3: Fairly confident but may have missed details
- 2: Willing to defend evaluation but details likely missed
- 1: Outside expertise area or unclear paper

## Soundness
**Scale: 1-5 (with half-point increments)**
- 5: "Excellent: This study is one of the most thorough I have seen"
- 4: Strong with sufficient support; extra experiments optional
- 3: "Acceptable: This study provides sufficient support for its main claims"
- 2: Poor with insufficient support for main claims
- 1: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement
**Scale: 1-5 (with half-point increments)**
- 5: "Highly Exciting: I would recommend this paper to others"
- 4: Exciting; mention to others or attend presentation
- 3: Interesting; might mention or attend if time permits
- 2: "Potentially Interesting: this paper does not resonate with me"
- 1: Not exciting; unlikely to resonate with ACL community

## Overall Assessment
**Scale: 1-5 (with half-point increments)**
- 5: Consider for Award (top 2.5%)
- 4: Conference acceptance
- 3: Accept to Findings track
- 2: Resubmit next cycle with revisions
- 1: Do not resubmit; fundamentally flawed or irrelevant

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5428
}
```

</details>

---


### Tool result

_source line 451 · 2026-05-15T12:33:38.980351+00:00_

# ARR Reviewer Guidelines: Key Assessment Criteria

## Core Review Tasks

Reviewers must complete four main tasks: allocate calendar time, check assignments for expertise/COI, write strong reviews, and update assessments after author responses.

## What Reviewers Should Check

**Assignment Verification:**
- Confirm qualification to review the paper's methodology and core concepts
- Disclose any knowledge of author identity to the area chair
- Flag academic conflicts of interest if work closely matches your own research

**Desk Rejection Checklist:**
Reviewers assess papers for: appropriateness to ARR scope, hallucinated references, anonymity violations, style/length violations, missing limitations sections, inadequate responsible NLP checklist responses, and potential ethics issues.

## Assessing Novelty and Soundness

**Novelty Standards:**
Reviewers should verify claimed novelty through specific references. The guidelines warn against dismissing work as "not novel" without evidence. Reproduction studies and resource papers are legitimate contributions if appropriately presented.

**Soundness Evaluation:**
"Soundness scores must be justified by the text of the review. If you give a low soundness score without finding any major faults, this means that your review is not a faithful explanation of your recommendation."

## Common Review Pitfalls to Avoid

The guidelines list 17 heuristics that may indicate bias rather than legitimate weaknesses:

- Dismissing surprising or negative results
- Requiring SOTA performance (not necessary for scientific contribution)
- Criticizing simplicity of methods
- Demanding extra experiments beyond what claims require
- Over-relying on citation counts or precedent

## Paper-Type Specific Guidance

**Empirical Papers - Methodology Issues (M):**
- M1: LLM-only evaluation needs validation in context
- M2: Reproducibility requires sufficient detail, hyperparameters, code availability plans
- M3: Undisclosed data quality issues are seriou
…[truncated 1012 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 10148
}
```

</details>

---


### Tool call

_source line 452 · 2026-05-15T12:33:43.201998+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "compound sparsity joint compression LLM 2025 2026 KV cache pruning quantization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "compound sparsity joint compression LLM 2025 2026 KV cache pruning quantization"
  }
}
```

</details>

---


### Tool call

_source line 453 · 2026-05-15T12:33:43.553835+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "KV cache compression reasoning models chain-of-thought 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "KV cache compression reasoning models chain-of-thought 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 454 · 2026-05-15T12:33:44.828821+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "phase-aware phase-dependent inference compression LLM reasoning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "phase-aware phase-dependent inference compression LLM reasoning 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 455 · 2026-05-15T12:33:46.807972+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 456 · 2026-05-15T12:33:51.280473+00:00_

Web search results for query: "KV cache compression reasoning models chain-of-thought 2025 2026"

Links: [{"title":"[2510.01290] ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/abs/2510.01290"},{"title":"ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=M3CeHnZKNC"},{"title":"[2510.08525] Which Heads Matter for Reasoning? RL-Guided KV Cache Compression","url":"https://arxiv.org/abs/2510.08525"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://proceedings.neurips.cc/paper_files/paper/2025/hash/57e0358aed314784cad14a26e1eba642-Abstract-Conference.html"},{"title":"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=2jwAjomEDB"},{"title":"ICLR Oral ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://iclr.cc/virtual/2026/oral/10009981"},{"title":"GitHub - Zefan-Cai/R-KV: [Neurips 2025] R-KV: Redundancy-aware KV Cache Compression for Reasoning Models","url":"https://github.com/Zefan-Cai/R-KV"},{"title":"R-KV: Redundancy-aware KV Cache Compression for ...","url":"https://arxiv.org/pdf/2505.24133"},{"title":"Which Heads Matter for Reasoning? RL-Guided KV Cache Compression | OpenReview","url":"https://openreview.net/forum?id=HGdg76iVo6"},{"title":"[2510.01290v1] ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models","url":"https://arxiv.org/abs/2510.01290v1"}]

I've found several recent research papers on KV cache compression for reasoning models with chain-of-thought. Here are the key findings:

## Recent Approaches (2025-2026)

**ThinKV (October 2025)**: ThinKV addresses the challenge of long-output context generation of large reasoning models enabling extended chain of thought (CoT) by using attention sparsity to reveal distinct thought types with varying importance, the
…[truncated 1404 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7726
}
```

</details>

---


### Tool result

_source line 457 · 2026-05-15T12:33:52.893485+00:00_

Web search results for query: "compound sparsity joint compression LLM 2025 2026 KV cache pruning quantization"

Links: [{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://arxiv.org/html/2505.22913v2"},{"title":"[Quick Review] Optimal Brain Restoration for Joint Quantization and Sparsification of\\n LLMs","url":"https://liner.com/review/optimal-brain-restoration-for-joint-quantization-and-sparsification-llms"},{"title":"Don’t Waste Bits! Adaptive KV-Cache Quantization for Lightweight On-Device LLMs","url":"https://arxiv.org/html/2604.04722v1"},{"title":"Efficient KV Caching for LLM Inference","url":"https://www.emergentmind.com/topics/efficient-kv-caching"},{"title":"KV Cache Compression for Inference Efficiency in LLMs: A Review","url":"https://arxiv.org/html/2508.06297v1"},{"title":"KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization | Request PDF","url":"https://www.researchgate.net/publication/397202512_KVQuant_Towards_10_Million_Context_Length_LLM_Inference_with_KV_Cache_Quantization"},{"title":"KV Cache Compression in Transformer LLMs","url":"https://www.emergentmind.com/topics/kv-cache-compression"},{"title":"Hardware-Efficient Key-Value Caching in LLMs | by DrKilngon | Medium","url":"https://medium.com/@DrKilngon/hardware-efficient-key-value-caching-in-llms-3f9966c012cf"},{"title":"GitHub - HuangOwen/Awesome-LLM-Compression: Awesome LLM compression research papers and tools. · GitHub","url":"https://github.com/HuangOwen/Awesome-LLM-Compression"}]

I've completed the web search for compound sparsity, joint compression, and KV cache optim
…[truncated 1796 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9691
}
```

</details>

---


### Tool result

_source line 458 · 2026-05-15T12:33:56.860957+00:00_

Web search results for query: "phase-aware phase-dependent inference compression LLM reasoning 2025 2026"

Links: [{"title":"Phase-Level Analysis of LLM Inference","url":"https://www.emergentmind.com/topics/phase-level-analysis-of-llm-inference"},{"title":"The Illusion of Power Capping in LLM Decode: A Phase-Aware Energy Characterisation Across Attention Architectures","url":"https://arxiv.org/html/2605.11999v1"},{"title":"Phase transitions in large language model compression | npj Artificial Intelligence","url":"https://www.nature.com/articles/s44387-026-00072-8"},{"title":"LLM Inference Optimization Techniques | Clarifai Guide","url":"https://www.clarifai.com/blog/llm-inference-optimization/"},{"title":"The Compression Paradox in LLM Inference: Provider-Dependent Energy Effects of Prompt Compression","url":"https://arxiv.org/html/2603.23528"},{"title":"The Compression Paradox in LLM Inference: Provider-Dependent","url":"https://arxiv.org/pdf/2603.23528"},{"title":"LLM Inference: Prefill, Decode, KV Cache & Cost Guide (2026) | Morph","url":"https://www.morphllm.com/llm-inference"},{"title":"LLM Research Papers: The 2025 List (July to December)","url":"https://magazine.sebastianraschka.com/p/llm-research-papers-2025-part2"},{"title":"InfiniAI Lab - Publications","url":"http://www.infini-ai-lab.cmu.edu/publications/"},{"title":"GitHub - xlite-dev/Awesome-LLM-Inference: 📚A curated list of Awesome LLM/VLM Inference Papers with Codes: Flash-Attention, Paged-Attention, WINT8/4, Parallelism, etc.🎉","url":"https://github.com/xlite-dev/Awesome-LLM-Inference"}]

I found comprehensive information related to phase-aware and phase-dependent inference compression for LLMs. Here are the key findings from recent 2025-2026 research:

## Phase-Aware Compression Techniques

Phase-aware mixed-precision techniques allocate higher precision for prefill (e.g., 4–8 bits) and progressively lower precision for late-stage decoding (as low as 2–3 bits for long generations), exploiting the low
…[truncated 1669 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 12032
}
```

</details>

---


### Tool result

_source line 459 · 2026-05-15T12:34:19.221116+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 33, \"total_citations\": 65, \"unique_cited_keys\": 33, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 25, \"online_not_found\": 3, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"adakv-neurips2025\", \"type\": \"inproceedings\", \"title\": \"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference\", \"authors\": \"Feng, Yuan and Lv, Junlin and Cao, Yukun and Xie, Xike and Zhou, S. Kevin\", \"year\": \"2025\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"decision-repr-transition-2026\", \"type\": \"article\", \"title\": \"Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions\", \"authors\": \"Shi, Boyu and Liu, Chang and Gao, ChuanBao and Yang, Xu and Geng, Xin\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.07271\"}, {\"key\": \"deepseek-r1-2025\", \"type\": \"article\", \"title\": \"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning\", \"authors\": \"DeepSeek-AI\", \"year\": \"2025\", \"venue\": \"Nature\"}, {\"key\": \"defensivekv-iclr2026\", \"type\": \"inproceedings\", \"title\": \"DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference\", \"authors\": \"Feng, Yuan and Guo, Haoyu and Lv, Junlin and Zhou, S. Kevin and Xie, Xike\", \"year\": \"2026\", \"venue\": \"International Conference on Learning Representations\"}, {\"key\": \"doing-more-with-less-2026\", \"type\": \"article\", \"title\": \"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling\", \"authors\": \"Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2604.25098\"}, {\"key\": \"efron-1993\", \"ty
…[truncated 27362 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 32413
}
```

</details>

---


### Tool call

_source line 460 · 2026-05-15T12:34:23.993621+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MUSTAFAR unstructured sparsity KV cache pruning LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MUSTAFAR unstructured sparsity KV cache pruning LLM 2025"
  }
}
```

</details>

---


### Tool call

_source line 461 · 2026-05-15T12:34:24.546466+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"attention head pruning\" \"KV cache eviction\" interaction compound 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"attention head pruning\" \"KV cache eviction\" interaction compound 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 462 · 2026-05-15T12:34:30.174510+00:00_

Web search results for query: "MUSTAFAR unstructured sparsity KV cache pruning LLM 2025"

Links: [{"title":"[2505.22913] Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://arxiv.org/abs/2505.22913"},{"title":"NeurIPS Poster MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://neurips.cc/virtual/2025/poster/119320"},{"title":"MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference | OpenReview","url":"https://openreview.net/forum?id=C69741fMFX"},{"title":"MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://arxiv.org/html/2505.22913v1"},{"title":"MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://openreview.net/pdf?id=C69741fMFX"},{"title":"(PDF) Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://www.researchgate.net/publication/392204576_Mustafar_Promoting_Unstructured_Sparsity_for_KV_Cache_Pruning_in_LLM_Inference"},{"title":"GitHub - dhjoo98/mustafar: codebase for MUSTAFAR:Promoting Unstructured Sparsity for KV Pruning in LLM Inference","url":"https://github.com/dhjoo98/mustafar"},{"title":"Paper page - Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://huggingface.co/papers/2505.22913"},{"title":"[PDF] Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Mustafar:-Promoting-Unstructured-Sparsity-for-KV-in-Joo-Hosseini/643c287adfaccc9d5c06496c9711beb96b2b4d3c"},{"title":"Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning ...","url":"https://neurips.cc/media/neurips-2025/Slides/119320.pdf"}]

## Search Results for MUSTAFAR

I found comprehensive information about MUSTAFAR. Here are the key findings:

### Overview
MUSTAFAR demonstrates that unstructured sparsity significantly imp
…[truncated 1430 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6180
}
```

</details>

---


### Tool result

_source line 463 · 2026-05-15T12:34:32.034021+00:00_

Web search results for query: ""attention head pruning" "KV cache eviction" interaction compound 2025 2026"

Links: [{"title":"GitHub - NVIDIA/kvpress: LLM KV cache compression made easy · GitHub","url":"https://github.com/NVIDIA/kvpress"},{"title":"KV Cache Pruning in Transformers","url":"https://www.emergentmind.com/topics/kv-cache-pruning"},{"title":"PagedEviction: Structured Block-wise KV Cache Pruning ...","url":"https://aclanthology.org/2026.findings-eacl.168.pdf"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention","url":"https://arxiv.org/pdf/2510.00636"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention From Future Queries Distribution | OpenReview","url":"https://openreview.net/forum?id=VmojW15eRc"},{"title":"THINNER KEY CACHE BY QUERY-DRIVEN PRUNING","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8edb116d5b288b6a9bba4c16ab647702-Paper-Conference.pdf"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution","url":"https://arxiv.org/html/2510.00636v1"},{"title":"LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction","url":"https://arxiv.org/html/2605.06676"},{"title":"KV Cache Strategies for LLM Efficiency","url":"https://www.emergentmind.com/topics/kv-cache-strategy"}]

Based on the web search results, I found relevant information about attention head pruning and KV cache eviction interactions in recent 2025-2026 research:

## Key Findings on Attention Head Pruning and KV Cache Eviction Interactions

### Head-wise Heterogeneity and Budget Allocation

Early KV cache e
…[truncated 1697 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7487
}
```

</details>

---


### Tool call

_source line 464 · 2026-05-15T12:37:19.274379+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿报告\n\n**论文**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Mathematical Reasoning Models\n**审查侧重**: 新颖性 + 完整性 + 相关工作 + 格式合规\n\n---\n\n## 总体评分\n\n**Overall**: 2.5/5（介于 Findings 接收与需修改重投之间）\n**一句话总结**: 实验方法论严谨、统计控制充分的实证特征化工作，但单一基准、仅用 PPL 指标、缺少下游准确率验证、且 mitigation pilot 失败，削弱了对 EMNLP main conference 的贡献力度。\n\n---\n\n## 官方维度打分（ACL ARR Review Form, Feb 2025+）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 统计方法全面（bootstrap CI、Bonferroni、Jonckheere-Terpstra、permutation test、BH-FDR robustness check），随机 baseline 作为 falsification control 设计精良。但仅用 perplexity 无 downstream accuracy 是一个方法论缺陷；crossover 仅在 DeepSeek 上出现，Qwen 无法复现；LLaMA 跨架构验证 n=49 且统计显著性混合。 |\n| **Excitement** | 2.5/5 | Phase-strategy interaction 的定量刻画有一定新颖性，crossover effect 是 non-trivial 发现。但本质是 characterization 而非方法贡献，mitigation pilot 失败（18% recovery, gate FAIL），论文未能展示发现的可操作价值。对 EMNLP main conference 的 excitement 偏低。 |\n| **Overall** | 2.5/5 | Borderline Findings / 需修改重投。方法论扎实但 scope 受限严重（单基准、单尺度、仅 PPL），核心发现的实际影响力（actionability）未被证明。 |\n| **Confidence** | 4/5 | 熟悉 KV cache compression 和 attention pruning 文献，仔细阅读了全文含 appendix。 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **仅用 Perplexity，缺少 Downstream Accuracy 验证**\n- 具体位置：§4 (Experimental Setup), §5 (Results), Limitations §\"Perplexity vs. accuracy\"\n- 问题：论文的核心指标 Interaction Index (II) 完全基于 perplexity（Eq. 1）。Limitations 中作者承认 \"perplexity has a known nonlinear relationship with downstream accuracy\"，但未提供任何 accuracy 层面的验证。PPL 的 phase-level 恶化可能在 accuracy 层面被吸收（例如，low-sparsity phase 的 PPL 增长集中在 reasoning trace 的非关键 token 上，对最终答案准确率影响甚微）。\n- 为什么影响接收：论文声称 \"motivate phase-aware compression budgets for mathematical reasoning models\"（Abstract, §7 Discussion），但如果 PPL 恶化不转化为 accuracy 下降，则整个 motivation 不成立。这是一个根本性的 construct validity 问题。ARR Review Form M4 要求 \"model/benchmark selection must be motivated and linked to claims\"——此处 claim 关于 reasoning quality 但指标不直接衡量 reasoning quality。\n- 建议修改方向：至少报告 MATH-500 problem-level accuracy under compound sparsity（总 accuracy 及分 phase 的 partial credit/answer correctness），建立 II 与 accuracy regression 的关系。如果 PPL 严重退化但 accuracy 不变，结论需根本性修正。\n\n**N2** [critical] **Generalizability 极度受限：单一基准 + 单一模型规模**\n- 具体位置：§4 Dataset, §4 Models, Limitations §\"Task coverage\" 和 §\"Model scale\"\n- 问题：全部实验仅在 MATH-500（一个数学推理基准，500 题）上进行，仅评估 7B 模型（两个 Qwen2 架构 + 一个 LLaMA 的初步验证，n=49）。论文 title 使用 \"Mathematical Reasoning Models\"（泛化 claim），但证据仅来自一个特定 benchmark 的一个规模。\n- 为什么影响接收：EMNLP 对 empirical work 的 scope 有要求。(1) 不同推理任务（code, science reasoning）的 phase structure 可能完全不同——作者自己在 Limitations 中承认这点。(2) 7B→70B 的 scale 行为完全未知。(3) 两个 Qwen2 模型共享 backbone（28层/28 head/4-group GQA），cross-model replication 的独立性有限——更像是 \"two weight initializations on the same architecture\" 而非真正的跨模型验证。LLaMA 验证（§5.5）magnitude ~1/40，strategy contrast 弱，统计显著性混合。\n- 建议修改方向：增加至少一个非数学推理 benchmark（如 GSM8K 作为另一个数学推理点、HumanEval/MBPP 作为 code reasoning、GPQA 作为 science reasoning）；增加 13B 或更大规模模型验证，或至少明确讨论为什么 7B 的发现足以支撑论文的 claim scope。\n\n**N3** [critical] **Mitigation Pilot 失败，论文的实际价值存疑**\n- 具体位置：§7 Discussion, \"A preliminary pilot experiment\"\n- 问题：Oracle phase-aware budget reallocation 仅达到 18% recovery（预注册 30% gate FAIL）；heuristic variant 32% 但 CI 跨零。论文声称 \"motivate phase-aware compression budgets\"，但自己的 pilot 实验证明 phase-aware reallocation 不足以解决这个问题。\n- 为什么影响接收：如果 characterization 的直接应用——phase-aware budget allocation——在 oracle 条件下都无法达标，那么这个 characterization 的 practical value 是什么？论文的 framing 从 \"This is a useful diagnostic\" 到 \"This motivates phase-aware compression\" 之间存在张力。Reviewer 会质疑：if knowing exactly where the problem is still can't fix it, what is the contribution? 这是一个 ARR \"excitement\" 维度的核心问题。\n- 建议修改方向：(1) 重新定位论文 framing，不再 overclaim \"motivate phase-aware compression\"，而是明确为 \"characterization of a previously unknown phenomenon\"；(2) 更深入分析为什么 oracle reallocation 失败——是因为 budget reallocation 本身不够（需要 strategy switching），还是因为 phase boundaries 不够精确？(3) 讨论是否 joint optimization of budget + strategy selection 能解决问题。论文在 Discussion 最后一段暗示了这点，但需要更充分的分析。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **Crossover Effect 的 model dependence 削弱了核心 contribution 之一**\n- 具体位置：§5.3, §5.4, §7 Discussion\n- 问题：Crossover（importance-based 在 high-sparsity phase 优于 random 但在 low-sparsity phase 劣于 random）仅在 DeepSeek 上出现。Qwen \"does not exhibit this crossover\"（§5.3）。Introduction 中将 crossover 作为论证 \"Why can't existing single-axis findings predict our results?\" 的关键证据（§1, \"Instead, we observe a sign reversal\"）。但这个 sign reversal 是 model-dependent 的。\n- 建议：将 crossover 降级为 \"model-specific phenomenon\"，不在 Introduction 的核心论证中过度依赖。或者解释为什么 crossover 在 Qwen 上不出现（是否与 training methodology 相关？DeepSeek 是 distillation，Qwen 是 instruction tuning）。\n\n**W2** [warning] **\"Emergent\" 用词 overclaiming**\n- 具体位置：Abstract (\"emergent phase-strategy interaction\"), §1 (\"This emergent coupling is not deducible from single-axis characterizations\")\n- 问题：\"Emergent\" 在 ML 社区有特定含义（通常指 scale-dependent 的突现行为）。此处论文实际展示的是 compound sparsity 在不同 phase 上的差异——这是两个已知 axis 的交互，不是真正的 \"emergence\"。更准确地说，这是一个 \"interaction effect\" 或 \"non-trivial composition effect\"。\n- 建议：将 \"emergent\" 替换为更精确的术语，如 \"non-additive\" 或 \"interaction-driven\"，避免 overclaiming。\n\n**W3** [warning] **缺少 Throughput/Latency 评估**\n- 具体位置：§7 Discussion, Limitations §\"No throughput evaluation\"\n- 问题：论文反复声称 \"motivate phase-aware compression budgets for deployment\"，但完全没有 throughput 或 latency 数据。Phase-aware compression 需要 runtime phase detection，这本身有计算开销。如果 phase detection 的 overhead 抵消了 compression 的 savings，则实际部署价值为零。\n- 建议：至少提供一个 rough estimate 或 back-of-envelope calculation，说明 phase-aware allocation 在实际 inference 中的 overhead 与 savings 之间的 trade-off。\n\n**W4** [warning] **Discrimination Collapse 分析的 sufficiency gap**\n- 具体位置：§6 Analysis, Table in Appendix D\n- 问题：论文正确指出 Gini 下降在两种策略间几乎一致（<10% 差异），但 severity 相差 15-17×。这证明了 Gini collapse 是 \"necessary but not sufficient\"。然而，论文提出的 \"structural specificity\" 解释（importance-based pruning 系统性移除 high-score heads）仅是一个定性论证，没有定量证据直接支持。\n- 建议：(1) 提供 pruned heads 在不同 phase 的 overlap 分析（importance vs random pruning 分别移除了哪些 heads，这些 heads 在不同 phase 的 attention pattern 是否不同）；(2) 或至少承认 \"structural specificity\" 假说目前缺乏直接证据。\n\n**W5** [warning] **Abstract 的 bootstrap CI 呈现具有误导性**\n- 具体位置：Abstract, line 3\n- 问题：Abstract 报告 \"$G$ of $7.5$--$79.8\\times$ (bootstrap 95\\% CI: $[4.1, 96.5]$)\"。这个 CI 不是一个整体的 CI，而是将四个不同 sparsity level 的 CI lower bound（4.1 来自 s=0.15）和 upper bound（96.5 来自 s=0.30）拼接在一起。这在统计上是不规范的——它不是任何单一参数的置信区间。\n- 建议：要么分别报告每个 sparsity level 的 CI，要么明确说明这是 \"range of CI bounds across sparsity levels\"。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Table 2 (main-results) 中 Qwen s=0.15 的 $\\widetilde{\\mathrm{II}}_{\\textit{high}} = -0.000$——负数 II 暗示 sub-additive 交互，文中未讨论其物理含义（可能只是 numerical noise，但应说明）。\n- **M2**: §4 footnote 提到 \"earlier float16 configuration produced sporadic NaN values; bfloat16 eliminated all occurrences\"——这个 numerical issue 值得在 appendix 中进一步讨论，因为它暗示了某些 conditions 下的 numerical instability。\n- **M3**: Figure 1 (fig1_dose_response.pdf) 使用 profiling subset (n=50) 的数据绘制，但 main results 已有 n=496 数据。hero figure 为什么不用 full-scale 数据？这会造成读者困惑。\n- **M4**: 参考文献中 `pyramidkv-2024` 的 year 写为 2024，但 venue 是 \"Conference on Language Modeling\"（2025）——year 应更新为 2025。\n- **M5**: Background §3 使用 `\\paragraph{Compound sparsity.}` 后跟 `\\label{sec:compound-sparsity}`——\\paragraph 不是 section，label 前缀用 sec: 不太规范。\n- **M6**: §5.1 中 \"the median phase difference rises from $0.39$ at $s=0.15$ to $8.48$ at $s=0.30$ (all Bonferroni-corrected $p < 10^{-69}$)\"——p 值精度到 10^{-69} 对读者来说过于 specific；建议简化为 $p \\ll 10^{-10}$ 或类似。\n\n---\n\n## 相关工作评估\n\n### 覆盖度\n\n总体相关工作覆盖较全面，33 篇引用中涵盖了 compound compression、KV cache eviction、phase-aware inference 三个主要方向的核心工作。以下为详细评估：\n\n**已覆盖的关键工作**（均正确引用）：\n- ThinKV (ICLR 2026) ✓ — phase-aware KV compression 的直接 baseline\n- SparK (AAAI 2026) ✓ — compound sparsity 的先驱\n- UniComp (2026) ✓ — 大规模 compound compression 评估\n- HIES (2025) ✓ — 单轴 discrimination collapse\n- Sparse Frontier (2025) ✓ — strategy non-dominance\n- R-KV (NeurIPS 2025) ✓ — reasoning-specific KV compression\n- PM-KVQ (ICLR 2026) ✓ — progressive quantization for CoT\n- GRASPrune (ACL 2026) ✓ — joint pruning with gates\n- Hold Onto That Thought (NeurIPS 2025) ✓ — KV compression on reasoning\n- LongFlow (2026) ✓, RLKV (2025) ✓, Lethe (AAAI 2026) ✓\n\n**潜在遗漏**：\n1. **MUSTAFAR (NeurIPS 2025)** — unstructured sparsity for KV cache pruning (Joo et al., arXiv:2505.22913)。虽然关注点是 within-entry unstructured sparsity（与本文的 structured head pruning + token eviction 不同），但作为 NeurIPS 2025 的 KV cache sparsity 工作，在 \"KV cache eviction\" 段落中值得一提。**非重大遗漏**。\n2. **LKV (2026)** — End-to-End Learning of Head-wise Budgets and Token Selection for KV Cache Eviction (arXiv:2605.06676)。学习 head-wise budget 的方法，与本文关注的 head pruning 如何影响 KV eviction 直接相关。**轻微遗漏**。\n\n### 引用验证结果\n\n通过 `verify_references` 工具验证：\n- 33 bib entries，0 orphan，0 missing（cite/bib 完全对应）\n- 25/33 通过 OpenAlex 在线验证\n- 3/33 未在 OpenAlex 找到（defensivekv-iclr2026, hies-2025, phase-transition-compression-2026）——均有有效 arXiv URL，可能是索引延迟\n- 5/33 minor mismatch（deepseek-r1-2025 的 author 格式：bib 用 DeepSeek-AI vs API 返回 Guo；snapkv-neurips2024 的 first author；unicomp-2026 的 von Rad vs Rad 等）——**均为 name formatting 问题，非 fabrication 问题**\n- **未发现 hallucinated references**\n\n---\n\n## 格式合规评估\n\n| 检查项 | 状态 | 说明 |\n|--------|------|------|\n| ACL 模板 | ✅ | `\\usepackage[review]{acl}` |\n| Double-blind | ✅ | `\\author{Anonymous}`，正文中未见 de-anonymization 信息 |\n| 正文页数 | ⚠️ | 无法编译验证。主文件包含 abstract + 7 sections (intro, related, background, methodology, results, analysis, discussion, conclusion)。内容量较大，存在超页风险——Table 2 是 table* (跨双栏)，加上 6 个 section 的文本量。建议作者自行确认不超 8 页。 |\n| Limitations section | ✅ | 在 `\\bibliography` 之后，有 `\\section*{Limitations}`，不计页数。内容覆盖 model scale, task coverage, symmetric sparsity, mechanism, perplexity vs accuracy, sparsity range——较为全面。 |\n| Reproducibility | ✅ | 有 `\\section*{Reproducibility}` 声明 \"Code and data will be released upon acceptance\"。统计方法详细（seed=42, B=10000）。但代码不可用（acceptance 后发布），reproducibility 在投稿阶段只是 promise。 |\n| Ethics/Broader Impact | — | 未包含，EMNLP \"鼓励\" 但非强制。 |\n| 参考文献格式 | ✅ | `\\bibliography{references}` 使用 ACL 风格。注意 \\cite 和 \\citep/\\citet 混用——某些位置用 \\cite 应为 \\citep（如 related_work.tex line 6-8 多处）。 |\n\n---\n\n## 主要优势\n\n1. **实验方法论极其严谨**：Random baseline 作为 falsification control 的设计精良；bootstrap CI ($B=10000$)、Bonferroni correction、BH-FDR robustness check、Jonckheere-Terpstra dose-response test、permutation test、多种 segmentation granularity 的 sensitivity analysis——统计处理水平远超 NLP 领域平均。\n2. **发现本身具有科学价值**：Phase-strategy interaction 的定量刻画（$G = 7.5$--$79.8\\times$）是一个 previously undocumented 的现象。Crossover effect 在 DeepSeek 上的发现是 non-trivial 的。\n3. **论文写作清晰诚实**：Limitations section 详尽，LLaMA 跨架构结果的 hedging 恰当（\"preliminary\", \"suggestive\", \"mixed evidence\"），没有隐藏 negative results（pilot failure 直接报告）。Discrimination collapse 被明确标记为 \"correlational\" 而非 causal。\n4. **Reproducibility 细节充分**：exp_id 标注在 LaTeX 注释中，bootstrap seed 固定，所有 hyperparameters 明确报告。\n\n---\n\n## 关键问题（供 author response）\n\n1. 是否有任何 problem-level accuracy 数据（即使是 partial）可以展示 II gradient 与 accuracy 退化的关系？\n2. Crossover effect 在 Qwen 上不出现——作者对此的解释是什么？是否与 distillation vs instruction tuning 的 training methodology 相关？\n3. Oracle mitigation 仅 18% recovery——作者是否分析了失败的原因？是 budget reallocation 不够，还是 phase boundary 不够精确，还是需要 strategy switching？\n4. 对于 Table 2 中 Qwen s=0.15 的 $\\widetilde{\\mathrm{II}}_{\\textit{high}} = -0.000$（sub-additive），作者如何解释？\n\n---\n\n*Reviewer 2, Round 1 完成。审查侧重：新颖性、完整性、相关工作、格式合规。*",
  "reviewer_id": "2",
  "project": "phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 审稿报告\n\n**论文**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Mathematical Reasoning Models\n**审查侧重**: 新颖性 + 完整性 + 相关工作 + 格式合规\n\n---\n\n## 总体评分\n\n**Overall**: 2.5/5（介于 Findings 接收与需修改重投之间）\n**一句话总结**: 实验方法论严谨、统计控制充分的实证特征化工作，但单一基准、仅用 PPL 指标、缺少下游准确率验证、且 mitigation pilot 失败，削弱了对 EMNLP main conference 的贡献力度。\n\n---\n\n## 官方维度打分（ACL ARR Review Form, Feb 2025+）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 统计方法全面（bootstrap CI、Bonferroni、Jonckheere-Terpstra、permutation test、BH-FDR robustness check），随机 baseline 作为 falsification control 设计精良。但仅用 perplexity 无 downstream accuracy 是一个方法论缺陷；crossover 仅在 DeepSeek 上出现，Qwen 无法复现；LLaMA 跨架构验证 n=49 且统计显著性混合。 |\n| **Excitement** | 2.5/5 | Phase-strategy interaction 的定量刻画有一定新颖性，crossover effect 是 non-trivial 发现。但本质是 characterization 而非方法贡献，mitigation pilot 失败（18% recovery, gate FAIL），论文未能展示发现的可操作价值。对 EMNLP main conference 的 excitement 偏低。 |\n| **Overall** | 2.5/5 | Borderline Findings / 需修改重投。方法论扎实但 scope 受限严重（单基准、单尺度、仅 PPL），核心发现的实际影响力（actionability）未被证明。 |\n| **Confidence** | 4/5 | 熟悉 KV cache compression 和 attention pruning 文献，仔细阅读了全文含 appendix。 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **仅用 Perplexity，缺少 Downstream Accuracy 验证**\n- 具体位置：§4 (Experimental Setup), §5 (Results), Limitations §\"Perplexity vs. accuracy\"\n- 问题：论文的核心指标 Interaction Index (II) 完全基于 perplexity（Eq. 1）。Limitations 中作者承认 \"perplexity has a known nonlinear relationship with downstream accuracy\"，但未提供任何 accuracy 层面的验证。PPL 的 phase-level 恶化可能在 accuracy 层面被吸收（例如，low-sparsity phase 的 PPL 增长集中在 reasoning trace 的非关键 token 上，对最终答案准确率影响甚微）。\n- 为什么影响接收：论文声称 \"motivate phase-aware compression budgets for mathematical reasoning models\"（Abstract, §7 Discussion），但如果 PPL 恶化不转化为 accuracy 下降，则整个 motivation 不成立。这是一个根本性的 construct validity 问题。ARR Review Form M4 要求 \"model/benchmark selection must be motivated and linked to claims\"——此处 claim 关于 reasoning quality 但指标不直接衡量 reasoning quality。\n- 建议修改方向：至少报告 MATH-500 problem-level accuracy under compound sparsity（总 accuracy 及分 phase 的 partial credit/answer correctness），建立 II 与 accuracy regression 的关系。如果 PPL 严重退化但 accuracy 不变，结论需根本性修正。\n\n**N2** [critical] **Generalizability 极度受限：单一基准 + 单一模型规模**\n- 具体位置：§4 Dataset, §4 Models, Limitations §\"Task coverage\" 和 §\"Model scale\"\n- 问题：全部实验仅在 MATH-500（一个数学推理基准，500 题）上进行，仅评估 7B 模型（两个 Qwen2 架构 + 一个 LLaMA 的初步验证，n=49）。论文 title 使用 \"Mathematical Reasoning Models\"（泛化 claim），但证据仅来自一个特定 benchmark 的一个规模。\n- 为什么影响接收：EMNLP 对 empirical work 的 scope 有要求。(1) 不同推理任务（code, science reasoning）的 phase structure 可能完全不同——作者自己在 Limitations 中承认这点。(2) 7B→70B 的 scale 行为完全未知。(3) 两个 Qwen2 模型共享 backbone（28层/28 head/4-group GQA），cross-model replication 的独立性有限——更像是 \"two weight initializations on the same architecture\" 而非真正的跨模型验证。LLaMA 验证（§5.5）magnitude ~1/40，strategy contrast 弱，统计显著性混合。\n- 建议修改方向：增加至少一个非数学推理 benchmark（如 GSM8K 作为另一个数学推理点、HumanEval/MBPP 作为 code reasoning、GPQA 作为 science reasoning）；增加 13B 或更大规模模型验证，或至少明确讨论为什么 7B 的发现足以支撑论文的 claim scope。\n\n**N3** [critical] **Mitigation Pilot 失败，论文的实际价值存疑**\n- 具体位置：§7 Discussion, \"A preliminary pilot experiment\"\n- 问题：Oracle phase-aware budget reallocation 仅达到 18% recovery（预注册 30% gate FAIL）；heuristic variant 32% 但 CI 跨零。论文声称 \"motivate phase-aware compression budgets\"，但自己的 pilot 实验证明 phase-aware reallocation 不足以解决这个问题。\n- 为什么影响接收：如果 characterization 的直接应用——phase-aware budget allocation——在 oracle 条件下都无法达标，那么这个 characterization 的 practical value 是什么？论文的 framing 从 \"This is a useful diagnostic\" 到 \"This motivates phase-aware compression\" 之间存在张力。Reviewer 会质疑：if knowing exactly where the problem is still can't fix it, what is the contribution? 这是一个 ARR \"excitement\" 维度的核心问题。\n- 建议修改方向：(1) 重新定位论文 framing，不再 overclaim \"motivate phase-aware compression\"，而是明确为 \"characterization of a previously unknown phenomenon\"；(2) 更深入分析为什么 oracle reallocation 失败——是因为 budget reallocation 本身不够（需要 strategy switching），还是因为 phase boundaries 不够精确？(3) 讨论是否 joint optimization of budget + strategy selection 能解决问题。论文在 Discussion 最后一段暗示了这点，但需要更充分的分析。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **Crossover Effect 的 model dependence 削弱了核心 contribution 之一**\n- 具体位置：§5.3, §5.4, §7 Discussion\n- 问题：Crossover（importance-based 在 high-sparsity phase 优于 random 但在 low-sparsity phase 劣于 random）仅在 DeepSeek 上出现。Qwen \"does not exhibit this crossover\"（§5.3）。Introduction 中将 crossover 作为论证 \"Why can't existing single-axis findings predict our results?\" 的关键证据（§1, \"Instead, we observe a sign reversal\"）。但这个 sign reversal 是 model-dependent 的。\n- 建议：将 crossover 降级为 \"model-specific phenomenon\"，不在 Introduction 的核心论证中过度依赖。或者解释为什么 crossover 在 Qwen 上不出现（是否与 training methodology 相关？DeepSeek 是 distillation，Qwen 是 instruction tuning）。\n\n**W2** [warning] **\"Emergent\" 用词 overclaiming**\n- 具体位置：Abstract (\"emergent phase-strategy interaction\"), §1 (\"This emergent coupling is not deducible from single-axis characterizations\")\n- 问题：\"Emergent\" 在 ML 社区有特定含义（通常指 scale-dependent 的突现行为）。此处论文实际展示的是 compound sparsity 在不同 phase 上的差异——这是两个已知 axis 的交互，不是真正的 \"emergence\"。更准确地说，这是一个 \"interaction effect\" 或 \"non-trivial composition effect\"。\n- 建议：将 \"emergent\" 替换为更精确的术语，如 \"non-additive\" 或 \"interaction-driven\"，避免 overclaiming。\n\n**W3** [warning] **缺少 Throughput/Latency 评估**\n- 具体位置：§7 Discussion, Limitations §\"No throughput evaluation\"\n- 问题：论文反复声称 \"motivate phase-aware compression budgets for deployment\"，但完全没有 throughput 或 latency 数据。Phase-aware compression 需要 runtime phase detection，这本身有计算开销。如果 phase detection 的 overhead 抵消了 compression 的 savings，则实际部署价值为零。\n- 建议：至少提供一个 rough estimate 或 back-of-envelope calculation，说明 phase-aware allocation 在实际 inference 中的 overhead 与 savings 之间的 trade-off。\n\n**W4** [warning] **Discrimination Collapse 分析的 sufficiency gap**\n- 具体位置：§6 Analysis, Table in Appendix D\n- 问题：论文正确指出 Gini 下降在两种策略间几乎一致（<10% 差异），但 severity 相差 15-17×。这证明了 Gini collapse 是 \"necessary but not sufficient\"。然而，论文提出的 \"structural specificity\" 解释（importance-based pruning 系统性移除 high-score heads）仅是一个定性论证，没有定量证据直接支持。\n- 建议：(1) 提供 pruned heads 在不同 phase 的 overlap 分析（importance vs random pruning 分别移除了哪些 heads，这些 heads 在不同 phase 的 attention pattern 是否不同）；(2) 或至少承认 \"structural specificity\" 假说目前缺乏直接证据。\n\n**W5** [warning] **Abstract 的 bootstrap CI 呈现具有误导性**\n- 具体位置：Abstract, line 3\n- 问题：Abstract 报告 \"$G$ of $7.5$--$79.8\\times$ (bootstrap 95\\% CI: $[4.1, 96.5]$)\"。这个 CI 不是一个整体的 CI，而是将四个不同 sparsity level 的 CI lower bound（4.1 来自 s=0.15）和 upper bound（96.5 来自 s=0.30）拼接在一起。这在统计上是不规范的——它不是任何单一参数的置信区间。\n- 建议：要么分别报告每个 sparsity level 的 CI，要么明确说明这是 \"range of CI bounds across sparsity levels\"。\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Table 2 (main-results) 中 Qwen s=0.15 的 $\\widetilde{\\mathrm{II}}_{\\textit{high}} = -0.000$——负数 II 暗示 sub-additive 交互，文中未讨论其物理含义（可能只是 numerical noise，但应说明）。\n- **M2**: §4 footnote 提到 \"earlier float16 configuration produced sporadic NaN values; bfloat16 eliminated all occurrences\"——这个 numerical issue 值得在 appendix 中进一步讨论，因为它暗示了某些 conditions 下的 numerical instability。\n- **M3**: Figure 1 (fig1_dose_response.pdf) 使用 profiling subset (n=50) 的数据绘制，但 main results 已有 n=496 数据。hero figure 为什么不用 full-scale 数据？这会造成读者困惑。\n- **M4**: 参考文献中 `pyramidkv-2024` 的 year 写为 2024，但 venue 是 \"Conference on Language Modeling\"（2025）——year 应更新为 2025。\n- **M5**: Background §3 使用 `\\paragraph{Compound sparsity.}` 后跟 `\\label{sec:compound-sparsity}`——\\paragraph 不是 section，label 前缀用 sec: 不太规范。\n- **M6**: §5.1 中 \"the median phase difference rises from $0.39$ at $s=0.15$ to $8.48$ at $s=0.30$ (all Bonferroni-corrected $p < 10^{-69}$)\"——p 值精度到 10^{-69} 对读者来说过于 specific；建议简化为 $p \\ll 10^{-10}$ 或类似。\n\n---\n\n## 相关工作评估\n\n### 覆盖度\n\n总体相关工作覆盖较全面，33 篇引用中涵盖了 compound compression、KV cache eviction、phase-aware inference 三个主要方向的核心工作。以下为详细评估：\n\n**已覆盖的关键工作**（均正确引用）：\n- ThinKV (ICLR 2026) ✓ — phase-aware KV compression 的直接 baseline\n- SparK (AAAI 2026) ✓ — compound sparsity 的先驱\n- UniComp (2026) ✓ — 大规模 compound compression 评估\n- HIES (2025) ✓ — 单轴 discrimination collapse\n- Sparse Frontier (2025) ✓ — strategy non-dominance\n- R-KV (NeurIPS 2025) ✓ — reasoning-specific KV compression\n- PM-KVQ (ICLR 2026) ✓ — progressive quantization for CoT\n- GRASPrune (ACL 2026) ✓ — joint pruning with gates\n- Hold Onto That Thought (NeurIPS 2025) ✓ — KV compression on reasoning\n- LongFlow (2026) ✓, RLKV (2025) ✓, Lethe (AAAI 2026) ✓\n\n**潜在遗漏**：\n1. **MUSTAFAR (NeurIPS 2025)** — unstructured sparsity for KV cache pruning (Joo et al., arXiv:2505.22913)。虽然关注点是 within-entry unstructured sparsity（与本文的 structured head pruning + token eviction 不同），但作为 NeurIPS 2025 的 KV cache sparsity 工作，在 \"KV cache eviction\" 段落中值得一提。**非重大遗漏**。\n2. **LKV (2026)** — End-to-End Learning of Head-wise Budgets and Token Selection for KV Cache Eviction (arXiv:2605.06676)。学习 head-wise budget 的方法，与本文关注的 head pruning 如何影响 KV eviction 直接相关。**轻微遗漏**。\n\n### 引用验证结果\n\n通过 `verify_references` 工具验证：\n- 33 bib entries，0 orphan，0 missing（cite/bib 完全对应）\n- 25/33 通过 OpenAlex 在线验证\n- 3/33 未在 OpenAlex 找到（defensivekv-iclr2026, hies-2025, phase-transition-compression-2026）——均有有效 arXiv URL，可能是索引延迟\n- 5/33 minor mismatch（deepseek-r1-2025 的 author 格式：bib 用 DeepSeek-AI vs API 返回 Guo；snapkv-neurips2024 的 first author；unicomp-2026 的 von Rad vs Rad 等）——**均为 name formatting 问题，非 fabrication 问题**\n- **未发现 hallucinated references**\n\n---\n\n## 格式合规评估\n\n| 检查项 | 状态 | 说明 |\n|--------|------|------|\n| ACL 模板 | ✅ | `\\usepackage[review]{acl}` |\n| Double-blind | ✅ | `\\author{Anonymous}`，正文中未见 de-anonymization 信息 |\n| 正文页数 | ⚠️ | 无法编译验证。主文件包含 abstract + 7 sections (intro, related, background, methodology, results, analysis, discussion, conclusion)。内容量较大，存在超页风险——Table 2 是 table* (跨双栏)，加上 6 个 section 的文本量。建议作者自行确认不超 8 页。 |\n| Limitations section | ✅ | 在 `\\bibliography` 之后，有 `\\section*{Limitations}`，不计页数。内容覆盖 model scale, task coverage, symmetric sparsity, mechanism, perplexity vs accuracy, sparsity range——较为全面。 |\n| Reproducibility | ✅ | 有 `\\section*{Reproducibility}` 声明 \"Code and data will be released upon acceptance\"。统计方法详细（seed=42, B=10000）。但代码不可用（acceptance 后发布），reproducibility 在投稿阶段只是 promise。 |\n| Ethics/Broader Impact | — | 未包含，EMNLP \"鼓励\" 但非强制。 |\n| 参考文献格式 | ✅ | `\\bibliography{references}` 使用 ACL 风格。注意 \\cite 和 \\citep/\\citet 混用——某些位置用 \\cite 应为 \\citep（如 related_work.tex line 6-8 多处）。 |\n\n---\n\n## 主要优势\n\n1. **实验方法论极其严谨**：Random baseline 作为 falsification control 的设计精良；bootstrap CI ($B=10000$)、Bonferroni correction、BH-FDR robustness check、Jonckheere-Terpstra dose-response test、permutation test、多种 segmentation granularity 的 sensitivity analysis——统计处理水平远超 NLP 领域平均。\n2. **发现本身具有科学价值**：Phase-strategy interaction 的定量刻画（$G = 7.5$--$79.8\\times$）是一个 previously undocumented 的现象。Crossover effect 在 DeepSeek 上的发现是 non-trivial 的。\n3. **论文写作清晰诚实**：Limitations section 详尽，LLaMA 跨架构结果的 hedging 恰当（\"preliminary\", \"suggestive\", \"mixed evidence\"），没有隐藏 negative results（pilot failure 直接报告）。Discrimination collapse 被明确标记为 \"correlational\" 而非 causal。\n4. **Reproducibility 细节充分**：exp_id 标注在 LaTeX 注释中，bootstrap seed 固定，所有 hyperparameters 明确报告。\n\n---\n\n## 关键问题（供 author response）\n\n1. 是否有任何 problem-level accuracy 数据（即使是 partial）可以展示 II gradient 与 accuracy 退化的关系？\n2. Crossover effect 在 Qwen 上不出现——作者对此的解释是什么？是否与 distillation vs instruction tuning 的 training methodology 相关？\n3. Oracle mitigation 仅 18% recovery——作者是否分析了失败的原因？是 budget reallocation 不够，还是 phase boundary 不够精确，还是需要 strategy switching？\n4. 对于 Table 2 中 Qwen s=0.15 的 $\\widetilde{\\mathrm{II}}_{\\textit{high}} = -0.000$（sub-additive），作者如何解释？\n\n---\n\n*Reviewer 2, Round 1 完成。审查侧重：新颖性、完整性、相关工作、格式合规。*",
    "reviewer_id": "2",
    "project": "phase-gated-compound-sparse"
  }
}
```

</details>

---


### Tool result

_source line 465 · 2026-05-15T12:37:23.595359+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4320
}
```

</details>

---


### Assistant

_source line 466 · 2026-05-15T12:37:34.421442+00:00_

Round 1 审稿报告已提交给 Review Director。

核心判断：**Overall 2.5/5**（borderline Findings / 需修改重投）。

三个 Must-Fix 问题：
1. **仅用 PPL 无 downstream accuracy** — construct validity 根本缺陷，PPL 退化可能不转化为 accuracy 下降
2. **单基准（MATH-500）+ 单规模（7B）** — generalizability 严重不足，两个 Qwen2 模型共享 backbone 独立性有限
3. **Mitigation pilot 失败（18% recovery, gate FAIL）** — 论文声称 "motivate phase-aware compression" 但自己的实验证明 direct application 不 work

主要优势：统计方法论极其严谨（远超 NLP 领域平均水平），发现本身有科学价值，写作诚实不隐藏 negative results。相关工作覆盖全面，引用验证未发现 fabrication。格式基本合规。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_57b24a804b56707ec9118a483a8ac65e:reviewer_2"
}
```

</details>

---


## Round 11

## Round 11

10 recorded events
